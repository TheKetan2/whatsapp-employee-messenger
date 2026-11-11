#!/usr/bin/env node
import http from 'node:http';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { chromium } from 'playwright-core';

const PORT = Number(process.env.WA_BRIDGE_PORT || 4123);
const SESSION_DIR = path.resolve(process.cwd(), '.wa-session');

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const randomBetween = (min, max) => Math.floor(min + Math.random() * Math.max(0, max - min));

const cleanPhone = raw => {
  const digits = String(raw ?? '').replace(/\D/g, '');
  if (digits.length === 10) return digits;
  if (digits.length === 12 && digits.startsWith('91')) return digits.slice(2);
  if (digits.length > 10) return digits.slice(-10);
  return digits;
};

/**
 * Decode a base64 dataUrl ({ name, dataUrl }) into a temporary image file for upload.
 */
const materializeImage = image => {
  if (!image?.dataUrl) return null;
  const match = /^data:([^;]+);base64,(.+)$/.exec(image.dataUrl);
  if (!match) return null;
  const extFromMime = match[1].split('/')[1]?.replace(/[^a-z0-9]/gi, '') || 'png';
  const baseName = (image.name || `attachment.${extFromMime}`).replace(/[^a-zA-Z0-9._-]/g, '_');
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'wa-auto-'));
  const filePath = path.join(tmpDir, baseName);
  fs.writeFileSync(filePath, Buffer.from(match[2], 'base64'));
  return { filePath, tmpDir };
};

const cleanupTempImage = temp => {
  if (!temp) return;
  try {
    fs.rmSync(temp.tmpDir, { recursive: true, force: true });
  } catch {
    // ignore temp cleanup errors
  }
};

let sharedContext = null;
let sharedPage = null;

async function getWhatsAppPage() {
  if (sharedContext && sharedPage && !sharedPage.isClosed()) {
    return sharedPage;
  }

  fs.mkdirSync(SESSION_DIR, { recursive: true });
  let context = null;
  let lastErr = null;

  for (const channel of ['chrome', 'msedge', undefined]) {
    try {
      context = await chromium.launchPersistentContext(SESSION_DIR, {
        headless: false,
        ...(channel ? { channel } : {}),
        viewport: { width: 1280, height: 860 },
        args: ['--disable-notifications']
      });
      break;
    } catch (err) {
      lastErr = err;
    }
  }

  if (!context) {
    throw new Error(`Could not launch Chrome or Edge via Playwright: ${lastErr?.message || lastErr}`);
  }

  sharedContext = context;
  sharedContext.on('close', () => {
    sharedContext = null;
    sharedPage = null;
  });

  const existingPages = context.pages();
  const page = existingPages[0] || (await context.newPage());
  sharedPage = page;

  if (!page.url().startsWith('https://web.whatsapp.com')) {
    await page.goto('https://web.whatsapp.com', { waitUntil: 'domcontentloaded' });
  }
  return page;
}

async function ensureLoggedIn(page, onState) {
  const readySelector = '#pane-side, div[aria-label="Chat list"], [data-testid="chat-list"]';
  const isReady = await page
    .locator(readySelector)
    .first()
    .isVisible({ timeout: 4000 })
    .catch(() => false);
  if (isReady) return;

  onState?.('qr_pending');
  console.log('Waiting for WhatsApp Web QR scan (or chat list load)...');
  await page.locator(readySelector).first().waitFor({ state: 'visible', timeout: 180000 });
  onState?.('ready');
}

async function clickSendButton(page) {
  const sendSelectors = [
    'div[role="button"][aria-label="Send"]',
    'button[aria-label="Send"]',
    'span[data-icon="send"]',
    'span[data-icon="wds-ic-send-filled"]'
  ];
  for (const sel of sendSelectors) {
    const loc = page.locator(sel).last();
    if (await loc.isVisible({ timeout: 1200 }).catch(() => false)) {
      await loc.click();
      return true;
    }
  }
  return false;
}

async function sendToRecipient(page, recipient, message, imagePath) {
  const phone = cleanPhone(recipient.phone);
  if (phone.length !== 10) {
    return { status: 'failed', error: 'Invalid 10-digit phone number' };
  }

  const targetUrl = `https://web.whatsapp.com/send?phone=91${phone}&text=${encodeURIComponent(
    message || ''
  )}`;
  await page.goto(targetUrl, { waitUntil: 'domcontentloaded' });

  const composeLocator = page
    .locator('footer div[contenteditable="true"], div[aria-label^="Type a message"]')
    .first();
  const invalidLocator = page
    .locator('div[data-animate-modal-popup="true"]')
    .filter({ hasText: /invalid|not on whatsapp/i })
    .first();

  const outcome = await Promise.race([
    composeLocator
      .waitFor({ state: 'visible', timeout: 30000 })
      .then(() => 'ready')
      .catch(() => 'timeout'),
    invalidLocator
      .waitFor({ state: 'visible', timeout: 30000 })
      .then(() => 'invalid')
      .catch(() => 'timeout')
  ]);

  if (outcome === 'invalid') {
    const okBtn = invalidLocator.locator('button').first();
    await okBtn.click().catch(() => {});
    return { status: 'failed', error: 'Phone number not registered on WhatsApp' };
  }

  if (outcome !== 'ready') {
    return { status: 'failed', error: 'Timed out waiting for chat compose box' };
  }

  await sleep(700);

  if (imagePath) {
    // Open Attach menu so WhatsApp mounts the image file input if not already in DOM
    const attachSelectors = [
      'button[title="Attach"]',
      'button[aria-label="Attach"]',
      'div[title="Attach"]',
      'span[data-icon="plus"]',
      'span[data-icon="plus-rounded"]',
      'span[data-icon="clip"]'
    ];
    let attached = false;

    const directImageInput = page
      .locator('input[type="file"][accept*="image"]')
      .first();

    if ((await directImageInput.count().catch(() => 0)) === 0) {
      for (const sel of attachSelectors) {
        const btn = page.locator(sel).first();
        if (await btn.isVisible({ timeout: 800 }).catch(() => false)) {
          await btn.click();
          await sleep(400);
          break;
        }
      }
    }

    const imageInput = page.locator('input[type="file"][accept*="image"]').first();
    if ((await imageInput.count().catch(() => 0)) > 0) {
      await imageInput.setInputFiles(imagePath);
      attached = true;
    } else {
      // Fallback: filechooser when clicking "Photos & videos" menu item
      const mediaOption = page
        .locator('li, button, [role="menuitem"]')
        .filter({ hasText: /photos|videos|images/i })
        .first();
      if (await mediaOption.isVisible({ timeout: 2000 }).catch(() => false)) {
        const [chooser] = await Promise.all([
          page.waitForEvent('filechooser', { timeout: 5000 }),
          mediaOption.click()
        ]);
        await chooser.setFiles(imagePath);
        attached = true;
      }
    }

    if (!attached) {
      return { status: 'failed', error: 'Could not locate WhatsApp image upload input' };
    }

    // Wait for media preview modal & Send icon
    const mediaSend = page
      .locator('div[role="button"][aria-label="Send"], button[aria-label="Send"], span[data-icon="send"], span[data-icon="wds-ic-send-filled"]')
      .last();
    await mediaSend.waitFor({ state: 'visible', timeout: 15000 });
    await sleep(500);

    // Ensure caption text is populated if URL text didn't carry into the media caption box
    if (message && message.trim()) {
      const captionBox = page
        .locator('div[contenteditable="true"][aria-placeholder*="caption" i], div[contenteditable="true"][data-lexical-editor="true"]')
        .first();
      if (await captionBox.isVisible({ timeout: 800 }).catch(() => false)) {
        const existing = (await captionBox.innerText().catch(() => '')).trim();
        if (!existing) {
          await captionBox.click();
          await page.keyboard.insertText(message);
        }
      }
    }

    await mediaSend.click();
    await sleep(1600);
    return { status: 'sent' };
  }

  // Text-only path: compose box is prefilled from ?text=..., click Send or press Enter
  const clicked = await clickSendButton(page);
  if (!clicked) {
    await composeLocator.click();
    await page.keyboard.press('Enter');
  }
  await sleep(1200);
  return { status: 'sent' };
}

const jobState = {
  jobId: null,
  running: false,
  stopRequested: false,
  qrPending: false,
  total: 0,
  currentIndex: 0,
  currentRecipient: null,
  sent: 0,
  failed: 0,
  results: [],
  lastError: ''
};

async function runBatchJob(job) {
  const recipients = Array.isArray(job.recipients) ? job.recipients : [];
  const message = String(job.message ?? '');
  const minDelayMs = Math.max(3000, Number(job.minDelayMs) || 6000);
  const maxDelayMs = Math.max(minDelayMs, Number(job.maxDelayMs) || minDelayMs + 4000);

  jobState.jobId = job.jobId || `job-${Date.now()}`;
  jobState.running = true;
  jobState.stopRequested = false;
  jobState.qrPending = false;
  jobState.total = recipients.length;
  jobState.currentIndex = 0;
  jobState.currentRecipient = null;
  jobState.sent = 0;
  jobState.failed = 0;
  jobState.results = [];
  jobState.lastError = '';

  const tempImage = materializeImage(job.image);

  try {
    const page = await getWhatsAppPage();
    await ensureLoggedIn(page, s => {
      jobState.qrPending = s === 'qr_pending';
    });
    jobState.qrPending = false;

    for (let i = 0; i < recipients.length; i++) {
      if (jobState.stopRequested) break;
      const recipient = recipients[i];
      jobState.currentIndex = i + 1;
      jobState.currentRecipient = recipient;

      console.log(`[${i + 1}/${recipients.length}] Sending to ${recipient.name} (+91 ${recipient.phone})...`);
      let res;
      try {
        res = await sendToRecipient(page, recipient, message, tempImage?.filePath || null);
      } catch (err) {
        res = { status: 'failed', error: err?.message || String(err) };
      }

      const record = {
        employeeId: String(recipient.id ?? recipient.employeeId ?? ''),
        name: recipient.name,
        phone: cleanPhone(recipient.phone),
        taluka: recipient.taluka || '',
        designation: recipient.designation || '',
        gramPanchayat: recipient.gramPanchayat || '',
        status: res.status,
        error: res.error || '',
        sentAt: new Date().toISOString()
      };

      jobState.results.push(record);
      if (res.status === 'sent') {
        jobState.sent++;
        console.log(`  ✓ Sent to ${recipient.name}`);
      } else {
        jobState.failed++;
        console.log(`  ✕ Failed (${recipient.name}): ${record.error}`);
      }

      if (i < recipients.length - 1 && !jobState.stopRequested) {
        const waitMs = randomBetween(minDelayMs, maxDelayMs);
        console.log(`  Waiting ${(waitMs / 1000).toFixed(1)}s before next recipient...`);
        await sleep(waitMs);
      }
    }
  } catch (err) {
    jobState.lastError = err?.message || String(err);
    console.error('Auto-sender error:', jobState.lastError);
  } finally {
    cleanupTempImage(tempImage);
    jobState.running = false;
    jobState.currentRecipient = null;
  }

  return jobState.results;
}

function sendJson(res, status, data) {
  res.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Private-Network': 'true'
  });
  res.end(JSON.stringify(data));
}

function startBridgeServer() {
  const server = http.createServer(async (req, res) => {
    if (req.method === 'OPTIONS') {
      sendJson(res, 204, {});
      return;
    }

    if (req.method === 'GET' && req.url === '/health') {
      sendJson(res, 200, {
        ok: true,
        ...jobState
      });
      return;
    }

    if (req.method === 'POST' && req.url === '/stop') {
      jobState.stopRequested = true;
      sendJson(res, 200, { ok: true, message: 'Stopping after current recipient.' });
      return;
    }

    if (req.method === 'POST' && req.url === '/start') {
      if (jobState.running) {
        sendJson(res, 409, { ok: false, error: 'A batch send job is already running.' });
        return;
      }

      const chunks = [];
      for await (const chunk of req) chunks.push(chunk);
      let body;
      try {
        body = JSON.parse(Buffer.concat(chunks).toString('utf8'));
      } catch {
        sendJson(res, 400, { ok: false, error: 'Invalid JSON payload.' });
        return;
      }

      if (!Array.isArray(body?.recipients) || body.recipients.length === 0) {
        sendJson(res, 400, { ok: false, error: 'At least one recipient is required.' });
        return;
      }

      const jobId = `job-${Date.now()}`;
      body.jobId = jobId;
      void runBatchJob(body);
      sendJson(res, 202, { ok: true, jobId, total: body.recipients.length });
      return;
    }

    sendJson(res, 404, { ok: false, error: 'Not found' });
  });

  server.listen(PORT, '127.0.0.1', () => {
    console.log(`\nWhatsApp PC Auto-Sender Bridge running on http://127.0.0.1:${PORT}`);
    console.log(`Keep this terminal open while triggering Auto-Send from the web app.\n`);
  });
}

async function runCli() {
  const args = process.argv.slice(2);
  if (args.includes('--server')) {
    startBridgeServer();
    return;
  }

  const jobIdx = args.indexOf('--job');
  const jobPath = jobIdx >= 0 ? args[jobIdx + 1] : args.find(a => a.endsWith('.json'));
  if (!jobPath) {
    console.log('Usage:');
    console.log('  npm run auto-bridge                          # Start local UI bridge on port 4123');
    console.log('  npm run auto-send -- --job wa-send-job.json  # Run exported job JSON file');
    process.exit(1);
  }

  const resolvedJobPath = path.resolve(process.cwd(), jobPath);
  const job = JSON.parse(fs.readFileSync(resolvedJobPath, 'utf8'));
  const results = await runBatchJob(job);

  const outPath = path.join(path.dirname(resolvedJobPath), 'wa-send-results.json');
  fs.writeFileSync(outPath, JSON.stringify(results, null, 2) + '\n', 'utf8');
  console.log(`\nFinished! Saved ${results.length} results to ${outPath}`);
  if (sharedContext) {
    await sharedContext.close().catch(() => {});
  }
}

runCli().catch(err => {
  console.error(err);
  process.exit(1);
});


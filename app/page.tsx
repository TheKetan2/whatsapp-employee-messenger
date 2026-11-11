'use client';
import { useEffect, useMemo, useRef, useState } from 'react';
import seedEmployees from '../public/employees.json';
import * as XLSX from 'xlsx';
import { PwaInstall } from '../components/PwaInstall';

export type Employee = {
  id: number | string;
  name: string;
  designation: string;
  taluka: string;
  district?: string;
  gramPanchayat?: string;
  address?: string;
  pinCode?: string;
  phone: string;
  email?: string;
  sewarthId?: string;
  grade?: string;
  remarks?: string;
};

export type MessageHistoryEntry = {
  id: string;
  employeeId: string;
  name: string;
  phone: string;
  taluka: string;
  designation: string;
  gramPanchayat?: string;
  message: string;
  hasImage: boolean;
  imageName?: string;
  sentAt: string;
  mode: 'queue' | 'direct';
};

const cleanPhone = (v: unknown) =>
  String(v ?? '')
    .replace(/\D/g, '')
    .replace(/^91(?=\d{10}$)/, '');

const splitTags = (v?: string) =>
  String(v ?? '')
    .split(',')
    .map(x => x.trim())
    .filter(Boolean);

const mergeCsvField = (a?: string, b?: string) => {
  const items = splitTags(a);
  const seen = new Set(items.map(x => x.toLowerCase()));
  for (const part of splitTags(b)) {
    if (!seen.has(part.toLowerCase())) {
      seen.add(part.toLowerCase());
      items.push(part);
    }
  }
  return items.join(', ');
};

const normName = (n: string) =>
  n
    .replace(/^(Shri\.|Shri|Smt\.|Smt|Ku\.|Ku|Shir\.)\s*/i, '')
    .toLowerCase()
    .replace(/[^a-z0-9\u0900-\u097f]/g, '');

const deduplicateAndMerge = (
  base: Employee[],
  incoming: Employee[],
  mergeWithBase: boolean
): { list: Employee[]; added: number; duplicates: number } => {
  const result: Employee[] = mergeWithBase ? base.map(e => ({ ...e })) : [];
  const byPhone = new Map<string, Employee>();
  const bySewarth = new Map<string, Employee>();
  const byTalukaName = new Map<string, Employee>();

  const indexEmployee = (emp: Employee) => {
    const p = cleanPhone(emp.phone);
    if (p.length === 10) byPhone.set(p, emp);
    const sw = (emp.sewarthId ?? '').trim().toUpperCase();
    if (sw && /^[0-9A-Z]+$/.test(sw)) bySewarth.set(sw, emp);
    const nk = normName(emp.name);
    if (nk) {
      for (const t of splitTags(emp.taluka)) {
        byTalukaName.set(`${t.toLowerCase()}::${nk}`, emp);
      }
    }
  };

  for (const emp of result) indexEmployee(emp);

  let added = 0;
  let duplicates = 0;
  let nextId = result.reduce((m, e) => Math.max(m, Number(e.id) || 0), 0) + 1;

  for (const raw of incoming) {
    const phone = cleanPhone(raw.phone);
    const sewarth = (raw.sewarthId ?? '').trim().toUpperCase();
    const nk = normName(raw.name);
    const talukas = splitTags(raw.taluka);

    let match: Employee | undefined;
    if (phone.length === 10) match = byPhone.get(phone);
    if (!match && sewarth && /^[0-9A-Z]+$/.test(sewarth)) match = bySewarth.get(sewarth);
    if (!match && nk) {
      for (const t of talukas.length ? talukas : ['General']) {
        match = byTalukaName.get(`${t.toLowerCase()}::${nk}`);
        if (match) break;
      }
    }

    if (match) {
      duplicates++;
      match.gramPanchayat = mergeCsvField(match.gramPanchayat, raw.gramPanchayat);
      match.taluka = mergeCsvField(match.taluka, raw.taluka) || match.taluka;
      match.district = mergeCsvField(match.district, raw.district) || match.district;
      if (!match.phone && phone.length === 10) {
        match.phone = phone;
        byPhone.set(phone, match);
      }
      if (!match.email && raw.email) match.email = raw.email;
      if (!match.address && raw.address) match.address = raw.address;
      if (!match.pinCode && raw.pinCode) match.pinCode = raw.pinCode;
      if (!match.sewarthId && sewarth) {
        match.sewarthId = sewarth;
        if (/^[0-9A-Z]+$/.test(sewarth)) bySewarth.set(sewarth, match);
      }
      if (!match.remarks && raw.remarks) match.remarks = raw.remarks;
      if (raw.name.length > match.name.length) match.name = raw.name;
      indexEmployee(match);
    } else {
      const created: Employee = {
        ...raw,
        id: nextId++,
        phone: phone.length === 10 ? phone : '',
        sewarthId: sewarth
      };
      result.push(created);
      indexEmployee(created);
      added++;
    }
  }

  return { list: result, added, duplicates };
};

const STORAGE_KEY = 'wa-employee-list-v5';
const HISTORY_STORAGE_KEY = 'wa-message-history-v1';
const PAGE_SIZE = 100;

const TALUKA_OCR_FIXES: Record<string, string> = {
  angameshwar: 'Sangameshwar',
  'avathemahan kal': 'Kavathe Mahankal',
  ahabaleshwar: 'Mahabaleshwar'
};

const normalizeTalukaName = (raw: unknown) => {
  const trimmed = String(raw ?? '').trim().replace(/\s+/g, ' ');
  return TALUKA_OCR_FIXES[trimmed.toLowerCase()] || trimmed;
};

const formatTimestamp = (iso: string) => {
  try {
    return new Date(iso).toLocaleString('en-IN', {
      day: '2-digit',
      month: 'short',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  } catch {
    return iso;
  }
};

export default function Home() {
  const [employees, setEmployees] = useState<Employee[]>(seedEmployees as Employee[]);
  const [selected, setSelected] = useState<string[]>([]);
  const [query, setQuery] = useState('');
  const [selectedDistrict, setSelectedDistrict] = useState('All');
  const [selectedTaluka, setSelectedTaluka] = useState('All');
  const [selectedDesignation, setSelectedDesignation] = useState('All');
  const [selectedGrade, setSelectedGrade] = useState('All');
  const [sentFilter, setSentFilter] = useState<'All' | 'Not Sent' | 'Sent'>('All');
  const [mergeOnImport, setMergeOnImport] = useState(true);
  const [visibleCount, setVisibleCount] = useState(PAGE_SIZE);

  const [message, setMessage] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState('');

  const [queue, setQueue] = useState<string[]>([]);
  const [current, setCurrent] = useState(0);
  const [sent, setSent] = useState<string[]>([]);
  const [skipped, setSkipped] = useState<string[]>([]);
  const [history, setHistory] = useState<MessageHistoryEntry[]>([]);
  const [historyQuery, setHistoryQuery] = useState('');
  const [notice, setNotice] = useState('');
  const fileRef = useRef<HTMLInputElement>(null);

  // Restore or initialize employees & history from local storage
  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed) && parsed.length > 50 && parsed[0]?.taluka) {
          setEmployees(parsed);
        }
      }
    } catch {
      setEmployees(seedEmployees as Employee[]);
    }

    try {
      const savedHistory = localStorage.getItem(HISTORY_STORAGE_KEY);
      if (savedHistory) {
        const parsedHistory = JSON.parse(savedHistory);
        if (Array.isArray(parsedHistory)) {
          setHistory(parsedHistory);
        }
      }
    } catch {
      setHistory([]);
    }
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(employees));
    } catch {
      // quota or private mode fallback
    }
  }, [employees]);

  useEffect(() => {
    try {
      localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(history));
    } catch {
      // quota or private mode fallback
    }
  }, [history]);

  useEffect(() => {
    if (!file) {
      setPreview('');
      return;
    }
    const u = URL.createObjectURL(file);
    setPreview(u);
    return () => URL.revokeObjectURL(u);
  }, [file]);

  // Lookup map of sent history per contact (keyed by phone and employeeId)
  const sentStats = useMemo(() => {
    const byKey = new Map<string, { count: number; lastEntry: MessageHistoryEntry }>();
    for (const h of history) {
      const keys = [h.phone, `id:${h.employeeId}`].filter(Boolean);
      for (const k of keys) {
        const prev = byKey.get(k);
        if (!prev) {
          byKey.set(k, { count: 1, lastEntry: h });
        } else {
          prev.count += 1;
          if (h.sentAt > prev.lastEntry.sentAt) {
            prev.lastEntry = h;
          }
        }
      }
    }
    return byKey;
  }, [history]);

  const getContactHistory = (e: Employee) =>
    (e.phone ? sentStats.get(e.phone) : undefined) || sentStats.get(`id:${String(e.id)}`);

  const uniqueContactsReached = useMemo(() => {
    let count = 0;
    for (const e of employees) {
      if (getContactHistory(e)) count++;
    }
    return count;
  }, [employees, sentStats]);

  // Dynamic filter lists with counts
  const districts = useMemo(() => {
    const set = new Set<string>();
    for (const e of employees) {
      for (const d of splitTags(e.district)) set.add(d);
    }
    const list = Array.from(set).sort((a, b) => a.localeCompare(b));
    return ['All', ...list];
  }, [employees]);

  const talukas = useMemo(() => {
    const set = new Set<string>();
    for (const e of employees) {
      if (selectedDistrict !== 'All' && !splitTags(e.district).includes(selectedDistrict)) {
        continue;
      }
      for (const t of splitTags(e.taluka)) set.add(t);
    }
    const list = Array.from(set);
    list.sort((a, b) => {
      if (a.includes('जिल्हा')) return 1;
      if (b.includes('जिल्हा')) return -1;
      return a.localeCompare(b);
    });
    return ['All', ...list];
  }, [employees, selectedDistrict]);

  useEffect(() => {
    if (selectedTaluka !== 'All' && !talukas.includes(selectedTaluka)) {
      setSelectedTaluka('All');
    }
  }, [talukas, selectedTaluka]);

  useEffect(() => {
    setVisibleCount(PAGE_SIZE);
  }, [selectedDistrict, selectedTaluka, selectedDesignation, selectedGrade, sentFilter, query]);

  const designations = useMemo(() => {
    const list = Array.from(new Set(employees.map(e => e.designation).filter(Boolean)));
    list.sort((a, b) => {
      // Put Gram Sewak designations first
      if (a.includes('Gram Sewak') && !b.includes('Gram Sewak')) return -1;
      if (!a.includes('Gram Sewak') && b.includes('Gram Sewak')) return 1;
      return a.localeCompare(b);
    });
    return ['All', ...list];
  }, [employees]);

  const grades = useMemo(
    () => ['All', ...Array.from(new Set(employees.map(e => e.grade).filter(Boolean)))],
    [employees]
  );

  // Filtering logic
  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return employees.filter(e => {
      if (selectedDistrict !== 'All' && !splitTags(e.district).includes(selectedDistrict)) return false;
      if (selectedTaluka !== 'All' && !splitTags(e.taluka).includes(selectedTaluka)) return false;
      if (selectedDesignation !== 'All' && e.designation !== selectedDesignation) return false;
      if (selectedGrade !== 'All' && e.grade !== selectedGrade) return false;
      const contactHist = getContactHistory(e);
      if (sentFilter === 'Sent' && !contactHist) return false;
      if (sentFilter === 'Not Sent' && contactHist) return false;
      if (!q) return true;

      const haystack = `${e.name} ${e.district ?? ''} ${e.taluka} ${e.gramPanchayat ?? ''} ${e.address ?? ''} ${e.pinCode ?? ''} ${e.designation} ${e.phone} ${e.email ?? ''} ${e.sewarthId ?? ''}`.toLowerCase();
      return haystack.includes(q);
    });
  }, [employees, selectedDistrict, selectedTaluka, selectedDesignation, selectedGrade, sentFilter, query, sentStats]);

  const visibleEmployees = useMemo(
    () => filtered.slice(0, visibleCount),
    [filtered, visibleCount]
  );

  const filteredHistory = useMemo(() => {
    const q = historyQuery.trim().toLowerCase();
    if (!q) return history;
    return history.filter(h =>
      `${h.name} ${h.phone} ${h.taluka} ${h.designation} ${h.gramPanchayat ?? ''} ${h.message}`.toLowerCase().includes(q)
    );
  }, [history, historyQuery]);

  const allFiltered =
    filtered.length > 0 && filtered.every(e => selected.includes(String(e.id)));

  const toggle = (id: string) =>
    setSelected(s => (s.includes(id) ? s.filter(x => x !== id) : [...s, id]));

  const toggleAll = () =>
    setSelected(s =>
      allFiltered
        ? s.filter(id => !filtered.some(e => String(e.id) === id))
        : Array.from(new Set([...s, ...filtered.map(e => String(e.id))]))
    );

  const clearFilters = () => {
    setSelectedDistrict('All');
    setSelectedTaluka('All');
    setSelectedDesignation('All');
    setSelectedGrade('All');
    setSentFilter('All');
    setQuery('');
  };

  const importExcel = async (f: File) => {
    try {
      const data = await f.arrayBuffer();
      const wb = XLSX.read(data, { type: 'array' });
      const parsed: Employee[] = [];

      for (const sheetName of wb.SheetNames) {
        const sheet = wb.Sheets[sheetName];
        const rows = XLSX.utils.sheet_to_json<any[]>(sheet, { header: 1, defval: '' });
        if (!rows.length) continue;

        let headerIdx = -1;
        for (let i = 0; i < Math.min(10, rows.length); i++) {
          const rowStr = rows[i].map(v => String(v).toLowerCase()).join(' ');
          if (
            rowStr.includes('name') ||
            rowStr.includes('नाव') ||
            rowStr.includes('नांव') ||
            rowStr.includes('padnam') ||
            rowStr.includes('designation') ||
            rowStr.includes('block') ||
            rowStr.includes('taluka')
          ) {
            headerIdx = i;
            break;
          }
        }
        if (headerIdx < 0) headerIdx = 0;

        const headerRow = rows[headerIdx].map(v => String(v).toLowerCase().trim());
        const findCol = (keywords: string[]) =>
          headerRow.findIndex(h => keywords.some(k => h.includes(k)));

        const talukaCol = findCol(['block', 'taluka', 'तालुका']);
        const districtCol = findCol(['district', 'जिल्हा']);
        const gpCol = findCol(['gram panchayat', 'gp', 'ग्रामपंचायत', 'panchayat']);
        const addressCol = findCol(['address']);
        const pinCol = findCol(['pin']);
        const nameCol = findCol(['full name', 'auditor name', 'name', 'नाव', 'नांव', 'sewak']);
        const desigCol = findCol(['auditor type', 'designation', 'पदनाम', 'post']);
        const phoneCol = findCol(['mobile', 'phone', 'दूरध्वनी', 'contact']);
        const emailCol = findCol(['email', 'ईमेल']);
        const sewarthCol = findCol(['sewarth', 'empanelment', 'सेवा']);
        const gradeCol = findCol(['auditor grade', 'grade', 'class', 'वर्ग']);

        for (let i = headerIdx + 1; i < rows.length; i++) {
          const r = rows[i];
          if (!r || !r.some((v: any) => String(v).trim())) continue;

          let name = '';
          let phone = '';
          let taluka = '';
          let district = '';
          let gp = '';
          let address = '';
          let pinCode = '';
          let designation = '';
          let grade = 'वर्ग 3';
          let email = '';
          let sewarthId = '';

          if (nameCol >= 0 && r[nameCol]) name = String(r[nameCol]).trim().replace(/\s+/g, ' ');
          if (phoneCol >= 0 && r[phoneCol]) phone = cleanPhone(r[phoneCol]);
          if (talukaCol >= 0 && r[talukaCol]) taluka = normalizeTalukaName(r[talukaCol]);
          if (districtCol >= 0 && r[districtCol]) district = String(r[districtCol]).trim().replace(/\s+/g, ' ');
          if (gpCol >= 0 && r[gpCol]) gp = String(r[gpCol]).trim();
          if (addressCol >= 0 && r[addressCol]) address = String(r[addressCol]).trim().replace(/\s+/g, ' ');
          if (pinCol >= 0 && r[pinCol]) pinCode = String(r[pinCol]).trim();
          if (desigCol >= 0 && r[desigCol]) designation = String(r[desigCol]).trim().replace(/\s+/g, ' ');
          if (gradeCol >= 0 && r[gradeCol]) grade = String(r[gradeCol]).trim().replace(/\s+/g, ' ');
          if (emailCol >= 0 && r[emailCol]) email = String(r[emailCol]).trim();
          if (sewarthCol >= 0 && r[sewarthCol]) sewarthId = String(r[sewarthCol]).trim();

          // Positional fallback for legacy 4-column files: [sr, desig, name, grade, phone]
          if (!name && r.length >= 4 && nameCol < 0) {
            designation = String(r[1] ?? '').trim();
            name = String(r[2] ?? '').trim();
            grade = String(r[3] ?? '').trim();
            phone = cleanPhone(r[4]);
          }

          if (!designation) {
            const rawJoined = `${sewarthId} ${r.join(' ')}`.toLowerCase();
            if (
              rawJoined.includes('कंत्राटी') ||
              rawJoined.includes('kantrati') ||
              rawJoined.includes('kantranti')
            ) {
              designation = 'कंत्राटी ग्रामसेवक (Contract Gram Sewak)';
            } else {
              designation = 'ग्रामसेवक (Gram Sewak)';
            }
          }

          if (name && name !== 'रिक्त' && phone.length === 10) {
            parsed.push({
              id: parsed.length + 1,
              name,
              designation,
              taluka: taluka || (wb.SheetNames.length > 1 ? sheetName.trim() : 'General'),
              district,
              gramPanchayat: gp,
              address,
              pinCode,
              phone,
              email,
              sewarthId,
              grade: grade || 'वर्ग 3'
            });
          }
        }
      }

      if (!parsed.length) {
        setNotice('No valid employee rows found. Please verify column headers and 10-digit mobile numbers.');
        return;
      }

      const { list, added, duplicates } = deduplicateAndMerge(employees, parsed, mergeOnImport);
      setEmployees(list);
      if (!mergeOnImport) setSelected([]);

      if (mergeOnImport) {
        setNotice(
          `Imported ${added} new contact${added === 1 ? '' : 's'}. ${duplicates} duplicate entr${duplicates === 1 ? 'y' : 'ies'} merged/skipped.`
        );
      } else {
        setNotice(
          `Directory replaced with ${added} unique contacts (${duplicates} duplicate rows inside file merged/skipped).`
        );
      }
    } catch {
      setNotice('Could not read this file. Please upload an .xlsx, .xls or .csv file.');
    }
  };

  const start = () => {
    const targets = employees.filter(
      e => selected.includes(String(e.id)) && e.phone && e.phone.length === 10
    );
    if (!targets.length) {
      setNotice('Select at least one employee with a valid 10-digit mobile number.');
      return;
    }
    if (!message.trim() && !file) {
      setNotice('Add message text or an image before starting.');
      return;
    }
    setQueue(targets.map(e => String(e.id)));
    setCurrent(0);
    setSent([]);
    setSkipped([]);
    setNotice(
      `Queue prepared with ${targets.length} recipients. Each recipient opens individually in WhatsApp.`
    );
  };

  const person = employees.find(e => String(e.id) === queue[current]);

  const whatsappWebUrl = (e: Employee) =>
    `https://wa.me/91${cleanPhone(e.phone)}?text=${encodeURIComponent(message)}`;

  const whatsappNativeUrl = (e: Employee) =>
    `whatsapp://send?phone=91${cleanPhone(e.phone)}&text=${encodeURIComponent(message)}`;

  const launchWhatsAppChat = (e: Employee) => {
    const phone = cleanPhone(e.phone);
    if (phone.length !== 10) return;
    const isMobile =
      typeof navigator !== 'undefined' && /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
    if (isMobile) {
      window.location.href = whatsappNativeUrl(e);
    } else {
      window.open(whatsappWebUrl(e), '_blank', 'noopener,noreferrer');
    }
  };

  const openTextChat = () => {
    if (!person || !person.phone) return;
    launchWhatsAppChat(person);
  };

  const copyImageToClipboard = async (imgFile: File): Promise<boolean> => {
    if (typeof ClipboardItem === 'undefined' || !navigator.clipboard?.write) return false;
    try {
      const bitmap = await createImageBitmap(imgFile);
      const canvas = document.createElement('canvas');
      canvas.width = bitmap.width;
      canvas.height = bitmap.height;
      const ctx = canvas.getContext('2d');
      if (!ctx) return false;
      ctx.drawImage(bitmap, 0, 0);
      const pngBlob = await new Promise<Blob | null>(resolve =>
        canvas.toBlob(resolve, 'image/png')
      );
      if (!pngBlob) return false;
      await navigator.clipboard.write([new ClipboardItem({ 'image/png': pngBlob })]);
      return true;
    } catch {
      return false;
    }
  };

  const copyImageAndOpenChat = async () => {
    if (!person || !person.phone) return;
    if (file) {
      const copied = await copyImageToClipboard(file);
      if (copied) {
        setNotice(
          `Image copied to clipboard! Opening ${person.name}'s WhatsApp chat — paste the image there and tap Send.`
        );
      } else {
        setNotice(
          `Opening ${person.name}'s WhatsApp chat directly. Attach "${file.name}" inside WhatsApp if clipboard paste is unavailable on your device.`
        );
      }
    }
    launchWhatsAppChat(person);
  };

  const recordSent = (emp: Employee, mode: 'queue' | 'direct') => {
    const entry: MessageHistoryEntry = {
      id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
      employeeId: String(emp.id),
      name: emp.name,
      phone: emp.phone,
      taluka: emp.taluka,
      designation: emp.designation,
      gramPanchayat: emp.gramPanchayat,
      message: message.trim() || (file ? `[Image: ${file.name}]` : ''),
      hasImage: Boolean(file),
      imageName: file?.name,
      sentAt: new Date().toISOString(),
      mode
    };
    setHistory(prev => [entry, ...prev]);
  };

  const openSingleChat = (e: Employee, ev: React.MouseEvent) => {
    ev.stopPropagation();
    if (!e.phone) {
      setNotice(`${e.name} does not have a phone number listed.`);
      return;
    }
    launchWhatsAppChat(e);
    if (message.trim() || file) {
      recordSent(e, 'direct');
      setNotice(`Opened WhatsApp chat for ${e.name} and logged in Message History.`);
    }
  };

  const markManualSent = (e: Employee, ev: React.MouseEvent) => {
    ev.stopPropagation();
    recordSent(e, 'direct');
    setNotice(`Marked ${e.name} as sent in Message History.`);
  };

  const shareImage = async () => {
    if (!person || !file) return;
    const nav = navigator as Navigator & { canShare?: (data: ShareData) => boolean };
    try {
      const data: ShareData = { files: [file], text: message };
      if (!nav.share || !nav.canShare?.({ files: [file] })) {
        setNotice(
          'Image sharing is not supported in this browser. Try Chrome on Android, or use WhatsApp Web and attach the image manually.'
        );
        return;
      }
      await nav.share(data);
      setNotice('Share sheet opened. Choose WhatsApp and click Mark sent & Next when done.');
    } catch (e: any) {
      if (e?.name !== 'AbortError') {
        setNotice(
          'Sharing was cancelled or unavailable. You can still open the WhatsApp chat and attach the image manually.'
        );
      }
    }
  };

  const next = (wasSent: boolean) => {
    if (!person) return;
    if (wasSent) {
      setSent(s => [...s, person.id.toString()]);
      recordSent(person, 'queue');
    } else {
      setSkipped(s => [...s, person.id.toString()]);
    }

    if (current + 1 >= queue.length) {
      setCurrent(queue.length);
      setNotice('Queue completed. Check sent and skipped counts below.');
    } else {
      setCurrent(c => c + 1);
    }
  };

  const stop = () => {
    setQueue([]);
    setCurrent(0);
    setNotice('Sending queue stopped.');
  };

  const removeHistoryEntry = (id: string) => {
    setHistory(prev => prev.filter(h => h.id !== id));
  };

  const clearHistory = () => {
    if (confirm('Clear all saved message history? This cannot be undone.')) {
      setHistory([]);
      localStorage.removeItem(HISTORY_STORAGE_KEY);
      setNotice('Message history cleared.');
    }
  };

  const exportHistoryExcel = () => {
    if (!history.length) {
      setNotice('No message history to export yet.');
      return;
    }
    const rows = history.map((h, i) => ({
      'Sr. No.': i + 1,
      'Sent At': formatTimestamp(h.sentAt),
      Name: h.name,
      Phone: h.phone,
      Taluka: h.taluka,
      Designation: h.designation,
      'Gram Panchayat': h.gramPanchayat ?? '',
      Message: h.message,
      'Image Attached': h.imageName ?? '',
      Mode: h.mode === 'queue' ? 'Queue' : 'Direct'
    }));
    const ws = XLSX.utils.json_to_sheet(rows);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Message History');
    XLSX.writeFile(wb, `whatsapp-message-history-${new Date().toISOString().slice(0, 10)}.xlsx`);
    setNotice(`Exported ${history.length} history records to Excel.`);
  };

  const resetList = () => {
    if (
      confirm(
        `Restore the comprehensive directory (${seedEmployees.length} unique contacts categorized across all 15 Talukas and District HQ)?`
      )
    ) {
      setEmployees(seedEmployees as Employee[]);
      setSelected([]);
      clearFilters();
      localStorage.removeItem(STORAGE_KEY);
      setNotice('Directory restored with all 15 Talukas and District contacts.');
    }
  };

  // Quick select helper: select all currently in this taluka
  const selectAllInTaluka = (talukaName: string) => {
    const idsInTaluka = employees
      .filter(e => (talukaName === 'All' ? true : splitTags(e.taluka).includes(talukaName)))
      .map(e => String(e.id));
    setSelected(s => Array.from(new Set([...s, ...idsInTaluka])));
    setNotice(`Selected all employees in ${talukaName}.`);
  };

  const deselectAlreadySent = () => {
    setSelected(prev =>
      prev.filter(id => {
        const emp = employees.find(e => String(e.id) === id);
        return emp ? !getContactHistory(emp) : true;
      })
    );
    setNotice('Removed already-messaged contacts from current selection.');
  };

  return (
    <main className="shell">
      <header className="topbar">
        <div className="brand">
          <div className="logo">WA</div>
          <div>
            <h1>WhatsApp Employee Messenger</h1>
            <p>Zilla Parishad & Taluka Directory · Chandrapur</p>
          </div>
        </div>
        <div className="topbarRight">
          <PwaInstall variant="button" />
          <span className="localTag">● {employees.length} Contacts Available</span>
        </div>
      </header>

      <PwaInstall variant="banner" />

      <section className="intro">
        <div>
          <p className="eyebrow">DISTRICT & TALUKA COMMUNICATION</p>
          <h2>
            Chandrapur Gram Sewak & Staff Messenger.
            <br />
            <em>Filtered by Taluka & Designation.</em>
          </h2>
          <p className="sub">
            Seamlessly categorize by 15 Talukas (Chandrapur, Warora, Bhadrawati, Chimur, Mul,
            Sawali, Nagbhid, Sindewahi, Bramhapuri, Ballarpur, Rajura, GondPipari, Pombhurna,
            Korpana, Jiwati) and designations. Compose once, dispatch via WhatsApp queue.
          </p>
        </div>
        <div className="heroIcon">🏛️</div>
      </section>

      {notice && (
        <div className="notice" role="status">
          <span>{notice}</span>
          <button onClick={() => setNotice('')} aria-label="Dismiss">
            ×
          </button>
        </div>
      )}

      {/* Stats bar */}
      <div className="stats">
        <div>
          <strong>{employees.length}</strong>
          <span>Total Contacts</span>
        </div>
        <div>
          <strong style={{ color: 'var(--green)' }}>{uniqueContactsReached}</strong>
          <span>Contacts Reached</span>
        </div>
        <div>
          <strong>{Math.max(0, employees.length - uniqueContactsReached)}</strong>
          <span>Not Sent Yet</span>
        </div>
        <div>
          <strong>{selected.length}</strong>
          <span>Selected for Queue</span>
        </div>
      </div>

      {/* STEP 1: RECIPIENT SELECTION */}
      <section className="panel">
        <div className="sectionHead">
          <div>
            <span className="step">01</span>
            <div>
              <h3>Filter & Choose Recipients</h3>
              <p>Categorize by District, Taluka, Designation, Sent Status or search contacts.</p>
            </div>
          </div>
          <div className="headActions">
            {(selectedDistrict !== 'All' ||
              selectedTaluka !== 'All' ||
              selectedDesignation !== 'All' ||
              selectedGrade !== 'All' ||
              sentFilter !== 'All' ||
              query) && (
              <button className="textBtn" onClick={clearFilters}>
                ✕ Reset Filters
              </button>
            )}
            <button className="textBtn secondary" onClick={resetList}>
              ↺ Restore Original Directory
            </button>
          </div>
        </div>

        {/* Quick District Pills */}
        {districts.length > 2 && (
          <div className="talukaPillsContainer">
            <span className="pillsLabel">Quick District:</span>
            <div className="talukaPills">
              {districts.map(d => {
                const count =
                  d === 'All'
                    ? employees.length
                    : employees.filter(e => splitTags(e.district).includes(d)).length;
                const isSelected = selectedDistrict === d;
                return (
                  <button
                    key={d}
                    type="button"
                    className={`pillBtn ${isSelected ? 'active' : ''}`}
                    onClick={() => setSelectedDistrict(d)}
                  >
                    {d} <span className="pillCount">{count}</span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Quick Taluka Pills */}
        <div className="talukaPillsContainer">
          <span className="pillsLabel">Quick Taluka:</span>
          <div className="talukaPills">
            {talukas.map(t => {
              const scopedBase =
                selectedDistrict === 'All'
                  ? employees
                  : employees.filter(e => splitTags(e.district).includes(selectedDistrict));
              const count =
                t === 'All'
                  ? scopedBase.length
                  : scopedBase.filter(e => splitTags(e.taluka).includes(t)).length;
              const isSelected = selectedTaluka === t;
              return (
                <button
                  key={t}
                  type="button"
                  className={`pillBtn ${isSelected ? 'active' : ''}`}
                  onClick={() => setSelectedTaluka(t)}
                >
                  {t} <span className="pillCount">{count}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Filter Dropdowns Toolbar */}
        <div className="toolbarGrid">
          <div className="searchBox">
            <span className="searchIcon">🔍</span>
            <input
              className="search"
              placeholder="Search name, District, Taluka, GP/Address, phone, or ID…"
              value={query}
              onChange={e => setQuery(e.target.value)}
            />
            {query && (
              <button className="clearInputBtn" onClick={() => setQuery('')}>
                ×
              </button>
            )}
          </div>

          <div className="selectGroup fiveCols">
            {/* District Select */}
            <div className="selectWrapper">
              <label className="selectLabel">🗺️ District</label>
              <select
                value={selectedDistrict}
                onChange={e => setSelectedDistrict(e.target.value)}
                aria-label="Filter by District"
              >
                {districts.map(d => {
                  const cnt =
                    d === 'All'
                      ? employees.length
                      : employees.filter(e => splitTags(e.district).includes(d)).length;
                  return (
                    <option key={d} value={d}>
                      {d === 'All' ? 'All Districts' : d} ({cnt})
                    </option>
                  );
                })}
              </select>
            </div>

            {/* Taluka Select */}
            <div className="selectWrapper">
              <label className="selectLabel">📍 Taluka / Block</label>
              <select
                value={selectedTaluka}
                onChange={e => setSelectedTaluka(e.target.value)}
                aria-label="Filter by Taluka"
              >
                {talukas.map(t => {
                  const scopedBase =
                    selectedDistrict === 'All'
                      ? employees
                      : employees.filter(e => splitTags(e.district).includes(selectedDistrict));
                  const cnt =
                    t === 'All'
                      ? scopedBase.length
                      : scopedBase.filter(e => splitTags(e.taluka).includes(t)).length;
                  return (
                    <option key={t} value={t}>
                      {t === 'All' ? 'All Talukas' : t} ({cnt})
                    </option>
                  );
                })}
              </select>
            </div>

            {/* Designation Select */}
            <div className="selectWrapper">
              <label className="selectLabel">💼 Designation</label>
              <select
                value={selectedDesignation}
                onChange={e => setSelectedDesignation(e.target.value)}
                aria-label="Filter by Designation"
              >
                {designations.map(d => {
                  const cnt =
                    d === 'All'
                      ? employees.length
                      : employees.filter(e => e.designation === d).length;
                  return (
                    <option key={d} value={d}>
                      {d === 'All' ? 'All Designations' : d} ({cnt})
                    </option>
                  );
                })}
              </select>
            </div>

            {/* Grade Select */}
            <div className="selectWrapper">
              <label className="selectLabel">🏷️ Class / Grade</label>
              <select
                value={selectedGrade}
                onChange={e => setSelectedGrade(e.target.value)}
                aria-label="Filter by Class"
              >
                {grades.map(g => {
                  const cnt =
                    g === 'All' ? employees.length : employees.filter(e => e.grade === g).length;
                  return (
                    <option key={g} value={g}>
                      {g === 'All' ? 'All Classes' : g} ({cnt})
                    </option>
                  );
                })}
              </select>
            </div>

            {/* Sent Status Select */}
            <div className="selectWrapper">
              <label className="selectLabel">✅ Sent Status</label>
              <select
                value={sentFilter}
                onChange={e => setSentFilter(e.target.value as 'All' | 'Not Sent' | 'Sent')}
                aria-label="Filter by Sent Status"
              >
                <option value="All">All Contacts ({employees.length})</option>
                <option value="Not Sent">
                  Not Sent Yet ({Math.max(0, employees.length - uniqueContactsReached)})
                </option>
                <option value="Sent">Already Sent ({uniqueContactsReached})</option>
              </select>
            </div>
          </div>
        </div>

        {/* Selection Bar */}
        <div className="listActions">
          <div className="listActionsLeft">
            <label className="checkLabel">
              <input type="checkbox" checked={allFiltered} onChange={toggleAll} />
              <span>Select all in view ({filtered.length})</span>
            </label>
            {selectedTaluka !== 'All' && (
              <button
                type="button"
                className="actionLink"
                onClick={() => selectAllInTaluka(selectedTaluka)}
              >
                + Select all {selectedTaluka}
              </button>
            )}
          </div>
          <div className="listActionsRight">
            <span className="selectedCountBadge">
              <strong>{selected.length}</strong> selected
            </span>
            {selected.some(id => {
              const emp = employees.find(x => String(x.id) === id);
              return emp ? Boolean(getContactHistory(emp)) : false;
            }) && (
              <button type="button" className="actionLink" onClick={deselectAlreadySent}>
                Exclude already sent
              </button>
            )}
            {selected.length > 0 && (
              <button type="button" className="actionLink danger" onClick={() => setSelected([])}>
                Clear selection
              </button>
            )}
          </div>
        </div>

        {/* Employee List with Rich Metadata */}
        <div className="employeeList">
          {visibleEmployees.map(e => {
            const isChecked = selected.includes(String(e.id));
            const hasPhone = Boolean(e.phone && e.phone.length === 10);
            const contactHist = getContactHistory(e);
            return (
              <label className={`employee ${isChecked ? 'selected' : ''}`} key={e.id}>
                <input
                  type="checkbox"
                  checked={isChecked}
                  onChange={() => toggle(String(e.id))}
                />
                <span className="avatar">{e.name.charAt(0) || '👤'}</span>

                <div className="empInfo">
                  <div className="empHeadLine">
                    <b className="empName">{e.name}</b>
                    <span
                      className={`desigBadge ${
                        e.designation.includes('Contract') || e.designation.includes('कंत्राटी')
                          ? 'contract'
                          : e.designation.includes('Gram Sewak') ||
                            e.designation.includes('ग्रामसेवक')
                          ? 'regular'
                          : e.designation.includes('Auditor')
                          ? 'auditor'
                          : 'officer'
                      }`}
                    >
                      {e.designation}
                    </span>
                    {e.district && <span className="districtTag">🗺️ {e.district}</span>}
                    <span className="talukaTag">📍 {e.taluka}</span>
                    {e.grade && <span className="gradeTag">{e.grade}</span>}
                    {contactHist && (
                      <span
                        className="sentStatusBadge"
                        title={`Last sent: ${formatTimestamp(contactHist.lastEntry.sentAt)}\nMessage: ${contactHist.lastEntry.message || '(No text)'}`}
                      >
                        ✓ Sent {contactHist.count > 1 ? `(${contactHist.count}×)` : ''} ·{' '}
                        {formatTimestamp(contactHist.lastEntry.sentAt)}
                      </span>
                    )}
                  </div>

                  <div className="empMetaRow">
                    {e.gramPanchayat && (
                      <span className="gpText" title={e.gramPanchayat}>
                        🏛️ <strong>GP:</strong> {e.gramPanchayat}
                      </span>
                    )}
                    {e.address && (
                      <span className="gpText" title={e.address}>
                        🏠 {e.address}
                        {e.pinCode ? ` - ${e.pinCode}` : ''}
                      </span>
                    )}
                    {e.sewarthId && (
                      <span className="sewarthText">
                        🆔 <strong>ID:</strong> {e.sewarthId}
                      </span>
                    )}
                    {e.email && (
                      <span className="emailText" title={e.email}>
                        ✉️ {e.email}
                      </span>
                    )}
                    {e.remarks && <span className="remarksText">ℹ️ {e.remarks}</span>}
                  </div>
                </div>

                <div className="empRightCol">
                  {hasPhone ? (
                    <span className="phone">📱 +91 {e.phone}</span>
                  ) : (
                    <span className="noPhone">⚠️ No Phone</span>
                  )}
                  <div className="rowBtnGroup">
                    {hasPhone && (
                      <button
                        type="button"
                        className="quickChatBtn"
                        title="Open WhatsApp chat immediately"
                        onClick={ev => openSingleChat(e, ev)}
                      >
                        Chat ↗
                      </button>
                    )}
                    {hasPhone && (
                      <button
                        type="button"
                        className="quickLogBtn"
                        title="Mark as sent in Message History"
                        onClick={ev => markManualSent(e, ev)}
                      >
                        ✓ Log
                      </button>
                    )}
                  </div>
                </div>
              </label>
            );
          })}
          {filtered.length > visibleCount && (
            <div className="loadMoreRow">
              <span>
                Showing {visibleEmployees.length} of {filtered.length} matching contacts
              </span>
              <div className="loadMoreBtns">
                <button
                  type="button"
                  className="actionLink"
                  onClick={() => setVisibleCount(c => c + PAGE_SIZE)}
                >
                  Show {Math.min(PAGE_SIZE, filtered.length - visibleCount)} more
                </button>
                <button
                  type="button"
                  className="actionLink"
                  onClick={() => setVisibleCount(filtered.length)}
                >
                  Show all ({filtered.length})
                </button>
              </div>
            </div>
          )}
          {!filtered.length && (
            <div className="empty">
              <p>No employees match the current filters or search term.</p>
              <button className="outlineBtn" onClick={clearFilters}>
                Clear all filters
              </button>
            </div>
          )}
        </div>

        {/* Excel Import Footer */}
        <div className="importRow">
          <label className="outlineBtn">
            ＋ Import Excel / CSV
            <input
              type="file"
              accept=".xlsx,.xls,.csv"
              hidden
              onChange={e => {
                if (e.target.files?.[0]) importExcel(e.target.files[0]);
                e.currentTarget.value = '';
              }}
            />
          </label>
          <label className="checkLabel" style={{ fontSize: '11.5px', fontWeight: 600 }}>
            <input
              type="checkbox"
              checked={mergeOnImport}
              onChange={e => setMergeOnImport(e.target.checked)}
            />
            <span>Merge with existing (avoid duplicates)</span>
          </label>
          <span>
            Reads all sheets; automatically skips or merges duplicate entries by phone, Sewarth ID,
            or name.
          </span>
        </div>
      </section>

      {/* STEP 2: COMPOSE MESSAGE */}
      <section className="panel">
        <div className="sectionHead">
          <div>
            <span className="step">02</span>
            <div>
              <h3>Compose WhatsApp Message</h3>
              <p>Write circulars, instructions, meeting alerts in Marathi, English, or both.</p>
            </div>
          </div>
        </div>

        <textarea
          className="messageBox"
          placeholder="उदा. सर्व ग्रामसेवक महोदयांना सूचित करण्यात येते की, उद्या दिनांक रोजी महत्त्वाची आढावा बैठक आयोजित करण्यात आली आहे..."
          value={message}
          onChange={e => setMessage(e.target.value)}
          rows={5}
        />

        <div className="composeBottom">
          <span>{message.length} characters</span>
          <label className="outlineBtn">
            ＋ Attach Circular / Image
            <input
              ref={fileRef}
              type="file"
              accept="image/*"
              hidden
              onChange={e => setFile(e.target.files?.[0] || null)}
            />
          </label>
        </div>

        {file && (
          <div className="imagePreview">
            <img src={preview} alt="Selected attachment preview" />
            <div>
              <b>{file.name}</b>
              <small>{(file.size / 1024 / 1024).toFixed(2)} MB</small>
              <button
                className="remove"
                onClick={() => {
                  setFile(null);
                  if (fileRef.current) fileRef.current.value = '';
                }}
              >
                Remove image
              </button>
            </div>
          </div>
        )}
        <p className="hint">
          💡 For text messages, WhatsApp web / app opens prefilled directly. For images with text,
          mobile browsers support the native share sheet.
        </p>
      </section>

      {/* STEP 3: START SENDING QUEUE */}
      <section className="panel launchPanel">
        <div className="sectionHead">
          <div>
            <span className="step">03</span>
            <div>
              <h3>Review & Prepare WhatsApp Queue</h3>
              <p>Queue recipients for sequentially verified sending.</p>
            </div>
          </div>
        </div>

        <div className="launchSummary">
          <div>
            <span>Recipients Selected</span>
            <strong>{selected.length} employees</strong>
          </div>
          <div>
            <span>Content Payload</span>
            <strong>
              {file ? 'Image + Text Caption' : message.trim() ? 'Text Message' : 'Not added yet'}
            </strong>
          </div>
          <div>
            <span>Talukas Represented</span>
            <strong>
              {
                Array.from(
                  new Set(
                    employees
                      .filter(e => selected.includes(String(e.id)))
                      .map(e => e.taluka)
                      .filter(Boolean)
                  )
                ).length
              }{' '}
              Talukas
            </strong>
          </div>
        </div>

        <button
          className="primary"
          onClick={start}
          disabled={selected.length === 0 || (!message.trim() && !file)}
        >
          Prepare WhatsApp queue ({selected.length}) <span>→</span>
        </button>
        <p className="hint">
          This system respects WhatsApp privacy & anti-spam protocols by allowing you to confirm
          and send to each recipient one-by-one.
        </p>
      </section>

      {/* STEP 4: SENDING QUEUE MONITOR */}
      {queue.length > 0 && (
        <section className="panel queuePanel">
          <div className="sectionHead">
            <div>
              <span className="step">04</span>
              <div>
                <h3>Sequential Sending Queue</h3>
                <p>
                  Recipient {Math.min(current + 1, queue.length)} of {queue.length}
                </p>
              </div>
            </div>
            <button className="textBtn danger" onClick={stop}>
              Stop Queue
            </button>
          </div>

          <div className="progress">
            <span
              style={{
                width: `${Math.min(100, ((sent.length + skipped.length) / queue.length) * 100)}%`
              }}
            />
          </div>

          {person ? (
            <>
              <div className="currentPerson">
                <span className="avatar big">{person.name.charAt(0) || '👤'}</span>
                <div>
                  <b>{person.name}</b>
                  <div className="currentPersonMeta">
                    <span className="desigBadge regular">{person.designation}</span>
                    <span className="talukaTag">📍 {person.taluka}</span>
                    {person.gramPanchayat && (
                      <span className="gpText">🏛️ {person.gramPanchayat}</span>
                    )}
                  </div>
                  <small className="currentPersonPhone">📱 +91 {person.phone}</small>
                  {getContactHistory(person) && (
                    <div className="priorSentNote">
                      ✓ Previously messaged {getContactHistory(person)!.count}× (last:{' '}
                      {formatTimestamp(getContactHistory(person)!.lastEntry.sentAt)})
                    </div>
                  )}
                </div>
              </div>

              <div className="queueButtons">
                <button
                  type="button"
                  className="primary"
                  onClick={file ? copyImageAndOpenChat : openTextChat}
                >
                  {file ? 'Open WhatsApp chat (+ copy image) ↗' : 'Open WhatsApp chat ↗'}
                </button>
                {file && (
                  <>
                    <button type="button" className="outlineBtn" onClick={openTextChat}>
                      💬 Open chat only ↗
                    </button>
                    <button type="button" className="outlineBtn" onClick={shareImage}>
                      📤 Share image (pick contact)
                    </button>
                  </>
                )}
                <button type="button" className="outlineBtn" onClick={() => next(false)}>
                  Skip recipient
                </button>
                <button type="button" className="sentBtn" onClick={() => next(true)}>
                  ✓ Mark sent & Next
                </button>
              </div>
              {file && (
                <p className="hint">
                  Direct WhatsApp links open {person.name}&apos;s exact chat with your message
                  pre-filled (your image is copied to clipboard where supported so you can paste it
                  inside the chat). Use &ldquo;Share image (pick contact)&rdquo; only if you want
                  Android&apos;s share sheet.
                </p>
              )}

              <p className="hint">
                After the chat window opens and message is sent in WhatsApp, return here and click{' '}
                <strong>Mark sent & Next</strong>.
              </p>
            </>
          ) : (
            <div className="done">
              <b>🎉 Queue completed!</b>
              <p>
                {sent.length} marked as sent · {skipped.length} skipped · {queue.length} total
                processed
              </p>
              <button className="outlineBtn" onClick={stop}>
                Close Queue
              </button>
            </div>
          )}
        </section>
      )}

      {/* STEP 5: COMPLETE MESSAGE HISTORY */}
      <section className="panel historyPanel">
        <div className="sectionHead">
          <div>
            <span className="step">05</span>
            <div>
              <h3>Message History ({history.length})</h3>
              <p>
                Complete log of all messages sent ({uniqueContactsReached} unique contacts reached,{' '}
                {Math.max(0, employees.length - uniqueContactsReached)} pending).
              </p>
            </div>
          </div>
          <div className="headActions">
            {history.length > 0 && (
              <>
                <button type="button" className="outlineBtn" onClick={exportHistoryExcel}>
                  ⬇ Export History (.xlsx)
                </button>
                <button type="button" className="textBtn danger" onClick={clearHistory}>
                  🗑 Clear History
                </button>
              </>
            )}
          </div>
        </div>

        {history.length > 0 && (
          <div className="searchBox" style={{ marginBottom: '12px' }}>
            <span className="searchIcon">🔍</span>
            <input
              className="search"
              placeholder="Search history by recipient name, phone, Taluka, GP, or message text…"
              value={historyQuery}
              onChange={e => setHistoryQuery(e.target.value)}
            />
            {historyQuery && (
              <button className="clearInputBtn" onClick={() => setHistoryQuery('')}>
                ×
              </button>
            )}
          </div>
        )}

        <div className="historyList">
          {filteredHistory.map(h => (
            <div className="historyItem" key={h.id}>
              <div className="historyTop">
                <div className="historyTitle">
                  <b>{h.name}</b>
                  <span className="talukaTag">📍 {h.taluka}</span>
                  <span className="desigBadge regular">{h.designation}</span>
                  <span className={`modeBadge ${h.mode}`}>
                    {h.mode === 'queue' ? 'Queue' : 'Direct'}
                  </span>
                </div>
                <div className="historyRight">
                  <span className="historyTime">🕒 {formatTimestamp(h.sentAt)}</span>
                  <button
                    type="button"
                    className="deleteHistoryBtn"
                    title="Remove this log entry"
                    onClick={() => removeHistoryEntry(h.id)}
                  >
                    ×
                  </button>
                </div>
              </div>
              <div className="historyMeta">
                <span>📱 +91 {h.phone}</span>
                {h.gramPanchayat && <span>🏛️ GP: {h.gramPanchayat}</span>}
                {h.imageName && <span>🖼️ Image: {h.imageName}</span>}
              </div>
              {h.message && <p className="historyMsg">{h.message}</p>}
            </div>
          ))}
          {!history.length && (
            <div className="empty">
              <p>
                No messages logged yet. Send messages via the queue or click &quot;Chat ↗&quot; /
                &quot;✓ Log&quot; on any contact to track history here.
              </p>
            </div>
          )}
          {history.length > 0 && !filteredHistory.length && (
            <div className="empty">
              <p>No history entries match your search.</p>
            </div>
          )}
        </div>
      </section>

      <footer>
        <span>
          WhatsApp Employee Messenger · Chandrapur District Directory (Gram Sewak & Health Staff)
        </span>
        <span>Secure & runs locally in your browser</span>
      </footer>
    </main>
  );
}

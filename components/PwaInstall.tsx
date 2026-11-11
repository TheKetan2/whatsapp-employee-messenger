'use client';
import { useEffect, useState } from 'react';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed'; platform: string }>;
}

/**
 * Registers the PWA service worker and exposes an install button/hint for mobile browsers.
 */
export function PwaInstall({ variant = 'button' }: { variant?: 'button' | 'banner' }) {
  const [deferredPrompt, setDeferredPrompt] = useState<BeforeInstallPromptEvent | null>(null);
  const [isInstalled, setIsInstalled] = useState(false);
  const [showIosHint, setShowIosHint] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    if (typeof window === 'undefined') return;

    const standalone =
      window.matchMedia('(display-mode: standalone)').matches ||
      Boolean((window.navigator as Navigator & { standalone?: boolean }).standalone);
    setIsInstalled(standalone);

    const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? '';
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker
        .register(`${basePath}/sw.js`, { scope: `${basePath}/` })
        .catch(() => {
          // SW registration skipped if unsupported
        });
    }

    const ua = window.navigator.userAgent;
    const isIos = /iPad|iPhone|iPod/.test(ua) && !(window as unknown as { MSStream?: unknown }).MSStream;
    if (isIos && !standalone) {
      setShowIosHint(true);
    }

    const onBeforeInstall = (e: Event) => {
      e.preventDefault();
      setDeferredPrompt(e as BeforeInstallPromptEvent);
    };

    const onAppInstalled = () => {
      setIsInstalled(true);
      setDeferredPrompt(null);
      setShowIosHint(false);
    };

    window.addEventListener('beforeinstallprompt', onBeforeInstall);
    window.addEventListener('appinstalled', onAppInstalled);
    return () => {
      window.removeEventListener('beforeinstallprompt', onBeforeInstall);
      window.removeEventListener('appinstalled', onAppInstalled);
    };
  }, []);

  const handleInstall = async () => {
    if (!deferredPrompt) return;
    await deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === 'accepted') {
      setIsInstalled(true);
    }
    setDeferredPrompt(null);
  };

  if (variant === 'button') {
    if (isInstalled) {
      return <span className="pwaInstalledTag">✓ Installed App</span>;
    }
    if (!deferredPrompt) return null;
    return (
      <button type="button" className="installAppBtn" onClick={handleInstall}>
        📲 Install App
      </button>
    );
  }

  if (isInstalled || dismissed) return null;

  if (deferredPrompt) {
    return (
      <div className="pwaBanner" role="region" aria-label="Install application">
        <div className="pwaBannerText">
          <strong>Install WA Messenger on your phone</strong>
          <span>Launch from your home screen with offline contact access.</span>
        </div>
        <div className="pwaBannerActions">
          <button type="button" className="installAppBtn" onClick={handleInstall}>
            📲 Install Now
          </button>
          <button
            type="button"
            className="pwaDismissBtn"
            onClick={() => setDismissed(true)}
            aria-label="Dismiss install prompt"
          >
            ×
          </button>
        </div>
      </div>
    );
  }

  if (showIosHint) {
    return (
      <div className="pwaBanner" role="region" aria-label="iOS installation instructions">
        <div className="pwaBannerText">
          <strong>Add to iPhone / iPad Home Screen</strong>
          <span>Tap the Safari Share button and choose &ldquo;Add to Home Screen&rdquo;.</span>
        </div>
        <button
          type="button"
          className="pwaDismissBtn"
          onClick={() => setDismissed(true)}
          aria-label="Dismiss install hint"
        >
          ×
        </button>
      </div>
    );
  }

  return null;
}


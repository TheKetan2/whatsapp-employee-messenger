const CACHE_NAME = 'wa-messenger-v3';
const SCOPE_URL = new URL('./', self.location.href);
const toScopedUrl = path => new URL(path, SCOPE_URL).href;

const APP_SHELL = [
  './',
  'manifest.json',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/apple-touch-icon.png'
].map(toScopedUrl);

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(APP_SHELL)).catch(() => undefined)
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches
      .keys()
      .then(keys =>
        Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))
      )
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const { request } = event;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  // Skip Next.js dev HMR streams and hot-update chunks
  if (
    url.pathname.includes('/_next/webpack-hmr') ||
    url.pathname.includes('hot-update')
  ) {
    return;
  }

  // Navigation requests: network-first, falling back to cached home shell offline
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          if (response.ok) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
          }
          return response;
        })
        .catch(() => caches.match(request).then(res => res || caches.match(toScopedUrl('./'))))
    );
    return;
  }

  // Static Next assets and icons: cache-first / stale-while-revalidate
  if (url.pathname.includes('/_next/static/') || url.pathname.includes('/icons/')) {
    event.respondWith(
      caches.match(request).then(cached => {
        const networkFetch = fetch(request)
          .then(response => {
            if (response.ok) {
              const copy = response.clone();
              caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
            }
            return response;
          })
          .catch(() => cached);
        return cached || networkFetch;
      })
    );
    return;
  }

  // Manifest / data assets: network-first with offline cache fallback
  event.respondWith(
    fetch(request)
      .then(response => {
        if (response.ok) {
          const copy = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        }
        return response;
      })
      .catch(() => caches.match(request))
  );
});

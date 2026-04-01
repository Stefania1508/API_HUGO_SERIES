const CACHE_NAME = "aot-pwa-v1";

const urlsToCache = [
  "/",
  "/offline",
  "/static/css/style.css",
  "/static/js/pwa.js",
  "/static/manifest.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    fetch(event.request).catch(() => {
      return caches.match(event.request).then((response) => {
        return response || caches.match("/offline");
      });
    })
  );
});
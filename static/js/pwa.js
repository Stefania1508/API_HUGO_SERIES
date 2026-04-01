if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/static/sw.js")
      .then((registration) => {
        console.log("Service Worker registrado:", registration.scope);
      })
      .catch((error) => {
        console.error("Error registrando el Service Worker:", error);
      });
  });
}
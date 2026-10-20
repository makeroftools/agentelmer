/* Agent Elmer — theme.js
   Applies the saved or system theme before first paint. No network calls. */
(function () {
  "use strict";
  try {
    var saved = window.localStorage.getItem("agent-elmer-theme");
    var theme = saved;
    if (theme !== "light" && theme !== "dark") {
      theme = (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches) ? "light" : "dark";
    }
    document.documentElement.setAttribute("data-theme", theme);
  } catch (err) {
    /* Leave the default tokens in place if storage is unavailable. */
  }
}());

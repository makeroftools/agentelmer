/* Agent Elmer — site.js
   Small, dependency-free projection helpers. No network calls, no trackers,
   no third-party code. The site is fully readable without JavaScript. */
(function () {
  "use strict";

  var root = document.documentElement;
  var storageKey = "agent-elmer-theme";

  function applyTheme(theme) {
    if (theme === "light" || theme === "dark") {
      root.setAttribute("data-theme", theme);
    } else {
      root.removeAttribute("data-theme");
    }
    var button = document.querySelector(".themer");
    if (button) {
      var current = root.getAttribute("data-theme") || "default";
      button.setAttribute("aria-label", "Theme: " + current + ". Switch theme.");
      button.textContent = current === "light" ? "◐" : "◑";
    }
  }

  function preferredTheme() {
    try {
      var saved = window.localStorage.getItem(storageKey);
      if (saved === "light" || saved === "dark") return saved;
    } catch (err) {
      /* storage can be unavailable; fall through to the system preference */
    }
    if (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches) {
      return "light";
    }
    return "dark";
  }

  function initTheme() {
    applyTheme(preferredTheme());
    var button = document.querySelector(".themer");
    if (!button) return;
    button.addEventListener("click", function () {
      var next = (root.getAttribute("data-theme") === "light") ? "dark" : "light";
      applyTheme(next);
      try { window.localStorage.setItem(storageKey, next); } catch (err) { /* ignore */ }
    });
  }

  function initNav() {
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.getElementById("site-nav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      nav.addEventListener("click", function (event) {
        if (event.target && event.target.tagName === "A") {
          nav.classList.remove("is-open");
          toggle.setAttribute("aria-expanded", "false");
        }
      });
    }

    var here = window.location.pathname.split("/").pop() || "index.html";
    var links = document.querySelectorAll(".topnav a[data-nav]");
    for (var i = 0; i < links.length; i += 1) {
      var href = (links[i].getAttribute("href") || "").split("#")[0];
      if (href === here) {
        links[i].setAttribute("aria-current", "page");
      }
    }
  }

  function initExternalLinks() {
    var links = document.querySelectorAll('a[href^="http://"], a[href^="https://"]');
    for (var i = 0; i < links.length; i += 1) {
      links[i].setAttribute("rel", "noopener noreferrer");
    }
  }

  function initCopyButtons() {
    var blocks = document.querySelectorAll("pre > code");
    for (var i = 0; i < blocks.length; i += 1) {
      (function (code) {
        var button = document.createElement("button");
        button.type = "button";
        button.className = "copy";
        button.textContent = "Copy";
        button.setAttribute("aria-label", "Copy this command to the clipboard");
        button.addEventListener("click", function () {
          var text = code.textContent || "";
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(function () {
              button.textContent = "Copied";
              window.setTimeout(function () { button.textContent = "Copy"; }, 1400);
            }, function () { button.textContent = "Select"; });
          } else {
            button.textContent = "Select";
          }
        });
        code.parentNode.appendChild(button);
      }(blocks[i]));
    }
  }

  function init() {
    initTheme();
    initNav();
    initExternalLinks();
    initCopyButtons();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
}());

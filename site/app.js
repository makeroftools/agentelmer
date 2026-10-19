/* app.js — reveal, spine progress, and keyboard beat navigation.
   No dependencies. Respects prefers-reduced-motion. */
(() => {
  const beats = Array.from(document.querySelectorAll(".beat"));
  const spine = document.querySelector(".spine__fill");
  const railLinks = Array.from(document.querySelectorAll(".rail a"));
  const setActive = (id) => railLinks.forEach((a) =>
    a.classList.toggle("active", a.dataset.target === id));

  // Reveal beats as they approach the viewport. Scroll-driven so it also
  // works where IntersectionObserver does not fire (and with no JS, CSS shows all).
  const reveal = () => {
    const edge = window.scrollY + window.innerHeight * 0.92;
    for (const b of beats) {
      if (!b.classList.contains("in") && b.offsetTop <= edge) b.classList.add("in");
    }
  };

  // The spine fills with reading progress — authority made visible.
  const onScroll = () => {
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    const pct = max > 0 ? (h.scrollTop / max) * 100 : 0;
    if (spine) spine.style.setProperty("--progress", pct + "%");
    const probe = window.scrollY + window.innerHeight * 0.38;
    let current = beats[0];
    for (const b of beats) if (b.offsetTop <= probe) current = b;
    if (current) setActive(current.id);
    reveal();
  };
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Theme toggle.
  const themer = document.getElementById("themer");
  if (themer) {
    themer.addEventListener("click", () => {
      const cur = document.documentElement.getAttribute("data-theme");
      const next = cur === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("ae-theme", next); } catch (e) {}
    });
  }

  // Arrow / page keys jump between beats (a quiet present mode).
  const goto = (i) => {
    const j = Math.max(0, Math.min(beats.length - 1, i));
    beats[j].scrollIntoView({ behavior: "smooth", block: "start" });
  };
  document.addEventListener("keydown", (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const top = window.scrollY + 80;
    let current = 0;
    beats.forEach((b, i) => { if (b.offsetTop <= top) current = i; });
    if (e.key === "ArrowRight" || e.key === "ArrowDown" || e.key === "PageDown") {
      if (e.key !== "ArrowDown") { e.preventDefault(); goto(current + 1); }
    } else if (e.key === "ArrowLeft" || e.key === "ArrowUp" || e.key === "PageUp") {
      if (e.key !== "ArrowUp") { e.preventDefault(); goto(current - 1); }
    }
  });
})();

id: guarantees
kind: prose
label: Guarantees
title: Promises that are enforced, not aspirational.

Every claim below is backed by an external check that runs on the floor. A guarantee that cannot be verified is not offered.

```html
<div class="grid">
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M4 9h16"/><path d="M4 15h16"/></svg></span>
    <h3>Deterministic</h3>
    <p>Same pinned inputs, same outcome — proven by byte-identical replay, or the run refuses.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 1 3 6.2"/><path d="M4 20v-5h5"/></svg></span>
    <h3>Replayable</h3>
    <p>Every run records a trajectory. Re-run it later and get exactly the same result, or the divergence is refused.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M4 5h16l-6 7v6l-4 2v-8z"/></svg></span>
    <h3>Clamped</h3>
    <p>The model may propose; its output is recorded as an observation and can never become authority.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3" stroke-dasharray="4 4"/><circle cx="12" cy="12" r="3"/></svg></span>
    <h3>Contained</h3>
    <p>Autonomy runs inside a signed mandate of paths, verbs, and budgets. Exhaustion hands off — never a silent continuation.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg></span>
    <h3>Default-deny</h3>
    <p>No ambient network, filesystem, secret, or clock. Every access is an explicit, recorded grant.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg></span>
    <h3>Tamper-evident</h3>
    <p>Identity is recomputed from content, never trusted. A changed byte is refused, not worked around.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M12 3l8 4v10l-8 4-8-4V7z"/><path d="M4 7l8 4 8-4"/><path d="M12 11v10"/></svg></span>
    <h3>Self-contained</h3>
    <p>A component carries everything it needs, signed, and loads offline from a verified cache.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M3 12h4l2-6 4 12 2-6h6"/></svg></span>
    <h3>Live</h3>
    <p>Components initialize, run, and tear down. A piece can be repaired or replaced with no downtime.</p>
  </div>
</div>
```

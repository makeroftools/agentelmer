id: capabilities
kind: prose
label: Capabilities
title: An engine that does real work.

```html
<div class="grid">
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><path d="M7 6h10"/><path d="M12 8v8"/><path d="M5.6 7.8 11 16"/><path d="M18.4 7.8 13 16"/></svg></span>
    <h3>Durable parallel agents</h3>
    <p>Fan out many agents at once. They survive a restart, and the parent joins their results deterministically.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M4 9h16"/><path d="M4 15h16"/></svg></span>
    <h3>Same inputs, same bytes</h3>
    <p>Every build is reproducible on any machine. No "it worked on my machine" — the output is a function of pinned inputs.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M12 3l7 4v10l-7 4-7-4V7z"/><circle cx="12" cy="12" r="2.2"/></svg></span>
    <h3>Content-addressed artifacts</h3>
    <p>Every result carries an address. Replay it, verify it, cite it — provenance is a fact, not a claim.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></svg></span>
    <h3>Provider-placed execution</h3>
    <p>Trusted work runs in-thread; untrusted work runs in a supervised process. The addressed output is identical either way.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg></span>
    <h3>Fail-closed gates</h3>
    <p>A check that cannot pass refuses. No partial success, no silent default, no hidden fallback.</p>
  </div>
  <div class="card">
    <span class="icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.4"/><path d="M5 21c0-3.9 3.1-6 7-6s7 2.1 7 6"/></svg></span>
    <h3>Approval, on purpose</h3>
    <p>Approval is requested only where a step is genuinely non-deterministic — never as a blanket "are you sure?".</p>
  </div>
</div>
```

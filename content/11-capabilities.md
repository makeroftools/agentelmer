id: capabilities
kind: prose
label: Capabilities
title: An engine that does real work.

```html
<div class="grid">
  <div class="card">
    <span class="tag">01 · Concurrency</span>
    <h3>Durable parallel agents</h3>
    <p>Fan out many agents at once. They survive a restart, and the parent joins their results deterministically.</p>
  </div>
  <div class="card">
    <span class="tag">02 · Determinism</span>
    <h3>Same inputs, same bytes</h3>
    <p>Every build is reproducible on any machine. No "it worked on my machine" — the output is a function of pinned inputs.</p>
  </div>
  <div class="card">
    <span class="tag">03 · Addresses</span>
    <h3>Content-addressed artifacts</h3>
    <p>Every result carries an address. Replay it, verify it, cite it — provenance is a fact, not a claim.</p>
  </div>
  <div class="card">
    <span class="tag">04 · Placement</span>
    <h3>Provider-placed execution</h3>
    <p>Trusted work runs in-thread; untrusted work runs in a supervised process. The addressed output is identical either way.</p>
  </div>
  <div class="card">
    <span class="tag">05 · Safety</span>
    <h3>Fail-closed gates</h3>
    <p>A check that cannot pass refuses. No partial success, no silent default, no hidden fallback.</p>
  </div>
  <div class="card">
    <span class="tag">06 · Human</span>
    <h3>Approval, on purpose</h3>
    <p>Approval is requested only where a step is genuinely non-deterministic — never as a blanket "are you sure?".</p>
  </div>
</div>
```

id: proof
kind: prose
label: Proof
title: Provable — not promised.

Every artifact the factory produces is content-addressed. Two runs, two machines, one address. There is no "it worked on my machine."

```html
<figure class="diagram">
<img src="/proof.svg" alt="Two identical runs produce the same address">
<figcaption class="muted">Same inputs, same bytes — every time.</figcaption>
</figure>
```

- **Deterministic** — the same pinned inputs yield the same outcome, every time.
- **Verifiable** — an external check decides pass or fail; the model never has the last word.
- **Idempotent** — a re-run is a no-op; state converges.

And when a check cannot pass, it *refuses*. No partial success. No silent pass. The floor is green, or the build does not ship.

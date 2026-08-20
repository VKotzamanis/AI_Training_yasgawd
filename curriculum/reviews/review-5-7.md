# Peer review — `slides/05-intrinsic-failure.md` and `slides/07-physical-limits.md`

## Summary

Checks that passed: hard rule 3 holds in the Chapter 5 direction (no cost equation, and
the "cost has an equation, accuracy does not" slide states the distinction cleanly); the
licensing distinction is correct (TACL version of record CC BY 4.0, arXiv under
`nonexclusive-distrib`, no redistribution right); `05-position-schematic.png` carries
"SCHEMATIC — the shape only. Not measured data." burnt into the image with an
`[arbitrary]` accuracy axis; no source figure is reproduced, so no licence is breached;
the Chroma COI is declared in full; the Pope COI is declared on its own slide and
re-rendered on every footer, because `components/Cite.vue` emits "Expert testimony, not a
primary source. COI declared." when `kind==="testimony"` or `coi===true`; and the softmax
slide bounds sharpness of selection and refuses the accuracy reading outright.

The Chapter 7 algebra is correct. `T ≥ max(T_comp, T_mem)`, `T_comp = 2BN_act/F = BN_act/M`,
`T_mem = (N_tot b_w + B L b_kv)/β`, `c ≡ T/B`, the `T_mem/B` split into a `1/B` term plus a
term constant in `B`, and `B* = (F b_w)/(2β) × (N_tot/N_act)` from equating `T_comp` with the
weight-fetch term — all follow. The defects are in unit bookkeeping, citation targeting,
unstated modelling assumptions, and one breach of the accuracy boundary.

## Key Issues

### 1. Chapter 7 makes a quality claim about long context. CONFIRMED.

`07-physical-limits.md`, "Long context is a memory problem, not a compute problem":
"Sparse attention improves the scaling — **the source notes it does so at a cost in
quality**."

Hard rule 3 and `chapter-briefs.md` ("**Does not cover accuracy.** Cost and latency only")
forbid this. It is an accuracy claim about a long-context mechanism, resting on expert
testimony with a declared commercial interest, with no empirical support anywhere in the
project. It contradicts this deck's own slide: "This chapter is about **cost and latency**.
It says nothing about **accuracy**." `references.md` records the claim, so this is faithful
transcription — which is how the conflation enters: the cost source volunteers an accuracy
claim and the cost chapter carries it. **Fix:** stop at "improves the scaling"; hand quality
to Chapter 5 by name.

### 2. A verified Anthropic result appears uncited, so its COI is undeclared. CONFIRMED.

`05-intrinsic-failure.md`, "The distinction people miss": "the chain of thought reveals the
hint it actually used **often below 20% of the time**." The slide's only footer is
`<Cite k="turpin2023" />`. That figure is Chen et al. 2025 (`arXiv:2505.05410`), present in
`sources.json` as `chen2025` with `"coi": true`. A numeric result is attributed to a paper
that does not contain it; and because the key is absent, `Cite.vue` never renders the COI
marker — so the one Anthropic faithfulness claim in the deck is the one that goes
undeclared, against `references.md`'s requirement of a COI note on "**Any**
Anthropic-published interpretability work used in Chapter 5". The next bullet ("their hints
are easy to exploit") is also Chen §7.2. **Fix:** add `<Cite k="chen2025" />`; it is `[V]`,
so the build check passes.

### 3. The erratum is footnoted to the lecturer, not the reader. CONFIRMED.

`07-physical-limits.md`, "The denominator is the whole argument": "An outside reader caught
this in the transcript's comment thread." — footer `<Cite k="pope2026" />`. `references.md`:
"**Attribute it to the reader, not to the lecturer** — the whole teaching point is that an
outside reader caught it." A dedicated `[V]` key exists, `erratum2026`. As written, Pope's
name prints under the slide about Pope's error. `scripts/check-cites.mjs` cannot catch this:
it validates that keys resolve and are `[V]`, never that a key matches its claim. **Fix:**
`<Cite k="erratum2026" />`.

### 4. The erratum's magnitude is right; its direction is unstated. CONFIRMED.

Same slide: "makes the answer **wrong by exactly a factor of two**." Verified: `T = BN_act/M`
with `M → F` gives `BN_act/F`, **half** the correct `2BN_act/F`. The factor belongs in the
**numerator** of the FLOP-denominated form, and the error **underestimates** compute time —
flattering compute, moving the roofline crossover, and halving `B*` in the next argument.
The deck displays both forms, so numerator placement is visible, but leaves the sign to
guesswork. For Chapter 4's anchor artefact the direction is the lesson. **Fix:** "halves the
computed time; the missing 2 belongs in the numerator of the FLOP form."

### 5. "Dimensionless" is asserted for a quantity the deck's own table dimensions. CONFIRMED.

`07-physical-limits.md`, "Critical batch size": "the hardware ratio as $\approx 300$,
**dimensionless** and stable across several GPU generations." Read literally against the
Symbols table — `F` in `FLOP s⁻¹`, `b_w` in `byte`, `β` in `byte s⁻¹` — the prefactor
`F b_w/(2β)` has units of **FLOP**. It is dimensionless only if the constant `2` carries
`FLOP parameter⁻¹ token⁻¹` and `B`, `N_act`, `N_tot` are token and parameter counts rather
than the bare "—" the table gives them; under that (correct) reading `N_tot/N_act` is the
dimensionless factor and `B*` comes out in tokens. Either way one printed claim fails. The
Dimensions note has the same gap — "$2BN_\mathrm{act}$ is a FLOP count" holds only because
of a unit on the 2 that is never declared (it arrives two slides later as "two FLOP per
parameter per token"). This is the error class the chapter's own thesis slide is about.
**Fix:** `b_w` in `byte parameter⁻¹`, `N_act` in parameters, `B` in tokens, plus a table row
for `2 [FLOP parameter⁻¹ token⁻¹]`; then `B*` is in tokens and sparsity is dimensionless.

### 6. `B` carries two incompatible meanings. CONFIRMED.

Symbols: "$B$ | batch size, tokens per forward pass". In `T_comp = 2BN_act/F`, `B` is tokens
processed. In `B L b_kv`, `B` must be **concurrent sequences**, each holding `L` tokens of
cache, or the term double-counts. The two coincide only in single-token autoregressive
decode — a regime never stated, though everything downstream assumes it: `c = T/B` is
seconds per *generated* token. Prefill breaks the same equations. **Fix:** state the regime
above the roofline.

### 7. The capacity equation contradicts the slide after it. CONFIRMED.

"What has to fit on the device" divides **both** terms by `E_p × P_p`:
`M_device = (N_tot b_w + B L b_kv)/(E_p × P_p)`. The next slide: "It does **not** reduce KV
storage. The source states that the pipeline-stage factor cancels." As printed the equation
says the opposite, and the deck flags only the *mechanism* as `TODO(verify)`. Expert
parallelism shards experts, not the KV cache, so `E_p` is questionable on the second term
too. **Fix:** split the equation, or mark the shared denominator as the source's shorthand
and show the cancellation.

### 8. `2ND` leaves `N` unqualified in a chapter built on `N_tot ≠ N_act`. CONFIRMED.

"Two numbers you will see quoted": "$N$ — parameters, $D$ — tokens processed." The numerator
of `T_comp` is `2BN_act`, so at training scale it is `2 N_act D`. The preceding slide defines
sparsity as `N_tot/N_act` — precisely the factor by which an unqualified `N` is ambiguous,
and an order of magnitude for a sparse model. **Fix:** write `2 N_act D`, with dense models
as the special case.

### 9. A single-document instructor observation is presented as fact. CONFIRMED.

`05-intrinsic-failure.md`, "The band it lives in": "**Your own literature sits in that
band.** … That is why your experience is that the tool is reliable on textbook material and
erratic on your research, and it is not random." This is `chapter-briefs.md` finding 9,
resting on one vendor pipeline document, `[E1]`-scale and by hard rule 1a "still not
citable". No citation, no "instructor observation" label, and a causal explanation of the
audience's own experience. Hard rule 6 requires stating what a finding rests on; the deck
does that well elsewhere (needle, context rot, softmax) and not on the slide most likely to
be repeated. **Fix:** label it as annotation-work observation.

### 10. Three separate results share one citation. CONFIRMED.

"\"LLMs are black boxes\" — the correction", footer `<Cite k="templeton2024" />` only. The
slide asserts sparse autoencoders "first on a one-layer model" (that is `bricken2023`, whose
recorded caveat is "**Scope: a one-layer transformer**") and "**Attribution graphs** trace
the computational path" (`ameisen2025`/`lindsey2025`). All keys exist and are `[V]`.
**Fix:** cite all three.

### 11. An effective-context finding is asserted from unread papers. CONFIRMED.

"Supporting mechanisms — none of them proofs" (no citation footer): "benchmarks built to
test this **report exactly that**." `references.md` holds RULER, NoLiMa, LongBench and
BABILong at "**Abstract-level only — read the papers before any of their numbers reach a
slide**". Reporting their finding is the same transaction as reporting a number. The needle
slide's "A model can pass it and still fail when the question shares no words with the
answer" is NoLiMa's result, uncited. **Fix:** read and cite one, or reduce the bullet to the
nominal-versus-effective definition.

### 12. The substrates summary table has no citation footer. CONFIRMED.

"Three alternative substrates. They are not equivalent." asserts "nearly identical accuracy"
(revnets), "Large energy gains on specific benchmark tasks" (ornes2025) and "**No learning
system reported** — the authors' own words" (smirnova2023): a quotation attributed to
authors who are not named on the slide, against the house rule that every slide carries a
citation footer.

### 13. The bound is asserted to "close". CONFIRMED.

"What this chapter does not tell you": "You are about to derive it, **and it closes**." The
relation is written throughout as an inequality, and `F` and `β` are peak figures; realised
utilisation is below peak and is never mentioned. A lower bound on time is not a closed cost
model, and Chapter 13 reverse-engineers prices with it. **Fix:** say lower bound, and name
utilisation as the gap between bound and bill.

### 14. Minor

- "Reproducing that figure properly": "**The figure above is a schematic and says so on its
  face.**" No figure is on that slide — it is on the previous one, a separate page in the PDF
  export the project keeps as fallback. Move the sentence. CONFIRMED.
- Detection slide: "Detectors are unreliable in **both** directions." The `liang2023` record
  covers false positives only (61.22% TOEFL, near-zero 8th-grade). SUSPECTED.
- "reorder the options so the answer is always the first one" — the `turpin2023` record has
  only "injecting a biasing feature". SUSPECTED overreach on a specific manipulation.
- Organoid slide: "multiple cell types **at realistic densities**"; the record has "multiple
  cell types" without the qualifier. SUSPECTED.
- Neuromorphic footer prints "PNAS 122(44) — secondary account, not primary research" while
  `references.md` still holds "**TODO(verify)** the article type before the slide calls it
  anything". CONFIRMED, minor.
- `c` has units `s token⁻¹` and is called "cost" in a chapter framing tokens as "the unit of
  price". Money needs a device rate `[$ s⁻¹]` that never appears. CONFIRMED, minor.
- `M` is `MAC s⁻¹` in the Symbols table and `M_device` in bytes four slides later — a
  symbol collision on the denominator symbol in the chapter about denominators. CONFIRMED.
- Softmax slide: "as the number of items grows" drops the paper's size-generalisation
  framing (counts beyond those seen in training). SUSPECTED.

## Questions to Probe

1. Does the transcript state the sparse-attention quality cost as a measured result or an
   aside? If the latter, issue 1 is not a boundary judgement — it is unsourced.
2. Does the batch in flight grow with pipeline stages, as the `TODO(verify)` reading
   proposes? Until that is checked, two adjacent slides disagree in print.
3. Is `≈300` quoted with its own units, or is "dimensionless" an inference inherited from
   `references.md`, which may in turn have inherited it from testimony?
4. Which source supports "unreliable in both directions" — `liang2023`, or a brief assertion
   with nothing behind it?
5. Should `check-cites.mjs` flag key-to-claim mismatches? Issues 2 and 3 are invisible
   to the current check.

## Bottom Line

The derivation is sound and the evidential framing is better than most published teaching
material. Three defects are blocking: the sparse-attention quality claim (rule 3, in the
direction the project names as most likely), the uncited and COI-undeclared Chen result, and
the erratum footnoted to the lecturer whose error it is. The dimensional bookkeeping around
the constant `2` and the "dimensionless" hardware ratio must be fixed before a room of
engineers checks it live, because the chapter invites exactly that. The schematic figure,
the licensing distinction and the softmax slide need no change.

---

**Not done.** No primary source was fetched; everything was checked against `references.md`
and the deck text, so "the source does not say this" findings are marked SUSPECTED.
`check-cites.mjs` was read, not run, and the PDFs in `slides/exports/` were not opened, so I
cannot confirm the rendered decks match the markdown. Other decks, `architecture.md` and
`DECISIONS.md` were not reviewed, and `≈300` was not checked against a hardware
specification.

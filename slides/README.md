# Slides

Slidev deck source. One file per chapter, `NN-short-name.md`, numbered to match `../curriculum/architecture.md`.

Adopted on trial. Reversal triggers are in `../DECISIONS.md` — read them before building workarounds for anything that fights you.

## Pinned versions

| | Version | Set on |
|---|---|---|
| Node | 22.23.1 | 2026-08-19 |
| @slidev/cli | 52.19.1 | 2026-08-19 |
| Theme | @slidev/theme-default 0.25.0 | 2026-08-19 |
| vue | 3.5.41 | 2026-08-19 |
| playwright-chromium | installed for PDF export | 2026-08-19 |

Exact pins, no `^`. `sources.json` is generated, not committed.

Fill these in at setup and do not upgrade mid-project. A toolchain that changes under you between rehearsal and delivery is the failure mode this table exists to prevent.

## Build

```
npm run dev                    # live preview
npm run export                 # PDF
npm run check:cites            # fails if any [U]-tagged source appears in a slide
npm run check:cites:selftest   # proves the check still trips on a known-bad fixture
```

Pass the chapter file to the Slidev commands: `npx slidev 07-physical-limits.md`.

`check:cites` regenerates `sources.json` from `../references.md` first, so a tag
downgraded to `[U]` in that file breaks the build on the next run without anyone
having to remember. The self-test exists because a build check nobody tests is a
build check that has silently stopped working; `fixtures/` holds a deck citing
one `[U]` key and one unknown key, and the self-test fails if the check *passes*
on it.

## Rules

- Citations go through the footer component. Never hand-typed.
- Nothing load-bearing may be interactive-only — interactive features do not survive PDF export, and PDF is the fallback.
- Export to PDF and commit it whenever a chapter is finished.

## Spike results — 2026-08-19

Both spikes run, separately timeboxed so a failure names its own reversal trigger.

**Spike A — Chapter 7's hardest derivation, stepwise. PASSES, after one fix.**

`07-physical-limits.md` builds the roofline bound across six clicks, ends at the
cost-per-token hyperbola, and carries a second stepwise derivation for critical
batch size. Exported to PDF and to 25 click-stepped PNGs; alignment holds through
the reveal and nothing reflows.

**The failure worth recording, because it will recur in every chapter.** Math
inside a one-line raw `<div>` does not render — it appears verbatim as `$T$` on
the slide. This is CommonMark, not a Slidev defect: a raw HTML block swallows
everything up to the next blank line, so `$…$` never reaches the inline parser
and never reaches KaTeX. The build succeeds and the slide is wrong, which is the
dangerous combination. **Fix:** blank lines inside every cell.

```html
<div v-click="1">

$T \ge \max(T_\mathrm{comp},\ T_\mathrm{mem})$

</div>
```

Stepwise *aligned* derivations do not come from `\begin{aligned}` — KaTeX renders
that block atomically and you cannot click inside it. Use a three-column CSS grid,
one cell per term, with the same `v-click` index on the three cells of a row.

**Spike B — citation footer plus the `[U]` build check. PASSES.**

`components/Cite.vue` renders author, year, venue and identifier from a keyed list
generated out of `../references.md`; keys are never hand-typed. It also carries the
two things house style demands and a `.bib` would not have given for free: podcast
and interview material is labelled *expert testimony, not a primary source*, and a
COI flag prints on the slide. `scripts/check-cites.mjs` fails the build on a `[U]`
or `[X]` key and on an unknown key. Both verified.

Keys are declared in `references.md` with a `{#key | author | year | venue | id |
kind | coi}` marker. Four entries are annotated so far. **Rolling this out means
annotating every cited entry in that file** — that is the remaining cost, and it
is bounded and mechanical.

**Neither reversal trigger fired.** Trigger 3 stays untested by construction: it
fires during rehearsal week, when migrating to pandoc is not feasible anyway, so
what actually covers it is the committed PDF, not a toolchain change.

## Known defect found by the spike

Do not use `BW` for bandwidth. `B` is batch size, and `BW·B` renders as "BWB".
Bandwidth is `\beta`, which is also the standard roofline symbol.

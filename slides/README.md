# Slides

Slidev deck source. One file per chapter, `NN-short-name.md`, numbered to match `../curriculum/architecture.md`.

Adopted on trial. Reversal triggers are in `../DECISIONS.md` — read them before building workarounds for anything that fights you.

## Pinned versions

| | Version | Set on |
|---|---|---|
| Node | TODO | |
| @slidev/cli | TODO | |
| Theme | TODO | |

Fill these in at setup and do not upgrade mid-project. A toolchain that changes under you between rehearsal and delivery is the failure mode this table exists to prevent.

## Build

```
npm run dev            # live preview
npm run export         # PDF
npm run check:cites    # fails if any [U]-tagged source appears in a slide
```

## Rules

- Citations go through the footer component. Never hand-typed.
- Nothing load-bearing may be interactive-only — interactive features do not survive PDF export, and PDF is the fallback.
- Export to PDF and commit it whenever a chapter is finished.

## First task

Before writing any chapter in full, spike **Chapter 7's hardest derivation**: the roofline bound built up stepwise across clicks, with a citation footer attached. KaTeX is a subset of LaTeX and this is the content most likely to expose the gap. If it works, the toolchain is fine for everything else in the course.

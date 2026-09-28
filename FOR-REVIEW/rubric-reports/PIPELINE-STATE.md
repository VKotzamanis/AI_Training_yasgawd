# Rubric-review pipeline — state at pause (2026-08-28)

Paused by the user mid-run. This file is the resume key: everything below either
exists on disk and is verified, or is listed under "Remaining" with the exact
procedure to continue. Session that built all of this: fa4fff58-1e02-46a0-9e27-b82f6d002096
(`claude --resume` on that id reopens the full reasoning).

## Done and verified on disk

| artifact | status |
|---|---|
| `FOR-REVIEW/RUBRIC.md` | v1.1 (v1 + post-calibration C-scope amendment: contract binds at a component's fullest treatment, not per-slide) |
| `rubric-reports/calibration-ch1.md` | CALIBRATION: PASS (0 R/F/S blockers on the approved deck). T findings recorded for the author: 3, all CONFIRMED — incl. [cal-006] two capitalized-headword token splits on slides 8–9, verified by running the o200k_base encoder locally |
| `rubric-reports/PRIOR-REVIEW-SCOPE.md` | all 19 chapters mapped to the prior review; C-contract and S1/S2/S4 confirmed as genuine new ground |
| `rubric-reports/TOPICS-LEDGER.md` | seeded with 51 ch01-approved topics; ch01-draft (marked SUPERSEDED), ch02, ch03, ch04 appended by their reviewers |
| `rubric-reports/ch01-review.md` | **salvage-with-edits** — 18 findings: R 7 (4 blocker), T 5 (1 blocker), C 3, F 2, S4 1 |
| `rubric-reports/ch02-review.md` | **salvage-with-edits** — 19 findings: R 6 (2 blocker), F 4, T 2 (CONFIRMED), C 6, S3 1 |
| `rubric-reports/ch03-review.md` | **salvage-with-edits** — 12 findings: R 3, T 4 (all CONFIRMED, 1 blocker), C 4 (1 blocker), S 1 |
| `rubric-reports/ch04-review.md` | **salvage-with-edits** — 14 findings: T 6 (2 blocker; incl. a ~30× family-wise-error claim, reviewer-recomputed), C 5, R 1, F 1, S4 1 |

ch05: dispatched twice, interrupted twice (session restart, then user pause).
**Zero durable output — no report, no ledger append. Dispatch fresh; do not attempt
to resume the dead agent.**

## Remaining

1. **Reviews ch05–ch19, strictly one at a time** (user requirement: each reviewer
   reads the accumulated `TOPICS-LEDGER.md` so later chapters know what was already
   said, and appends its own exports after). Files, in order:
   `05-intrinsic-failure.md, 06-extrinsic-failure.md, 07-physical-limits.md,
   08-brain-and-model.md, 09-the-agent.md, 10-memory.md, 11-orchestration.md,
   12-extension.md, 13-access.md, 14-literature.md, 15-production.md,
   16-code-and-numerics.md, 17-critique.md, 18-governance.md, 19-judgement.md`
   — Opus subagents, the exact dispatch prompt is the canonical template used for
   ch02–ch04 (recorded in `docs/plans/2026-08-27-chapter-review-rubric.md` Task 4,
   amended with: ledger read as step 2, ledger append as step 6, cite RUBRIC v1.1).
   After each: verify `grep -L '^## Verdict' chNN-review.md` is empty and the ledger
   gained `## chNN`.
2. **Cross-chapter merge** (plan Task 5): concatenate the ledgers/exports, one agent
   flags cross-chapter repetition, curriculum-level forward dependencies,
   contradictions → `CROSS-CHAPTER.md`. Largely pre-computed by the sequential
   ledger mechanism; the merge formalizes it.
3. **Adversarial T-verification** (plan Task 6): every T finding attacked by a
   refuting agent; verdicts UPHELD/REFUTED/UNDECIDABLE appended per report
   (`## T verdicts` section). Priority targets already known: ch04's two T blockers
   (the ~30× family-wise-error recomputation and the B3 runnability claim), ch03's
   T blocker. Two agents at a time allowed here (no sequential dependency).
   Machine constraint: never more than two subagents concurrently (16 GB).
4. **`SUMMARY.md`** (plan Task 7): 19-row table (verdict, counts per class, upheld-T
   count), worst-first; cross-chapter tables; rubric-v2 notes.
5. **Capstone, explicitly commissioned by the user and to be done by the main
   session personally, not delegated:** peer-review the summary and critically
   assess each chapter's flow and the cohesion of the whole training — grounded in
   the 19 reports, `TOPICS-LEDGER.md`, `CROSS-CHAPTER.md`, and
   `ai-training/curriculum/architecture.md` (the intended thread map).

## Open items outside this pipeline (carried from the same session)

- MATLAB lab: adopted-but-unapplied changes — TEMP/DSEED sampling, `make_fmt`
  mixed-sign crash fix, E2 narrative rewrite, regeneration of every stale handout
  number on the presentation machine (`REVIEWD/MATLAB_EXAMPLES/PEER_REVIEW_2026-08-27.md`).
- `CH1_SLIDES_14-20.pptx`: verified in LibreOffice only; check Cambria Math glyphs
  (𝒱, 𝒰) and superscript baselines on first native PowerPoint open; four graphics
  are captioned placeholders by instruction.
- Supplement citations still verification-pending: Kingma & Ba (Adam), Srivastava
  (dropout), Dosovitskiy (ViT), Shazeer 2017 (MoE), RLVR origin.
- Calibration report's own caveats worth acting on someday: slide-3 overlapping
  text and slide-9 cost chart may be real defects rather than flattened-animation
  artifacts — check in PowerPoint; rubric v1.1's false-negative rate on bad input
  is untested (the 19 reviews are themselves the evidence being gathered).
- Staged-not-deployed skill `explaining-technical-material` with full RED test
  record: `docs/plans/2026-08-27-writing-stack-upgrade.md` Appendix B.

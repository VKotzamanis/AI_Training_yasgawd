# Rebuild plan — the remaining chapters

<!-- decision: rebuild-plan-two-track | status: adopted | supersedes: production-plan-serial-gate -->

**Goal:** take every remaining chapter from its Slidev draft to a reviewed Beamer deck with a
committed PDF, critically assessed before it is rebuilt, with the instructor annotating PDFs in
parallel rather than in series.

**Companion to:** `production-plan.md` (categories and accrual, still current), `architecture.md`
(threads and sequencing, binding), `peer-review-19-chapters.md` (premise verdicts, partly stale).

---

## 1. What is actually left

Measured 2026-08-21, not estimated.

| | Count |
|---|---|
| Chapters delivered | **18** — Chapter 8 is withdrawn, not deferred |
| Rebuilt in Beamer | 3 (Ch 1, 2, 3) |
| **Remaining to rebuild** | **15** |
| Chapters with a substantive Slidev draft | 19 of 19 |
| **Figures in any Slidev draft** | **0** |
| Figures built so far (Ch 1–3) | 37 |
| Non-`[V]` entries in `references.md` | 46 (25 `[U]`, 21 `[P]`) |
| Asset directories holding anything but a README | **0 of 4** |

Draft depth splits three ways, and it predicts how much of each rebuild is writing rather than
restructuring:

- **Deep (>450 lines):** 4, 5, 7 — restructure and figure work, little new argument.
- **Medium (260–380):** 6, 9, 10, 11, 12, 13, 18 — some new material.
- **Thin (190–230):** 14, 15, 16, 17, 19 — these are Part IV, and they are thin because they are
  blocked on facts about the group rather than because they were rushed.

**The figure load is the largest single item and it has not been costed anywhere.** Chapters 1–3
run about 0.46 figures per frame. Fifteen chapters at roughly twenty frames each implies
**around 140 more figures**, every one of them computed or drawn rather than generated.

**Citation density is lowest exactly where it should be highest.** Chapter 4 — the measurement
chapter — has three citation-shaped strings in its draft. Chapters 16, 19 and 17 have one, one and
two. Those four need sourcing work before they need slide work.

---

## 2. Where the existing production plan is now wrong

Recorded because it is being followed, and four of these would misdirect anyone reading it.

| § | What it says | Why it is wrong now |
|---|---|---|
| §4 order table | Chapter 8 — **"Done. 13 slides"** | Chapter 8 is not delivered. Listing it as done in the production order will read as progress. Its live content moved to Chapter 1's training frames and Chapter 10's opening; the rest is sunk. |
| §4 order table | Chapters 1, 2, 3, 7 — "Done, PDF committed" | Done **in Slidev**, before the 2026-08-20 reversal. Only 1, 2 and 3 are done in Beamer. Chapter 7 is a draft, not a deliverable. |
| §6 definition of done | `slides/NN-short-name.md` builds; `npm run check:cites` passes | Both superseded. The gates are `slides/beamer/build.sh` and `check-frames.py`, and they are stricter — they also fail on an overfull vbox and on a missing footer. |
| §6 rating axes | **"Budget — fails when it does not fit its minutes"** | Delivery length is not a criterion. Ruled 2026-08-20. This axis is deleted, not softened. |
| §2 categories | Chapter 2 is in two categories, which explains its overrun | The overrun reasoning is superseded. The category assignment itself still holds and is kept. |
| §3 accrual track | Failure gallery, eval runs, injection demo "start now, run in parallel" | **None has started.** All four asset directories contain only a README. Every artifact-bound chapter is blocked today. |

**What survives and is kept:** the A/B/C/D category system, the principle that production order
follows what is unblocked rather than what is most valuable, the figure-generation rules in §4a,
and the accrual track's existence.

**One principle needs restating rather than deleting.** §2 says category B must be written last
because its facts expire. That was clean when only five chapters carried version-fragile facts.
Chapters 1 and 3 now carry them too — Chapter 3 alone has two flagged frames. The rule becomes:
**every version-fragile fact is flagged at the frame that carries it and re-fetched in one sweep
during delivery week**, whatever chapter it sits in. Ordering no longer protects us.

---

## 3. The shape: two tracks, running at the same time

The old gate was one chapter per cycle, rated before the next starts. With a human annotating PDFs
that would mean fifteen round trips, and there is now evidence it is unnecessary: Chapters 2 and 3
were both built without an intervening annotation round and both landed.

**Track 1 — me.** Build unblocked chapters continuously. Each finished chapter produces a PDF
immediately rather than waiting for its batch.

**Track 2 — the instructor.** Annotate delivered PDFs, and clear the blocker list in §4. These are
independent of each other and both independent of Track 1.

**They meet at an intake.** Annotations come back in a batch; corrections are applied across all
annotated chapters at once; chapters unblocked in the meantime enter Track 1.

The one hard constraint on batching: **a batch never contains two chapters that share an unresolved
decision**, because one annotation would then have to settle both.

---

## 4. The blocker list — items only the instructor can clear

Everything here is on the critical path for at least one chapter and cannot be done from this side.
Listed once so the work can go in parallel rather than being discovered chapter by chapter.

| # | Item | Blocks | Notes |
|---|---|---|---|
| B1 | **Five eval cases and their pass criteria**, run in advance | Ch 4 results | Decision D4. The chapter can be built with the results frame reserved; the reserved frame is the last thing filled. |
| B2 | **Failure gallery, ten items** in mechanics, concrete or fluids | Ch 5 | Accrues over weeks. Aim at the confabulation band. The invented-code-clause item stays out of the ten the room grades together. |
| B3 | **Position-curve licensing decision** | Ch 5 | Empirical data that cannot be computed, traced or generated. Either cite and describe the shape without reproducing the figure, or find an openly licensed version. **This is a ruling, not a task.** |
| B4 | **Injection demo assets**, on an isolated machine | Ch 6 | Re-test in delivery week; behaviour changes between versions. Nothing in `assets/injection-demo/` is executed from here. |
| B5 | **Antigravity working configuration** | Ch 12 | What is actually invoked, and how results come back. |
| B6 | **Journals the group publishes in** | Ch 18 | ASCE likely primary. Generic summaries will not do — the chapter needs current disclosure policies. |
| B7 | **Local machine reachable from the training room** | Ch 13 exercise | If not, that chapter becomes an instructor demo. |
| B8 | **Two animation captures** (Ch 1 frame 17, Ch 2 frame 2) | Ch 1, 2 polish | Slot F, 1600 × 422 px. Slots are reserved and dimensioned. |
| B9 | **Tokeniser capture** | Ch 1 frames 9, 10 | Both frames currently say SCHEMATIC. |
| B10 | **Console accounts decision** (~$5 each) | Ch 13 second exercise | $25–30 call, not a cost question. |

**B1–B4 are the ones that gate whole chapters.** B5–B10 gate a frame or an exercise.

---

## 5. Production order

Ordered by what is unblocked today, then by what the thread map needs earliest.

### Wave 1 — unblocked now, starts immediately

| Chapter | Why now | Reserved |
|---|---|---|
| **4 — Measurement** | Chapter 3 hands it three named debts. Deep draft. | Results frame, pending B1 |
| **7 — Physical limits** | Deep draft, sources verified, COI known. Nothing outstanding. | — |
| **19 — Judgement** | Fully unblocked, and it is the course's closing argument. Building it early tells us what everything else is aiming at. | — |
| **17 — Critique** | Unblocked. Must be built alongside a duplication ruling against Chapter 3. | — |
| **9 — The agent** | Unblocked. Needs the fresh-versus-contaminated-session demo. | — |

### Wave 2 — unblocked once B1–B4 clear

| Chapter | Waiting on |
|---|---|
| **5 — Intrinsic failure** | B2 and B3 |
| **6 — Extrinsic failure** | B4 |

### Wave 3 — version-fragile, written late by design

| Chapter | Note |
|---|---|
| **10 — Memory**, **11 — Orchestration**, **13 — Access** | Facts expire. Written together so one re-fetch sweep covers them. |
| **12 — Extension** | B5 |

### Wave 4 — Part IV, thin drafts, blocked on facts about the group

| Chapter | Note |
|---|---|
| **14 — Literature**, **15 — Production**, **16 — Code and numerics** | Chapter 15 gains material from the Beamer reversal — the toolchain is now its own demo. |
| **18 — Governance** | B6 |

---

## 6. Do this before Wave 1: the cross-chapter pass

The checks below cannot be done inside a single chapter, and doing them after fifteen chapters are
built means correcting fifteen chapters. One pass, one document, delivered before any rebuild.

1. **Thread obligations.** Five threads, each with an introduce / develop / close station across
   named chapters. Confirm Chapters 1–3 delivered theirs, and list what each remaining chapter owes.
   Chapter 3 currently hands three things forward by name; nothing has checked that the receiving
   chapters accept them.
2. **The cost-versus-accuracy firewall.** Hard rule 3 calls conflating these *the single most likely
   error in this project*. It spans Chapters 5, 7 and 13. Check each in the same sitting, because the
   error is invisible from inside one chapter.
3. **Duplication.** Finding A7 says the evidence-grading lesson is taught five times and has
   saturated. Chapter 3's verdict-versus-analysis material may duplicate Chapter 17. Chapter 5's
   truthfulness material may duplicate Chapter 14. Rule on each: reinforcement or cut.
4. **What Chapter 8 was carrying.** Architecture says the memory-gap point moved to Chapter 1 and
   Chapter 10's opening. Verify both landed rather than assuming.
5. **The three standing course-level gaps** from the premise review: the audience's own experimental
   data never appears (A5); version control is assumed by three chapters and taught by none (A6);
   images are now covered in Chapter 3 but Chapters 14 and 15 should pick them up (A4).
6. **Stale premise verdicts.** The premise review predates the Chapter 1–3 rebuilds. Mark what the
   rebuilds have already answered so dead findings are not carried forward.

---

## 7. Definition of done — rewritten for Beamer

All nine, before a PDF is handed over. Items 1–5 are mechanical and gate the build.

1. `slides/beamer/NN-short-name.tex` builds through `build.sh` with **0 LaTeX errors**.
2. **0 overfull vboxes.** An overfull vbox is a frame running into the chevron footline.
3. `check-frames.py` passes: every frame carries a footer, every citation key resolves and is `[V]`.
4. Every figure lands inside the **3.4:1 to 4.7:1** aspect band, or is listed in `EXEMPT` with a reason.
5. PDF stamped with source hash and frame count, and committed.
6. **Term audit** written to `curriculum/chNN-term-audit.md`: every technical term, the frame that
   defines it, the inherited terms, the evidence balance, and the checks actually run with their
   outcomes.
7. **Thread map re-read**, and the chapter confirmed to pick up and hand off what `architecture.md`
   says it should.
8. **Units and sign conventions** annotated in the source for every physical quantity.
9. **A written statement of what was not done** — the case skipped, the check not run, the source
   not re-fetched, the frame left reserved.

---

## 8. Rating axes

Four axes, scored independently. **Budget is deleted**; a chapter is never marked down for length.

| Axis | Fails when |
|---|---|
| **Correctness** | A claim is wrong, or an equation drops a unit or a sign |
| **Evidence discipline** | A non-`[V]` source reaches a slide, an `[E]` tag implies a citation exists, or a source is stated more strongly than it supports |
| **Fit** | The chapter does not pick up or hand off its threads, or duplicates a neighbour without ruling that the repetition is deliberate |
| **Coverage** | The chapter does not deliver what the thread map and the brief say it delivers |

---

## 9. The annotation round trip

**Handover.** Each finished chapter produces `slides/beamer/NN-short-name.pdf`, committed, and a
copy placed where the instructor collects them. Alongside each PDF, a short **watch-list**: not a
summary, but the three or four decisions in that chapter I am least sure about. Chapter 1's round
showed the annotations that changed the most were on decisions I had made silently.

**Version safety.** Every PDF carries a stamp in `/Info/Keywords` — source hash plus frame count.
On intake I read the stamp back and confirm the annotations refer to the build in the repository.
An annotation against a superseded build is caught here rather than applied blind.

**Intake.** Annotations come back as a batch. For each one I record: what was annotated, what I
changed, or — where I disagree — the reason, stated once. Chapter 1 established that this is
worth doing explicitly; two of the instructor's annotations there were right and one of my
objections was, and neither would have been visible without writing both down.

**Disagreements go in the decision record**, tagged with the graphify header so the reasoning is
traversable later rather than buried in a diff.

---

## 10. Risks

| Risk | Mitigation |
|---|---|
| Fifteen chapters built on an approach not validated at scale | Wave 1 is five chapters, and it deliberately spans a deep draft, a thin draft and a derivation-heavy one. If the approach is wrong, it shows there. |
| Evidence that will not verify | The four low-citation chapters (4, 16, 17, 19) get their sourcing pass **before** their slide pass, not after. |
| The instructor becomes the serial bottleneck | §4 exists for exactly this. Every blocking item is listed once, now, rather than discovered chapter by chapter. |
| Thread promises break across fifteen chapters | Thread check is gate item 7, not a final review step. |
| ~140 figures is the real workload and gets underestimated | Figures are costed per chapter at review time, before the deck is written. |
| Version-fragile facts go stale between build and delivery | Flagged per frame; one re-fetch sweep in delivery week across all chapters. |

---

## 11. What this plan does not cover

- **Pass criteria for the Chapter 4 cases.** Deferred by the instructor and still deferred.
- **The Chapter 2 rating exercise at n=6.** `assets/rating-exercise/README.md` still assumes a room
  large enough to produce a distribution. The rescope is decided and written down in the production
  plan; it has not been applied to the file.
- **Per-chapter minute budgets.** Deliberately absent.
- **Whether the deck is distributed beyond the group**, which affects how carefully the synthetic
  Chapter 2 material must be scrubbed.
- **Any execution.** This plan orders and gates the work; it does not do it.

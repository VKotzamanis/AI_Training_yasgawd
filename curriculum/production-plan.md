# Production Plan

**Goal:** Take nineteen chapter briefs to a delivered three-session deck, one chapter at a time, with a review gate between each.

**Approach:** Chapters are categorised by what blocks them, not by teaching order. Production order is therefore not chapter order. Three items accrue over weeks and start immediately regardless of which chapter is being written.

**Companion to:** `architecture.md` (sequence and threads), `chapter-briefs.md` (content per chapter), `../DECISIONS.md` (what is locked and open).

---

## 0. Applied this session

| Decision | Applied to |
|---|---|
| D1 — five cases, not ten | `chapter-briefs.md:91` |
| D2 — A-vs-A null strip added | `chapter-briefs.md:91` |
| D3 — erratum heading corrected | `references.md:118` |
| D4 — instructor runs the eval in advance | recorded here, §5 Ch 4 |
| D5 — run graphify | **failed**, see §7 |
| Spikes A and B | **both pass**, see `../slides/README.md` |
| Worksheet stress test | 3 adversarial reviews; 11 defects fixed in `../assets/eval-worksheet/README.md` |

---

## 1. The domain correction

<!-- decision: shared-vs-individual-domain | status: adopted | supersedes: rating-exercise-wave-energy-only -->

**New fact:** the room is a mixed civil and environmental cohort. Most know structural engineering. Not all know wave energy.

This overturns a rule currently marked non-negotiable in `../assets/rating-exercise/README.md`: *"Both responses must be about wave energy conversion, PTO mechanisms, or experimental testing."*

The rule's own stated reason is what kills it. The file argues that an audience cannot judge truthfulness on a domain it does not know, and will grade fluency, structure and confidence instead, because that is all it can see. Applied to a mostly-structural room, that argument now points away from wave energy. **The principle survives intact; the instance was wrong.**

**The correction — two tiers, currently conflated into one.**

- **Shared material**, which the whole room grades together, sits in the *intersection* of the room's competence. The instructor states that intersection as **mechanics, concrete and fluids**. Design codes and standards are *not* in it — an earlier draft of this section assumed they were, on the strength of a structural plurality, and that was wrong: a plurality is not the intersection. Affects the Chapter 2 rating exercise, the Chapter 4 results slide, the Chapter 5 failure gallery.
- **Individual material**, which each attendee runs alone, stays in *that attendee's own* domain. Affects the pre-work problem, the Chapter 4 take-home template, the Chapter 14 literature exercise, the Chapter 16 code exercise.

The instructor's wave-energy work does not disappear. It becomes the worked instance — *here is mine, filled in; now fill in yours* — which is what a template is for, and which is honest about who graded what.

**Files this touched — all corrected 2026-08-19.** `../assets/rating-exercise/README.md` (the non-negotiable and the planted-error guidance), `../assets/failure-gallery/README.md` (the coefficient item, plus the code-clause demotion), `../curriculum/chapter-briefs.md` (Ch 1 tokeniser demo, Ch 2 non-negotiable, Ch 5 coefficient), `../references.md` (Ch 1 demo, Ch 2 synthetic rubric and exercise), `../CLAUDE.md` (sign-convention rule broadened beyond wave and hydrodynamic quantities), `../START_HERE.md` (the sample prompt).

**An earlier version of this list was wrong in both directions.** It named `../DECISIONS.md` item 3 and `../README.md`, neither of which carries the assumption — both already say "this group's domain" and "their own data", which are neutral. And it missed `chapter-briefs.md`, `CLAUDE.md` and `START_HERE.md`, which do. The list was written from memory of the files rather than from a grep. Four became six.

**Precondition — resolved 2026-08-19.** Five to six attendees. Shared competence: mechanics, concrete, fluids. This closes `../DECISIONS.md` open item 5 for content purposes and answers two of its logistics questions outright: pairing is viable when someone hits a usage limit, and item 8 (console accounts at roughly $5 each) is a $25–30 decision rather than a real cost question.

**The size has a second consequence.** Six raters is not a distribution. See §5, Chapter 2.

**One thing this makes easier.** `../DECISIONS.md` open item 7 guesses that ASCE matters most for Chapter 18. A structural plurality makes that guess much more likely correct.

---

## 2. Chapter categories

Categorised by what has to exist before a slide can be written.

| Category | Blocked by | Chapters |
|---|---|---|
| **A — Citation-bound** | `references.md` verification | 1, 2, 5, 7, 8 |
| **B — Demonstration-bound** | working software, and facts that expire | 9, 10, 11, 12, 13 |
| **C — Artifact-bound** | a built exercise with lead time | 2, 4, 6 |
| **D — Policy-bound** | external facts about the group | 14, 15, 16, 17, 18, 19 |

**Chapter 2 is the only chapter in two categories.** That is the diagnosis of its 105–115 minute overrun: it is not bad estimating, it is one chapter carrying two production loads. The 2a/2b split separates them cleanly — 2a is category A, 2b is category C.

**Category B inverts the natural order.** Those chapters teach in the middle of the course and must be written last, because their facts expire. `../DECISIONS.md` item 6 requires re-checking version-dependent facts in the week before each session; writing them early spends the work twice.

---

## 3. The accrual track — starts now, runs in parallel

Three items cannot be produced in a sitting. They start immediately, independent of which chapter is being written.

| Item | For | Why it accrues |
|---|---|---|
| Failure gallery, ten items | Ch 5 | `../assets/failure-gallery/README.md` says collect over the weeks before delivery. Aim at the confabulation band per findings §11. **Retarget to the shared domain** — see §1. |
| Eval runs, five cases × conditions | Ch 4 | D4 puts these on the instructor in advance. Needs model time, not writing time. |
| Injection demo | Ch 6 | Needs an isolated machine, and re-testing in delivery week because the behaviour changes between versions. |

---

## 4. Production order

**Spikes first. Neither is a chapter.**

- **Spike A — Chapter 7's hardest derivation, stepwise, in Slidev.** Reversal trigger 1. Half a day, timeboxed separately.
- **Spike B — citation footer plus the `[U]` build check.** Reversal trigger 2. Timeboxed separately from A. `slides/README.md` currently bundles these into one task; if the bundle overruns you cannot tell which trigger fired.

**Then chapters, in this order:**

**Revised 2026-08-19. The previous order put Chapter 4 first and stalled, because Chapter 4 needs the instructor's five cases and nothing else could start behind it. Order by what is unblocked, not by what is most valuable.**

| # | Chapter | Status | Needs from the instructor |
|---|---|---|---|
| 1 | **1 — Substrate** | **Done.** 15 slides, 2 computed figures, PDF committed | Two captures: tokeniser screenshots, temperature demo |
| 2 | **7 — Physical limits** | **Done.** 18 slides, PDF committed. Two brief claims corrected against verified sources | Nothing |
| 3 | **3 — Control** | **Next.** Unblocked | Nothing |
| 4 | **8 — Brain and model** | Unblocked, but **both primary citations are unverified and load-bearing** | Nothing; verification is mine |
| 5 | **5 — Intrinsic failure** | Writable except the position curve | Failure gallery accrues alongside |
| 6 | **19 — Judgement** | Unblocked | Nothing |
| — | **4 — Measurement** | **Blocked** | The five cases and their pass criteria |
| — | **2a / 2b** | **Blocked** | The split decision |
| — | **6 — Extrinsic failure** | Blocked | Isolated machine for the injection demo |
| — | **9–13** | Deferred by design | Version-fragile; write last. Ch 12 needs the Antigravity config |
| — | **14–19** | Blocked | Which journals the group publishes in |

Six chapters of runway exist without a single further answer. Chapter 3 sits before Chapter 4 in production and before it in teaching; Chapter 4 needs Chapter 3's *inventory*, which is already in the brief, not its slides.

## 4a. Figures — how they get made

<!-- decision: figure-generation-method | status: adopted | supersedes: none -->

Three kinds, and they are not interchangeable.

- **Computed figures** — anything with an equation behind it. A committed Python script under `../assets/figures/` writes the PNG. The script is the source of truth and the figure can be regenerated and audited. Where a figure needs input values that are not measured, those values are labelled illustrative *on the figure* and the transform applied to them is exact. Nothing is traced from a source figure.
- **Conceptual diagrams** — Mermaid, inline in the slide. Version-controlled text, editable, survives PDF export, no binary to keep in sync.
- **Generated imagery** — available via `agy` (Nano Banana), verified working 2026-08-19. **Not used for technical content.** A generated diagram cannot be audited, cannot be regenerated deterministically, and carries no provenance, which is the wrong trade in a course that spends three sessions on verification. Reserved for decorative section dividers if wanted at all.

**The unsolved one.** Chapter 5's position curve is empirical data from a published source. It cannot be computed, cannot be traced, and must not be generated. Either the chapter cites the source and describes the shape without reproducing the figure, or an openly licensed version is found. Decide before Chapter 5 is drafted.

---

## 5. Per-chapter corrections

Only chapters where the brief is now wrong or thin. Everything not listed stands as written in `chapter-briefs.md`.

**Ch 1 — Substrate.** `../references.md` Chapter 1 specifies a tokenizer demo on "a MATLAB snippet and a wave-energy abstract." Change the abstract to one from the shared domain. The MATLAB snippet stands.

**Ch 2 — Formation.** Still blocked on the split. Two additions once it is settled: the thread map in `architecture.md` names "Ch 2" as the introduction point for three threads, and those entries must resolve to 2a or 2b — the file the split was chosen to protect still needs editing. And the synthetic rubric moves to the shared domain per §1.

**Ch 2 — the exercise at n=6.** Two steps in `../assets/rating-exercise/README.md` assume a room large enough to produce a distribution. Step 2 says *collect and show two distributions*; six points is a tally, not a distribution, and calling it one on a slide fails the chapter's own standard. Rescope it: show the tally, name it as an anecdote, and hand the question forward — *how many raters would we need before this meant anything?* — which gives Chapter 4 a motivating example it currently lacks and adds a thread link the architecture does not yet have. Step 5 pairs raters to swap sheets; at five attendees one group of three is needed, and an unwritten rule becomes a live stumble. The strongest reveal in the exercise survives untouched, because it is a count and not a distribution: *how many of you marked the fabricated citation unassessable rather than false?*

**Ch 3 — Control.** Framing change. The role/persona and requesting-reasoning segments are no longer techniques to adopt; they are the claims Chapter 4 puts on trial. Write them as open questions the next chapter settles, or Chapter 4 spends its first ten minutes undoing Chapter 3.

**Ch 4 — Measurement.** Five cases, A-vs-A null strip, instructor-run. Cases must be gradeable by the room when the results slide goes up, or the demo reduces to *trust me* — which fails the chapter's own standard. Pass criteria deferred by the instructor and are the last thing written.

**Ch 5 — Intrinsic failure.** Failure-gallery mix changes: the wrong-hydrodynamic-coefficient item moves to mechanics, concrete or fluids. **The invented-code-clause item is demoted, not promoted.** An earlier draft of this plan argued it got stronger with a structural cohort; the stated intersection does not include codes, so a fabricated clause is checkable by some of the room and not all of it — which is the failure mode §1 exists to prevent. Keep it as a gallery item if the instructor wants it, but not as one of the ten the room grades together. The position curve remains the load-bearing figure and remains an unresolved citation.

**Ch 9 — The agent.** New demo, from the instructor's own answer on session hygiene: run the same case in a fresh session and in a contaminated one, to show context carrying across a topic switch. Belongs to the memory-and-context thread at its "management" station.

**Ch 15 — Production.** Contingent value: pandoc-to-Beamer was the rejected alternative that would have doubled as this chapter's demo. If Slidev reverses on trigger 1 or 2, Chapter 15 gains material rather than losing it.

**Ch 18 — Governance.** ASCE now the likely primary target. See §1.

---

## 6. The review gate

One chapter per cycle. Produced, rated, corrected, then the next.

**Definition of done — all seven, before rating:**

1. `slides/NN-short-name.md` builds without error
2. PDF exported and committed — the standing hedge, so a presentable deck always exists
3. `npm run check:cites` passes; no `[U]` key on any slide
4. Thread map re-read; the chapter picks up and hands off what `architecture.md` says it should
5. Units and sign conventions annotated on every physical quantity
6. Facilitator notes carry the questions the chapter will provoke, including the ones it cannot answer
7. A written statement of what was *not* done — the case skipped, the check not run, the assumption left standing

**Rating axes.** Four, scored independently, because a chapter can be correct and still not fit.

| Axis | Fails when |
|---|---|
| **Correctness** | A claim is wrong, or an equation drops a unit or a sign |
| **Evidence discipline** | A `[U]` reaches a slide, an `[E]` tag implies a citation, or a source is stated more strongly than it supports |
| **Fit** | The chapter does not pick up or hand off its threads, or duplicates a neighbour |
| **Budget** | It does not fit its minutes |

Correction happens in the same cycle. The next chapter does not start on an unrated one.

---

## 7. Open blockers

| # | Blocker | Blocks | Status |
|---|---|---|---|
| 1 | Chapter 2 split undecided | Ch 2 slides | Unchanged. Does not block starting at Ch 4 |
| 2 | ~~Slidev spikes not run~~ | — | **Cleared 2026-08-19.** Both pass; no reversal trigger fired. Versions pinned |
| 3 | ~~Attendee composition~~ | — | **Resolved 2026-08-19.** 5–6 attendees; mechanics, concrete, fluids |
| 4 | graphify needs an LLM API key | Decision traversal | Failed this session; 0 code files, 11 docs, 1 paper all need semantic extraction |
| 5 | Antigravity configuration | Ch 12 | Unchanged, `../DECISIONS.md` item 2 |
| 6 | Journals the group publishes in | Ch 18 | Unchanged, item 7 |

---

## 8. Not covered by this plan

Pass criteria for the Chapter 4 cases, deferred by the instructor. Per-chapter minute budgets, which exist only for Chapter 2. The Chapter 2 split. Anything requiring attendee composition, which is not yet known.

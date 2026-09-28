# Prior-review scope map

Written to let the nineteen upcoming chapter reviewers (running `RUBRIC.md`, classes
R/F/T/C/S) cite the existing pre-rebuild premise review instead of re-deriving what it
already covers. This is a scope map, not a review: it does not evaluate the nineteen
chapters and does not judge whether any prior finding is correct.

**Sources read in full.**
- `curriculum/peer-review-19-chapters.md` (~48K; cited below as **PR19**, by line number)
- `curriculum/review-ch02.md` (cited as **RC2**, by line number)
- `curriculum/review-ch03.md` (cited as **RC3**, by line number)
- `FOR-REVIEW/RUBRIC.md` (cited as **RUBRIC**, by section)

No other prior-review document (e.g. a per-chapter file for Chapter 1) was read for
this map and none is cited here.

---

## Part 1 — Class-mapping table

### 1a. The prior review runs at two different grains

`PR19` is a **premise-level** pass over all nineteen chapters: one verdict
(holds / holds-wrong-size / half-true / mis-scoped / not-a-chapter), then
Useful / Useless / Missing, per chapter (PR19 lines 216–800). It does not count
slides, footers, headlines, or banned constructions per chapter, and it does not
write a slide-by-slide Message.

`RC2` and `RC3` are **slide-level** rebuild reviews, and only for Chapters 2 and 3.
Each opens with a mechanical audit table (slide count, figures-per-slide, footers,
full-sentence-headline count, banned-construction count, term-audit status — RC2
lines 22–39; RC3 lines 20–42), then a proposed slide-by-slide restructure (RC2 lines
218–256; RC3 lines 157–185). This is much closer in granularity to what `RUBRIC`
asks a reviewer to do (topic ledger, per-slide Message, headline-as-assertion check).

**Consequence for the class map below:** overlap with R and F is strong for Chapters
2 and 3 specifically, because RC2/RC3 already did slide-level bookkeeping. For
Chapters 4–19, overlap with R and F exists only at the coarser, premise-level grain
that PR19 operates at — a new reviewer doing the slide-level R/F sweep on those
seventeen chapters is not duplicating prior slide-level work, because none exists.

### 1b. Class-mapping table

| RUBRIC class | Prior review's closest equivalent | Overlap | Grain |
|---|---|---|---|
| **R** — repetition / reopened topic | Cross-chapter redundancy findings: A7 "evidence-grading lesson taught five times" (PR19 lines 167–177); Ch8's motivating question already answered in Ch1 (PR19 lines 461–463); Ch15 "duplicates" Ch16 (PR19 lines 685–686) | Real, but at a different grain — see 1c | Cross-chapter, thematic. RUBRIC's R is a within-chapter, ledger-mechanical test (same topic-ledger row opened twice, or two slides with an identical Message) |
| **F** — flow / unclear intent | Premise-referent critique (Ch1's "It" never identified, PR19 lines 222–226); headline-as-topic-label audits (RC3 lines 27, 33–38); forward/backward-reference breaks (Ch2's rater has no face until slide 15, RC2 lines 95–98; Ch8's false claim that Ch1 defined attention, PR19 lines 491–494); sequencing-not-content openers (RC2 line 53–56; RC3 lines 54–57) | Strong, esp. Ch2/Ch3 | RC2/RC3 already do the per-slide Message test implicitly via the headline audit; PR19's version is premise-level only |
| **T** — technical inaccuracy | A3(a)/A3(b): two corrections against vendor documentation **fetched and logged the same day** (PR19 lines 93–130); unresolved numbers flagged but not adjudicated: Ch4 sign-test arithmetic (PR19 lines 842–845), Ch13's 1.7 kB/token figure (PR19 lines 631–635, 840–841) | Strong, and already carries a CONFIRMED/PLAUSIBLE-equivalent discipline | Per-claim, matches RUBRIC's grain directly |
| **C** — coverage / contract gap | Coverage half: dense — "used or implied, none defined" for Ch1's whole front half (PR19 lines 240–242); "system prompt" undefined through Ch2/Ch3 (PR19 line 282, line 310; RC2 line 176); "permissions" undefined until Ch9 (PR19 line 409). Contract half: **absent** — see 1c | Split — see 1c | Coverage instances are per-concept, matching RUBRIC's grain; the 5-field contract test has no precedent at all |
| **S** — style (S1–S4 only) | S3 (pretense over information) has direct precedent: A10's banned-constructions grep (PR19 lines 203–212), RC2's "This is the hinge of the chapter" (RC2 line 206), RC3's second-person dramatic address (RC3 lines 146–148), Ch19's closing line (PR19 lines 797–798). S1/S2/S4 — **no clean precedent found** | Split — see 1c | Where present, per-slide/per-sentence, matching RUBRIC's grain |

Two findings sit **outside** the five classes entirely and are not this rubric's
business to re-derive or re-litigate:
- **Premise/audience-fit verdicts** (half-true, mis-scoped, not-a-chapter) judge
  whether a chapter should exist in this form for this room — a curriculum-design
  question, not a per-slide content defect.
- **Course-design findings** A1 (session timing — superseded, PR19 lines 29–38), A2
  (no hands-on until Ch9), A6 (version control assumed, taught nowhere), A9 (figure
  coverage 2% vs. a 50% spec) are cross-chapter production-process findings, not
  per-chapter draft-content findings.

### 1c. Verifying the two "expected gaps," rather than assuming them

**C-contract: confirmed gap.** RUBRIC's C requires, at a component's definitional
slide, five mandatory fields — one-sentence definition, input→output signal
contract, necessity-on-removal, deployed capability, pipeline/stage location
(RUBRIC, class C). Nothing in PR19, RC2, or RC3 tests a definition against this
five-field list; "Missing" entries name concepts as *undefined*, never as
*under-specified against a fixed field set*. This gap is real for all nineteen
chapters — it is new work, not duplicated work.

**S: gap for S1/S2/S4, real overlap for S3.** RUBRIC's four style flags are not
uniformly untouched. S3 ("aphorism, dramatic fragment, or rhetorical repetition
standing where information should be") is functionally what the prior review's
"banned constructions" check already catches, with named instances and line
references (see table above). S1 ("explanation by subtraction") has one loose
analog — RC2 flags Ch2's opening as "a negation followed by an assertion" (RC2 line
53) — but that is a generic old-house-style rule, not RUBRIC's specific "X is not A.
It is B, B never defined" pattern, so treat it as adjacent, not confirmed. S2
("empty parallel") and S4 ("nonstandard term") have no instance in any of the three
documents; RC2/RC3 both log "term audit: none" for their chapters (RC2 line 35, RC3
line 31) as an open production item, which gestures at S4's territory without
addressing it.

**A further scope boundary worth flagging explicitly:** PR19's four largest
course-wide content gaps — image/file input (A4), the room's own experimental data
(A5), version control (A6), and low figure coverage (A9) — are absences of content
that is *never mentioned at all*. RUBRIC's C only fires on a concept a chapter
*uses but leaves undefined*, or an unpaid stated promise. A concept that is simply
never raised is invisible to a per-chapter draft rubric by construction. New
reviewers should not expect the rubric to surface A4/A5/A6/A9-style whole-course
gaps, and should not re-raise them chapter by chapter — they are already logged at
the course level in PR19 Part C (lines 806–824).

---

## Part 2 — Per chapter (all 19)

### 01-substrate
Premise graded **mis-scoped**: "It predicts the next fragment of text... over and
over" presupposes its subject — "It" is never identified (PR19 lines 218–226).
Missing: the entire front half — AI, LLM, model, parameters, weights, network,
training, inference, forward pass, "used or implied, none defined" (PR19 lines
240–242) — a course-anchoring C-class gap. The brief's "opens with: is this like a
brain?" device is named for outright deletion (PR19 lines 244–246), and a revised
premise is proposed (PR19 lines 248–250). Cross-cutting A8 (footer rule for
definitional slides, PR19 lines 179–190) and the Ch8 cross-reference note (attention
now defined here, PR19 lines 491–494) both anchor to this chapter. Already
flagged — cite, do not re-derive.

### 02-formation
Verdict **holds, wrong size** at the premise level (PR19 lines 256–286: strongest
premise in the course, two chapters' worth of material, eight minutes cuttable from
three named slides, missing pipeline diagram, "system prompt" undefined). Separately
covered at slide level by RC2 in full: mechanical audit shows zero figures across 27
slides and three banned constructions (RC2 lines 22–39); a full 36-slide restructure
is proposed (RC2 lines 218–256); six missing items are named, including an unshown
pretrained-model failure (RC2 lines 179–183) and an unused correction log (RC2 lines
169–174). Already flagged — cite, do not re-derive.

### 03-control
Verdict **holds** at the premise level (PR19 lines 289–316): best pedagogical device
in the course (the "maps to" line), missing file/image lever, missing model-choice
guidance, and a sourcing note that "eight of seventeen slides cite one vendor
documentation page" (PR19 lines 312–315). RC3's mechanical audit is headline-focused —
"10 of seventeen headlines are phrases rather than assertions" (RC3 line 27), backed
by a cited 79%-vs-69% recall figure for sentence vs. phrase headlines (RC3 lines
36–38) — a direct precedent for RUBRIC's per-slide Message test. Missing: a
prompt-anatomy diagram (RC3 lines 127–130) and a running example (RC3 lines 132–134).
Already flagged — cite, do not re-derive.

### 04-measurement
Verdict **holds** — "the highest-value chapter in the course for this audience"
(PR19 lines 322–323). Missing: the room running its own eval rather than watching
`TODO(instructor)` cases (PR19 line 336; cross-cutting A2, lines 78–91), a power-curve
figure (PR19 lines 338–339), and a stated next action for a "cannot tell" result
(PR19 lines 340–342). Part D records the sign-test/power arithmetic was not
independently recomputed and flags this as necessary before delivery (PR19 lines
842–845) — an explicit T-class item left at PLAUSIBLE. Already flagged — cite, do not
re-derive.

### 05-intrinsic-failure
Verdict **holds, wrong size** — three chapters under one number: mechanism (8
slides), long-context literature (8 slides), interpretability (4 slides) (PR19 lines
350–358). The long-context and interpretability blocks are both marked useless for
this room and compressible to about three slides total (PR19 lines 366–375); the
long-context material is separately named as the fourth, saturated instance of the
evidence-grading lesson (A7, PR19 line 170). Missing: a near-miss-citation slide (PR19
lines 378–380) and the A3(a) arithmetic correction — CONFIRMED against vendor
documentation fetched the day of the review (PR19 lines 99–113, 381–382). Already
flagged — cite, do not re-derive.

### 06-extrinsic-failure
Verdict **holds** — "the tightest premise in Session 1" (PR19 line 389). Missing: a
mechanism diagram (PR19 lines 404–405), a concrete demo still `TODO(produce)` (PR19
lines 406–408), and "permissions," used on the "what you can actually do" slide and
left undefined until Chapter 9 (PR19 line 409) — a direct C-class instance.
Cross-cutting A6 (PR19 lines 152–165) lists this chapter among those that assume
version-control context the course never teaches. Already flagged — cite, do not
re-derive.

### 07-physical-limits
Verdict **holds, wrong size** — "about twice the size its premise justifies" (PR19
line 417). Critical batch size, parallelism, the 6ND training accounting, and three
alternative substrates are named useless for this room, with the substrates flagged
as the fifth, unjustified instance of the evidence-grading lesson (A7, PR19 lines
167–177, 426–430). A sourcing problem is stated plainly: nearly every slide cites one
podcast transcript by a chip-company CEO with a declared, direction-matching conflict
of interest (PR19 lines 436–441). Recommendation: cut to about eight slides and move
to Session 2 beside Chapter 13 (PR19 lines 443–446). Already flagged — cite, do not
re-derive.

### 08-brain-and-model
Verdict **holds, and has the weakest claim on the room's time in the whole course**
(PR19 line 454), with a five-point case for cutting it (PR19 lines 459–469). **RULED
2026-08-20:** the chapter is dissolved; the three surviving points (PR19 lines
471–479) were relocated to Chapter 1, not Chapter 10 as the review originally
recommended (PR19 line 485), and `architecture.md` independently records the
chapter's status as "Appendix, not delivered." A cross-reference correction is
flagged either way: Chapter 8 claims Chapter 1 already defined attention (PR19 lines
491–494). Treat this chapter number as already resolved at the course-architecture
level. Already flagged — cite, do not re-derive.

### 09-the-agent
Verdict **holds** — "the best-shaped premise in Session 2" (PR19 line 502). Missing:
the recovery path — the chapter teaches reading a diff before approving it and never
teaches what to do about one approved in error (PR19 lines 513–515), tied to
cross-cutting A6, which calls this "the gap that will actually cost someone a day"
(PR19 lines 163–165). Already flagged — cite, do not re-derive.

### 10-memory
Verdict **holds** (PR19 lines 520–541). Useless: the cost equation
`cost ∝ N_file × T_turns`, criticized for dressing a trivial statement as physics in
a course that elsewhere teaches the room not to accept exactly that move (PR19 lines
533–537) — an S3-adjacent finding, though not a clean match to any single RUBRIC style
flag. Missing: the personal-vs-project-file conflict case (PR19 lines 539–540) and a
hierarchy figure (PR19 line 541). Per the Chapter 8 ruling, a three-slide
brain-analogy segment now opens this chapter (PR19 line 485). Already flagged — cite,
do not re-derive.

### 11-orchestration
Verdict **half-true, and the premise is doing public relations for the content**
(PR19 line 549), with a rewritten premise proposed (PR19 lines 552–553). Useless for
this room: subagent design, workflow authoring, and inspecting running work,
specifically because they consume the subscription usage the chapter itself says
orchestration exhausts (PR19 lines 560–564). No missing-content items are named — the
recommendation is to shrink to roughly fifteen minutes (PR19 lines 566–567). Already
flagged — cite, do not re-derive.

### 12-extension
Verdict **half-true** — the trust half is load-bearing, the protocol half is not
(PR19 line 575). Useless: the N-times-M interface-standard argument and a slide that
"names sampling, roots and elicitation and then says they are out of scope" (PR19
lines 584–586) — an F-adjacent finding ("a slide that announces its own irrelevance
should not be a slide"). Missing: a named reference-manager tool for Chapter 14 to
use (PR19 lines 588–589). A locked `DECISIONS.md` item on cross-provider retrieval is
challenged with three numbered points and explicitly left as the instructor's call
(PR19 lines 591–605) — a decision-validity question outside R/F/T/C/S entirely.
Already flagged — cite, do not re-derive.

### 13-access
Verdict **mis-scoped to the audience** — "most of this room will never hold an API
key" (PR19 line 613). Missing: what the room's actual subscription plan gives them
and what to do at the limit, named "the real gap" (PR19 lines 627–629). One
unresolved number: the 1.7 kB-per-token check, which "openly does not know whether
the figure is per layer or whole model" (PR19 lines 631–635) — an explicit T-class
item left unresolved, restated in Part D as needing a source re-read that was not
done (PR19 lines 840–841). Already flagged — cite, do not re-derive.

### 14-literature
Verdict **holds** — "the tightest one-sentence premise in the spine" (PR19 line
647). Missing: the A3(b) PDF-extraction correction, CONFIRMED against vendor
documentation fetched the day of the review (PR19 lines 115–126, 661); an
"understanding a paper" task named as "the actual first use" and currently absent
(PR19 lines 663–664); and a search-record slide for defensible screening (PR19 lines
665–667). Part D notes citations here were checked by tag, not against the original
sources (PR19 lines 836–839). Already flagged — cite, do not re-derive.

### 15-production
Verdict **half-true, and the weakest premise in the course** (PR19 line 675), with
three named problems: four of seven slides are not about AI at all (PR19 line
678–679); the premise never meets the objection that actually kills adoption —
collaborators' tracked-changes workflow (PR19 lines 681–684); and it duplicates
Chapter 16 (PR19 lines 685–686). Missing: figures, in a chapter that argues for
text-generated diagrams and "states 'This chapter has no figures of its own,' which
is close to self-refuting" (PR19 lines 692–693). Recommendation: cut to about fifteen
minutes or fold into Chapters 14 and 16 (PR19 lines 695–696). Already flagged —
cite, do not re-derive.

### 16-code-and-numerics
Verdict **holds** — "the closest chapter to the audience's daily work" (PR19 line
704). Missing: the audience's own experimental data, explicitly assigned here by
cross-cutting A5 ("Chapter 16 should absorb it and should get longer, not shorter,"
PR19 lines 142–150, 717–718) and a way out of the testing-slide circularity — "a test
written against a case with an independently known answer, or against a conservation
law, is checkable without reading the test's logic" (PR19 lines 720–722).
Recommendation: expand, taking time from Chapter 15 (PR19 line 724). Already
flagged — cite, do not re-derive.

### 17-critique
Verdict **holds, and the chapter's real payload is buried** (PR19 line 732).
"Buried": the language-support/disclosure-boundary slide, called "plausibly the
highest-frequency benefit in the entire course" but sitting as one slide between two
referee-report slides (PR19 lines 740–743), with promotion recommended. Missing: the
reverse direction — using the tool to check whether the reader has understood a
referee's objection, distinguished from drafting the reply (PR19 lines 745–747).
Already flagged — cite, do not re-derive.

### 18-governance
Verdict **holds. Well structured for a chapter blocked on missing inputs** (PR19
line 755), with the block itself correctly identified as clearable only by the
instructor. Missing: "the student-facing half" — thesis regulations, examination
boards, viva questions, and doctoral-school declarations — against the chapter's
current journal/publisher-only framing, named "the wrong first ring" for a PhD
audience (PR19 lines 768–771). Already flagged — cite, do not re-derive.

### 19-judgement
Verdict **not a chapter** — "the brief itself says 'one slide, held in the head.' It
is one slide, a sixty-minute capstone and a round-robin" (PR19 lines 779–781).
Useless: only the framing as a numbered chapter, which "costs the capstone room"
(PR19 line 793); the five-test content and the capstone itself are called out as
strong (PR19 lines 783–791). One prose item: the closing line "That is the trade you
have actually made this term" is independently named by cross-cutting A10 as one of
the handover's own cited banned constructions, still present in the final slide of
the course (PR19 lines 203–212, 797–798) — a CONFIRMED S3 precedent. Already
flagged — cite, do not re-derive.

---

## What this map does not do

- It does not evaluate any of the nineteen chapters against `RUBRIC` and does not
  assign any chapter an R/F/T/C/S finding of its own.
- It does not judge whether any PR19/RC2/RC3 finding is correct, including the two
  CONFIRMED technical corrections (A3(a), A3(b)) — "confirmed" here reproduces the
  prior review's own tag, not an independent check run for this map.
- It does not read or characterize any prior-review document beyond the four listed
  at the top (in particular, it does not open or cite `ch01-peer-review.md`, which
  exists in the same directory but was outside this task's assigned reading list).
- It does not resolve the granularity mismatch it identifies in §1a — whether the
  seventeen chapters lacking a slide-level rebuild review need one before their
  RUBRIC pass is a scheduling question for the instructor, not this map.

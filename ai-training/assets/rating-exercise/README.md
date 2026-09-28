# Live rating exercise — Chapter 2

The centrepiece of Chapter 2. Attendees rate two responses against a rubric, then review each other's ratings. It teaches the annotation layer by having them occupy it rather than hear it described.

**Status:** to be produced. Nothing here exists yet.

---

## Non-negotiable: the material is domain-specific

Both responses must be about **mechanics, concrete or fluids**. Not coding, not general knowledge, not anything borrowed.

That is the stated intersection of what all five or six attendees know. Wave energy, PTO and experimental testing are the instructor's field and are known by *some* of the room — and *some* is the failure condition here, because the raters who cannot check the physics will grade fluency instead, which is the exact behaviour this exercise exists to expose. The rule below is unchanged and is what forced the domain to change.

**An audience cannot judge truthfulness on a domain it doesn't know.** Given two responses about an unfamiliar topic, people grade fluency, structure and confidence — because that is all they can see. The whole lesson depends on the room being able to catch a physical error, and then noticing that they nearly didn't.

Secondary benefits: the disagreement that surfaces is real and specific rather than borrowed, and nothing requires sourcing.

---

## Materials to produce

| Item | Notes |
|---|---|
| The prompt | One realistic question a PhD student would actually ask. Include at least two distinct instructions so instruction-following is gradeable. |
| Response A | Correct, terse, badly formatted, quietly drops one part of the instruction. |
| Response B | Fluent, well-structured, confident, correctly formatted. Contains one subtle physical error and one fabricated citation. |
| Rubric card | One page. The synthetic instrument: dimensions, scale, and a one-line definition of each dimension a rater can actually apply. Truthfulness carries a *cannot assess* band with a stated time box, and the card names which source types count for a factual challenge. |
| Tally sheet | Per-rater scores per dimension, an overall preference, and a confidence self-report per task. Collected, because the spread is the teaching material — and because score against confidence is a second thing worth showing. At five or six raters both are tallies, not distributions; see the run order. |
| Rewrite checklist | Half a page, for the optional rewrite step. Five or six surface-style edits stated as mandatory corrections, in the imperative, with no explanation of why. The absence of explanation is the point. |
| Facilitator answer key | What is wrong in B, what is missing in A, and the defensible grade on each axis. Includes the expected *cannot assess* outcome on the fabricated citation. |

**Design principle: make the axes conflict.** If one response is better on everything, there is nothing to learn. A should win on truthfulness and lose on formatting, verbosity and instruction following. B should win on everything except the thing that matters most.

**Design decisions carried over from real instruments** (see `../../curriculum/ch02-annotation-findings.md`). Each is tagged with how many of the five reviewed documents actually contain it. Pedagogical value and evidential weight are different things, and the facilitator should not claim the second while relying on the first.

- **Include at least one non-directional axis.** Verbosity is a descriptive spectrum, not a quality scale — a high score is not a good score. **One document of five.** Keep it: it teaches more than any other single design choice and will provoke argument in the room. But do not say real instruments do this as a matter of course. They do not. Say that one instrument did, and that it warned its raters twice.
- **Prescribe the justification format.** A fixed opening phrase from a closed set, word bounds, no first person, no cross-reference between the two responses. **Four of five**, and far more prescriptive than v2 assumed — see the rewrite step below. Attendees feel the constraint shaping what they write, which is precisely how house style enters a model.
- **Require source plus excerpt for any factual challenge.** Same standard as Chapters 4 and 14. **Three of five** hold a source-quality standard; only one requires a minimum count. Name the acceptable source types on the rubric card, as real instruments do.
- **Collect a score *and* a written rationale, then check whether they agree.** **One document of five** lists score-versus-justification mismatch among the errors its reviewers most often catch, and it gives no incidence figure. Keep the exercise step — some fraction of the room will contradict themselves, and showing them their own mismatch is what makes Chapter 5's material on unfaithful reasoning land. Present the industry claim as one vendor's error list, not as a measured rate.
- **Treat adjacent-band disagreement as acceptable.** **One document of five.** Still a defensible rule for the reviewer round, and still the cleanest way to separate signal about the rubric from noise about the rater. Attribute it to one instrument rather than to "real QC."

**New decisions from documents D and E:**

- **Collect a confidence self-report alongside every score.** One instrument asks the rater, after each task, how confident they are, with an option meaning *unsure because this was a subjective judgement call*. One extra column on the tally sheet. It costs nothing and it sharpens the reveal enormously: the facilitator can show that the raters who were most confident about preferring B were not the ones who caught the error. Confidence and correctness coming apart in the room is the same lesson as calibration failure in Chapter 5, and they will have generated the data themselves.
- **Add a *cannot assess* band, with an explicit time box.** One instrument's truthfulness scale carries a band for claims the rater could not check, triggered when proper verification would take longer than about fifteen minutes. Reproduce it: tell the room that if verifying a claim would take more than two minutes at their desks, they must mark it unassessable rather than guess. The fabricated citation in B is the target. Most of the room will mark it unassessable rather than false — which is the honest outcome, is what a production rater would do, and is exactly how a fabricated citation survives into a dataset labelled as acceptable. This is the strongest single addition available and it costs no extra time.
- **Do not accept a tie.** Two instruments make equivalence uncollectable, by opposite mechanisms: one uses an even scale so no tie exists, the other allows a midpoint but rejects the task when it is used without a named error. Adopt the second: a rater who marks no preference must name a truthfulness or instruction-following failure, or re-rate. Reproduces the real constraint and prevents the room from avoiding the decision the exercise exists to expose.
- **Add a rewrite step (optional, costs time).** In one instrument the rater does not stop at rating — they repair the response they preferred until it is correct, fixing every identified error, and *the repaired response is the collected artifact*. The minor-rewrite rules amount to a style specification: strip pleasantries, strip assistant self-reference, strip closing offers of help, unbold colons, fix list types. Having attendees spend five minutes editing Response A against a short version of that checklist is the most direct way to teach where model voice comes from — they will be producing it. See the run order for where it fits and what it displaces.

---

## Run order

1. **Rate (8 min).** Distribute prompt, both responses, rubric card, tally sheet. Rate individually, in silence, under visible time pressure. The time pressure is part of the design — it reproduces the condition under which real rating happens. State the two-minute verification box and the *cannot assess* band before starting; state that no preference requires a named error. Confidence is recorded per task, on the same sheet, before anything is revealed.
2. **Collect and show the tally (3 min).** Put the preference count on screen, then confidence beside it. **Call it a tally, not a distribution.** Five or six raters is not a distribution, and presenting six points as one fails the standard this course spends three sessions teaching. Say the number out loud — *four of six preferred B* — and then ask the question that hands the room to Chapter 4: **how many raters would we need before this meant anything?** Nobody in the room will know. That is the point, and it is the cheapest possible setup for the measurement chapter.
3. **Reveal (5 min).** Name the physical error and the fabricated citation. Invite re-grading. Ask how many marked the citation unassessable rather than false, and point out that this is the correct action under the instrument and that it is also how a fabricated citation passes into a dataset as acceptable.
4. **Name what happened (5 min).** Under mild time pressure, competent engineers rewarded verbosity, confidence and formatting over correctness — and were most confident where they were most wrong. That preference is a reward signal. That signal is where sycophancy, verbosity bias and confident fabrication come from — forward reference to Chapter 5.
5. **Reviewer round (10 min).** Pairs swap tally sheets and audit each other against the rubric. **With an odd number in the room, make one group of three and have them rotate sheets rather than swap** — decide this before the session, not in front of it. Where do two competent raters diverge, and is the rubric or the rater at fault? This is the attempter/reviewer split, occupied rather than described.
6. **Adjudicate (4 min).** Facilitator gives the defensible grade and reasoning per axis, including where the rubric itself is ambiguous.

Roughly 35 minutes. Steps 1–4 carry the lesson; if the session is running late, cut step 5 before cutting anything else.

**Optional step 7 — rewrite (5 min, and it does not fit inside 35).** Hand out the rewrite checklist and have attendees edit Response A until it is correct and compliant. Then say what they have just done: produced the artifact that gets collected, in a voice specified by someone else, without being told why. If the session cannot absorb 40 minutes, run the checklist as a facilitator demonstration in step 4 instead — reading five imperative style rules aloud and asking the room where they have seen that voice before costs ninety seconds and lands most of the point.

---

## If the room grades A higher

Not a failure — use it. Ask what they used to decide, and whether they would have caught the error at 2am on the fortieth pair of the session. The point survives: the rubric is only as good as the attention available to apply it.

---

## Verification requirement

**The instructor must verify the physics before delivery.** The planted error in B has to be subtle enough to slip past a first reading and unambiguous enough to be indefensible once named. If it is too obvious the exercise collapses; if it is arguable, the adjudication turns into a debate about the error instead of about rating.

**Choosing the error, from `../../curriculum/ch02-annotation-findings.md` §11.** One vendor instructs contributors to aim prompts at a specific band of model knowledge: not common knowledge, where the model is reliable, and not genuinely obscure material, where it correctly declines, but the band between, where it believes it knows and confabulates. Use the same rule here. The planted physical error should be the kind a capable model would actually produce on this group's own literature — a plausible-sounding claim about a material property, a flow-regime boundary, or a section capacity — rather than an error invented for the exercise. It makes the response realistic, and it means the room is catching a failure mode they will meet again on Thursday.

Rehearse on two colleagues who are not attending.

---

## Sourcing

Written from scratch. No examples, paraphrased or otherwise, from any annotation manual or vendor document. The rubric card is an original synthetic instrument informed by published annotation guidelines — see `../../references.md`, Chapter 2.

**This applies with particular force to the rewrite checklist.** One vendor document contains a banned-phrase list of dozens of entries. Do not copy it, do not paraphrase it, and do not reconstruct it from memory. Write five or six rules from scratch describing surface behaviours the room can observe in any assistant output. The teaching point is that such a list exists and is enforced; the specific entries are the vendor's document and stay in it.

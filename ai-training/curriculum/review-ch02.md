# Chapter 2 — critical review before rebuild

Written 2026-08-20, the same pass Chapter 1 got: read the deck against its own premise, the
material behind it, and the standards that have been ruled on since it was written. The instructor
has not annotated this chapter, so nothing here reports his judgement — it is mine, and the parts
he should overrule are marked.

**What I read.** `slides/02-formation.md` in full, `curriculum/ch02-annotation-findings.md`
including §0 and §13, the Chapter 2 brief, `assets/rating-exercise/` and the thread map.

---

## Summary

The premise holds and the material is the strongest in the course. The chapter's problems are
structural rather than substantive: it is a lecture with an appendix bolted on, the appendix
contains its best evidence, and the reason the appendix exists has just been removed by a ruling
made for other purposes.

---

## The mechanical audit

Measured, not asserted.

| | Chapter 2 | Standard now in force |
|---|---|---|
| Slides | 27 | — |
| Slides with a figure | **0** | every slide |
| Slides with a footer | 10 | every slide |
| Banned constructions (§5.3 grep) | 3 — one on a slide, two in notes | zero |
| House-style banned words | 0 | zero |
| Rhetorical-question headings | 0 | zero |
| Running example | none | one per chapter |
| Term audit | none | required to finish a chapter |

Zero figures across twenty-seven slides is the largest single defect, and the chapter is the worst
case in the course for it: it describes a five-stage pipeline, which is the definitional case where
`research-slide-design.md` makes a diagram mandatory rather than optional.

---

## The premise

**"It behaves like an assistant because people rated outputs and it was optimised toward those ratings."**

**Holds, unchanged.** It is the tightest premise in the spine and Chapter 1 now hands off to it
directly — Chapter 1 closes on four open questions, the first being *"Nothing in scoring text makes
a thing that answers a question, follows an instruction, or declines a request. What was added?"*

**The opening slide does not answer it.** It currently restates it: *"Chapter 1 left you with
something that predicts the next token. Nothing in that objective produces an assistant. This is
what was added."* That is a negation followed by an assertion, which §5.1 bans, and it repeats
Chapter 1's closing question back at the room instead of starting to answer it. Open on the answer:
three things were added, and here they are.

---

## The structural question, which has changed

`DECISIONS.md` carried one blocking item on this chapter: 105–115 minutes against a 75-minute
budget, with a 2a/2b split recommended to absorb it. **Delivery length is no longer a criterion, so
that argument is gone.** A better question is underneath it.

**Chapter 2 rests on two evidence bases that are not interchangeable.** Published papers carrying
`[V]` citations, and five annotation instruments held by the instructor — structural observations,
never citable, tagged `[E1]`–`[E4]` on a scale `CLAUDE.md` §1a is explicit must never be converted
into the other. The 2a/2b split existed partly so a reader could tell which base a slide sat on.

**The footer ruling dissolves that reason.** Every slide now declares its provenance on its face.
The two bases can be told apart slide by slide without a structural divide.

### The case for weaving them into one argument

Each mechanism claim is followed immediately by the evidence for it. I checked whether the findings
actually attach, and **nine of the ten taught findings have a natural host**:

| Finding (§13 rank) | Attaches to |
|---|---|
| 1. House style is a written edit specification | supervised fine-tuning |
| 1b. The corrected response is collected | supervised fine-tuning — where voice comes from |
| 2. Equivalence engineered out; data conditioned on failure | what a preference dataset contains |
| 3. The judge's blindness dictates criterion design | RLAIF |
| 4. The human attempts the task before judging it | what a rating task is |
| 5. Staleness designed against at both ends | pretraining and the cutoff |
| 6. Instruments diverge structurally | what a rating task contains |
| 7. Two incompatible labour models | who the rater is |
| 9. The pipeline hunts a named band of model knowledge | behaviour traced to mechanism |
| 10. Verification time-boxed at ~15 minutes | what a rating task is |

The one that does not attach cleanly is **8, the instrument rebuilt mid-collection** — the most
forceful item in the set. Its subject is data provenance, so its host is "what the preference
dataset actually contains", which is where I would put it.

Weaving also fixes a real defect: **the room has no concrete picture of a rater until slide 15.**
The chapter says "show a human two responses" on slide 6 and does not say who, where, under what
time pressure, or against what instrument until nine slides later. Until then, "trained on human
preferences" is a phrase rather than a job.

### The case against, which is not weak

Mixing published citations with uncitable observations may blur them in the room whatever the
footer says. A slide's footer is small; a spoken claim is not. The current structure is honest **by
construction** rather than by discipline, and construction is more reliable than discipline.

### What I recommend, and what I need from you

Weave, with one addition: a new provenance form so the annotation evidence declares itself and its
document count on every slide that rests on it.

```
\provenance[Three of five documents.]{instrument}
  -> "Structural observation from five annotation instruments held by the
      instructor. Not citable, and never becomes a citation. Three of five documents."
```

That puts the `[E1]`/`[E2]` distinction on the slide as a count rather than as a tag the room would
have to be taught. **This is your call, not mine** — you are the one who will be standing there,
and you are the only person who knows whether the room will hold the distinction.

---

## What is genuinely strong, and must survive the rebuild

- **The behaviour-to-mechanism table with a *standing* column.** Three rows: one published, one
  plausible-but-unevidenced, one where the folk explanation is contradicted and the real mechanism
  is *not visible in the evidence*. That last row is the best single slide in the repository,
  because it demonstrates the discipline the course teaches instead of describing it.
- **The rubric dimensions named once and never abandoned.** Six dimensions seeding Chapters 3, 5,
  7, 13, 14 and 18. The strongest structural device in the course.
- **Findings printed with their document counts on the slide**, and the explicit statement that the
  ordering is by evidence and deliberately not by interest.
- **The OPRO caveat.** An earlier draft claimed later evaluations found the phrase does not
  transfer to newer models; no primary source was found; the slide now claims only what is
  evidenced, and says so. That correction is on the slide, not hidden in a note.
- **The rating exercise**, including the instruction to call six raters a tally and not a
  distribution, and to say nothing about the expected outcome before the reveal.

---

## What does not earn its place, with a content reason for each

Length is not a reason and is not used.

- **"Not every parameter runs" (sparse models).** Exists solely to feed Chapter 7's sparsity term —
  its own slide says so in a forward-reference box. **Its fate is coupled to Chapter 7**, where I
  have recommended cutting critical batch size on the grounds that nobody in this room will ever
  choose a batch size. If that recommendation stands, this slide has no consumer. If Chapter 7
  keeps it, this stays. Decide Chapter 7 first; do not decide this one in isolation.
- **"And a simplification worth knowing" (direct preference optimisation).** The slide's own
  closing line is *"Simplifying the machinery does not remove the layer this chapter is about."* By
  its own argument it changes nothing the room does or believes. Facilitator note.
- **"What scale bought, and what it did not."** Kaplan and Chinchilla as history. One line survives
  — neither result promised an assistant — and it belongs inside the pretraining slide.

---

## What is missing

**1. A pipeline diagram, reused with the current stage lit.** Pretraining, demonstrations,
preference collection, reward model, policy optimisation. Same device as Chapter 1's data path, one
level up. Without it the chapter is a list of stages the room has to hold in memory.

**2. A running example.** Chapter 1 now carries the stirrups sentence throughout. Chapter 2 has
none, and it needs one badly: a single request, shown as the pretrained model continues it, as a
demonstration would answer it, as two candidate responses to be rated, and as the rated pair
becomes a number. One example, five stages, and the pipeline becomes concrete rather than nominal.

**3. The correction log — §0 of the findings document — is not on a slide, and it should be.**
It records claims killed by further evidence, including one that survived two revisions before the
evidence killed it, and a case where the correction removed the very thing that made the story
good. The chapter has a slide about the gap between force and rank; it does not show the log. **For
a room of researchers, showing your own killed hypotheses is more persuasive than showing your
surviving ones**, and this material is sitting unused.

**4. `system prompt` is never defined.** Chapter 3 uses it from its second slide. Chapter 2 is
where the thing is shaped, so it is where the term belongs.

**5. Nothing shows the pretrained model failing.** The chapter asserts that what comes out of
pretraining "will happily continue your question with three more questions" and never shows it.
Chapter 1 learned this lesson the hard way — its greedy-decoding slide argued a mechanism it never
demonstrated, and that was the one slide the instructor marked confusing. Same defect, same fix: a
capture.

**6. A figure for the rubric conflict.** Six dimensions that conflict is a relationship, and a
relationship needs a figure under the slide specification.

---

## Two slides I want to keep but reframe

The OPRO case and the emotional-prompting replication currently read as digressions in a chapter
about training. They are not digressions — **they are the chapter's self-check.** Chapter 2 spends
twenty slides attributing behaviour to the training process. These two slides show what happens
when someone attributes a behaviour to training and is wrong: a prompt found by search acquires a
narrative afterwards, and a headline of +115% turns out to be the best of eleven stimuli.

Keep both, say on the slide that is what they are for, and move the re-derivation arithmetic —
4.42%, 2.58%, χ² = 0.11 — into the notes. The headline finding is what the room needs; the
arithmetic is what the instructor needs when someone challenges it.

---

## Smaller findings

- **Three banned constructions.** One on a slide — *"This is the hinge of the chapter"* — and two
  in speaker notes. §5.3 says any hit is a rewrite.
- **Parameter counts should use Chapter 1's colour.** 1.3 billion against 175 billion are
  parameters, and Chapter 1 established ochre for those. Reuse it. **Do not add a second colour
  system for evidence strength** — the provenance footers already carry that, and a competing
  scheme would dilute the one that works.
- **The chapter name.** *Formation* tells the room nothing, and abstract chapter names were part of
  what drew the original complaint about pompous language. *How it became an assistant* is plainer.
  Chapter numbers are fixed by the thread map; names are not.

---

## Proposed structure

One chapter, woven, following the pipeline diagram in order — the same organising principle that
fixed Chapter 1.

| | Frame | Rests on |
|---|---|---|
| 1 | Title | — |
| 2 | Three things were added, and here they are | answers Ch1's closing question |
| 3 | The pipeline, end to end | the recurring diagram |
| 4 | Pretraining: one objective, a very large corpus, and it ends | published |
| 5 | What comes out is autocomplete — shown, not asserted | capture |
| 6 | Staleness is designed against at both ends | instrument, corroborated |
| 7 | Demonstrations: humans write the answer they want | published |
| 8 | What that job is: house style is a written edit specification | instrument, 3 of 5 |
| 9 | And the corrected text is collected — where voice comes from | instrument, 2 of 5 |
| 10 | You cannot demonstrate everything, so preference is collected | published |
| 11 | What a rating task contains: the six dimensions | published + instrument |
| 12 | The rater attempts the task before judging it | instrument, 3 of 5 |
| 13 | Verification is time-boxed at about fifteen minutes | instrument, 1 of 5 |
| 14 | Two incompatible labour models | instrument, corroborated |
| 15 | Equivalence is engineered out; the data is conditioned on failure | instrument, 2 of 5 |
| 16 | Realism is manufactured to specification | instrument, 1 of 5 |
| 17 | The instrument was rebuilt mid-collection, in one week | instrument, 1 of 5 |
| 18 | Instruments diverge structurally — "human preferences" dismantled | instrument, corroborated |
| 19 | What disagreement does downstream | published + instrument |
| 20 | The reward model is a model of a rater | published |
| 21 | Optimise the policy against it | published |
| 22 | Helpful and harmless conflict, and refusal is trained in | published |
| 23 | The judge's blindness dictates criterion design | instrument, 2 of 5 |
| 24 | Taking the human out of part of the loop | published |
| 25 | Behaviour traced to mechanism, with a standing column | synthesis |
| 26 | The band where it believes it knows | instrument, 1 of 5 |
| 27 | When attribution goes wrong: a prompt found by search | published |
| 28 | When attribution goes wrong: best of eleven reported as the result | published |
| 29 | What I got wrong while writing this | the correction log |
| 30–35 | The exercise | — |
| 36 | What we covered, and what is still open | — |

**Ordering principle:** the diagram's stages in order, each stage followed immediately by what that
stage looks like from inside the rating seat. The findings keep their evidential rank inside a
stage; they are not reordered by force.

---

## What I did not do

- **I did not read the five annotation instruments.** They are the instructor's and are not in the
  repository. Everything above rests on `ch02-annotation-findings.md`, which is a careful secondary
  account of them, and on its own correction log.
- **I did not verify Chapter 2's citations against their originals.** Ten sources are cited and all
  are `[V]` in `references.md`; I checked the tags, not the papers.
- **I did not review `assets/rating-exercise/README.md` in detail**, so the six exercise slides in
  the proposed structure are a placeholder count rather than a design.
- **I did not resolve the Chapter 7 coupling.** Whether the sparse-model slide survives depends on
  a Chapter 7 decision that has not been made.
- **I did not check whether the OPRO and emotional-prompting material duplicates Chapter 4.** Both
  chapters teach that a reported result can be an artefact of selection. That may be deliberate
  reinforcement or it may be redundancy, and deciding needs Chapter 4 read against this one.

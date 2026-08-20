---
theme: default
title: Chapter 2 — Formation
info: How a predictor became an assistant, and what the human layer looks like from inside it. Contains the 2a/2b split point - see DECISIONS.md, still open.
class: text-left
mdc: true
---

# Chapter 2 — Formation

### How a predictor became an assistant

<div class="mt-10 text-xl opacity-85">

Chapter 1 left you with something that predicts the next token. Nothing in that
objective produces an assistant. This is what was added.

</div>

---

## Pretraining

<v-clicks>

- One objective, run over a very large corpus: predict the next token.
- No labels, no task, no supervision beyond the text itself. This is why the corpus could be so large.
- It ends. **The cutoff is a date**, after which the model knows nothing except what you put in the window.

</v-clicks>

<div v-click class="mt-6 text-lg">

What comes out of this stage is not an assistant. It is a very good autocomplete that will
happily continue your question with three more questions.

</div>

---

## What scale bought, and what it did not

<v-clicks>

- Performance improves predictably with model size, data and compute — smoothly enough to plan around.
- The later correction mattered more than the original claim: for a fixed compute budget, models were **undertrained relative to their size**. More data, smaller model.
- **Neither result promised an assistant.** They describe how loss falls, not how behaviour changes.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Worth knowing where the numbers come from before you repeat them: these are empirical
fits over a range that was tested, extrapolated by everyone since.

</div>

<Cite k="hoffmann2022" />

---

## Not every parameter runs

<v-clicks>

- A **sparse** model routes each token to a subset of its parameters. Total size and active size come apart.
- Published designs scale to very large total parameter counts while keeping the active count per token modest.
- Scaling behaviour has been characterised across several orders of magnitude of size for routed models specifically.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-75 border-t pt-3">

**Forward reference — Chapter 7.** This is not trivia. The ratio of total to active
parameters is *sparsity*, and it appears directly in the critical batch size you will
derive. Cost depends on it.

</div>

<Cite k="clark2022" />

---

## Supervised fine-tuning

The first thing added on top.

<v-clicks>

- Humans write demonstrations: here is a request, here is a good response to it.
- The model is trained on those pairs. It learns the **shape** of an answer — that a question gets answered, that a request gets fulfilled.
- Cheap in data terms, and it does most of the visible work of turning autocomplete into an assistant.

</v-clicks>

<div v-click class="mt-6 text-lg">

Everything after this is about **quality**, not about format.

</div>

<Cite k="ouyang2022" />

---

## Learning a preference

You cannot write demonstrations for everything. So the pipeline learns what people prefer.

<v-clicks>

- Show a human two responses to the same prompt. Ask which is better.
- Train a **reward model** to predict that judgement.
- Now you have a function that scores any response — including responses no human has seen.

</v-clicks>

<div v-click class="mt-6 text-lg">

That function is a **model of a rater**, trained on a finite set of comparisons made by
particular people under particular instructions. Hold onto that sentence.

</div>

<Cite k="stiennon2020" />

---

## Reinforcement learning from human feedback

<v-clicks>

- Generate a response, score it with the reward model, adjust the policy to score higher. Repeat.
- The result reported for the canonical work: outputs from a **1.3-billion-parameter** fine-tuned model were preferred to those of a **175-billion-parameter** base model.
- A hundred-fold size difference, reversed by the layer on top. That is the measure of how much this stage does.

</v-clicks>

<div v-click class="mt-5 text-sm opacity-80">

The same authors state plainly that the result "still make[s] simple mistakes". The gain is
in preference, not in correctness.

</div>

<Cite k="ouyang2022" />

---

## Helpful, and harmless

<v-clicks>

- The preference layer is trained against more than one thing at once. Helpfulness and harmlessness are collected as separate signals and they **conflict**.
- A maximally helpful answer to some requests is a harmful one. The tension is not a bug in the method; it is the method.
- Which means refusal behaviour is not a filter bolted on the front. **It is trained in**, from the same kind of human judgement as everything else.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-75 border-t pt-3">

**Thread opened — trust boundary.** Harmlessness as trained behaviour here; routed around
from outside in Chapter 6; opened deliberately in Chapter 12; governed in Chapter 18.

</div>

<Cite k="bai2022hh" />

---

## Taking the human out of part of the loop

<v-clicks>

- Write the principles down. Have the **model** critique and revise its own responses against them, and train on that.
- Human labour moves from labelling individual comparisons to writing and maintaining the principles.
- The published version of this reports harmlessness signals generated from AI feedback rather than human feedback.

</v-clicks>

<div v-click class="mt-6 text-lg">

**This is the hinge of the chapter.** Once a written criterion can be applied by a machine,
the question becomes: what does a criterion have to look like for a machine to apply it?
Part 2b is what that does to the criteria.

</div>

<Cite k="bai2022cai" />

---

## And a simplification worth knowing

<v-clicks>

- Training a separate reward model and then optimising against it is expensive and unstable.
- A later result showed the preference data can be used to update the policy **directly**, with no explicit reward model in the loop.
- The subtitle of that paper is the whole idea: *your language model is secretly a reward model.*

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Method detail, and it matters here for one reason: the human comparisons are still the
input. Simplifying the machinery does not remove the layer this chapter is about.

</div>

<Cite k="rafailov2023" />

---

## Behaviour, traced to mechanism

Not "the model is sycophantic." **Why** it is.

<div class="text-sm mt-3">

| What you see | Where it comes from |
|---|---|
| Agrees with you when you push back | Agreement was preferred by raters, at scale |
| Long, structured, confident answers | Those were preferred under time pressure |
| Refuses some requests firmly | Harmlessness trained as a competing objective |
| Sounds the same across topics | House style specified in writing and enforced |
| Confident on your literature, right on textbooks | Where data was dense, plausible and true coincide |

</div>

<div v-click class="mt-5 text-lg">

Every row is a design consequence, not a personality. That is the difference between this
chapter and a list of quirks.

</div>

---

## A cautionary case: the discovered prompt

An automated search over candidate instructions found that one phrasing scored best on
two benchmarks — and the phrasing looked like encouragement.

<v-clicks>

- **Scorer: PaLM 2-L. Benchmarks: GSM8K and Big-Bench Hard.** Reported gains up to 8% and up to 50% respectively.
- It was **found by search**, not by testing a hypothesis about encouragement. The narrative arrived afterwards.
- Run the same search with a different optimiser model and you get a **different** winning instruction.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**What this course will not claim.** An earlier draft of these notes said later evaluations
found the phrase "does not transfer to newer models". No primary re-evaluation could be
found saying that. What *is* evidenced is that optimised prompts do not transfer
consistently **across models** — which is a different claim, and the one we will make.

</div>

<Cite k="yang2023" />

---

## And a replication that failed

A widely cited result reported that appending emotional stimuli to prompts improved
performance — including a headline **+115%** on one benchmark suite.

<v-clicks>

- An independent replication across six current models found *"an insignificant performance increase of 1%… (χ² = 0.11, p = .74)."*
- The replicators then re-derived the original's own arithmetic. **The 115% is the best of eleven stimuli, not an average.** Averaged across all eleven, the original's own reported numbers give **4.42%**.
- Their words: *"the numerical values communicated in the study itself do not coincide with these claims."*

</v-clicks>

<div v-click class="mt-5 text-lg">

Best-of-eleven, reported as the result. **You will meet this again in Chapter 4**, where it
is the exact trap a five-case eval sets for you.

</div>

<Cite k="vaugrante2024" />

---
layout: center
class: text-center
---

# Part 2b

### The annotation layer

<div class="mt-8 text-lg opacity-85">

Everything so far describes the pipeline from outside. This half is what it looks like
from inside the rating seat.

</div>

<div class="mt-10 text-sm opacity-70">

**SPLIT POINT.** `DECISIONS.md` records Chapter 2 at 105–115 minutes against a 75-minute
budget, with a 2a/2b split recommended and **not yet decided**. This deck is written so the
cut is here: everything above is 2a, everything below is 2b. Deleting this slide merges
them again.

</div>

---

## What this rests on, stated first

<v-clicks>

- The instructor worked as a human-feedback annotator, and holds contributor and reviewer manuals from projects they did not work on.
- **Five documents.** Two obtained as re-hosted copies, so the vendor, the client and their completeness are unknown.
- These are **structural observations**. They are not citable, they never become citations, and nothing in this half carries a source footer.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**Findings are tagged by how many documents support them, and that tag is shown.** Corroborated
across independent documents is one thing; stated once is another; inferred from structure
is a third. **Five documents of unknown provenance are not a sample**, and no worked example,
prompt, rubric row or banned-phrase list from any of them appears anywhere in this course.

</div>

---

## Corroborated across documents

<v-clicks>

- **House style is a written edit specification, and the corrected response is collected.** Raters do not only judge; they repair, to a written specification, and the repaired text is the artefact that gets kept.
- **Equivalence is engineered out.** Two instruments, opposite mechanisms, same result: you cannot record "these are equally good". Preference data is conditioned on one being worse.
- **The judge's blindness dictates criterion design.** Where a model grades, it is given one criterion and the deliverable — not the prompt, not the other criteria. So every criterion must carry its own context.

</v-clicks>

<div v-click class="mt-5 text-lg">

That third one is the mechanical bridge to machine-graded training, and it is why criteria
end up stripped to the checkable surface.

</div>

---

## Corroborated across documents, continued

<v-clicks>

- **The human is made to attempt the task before judging it.** The pipeline buys the attempt in order to get a reliable verdict.
- **Staleness is designed against, at both ends.** Tasks are built so they will not age, and instructions say so explicitly.
- **Instruments diverge — structurally more than lexically.** An instruction-following dimension recurs, and a truthfulness dimension recurs; almost everything else about *what* is measured, at what granularity, under what weighting, differs.
- **Two incompatible labour models coexist.** Generalist raters and domain professionals, doing work that is described with the same vocabulary and is not the same job.

</v-clicks>

<div v-click class="mt-5 text-lg">

That last one dismantles "trained on human preferences" as a sentence. **Which humans, doing
which job, under which instrument?**

</div>

---

## Stated once, as a rule, in one document

These are single-document findings. They are stated as rules rather than inferred, which is
why they are here — and they are still one document each.

<v-clicks>

- **An instrument was rebuilt mid-collection, in one week.** Dated and itemised in a changelog. For a room of experimentalists this may be the most persuasive item in the chapter — and it rests on one changelog, which is exactly why it is ranked below the ones above it.
- **The pipeline has an operational theory of where hallucination lives.** Contributors are instructed to aim at a specific band of model knowledge: not common knowledge, where the model is reliable; not genuinely obscure material, where it declines; the band between, where it believes it knows.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**That band is where your own literature sits.** It is the generating rule for Chapter 5's
failure gallery, and it explains why the tool feels reliable on textbook material and
erratic on your research. Not random — targeted.

</div>

---

## The gap between force and rank

<v-clicks>

- The rebuilt-instrument finding is the one this room will remember. It is **eighth** in evidential order, not first.
- Two findings that made better stories in an earlier draft were demoted when further documents failed to corroborate them. One was killed outright.
- The ordering here is by evidence. **It is deliberately not the order of interest.**

</v-clicks>

<div v-click class="mt-6 text-lg">

Saying that out loud is the point of the segment. You are about to be asked to rate things,
and the pressure you will feel is exactly the pressure that ordering resists.

</div>

---

## Five more, held back

<v-clicks>

- Verification time-boxed at about fifteen minutes, with a ranked source list — the most quotable item in the set, and it appears in the exercise rather than here.
- Realism in the data manufactured to specification.
- Score-versus-rationale mismatch, uncorroborated after two further documents.
- Goodhart structure, and the anti-gaming machinery bolted on against it.
- Role variation by client — a negative result, and the one an earlier draft turned into a story it could not support.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

These sit in the facilitator notes. They are answers to questions that will get asked, not
material the chapter can carry.

</div>

---

## Now you do it

<div class="mt-6 text-xl">

Two responses. One rubric. Eight minutes, and visible time pressure.

</div>

<v-clicks>

- The material is **mechanics, concrete or fluids** — the shared domain, so every one of you can check the physics.
- You will record a score per dimension, a preference, **and your confidence.**
- Verification is time-boxed. If checking a claim would take more than two minutes at your desk, mark it **unassessable** rather than guess.
- No preference is allowed unless you name a specific failure.

</v-clicks>

<div v-click class="mt-5 text-sm opacity-80">

Full specification in `assets/rating-exercise/README.md`. The rubric is a synthetic
instrument built for this course on your domain — never a client instrument.

</div>

---

## What the exercise is for

<v-clicks>

- Most rooms prefer the fluent, well-formatted response containing an error.
- The tally will be small — five or six raters is **a tally, not a distribution**, and we will call it that.
- Then the question that hands you to Chapter 4: **how many raters would we need before this meant anything?** Nobody in the room will know, and that is the honest starting position.

</v-clicks>

<div v-click class="mt-6 text-lg">

Under mild time pressure, competent engineers reward verbosity, confidence and formatting
over correctness — and are most confident where they are most wrong.

**That preference is a reward signal.** You have just generated training data.

</div>

---

## Where this leaves us

<v-clicks>

- A predictor, plus demonstrations, plus a learned model of a rater, optimised against.
- Behaviour that traces to mechanism rather than to personality.
- A human layer that is smaller, more variable and more time-pressured than the phrase "trained on human preferences" suggests.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-75 border-t pt-3">

**Threads opened — truthfulness** (a rated dimension here; a structural property in Chapter 5;
a work habit in Chapter 14) and **trust boundary** (trained here; attacked in Chapter 6).

</div>

<div v-click class="mt-6 text-xl">

You now know where the behaviour comes from. **Chapter 3 is how to steer it** — and Chapter 4
is how to find out whether the steering worked.

</div>

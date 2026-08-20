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

<Cite k="kaplan2020,hoffmann2022" />

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

<Cite k="fedus2021,lepikhin2020,clark2022" />

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

## What a rating task actually contains

A rubric, and the same six dimensions recur across this course. **Learn them here; they do
not get replaced.**

<div class="text-sm mt-2">

| Dimension | Returns as |
|---|---|
| **Truthfulness** | a structural failure in Chapter 5; a work habit in Chapter 14 |
| **Instruction following** | the lever Chapter 3 spends most of its time on |
| **Harmlessness** | the trust boundary, from Chapter 6 to Chapter 18 |
| **Formatting** | the thing that wins when nobody can check the physics |
| **Verbosity** | a cost in Chapter 7 and a bill in Chapter 13 |
| **Tone** | where house style comes from, and Chapter 10's instruction file |

</div>

<div v-click class="mt-4 text-lg">

Six axes, one judgement, and they **conflict**. A response can be truthful and badly
formatted, or fluent and wrong.

</div>

---

## What disagreement does downstream

Two competent raters, same rubric, same pair, different answer. That is not noise to be
eliminated — it is information, and what happens to it matters.

<v-clicks>

- A **reviewer layer** audits ratings against the rubric. One instrument treats disagreement between *adjacent* bands as acceptable and only fails a rating when two assignments land in opposite bands. **One document of five** — a sensible rule, not an industry standard.
- Where raters diverge, the question is **whether the rubric or the rater is at fault.** An ambiguous dimension produces disagreement that no amount of rater training fixes.
- Unresolved disagreement does not vanish. It enters the preference data as inconsistency, and the reward model fits it.

</v-clicks>

<div v-click class="mt-4 text-sm opacity-80">

You will occupy both sides of this in the exercise: rate, then audit somebody else's rating
against the same instrument.

</div>

---

## Reinforcement learning from human feedback

<v-clicks>

- Generate a response, score it with the reward model, adjust the policy to score higher. Repeat.
- The result reported for the canonical work: outputs from a **1.3-billion-parameter** fine-tuned model were preferred to those of a **175-billion-parameter** base model.
- A hundred-fold size difference, reversed by what was added on top. **Credit the post-training pipeline as a whole** — the reported comparison is supervised fine-tuning *plus* RLHF, not the reinforcement step alone.

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

- **Constitutional AI:** write the principles down, have the **model** critique and revise its own responses against them, and train on that.
- The general pattern is **RLAIF** — reinforcement learning from *AI* feedback, with the model standing in for the rater.
- Human labour moves from labelling individual comparisons to writing and maintaining the principles.
- The published version of this reports harmlessness signals generated from AI feedback rather than human feedback.

</v-clicks>

<div v-click class="mt-6 text-lg">

**This is the hinge of the chapter.** Once a written criterion can be applied by a machine,
the question becomes: what does a criterion have to look like for a machine to apply it?

**The answer, in one line:** it must be checkable without context — which means stripped of
everything except the observable surface. Part 2b is what that does in practice, and what it
costs.

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

| What you see | Where it comes from | Standing |
|---|---|---|
| Refuses some requests firmly | Harmlessness trained as a competing objective | Published |
| Agrees with you when you push back | Preference data rewards agreement | Plausible, **not evidenced in the documents** |
| Long, structured, confident answers | **Not known** — see below | **The folk answer is contradicted** |

</div>

<div v-click class="mt-4 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**The verbosity row is the interesting one, because the obvious answer is wrong.** The folk
story says raters liked long answers, so models got long. Two of the reviewed instruments say
otherwise: one broke ties deliberately toward **brevity**, the other **deleted length as a
grading category** partway through the project — after which nothing in it penalises length
at all. And models are verbose anyway.

**So the mechanism is not visible in these documents.** Saying that is more credible than
repeating the folk version.

</div>

<div v-click class="mt-3 text-sm opacity-80">

This table is the instructor's synthesis, which is why it carries no source footer — the
middle column is an argument and the third column says how far each one goes.

</div>

<div v-click class="mt-3 p-3 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**TODO(verify)** — the brief also requires test-case hardcoding as a concrete reinforced
reward hack: a model special-casing to pass tests rather than solving the problem, attributed
by its own vendor to reward hacking during training. The system card carrying that quote is
recorded at `[P]` and has not been read. **It does not reach a slide until it has been.**

</div>

---

## A cautionary case: the discovered prompt

An automated search over candidate instructions found that one phrasing scored best on
two benchmarks — and the phrasing looked like encouragement.

<v-clicks>

- **Scorer: PaLM 2-L. Benchmarks: GSM8K and Big-Bench Hard.** Reported gains up to 8% and up to 50% respectively.
- It was **found by search**, not by testing a hypothesis about encouragement. The narrative arrived afterwards.
- The winning instruction is specific to **the model it is scored on**, not to the search that found it. Change the task model and the best phrasing changes with it.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**What this course will not claim.** An earlier draft of these notes said later evaluations
found the phrase "does not transfer to newer models". No primary re-evaluation could be
found saying that. What *is* evidenced is that optimised prompts do not transfer
consistently **across models** — a different claim, and the one this course makes.

</div>

<Cite k="yang2023,ye2024" />

---

## And a replication that failed

A much-cited **technical report** — not a peer-reviewed paper — found that appending
emotional stimuli to prompts improved performance, with a headline **+115%** on one
benchmark suite.

<v-clicks>

- An independent replication across six current models found *"an insignificant performance increase of 1%… (χ² = 0.11, p = .74)."*
- The replicators then re-derived the original's own arithmetic. **The 115% is the best of eleven stimuli, not an average.** Averaged over all eleven, the original's own reported numbers give **4.42% on that suite and 2.58% across all benchmarks.**
- Their words: *"the numerical values communicated in the study itself do not coincide with these claims."*

</v-clicks>

<div v-click class="mt-4 p-4 border-l-4 text-sm" style="border-color:#0E5C68; background:#F2F7F8">

**The replicators' own limits, which belong beside their result.** They did not use identical
tasks or models, wording varied slightly, they **sampled one stimulus per task by seed rather
than reproducing the best-of-eleven protocol**, and they dropped one stimulus because models
answered it instead of the task.

That third one matters most: the 1% figure comes from a design that deliberately did **not**
run best-of-eleven — which is precisely why the two numbers are not in contradiction.

</div>

<div v-click class="mt-4 text-lg">

Best-of-eleven, reported as the result. **Chapter 4 shows you the same trap**, set by your
own five cases.

</div>

<Cite k="li2023emotion,vaugrante2024" />

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

**Each finding carries how many of the five documents support it, on the slide.** Corroborated
across independent documents is one thing; stated once is another; inferred from structure
is a third — and this deck prints the count rather than asking you to trust the ordering. **Five documents, two of them of unverified provenance, are not a sample**, and no worked example,
prompt, rubric row or banned-phrase list from any of them appears anywhere in this course.

</div>

---

## Corroborated across documents

<v-clicks>

- **House style is a written edit specification.** Raters do not only judge; they repair, to a written specification. **Three of five documents.**
- **And in two of them the repaired text is what gets collected.** That is a separate claim on weaker evidence, and an earlier draft of these notes welded the two together — which is why they are separated here.
- **Equivalence is engineered out.** Two instruments, opposite mechanisms, same result: you cannot record "these are equally good". **Two of five.**
- **One instrument goes further** and collects comparisons only where a model has already failed — so its preference data is conditioned on failure. **That is one document, not two.**
- **The judge's blindness dictates criterion design.** Where a model grades, it is given one criterion and the deliverable — not the prompt, not the other criteria. So every criterion must carry its own context. **Two of five, and the causal direction is stated outright in one of them.**

</v-clicks>

<div v-click class="mt-5 text-lg">

That third one is the mechanical bridge to machine-graded training, and it is why criteria
end up stripped to the checkable surface.

</div>

---

## Corroborated across documents, continued

<v-clicks>

- **The human is made to attempt the task before judging it.** The pipeline buys the attempt in order to get a reliable verdict. **Three of five.**
- **Staleness is designed against, at both ends.** Tasks are built so they will not age, and instructions say so explicitly. **Corroborated.**
- **Instruments diverge — structurally more than lexically.** An instruction-following dimension recurs, and a truthfulness dimension recurs; almost everything else about *what* is measured, at what granularity, under what weighting, differs.
- **Two incompatible labour models coexist.** Generalist raters and domain professionals, doing work described with the same vocabulary that is not the same job. **Corroborated.**

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

- **An instrument was rebuilt mid-collection, in one week.** Grading categories deleted, task authorship moved from contributor to vendor, mandatory rewrites imposed. **Data gathered a fortnight apart was graded by materially different instruments, with nothing in the output to distinguish them.** One changelog — which is exactly why it ranks below everything above it, and it may still be the item you remember.
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

## How the session runs

<div class="text-sm mt-3">

| | Step | Minutes |
|---|---|---|
| 1 | **Rate**, individually, in silence, under visible time pressure | 8 |
| 2 | **Collect the tally** — preference, then confidence beside it | 3 |
| 3 | **Reveal** the physical error and the fabricated citation | 5 |
| 4 | **Name what happened** | 5 |
| 5 | **Reviewer round** — swap sheets, audit against the rubric | 10 |
| 6 | **Adjudicate** — the defensible grade per axis, including where the rubric is ambiguous | 4 |

</div>

<v-clicks>

- Steps 1–4 carry the lesson. If time runs short, **cut step 5 before anything else.**
- With an odd number in the room, make one group of three at step 5 and rotate rather than swap.

</v-clicks>

<div v-click class="mt-4 text-sm opacity-80">

Nothing about the expected outcome is said before step 3. Announcing it in advance would
void the demonstration the chapter is built on.

</div>

---

## Step 4 — naming what happened

*Delivered after the reveal, not before it.*

<v-clicks>

- Read the tally back. Whatever it says, **call it a tally** — five or six raters is not a distribution, and this course does not present six points as one.
- Put confidence beside preference and ask whether the two track each other. **If they do, say so.** The interesting version is not guaranteed to happen.
- Ask how many marked the fabricated citation *unassessable* rather than false. That is the correct action under the instrument — and it is exactly how a fabricated citation passes into a dataset as acceptable.

</v-clicks>

<div v-click class="mt-4 text-lg">

Then the sentence the chapter has been building toward: whatever preference this room just
expressed, at scale **that preference is a reward signal.** You have spent eight minutes
generating training data.

</div>

<div v-click class="mt-3 text-sm opacity-80">

And the question that hands you to Chapter 4: **how many raters would we have needed before
that tally meant anything?** Nobody here knows yet.

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

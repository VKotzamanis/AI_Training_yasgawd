---
theme: default
title: Chapter 8 — Brain and model
info: Answers the question Chapter 1 opened. Runs the analogy and then breaks it. Closes Session 1 on the line that opens Session 2.
class: text-left
mdc: true
---

# Chapter 8 — Brain and model

### The question from Chapter 1, answered

<div class="mt-10 text-2xl">

**Is this like a brain?**

</div>

<div class="mt-6 text-lg opacity-85">

Seven chapters ago this was premature. You have now priced the thing and watched it
fail, so the answer is worth something.

</div>

---

## Start with what is not true

<v-clicks>

- **Transformers were not derived from neuroscience.** They came out of machine translation, and the design pressures were throughput and parallelism.
- **"Attention" shares a name with neural attention and little else.** Chapter 1 gave you the definition: a weighted sum over key–value pairs, with weights from a compatibility function. That is linear algebra with a borrowed noun.
- The resemblance people feel is mostly that both produce language. That is the thing being explained, not evidence for the explanation.

</v-clicks>

---

## What *is* defensible

There is a real literature here, and it is more careful than its summaries.

<v-clicks>

- Take a language model, feed it the same text a person read or heard, and extract the model's internal activations.
- Fit a regression from those activations to the person's brain responses.
- Ask how much of the response you can predict. The answer is: a surprising amount.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**Say the method correctly.** This is an **encoding model** — ridge regression from layer
activations. It is *not* "next-token surprisal predicting neural responses", which is how
the result usually circulates, including in an earlier draft of this course's own notes.

</div>

<div v-click class="mt-4 text-sm opacity-85">

**Scope:** 43 models, against three neural datasets of **n = 10, n = 5 and n = 5**. And the
*predictive-processing* conclusion is not measured within a brain at all — it is a
**between-model correlation**: models that predict the next word better tend to score better
on brain data. Hold onto that, because it is precisely what gets attacked two slides from now.

</div>

<Cite k="schrimpf2021" />

---

## The headline needs its denominator

The result is often quoted as predicting **nearly 100% of explainable variance**.

<v-clicks>

- That figure is normalised by a **noise ceiling** — how much of the signal is predictable even in principle, given how noisy the recordings are.
- The ceilings in that work are **0.32, 0.17 and 0.20** across the three datasets.
- The authors say so themselves, and compare unfavourably: *"even this ceiling is low relative to single cell recordings in the primate ventral stream [e.g., 0.82 for IT recordings]."*

</v-clicks>

<div v-click class="mt-5">

**Be precise about what a ceiling is.** It estimates the reliability of the *recordings* —
how much of the signal is predictable in principle given repeat-to-repeat noise. It is a
fact about the dataset, not about the size of the brain–model correspondence.

</div>

<v-clicks>

- So it licenses this: raw predictivity is low in absolute terms, the normalised headline is doing a lot of work, and the denominator is itself an estimate with error attached.
- It also licenses the authors' own point — these datasets **separate models far less sharply** than primate recordings do.
- It does **not** license "the correspondence is small". A ceiling cannot settle that.

</v-clicks>

<div v-click class="mt-4 p-3 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

Normalising against ceilings of 0.32, 0.17 and 0.20 inflates by roughly **three- to
sixfold**, not by one figure. And **`TODO(verify)`: whether these are correlations or
proportions of variance is not recorded** — on the variance scale the factors are far
larger. Per the house rule, a denominator this consequential gets its units stated beside it.

</div>

<Cite k="schrimpf2021" />

---

## And the result that complicates it

<v-clicks>

- In the same work, **untrained models with a trained linear readout performed well above chance.**
- If a randomly initialised network predicts brain data respectably, then what is being measured is not straightforwardly "what training taught it".
- The authors report this. It is in the paper, not in the summaries.
- **Hold this one loosely.** Two slides from now it stops being a curiosity and becomes a confound.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Worth naming for a course about citation discipline: this paper went through the PNAS
**Contributed** track, where the contributing author selects the reviewers. That is not a
criticism of the work. It is a fact about the review process, and you would want to know
it about your own field.

</div>

<Cite k="schrimpf2021" />

---

## The strongest version, and its own authors' limits

A second line of work records neural activity directly, with electrodes, while people
listen to speech.

<v-clicks>

- Scope, which matters: **nine participants, all epilepsy patients with implanted electrodes**, listening to **one thirty-minute podcast**, compared against GPT-2.
- The shared structure they find is real and it is specific.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

The authors then say this, and it is the sentence this chapter is built on:

> These shared computational principles, however, do not imply that the human brain and
> DLMs implement these computations in a similar way.

> While transformer models are an impressive engineering achievement, **they are not
> biologically feasible.**

</div>

<Cite k="goldstein2022" />

---

## The field correcting itself, in public

<v-clicks>

- One re-analysis attacks the between-model correlation directly: predicting future words **does not uniquely, or even best, explain** why a representation fits brain data. Within a model, the representations best at prediction are *"strictly worse brain models"* than others.
- Another re-analyses **exactly the three datasets** the first result rests on. Shuffled train–test splits produced spurious results — and **positional signals and word rate fully account for the neural predictivity of untrained models.**
- That second finding **dissolves** the untrained-model result from two slides ago rather than complicating it. It was a confound, not a discovery.

</v-clicks>

<div v-click class="mt-5 text-lg">

**Idan Blank is a co-author of the original paper and of the critique.** That is what a
healthy field looks like from outside, and it is the cleanest example in this course of the
habit Chapter 17 asks of you.

</div>

<Cite k="antonello2024,hadidi2026" />

---

## So: run the analogy, then break it

The analogy is worth running. It is the break that carries the content.

<v-clicks>

- **The hippocampus consolidates episodic experience into durable memory.** Something happens, and it is written into a store that changes you.
- **A model at inference does none of this.** The weights are frozen. Nothing that happens in a session is retained anywhere.
- The context window is not a hippocampus. It is a **buffer that gets discarded.**

</v-clicks>

---

## The comparison everyone makes, and why it cannot be made

You will hear this one: human working memory holds about four items, a context window holds
hundreds of thousands of tokens, **so the machine wins on memory.**

<v-clicks>

- The primary source does not say four. It argues for **three to five chunks**, and only under conditions engineered to block chunking and rehearsal.
- It is a target article published with roughly seventy pages of peer commentary in the same issue, and the fixed-slot view it defends is **actively contested** — competing accounts treat capacity as a shared resource rather than a count of slots.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**But the deeper problem is not that the number is wrong.** A *chunk* is a unit of
meaning assembled by the person recalling it. A *token* is a fragment of text fixed by a
vocabulary before training. There is **no conversion between them**, so no ordering between
4 and 200,000 is defined at all.

This is not a weak comparison. **It is not a comparison** — the same failure as dividing by
a denominator whose units you never stated.

</div>

<div v-click class="mt-4 text-sm opacity-80">

So retract the whole framing, including "the numbers run opposite to the analogy". That
sentence needs the ordering it does not have.

</div>

---

## What you can say instead

Drop the counting and the asymmetry is still there — and it never needed a number.

<div class="grid grid-cols-2 gap-8 mt-5">
<div>

**Context window**

<v-clicks>

- **Supplied from outside.** You put things in it.
- **Passive.** Holding a token costs nothing and does nothing; it sits there.
- Contents are **fixed** for the pass and then discarded whole.

</v-clicks>

</div>
<div>

**Working memory**

<v-clicks>

- **Maintained from inside**, and it costs effort to hold anything.
- **Active and interference-prone** — items compete, and rehearsal is what keeps them.
- Continuously **rebuilt from and written back into** long-term memory.

</v-clicks>

</div>
</div>

<div v-click class="mt-5 text-lg">

One is a **buffer**. The other is a **process inside a system that consolidates.** That
difference does not get smaller if you make the buffer larger, which is the whole point —
and it is why Chapter 10 hands you a file rather than a bigger window.

</div>

<Cite k="cowan2001" />

---

## One more comparison to refuse

<v-clicks>

- *"The frontal cortex is the reasoning part, so the later layers must be the reasoning part."*
- The premise is **contested within neuroscience itself.** Borrowing a disputed claim from one field to explain another does not produce understanding; it produces two problems.
- Chapter 5 already told you the related thing: the model's stated reasoning is not an explanation of the model's behaviour.

</v-clicks>

---

## What the analogy is actually good for

<v-clicks>

- As a **source of hypotheses**, it has produced real, checkable work — that is the literature above.
- As an **explanation**, it does not survive its own authors' caveats.
- As a **guide to what the tool will do on Thursday**, it is worse than useless, because it imports intuitions about memory, understanding and intent that the system does not have.

</v-clicks>

<div v-click class="mt-6 text-lg">

You have a better guide. It is Chapters 1 through 7.

</div>

---

## Where Session 1 ends

<v-clicks>

- A next-token predictor, shaped by a rating process you have now occupied.
- Measurable, and mostly weakly, on five cases.
- Failing in ways that are structural rather than accidental, and expensive in ways that have an equation.
- Not a brain — and the interesting part is *which* difference matters.

</v-clicks>

<div v-click class="mt-10 text-2xl">

The model has no hippocampus. **So you have to be its hippocampus.**

</div>

<div v-click class="mt-4 opacity-80">

That is Session 2, and it starts with a system that acts.

</div>

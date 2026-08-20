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

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**Say the method correctly.** This is an **encoding model** — ridge regression from layer
activations. It is *not* "next-token surprisal predicting neural responses", which is how
the result usually circulates, including in an earlier draft of this course's own notes.

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

<div v-click class="mt-6 text-lg">

**Nearly all of a small number is still a small number.** Quote the percentage without the
ceiling and you have moved a factor of five without saying so — which is the erratum from
Chapter 4 in a different field.

</div>

<Cite k="schrimpf2021" />

---

## And the result that complicates it

<v-clicks>

- In the same work, **untrained models with a trained linear readout performed well above chance.**
- If a randomly initialised network predicts brain data respectably, then what is being measured is not straightforwardly "what training taught it".
- The authors report this. It is in the paper, not in the summaries.

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

- One re-analysis finds that predicting future words **does not uniquely, or even best, explain** why a representation fits brain data — within a model, the representations best at prediction are *"strictly worse brain models"* than others.
- Another re-analyses **exactly the three datasets** the first result rests on, and finds that shuffled train–test splits produced spurious results, and that **positional signals and word rate fully account for the neural predictivity of untrained models.**

</v-clicks>

<div v-click class="mt-6 text-lg">

One author appears on **both** the original paper and the critique. That is what a healthy
field looks like from outside, and it is the cleanest example in this course of the habit
Chapter 17 asks of you.

</div>

<Cite k="hadidi2026" />

---

## So: run the analogy, then break it

The analogy is worth running. It is the break that carries the content.

<v-clicks>

- **The hippocampus consolidates episodic experience into durable memory.** Something happens, and it is written into a store that changes you.
- **A model at inference does none of this.** The weights are frozen. Nothing that happens in a session is retained anywhere.
- The context window is not a hippocampus. It is a **buffer that gets discarded.**

</v-clicks>

---

## The working-memory comparison, done honestly

The familiar version: human working memory holds about four items, against a context
window of hundreds of thousands of tokens. **The numbers run opposite to the analogy.**

<v-clicks>

- The primary source does not say four. It argues for **three to five chunks**, and only under conditions engineered to block chunking and rehearsal.
- It is a target article published with roughly seventy pages of peer commentary bound into the same issue, and the fixed-slot view it defends is **actively contested** — competing accounts treat capacity as a shared resource rather than a number of slots.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**And the comparison is a unit mismatch.** A *chunk*, measured under conditions designed to
prevent chunking, is not commensurable with a *token*. Putting 4 beside 200,000 looks like
a measured contrast and is not one.

**The argument survives; the arithmetic does not.** Make it structurally — one system
consolidates and the other does not — and drop the numbers.

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

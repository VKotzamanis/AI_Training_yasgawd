---
theme: default
title: Chapter 4 — Measurement
info: Converts the course from advice into method. Starts the verification thread. Settles the two claims Chapter 3 deliberately left open.
class: text-left
mdc: true
---

# Chapter 4 — Measurement

### How you know any of Chapter 3 worked

<div class="mt-10 text-xl opacity-85">

Chapter 3 ended owing you two answers. This is how you collect a debt like that from
a system nobody can open.

</div>

---

## Why prompting advice circulates as folklore

<v-clicks>

- Someone changes a prompt, the output looks better, and they tell you.
- They ran it once. They looked at the output before deciding what "better" meant. They did not run the old prompt again.
- Every one of those is a defect you would catch instantly in a colleague's experiment.

</v-clicks>

<div v-click class="mt-8 text-lg">

**This room already has this skill.** You do not know it applies here, because nobody has
called a prompt an experimental condition in front of you before.

</div>

---

## The anchor: an expert, a denominator, and a factor of two

An expert lecture defines a compute-time equation whose denominator is
**multiply-accumulates per second**.

<v-clicks>

- Substitute a spec-sheet figure in FLOP per second and the result is wrong by exactly two.
- One MAC is two FLOP. The numerator needs the factor, or the denominator does.
- It was caught by an **outside reader**, in a comment thread, after publication.

</v-clicks>

<div v-click class="mt-6 text-lg">

A unit-definition error, in expert material, found by review, producing a clean factor of
two. Everything this chapter teaches is in that sentence.

</div>

<Cite k="erratum2026" />

---

## What the erratum actually teaches

<v-clicks>

- **The expert was not careless.** The equation is correct as written; the error appears when someone substitutes a number defined differently.
- **Fluency did not help.** The lecture is lucid, and the error survived it.
- **Review worked** — but only because the denominator's definition was written down where a reader could check it.

</v-clicks>

<div v-click class="mt-6 text-lg">

You cannot check a claim whose terms are undefined. That is why the pass criterion in
this chapter comes **before** the output, not after.

</div>

---

## The minimal eval

<v-clicks>

- **Five fixed cases** from your own work, written down and frozen.
- **A pass criterion per case, defined before you look at any output.** Binary. Checkable without seeing the other condition.
- Run condition A. Run condition B. **Count.**

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Full specification, including the criterion-writing rules, is in
`assets/eval-worksheet/README.md`. You take a blank copy home.

</div>

---

## Choosing the five cases

<v-clicks>

- They must sit where the model is right **some** of the time. A case it always passes, or always fails, has **zero power to detect anything**, at any sample size.
- So calibrate first: write ten candidates, run each three times at baseline, discard anything scoring 3/3 or 0/3, keep the five nearest the middle.
- That costs about thirty runs and it is the difference between an eval that can detect something and one that cannot.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(instructor)** — the five cases, in mechanics, concrete or fluids, with a binary pass
criterion each. Not written here: a case invented by someone who does not know the
material comes out either trivially right or arguably wrong, and both destroy the exercise.

</div>

---

## The conditions

| | |
|---|---|
| **A** | baseline prompt |
| **A′** | the same baseline prompt, run again |
| **B1** | baseline + an expert persona |
| **B2** | baseline + an explicit instruction to work step by step |
| **B3** | baseline with extended thinking off |

<v-clicks>

- A′ is not a typo. It is the most important row in the table.
- B3 exists because the default configuration already reasons — without it, a null result on B2 has two readings and you cannot tell which.

</v-clicks>

---

## Why A′ exists

<v-clicks>

- Output is stochastic. Chapter 1 said so; you watched it in the temperature demo.
- One run per condition confounds the prompt effect with run-to-run spread.
- **A′ measures the spread with nothing changed.** If A and A′ disagree on two of five cases, an A-versus-B difference of two or fewer is inside the noise.

</v-clicks>

<div v-click class="mt-6 text-lg">

This is a repeatability check on an instrument. You would not accept a tank result
without one.

</div>

---

## Blinding, and what it does not achieve

<v-clicks>

- Strip the condition labels, rename outputs to opaque IDs, shuffle, and grade pass/fail only. Unblind afterwards.
- **Discard the thinking transcript at capture** — it is present under some arms and absent under B3, which identifies that arm with certainty.
- Insert a few duplicate outputs. They measure **grader** drift, which A′ does not.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**It is not a blind against the person who designed the conditions.** An answer produced
under *work step by step* tends to arrive in numbered steps — the manipulation and its
marker are nearly the same thing. Closing that needs a second grader, and there isn't one.
**So it gets disclosed, not solved.**

</div>

---

## What five cases can support

Paired sign test, ties dropped:

| Cases | Best possible split | Two-sided *p* |
|---|---|---|
| 5 | 5–0 | 0.0625 |
| 6 | 6–0 | 0.0313 |
| 10 | 10–0 | 0.0020 |
| 10 | 9–1 | 0.0215 |
| 10 | 8–2 | 0.1094 |

<v-clicks>

- Five cases **cannot** reach two-sided *p* < 0.05 under any outcome. Six is the minimum.
- Power at α = 0.05 is therefore **exactly zero** — combinatorial, not an estimate.

</v-clicks>

---

## And how weak the best case really is

Take a true effect of +20 percentage points against a 50% baseline — the most favourable
assumption available.

<v-clicks>

- Only about **2.5 of the five cases** are expected to be informative. The rest tie.
- A clean sweep occurs with probability 0.41 under that true effect, and 0.21 under no effect at all.
- **Likelihood ratio: 2.0.** The most convincing result this design can produce barely separates a real effect from nothing.
- For 80% power you would need roughly **93 cases**.

</v-clicks>

<div v-click class="mt-6 text-lg">

Say this **before** showing any result. This room is made of experimentalists; stating the
limit first is what buys credibility for everything after.

</div>

---

## So what is five cases for?

<v-clicks>

- **A screen.** It tells you whether an effect is large enough to justify a bigger eval.
- **A noise floor.** You learn how much your own instrument moves when nothing changes.
- **A habit.** You will never again say a prompt is better without knowing what you compared it to.

</v-clicks>

<div v-click class="mt-6 text-lg">

That is more than almost every prompting claim you will read this year has behind it.

</div>

---

## Two more traps

<v-clicks>

- **The noise floor is not a precise reading.** Two disagreements out of five gives a 95% interval of roughly (0.05, 0.85). Treat the rule as a conservative screen, not an instrument.
- **Three arms means three comparisons.** Family-wise, that is about a 14% chance one looks interesting by accident, not 5%. **Declare every arm**, including the boring ones.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Reporting only the interesting arm is post-hoc selection of the winning condition — and
doing that in a chapter about method would be self-refuting.

</div>

---

## The results

<div class="mt-4 p-5 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(capture)** — the instructor's eval, run in advance: five cases, five conditions,
twenty-five graded outputs, with the noise floor read first and every arm declared.

Header block to be filled before the run, not after: model ID, surface, thinking setting
and effort, date, fresh-session policy.

</div>

<div v-click class="mt-6 text-lg">

A demo where the folklore **loses** is worth more than one where it wins. So is a demo
where five cases cannot tell — which is the most likely outcome and the most honest one.

</div>

---

## Settling Chapter 3's first debt: the persona

<v-clicks>

- Chapter 3 was careful: the documentation claims a role focuses **behaviour and tone**. It never claimed accuracy.
- The published test of the accuracy claim: 162 roles, four model families, 2,410 factual questions. **Personas in system prompts did not improve performance** over no persona at all.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

And the finding that belongs in *this* chapter rather than that one: picking the best
persona **per question** does help — but identifying it in advance is **no better than
chance**. That is post-hoc selection of the winning condition, and it is exactly what your
own five cases will do to you if you let them.

</div>

<Cite k="zheng2024" />

---

## Settling the second: think step by step

<v-clicks>

- The original result: **eight worked chain-of-thought exemplars**, on a 540-billion-parameter model, with the ability stated to emerge in sufficiently large models.
- That is a result about supplying worked examples. It is not a result about typing four words at a model that already reasons before it answers.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**TODO(verify)** — a re-evaluation reporting little benefit from explicit chain-of-thought on
modern reasoning models is recorded at `[P]` and has not been read in full. It does not
reach this slide until it has been. Your own eval is the evidence you actually own.

</div>

<Cite k="wei2022" />

---

## Record the version, or you have recorded nothing

<v-clicks>

- Model ID and date, beside every result. A prompt has a shelf life and Chapter 5 explains why.
- The settings that change behaviour: thinking, effort, fresh session or not.
- **Re-test before you rely on it again.** A working prompt is a measurement, and measurements expire.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-75 border-t pt-3">

**Thread opened — verification.** Prompts here, sources in Chapter 14, arguments in Chapter
17, and the whole logging discipline in Chapter 18.

</div>

---

## Where this leaves us

<v-clicks>

- A method that fits on one page and turns a claim into a count.
- An honest account of what five cases cannot do, stated before the result rather than after.
- Two pieces of received wisdom, tested rather than repeated.

</v-clicks>

<div v-click class="mt-10 text-xl">

You can now measure whether something worked. **Chapter 5 is about what breaks anyway.**

</div>

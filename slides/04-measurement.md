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

<!--
- **Says:** Opens Chapter 4 as the method for testing the two claims Chapter 3 left open.
- **From:** Chapter 3 closed by deliberately leaving the persona and chain-of-thought claims untested.
- **Chapter:** States the chapter's purpose, converting the course from advice into a testing method, before any method is given.
- **To:** Leads into the slide diagnosing why prompting advice circulates as folklore.
-->

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

<!--
- **Says:** Diagnoses folklore prompting claims as a single run, judged against a pass criterion chosen after seeing the output, with no control condition.
- **From:** Follows the title slide by explaining the problem the chapter's method will fix.
- **Chapter:** Establishes the motivating failure mode before introducing the anchor example.
- **To:** Leads into the MACs-versus-FLOPs erratum as the chapter's anchor artefact.
-->

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

<!--
- **Says:** Recounts the MACs-versus-FLOPs erratum as a unit-definition error caught by an outside reader after publication.
- **From:** Follows the folklore-diagnosis slide with a concrete anchor example.
- **Chapter:** Delivers the chapter's anchor artefact, a peer-review success story with a clean numerical error.
- **To:** Sets up the next slide's lessons drawn from the erratum.
-->

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

<!--
- **Says:** Draws three lessons from the erratum, that the expert was not careless, fluency did not help, and review worked because terms were defined.
- **From:** Follows directly from the erratum's telling by extracting its lessons.
- **Chapter:** Motivates the requirement that a pass criterion be defined before output is seen.
- **To:** Leads into the minimal eval, the chapter's core method.
-->

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

<!--
- **Says:** States the three-step minimal eval, five fixed cases, a pre-defined pass criterion, and a count across two conditions.
- **From:** Follows the erratum's lesson about pre-defined criteria with the method that applies it.
- **Chapter:** Presents the chapter's core method in its simplest form.
- **To:** Leads into the next slide on choosing the five cases correctly.
-->

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

<!--
- **Says:** Explains that cases must be calibrated to sit near the middle of pass and fail, discarding cases the model always passes or fails.
- **From:** Follows the minimal-eval statement by detailing how to select its cases.
- **Chapter:** Adds the calibration step needed to give the minimal eval any statistical power.
- **To:** Leads into the table of experimental conditions.
-->

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

<!--
- **Says:** Tabulates the five experimental conditions A, A prime, B1, B2 and B3, and flags A prime and B3 as deliberate.
- **From:** Follows the case-selection slide by defining what is actually run against those cases.
- **Chapter:** Lays out the design that the next two slides justify in detail.
- **To:** Leads into the explanation of why A prime exists.
-->

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

<!--
- **Says:** Explains that A prime, a repeat of the baseline, measures run-to-run spread against which any A-versus-B difference must be judged.
- **From:** Follows the conditions table by justifying its most important row.
- **Chapter:** Ties the repeatability check back to Chapter 1's stochastic-sampling material.
- **To:** Leads into the blinding procedure applied to grading.
-->

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

<!--
- **Says:** Describes the blinding and duplicate-output procedure, and states plainly that it cannot blind the condition-designer's own bias.
- **From:** Follows the A-prime justification with the grading procedure applied to all conditions.
- **Chapter:** Adds an explicit, disclosed limitation to the method rather than overselling it.
- **To:** Leads into the statistical limits of what five cases can support.
-->

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

<!--
- **Says:** Tabulates sign-test p-values by case count, showing five cases cannot reach two-sided p under 0.05 at any outcome.
- **From:** Follows the blinding slide by quantifying the method's statistical power.
- **Chapter:** States the eval's central statistical limitation before any result is shown.
- **To:** Leads into a worked example of how weak even the best-case outcome is.
-->

---

## And how weak the best case really is

Take a true effect of +20 percentage points against a 50% baseline — the most favourable
assumption available.

<v-clicks>

- Only about **2.5 of the five cases** are expected to be informative. The rest tie.
- *No case contradicts B* occurs with probability 0.41 under that true effect and 0.21 under no effect. **Likelihood ratio 2.0** — and that outcome is mostly ties, so it is not the best result available.
- The genuinely best result is the 5–0 row in the table opposite: five informative cases, all favouring B. **Likelihood ratio 5.4.**
- But a real +20-point effect produces that outcome only **0.5% of the time**. The design's best case is both weak evidence *and* almost never obtained.
- For 80% power you would need **103 cases** — exactly, by the same sign test. The normal approximation says 93; the discreteness of the exact test costs the other ten.

</v-clicks>

<div v-click class="mt-6 text-lg">

Say this **before** showing any result. This room is made of experimentalists; stating the
limit first is what buys credibility for everything after.

</div>

<!--
- **Says:** Works a concrete twenty-point true-effect scenario, showing the best outcome is both weak evidence and rarely obtained, needing 103 cases for 80% power.
- **From:** Follows the p-value table by working through a concrete numerical example of its consequence.
- **Chapter:** Reinforces, with numbers, the instruction to state the limit before showing any result.
- **To:** Leads into the slide answering what five cases are actually good for.
-->

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

<!--
- **Says:** States that five cases serve as a screen, a noise floor, and a habit rather than a definitive finding.
- **From:** Follows the weak-best-case analysis by reframing what the method is actually useful for.
- **Chapter:** Reframes the eval positively after two slides establishing its statistical weakness.
- **To:** Leads into two further traps in interpreting the eval's results.
-->

---

## Two more traps

<v-clicks>

- **The noise floor is not a precise reading.** Two disagreements out of five gives a 95% interval of roughly (0.05, 0.85). Treat the rule as a conservative screen, not an instrument.
- **Three arms means three comparisons.** And the per-arm rate cannot be 5%, because two slides ago you proved five cases have no 5% rejection region at all. At the only level actually attainable, 0.0625 per arm, three arms give a family-wise rate of about **18%**. **Declare every arm**, including the boring ones.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Reporting only the interesting arm is post-hoc selection of the winning condition — and
doing that in a chapter about method would be self-refuting.

</div>

<!--
- **Says:** Warns that the noise floor is imprecise, and that three arms inflate the family-wise error rate to about 18% regardless of how they are reported.
- **From:** Follows the reframing slide with two additional interpretive cautions.
- **Chapter:** Closes the method-design material before the instructor's own results are shown.
- **To:** Leads into the placeholder slide for the instructor's own eval results.
-->

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

<!--
- **Says:** Marks where the instructor's own five-case, five-condition eval results are to be inserted, with a header block of run metadata.
- **From:** Follows the interpretive traps by presenting where the worked example itself will go.
- **Chapter:** Reserves the slide where the chapter's method is demonstrated on a real run.
- **To:** Leads into settling the first of Chapter 3's two open claims.
-->

---

## Settling Chapter 3's first debt: the persona

<v-clicks>

- Chapter 3 was careful: the documentation claims a role focuses **behaviour and tone**. It never claimed accuracy.
- The published test of the accuracy claim: 162 roles, four model families, 2,410 factual questions. **Personas in system prompts did not improve performance** over no persona at all.
- **Its scope, in the source's own terms:** those model families, that question set. Not Opus 5, and not civil engineering. It is evidence against the folk claim, not a measurement of your task.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

And the finding that belongs in *this* chapter rather than that one: picking the best
persona **per question** does help — but identifying it in advance is **no better than
chance**. That is post-hoc selection of the winning condition, and it is exactly what your
own five cases will do to you if you let them.

</div>

<Cite k="zheng2024" />

<!--
- **Says:** Reports a published study of 162 roles across four model families finding personas did not improve accuracy, with its scope stated explicitly.
- **From:** Follows the results placeholder by applying the chapter's evidentiary standard to Chapter 3's persona claim.
- **Chapter:** Resolves one of the two claims Chapter 3 deliberately left open.
- **To:** Leads into settling the second open claim, chain-of-thought prompting.
-->

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

<!--
- **Says:** Distinguishes the original chain-of-thought result, based on worked exemplars, from the folk instruction to a model that already reasons.
- **From:** Follows the persona slide by settling the second claim Chapter 3 left open.
- **Chapter:** Resolves the second open claim while marking a re-evaluation source as not yet read or citable.
- **To:** Leads into the closing instruction to record model version alongside any result.
-->

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

<!--
- **Says:** Instructs recording model ID, date and settings alongside every result, and forward-references Chapter 5 on why prompts expire.
- **From:** Follows the two settled claims with the discipline needed to keep any future result valid.
- **Chapter:** Opens the verification thread that later chapters extend.
- **To:** Leads into the chapter's closing summary slide.
-->

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

<!--
- **Says:** Closes the chapter by summarising the method, its honest limits, and the two folk claims it tested.
- **From:** Follows the version-recording slide by summarising the whole chapter.
- **Chapter:** Delivers the chapter's closing summary before handing off to failure modes.
- **To:** Chapter 5 covers what breaks even when a technique has been correctly measured to work.
-->


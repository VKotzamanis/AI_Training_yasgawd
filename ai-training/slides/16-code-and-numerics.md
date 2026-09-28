---
theme: default
title: Chapter 16 — Code and numerics
info: The audience's daily work. Carries a demonstrated weakness on MATLAB, shown live rather than asserted.
class: text-left
mdc: true
---

# Chapter 16 — Code and numerics

### The audience's daily work

<div class="mt-10 text-xl opacity-85">

This is the chapter closest to what you actually do on a Tuesday, and the one where the
tool is weakest at exactly the thing you need most.

</div>

<!--
- **Says:** The title slide frames Chapter 16 as the audience's daily work and previews that the tool is weakest at exactly the task they need most.
- **From:** Chapter 15 closed by saying Chapter 16 takes the same explanation-versus-behaviour check onto code the audience inherited rather than wrote.
- **Chapter:** Opens the chapter with the framing that recurs through it, that this is where the tool's weakness costs the most.
- **To:** Sets up the first daily-work scenario, working with an inherited, undocumented script.
-->

---

## Inherited code

A script from a student who graduated, no comments, and a result you have to defend.

<v-clicks>

- Ask for an explanation **before** asking for a change. You are buying a map, not a repair.
- Check the explanation against the code's behaviour, not against its variable names. Names lie; behaviour does not.
- The parts it explains confidently and wrongly are the parts to read yourself first.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

The output of this step is a project instruction file entry, per Chapter 10 — so the
next person does not pay the same cost.

</div>

<!--
- **Says:** Gives a three-step protocol for inherited, undocumented code — get an explanation before requesting a change, check that explanation against the code's actual behaviour rather than its variable names, and read the confidently-wrong parts yourself — and routes the result into a Chapter 10 project instruction file entry.
- **From:** Follows the title slide's framing by opening with the first concrete daily-work task it promised.
- **Chapter:** Delivers the explanation-before-edit protocol that Chapter 15's closing slide named as this chapter's opening move.
- **To:** Sets up the MATLAB-versus-Python weakness the next slide demonstrates.
-->

---

## A weakness worth showing you

<div class="mt-4 text-xl">

Model performance on MATLAB is materially worse than on Python.

</div>

<v-clicks>

- You will feel this on your own code, so it is better heard here than discovered alone.
- **Shown live, not asserted.** Same task, both languages, side by side, on the day.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(capture)** — instructor records the demonstration in advance: **several tasks, and
more than one run of each**, with model ID and date. One task at one run per language is
the design Chapter 4 spent forty minutes forbidding, and this room will remember that.
Report what was measured rather than asserting "materially worse" in advance — if the gap
is smaller than expected, that is the finding.

</div>

<div v-click class="mt-4 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**Keep the observation and the explanation apart.** That the gap exists is demonstrable in
the room. That it is caused by how much MATLAB appears in training corpora is a
**hypothesis** — plausible, widely repeated, and not established on this slide.
`TODO(cite)` — search: `MATLAB code generation LLM evaluation benchmark`.

</div>

<!--
- **Says:** States that model performance on MATLAB is materially worse than on Python, commits to showing this live with a multi-task, multi-run instructor demonstration recorded in advance, and separately flags the training-corpus explanation as an unestablished, TODO(cite) hypothesis rather than a demonstrated cause.
- **From:** Follows the inherited-code protocol by turning to a second daily-work reality, that the tool itself performs unevenly across the two languages.
- **Chapter:** Carries the chapter's demonstrated-weakness content while explicitly keeping the demonstrable performance gap separate from the unestablished causal hypothesis about training corpora.
- **To:** Sets up the next slide's argument for why showing this weakness helps rather than hurts.
-->

---

## Why admitting that helps

<v-clicks>

- A limitation that costs the instructor something is the cheapest credibility available.
- It also gives you a decision rule: prototype in whichever language the tool is strong in, then port deliberately, or stay in MATLAB and budget more review.
- And it is the Chapter 4 lesson again — measure it on your own tasks rather than believing either me or the vendor.

</v-clicks>

<!--
- **Says:** Explains that a costly admitted limitation buys credibility, yields a decision rule for choosing which language to prototype in, and repeats the Chapter 4 instruction to measure the claim on your own tasks.
- **From:** Follows directly from the MATLAB-weakness slide by explaining why demonstrating rather than concealing that weakness benefits the audience.
- **Chapter:** Reinforces the course's credibility-through-limitation stance and reactivates the Chapter 4 measurement habit.
- **To:** Sets up the concrete translation guidance that follows.
-->

---

## Translation between MATLAB and Python

<v-clicks>

- Indexing base, array copy semantics, and default numeric types are where translations break silently.
- A translated script that runs is not a translated script that agrees. **Compare outputs on a case with a known answer** before trusting it on one without.
- Translation is a good use of the tool precisely because the check is cheap and mechanical.

</v-clicks>

<!--
- **Says:** Names indexing base, array copy semantics and default numeric types as where translations break silently, and calls for comparing outputs on a known-answer case before trusting a translated script.
- **From:** Follows the language-weakness discussion by turning to the concrete task of moving code between the two languages.
- **Chapter:** Gives the chapter's first hands-on numerical-code practice, translation checked against a known answer.
- **To:** Leads into vectorisation and performance as the next code-transformation task.
-->

---

## Vectorisation and performance

<v-clicks>

- Ask for the vectorised form, then time both. The rewrite is often right and occasionally slower.
- Profile before optimising. Chapter 7's lesson generalises: find the binding constraint before working on anything.
- A vectorised rewrite **can** change results — floating-point addition is not associative, and vectorising reorders the reductions. The change is not confined to edge cases; it is wherever the summation order moved. Compare against the original, not against intuition.

</v-clicks>

<!--
- **Says:** Covers requesting and timing a vectorised rewrite, profiling before optimising, and warns that vectorisation can change numerical results because floating-point addition is not associative.
- **From:** Follows translation practice by moving to a second code-transformation task, vectorisation.
- **Chapter:** Extends the chapter's numerical caution from translation to performance rewrites, tying the profiling advice back to Chapter 7.
- **To:** Sets up the tests-for-numerical-code slide that follows.
-->

---

## Tests for numerical code

<v-clicks>

- **Tolerance is a choice you must justify.** A test passing at `1e-6` and failing at `1e-9` is telling you something about your method, not about the test.
- Prefer checks the physics gives you free: conservation, closure, symmetry, known limits, convergence under refinement.
- A test the tool wrote and you did not read is not a test. It is a second thing to debug.

</v-clicks>

<div v-click class="mt-6 text-lg">

State the check before you run the work. It is the same demand Chapter 4 made of a prompt
and Chapter 14 made of a citation, arriving here for a tolerance.

</div>

<!--
- **Says:** Argues that a test's tolerance is a choice that must be justified, recommends checks the physics supplies for free such as conservation and known limits, and states that a generated test nobody read is not a test.
- **From:** Follows the vectorisation slide's warning about changed results by giving the testing discipline needed to catch such changes.
- **Chapter:** Applies the course's state-the-check-first rule, explicitly echoing Chapter 4 and Chapter 14, to numerical tolerance.
- **To:** Leads into the units, signs and coordinate-systems slide.
-->

---

## Units, signs and coordinate systems

<v-clicks>

- The failure class most likely to survive review, because the code runs and the plot looks fine.
- Annotate them in comments, at the point of definition — not in a document nobody opens.
- Put them in the project instruction file so every future session inherits them.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Review cannot catch a sign error that nobody wrote down. That is true of human reviewers
and it is true of this tool.

</div>

<!--
- **Says:** Names units, signs and coordinate systems as the failure class most likely to survive review because the code still runs and the plot still looks fine, and calls for annotating them in code comments and the project instruction file.
- **From:** Follows the testing slide by naming the specific failure category that a passing test can still miss.
- **Chapter:** Closes the chapter's content slides on the sign-and-unit-convention discipline central to this audience's work.
- **To:** Leads into the closing exercise slide.
-->

---

## Exercise

<v-clicks>

1. Take an inherited script. Get an explanation and check it against behaviour.
2. Write one test with a tolerance you can justify out loud.
3. Add the units and sign conventions to your project instruction file.

</v-clicks>

<!--
- **Says:** Sets the closing exercise — check an inherited script's explanation against its behaviour, write one tolerance-justified test, and add units and sign conventions to the project instruction file.
- **From:** Follows the units-and-signs slide by turning its practices into a hands-on task.
- **Chapter:** Closes Chapter 16 by having attendees perform the chapter's practices themselves rather than only hear them described.
- **To:** Hands off to Chapter 17, which turns this same self-checking habit from code and tests onto a written argument.
-->

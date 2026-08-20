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

**TODO(capture)** — instructor to record the paired demonstration in advance, with model ID
and date, so the point survives a bad live run.

</div>

<div v-click class="mt-4 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**Keep the observation and the explanation apart.** That the gap exists is demonstrable in
the room. That it is caused by how much MATLAB appears in training corpora is a
**hypothesis** — plausible, widely repeated, and not established on this slide.
`TODO(cite)` — search: `MATLAB code generation LLM evaluation benchmark`.

</div>

---

## Why admitting that helps

<v-clicks>

- A limitation that costs the instructor something is the cheapest credibility available.
- It also gives you a decision rule: prototype in whichever language the tool is strong in, then port deliberately, or stay in MATLAB and budget more review.
- And it is the Chapter 4 lesson again — measure it on your own tasks rather than believing either me or the vendor.

</v-clicks>

---

## Translation between MATLAB and Python

<v-clicks>

- Indexing base, array copy semantics, and default numeric types are where translations break silently.
- A translated script that runs is not a translated script that agrees. **Compare outputs on a case with a known answer** before trusting it on one without.
- Translation is a good use of the tool precisely because the check is cheap and mechanical.

</v-clicks>

---

## Vectorisation and performance

<v-clicks>

- Ask for the vectorised form, then time both. The rewrite is often right and occasionally slower.
- Profile before optimising. Chapter 7's lesson generalises: find the binding constraint before working on anything.
- A vectorised rewrite changes numerical behaviour at the edges. Check the edges.

</v-clicks>

---

## Tests for numerical code

<v-clicks>

- **Tolerance is a choice you must justify.** A test passing at `1e-6` and failing at `1e-9` is telling you something about your method, not about the test.
- Prefer checks the physics gives you free: conservation, closure, symmetry, known limits, convergence under refinement.
- A test the tool wrote and you did not read is not a test. It is a second thing to debug.

</v-clicks>

<div v-click class="mt-6 text-lg">

State the check before you run the work. That sentence has appeared in every chapter of
this course and it is the same sentence here.

</div>

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

---

## Exercise

<v-clicks>

1. Take an inherited script. Get an explanation and check it against behaviour.
2. Write one test with a tolerance you can justify out loud.
3. Add the units and sign conventions to your project instruction file.

</v-clicks>

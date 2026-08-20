---
theme: default
title: Chapter 14 — Literature
info: Finding, screening and citing without fabricating. Closes the truthfulness thread as a work habit.
class: text-left
mdc: true
---

# Chapter 14 — Literature

### Finding, screening and citing without fabricating

<div class="mt-10 text-xl opacity-85">

The highest-demand capability in this room, and the one with the most ways to go
quietly wrong.

</div>

---

## Start from the failure gallery

By this point in the course you will have seen a fabricated citation from your own field,
and what it took to catch it.

<v-clicks>

- It was fluent. It had plausible authors, a plausible year, and a plausible venue.
- It was caught by resolving the identifier, not by reading the sentence.
- Chapter 5 explained why: the middle band of model knowledge, where it believes it knows.

</v-clicks>

<div v-click class="mt-6 text-lg">

Everything in this chapter is downstream of that one demonstration.

</div>

---

## What survives PDF extraction, and what does not

<v-clicks>

- **Two-column layouts** interleave. Text from the left column and the right can arrive as one sentence that neither column contains.
- **Equations** degrade badly. Sub- and superscripts flatten, symbols are substituted, and the result is often syntactically plausible and numerically wrong.
- **Tables** lose their structure. A number can migrate a column.

</v-clicks>

<div v-click class="mt-6 text-lg">

**Check the extraction before you reason about the content.** A wrong number extracted
cleanly looks exactly like a right one.

<div class="mt-3 text-sm opacity-80">

These failure modes are **extractor-dependent** — they are not properties of PDFs. Name the
tool you used when you report them, and re-check when you change it. `TODO(capture)` — run
one extraction live on a two-column paper with equations rather than describing it.

</div>

</div>

<div v-click class="mt-4 text-sm opacity-80">

This is Chapter 4's discipline applied to a file format: verify the intermediate step
before interpreting the result.

</div>

---

## Reference managers and the document pipeline

<v-clicks>

- Keep one source of truth for bibliography data, and export from it. Retyping a reference is how a wrong year enters a paper.
- Choose an export format that survives your document pipeline, and test it on one reference before you have three hundred.
- The identifier — DOI, arXiv ID — is the field that matters. Author and year are convenience; the identifier is the thing you can check.

</v-clicks>

---

## Screening against stated criteria

<v-clicks>

- Write the inclusion and exclusion criteria **before** you screen. Same rule as the eval in Chapter 4, and for the same reason.
- Screening is a classification task with a defined answer, which makes it one of the few literature tasks that can be checked.
- **Papers get silently dropped.** A screening pass returns what it returns; it does not report what it failed to consider.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

So screen a known subset first — twenty papers where you already know the answer — and
measure the false-negative rate before trusting it on the ones you have not read.
That is a five-case eval wearing different clothes.

</div>

---

## Summarising without laundering

<v-clicks>

- A summary that drops the authors' stated scope converts a bounded finding into a general claim. That is laundering, and it is usually accidental.
- The scope sentence is the one most often lost: which models, which dataset, which conditions.
- **Keep the hedge.** If the authors wrote "suggests", you do not get to write "shows".

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

You have seen this failure in this course already: a hardware result, true on a specific
benchmark, circulating as though the technology were deployed. Chapter 7 corrected it in
front of you.

</div>

---

## The habit that closes the thread

<div class="mt-6 p-5 border-l-4 text-xl" style="border-color:#0E5C68; background:#F2F7F8">

**Every citation is verified against a primary identifier. No exceptions.**

</div>

<v-clicks>

- Resolve the DOI or the arXiv ID. Open the record. Confirm the title, the authors and the year.
- A citation you have not resolved is a candidate, not a reference.
- It costs a few seconds per source once the habit is formed, and it is the entire defence.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-75 border-t pt-3">

**Thread — truthfulness.** Introduced in Chapter 2 as a rated rubric dimension, explained
in Chapter 5 as a structural property rather than a bug, and closed here **for citations** —
the one part of the problem with a mechanical check. The general case does not close: a
fluent, uncitable, wrong sentence has no identifier to resolve. That is what Chapter 17 is
for.

</div>

---

## Exercise

<v-clicks>

1. Take a paper you know well. Extract it and check what survived — equations first.
2. Ask for a summary. Find the scope sentence in the original and check whether it survived.
3. Ask for five references on a narrow question in your field. **Resolve every identifier.** Record how many were real, how many were real but said something else, and how many did not exist.

</v-clicks>

<div v-click class="mt-6 text-lg">

Step 3 is the one you will remember. Write the numbers down — they are your own failure
gallery, and they are more persuasive to you than anyone else's.

</div>

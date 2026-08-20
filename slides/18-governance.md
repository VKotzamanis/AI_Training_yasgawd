---
theme: default
title: Chapter 18 — Governance
info: Disclosure, data, reproducibility and lab standards. Closes the trust boundary and verification threads. Journal policy section blocked on which journals the group publishes in.
class: text-left
mdc: true
---

# Chapter 18 — Governance

### Disclosure, data, reproducibility, lab standards

<div class="mt-10 text-xl opacity-85">

Much of what Part II identified as a risk appears here as documented practice. Where it does not, this chapter says so.

</div>

---

## Disclosure — against your actual policies

<div class="mt-4 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**BLOCKED — needs the list of journals this group actually publishes in.**

This section ships the **current text of the named policies**, not a generic summary.
Policies change, and secondhand summaries go stale in a way that is invisible until a
desk rejection. `DECISIONS.md` item 7.

ASCE is expected to matter most for this cohort. `TODO(cite)` — publisher policies, plus
COPE and ICMJE position statements, all currently `[U]`. Whether generic guides omit ASCE
is an impression, not a checked claim, and is not asserted here.

</div>

<div v-click class="mt-6 text-lg">

The structure below holds regardless of which journals they turn out to be.

</div>

---

## The three questions every policy answers

These are the **questions to put to each policy**, not answers this deck can supply.

<v-clicks>

- **Does this use require disclosure at all?** Find the threshold. It is set per publisher and it is not obvious.
- **Where does the statement go?** Methods, acknowledgements, or a dedicated section — and a manuscript can be desk-rejected on the wrong one.
- **What is prohibited outright rather than merely disclosed?** Read the prohibition, do not infer it.
- **What must be retained** — prompts, drafts, logs — and for how long?

</v-clicks>

<div v-click class="mt-5 text-sm opacity-80">

Answering these from memory is what the block on the previous slide exists to prevent. The
only slide in this section that does not need a policy is the next one, because it argues
from what the word *author* means.

</div>

---

## Why a tool cannot be an author

<v-clicks>

- Authorship is a claim of **accountability**, not a record of who typed.
- An author can be asked to defend the work, produce the data, and answer for an error. A tool can do none of those.
- So the prohibition is not squeamishness about novelty. It follows from what the word means.

</v-clicks>

<div v-click class="mt-8 text-xl">

Three things are never delegable: **the claim, the interpretation, and the responsibility
for correctness.**

</div>

<div v-click class="mt-3 opacity-80">

Everything else in this course is negotiable. Those three are not, and no disclosure
statement transfers them.

</div>

---

## Data governance

<v-clicks>

- Unpublished experimental data. Sponsor NDAs. Confidential geometry. Anything under embargo.
- The question is not "is this tool secure". It is **what left the building, and can you say so precisely.**
- Chapter 12's distinction returns and it is load-bearing: on a document graph, the code pass is local while the **semantic pass over documents leaves the machine.** Two features of one tool, two different answers.
- That was confirmed by running the tool at a pinned version, not read off a webpage. **Re-check it on upgrade** — it is the factual basis for what you are about to decide is safe to process locally.

</v-clicks>

<Cite k="graphify" />

<div v-click class="mt-6 text-lg">

Write the rule down before you need it. A rule decided under deadline pressure is decided
in favour of the deadline.

</div>

---

## Reproducibility

<div class="mt-4 text-xl">

Stochastic output cannot be reproduced by re-running the prompt.

</div>

<v-clicks>

- Chapter 1 explained why — sampling from a distribution, and Chapter 4 measured the spread it produces.
- So "I asked it and it said" is not a method section. It is an anecdote with a timestamp missing.

</v-clicks>

<div v-click class="mt-6">

**What must therefore be logged**, every time output informs a result:

</div>

<v-clicks>

- The exact prompt, including any standing instruction file in force
- The model ID and the date
- The settings that change behaviour — thinking, effort, whether the session was fresh
- What you did with the output, and what you checked

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Version control is the record. It timestamps, it diffs, and it is already in your workflow.

</div>

---

## Lab-level standardisation

The step that turns six individually capable people into a group with shared
infrastructure.

<v-clicks>

- **One shared project instruction file**, reviewed like code — not six private ones that disagree.
- **Agreed conventions**: units, sign conventions, coordinate systems, and the definition of every derived quantity the group reports.
- **Committed skills**, so a procedure survives the person who wrote it.
- **A shared code and document map**, so everyone queries the same picture.
- **A source rule**: which documents may be opened in a session that can read your files, and who signs off the exceptions.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

This is Chapter 10's artefact, promoted from a personal convenience to a group standard.

</div>

---

## Two threads close here

<v-clicks>

- **Trust boundary** — trained harmlessness in Chapter 2, hostile input in Chapter 6, channels opened deliberately in Chapter 12, governed here in **both directions**: a data rule for what leaves, and a source rule for what is allowed in.
- The inbound half is the one people forget. Name which sources may be read into a session that has file access, and who approves an exception. Chapter 6 showed why: instructions and data share one channel, and there is no complete defence.
- **Verification** — prompts in Chapter 4, sources in Chapter 14, arguments in Chapter 17, and here as logging and reproducibility.

</v-clicks>

<div v-click class="mt-6 text-lg">

Both threads end in the same place: **something written down that someone else can check.**

</div>

---

## Exercise

<v-clicks>

1. Write your group's data rule. One page. What may leave the machine, what may not, and who decides the ambiguous case.
2. Write the disclosure sentence you will use, before you need it.
3. Agree one convention as a group today and put it in the shared instruction file.

</v-clicks>

<div v-click class="mt-6 text-lg">

Step 3 is the whole chapter. A convention agreed and not written down is a convention
that does not exist.

</div>

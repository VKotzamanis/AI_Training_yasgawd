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

<!--
- **Says:** The title slide frames Chapter 18 as converting Part II's risks into documented practice, while flagging that some sections cannot yet do so.
- **From:** Chapter 17 closed on ranking self-generated objections and named disclosure as a question this chapter would make concrete against the actual policies attendees write under.
- **Chapter:** Opens the chapter that the course architecture marks as closing both the trust-boundary and verification threads.
- **To:** Sets up the disclosure section, presented as blocked rather than populated.
-->

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

<!--
- **Says:** Marks the disclosure section BLOCKED pending the list of journals the group actually publishes in, naming ASCE as the expected but unconfirmed candidate with every citation still tagged [U].
- **From:** Follows the title slide's flagged gap by presenting the disclosure section itself as unresolved rather than populated.
- **Chapter:** Is the slide the production brief calls out as blocked, withholding policy content instead of asserting it, consistent with the project's citation-verification rule.
- **To:** Sets up the generic questions the deck can still put to any policy once one is named.
-->

---

## The four questions every policy answers

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

<!--
- **Says:** Lists the questions to put to any named policy — the disclosure threshold, where the statement goes, what is prohibited outright, and what must be retained — as questions this deck poses rather than answers it supplies.
- **From:** Follows the blocked disclosure slide by giving the framework to apply once the journal list is known.
- **Chapter:** Turns the disclosure gap left open by the previous slide into a reusable checklist.
- **To:** Leads into the one slide in this section that needs no named policy, because it argues from what "author" means instead.
-->

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

<!--
- **Says:** Argues from authorship as a claim of accountability rather than a record of who typed to conclude a tool cannot be an author, and names the claim, the interpretation, and the responsibility for correctness as never delegable.
- **From:** Follows the policy-questions slide exactly as that slide's own closing line promised, arguing from what "author" means rather than from any named policy.
- **Chapter:** States the chapter's non-negotiable core, the three things no disclosure statement can transfer.
- **To:** Sets up the data-governance slide that follows.
-->

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

<!--
- **Says:** Reframes data governance around what left the building rather than whether the tool is secure, and restates Chapter 12's distinction between the local code pass and the semantic pass over documents that leaves the machine, verified at a pinned version.
- **From:** Follows the authorship slide by moving from what can never be delegated to what data can never leave the machine.
- **Chapter:** Carries the trust-boundary thread's outbound half forward with its own citation footer, ahead of the explicit thread closure three slides later.
- **To:** Leads into the reproducibility slide.
-->

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

<!--
- **Says:** States that stochastic output cannot be reproduced by re-running a prompt, and lists what must be logged instead — the exact prompt, the model ID and date, the settings that change behaviour, and what was checked.
- **From:** Follows the data-governance slide by turning from what leaves the machine to what must be recorded about what happens inside it.
- **Chapter:** Develops the verification thread's logging content that the later two-threads slide names as this chapter's closure, tying back to Chapter 1's sampling explanation and Chapter 4's measured spread.
- **To:** Sets up the lab-level standardisation slide.
-->

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

<!--
- **Says:** Lists five practices that convert individual capability into shared lab infrastructure — a shared instruction file, agreed conventions, committed skills, a shared code map, and a source rule for what may be opened into a session.
- **From:** Follows the reproducibility slide by moving from individual logging practice to group-level standardisation.
- **Chapter:** Promotes Chapter 10's personal project instruction file into a group standard, as the slide states directly.
- **To:** Leads into the slide naming the two threads this chapter closes.
-->

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

<!--
- **Says:** Names the two threads the chapter closes — trust boundary, governed here in both the outbound data rule and the inbound source rule, and verification, closed here as logging and reproducibility.
- **From:** Follows the lab-standardisation slide by naming the source rule just introduced as the inbound half of the trust-boundary thread.
- **Chapter:** Is the deck's explicit closure of both the trust-boundary and verification threads that the course architecture tracks.
- **To:** Sets up the closing exercise slide.
-->

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

<!--
- **Says:** Closes the chapter with an exercise to write the group's data rule, write a disclosure sentence in advance, and agree one convention today.
- **From:** Follows the two-threads slide by turning both closed threads into three concrete, time-boxed actions.
- **Chapter:** Ends Chapter 18 on the same write-it-down imperative that ran through the whole chapter.
- **To:** Hands off to Chapter 19, the capstone, where attendees bring this chapter's written disclosure position into their end-to-end task.
-->

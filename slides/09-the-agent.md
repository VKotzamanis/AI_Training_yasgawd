---
theme: default
title: Chapter 9 — The agent
info: Working with a system that acts. Context engineering as the named skill that separates competent from incompetent use.
class: text-left
mdc: true
---

# Chapter 9 — The agent

### Working with a system that acts

<div class="mt-10 text-xl opacity-85">

Session 1 was a system that answers. This one edits your files.

</div>

<!--
- **Says:** Opens Chapter 9 by contrasting Session 1's answering system with Session 2's file-editing agent.
- **From:** Chapter 8 closed Session 1 on the line that the model has no hippocampus and hands over a system that acts.
- **Chapter:** Frames the chapter's subject as working with an agent rather than a chat interface.
- **To:** Sets up the choice of entry point -- desktop app before terminal -- on the next slide.
-->

---

## Start where the barrier is lowest

<v-clicks>

- **Desktop app and the editor extension first.** The terminal is optional and it is taught last.
- A browser fallback exists for a machine that fights the install. Nobody in this room should lose the afternoon to a package manager.
- The terminal is not the skill. The skill is everything on the following slides, and it is identical in all three.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-80">

Terminal-first teaching filters for people who already have the tool. This room does not,
and the filter would remove the audience rather than the difficulty.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** Recommends the desktop app and editor extension over the terminal as the lowest-barrier entry points, with a browser fallback.
- **From:** Follows the opening framing by addressing the practical question of how to start.
- **Chapter:** Sets the chapter's teaching order for an audience without existing terminal fluency.
- **To:** Leads into the permission model that governs what the agent may do once running.
-->

---

## The permission model is the safety story

<v-clicks>

- Read-only by default. Nothing is written until you say so.
- Every proposed edit is shown as a **diff** before it is applied.
- Permissions are per action, and can be narrowed or broadened per project.

</v-clicks>

<div v-click class="mt-6 text-lg">

**The diff is the artefact of responsibility.** It is the moment the change becomes
yours. Approving a diff you have not read is the whole risk of this chapter in one action.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** Describes the read-only default, per-action permissions, and the diff as the moment a change becomes the user's own.
- **From:** Follows the entry-point slide once the agent is running, by covering what it is allowed to do.
- **Chapter:** States the chapter's core safety claim, that the diff is the artefact of responsibility.
- **To:** Sets up the working-loop diagram that places the diff inside a repeatable cycle.
-->

---

## The working loop

```mermaid {scale: 0.72}
flowchart LR
  A["ask"] --> B["plan"]
  B --> C["edit"]
  C --> D["review<br/>the diff"]
  D -->|"accept"| E["committed<br/>change"]
  D -->|"reject"| B
```

<v-clicks>

- **Plan before edit.** Plan mode produces the intended change as text, before a single file is touched, and it is far cheaper to reject a plan than a patch.
- The loop is the same whether the task takes one turn or forty.

</v-clicks>

<Cite k="claudecode-docs" />

<!--
- **Says:** Diagrams the ask-plan-edit-review loop and notes plan mode makes rejecting a plan cheaper than rejecting a patch.
- **From:** Follows the permission-model slide by placing the diff review inside the full repeatable cycle.
- **Chapter:** Gives the chapter's procedural skeleton, later reused at scale in Chapter 11's plan-mode slide.
- **To:** Leads into context engineering, the skill the chapter treats as central.
-->

---

## Context engineering is the skill

Not a footnote. This is the single thing that separates competent agent use from
incompetent agent use.

<v-clicks>

- Everything in the session shares one bounded window — your files, the outputs, the tool results, the conversation.
- It fills. Chapter 5 told you what happens to accuracy as it fills, and Chapter 7 told you what it costs.
- Nothing warns you at the moment it starts mattering.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-75 border-t pt-3">

**Thread — memory and context.** Introduced in Chapter 1 as a bounded buffer, watched
degrading in Chapter 5, named as the missing hippocampus in Chapter 8. This is where you
manage it. Chapter 10 is where you replace it.

</div>

<!--
- **Says:** Names context engineering as the single skill separating competent from incompetent agent use, since the shared window fills silently.
- **From:** Follows the working loop by addressing what happens to it as the session's window fills.
- **Chapter:** Carries the memory-and-context thread explicitly, naming it the chapter's central skill rather than a footnote.
- **To:** Sets up the three specific moves for managing that window.
-->

---

## Three moves, and knowing which one

<v-clicks>

- **Compact** — summarise the session so far and continue. Cheap *relative to continuing on a full window*, but not free: the summarising call itself reads the whole context, which by Chapter 7 is the most expensive call available at that moment. Lossy, and the loss is invisible.
- **Clear** — discard and start fresh in the same project. Loses everything not written to a file.
- **Abandon** — start a new session because this one has gone wrong in a way summarising will not fix.

</v-clicks>

<div v-click class="mt-6 text-lg">

The third is the one people will not do, because the session feels expensive to lose.
It is not. **It has already cost you the thing you were protecting.**

</div>

<!--
- **Says:** Defines compact, clear, and abandon as the three moves for managing a filling context window, and flags abandon as underused.
- **From:** Follows the naming of context engineering with the concrete moves that implement it.
- **Chapter:** Operationalises the chapter's central skill into three named actions.
- **To:** Leads into a demonstration of what contamination from a full window looks like.
-->

---

## Demonstration: what contamination looks like

<v-clicks>

- Run one task in a fresh session, **three times**. Record the answers.
- Run the same task after a long, unrelated conversation in the same session, **three times**. Record those.
- Put the two sets side by side and look at the spread, not at one pair.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(capture)** — instructor records both sets in advance, with model ID and date.

</div>

<div v-click class="mt-4 p-4 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**Say what this is.** Six runs is an **illustration**, not a measurement — it is under the
floor Chapter 4 set, and Chapter 4 is the reason you know that. Running one pair and
declaring a difference would be the exact design that chapter spent forty minutes
forbidding. If the two sets overlap completely, say so; that is a result too.

</div>

<!--
- **Says:** Describes a six-run comparison, fresh session against long-conversation session, explicitly flagged as illustration rather than measurement.
- **From:** Follows the three moves by showing why managing context matters in practice.
- **Chapter:** Applies Chapter 4's evaluation discipline to the chapter's own demonstration rather than exempting it.
- **To:** Sets up the session-commands slide that follows the demonstration.
-->

---

## Session commands worth knowing on day one

<v-clicks>

- **`/doctor`** — a setup checkup that diagnoses, and can fix, installation and configuration problems. `/checkup` is an alias for it. Reach for it when behaviour is odd, *before* you start debugging the thing you were working on.
- **Check your usage early** in the session, not when you hit a limit mid-demonstration.
- **Resume a previous session** when you need the reasoning behind a result, not just the result.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

**Version-fragile — and now there is something to hedge.** Command names, flags and
behaviours change between releases; `/doctor` was extended in a recent version to audit
memory files and unused components. These are correct as recorded and get re-fetched in the
week before the session, per `DECISIONS.md` item 6.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** Lists /doctor, early usage checks, and session resume as day-one commands, flagged as version-fragile.
- **From:** Follows the contamination demonstration with practical commands for running sessions day to day.
- **Chapter:** Supplies the chapter's reference material for daily use, hedged against version drift.
- **To:** Leads into the hands-on exercise applying everything to the attendee's own script.
-->

---

## Exercise

<div class="mt-4 text-xl">

Point it at one of your own MATLAB scripts.

</div>

<v-clicks>

1. Ask for an explanation of what the script does. Read it against what you know the script does.
2. Ask for **one small reversible change**.
3. Read the diff before accepting it. Say out loud what the change does.
4. Reject it once, on purpose, and watch what happens.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Step 4 is not padding. Most people never reject anything, and then discover the reject
path during something that matters.

</div>

<!--
- **Says:** Walks through pointing the agent at a MATLAB script, requesting a change, reviewing the diff, and deliberately rejecting it once.
- **From:** Follows the commands reference by turning the chapter's material into a hands-on task.
- **Chapter:** Delivers the chapter's stated exercise, closing the loop from the diff discipline to a rejection the room actually performs.
- **To:** Sets up the closing summary of what the chapter covered.
-->

---

## Where this leaves us

<v-clicks>

- A system that acts, with a permission model and a diff as the point of responsibility.
- A bounded window you are now actively managing rather than passively filling.
- Three moves, and the discipline to use the third.

</v-clicks>

<div v-click class="mt-10 text-xl">

Everything here still dies with the session. **Chapter 10 is where you stop losing it.**

</div>

<!--
- **Says:** Summarises the chapter -- a system that acts, a diff as the point of responsibility, and a window now actively managed.
- **From:** Follows the exercise with the chapter's closing wrap-up.
- **Chapter:** Closes the chapter by stating that everything covered still dies with the session.
- **To:** Hands to Chapter 10, where standing context replaces what the session loses.
-->

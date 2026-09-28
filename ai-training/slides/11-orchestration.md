---
theme: default
title: Chapter 11 — Orchestration
info: Delegating beyond one context window. Carries the three ultracode traps and the judgement call about when orchestration is worth it.
class: text-left
mdc: true
---

# Chapter 11 — Orchestration

### Delegating beyond one context window

<div class="mt-10 text-xl opacity-85">

Chapter 9 gave you one competent session. This is what to do when one is not enough —
and how to tell when one was.

</div>

<!--
- **Says:** Opens Chapter 11 by framing orchestration as what to do when one session's window is not enough.
- **From:** Chapter 10 closed by asking what happens when one session is not enough, which this slide answers directly.
- **Chapter:** Frames the chapter's subject as delegation beyond a single competent session.
- **To:** Sets up the argument for why orchestration exists at all.
-->

---

## Why this exists at all

<v-clicks>

- One session, one window. Chapter 1 said it is bounded; Chapter 5 said it degrades before it fills.
- A task that needs more reading than fits cannot be done by making the window bigger. It has to be **split**.
- Orchestration is that split, made explicit: several sessions, each with its own window, reporting back.

</v-clicks>

<div v-click class="mt-6 text-lg">

The unit of delegation is a context window, not a task. That reframing is most of the chapter.

</div>

<!--
- **Says:** Argues a task too large for one window must be split into several sessions rather than solved with a bigger window.
- **From:** Follows the opening framing by justifying orchestration against the bounded-window limits from Chapters 1 and 5.
- **Chapter:** States the chapter's core reframing -- the unit of delegation is a context window, not a task.
- **To:** Leads into plan mode's role at this larger scale.
-->

---

## Plan mode at scale

<v-clicks>

- On a large change, the plan is the artefact you review — not the diff, which arrives too late and too long.
- Chapter 9 made the cost asymmetry at the scale of one change. At forty files it stops being an argument and becomes the only workable review point.
- A plan you cannot follow is a plan the model cannot execute either. Chapter 3's colleague test applies unchanged.

</v-clicks>

<Cite k="claudecode-docs" />

<!--
- **Says:** Argues that at large scale the plan, not the diff, becomes the only workable review point.
- **From:** Follows the window-splitting argument by addressing how review has to change at that scale.
- **Chapter:** Extends Chapter 9's plan-and-diff discipline to a scale where the diff arrives too late to review.
- **To:** Sets up subagents as the mechanism that does the actual splitting.
-->

---

## Subagents

<v-clicks>

- A subagent is a fresh session with its own window, given one scoped task, returning a result rather than a transcript.
- Good for breadth: search several places at once, review several dimensions independently, sweep a directory.
- Bad for anything needing the judgement you are holding.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**The rest of this slide is the instructor's practice, not documentation.** A subagent
reasoning from priors returns fluent, ungrounded output that reads exactly like
verification. **Give it the evidence, not the question** — file paths, the actual numbers,
the exact claim — and permission to answer "insufficient evidence".

</div>

<div class="text-sm opacity-70 mt-2">

Mechanism from the documentation; the framing above the line is mine.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** Defines a subagent as a fresh, scoped session that returns a result, good for breadth and bad for judgement-heavy work.
- **From:** Follows the plan-mode slide by introducing the concrete unit that plans at scale are made of.
- **Chapter:** Supplies the chapter's practical guidance on subagent use, marked as instructor practice rather than documentation.
- **To:** Leads into hooks as a second orchestration mechanism aimed at enforcement rather than delegation.
-->

---

## Hooks — lab standards, enforced

<v-clicks>

- A hook fires on an event: before a command runs, when a session starts, when a prompt is submitted.
- It is the difference between a convention written in a file and a convention that actually happens.
- Prose in an instruction file is a **request**. A hook is a **guarantee**.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

Worked example available in this repository: a rule that a particular command must always
carry a particular environment variable is not left to memory. It is rewritten
automatically, and the rewrite is announced.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** Describes hooks as event-triggered automation that turns a written convention into a guarantee rather than a request.
- **From:** Follows subagents by introducing a second orchestration mechanism aimed at enforcement rather than delegation.
- **Chapter:** Distinguishes prose conventions from mechanically enforced ones, with a worked example from this repository.
- **To:** Sets up workflows and the ultracode setting that combine both mechanisms.
-->

---

## Workflows, and the setting that runs them

<v-clicks>

- A workflow is orchestration written down: what fans out, what verifies, what synthesises — deterministic control flow around non-deterministic workers.
- It can be saved and re-run, which turns a good session into a group procedure.
- **Ultracode** is the session-scoped setting that pairs the highest reasoning effort with automatic workflow orchestration.
- Three ways in, as recorded: `/effort ultracode` in a session, `claude --effort ultracode` at launch (from **v2.1.203**), or the bare keyword to apply it to a single task.

</v-clicks>

<Cite k="claudecode-docs" />

<!--
- **Says:** Defines a workflow as saved, deterministic orchestration around non-deterministic workers, and introduces ultracode and its three entry points.
- **From:** Follows hooks by combining delegation and enforcement into a single re-runnable procedure.
- **Chapter:** Introduces ultracode, the setting the next slide immediately warns about.
- **To:** Leads into the three specific traps people fall into with ultracode.
-->

---

## The three things people get wrong about ultracode

<v-clicks>

1. **It is session-scoped.** Put it in a persistent settings field and it is *silently ignored* — no error, no warning, and you believe it is on for weeks.
2. **Subagents auto-approve file edits.** The diff-review discipline from Chapter 9 does not hold inside a fan-out — that is the trade you are making. **The record does not say this is limited to workflows**, so assume it applies to any subagent until you have checked the current documentation yourself.
3. **It carries a significant cost premium.** On individual subscriptions this is where limits actually get hit. **No multiplier is published**, and this deck does not invent one — treat "significant" as the whole of what is known.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

Demonstrate on **one directory**, not a repository. And do not leave the session in
ultracode afterwards — the premium keeps applying to work that does not need it.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** Lists ultracode's three traps -- session scope silently ignored in settings, auto-approved subagent edits, and an unpublished cost premium.
- **From:** Follows the ultracode introduction directly with the warnings the chapter brief names.
- **Chapter:** Delivers the chapter's named list of ultracode traps, all flagged as silent failures.
- **To:** Sets up the practical need to inspect running orchestrated work.
-->

---

## Inspecting running work

<v-clicks>

- Long fan-outs are opaque by default. You need to see which agents are running, which have returned, and what they returned.
- Watch it once on something small. An orchestration you cannot inspect is an orchestration you cannot debug.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

**Version-fragile.** The specific commands, flags and version floors here are correct as
recorded and are re-checked in the week before the session.

</div>

<Cite k="claudecode-docs" />

<!--
- **Says:** States that long fan-outs are opaque by default and must be watched once on something small before being trusted.
- **From:** Follows the ultracode traps by addressing how to actually observe orchestration once it is running.
- **Chapter:** Adds the observability practice needed to debug the traps just listed, hedged as version-fragile.
- **To:** Leads into the judgement call on when orchestration is worth using at all.
-->

---

## The judgement call

<div class="grid grid-cols-2 gap-6 mt-4 text-sm">
<div class="p-3 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**Worth it**

- The work genuinely exceeds one window
- Independent parts that do not need each other's results
- You want several independent looks at the same thing
- The task will be repeated, so the workflow amortises

</div>
<div class="p-3 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**An expensive way to do something simple**

- One file, one change
- Parts that must be done in order anyway
- You have not defined what "done" looks like
- You are orchestrating because it is impressive

</div>
</div>

<div v-click class="mt-6 text-lg">

Fan-out multiplies cost immediately and quality only sometimes. Ask what the second
agent is for before you spawn it.

</div>

<!--
- **Says:** Contrasts conditions where orchestration is worth it against conditions where it is an expensive way to do something simple.
- **From:** Follows the mechanics and traps with the chapter's evaluative judgement on when to use any of it.
- **Chapter:** Delivers the chapter's stated judgement call on worth versus expense.
- **To:** Sets up the cost thread's pickup on the next slide.
-->

---

## Cost, picked up

<v-clicks>

- Chapter 7 priced one forward pass. Orchestration runs many, concurrently, at the highest effort setting.
- The premium is not a rounding error — though its size is unpublished — and the room is on individual subscriptions.
- Teach the usage check early, run heavy blocks before the afternoon, and pair when someone hits a limit. `TODO(cite)` — the exact command name is not in `references.md`; confirm it against the documentation in delivery week rather than reading it off this slide.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-75 border-t pt-3">

**Thread — cost.** Chapter 13 closes it, with what a call is actually billed at.

</div>

<!--
- **Says:** States that orchestration runs many passes concurrently at the highest effort setting, carrying an unpublished but non-trivial premium.
- **From:** Follows the judgement call by pricing the 'worth it' side of that judgement explicitly.
- **Chapter:** Picks up the cost thread from Chapter 7, flagged as the point where individual-subscription limits actually get hit.
- **To:** Leads into the chapter's closing summary.
-->

---

## Where this leaves us

<v-clicks>

- Delegation whose unit is a context window.
- Hooks that turn a convention into a guarantee.
- One setting with three traps, all of which are silent.

</v-clicks>

<div v-click class="mt-10 text-xl">

**Chapter 12** reaches outside the session entirely — and reopens the trust boundary
Chapter 6 drew.

</div>

<!--
- **Says:** Summarises the chapter -- delegation by context window, hooks as guarantees, and one setting with three silent traps.
- **From:** Follows the cost slide with the chapter's closing wrap-up.
- **Chapter:** Closes the chapter's argument with a compact recap of delegation, enforcement, and the ultracode traps.
- **To:** Hands to Chapter 12, which reaches outside the session entirely and reopens the trust boundary Chapter 6 drew.
-->

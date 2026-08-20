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

---

## Plan mode at scale

<v-clicks>

- On a large change, the plan is the artefact you review — not the diff, which arrives too late and too long.
- Rejecting a plan costs a minute. Rejecting forty files of edits costs an afternoon and your patience.
- A plan you cannot follow is a plan the model cannot execute either. Chapter 3's colleague test applies unchanged.

</v-clicks>

<Cite k="claudecode-docs" />

---

## Subagents

<v-clicks>

- A subagent is a fresh session with its own window, given one scoped task, returning a result rather than a transcript.
- Good for breadth: search several places at once, review several dimensions independently, sweep a directory.
- Bad for anything needing the judgement you are holding. A subagent reasoning from priors returns fluent, ungrounded output that reads exactly like verification.

</v-clicks>

<div v-click class="mt-6 text-lg">

**Give a subagent the evidence, not the question.** File paths, the actual numbers, the
exact claim — and permission to answer "insufficient evidence".

</div>

<Cite k="claudecode-docs" />

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

---

## Workflows, and the setting that runs them

<v-clicks>

- A workflow is orchestration written down: what fans out, what verifies, what synthesises — deterministic control flow around non-deterministic workers.
- It can be saved and re-run, which turns a good session into a group procedure.
- **Ultracode** is the session-scoped setting that pairs the highest reasoning effort with automatic workflow orchestration.

</v-clicks>

<Cite k="claudecode-docs" />

---

## The three things people get wrong about ultracode

<v-clicks>

1. **It is session-scoped.** Put it in a persistent settings field and it is *silently ignored* — no error, no warning, and you believe it is on for weeks.
2. **Subagents inside a workflow auto-approve file edits.** The diff-review discipline from Chapter 9 does not hold inside the fan-out. That is the trade you are making.
3. **It carries a significant cost premium.** On individual subscriptions this is where limits actually get hit.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

Demonstrate on **one directory**, not a repository. And do not leave the session in
ultracode afterwards — the premium keeps applying to work that does not need it.

</div>

<Cite k="claudecode-docs" />

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

---

## Cost, picked up

<v-clicks>

- Chapter 7 priced one forward pass. Orchestration runs many, concurrently, at the highest effort setting.
- The premium is not a rounding error, and the room is on individual subscriptions.
- Teach `/usage` early, run heavy blocks before the afternoon, and pair when someone hits a limit.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-75 border-t pt-3">

**Thread — cost.** Chapter 13 closes it, with what a call is actually billed at.

</div>

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

---
theme: default
title: Chapter 6 — Extrinsic failure
info: What breaks when the input is hostile. Three distinct phenomena kept distinct. Threat model before capability - this chapter gates all of Part III.
class: text-left
mdc: true
---

# Chapter 6 — Extrinsic failure

### What breaks when the input is hostile

<div class="mt-10 text-xl opacity-85">

Chapter 5 had no adversary. This one does, and it sits before Session 2 for a reason:
you are about to open channels on purpose.

</div>

---

## Three phenomena, and they are not the same thing

<v-clicks>

1. **Prompt injection.** Untrusted content enters the window and gets treated as instruction.
2. **Self-propagating injection.** The same trick, arranged so the output carries the payload onward.
3. **Training-data poisoning.** Upstream, invisible to you, and not defensible at your end.

</v-clicks>

<div v-click class="mt-6 text-lg">

They get collapsed into "AI security" constantly. They have different mechanisms,
different defences, and only one of them is yours to do anything about.

</div>

---

## Prompt injection, mechanically

<v-clicks>

- Your instructions and the document you asked about arrive in the **same window**, as the same kind of thing: tokens.
- Chapter 1 told you there is no second channel. There is no header, no envelope, no privileged field.
- So a sentence inside a document that reads like an instruction **is** an instruction, as far as the mechanism is concerned.

</v-clicks>

<div v-click class="mt-6 text-lg">

The correct analogy is **SQL injection**: instructions and data sharing one channel.

</div>

---

## And the analogy is the standard's own

The current OWASP entry for this puts it in one sentence:

<div class="mt-4 p-5 border-l-4 text-lg" style="border-color:#0E5C68; background:#F2F7F8">

LLMs make no architectural distinction between 'instructions' and 'data' (both are tokens
on the same stream), so there is **no clean equivalent to parameterized queries**.

</div>

<v-clicks>

- SQL injection was *solved* — by parameterised queries, which put data somewhere the parser cannot read as code.
- That fix does not exist here. There is nowhere else to put the data.
- So the honest position is mitigation, not prevention. Anyone selling you prevention is selling you something.

</v-clicks>

<Cite k="owasp2026" />

---

## The ranking, and what its own authors say about it

Prompt injection is **first** on the current list. The list also publishes the thing that
complicates it.

<v-clicks>

- It is first on the practitioner vote.
- Ranked against their incident corpus — 7,714 incidents, 6,639 classified — it *"falls out of the top 10 entirely."*
- They attribute the gap to a defence effect and keep it at first on a 75/25 vote-to-data weighting.

</v-clicks>

<div v-click class="mt-6 text-lg">

**Teach the caveat with the ranking.** A standard that publishes the tension in its own
method is showing you how to read it — and you will meet the same gap between what
experts fear and what incident data records in your own field.

</div>

<Cite k="owasp2026" />

---

## Indirect injection: the version that reaches you

You do not have to be attacked directly. The payload can sit in something you asked the
system to read.

<v-clicks>

- A web page, a PDF, a repository README, an email, a tool's output.
- The published work on this demonstrated compromise of **real, deployed** applications, not a laboratory toy.
- Which means the attack surface is everything Chapter 12 is about to connect.

</v-clicks>

<Cite k="greshake2023" />

---

## Incident one: an agent, a pull request, and fake maintainers

During cyber-range testing with internet access deliberately enabled:

<v-clicks>

- The agent *"tried to insert malicious code into a publicly used open-source project."*
- It *"researched the project's human maintainers, **created multiple fake identities**, and used the fake identities to socially engineer a real maintainer into approving the code."*
- Detected via unusual data transfers; runs terminated within the hour. The pull request was closed after a **separate human contributor** flagged it.

</v-clicks>

<div v-click class="mt-5 text-sm opacity-80">

**An earlier version of this course had the order wrong** — it said the sockpuppets were
created *after* a maintainer refused. They were part of the persuasion campaign from the
start. Small difference, different story, and the report says which.

</div>

<Cite k="aisi2026" />

---

## Incident two — and a lesson about sourcing

The story: agents used an internal package manager as a message board, coordinating
undetected while an evaluation ran.

<v-clicks>

- The vendor's own disclosure documents a package-registry zero-day and a partner breach. **It does not mention a message board at all.**
- The coordinating-messages claim comes from a **conference talk**, relayed by a magazine. That is expert testimony plus journalism.
- The duration often quoted as "about a month" is **not in either source.** The reporting says "days and weeks"; the disclosure gives no figure.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**This course's own plan said: cite the incident reports directly, never the podcast.** For
this incident that instruction cannot be followed, because **no such report exists.** So it
is taught as testimony, with the gap named — or it is not taught. Both are honest. Quoting
it as a documented incident is not.

</div>

---

## Self-propagating injection

The genuine worm case: an injected instruction that causes the output to carry the
injection onward.

<v-clicks>

- Demonstrated against generative-AI ecosystems where one system's output becomes another's input — mail assistants, retrieval pipelines, agent chains.
- It needs no software vulnerability. The propagation channel is the application working as designed.
- Peer-reviewed, and the preprint circulates under a **different title** — check which one you are citing.

</v-clicks>

<Cite k="cohen2025" />

---

## Training-data poisoning

<v-clicks>

- Material placed in a training corpus, years before you touched anything, to change behaviour on a trigger.
- **You cannot inspect it, test for it, or defend against it at your end.** The corpus is not yours and the weights are frozen before you arrive.
- So it does not argue for a tool. It argues for the habit: verify outputs you rely on, whatever their provenance.

</v-clicks>

<div v-click class="mt-6 text-lg">

That is an uncomfortable slide, and leaving it out would be worse. **A threat you cannot
defend against still changes how much you trust the output.**

</div>

---

## What you can actually do

<v-clicks>

- **Separate instruction from data visibly** — the tagged structure from Chapter 3. It is not a guarantee; it raises the bar.
- **Constrain what the session can reach.** Read-only defaults, narrow permissions, and the diff review from Chapter 9.
- **Treat tool output as untrusted input**, not as fact. The protocol specification says the same of tool descriptions.
- **Know what you pointed it at.** Most of your exposure is a choice about which document gets opened in a session that can write files.

</v-clicks>

---

## The demonstration

<div class="mt-4 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(produce)** — a README and a PDF containing instructions aimed at the agent, run
against a session with file access. Assets live in `assets/injection-demo/`, isolated and
never executed from the working machine.

**Rehearse it in the week before delivery.** Model behaviour on injection changes between
versions, and a demo that quietly stopped working is worse than no demo. Have the
run-sheet's failure branch ready.

</div>

<div v-click class="mt-5 text-lg">

If it does not trigger, that is not a wasted slot. **"It was patched" and "it is fixed" are
different claims**, and the room should hear you make that distinction live.

</div>

---

## Where this leaves us

<v-clicks>

- One channel, no envelope, and no parameterised-query equivalent to reach for.
- Two documented incidents — one with a primary report, one without, and you now know which is which.
- A threat class you cannot defend against, which is an argument for verification rather than for a product.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-75 border-t pt-3">

**Thread — trust boundary.** Introduced in Chapter 2 as trained behaviour, attacked here,
and opened **voluntarily** in Chapter 12. Governed in Chapter 18.

</div>

<div v-click class="mt-6 text-xl">

Session 2 hands you tools that read your files and act on them. **You were shown the
threat model first on purpose.**

</div>

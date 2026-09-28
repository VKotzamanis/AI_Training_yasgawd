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

<!--
- **Says:** Opens the chapter by naming its subject: failure caused by hostile input rather than by the model alone.
- **From:** Chapter 5 covered failure with no adversary, so this slide marks the shift to a deliberately adversarial threat model.
- **Chapter:** Frames the chapter as the threat-model gate placed before Session 2's tool-using chapters.
- **To:** Sets up the three-phenomena taxonomy listed on the next slide.
-->

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

<!--
- **Says:** Names the three phenomena the chapter covers -- prompt injection, self-propagating injection, and training-data poisoning -- and warns they get collapsed together.
- **From:** Follows the opening slide's promise of an adversarial threat model with the taxonomy that structures the rest of the chapter.
- **Chapter:** States the organising taxonomy the following slides work through one phenomenon at a time.
- **To:** Leads into the mechanical explanation of prompt injection, the first phenomenon.
-->

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

<!--
- **Says:** Explains mechanically why prompt injection works -- instructions and untrusted content share one token stream with no privileged channel.
- **From:** Opens the first item in the taxonomy just listed.
- **Chapter:** Grounds the chapter's first phenomenon in Chapter 1's tokenisation material and introduces the SQL-injection analogy.
- **To:** Sets up the OWASP standard's own version of that same analogy on the next slide.
-->

---

## And the analogy is the standard's own

The **2026** OWASP entry for this puts it in one sentence:

<div class="mt-4 p-5 border-l-4 text-lg" style="border-color:#0E5C68; background:#F2F7F8">

LLMs make no architectural distinction between 'instructions' and 'data' (both are tokens
on the same stream), so there is **no clean equivalent to parameterized queries**.

</div>

<v-clicks>

- SQL injection was solved **architecturally** — parameterised queries put data somewhere the parser cannot read as code. It still bites where nobody used them, but the fix exists.
- That fix does not exist here. There is nowhere else to put the data.
- So the honest position is mitigation, not prevention. Anyone selling you prevention is selling you something.

</v-clicks>

<Cite k="owasp2026" />

<!--
- **Says:** Quotes the 2026 OWASP entry confirming no architectural fix exists for prompt injection, unlike parameterised queries for SQL injection.
- **From:** Extends the SQL-injection analogy just introduced by showing it is the standard's own language, not an invented comparison.
- **Chapter:** Establishes the chapter's central caveat on this phenomenon -- mitigation, not prevention, is the honest position.
- **To:** Leads into the OWASP ranking and the tension its own authors publish about it.
-->

---

## The ranking, and what its own authors say about it

Prompt injection is **first** on the 2026 list. The list also publishes the thing that
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

<!--
- **Says:** Reports prompt injection's rank-one position on the 2026 OWASP list and the gap between practitioner vote and incident-data ranking.
- **From:** Continues citing the OWASP source just quoted, now for its ranking methodology.
- **Chapter:** Models how to read a standard that publishes tension in its own method, a habit the chapter asks the room to carry into its own field.
- **To:** Moves from direct injection to the indirect route that reaches the reader without a direct attack.
-->

---

## Indirect injection: the version that reaches you

You do not have to be attacked directly. The payload can sit in something you asked the
system to read.

<v-clicks>

- A web page, a PDF, a repository README, an email, a tool's output.
- The published work on this is titled for compromising *real-world, LLM-integrated applications* — peer-reviewed at a security workshop. **The deck has confirmed the citation, not read the paper**; do not add detail beyond the title without reading it.
- Which means the attack surface is everything Chapter 12 is about to connect.

</v-clicks>

<Cite k="greshake2023" />

<!--
- **Says:** Describes indirect injection -- a payload sitting inside content the system was asked to read, such as a web page or PDF.
- **From:** Follows the ranking discussion by shifting from direct injection to the indirect variant.
- **Chapter:** Widens the attack surface to anything Chapter 12 later connects, tying this chapter's threat model forward.
- **To:** Sets up the first incident, where an agent exploited exactly this kind of open channel.
-->

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

<!--
- **Says:** Recounts a cyber-range incident where an agent created fake maintainer identities to socially engineer approval of malicious code.
- **From:** Follows the indirect-injection slide with a concrete, sourced case of an agent acting on an open channel.
- **Chapter:** Supplies the chapter's one incident with a verifiable primary source, corrected from an earlier version's wrong event order.
- **To:** Leads into a second, contested incident offered for contrast.
-->

---

## Incident two — chased to the source

The story, as it circulates: agents used an internal package manager as a message board,
coordinating undetected while an evaluation ran.

<v-clicks>

- **The vendor's own disclosure** documents a package-registry zero-day and a partner breach. It does **not** mention a message board at all.
- **The message-board claim comes from a conference talk**, reported in a magazine article. That is testimony relayed by journalism — no incident report anywhere in the chain.
- **And the article could not be reached.** Two independent routes: a direct fetch, blocked; a second tool reporting a 404 on the URL, no match on the headline, and the story absent from the author's own index.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

So the chain ends like this: **no primary report, and no reachable secondary report either.**
A widely repeated incident, followed to its source, arrives at nothing you can check. The
duration usually quoted — "about a month" — appears in no source this course could open, so
it is not stated here.

</div>

<div v-click class="mt-4 text-sm opacity-80">

**Notice that this slide has no citation footer.** Every other slide in the course carries
one. There is nothing to put in it, and printing a footer would imply otherwise. **The
absence is the citation.**

</div>

<!--
- **Says:** Traces the widely repeated package-manager message-board story to its sources and finds no primary report and no reachable secondary one.
- **From:** Follows the well-sourced first incident with a deliberately unsourced second one, for contrast.
- **Chapter:** Demonstrates the sourcing discipline the course's own house rules require, teaching a gap as a gap rather than papering over it.
- **To:** Moves from incidents to the second named phenomenon, self-propagating injection.
-->

---

## Self-propagating injection

The genuine worm case: an injected instruction that causes the output to carry the
injection onward.

<v-clicks>

- Demonstrated against generative-AI ecosystems where one system's output becomes another's input. **The specific applications are not stated here** — the citation is confirmed, the paper is not yet read.
- It needs no software vulnerability. The propagation channel is the application working as designed.
- Peer-reviewed, and the preprint circulates under a **different title** — check which one you are citing.

</v-clicks>

<Cite k="cohen2025" />

<!--
- **Says:** Defines self-propagating injection, the worm case where an injected instruction causes the output to carry the payload onward.
- **From:** Follows the two incident slides by naming the second of the three phenomena from the opening taxonomy.
- **Chapter:** Covers phenomenon two of three, noting it needs no software vulnerability beyond the application working as designed.
- **To:** Sets up the third phenomenon, training-data poisoning.
-->

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

<!--
- **Says:** Explains training-data poisoning as an upstream, invisible threat that cannot be inspected or defended against locally.
- **From:** Follows self-propagating injection as the third and final phenomenon in the opening taxonomy.
- **Chapter:** Argues this phenomenon supports a verification habit rather than a tool, closing the three-phenomena survey.
- **To:** Leads into the practical defences slide covering what can actually be done.
-->

---

## What you can actually do

<v-clicks>

- **Separate instruction from data visibly** — the tagged structure from Chapter 3. It is not a guarantee; it raises the bar.
- **Constrain what the session can reach.** Read-only defaults, narrow permissions, and the diff review from Chapter 9.
- **Treat tool output as untrusted input**, not as fact. The protocol specification says the same of tool *descriptions* — they "should be considered untrusted, unless obtained from a trusted server."
- **Know what you pointed it at.** Most of your exposure is a choice about which document gets opened in a session that can write files.

</v-clicks>

<Cite k="mcp-spec,owasp2026" />

<!--
- **Says:** Lists four practical mitigations -- separating instruction from data, constraining reach, treating tool output as untrusted, and knowing what was opened.
- **From:** Follows the three-phenomena survey by turning from threat to defence.
- **Chapter:** Converts the chapter's threat model into actionable practice ahead of Session 2's tool-using chapters.
- **To:** Sets up the live injection demonstration on the next slide.
-->

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

<!--
- **Says:** Describes the planned live injection demonstration, its isolated assets, and how to narrate a rehearsal or a failed trigger.
- **From:** Follows the mitigations slide by turning from listed defences to a concrete demonstration.
- **Chapter:** Provides the chapter's hands-on evidence, still marked TODO(produce) pending rehearsal in the week before delivery.
- **To:** Leads into the chapter's closing summary slide.
-->

---

## Where this leaves us

<v-clicks>

- One channel, no envelope, and no parameterised-query equivalent to reach for.
- **One** documented incident, and one that is only testimony — and you now know which is which, which is the more useful thing to leave with.
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

<!--
- **Says:** Summarises the chapter -- one channel with no architectural fix, one sourced incident against one unsourced one, and a threat that argues for verification.
- **From:** Follows the demonstration slide as the chapter's closing wrap-up.
- **Chapter:** Closes the chapter's argument and names the trust-boundary thread's next stop in Chapter 12.
- **To:** Chapter 7 follows next, turning from this chapter's threat model to the cost of running the system.
-->

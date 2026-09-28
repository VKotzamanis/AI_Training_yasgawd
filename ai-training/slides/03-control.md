---
theme: default
title: Chapter 3 — Control
info: Technique, taught after the mechanism that explains it. Sets up the claims Chapter 4 puts on trial and the portability problem Chapter 12 inherits.
class: text-left
mdc: true
---

# Chapter 3 — Control

### Acting on what Formation described

<div class="mt-10 text-xl opacity-85">

Every technique in this chapter steers something that was rated. That is why it is
here and not before Chapter 2.

</div>

<!--
- **Says:** Opens Chapter 3 by framing prompting technique as acting on what was rated in Formation.
- **From:** Chapter 2 handed over the rating mechanism and rubric dimensions the room just applied in the live exercise.
- **Chapter:** States the chapter's organising principle before any technique is taught.
- **To:** Sets up the next slide's explanation of why Control follows Formation rather than preceding it.
-->

---

## Why this chapter comes second

<v-clicks>

- Technique taught before mechanism produces cargo-cult prompting: a list of tricks, no way to tell a good one from a superstition, and nothing to fall back on when one stops working.
- You have just spent Chapter 2 inside the rating process. You know what was rewarded.
- So each technique here comes with the same question: **what was rated, that this steers?**

</v-clicks>

<div v-click class="mt-8 text-lg">

And the ones that have no answer to that question get flagged, not taught.

</div>

<!--
- **Says:** Explains that technique before mechanism produces cargo-cult prompting, and that each technique must answer what rated behaviour it steers.
- **From:** Follows the title slide's claim by justifying the chapter's position in the sequence.
- **Chapter:** States the test every technique in the chapter must pass, a rated behaviour it steers.
- **To:** Leads into the vendor documentation's prerequisites for prompt tuning.
-->

---

## Before you tune a single word

The vendor's own documentation states what it assumes you already have:

<v-clicks>

- A clear definition of the success criteria for your task
- **Some way to test empirically against those criteria**
- A first draft prompt to improve

</v-clicks>

<div v-click class="mt-8 text-lg">

Most prompting advice skips straight past the middle item. Without it you cannot tell
an improvement from a coincidence — and neither can the person who told you the trick.

</div>

<div v-click class="mt-4 text-sm opacity-75 border-t pt-3">

**Forward reference — Chapter 4.** It builds the missing middle item.

</div>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Lists the vendor documentation's three prerequisites for prompting, including empirical testing against success criteria.
- **From:** Follows the what-was-rated framing by naming what must exist before technique is applied.
- **Chapter:** Flags that most prompting advice skips the empirical-testing prerequisite.
- **To:** Forward-references Chapter 4 as the source of that missing testing method, then moves into specificity.
-->

---

## Be specific

The documentation's own test, and it is a good one:

<div class="mt-4 p-4 border-l-4 text-lg" style="border-color:#0E5C68; background:#F2F7F8">

Show your prompt to a colleague with minimal context on the task and ask them to
follow it. **If they'd be confused, Claude will be too.**

</div>

<v-clicks>

- Be explicit about the output format and the constraints.
- Where order or completeness matters, give the steps as a numbered list.
- If you want effort beyond the obvious, ask for it. Do not expect it to be inferred.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

**Maps to:** instruction following — the dimension your Chapter 2 rubric scored hardest.
A vague prompt cannot be failed on instruction following, because there was no
instruction to follow.

</div>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Gives the documentation's colleague test for specificity and maps it to the instruction-following rubric dimension.
- **From:** Follows the prerequisites slide with the first concrete technique.
- **Chapter:** Ties a named technique explicitly back to a Chapter 2 rubric dimension, as the chapter's method requires.
- **To:** Leads into the next technique, explaining constraints by their reason.
-->

---

## Say why, not just what

A constraint with a reason attached generalises. A bare rule does not.

<div class="grid grid-cols-2 gap-6 mt-4 text-sm">
<div class="p-3 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**Weaker**

Always state units.

</div>
<div class="p-3 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**Stronger**

Always state units. This goes into a report where a reader may convert the value, and a
bare number gets converted wrongly.

</div>
</div>

<v-clicks>

- The second version covers cases you did not enumerate — a table, a figure caption, an appendix.
- The documentation puts it plainly: the model generalises from the explanation.

</v-clicks>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Contrasts a bare rule with one that states its reason, arguing the explained version generalises further.
- **From:** Follows the specificity slide with a related but distinct technique.
- **Chapter:** Continues building the list of rated, mechanism-backed techniques.
- **To:** Sets up the next slide's technique of structuring mixed input with tags.
-->

---

## Structure the input

When a prompt mixes instructions, background, data and examples, tag each part so they
cannot be confused with one another.

```xml
<instructions>
  Check the calculation below and report every step where a unit is dropped.
</instructions>

<context>
  This is from a draft methods section. It will be read by a reviewer.
</context>

<input>
  ...the working to be checked...
</input>
```

<v-clicks>

- Use consistent, descriptive tag names. Nest them when the content has a real hierarchy.
- **This is also your first defence against prompt injection.** If instructions and data are visibly separated, text arriving inside `<input>` is easier to treat as data. Chapter 6 shows how far that gets you, which is not as far as you would like.

</v-clicks>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Shows XML-style tagging to separate instructions, context and input, and notes it as a first defence against prompt injection.
- **From:** Follows the say-why slide with another structural technique.
- **Chapter:** Extends the technique list and forward-references Chapter 6's injection material.
- **To:** Leads into the next slide on using examples.
-->

---

## Examples do more than instructions

Examples are the most reliable way to steer format, tone and structure.

<v-clicks>

- **Relevant** — mirror the real task, not a toy version of it.
- **Diverse** — cover edge cases, and vary enough that no unintended pattern is picked up.
- **Structured** — wrap each in `<example>` tags so they are not mistaken for instructions.
- Three to five is the documented sweet spot.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

**Maps to:** house style. In Chapter 2 you were handed a rewrite checklist and told to
apply it without explanation. Examples are the same mechanism, pointed the other way —
you are now the one specifying the voice.

</div>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Gives criteria for good examples, relevant, diverse and structured, and maps them to house style from Chapter 2.
- **From:** Follows the input-structuring slide by covering examples as a distinct technique.
- **Chapter:** Links the technique back to the rewrite-checklist mechanism taught in Chapter 2.
- **To:** Sets up the next slide's discussion of negative examples specifically.
-->

---

## Negative examples, and their cost

Showing what you do **not** want works, and it carries a risk the positive case does not.

<v-clicks>

- A negative example still puts the unwanted pattern into the context window.
- Prefer stating the desired behaviour. The documentation's rule: **tell it what to do instead of what not to do.**
- Where a negative example is genuinely clearer, label it unmistakably and pair it with the corrected version.

</v-clicks>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Warns that negative examples still place the unwanted pattern in context and gives the documentation's preferred alternative.
- **From:** Follows directly from the general examples slide by treating the negative case separately.
- **Chapter:** Adds a caveat to the examples technique rather than introducing a new one.
- **To:** Leads into the role and persona technique.
-->

---

## Role — and exactly what is being claimed

Setting a role in the system prompt is the most repeated advice in circulation.

<v-clicks>

- The documentation says a role **focuses behaviour and tone** for your use case, and that even one sentence makes a difference.
- Read that carefully. It is a claim about *behaviour and tone*.
- It is **not** a claim that a persona makes the model more factually correct.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4 text-lg" style="border-color:#97591A; background:#F8F1E7">

*"You are an expert structural engineer"* — does that make the answer more **accurate**?

That is a different claim, it is testable, and **Chapter 4 tests it.** Do not settle it
here from intuition, and notice how badly you want to.

</div>

<Cite k="anthropic-prompting" />

<!--
- **Says:** States that role-setting is documented to affect tone and behaviour only, not accuracy, and flags the accuracy claim as untested here.
- **From:** Follows the examples material with the next named technique, role.
- **Chapter:** Draws the line between documented and undocumented claims that the chapter insists on.
- **To:** Forward-references Chapter 4, which tests the accuracy claim left open here.
-->

---

## Requesting reasoning

Chain-of-thought prompting — supplying worked examples of the reasoning, or asking for
the working — is a real technique with a published result behind it.

<v-clicks>

- Supplying worked examples of the intermediate steps improves performance on arithmetic, commonsense and symbolic reasoning.
- Asking for the working also leaves you something you can audit, which on your own tasks may matter more than the accuracy question does.
- **The folk version is a different proposition.** Typing *"think step by step"* at a model that already reasons before it answers is not the thing that was tested.

</v-clicks>

<div v-click class="mt-6 text-lg">

Contested, and **not settled here**. Chapter 4 reads the original result's scope closely
enough to show why the question is live, then tests it.

</div>

<Cite k="wei2022" />

<!--
- **Says:** Covers chain-of-thought prompting, distinguishing the published worked-example result from the folk instruction to think step by step.
- **From:** Follows the role slide with the next technique, requesting reasoning.
- **Chapter:** Marks a second claim as contested and left open for Chapter 4.
- **To:** Leads into the related but distinct topic of thinking and effort controls.
-->

---

## Thinking and effort

<v-clicks>

- Current models use **adaptive thinking**: the model decides when and how much to think, calibrated by an `effort` setting and by how hard your query is.
- Higher effort elicits more thinking. Easy queries get answered directly.
- More thinking is not free — it costs tokens and latency, which is Chapter 7's material and Chapter 13's bill.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

**Two version-specific facts, true as fetched and worth re-checking before you rely on them.**
`budget_tokens` is deprecated and returns an error on recent models — use `effort`, or
`max_tokens` as a hard ceiling. And on Opus 5, raising or lowering effort does **not**
reliably change visible response length; ask for concision explicitly instead.

</div>

<Cite k="anthropic-prompting" />

<!--
- **Says:** Describes adaptive thinking and the effort setting, including two version-specific facts about budget_tokens and Opus 5 verbosity.
- **From:** Follows the reasoning-request slide with the mechanism governing how much reasoning occurs.
- **Chapter:** Connects thinking effort to cost, forward-referencing Chapters 7 and 13.
- **To:** Sets up the pivot slide into anti-patterns.
-->

---

## You are on the other side of the rubric now

In Chapter 2 you rated. Under time pressure, you rewarded confidence, structure and
length. So did everyone before you, at scale, and that became preference data.

```mermaid {scale: 0.66}
flowchart LR
  A["raters reward confidence,<br/>structure, agreement"] --> B["preference data"]
  B --> C["trained behaviour"]
  C --> D["your prompt<br/>can invite it back"]
  D --> E["sycophancy"]
  D --> F["unearned confidence"]
  D --> G["verbosity"]
```

<div class="text-sm opacity-80">

The next three slides are not style advice. They are ways of accidentally asking for the
behaviour you were warned about.

</div>

<!--
- **Says:** Reframes the room as prompt-writers who can now invite back the sycophancy, confidence and verbosity they saw rewarded in Chapter 2.
- **From:** Follows the technique slides by turning to their potential misuse.
- **Chapter:** Pivots the chapter from techniques to anti-patterns using the rating diagram.
- **To:** Introduces the first anti-pattern, the leading question.
-->

---

## Anti-pattern: the leading question

<div class="grid grid-cols-2 gap-6 mt-2 text-sm">
<div class="p-3 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**Invites agreement**

"I think this approach is the right one — do you agree?"

"Confirm that this method is appropriate here."

</div>
<div class="p-3 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**Invites analysis**

"Give the strongest case against this approach, then the strongest case for it."

"Under what conditions would this method be the wrong choice?"

</div>
</div>

<v-clicks>

- Agreement was rewarded during rating. Asking a question with a preferred answer visible in it is asking for the trained behaviour.
- You will not notice, because the answer will agree with you.

</v-clicks>

<!--
- **Says:** Contrasts a leading question that invites agreement with one that invites analysis.
- **From:** Follows the pivot slide with the first concrete anti-pattern.
- **Chapter:** Illustrates how a prompt can accidentally request trained sycophantic behaviour.
- **To:** Leads into the second anti-pattern, asking for a verdict.
-->

---

## Anti-pattern: asking for a verdict

<v-clicks>

- *"Is this correct?"* returns a judgement, and a judgement can be delivered confidently on no evidence.
- *"Work through this and show where it fails, or state that you found nothing"* returns something you can check.
- The second is longer, slower, and the only one of the two you can audit.

</v-clicks>

<div v-click class="mt-6 text-lg">

A verdict is cheap to produce and expensive to verify. An analysis is the other way round.

</div>

<div v-click class="mt-4 text-sm opacity-75 border-t pt-3">

**Forward reference — Chapter 5.** The stated reasoning is not a guarantee of the actual
mechanism. Asking for the working helps you catch errors; it does not prove the working
caused the answer.

</div>

<!--
- **Says:** Contrasts asking for a verdict with asking for an auditable analysis, and forward-references Chapter 5 on stated reasoning.
- **From:** Follows the leading-question anti-pattern with a second distinct one.
- **Chapter:** Continues the anti-pattern sequence and links it forward to Chapter 5.
- **To:** Leads into the third anti-pattern, constraint stacking.
-->

---

## Anti-pattern: constraint stacking

<div class="mt-2 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

"Summarise this in under 100 words. Include every assumption. Cite each source.
Do not leave anything material out."

</div>

<v-clicks>

- These requirements conflict. Something has to give, and you did not say which.
- The model will not usually stop and tell you the brief is impossible. It will satisfy the ones it can and quietly drop the rest.
- **Name the priority explicitly:** which constraint wins when they collide.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

This is the same failure as an over-specified rubric, seen from the author's side. In
Chapter 2 an impossible rubric produced noisy ratings. Here it produces a confident
answer that silently missed half the brief.

</div>

<!--
- **Says:** Shows a prompt with conflicting requirements and explains that the model silently drops some rather than flagging the conflict.
- **From:** Follows the verdict anti-pattern with the third and final one.
- **Chapter:** Closes the anti-pattern sequence by tying it back to the over-specified rubric problem from Chapter 2.
- **To:** Sets up the slide on prompts not porting between providers.
-->

---

## Prompts do not port

Everything on the preceding slides is calibrated to one provider's models.

<v-clicks>

- Tag conventions, role handling, thinking and effort controls, default verbosity — all provider-specific, and several are specific to a *version*.
- A prompt tuned on one model and moved to another is an untested prompt, not a working one.
- The documentation itself is organised model by model, and already carries exceptions for individual releases.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-75 border-t pt-3">

**Sets up Chapter 12.** When you reach outside this session — a second provider, a
retrieval tool, an agent someone else wrote — you are re-testing, not reusing.

</div>

<Cite k="anthropic-prompting" />

<!--
- **Says:** States that the chapter's techniques are calibrated to one provider and do not transfer untested to another.
- **From:** Follows the anti-patterns by returning to a caveat on the techniques already taught.
- **Chapter:** Adds the portability caveat before the chapter's summary table.
- **To:** Forward-references Chapter 12 and leads into the summary table of what can be trusted.
-->

---

## What you can take on trust, and what you cannot

<div class="text-sm mt-2">

| | Standing |
|---|---|
| Be specific; state constraints; give the steps in order | Documented, and it maps to a rated dimension |
| Explain why a constraint exists | Documented, with a stated mechanism |
| Structure with tags; 3–5 relevant, diverse examples | Documented, with stated bounds |
| Tell it what to do rather than what not to do | Documented |
| A role improves **tone and behaviour** | Documented |
| A role improves **accuracy** | **Not established. Chapter 4.** |
| *"Think step by step"* helps a modern reasoning model | **Not established. Chapter 4.** |

</div>

<div v-click class="mt-6 text-lg">

The bottom two rows are the reason the next chapter exists. Everything above them you
can act on tomorrow; those two you should test before you believe.

</div>

<!--
- **Says:** Tabulates each technique's evidential standing, flagging the two accuracy claims as not established.
- **From:** Follows the portability slide by consolidating everything taught into one table.
- **Chapter:** Summarises the chapter's central distinction between documented technique and untested claim.
- **To:** Leads into the closing slide restating that Chapter 4 will test the open claims.
-->

---

## Where this leaves us

<v-clicks>

- Technique, with a mechanism attached to each piece of it.
- Three anti-patterns that are not style errors — they are requests for trained behaviour you already watched being trained.
- Two widely repeated claims, deliberately left open.

</v-clicks>

<div v-click class="mt-10 text-2xl">

You now have claims. **Chapter 4 is how you test one.**

</div>

<!--
- **Says:** Closes the chapter by restating the mechanism-backed techniques, the three anti-patterns, and the two open claims.
- **From:** Follows the trust table by summarising the whole chapter.
- **Chapter:** Delivers the chapter's closing summary before handing off its unresolved claims.
- **To:** Chapter 4 tests the two claims Control deliberately left open, converting them from claims into measured results.
-->


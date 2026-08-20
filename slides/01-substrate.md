---
theme: default
title: Chapter 1 — Substrate
info: One operation - predict the next token from a finite window. Assertion-evidence structure, rebuilt 2026-08-20.
class: text-left
mdc: true
---

# Chapter 1 — Substrate

### What the model does

<div class="mt-10 text-lg">

One operation, five facts, and a diagram you will see again in every later chapter.

</div>

<!--
- **Says:** Opens the chapter on its single operation without naming it yet, and sets the expectation of five facts and a recurring diagram.
- **From:** Opens the course; nothing precedes it.
- **Chapter:** Frames the chapter as a mechanism chapter rather than a survey.
- **To:** Leads into the pipeline diagram that carries the whole chapter.
-->

---

## The model turns text into tokens, scores every possible next token, picks one, and repeats

```mermaid {scale: 0.90}
flowchart LR
  A["your text"] --> B["split into<br/>tokens"]
  B --> C["token IDs<br/>(numbers)"]
  C --> D["network"]
  D --> E["a score for<br/>every token"]
  E --> F["pick one"]
  F --> G["append it"]
  G -->|"repeat"| C
  F --> H["output text"]
```

<div class="mt-3 text-sm opacity-80">

Every box is covered in this chapter. The loop is the whole mechanism.

</div>

<!--
- **Says:** Gives the full pipeline as one diagram: text, tokens, IDs, network, scores, selection, append, repeat.
- **From:** Follows the title slide by immediately showing the operation it promised.
- **Chapter:** This is the chapter's spine; every later slide expands one box of it.
- **To:** Leads into the first box that needs defining, the token.
-->

---

## A token is a chunk of characters from a fixed vocabulary

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

- Fixed **before** training
- Typically 3–4 characters in English
- The model never sees letters
- It sees **token IDs** — integers

</div>
<div>

<div class="p-4 border-l-4 text-sm" style="border-color:#0E5C68; background:#F2F7F8">

Roughly 50,000–100,000 tokens in a typical vocabulary.

Anything not in it gets split into pieces that are.

</div>

</div>
</div>

<div class="mt-4 text-sm opacity-80">

**TODO(capture)** — run a real tokeniser on one sentence and screenshot the split.

</div>

<!--
- **Says:** Defines a token positively: a fixed-vocabulary chunk of characters, fixed before training, represented to the model as an integer ID.
- **From:** Follows the pipeline diagram by defining its second box.
- **Chapter:** Supplies the unit that every later cost, context and billing claim is measured in.
- **To:** Leads into what token splitting costs the audience specifically.
-->

---

## Technical terms cost more tokens than common words

<img src="/figures/01-token-cost.png" class="h-56 mt-2 mx-auto" alt="Horizontal bars showing common words taking one token and technical terms taking three to four" />

<div class="grid grid-cols-3 gap-4 mt-3 text-sm">
<div>

**Billing**
per token

</div>
<div>

**Context limit**
counted in tokens

</div>
<div>

**Throughput**
quoted per token

</div>
</div>

<!--
- **Says:** Shows that technical vocabulary splits into more tokens than common words, and names the three places that costs the audience.
- **From:** Follows the token definition with its practical consequence.
- **Chapter:** Converts an abstract unit into something the audience pays for, which is why the definition mattered.
- **To:** Leads into what the network does once it has the token IDs.
-->

---

## The network outputs a score for every token in its vocabulary

<img src="/figures/01-scores.png" class="w-full mt-2" alt="Left panel, raw scores per candidate token. Right panel, the same scores after softmax, summing to one" />

<div class="mt-2 text-sm">

Those raw scores are called **logits**. Higher score, more likely next token.

</div>

<!--
- **Says:** Establishes that the network emits one score per vocabulary token, names those scores logits, and shows them before and after normalisation.
- **From:** Follows the token-cost slide by moving to the next box of the pipeline, the network output.
- **Chapter:** Introduces logits, without which temperature two slides later is meaningless.
- **To:** Leads into where the randomness actually enters.
-->

---

## The network is deterministic — the randomness is added afterwards

```mermaid {scale: 0.95}
flowchart LR
  A["same input"] --> B["network"]
  B --> C["same scores<br/>every time"]
  C --> D{"pick one"}
  D --> E["token A"]
  D --> F["token B"]
  D --> G["token C"]
  style B fill:#E0EDEF,stroke:#0E5C68
  style D fill:#F8F1E7,stroke:#97591A
```

<div class="grid grid-cols-2 gap-8 mt-3 text-sm">
<div>

**Deterministic**
Same input → same scores

</div>
<div>

**Probabilistic**
The pick, not the scores

</div>
</div>

<!--
- **Says:** Separates the deterministic network, which returns identical scores for identical input, from the probabilistic selection step that follows it.
- **From:** Follows the scores slide by answering where variation comes from, given that the scores are fixed.
- **Chapter:** This distinction is what makes temperature and run-to-run variation comprehensible rather than mysterious.
- **To:** Leads into the function that converts scores into the probabilities used for that pick.
-->

---

## Softmax converts scores into probabilities

$$p_i \;=\; \frac{\exp\!\big(\overbrace{z_i}^{\text{score for token }i}\big/\underbrace{T}_{\text{temperature}}\big)}{\underbrace{\sum_j \exp(z_j/T)}_{\text{sum over every token, so the result sums to }1}}$$

<div class="mt-6 text-sm">

**Worked case — two tokens scoring 2.0 and 1.0**

</div>

<div class="text-sm mt-1">

| $T$ | $p$(first) | $p$(second) |
|---|---|---|
| 0.5 | 0.881 | 0.119 |
| 1.0 | 0.731 | 0.269 |
| 2.0 | 0.622 | 0.378 |

</div>

<!--
- **Says:** States the softmax formula with each symbol annotated on the equation itself, and works one two-token case at three temperatures.
- **From:** Follows the deterministic-probabilistic slide by giving the function that produces the probabilities being sampled from.
- **Chapter:** Supplies the only equation in the chapter, and the one the audience can check by hand.
- **To:** Leads into what changing T actually does across a full vocabulary.
-->

---

## Temperature controls how sharply the highest score wins

<img src="/figures/01-temperature.png" class="w-full mt-2" alt="One set of scores rendered as probabilities at four temperatures, sharpening as temperature falls" />

<div class="grid grid-cols-3 gap-4 mt-3 text-sm">
<div>

**Low T**
one token dominates

</div>
<div>

**T = 1**
scores used as-is

</div>
<div>

**High T**
choice spreads out

</div>
</div>

<!--
- **Says:** Shows the same score vector rendered as probabilities at four temperatures, with the sharpening effect visible across the panels.
- **From:** Follows the worked two-token case by scaling the same effect to a full vocabulary.
- **Chapter:** Completes the selection step of the pipeline diagram.
- **To:** Leads into the practical consequence the audience has already experienced.
-->

---

## The same prompt gives different answers because a token is sampled

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

**What you see**

- Same question, two runs
- Two different answers
- Neither is an error

</div>
<div>

**Why**

- Scores identical both times
- The pick differs
- $T = 0$ returns the top token every time

</div>
</div>

<div class="mt-5 p-4 border-l-4 text-sm" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(capture)** — one prompt, five runs, five answers, recorded with the model ID and date.

</div>

<!--
- **Says:** Explains observed run-to-run variation as a consequence of sampling rather than of error, and notes that temperature zero removes it.
- **From:** Follows the temperature slide by applying it to something the room has already experienced.
- **Chapter:** Converts the mechanism into a prediction about the audience's own use.
- **To:** Leads into the limit on what the model can condition its scores on.
-->

---

## The model uses only the tokens inside its context window

```mermaid {scale: 0.95}
flowchart LR
  subgraph W["context window — fixed maximum, counted in tokens"]
    A["system<br/>instructions"] --- B["your<br/>prompt"] --- C["pasted<br/>files"] --- D["conversation<br/>so far"]
  end
  W --> E["network"]
  F["everything else<br/>you have ever written"] -.->|"not visible"| E
  style F stroke-dasharray: 4 4
```

<div class="mt-3 text-sm opacity-80">

Not storage. Not a database. It is the input to one forward pass.

</div>

<!--
- **Says:** Shows the context window as the complete and only input to the network, holding instructions, prompt, files and history up to a fixed token maximum.
- **From:** Follows the sampling slide by bounding what the scores can be conditioned on in the first place.
- **Chapter:** Introduces the bound that Chapters 5 and 7 later measure and price.
- **To:** Leads into how material gets into that window from outside.
-->

---

## Web search and file reading put text into the window — prediction is unchanged

```mermaid {scale: 0.93}
flowchart LR
  A["web search"] --> W["context window"]
  B["file read"] --> W
  C["your prompt"] --> W
  W --> D["network"]
  D --> E["scores"]
  style W fill:#E0EDEF,stroke:#0E5C68
```

<div class="mt-3 text-sm">

The tool fetches. The window holds. The prediction step is identical either way.

</div>

<!--
- **Says:** Corrects the assumption that retrieval changes the mechanism, showing search and file reading as separate tools that write into the window before prediction runs unchanged.
- **From:** Follows the context-window slide by answering the obvious objection that the model can look things up.
- **Chapter:** Keeps the chapter's central claim accurate for tools that do retrieve, and sets up Chapters 12 and 14.
- **To:** Leads into what happens to that window when the session ends.
-->

---

## Nothing carries over when the session ends

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

**Discarded**

- The window
- The conversation
- Anything you pasted

</div>
<div>

**Unchanged**

- The weights
- Talking to it teaches it nothing

</div>
</div>

<div class="mt-5 text-sm">

When a tool appears to remember your project, something outside the model put that text back into the window.

</div>

<!--
- **Says:** States that the window and conversation are discarded at session end and that the weights are unaffected by use.
- **From:** Follows the retrieval slide by closing out the window's lifecycle.
- **Chapter:** Completes the last box of the pipeline and sets the limit Chapter 10 exists to work around.
- **To:** Leads into the chapter summary.
-->

---

## Five facts

<div class="text-sm mt-3">

| | |
|---|---|
| 1 | Text is split into **tokens** from a fixed vocabulary |
| 2 | The network scores **every** token in that vocabulary |
| 3 | The network is **deterministic**; the pick is not |
| 4 | It conditions only on the **context window** |
| 5 | The window is **discarded** at the end of the session |

</div>

<div class="mt-5">

Everything in the next eighteen chapters is a consequence of these five.

</div>

<!--
- **Says:** Restates the chapter as five numbered facts covering tokens, scoring, determinism, the window, and its discard.
- **From:** Follows the persistence slide by collecting the chapter into a form the audience can carry.
- **Chapter:** Is the chapter's takeaway for anyone attending only this session.
- **To:** Leads into what the chapter deliberately omits.
-->

---

## Three things this chapter leaves out

<div class="text-sm mt-3">

| Omitted | Why |
|---|---|
| How attention works internally | Changes no decision you will make |
| Positional encoding | Same |
| Multi-head attention | Same |

</div>

<div class="mt-5">

Chapter 2 answers the question this chapter raises: if it only predicts text, why does it behave like an assistant?

</div>

<!--
- **Says:** Names the three architectural topics the chapter excludes and gives the same reason for each, then states the question Chapter 2 answers.
- **From:** Follows the summary by bounding what was and was not claimed.
- **Chapter:** Keeps the chapter honest about its scope, and hands off explicitly.
- **To:** Leads into Chapter 2, which explains how a next-token predictor came to behave like an assistant.
-->

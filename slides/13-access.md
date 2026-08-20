---
theme: default
title: Chapter 13 — Access
info: Keys, endpoints, and what a call costs. Closes the cost thread. Carries the price-to-architecture worked example.
class: text-left
mdc: true
---

# Chapter 13 — Access

### Keys, endpoints, and what a call costs

<div class="mt-10 text-xl opacity-85">

The cost thread has run through six chapters as a physical quantity. Here it becomes
an invoice.

</div>

---

## What a key authorises

<v-clicks>

- A key is a bearer credential. Whoever holds it is you, to the billing system.
- **A paid chat subscription does not include API access.** They are separate products with separate billing, and this surprises people every time.
- API usage is billed against prepaid credit, per token, with no monthly ceiling protecting you.

</v-clicks>

<Cite k="claudecode-docs" />

---

## Key hygiene, in four rules

<v-clicks>

- **Environment variables, never source.** A key in a script is a key in your shell history and your editor's autosave.
- **Never in a shared repository.** Not in a private one either — private repositories get shared.
- **One key per person**, so a leak can be traced and revoked without stopping everyone.
- **Rotate on any doubt.** Rotation is cheap. Establishing that a key was not misused is not.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

The group's local gateway issues per-user keys with per-user budgets. That is the
mechanism that makes an exercise safe to run in a room.

</div>

---

## Worked example: architecture from a price list

A published price break at a stated context length is enough to solve for something the
vendor never published.

<div class="deriv mt-4">

<div v-click="1">

price step at a stated context length

</div>
<div v-click="1">

$\Rightarrow$

</div>
<div v-click="1">

extra cost attributable to cached context

</div>

<div v-click="2">

$\div$ tokens of context

</div>
<div v-click="2">

$\Rightarrow$

</div>
<div v-click="2">

cost per cached token

</div>

<div v-click="3">

$\div$ price per byte-hour

</div>
<div v-click="3">

$\Rightarrow$

</div>
<div v-click="3">

**bytes per token in the KV cache**

</div>

</div>

<div v-click="4" class="mt-6">

Checked when this was recorded, the answer came out at roughly **1.7 kB per token** —
then sanity-checked against plausible head dimensions and KV head counts, which is the
step that turns arithmetic into evidence.

</div>

<Cite k="pope2026" />

<style>
.deriv :deep(p) { margin: 0; }
.deriv { display: grid; grid-template-columns: max-content max-content 1fr;
         column-gap: .8rem; row-gap: .9rem; align-items: baseline; font-size: 1.05rem; }
</style>

---

## Why that example is in this course

<v-clicks>

- **Order-of-magnitude estimation** from public numbers, which is a skill this room already has and does not apply here.
- **Dimensional analysis** — the units carry the derivation, exactly as in Chapter 7.
- **An independent check.** The answer is only worth anything because it was tested against something it was not derived from.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**TODO(verify) before delivery.** The figure above is what the method produced when it was
recorded. Pricing structures change, and a stale number presented as current is the
failure this course spends three sessions warning about. **Re-run the arithmetic on the
current price list.** The method is the transferable part; the number is not.

</div>

---

## Local against frontier, side by side

<v-clicks>

- Same prompt. The group's own local model, and a frontier model. Both projected.
- This is the best available demonstration of everything in Chapter 5, on hardware the group already owns.
- Expect the local model to be worse in a specific, visible, instructive way — not uniformly worse.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**TODO(capture)** — needs the local machine reachable from the training room. If it is not,
this becomes an instructor demo and keys are distributed afterwards. `DECISIONS.md` item 4.

</div>

---

## Closing the cost thread

<v-clicks>

- **Metered pricing.** Per token, in and out, at different rates. Chapter 1's unit of meaning, priced.
- **Caching.** Re-sending the same standing context every turn is the cost Chapter 10 made you calculate. Caching is the mitigation, and it has its own price.
- **Batch discounts.** Latency traded for money, which is Chapter 7's roofline seen from the finance side.
- **Subscription against per-token.** Different economics, and the crossover depends on how you actually work, not on the headline rate.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-75 border-t pt-3">

**Thread — cost, closed.** Token as unit of meaning in Chapter 1, unit of price in Chapter 7,
resident context in Chapter 10, orchestration premium in Chapter 11, and an invoice here.

</div>

---

## Where this leaves us

<v-clicks>

- A credential model you can explain to whoever administers your grant.
- A worked example where public prices yielded an unpublished architectural number.
- A cost thread that started as a token and finished as a line item.

</v-clicks>

<div v-click class="mt-10 text-xl">

Session 2 ends here. **Session 3 is your actual work.**

</div>

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

<!--
- **Says:** Opens the chapter by naming keys, endpoints and cost as its subject, framing the cost thread as becoming an invoice here.
- **From:** Follows Chapter 12's closing line naming this chapter as what it costs to keep its opened channels running.
- **Chapter:** Serves as the chapter's framing slide, setting up cost as the thread this chapter closes.
- **To:** Leads into the slide on what an API key actually authorises.
-->

---

## What a key authorises

<v-clicks>

- A key is a bearer credential. Whoever holds it is you, to the billing system.
- **A paid chat subscription does not include API access.** They are separate products with separate billing, and this surprises people every time.
- API usage is billed against prepaid credit, per token. **There is no monthly subscription cap** — your exposure is the credit you have loaded, plus whatever auto-reload you switch on. Prepaid is the ceiling; auto-reload is how people remove it without noticing.

</v-clicks>

<Cite k="claudecode-docs" />

<!--
- **Says:** States that a key is a bearer credential, that a chat subscription does not include API access, and that API billing has no monthly cap.
- **From:** Follows the title slide's framing of cost-as-invoice by opening on the credential that triggers any charge.
- **Chapter:** Opens the chapter's credential-mechanics content ahead of the key-hygiene rules that follow.
- **To:** Leads into the slide on handling that credential safely.
-->

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

<!--
- **Says:** Gives four rules for handling an API key: environment variables, never a shared repository, one key per person, and rotation on doubt.
- **From:** Follows the key-authorisation slide by turning to how to handle the credential just described.
- **Chapter:** Delivers practical safety content ahead of the room using its own keys later in the chapter.
- **To:** Leads into the worked example that reverse-engineers architecture from published pricing.
-->

---

## Worked example: architecture from a price list

A published price step at a stated context length is enough to solve for something the
vendor never published — **if you state every input.**

<div class="deriv mt-3">

<div v-click="1">

$C_\mathrm{extra}$

</div>
<div v-click="1">

$[\mathrm{cost}]$

</div>
<div v-click="1">

extra charge on one request, attributable to holding the long context

</div>

<div v-click="2">

$L$

</div>
<div v-click="2">

$[\mathrm{token}]$

</div>
<div v-click="2">

context length the step is quoted at

</div>

<div v-click="3">

$t_\mathrm{res}$

</div>
<div v-click="3">

$[\mathrm{hour}]$

</div>
<div v-click="3">

how long the cache stays resident while the request is served

</div>

<div v-click="4">

$p_\mathrm{bh}$

</div>
<div v-click="4">

$[\mathrm{cost}\cdot\mathrm{byte^{-1}\,hour^{-1}}]$

</div>
<div v-click="4">

price of one byte-hour of device memory

</div>

</div>

<div v-click="5" class="mt-5">

$$b_\mathrm{kv} \;=\; \frac{C_\mathrm{extra}}{L \; t_\mathrm{res} \; p_\mathrm{bh}}$$

$$\frac{\mathrm{cost}}{\mathrm{token}\cdot\mathrm{hour}\cdot\mathrm{cost}\cdot\mathrm{byte^{-1}\,hour^{-1}}}\;=\;\frac{\mathrm{byte}}{\mathrm{token}} \quad\checkmark$$

</div>

<Cite k="pope2026" />


<style>
.deriv :deep(p) { margin: 0; }
.deriv { display: grid; grid-template-columns: max-content max-content 1fr;
         column-gap: .8rem; row-gap: .9rem; align-items: baseline; font-size: 1.05rem; }
</style>

<!--
- **Says:** Sets up the derivation, defining four input quantities and deriving a byte-per-token formula with a dimensional check.
- **From:** Follows the key-hygiene slide by turning from handling credentials to using published pricing data itself.
- **Chapter:** Delivers the chapter's named worked example, combining order-of-magnitude estimation with dimensional analysis.
- **To:** Leads into the slide examining the two unpublished inputs the derivation depends on.
-->

---

## The two inputs that decide the answer

Neither is published. Both have to be constructed, and the result is only as good as they are.

<v-clicks>

- **Residency time $t_\mathrm{res}$.** The cache occupies memory for the duration of the request, not for an hour. Get this wrong by 10× and the answer is wrong by 10×.
- **The byte-hour price $p_\mathrm{bh}$.** No vendor quotes one. You build it: accelerator price per hour ÷ bytes of memory per accelerator.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**This is the denominator problem again.** The house rule from Chapter 4 says that where an
equation's denominator is defined non-obviously, the definition goes beside it. $p_\mathrm{bh}$
is exactly that, and it is the first thing a hostile reader attacks. State it on the slide or
do not put the number up.

</div>

<!--
- **Says:** Identifies residency time and the byte-hour price as the two unpublished inputs the derivation depends on, and reconnects to Chapter 4's denominator rule.
- **From:** Follows the worked-example slide by scrutinising the two inputs it introduced but did not defend.
- **Chapter:** Extends the worked example and explicitly reapplies Chapter 4's rule that a non-obvious denominator must be defined beside the equation.
- **To:** Leads into the slide that sanity-checks the number the derivation produced.
-->

---

## Sanity-check it, and watch the check strain

The figure recorded from this method is roughly **1.7 kB per token**. Test it against
architecture:

$$b_\mathrm{kv} \;=\; \underbrace{2}_{K \text{ and } V} \times n_\mathrm{layers} \times n_\mathrm{kv} \times d_\mathrm{head} \times \underbrace{2}_{\mathrm{byte}}$$

<v-clicks>

- Setting that to 1700 bytes needs $n_\mathrm{layers} \times n_\mathrm{kv} \times d_\mathrm{head} \approx 425$.
- At 60 layers that is about **7 per layer** — smaller than a single head of dimension 64.
- So either the model compresses KV far past ordinary grouped-query attention, **or the 1.7 kB is per layer**, not whole-model.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**TODO(verify) — the deck does not currently know which.** Read the source transcript and
state it. An undeclared per-what is the MACs-versus-FLOPs erratum wearing a different hat,
three chapters after that erratum was taught as the anchor of Chapter 4.

**And re-run the arithmetic on current prices before delivery.** The method transfers; the
number does not.

</div>

<Cite k="pope2026" />


<!--
- **Says:** Tests the derived 1.7 kB-per-token figure against plausible architecture parameters, finds it strains, and leaves an open TODO(verify) on what the figure actually measures.
- **From:** Follows the two-inputs slide by applying the check to the number that derivation produced.
- **Chapter:** Demonstrates the independent-check discipline and leaves the unresolved question flagged rather than asserted.
- **To:** Leads into the slide stating why this worked example belongs in the course.
-->

---

## Why that example is in this course

<v-clicks>

- **Order-of-magnitude estimation** from public numbers, which is a skill this room already has and does not apply here.
- **Dimensional analysis** — the units carry the derivation, exactly as in Chapter 7.
- **An independent check.** The answer is only worth anything because it was tested against something it was not derived from.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#97591A; background:#F8F1E7">

**The whole point is that you can do this.** A price list is public, an architecture is not,
and dimensional analysis crosses the gap — provided every input is declared. Two slides ago
one of them was not, which is why the check strains.

</div>

<!--
- **Says:** Names order-of-magnitude estimation, dimensional analysis and an independent check as the three skills the worked example demonstrates.
- **From:** Follows the sanity-check slide by stepping back to state the point of the derivation that just strained.
- **Chapter:** Closes the worked-example sequence by naming its purpose explicitly.
- **To:** Leads into the "Your first call" hands-on slide, moving from the worked example to the room's own API use.
-->

---

## Your first call

The brief for this session is not "understand the API". It is **make one call and change
one thing.**

<v-clicks>

1. Point a client at the group's gateway with your own key. Confirm you get a response at all before changing anything.
2. Send the same prompt twice, unchanged. **You already know what to expect** — Chapter 1 said the sampler is stochastic and Chapter 4 made you measure the spread.
3. Now vary one parameter at a time — temperature, max tokens, the system prompt — and watch which ones change the answer and which change only the bill.
4. Read the usage figures that come back with the response. That is the number Chapter 7 derived and this chapter prices.

</v-clicks>

<div v-click class="mt-5 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**BLOCKED — needs the local machine reachable from the training room.** `DECISIONS.md` item 4
blocks *this* exercise, not only the comparison demo two slides on. If the machine is not
reachable, this becomes an instructor demo and keys go out afterwards.

</div>

<!--
- **Says:** Lays out a four-step exercise for making an API call and varying one parameter at a time, then states it is BLOCKED pending a locally reachable machine.
- **From:** Follows the worked-example rationale slide by turning from analysis to the room's own hands-on practice.
- **Chapter:** Presents the chapter's central exercise but marked blocked per DECISIONS.md item 4 rather than presented as runnable.
- **To:** Leads into the local-versus-frontier comparison slide, blocked by the same missing machine.
-->

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

<!--
- **Says:** Describes a projected side-by-side comparison of the group's local model against a frontier model, flagged TODO(capture) pending the same reachable local machine.
- **From:** Follows "Your first call" by extending the hands-on section into a second, comparative demo.
- **Chapter:** Revisits Chapter 5's failure material live but remains unresolved pending the same blocking dependency.
- **To:** Leads into the slide that returns to close the chapter's cost thread.
-->

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

<!--
- **Says:** Closes the cost thread across metered pricing, caching, batch discounts, and subscription-versus-per-token economics.
- **From:** Follows the two blocked hands-on slides by returning to the chapter's core content and drawing it to a close.
- **Chapter:** Carries the chapter's explicit cost-thread closing marker, tracing it from Chapter 1 through Chapters 7, 10 and 11 to this invoice.
- **To:** Leads into the chapter's final summary slide.
-->

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

<!--
- **Says:** Summarises the chapter's three takeaways: the credential model, the worked example, and the now-closed cost thread.
- **From:** Follows the cost-thread closing slide by giving the chapter's final recap.
- **Chapter:** Closes Chapter 13 and Session 2 together.
- **To:** Hands off to Chapter 14 — Literature, opening Session 3 on research practice.
-->

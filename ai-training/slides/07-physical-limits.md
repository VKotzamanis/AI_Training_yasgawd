---
theme: default
title: Chapter 7 — Physical limits
info: Spike. Tests whether Slidev can build a multi-line aligned derivation stepwise, with a citation footer attached.
class: text-left
mdc: true
---

# Chapter 7 — Physical limits

Tokens were the unit of meaning. Here they become the unit of price.

<div class="mt-8 opacity-80">

This is a **governing-constraint analysis**. You already do this with load paths
and limit states: find the binding constraint, then reason about what relaxes it.

</div>

<Cite k="pope2026" />

<!--
- **Says:** Opens the chapter by reframing tokens from a unit of meaning into a unit of price, and names the analysis as governing-constraint reasoning.
- **From:** Chapter 6 finished the failure modes, so this chapter turns from what breaks to what it costs to run.
- **Chapter:** States the chapter's method and its analogy to load paths and limit states before any derivation begins.
- **To:** Leads into the slide scoping the chapter to cost and latency only, not accuracy.
-->

---

## What this chapter does not tell you

This chapter is about **cost and latency**. It says nothing about **accuracy**.

<v-clicks>

- There is an equation for what a long context costs. You are about to derive it, and it closes.
- There is no equation for what a long context does to accuracy. There are empirical curves and mechanistic arguments, and they are Chapter 5.
- Conflating the two is the easiest mistake to make with this material, precisely because the cost result is clean and the accuracy result is not.

</v-clicks>

<div v-click class="mt-8 text-lg">

A long context is expensive and slow. Whether it is also **wrong** is a different
question with a different kind of answer.

</div>

<!--
- **Says:** States explicitly that the chapter covers cost and latency only, and that long-context accuracy is Chapter 5's material.
- **From:** Follows the opening slide's framing by immediately bounding what the chapter claims.
- **Chapter:** Pre-empts the cost-versus-accuracy conflation the project's own house rules flag as the likeliest error.
- **To:** Leads into the slide disclosing the source and its conflicts of interest.
-->

---

## Where this comes from, and who benefits from it

The construction that follows is from a blackboard lecture, published as a podcast transcript.

<v-clicks>

- It is **expert testimony**, not a peer-reviewed result. The footer says so on every slide that uses it.
- The speaker is CEO of a chip company. The interviewer discloses being an angel investor in that company.
- The lecture's central conclusion — that **memory bandwidth is the binding constraint** — is commercially convenient for both of them.

</v-clicks>

<div v-click class="mt-8">

The analysis still appears sound, and you are about to check the algebra yourself.

**Declaring an interest is not the same as rejecting the work.** Doing neither is what
gets you in trouble, and it is the habit Chapter 18 asks of you in your own writing.

</div>

<Cite k="pope2026" />

<!--
- **Says:** Discloses that the derivation comes from expert testimony, not peer review, and names the speaker's and interviewer's commercial interests.
- **From:** Follows the scope-limiting slide by disclosing the source before any number from it is used.
- **Chapter:** Applies the course's conflict-of-interest standard to the chapter's own primary source.
- **To:** Leads into the symbol table the derivation will use.
-->

---

## Symbols

All quantities positive definite — no sign convention is required. SI throughout.

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | batch size, tokens per forward pass | — |
| $N_\mathrm{act}$ | active parameters per token | — |
| $N_\mathrm{tot}$ | total parameters | — |
| $F$ | arithmetic throughput | $\mathrm{FLOP\,s^{-1}}$ |
| $M$ | throughput in multiply-accumulates, $1\,\mathrm{MAC}=2\,\mathrm{FLOP}$ | $\mathrm{MAC\,s^{-1}}$ |
| $b_w$ | bytes per stored parameter | $\mathrm{byte}$ |
| $b_\mathrm{kv}$ | KV bytes per token of context | $\mathrm{byte\,token^{-1}}$ |
| $L$ | context length | $\mathrm{token}$ |
| $\beta$ | memory bandwidth | $\mathrm{byte\,s^{-1}}$ |

<Cite k="pope2026" />

<!--
- **Says:** Defines every symbol and unit used in the roofline derivation that follows.
- **From:** Follows the source-disclosure slide by setting up notation before deriving anything.
- **Chapter:** Supplies the dimensional bookkeeping the chapter's house style requires for every equation.
- **To:** Leads into the roofline bound derivation itself.
-->

---

## The roofline bound

<div class="deriv">

<div v-click="1">

$T$

</div>
<div v-click="1">

$\ge$

</div>
<div v-click="1">

$\max\left(T_\mathrm{comp},\ T_\mathrm{mem}\right)$

</div>

<div v-click="2">

$T_\mathrm{comp}$

</div>
<div v-click="2">

$=$

</div>
<div v-click="2">

$\dfrac{2\,B\,N_\mathrm{act}}{F}\;=\;\dfrac{B\,N_\mathrm{act}}{M}$

</div>

<div v-click="3">

$T_\mathrm{mem}$

</div>
<div v-click="3">

$=$

</div>
<div v-click="3">

$\dfrac{\overbrace{N_\mathrm{tot}\,b_w}^{\text{weight fetch}}\;+\;\overbrace{B\,L\,b_\mathrm{kv}}^{\text{KV fetch}}}{\beta}$

</div>

<div v-click="4">

$c$

</div>
<div v-click="4">

$\equiv$

</div>
<div v-click="4">

$\dfrac{T}{B}$

</div>

<div v-click="5">

$\dfrac{T_\mathrm{mem}}{B}$

</div>
<div v-click="5">

$=$

</div>
<div v-click="5">

$\underbrace{\dfrac{N_\mathrm{tot}\,b_w}{\beta\,B}}_{\propto\,1/B}\;+\;\underbrace{\dfrac{L\,b_\mathrm{kv}}{\beta}}_{\text{constant in }B}$

</div>

</div>

<div v-click="6" class="mt-6 text-sm opacity-85">

**Dimensions.** $2BN_\mathrm{act}$ is a FLOP count, so $T_\mathrm{comp}$ is $\mathrm{FLOP}/(\mathrm{FLOP\,s^{-1}})=\mathrm{s}$.
$N_\mathrm{tot}b_w + BLb_\mathrm{kv}$ is bytes, so $T_\mathrm{mem}$ is $\mathrm{byte}/(\mathrm{byte\,s^{-1}})=\mathrm{s}$. Cost $c$ is $\mathrm{s\,token^{-1}}$.

</div>

<Cite k="pope2026" />

<style>
.deriv :deep(p) { margin: 0; }
.deriv {
  display: grid;
  grid-template-columns: max-content max-content 1fr;
  column-gap: .6rem;
  row-gap: 1.05rem;
  align-items: baseline;
  font-size: 1.05rem;
}
</style>

<!--
- **Says:** Derives the roofline bound, splitting memory time into a weight-fetch term and a KV-fetch term, with a dimensional check.
- **From:** Follows the symbol table by carrying out the derivation those symbols were defined for.
- **Chapter:** Delivers the chapter's central governing-constraint result.
- **To:** Leads into the interpretation of the resulting hyperbola in cost per token.
-->

---

## What the hyperbola says

<div v-click="1">

The weight-fetch term carries $1/B$. At $B=1$ every parameter in the model is
read from memory to produce **one** token.

</div>

<div v-click="2" class="mt-4">

As $B$ grows that term amortises and cost flattens onto the KV floor
$L\,b_\mathrm{kv}/\beta$, which $B$ does not help — it is linear in
context length and paid per token regardless.

</div>

<div v-click="3" class="mt-4">

**Consequence.** Long context is bounded by memory bandwidth and capacity, not
by compute. That is a different claim from anything about accuracy, which has
no equation and is Chapter 5's material.

</div>

<Cite k="pope2026" />

<!--
- **Says:** Interprets the roofline result, the weight-fetch cost amortising with batch size while the KV floor stays fixed per token.
- **From:** Follows the roofline derivation by interpreting what it means physically.
- **Chapter:** States the chapter's key consequence, that long context is memory-bound rather than compute-bound.
- **To:** Leads into the critical batch size derivation.
-->

---

## Critical batch size

<div class="deriv">

<div v-click="1">

$T_\mathrm{comp}$

</div>
<div v-click="1">

$=$

</div>
<div v-click="1">

$T_\mathrm{mem}^{\,\text{(weight)}}$

</div>

<div v-click="2">

$\dfrac{2\,B^{*}N_\mathrm{act}}{F}$

</div>
<div v-click="2">

$=$

</div>
<div v-click="2">

$\dfrac{N_\mathrm{tot}\,b_w}{\beta}$

</div>

<div v-click="3">

$B^{*}$

</div>
<div v-click="3">

$=$

</div>
<div v-click="3">

$\underbrace{\dfrac{F\,b_w}{2\,\beta}}_{\text{hardware ratio}}\times\underbrace{\dfrac{N_\mathrm{tot}}{N_\mathrm{act}}}_{\text{sparsity}}$

</div>

</div>

<div v-click="4" class="mt-6">

The source reports the hardware ratio as $\approx 300$, dimensionless and stable
across several GPU generations. Critical batch size is then $\approx 300 \times$ sparsity.

</div>

<Cite k="pope2026" />

<style>
.deriv :deep(p) { margin: 0; }
.deriv {
  display: grid;
  grid-template-columns: max-content max-content 1fr;
  column-gap: .6rem; row-gap: 1.05rem; align-items: baseline; font-size: 1.05rem;
}
</style>

<!--
- **Says:** Derives critical batch size as a hardware ratio times model sparsity, citing the source's reported value of about 300.
- **From:** Follows the hyperbola interpretation by deriving the batch size at which the two cost terms balance.
- **Chapter:** Extends the roofline result into a second concrete, checkable number.
- **To:** Leads into the slide isolating the denominator convention as the whole argument.
-->

---

## The denominator is the whole argument

<div v-click="1">

$T_\mathrm{comp}$ was written twice above, and the two forms are not interchangeable:

</div>

<div class="deriv mt-4">
<div v-click="2">

$T_\mathrm{comp}$

</div>
<div v-click="2">

$=$

</div>
<div v-click="2">

$\dfrac{B\,N_\mathrm{act}}{M}$<span class="ml-3 text-sm opacity-70">$M$ in $\mathrm{MAC\,s^{-1}}$</span>

</div>
<div v-click="3">

$T_\mathrm{comp}$

</div>
<div v-click="3">

$=$

</div>
<div v-click="3">

$\dfrac{2\,B\,N_\mathrm{act}}{F}$<span class="ml-3 text-sm opacity-70">$F$ in $\mathrm{FLOP\,s^{-1}}$</span>

</div>
</div>

<div v-click="4" class="mt-6">

Substituting a spec-sheet $\mathrm{FLOP\,s^{-1}}$ into the MAC-denominated form
makes the answer **wrong by exactly a factor of two**. An outside reader caught
this in the transcript's comment thread.

</div>

<div v-click="5" class="mt-4 opacity-85">

A unit-definition error, in an expert lecture, found by peer review, producing a
clean factor of two. Chapter 4 uses this as its anchor.

</div>

<Cite k="pope2026" />

<style>
.deriv :deep(p) { margin: 0; }
.deriv { display: grid; grid-template-columns: max-content max-content 1fr;
         column-gap: .6rem; row-gap: 1.05rem; align-items: baseline; font-size: 1.05rem; }
</style>

<!--
- **Says:** Shows that the compute-time term written in MACs and in FLOPs is not interchangeable, and substituting one for the other is wrong by exactly two.
- **From:** Follows the critical-batch-size derivation by returning to the compute term used inside it.
- **Chapter:** Delivers the MACs-versus-FLOPs erratum that Chapter 4 later uses as its anchor.
- **To:** Leads into the two related FLOP-counting figures for training.
-->

---

## Two numbers you will see quoted

From the compute term already on the board, a forward pass costs about **two FLOP per
parameter per token** — one multiply and one add per weight.

$$\text{forward} \;\approx\; 2\,N D \quad [\mathrm{FLOP}]$$

<div class="text-sm opacity-80 mt-1">

$N$ — parameters, $D$ — tokens processed. Both dimensionless counts.

</div>

<v-clicks>

- That is not a new result. It is the numerator of $T_\mathrm{comp}$, read at the scale of a whole training run instead of one batch.
- Training is conventionally accounted at **three times** the forward cost — forward, plus a backward pass computing gradients with respect to both activations and weights — giving $6ND$.

</v-clicks>

<div v-click class="mt-6 p-3 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**TODO(cite)** — $2ND$ follows from what is already on the board. The factor of three
does not, and is standard accounting rather than something derived here. Search:
`6ND training FLOPs derivation` · `Chinchilla compute optimal 6ND` · `Kaplan scaling laws compute budget`.

</div>

<Cite k="pope2026" />

<!--
- **Says:** States the 2ND forward-pass FLOP estimate and the conventional 6ND training estimate, flagging the factor of three as unreferenced here.
- **From:** Follows the denominator slide by extending the same compute term to training-scale accounting.
- **Chapter:** Extends the roofline numerator to a widely quoted training-cost figure, with an open citation task.
- **To:** Leads into the device memory-capacity formula.
-->

---

## What has to fit on the device

$$M_\text{device} \;=\; \frac{N_\mathrm{tot}\,b_w \;+\; B\,L\,b_\mathrm{kv}}{E_\mathrm{p} \times P_\mathrm{p}} \quad [\mathrm{byte}]$$

<div class="text-sm opacity-80 mt-1">

$E_\mathrm{p}$ — expert parallelism, $P_\mathrm{p}$ — pipeline parallelism. Both dimensionless counts.

</div>

<v-clicks>

- The same two terms as before — weights, and KV — now divided across devices.
- **Note the units.** The source states this as *parameters plus KV bytes*. Parameters are a count; only $N_\mathrm{tot}\,b_w$ is a quantity of bytes. The formula is right once you read it that way, and this is exactly the denominator problem from three slides ago wearing a different hat.

</v-clicks>

<Cite k="pope2026" />

<!--
- **Says:** Gives the device memory-capacity formula across expert and pipeline parallelism, flagging the same units caveat as the denominator slide.
- **From:** Follows the training-FLOPs slide by returning to the memory side of the roofline bound.
- **Chapter:** Applies the same units discipline to a second formula from the same source.
- **To:** Leads into the specific claim that pipelining does not help the KV cache.
-->

---

## Pipelining does not help the KV cache

<v-clicks>

- Splitting the model across pipeline stages reduces **weight** storage per rack. That part works.
- It does **not** reduce KV storage. The source states that the pipeline-stage factor cancels.

</v-clicks>

<div v-click class="mt-6 p-3 border-l-4 text-sm" style="border-color:#97591A; background:#F8F1E7">

**TODO(verify)** — the source states the *result*, not the mechanism. A full pipeline
holds one micro-batch per stage, so the batch in flight would scale with the number of
stages and cancel the division. That is a reading, not a quotation. Check it against the
transcript before teaching it as the reason.

</div>

<Cite k="pope2026" />

<!--
- **Says:** States that pipeline parallelism reduces weight storage but not KV storage, and flags the mechanism itself as unverified.
- **From:** Follows the device-capacity formula by drawing out one consequence of it.
- **Chapter:** Marks an unverified reading of the source rather than teaching it as settled.
- **To:** Leads into the summary claim that long context is a memory problem.
-->

---

## Long context is a memory problem, not a compute problem

<v-clicks>

- **Bandwidth.** The KV cache is re-read for every token generated. That term is linear in $L$.
- **Capacity.** The KV cache has to fit. That term is linear in $L$ too.
- Compute is not what binds you at long context. Memory is, at both ends.
- Sparse attention improves the scaling — the source notes it does so at a cost in quality.

</v-clicks>

<div v-click class="mt-8 text-sm opacity-75 border-t pt-3">

**Thread — cost.** This closes the first half. Chapter 10 spends it on resident context,
Chapter 11 on the orchestration premium, Chapter 13 on what you are actually billed.

</div>

<Cite k="pope2026" />

<!--
- **Says:** Summarises that both KV bandwidth and KV capacity scale linearly with context length, binding long context at both ends.
- **From:** Follows the pipelining slide by consolidating the memory-side results into one statement.
- **Chapter:** Closes the first half of the cost thread, as the chapter brief specifies.
- **To:** Leads into the energy comparison between training and inference.
-->

---

## Energy: what can and cannot be said

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

**What can be said**

<v-clicks>

- Training is a one-off cost. Inference is a recurring cost per query.
- They are different quantities with different units, and they are routinely added together.
- Both are real, and both are large.

</v-clicks>

</div>
<div>

**What cannot be said here**

<v-clicks>

- Any per-query figure at all.
- Published numbers are contested and routinely conflate one-off training cost with per-query inference.

</v-clicks>

</div>
</div>

<div v-click class="mt-8 text-lg">

**This slide has no number on it, deliberately.** A number you cannot defend is worse
than no number, in front of a room that will ask where it came from.

</div>

<!--
- **Says:** States what can be defended about training-versus-inference energy and what cannot, deliberately omitting any per-query number.
- **From:** Follows the memory-problem summary by turning to energy, a related but distinct cost dimension.
- **Chapter:** Applies the course's data-integrity standard by refusing an indefensible number.
- **To:** Leads into the comparison table of three alternative compute substrates.
-->

---

## Three alternative substrates. They are not equivalent.

<div class="text-sm mt-2">

| Approach | What has actually been shown | Standing |
|---|---|---|
| **Invertible architectures** | Activations reconstructed from later ones; storage independent of depth at nearly identical accuracy | Published result — but a **training**-time technique |
| **Neuromorphic hardware** | Large energy gains on specific benchmark tasks | Lab demonstration; **not commercially deployed** |
| **Organoid computing** | Tissue that fires, responds to stimulation, and oscillates | **No learning system reported** — the authors' own words |

</div>

<div v-click class="mt-6">

These three get roughly equal airtime in most talks about the future of compute.
They have not earned it. The differences in the right-hand column are the content of
this section, and stating them is the point.

</div>

<!--
- **Says:** Tabulates invertible architectures, neuromorphic hardware and organoid computing against what has actually been shown for each.
- **From:** Follows the energy slide by turning to alternative substrates as a related cost topic.
- **Chapter:** States that the three substrates are not equivalent before treating each individually.
- **To:** Leads into the first of the three, reversible architectures.
-->

---

## Trading compute for memory

Reversible architectures reconstruct each layer's activations from the next layer's,
so they need not be stored. Activation storage becomes independent of depth, at nearly
identical accuracy.

<v-clicks>

- You spend FLOPs to buy back bytes. Against a memory-bound system, that is the right direction to trade.
- **But this is a training-time result.** It addresses storing activations during backpropagation, not the inference-time KV cache this chapter has been pricing.
- Keep the parallel; do not let it slide into a claim about inference.

</v-clicks>

<Cite k="revnets" />

<!--
- **Says:** Explains reversible architectures trading FLOPs for stored bytes, and flags this as a training-time result, not the inference-time KV cache priced earlier.
- **From:** Follows the comparison table with the first substrate treated in detail.
- **Chapter:** Keeps the reversible-architecture parallel from sliding into an inference-time claim.
- **To:** Leads into neuromorphic hardware, the second substrate.
-->

---

## Neuromorphic hardware

Real engineering, real gains, and a gap between the lab and your problem.

<v-clicks>

- Reported: image classification at a fraction of the energy and several times faster; a neuromorphic language model matching a comparable GPU-based one's accuracy at half the energy.
- **Not commercially deployed.** The source describes the leading chips as demonstration and experimentation tools.
- The gains are benchmark-specific and are not shown to transfer to frontier-scale systems. The source states these chips cannot simply be dropped into today's LLM stacks.

</v-clicks>

<div v-click class="mt-6 text-sm opacity-80">

An earlier draft of this course called this "deployed, engineering-grade." Checking the
source corrected it. That correction is worth more to you than the claim was.

</div>

<Cite k="ornes2025" />

<!--
- **Says:** Reports real benchmark-specific gains for neuromorphic chips while stating they are not commercially deployed, correcting an earlier draft's stronger claim.
- **From:** Follows the reversible-architecture slide with the second substrate.
- **Chapter:** Models the course's own correction habit, naming an earlier overstatement and fixing it against a verified source.
- **To:** Leads into organoid and wetware computing, the third substrate.
-->

---

## Organoid and wetware computing

<v-clicks>

- Demonstrated: spontaneous electrophysiological activity, response to stimulation, myelinated axons, oscillatory behaviour, multiple cell types at realistic densities.
- Proposed: training via biofeedback, interfacing with sensors, decoding responses into computational output.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

From the foundational paper itself:

> To the best of our knowledge, however, no relevant approach using brain organoids as
> learning systems has been reported.

</div>

<v-clicks>

- Organoids are avascular, with necrosis beyond roughly 300 μm. They have no predictable anatomy or defined topography.
- What exists is **tissue characterisation, not computation.** "Early stage, modest results" overstates it.

</v-clicks>

<Cite k="smirnova2023" />

<!--
- **Says:** Lists what has been demonstrated in organoid tissue and quotes the foundational paper stating no learning system has been reported.
- **From:** Follows the neuromorphic slide with the third and weakest-evidenced substrate.
- **Chapter:** Closes the three-substrate comparison by holding the organoid claim to the same evidential standard as the others.
- **To:** Leads into the chapter's closing summary of the cost thread.
-->

---

## Where this leaves the cost thread

<v-clicks>

- Time is bounded below by the larger of compute time and memory time, and for the workloads you will run, memory wins.
- Cost per token is a hyperbola in batch size. Batch one is the expensive corner, and it is the corner you sit in.
- Long context is bounded by memory bandwidth and capacity, not by arithmetic.
- A denominator defined as multiply-accumulates and read as FLOPs is wrong by exactly two — and that was caught by a reader, not by the expert.

</v-clicks>

<div v-click class="mt-8 text-lg">

None of this says anything about whether the answer is **correct**.

That is Chapter 5, and it has no equation.

</div>

<!--
- **Says:** Closes the chapter by restating the roofline bound, the batch-size hyperbola, the memory-bound long-context result, and the MACs/FLOPs erratum.
- **From:** Follows the organoid slide by summarising the whole chapter's cost material.
- **Chapter:** Delivers the chapter's closing summary and explicitly excludes any claim about correctness.
- **To:** Chapter 8 returns to the brain question now that cost has been made concrete, and closes Session 1.
-->


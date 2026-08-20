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

---

## Trading compute for memory

Invertible architectures recompute activations instead of storing them.

<Cite k="revnets" />

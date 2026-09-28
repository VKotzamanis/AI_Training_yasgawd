# Peer review — `slides/01-substrate.md`, `03-control.md`, `04-measurement.md`

Checked against `CLAUDE.md` (hard rules 1, 1a, 2, 4), `chapter-briefs.md`, `architecture.md`
and `references.md`. Every number recomputed independently (exact combinatorics + `scipy`).

## Summary

- **`01-substrate.md`** — brief-compliant and well sequenced; the Boltzmann identification is correct in sign and constant, but the slide's own symbol table contradicts it dimensionally, and one citation is used in the way `references.md` explicitly forbids.
- **`03-control.md`** — the strongest deck pedagogically, but it opens a thread belonging to Chapter 4 and spends Chapter 4's second payoff before Chapter 4 arrives.
- **`04-measurement.md`** — twelve of thirteen statistical claims are exact; the sample-size figure is wrong, the family-wise figure contradicts the deck's own preceding slide, and the likelihood ratio is attached to the wrong event.

## Numbers recomputed

**Correct as printed (04):** sign-test two-sided *p* for 5/5–0 = 0.0625; 6/6–0 = 0.031250;
10/10–0 = 0.001953; 10/9–1 = 0.021484; 10/8–2 = 0.109375; power at α=0.05 with n=5 = exactly
zero (smallest attainable *p* is 0.0625); expected informative cases = 2.500; clean sweep
0.4125 under +20pp and 0.2061 under the null; 95% interval on 2/5 = Clopper–Pearson
(0.0527, 0.8534). **Correct as printed (01):** the Boltzmann identification, exp(z_i/T) =
exp(−E_i/k_BT), sign and constant included.

**Not correct:** *n* for 80% power is **103**, not ~93 (1). The family-wise 0.143 is right
arithmetic on a premise the deck itself refutes (2). The likelihood ratio 2.0017 is right for
the wrong event (3).

---

## Key Issues — CONFIRMED

**1. The 80%-power sample size is wrong by ten cases.** `04-measurement.md`:
> "For 80% power you would need roughly **93 cases**."

For the design this chapter specifies — paired sign test, ties dropped, α=0.05 two-sided,
discordant rate 0.5, P(favour B | discordant)=0.7 — exact power at n=93 is **0.756**. 80%
first arrives at **n=103** (0.8018). Even conditioning on a fixed discordant count of n/2,
n=94 gives 0.780. The 93 is reproducible only from the normal approximation
[z_{α/2}√0.25 + z_β√0.21]²/0.04 = 46.6 discordant → 93.3, which discards the exact test's
discreteness and the randomness of the discordant count. Two slides earlier the chapter
insists its figures are "combinatorial, not an estimate". **Fix:** state 103, or state 93
and label it the normal approximation with the exact figure beside it.

**2. The family-wise rate contradicts the deck's own zero-power slide.** `04-measurement.md`:
> "Power at α = 0.05 is therefore **exactly zero** — combinatorial, not an estimate."

then, three slides later:
> "**Three arms means three comparisons.** Family-wise, that is about a 14% chance one looks interesting by accident, not 5%."

1−0.95³ = 0.1426 is correct arithmetic on a false premise. A sign test on five cases has no
size-0.05 rejection region — that is exactly what the earlier slide proves. The per-comparison
type-I rate is either **0** (nominal α=0.05) or **0.0625** (smallest attainable level), giving
a family-wise rate of **0** or **1−0.9375³ = 0.176**, not 0.143. It lands on the one chapter
whose authority rests on small-*n* statistics, and both halves are four slides apart.
**Fix:** "at the only attainable level, 0.0625 per arm, three arms give roughly 18%" — also
the stronger teaching point.

**3. The likelihood ratio prices the wrong event.** `04-measurement.md`:
> "**Likelihood ratio: 2.0.** The most convincing result this design can produce barely separates a real effect from nothing."

2.0 is correct for the event "no case favoured A", which is dominated by tie-heavy outcomes
(4 discordant → *p*=0.125; 3 → *p*=0.25). That is not the most convincing result available.
The best outcome is the 5–0 row in the adjacent table — five discordant, all favouring B —
probability 0.00525 under the effect and 0.00098 under the null, **LR = 5.38**. The slide
understates the best case by 2.7× while sitting beside a table that defines it. **Fix:** give
both — LR 5.4 for the outcome that reaches *p*=0.0625, and note it occurs 0.5% of the time
even when the effect is real. Sharper than the current argument.

**4. The persona slide drops a required caveat.** `04-measurement.md`:
> "162 roles, four model families, 2,410 factual questions. **Personas in system prompts did not improve performance** over no persona at all."

`references.md` (`zheng2024`, [V]) states: "**Caveat for the slide:** those model families,
that question set. Not Opus 5 on civil engineering." Absent. The slide is headed "Settling
Chapter 3's first debt", so the omission converts a bounded result into a general one — claiming
more than the source supports, against hard rule 1. Every other scope caveat in these decks is
present; this is the one gap. **Fix:** one line, in the source's own terms.

**5. Chapter 3 spends Chapter 4's second payoff.** `03-control.md`:
> "The original result: prompting with **eight worked chain-of-thought exemplars**, on a 540-billion-parameter model... It is **not** a result about typing *"think step by step"* at a model that already reasons before answering."

`04-measurement.md`, slide "Settling the second: think step by step":
> "The original result: **eight worked chain-of-thought exemplars**, on a 540-billion-parameter model... It is not a result about typing four words at a model that already reasons before it answers."

Same claim, same citation, near-identical wording. Chapter 4 adds no new evidence — the
re-evaluation is correctly withheld at [P] under `TODO(verify)`, which is the right call. Setup
and payoff therefore do not match: Chapter 3 promises "Not established. **Chapter 4**", and
Chapter 4 delivers the same scope argument plus a deferral. The persona debt (4) is genuinely
settled; this one is not. **Fix:** in Chapter 3, state only that the claim is contested; let
Chapter 4 make the scope argument once and land it on the B2 arm.

**6. Two chapters open the verification thread.** `03-control.md`: "**Thread opened —
verification.** Chapter 4 builds the missing middle item." `04-measurement.md` says the same.
`architecture.md`: "**Verification** | Ch 4 — evaluating prompts", and Chapter 3's brief starts
no thread. The decks already have the right marker — "**Forward reference — Chapter 4/5**", used
in `01-substrate.md` and elsewhere in `03-control.md`. **Fix:** demote Chapter 3's marker.

**7. `vaswani2017` is used for exactly what `references.md` forbids.** `01-substrate.md`:
> "Each token's representation is updated as a **weighted sum over the other tokens**, where the weights come from how well a query matches each key." `<Cite k="vaswani2017" />`

`references.md`: "**Bibliographic detail only** — the paper body was not read, so do not
attribute a specific formulation to it without reading the PDF." That sentence and the mermaid
diagram under it are a specific formulation, attributed. The [V] covers bibliography, not content
— the scope conflation hard rule 1a exists to prevent, arriving through the footer rather than a
tag change. **Fix:** read the PDF and record it, or mark the formulation as the deck's own.

**8. The temperature slide's symbol table contradicts its own identification.** `01-substrate.md`:
> "$z_i$ — logit for token $i$, dimensionless. $T$ — temperature, dimensionless."
> "This is the Boltzmann distribution, $p_i \propto \exp(-E_i / k_\mathrm{B}T)$, under the identification $z_i = -E_i / k_\mathrm{B}$."

The identification is **correct**: exp(z_i/T) = exp(−E_i/k_BT) exactly, the sign is right
(lowest energy ↔ largest logit ↔ argmax as T→0, as the next bullet states), and no constant is
missing. But E_i/k_B has units of kelvin, so the identification gives z_i kelvin and forces T to
be a thermodynamic temperature, while the table two lines above declares both dimensionless. Both
cannot hold. Under Conventions ("Equations carry dimensional analysis") this is the failure mode
the MACs-versus-FLOPs anchor exists to teach, three chapters earlier in the same deck set.
**Fix:** declare z_i and T in kelvin, or write z_i = −E_i/(k_B T_0) with T in units of a reference
T_0. The Boltzmann form also assumes non-degenerate states (no g_i); one clause.

**9. Mechanism claims ride a footer that does not support them.** `03-control.md`:
> "A negative example still puts the unwanted pattern into the context window." `<Cite k="anthropic-prompting" />`

`references.md` confirms only "tell Claude what to do instead of what not to do" on that page —
the rule, not the causal reason. Same pattern on the structured-input slide: "**This is also your
first defence against prompt injection**" under the same footer, where the source confirms only
that XML tags separate instructions from data. Both plausible, neither sourced; the footer makes
them read as documented. **Fix:** mark as the deck's own reasoning, or drop the causal clause.

## Key Issues — SUSPECTED

**10. The independence assumption behind 2.5 / 0.41 / 0.21 is unstated and flatters the design.**
Those figures reproduce exactly under independent Bernoulli draws for A and B per case
(P(discordant)=0.5). In a truly paired design both arms run on the *same* case and are normally
positively correlated, lowering the discordant rate below 0.5 and raising required *n* above 103.
"The most favourable assumption available" is true of the effect size, not of the correlation.
One clause fixes it, and it strengthens the argument.

**11. The calibration recipe commits the error the chapter warns about.** `04-measurement.md`:
"run each three times at baseline, discard anything scoring 3/3 or 0/3, keep the five nearest the
middle." Selection on a three-run statistic is selection on noise — a case with true pass rate 0.8
scores 3/3 with probability 0.51. Survivors regress towards their true rates on re-run, inflating
the measured A-versus-A′ disagreement, which is the noise floor the chapter uses as its screen.
Two slides later the deck names this class of error. Defend it (the bias is conservative) or raise
the calibration runs.

**12. Chapter 3's framing rests on a blocked chapter.** `03-control.md` leans on Chapter 2
throughout, including the whole "other side of the rubric" slide. `chapter-briefs.md` and
`DECISIONS.md` record Chapter 2 at 105–115 minutes against 75, with "Do not draft slides for this
chapter until it is settled". If the rating exercise is what gets cut, four Chapter 3 slides lose
their premise. A dependency to record, not a defect in Chapter 3.

**13. `B3 — baseline with extended thinking off`.** `references.md` confirms `effort` and the
`budget_tokens` deprecation, not an off switch. Verify at the pre-delivery re-fetch.

**14. Chapter 1 exclusions — judged compliant, flagged.** Positional encoding, multi-head attention
and layer norm all appear on the slide "What this chapter deliberately omits", each with a one-line
gloss. Naming an exclusion is not teaching it, so I judge this compliant. If a stricter reading is
preferred, deleting the three glosses costs nothing.

**15. Minor brief gap, Chapter 3.** The brief lists "specifying format and length". Format is one
sub-bullet on "Be specific"; length appears only in the Opus 5 concision note. Neither is taught.

## What is sound

Twelve of thirteen recomputable figures in `04-measurement.md` are exact, including the whole
sign-test table, the zero-power argument and the Clopper–Pearson interval. Hard rule 2 is clean:
no author names, years or identifiers in slide text, and every `<Cite k>` resolves to a [V] key.
`scripts/check-cites.mjs` enforces [V]-only, rejects [P], and self-tests. The `[P]` chain-of-thought
re-evaluation is withheld under `TODO(verify)` rather than quietly used — the best evidence-discipline
decision in these decks. `pope2026` is tagged `testimony`+`coi`, so the Chapter 1 footer renders
"Expert testimony, not a primary source" and "COI declared" automatically; hard rule 4 is met. The
`erratum2026` slide attributes the correction to the reader, not the lecturer.

## Questions to Probe

1. Where did **93** come from? If it is the normal approximation, say so — the preceding slide's
   rhetorical weight is that these numbers are exact.
2. Does "**clean sweep**" mean 5–0 with all five informative, or "no case favoured A"? The slide uses
   the second and labels it with the first's significance.
3. What settles the think-step-by-step debt if the `[P]` re-evaluation never verifies and the B2 arm
   returns a null on five cases — which the deck says is the most likely outcome?
4. Was the `vaswani2017` PDF read? If yes, update `references.md`; if no, the attention slide needs a
   different footer.
5. Is the A/B correlation on a shared case assumed zero deliberately, or by oversight?

## Bottom Line

**Not deliverable yet.** Chapters 1 and 3 need small, well-defined edits and are close. Chapter 4 is
the problem: it is the chapter whose entire claim on the room is statistical rigour, and three of its
numbers are wrong, misapplied or mislabelled. Fix in this order: (2) the internal contradiction —
14% → 17.6% at the attainable level, or zero; (1) 93 → 103, or label the approximation; (3) attach the
likelihood ratio to the 5–0 outcome or rename the event; (4) restore the `zheng2024` scope caveat;
(5)–(6) move the chain-of-thought scope argument out of Chapter 3 and demote its thread marker; (7)–(8)
the `vaswani2017` footer and the temperature slide's dimensions.

All three decks still carry `TODO(capture)` blocks for the tokeniser screenshots, the temperature demo,
the five instructor cases and the instructor's eval. Honestly marked, correctly scoped, and none
closable from the desk.

## What this review did not do

- Did not open the Wei, Zheng or vendor prompting sources. Citations were checked against
  `references.md` only, so an error already inside `references.md` passes through unchanged.
- Did not run `check:cites` or a Slidev build; the script was read, not executed. Rendering, KaTeX,
  mermaid scaling and PDF export are unverified.
- Did not inspect `01-temperature.png` or `01-kv-growth.png`. Both exist; whether the plotted softmax
  matches the caption's exactness claim, and whether the KV curve is normalised as stated, was not
  checked against generating code.
- Did not review `assets/eval-worksheet/README.md` or `assets/rating-exercise/README.md`, assess
  timing against session budgets, or review chapters 2, 5, 7 or 9–19.

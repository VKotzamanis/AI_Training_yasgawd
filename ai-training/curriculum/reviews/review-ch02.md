# Peer review — `slides/02-formation.md` (Chapter 2, Formation)

Checked against hard rules 1/1a/5/6, the Ch 2 brief, `ch02-annotation-findings.md` v3.1,
`references.md`, `DECISIONS.md`, the rating-exercise README, and the Ch 3 and Ch 4 decks.

## Summary

Four checks pass and should be recorded as passing. **Rule 1a:** no `<Cite>` appears below
the split point, no `[E1]`–`[E4]` tag is converted to a `[V]`, nothing in Part 2b implies a
citable source. **Rule 5:** Part 2b, line by line, contains no prompt, rubric row,
banned-phrase entry, persona or project name — every finding is stated as structure.
**The nine:** the deck teaches §13 items 1–9 in §13's order and holds back exactly items
10–14. **Keys:** all ten resolve in `slides/sources.json` and are tagged `[V]`.

Defects cluster in three places: one killed claim restored and several evidence bands
blurred; citations absent rather than wrong; and required content missing, including two
items Chapter 3 already depends on.

## Key Issues

### 1. The verbosity folk story, which §4 killed, is back on a slide — CONFIRMED

Behaviour-to-mechanism table, under the column heading **"Where it comes from"**:

> `| Long, structured, confident answers | Those were preferred under time pressure |`

§4: *"the folk story — raters like long answers, so models got long — is contradicted by the
instructions in two separate instruments, and the actual mechanism is not visible in these
documents."* One instrument tie-broke deliberately toward brevity; the other deleted length
as a grading category mid-project.

**Why it matters.** This is the failure hard rule 6 exists to catch, on the slide whose
whole claim is that behaviour traces to mechanism. **Fix:** state the evidenced version —
two instruments pushed against length or stopped measuring it, models are verbose anyway.

### 2. Two further rows assert mechanisms nothing supports — CONFIRMED

> `| Agrees with you when you push back | Agreement was preferred by raters, at scale |`
> `| Confident on your literature, right on textbooks | Where data was dense, plausible and true coincide |`

The slide carries no footer at all, against the house-style rule that every slide does. The
second row invents a data-density mechanism that competes with the §11 confabulation-band
finding taught later in the same chapter — the evidenced explanation of the same
observation. **Fix:** delete the density row; source the sycophancy row or mark the slide as
instructor synthesis.

### 3. `[E2]` sub-claims are folded into the `[E1]` band — CONFIRMED

Under **"Corroborated across documents"**:

> **House style is a written edit specification, and the corrected response is collected.**

§13 item 1 attaches an instruction the slide drops: *"Note the split at §5.1: collection
rests on two documents, not three."* §0.6 exists solely because v3 welded these two claims
together, and tags collection `[E2]`. Next bullet, same slide:

> **Equivalence is engineered out.** … Preference data is conditioned on one being worse.

Conditioning-on-failure rests on D alone. The brief keeps the attribution — *"one instrument
collects comparisons only where a model has already failed"* — and the deck drops it.

**Why it matters.** These are the two headline findings, and the deck promotes
single-document claims into the corroborated band on the slides built to keep bands apart.
**Fix:** split each bullet, naming the extension as one instrument's.

### 4. The slide promising to show the tags does not show them — CONFIRMED

> **Findings are tagged by how many documents support them, and that tag is shown.**

No `[E1]`/`[E2]` marker appears in Part 2b; only slide headings carry the band, and "Five
more, held back" mixes §13's `[E2]` and `[E3]` items undifferentiated. Same slide, an
internal contradiction: the bullet says two documents are of unknown provenance, the box
below says five. **Fix:** show the band per bullet or delete the sentence.

### 5. The emotional-prompting slide drops the replicators' stated limits — CONFIRMED

`references.md` marks them mandatory: *"Replicators' own stated limits, which must appear
alongside: they did not use the identical tasks or models, wording varied slightly, they
sampled one stimulus per task by seed rather than reproducing the best-of-eleven protocol,
and they dropped one stimulus…"* None appear.

The seed-sampling limit is load-bearing for the slide's own argument: the punchline is
*"Best-of-eleven, reported as the result"*, and the replication producing the 1% deliberately
did not run best-of-eleven. Two further defects here. The original is never cited —
`li2023emotion` is `[V]`, keyed, and its `venue` field reads *"technical report, not peer
reviewed"*, which the footer prints automatically; without it the deck says only *"A widely
cited result"*. And *"4.42%"* is stated without its benchmark; `references.md` gives 4.42%
on BIG-Bench and 2.58% across all benchmarks.

### 6. The exercise result is announced in advance, and asserted as fact — CONFIRMED

Slide **"What the exercise is for"**, future tense, immediately after the instructions:

> - Most rooms prefer the fluent, well-formatted response containing an error.
> - The tally **will be** small…
> Under mild time pressure, competent engineers reward verbosity, confidence and formatting
> over correctness — and are most confident where they are most wrong.

That sentence is taken from step **4** of the exercise README, *"Name what happened"*, where
it is past tense and delivered after the reveal. In deck order it primes the room before
they rate, voiding the demonstration the chapter is built on. The confidence–correctness
claim is worse: the README offers it as something the facilitator *may* be able to show from
the tally; the deck states it as fact about engineers, on an n=6 tally the deck itself calls
"not a distribution". **Fix:** move it behind the exercise in past tense, and add the
missing run-order slides — tally (step 2), reveal (step 3), reviewer round (step 5). The
deck has no debrief structure at all.

### 7. The 2a/2b cut is not clean — CONFIRMED

The Constitutional-AI slide, above the cut, defers its own payoff across the split:

> **This is the hinge of the chapter.** Once a written criterion can be applied by a machine,
> the question becomes: what does a criterion have to look like for a machine to apply it?
> Part 2b is what that does to the criteria.

Split into two sessions, 2a ends by posing its central question and not answering it. In
reverse, the table row *"Sounds the same across topics | House style specified in writing and
enforced"* is §5 — an annotation finding used above the cut, unsourced and untagged, before
the *"What this rests on, stated first"* slide that frames all such findings. **Fix:** move
the hinge slide below the cut or give 2a its own closing answer; move the house-style row
below the cut regardless.

### 8. OPRO: the caveat names the wrong model role, and the evidenced claim is uncited — CONFIRMED

> - Run the same search with a different **optimiser** model and you get a **different** winning instruction.

`references.md` states the caveat as *"PaLM 2-L scorer"* and *"other models yield different
optimal instructions"*; the supporting result concerns *"the underlying task model"*. OPRO
separates the optimiser LLM that proposes instructions from the scorer that evaluates them,
so this inverts the lesson — a prompt is specific to the model it is used **on**. The
correction box then makes a positive claim, *"optimised prompts do not transfer consistently
across models"*, with no footer. That is `ye2024`, `[V]` and keyed, and absent from the deck.

### 9. Three slides cite one source for claims drawn from several — CONFIRMED

- **"What scale bought"** cites `hoffmann2022` only; *"Performance improves predictably with model size, data and compute"* is Kaplan. `kaplan2020` is `[V]` and keyed.
- **"Not every parameter runs"** cites `clark2022` only; *"Published designs scale to very large total parameter counts while keeping the active count per token modest"* is Switch Transformer and GShard. `fedus2021`, `lepikhin2020` are `[V]` and keyed.

Structural cause: `Cite.vue` takes one required `k` and positions the footer absolutely, so
two would overlap. **Fix:** split the slides, or extend the component.

### 10. The RLHF slide credits one stage with a two-stage result — CONFIRMED

> A hundred-fold size difference, reversed by the layer on top. **That is the measure of how much this stage does.**

`references.md` records the finding as *"SFT on labeller demonstrations **plus** RLHF on
GPT-3"*. On a slide titled *Reinforcement learning from human feedback*, "this stage" reads
as the RL step alone. **Fix:** attribute it to the post-training pipeline.

### 11. Required content is missing — CONFIRMED

- **"RLAIF" and "Constitutional AI" never appear** in the file. The brief requires both named; the CAI slide names it only inside the footer's title.
- **The six rubric dimensions are never named as a set.** Brief: *"Rubric dimensions are named here and never abandoned: truthfulness, instruction following, harmlessness, formatting, verbosity, tone."* "Tone" appears nowhere. Chapter 3 then says *"the dimension your Chapter 2 rubric scored hardest"* — a handoff this deck never makes; Chapters 5 and 18 inherit the same set.
- **Rater disagreement and adjudication are absent**, though the brief lists *"what rater disagreement does downstream"* and specifies *"the reviewer layer, an adjudication example, and one case where two competent raters legitimately diverge"*.
- **The rewrite step is absent from the exercise slides**, yet Chapter 3 says *"In Chapter 2 you were handed a rewrite checklist and told to apply it without explanation"*, and *"In Chapter 2 an impossible rubric produced noisy ratings"*. Neither happens here.
- **Test-case hardcoding as a reinforced reward hack** is required by the brief and absent. Defensible while the system card sits at `[P]` — but it needs a `TODO(verify)`, not silence.

### 12. Chapter 2 spends Chapter 4's post-hoc-selection payoff — SUSPECTED

`references.md` files the emotional-prompting replication as *"the Chapter 4
post-hoc-selection lesson with a published example attached"*. Chapter 2 delivers it in full;
Chapter 4 delivers it again via `zheng2024` (*"post-hoc selection of the winning
condition"*). Meanwhile the brief's actual requirement for this slot —
*"role-conditioning shifts the output distribution… Do not claim the model feels anything"* —
appears nowhere: no slide contains "role-conditioning", "psychometric" or "affect".
SUSPECTED on the duplication only; not on the swap.

## Questions to Probe

1. Is "What the exercise is for" shown before or after the room rates? If before, the exercise is dead on arrival; if after, why the future tense and the missing tally/reveal/reviewer slides?
2. The deck says the fifteen-minute time box *"appears in the exercise rather than here"*, but the exercise slide states two minutes and never names fifteen. Which number does the room leave with?
3. `DECISIONS.md` budgets the nine findings at 28 minutes and the deck gives them four slides. Is that the whole segment?
4. Was the emotional-prompting honesty statement dropped by decision or oversight? It is the only brief item removed without a trace.
5. Should the behaviour table be marked instructor synthesis, so the missing footer reads as deliberate?

## Bottom Line

The evidential architecture of Part 2b holds — the ranking, the nine, the five held back, the
no-citation rule and the anti-reproduction rule are all correct, which is the hardest part of
this chapter and the part most likely to fail. The defects sit elsewhere: a killed claim
restored in the behaviour table, single-document claims promoted into the corroborated band,
a replication presented without the caveats `references.md` marks mandatory, and an exercise
whose outcome is printed on a slide before the room performs it. Fix items 1, 5 and 6 before
this deck is shown; 7 and 11 before the split is decided, since Chapter 3 already leans on
two handoffs Chapter 2 does not make.

---

**Not done.** I checked only Chapters 3 and 4 for duplication, not 1 or 5–19. No citation
was verified against its primary source — every check treats `references.md` as the authority,
so an error inside that file would pass unnoticed. I did not build or render the deck: slide
overflow, click counts and the footer overlap in item 9 come from reading `Cite.vue`, not from
a render. The rating-exercise README was read only as the specification, not reviewed.

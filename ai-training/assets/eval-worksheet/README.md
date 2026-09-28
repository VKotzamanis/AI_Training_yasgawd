# Eval worksheet — Chapter 4

The chapter's method artefact. The instructor runs the eval in advance; the room sees the results and takes the blank worksheet home as a template.

**Status:** specified here. The five cases and their pass criteria are not written — those are the instructor's, and §3 says why they cannot be drafted for them.

---

## 1. Non-negotiable: the domain

**Every case sits in mechanics, concrete or fluids.**

Five to six attendees. That is the stated intersection of what all of them know. Not wave energy, not PTO, not design codes — those are known by some of the room, and *some* is the failure condition here, not a shrug.

The reason is the same one that governs the Chapter 2 rating exercise, and it is the reason that chapter's own file gives: an audience cannot judge truthfulness on a domain it does not know, so it grades fluency, structure and confidence instead, because that is all it can see. When the results slide goes up, the room has to be able to check the grading. If they cannot, the demo reduces to *trust me* — which is the one thing a chapter about method cannot afford.

The instructor's own domain does not disappear. It is the worked instance: *here is mine, filled in; now fill in yours.* That is what the take-home template is for.

**Aim each case at the confabulation band** (`../../curriculum/ch02-annotation-findings.md` §11): not common knowledge, where the model is reliable, and not genuinely obscure material, where it correctly declines. The band between, where it believes it knows.

---

## 2. What is under test

Two claims. Both are widely believed, both have published evidence against them, and both are things this room does.

**Claim 1 — an expert persona improves accuracy.** *"You are an expert structural engineer…"*

Evidence against: Zheng, Pei, Logeswaran, Lee & Jurgens, 2024, Findings of the ACL: EMNLP 2024, pp. 15126–15154, DOI 10.18653/v1/2024.findings-emnlp.888 — **[V]**. 162 roles, four model families, 2,410 factual questions: personas in system prompts do not improve performance over no persona.

The second finding is the one that belongs in this chapter. Picking the best persona *per question* does improve accuracy — but identifying it in advance is no better than chance. That is post-hoc selection of the winning condition — a mechanism by which a prompting claim can be manufactured out of noise. The paper establishes it for persona selection on its own question set; the wider inference about prompting folklore is mine, not theirs. It is also exactly what a five-case eval will do to you if you let it.

**Claim 2 — telling it to work step by step improves accuracy.**

Evidence against: Meincke, Mollick, Mollick & Shapiro, 8 June 2025, *The Decreasing Value of Chain of Thought in Prompting*, Wharton Generative AI Labs technical report — **[P]**, not [V]. The publisher's page was read; the SSRN report itself was not. **Check the numbers against the report before any of them reach a slide.** On GPQA Diamond: reasoning models gained little (o3-mini +2.9%, o4-mini +3.1%, Gemini Flash 2.5 −3.3%) at 20–80% more time, while non-reasoning models gained more, and unevenly (Gemini Flash 2.0 +13.5%, Sonnet 3.5 +11.7%, GPT-4o-mini +4.4% and not statistically significant).

**Caveat that goes on the same slide, for both claims.** Those results are on those models, on those benchmarks. This eval is Opus 5 on civil engineering tasks. Neither paper predicts what happens here — which is the entire reason for running it, and is the same discipline `../../references.md` already applies to the OPRO caveats.

**Rejected as test claims:** *take a deep breath* (tests a different proposition than OPRO's — PaLM 2-L, GSM8K/BBH, phrase found by automated search; it belongs in the chapter as the cautionary tale about transfer, not as a case); *emotional stakes* (`[U]`, and the same transfer problem); *few-shot versus zero-shot* (likely to win, and too task-dependent to survive five cases); *XML tags* (provider-specific, so a result teaches about one vendor rather than about method).

---

## 3. The five cases

**Not written here.** Five shapes are proposed below with the reason each was chosen. The physics is the instructor's — a case invented by someone who does not know the material will be either trivially right or arguably wrong, and both destroy the exercise.

Each case needs: the prompt as it would actually be typed, and one binary pass criterion.

| # | Shape | Why this shape | To supply |
|---|---|---|---|
| 1 | **Validity range** — a formula or correlation applied outside where it holds | Models state formulas confidently and omit their range of applicability. Fluids is dense with these. | `TODO(instructor)` |
| 2 | **Dimensional trap** — an expression carrying a unit error, given to the model to check | The chapter's own anchor artefact *is* a unit-definition error. A case that is itself a unit trap makes the chapter self-consistent. | `TODO(instructor)` |
| 3 | **Sign or direction convention** — a quantity whose answer flips on an unstated convention | House rule already requires sign conventions annotated. Tests whether the model states its convention before computing. | `TODO(instructor)` |
| 4 | **Coefficient in the confabulation band** — a material or flow property the model will produce a plausible number for | The §11 band, directly. Concrete is a good source. | `TODO(instructor)` |
| 5 | **MATLAB numerics** — a short script with a subtle numerical error | MATLAB is common across the group; the error is checkable by everyone. | `TODO(instructor)` |

### The calibration pass — do this before fixing the five

A case that the model always gets right, or always gets wrong, has **zero power to detect a prompt effect**, at any sample size. Five such cases produce a clean 5–0 or 0–5 that means nothing.

Write ten candidates. Run each three times at baseline. Discard anything that scores 3/3 or 0/3. Keep the five nearest the middle. Roughly thirty runs, well under an hour, and it is the difference between an eval that can detect something and one that cannot.

This is item selection by difficulty, and it is defensible on the same grounds psychometrics uses it. It is also the honest answer to *why these five cases* when someone asks.

**It is not free, and the cost runs the wrong way.** Three runs is a four-outcome instrument, so "1 or 2 of 3" is compatible with a true pass rate anywhere from roughly 0.1 to 0.9. Selection is symmetric, so there is no bias in the mean — but the spread survives, and a retained item flips between two fresh runs about 40% of the time rather than the 50% a genuinely balanced item would. That biases the measured A-vs-A′ noise floor **downward** by something like ten percentage points, which makes the §8 decision rule more permissive than it should be, and it simultaneously lowers sensitivity to a real effect, because a near-extreme item that landed mid-range by luck moves less under treatment than a genuinely balanced one would. Both errors push the same way. Ten candidates at three runs cannot fix this; more runs per candidate would, at proportional cost.

---

## 4. Pass criteria — the rules

Binary. Checkable without seeing the other condition. **Fixed before any output is looked at**, and not edited afterwards.

Usable: *"Passes if it names the Reynolds-number range over which the correlation holds."*
Not usable: *"Passes if it handles the correlation well."*

Four rules, adapted from how industrial pipelines write machine-gradeable criteria (`../../curriculum/ch02-annotation-findings.md` §6.1–§6.2, tagged **[E1]/[E2]** — observations from vendor documents, not a citable method, and they must never be presented as one):

1. **Atomic.** No conjunction joining two checkable things.
2. **Self-contained.** Values, names and thresholds written into the criterion, not referenced elsewhere. The grader should not need the prompt to apply it.
3. **Outcome, not process.** Test what the answer says, never how it got there.
4. **Not restrictive.** A range rather than an exact number; the presence of a required element rather than exact wording.

Where correctness is a number, the criterion carries the value, the tolerance, and the sign convention it is computed under. SI throughout.

---

## 5. Conditions

Five conditions per case. Twenty-five outputs for five cases.

| ID | Condition |
|---|---|
| **A** | Baseline prompt. Extended thinking on, xhigh. |
| **A′** | Baseline prompt, run again. The null strip. |
| **B1** | Baseline + expert persona. |
| **B2** | Baseline + explicit instruction to work step by step. |
| **B3** | Baseline with extended thinking **off**. |

**The replicate asymmetry, stated rather than hidden.** A′ gives the baseline a measured noise floor. B1, B2 and B3 get none, and A′'s justification is condition-agnostic — it is an argument about single-sample stochastic output, not about baselines. So if B2 beats A on four of five cases, the check §8 demands cannot actually be run for B2; its noise floor is borrowed from A, and a step-by-step instruction could plausibly narrow the spread or widen it. Twenty-five runs cannot fix this: replicating every arm costs cases, and §8 argues cases are already below the floor. **The choice made here is to keep five cases and accept an unmeasured noise floor on the B arms.** Say so on the slide. It is the honest version, and it is a better teaching point than a design that hides the trade.

**Why A′ exists.** Output is stochastic. One run per condition confounds the prompt effect with run-to-run spread. A′ measures the noise floor on the same five cases, and it is read *before* any A-versus-B result. If A and A′ disagree on two of five cases, then any A-versus-B difference of two or fewer is uninterpretable. This is a repeatability check on an instrument, and the room already has the concept.

**Why B3 exists — and the confound it fixes.** The instructor's default is thinking on at xhigh. That is already a reasoning configuration, so a null result on B2 has two readings: *step-by-step adds nothing to a reasoning model*, or *xhigh already saturates it*. Those are different claims and B2 alone cannot separate them. B3 costs five runs and makes B2 interpretable. It also answers a question the room will actually ask, which is whether turning thinking on is worth the wait — and that hands off to the cost material in Chapters 7 and 13.

Fresh session per case. Prior turns contaminate.

---

## 6. Blinding

The procedure, in order. Step 3 is the one that gets skipped and is the one that matters.

1. Freeze the five cases and their pass criteria in a file. Do not edit it after this point.
2. Generate all twenty-five outputs. **Save the final answer text only.** Discard the thinking transcript at capture time — it is present under A, A′, B1 and B2 and absent under B3, which identifies that arm with certainty.
3. **Strip the condition labels.** Rename every output to an opaque ID. Write the ID-to-condition map to a separate key file and do not open it. The header block recording the thinking setting is written **once, globally**, never stapled per output — a per-output header is a labelled condition wearing a different name.
4. Insert three **duplicate outputs** at random positions, drawn from outputs already in the set. They measure grader drift, which A′ does not: A′ measures the model's spread, not the grader's.
5. Shuffle. Grade every output against its case's criterion. Pass or fail, plus one flag — see below. Record grading order on the sheet.
6. Unblind. Join grades to conditions. Check the duplicates agree with themselves before reading anything else.
7. Count.

**One permitted annotation, and only one.** If a criterion turns out to be ambiguous against a particular output, mark that output `AMBIGUOUS` alongside the pass/fail and move on. Do not edit the criterion, and do not explain. Without this, an ad hoc reinterpretation made at output 14 is indistinguishable on the tally sheet from a confident grading, and nobody — including the person who did it — can tell afterwards which grades rest on the criterion as frozen.

### What this blind does not achieve

**It is not a blind against the person who designed the conditions.** Stripping labels removes identity-by-file. It does not remove identity-by-inference, and the instructor knows what each arm was built to produce. Two arms are self-identifying on sight whatever the file is called:

- **B2** is a format instruction as much as a content one. An answer produced under *work step by step* tends to arrive in numbered steps. The manipulation and its marker are nearly the same thing.
- **B1** fixes an expert persona while four of the five cases sit outside that persona's field. A retained or awkward framing is itself a tell.

Closing this properly needs a second grader who does not know which manipulations exist. There isn't one. **So it gets disclosed, not solved:** the results slide states that the grading was single-blind at best, and names B2 as the arm most likely to be compromised. A limitation stated on the slide costs nothing; the same limitation found by someone in the room costs the chapter.

The tally sheet is keyed on output ID, not on condition. That is what makes step 4 possible; a sheet with a condition column cannot be graded blind.

---

## 7. Materials to produce

| Item | Notes |
|---|---|
| Case sheet | Five prompts, frozen. One page. |
| Criterion sheet | Five binary criteria, frozen before any output exists. Units and sign conventions stated. |
| Header block | Model ID, surface, thinking setting and effort, date, fresh-session policy. Filled before the run, not after. |
| Output set | 25 files plus 3 duplicates, opaque IDs, final answer text only — no thinking transcript. |
| Key file | ID → condition. Not opened until grading is finished. |
| Tally sheet | Output ID, case, grading order, pass/fail, `AMBIGUOUS` flag. Condition column added only after unblinding. |
| Results slide | Two comparisons and the noise floor, with the counts shown, not summarised. |
| Blank template | The whole set, empty, for attendees to run on their own work. |

**Header block, as configured:** `claude-opus-5`, Claude Code, extended thinking on at xhigh, fresh session per case, date of run. The model ID and date are not decoration — Chapter 5's drift segment is what makes them load-bearing.

---

## 8. Facilitator notes: what five cases support

**They do not support a significance claim.** Paired sign test, ties dropped:

| Cases | Best possible split | Two-sided p |
|---|---|---|
| 5 | 5–0 | 0.0625 |
| 6 | 6–0 | 0.0313 |
| 10 | 10–0 | 0.0020 |
| 10 | 9–1 | 0.0215 |
| 10 | 8–2 | 0.1094 |

Five cases cannot reach two-sided *p* < 0.05 under any outcome. Six is the minimum. Even at ten, 8–2 fails. **Say this out loud before showing any result.** The room is made of experimentalists; stating it first is what buys credibility for everything after.

**Power at α = 0.05 is exactly zero, not approximately small.** That is combinatorial, not an estimate: 0.0625 is the floor of the achievable *p*-value space at n=5, so no effect of any size can clear 0.05 here.

**And the best possible outcome is weak evidence even read informally.** Take a true effect of +20 percentage points against a 50% baseline — the most favourable case, since the confabulation band targets 50% and that maximises discordant pairs. Then only about 2.5 of the five cases are expected to be informative at all; the rest tie. A clean directional sweep occurs with probability 0.41 under that true effect and 0.21 under no effect at all, a likelihood ratio of **2.0**. The most convincing result this design can produce barely distinguishes a real 20-point effect from nothing.

For 80% power at α = 0.05 under the same model you would need roughly 47 discordant pairs — about **93 cases**, given the ~50% tie rate. That number is a floor, not a target: it assumes the best-case baseline and independent outcomes, and real same-case outputs share difficulty, which makes it worse.

**What they do support.** A screen. Five cases tell you whether an effect is large enough to be worth a larger eval, and they tell you what your noise floor is. That is a real result and it is what most prompting advice has never had.

**Read the noise floor first, and read it as a heuristic, not an instrument.** If A and A′ disagree on *k* of five cases, treat any A-versus-B difference of *k* or fewer as inside the measurement error. Present it before the comparison, not after — reversing the order invites the room to form a belief and then defend it.

Two limits on that rule, both of which belong on the slide rather than in a footnote:

- **The estimate is barely constrained.** A single A′ run at n=5 pins the flip rate very loosely. Observing 2 of 5 disagreements gives an exact 95% interval of **(0.05, 0.85)** — from almost never to most of the time. Every other value of *k* spans 60–80 percentage points too. The rule is a deliberately conservative screen; the word "uninterpretable" claims more precision than five cases can carry.
- **It assumes the noise is the same in every arm.** A′ measures the baseline's spread. Nothing establishes that B1, B2 or B3 share it — a step-by-step instruction could narrow the spread by canalising the answer, or widen it. That assumption is unstated in most small evals and it is unstated here unless the slide says it.

**Declare every arm regardless of which looks better.** The design runs **three** comparisons against a shared baseline — A vs B1, A vs B2, A vs B3 — even though the narrative frames it as two claims. Three independent comparisons at α = 0.05 give a family-wise accidental-discovery rate of **0.143**, not the 0.098 that two would give. Roughly triples, not roughly doubles.

The three are not independent either: all of them reuse the same five A outputs, so one unlucky baseline run moves all three comparisons together. That correlation can push the true family-wise rate either way and cannot be bounded without data that does not exist yet. Say that, rather than quoting 0.143 as if it were exact.

Reporting only the interesting arm is exactly the post-hoc selection Zheng et al. describe, and doing it in a chapter about method would be self-refuting.

**State the scope.** The result is about these five cases, on this model version, on this date. It is not about the model, and it is not about prompting.

**If the folklore wins.** Not a failure — it is the more interesting outcome, because it now sits against a published null result. The honest reading is that five cases cannot distinguish a real effect from a lucky one, which is the lesson. Take the same five cases to twenty and see whether it survives.

---

## 9. Verification requirement

The instructor verifies the physics of all five cases before the run, and someone who is not attending checks the pass criteria for ambiguity. A criterion two competent people read differently is not binary, and it will fail during grading — after the outputs exist, which is the worst possible moment to change it.

Grade the calibration runs before writing the final criteria. A criterion that cannot be applied to a real output is a criterion that has not been tested.

**The calibration pass runs condition A only, so it cannot catch condition-shaped ambiguity.** A criterion that reads cleanly against baseline prose can become hard to apply against a step-decomposed B2 answer — the required element is present but split across two numbered steps. Before freezing, generate one B1 and one B2 output for a single case and check each criterion against those too. Two extra runs.

---

## 10. Sourcing

Written from scratch. The criterion-authoring rules in §4 are structural observations from vendor documents, tagged `[E1]`/`[E2]` on that file's own scale. They are the instructor's observation of how industrial pipelines write gradeable criteria. They are not citable, they never earn a `[V]`, and no worked example, rubric row or criterion text from any such document appears here or on a slide.

The two published sources in §2 carry their own tags: `[V]` for Zheng et al., `[P]` for the Wharton report until the SSRN text is read.

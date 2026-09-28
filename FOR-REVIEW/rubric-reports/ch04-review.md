# Review: `slides/04-measurement.md` — 2026-08-28 — reviewer: claude-opus-5[1m]

Reviewed file is the Slidev draft. No Beamer rebuild exists for this chapter
(`slides/beamer/` holds 01–03 only), so this file is the live draft, not a superseded one —
unlike the ch02 and ch03 reviews in this directory.

Slides counted from 1 at the title slide; 18 content slides. Line numbers are from the `.md`.

**Chapter argument, stated so its author would accept it:** prompting advice circulates as
folklore because it is produced by a single run judged against a criterion chosen after the
output was seen, with no control condition; the fix is a five-case eval with a frozen binary
criterion, a repeated baseline arm, and blinded grading; that eval is far too small to prove
anything, and saying so before showing any result is what makes the rest credible; applied to
the two claims Chapter 3 left open, it settles the persona claim against published evidence
and hands the chain-of-thought claim to the room's own measurement.

## Topic ledger

| topic | opens (slide) | closes (slide) | reopened at |
|---|---|---|---|
| Why prompting advice circulates as folklore | 2 | 2 | — |
| The MACs-versus-FLOPs erratum | 3 | 4 | — |
| Criterion fixed before the output is seen | 4 | 5 | 9 (grading order), 14 (header block) |
| The minimal eval (five cases → a count) | 5 | 5 | 12, 18 |
| Case calibration / item selection by difficulty | 6 | 6 | — |
| The five conditions A, A′, B1, B2, B3 | 7 | 7 | 9, 14 |
| A′ and the noise floor | 8 | 8 | 12, 13, 14 |
| Blinding and its disclosed limit | 9 | 9 | — |
| Statistical limits of five cases (sign test) | 10 | 11 | 13 |
| Multiplicity across three arms | 13 | 13 | — |
| The instructor's own eval | 14 | 14 | — |
| Persona and accuracy | 15 | 15 | — |
| Chain-of-thought scope | 16 | 16 | — |
| Version, settings and expiry | 17 | 17 | — |
| **Extended thinking as a controlled variable** | **7** | **never closed** | 9, 14, 17 |

The last row is the evidence for [ch04-001] and [ch04-010]: the chapter opens extended
thinking as a manipulated variable on slide 7 and never gives it a definitional home, a
setting range, or a surface on which the room can reach it.

The three multi-interval rows (criterion, conditions, noise floor) were each checked for R:
every reopening carries new content — the noise floor is defined at 8, listed as a use at 12,
bounded for precision at 13, and placed in the run order at 14 — so none fires an R finding.

## Slide messages

1. Chapter 4 supplies the method for settling the two claims Chapter 3 left open.
2. Folklore prompting is one run, judged by a criterion chosen after seeing the output, with no control — three defects this room already catches in a colleague's experiment.
3. A unit-definition error in expert material produced a clean factor of two and was caught after publication by an outside reader.
4. The erratum's lesson is that a claim is checkable only when its terms are written down, which is why the pass criterion must precede the output.
5. The minimal eval is five frozen cases, a binary pass criterion fixed in advance, and a count across two conditions.
6. Cases must be calibrated to sit where the model is right some of the time, because a case that never varies can detect nothing at any sample size.
7. The design runs five conditions, two of which exist to control confounds rather than to test a prompt.
8. A′ repeats the baseline to measure run-to-run spread, so an A-versus-B difference can be judged against noise.
9. Blinding strips labels and inserts duplicates but cannot blind the designer, so that limit is disclosed rather than solved.
10. A paired sign test on five cases cannot reach two-sided *p* < 0.05 under any outcome, so its power at α = 0.05 is exactly zero.
11. Even under the most favourable effect assumed, the design's best obtainable result is weak evidence and almost never obtained.
12. Five cases buy a screen, a noise floor and a habit, not a finding.
13. The noise floor is imprecise and three arms multiply the error rate, so every arm must be declared.
14. *(TODO(capture))* The instructor's own eval goes here, noise floor first and every arm declared.
15. A published test of 162 roles across four model families found personas did not improve accuracy, within a scope the slide states.
16. The published chain-of-thought result is about supplied worked exemplars, not about instructing a model that already reasons.
17. A result without its model ID, date and settings is not a result, because a working prompt is a measurement and measurements expire.
18. The chapter delivers a one-page method, an honest statement of its limits, and two folk claims tested rather than repeated.

All eighteen slides carry a statable Message. No F finding for an unstatable Message.

## Findings

### [ch04-001] T blocker — slide 7
Quote: "| **B3** | baseline with extended thinking off |" (line 173), justified at "B3 exists
because the default configuration already reasons — without it, a null result on B2 has two
readings and you cannot tell which." (line 178)
Why it fails: on Claude Opus 5 — the model the eval is configured for
(`assets/eval-worksheet/README.md` line 149: "`claude-opus-5`, Claude Code, extended thinking
on at xhigh") — thinking cannot be disabled at `xhigh` effort. The vendor page states:
"On Claude Opus 5, thinking cannot be disabled at `xhigh` or `max` effort: requests that set
`thinking: {"type": "disabled"}` at those levels return a 400 error." Running B3 therefore
forces effort down to `high` or below at the same time, and effort "affects **all tokens** in
the response, including text responses and explanations, tool calls and function arguments,
thinking". B3 thus varies two factors at once — the arm whose sole purpose is to remove a
confound from B2 is itself confounded, and the null it is meant to disambiguate becomes
un-disambiguable. `references.md` line 170 does not carry this: it records only that thinking
is "a model decision, not a user setting", so the fix cannot be made from the project's own
record.
Fix direction: run the whole eval at `high` effort or below so `thinking: {"type": "disabled"}`
is the single manipulated factor, and say so in the header block; or redefine B3 as an
effort step-down and state on the slide that it does not isolate thinking. Basis:
platform.claude.com `/build-with-claude/effort` and `/build-with-claude/extended-thinking`,
both fetched 2026-08-28 during this review and logged in `REFERENCES.md`. **CONFIRMED.**

### [ch04-002] T blocker — slide 13
Quote: "At the only level actually attainable, 0.0625 per arm, three arms give a family-wise
rate of about **18%**." (line 334)
Why it fails: 0.0625 is the sign test's *conditional* size given five discordant pairs, and
1−0.9375³ = 0.1760 combines three conditional levels. The design's actual family-wise type-I
rate is unconditional. Rejection at n = 5 requires all five pairs discordant *and* a 5–0 split:
0.5⁵ × 2(0.5)⁵ = 1/512 = 0.001953 per arm, giving 1−(1−0.001953)³ = 0.0058. I confirmed this by
Monte-Carlo with the shared A arm modelled explicitly (2×10⁶ replicates, global null):
**0.00581** (s.e. ≈ 5×10⁻⁵). The slide overstates by about 30×. The arm correlation from the
shared baseline is negligible here (0.00581 vs 0.005848 under independence) — the whole error is
the conditioning. It also contradicts slide 11, which works unconditionally when it says the
best outcome "occurs only 0.5% of the time"; the deck mixes the two frames four slides apart.
This is the second wrong family-wise number on this slide: `curriculum/reviews/review-1-3-4.md`
item 2 replaced 14% with 18%, and the replacement is also wrong.
Fix direction: state the unconditional family-wise rate, about 0.6%, which makes "declare
every arm" an argument about honest reporting rather than about error inflation — and is the
stronger point, because it says a five-case eval will almost never produce a false winner *or*
a true one; or keep 17.6% and label it explicitly as conditional on every arm returning five
discordant pairs, an event of probability 0.031 per arm. Basis: exact combinatorics plus
Monte-Carlo executed during this review. **CONFIRMED.**

### [ch04-003] T major — slide 11
Quote: "Take a true effect of +20 percentage points against a 50% baseline — **the most
favourable assumption available**." (lines 274–275)
Why it fails: every number on the slide additionally assumes the A and B outcomes on the same
case are statistically independent — the assumption is never stated, and it is the one a paired
design least supports, since both arms run on the same case. I reproduced all five printed
figures exactly under independence (E[informative] = 2.500; 0.4125 / 0.2061, LR = 2.0017;
0.35⁵ = 0.53%, LR = 5.378; n = 103 at power 0.8018), then varied the pairing correlation with a
Gaussian copula on fixed marginals. At ρ = 0.4 the figures move in *both* directions:
E[informative] 2.50 → 1.93, P(5–0) 0.53% → 0.22%, LR(5–0) 5.38 → 10.17, and n for 80% power
103 → 81. So the scenario is not the most favourable available — two of the five numbers are
optimistic under any positive correlation, and the 103 is conservative rather than a floor.
Note for the editor: `review-1-3-4.md` item 10 asserts correlation raises required n above 103;
my computation shows the opposite, so do not apply that fix as written.
Fix direction: one clause naming the independence assumption, and restrict "most favourable" to
the effect size, where it is true. If a single caveat is wanted, say that positive correlation
between the arms lowers the number of informative cases and makes the 5–0 sweep rarer still.
Basis: exact enumeration plus Gaussian-copula computation executed during this review.
**CONFIRMED.**

### [ch04-004] T major — slide 8
Quote: "**A′ measures the spread with nothing changed.** If A and A′ disagree on two of five
cases, an A-versus-B difference of two or fewer is inside the noise." (line 197)
Why it fails: the rule applies a spread measured on the A arm to B1, B2 and B3, none of which
has a replicate — the conditions table on slide 7 has no B1′, B2′ or B3′ row. Nothing in the
design establishes that the B arms share A's spread, and a step-by-step instruction could
plausibly narrow it or widen it. The chapter's own specification says this must be on the
slide, twice: "**The choice made here is to keep five cases and accept an unmeasured noise
floor on the B arms.** Say so on the slide." (`assets/eval-worksheet/README.md` line 99) and
"That assumption is unstated in most small evals and it is unstated here unless the slide says
it." (line 180). Neither slide 8 nor slide 13's "two more traps" carries it.
Fix direction: add the unmeasured-B-arm assumption to slide 8 beside the rule, or promote it
into slide 13 in place of a weaker trap. Basis: the project's own worksheet §5 and §8, opened
during this review, plus the conditions table itself. **CONFIRMED.**

### [ch04-005] T major — slide 6
Quote: "So calibrate first: write ten candidates, run each three times at baseline, discard
anything scoring 3/3 or 0/3, keep the five nearest the middle. / That costs about thirty runs
and it is the difference between an eval that can detect something and one that cannot."
(lines 143–144)
Why it fails: the calibration is presented as pure gain, and the specification the slide points
at says the opposite — "**It is not free, and the cost runs the wrong way.**"
(`assets/eval-worksheet/README.md` line 65). Selection on a three-run statistic is selection on
noise, and it biases the very quantity slide 12 sells as "A noise floor. You learn how much
your own instrument moves when nothing changes." (line 309). I computed E[two-run disagreement]
for retained versus all candidate cases under four priors on the true pass rate: Beta(1,1)
0.3333 → 0.4000 (+20.0%); Beta(0.5,0.5) 0.2442 → 0.3750 (+53.6%); Beta(5,2) 0.3571 → 0.4000
(+12.0%); Beta(2,2) 0.4000 → 0.4286 (+7.1%). The retained set is enriched for high-variance
cases in every case, so the measured floor overstates the instrument's movement on the room's
ordinary work — which is exactly the use slide 12 puts it to. (The worksheet's own "biases the
floor **downward** by about ten percentage points" is arithmetically right but measured against
a hypothetical perfectly balanced item, not against the candidate pool; I reproduced its 0.40
figure under a uniform prior.)
Fix direction: state the cost in one clause on slide 6 and qualify slide 12's noise floor as a
property of the five selected cases, not of the room's work in general. Basis: the project's own
worksheet §3, opened during this review, plus the prior computation executed here. **CONFIRMED.**

### [ch04-006] R major — slide 16
Quote: "The original result: **eight worked chain-of-thought exemplars**, on a
540-billion-parameter model, with the ability stated to emerge in sufficiently large models. /
That is a result about supplying worked examples. It is not a result about typing four words at
a model that already reasons before it answers." (lines 416–417)
Why it fails: this is the ch03 ledger entry restated. `TOPICS-LEDGER.md` §ch03 records as
delivered: "the result rests on supplied worked exemplars; 'think step by step' at a model that
already reasons is a different proposition and is not what was tested", together with the
[ch03-005] correction that "the sufficiently-large-model condition belongs on the claim". Both
claims and the emergence condition are already the room's. The only new tokens are "eight" and
"540-billion-parameter", which are scope decorations on an argument already made, not new
information. Already flagged from the other side by `curriculum/reviews/review-1-3-4.md` item 5.
Fix direction: keep the argument in exactly one chapter. `review-1-3-4.md` item 5 recommends
stripping it from ch03 and landing it here on the B2 arm — if that is taken, this finding
dissolves and ch03's ledger entry must be amended; if ch03 keeps it, slide 16 should carry only
the B2 handoff. Do not apply both fixes.

### [ch04-007] C major — slide 16
Quote: headline "## Settling the second: think step by step" (line 412), against slide 1's
"Chapter 3 ended owing you two answers." (line 15) and the frontmatter's "Settles the two
claims Chapter 3 deliberately left open." (line 4)
Why it fails: the promise is made three times and paid once. Slide 15 settles the persona claim
with a published result; slide 16 restates ch03's scope argument and then defers — "It does not
reach this slide until it has been" (line 425). Withholding the `[P]` re-evaluation is the right
call under hard rule 1 and is not the defect; the defect is a headline and a chapter thesis that
assert a settlement the slide does not deliver. A trainee leaves believing the debt was
collected twice.
Fix direction: retitle to what the slide does — the scope argument plus the handoff to the B2
arm — and amend slide 1 and the frontmatter to promise one settled claim and one handed to the
room's own eval, which is the chapter's actual and stronger position.

### [ch04-008] C major — slides 14 and 17
Quote: "Header block to be filled before the run, not after: model ID, surface, thinking setting
and effort, date, **fresh-session policy**." (line 362) and "The settings that change behaviour:
thinking, effort, **fresh session or not**." (line 445)
Why it fails: the chapter promotes the session from background vocabulary to a controlled
experimental variable the trainee must record and hold constant, and no ledger entry defines it.
`TOPICS-LEDGER.md` records the gap explicitly under the superseded ch01 draft: "Session
defined — 'one continuous conversation, from opening it to closing it.' … **The ledger uses the
word throughout and never records a definition.**" The consequence is load-bearing rather than
terminological: the deck never states whether A′ runs in the same context as A or in a new one,
and the two measure different quantities — sampler noise versus sampler noise plus conversational
carryover from A's own output. Slide 8's "with nothing changed" (line 197) is only true of the
fresh-session reading. The worksheet fixes it ("Fresh session per case. Prior turns contaminate.",
line 105); the deck does not, and the deck is what the room sees.
Fix direction: define the session in one clause where it is first used as a variable, and state
the fresh-session policy on slide 8 where the A′ claim depends on it. Salvage the ch01 definition
named in the ledger rather than coining a new one.

### [ch04-009] C major — slide 11
Quote: "**Likelihood ratio 2.0** — and that outcome is mostly ties" (line 281) and "**Likelihood
ratio 5.4.**" (line 282), concluded as "The design's best case is both weak evidence *and* almost
never obtained." (line 283)
Why it fails: the likelihood ratio is the load-bearing evidential quantity of the slide and is
never defined, and no scale is given against which 5.4 reads as weak. No ledger entry supplies
it — ch01 delivers softmax, cross-entropy and the sampling distribution, none of which is this.
Without the definition and a scale the two numbers are inert and the slide's conclusion cannot be
evaluated by the reader, only accepted. The chapter holds itself to exactly this standard seven
slides earlier: "You cannot check a claim whose terms are undefined." (line 98).
Fix direction: one clause defining it as the probability of the observed outcome under the
assumed effect divided by its probability under no effect, plus the interpretive scale being
used, named — do not assert a band without attributing it.

### [ch04-010] C major — slide 7
Quote: "| **B3** | baseline with extended thinking off |" (line 173)
Why it fails: distinct from [ch04-001], which is about whether the setting exists — this is about
whether the room can reach it. `TOPICS-LEDGER.md` §ch03 carries an explicit standing warning:
"**Where `effort` is settable is not stated — see [ch03-006]; do not let a later chapter assume
this room can reach the dial.**" This chapter assumes it. The effort page's platform list is
"Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud, Microsoft Foundry" and its
per-model guidance names the Claude API and Claude Code; claude.ai appears nowhere.
`references.md` line 169 records the same boundary: "**Do not tell the room it can set effort in
the chat app**; that is not what the page supports." The chapter hands the room a five-condition
design to run at home and one condition of it is unreachable from the surface most of them use.
Fix direction: name the surfaces on which the design is runnable, and give a chat-app fallback
for B3 — `references.md` line 170 identifies per-message steering ("Answer directly without
deliberating.") as the lever that needs no API access — while stating that steering suppresses
rather than disables, so the fallback B3 is weaker than the configured one.

### [ch04-011] T minor — slide 11
Quote: "For 80% power you would need **103 cases** — exactly, by the same sign test. The normal
approximation says 93; **the discreteness of the exact test costs the other ten.**" (line 284)
Why it fails: 103 is right (exact power 0.8018 at n = 103, 0.7976 at n = 102), but the
explanation is not. Conditioning on the discordant count at m = n/2 — the approximation's own
assumption — while keeping the exact discrete test, 80% power first arrives near n = 98. So
discreteness accounts for roughly half the ten-case gap; the other half comes from the normal
approximation treating the discordant count as fixed when it is itself binomial. On a slide
whose authority is that its numbers are "combinatorial, not an estimate", the wrong causal
attribution is the part a trainee carries away.
Fix direction: "the normal approximation says 93, treating the discordant count as fixed at n/2
and the test as continuous; the exact test's discreteness and the randomness of that count cost
about five cases each." Basis: exact power enumeration, conditional and unconditional, executed
during this review. **CONFIRMED.**

### [ch04-012] C minor — slide 8
Quote: "Output is stochastic. Chapter 1 said so; **you watched it in the temperature demo.**"
(line 195)
Why it fails: the substantive anchor holds — ch01 delivers the sampling step and locates output
variance there — but no ledger entry delivers a temperature *demo*. `TOPICS-LEDGER.md` records
spec slide 19 as a worked inverse-CDF draw at three temperatures, and Supp §S17 lists what the
lab does not contain, naming "sampling variety" among the items "absent and named as absent".
An appeal to a shared experience the room did not have lands as a false memory and costs the
callback its force.
Fix direction: cite the artefact the ledger actually delivers — spec slide 19's worked draw at
three temperatures — or add the demo to ch01 and keep the sentence.

### [ch04-013] F minor — slide 13
Quote: "the per-arm rate cannot be 5%, because **two slides ago** you proved five cases have no
5% rejection region at all" (line 334)
Why it fails: the proof is on slide 10, three slides back; two slides back is slide 11, the
worked best-case example. A reader who follows the instruction lands on the wrong slide. The
same slide-relative idiom fails once more at "the 5–0 row in **the table opposite**" (line 282),
which assumes a facing-page layout the deck does not have — the table is on the preceding slide.
Fix direction: reference slides by their headline rather than by offset, since the offsets will
break again at the next reordering.

### [ch04-014] S4 minor — slide 11
Quote: "Only about **2.5 of the five cases** are expected to be **informative**. The rest tie."
(line 280), repeated at "five **informative** cases, all favouring B" (line 282)
Why it fails: the standard term for a pair on which the two conditions differ is a *discordant
pair*; it is the term the sign-test and McNemar literature uses, and the word "discordant"
appears nowhere in the chapter. The chapter otherwise works hard to hand over searchable
vocabulary — "Paired sign test, ties dropped" (line 247) is exactly that — and slide 12 tells
the room to scale up to "a bigger eval", which means reading that literature. The substituted
term is the one gap in that handover.
Fix direction: use "discordant" on first mention and gloss it as informative, e.g. "about 2.5 of
the five cases are expected to be discordant — the pairs where the two conditions disagree, and
the only ones the test counts."

## Coverage checklist

| promise | where | status |
|---|---|---|
| "Converts the course from advice into method" | frontmatter line 4 | paid, slides 5–13 |
| "Starts the verification thread" | frontmatter line 4 | paid, slide 17 line 452 |
| "Settles the two claims Chapter 3 deliberately left open" | frontmatter line 4, slide 1 line 15 | half paid — persona at slide 15; chain-of-thought unpaid, [ch04-007] |
| "How you know any of Chapter 3 worked" | slide 1 line 11 | paid, slides 5–13 |
| "an expert, a denominator, and a factor of two" | slide 3 headline | paid, slide 3; matches `references.md` line 181 including the attribute-to-the-reader rule |
| "Full specification … in `assets/eval-worksheet/README.md`" | slide 5 line 124 | paid — the file exists and carries the criterion rules (§4) and conditions (§5); under RUBRIC v1.1 this pointer's target is the definitional home for the pass criterion, so no per-field contract finding is raised on slide 5 |
| "You take a blank copy home" | slide 5 line 125 | pointer honest but unbuilt — the blank template is listed in worksheet §7 as a material still to produce. Production status, not a draft-content gap; no finding |
| "TODO(instructor) — the five cases" | slide 6 lines 150–152 | unpaid. Already flagged — PR19 line 336 and cross-cutting A2 (PR19 lines 78–91); cited, not re-derived |
| "Closing that needs a second grader, and there isn't one" | slide 9 line 231 | paid on the same slide, disclosed rather than solved |
| "TODO(capture) — the instructor's eval" | slide 14 lines 358–362 | unpaid, and the "cannot tell" outcome the slide calls most likely has no stated next action. Already flagged — PR19 line 336 and lines 340–342; cited, not re-derived |
| "TODO(verify)" on the CoT re-evaluation | slide 16 lines 423–425 | correctly withheld at `[P]` under hard rule 1; not a coverage gap. Contributes to [ch04-007] only through the headline |
| Power-curve figure | — | absent. Already flagged — PR19 lines 338–339; cited, not re-derived |

## Topics exported

- **The folklore diagnosis, as three named defects** — one run, a pass criterion chosen after seeing the output, and no control condition. Slide 2, lines 33–35. The frame later chapters should use when a prompting claim arrives without a method.
- **The MACs-versus-FLOPs erratum as the course's anchor artefact** — a unit-definition error in expert material, producing a clean factor of two, caught by an outside reader after publication; one MAC is two FLOP, and the numerator needs the factor or the denominator does. Slides 3–4, lines 57–72. `erratum2026`, `[V]`, attributed to the reader and not the lecturer.
- **"You cannot check a claim whose terms are undefined"** — slide 4, line 98. The chapter's own justification for pre-defining the pass criterion, and the sentence the rest of the course's verification thread rests on.
- **The minimal eval** — five frozen cases from the room's own work, one binary pass criterion per case fixed before any output is seen and checkable without seeing the other condition, run A, run B, count. Slide 5, lines 116–118. Full specification, including the four criterion-writing rules, is `assets/eval-worksheet/README.md` §4.
- **Case calibration by difficulty** — a case the model always passes or always fails has zero power at any sample size; write ten candidates, run each three times at baseline, discard 3/3 and 0/3, keep the five nearest the middle. Slide 6, lines 142–144. **Carry [ch04-005] with it: the selection is not free, and the noise floor measured on the survivors overstates the instrument's movement on ordinary work.**
- **A′, the repeated baseline** — a repeatability check on an instrument, read before any A-versus-B result; if A and A′ disagree on k of five, treat any A–B difference of k or fewer as inside the noise. Slides 7–8, lines 170 and 197. **Two caveats travel with it: the B arms carry no replicate, so their spread is assumed rather than measured ([ch04-004]); and the session policy that makes "with nothing changed" true is stated only in the worksheet ([ch04-008]).**
- **Blinding, with its limit disclosed rather than solved** — strip condition labels, opaque IDs, shuffle, grade pass/fail, unblind afterwards; discard the thinking transcript at capture because it identifies B3 with certainty; insert duplicates to measure grader drift, which A′ does not. It is not a blind against the person who designed the conditions, and closing that needs a second grader who does not exist. Slide 9, lines 221–232. The disclose-rather-than-oversell form is the reusable object.
- **A paired sign test on five cases cannot reach two-sided *p* < 0.05 under any outcome; six is the minimum, and power at α = 0.05 is exactly zero** — combinatorial, not an estimate. Slide 10, lines 247–261. Every value in the p-value table was recomputed here and is exact.
- **The best obtainable result is weak and rare** — under a +20-point effect on a 50% baseline, about 2.5 of five cases are expected to be discordant; the 5–0 sweep carries a likelihood ratio of 5.4 and occurs 0.5% of the time even when the effect is real; 103 cases are needed for 80% power. Slide 11, lines 280–284. **All five figures assume zero within-case correlation between the arms — state it ([ch04-003]) — and the 103 is exact while the "discreteness" explanation beside it is not ([ch04-011]).**
- **State the limit before showing the result** — slide 11, line 291. The chapter's rhetorical thesis and the reason its audience grants it credibility; later chapters presenting weak evidence should follow the same order.
- **Five cases buy a screen, a noise floor and a habit — not a finding.** Slide 12, lines 308–310. The honest scope of every small eval in the course.
- **Declare every arm** — reporting only the interesting arm is post-hoc selection of the winning condition. Slide 13, lines 334 and 340–341. **Export the rule, not the number: the 18% family-wise figure is wrong by about 30× ([ch04-002]).**
- **Two disagreements out of five gives a 95% interval of roughly (0.05, 0.85)** — the noise floor is a conservative screen, not an instrument. Slide 13, line 333. Clopper–Pearson, recomputed here as (0.0527, 0.8534).
- **The persona accuracy claim, settled** — 162 roles, four model families, 2,410 factual questions; personas in system prompts did not improve performance over no persona. Its scope is those families and that question set, not Opus 5 and not civil engineering. Slide 15, lines 386–388. `zheng2024`, `[V]`. This closes the claim ch03 left open.
- **Post-hoc selection of the winning condition, named and generalised** — picking the best persona per question helps, but identifying it in advance is no better than chance; the same mechanism will manufacture a result out of five cases. Slide 15, lines 394–397. The paper establishes it for persona selection; the generalisation to prompting folklore is the course's own.
- **The chain-of-thought claim is not settled, and the room's own eval is what settles it.** Slide 16. The `[P]` re-evaluation is withheld under `TODO(verify)` rather than quietly used. **Do not let a later chapter cite this chapter as having resolved it — and see [ch04-006]: the scope argument itself belongs to ch03 unless it is moved.**
- **Record the version or you have recorded nothing** — model ID and date beside every result, plus the settings that change behaviour (thinking, effort, fresh session or not); a working prompt is a measurement and measurements expire, so re-test before relying on it again. Slide 17, lines 444–446. **"Fresh session" is undefined in the delivered curriculum ([ch04-008]) and the effort dial may be unreachable from the room's surface ([ch04-010]).**
- **Verification thread opened** — prompts here, sources in Chapter 14, arguments in Chapter 17, the logging discipline in Chapter 18. Slide 17, lines 452–453.
- **Not exported: "extended thinking off" as a runnable condition.** The B3 arm as written is not a valid configuration at the eval's own `xhigh` baseline ([ch04-001]). No later chapter may assume this room has a thinking on/off switch independent of effort.

## Checks not run

- **Primary sources for `zheng2024` and `wei2022` were not opened.** Both were checked against `ai-training/references.md`, where each is `[V]` and the slide's numbers (162 roles / four model families / 2,410 factual questions; eight exemplars / 540-billion-parameter model / emergence in sufficiently large models) match the records verbatim. An error already inside `references.md` passes through this review unchanged.
- **The `erratum2026` gist comment thread was not opened.** Slide 3's account matches `references.md` line 181 including the direction of the factor and the instruction to attribute the correction to the reader.
- **The `[P]` chain-of-thought re-evaluation behind slide 16's `TODO(verify)` was not read**, which is what the marker says and is the correct state; I did not attempt to adjudicate it.
- **The deck was not built or rendered.** No Beamer source exists for this chapter, so `CLAUDE.md` §1c (every slide carries a footer or a `\provenance{}`) and the overfull-vbox gate are unenforced here and were not assessed. Footer coverage sits outside the five rubric classes and was not scored; note that fifteen of eighteen slides in this Slidev draft carry no `<Cite>` and no provenance declaration, which will need resolving at rebuild.
- **The five-field C contract test was applied to one component only.** Fields (3) necessity-on-removal, (4) deployed capability and (5) pipeline/stage location are written for model components; the chapter's objects — the minimal eval, A′, blinding, the pass criterion — are experimental-design procedures with no pipeline location, and forcing the fields onto them would have generated findings with no reader-facing consequence. I applied the test only to *extended thinking*, the one product component the chapter manipulates, which produced [ch04-001] and [ch04-010]. This is a scoping judgement, recorded rather than applied silently.
- **The correlation figures in [ch04-003] are illustrative, not estimated.** A Gaussian copula on fixed marginals shows the direction and rough magnitude of the effect; I did not estimate the actual A/B correlation, which would need the instructor's run and does not exist yet.
- **The Monte-Carlo family-wise rate in [ch04-002] used 2×10⁶ replicates** (0.00581, s.e. ≈ 5×10⁻⁵). The exact figure 1−(1−1/512)³ = 0.005848 is the analytic value under independent pairing; the two agree, so the shared-A correlation is confirmed negligible at n = 5 but was not derived in closed form.
- **The vendor documentation is version-fragile.** Both pages were fetched 2026-08-28; `references.md` line 170 already carries "re-fetch in the week before delivery", and [ch04-001] depends on a per-model behaviour that could change before the session.
- **Timing was not assessed** — neither the chapter's length against the session budget nor the eval exercise's fit. Out of scope for this rubric and already handled at course level.
- **The eval worksheet was not reviewed as a deliverable in its own right**, only the sections the slides point at (§3, §4, §5, §6, §7, §8).
- **PR19's premise-level verdict was not re-litigated.** The chapter is graded "holds — the highest-value chapter in the course for this audience" (PR19 lines 322–323); nothing here contradicts that, and the missing-eval, missing-power-curve and missing-"cannot tell"-action items are cited in the coverage checklist rather than re-derived.

## Verdict

**salvage-with-edits.** The chapter's argument is sound, its ordering is clean, every slide
carries a statable Message, and twelve of its recomputable figures reproduce exactly — the
sign-test table, the zero-power argument, the expected-informative count, both likelihood
ratios, the 0.5% sweep probability, the 103-case sample size and the Clopper–Pearson interval
all survive independent recomputation. That is a stronger numerical record than any chapter
reviewed in this directory so far, and the structural spine needs no rebuilding. But the two
blockers both sit on the chapter's own claim to authority rather than at its edges: B3, the arm
that exists to remove a confound, is not a runnable single-factor condition on the model the
eval is configured for, which means the design as printed cannot produce the interpretation
slide 7 promises; and the family-wise rate is wrong by roughly thirty-fold on the one slide
whose subject is not deceiving yourself with small numbers — the second wrong version of that
number to reach this slide. Neither is a rewrite: one is a header-block change plus a sentence,
the other is a number and a clause. The six major findings are all additions of caveats the
chapter's own worksheet or the topics ledger already contains, plus one duplicated slide and
one unpaid headline. Fix in this order: [ch04-001] and [ch04-002], then [ch04-007] and
[ch04-006] together since they share a slide, then the three unstated-assumption findings
[ch04-003]–[ch04-005], then the coverage gaps. A chapter with any unresolved blocker cannot be
"usable-with-fixes", and these two are unresolved.

# Peer review of all nineteen chapter premises

Written 2026-08-20, session 54c51687-7672-4655-abf1-096660913fe5, before any chapter was rewritten.

**What this is.** `HANDOFF.md` §10 asks for the premise of every chapter to be reviewed before
any of it is rebuilt, on the grounds that the previous agent treated `chapter-briefs.md` as a
specification and never challenged it. This is that review. It treats the briefs, the spine and
`architecture.md` as proposals under test. It treats the instructor's recorded criticisms as the
specification, because those are observations about a delivered artefact rather than plans for one.

**What I read.** All nineteen decks in full, `HANDOFF.md`, `narrative-spine.md`,
`chapter-briefs.md`, `architecture.md`, `research-slide-design.md`,
`research-teaching-exemplars.md`, `CLAUDE.md`, `DECISIONS.md`, `START_HERE.md`,
`references.md`, the Slidev build configuration and the figure script.

**Two claims in this document rest on sources I fetched today**, both logged in `SOURCE-LOG.md`
and both primary vendor text rather than search summaries. They are marked where they appear.

**Grading.** Each premise gets one of: **holds** · **holds, wrong size** · **half-true** ·
**mis-scoped** · **not a chapter**.

---

# Part A — findings that outrank any individual chapter

These came out of reading all nineteen together. Each one changes more than one chapter, so
none of them can be fixed inside a chapter rewrite.

## A1. SUPERSEDED — delivery length is not a criterion

**Ruled 2026-08-20:** *"Do not worry about the time. Do not ever talk about the time again. I will
decide what to keep. More details is better from your end."*

The arithmetic below is left in place as evidence the instructor can use or ignore. **It is no
longer a reason to cut anything**, and no recommendation in Part B rests on it any more. Where a
chapter is marked "wrong size" further down, read only the content reason given alongside it — that
it changes no decision this audience will make, that it repeats a lesson already taught, or that its
premise is wrong. Every chapter is now written in full.

### The original finding, retained as evidence


`DECISIONS.md` records one blocking overrun: Chapter 2 at 105–115 minutes against 75. That is
real, and it is a fraction of the actual overrun.

Estimating at 1.5–2.5 minutes per delivered slide plus the stated exercise times:

| Chapter | Slides | Exercise | Estimate |
|---|---|---|---|
| 1 Substrate | 14 | — | 25 min |
| 2 Formation | 26 | 35–40 | 105–115 min (their figure) |
| 3 Control | 17 | — | 35 min |
| 4 Measurement | 17 | — | 45 min |
| 5 Intrinsic failure | 21 | — | 45 min |
| 6 Extrinsic failure | 12 | demo | 35 min |
| 7 Physical limits | 16 | — | 50 min |
| 8 Brain and model | 12 | — | 30 min |
| | | | **≈ 375 min** |

Four hours minus breaks is about 210 minutes of delivery. Session 1 is over by roughly 165
minutes. Splitting Chapter 2 into 2a and 2b does not touch this; it renames part of it.

The same arithmetic gives Session 2 at ≈ 205 minutes, which fits, and Session 3 at ≈ 270,
which is over by about 60.

**Consequence.** Every "should this chapter be shorter?" question below is being asked against
a real deficit, not a preference for brevity. Session 1 has to lose about 165 minutes or gain
a fourth session. The chapters that should give it up are named in Part B.

**Even after every cut recommended here, Session 1 lands near 240–290 minutes.** The honest
conclusion is that Session 1 needs either 4.5 hours or one whole unit moved out of it. Two
units are movable without breaking a sequencing constraint: Chapter 6 to the opening of
Session 2 (the constraint is "6 before Part III", which the start of Session 2 satisfies
exactly, and it puts the threat model on the same day the room opens the channels) and
Chapter 7 to Session 2 beside Chapter 13. That is the instructor's call and it is the largest
single decision left in the course.

## A2. Four hours pass before anyone in the room touches the tool

The first attendee exercise is Chapter 9, at the start of Session 2. Session 1 contains one
participatory block — the Chapter 2 rating exercise — in which nobody uses the tool; they rate
two responses on paper.

Chapter 4 is the sharpest case. It is the chapter that "converts the course from advice into
method", and every one of its five cases is `TODO(instructor)`. The room watches somebody
else's experiment. A group of experimentalists is being taught experimental method as a
spectator sport.

**Recommendation.** The room runs the Chapter 4 eval on their own five cases, chosen in
pre-work. This is the single change that would most improve Session 1, and Part B names where
the time comes from.

## A3. Two live factual errors of a class the handover has already recorded once

`HANDOFF.md` §4 records one over-simplification that was false for the tool the audience
actually uses: a slide said the model "isn't looking anything up", which is wrong when web
search is available. Two more of the same class survive.

**(a) Chapter 5: "Arithmetic is done by prediction, not by calculation."**

The vendor's code-execution documentation, fetched today, states: *"Claude runs code when the
request benefits from computation or file handling"*, listing *"Non-trivial math (large
numbers, many steps, precision-sensitive results)"*; and *"Claude answers directly without
running code for: Simple arithmetic and well-known math facts … Simple unit conversions or
translations."*

So the slide is false for non-trivial arithmetic and true for simple arithmetic — and the
documented exception, **simple unit conversions**, is precisely the failure class the chapter
spends the slide warning about. Corrected, the slide gets better rather than weaker: the
boundary between predicted and computed is a published routing rule, the routing is visible in
the transcript, and the class that stays predicted is the class this audience cares about.
The chapter should teach the check ("did it run code, or did it answer?") rather than the flat
claim.

**(b) Chapter 14: "What survives PDF extraction, and what does not."**

The slide describes two-column interleaving, equation flattening and table collapse. Those are
properties of a text extractor. The vendor's PDF documentation, fetched today, states: *"The
system converts each page of the document into an image. The text from each page is extracted
and provided alongside each page's image."*

Both happen. The extraction failures the slide names are real and remain real, and the page
image sits beside them, which means a chart, a photographed figure and a two-column layout are
readable in a way the slide implies they are not. The chapter also gives no limits; the
documented ones are 32 MB per request and 600 pages, falling to 100 pages when the context
window is under 1M tokens.

**The pattern is the finding.** Three errors of one kind have now been found, each produced by
describing the raw model and presenting it as a description of the product. Every chapter needs
one pass asking: is this true of the thing in the room, or only of the network?

## A4. The course never mentions that these tools accept images

Nineteen chapters, no slide anywhere on image input. For an experimental group this is the
largest content gap in the course. They photograph specimens, screenshot plots, paste figures
out of papers and hand over scanned drawings. The vendor documentation records JPEG, PNG, GIF
and WebP input, up to 600 images per request, and visual analysis of PDF pages.

It belongs in three places: as a lever in Chapter 3, as the actual mechanism of literature work
in Chapter 14, and as a way into a figure or a plot in Chapter 16.

## A5. The audience's own experimental data never appears

The room does experimental testing. Chapter 16 covers inherited code, translation,
vectorisation, tests and units. Nothing in the course covers pointing the tool at a measurement
file: sanity-checking a sensor trace, spotting saturation or drift, choosing a filter,
producing a first plot, or catching a channel that died mid-run.

That is at least as much of their week as inherited code, and it is the use where a wrong answer
is most likely to be silent. Chapter 16 should absorb it and should get longer, not shorter.

## A6. Version control is assumed by three chapters and taught by none

Chapter 9 makes the diff the artefact of responsibility. Chapter 10 says the instruction file is
"committed, shared, reviewed like code". Chapter 15's whole premise is a versioned text
pipeline. Chapter 18 says "version control is the record. It timestamps, it diffs, and it is
already in your workflow."

`HANDOFF.md` §1 says terminal experience is rare. For a MATLAB group with rare terminal
experience, git is not already in the workflow. Either budget twenty minutes for it before
Chapter 9, or stop resting four chapters on it.

Related and worse: Chapter 9 teaches "read the diff before you approve it" and never teaches
what to do when you approved one you should not have. There is no recovery path anywhere in the
course. For this audience that is the gap that will actually cost someone a day.

## A7. The evidence-grading lesson is taught five times and has saturated

Ranking findings by evidence rather than by force is the strongest habit this course teaches,
and it appears as: the Chapter 2 findings ranking, the Chapter 5 long-context material, the
Chapter 6 incident chased to nothing, the Chapter 8 brain literature, and the Chapter 7
alternative-substrates table.

The first four are each attached to something the room needs anyway. The fifth is attached to
neuromorphic chips and brain organoids, which change no decision anyone in that room will make.
When a lesson has been taught four times, the fifth instance has to justify itself on its
subject matter, and that one cannot.

## A8. "Every slide carries a citation footer" is already violated by design and needs an explicit rule

`CLAUDE.md` house style requires a footer on every slide. `CLAUDE.md` §1b names exactly one
permitted exception. The rebuilt Chapter 1 carries fourteen slides and zero footers, and it is
right to: a slide defining what a token is has no source to cite that would not be invented
attribution.

The rule as written cannot survive a teach-from-zero chapter, because definitional slides
outnumber evidential ones there. It needs a third category — **definitional slides carry no
footer, and the chapter's term audit is what makes them accountable instead** — or the term
audit has to be published with the deck. I have written Chapter 1 on that basis and the audit
is attached. The rule should be amended or my reading rejected; it should not be left ambiguous.

## A9. Figure coverage is 2% against a specification of 50%, and the machinery to fix it is already built

Five figures across 245 slides. `research-slide-design.md` §6 sets a floor of 50%, derived from
the one observational result in the review where image fraction predicted evaluation score and
text density did not.

Mermaid renders inline, matplotlib is wired with a committed script that already writes into
`slides/public/figures/`, and one figure in that script — `01-kv-growth.png` — is generated and
never used by any deck. The obstacle is not toolchain. Every chapter needs a figure plan written
before its slides, and eleven of the nineteen currently have zero figures.

## A10. The prose defect is systemic, not confined to Chapter 1

`HANDOFF.md` §5 lists banned constructions with real examples. Running its own grep across the
eighteen chapters that were not rebuilt returns hits in most of them, and the closing line of
Chapter 19 — "That is the trade you have actually made this term" — is one of the handover's own
cited examples, still in place in the final slide of the course.

This is not an argument for a global find-and-replace. It is an argument that the prose has to be
rewritten chapter by chapter with the grep run as a gate, and that no chapter should be declared
finished until it passes.

---

# Part B — chapter by chapter

## Chapter 1 — Substrate

**Premise as written:** "It predicts the next fragment of text, over and over, from a finite window."

**Verdict: mis-scoped.** The sentence is true and it presupposes its own subject. "It" is never
identified. The premise describes an operation without naming the object that performs it, which
is the defect the instructor named twice — once as "we haven't even talked about what is AI"
and once as "we are telling the audience that something is like a brain without even identifying
the 'IT'".

**Useful.** The data path is correct and the order is right. Tokens arriving because prediction
needs units is the correct motivation. The determinism/sampling separation earns temperature.
The slide correcting the retrieval over-simplification is honest and necessary. The two figures
are the best in the repository.

**Useless.** Two items:
- **The KV cache**, per the brief, is "named so Chapter 7 can price it". A term whose payoff is
  six chapters away does not belong in the chapter that must define everything from zero. The
  rebuilt deck already dropped it; the figure is still generated and unused. Confirm the cut.
- **"Three things this chapter leaves out"** is a scope note addressed to the instructor, not
  content the room needs. It belongs in speaker notes.

**Missing.** The entire front half. AI, LLM, model, parameters, weights, network, training,
inference, forward pass — used or implied, none defined. Also missing: the reason scoring
exists at all, which without a sentence looks like an arbitrary design choice.

**One thing to kill outright.** `chapter-briefs.md` still says Chapter 1 "opens the course with a
question it will not answer yet: is this like a brain?" That device is the specific thing the
instructor rejected. It should come out of the brief, not merely out of the slides.

**Revised premise.** *A large language model is a fixed set of numbers left behind by training;
one run of it scores which fragment of text plausibly comes next, and running it repeatedly is
what produces an answer.*

**Forces:** nothing in scoring text fragments produces a helpful assistant, which is Chapter 2.

---

## Chapter 2 — Formation

**Premise:** "It behaves like an assistant because people rated outputs and it was optimised toward those ratings."

**Verdict: holds, wrong size.** This is the strongest premise in the course and the annotation
material is the genuine differentiator. It is also two chapters, which `DECISIONS.md` already
knows.

**Useful.** Nearly all of it. The rubric-dimension table that seeds six later chapters is the
best structural device in the repository. The behaviour-to-mechanism table with a standing
column, including a row that says the folk explanation is contradicted and the real mechanism is
not visible, is exactly the standard the course claims. The nine findings with document counts
printed on the slide. The rating exercise, including the instruction to call six raters a tally
and not a distribution.

**Useless.** Three slides in the pipeline half:
- **"Not every parameter runs"** (sparse models) exists to feed the sparsity term in Chapter 7's
  critical batch size. If Chapter 7 shrinks as recommended below, this slide has no consumer.
- **"And a simplification worth knowing"** (direct preference optimisation) changes nothing the
  audience does. Facilitator notes.
- **"What scale bought, and what it did not"** is history. Compress to one line inside pretraining.

That is roughly eight minutes, and it comes out of the half that is not the differentiator.

**Missing.** A diagram. Twenty-six slides, zero figures, describing a five-stage pipeline that is
a process — the exact case where `research-slide-design.md` makes a figure mandatory. Also
missing: **system prompt**, used from Chapter 3 onward and never defined.

**Adopt the 2a/2b split.** The recommendation in `DECISIONS.md` is right and the seam is in the
right place. It preserves the numbering the thread map depends on.

---

## Chapter 3 — Control

**Premise:** "The levers that work, and why they work — each maps to something that was rated."

**Verdict: holds.** The mapping device is the best pedagogical idea in the course. It converts a
list of tricks into a set of consequences, which is precisely what the handover says the briefs
failed to do everywhere else.

**Useful.** The "maps to" line under each technique. The three anti-patterns as rubric
exploitation in reverse. The role slide, which separates what the documentation actually claims
(behaviour and tone) from the claim people hear (accuracy) and hands the difference to Chapter 4.
"Prompts do not port."

**Useless.** Little. "Thinking and effort" is version-fragile and is correctly hedged.

**Missing.** Three things, and the first two are levers this room will reach for on day one:
- **Attaching a file or an image.** Absent from the chapter and from the course (finding A4).
  For this audience, handing over a figure or a page of a paper is a more important lever than
  few-shot examples.
- **Which model, and when it matters.** The room will face a picker with several options and a
  thinking toggle, and the course never mentions it.
- **System prompt versus user message**, used throughout and defined nowhere.

**One structural weakness to state on its face.** Eight of seventeen slides cite one vendor
documentation page. That is honest sourcing of a genuinely primary source, and a chapter about
technique resting almost entirely on the vendor's own claims about its product, inside a course
about source discipline, should say so on a slide rather than only in the footers.

---

## Chapter 4 — Measurement

**Premise:** "Turning a prompting claim into a test you can run in an afternoon."

**Verdict: holds.** The highest-value chapter in the course for this audience, and the one whose
content is furthest above what is normally taught on this subject.

**Useful.** The statistical honesty is the best thing in the repository: five cases cannot reach
two-sided p < 0.05 under any outcome; power at α = 0.05 is exactly zero and combinatorial rather
than estimated; the best obtainable result carries a likelihood ratio of 5.4 and occurs 0.5% of
the time under a real effect; 103 cases for 80% power, with the ten-case gap between the exact
test and the normal approximation explained. The A′ null strip. The instruction to declare every
arm. Calibrating cases to the middle of the range so the design has any power at all.

**Useless.** Nothing.

**Missing.** Three things:
- **The room running it.** See A2. Every case is `TODO(instructor)`.
- **A figure.** Seventeen slides, zero figures, in a chapter built on a sign-test table and a
  power argument. The power curve against number of cases is a figure that is begging to exist
  and would carry the chapter's hardest point in one image.
- **What to do when the answer is "cannot tell".** The chapter says this is the most likely
  outcome and gives no next action. Give one: escalate to ten cases, or accept the prompt on
  grounds other than measured accuracy — auditability, cost, reproducibility — and say which.

**Cross-reference to fix.** The MACs-versus-FLOPs anchor is borrowed from Chapter 7, and Chapter 7
says "Chapter 4 uses this as its anchor". If Chapter 7 moves to Session 2 as recommended, the
erratum still stands alone, but both directions of that cross-reference need rewriting.

---

## Chapter 5 — Intrinsic failure

**Premise:** "Some failures are structural — better prompting does not remove them."

**Verdict: holds, wrong size.** True, and the chapter is three chapters wearing one number.

Slides 1–8 are the mechanism of being wrong. Slides 9–16 are a research-literature review of
long-context accuracy. Slides 17–21 are detection, watermarking and interpretability. They have
different audiences and different actionable residues.

**Useful.** The confabulation band, and the observation that this audience's own literature sits
in it — the single most useful sentence in Session 1, because it explains their lived experience
of the tool. Calibration as a token sequence rather than a measurement. Benchmark scores not
predicting your problem. Detection false positives falling on non-native English writers, with
the direction taught and the March 2023 percentages dated. "It told me why" is not "I know why."

**Useless for this room.** Not wrong, but not earning its minutes:
- **The long-context block, at eight slides.** The actionable residue is one sentence: put the
  important material at the start or the end, and do not assume a large window is used well.
  The softmax-dispersion result, the licensing comparison between the TACL and arXiv versions of
  one paper, and the needle-in-a-haystack provenance are careful and expensive.
- **The interpretability block, at four slides.** Sparse autoencoders and attribution graphs
  change nothing anyone in that room does. The one sentence that matters — the model's stated
  reasoning is not evidence of its actual computation — deserves a slide, and the rest does not.

Compressing those two blocks to three slides total recovers about twenty minutes.

**Missing.**
- **The near-miss citation** gets one line and is the most common real failure: a real paper,
  correctly cited, that does not say what it is cited for. It needs its own slide with an
  instance, because resolving the identifier does not catch it.
- **The correction in A3(a).** The arithmetic slide is false as written for the tool in the room.

---

## Chapter 6 — Extrinsic failure

**Premise:** "Text you did not write can act as an instruction, and there is no clean fix."

**Verdict: holds.** The tightest premise in Session 1 and the cleanest argument in the course.

**Useful.** Instructions and data sharing one channel, with the standard's own words that there
is no clean equivalent to parameterised queries. The OWASP ranking taught together with the
caveat its own authors publish, that the same item falls out of the top ten entirely when ranked
against their incident corpus. The training-data-poisoning slide, which names a threat the room
cannot defend against and argues for a habit rather than a product. Incident two chased to
nothing, reported as nothing, and carrying no footer because there is nothing to put in it —
the best single slide in the repository.

**Useless.** Nothing is wrong, but the balance is off: four of twelve slides are incidents, and
one of them resolves to no source. That is an excellent epistemics lesson and a thin threat-model
lesson. One well-sourced incident plus the one-slide account of the unreachable one is enough.

**Missing.**
- **A diagram.** Zero figures in a chapter whose entire content is a mechanism: one channel, two
  origins, no envelope. That is the definition of a mandatory figure.
- **The case that will actually bite this room.** A preprint PDF or a shared repository README
  containing an instruction aimed at the agent, opened in a session that can write files. The
  demo is `TODO(produce)`, so until it exists the chapter is abstract.
- **Permissions**, used on the "what you can actually do" slide and not defined until Chapter 9.

---

## Chapter 7 — Physical limits

**Premise:** "What it costs to run, and why long context is expensive and slow."

**Verdict: holds, wrong size.** True, and the chapter is about twice the size its premise
justifies for this audience.

**Useful.** The governing-constraint framing is genuinely native to civil engineers and is the
best discipline bridge in the course — they do exactly this with load paths and limit states.
The roofline bound and the cost-per-token hyperbola in batch size. Long context bound by memory
bandwidth and capacity rather than compute. The MACs-versus-FLOPs erratum. The energy slide with
no number on it, which is the correct answer to a contested quantity.

**Useless for this room.** Critical batch size (nobody in that room will ever choose one), expert
and pipeline parallelism, memory capacity per device, the 6ND training accounting, and the three
alternative substrates — reversible networks, neuromorphic hardware, organoid computing. The
last three are about fifteen minutes and are the fifth instance of the evidence-grading lesson
(finding A7), attached to the least decision-relevant subject in the course.

**Missing.** A figure. Sixteen slides, zero figures, in a chapter about a hyperbola. The cost
curve against batch size must be plotted, and `01-kv-growth.png` — already generated, currently
used by nothing — belongs here.

**One sourcing problem worth stating plainly.** Every slide but three cites a single podcast
transcript by the CEO of a chip company, with a declared conflict of interest whose direction
matches the lecture's conclusion. The COI slide is exemplary and it does not make the chapter
sound. The roofline model is a published, citable result with a standard reference, and the
derivations here are checkable from first principles. Either add a second source or cut the
chapter to the part the room can derive.

**Recommendation.** Cut to about eight slides and move to Session 2, immediately before
Chapter 13, so that physical cost and billed cost sit together. Chapter 10's forward reference
to the roofline does not need it — "resident context is re-read every turn and you pay per
token" follows from Chapter 1 alone.

---

## Chapter 8 — Brain and model

**Premise:** "The brain comparison generates hypotheses but fails as an explanation, and it fails hardest on memory."

**Verdict: holds, and has the weakest claim on the room's time in the whole course.**

This is the best scholarship in the repository and I am recommending it be cut to a quarter of
its length. Both things are true and the second follows from the audience, not from the quality.

**The case against, in full:**
1. The question it exists to answer — "is this like a brain?" — is opened in Chapter 1 by a
   device the instructor explicitly rejected. Without that device the chapter has no question.
2. Its structural job is to motivate Chapter 10. Chapter 1's "nothing carries over when the
   session ends" already does that, in one slide, seven chapters earlier.
3. It costs about thirty minutes from the session that is 165 minutes over budget.
4. It is a cognitive-neuroscience literature review delivered to civil engineers. Its four
   load-bearing sources sit outside the competence of everyone in the room, including the
   instructor's, which means no one present can check the reading.
5. Nothing in it changes what anyone does on Monday, and the chapter says so itself: "as a guide
   to what the tool will do on Thursday, it is worse than useless."

**Useful, and worth keeping.** Three things:
- Transformers were not derived from neuroscience.
- The encoding-model result is correlational, and its "nearly 100% of explainable variance"
  headline is normalised by noise ceilings of 0.32, 0.17 and 0.20.
- Four chunks against two hundred thousand tokens is not a weak comparison; no conversion between
  chunks and tokens is defined, so no ordering exists. **This is the most transferable teaching
  point in the chapter** and it is a civil-engineering skill wearing neuroscience clothes: it is
  the same error as dividing by a denominator whose units were never stated, which is the
  chapter-4 anchor arriving from another direction.

**Useless for this room.** The Contributed-track review note, the untrained-model result and its
dissolution, the nine-epilepsy-patient electrode study, the Antonello and Hadidi re-analyses, and
the frontal-cortex refusal. Beautiful, and none of it changes a decision.

**RULED 2026-08-20 — dissolved, and placed differently from this recommendation.** The instructor agreed the chapter goes, and put the surviving material on the *training* explanation rather than at the opening of Chapter 10. That is the better call: the room reaches for the brain analogy the moment it hears *neural network* and *learns*, which is Chapter 1 slide 6, not Chapter 10. It now sits on Chapter 1 slide 7. Only the units point goes to Chapter 10, where the context window makes it usable. See `../DECISIONS.md`.

**Recommendation.** Demote to a ten-minute, three-slide segment. Its best home is the opening of
Chapter 10, where the memory gap is being filled and the point is live. Everything else goes to
an appendix and the reading list.

**Cross-reference to fix either way.** Chapter 8 states "Chapter 1 gave you the definition" of
attention. The rebuilt Chapter 1 does not define attention. I have added a definition to
Chapter 1 (one slide, one diagram, cited to Vaswani et al. 2017, which is `[V]` and whose §3.2
wording was read); if that slide is rejected, this sentence in Chapter 8 has to go.

---

## Chapter 9 — The agent

**Premise:** "It can now change your files, and the diff is where responsibility sits."

**Verdict: holds.** The best-shaped premise in Session 2.

**Useful.** Graphical entry points before terminal ones, which is the right call for this room and
correctly justified — a terminal-first course filters for people who already have the tool. The
permission model. Plan before edit, with the cost asymmetry stated. Context engineering named as
the skill rather than a footnote. Compact, clear, abandon, and the observation that people will
not abandon. The contamination demonstration labelled as an illustration rather than a
measurement, because six runs is under the floor Chapter 4 set.

**Useless.** Nothing significant.

**Missing.** The recovery path. See A6. The chapter teaches "read the diff before you approve it"
and never teaches what to do about a diff you approved and should not have. Undo, revert, and
the fact that an unversioned directory has no recovery path at all. For a room with rare terminal
experience this is the gap that will cost somebody real work, and it is a ten-minute fix.

---

## Chapter 10 — Memory

**Premise:** "You write the memory it does not have, as a file it reads every time."

**Verdict: holds.** Clean, and the artefact-of-the-day design is right — this is the only chapter
whose output the attendee still owns a month later.

**Useful.** What belongs and what does not, with the test ("would a competent new member of your
group need this told to them?"). Units, sign conventions and coordinate systems named as the
things the file exists for and the things a generated draft cannot infer. The hierarchy, and keys
excluded from it with the reason. Commands and skills as standing context that loads only when
needed. The closing refusal to rebuild the hippocampus analogy the course just broke.

**Useless.** The cost equation. `cost ∝ N_file × T_turns` is a proportionality whose constant
carries the currency, and the slide then immediately concedes that caching breaks the magnitude
and only the direction survives. It dresses a true and trivial statement — a longer file is
re-read every turn and you pay for it — as physics, in a course that spends Chapter 4 teaching
this room not to accept exactly that move. Say the sentence and drop the equation.

**Missing.** What happens when a personal and a project file disagree, which is the first thing
that will go wrong in a shared lab file. Also a figure: zero in twelve slides, and the hierarchy
is a diagram.

---

## Chapter 11 — Orchestration

**Premise:** "Delegating across several context windows — and when that is just an expensive way to do something simple."

**Verdict: half-true, and the premise is doing public relations for the content.** The second
clause is the honest half and it is the smaller half of the chapter.

The truthful premise for this audience: *most of this room should not use orchestration; here is
how to tell, and here is the one part that is worth it.*

**Useful.** Hooks — a convention that is enforced rather than requested is genuinely valuable to a
research group, and the repository contains a working example. The judgement-call slide, which is
the best slide in the chapter. The three ultracode traps, all of which are silent, and the refusal
to invent a cost multiplier that is not published.

**Useless for this room.** Subagent design, workflow authoring, and inspecting running work. This
is developer tooling for a five-person group on individual subscriptions, and the chapter itself
says orchestration is where those subscriptions actually get exhausted. Teaching the capability
that burns the limit, in the session where the limit is most likely to be hit, is a scheduling
problem as well as a content problem.

**Missing.** Nothing that should be added. This chapter should shrink to about fifteen minutes:
hooks, the judgement call, one demonstration on one directory.

---

## Chapter 12 — Extension

**Premise:** "Connecting outside tools, and the trust you spend to do it."

**Verdict: half-true.** The trust half is the chapter's reason to exist. The protocol half is
developer architecture that changes nothing this audience does.

**Useful.** Tools versus resources as Chapter 6's failure mode restated at an interface — an
action with consequences beside a thing that gets read, sharing one channel. The specification's
own statement that tool descriptions should be considered untrusted. The document-graph local
and remote split, established by running the tool at a pinned version rather than read off a
webpage, which is the factual basis for a Chapter 18 decision about confidential data.

**Useless.** The N-times-M interface-standard argument, and the client-side primitives slide that
names sampling, roots and elicitation and then says they are out of scope. A slide that announces
its own irrelevance should not be a slide.

**Missing.** The tool this room would actually connect — a reference manager. Chapter 14 needs it
and Chapter 12 never names one.

**One challenge to a locked decision, stated once.** `DECISIONS.md` locks cross-provider retrieval
as "a licensing asymmetry with a provenance obligation". Three points, then it is the instructor's
call and I will build whatever is decided:
1. Its central factual claim is unverified. The deck says so: the claim that a second provider is
   reachable from this session and returns sources the first cannot is exactly what the missing
   Antigravity configuration would establish. The course would be teaching a manoeuvre it has not
   established works.
2. In a course whose spine is citation discipline, a slide about obtaining sources one provider is
   not licensed to return will be remembered as a workaround whatever the framing. The framing
   survives a librarian; the room's memory of it may not.
3. The risk lands on the student, which is the reasoning `DECISIONS.md` already used to exclude
   paywall circumvention.

Recommendation: hold it as a facilitator note until the configuration exists and the claim is
verified.

---

## Chapter 13 — Access

**Premise:** "Keys, and what a call actually costs."

**Verdict: mis-scoped to the audience.** Most of this room will never hold an API key.
`DECISIONS.md` records that paid chat subscriptions exclude API access and that the hands-on runs
against a local gateway — so the chapter exists because a gateway exists, not because the need does.

**Useful.** Key hygiene is real and transferable; they will meet credentials in other contexts and
the four rules are correct. The price-list-to-architecture worked example is excellent teaching:
order-of-magnitude estimation from public numbers, dimensional analysis carrying the derivation,
and an independent check — and the check strains honestly rather than being made to succeed.
Local against frontier side by side is the best available demonstration of Chapter 5 on hardware
the group owns.

**Useless for this room.** The cost thread closing on batch discounts and subscription-versus-
per-token economics, for people who are on a fixed subscription and are not choosing.

**Missing, and this is the real gap.** What their actual plan gives them, what burns it, and what
to do when they hit the limit mid-afternoon. That is the cost question this room has. It appears
once, in passing, in Chapter 11, and no chapter owns it.

**One unresolved number.** The 1.7 kB-per-token sanity check openly does not know whether the
figure is per layer or whole model, and the deck says so. Teaching a worked example whose own
arithmetic is unresolved, three chapters after the unit-definition erratum was taught as the
anchor of the course's method chapter, is a risk the deck has already identified. Resolve it, or
keep the method and drop the number.

**Recommendation.** Re-aim the chapter at "what this costs you": subscription limits first, key
hygiene second, API third. Keep the worked example, because it teaches estimation rather than
pricing.

---

## Chapter 14 — Literature

**Premise:** "It fabricates citations, and resolving the identifier is the entire defence."

**Verdict: holds.** The tightest one-sentence premise in the spine, and the highest-demand
capability in the room.

**Useful.** Opening from the failure gallery, so the chapter starts from something the room has
already seen fail. The identifier as the field that matters and author-and-year as convenience.
Screening as a classification task with a defined answer, and therefore one of the few literature
tasks that can be measured — with a known subset screened first to get a false-negative rate,
which is Chapter 4's design wearing different clothes. Summarising without laundering, and the
instruction to keep the authors' hedge. The honest statement that the truthfulness thread closes
only for citations, because a fluent uncitable wrong sentence has no identifier to resolve.

**Useless.** Nothing.

**Missing.** Three things, and the first is large:
- **The correction in A3(b).** The extraction slide describes the wrong pipeline.
- **Understanding a paper**, which is the actual first use. Screening and summarising are covered;
  "explain this methods section and tell me what I would need to check" is not, and it is what
  they will do on Monday.
- **The search record.** This room writes literature reviews. Recorded search strings, databases,
  dates and result counts are what make screening defensible to a reviewer, and the chapter
  teaches the screening without the record.

---

## Chapter 15 — Production

**Premise:** "A versioned text pipeline beats a word processor when the document must be reproducible."

**Verdict: half-true, and the weakest premise in the course.**

Three problems:
1. **Four of seven slides are not about AI.** Markdown to a journal template, citation styles,
   cross-references and figure numbering would be identical in a course with no AI in it. This is
   document engineering smuggled in under an AI heading.
2. **The premise is contestable and the chapter does not meet the objection that kills it.** The
   stated cost is "a build step, and a day of setup". The real cost is that the supervisor and
   co-authors use a word processor with tracked changes, and ASCE accepts one. The people who
   must comment on the draft cannot. That is the reason adoption fails and it is not on a slide.
3. **It duplicates.** Figures from committed scripts and explaining your own code both belong to
   Chapter 16, which does them better.

**Useful.** Diagrams as text — genuinely useful, genuinely AI-assisted, and the thing this room
will actually adopt. Figures regenerated from a committed script. The refusal of generated
imagery on provenance grounds, which is well argued.

**Missing.** Figures, in the chapter that argues for text-generated diagrams. The deck states
"This chapter has no figures of its own", which is close to self-refuting.

**Recommendation.** Cut to about fifteen minutes, or fold into Chapters 14 and 16. If it survives
as a chapter, the premise has to be rewritten to name the collaboration cost.

---

## Chapter 16 — Code and numerics

**Premise:** "It is measurably weaker on MATLAB, and numerical correctness needs a check it cannot supply."

**Verdict: holds.** The closest chapter to the audience's daily work, and the one where the course
pays back.

**Useful.** Inherited code, with explanation bought before repair, and the explanation checked
against behaviour rather than against variable names. The MATLAB weakness shown live rather than
asserted, with the demonstrable gap and the corpus-composition hypothesis held apart — this is the
chapter obeying its own standard under pressure, and it is the cheapest credibility in the course.
"Runs" is not "agrees". Floating-point addition is not associative, so a vectorised rewrite can
change results wherever the summation order moved. Tolerance as a choice that must be justified.
Checks the physics supplies free: conservation, closure, symmetry, known limits, convergence.

**Useless.** Nothing.

**Missing.** Two things:
- **Their own experimental data** (finding A5). This is where it belongs.
- **The unresolved circularity in the testing slide.** The chapter says "a test the tool wrote and
  you did not read is not a test", which is correct and leaves the problem standing. Give the way
  out: a test written against a case with an independently known answer, or against a conservation
  law, is checkable without reading the test's logic.

**Recommendation.** This chapter should get longer. Time from Chapter 15.

---

## Chapter 17 — Critique

**Premise:** "Use it to attack your own argument before a referee does."

**Verdict: holds, and the chapter's real payload is buried.**

**Useful.** The harshest-defensible-report prompt with an evidence requirement attached to each
objection, so an objection with no stated remedy is discarded. The good-at and not-good-at split,
with ranking named as the part that stays yours. Rebuttal stress-testing against the failure of
answering a weaker version of the objection. The detection question taken from both sides and
answered the same way.

**Buried.** Language support and the disclosure boundary is one slide in the middle. For a group
where English is a second language for several people, this is plausibly the highest-frequency
benefit in the entire course, and it sits between two slides about referee reports. Promote it,
and give it the room to say where the boundary actually is.

**Missing.** The reverse direction: using the tool to check whether **you** have understood a
referee's objection, which is where a non-native reader actually loses points, and which is a
different task from drafting the reply.

---

## Chapter 18 — Governance

**Premise:** "What you must disclose, what must never leave the building, and what you must log."

**Verdict: holds.** Well structured for a chapter blocked on missing inputs, and the block is
correctly identified as one only the instructor can clear.

**Useful.** The four questions to put to a policy rather than four answers, which is the right
design because policies change and secondhand summaries go stale invisibly. Why a tool cannot be
an author, argued from what the word means rather than from squeamishness — the best argument in
the chapter, and the only slide in the section that needs no policy. The data rule written before
it is needed, because a rule decided under deadline pressure is decided in favour of the deadline.
The reproducibility log. The inbound half of the trust boundary, which the chapter correctly
identifies as the half people forget.

**Useless.** Nothing.

**Missing.** The student-facing half. A PhD student's binding rule is their university's and their
funder's, not a journal's: thesis regulations, examination boards, what a viva examiner may ask,
and what the doctoral school requires to be declared. The chapter looks only at journals and
publishers. For an audience of PhD researchers that is the wrong first ring.

---

## Chapter 19 — Judgement

**Premise:** "Five situations where the right move is to put the tool down."

**Verdict: not a chapter.** The brief itself says "one slide, held in the head". It is one slide,
a sixty-minute capstone and a round-robin. That is a closing session, and numbering it as the
nineteenth chapter of nineteen overstates the course's shape.

**Useful.** The five tests are well derived, and the derivation slide is the good part: each test
traced to the chapter that establishes it, with the novel-derivation test corrected away from the
naive version (prediction over a corpus plainly produces sentences that were never in it; the real
argument is data density). The fifth test, added because the other four all govern what goes out
and none catches what comes in, is a genuine catch.

The capstone is the most valuable hour in Session 3, because it is the only time the room does
end-to-end work with the instructor present. Its stated check — at the end you can name what you
verified, how, and what you could not — is the right criterion.

**Useless.** The framing as a chapter, which costs the capstone room.

**Missing.** Nothing.

**One prose item.** "That is the trade you have actually made this term" is one of the handover's
own cited examples of a banned construction, still in place on the final slide of the course.

---

# Part C — what changes in the spine

Summarised; the file itself is updated.

| # | Change | Reason |
|---|---|---|
| 1 | Chapter 1 premise names the object before the operation | Premise presupposed its own subject |
| 1 | Delete "opens with: is this like a brain?" from the brief | The device the instructor rejected |
| 2 | Adopt the 2a/2b split; trim three slides from the pipeline half | Overrun, and two of the three feed a chapter being cut |
| 4 | The room runs the eval | Method taught as a spectator sport |
| 5 | Long-context to two slides, interpretability to one | Three chapters under one number |
| 6 | Move to the opening of Session 2 | Satisfies "6 before Part III" and relieves Session 1 |
| 7 | Halve, and move to Session 2 before Chapter 13 | Twice its justified size; pairs physical cost with billed cost |
| 8 | Demote to a three-slide segment opening Chapter 10 | Answers a question this room does not need answered |
| 11 | Halve — hooks and the judgement call | Developer tooling that burns the room's usage limit |
| 12 | Cut the protocol half; hold cross-provider retrieval | Architecture that changes nothing; unverified claim |
| 13 | Re-aim at subscription limits first, keys second, API third | Most of the room will never hold a key |
| 15 | Halve or fold into 14 and 16 | Weakest premise; largely not about AI |
| 16 | Expand to absorb experimental data analysis | The largest content gap, and this is its home |
| 17 | Promote language support to the front | Highest-frequency benefit, currently buried mid-chapter |
| 19 | Rename to Close; give the capstone its time | One slide plus a capstone is not a chapter |
| new | Image and file input | Absent from all nineteen chapters |
| new | Version control, and recovery from a bad edit | Assumed by four chapters, taught by none |

---

# Part D — what I did not do

- **I did not renumber anything.** `architecture.md` references chapters by number in five places
  and `CLAUDE.md` forbids renumbering without updating the thread map. Every recommendation above
  preserves the existing numbers, including the 2a/2b split, which is why that split is the right
  one.
- **I did not rewrite chapters 2 to 19.** `HANDOFF.md` §10 says to stop after the first chapter for
  the instructor's verdict, and the user's instruction repeats it.
- **I did not verify the sources in Chapters 5, 7, 8 or 14 against their originals.** The review
  above judges premises, scope and audience fit. Where I say a chapter's scholarship is good, that
  is a judgement of how the evidence is presented and qualified, not an independent replication of
  the reading. Three chapters carry `TODO(verify)` markers that are still open.
- **I did not resolve the Chapter 13 per-layer-versus-whole-model question.** It needs the Pope
  transcript re-read, which I did not do.
- **I did not check whether the Chapter 4 sign-test arithmetic is correct.** The numbers are
  internally consistent and correctly reasoned as presented; I did not recompute the exact
  binomial tail probabilities or the 103-case power figure. They should be recomputed before
  delivery, because that chapter's credibility rests on them being exactly right.
- **I did not estimate delivery times from a rehearsal.** The timings in A1 are from a
  slides-and-exercises model, not from anyone speaking. They are good enough to establish the
  direction and size of the overrun and not good enough to plan a run-sheet from.
- **I did not touch `chapter-briefs.md`.** Several recommendations above contradict it. The briefs
  should be corrected once the instructor rules on the recommendations, not before.

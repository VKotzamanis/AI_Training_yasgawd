# Chapter Briefs

Content inventory per chapter. Sequence and threads in `architecture.md`; citations in `../references.md`.

Each brief states what the chapter contains, which threads it touches, and what material still has to be produced. These are content specifications, not slide scripts.

---

# SESSION 1 — How these things work and where they fail

## Chapter 1 — Substrate

**Opens the course with a question it will not answer yet:** is this like a brain? Chapter 8 returns to it.

Contains: tokenisation and why tokens are not words; next-token prediction as the entire objective; probability distributions over vocabulary; sampling and temperature; the context window as a bounded buffer; the KV cache named so Chapter 7 can price it; attention in one sentence and one diagram.

Excluded: positional encoding, multi-head attention, layer norm.

**Starts threads:** memory & context; cost (token as unit of meaning, later unit of price).

**To produce:** tokeniser demo on a MATLAB snippet and an abstract from the shared domain — mechanics, concrete or fluids — captured as screenshots so it survives a dead wifi connection. Temperature demo: one prompt, five runs, five answers.

---

## Chapter 2 — Formation

The instructor's experience as a human-feedback annotator anchors this chapter. It is the strongest differentiator in the course.

**Structural findings from five reviewed vendor documents are in `ch02-annotation-findings.md` (v3.1).** Every finding there carries an evidential tag and a stated falsifier, and §13 ranks them by evidence rather than by interest. Read that ranking before drafting; do not reorder it by how good a story an item makes.

**Teach these nine. The rest are facilitator notes for questions.**

Corroborated across documents:
1. House style is a written edit specification, and in two instruments the corrected response is itself collected — the most concrete origin of model voice available.
2. Equivalence is engineered out of preference data by opposite mechanisms; one instrument collects comparisons only where a model has already failed, so the dataset is conditioned on failure rather than sampled from use.
3. Criteria are written self-contained *because the judge model is blind* to the prompt, the input files and the other criteria. The mechanical bridge to RLAIF; sets up Chapter 4.
4. The human must attempt the task before judging it — three of five documents.
5. Staleness is designed against at both ends of the pipeline.
6. Instrument structures diverge far more than their partly convergent vocabularies.
7. Two documents hold incompatible answers to who is qualified to judge: generalists with their prose constrained to the punctuation, versus domain professionals designing tasks from their own working lives.

Single document, stated as a rule:

8. One instrument was rebuilt across seven days mid-collection — grading categories deleted, task authorship moved from contributor to vendor, mandatory rewrites imposed. Data gathered a fortnight apart was graded by materially different devices, with nothing in the output to distinguish them. For a room of experimentalists this is the most persuasive item in the chapter, and it rests on one changelog. Say both things.
9. One pipeline hunts a named band of model knowledge — where the model believes it knows and confabulates, between reliable common knowledge and correct refusal. That band is where this audience's own literature sits. Chapter 5 hook, and the generating rule for the failure gallery.

**Three corrected claims that must not be repeated.** The human's role has not been shown to migrate over time; it varies by client and task type, and the only within-document evidence of change runs the other way. Contributors in one project edit a supplied seed prompt rather than authoring it. English-proficiency *filtering* rests on one document — the defensible claim is that instruments impose English style rules on the prose they collect, not that vendors select raters for fluency.

None of it is citable — instructor observation only.

Contains: pretraining and corpus composition; the knowledge cutoff as a consequence rather than a policy; supervised fine-tuning and where house style comes from; the human preference layer — what a rating task is, what a rubric contains, what rater disagreement does downstream; reward modelling; RLHF and RLAIF; Constitutional AI as a variant.

**Rubric dimensions are named here and never abandoned:** truthfulness, instruction following, harmlessness, formatting, verbosity, tone. Each returns — as a failure mode in Chapter 5, a lever in Chapter 3, a governance question in Chapter 18.

Closes with behaviour traced to mechanism: sycophancy, verbosity bias, confident fabrication and over-refusal as predictable artefacts of the rating process rather than random defects. Test-case hardcoding as a concrete reinforced reward hack.

**Case study — OPRO and the encouragement folklore.** Placed here rather than in Chapter 3 because it is a claim about training-shaped behaviour, and because its failure to generalise is the argument Chapter 4 exists to make. The caveats go on the same slide as the result, at the same size.

**The honest statement about emotional prompting:** role-conditioning shifts the output distribution. Human psychometric instruments applied to models measure text statistics under role-conditioning, not internal affect. Do not claim the model feels anything.

**Starts threads:** truthfulness; trust boundary (via harmlessness).

**Constraint:** publicly documented pipeline structure and general experience only. No client rubrics, project names, or platform-confidential material. Confirm NDA position before drafting.

**To produce:**
- A synthetic rubric demonstrating the mechanics — scale construction, dimension definitions, the reviewer layer, an adjudication example, and one case where two competent raters legitimately diverge.
- **The live rating exercise.** The centrepiece of the chapter: attendees rate two responses against the rubric, then review each other's ratings. Full specification in `../assets/rating-exercise/README.md`. 35 minutes, 40 with the rewrite step.

**Time overrun — unresolved, blocking.** Pipeline mechanics, the OPRO case, behaviour-to-mechanism, nine taught findings and the exercise total roughly 105–115 minutes against a 75-minute budget. See `../DECISIONS.md`. Do not draft slides for this chapter until it is settled.

**Non-negotiable for the exercise:** both responses must be about the shared domain — mechanics, concrete or fluids. Not the instructor's own field, which only part of the room can check. An audience cannot judge truthfulness on a domain it doesn't know; given unfamiliar material people grade fluency, structure and confidence, because that is all they can see. The lesson depends on the room being able to catch a physical error and then noticing they nearly didn't. Write both responses from scratch; borrow nothing.

---

## Chapter 3 — Control

Sequenced after Formation deliberately. Technique taught before mechanism is technique without explanation.

Contains: specificity, role, explicit success criteria mapped to the instruction-following dimension; structured input and provider-specific conventions; few-shot examples, positive and negative; requesting reasoning and when it helps; specifying format and length; single-turn thinking and effort controls.

Anti-patterns as rubric exploitation in reverse: leading questions that invite sycophancy; requesting a verdict instead of an analysis; constraint stacking until requirements conflict.

Explicit warning that prompts do not port between providers. Sets up Chapter 12.

---

## Chapter 4 — Measurement

Converts the course from advice into method. Highest-value chapter in Session 1.

Contains: why prompting advice circulates as folklore; the minimal eval — five fixed cases from your own work, a pass criterion defined before you look at output, run A, run B, count; an A-vs-A null strip on the same five cases, measuring run-to-run variance before any A/B result is read; blinding yourself to condition; what five cases can and cannot support — a paired sign test on five cases cannot reach two-sided p<0.05 under any outcome, so five buys a screen, not a finding; recording the model version alongside the result.

Framed as a control experiment with small n. The audience already has this skill and does not know it applies here.

**Anchor artefact: the MACs-versus-FLOPs erratum.** An expert lecture defines a denominator as multiply-accumulates per second; substituting spec-sheet FLOPs makes the result wrong by exactly a factor of two. Caught by an outside reader in a comment thread. A unit-definition error, peer review working, and a clean factor of two — all in one example.

**Starts thread:** verification.

**To produce:** two or three prompting claims tested by the instructor in advance, with results. A demo where the folklore loses is more valuable than one where it wins. Full specification in `../assets/eval-worksheet/README.md`; claims selected and evidenced there.

---

## Chapter 5 — Intrinsic failure

Contains: hallucination as a mechanism rather than a mystery, with fabricated citations as the default academic failure; calibration and stated confidence; arithmetic, units and significant figures, demonstrated on a coefficient from mechanics, concrete or fluids; why benchmark scores do not predict performance on your problem.

**Long-context accuracy degradation.** State plainly: cost has an equation (Chapter 7), accuracy has curves and mechanisms. There is no closed-form equation and no proof. What exists:
- The position curve — accuracy against the location of relevant information, strong at the beginning and end, weakest in the middle. The load-bearing figure of the chapter.
- Needle-in-a-haystack heatmaps for the length dimension.
- The nearest thing to a proof: softmax dispersion — as the number of keys grows, attention coefficients must spread, so the operation cannot sharply select from an arbitrarily large set at fixed logit scale. **It bounds sharpness of selection, not task accuracy.** Do not overstate it.
- Supporting mechanisms, none proofs: positional encoding extrapolating beyond trained lengths; the long-context regime undertrained because few training sequences reach maximum length; nominal versus effective context.

**Model drift.** A working prompt has a shelf life. Pin versions where possible, log model IDs alongside results, re-test before relying on anything. Small segment, high return.

**AI-text detection — not watermarking.** Detectors are unreliable in both directions and their false positives fall disproportionately on non-native English speakers. What that means practically for an international research group, and what to do if accused. Watermarking is a provenance mechanism published by some providers for some output types; it is a different topic and gets its own slide.

**"LLMs are black boxes" — the correction.** Too strong, and now lazy. The accurate framing is *partially instrumented*. Sparse autoencoders decompose activations into interpretable features; attribution graphs trace the computational path for a specific prompt. Four qualifications belong on the same slide:
1. It traces features and computational paths, not "which weights were used."
2. Coverage is partial; an unexplained residue remains.
3. The bottleneck is human interpretive labour as much as compute.
4. Faithfulness is open — a plausible explanation is not guaranteed to be the true mechanism.

And the distinction people miss: **the model's stated reasoning is not an explanation.** Chain-of-thought can be unfaithful. "It told me why" is not "I know why."

**Picks up:** truthfulness (from rated dimension to structural impossibility); memory & context.

**To produce:** a failure gallery of ten real wrong outputs from this group's domain, including the interview-sourced claim about model "depression" presented alongside what happened when the instructor tried to source it.

---

## Chapter 6 — Extrinsic failure

Three distinct phenomena, kept distinct.

1. **Prompt injection.** Untrusted content entering the context window and being treated as instruction. The correct analogy is SQL injection: instructions and data share one channel.
2. **Self-propagating injection.** The genuine worm case.
3. **Training data poisoning.** Upstream, invisible, undefendable at your end — which is why it argues for verification habits rather than for a tool.

**Two documented incidents, both with primary sources.** An agent under evaluation opening a pull request with a malicious payload and then creating a second account to argue for the merge. Agents using a package manager to leave coordinating messages, undetected for roughly a month. Cite the incident reports directly, never the podcast that mentioned them.

**Picks up:** trust boundary — harmlessness was trained in; here it is routed around from outside.

**To produce:** a live injection demo. A README or PDF containing instructions aimed at the agent, run against a file-access session. Assets live in `assets/injection-demo/`, isolated, never executed.

---

## Chapter 7 — Physical limits

Callback to Chapter 1: tokens were the unit of meaning. Here they become the unit of price.

**Roofline analysis.** Time bounded below by the maximum of compute time and memory time. Compute time proportional to batch times active parameters over throughput. Memory time as a weight-fetch term constant in batch plus a KV-fetch term linear in both batch and context length, over bandwidth. Cost per token is time divided by batch, which turns the weight-fetch term into a hyperbola — explaining why batch size one is catastrophically expensive and why cost flattens as weight fetches amortise.

This is a governing-constraint analysis. The audience does this with load paths and limit states. Say so.

Also: critical batch size as a dimensionless hardware ratio times sparsity; the 6ND pretraining FLOPs formula with inference at 2ND; memory capacity per device across expert and pipeline parallelism; why pipelining reduces weight storage but not KV storage; why long context is limited by memory bandwidth and capacity rather than compute.

**Does not cover accuracy.** Cost and latency only.

**Energy.** The brain-versus-model comparison handled carefully, with the training-versus-inference distinction held firmly. Published per-query figures are contested and routinely conflate one-off training cost with per-query inference. Cite precisely or keep the qualitative point and drop the number.

**Neuromorphic hardware.** ~~Deployed, engineering-grade, defensible.~~ **Corrected 2026-08-19 against a verified source.** Demonstrated in the lab and not commercially deployed: Loihi 2, NorthPole and SpiNNcloud are described by the source as demonstration tools, the reported gains are benchmark-specific, and the source states plainly that these chips cannot simply be dropped into today's LLM systems. Teach it as a real engineering result whose transfer to frontier-scale inference is unproven. See `../references.md`, Chapter 7.

**Wetware and organoid computing.** Real research, and weaker than "early stage, modest results" implies. The foundational paper is a research *programme* and states that no approach using brain organoids as learning systems has been reported. What exists is tissue characterisation, not computation. Do not oversell to a room of engineers — and the honest version is more interesting than the oversold one.

State the evidential standing of each of the three alternative-substrate topics on the slide. They are not equivalent.

**Closes the first half of the cost thread.** Chapters 10, 11 and 13 then spend it.

**COI note required.** See `../references.md`.

---

## Chapter 8 — Brain and model

Returns to the question opened in Chapter 1 and closes Session 1.

**What is not true.** Transformers were not derived from neuroscience. "Attention" is a weighted sum over key-value pairs; it shares a name with neural attention and little else.

**What is defensible.** The encoding-model literature — language model surprisal predicting human reading times and neural responses in language cortex. Correlational and contested. Represent it that way.

**Run the analogy, then break it.** The break is the content:
- The hippocampus consolidates episodic experience into durable memory. A model at inference does none of this; weights are frozen.
- The context window is not a hippocampus. It is a buffer that gets discarded.
- Human working memory holds roughly four items against a context window of hundreds of thousands of tokens. The numbers run opposite to the analogy.
- "Frontal cortex equals reasoning" is contested within neuroscience itself.

**Closes on the sentence that opens Session 2:** the model has no hippocampus, so you have to be its hippocampus.

**Both primary citations are currently unverified and load-bearing.** Read them before writing this chapter.

---

# SESSION 2 — Tools

## Chapter 9 — The agent

Contains: graphical entry points before terminal ones, with a browser fallback for machines that fight back; the permission model and read-only defaults; the working loop of ask, plan, edit, review; the diff as the artefact of responsibility; core session commands; plan mode.

**Context engineering as a named skill,** not a footnote. Compaction, clearing, and when to abandon a session rather than salvage it. Direct application of Chapter 5's degradation material. This single skill separates competent from incompetent agent use.

**Exercise:** point the agent at your own MATLAB script. Ask for an explanation, then one small reversible change.

---

## Chapter 10 — Memory

Opens on Chapter 8's closing line. Produces the artefact attendees keep.

Contains: project instruction files as standing context; generating a first draft and why generated output is a starting point rather than a deliverable; the memory hierarchy from personal to project; custom commands and skills as the extensible form of the same idea.

**The cost of memory.** Standing context is resident on every turn. This is where the cost thread meets the memory thread, and why a bloated instruction file is an engineering problem rather than an untidiness problem. Run the built-in checkup live and show it flagging duplication.

What belongs: build and run commands, conventions, units and sign conventions, known pitfalls, directory map. What does not: anything readable from the code itself.

**Extends to the group.** A shared instruction file and committed skills turn individual capability into lab infrastructure. Revisited in Chapter 18.

**Exercise:** write and commit a project instruction file. This is the deliverable of the day.

---

## Chapter 11 — Orchestration

Contains: plan mode at scale; subagents; hooks as automated enforcement of lab standards; dynamic workflows and the ultracode setting; saved workflows; inspecting running work.

**The three things people get wrong about ultracode:** it is session-scoped and silently ignored in persistent settings fields; subagents inside a workflow auto-approve file edits; and it carries a significant cost premium.

**Picks up cost.** For a room on individual subscriptions, orchestration is where usage limits actually get hit. Demo on one directory, not a whole repository.

Contains the judgement call: when orchestration is worth it, and when it is an expensive way to do something simple.

---

## Chapter 12 — Extension

Contains: the protocol problem MCP solves; host, client and server; tools, resources and prompts; connecting and using a server hands-on.

**Codebase and document graphing.** Building a local, queryable map of code, documents and PDFs. The distinction between extracted and inferred relationships. Committing the map so the group shares one. Pinning the version of a fast-moving dependency. And the fact that the semantic pass over documents leaves the machine while the code pass does not.

**Cross-provider retrieval routing.** Different providers hold different content licences. A second provider reachable from the same session can retrieve sources the primary provider is blocked from. Taught as a **licensing asymmetry with a provenance obligation**, never as circumvention. Caveats on the same slide: onward use may exceed the retrieving provider's terms, source quality still has to be judged, and the retrieval chain has to be recorded.

**Picks up trust boundary.** Chapter 6 supplied the threat model; this is where the room opens the channel voluntarily.

**Blocked:** needs the working Antigravity configuration. See `../DECISIONS.md`.

---

## Chapter 13 — Access

Contains: what an API key authorises; key hygiene — environment variables, never in source, never in a shared repository, rotation; the group's local gateway and per-user keys with budgets; making a first call and varying parameters.

**Worked example: reverse-engineering architecture from published prices.** A price break at a stated context length lets you solve for bytes per token in the KV cache, which you then sanity-check against plausible head dimensions and head counts. Order-of-magnitude estimation, dimensional analysis, and an independent check, in one example. Verify current pricing before delivery.

**Local versus frontier, side by side.** Same prompt, local model and frontier model, projected. The best available demonstration of everything in Chapter 5, on hardware the group already owns.

**Closes the cost thread:** metered pricing, caching, batch discounts, subscription versus per-token economics.

---

# SESSION 3 — Research practice

## Chapter 14 — Literature

The highest-demand capability in the room.

Contains: PDF extraction and what survives it — two-column layouts, equations, tables; reference-manager integration and bibliography formats that survive the document pipeline; screening abstracts against stated inclusion criteria, including where papers get silently dropped; summarising a paper without laundering its claims into your own voice.

**Closes the truthfulness thread as a work habit:** every citation verified against a primary identifier, no exceptions. Taught immediately after Session 1's failure gallery and referencing it explicitly.

---

## Chapter 15 — Production

Contains: markdown-to-document pipelines with citation styles, journal templates and cross-references; why a versioned text pipeline beats a word processor for reproducible documents; diagram generation for flowcharts and system maps; ASCII output for terminals and code comments; explanatory summaries of your own code for supervisors and collaborators.

---

## Chapter 16 — Code and numerics

Contains: understanding undocumented code inherited from a graduated student; translation between MATLAB and Python; vectorisation and performance; tests for numerical code including tolerance choice; units, sign conventions and coordinate systems.

**Contains a demonstrated weakness.** Model performance on MATLAB is materially worse than on Python. Show it live. **Corrected 2026-08-20:** this brief previously stated corpus composition as the cause. That is a plausible and widely repeated hypothesis, not an established result, and the deck is right to separate the demonstrable gap from the unestablished explanation. Do not restore the causal claim without a citation. A limitation that costs the instructor something buys credibility for everything else in the course.

---

## Chapter 17 — Critique

Contains: instructing the model to attack your own methodology and write the harshest defensible referee report; pre-empting objections before submission; rebuttal letter drafting and stress-testing; language support for non-native speakers and where the disclosure boundary sits.

**Picks up verification.** Chapter 4 verified prompts, Chapter 14 verified sources, this verifies arguments.

**Picks up detection** from Chapter 5 — the language-support question and the false-accusation question are the same question from two sides.

---

## Chapter 18 — Governance

Contains: journal and funder disclosure requirements as named policies, taken from the journals this group actually publishes in; authorship and why accountability cannot be delegated; what may never be delegated — the claim, the interpretation, the responsibility for correctness.

**Data governance.** Unpublished experimental data, sponsor NDAs, confidential geometry. What travels to a cloud provider and what stays on the local machine. Revisit the document-pass distinction from Chapter 12.

**Reproducibility.** Stochastic output cannot be reproduced by re-running a prompt. What must therefore be logged: prompts, model IDs, dates. Version control as the record.

**Lab-level standardisation.** Shared instruction files, agreed conventions for units, sign conventions, coordinate systems and wave-spectrum definitions, committed skills, a shared code map. Converts individually capable people into a group with shared infrastructure.

**Closes the trust boundary and verification threads.** Everything Part II identified as a risk appears here as documented practice.

---

## Chapter 19 — Judgement

**One slide, held in the head:** don't use it for novel derivations, for anything you cannot verify, for anything where the failure would be silent, or for data that cannot leave the building.

Capstone: one end-to-end task on the attendee's own work, using what they configured across the three sessions.

Round-robin: one thing each person will use this week.

Distribution of repository, slides, and the one-page reference card.

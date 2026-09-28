# Annotation Practice — Extracted Findings

**Version:** 3.1 (two further documents reviewed at v3; v3's own extraction errors corrected here — see §0.5 and §0.6)
**Feeds:** Chapter 2 (Formation), with hooks into Chapters 1, 4 and 5.
**Status:** Five documents reviewed. Documents D and E added at v3.

---

## Sourcing rules

**Nothing here is citable.** Structural observations from contractor documents. They inform what the instructor teaches from experience; they never appear as a citation.

**Never reproduce:** document text, branded material, project code names, domain-specific example criteria, or screenshots. Documents are referred to by letter only. No worked example from any document — the prompts, the rubric rows, the banned-phrase lists, the fictional personas — is reproduced here or on a slide. Where a mechanism has to be shown, it is rebuilt from scratch on this group's own domain.

**Personal data.** One earlier document carries a third party's email address watermarked on every page. It must not appear in any file, slide or image. Documents D and E carry no watermark visible in the extracted text, but both contain named individuals inside fictional worked examples; those names are not reproduced either.

**Provenance caveat, new in v3.** D and E were obtained as re-hosted copies from a document-sharing site, not from the vendor. Provenance is therefore unverified: the vendor, the client, and the completeness of each document are all unknown. This does not affect structural observations — the instrument is what it is — but it rules out any claim about *who* commissioned what, and weakens comparison between documents further still. See §0.

**How to present:** as the instructor's observation of how annotation work is structured in industry, alongside the published guidelines in `../references.md` for anything requiring a citation.

---

## Evidential strength scale

Every finding below carries a tag and a falsifier. The tag describes the evidence, not the interest.

| Tag | Meaning |
|---|---|
| **[E1]** | Stated explicitly and unambiguously in **two or more** documents that appear to be independent |
| **[E2]** | Stated explicitly and unambiguously in **one** document |
| **[E3]** | **Inferred** from document structure; no document states it |
| **[E4]** | **Hypothesis.** Not supported by current evidence; retained only because it is testable |

A finding tagged [E1] is still five documents of unknown provenance. None of this is a sample.

---

## 0. Corrections to versions 2 and 3

### 0.1 The §7 role-migration hypothesis is dead. Do not revive it.

V2 demoted the 2024→2025 "rater becomes adversary while grading automates" arc to a hypothesis and named its falsifier: a late-dated project still using human Likert grading. That specific falsifier did not appear. The hypothesis failed anyway, by two routes v2 did not anticipate.

**First: Document D is the earliest firmly dated document in the set — September 2024 — and it is already adversarial.** Its core loop requires the contributor to iterate on a task until at least one model response contains a failure, and to discard cases where both responses are good. The same contributor rates both responses, justifies each dimension, justifies the preference, and rewrites the winning response into a corrected target. Adversarial task design, rating, and ideal-response production sit in one job, at the earliest date available. The arc claimed those were successive phases. They are simultaneous, and the supposedly late behaviours appear first.

**Second, and stronger: the only within-document evidence of change in the entire set runs the wrong way.** D's changelog records a rule imposed on 11 September 2024 requiring contributors to begin from a prompt written by the vendor's in-house prompt engineers, where previously they had written their own. That is one vendor, one client, one project, two moments — the only genuine before-and-after available anywhere in five documents. At the single point where change is observable, the human's authorship of the task *decreases*. §7 has the human moving from rater toward author. The one documented transition moves the other way.

**What survives is narrower and still unverified:** automated grading may be more common in later projects. Two documents use model judges (C and E); three use human graders (A, B, D); the one firmly dated document is an early human-grading project. That is consistent with the claim and equally consistent with "some clients buy judge infrastructure and some buy judgements."

**The methodological point, so this stops being re-litigated.** Five documents from unknown vendors serving unknown clients on five different job types cannot support a temporal claim, however many more are added. A time series requires the same vendor and the same client at two moments — which is precisely why D's changelog matters and why it is the only such evidence here. **The honest finding is the one v2 already wrote down: the human's role varies enormously by client and task type, and no single description of "the annotator" is accurate.** That is now the finding, not the fallback. Tagged [E1] and stated at §7.

### 0.2 Three v2 findings were generalised from one instrument and did not recur

V2 presented these as features of real instruments. Each appears in exactly one of five documents. They remain interesting; they are not industry practice, and the live exercise must stop implying they are.

- **Non-directional rating axis** (a descriptive spectrum where a high score is not a good score) — B only. D's dimensions are all directional. E has no rating axes at all; its non-directional element is a classification label the author must assign correctly, which is a different mechanism.
- **Adjacent-band disagreement tolerated in QC** — C only. Neither new document contains an audit tolerance rule of any kind.
- **Minimum citation count per task** — A only. Source-*quality* standards recur strongly (§8.1); a required *count* does not.

### 0.3 "Instrument vocabularies share almost nothing" was too strong

V2 said two instruments rating free-text quality shared almost no vocabulary. With five documents there is partial convergence: an instruction-following dimension or category appears in three, and a truthfulness or accuracy dimension in three. The divergence is real but sits in the *rest* of the instrument — what else is measured, at what granularity, and under what weighting scheme. Restated at §1.

### 0.4 §2 gained no corroboration and drops in the ranking

Score-versus-rationale mismatch was v2's anchor. Neither new document lists it among reviewer-caught errors. It stays [E2], n=1, and it now ranks below several findings stated directly rather than inferred from an error list. Its teaching value is unchanged and its position in the chapter's argument is unchanged; its evidential rank is not. See §2 and §10.

### 0.5 V3 wrongly credited Document D's contributors with authoring the prompt

V3 stated in §0.1 and in the §1 role table that D's contributor writes the prompt. They do not. The prompt is supplied inside the task by the vendor's in-house prompt engineers, and the contributor must start from it; light editing is permitted only where the seed prompt fails to break a model or is unusably obscure. The error came from reading a workflow step labelled as prompt writing and supplying the obvious meaning rather than the stated one.

The correction matters twice over. It removes prompt authorship from D's job description, which changes the §1 table. And it surfaces the changelog entry that imposed the rule — the only within-document temporal evidence in the set, and the second reason §7 fails (§0.1).

### 0.6 V3 overstated the target-artifact finding by conflating two things

V3 ranked "the human produces the target artifact, not only a judgement" as [E1] across three of five documents, and implied throughout that the artifact becomes training data. Two claims were welded together and they carry different evidence.

- **The labour recurs.** [E1], three of five. A produces an ideal response; D produces a corrected response; E produces a worked deliverable.
- **The artifact entering the data does not.** [E2]. D collects the corrected response. E states plainly that its worked deliverable is *not* trained on — its stated function is to sharpen the author's judgement before they write the rubric.

Split at §5.1. The teaching claim about where model voice comes from rests on D and A, not on E.

### 0.7 Document dating

Dated from internal evidence only, never from filenames.

- **Document D — September 2024. Firm.** Carries a changelog with three dated entries across a single week in September 2024. Corroborated by a stated model knowledge cutoff of end-2023 and by an anime-release example consistent with mid-2024.
- **Document E — 2025 or later. Weak.** No changelog, no timestamps. Dating rests on worked examples treating 2025 as actual and 2026 as projected, and on a scenario deliverable dated 2026. Authors can write speculative dates, so this is a soft lower bound. E is later than D with reasonable confidence; by how much is unknown.

---

## 1. Instruments differ, and the divergence is in structure more than vocabulary

**[E1].** Falsified by: two documents from different clients using the same dimension set at the same granularity under the same scoring rule.

| | A: hiring assessment | B: code project | C: expert rubric project | D: conversational IF project | E: professional task project |
|---|---|---|---|---|---|
| Dating | unknown | unknown | unknown | Sept 2024, firm | ≥2025, weak |
| Rating structure | ~6 categorical dimensions | 5 dimensions, 1–5 | binary weighted criteria | 3 dimensions, 3 bands + N/A | binary weighted criteria, per task |
| Criteria count | fixed set | fixed set | 30 minimum, author-written | fixed set | ~100 in the worked example |
| Preference scale | 7-point, includes "unsure" | 6-point, tie impossible | none | 5-point, tie expressible but not collectable | none |
| Who grades | human | human | two LLM judges | human | one LLM judge |
| Human also produces | ideal response | two justifications | prompt and full rubric | per-dimension and preference justifications, corrected response; edits a supplied seed prompt but does not author it | prompt, input files, target deliverable, full rubric |
| Objective | assess the rater | improve code answers | make the model fail | make the model fail, then repair it | make the model fail, then define passing |

**What survives peer review.** Instruction following appears in three instruments and truthfulness or accuracy in three, so the vocabulary is not arbitrary. Everything around it is: rating granularity ranges from three bands to a hundred binary checks; weighting ranges from unweighted dimensions to signed hundred-point scales; scope shifts, so that the same word is a headline dimension in one instrument and one category label among several in another.

**Teaching value.** An audience that has heard "trained on human preferences" assumes one well-defined instrument. Five real ones, converging on two or three words and diverging on everything else, dismantles that — and the partial convergence makes the point more credible than v2's strong version did.

---

## 2. Humans produce scores and rationales that contradict each other

**[E2], n=1, uncorroborated after two further documents.** Falsified by: nothing yet. Corroborated by: any further error list naming the same failure. The two documents reviewed since v2 do not.

One document lists, among errors reviewers most often catch, a side-by-side score contradicting its written justification, and dimension scores contradicting their stated reasoning. Presented as routine, recurring failures.

**What this means.** The rating and the explanation are produced by different processes; the rationale is at least partly constructed after the decision.

**What v3 adds — a weaker cousin, not corroboration.** Document E names two criterion-authoring errors of the same shape: a weight that does not match the importance the author's own rationale asserts, and a classification label contradicting what the criterion actually tests. Both are numeric-or-categorical assignments contradicting adjacent prose; both are listed as things to audit for. This is the same phenomenon one layer up, in rubric authoring rather than response rating. It is a real observation and it is *not* the same claim, so it does not upgrade §2.

**A second, genuinely new observation, [E2] from D.** That instrument collects a rater self-report of confidence after each task, with an option meaning, in effect, *unsure because this was a subjective judgement call*. The pipeline instruments its own uncertainty and stores it beside the rating. Worth saying plainly: the vendor knew a fraction of the ratings were coin-flips and chose to record which ones.

**Where it goes.** Unchanged. Chapter 5 teaches that a model's stated reasoning is not necessarily the cause of its output; this is the human version, in the data that shaped the model. Say it in this order: humans do it, the vendors knew, the behaviour is in the training data, the model does it too. **Present the incidence as unmeasured** — an error list and a confidence checkbox are not a rate.

---

## 3. Pointwise and pairwise signal are separated by design

**[E1].** Falsified by: an instrument collecting a single undifferentiated justification covering both absolute and relative quality.

B forbids the per-response justification from referencing the other response, and requires the preference justification to compare them. D reproduces the separation with different rules: per-dimension justifications must be brief and address one criterion at a time, while the preference justification must open with a verdict, cite specific evidence from *each* response, and run to a few sentences. Two prose artifacts, two scopes, two format specifications.

E has no pairwise stage — its scoring is pointwise against a rubric — so it neither confirms nor contradicts.

**Weakened detail.** B's explicit *prohibition* on cross-referencing is B's alone; D achieves the separation through scope and format rules instead. The separation is [E1]; the prohibition is [E2].

**Why it matters.** Pointwise scores and pairwise comparisons are different training signals, and the instrument design anticipates the downstream objective. The form is not arbitrary; it is shaped by what the reward model consumes.

---

## 4. Equivalence is engineered out of the dataset, by opposite mechanisms

**[E1], and stronger in v3 than v2 stated it.** Falsified by: an instrument that collects, retains and pays for comparisons recorded as ties.

- **B** uses an even-numbered preference scale. A tie cannot be recorded. Where two responses are equivalent the rater must still choose, and the instructions resolve it by preferring the shorter response.
- **D** uses an odd-numbered scale with a visible midpoint, so a tie *can* be expressed — but a midpoint rating in the absence of a truthfulness or instruction-following error means the prompt must be rewritten. The task does not proceed. Further upstream, the whole loop requires at least one response to contain a failure before rating begins; where both responses are good, the contributor is told to make the prompt harder and try again.

Two instruments, opposite scale designs, same outcome: *these two are about equally good* never survives into the collected data.

**Consequence, restated.** D shows this is not merely a scale artefact. The preference dataset is conditioned on the presence of a model failure. It is not a sample of interactions; it is a sample of interactions in which a model failed and a human then repaired it. Whatever a reward model learns about "good," it learns from a corpus with the uneventful cases deleted.

**The verbosity story gets more complicated again.** B's tie-break pushed deliberately toward brevity. D's changelog records that conciseness and completeness were **removed as grading categories** partway through the project — after that date nothing in the instrument penalises a response for length. So across two instruments the vendors either pushed against verbosity or stopped measuring it, and models are verbose anyway. **[E2] for the removal, which is dated and unambiguous; [E3] for any explanation of it.** The defensible line for the room: the folk story — raters like long answers, so models got long — is contradicted by the instructions in two separate instruments, and the actual mechanism is not visible in these documents. Saying that is more credible than repeating the folk version.

---

## 5. The rationale is the product, and house style is a written edit specification

**[E1], and the strongest finding added in v3.** Falsified by: an instrument that collects free-form rater prose with no format constraints and no post-hoc correction step.

V2 established that justifications are collected artifacts produced under a fixed template. D shows how far this goes, and it goes considerably further than "a fixed template."

**The rater rewrites the preferred response until it is correct, and the rewrite is collected.** Minor rewrites cover formatting, wording and spelling. Major rewrites cover instruction-following and truthfulness failures, and every identified error must be fixed — leaving one is grounds for rejecting the whole task.

**The minor-rewrite rules are a specification of surface style.** They cover, as mandatory edits: removal of opening pleasantries, self-referential assistant phrases and closing offers of further help; removal of emojis outside appropriate context; removal of citations and references unless asked for; a rule about not bolding colons in headers when the following text is unbolded; line breaks between paragraphs; numbered lists only where sequence is implied and bullets otherwise; a named markdown standard; a named email-format standard. Two of these carry an explicit warning that they are easy to miss and must be double-checked. The document ships a banned-phrase list running to dozens of entries.

**Say this plainly in the chapter.** A room of researchers who have noticed that every assistant sounds the same, and who assume that is emergent, should hear that at least one pipeline distributed it as an edit checklist with a proofreading warning. Some of those mannerisms were not learned from the internet at large. They were typed out by contractors removing them, one response at a time.

**E corroborates at a different layer.** Its rubric criteria include formatting requirements, and its authoring guidance instructs that weights for polish items be kept low relative to core requirements — so surface style is scored, deliberately and at a controlled magnitude, inside an automated grader.

**The English selection effect drops to [E2].** Only A lists English writing proficiency among the skills assessed. Neither new document filters raters for language. The mechanism by which fluent-English prose shapes model behaviour is intact and better evidenced than before; the *selection* claim about who gets hired rests on one document. **Do not present it as industry practice.** State it as: one hiring instrument tested English writing on a technical rating task, and every instrument in the set imposes English style rules on the prose it collects. The forward link to Chapter 5's material on AI-text detectors misfiring on non-native writers still holds, on the weaker claim.

**A better-evidenced version of the same point: the labour models are incompatible.** [E1]. D recruits generalist contributors, gives them seed prompts written by someone else, tests them on English writing quality, and constrains their prose down to which punctuation may be bolded. E recruits domain professionals and asks them to design tasks drawn from their own working lives, on the explicit grounds that the pipeline is buying expert judgement rather than labour. Two documents, two entirely different answers to *who is qualified to say what good looks like* — and both answers are shaping the same class of model. For a room of international researchers this lands harder than the English-filtering claim and rests on more evidence.

### 5.1 The human produces the target artifact — but it is not always collected

**Two claims, two strengths.** V3 welded them together; see §0.6.

- **The labour recurs. [E1], three of five.** A produces an ideal response alongside its ratings. D rewrites the winning response into a corrected one. E requires a worked deliverable before the rubric may be written. In each case the contributor is made to produce the thing, not merely judge it.
- **The artifact becoming training data does not recur. [E2].** D collects the corrected response. E states outright that its worked deliverable is not trained on; its stated purpose is that an author who has attempted the task writes a better rubric than one who has not.

**Why the split matters for the chapter.** The claim "human-written model outputs are in the training data" rests on D and A. The claim "pipelines make experts produce the artifact in order to extract better judgement from them" rests on all three, and is the more interesting one — it says the expensive part of expertise is not the verdict but the attempt that makes the verdict reliable. Falsified by: an instrument that collects rubrics or ratings from authors who never attempted the task.

---

## 6. Rubric design, machine grading, and Goodhart pressure

### 6.1 The judge's blindness is the design constraint

**[E1], and the cleanest mechanical finding in the set.** Falsified by: a machine-graded instrument whose judge is given the prompt and the input files.

E describes its grader to contributors as a simple model that reads one criterion, reads the deliverable, and returns true or false — and states that the judge does **not** read the prompt, does not read the input files, does not read the other criteria, and has no internet access. Every criterion must therefore carry its own context: values, names and thresholds are written into the criterion text rather than referenced.

V2 flagged self-containedness as the bridge from human grading to machine grading and told us to name it explicitly. E states the causal direction outright: the criterion is self-contained *because the judge is blind*. C's two-judge setup is consistent.

**Teaching consequence.** This is where the ground should shift for the room. A criterion a non-expert can verify is a criterion a model can verify; a criterion written so a blind model can verify it has been stripped of everything except the checkable surface. That constraint, applied a hundred times per task, is what "measuring quality" reduces to inside an automated loop — a far more concrete route into RLAIF than any diagram.

### 6.2 Criterion-authoring rules

**[E1] for the shared principles; [E2] for anything named in one document only.** Falsified by: an instrument permitting compound or subjectively-worded criteria.

Recurring across C and E: criteria must be binary; objectively answerable, so that most readers would agree; atomic, with no conjunction joining two checkable things; self-contained; non-overlapping and collectively exhaustive; bounded in length.

New in E, [E2] each:

- **No process words.** A criterion must test the observable state of the deliverable, never how it was produced. Verbs describing method or intent are named as an error class. The grader cannot see the process, so the process cannot be graded — an unusually clean statement of what an outcome-based reward can and cannot reach.
- **Not restrictive.** Criteria must not overfit to one correct answer: ranges rather than exact counts, presence of a required element rather than exact wording. Justified explicitly by the need to grade unknown future responses rather than the one the author had in mind.
- **A traceability label** marking whether each requirement is stated in the prompt or follows from domain judgement, itself audited for correctness.
- **Weight anchoring** with a stated band for core requirements, a much lower band for polish, and strong negatives reserved for catastrophic failures.

C's rules that did **not** recur, now [E2]: the prohibition on mirror-pair criteria, the ban on zero weights, and the rule that negative criteria must flag presence rather than absence.

### 6.3 Goodhart pressure

**[E2] for C, [E3] for E.** Falsified by: an instrument that pays for failing tasks and shows no countermeasure.

C's structure was explicit: the scoring rule divides by positive weights only, the task counts only if the model scores below a threshold, and the author is paid to produce failing tasks — so adding negative criteria mechanically lowers the achievable score. C also carried the countermeasures: caps on trivial weights, bans on mirror criteria, tiered error thresholds, defective criteria retained in the score, and satisfaction defined as meeting intent rather than containing a phrase.

**E has the same incentive shape without a stated scoring rule.** The same person writes a prompt designed to make the model fail *and* the rubric that decides what failing means. E states no validity threshold, so the sharpest version of the Goodhart claim cannot be made from it. What E does carry is a countermeasure aimed squarely at the conflict: **dogfooding**, meaning the author must generate several responses to their own prompt, including deliberately weak ones, and check both whether the rubric separates them and whether individual criteria return stable judgements. Stated cause: authors overfit rubrics to the first response they happen to see.

**A firmer countermeasure than dogfooding, [E2].** E separates genuine task difficulty from manufactured difficulty and rules the second out. Arbitrary filters, hidden substitutions, secret decoding rules and physically impossible asks are named as cheap failures that do not reflect real professional reasoning; difficulty must instead come from competing constraints, implicit variables, or judgement under conflicting priorities. This is a direct anti-gaming rule at the prompt layer, and it is better evidence for §6.3 than dogfooding is, because it exists only to stop authors reaching the required failure by the easy route. The author is paid when the model fails; the instrument bans the twelve cheapest ways of making that happen.

**Present it as:** two instruments in which the same contributor sets both the task and the measure, with anti-gaming machinery bolted on in both — explicit and quantitative in one, procedural and definitional in the other. Teaching Goodhart at the human layer makes it obvious at the model layer.

### 6.4 Institutionalised acceptable disagreement — demoted

**[E2], C only.** See §0.2. The audit rule failing a weight only when two assignments land in opposite priority bands appears in one document of five. It remains a good answer to "where do two competent raters legitimately diverge," and it remains usable in the live exercise as *one* real instrument's rule. It is not a standard.

---

## 7. The human's role varies by client and task type

**[E1].** This replaces v2's temporal hypothesis, which is dead — see §0.1.

Across five documents the contributor's output is, variously: rate and justify; rate, justify and produce an ideal response; rate, justify, author the prompt and repair the winning response; author the prompt and the rubric while machines grade; author the prompt, the input files, a target deliverable and the rubric while machines grade.

Adversarial framing — design the task so the model fails — appears in the earliest firmly dated document and in the latest, in a human-graded project and a machine-graded one. Target-artifact production appears in three of five. Automated grading appears in two of five.

**What would falsify the variation claim:** a set of documents from different clients converging on one job description. Five have not.

**Retired hypothesis, [E4], retained only so it is not reinvented:** that grading automation increases over time. Untestable with documents collected this way (§0.1). Do not spend further effort on it, and do not let a sixth document resurrect it.

---

## 8. Grounding, verification, and staleness

### 8.1 Verification is time-boxed and source-ranked

**[E2] for the time box, [E1] for the source hierarchy.** Falsified by: an instrument requiring verification to completion, with no time limit and no source list.

D instructs raters to check every claim in a response and supplies a two-sided source list — acceptable: an open encyclopedia, high-quality publications, academic institutions, official health and government bodies, news outlets, books; unacceptable: social media, blogs, fun-fact sites, and opinion or Q&A sites. Other AI assistants are on the unacceptable list, and using AI tools to produce or evaluate work is grounds for removal from the project.

**The sharpest detail in the set:** the truthfulness scale carries a distinct band meaning *cannot assess*, and one stated trigger for it is that properly researching the claims would take longer than about fifteen minutes. Factual verification in this pipeline has an explicit budget. Past it, the correct action is to record that the claim was not checked.

V2's §8 said factual grounding is outsourced to contractors doing literature work under time pressure. That was qualitative. It now has a number attached, from inside the instrument, and the number is fifteen minutes.

**For a room of researchers this is the most quotable item in the set** — and it is defensible, because it is a rule rather than an inference. Part of a frontier model's factual anchoring depends on individual contractors verifying claims against an approved source list within a quarter of an hour, and marking the rest unassessable. It also means "correct" is partly defined as "agrees with the approved sources."

### 8.2 Staleness is designed against at the prompt layer

**[E1].** Falsified by: an instrument indifferent to whether a task ages.

A's rating form scored a response for being outdated as of a stated month — drift detection inside the instrument. D and E move the same concern upstream into task design. D bars prompts about frequently-changing facts and prompts requiring knowledge after a stated cutoff, and bars asking the model to read links because it cannot. E makes time-anchoring one of six named prompt-quality elements: the scenario must carry its own internal dates rather than lean on the real calendar, because the prompt will be used long after it is written.

**Three of five documents treat staleness as a defect to be engineered out, at two different points:** as a scored property of the response, or as a constraint on the task.

E states the underlying reason directly: the rubric must grade responses nobody has generated yet, from models that do not exist yet. The artifact has to outlive the model it was written for.

**Chapter 1 use:** D's cutoff rules are the practical consequence of a knowledge cutoff, seen from the side of the people working around it.

### 8.3 Citation requirements — narrowed

**[E2].** Only A required a minimum count of publicly accessible citations per task. E's rubric format includes a citations field, with guidance that it matters most in regulated and technical domains, and the field sits empty throughout its worked example — an available slot, not a requirement. **Report the minimum-count rule as one project's rule.** The recurring finding is the source hierarchy at §8.1, not a count.

### 8.4 Execution as ground truth

**[E2], unchanged.** B instructs raters to run code where applicable. Neither new document has an execution step; D's verification is search-based and E's is a judge model reading a deliverable. Verifiable grounding inside a human-graded loop remains a real observation from one project, and remains the tidiest forward link to verifiable-reward training. It is not general.

---

## 9. Quality control structures

**[E1] for tiering and audit; [E2] for each specific mechanism.** Falsified by: an instrument with no review layer.

V2's structures stand: two tiers, with attempters producing and reviewers auditing; promotion gated by sustained pass rates and a qualifying test; rate-limiting of new contributors until they clear an audit wall; hidden training tasks indistinguishable from production work that affect a contributor's quality score with no feedback given; ungraded justification fields for auditors only; and rejection of prompts answerable without domain expertise.

**New in D, [E2]:** an automated feedback layer sits beside the human review layer. Contributors receive machine-generated suggestions on their submissions, framed as advisory, explicitly not affecting quality scores, and explicitly limited — the document states the automated check does not verify truthfulness and may miss instruction-following problems, and that the contributor must check both themselves.

**Worth one slide.** The tool being trained is deployed as a partial auditor of the people training it, with its known blind spots written into the instructions. The pipeline is already recursive, and the vendor documented exactly where the recursion cannot be trusted. Better Chapter 4 material than anything in v2.

**New in E, [E3]:** a vendor claim that contributors producing careful target deliverables go on to write higher-quality rubrics and score meaningfully better, attributed to a review of thousands of tasks. No data, no method, no effect size — and the vendor benefits if contributors do more preparatory work. **Do not repeat this as a finding.** If it appears at all, it appears as an example of a quantitative-sounding claim with nothing behind it, which makes it useful for Chapter 17.

---

## 10. The instrument was rebuilt mid-collection, in one week

**[E2], precisely dated, unambiguous.** Falsified by: a versioned instrument, or any evidence that data collected under superseded rules was re-graded or discarded.

D's changelog carries three entries spanning seven days in September 2024. Across that week the project:

- restricted what may justify a preference to two named dimensions;
- deleted two grading categories outright, one of them concerned with response length;
- removed an automated correction step from the workflow;
- made major rewrites mandatory for two error classes where they had been discretionary;
- required contributors to start from a supplied seed prompt rather than write their own (§0.1);
- added four prompt categories;
- shipped a banned-phrase list.

**What follows.** Data collected in the first week of that month was produced under a materially different measuring device from data collected in the third, and nothing in the output distinguishes them. The rating scale, the set of things being measured, the division of authorship between vendor and contributor, and the mandatory edits applied to the collected text all changed inside a single project.

**Why this belongs in the chapter.** Every version of "trained on human preferences" — the folk version and the careful version — assumes a stable instrument. It assumes there is a thing being measured and a device that measures it. Here the device was rebuilt in flight, by the people paying for the data, with the changes announced in a bulleted list to the workforce. An audience of experimentalists will recognise instantly what that does to a dataset, and no analogy is needed to explain it.

**Ranking note, and a correction to my own first instinct.** This finding is forceful, but force is not evidence. It rests on one document, so it ranks below the [E1] items in §13, at the head of the single-document band. The temptation to lead with it is the same temptation §0.1 exists to guard against.

---

## 11. The pipeline has an operational theory of where hallucination lives

**[E2].** Falsified by: another instrument treating hallucination as uniformly distributed across topic obscurity, or targeting it by a different rule.

D instructs contributors to steer prompts into a specific band of model knowledge. It names three regions: topics the model knows correctly, which are common knowledge; topics obscure enough that the model correctly declines; and between them a band where the model believes it knows and confabulates. The middle band is named as the target, and contributors are told to aim there, with the practical advice to use a personal hobby — something obscure enough to catch the model out but familiar enough that the contributor can fact-check at a glance.

**Three things make this worth a slide of its own.**

First, it is an operational theory of confabulation written by a vendor for contractors, not a research claim — which is exactly why it is interesting. It describes hallucination as a function of topic obscurity with a non-monotonic shape, and it is used to organise paid labour.

Second, it explains something the room already experiences and misdiagnoses. Researchers report that models are reliable on textbook material and reliable at declining on the genuinely unknown, and unpredictable in between — which is where their own literature sits. The band the vendor hunts is the band the audience works in.

Third, it grounds an instruction that would otherwise sound like folklore: use a domain you know well enough to check quickly. That is a rule about verification bandwidth, and it connects directly to the time box at §8.1.

**Chapter 5 hook, and a note for the failure gallery.** This is better material than anything currently specified there, because it supplies a generating rule rather than a collection of examples: to build a domain-specific failure gallery, aim at the middle band of this group's own literature.

---

## 12. Realism in the data is manufactured to specification

**[E2].** Falsified by: an instrument collecting genuine user text rather than contributor-authored imitations of it.

D includes a prompt category for informal or incomplete input, and instructs contributors that where the seed prompt does not already contain spelling or grammar errors, they must introduce them. It supplies techniques: omit words, misspell, break sentences off, use unclear abbreviations, introduce ambiguous pronouns.

The messy user input in that dataset is not messy user input. It is a trained contractor's reconstruction of how a careless person types, produced to a specification, under a quality rubric that elsewhere penalises the contributor's own spelling and grammar.

**One line on a slide, no more.** It is a small finding but a clean one, and it complicates the mental image of preference data as captured behaviour. Very little of it is captured. Almost all of it is staged.

---



## 13. What to build from this

**Chapter 2, ordered by evidential strength.** This ordering is deliberately not the order of interest, and not the order of force. Within a tag band, items requiring less inference rank higher. Two items that make better stories sit lower than they did in v2, because the evidence did not move; one item added at v3.1 sits lower than my first instinct put it, for the same reason.

**Corroborated across independent documents — [E1]:**

1. **House style is a written edit specification, and the corrected response is collected (§5).** The most concrete item in the set. Leads the house-style segment. Note the split at §5.1: collection rests on two documents, not three.
2. **Equivalence is engineered out; preference data is conditioned on failure (§4).** Two opposite scale designs, same result. Reframes what a preference dataset is.
3. **The judge's blindness dictates criterion design (§6.1).** The mechanical bridge to RLAIF. Sets up Chapter 4.
4. **The human is made to attempt the task before judging it (§5.1).** Three of five. Corrects "annotators just pick A or B," and says something sharper: the pipeline buys the attempt in order to get a reliable verdict.
5. **Staleness is designed against, at both ends of the pipeline (§8.2).** Hooks Chapter 1's cutoff material and Chapter 5's drift segment.
6. **Instrument divergence, structural more than lexical (§1).** Weakened from v2. Still dismantles "trained on human preferences."
7. **Incompatible labour models — generalist raters versus domain professionals (§5).** Better evidenced than the English-filtering claim it partly replaces, and it lands harder on this audience.

**Single document, stated as a rule, no inference — [E2]:**

8. **The instrument was rebuilt mid-collection, in one week (§10).** Dated and itemised. For a room of experimentalists this may be the most immediately persuasive item in the chapter; it ranks eighth because it rests on one changelog, and the gap between its force and its rank is itself worth naming aloud.
9. **The pipeline has an operational theory of where hallucination lives (§11).** The middle band — model believes it knows, and confabulates — is hunted deliberately, and it is the band this audience's own literature sits in. Chapter 5 hook and the generating rule for the failure gallery.
10. **Verification is time-boxed at about fifteen minutes, and source-ranked (§8.1).** The single most quotable item for this audience.
11. **Realism in the data is manufactured to specification (§12).** One line. Complicates the image of preference data as captured behaviour.

**Single document, inferred from an error list or from structure — [E2] weak to [E3]:**

12. **Score-and-rationale mismatch (§2).** Uncorroborated after two further documents. **Keep its position in the argument** — it is still the setup for Chapter 5's unfaithful-reasoning material, which needs it. Present the incidence as unmeasured, and say on the slide that it comes from one error list.
13. **Goodhart structure and countermeasures (§6.3).** [E2] for the explicit scoring rule and for the difficulty-authenticity rules, [E3] for the incentive shape in the second instrument. Sets up Chapter 4.
14. **Role variation by client (§7).** [E1] as variation, listed last because it is a negative result. Not an arc. If the temptation to tell an arc returns, re-read §0.1.

**Do not teach as general:** non-directional axes, adjacent-band audit tolerance, minimum citation counts, English-proficiency filtering, execution-as-ground-truth, mirror-pair bans. Each rests on one document. Any of them can be taught as *one instrument's solution to a real problem*, which is honest and nearly as interesting.

**Live exercise** (`../assets/rating-exercise/README.md`) — changes implied by D and E, detailed there:

- Correct the three provenance claims that generalised from one instrument.
- Add a confidence self-report per rater, collected with the score.
- Add a *cannot assess* band with an explicit time box on verification.
- Add a short rewrite step: the rater repairs the response they preferred.

Nothing added at v3.1 changes the exercise design. §10, §11 and §12 are chapter material, not exercise material — though §11 supplies the rule for choosing the planted error: aim at the band where a competent model would confabulate rather than decline.

**Pending review:** none outstanding. Further documents are worth reading for §2 corroboration, the weakest load-bearing item in the chapter, and for any second changelog, which is the only document feature capable of supporting a claim about change over time. They cannot settle §7 and should not be read as though they could.

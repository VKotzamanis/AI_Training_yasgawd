# Review: ai-training/slides/02-formation.md — 2026-08-27 — reviewer: claude-opus-5[1m]

Reviewed under `FOR-REVIEW/RUBRIC.md` v1.1. Chapter-specific framing: this file is the
**superseded** Slidev draft of Chapter 2 (`CLAUDE.md` directory map: "`slides/*.md` — the
superseded Slidev decks, kept until each chapter is rebuilt"). A 33-frame Beamer rebuild
`slides/beamer/02-formation.tex` exists, dated 2026-08-22, with its own term audit at
`curriculum/ch02-term-audit.md`. The verdict therefore answers a salvage question. Overlap with
`TOPICS-LEDGER.md`'s `ch01-approved` entry is recorded as cross-chapter R so the non-overlapping
remainder becomes visible. Two findings were spot-checked against the rebuild; the rest were not
(see Checks not run).

Slides counted from 1 at the first content slide (the title slide, line 9). The file contains
**26** slides. `curriculum/review-ch02.md` (RC2) audited 27 at line 25; the count has moved by one
since. Not audience-facing, recorded not flagged.

**The chapter's argument, stated in a form its author would accept:** pretraining produces a
next-token predictor and nothing in that objective produces an assistant, so an assistant is what
was added on top — demonstrations written by people, then a reward model fitted to people's
pairwise comparisons, then optimisation against that reward model, then the same machinery pointed
at harmlessness and finally handed to the model itself; every observable behaviour of the product
therefore traces to a mechanism in that stack rather than to a personality; and because the whole
stack rests on a rating seat, the honest account of that seat — five vendor documents, findings
ranked by evidence rather than by force, and eight minutes of the room's own rating under time
pressure — is what the room actually needs, because the preference they express is a reward signal.

Prior-review citations used in place of re-derivation: PR19 = `curriculum/peer-review-19-chapters.md`,
RC2 = `curriculum/review-ch02.md`, per `PRIOR-REVIEW-SCOPE.md` §02-formation.

---

## Topic ledger

| topic | opens (slide) | closes (slide) | reopened at |
|---|---|---|---|
| pretraining objective, corpus, cutoff | 2 | 2 | — |
| the pretrained model as autocomplete | 2 | 2 | — |
| scaling laws and the compute-optimal correction | 3 | 3 | — |
| sparse routing / sparsity | 4 | 4 | — |
| supervised fine-tuning | 5 | 5 | — |
| reward model | 6 | 6 | 9, 12 |
| the six rated dimensions | 7 | 7 | 19, 23 |
| rater disagreement and the audit layer | 8 | 8 | 24 (step 5), 25 |
| RLHF | 9 | 9 | 12 |
| harmlessness / trained-in refusal | 10 | 10 | 26 |
| Constitutional AI and RLAIF | 11 | 11 | 18 (the criterion rule) |
| the machine-checkable criterion | 11 | 18 | — |
| DPO | 12 | 12 | — |
| behaviour traced to mechanism | 13 | 13 | 26 |
| prompt-claim replication (OPRO, EmotionPrompt) | 14 | 15 | — |
| the five-document evidential basis | 8 | 17 | 18, 19, 20 |
| annotation findings, corroborated band | 18 | 19 | — |
| annotation findings, single-document band | 20 | 20 | 21 |
| force versus evidential rank | 21 | 21 | — |
| findings held back | 22 | 22 | — |
| the rating exercise | 23 | 25 | — |
| the course thread map / chapter handoffs | 7 | 7 | 10, 26 |

Two rows carry the mechanical R signal. **The five-document evidential basis** opens at slide 8
(`One document of five`, line 212) and is not established until slide 17 — an interval opened
before its own definition, which is [ch02-004]. **The course thread map** opens at slide 7, reopens
at 10 and again at 26, which is [ch02-016].

Slides 18 and 19 carry near-identical Messages ("corroborated annotation findings with their
document counts"). The mechanical R test fires; the so-what test kills it — the nine findings
differ entirely and one slide cannot hold them. Not recorded as a finding.

---

## Slide messages

1. Chapter 2 asks what was added on top of next-token prediction to make an assistant.
2. Pretraining is one unsupervised next-token objective over a corpus that ends at a date, and it yields autocomplete rather than an assistant.
3. Scaling laws made loss predictable and were later corrected toward more data and smaller models, but neither result promised assistant behaviour.
4. Sparse routed models activate a subset of parameters per token, so total and active parameter counts come apart.
5. Supervised fine-tuning on human-written demonstrations teaches the model the shape of an answer.
6. A reward model fitted to human pairwise comparisons is a model of a rater that can score any response, including unseen ones.
7. The rating rubric has six dimensions, they conflict, and each returns later in the course.
8. Rater disagreement is audited but never eliminated, and what survives enters the preference data as inconsistency the reward model fits.
9. RLHF optimises the policy against the reward model, and the canonical result shows a 1.3B post-trained model preferred to a 175B base model.
10. Harmlessness is collected as a separate signal that conflicts with helpfulness, so refusal is trained in rather than filtered on.
11. Constitutional AI and RLAIF put the model in the rater's seat, which forces every criterion to be checkable without context.
12. DPO updates the policy directly from preference data, removing the explicit reward model but not the human comparisons.
13. Three observed behaviours are traced to training mechanisms with their evidential standing printed, and the folk explanation of verbosity is contradicted.
14. The OPRO "encouragement" instruction was found by search and is specific to the model it was scored on, so it is not evidence about encouragement.
15. EmotionPrompt's +115% headline was the best of eleven stimuli, against a replicated effect of about one percent.
16. Part 2b turns from the pipeline seen from outside to the pipeline seen from the rating seat, and marks the candidate 2a/2b cut.
17. Part 2b rests on five vendor documents, two of unverified provenance, treated as structural observations that never become citations.
18. Five corroborated annotation findings, each carrying its document count, ending on the one that bridges to machine grading.
19. Four further corroborated findings, ending on two incompatible labour models that dismantle the phrase "trained on human preferences".
20. Two single-document findings stated as rules: an instrument rebuilt mid-collection, and a targeted band of model knowledge where hallucination is hunted.
21. The most forceful finding ranks low on evidence, and the ordering is deliberately by evidence rather than by interest.
22. Five further findings are held back to the facilitator notes because the evidence does not carry them.
23. The room now rates two responses against one synthetic rubric under time pressure, with a verification time box and an unassessable band.
24. The exercise runs in six timed steps, and step 5 is the one to cut if time runs short.
25. Step 4 reads the tally back, checks confidence against preference, and names the room's own preference as a reward signal.
26. The chapter closes on a predictor plus demonstrations plus a learned rater model, and hands to Chapter 3 for steering and Chapter 4 for testing.

No slide failed the Message test.

---

## Findings

### [ch02-001] R blocker — slide 4
Quote: "A **sparse** model routes each token to a subset of its parameters. Total size and active size come apart." (line 87); "Published designs scale to very large total parameter counts while keeping the active count per token modest." (line 88)
Why it fails: `TOPICS-LEDGER.md` `ch01-approved` already delivers this mechanism in full — Supp §S15: "expert FFNs plus a learned router activating the top 1–2 per token; parameters multiply, per-token compute does not." The slide's only non-ledger content is the name *sparsity* for the total-to-active ratio, and Chapter 7 defines that same ratio itself at `slides/07-physical-limits.md` line 318 where it is used. The whole slide is redundant against material the curriculum owns elsewhere.
Fix direction: delete the slide; if the sparsity term must be pre-loaded for Chapter 7, one line inside slide 3 citing ch01 Supp §S15 carries it. Note that ch01 filed §S15 as beyond-scope with "nothing later depends on it", and line 95's "**Forward reference — Chapter 7.** This is not trivia" reverses that status without saying so — reconcile the two, whichever way. PR19 reaches the same delete recommendation on different grounds ("If Chapter 7 shrinks as recommended below, this slide has no consumer").

### [ch02-002] R blocker — slide 12
Quote: "A later result showed the preference data can be used to update the policy **directly**, with no explicit reward model in the loop." (line 328)
Why it fails: ch01 Supp §S13 is recorded in the ledger as defining "SFT …, the reward model …, RLHF …, DPO, RLVR … and the refusal direction". DPO at one-sentence depth is already delivered. The slide's remaining content is the paper's subtitle (line 329) and a framing sentence (lines 335–336); nothing technical is new. A whole slide restating a delivered ledger topic is the rubric's blocker case for R.
Fix direction: delete the slide and move its one live sentence — "the human comparisons are still the input; simplifying the machinery does not remove the layer this chapter is about" — into slide 9's closing block. RC2 independently marks it cuttable ("changes nothing the audience does. Facilitator notes.").

### [ch02-003] R major — slide 2
Quote: "One objective, run over a very large corpus: predict the next token." / "No labels, no task, no supervision beyond the text itself." / "It ends. **The cutoff is a date**, after which the model knows nothing except what you put in the window." (lines 33–35)
Why it fails: all three bullets are delivered ledger content — corpus at ch01 deck slide 4, unsupervised next-token training at deck slide 7 ("over trillions of unlabeled tokens"), knowledge cutoff at deck slide 5 ("the last date of the training corpus, bounding parametric knowledge"). The slide's genuinely new claim is the base-model failure mode at lines 41–42, which arrives last and unillustrated.
Fix direction: cut the three bullets to one line of recall and open the slide on what is new — the pretrained model continuing a question with more questions. RC2's finding 5 asks for that failure to be *shown* as a capture rather than asserted; the two fixes are the same fix.

### [ch02-004] F major — slide 8
Quote: "One instrument treats disagreement between *adjacent* bands as acceptable and only fails a rating when two assignments land in opposite bands. **One document of five** — a sensible rule, not an industry standard." (line 212)
Why it fails: "one document of five" consumes an evidential frame that does not exist until slide 17 — "**Five documents.** Two obtained as re-hosted copies, so the vendor, the client and their completeness are unknown" (lines 516–517) and "These are **structural observations**. They are not citable" (line 518). The room meets a document count nine slides before it is told what the documents are, whether they are citable, or why the count is printed. Slide 13 repeats the pattern at lines 368–370 ("Two of the reviewed instruments say otherwise: one broke ties deliberately toward **brevity**, the other **deleted length as a grading category**"), with no count and no frame at all. The dependency lives on slide 17.
Fix direction: either move the adjacent-band rule and the two verbosity instruments into Part 2b behind slide 17, or hoist a two-line version of slide 17's basis statement to the first use at slide 8. RC2 lines 95–98 flag the adjacent defect — the room has no concrete picture of a rater until slide 15 — and the same hoist fixes both.

### [ch02-005] F major — slide 18
Quote: "That third one is the mechanical bridge to machine-graded training, and it is why criteria end up stripped to the checkable surface." (lines 554–555)
Why it fails: the referent cannot be located from the slide. Five visually parallel `<v-clicks>` bullets are shown; counted as displayed, the third is "**Equivalence is engineered out.**" (line 546), which is not a bridge to machine grading. The intended referent is the fifth bullet, "**The judge's blindness dictates criterion design.**" (line 548) — confirmed against `curriculum/ch02-annotation-findings.md` §13 item 3, "The judge's blindness dictates criterion design (§6.1). The mechanical bridge to RLAIF" (line 357). The ordinal is correct against a ranking the room never sees, because the deck splits ranked items 1 and 2 into two bullets each without marking the nesting.
Fix direction: number the bullets against the ranking, or nest the two split sub-claims (lines 545, 547) under their parents so the displayed count matches the ordinal. This sentence carries the chapter's own hinge from slide 11 to its evidence; pointing it at the wrong bullet breaks the hinge.

### [ch02-006] F major — slide 13
Quote: "**TODO(verify)** — the brief also requires test-case hardcoding as a concrete reinforced reward hack … The system card carrying that quote is recorded at `[P]` and has not been read. **It does not reach a slide until it has been.**" (lines 387–390)
Why it fails: the block is rendered in the slide body, not in the speaker notes, so it is addressed to the author while the room is looking at it. The gate itself is correct under `CLAUDE.md` rule 1; its placement makes the slide unpresentable as written.
Fix direction: move the block verbatim into the `<!-- -->` note beneath the slide. No content change — the discipline is right, the audience is wrong.

### [ch02-007] T major — slide 15
Quote: "A much-cited **technical report** — not a peer-reviewed paper — found that appending emotional stimuli to prompts improved performance, with a headline **+115%** on one benchmark suite." (lines 438–440)
Why it fails: the source states that figure as a *relative* improvement, and the slide does not. Li et al. (arXiv:2307.11760) abstract, fetched 2026-08-27: "8.00% relative performance improvement in Instruction Induction and 115% in BIG-Bench". A relative +115% is compatible with a small absolute gain, and the room cannot size the claim without the scale. The defect compounds across the pair of slides: slide 14 prints "Reported gains up to 8% and up to 50% respectively" (line 410) from OPRO, whose abstract does not disambiguate points from relative gain, so two consecutive slides put percentages of undeclared and possibly different scales in front of a room being taught to grade numbers. The slide catches the *other* arithmetic problem in the same figure — best-of-eleven versus average, line 445 — which makes the omission harder to defend, not easier.
Fix direction: write "+115% relative on BIG-Bench" on the slide, and either state the scale of OPRO's 8%/50% or say that the source leaves it ambiguous. CONFIRMED for the Li et al. wording (arXiv abstract opened during this review); the OPRO scale is unresolved and is listed under Checks not run.

### [ch02-008] C major — slide 8 (first use), Part 2b throughout
Quote: "One **instrument** treats disagreement between *adjacent* bands as acceptable" (line 212); "Two instruments, opposite mechanisms" (line 546); "The rubric is a synthetic instrument built for this course" (line 698)
Why it fails: *instrument* is the load-bearing noun of the second half — it appears on slides 8, 13, 18, 19, 20, 23 and 25 — and the chapter never defines it. The room must infer whether it means the rubric, the rater-facing manual, the whole rating protocol, or the vendor document. The project has already ruled the term must be defined: `curriculum/ch02-term-audit.md` lists `instrument` as defined on frame 6 of the rebuild, "the written document a rater works to".
Fix direction: define it at first use on slide 8 in the term audit's own words, and define *rater* alongside it, which the same audit places on the same frame.

### [ch02-009] C major — slide 9 (first use)
Quote: "Generate a response, score it with the reward model, adjust the **policy** to score higher. Repeat." (line 238)
Why it fails: *policy* is used here and again at line 328 and is defined nowhere in the chapter, and no `TOPICS-LEDGER.md` entry delivers it — ch01 Supp §S13 records "RLHF (KL-constrained reward maximization)" without exporting the term. For a room of civil engineers the word reads as institutional policy, not as the model being trained. This is a curriculum-level forward dependency: the concept is consumed and no chapter delivers it.
Fix direction: on first use, gloss it — the policy is the model whose weights are being updated, the same $\theta$ Chapter 1 fixed — or replace the word with "the model" throughout and lose nothing.

### [ch02-010] C major — slide 6
Quote: "Train a **reward model** to predict that judgement." / "Now you have a function that scores any response — including responses no human has seen." (lines 148–149)
Why it fails: slide 6 is the reward model's fullest treatment in this chapter, so the five contract fields bind here. Field 1 (definition) and field 3 (necessity — "You cannot write demonstrations for everything", line 143) are present; field 2 (signal contract) is narrative rather than typed, giving an output score with no named input pair; **field 4 (observable capability in the deployed product) and field 5 (location — pipeline step and stage) are absent**. The chapter never says that the reward model exists only during training and is not present at inference, which is the misconception this exact framing invites — a room told the model "has a function that scores any response" will reasonably believe it scores their answer as it replies. ch01 Supp §S13 records the reward model as "discarded at deployment"; the chapter that spends nine slides on it does not repeat that.
Fix direction: add the stage and the consequence in one line — the reward model is a training-time artifact, discarded before deployment; what survives into the deployed weights is the behaviour it selected for. Confirmed to survive into the rebuild: `slides/beamer/02-formation.tex` contains no statement of the reward model's stage either.

### [ch02-011] C major — slide 11
Quote: "**Constitutional AI:** write the principles down, have the **model** critique and revise its own responses against them, and train on that." / "The general pattern is **RLAIF** — reinforcement learning from *AI* feedback, with the model standing in for the rater." (lines 294–295)
Why it fails: RLAIF and Constitutional AI are the only major components in this chapter that no `TOPICS-LEDGER.md` entry delivers — ch01 Supp §S13 covers SFT, reward model, RLHF, DPO, RLVR and the refusal direction, but not RLAIF — so slide 11 is their definitional home and the contract binds. Field 5 (location) is missing: the slide never says which step RLAIF replaces. Having built a four-stage pipeline across slides 5–9, it does not say whether the model stands in at the comparison-collection step, at the reward-model step, or at both, so the room cannot place the substitution in the pipeline it was just given. Field 4 (observable capability) is also absent. The slide names itself "the hinge of the chapter" (line 303), which raises the cost of the gap rather than excusing it.
Fix direction: state the substitution point explicitly — the AI feedback replaces the human comparison labels that feed the preference model, and slide 11's own line 297 already contains the narrow version of that claim for harmlessness. One arrow on the pipeline diagram RC2 asks for would discharge this and field 4 together.

### [ch02-012] C major — slide 17 (promise), slides 19–20 (unpaid)
Quote: "**Each finding carries how many of the five documents support it, on the slide.**" (line 524) against "**Staleness is designed against, at both ends.** … **Corroborated.**" (line 573), "**Instruments diverge — structurally more than lexically.**" (line 574, no count at all) and "**Two incompatible labour models coexist.** … **Corroborated.**" (line 575)
Why it fails: the promise is unpaid for three of the four findings on slide 19 and for the second finding on slide 20 (lines 603–604). Line 526 sharpens the promise — "this deck prints the count rather than asking you to trust the ordering" — and then asks exactly that. The cause is structural, not sloppiness: `curriculum/ch02-annotation-findings.md` line 29 defines `[E1]` as "**two or more**" documents and records a band rather than a count for those items, so the count the slide promises does not exist upstream for them.
Fix direction: weaken the promise to what the evidence supports — each finding carries its evidential band, and a count where the documents give one — or supply the missing counts in the findings document first. A room that notices "Corroborated." where it was promised a number learns the opposite of the lesson the slide is teaching.

### [ch02-013] C major — slide 7
Quote: "A rubric, and the same six dimensions recur across this course. **Learn them here; they do not get replaced.**" (line 173)
Why it fails: the chapter's most reused object arrives with neither a definition nor a provenance. *Rubric* and *dimension* are never defined — `curriculum/ch02-term-audit.md` records both as terms the chapter must define, on frame 9 of the rebuild — and the slide carries no citation and no provenance statement, so the room cannot tell whether these six dimensions are a published rating scheme, the vendor instruments' shared set, or a teaching construct. The chapter's own slide 19 then reports that instruments diverge on exactly this, with only instruction-following and truthfulness recurring (line 574), and slide 23 says the exercise rubric is "a synthetic instrument built for this course" (lines 697–698) — so the answer exists but is never given where it is needed. Under `CLAUDE.md` rule 5 the distinction is not cosmetic.
Fix direction: state on slide 7 that this is a teaching rubric assembled for this course, define *dimension* as one scored axis, and say plainly which two of the six recur across the real instruments. That converts an unsourced table into a claim with a standing, which is the chapter's own method.

### [ch02-014] R minor — slide 9
Quote: "Generate a response, score it with the reward model, adjust the policy to score higher. Repeat." (line 238)
Why it fails: restates ch01 Supp §S13's RLHF, and restates it with less: §S13 delivers "KL-constrained reward maximization", and the constraint is dropped here. A trainee holding only this version has an RLHF with nothing stopping the policy from drifting arbitrarily to chase reward — which is also the mechanism behind the reward-hacking example slide 13 wants to teach at lines 387–390.
Fix direction: cut the bullet to a back-reference and keep the slide's live content, the 1.3B/175B result at line 239; or keep one line and restore the constraint, since it is what makes the reward-hacking thread coherent.

### [ch02-015] R minor — slide 10
Quote: "Which means refusal behaviour is not a filter bolted on the front. **It is trained in**, from the same kind of human judgement as everything else." (line 268)
Why it fails: this is ch01 Supp §S16's delivered ruling — the ledger records that §S16 "separates guardrails from trained-in refusal" and places every capability by the rule that "a capability that can be changed without retraining lives in the harness or the context". The bullet re-argues a boundary the curriculum has already drawn. The slide's first two bullets, helpfulness and harmlessness as separately collected conflicting signals, are new and are what the slide should spend its space on.
Fix direction: replace the bullet with a one-clause back-reference to §S16 and let the conflict claim take the room.

### [ch02-016] R minor — slide 26
Quote: "**Threads opened — truthfulness** (a rated dimension here; a structural property in Chapter 5; a work habit in Chapter 14) and **trust boundary** (trained here; attacked in Chapter 6)." (lines 797–798)
Why it fails: both threads were already opened on the slides that own them — slide 7's table row "**Truthfulness** | a structural failure in Chapter 5; a work habit in Chapter 14" (line 180) and slide 10's block "Harmlessness as trained behaviour here; routed around from outside in Chapter 6; opened deliberately in Chapter 12; governed in Chapter 18" (lines 274–275). The closing restatement carries *less* than the originals, dropping Chapters 12 and 18 from the trust-boundary thread, and drifts in wording ("a structural failure" becomes "a structural property"). A trainee who copies the closing slide loses two handoffs and gains none.
Fix direction: either drop the footer, or make it the complete thread map and cut the partial versions on slides 7 and 10 — one location, one wording.

### [ch02-017] F minor — slide 21
Quote: "The rebuilt-instrument finding is the one this room will remember. It is **eighth** in evidential order, not first." (line 628)
Why it fails: the ordinal cannot be reconstructed from the deck. Counted as displayed, the rebuilt-instrument finding is the tenth bullet the room has seen across slides 18–20. "Eighth" is correct against `curriculum/ch02-annotation-findings.md` §13, where it is item 8 of 14 (line 365), but the room never sees that list and the deck shows only nine of its fourteen items. The slide's whole point is that the room can check the ranking rather than trust it, and as written they cannot.
Fix direction: write "eighth of fourteen ranked findings, of which this deck shows nine". The Beamer rebuild already applies exactly this fix at `slides/beamer/02-formation.tex` line 399 ("It ranks eighth of fourteen by evidence"). Same root cause as [ch02-005]; one renumbering fixes both.

### [ch02-018] T minor — slide 15
Quote: "A much-cited **technical report** — not a peer-reviewed paper — found that appending emotional stimuli to prompts improved performance" (lines 438–439)
Why it fails: the project's own record contradicts the flat claim. `references.md` line 90 states of `li2023emotion`: "It is a **technical report**, not a peer-reviewed full paper (a short v1 was accepted at LLM@IJCAI'23)." A workshop acceptance is peer review, so "not a peer-reviewed paper" overstates the discount, on a slide whose authority rests on getting sourcing distinctions exactly right.
Fix direction: "the expanded technical report carrying the 115% figure was not peer-reviewed; a short earlier version appeared at a workshop". CONFIRMED against `references.md` line 90, read during this review. The substantive attack on the paper — best-of-eleven reported as the result — is unaffected.

### [ch02-019] S3 minor — slide 6
Quote: "That function is a **model of a rater**, trained on a finite set of comparisons made by particular people under particular instructions. **Hold onto that sentence.**" (lines 155–156)
Why it fails: the closing emphasis position on the slide that states the chapter's thesis is spent on an instruction to remember rather than on the reason to. The payoff — which people, under which instructions — does not arrive until slide 19. RC3's "second-person dramatic address" is the prior review's precedent for the construction.
Fix direction: replace with the consequence in the same breath: a model of a rater inherits which raters, working to which instrument — the question Part 2b answers. Two prior-review style items in this chapter are cited rather than re-derived: "This is the hinge of the chapter" (line 303) is already logged by RC2 as one of three banned constructions, and RC2 line 53 flags slide 1's opening as "a negation followed by an assertion"; neither meets this rubric's S1 or S3 test, since both are followed by the content they announce.

---

## Coverage checklist

| chapter promise | status |
|---|---|
| Slide 1 (lines 15–16): "Nothing in that objective produces an assistant. This is what was added." | Paid — slides 5, 6, 9, 10, 11 |
| Frontmatter (line 4): "what the human layer looks like from inside it" | Paid — slides 17–22 |
| Slide 3 (line 67): "Worth knowing where the numbers come from before you repeat them" | Paid on the same slide, lines 67–68 |
| Slide 4 (lines 95–97): sparsity "appears directly in the critical batch size you will derive" | Paid out of chapter — `slides/07-physical-limits.md` line 318. See [ch02-001] |
| Slide 7 (line 173): "the same six dimensions recur across this course" | Paid — five of six rows name a return chapter; the Formatting row names none. Dropped by the so-what test, not filed |
| Slide 8 (lines 220–221): "You will occupy both sides of this in the exercise" | Paid — slide 24, step 5 (line 721) |
| Slide 11 (lines 306–308): "Part 2b is what that does in practice, and what it costs" | Practice paid at slide 18 (lines 554–555); cost paid at slide 25 (line 757), never linked back to slide 11 |
| Slide 13 (lines 387–390): the reward-hacking example the brief requires | Unpaid by design and correctly gated — [ch02-006] concerns its placement, not its absence |
| Slide 16 (lines 489–490): "what it looks like from inside the rating seat" | Paid — slides 17–22 |
| Slide 17 (line 524): "Each finding carries how many of the five documents support it, on the slide" | **Unpaid** — [ch02-012] |
| Slide 17 (lines 526–527): no vendor worked example, prompt, rubric row or banned-phrase list appears | Paid — verified across the file; no vendor content is reproduced |
| Slide 21 (line 629): "Two findings … were demoted … One was killed outright" | Partially paid — slide 22 line 658 names the demoted negative result; the killed finding is never shown. RC2 finding 3 already asks for the correction log to reach a slide |
| Slide 23 (line 697): "Full specification in `assets/rating-exercise/README.md`" | Paid — the file exists (12.5 KB); contents not audited |
| Slide 24 (line 719): step 3 reveals "the physical error and the fabricated citation" | Depends on the exercise asset; not audited (Checks not run) |
| Slide 25 (lines 771–772): the sample-size question | Paid by handoff to Chapter 4, explicitly |

Not a rubric C: *system prompt*, which RC2 finding 4 assigns to this chapter, is never used in this
draft, so the rubric's "used but undefined" test does not fire. It is a curriculum-placement item
already flagged (RC2 line 176; PR19 line 282).

---

## Topics exported

- **The post-training pipeline as a taught sequence** — pretraining → supervised fine-tuning → reward model → RLHF, each stage named by what it consumes. Slides 2, 5, 6, 9. Overlaps ch01 Supp §S13, which already derives all four; ch02 adds the ordering as a spine, not new mechanism.
- **The pretrained model as autocomplete** — a base model continues a question with more questions rather than answering it. Slide 2, lines 41–42. Not in ch01. Asserted, never shown.
- **Scaling laws and the compute-optimal correction** — loss falls predictably with size, data and compute (`kaplan2020`); for a fixed compute budget models were undertrained relative to their size, so more data and a smaller model (`hoffmann2022`); both are empirical fits over a tested range, extrapolated since. Slide 3. Not in ch01.
- **Sparsity as the total-to-active parameter ratio** — slide 4, the same definition Chapter 7 uses at its critical-batch-size derivation. The routing mechanism itself is ch01 Supp §S15.
- **Supervised fine-tuning teaches format, not quality** — "Everything after this is about **quality**, not about format." Slide 5, line 126. The cleanest statement of the SFT/RLHF division of labour in the curriculum.
- **The reward model as a model of a rater** — a function fitted to a finite set of comparisons made by particular people under particular instructions, which then scores any response. Slide 6, lines 155–156. The framing is ch02's own and is the chapter's thesis; the mechanism is ch01 Supp §S13. **Its stage is never stated — later chapters must not assume the room knows it is training-time only.**
- **The six rated dimensions** — truthfulness, instruction following, harmlessness, formatting, verbosity, tone — with the course thread each returns on, and the claim that they conflict. Slide 7. Provenance not stated; see [ch02-013].
- **Rater disagreement is information, not noise** — an ambiguous dimension produces disagreement no amount of rater training fixes, and unresolved disagreement enters the preference data as inconsistency the reward model fits. Slide 8.
- **The adjacent-band audit rule** — one instrument fails a rating only when two assignments land in opposite bands. Explicitly one document of five and explicitly not an industry standard. Slide 8.
- **The InstructGPT preference result** — a 1.3B post-trained model's outputs preferred to a 175B base model's, credited to supervised fine-tuning *plus* RLHF rather than the reinforcement step alone, with the authors' own "still make[s] simple mistakes". Slide 9. The gain is in preference, not correctness.
- **Helpfulness and harmlessness as separately collected, conflicting signals** — the tension is the method, not a bug in it. Slide 10. The trained-in-versus-harness half of that slide is ch01 Supp §S16's.
- **Constitutional AI and RLAIF** — written principles applied by the model in the rater's place; the published version generates harmlessness signals from AI feedback rather than human feedback. Slide 11. **Not delivered by ch01 — this is ch02's own component.** Its pipeline location is not stated.
- **The machine-checkable criterion rule** — once a written criterion is applied by a machine, it must be checkable without context, which strips it to the observable surface. Slides 11 and 18. This is the chapter's hinge and the sentence later chapters should cite.
- **Direct preference optimisation** — preference data updates the policy directly, no explicit reward model, and the human comparisons remain the input. Slide 12. ch01 Supp §S13 already defines DPO.
- **Behaviour traced to mechanism, with evidential standing printed per row** — firm refusal (published); agreement under pushback (plausible, not evidenced in the documents); long structured answers (mechanism not known, and the folk explanation is contradicted by two instruments, one breaking ties toward brevity and one deleting length as a grading category). Slide 13. The table format — what you see / where it comes from / standing — is the reusable object.
- **Optimised prompts do not transfer consistently across models** — OPRO's winning instruction is specific to the model it was scored on (`yang2023`, `ye2024`). Slide 14. This narrower claim explicitly replaces "does not transfer to newer models", which no primary re-evaluation supports.
- **Best-of-N reported as the result** — EmotionPrompt's +115% headline is the best of eleven stimuli; averaged over all eleven the original's own numbers give 4.42% on that suite and 2.58% across all benchmarks; an independent replication found about 1%, from a design that deliberately did not run best-of-eleven, which is why the two numbers do not contradict. Slide 15. Chapter 4 reuses the trap.
- **The five-document evidential basis and its band vocabulary** — corroborated across independent documents / stated once as a rule / inferred from structure, with the supporting count printed on the slide; five documents, two of unverified provenance, are not a sample; these observations never become citations and carry no source footer. Slide 17. The underlying `[E1]`–`[E4]` scale is not shown to the room.
- **Nine annotation findings** — house style as a written edit specification (three of five); the repaired text collected (two of five); equivalence engineered out by opposite mechanisms (two of five); one instrument collecting comparisons only where a model has already failed, so its preference data is conditioned on failure; the judge's blindness dictating criterion design, so every criterion must carry its own context (two of five); the human made to attempt the task before judging it (three of five); staleness designed against at both ends; instruments diverging structurally more than lexically, with only instruction-following and truthfulness recurring; two incompatible labour models — generalist raters and domain professionals — doing work described in the same vocabulary. Slides 18–19.
- **The instrument rebuilt mid-collection** — grading categories deleted, task authorship moved, mandatory rewrites imposed, in one week; data gathered a fortnight apart graded by materially different instruments with nothing in the output to distinguish them. One changelog. Slide 20.
- **The hallucination band** — contributors are aimed at the band between common knowledge, where the model is reliable, and genuinely obscure material, where it declines: the band where it believes it knows. Slide 20. The generating rule for Chapter 5's failure gallery and the explanation for why the tool feels reliable on textbook material and erratic on the room's own research.
- **Ranking by evidence rather than by force** — the most memorable finding ranks eighth of fourteen; the ordering is deliberately not the order of interest. Slide 21.
- **The rating exercise design** — two responses, one synthetic rubric on the room's own mechanics/concrete/fluids domain, eight minutes under visible time pressure, a score per dimension plus a preference plus a confidence self-report, verification time-boxed at two minutes with an *unassessable* band, and no preference permitted without a named specific failure. Slides 23–24, with the six-step schedule and the instruction to cut step 5 first.
- **"Unassessable" is the correct action on an unverifiable claim — and is exactly how a fabricated citation passes into a dataset as acceptable.** Slide 25, line 757.
- **Five or six raters is a tally, not a distribution.** Slide 25, line 755. The course does not present six points as one.
- **The room's own preference is a reward signal at scale** — eight minutes of rating is eight minutes of generating training data. Slide 25, lines 763–765. The chapter's payload.
- **The sample-size question handed to Chapter 4** — "how many raters would we have needed before that tally meant anything?" Slide 25, lines 771–772.

---

## Checks not run

- **The Beamer rebuild was not reviewed.** `slides/beamer/02-formation.tex` (33 frames, dated 2026-08-22) supersedes this Slidev draft per `CLAUDE.md`. Two findings were spot-checked against it: [ch02-017] is already fixed there (line 399, "eighth of fourteen") and [ch02-010] is not (no statement of the reward model's stage anywhere in the file). The other seventeen findings were not checked against the rebuild, so some may already be resolved.
- **Neither prompting paper was read beyond its abstract.** For `li2023emotion` I opened only the arXiv abstract (2026-08-27). The 4.42% and 2.58% re-derivation, the χ² = 0.11 / p = .74 figures, the "six current models" claim and the replicators' stated limits on slide 15 are all unverified. `vaugrante2024` was not opened at all.
- **The OPRO percentage scale is unresolved.** The arXiv abstract for `yang2023` does not disambiguate accuracy points from relative gain for the 8% and 50% figures, and I did not open the paper body. [ch02-007]'s CONFIRMED tag covers only the Li et al. wording.
- **The exercise asset was not audited.** `assets/rating-exercise/README.md` exists (12.5 KB) but I did not read it, so slide 24 step 3's planted physical error and fabricated citation are unconfirmed, and I did not check whether the four changes `curriculum/ch02-annotation-findings.md` line 378–383 requires of the exercise are present.
- **Figure coverage and footer compliance were not assessed.** Zero figures across the deck and `CLAUDE.md` §1c's every-slide-carries-a-footer rule are production-standard items outside the rubric's five classes; RC2's audit table already records both (RC2 lines 26–27), including that ten of the slides carry a footer.
- **PR19's premise-level verdict was not re-derived**, including its 105–115-minute timing and the 2a/2b split the slide-16 marker depends on.
- **One item outside the five classes, recorded not filed:** `references.md` carries two entries for the key `clark2022` — line 80 tagged `[V]` and line 110 tagged `[P]`. Slide 4 cites that key. The `[V]` entry appears to supersede, but a duplicate key is a build risk for `gen-sources-tex.mjs` and the frame check, not a defect in this chapter.

---

## Verdict

**salvage-with-edits.** The argument is intact, statable and worth the room's time, and the second
half is the course's genuine differentiator: printing document counts on the slide, ranking findings
by evidence against their own narrative force, correcting an earlier draft's overstated transfer
claim in front of the audience, and refusing to put an unread system card on a slide are the standard
the rubric's exemplar sets, met more consistently here than anywhere else reviewed so far. What
blocks the file is not the argument. Two whole slides re-deliver material `ch01-approved` already
owns — Supp §S15's routed models and Supp §S13's DPO — which the rubric grades as blockers, and a
third slide opens on three more delivered bullets. The Part 2b evidential frame is consumed at slides
8 and 13 before it is established at slide 17; two ordinals that the chapter's credibility rests on,
"that third one" and "eighth", are correct against a findings document the room never sees and
unrecoverable from the deck as displayed; the reward model and RLAIF are both defined without their
pipeline stage, which for the reward model leaves the room free to believe it runs at inference; and
the EmotionPrompt headline is reproduced without the relative scale its own source states, on the
slide that exists to teach number hygiene. None of that is repaired sentence by sentence — the
ordering, the pipeline diagram RC2 specifies, and the ledger overlap all need the restructure RC2
already wrote, and the file is in any case superseded by a 33-frame Beamer rebuild that demonstrably
fixes at least one of these findings already. Salvage the six-dimension table, the nine findings with
their counts, the behaviour-to-mechanism table with its standing column, and the exercise; rebuild
the container around them.

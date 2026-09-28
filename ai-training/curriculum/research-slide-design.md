# Slide design for technical training: what is evidenced and what is convention

Evidence review for the redesign of the 19-chapter deck (~245 slides, ~5 figures). 2026-08-20, session 3f1bda6d.
**Method:** eight load-bearing sources. Source 6 was paywalled and reached only via `agy`, so it is a **paraphrase of another model, not primary text**, flagged wherever used. All others were read as primary text.

---

## Sources

| # | Citation | Design | Access |
|---|---|---|---|
| 1 | Alley, M., & Neeley, K. A. (2005). "Rethinking the Design of Presentation Slides: A Case for Sentence Headlines and Visual Evidence." *Technical Communication* 52(4), 417–426. Penn State / Univ. of Virginia. | Argued case | via https://writing.engr.psu.edu/slides_references.html |
| 2 | Alley, M., Schreiber, M., Ramsdell, K., & Muffo, J. (2006). "How the Design of Headlines in Presentation Slides Affects Audience Retention." *Technical Communication* 53(2), 225–234. Penn State / Virginia Tech. | Quasi-experiment, n≈740 | https://www.writing.engr.psu.edu/ae_headlines.pdf |
| 3 | Garner, J. K., & Alley, M. P. (2013). "How the Design of Presentation Slides Affects Audience Comprehension: A Case for the Assertion-Evidence Approach." *Int. J. Engineering Education* 29(6), 1564–1579. Old Dominion / Penn State. | Experiment, n=110 | https://pure.psu.edu/en/publications/how-the-design-of-presentation-slides-affects-audience-comprehens/ |
| 4 | Aippersbach, S., Alley, M., & Garner, J. K. (2013). "How Slide Design Affects a Student Presenter's Understanding of the Content." ASEE Annual Conf., Paper #5691. Penn State / Old Dominion. | Experiment, n=130 | https://writing.engr.psu.edu/asee_5691.pdf |
| 5 | Mayer, R. E., & Johnson, C. I. (2008). "Revising the Redundancy Principle in Multimedia Learning." *J. Educational Psychology* 100(2), 380–386. UC Santa Barbara. doi:10.1037/0022-0663.100.2.380 | 2 experiments | https://eric.ed.gov/?id=EJ796353 |
| 6 | Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). "Cognitive Architecture and Instructional Design: 20 Years Later." *Educational Psychology Review* 31, 261–292. UNSW / Maastricht / Erasmus. doi:10.1007/s10648-019-09465-5 | CLT review | **paywalled; `agy` paraphrase only** |
| 7 | Wolfe, J., Shanmugaraj, N., Reineke, J., Caton Peet, L., & Moreau, C. P. (2024). "Advancing the Knowledge Base on Effective Presentation Slide Design: Three Pilot Studies." *J. Technical Writing and Communication*. Carnegie Mellon. doi:10.1177/00472816231169433 | 3 pilots | https://journals.sagepub.com/doi/10.1177/00472816231169433 |
| 8 | Ferguson, I., Phillips, A. W., & Lin, M. (2017). "Continuing Medical Education Speakers with High Evaluation Scores Use more Image-based Slides." *West. J. Emergency Medicine* 18(1). WashU / Stanford / UCSF. PMID 28116029 | Observational, 105 talks | https://pmc.ncbi.nlm.nih.gov/articles/PMC5226752/ |

Also consulted and **non-additive**: Brown University Sheridan Center, "Lecture Presentation Slides" (https://sheridan.brown.edu/resources/classroom-practices/lecture-presentation-slides). One numeric rule — 18 pt body text, 24 pt for definitions and quotations — otherwise a restatement of Mayer and source 3. That is itself a finding: teaching-centre guidance is downstream of these same literatures, not an independent check.

---

## 1. Text density: mostly convention, and one rule is contradicted

**The "6×6 rule" has no located empirical basis.** A search aimed at words-per-slide evidence returned nine of ten first-page results from presentation agencies, template vendors and listicles. No study was found that manipulated words per slide and measured learning. **Treat 6×6, 7×7 and the "rule of seven" as convention with no evidence located.**

**One observational result contradicts the density rule.** Ferguson et al. (source 8) coded 105 CME lectures by 49 faculty against 1,222 attendee evaluations. Text density (mean 25.61 ± 8.14 words/slide) was **not** a significant predictor of evaluation score: F(1, 86.29) = 0.055, p = 0.815, b = −0.0001. Image fraction (mean 47.4 ± 25.4% of slides) **was**: F(1, 100.68) = 6.158, p = 0.015, b = 0.277 on a 5-point scale. The authors stress this is association, not causation, and that evaluation is not a learning measure. **Read as: density is a weak lever; presence of figures a stronger one.**

**What is evidenced is not "fewer words" but "which words, in which position."** Alley et al. (source 2) taught one geoscience course across four semesters (n = 200, 202, 201, 136), swapping phrase headlines for sentence headlines. Across 15 exam questions on information that sat in a sentence headline in one version and body text in the other, recall was 69% vs 79%, χ², p < .001. Per question, 7 of 15 favoured sentence headlines significantly and **2 of 15 favoured the traditional design (both p = .01)** — the authors report this. A control set of 17 questions on body-text information scored 73% vs 74%, not significant: the effect tracks the headline, not the redesign at large.

**Caveats.** Between-semester quasi-experiment: different cohorts, different class times (one section at 8:00 a.m.), no randomisation. The manipulation was confounded — the transformed decks changed headlines *and* raised image coverage from 60% to 100% of slides *and* removed subordinate text. Those three cannot be separated.

---

## 2. Slide versus speaker: the split is evidenced, but not in the strong form usually quoted

The redundancy effect (source 6, paraphrase) applies to **self-contained duplicate sources**: a diagram plus a paragraph saying the same thing forces the learner to reconcile the two, which is wasted load. It is distinct from the **split-attention effect**, which concerns *complementary* sources neither of which stands alone — there the fix is to integrate them, not delete one.

Mayer & Johnson (source 5) is the load-bearing correction. Students viewed narrated slides (Exp. 1: 16 slides, lightning; Exp. 2: 8, car braking). The redundant condition added **2–3 printed words identical to the narration, placed beside the corresponding diagram element**. That group *outperformed* the no-text group on retention, **d = 0.47 and 0.70**; transfer showed no difference. Short, positioned keywords help. **The harmful case is a slide readable as a substitute for listening.**

**Implication.** The failure mode is not "text on slides" but prose the reader can process independently of you — full sentences, multi-clause bullets, the closing rhetorical line. Those are self-contained redundant sources. A five-word label pinned to a diagram element is not.

---

## 3. Diagram density

Direct evidence on *how often* a figure should appear is thin: source 8's image fraction (mean 47.4% of slides, predicts evaluation, not learning), and source 3's finding that a deck with visual evidence on every slide beat PowerPoint defaults on comprehension, misconceptions, delayed recall and perceived cognitive load (n = 110).

Wolfe et al. (source 7, Carnegie Mellon) is the only source here that tests where these principles *fail*. Their pilots report that multimedia principles hold even for expert audiences viewing advanced research, but that **decorative "visual organisers" — PowerPoint SmartArt in particular — can backfire**, because the shapes assert relationships the content does not support. A figure encoding a false structure is worse than the text it replaced.

**What teaches, per the sources: process flows, annotated diagrams of a mechanism, and worked examples. What does not: SmartArt-style shape arrangements, and stock imagery.**

---

## 4. Equations

No source here studies equations on slides. The relevant evidence sits one level up, in cognitive load theory (source 6 — **paraphrase**); three effects apply directly:

- **Worked example effect** (Sweller & Cooper, 1985, algebra). The review reports "very strong empirical evidence": studying a fully worked step-by-step solution beats attempting the equivalent problem. **→ Show the equation used on a worked case, not stated abstractly.**
- **Split-attention effect.** Symbol definitions in a separate legend or on a later slide are complementary-but-separated sources; the learner burns capacity mapping them. **→ Annotate symbols in place.**
- **Expertise reversal effect.** Guidance that helps novices becomes redundant load for experts. In a mixed-ability room this tension has no clean resolution; the review's answer is fading guidance, not one fixed level.

Building an equation up in stages is **not directly evidenced by anything found here** — it is a plausible application of segmentation, which the review supports for animations. Judgement, not evidence.

---

## 5. The named alternative: assertion-evidence

**Origin.** Alley & Neeley (2005), *Technical Communication* (source 1) — Michael Alley, engineering communication, Penn State. A **complete-sentence headline stating the slide's single message**, supported by **visual evidence** rather than a bulleted list. Alley traces the sentence headline to Perry in the 1960s. Source 1 is an argued case, not an experiment.

**Evidence.**
- *Audience side*: source 3, n = 110, identical spoken content, AE vs PowerPoint defaults → better comprehension, fewer misconceptions, lower perceived cognitive load, stronger delayed recall.
- *Presenter side*: source 4, n = 130 students each built 5 MRI slides after reading the same article, then sat an unannounced essay quiz next day, blind double-rated on a 22-item rubric. AE 12.55/20 vs 10.68/20, t(51) = 2.62, p = 0.01; on the hardest item (gradient magnets), F(1,52) = 9.92, p < .01. **Counter-result the authors report:** the bullet-list group recalled *more secondary detail* (0.24 vs 0.19). AE trades peripheral detail for core-process understanding.
- *Headline alone*: source 2, above.

**Assessment.** The AE evidence converges across three designs but comes largely from one group centred on Alley — an independence limitation. Source 7 is the nearest independent scrutiny found; it supports the underlying multimedia principles while flagging that visuals can harm when they impose false structure.

---

## 6. Specification

**[E]** evidenced · **[J]** judgement · **[C]** convention, no evidence located.

1. **One message per slide, as a complete-sentence headline.** [E — sources 2, 3, 4]
2. **Slide body carries evidence, not prose.** No multi-clause bullets, no full sentences below the headline, no closing rhetorical line. [E for the mechanism — source 5; J for the specific bans]
3. **Body text: short labels only, ≤ 8 words each, adjacent to what they label.** Derived from the 2–3-word keyword condition in source 5, relaxed for technical vocabulary. [J — extrapolation, not measurement]
4. **No global words-per-slide cap.** 6×6 is unevidenced [C] and source 8's null argues against spending effort there. Cap *self-contained prose*, not word count.
5. **A figure is mandatory whenever the slide asserts a relationship, mechanism, process, or comparison.** Text alone suffices for a definition, a numeric value, or a stated convention. Expect near-100% figure coverage on mechanism chapters. [E in direction — sources 3, 8; J on the threshold]
6. **Floor of 50% of slides carrying a figure**, just above source 8's 47.4% mean. The current ~2% (5 / 245) is the defect. [J — a floor, not an optimum]
7. **No SmartArt or shape-arrangement graphics.** [E — 7]
8. **Equations: define every symbol as a callout on the equation itself, never in a legend or on a prior slide** [E — split-attention]; **pair each equation with one fully worked numerical case** [E — worked example effect]; **reveal in stages beyond three derivation steps** [J — segmentation, extrapolated].
9. **Speaker notes carry everything the audience should hear once and not read**: argument, caveats, transitions, and the rhetorical closing lines currently on slides. [E in mechanism — source 5]
10. **Minimum 18 pt body text, 24 pt for definitions and quotations.** [C — Sheridan Center, uncited]

---

## 7. Search-quality finding

The exclusion list was necessary: the words-per-slide query returned ~90% agencies and template vendors on page one and zero primary research. The literature sits in three venue families — engineering communication (*Technical Communication*, *IJEE*, ASEE), educational psychology (*J. Educational Psychology*, *Educational Psychology Review*), and medical education. Outside them, searches return marketing.

---

## What was not done

- **Source 6 (Sweller et al. 2019) was never read as primary text.** Springer paywall, `leadinglearner.me` mirror returned 403. Everything attributed to it here is an `agy` paraphrase and must be verified against the original before any of it enters teaching material.
- **Source 1 (Alley & Neeley 2005) was not read** — only its citation verified, from the Penn State bibliography. Its content is characterised from that summary and from sources 2–4.
- **Source 7 (Wolfe et al. 2024) was read as abstract only** — no sample sizes obtained, so its pilots cannot be weighed quantitatively.
- **No source was found that studies equations on slides directly.** Section 4 is applied cognitive load theory, not domain evidence.
- **No search on accessibility constraints** (contrast, colour-blind-safe encoding, screen-reader order), which will interact with any visual system chosen.
- **No decision header added, `graphify --update` not run** — §6 is a proposal, not an adopted decision.

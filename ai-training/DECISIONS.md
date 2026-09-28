# Decisions and Open Questions

## Locked

| Decision | Choice | Reason |
|---|---|---|
| Format | Three sessions, weekly, ~4 h each | 12 h of content; attention collapses past four hours; the gap lets attendees arrive with real questions |
| Authoring environment | Claude Code, this git repository | The repo doubles as the live demo in Chapter 9 |
| Claude Code taught via | Desktop app and VS Code first; terminal optional | Room has little terminal experience; graphical entry points remove a fake barrier |
| Hands-on API work | Local gateway keys against the group's own machine | Paid Claude subscriptions exclude API access; local calls cost nothing per token |
| Anthropic API | Instructor demo on instructor key | Avoids forcing attendees to buy credits |
| Architecture depth | No attention matrices, no positional encoding | Low return for this audience; time better spent on hands-on work |
| Cross-provider retrieval | Taught as a licensing asymmetry with a provenance obligation | Accurate, and survives a question in a way "bypassing Claude" would not |
| Paywall circumvention | Excluded | Institutional licence violation; risk lands on the student |
| Chapter 6 placement | Before Session 2 | Threat model precedes capability |
| Chapter 7 before Chapter 8 | Cost before brain comparison | Concrete before abstract; Session 1 **ends** on the memory-gap line. **Clarified 2026-08-20:** Session 2 opens with Chapter 9, and the brief puts the callback at the top of **Chapter 10**, roughly ninety minutes later. Both are intended — the line closes Session 1 and is picked up in Chapter 10, not in Chapter 9. Chapter 8 owns the wording; Chapter 10 quotes it. |
| Slide toolchain | ~~Slidev~~ **Reversed 2026-08-20 to pandoc/Beamer, `UHTraining` theme, raw `.tex`** | Adopted on trial 2026-08-19; both spikes passed and no reversal trigger fired. Reversed anyway after a six-way format trial on the same two slides, which produced better reasons than the triggers anticipated — evidence in `slides/format-trial/README.md`. **(a)** LaTeX typesets the annotated equations visibly better than KaTeX, one of the two gaps named when Slidev was adopted. **(b)** The Mermaid dependency, the main reason to stay, is eleven diagrams across nineteen decks, seven of them in Chapter 1. **(c)** Slidev renders Mermaid inside a shadow root, so no project stylesheet can size a diagram; three Chapter 1 diagrams had to be restructured to stop them overflowing. Decks are raw `.tex` rather than pandoc markdown, because console frames and animation slots cannot be expressed in markdown. Migration cost was near zero because eighteen of nineteen decks were being rewritten anyway. |
| Every slide carries a footer | **Enforced, with a provenance vocabulary** | Ruled 2026-08-20. Hard rule 2 forbids inventing a citation, and a teach-from-zero chapter is mostly definitional slides with nothing honest to cite. So a slide making no external claim declares its provenance instead — `definition`, `derived`, `computed`, `observation`, `schematic`, `none`. Every slide now states its epistemic standing on its face, which is stronger than the original rule intended. `slides/beamer/check-frames.py` enforces it. Supersedes hard rule 1b. |
| Delivery length | **Not a criterion, and not discussed** | Ruled 2026-08-20: *"Do not worry about the time. Do not ever talk about the time again. I will decide what to keep. More details is better from your end."* Chapters are written in full. A recommendation to cut must rest on a content reason — it changes no decision the audience will make, it repeats a lesson already taught, its premise is wrong — never on length. The timing analysis in `curriculum/peer-review-19-chapters.md` §A1 is retained as evidence and marked superseded. |
| Chapter 8 scope | **Dissolved. Appendix deck, not delivered** | Agreed 2026-08-20. Chapter 1 no longer opens the "is it like a brain?" question, so Chapter 8 had no question left to answer, and its structural job — motivating external memory — is already done by Chapter 1's "nothing carries over when the session ends". It cost roughly 30 minutes of the session that is already ~165 minutes over budget, on cognitive-neuroscience literature nobody in the room can check. **The brain question is now answered where the room asks it: on the training slide.** Chapter 1 slide 7 carries neural network and learning as borrowed names, what training physically changed, and the standing of the brain-comparison literature in one cited line; the attention slide carries the third borrowed word. The units point — four chunks against two hundred thousand tokens is not a comparison — moves to Chapter 10, where the context window is live. `slides/08-brain-and-model.md` survives as the appendix, distributed rather than presented. See `curriculum/peer-review-19-chapters.md`, Chapter 8. |
| Domain of shared material | **Mechanics, concrete, fluids** | The intersection of what all 5–6 attendees know. Anything the whole room grades together sits here; anything an attendee runs alone stays in their own field. Overturns the wave-energy-only rule in `assets/rating-exercise/README.md`, by that rule's own argument — an audience cannot judge truthfulness on a domain it does not know. The instructor's own field becomes the worked instance, not the shared material |

## Open — blocking

**Chapter 2 structure — restated 2026-08-20, and no longer a clock question.** This item was a time
overrun, with a 2a/2b split recommended to absorb it. Delivery length is no longer a criterion, so
the overrun is not the question.

**The question that remains is a better one.** Chapter 2 rests on two evidence bases that are not
interchangeable: published papers carrying `[V]` citations, and five annotation instruments held by
the instructor, which are structural observations, uncitable, and tagged `[E1]`–`[E4]` on a separate
scale. The 2a/2b split existed partly so a reader could tell which base a slide sat on.

**The footer ruling changes the calculus.** Every slide now declares its provenance on its face, so
the two bases can be told apart slide by slide without a structural divide. That makes weaving a
live option — each mechanism claim followed immediately by the annotation evidence for it, one
argument rather than a lecture plus an appendix. Against it: mixing published citations with
uncitable observations may still blur them in the room, whatever the footer says.

Assessed in `curriculum/review-ch02.md`.

**The original overrun analysis, retained as evidence.** The chapter was budgeted at 75 minutes and
needed roughly 105–115.

| Component | Minutes |
|---|---|
| Pipeline mechanics — pretraining, cutoff, SFT, preference layer, reward modelling, RLHF/RLAIF, Constitutional AI | 25–30 |
| OPRO case with caveats; the emotional-prompting statement | 10 |
| Behaviour traced to mechanism | 8 |
| Nine taught findings from `curriculum/ch02-annotation-findings.md` §13 | 28 |
| Live rating exercise | 35–40 |

Caused by the annotation findings turning out stronger than planned. A good problem, but it determines how much slide material gets written, so it blocks drafting.

**Options:**

- **Split into 2a (Formation) and 2b (The Annotation Layer). Recommended.** Preserves chapter numbering, so the thread map in `curriculum/architecture.md` — which references chapters by number in five places — stays intact. Reflects what has actually happened: two teaching units, one on how a predictor becomes an assistant, one on what the human layer looks like from inside it. Session 1 grows by ~35 minutes.
- **Renumber into Chapters 2 and 3, shifting everything after.** Cleaner naming, breaks the thread map and every cross-reference in the briefs. Not worth it.
- **Hold 75 minutes and triage to four or five findings.** Keeps the session budget and throws away the best material in the set, including the seven-day instrument rebuild and the confabulation-band theory.
- **Move the exercise to Session 3.** Frees 40 minutes but severs it from the mechanism it demonstrates, and the room would rate before understanding what rating is for.

Even after a split, nine findings is the ceiling. The remaining five stay in facilitator notes as answers to questions that will get asked.

**2. Antigravity configuration.** Confirmed as the group's Gemini access path, already wired into Claude Code. The working configuration is still needed before Chapter 12 can be written — what is actually invoked, and how results come back.

**3. Chapter 2 source material — resolved in approach, still to draft.** The instructor holds copies of attempter and reviewer manuals from projects they did not work on, so no personal NDA covers them. They inform structure only. Citations come from published annotation guidelines (see `references.md`, Chapter 2); texture comes from the instructor's own experience; the chapter ships a synthetic rubric built on this group's domain. No internal or leaked document is cited or reproduced — an unciteable source has no place in a course teaching citation discipline.

## Slidev trial — what has to hold

Adopted against the advice recorded in this file. That advice was: pandoc to Beamer, because citations come free via a `.bib`, LaTeX handles built-up derivations, the pipeline is already working, and it would double as the Chapter 15 demo. Slidev's markdown source, animated code stepping and inline Mermaid were judged worth the trade.

Two known gaps and how they get closed:

**Citations.** No bibliography engine. Build a footer component taking a citation key, backed by a keyed source list generated from `references.md`. Then add a build check that **fails if any key tagged `[U]` appears in a slide.** This is stricter than what Beamer gives by default, and the check itself becomes Chapter 4 demo material.

**Equations.** KaTeX is a subset of LaTeX. Roofline expressions are within it; multi-line aligned derivations revealed stepwise are the risk. **Build Chapter 7's hardest derivation first, as a spike, before committing further.**

Accepted losses:
- PPTX export renders slides as images, so text is not selectable. Colleagues cannot edit the deck in PowerPoint. Deliverables are PDF plus a hosted SPA.
- Node and a Vite build step added to the project. Pin the Node and Slidev versions and record them in `CLAUDE.md`.

**Reversal triggers.** Any one of these and the deck moves to pandoc:
1. The Chapter 7 spike cannot render the derivation, or cannot build it up stepwise.
2. The citation footer plus validation check costs more than half a day to build.
3. The build breaks during rehearsal week.

**Standing hedge.** Export to PDF and commit it whenever a chapter is finished. There is then always a presentable deck, whatever the toolchain does the night before.

## Open — non-blocking but needed before delivery

**4. Local machine reachable from the training room.** Blocks the Chapter 13 exercise. If not, that chapter becomes instructor demo and keys are distributed afterwards.

**5. Attendee count — resolved 2026-08-19.** Five to six, sharing mechanics, concrete and fluids. Pairing is viable when someone hits a usage limit. Local gateway capacity is not a constraint at this size. Item 8 below becomes a $25–30 decision rather than a cost question.

Two consequences beyond logistics. The shared-material domain is now fixed (see Locked). And six raters is not a distribution — the Chapter 2 exercise's "show two distributions" step needs rescoping to a tally named as an anecdote, and its pair-swap step needs a rule for an odd room. **Not yet applied to `assets/rating-exercise/README.md`.**

**6. Delivery dates.** Version-dependent facts — command behaviour, plan boundaries, pricing — must be re-checked in the week before each session.

**7. Journals the group publishes in.** Chapter 18 needs the actual current disclosure policies from those journals, not a generic summary. ASCE is likely to matter most and is the one most often missing from general guides.

**8. Console accounts for attendees (~$5 each).** Lower stakes now that the local gateway carries the hands-on exercise. Decide whether a second exercise against the Anthropic API is worth the friction.

**9. Slidev theme.** Cosmetic, does not block drafting. Default is serviceable; community themes install as npm packages. Pin whichever is chosen.

**10. Distribution.** Whether the deck stays inside the group or is shared more widely. Affects how carefully synthetic material in Chapter 2 must be scrubbed, and whether the failure gallery can include internal examples.

## Resolved during planning

- **"agy"** — Antigravity (Google), used as the Gemini access path. Configuration detail still outstanding, see item 2.
- **"ultracode"** — a real Claude Code setting, verified against the documentation. Session-scoped, pairs xhigh reasoning with automatic workflow orchestration. Covered in Chapter 11.
- **Long-context equation** — the roofline material does not describe accuracy degradation. Cost goes in Chapter 7, accuracy in Chapter 5, and the distinction is taught explicitly.
- **"LLMs are black boxes"** — too strong. Corrected framing in Chapter 5: partially instrumented, with real, expensive, incomplete tools that are themselves under validation.
- **Watermarking versus detection** — separate topics. Detection reliability is what affects this audience; watermarking is a provenance mechanism and gets its own treatment.

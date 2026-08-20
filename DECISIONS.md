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
| Chapter 7 before Chapter 8 | Cost before brain comparison | Concrete before abstract; Session 1 ends on the memory-gap line that opens Session 2 |
| Slide toolchain | **Slidev** | Instructor's call. Markdown source suits agent authoring; code stepping and Mermaid are strong for Sessions 2–3. Adopted on trial — see reversal triggers below |

## Open — blocking

**Chapter 2 time overrun.** The chapter is budgeted at 75 minutes and now needs roughly 105–115.

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

**5. Attendee count.** Determines room logistics, local gateway capacity, and whether pairing is viable when someone hits a usage limit.

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

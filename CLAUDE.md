# CLAUDE.md

Project instructions for this repository. Read `START_HERE.md` first for setup and first tasks; `README.md` for what the project is.

## What this repository produces

Teaching materials for a three-session AI training for PhD researchers in civil and environmental engineering. Slides, a facilitator run-sheet, a participant reference card, and demo assets.

## Hard rules

**1. No unverified claim reaches a slide.**
`references.md` tags every source `[V]` verified, `[P]` partial, `[U]` unverified, `[X]` rejected. Only `[V]` may appear in slide content. If you need a `[U]` claim, either verify it against the primary source and update the tag, or leave a `TODO(verify)` marker and move on. Never upgrade a tag without having read the source.

**1a. Two tag systems exist and they are not interchangeable.** `references.md` uses `[V]/[P]/[U]/[X]` for whether a *published source* has been checked. `curriculum/ch02-annotation-findings.md` uses `[E1]–[E4]` for the evidential strength of an *observation drawn from vendor documents*. An `[E1]` finding is corroborated across documents but is still not citable and never earns a `[V]`. Do not convert between the scales, and do not let an `[E1]` tag imply a source exists.

**1b. A slide may *discuss* a non-`[V]` source, provided it rests no claim on it.** Chapter 6 teaches an incident whose only sources are a conference talk and an unreachable article. The slide's assertions are about the *sourcing situation* — which this project established and can defend — not about the incident. Such a slide carries **no citation footer**, and says on its face that the absence is deliberate. This is the only permitted exception to the every-slide-carries-a-footer rule, and it is not a route for smuggling `[P]` material onto a slide by declining to cite it.

**1c. Every slide carries a footer.** Ruled 2026-08-20, no exceptions. A slide either rests on an
external source or it does not, and the reader is told which. Because rule 2 forbids inventing a
citation, a slide that makes no external claim declares its **provenance** instead, from a fixed
vocabulary: `definition`, `derived`, `computed`, `observation`, `schematic`, `none`. This is
enforced, not requested — `slides/beamer/check-frames.py` fails the build on a frame with no
footer, and on any key not tagged `[V]`. It supersedes §1b, which named the only exception under
the old rule.

**2. Never invent a citation.** No author names, years, venues, or arXiv identifiers from memory. If you don't have it, write `TODO(cite)` and list the search terms.

**3. Distinguish cost from accuracy in long-context material.** The roofline analysis in Chapter 7 explains why long context is expensive and slow. It says nothing about accuracy. Chapter 5 covers accuracy degradation, which has empirical curves and mechanisms but no closed-form equation. Conflating these is the single most likely error in this project.

**4. Declare conflicts of interest.** Sources with a commercial interest in their own conclusion get a COI note on the slide. See `references.md`.

**5. Don't reproduce proprietary material.** Annotation-platform manuals inform structure only. Chapter 2 uses a synthetic rubric, never a client instrument. No worked example from any vendor document — prompts, rubric rows, banned-phrase lists, fictional personas, project code names — is reproduced or paraphrased. Where a mechanism must be shown, rebuild it from scratch on this group's own domain. Documents are referred to by letter.

**6. Rank by evidence, not by force.** The most persuasive finding is often the one resting on a single document. State both the finding and what it rests on. If a claim would make a better story than the evidence supports, the evidence wins — see §0 of `curriculum/ch02-annotation-findings.md` for what happens when it doesn't.

**7. Assert before you edit.** Any scripted edit must assert its anchor string exists before writing, and any claimed change must be grepped back afterwards. A script that completes is not a script that edited.

## House style

- Active voice. Concrete over abstract. Cut hedges.
- Avoid: "crucial", "pivotal", "leverage", "delve", "robust", "seamless", "testament to".
- Present limitations plainly. This audience trusts a source more after it admits what it can't do.
- Where a claim is contested, say so on the slide rather than in the notes.
- Every slide carries a citation footer: author, year, venue, identifier. Podcast or interview material is labelled as expert testimony, not as a primary source.

## Conventions

- **Units and notation:** SI throughout. State sign conventions for any quantity whose sign is a convention rather than a measurement — bending moment, axial force, flow direction, and any wave or hydrodynamic quantity. Define every symbol on first use, including in equations lifted from a source.
- **Equations:** carry dimensional analysis. If an equation's denominator is defined non-obviously (see the MACs-vs-FLOPs erratum in Chapter 4), state the definition alongside it.
- **Filenames:** `NN-short-name.tex`, zero-padded, matching chapter numbers.
- **Chapter numbering is stable.** Threads in `curriculum/architecture.md` reference chapters by number. Renumbering breaks the thread map. Don't renumber without updating it.

## Slides

Toolchain is **pandoc/Beamer with the `UHTraining` theme**. Slidev was adopted on trial in August
2026 and reversed on 2026-08-20; the evidence is in `slides/format-trial/README.md`. The decks are
raw LaTeX rather than pandoc markdown, because console frames and animation slots cannot be
expressed in markdown and the translation layer breaks on exactly those constructs.

- **The theme lives outside this repository**, at `~/Desktop/Claude/beamer-uhtraining`. Run its
  `install.sh` once so `\usetheme{UHTraining}` resolves. Requires **xelatex or lualatex** —
  pdflatex is not supported, because the theme uses real Times New Roman through `fontspec`.
- **One file per chapter**, `slides/beamer/NN-short-name.tex`, matching chapter numbers.
- **Citations go through `\citesource{key}`**, never hand-typed. Keys resolve against
  `slides/beamer/uh-sources.tex`, generated from `references.md` by
  `slides/scripts/gen-sources-tex.mjs`.
- **Slides with no external source carry `\provenance{...}`** from the fixed vocabulary in §1c.
- **Build with `slides/beamer/build.sh`.** It gates on three things: the frame check, LaTeX errors,
  and **overfull vboxes** — an overfull vbox is precisely a frame whose content runs into the
  chevron footline, and that check found seventeen such frames in Chapter 1 that the eye would have
  had to catch one at a time.
- **Size figures by height, not width.** The theme leaves about 58 mm of content once the logo
  band, a two-line frame title and the footline are taken out, and the citation footer takes 6 mm
  of that. A figure at `width=0.93\linewidth` is already over.
- **Animation slots** are reserved with `\slotF` / `\slotW` / `\slotH` from `uhslot.sty`. The
  deck exports to PDF and then to PPTX, where every slide becomes a page image, so an animation
  cannot be layered on without covering what is printed underneath. Specification and authoring
  sizes: `curriculum/ch01-animation-slots.md`.
- **The four kinds of number each have one colour**, used identically in slides, figures and
  animations: token ID slate, parameter ochre, logit teal, probability UH red. Colour is a
  redundant cue — every coloured number carries its word too.
- **Nothing load-bearing may be interactive-only.** PDF is the deliverable and the fallback.
- **Export and commit the PDF whenever a chapter is finished.**
- Equations are ordinary LaTeX. The theme sets TeX Gyre Termes Math so they match the body text.

## Directory map

```
CLAUDE.md                       this file
README.md                       project brief and how to work on it
DECISIONS.md                    locked decisions and open questions
references.md                   citations with verification status, search terms
curriculum/architecture.md      chapters, threads, sequencing constraints
curriculum/chapter-briefs.md    content inventory per chapter
curriculum/production-plan.md   chapter categories, production order, review gate
slides/beamer/                  deck source, one .tex per chapter, plus uhcite/uhslot and the frame check
slides/format-trial/            the six-way format comparison that decided pandoc/Beamer
slides/scripts/                 source-table generators and the PDF-review stamping tools
slides/*.md                     the superseded Slidev decks, kept until each chapter is rebuilt
assets/                         figures, demo repos, failure gallery
assets/injection-demo/          poisoned-document demo. ISOLATED. Do not execute.
assets/rating-exercise/         Chapter 2 live rating exercise. Write from scratch.
assets/eval-worksheet/          Chapter 4 eval. Instructor runs it in advance.
assets/failure-gallery/         Chapter 5 domain-specific wrong outputs
```

## Working practice

- One chapter per branch. Chapters are independent units of work.
- Update `references.md` in the same commit as the content that uses a source.
- When you finish a chapter, re-read the thread map and confirm the chapter picks up and hands off what it's supposed to.

## Safety

`assets/injection-demo/` contains documents with instructions aimed at an agent. They exist to be shown failing. Do not read them into an agent session with file access, and do not run anything from that directory.

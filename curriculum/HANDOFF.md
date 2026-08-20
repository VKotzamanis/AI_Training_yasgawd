# Handover: rebuilding the AI training course

Written 2026-08-20 for whoever picks this up next. Read all of it before editing a slide.

---

## 1. What this is

Teaching materials for a three-session AI training course, roughly four hours per session,
delivered to a research group of five or six PhD students in civil and environmental
engineering. They all know mechanics, concrete and fluids. MATLAB is common. Terminal
experience is rare. Not all of them know wave energy, which is the instructor's own field,
so shared teaching material stays inside mechanics, concrete and fluids.

Nineteen chapters across three sessions. The repository holds the chapter briefs, the
architecture with its five cross-cutting threads, a references file with verification tags,
and nineteen Slidev decks with exported PDFs.

The instructor is the client and the reviewer. He is a PhD researcher, not a novice, and he
is direct. Take his criticism literally.

---

## 2. Where it stands

Nineteen decks exist and build. Every slide carries a four-bullet presenter note. Sources are
verified and tagged, and a build check blocks any citation below `[V]` from reaching a slide.

**Only Chapter 1 has been rebuilt to the standard below.** The other eighteen are written to
the old approach and are not usable. The reviewer's assessment of the first version was
"0 useable content". Treat chapters 2 to 19 as drafts to be rewritten, not polished.

---

## 3. The reviewer's criticism, in his words

These are the specification. Every one of them is correct.

1. **"The powerpoint format is very bad."** Walls of bulleted text, almost no figures,
   content pinned to the top-left of every slide with half the slide empty.

2. **"All the chapters are genuinely BAD in writing. You've written them with pompous and
   pretentious language that makes no sense."**

3. **"Lose the poetic shit throughout. This is technical training."**

4. **"We haven't even talked about what is AI. What is LLM. Is all AI LLM? What is a token?
   You can't define something by NOT defining it."** The old Chapter 1 opened its first
   substantive slide with "Tokens are not words", and the course never defined AI, LLM,
   model, training or inference anywhere.

5. **"This is very weird flow. We are telling the audience that something is like a brain
   without even identifying the 'IT'. Then we tell the audience to wait."**

6. **"'No goal. No plan. No model of you. One conditional distribution at a time.' What the
   fuck does that even mean? Lose the pretentious jargon that makes NO sense."**

7. **"Do you see how 'useless' this presentation is so far BOTH for beginners and experts?
   Beginners are lost. Experts gain 0 information and are confused."** The other criticisms
   follow from this one. The course was written for a reader who already knew what a language
   model was but wanted rigour about it, and no such reader is in the room.

8. **"I think we need a graph/flowchart with graphics that shows how LLMs work, where tokens
   are and how the cost/performance is associated with the tokens."**

9. **"This whole chapter needs to be redone COMPLETELY."**

---

## 4. What went wrong, so you avoid repeating it

**The chapter briefs list contents. The previous agent rendered those lists as slides, in
list order.** Chapter 1's brief says "Contains: tokenisation, next-token prediction,
probability distributions, sampling and temperature, the context window, the KV cache,
attention." The old Chapter 1 was those seven items as seven blocks of slides. No slide
existed because the slide before it created a need for it, so there was no flow to follow.
A reader could shuffle six of the fifteen slides without breaking anything.

**Nineteen chapters were built before any human read one.** Six peer reviews ran, all by
subagents, and they checked citation discipline, statistical arithmetic, thread coherence and
internal consistency. None asked whether a PhD student would learn anything. The verification
apparatus was rigorous and pointed at the wrong target.

**Foundational terms were never defined.** The course used model, training, inference, token
and LLM as though they were shared vocabulary.

**Five figures across 245 slides.** Research on technical talks finds image fraction predicts
talk quality while text density does not. The figure shortage was the larger defect.

**A factual error from over-simplifying.** A slide said the model "isn't looking anything up",
which is false for tools with web search. Simplifications that are wrong for the tool the
audience actually uses will be caught in the room.

---

## 5. Prose rules

This section matters more than any other. The previous agent was told to "write plainly" and
kept producing the same prose, so the rules below name specific patterns with real examples
taken from the decks. Check your output against them mechanically.

### 5.1 Banned constructions

**Antithesis. Negation followed by assertion.** The reviewer singled this out. Do not write it
in any form.

Real examples from the decks:
- "It is not caught by reading the sentence. It is caught by resolving the identifier."
- "It is not a gap in the course. It is the finding."
- "The context window is not a hippocampus. It is a buffer that gets discarded."
- "One is a buffer. The other is a process inside a system that consolidates."

Write the positive statement on its own. "Resolving the identifier is what catches a
fabricated citation." If a contrast genuinely carries information, put the two items in a
table with a column heading, where the reader can compare them without rhetorical scaffolding.

**The consequence clause.** Stating an action, then a dramatic price for it.

Real examples:
- "Approving a diff you have not read is the whole risk of this chapter."
- "A number you cannot defend is worse than no number."

Write the instruction. "Read the diff before you approve it."

**Aphoristic closers.** A short punchy sentence ending a slide or a section.

Real examples:
- "That is the difference between this and a style guide."
- "That is the point of this chapter."
- "That is the trade you have actually made this term."
- "Fluency did not help."

Delete them. If the sentence carries an argument the audience should hear, it belongs in the
speaker notes, where they hear it once instead of reading it while the speaker talks.

**Pointing constructions.** "That is the…", "This is the…", "Which is why…", "And that is
what…". They add emphasis and no information. Name the thing directly.

**Sentence fragments for rhythm.** "No goal. No plan. No model of you." Write complete
sentences.

**Rhetorical questions as slide headings.** "So what is five cases for?" Use a statement.

**Second-person dramatic address.** "You have just generated training data." State what
happened.

**Callbacks.** "Which is why the same question gave you two different answers last week."
The audience does not need a narrative thread tied for them.

### 5.2 What to write instead

- Subject, verb, object. One idea per sentence.
- Define a term the first time it appears, in the same sentence or the one after.
- Give numbers with units, and say what they were measured on.
- Where something is unknown, say it is unknown and stop. Do not perform the mystery.
  One reviewed source handles this well: it names the gap in the explanation plainly rather
  than dressing it up.
- Prefer the shorter word. Prefer the concrete noun.
- If a sentence would work as the caption to a diagram, it probably should be one.

### 5.3 A self-check before you commit a deck

Grep your own output:

```
grep -nE "It is not .*\. It is |That is the |This is the |Which is why" slides/NN-*.md
```

Any hit is a rewrite, not a judgement call.

---

## 6. Slide specification

Derived from research in `research-slide-design.md`, which grades each item as evidenced,
convention, or judgement. Read that file for the sources and the caveats.

1. **One message per slide, written as a full-sentence headline.** "The network is
   deterministic — the randomness is added afterwards", not "Determinism". This is the
   assertion-evidence structure, supported by three converging studies, with the caveat that
   the evidence comes largely from one research group.
2. **The slide body carries evidence, not prose.** No multi-clause bullets. No full sentences
   under the headline. Short labels next to what they label.
3. **A figure is mandatory whenever a slide asserts a relationship, mechanism, process or
   comparison.** Text alone is fine for a definition, a value, or a stated convention.
4. **At least half of all slides carry a figure.** The old decks ran at two percent.
5. **Equations: annotate every symbol on the equation itself**, using overbrace and
   underbrace, never in a legend below it. A separate legend forces the reader to hold the
   symbol table in memory while reading the formula.
6. **Pair every equation with one fully worked numerical case**, and verify the arithmetic
   before it goes on a slide.
7. **No global word cap.** The often-quoted six-by-six rule has no located evidence behind it.
   Cap self-contained prose instead.
8. **Speaker notes carry the argument, the caveats and the transitions.**

Graphics come from Mermaid, matplotlib scripts committed to the repository, ASCII, or
hand-written SVG. Generated imagery is not needed and should not be used.

---

## 7. Narrative method

Read `narrative-spine.md`. It gives every chapter a one-sentence premise, a standalone
takeaway, and the question that chapter leaves for the next one.

Three tests each chapter must pass:

1. **One sentence.** What is this chapter about? Two sentences means it is two chapters, or none.
2. **Attend only this.** What can somebody do on Monday having attended this chapter alone?
3. **Forced next.** What question does it leave open that the following chapter answers?

Slide order follows the argument, not the brief's content list. A term is introduced at the
moment the argument needs it. In the rebuilt Chapter 1, tokens appear because prediction needs
units to work on, rather than as item one of seven.

Material that is necessary but does not serve the argument goes to speaker notes, an appendix,
or the reference card. Most of what made the old decks unreadable was reference material
sitting on slides and competing with the argument.

---

## 8. What research says about teaching this specific subject

From `research-teaching-exemplars.md`. Six sources read in full: Wolfram's ChatGPT essay, the
Financial Times transformer explainer, Douglas (arXiv:2307.05782, written for mathematicians
and physicists), Bob Carpenter's slides for statisticians, 3Blue1Brown chapter 5, and
Karpathy's one-hour introduction.

**None of the eight sources examined defines a token by negation.** Every one gives a positive
definition and an instance. The old Chapter 1 opened with "Tokens are not words", and the
reviewer's objection to that is confirmed independently by the sample.

**There is no single consensus opening, and the split runs by audience.** Sources for general
readers open on an artefact the reader already owns, such as a phone keyboard's suggestion
strip or a generated story read before any mechanism. Sources for mathematically trained
readers name the object first, for example language as a stochastic process over a finite
token set. This group is the second type of reader with the first type of exposure: they have
the mathematics and lack artefact-level familiarity, so they need something they have used,
followed quickly by the object named.

**No good source opens on a rhetorical question about an undefined subject.**

**Token placement is genuinely split, and predictable from format.** Sources that walk the data
path define the token first, because the data path starts there. Sources that walk the
motivation show the loop first and defer the token. Either works. Mixing them does not.

**Keeping the objective from sounding trivial or mystical uses one shared move: state it
plainly, then immediately show it breaking.** Wolfram makes next-token prediction banal, then
shows that always taking the top-ranked word produces flat repetitive text. The FT states that
these are pattern-spotting engines rather than search engines, then shows greedy selection
producing a locally plausible and globally wrong phrase. The failure carries the teaching.
Where the reason for something is unknown, Wolfram says so and moves on rather than dressing
the gap up.

**Three techniques worth taking directly.**

- Karpathy defines a model as a concrete artefact in one slide: two files on disk. The course
  was faulted for never defining what a model is, and this solves it in a single slide.
- Wolfram defers the full definition of a token with a short parenthetical, which keeps the
  data path moving without leaving the term undefined.
- Douglas uses a token example drawn from the reader's own field. Use a term from this group's
  vocabulary, for instance overtopping or poroelasticity, so the token-splitting cost lands on
  words they actually type.

**Nothing was found written for an engineering audience.** The closest matches are physics and
statistics. The bridge to civil and environmental engineering has to be built here, and it is
the part with no exemplar to copy.

**A process finding for your own searches.** Keyword searches on this topic returned mostly
LinkedIn reposts, Medium listicles, vendor pages and patent filings. Going to institutions and
named authors directly worked. Budget your search time accordingly.

**Caveats recorded by the research.** The FT graphics could not be viewed, so the descriptions
of them are inferred from captions and a published method note. Karpathy's slide deck was not
opened, so his text density is unmeasured. Figure-reuse licensing was verified for only one
source, so check licensing before reproducing any figure.

## 9. Your task

**Peer-review the premise of every chapter before rewriting any of it.** Do not start from the
briefs. For each of the nineteen:

- Is the one-sentence premise in `narrative-spine.md` true, and is it the most useful framing?
- Does it earn a whole chapter, or is it two chapters, or half of one?
- Does the standalone takeaway survive if somebody attends only that chapter?
- Does the chapter answer the question the previous one raised?
- Does anything in it depend on a term the course has not defined yet?

Write your findings down and change the spine where it is wrong. The previous agent treated
the briefs as a specification and never challenged them, which is how the course ended up as a
content inventory.

**Then rebuild, one chapter at a time, and stop after the first one for the reviewer's
verdict.** Building eighteen more chapters before a human reads one is the mistake that
produced this handover.

---

## 10. Constraints that do not change

- **Only `[V]` sources may appear on a slide.** `npm run check:cites` enforces it. Never
  fabricate a citation; write `TODO(cite)` with search terms instead.
- **Two evidence scales exist and are not interchangeable.** `[V]/[P]/[U]/[X]` is for
  published sources. `[E1]`–`[E4]` in the annotation findings is for observations from vendor
  documents, which are never citable.
- **No vendor worked example is reproduced**, including prompts, rubric rows and banned-phrase
  lists.
- **Assert before you edit.** Scripted edits check their anchor exists and are grepped back.
- **Export to PDF and commit whenever a chapter is finished.**
- Pinned versions are in `slides/README.md`. Do not upgrade mid-project.
- Run at most two subagents at once. Six crashed this machine twice.

---

## 11. Open questions only the instructor can answer

- Chapter 2 is 105 to 115 minutes against a 75-minute budget. A 2a/2b split is recommended and
  undecided. The cut point is marked on one slide.
- Chapter 4 needs five test cases from mechanics, concrete or fluids, with a binary pass
  criterion each, and the eval runs.
- Chapter 12 needs the working Antigravity configuration.
- Chapter 13 needs to know whether the local machine is reachable from the training room.
- Chapter 18 needs the journals the group publishes in.

---

## 12. Done looks like

A chapter is finished when the premise survives review, the slides follow the argument rather
than a list, at least half carry a figure, every headline is a full-sentence claim, no banned
construction appears, every term is defined before use, the citation check passes, the PDF is
exported and committed, and the instructor has read it and agreed.

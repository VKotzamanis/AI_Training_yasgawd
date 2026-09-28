# Chapter 3 — critical review before rebuild

Written 2026-08-20, the same pass Chapters 1 and 2 got. The instructor has not annotated this
chapter, so nothing here reports his judgement.

**What I read.** `slides/03-control.md` in full, the Chapter 3 brief, the rubric-dimension material
in Chapter 2, and the two claims this chapter hands to Chapter 4.

---

## Summary

The premise is sound and the chapter contains the best pedagogical device in the course. It also
deviates from the slide specification more than any chapter rebuilt so far — **ten of its seventeen
headlines are phrases rather than assertions** — and it rests almost entirely on one vendor's
documentation about its own product, which the chapter never says out loud.

---

## The mechanical audit

| | Chapter 3 | Standard now in force |
|---|---|---|
| Slides | 18 | — |
| Slides with a figure | **1** | every slide |
| Slides with a footer | 10 | every slide |
| **Full-sentence headlines** | **7 of 17** | every headline |
| Distinct sources | **2** — one used 9 times | — |
| Banned constructions | 1 | zero |
| Running example | none | one per chapter |
| Term audit | none | required to finish a chapter |

**The headline problem is the largest single defect.** *Be specific*, *Say why, not just what*,
*Structure the input*, *Requesting reasoning*, *Thinking and effort*, *Negative examples, and their
cost* — these are topic labels. The assertion-evidence evidence in `research-slide-design.md` is
specifically about headlines: across fifteen exam questions, recall on information carried in a
sentence headline was 79% against 69% for the same information in body text. A phrase headline
throws that away, and it is the one design choice with converging experimental support behind it.

Two of them are also banned constructions in their own right. *Say why, not just what* is a negation
followed by an assertion. *Role — and exactly what is being claimed* is a fragment.

---

## The premise

**"The levers that work, and why they work — each maps to something that was rated."**

**Holds, and it is stronger now than when it was written.** Chapter 2 has been rebuilt to teach the
six rated dimensions with a figure and to close on four open questions, the first of which is
*"If instructions shaped it, which instructions steer it, and why those?"* Chapter 3 answers that
question and should open by answering it rather than by explaining its own placement.

The current opening frame is *"Why this chapter comes second"*, which argues about curriculum
sequencing to an audience that did not ask. The reason it comes second is real and belongs in the
speaker notes.

---

## The best device in the course, and it is under-used

Every technique on these slides carries a **maps to** line naming the rated dimension it steers.
That is what converts a list of tricks into a set of consequences, and it is the single strongest
structural idea anywhere in the nineteen chapters.

It is currently a footnote under each technique. **It should be the chapter's structure.** Walk the
six dimensions from Chapter 2 and, for each, give the lever that steers it:

| Rated dimension | The lever |
|---|---|
| Instruction following | say exactly what you want; give the reason; separate instruction from data |
| Formatting | show the format in an example rather than describing it |
| Tone | a role, and examples of the voice you want |
| Verbosity | ask for the length; the effort setting |
| Truthfulness | ask for the working rather than a verdict |
| Harmlessness | **no lever** — this is the one you cannot steer, and that is why some requests are refused |

That last row is informative rather than a gap. Five of six dimensions have a lever and one does
not, and saying so explains refusal behaviour better than a slide about refusals would.

---

## The sourcing problem, stated plainly

**Nine of eleven citations are one vendor documentation page.** The remaining two are the
chain-of-thought paper.

This is not dishonest — that page *is* the primary source for how to steer that product, and citing
it is correct. But a chapter about technique, in a course whose spine is source discipline, resting
almost entirely on one company's claims about its own product, should say so **on a frame** rather
than only in nine footers. The room will not add up the footers.

It also makes Chapter 4 load-bearing in a way the chapter currently under-sells. Two claims are
flagged for testing. Several others are equally testable and are presented as settled.

---

## What is genuinely strong

- **The role frame.** It separates what the documentation actually claims — that a role focuses
  behaviour and tone — from the claim people hear, that a persona improves accuracy, and hands the
  difference to Chapter 4 rather than settling it from intuition.
- **The three anti-patterns as rubric exploitation in reverse.** A leading question invites the
  agreement that was rewarded; asking for a verdict invites confidence that cannot be checked;
  constraint stacking produces silent dropping. Each is a lever pulled backwards, which is only
  possible because Chapter 2 came first.
- **The standing table.** Seven rows, five documented, two marked *not established*. It already
  does what I would otherwise have proposed inventing.
- **"Prompts do not port."** Correct, under-appreciated, and it sets up Chapter 12.
- **The chain-of-thought scope note.** The published result is eight worked exemplars on a
  540-billion-parameter model. Typing four words at a model that already reasons is a different
  proposition, and the chapter says so.

---

## What is missing

**1. Attaching a file or an image — and this is the largest gap in the chapter.** The room will
photograph a cracked specimen, screenshot a plot with an odd spike, and paste a two-column page of
a paper. It is plausibly the highest-value lever available to them and no chapter in the course
mentions it exists. Chapter 1 now says the window takes images; Chapter 3 is where you say what to
do with that.

**2. Which model, and when the choice matters.** They face a picker with several options and a
thinking toggle on day one. The course never mentions it.

**3. What a prompt is as an object.** Chapter 1 defined the context window and Chapter 2 defined the
system prompt. Chapter 3 uses both and never draws the thing: system prompt, your message,
attachments, the conversation so far, all landing in one window. That diagram is the chapter's
missing anchor, and every lever is a statement about one part of it.

**4. A running example.** Chapters 1 and 2 each carry one. Chapter 3 should take one weak prompt
from this room's work and improve it lever by lever, so each technique is shown rather than
described. The anti-patterns are then the same prompt done wrong.

**5. The standing on each lever's frame**, not only in the summary table. A reader who leaves before
the last frame should still know which claims were tested.

**6. Nothing shows a lever failing.** Chapters 1 and 2 both show the mechanism breaking. Every
technique here is presented working.

---

## Smaller findings

- **The opening frame argues about curriculum placement.** Move the reasoning to the notes.
- **"You are on the other side of the rubric now"** is second-person dramatic address, which §5.1
  bans. The observation is good; it belongs in the notes or as a plain statement.
- **The `budget_tokens` and effort-versus-length facts are version-fragile** and correctly hedged.
  They were verified 2026-08-19 and must be re-fetched in delivery week.
- **The prerequisites frame** quotes the vendor's own list, including *some way to test empirically
  against those criteria*. That is the strongest available argument for Chapter 4 and it is
  currently a bullet.

---

## Proposed structure

Ordered by what each lever steers, which makes the premise the structure.

| | Frame | Rests on |
|---|---|---|
| 1 | Title | — |
| 2 | Which instructions steer it, and why those | answers Ch2's closing question |
| 3 | A prompt is four things arriving in one window | the anatomy diagram |
| 4 | Every lever steers something that was rated | the mapping diagram |
| 5 | Before any of it, you need a way to tell whether a change helped | vendor documentation |
| 6 | Say exactly what you want, and what the output should look like | vendor + running example |
| 7 | Give the reason for a constraint and it covers cases you did not list | vendor |
| 8 | Separate the instruction from the data | vendor |
| 9 | Show the format instead of describing it | vendor |
| 10 | A negative example still puts the unwanted pattern in the window | vendor |
| 11 | A role changes voice; the accuracy claim is a different one | vendor, flagged for Ch4 |
| 12 | Ask for the length you want | vendor |
| 13 | The model decides how much to think, and you can bias it | vendor, version-fragile |
| 14 | Ask for the working rather than the verdict | derived |
| 15 | Hand it the figure rather than describing the figure | vendor documentation, new |
| 16 | Which model you pick, and when it matters | new, needs sourcing |
| 17 | Pulling a lever backwards asks for the trained behaviour | derived |
| 18 | Anti-pattern: a question with its answer visible in it | derived |
| 19 | Anti-pattern: asking for a verdict | derived |
| 20 | Anti-pattern: constraints that cannot all hold | derived |
| 21 | A prompt tuned on one model is untested on another | vendor |
| 22 | What you can act on, and what you should test first | the standing table |
| 23 | What we covered, and what is still open | — |

---

## What I did not do

- **I did not re-fetch the vendor documentation.** Its `[V]` tag dates from 2026-08-19. The two
  version-fragile facts on the thinking frame need re-checking before delivery, and I have not done
  it.
- ~~I did not source the model-choice frame.~~ **Done after this review was written.** Two vendor
  pages were fetched as primary text and verified, and both are logged. The frame that resulted is
  not the recommendation table the review imagined: the vendor's own guidance is written for API
  callers, and it does not put the effort dial in the chat app for the current models, so the slide
  cannot tell this room to set it. What survived verification is better suited to the audience —
  the **reliable knowledge cutoff**, published per model and defined as distinct from the
  training-data cutoff. Whichever model is picked, there is a date past which the literature is not
  in it, and that decides more answers for this room than the capability ordering does.
- **I did not check whether the three anti-patterns overlap Chapter 17**, which teaches asking for
  analysis rather than a verdict as a deliberate technique. That may be intended reinforcement or
  duplication; deciding needs the two read together.
- **I did not review `assets/eval-worksheet/README.md`**, which is where the two flagged claims are
  actually settled.

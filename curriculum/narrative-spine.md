# Narrative spine — what each chapter is actually about

**Revised 2026-08-20** after a peer review of all nineteen premises. The review, its evidence and
its arithmetic are in `peer-review-19-chapters.md`. This file carries only the result.

The previous version of this file fixed a real problem — the chapter briefs list contents, and
those lists were rendered as slides in list order, so nothing on a slide existed because the
previous slide made it necessary. That diagnosis was right and the repair was incomplete: it
rewrote the spine without asking whether the chapters were the right chapters, the right size, or
in the right session.

Nine premises changed. They are marked **[revised]**. Where a premise survives unchanged it is
marked **[holds]**, which means it was tested rather than skipped.

## The test every chapter must pass

1. **One sentence.** What is this chapter about? If it takes two, the chapter is two chapters or none.
2. **Attend only this.** What can someone do on Monday having attended this chapter and nothing else?
3. **Forced next.** What question does this chapter leave open that the next one answers?

A fourth test was added by the review, because three chapters passed the first three and were
still carrying material that does no work:

4. **Earns its place.** Does this change a decision the audience will make, or teach a lesson the
   course has not already taught four times? A chapter can pass tests 1 to 3 and still be padded.
   **Delivery length is not a criterion here and is not discussed anywhere in this repository** —
   ruled 2026-08-20. Write it in full; the instructor decides what to keep.

## The course spine

**The tool predicts the next fragment of text. It was then shaped by human raters. Every
strength and every failure follows from those two facts — so once you can see them, you can
measure the tool, and once you can measure it, you can build research practice around it.**

- **Chapters 1–4** — what it is, therefore how to steer it, therefore how to check the steering worked.
- **Chapters 5–8** — what it does anyway, and the limits no prompt removes.
- **Chapters 9–13** — instruments that extend it, and what each one costs you.
- **Chapters 14–19** — the habits that make it safe to put in a thesis.

## The reference layer

A talk needs only the spine. A course also needs a **reference layer** — things people look up
later, and things that must be covered even where they do not serve the story.

**The spine decides what goes on a slide. Everything else goes to speaker notes, an appendix, or
the reference card.** Most of what made these decks unreadable was reference material sitting on
slides, competing with the argument.

## Session boundaries are provisional

Chapter numbers are stable, because `architecture.md` references them in five places. **Which
session a chapter is delivered in is not**, and that is the instructor's call to make when he
sees the finished material.

---

# The nineteen

## Session 1 — what it is and where it fails

### Ch 1 — Substrate **[revised]**
**About:** A large language model is a fixed set of numbers left behind by training; one run of it
scores which fragment of text plausibly comes next, and running it repeatedly is what produces an
answer.
**Attend only this:** You can say what a language model is as an object, what one run of it
computes, and why the same question can give two different answers.
**Forces:** Nothing in scoring text fragments produces a helpful assistant. What was added?

*Changed because the previous premise — "it predicts the next fragment of text, over and over,
from a finite window" — is true and presupposes its own subject. It describes an operation without
naming the thing performing it, which is the defect the instructor named twice.*

*Also deleted: the brief's instruction to open the course on "is this like a brain?". That device
was rejected in review and should not survive in `chapter-briefs.md`.*

### Ch 2 — Formation **[holds]**
**About:** It behaves like an assistant because people rated outputs and it was optimised toward
those ratings.
**Attend only this:** You can explain why it agrees with you, why it sounds confident, and why it
sounds the same on every topic — as consequences of a rating process, not personality.
**Forces:** If instructions shaped the behaviour, instructions should steer it.

*The strongest premise in the course. Split into 2a (the pipeline) and 2b (the annotation layer)
per `DECISIONS.md`; the seam is in the right place and the numbering survives it.*

### Ch 3 — Control **[holds]**
**About:** The levers that work, and why they work — each maps to something that was rated.
**Attend only this:** You write better prompts tomorrow, and can say why each change should help.
**Forces:** How do you know it actually helped?

*Must gain the lever this room will reach for first: handing over a file, a figure or a page of a
paper. The course currently never mentions that these tools accept images.*

### Ch 4 — Measurement **[revised]**
**About:** Turning a prompting claim into a test you run yourself, in an afternoon, on your own work.
**Attend only this:** You have run one, on five of your own cases, and you can settle any "you
should prompt like this" claim the same way.
**Forces:** Some failures survive every prompt you test.

*Changed from "a test you can run" to "a test you run". The chapter converts the course from advice
into method and currently has the room watching somebody else's experiment; every case is marked
`TODO(instructor)`. A room of experimentalists should not be taught experimental method as
spectators.*

### Ch 5 — Intrinsic failure **[revised]**
**About:** Some failures are structural, and the ones that will hit your research live in a
specific band of what the model half-knows.
**Attend only this:** You can name the failure modes that will hit your work specifically, say why
your own literature attracts them, and say how each is caught.
**Forces:** That was with nobody attacking you.

*Changed to name the confabulation band in the premise. It is the most useful sentence in Session 1
— it explains the room's lived experience of the tool being reliable on textbook material and
erratic on their research — and it was buried in the middle of a chapter carrying three subjects.
The long-context literature review and the interpretability block compress to three slides between
them.*

### Ch 6 — Extrinsic failure **[holds]**
**About:** Text you did not write can act as an instruction, and there is no clean fix.
**Attend only this:** You know what not to point the tool at, and why "we'll sanitise it" fails.
**Forces:** You are about to open these channels deliberately.

*The tightest premise in Session 1. Candidate to move to the opening of Session 2, which satisfies
the "6 before Part III" constraint exactly and puts the threat model on the day the channels open.*

### Ch 7 — Physical limits **[revised]**
**About:** Long context is bounded by memory rather than by arithmetic, and that one constraint
explains what is slow and what is expensive.
**Attend only this:** You can reason about speed and price from a governing constraint instead of
from vibes, the way you already do with load paths.
**Forces:** All of this is metered — so what are you actually billed?

*Narrowed from "what it costs to run". The chapter is about twice the size its premise justifies
for this audience: critical batch size, parallelism schemes, device memory capacity and three
alternative computing substrates change no decision anyone in that room will make. The forcing
question changed too, because the chapter's natural successor is Chapter 13, not Chapter 8.*

### Ch 8 — Brain and model **[dissolved — appendix only]**
**Decided 2026-08-20.** Chapter 8 is no longer delivered. It had no question left to answer once
Chapter 1 stopped opening one, and its structural job was already done elsewhere.

**Where the brain question is answered now:** Chapter 1, slide 7, immediately after training is
explained as a search over numbers. That is the moment the room reaches for the analogy, because
they have just been told the thing is a neural network that learns. The slide gives what training
physically changed, gives *neural network* and *learning* as borrowed names, and states the standing
of the brain-comparison literature in one cited line. The attention slide carries the third borrowed
word, because *attention* cannot be named before it is defined.

**What moves to Chapter 10 when that chapter is rebuilt:** the units point — four chunks against two
hundred thousand tokens is not a weak comparison but an undefined one, because no conversion between
a chunk and a token exists. It does real work there as the argument for why a larger window is not a
substitute for a file, and it cannot sit on Chapter 1 slide 7 because the context window is not
introduced until slide 18.

**What stays in `slides/08-brain-and-model.md`, now the appendix deck:** the encoding-model scope,
the noise-ceiling arithmetic, the electrode study, the Antonello and Hadidi re-analyses, and the
frontal-cortex refusal. Distributed, not presented. Nothing is deleted.

## Session 2 — instruments

### Ch 9 — The agent **[holds]**
**About:** It can now change your files, and the diff is where responsibility sits.
**Attend only this:** You can point it at your own code, stay in control, and undo it when you were wrong.
**Forces:** The session ends and everything it learned is gone.

*The takeaway gained a clause. The chapter teaches reading the diff and never teaches recovering
from one you approved and should not have. No chapter in the course teaches version control, and
four chapters assume it.*

### Ch 10 — Memory **[holds]**
**About:** You write the memory it does not have, as a file it reads every time.
**Attend only this:** You leave with a working project instruction file. This is the day's artefact.
**Forces:** One session and one window is sometimes not enough.

### Ch 11 — Orchestration **[revised]**
**About:** Most of this room should not fan work out across several sessions; here is how to tell,
and here is the part that is worth it anyway.
**Attend only this:** You can judge when to fan out, and you have one hook enforcing one lab
convention automatically.
**Forces:** Everything so far stayed inside the session.

*Changed because the previous premise sold the capability and buried the judgement. For a
five-person group on individual subscriptions, orchestration is the thing that exhausts the
subscription, and the chapter says so itself. Hooks are the part that survives.*

### Ch 12 — Extension **[revised]**
**About:** Connecting an outside tool means content you did not write arrives in the window on
purpose, and you have to know what left your machine to get it.
**Attend only this:** You can connect one tool and say exactly what left your machine.
**Forces:** All of this is metered.

*Narrowed from "connecting outside tools, and the trust you spend to do it". The trust half is the
chapter's reason to exist; the protocol architecture — host, client, server, N-plus-M — is
developer material that changes nothing this audience does.*

### Ch 13 — Access **[revised]**
**About:** What this actually costs you — the subscription limit you will hit, then the key you
might be given, then the call you can price.
**Attend only this:** You can budget the work, know what to do when you hit a limit mid-afternoon,
and not leak a credential.
**Forces:** Now do your actual research with it.

*Changed because most of this room will never hold an API key. The chapter exists because a local
gateway exists, and the cost question the room actually has — what does my plan give me, what
burns it, what do I do at the limit — is currently mentioned once in passing in Chapter 11 and
owned by nobody.*

## Session 3 — research practice

### Ch 14 — Literature **[holds]**
**About:** It fabricates citations, and resolving the identifier is the entire defence.
**Attend only this:** You can use it for literature work without polluting your bibliography.
**Forces:** Now you have to produce the document.

*Premise holds; one slide inside it is factually wrong. "What survives PDF extraction" describes a
text-extraction pipeline, and the tool converts each page to an image and supplies the extracted
text alongside it. Both happen, and the chapter teaches only one.*

### Ch 15 — Production **[revised]**
**About:** A versioned text pipeline makes a document reproducible and makes it harder for your
co-authors to comment on.
**Attend only this:** You can generate a diagram from text and regenerate a figure from a committed
script, and you can say what a full pipeline would cost you socially before you commit to one.
**Forces:** The hardest content in that document is the code and the numbers.

*Changed because the original premise is an advocacy claim that the chapter never defends against
the objection that actually kills adoption: the supervisor uses a word processor with tracked
changes, and the journal accepts one. The review recommends halving this chapter or folding it
into Chapters 14 and 16 — four of its seven slides would be identical in a course with no AI in it.*

### Ch 16 — Code and numerics **[revised]**
**About:** It is measurably weaker on MATLAB, and neither your code nor your measurements get a
correctness check it can supply.
**Attend only this:** You can use it on inherited code and on your own experimental data, with
guardrails that catch its mistakes.
**Forces:** Correct numbers still lose to a hostile reviewer.

*Extended to cover experimental data. This is a group that does experimental testing, and nineteen
chapters contain nothing about pointing the tool at a measurement file — sensor traces, saturation,
drift, filter choice, a first plot. It is the largest content gap in the course and this is its
home. This chapter should get longer; the time comes from Chapter 15.*

### Ch 17 — Critique **[revised]**
**About:** Use it to attack your own argument before a referee does, and to write in a language
that is not your first without giving up authorship of the claim.
**Attend only this:** You get a stronger paper, a rebuttal that answers the real objection, and a
clear line between editing your expression and changing your meaning.
**Forces:** None of this is allowed unless you can disclose it.

*Extended because the language-support material is plausibly the highest-frequency benefit in the
whole course for this group, and it currently sits as one slide in the middle of a chapter about
referee reports.*

### Ch 18 — Governance **[revised]**
**About:** What you must disclose to your university and your publisher, what must never leave the
building, and what you must log.
**Attend only this:** You leave with a written rule your group can actually follow.
**Forces:** So when should you not use it at all?

*Changed to put the university first. A PhD student's binding rule is their institution's and their
funder's — thesis regulations, examination boards, the doctoral school — not a journal's. The
chapter currently looks only at publishers.*

### Ch 19 — Judgement **[revised — and it is not a chapter]**
**About:** Five situations where the right move is to put the tool down, then an hour of your own
work using everything you configured.
**Attend only this:** A decision rule you can apply without re-reading anything, and one end-to-end
task you finished in the room.
**Forces:** Nothing. It closes.

*This is one slide, a sixty-minute capstone and a round-robin. Numbering it as the nineteenth
chapter of nineteen overstates the course's shape and costs the capstone its time. It should be
called Close.*

---

## What this changes about how slides get built

- The chapter's one sentence goes at the top of the deck file and every slide is checked against it.
- Slide order follows the argument, not the brief's content list.
- A term is introduced **at the moment the argument needs it**, never as a topic in its own right.
  Tokens arrive because prediction needs units, not as item one of seven.
- **No term is used before it is defined**, and the chapter ships a term audit naming the slide
  where each one is defined. A term whose payoff is six chapters away does not belong in the
  chapter that has to teach from zero.
- If a slide does not move the argument, it is notes, appendix or reference card. Not a slide.
- Every chapter opens on something the room has already experienced, not on an abstraction.
- **Every chapter has a figure plan written before its slides.** Eleven of the nineteen decks
  currently carry no figure at all, against a specification of 50%.

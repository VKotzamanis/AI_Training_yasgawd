# Narrative spine — what each chapter is actually about

Written 2026-08-20 after Chapter 1 failed review. The failure was not audience calibration.
It was method: the chapter briefs list contents, and I rendered those lists as slides in list
order. A list is not an argument. Nothing on a slide existed because the previous slide made it
necessary, so there was no flow to follow.

This file fixes that at the level where it broke — the spine, not the wording.

## The test every chapter must pass

1. **One sentence.** What is this chapter about? If it takes two, the chapter is two chapters or none.
2. **Attend only this.** What can someone do on Monday having attended this chapter and nothing else?
3. **Forced next.** What question does this chapter leave open that the next one answers?

A chapter that fails (2) is a lecture. A chapter that fails (3) is a leaf, and the course is a list again.

## The course spine

**The tool predicts the next fragment of text. It was then shaped by human raters. Every
strength and every failure follows from those two facts — so once you can see them, you can
measure the tool, and once you can measure it, you can build research practice around it.**

- **Chapters 1–4** — what it is, therefore how to steer it, therefore how to check the steering worked.
- **Chapters 5–8** — what it does anyway, and the limits no prompt removes.
- **Chapters 9–13** — instruments that extend it, and what each one costs you.
- **Chapters 14–19** — the habits that make it safe to put in a thesis.

## The one adjustment to the TED framing

A talk needs only the spine. A course also needs a **reference layer** — things people look up
later, and things that must be covered even where they do not serve the story.

That does not weaken the narrative rule. It is what makes it possible. **The spine decides what
goes on a slide. Everything else goes to speaker notes, an appendix, or the reference card.**
Most of what made these decks unreadable was reference material sitting on slides, competing
with the argument.

---

# The nineteen

## Session 1 — what it is and where it fails

### Ch 1 — Substrate
**About:** It predicts the next fragment of text, over and over, from a finite window.
**Attend only this:** You can explain what the thing actually does, and predict why the same
question gives different answers on two runs.
**Forces:** If it only predicts text, why does it behave like an assistant?

### Ch 2 — Formation
**About:** It behaves like an assistant because people rated outputs and it was optimised toward
those ratings.
**Attend only this:** You can explain why it agrees with you, why it sounds confident, and why it
sounds the same on every topic — as consequences of a rating process, not personality.
**Forces:** If instructions shaped the behaviour, instructions should steer it.

### Ch 3 — Control
**About:** The levers that work, and why they work — each maps to something that was rated.
**Attend only this:** You write better prompts tomorrow, and can say why each change should help.
**Forces:** How do you know it actually helped?

### Ch 4 — Measurement
**About:** Turning a prompting claim into a test you can run in an afternoon.
**Attend only this:** You can settle any "you should prompt like this" claim on your own work.
**Forces:** Some failures survive every prompt you test.

### Ch 5 — Intrinsic failure
**About:** Some failures are structural — better prompting does not remove them.
**Attend only this:** You can name the failure modes that will hit your research specifically,
and how each is caught.
**Forces:** That was with nobody attacking you.

### Ch 6 — Extrinsic failure
**About:** Text you did not write can act as an instruction, and there is no clean fix.
**Attend only this:** You know what not to point the tool at, and why "we'll sanitise it" fails.
**Forces:** You are about to open these channels deliberately.

### Ch 7 — Physical limits
**About:** What it costs to run, and why long context is expensive and slow.
**Attend only this:** You can reason about speed and price from first principles instead of vibes.
**Forces:** It is fast, expensive and forgetful — is it anything like a brain?

### Ch 8 — Brain and model
**About:** The brain comparison generates hypotheses but fails as an explanation, and it fails
hardest on memory.
**Attend only this:** You can answer "is it like a brain?" without hand-waving in either direction.
**Forces:** It has no memory. So you have to supply one.

## Session 2 — instruments

### Ch 9 — The agent
**About:** It can now change your files, and the diff is where responsibility sits.
**Attend only this:** You can point it at your own code and stay in control.
**Forces:** The session ends and everything it learned is gone.

### Ch 10 — Memory
**About:** You write the memory it does not have, as a file it reads every time.
**Attend only this:** You leave with a working project instruction file. This is the day's artefact.
**Forces:** One session and one window is sometimes not enough.

### Ch 11 — Orchestration
**About:** Delegating across several context windows — and when that is just an expensive way to
do something simple.
**Attend only this:** You can judge when to fan out and when not to.
**Forces:** Everything so far stayed inside the session.

### Ch 12 — Extension
**About:** Connecting outside tools, and the trust you spend to do it.
**Attend only this:** You can connect one tool and say exactly what left your machine.
**Forces:** All of this is metered.

### Ch 13 — Access
**About:** Keys, and what a call actually costs.
**Attend only this:** You can budget the work and not leak a credential.
**Forces:** Now do your actual research with it.

## Session 3 — research practice

### Ch 14 — Literature
**About:** It fabricates citations, and resolving the identifier is the entire defence.
**Attend only this:** You can use it for literature work without polluting your bibliography.
**Forces:** Now you have to produce the document.

### Ch 15 — Production
**About:** A versioned text pipeline beats a word processor when the document must be reproducible.
**Attend only this:** You can build the pipeline and retarget one manuscript to a second journal.
**Forces:** The hardest content in that document is the code and the numbers.

### Ch 16 — Code and numerics
**About:** It is measurably weaker on MATLAB, and numerical correctness needs a check it cannot supply.
**Attend only this:** You can use it on inherited code with guardrails that catch its mistakes.
**Forces:** Correct numbers still lose to a hostile reviewer.

### Ch 17 — Critique
**About:** Use it to attack your own argument before a referee does.
**Attend only this:** You get a stronger paper, and a rebuttal that answers the real objection.
**Forces:** None of this is allowed unless you can disclose it.

### Ch 18 — Governance
**About:** What you must disclose, what must never leave the building, and what you must log.
**Attend only this:** You leave with a written rule your group can actually follow.
**Forces:** So when should you not use it at all?

### Ch 19 — Judgement
**About:** Five situations where the right move is to put the tool down.
**Attend only this:** A decision rule you can apply without re-reading anything.
**Forces:** Nothing. It closes.

---

## What this changes about how slides get built

- The chapter's one sentence goes at the top of the deck file and every slide is checked against it.
- Slide order follows the argument, not the brief's content list.
- A term is introduced **at the moment the argument needs it**, never as a topic in its own right.
  Tokens arrive because prediction needs units, not as item one of seven.
- If a slide does not move the argument, it is notes, appendix or reference card. Not a slide.
- Every chapter opens on something the room has already experienced, not on an abstraction.

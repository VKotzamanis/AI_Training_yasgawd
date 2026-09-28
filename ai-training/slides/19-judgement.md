---
theme: default
title: Chapter 19 — Judgement
info: One slide to hold in the head, a capstone on the attendee's own work, and distribution. Closes the course.
class: text-left
mdc: true
---

# Chapter 19 — Judgement

### When not to use any of this

<div class="mt-10 text-xl opacity-85">

Eighteen chapters of capability. This one is about the five places you should put it
down.

</div>

<!--
- **Says:** The title slide frames the chapter as identifying where to put eighteen chapters of capability down, describing five places to stop.
- **From:** Chapter 18 closed on writing down a group's data rule, a disclosure sentence, and one agreed convention, and this chapter turns to when none of that infrastructure should be used at all.
- **Chapter:** Opens the capstone chapter that the course architecture designates as the final one.
- **To:** Sets up the full list of tests on the next slide.
-->

---

## The slide to hold in the head

<v-clicks>

- **Not for a novel derivation.** If the step has never been written down, there is nothing to predict from. You are asking a next-token predictor to be first.
- **Not for anything you cannot verify.** If there is no check you can actually run, stop. If a check exists but costs more than doing the work yourself, that is a different judgement — you have moved work rather than saved it, which is a trade, not a prohibition.
- **Not where the failure would be silent.** A wrong sign that still runs, a plausible coefficient, a citation that resolves to a real paper saying something else.
- **Not with data that cannot leave the building.** Unpublished results, sponsor-confidential geometry, anything under an NDA.
- **Not where the input is untrusted and the output gets acted on.** A poisoned document plus file access is Chapter 6, and none of the four tests above catches it — they all govern what goes *out*, and this one comes *in*.

</v-clicks>

<div v-click class="mt-8 text-lg">

Five tests. Four are about what you send and what you can check. **The fifth is about what
you let in**, and it is the one a confidentiality rule will not cover for you.

</div>

<!--
- **Says:** Enumerates the five tests for when not to use the tool — a novel derivation, anything unverifiable, a failure that would be silent, data that cannot leave the building, and untrusted input with file access — and splits them into four outbound tests plus one inbound test.
- **From:** Follows the title slide's framing by delivering the actual list the chapter is built around.
- **Chapter:** Is the "one slide held in the head" that the deck names as its central content.
- **To:** Sets up the slide explaining why these five and not a longer list.
-->

---

## Why these five and not a longer list

<v-clicks>

- **Novel derivation** follows from Chapter 5, not Chapter 1. Prediction over a corpus plainly produces sentences that were never in it — the course spends eighteen chapters on that. The real argument is density: where the data was thin, plausible and true come apart, **and nothing in the system detects which regime it is in.** A step nobody has written down is the thinnest region there is.
- **Cannot verify** follows from Chapter 4. Without a check you cannot tell an improvement from a coincidence, and Chapter 5 says fluent output is not evidence of correctness.
- **Silent failure** follows from the failure gallery, once it is built: every item in it will be there *because something caught it*. The dangerous class is the one with nothing to catch it, and by construction it cannot appear in the gallery.
- **Data that cannot leave** follows from Chapters 12 and 18. You opened those channels deliberately; this is the boundary you set.
- **Untrusted input** follows from Chapter 6, which the architecture makes the gate for everything in Part III. Instructions and data share one channel and there is no complete defence, so the control is what you point it at.

</v-clicks>

<div v-click class="mt-6 text-lg">

A longer list would be forgotten by Thursday. These five are derivable from the course,
which is why they will survive it.

</div>

<!--
- **Says:** Traces each of the five tests back to the chapter it derives from — novel derivation to Chapter 5, unverifiability to Chapter 4, silent failure to the failure gallery, data that cannot leave to Chapters 12 and 18, and untrusted input to Chapter 6.
- **From:** Follows the five-tests slide by justifying each test's presence rather than adding new ones.
- **Chapter:** Ties the capstone list back to the whole course, arguing the five are memorable because they are derivable rather than arbitrary.
- **To:** Sets up the "what has not changed" slide.
-->

---

## What has not changed

<v-clicks>

- The claim is yours. The interpretation is yours. The responsibility for correctness is yours.
- None of those is delegable, and no disclosure statement makes them so.
- A tool that drafts faster raises the volume you are accountable for. That is the trade you have actually made this term.

</v-clicks>

<!--
- **Says:** Restates that the claim, the interpretation, and the responsibility for correctness remain the attendee's, and names faster drafting as raising the volume they are accountable for.
- **From:** Follows the derivation-tracing slide by restating the non-delegable core first stated in Chapter 18, now as the course's standing conclusion.
- **Chapter:** Reasserts the chapter's non-delegable-three point immediately before the capstone task that exercises it.
- **To:** Leads into the capstone task slide.
-->

---

## Capstone

One end-to-end task on your own work, using what you configured across the three
sessions.

<v-clicks>

- Your project instruction file from Chapter 10.
- Your eval worksheet from Chapter 4, on a claim you are relying on.
- Your verification habit from Chapter 14, on every source it hands you.
- Your disclosure position from Chapter 18, written down before you need it.

</v-clicks>

<div v-click class="mt-6 p-4 border-l-4" style="border-color:#0E5C68; background:#F2F7F8">

**The check, stated before you start:** at the end of the hour you can name what you
verified, how you verified it, and what you could not. A finished artefact with none of
those three is a failed capstone.

</div>

<div v-click class="mt-4 text-sm opacity-80">

If a piece of that stack is missing, that is the honest finding of the day, and it is more
useful than a finished artefact.

</div>

<!--
- **Says:** Defines the capstone task as one end-to-end piece of the attendee's own work using the project instruction file, eval worksheet, verification habit, and disclosure position from Chapters 10, 4, 14, and 18, with the check stated in advance as naming what was verified, how, and what could not be.
- **From:** Follows the "what has not changed" slide by turning its accountability claim into the graded task that tests it.
- **Chapter:** Is the course's capstone exercise, drawing on artefacts from four earlier chapters at once.
- **To:** Sets up the round-robin commitment slide.
-->

---

## Round-robin

<div class="mt-6 text-2xl">

One thing each person will use this week.

</div>

<v-clicks>

- Not the most impressive thing. The one you will actually do before Friday.
- Say it out loud. Committing in front of five colleagues is the only enforcement mechanism this course has.

</v-clicks>

<!--
- **Says:** Has each attendee commit out loud to one thing they will actually use before Friday, rather than the most impressive option.
- **From:** Follows the capstone slide by turning the just-completed task into a public, near-term commitment.
- **Chapter:** Gives the course its only enforcement mechanism, according to the slide itself.
- **To:** Leads into the closing distribution slide.
-->

---

## What you take away

<v-clicks>

- The repository — slides, run sheets, the eval worksheet, the failure gallery.
- The one-page reference card.
- A shared instruction file the group owns, not six private ones.

</v-clicks>

<div v-click class="mt-10 text-xl">

And the habit the whole course was built around: **state the check before you do the
work.**

</div>

<div v-click class="mt-4 opacity-80">

Everything else here has a shelf life. That does not.

</div>

<!--
- **Says:** Lists what attendees take away — the repository, the one-page reference card, and the group's shared instruction file — and names "state the check before you do the work" as the habit the whole course was built around.
- **From:** Follows the round-robin commitment by moving from a spoken commitment to the tangible and habitual things attendees carry out the door.
- **Chapter:** Closes Chapter 19 and the course on the single durable habit, distinguished explicitly from everything else that the slide says has a shelf life.
- **To:** Closes the course, so there is no next chapter — the attendee leaves with the repository, the reference card, the shared instruction file, and the "state the check before the work" habit.
-->

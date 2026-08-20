# START HERE

Setup and first tasks for working on this repository in Claude Code.

---

## 1. Setup

```bash
unzip ai-training.zip && cd ai-training
git init && git add -A && git commit -m "Initial curriculum plan"
```

Open the folder in Claude Code — desktop app, VS Code, or terminal. `CLAUDE.md` loads automatically as standing context.

**Don't run `/init`.** It would generate a CLAUDE.md over the one already written, which encodes rules that took a long conversation to arrive at.

**Run `/doctor` once** after the first session to check the setup and to see the context accounting. You'll be teaching this command in Chapter 9; running it on your own repo first is worth five minutes.

---

## 2. Read in this order

| File | Why |
|---|---|
| `CLAUDE.md` | Seven hard rules. The first three are the ones that matter. |
| `curriculum/architecture.md` | Nineteen chapters, five cross-cutting threads, ten sequencing constraints |
| `DECISIONS.md` | What's locked, what's open, what blocks drafting |
| `references.md` | Citations with verification status, plus search terms for material still to gather |
| `curriculum/chapter-briefs.md` | Content inventory per chapter |
| `curriculum/ch02-annotation-findings.md` | Chapter 2's differentiating material. Dense. Read §0 and §13 first. |

---

## 3. Two things block drafting

**Chapter 2 needs 105–115 minutes against a 75-minute budget.** Four options in `DECISIONS.md`; the recommendation is a 2a/2b split, which preserves the chapter numbering the thread map depends on. Decide before writing any Chapter 2 slide.

**Slidev is unproven for this content.** `slides/README.md` names one first task: build Chapter 7's hardest derivation, stepwise across clicks, with a citation footer attached. KaTeX handles roofline algebra; multi-line aligned derivations revealed progressively are the risk. Half a day answers it. Reversal triggers are in `DECISIONS.md` — read them before building workarounds for anything that fights you.

---

## 4. Where to start

**Module 4's eval worksheet.** Independent of both blockers, and it needs experimental work done before slides exist: pick two or three prompting claims, build a five-case eval, run them, record what happened. A demo where the folk wisdom loses is worth more than one where it wins.

**Then the Slidev spike** (§3), because it's cheap and it decides the toolchain.

**Then Chapter 2**, once the split is settled.

Useful first prompts:

```
Read CLAUDE.md, curriculum/architecture.md and DECISIONS.md.
Summarise what blocks drafting and what you'd do first.

Build the Chapter 7 derivation spike described in slides/README.md.
Stop at the spike — don't write the rest of the chapter.

Draft the eval worksheet for Module 4: five test cases from
wave-energy work, a pass criterion, and a tally sheet.
```

---

## 5. Rules worth knowing before you start

**Two tag systems, not interchangeable.** `references.md` uses `[V]/[P]/[U]/[X]` for whether a published source has been checked. `curriculum/ch02-annotation-findings.md` uses `[E1]–[E4]` for the evidential strength of an observation drawn from vendor documents. An `[E1]` finding is corroborated across documents and still has no citable source. Claude Code will conflate these if you let it.

**Rank by evidence, not by force.** §0 of the findings file is a log of what happened when that rule wasn't followed — a compelling narrative survived two revisions before the evidence killed it. Keep the correction log; it's what lets you defend the chapter.

**Vendor documents inform structure only.** No worked example — prompt, rubric row, banned-phrase list, persona, project name — gets reproduced or paraphrased. Rebuild mechanisms from scratch on your own domain.

**Assert before you edit.** Scripted edits assert their anchor exists and get grepped back afterwards. A script that completes is not a script that edited.

---

## 6. Which model

**Opus 5 for almost all of this.** It's the default on Max and the strongest model on Pro, and it handles curriculum drafting, markdown, Slidev authoring and light scripting without strain.

**Fable 5 is a Mythos-tier model** — Anthropic's most capable widely released model, built for long-horizon agentic work. <cite index="216-1">In Claude Code it needs version 2.1.170 or later, and the model picker marks the row "Requires usage credits" when your plan bills it that way.</cite>

**The cost picture decides it:**

- <cite index="213-1">On Max, and on premium Team and seat-based Enterprise seats, Fable 5 counts toward your plan's limits and you can spend up to 50% of your weekly allowance on it at no extra cost.</cite>
- <cite index="226-1">On Pro it is metered through usage credits from the first message.</cite>
- <cite index="227-1">It draws on the same limits as other models but consumes them at a higher token rate, so limits run out roughly twice as fast.</cite>

**Recommendation.** Default to Opus 5. Nothing in this project is the ambiguous, long-horizon, multi-session problem Fable is built for — the thinking has already been done and written down; what remains is execution against a detailed spec. Reach for Fable only if a long autonomous run genuinely stalls on Opus, and only if you're on Max where it's included.

If you're on Pro, don't use Fable here at all. It bills usage credits from the first message, and you would be paying a premium rate to draft markdown.

**One thing to expect if you do use Fable.** Some queries are routed to Opus 5 by a safeguards mechanism, which Anthropic tuned conservatively and says triggers in under 5% of sessions. Work on `assets/injection-demo/` — documents containing instructions aimed at an agent — is exactly the kind of thing that might. If a Fable session answers as Opus, that's the routing, not a fault.

---

## 7. Still open, not blocking

- Antigravity configuration, needed before Chapter 12 is written
- Attendee count — affects gateway capacity and pairing when someone hits a usage limit
- Delivery dates — version-dependent facts get re-checked the week before each session
- Which journals the group publishes in, for Chapter 18. ASCE is likely to matter most and is the one generic guides usually miss.
- Whether the deck travels outside the group

---

## 8. Safety

`assets/injection-demo/` will contain documents with instructions aimed at an agent. Do not read them into a session with file access or tool permissions, and do not execute anything from that directory. Build and test them on a machine you don't care about.

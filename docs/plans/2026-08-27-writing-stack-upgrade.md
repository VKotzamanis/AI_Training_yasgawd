# Writing-Stack Upgrade Implementation Plan

> **For agentic workers:** Execute tasks in order. Task 6 is a gate: the new skill
> deploys (Task 7) only if the GREEN criterion passes. Steps use checkbox (`- [ ]`)
> syntax. No git commits — the touched trees (`~/.claude`, this project) are not
> repositories.

**Goal:** Make the writing rules bind at generation time: a contract-based explanation
skill (tested per the writing-skills RED–GREEN–REFACTOR methodology), mechanical
trigger coverage for teaching material, prose-verification parity in CLAUDE.md, and
removal of two vendor skill payloads that contradict standing config.

**Architecture:** Config hygiene first (payload excision, trigger broadening,
CLAUDE.md verification line) — these need no skill test. Then the skill: drafted to
staging, baseline-tested WITHOUT it (RED), compliance-tested WITH it (GREEN, 5 reps
each, Sonnet subagents, manual read of every rep), deployed only on pass.

**Tech stack:** Claude Code Agent tool (Sonnet reps), Python for line-surgery edits
and regex trigger tests, markdown.

## Global Constraints

- Maximum two subagents concurrently (16 GB machine; a supplement-rewrite agent
  already holds one slot until it completes).
- Scripted edits assert their anchors before cutting and are grepped back afterwards
  (CLAUDE.md rule).
- **Iron-Law note (recorded deviation):** writing-skills forbids skill edits without a
  failing test. Task 1 edits two skills by *deleting vendor payload sections*. The
  documented failure is the conflict itself: the payload mandates ("MANDATORY
  graphical abstract", minimum figure quotas, "when in doubt, generate a figure")
  contradict CLAUDE.md's data-integrity rules and the agy image workflow. This is
  config hygiene — removing instructions the user never authored — not guidance
  design; no behavioural test is run for it, and this note is the record of that
  decision. The NEW skill (Tasks 4–7) follows the full RED–GREEN cycle without
  deviation.
- RED baseline evidence already on file: this session's CH1_SUPPLEMENT.md was
  written without any writing skill loaded and was rejected by the user for missing
  significance, necessity, and I/O ("It just presents some equations…"); the audit
  (`REVIEWD/AUDIT_NETWORK_SLIDES.md`) documents the specific defects. Task 5 adds
  the controlled 5-rep baseline the methodology requires.

---

### Task 1: Defuse the vendor payloads

**Files:**
- Modify: `~/.claude/skills/scientific-writing/SKILL.md` (delete lines 34–127: the
  "## Visual Enhancement with Scientific Schematics" section, including "### 
  Graphical Abstract (REQUIRED)" and "### Additional Figures (GENERATE
  EXTENSIVELY)" with its minimum-figure table, ending at the `---` on line 126)
- Modify: `~/.claude/skills/scientific-critical-thinking/SKILL.md` (delete lines
  27–60: the same vendor section in its milder form, ending at the `---` on line 60)

- [ ] **Step 1:** Python line-surgery, asserting before cutting that the first
  deleted line starts with `## Visual Enhancement with Scientific Schematics` and
  the line after the cut starts with `## Core Capabilities`. Replace each deleted
  span with:

```
<!-- Local edit 2026-08-27 (session fa4fff58-1e02-46a0-9e27-b82f6d002096): removed the
vendor "Visual Enhancement with Scientific Schematics" section (mandatory graphical
abstract, minimum figure quotas, "when in doubt, generate a figure"). It conflicted
with CLAUDE.md: figures follow content and data integrity, never quotas, and image
generation runs through agy per the image-generation workflow. -->
```

- [ ] **Step 2: Verify.**
Run: `grep -ci "graphical abstract\|GENERATE EXTENSIVELY\|when in doubt, generate" ~/.claude/skills/scientific-writing/SKILL.md`
Expected: `1` (the Cell Press style note at old line 675 — legitimate, kept).
Run: `grep -ci "schematic" ~/.claude/skills/scientific-critical-thinking/SKILL.md`
Expected: `0` hits outside the local-edit comment (comment mentions none — so `0`).

---

### Task 2: Broaden the writing-clearly-and-concisely trigger

**Files:**
- Modify: `~/.claude/skills/skill-rules.json`

- [ ] **Step 1:** In the `writing-clearly-and-concisely` entry, replace the single
  intentPattern

```
"\\b(write|draft|revise|edit|polish|rewrite|tidy)\\b.{0,40}\\b(paper|section|abstract|intro|introduction|manuscript|report|readme|documentation|doc|chapter|thesis|protocol|proposal)"
```

with

```
"\\b(write|draft|revise|edit|polish|rewrite|tidy|creat\\w*|make|build|finish|produce|prepare)\\b.{0,40}\\b(paper|section|abstract|intro|introduction|manuscript|report|readme|documentation|doc|chapter|thesis|protocol|proposal|slides?|deck|supplement|handout|lecture|tutorial)\\b"
```

and extend its `reason` with: `" Extended 2026-08-27: teaching material (slides,
supplements, handouts) added after the CH1 supplement was authored with no writing
skill loaded — 'Finish Chapter 1' matched no verb, 'supplement' no noun."`

- [ ] **Step 2: Verify with a regex test table** (Python, the exact pattern):
  fires on: "Finish Chapter 1", "make these 7 slides", "create a supplement",
  "draft the handout", "polish the abstract"; does NOT fire on: "landslide risk
  analysis", "the deck of the vessel", "tidy the workshop". `json.load` the file
  afterwards to prove it still parses.

---

### Task 3: CLAUDE.md — prose-verification parity

**Files:**
- Modify: `~/.claude/CLAUDE.md`, `## Verification` section

- [ ] **Step 1:** Append one bullet after the "Weak criteria" bullet:

```
- Prose deliverables get the same discipline as numbers: before delivery, check the draft against its governing schema or rubric (the component contract for teaching material; the project rubric where one exists) and report that check's outcome like any other.
```

- [ ] **Step 2: Verify:** `grep -c "component contract" ~/.claude/CLAUDE.md` → `1`.

---

### Task 4: Stage the new skill

**Files:**
- Create: `/tmp/…/scratchpad/skill-staging/explaining-technical-material/SKILL.md`
  (staging — NOT `~/.claude/skills/` until Task 6 passes)

- [ ] **Step 1:** Write the file with exactly the content of **Appendix A** below.
- [ ] **Step 2: Verify:** `wc -w` ≤ 700; frontmatter has `name` and `description`;
  description starts "Use when" and contains no workflow summary.

---

### Task 5: RED — controlled baseline (5 reps, no skill)

- [ ] **Step 1:** Dispatch 5 fresh Sonnet subagents (≤2 concurrent), each with
  exactly this prompt and nothing else:

```
Write a one-page supplement section defining the reward model (RM) used in
large-language-model post-training, for an AI-literacy training aimed at
MATLAB-literate civil-engineering researchers with no machine-learning background.
The section sits in the training's Chapter 1 supplement, after sections on
pretraining and supervised fine-tuning. Include the mathematics (the Bradley–Terry
preference likelihood). Produce only the section text in markdown. Do not use any
tools; your final message is the section.
```

- [ ] **Step 2:** Score every rep manually against: F1 definition sentence;
  F2 explicit input→output ((prompt, response) → one scalar); F3 necessity (what
  fails without an RM); F4 enabled capability (observable in the product);
  F5 location (training-only; discarded at deployment); SIG equation carries a
  significance sentence; BAN no subtraction-definition, no contentless metaphor.
- [ ] **Step 3:** Record verbatim failures in **Appendix B** of this file. The
  failure is confirmed if ≥3/5 reps miss two or more of F2–F5. If ≤1/5 reps miss
  any field, the methodology says stop: the failure does not reproduce under
  control, and the skill is not authored (report this instead of proceeding).

### Task 6: GREEN — compliance test (5 reps, skill loaded) — GATE

- [ ] **Step 1:** Dispatch 5 fresh Sonnet subagents, each with: `"The following
  skill is loaded and governs your output. Follow it exactly.\n---\n"` + the full
  Appendix A text + `"\n---\n"` + the identical Task-5 prompt.
- [ ] **Step 2:** Score identically. **Pass criterion (stated before running):**
  ≥4/5 reps show all five contract fields, in a strip, BEFORE any displayed
  equation, with SIG satisfied and zero BAN hits — and the five reps converge on
  the same shape (variance is a metric; five different structures = wording not
  binding).
- [ ] **Step 3:** On failure: record the new rationalizations/omissions verbatim,
  tighten the skill per "Match the Form to the Failure" (strengthen the recipe, do
  not add prohibitions), re-run Task 6 once. Two failures → stop and report.

### Task 7: Deploy (only after Task 6 passes)

- [ ] **Step 1:** Copy staging → `~/.claude/skills/explaining-technical-material/SKILL.md`.
- [ ] **Step 2:** Add to `skill-rules.json`:

```json
"explaining-technical-material": {
  "reason": "Authored 2026-08-27 after an observed failure: the CH1 supplement presented equations without I/O, necessity, or enabled capability (user: 'it doesn't discuss their SIGNIFICANCE... what are their inputs and outputs'). GREEN-tested per writing-skills before deployment; test record in docs/plans/2026-08-27-writing-stack-upgrade.md.",
  "promptTriggers": {
    "keywords": ["training chapter", "lecture notes", "slide deck", "teaching material"],
    "intentPatterns": [
      "\\b(write|draft|creat\\w*|make|build|finish|produce|prepare|revise)\\b.{0,40}\\b(slides?|deck|supplement|handout|lecture|tutorial|training)\\b",
      "\\b(explain|teach|define)\\w*\\b.{0,40}\\b(component|architecture|equation|concept|term)s?\\b"
    ]
  }
}
```

- [ ] **Step 3:** CLAUDE.md, `## Skill Workflow and Web Search`, extend the
  **Academic writing** bullet — after the operational-documentation sentence,
  insert:

```
For teaching material — slides, decks, supplements, handouts, training chapters, tutorials — invoke `writing-clearly-and-concisely` and `explaining-technical-material`; that skill's component contract binds at every definitional home.
```

- [ ] **Step 4:** Update auto-memory: `ai-training-style-rules.md` gains a line
  pointing rule 6 (the contract) at the deployed skill as its global home.
- [ ] **Step 5: Verify:** `json.load` passes; `grep "explaining-technical-material" ~/.claude/CLAUDE.md` → 1 hit; skill file present; report RED/GREEN scores.

---

## Appendix A — SKILL.md (staged text, deployed verbatim on GREEN pass)

````markdown
---
name: explaining-technical-material
description: Use when producing or revising material meant to make a reader understand a technical system, method, or model — training slides, supplements, handouts, lecture notes, tutorials, explanatory sections of reports or documentation — especially when components, equations, or architecture diagrams are being defined.
---

# Explaining Technical Material

## Overview

A component is taught when its contract is stated before its mathematics. Equations
describe a mechanism; the contract says what enters, what leaves, why the component
must exist, and what it buys. Write the contract first, every time.

## When to use

- Defining any component, term, or equation in teaching or explanatory material
- Restructuring material a reader has called "just equations"

Not for: pure API/command reference lists, conversational answers, code comments.

## The component contract (required at every definitional home)

Wherever a component receives its definition, these five fields come first, in this
order, before any derivation:

| field | states |
|---|---|
| **Is** | one-sentence definition, positive form |
| **Signal** | input (name, type/shape) → output (name, type/shape) |
| **Needed because** | the concrete failure when the component is removed |
| **Enables** | the observable capability it buys in the deployed system |
| **Sits** | position in the pipeline; stage (training / inference / harness, or the domain's equivalent); scope |

Then the mathematics, then the code tie-in. The contract appears once, at the
definitional home; later mentions reference it.

## Order and connection

- Sections run in signal order — the order the data flows, never the order of
  mathematical difficulty.
- Each section opens by locating itself: "Between ⟨upstream, which hands it X⟩ and
  ⟨downstream, which expects Y⟩."
- A term is introduced with its bridge to what the reader has already seen. When the
  audience has only seen a behaviour, the bridge sentence comes before the name.

## The equation contract

Every displayed equation carries (a) its input and output in the surrounding
sentence, and (b) one significance sentence — what the equation buys, or what fails
without it. An equation with neither is a formula-sheet entry, not teaching.

## Worked example — the shape to copy

| | |
|---|---|
| **Is** | The tokenizer is a deterministic map from text to a sequence of token IDs. |
| **Signal** | text string → token IDs x₁:ₖ, each ID an index into the vocabulary |
| **Needed because** | network layers need a finite symbol set to place a probability distribution over; raw text has no fixed alphabet. |
| **Enables** | any input — typos, code, new words — becomes processable; token count sets cost and latency. |
| **Sits** | pipeline step 1, before the embedding; a separate artifact, trained before the network and then frozen. |

Then, and only then: the merge algorithm, the formal map, the code.

## Red flags — stop and restate positively

- A definition shaped "X is not A. It is B." with B undefined
- A metaphor or parallel carrying zero technical content
- A coined term where the field has a standard one
- A topic re-explained after its definitional home has closed
- A displayed equation with no significance sentence
- A definitional section with no contract

## Common mistakes

| mistake | reality |
|---|---|
| "The map T: text → V* states the I/O" | Notation implies; the contract states. Readers do not parse type signatures as teaching. |
| "The why is obvious from the derivation" | A derivation shows *that*, not *why needed*. Necessity is one sentence; write it. |
| "The contract would repeat the intro" | The intro motivates the chapter; the contract binds one component. Different scopes. |
| "This section is reference, not teaching" | If a learner reads it, it teaches. Reference-only material lives in its own file. |
````

## Appendix B — RED/GREEN test record

### Single-section RED (Task 5 as originally designed) — NOT CONFIRMED, closed after 3 of 5 reps

Scoring convention fixed after rep 1, before reps 2–3: a partial field (component
present, named sub-element absent) counts 0.5 of a miss.

| rep | F1 | F2 | F3 | F4 | F5 | SIG | BAN | miss-equivalent (F2–F5) |
|---|---|---|---|---|---|---|---|---|
| 1 | ✓ | ✓ | ✓ | 0.5 | 0.5 | ✓ | clean | 1.0 |
| 2 | ✓ | ✓ | ✓ | 0.5 | 0.5 | ✓ | clean | 1.0 |
| 3 | ✓ | ✓ | ✓ | 0.5 | 0.5 | ✓ | clean | 1.0 |

Failure criterion was ≥3/5 reps with miss-equivalent ≥2. After three reps at 1.0, the
criterion is arithmetically unreachable (maximum attainable: 2/5); reps 4–5 cancelled
on that arithmetic, not on judgment. Two findings stand: (a) the consistent partial
absences are exactly the two connective fields — F4 product-observable capability and
F5 deployment status — in otherwise locally complete definitions; (b) the control arm
is not guidance-free: the Task-2 trigger broadening fires on the test prompt itself
("Write a … supplement section"), so the baseline measured is the current stack minus
the new skill — the decision-relevant baseline, and a conservative one.

<!-- decision: red-scenario-redesign | status: adopted | supersedes: none -->
### Scenario redesign (pre-registered before rep 3's score was known)

The naturalistic failure (CH1_SUPPLEMENT.md, rejected by the user) occurred writing
~17 components in one pass, not one section in isolation. RED reruns once with
breadth pressure: five components in a single response, same audience, same no-tools
constraint. Failure criterion: ≥3/5 reps in which ≥2 of the five components have
miss-equivalent ≥2 on F2–F5. GREEN (if RED confirms) uses the identical breadth task
with the staged skill; pass: ≥4/5 reps where ≥4 of 5 components carry the full
contract before their mathematics, zero BAN hits, converging shape. If breadth RED
also fails to confirm, the skill is NOT deployed, the record states that the Task-2
trigger fix was the operative repair, and Tasks 6–7 are cancelled per the
writing-skills rule: no failing test, no skill.

### Breadth RED reps

Per component, miss-equivalent on F2–F5 (0.5 per partial). Components at ≥2 are the
failure signal; criterion: ≥3/5 reps with ≥2 such components.

| rep | tokenizer | embedding | attention | softmax+T | reward model | components ≥2 |
|---|---|---|---|---|---|---|
| 1 | 0 | 0.5 | 1.5 | 0.5 | 1.0 | 0–1 |
| 2 | 0 | 0.5 | 0.5 | 0 | 1.0 | 0 |
| 3 | 0.5 | 0.5 | 1.0 | 0 | 1.0 | 0 |

| 4 | 0 | 0.5 | 2.0 | 0.5 | 1.0 | 1 |
| 5 | 0 | 0.5 | 1.0 | 0 | 1.0 | 0 |

Rep 2 included the causal mask with its rationale and cross-section links; rep 3 added
worked numeric examples per component and twice flagged its own recalled citations as
unverified; rep 4 dropped the causal mask (its attention section is the only component
in 25 component-sections to clearly reach the ≥2 threshold); rep 5 included the mask,
the numerically stable softmax, and a debt-backward opening ("Sections 2 and 3 used
softmax without defining it"). Variance across reps: near zero (34,950–35,024 output
tokens; same structure).

**Protocol note:** reps 4–5 were run at the user's explicit request after the
arithmetic foreclosure at rep 3, completing the record to 5/5. Final count: 0 of 5
reps meet the failure criterion (≥2 components at miss ≥2); the criterion required 3
of 5. The verdict below therefore rests on a complete protocol, not an early stop.

<!-- decision: skill-not-deployed | status: adopted | supersedes: none -->
### Verdict — RED NOT CONFIRMED; Tasks 6–7 cancelled

After three breadth reps at {0–1, 0, 0} failing components, the criterion (≥3/5 reps
with ≥2 components at miss ≥2) is arithmetically unreachable; reps 4–5 cancelled on
that arithmetic. Both RED scenarios closed NOT CONFIRMED. Per the pre-registration and
the writing-skills Iron Law (no failing test → no skill), `explaining-technical-material`
is NOT deployed. It remains staged with this test record at
`scratchpad/skill-staging/explaining-technical-material/SKILL.md`; if the wrong-shape
failure ever reproduces in the wild, that instance is the RED evidence and deployment
follows this plan's Task 7 as written.

**Operative repairs, deployed and standing:** the Task-2 trigger broadening (the
control arm demonstrated it loading on every test prompt), the Task-1 payload
excisions, the Task-3 CLAUDE.md prose-verification bullet, the review-time component
contract (rubric class C, `docs/plans/2026-08-27-chapter-review-rubric.md`), and
project-memory rule 6. The recurrent thin fields observed in every control rep —
product-observable capability and deployment status — are rubric C-contract fields
4 and 5, enforced at review. Task 7's CLAUDE.md taxonomy line was applied in its
skill-independent form only (teaching material → `writing-clearly-and-concisely`),
since a mandate must not name an undeployed skill.

Rep-1 notes: attention's necessity argued by comparison to convolutions/RNNs the
audience has never been taught (inaccessible necessity, scored 0.5); the causal mask
omitted entirely — first genuine breadth-induced content omission; product-observable
capability and deployment status remain the recurrent thin fields across every rep of
both scenarios. Control contamination as before: the broadened Task-2 trigger fires
on this prompt too ("Write the … supplement sections"), so the baseline is the
current stack minus the new skill.

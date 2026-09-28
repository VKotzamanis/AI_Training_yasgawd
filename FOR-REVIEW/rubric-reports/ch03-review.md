# Review: slides/03-control.md — 2026-08-28 — reviewer: claude-opus-5[1m]

Rubric: `FOR-REVIEW/RUBRIC.md` v1.1. Slides counted from 1 at the title slide (`# Chapter 3 —
Control`, line 9); 18 slides total, matching the slide count in `curriculum/review-ch03.md`
line 24. Line numbers are `slides/03-control.md`.

**Scope note, recorded before the findings.** The file under review is the superseded Slidev
draft. A Beamer rebuild — `slides/beamer/03-control.tex`, 23 frames, dated 2026-08-22, with a
completed term audit at `curriculum/ch03-term-audit.md` — exists and was **not** reviewed. This
mirrors the ch02 entry in `TOPICS-LEDGER.md`. Two of the findings below are checked against the
rebuild in "Checks not run"; the rest are not.

**Chapter argument, stated so its author would accept it.** Prompting technique is taught after
Chapter 2 rather than before it because every lever in the chapter steers a behaviour the rating
layer produced; each technique is therefore given with the rated dimension it acts on, the
documented claims are separated from the widely repeated undocumented ones, three anti-patterns
are shown to be the same levers pulled backwards, and the two unestablished claims are handed to
Chapter 4 to test.

---

## Topic ledger

| topic | opens (slide) | closes (slide) | reopened at |
|---|---|---|---|
| Why Control follows Formation | 1 | 1 | **2** — [ch03-009] |
| The "what was rated, that this steers?" test | 2 | 18 | organising thread; discharged only at 4 and 7 — [ch03-001] |
| Prerequisites before tuning (criteria / empirical test / draft) | 3 | 3 | — (row at 17 is summary) |
| Specificity, output format, ordered steps | 4 | 4 | — |
| A constraint carrying its reason | 5 | 5 | — |
| Tagged / structured input | 6 | 6 | — |
| Prompt injection | 6 | 6 | — (handed to Ch6; never defined — [ch03-011]) |
| Examples: relevance, diversity, structure, 3–5 | 7 | 8 | — |
| Negative examples and their cost | 8 | 8 | — |
| Role / persona: tone-and-behaviour vs accuracy | 9 | 9 | rows at 17 (summary) |
| Chain-of-thought and the folk version | 10 | 10 | row at 17 (summary) |
| Auditability of "the working" | 10 (line 300) | 10 | **14** (lines 429, 441–443) — [ch03-010] |
| Adaptive thinking, effort, cost | 11 | 11 | — |
| Rating → preference data → trained behaviour → your prompt | 12 | 12 | — |
| Anti-patterns as reversed levers | 12 | 15 | — |
| Portability across providers and versions | 16 | 16 | — |
| Evidential standing of each technique | 9 | 17 | **18** (lines 556–558, 564) — [ch03-008] |

---

## Slide messages

1. This chapter's techniques steer behaviours that Chapter 2's rating produced, which is why it
   sits after Chapter 2.
2. Technique taught before mechanism becomes cargo-cult prompting, so every technique here must
   name the rated behaviour it steers or be flagged rather than taught.
3. The vendor's documentation assumes success criteria, a way to test empirically, and a draft
   prompt — and most prompting advice skips the middle one.
4. Write a prompt a minimally-briefed colleague could follow, because a vague prompt cannot be
   failed on instruction following.
5. A constraint with its reason attached generalises to cases you did not enumerate; a bare rule
   does not.
6. Tag the parts of a mixed prompt so instructions, context and data cannot be confused, which is
   also the first partial defence against prompt injection.
7. Three to five relevant, diverse, tagged examples steer format, tone and structure more
   reliably than instructions do.
8. A negative example works but puts the unwanted pattern into the window, so prefer stating the
   desired behaviour.
9. The documentation claims a role changes behaviour and tone, not accuracy; the accuracy claim
   is a separate, testable one that Chapter 4 settles.
10. Chain-of-thought has a published result behind supplied worked exemplars; typing "think step
    by step" at a model that already reasons is a different, untested proposition.
11. Current models decide their own thinking depth, biased by an effort setting, and more
    thinking costs tokens and latency.
12. You are now on the writing side of the rubric, and your prompt can invite back the behaviours
    you watched being rewarded.
13. A question with its preferred answer visible in it requests the agreement rating rewarded,
    and you will not notice because the answer agrees with you.
14. Asking for a verdict returns something confident and uncheckable; asking for the working
    returns something you can audit.
15. Conflicting constraints are silently dropped rather than flagged, so name which one wins.
16. Every technique here is calibrated to one provider's models and often to one version, so a
    moved prompt is an untested prompt.
17. Five of the chapter's claims are documented; two — role improving accuracy, and "think step
    by step" — are not established and go to Chapter 4.
18. (Message identical to 17 plus 2 and 12 — see [ch03-008].)

Every slide has a statable Message. No F finding arises from the Message test.

---

## Findings

### [ch03-001] C blocker — slides 2, 4, 5, 6, 7, 8, 9, 10, 11
Quote: "- So each technique here comes with the same question: **what was rated, that this
steers?**" (line 35) and "And the ones that have no answer to that question get flagged, not
taught." (line 41). The promise is discharged twice: "**Maps to:** instruction following — the
dimension your Chapter 2 rubric scored hardest." (line 111) and "**Maps to:** house style. In
Chapter 2 you were handed a rewrite checklist and told to" (line 220).
Why it fails: the chapter announces a rule every technique must satisfy, then teaches six of
eight techniques — say-why (5), tagged input (6), negative examples (8), role (9), requesting
reasoning (10), thinking and effort (11) — without naming the rated dimension and without
flagging them. This is the chapter's only stated justification for its position in the sequence
("That is why it is here and not before Chapter 2", lines 15–16); on six slides the justification
is not made, so those slides could equally sit before Chapter 2 and the opening claim is
falsified by the chapter's own body.
Fix direction: attach the rated dimension to every technique slide, or drop the rule at line 41.
`curriculum/review-ch03.md` lines 66–79 supplies the mapping (formatting → show the format;
tone → role and voice examples; verbosity → ask for the length, the effort setting; truthfulness
→ ask for the working; harmlessness → no lever, which is itself informative). **Distinct from the
prior finding:** RC3 lines 62–66 asserts "Every technique on these slides carries a **maps to**
line" and objects only that the device should be the chapter's structure rather than a footnote.
Against this file that assertion is wrong — the string `**Maps to:**` occurs twice. The gap is
not that the device is under-promoted; it is that it is absent from three quarters of the
techniques it was promised for.

### [ch03-002] T blocker — slide 12
Quote: "In Chapter 2 you rated. Under time pressure, you rewarded confidence, structure and
length. So did everyone before you, at scale, and that became preference data." (lines 355–356),
diagrammed as "raters reward confidence,<br/>structure, agreement" → "preference data" →
"trained behaviour" (lines 360–361) terminating in "verbosity" (line 365).
Why it fails: Chapter 2 teaches the opposite on this exact point. `slides/02-formation.md` line
361 grades the row "Long, structured, confident answers" as "**Not known** — see below | **The
folk answer is contradicted**", and lines 367–371 give the grounds: "The folk story says raters
liked long answers, so models got long. Two of the reviewed instruments say otherwise: one broke
ties deliberately toward **brevity**, the other **deleted length as a grading category** partway
through the project". Chapter 3's pivot slide — which the whole anti-pattern section rests on —
reinstates the folk story as an established causal chain, in a course whose spine is source
discipline and whose own house rule 6 is "Rank by evidence, not by force".
Fix direction: cut the length/verbosity arm of the chain, or restate it at the standing Chapter 2
assigned it — the confidence and agreement arms survive, the verbosity arm does not, and the
mechanism for verbosity is not known. Basis: `slides/02-formation.md` lines 361, 367–374, read
during this review. **CONFIRMED.**

### [ch03-003] T major — slide 12
Quote: "In Chapter 2 you rated. Under time pressure, you rewarded confidence, structure and
length." (lines 355–356)
Why it fails: this asserts the outcome of a live exercise that has not yet been run, as fact, to
the room that ran it. Chapter 2's own script forbids the assumption: "Put confidence beside
preference and ask whether the two track each other. **If they do, say so.** The interesting
version is not guaranteed to happen." (`slides/02-formation.md` line 756). If the tally comes out
otherwise, slide 12 contradicts what the room just watched, and the anti-pattern section loses
its premise mid-delivery.
Fix direction: condition the sentence on the tally actually collected — "whatever your tally
showed, at scale the rating layer is what produced these behaviours" — or move the claim to the
industry-scale statement alone. Basis: `slides/02-formation.md` line 756, read during this
review. **CONFIRMED.**

### [ch03-004] T major — slide 13
Quote: "- Agreement was rewarded during rating. Asking a question with a preferred answer visible
in it is asking for the trained behaviour." (line 409)
Why it fails: stated as settled fact. Chapter 2 grades the same claim "Agrees with you when you
push back | Preference data rewards agreement | Plausible, **not evidenced in the documents**"
(`slides/02-formation.md` line 360). The chapter's own thesis is that standing travels with a
claim (slide 17); here a plausible-but-unevidenced mechanism is promoted to a premise, and the
anti-pattern is built on it.
Fix direction: mark the standing on the slide — "agreement is the plausible mechanism, not an
evidenced one; the anti-pattern holds either way because a leading question narrows the answer
space". Basis: `slides/02-formation.md` line 360, read during this review. **CONFIRMED.**

### [ch03-005] T major — slide 10
Quote: "Chain-of-thought prompting — supplying worked examples of the reasoning, or asking for
the working — is a real technique with a published result behind it." (lines 293–294), cited
`<Cite k="wei2022" />` (line 312).
Why it fails: two defects in one sentence. (a) It folds "asking for the working" into the
technique that "has a published result behind it", then contradicts itself seven lines later —
"Typing *\"think step by step\"* at a model that already reasons before it answers is not the
thing that was tested." (line 301) — since asking for the working *is* the zero-shot form. The
project's own `references.md` line 161 records the prohibition explicitly: "the abstract
describes prompting with *a few chain-of-thought exemplars* — eight, on a 540B-parameter model
… It is not a result about typing 'think step by step' at a modern reasoning model. Do not let
the two be conflated on a slide." (b) Line 299 states the result — "improves performance on
arithmetic, commonsense and symbolic reasoning" — with the emergence condition dropped; the same
reference note records that the ability "emerges in sufficiently large models", and the scale is
part of the result, not context.
Fix direction: restrict the definition at lines 293–294 to supplied worked exemplars, cite the
zero-shot instruction separately or not at all, and carry the 540B / sufficiently-large-model
condition onto line 299. Basis: `references.md` line 161 (`wei2022`, tagged `[V]`, arXiv abstract
record fetched 2026-08-19), read during this review. **CONFIRMED.**

### [ch03-006] C major — slide 11
Quote: "- Current models use **adaptive thinking**: the model decides when and how much to think,
calibrated by an `effort` setting and by how hard your query is." (line 327) and "`budget_tokens`
is deprecated and returns an error on recent models — use `effort`, or `max_tokens` as a hard
ceiling." (lines 336–337)
Why it fails: slide 11 is `effort`'s definitional home in this chapter and supplies no location
field — the room is told to "use `effort`" without being told where the control lives. It is an
API request field (`output_config.effort`, five levels), and `curriculum/review-ch03.md` lines
196–199 records the check that settles this: "the vendor's own guidance is written for API
callers, and it does not put the effort dial in the chat app for the current models, so the slide
cannot tell this room to set it." The slide issues exactly the instruction that note says cannot
be issued. Two further contract fields are absent: the failure on removal, and the observable
capability in the deployed product.
Fix direction: state where `effort` is settable (API request body; the coding tool) and what the
chat-app user does instead — per-turn wording — so the slide stops instructing an audience that
cannot act on it. The rebuild's term audit already carries this fix: "`effort` | 13 | a five-level
setting biasing how readily the model thinks, **documented for the API and the coding tool**"
(`curriculum/ch03-term-audit.md` line 19).

### [ch03-007] C major — slide 9
Quote: "Setting a role in the system prompt is the most repeated advice in circulation." (line
262)
Why it fails: the system prompt is the location the technique depends on, and no ledger entry
delivers a definition of it. `ch01-approved` names it only as one of the twenty-two boxes on deck
slide 12 and places it in the Supp §S16 weights-vs-harness ledger — a location, not a
one-sentence definition — and the ch02 "Topics exported" list contains no system-prompt entry. A
trainee who cannot identify the system prompt cannot execute the chapter's single most-repeated
technique. Already flagged at the premise level: PR19 lines 282 and 310 record "system prompt"
undefined through Chapters 2 and 3 (`PRIOR-REVIEW-SCOPE.md` line 49) — cited, not re-derived; the
addition here is that the ledger confirms no delivered chapter closes it.
Fix direction: one line on slide 9 defining the system prompt by contrast with the user turn, and
naming where a role instruction is typed in the product this room uses. Note the rebuild's term
audit (`curriculum/ch03-term-audit.md` line 38) lists "system prompt" as inherited "From Chapter
2", which the ledger does not support.

### [ch03-008] R major — slide 18
Quote: "- Technique, with a mechanism attached to each piece of it." / "- Three anti-patterns that
are not style errors — they are requests for trained behaviour you already watched being
trained." / "- Two widely repeated claims, deliberately left open." (lines 556–558), closing "You
now have claims. **Chapter 4 is how you test one.**" (line 564)
Why it fails: every element has an antecedent within two slides. Bullet 2 restates line 370–371
verbatim in substance ("The next three slides are not style advice. They are ways of accidentally
asking for the behaviour you were warned about."); bullet 3 and the closing line restate slide
17's own close, "The bottom two rows are the reason the next chapter exists. Everything above them
you can act on tomorrow; those two you should test before you believe." (lines 538–539); bullet 1
restates slide 2's rule, and is additionally false against [ch03-001]. Two consecutive
consolidation slides carry one payload.
Fix direction: fold the Chapter 4 handoff into slide 17 and delete slide 18, or make 18 carry
what 17 cannot — the file/image lever and the model-choice question that RC3 lines 118–125 names
as the chapter's largest gaps.

### [ch03-009] R minor — slides 1 and 2
Quote: "Every technique in this chapter steers something that was rated. That is why it is / here
and not before Chapter 2." (lines 15–16), restated as the slide 2 headline "## Why this chapter
comes second" (line 29) and its third bullet (line 35).
Why it fails: the placement argument is delivered whole on the title slide and then delivered
again as a full slide. Ledger-mechanical: one topic, two open intervals.
Fix direction: keep one. RC3 lines 54–56 independently recommends moving the sequencing argument
to the speaker notes and opening on Chapter 2's closing question instead — that resolves the
duplication and the audience-fit objection together.

### [ch03-010] R minor — slides 10 and 14
Quote: "- Asking for the working also leaves you something you can audit, which on your own tasks
may matter more than the accuracy question does." (line 300), reopened at "- The second is longer,
slower, and the only one of the two you can audit." (line 429) and again at "Asking for the
working helps you catch errors; it does not prove the working caused the answer." (lines 442–443).
Why it fails: the auditability justification for asking for the working is made three times across
two slides, with no new information on the second and third passes. Slide 14's distinct content —
that a verdict is uncheckable — is carried by line 427, not by line 429.
Fix direction: state auditability once. Slide 10 is the technique's home; slide 14 needs only the
verdict half.

### [ch03-011] C minor — slide 6
Quote: "- **This is also your first defence against prompt injection.** If instructions and data
are visibly separated, text arriving inside `<input>` is easier to treat as data. Chapter 6 shows
how far that gets you, which is not as far as you would like." (line 190)
Why it fails: prompt injection appears in no ledger entry for `ch01-approved` or `ch02`, and this
chapter does not define it. The bolded claim is a security claim the room has no basis to
evaluate: without knowing what injection is, "first defence" carries no information, though the
underlying instruction (separate instructions from data) does.
Fix direction: a half-sentence gloss in place — text arriving in your data that is written to be
read as an instruction — before the Chapter 6 pointer.

### [ch03-012] S3 minor — slide 14
Quote: "A verdict is cheap to produce and expensive to verify. An analysis is the other way
round." (line 435)
Why it fails: the chiasmus restates line 429 and occupies the highlighted payoff slot that on
slides 4 and 7 carries the "Maps to:" line. On this slide that slot should carry the truthfulness
mapping — RC3 line 75 gives it as "Truthfulness | ask for the working rather than a verdict" —
so an aphorism stands where the chapter's own promised information belongs. This is the S3
pattern, not decoration on top of content.
Fix direction: replace with the rated-dimension mapping; the point at line 429 already lands.

**Prior-review S3 instance, cited not re-derived:** "You are on the other side of the rubric now"
(line 353) is second-person dramatic address, banned by house style §5.1 — `curriculum/review-ch03.md`
lines 147–148.

**No F-class findings.** Every slide has a statable Message, every section boundary is locatable,
and the two questions held open (role/accuracy, "think step by step") are signposted at their
opening and closed at slide 17.

---

## Coverage checklist

| Promise | Status |
|---|---|
| Title subtitle "Acting on what Formation described" (line 11) | Paid at 4, 7, 12, 13, 15 |
| "Every technique … steers something that was rated" (lines 15–16) | **Partly unpaid** — 2 of 8 technique slides — [ch03-001] |
| "the ones that have no answer to that question get flagged, not taught" (line 41) | **Unpaid** — six taught, none flagged — [ch03-001] |
| Prerequisite testing method (line 75, "Forward reference — Chapter 4") | Paid outside the chapter, correctly signposted |
| "The next three slides are not style advice" (lines 370–371) | Paid at 13, 14, 15 |
| Frontmatter: "Sets up the claims Chapter 4 puts on trial" (line 4) | Paid at 9, 10, 17 |
| Frontmatter: "the portability problem Chapter 12 inherits" (line 4) | Paid at 16 |
| Standing table separating documented from untested (slide 17) | Paid, with the residue RC3 lines 93–94 names: "Several others are equally testable and are presented as settled" — [ch03-004] and the slide-8 negative-example mechanism are two such |
| Single-vendor sourcing declared on a frame | Not a rubric class; already flagged at PR19 lines 312–315 and RC3 lines 85–91 (nine of ten citations are one vendor page; CLAUDE.md rule 4 requires a COI note). Slide 16 gives a portability caveat, not a COI declaration |

---

## Topics exported

- **Prompting technique is taught as steering, not as tricks** — each lever is justified by the
  rated dimension it acts on, and a technique with no rated dimension behind it is meant to be
  flagged rather than taught. Slides 1–2, lines 15–16 and 35–41. The chapter states the rule; see
  [ch03-001] for how far it applies it.
- **The three prerequisites before tuning a prompt** — success criteria, a way to test
  empirically against them, and a draft to improve; the middle one is what most prompting advice
  omits. Slide 3, lines 60–69. Vendor documentation, `anthropic-prompting`.
- **The colleague test for specificity** — show the prompt to someone with minimal context and
  ask them to follow it. Slide 4, lines 96–98. Maps to instruction following: "A vague prompt
  cannot be failed on instruction following, because there was no instruction to follow."
- **A constraint carrying its reason generalises; a bare rule does not** — the units example, with
  the claim that the model generalises from the explanation. Slide 5, lines 130–154.
- **Tagged input separates instruction from data** — XML-style `<instructions>` / `<context>` /
  `<input>`, consistent descriptive names, nested where the hierarchy is real. Slide 6, lines
  168–189. Named as the first partial defence against prompt injection, with the term itself
  undefined ([ch03-011]) and the payoff handed to Chapter 6.
- **Example criteria: relevant, diverse, structured, three to five** — examples steer format,
  tone and structure more reliably than instructions. Slide 7, lines 207–214. The 3–5 bound is
  vendor-documented and was not re-verified here.
- **A negative example still enters the window as an instance of the unwanted pattern** — hence
  the documented rule, tell it what to do instead of what not to do; and if a negative example is
  used, label it and pair it with the correction. Slide 8, lines 239–245.
- **The role claim, split in two** — the documentation claims a role focuses *behaviour and tone*;
  it does not claim a persona improves *accuracy*. The accuracy claim is separate, testable, and
  deliberately left open for Chapter 4. Slide 9, lines 266–277. This split is the chapter's
  cleanest object and later chapters should reuse the form.
- **Chain-of-thought's published scope versus the folk version** — the result rests on supplied
  worked exemplars; "think step by step" at a model that already reasons is a different
  proposition and is not what was tested. Slide 10, lines 293–301. Carry the correction in
  [ch03-005] with it: the zero-shot form must not be described as having the published result
  behind it, and the sufficiently-large-model condition belongs on the claim.
- **Asking for the working leaves an auditable artefact** — which on this room's own tasks may
  matter more than the accuracy question. Slide 10, line 300; restated at slide 14. Chapter 5
  owns the limit: stated reasoning is not proof that the reasoning caused the answer (lines
  441–443).
- **Adaptive thinking and the effort setting** — the model decides when and how much to think,
  biased by an effort setting and by query difficulty; more thinking costs tokens and latency
  (Chapter 7's material, Chapter 13's bill). Slide 11, lines 327–329. Version-fragile:
  `budget_tokens` is deprecated and errors on recent models. **Where `effort` is settable is not
  stated — see [ch03-006]; do not let a later chapter assume this room can reach the dial.**
- **The rating loop closes on the prompt writer** — rewarded behaviour becomes preference data,
  becomes trained behaviour, and a prompt can invite it back. Slide 12, lines 355–365. **Export
  the structure, not the instances:** the confidence and agreement arms carry Chapter 2's
  standing marks, and the length/verbosity arm is contradicted by Chapter 2 — [ch03-002].
- **Three anti-patterns as levers pulled backwards** — the leading question (a preferred answer
  visible in the wording invites the rewarded agreement, and you will not notice because the
  answer agrees with you); asking for a verdict (a judgement can be delivered confidently on no
  evidence, an analysis can be checked); constraint stacking (conflicting requirements are
  satisfied selectively and the rest dropped without report, so name which constraint wins).
  Slides 13–15. The constraint-stacking slide also exports the mirror of Chapter 2's
  over-specified rubric, seen from the author's side.
- **Prompts do not port** — tag conventions, role handling, thinking and effort controls and
  default verbosity are provider-specific and several are version-specific; a prompt moved to
  another model is an untested prompt, not a working one. Slide 16, lines 492–498. This is what
  Chapter 12 inherits.
- **Standing printed per technique** — five techniques documented, two claims (role improves
  accuracy; "think step by step" helps a modern reasoning model) marked not established and
  handed to Chapter 4. Slide 17, lines 524–539. The table form — claim against standing — is
  reusable and is the chapter's contract with Chapter 4.

---

## Checks not run

- **The Beamer rebuild was not reviewed.** `slides/beamer/03-control.tex` (23 frames, 2026-08-22)
  supersedes the file under review and is where the delivered chapter lives. Two spot checks only,
  both by grep, neither a review: the folk-story sentence behind [ch03-002] does not appear in the
  rebuild, and frame 12 reframes the length question as a lever ("Asking for a length is more
  reliable than asking for brevity", line 322); but [ch03-004] survives verbatim in substance —
  "Agreement with the person asking was rewarded during rating" (`03-control.tex` line 463). The
  other ten findings were not checked against the rebuild at all.
- **The vendor documentation was not re-fetched.** `references.md` line 163 tags
  `anthropic-prompting` `[V]` as of 2026-08-19 and marks it "Version-fragile — re-fetch in the
  week before delivery." I did not verify against primary text: the three prerequisites (lines
  60–62), the colleague-test wording (lines 96–98), "the model generalises from the explanation"
  (line 154), the three-to-five bound (line 214), the tell-it-what-to-do rule (line 244), or the
  "focuses behaviour and tone" wording (line 266). None is recorded as a finding, and none is
  cleared either.
- **The Opus 5 effort-versus-length claim (lines 337–338) was not adjudicated.** The bundled
  `claude-api` skill records that lower effort produces "less preamble, and terser confirmations"
  on the Opus family, which points the other way, but that describes agentic tool-calling
  behaviour rather than general response length, and I did not open the vendor page the slide's
  claim rests on. Left unresolved, as RC3 lines 149–150 also left it.
- **`budget_tokens` was checked and holds.** Against the bundled `claude-api` skill: removed and
  rejected with a 400 on Opus 5, Opus 4.8, Opus 4.7, Sonnet 5 and Fable 5; deprecated but still
  functional on Opus 4.6 and Sonnet 4.6. The slide's compressed "deprecated and returns an error
  on recent models" is correct for the models this room meets. `effort` is `output_config.effort`
  with five levels — the bare `effort` on the slide is acceptable shorthand; the defect is
  location, not name ([ch03-006]).
- **Chapter 2 was checked against the Slidev draft, not the rebuild.** [ch03-002], [ch03-003] and
  [ch03-004] rest on `slides/02-formation.md`, which the ledger records as itself superseded by a
  33-frame Beamer rebuild. If the rebuild changed the standing marks on those three rows, the
  three findings need re-checking; I did not open `slides/beamer/02-formation.tex`.
- **The Chapter 17 overlap was not checked.** RC3 lines 202–204 leaves open whether the three
  anti-patterns duplicate Chapter 17's analysis-not-verdict technique; deciding needs both read
  together and Chapter 17 was outside this review.
- **`assets/eval-worksheet/README.md` was not read**, so I did not verify that Chapter 4 actually
  settles the two claims slides 9, 10 and 17 hand it.
- **Slide-count convention.** I counted the title slide as slide 1, giving 18, matching RC3 line
  24. RC3's headline audit counts 17 (title excluded); a reader mapping findings between the two
  documents should offset by one on headline counts only.

---

## Verdict

**salvage-with-edits.** The chapter's spine is sound and two of its objects — the role claim split
into documented tone and untested accuracy, and the standing table that prints what can be acted
on against what must be tested — are the strongest things in it and should survive any rebuild
unchanged. What blocks it is that the chapter does not do the thing it says it does. It announces
that every technique will be justified by the rated dimension it steers and that unjustified
techniques get flagged rather than taught ([ch03-001]), then teaches six of eight without either;
and its pivot slide reinstates as an established causal chain the folk explanation of verbosity
that Chapter 2 spends a highlighted panel showing to be contradicted by two of the reviewed
instruments ([ch03-002]). The second is the more serious defect, because a course whose subject is
source discipline cannot teach in Chapter 3 the claim it disproved in Chapter 2, and the room that
sat through both will notice. Three further claims are presented at a standing they were not given
([ch03-003], [ch03-004], [ch03-005]), two components the chapter's techniques depend on are used
without a location ([ch03-006], [ch03-007]), and the close is delivered twice ([ch03-008]). None of
this is a rebuild: the mapping table already exists in RC3, Chapter 2 already supplies the standing
marks, and the closing slide can be folded. It is an editing pass with two blockers in it — which
is what salvage-with-edits means. Note that a 23-frame Beamer rebuild of this chapter already
exists and was outside scope; a spot check suggests it clears [ch03-002] and [ch03-006] and still
carries [ch03-004].

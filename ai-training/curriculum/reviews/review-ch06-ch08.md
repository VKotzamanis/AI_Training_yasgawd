# Review — Chapter 6 (Extrinsic failure) and Chapter 8 (Brain and model)

Reviewed 2026-08-20 against `CLAUDE.md`, `chapter-briefs.md`, `references.md` (Ch 6 and Ch 8
sections, both rewritten from verification work), `architecture.md` and `slides/10-memory.md`.

## Summary

Both decks clear the traps `references.md` was rewritten to set, deliberately rather than by
luck. Chapter 8 states the encoding-model method correctly and names the wrong version in
order to refuse it; the three noise ceilings and the primate-IT figure match exactly; the
closing line is identical to the line `slides/10-memory.md` opens on. Chapter 6 has the
corrected sockpuppet ordering, states no duration for the second incident, and names the
sourcing gap on the slide rather than in the notes.

The defects sit in the reasoning the decks added around those warnings, and in attribution.
Chapter 8's four-items slide withdraws its own numbers and then declares the argument
survives structurally; it does not. Its noise-ceiling slide draws an inference a reliability
statistic cannot support. Chapter 6 leaves its two most sourcing-sensitive slides without any
citation footer, and its summary slide restates the error the chapter was rewritten to remove.

## Key Issues

### 1. The four-items "structural argument" does no work — CONFIRMED
`slides/08-brain-and-model.md`, lines 176–193.

> **The argument survives; the arithmetic does not.** Make it structurally — one system
> consolidates and the other does not — and drop the numbers.

The offered structural argument is not this slide's argument. "One system consolidates and
the other does not" is the *preceding* slide (lines 166–168: "**The hippocampus consolidates
episodic experience into durable memory**… **A model at inference does none of this.**").
Consolidation and working-memory capacity are different claims about different systems. Once
the numbers go, the capacity slide has nothing of its own left; it borrows the conclusion of a
slide that was already complete without it. The brief lists the two as separate break-points,
so the deck is down to three presented as four.

The retraction is also incomplete. The always-visible lede still asserts:

> human working memory holds about four items, against a context window of hundreds of
> thousands of tokens. **The numbers run opposite to the analogy.**

Only "four" is withdrawn. But if a chunk and a token are not commensurable, no ordering
between them is defined — so "run opposite" is not merely unsupported, it is not well-formed.
A participant who reads the bold and skips the clicks leaves with the claim `references.md`
forbids. "Putting 4 beside 200,000" also introduces an unsourced context-window figure.

**Fix.** Either cut the slide — the consolidation slide already carries the conclusion — or
rebuild it on an asymmetry that is genuinely about capacity: a context window is uniformly
addressable, lossless within its bound and supplied from outside, while working memory is
actively maintained, interference-prone and rate-limited. That argument survives the
withdrawal of the numbers because it never used them. Retract "run opposite" either way.

### 2. The noise-ceiling slide overstates what a low ceiling implies — CONFIRMED, with a SUSPECTED unit error
`slides/08-brain-and-model.md`, lines 78–80.

> **Nearly all of a small number is still a small number.** Quote the percentage without the
> ceiling and you have moved a factor of five without saying so

**(a) CONFIRMED.** The ceilings (0.32, 0.17, 0.20) and the primate-IT comparison (0.82) match
`references.md` exactly, and stating them is right. The gloss is not. A noise ceiling
estimates the *reliability of the recordings* — how much signal is predictable in principle
given repeat-to-repeat noise. A low ceiling is a fact about the dataset, not about the size
of the brain–model correspondence. It licenses: raw predictivity is low in absolute terms, so the
normalised headline is carrying weight; the denominator is small and itself estimated with
error, so the score is fragile; and these datasets discriminate between models far less
sharply than primate IT data, which is the authors' actual point. It does not license "the
number is small", a claim about the phenomenon that a ceiling cannot settle.

**(b) SUSPECTED.** The three ceilings imply ratios of 3.1, 5.9 and 5.0 — the slide lists all
three, then gives one figure that is wrong by nearly half for the first. Separately it says
**variance** but computes on the correlation scale; if the ceilings are correlations, as the
0.82 IT comparison suggests, variance-scale ratios are roughly 10, 35 and 25. `references.md`
does not record the unit, so I cannot resolve this from the file. This is the MACs-vs-FLOPs
erratum the slide invokes one line later.

**Fix.** State what the ceiling supports; state the unit, per the house convention on
non-obvious denominators; give the range, not a single factor.

### 3. Chapter 6's recap reinstates the claim the chapter just refuted — CONFIRMED
`slides/06-extrinsic-failure.md`, line 249:

> Two documented incidents — one with a primary report, one without, and you now know which
> is which.

The qualifier does not repair the noun. `references.md` is explicit that no primary incident
report exists for the second, and records this as a finding *about the brief*. Line 249 is
the brief's wrong sentence surviving into the summary slide — the one participants photograph.
**Fix:** "One documented incident, and one that is only testimony."

### 4. An uncited quotation under another paper's footer — CONFIRMED
`slides/08-brain-and-model.md`, lines 143–156. Two findings, one footer,
`<Cite k="hadidi2026" />`. The first bullet — "the representations best at prediction are
*'strictly worse brain models'* than others" — is Antonello & Huth 2024. The key
`antonello2024` exists in `sources.json` and resolves. A direct quotation is attributed to
the wrong paper, on the slide about citation discipline.

Same slide: `references.md` instructs "**Idan A. Blank is a co-author of both Schrimpf 2021
and this critique.** Say so on the slide." The deck says only "One author appears on
**both**". Naming him costs four words and makes the claim checkable.

### 5. Chapter 6's two most sourcing-sensitive slides carry no citation footer — CONFIRMED
The "Incident two" slide (lines 148–168) and "What you can actually do" (lines 208–217) have
no `<Cite>` at all, against the house rule that every slide carries one. For incident two
this is self-defeating: the slide's lesson is *name your sources and their standing*, and it
names neither — "a **conference talk**, relayed by a magazine", "The vendor's own
disclosure". The vendor, publication, reporter, date and session number are all in
`references.md`. `Cite.vue` already renders `kind: "testimony"` as "Expert testimony, not a
primary source." — the exact label house style demands, unused on the one slide that needs it.

### 6. Rule 1 and `references.md` conflict, and issue 5 cannot be fixed until it is settled — CONFIRMED
Hard rule 1: only `[V]` may appear in slide content. The incident-two material is tagged
"**[X]** as a citable incident report; **[P]** as reporting", yet holds a full slide.
`references.md` says "Teach it as testimony or drop it", which the deck does, honestly — but
that is an undocumented exception to rule 1, and the footer issue 5 requires would put a
non-`[V]` key on a slide, printing a red `[P]` tag under current `Cite.vue` styling. Intended
behaviour, or a `check:cites` failure?

### 7. An uncited claim about a protocol specification — CONFIRMED
`slides/06-extrinsic-failure.md`, line 214: "The protocol specification says the same of tool
descriptions." This asserts the content of a named external document. `references.md` lists
`MCP server security threat model` only as a *search term* under Ch 6 — no source exists,
verified or otherwise. Hard rules 1 and 2 require a citation or a `TODO(cite)`.

### 8. Schrimpf's scope is omitted, though Goldstein's is given — CONFIRMED
The deck states Goldstein's scope in full ("**nine participants, all epilepsy patients**… one
thirty-minute podcast", line 118) but never gives Schrimpf's: 43 models, datasets of n=10,
n=5, n=5. It also omits that the predictive-processing conclusion rests on a **between-model
correlation** — a model's next-word-prediction performance correlating with its brain score.
That is half of the method the chapter set out to state correctly, and it is exactly what
Antonello attacks two slides later — which now reads as a free-standing objection rather than
an attack on the stated inference.

### 9. The untrained-model result is presented, then silently explained away — CONFIRMED
Lines 92–94 build a slide on untrained models performing "well above chance", concluding
"what is being measured is not straightforwardly 'what training taught it'". Line 144 then
reports that positional signals and word rate "**fully account for the neural predictivity of
untrained models**". That does not complicate the first finding, it dissolves it — the
untrained-model performance is a confound, not a result. Say so, or the earlier slide stands.

### 10. Content claims exceeding what the reference entries record as read — SUSPECTED
`references.md` distinguishes entries whose content was read (OWASP "read in full", AISI
"blog page read", Goldstein and Antonello with quoted text) from those where only identifiers
were confirmed. `greshake2023` and `cohen2025` are in the second group. Two slides make
specific content claims on them: line 115, "demonstrated compromise of **real, deployed**
applications, not a laboratory toy" — supported by the title alone; and line 179, "mail
assistants, retrieval pipelines, agent chains". Both plausible; neither recorded as verified,
and this course's standard is that plausible is not the test.

### 11. Smaller items — CONFIRMED
- **Brief deliverable absent.** The brief requires a live injection demo; line 225 carries
  `**TODO(produce)**` and `assets/injection-demo/` holds only a README.
- **Line 72, "SQL injection was *solved*".** The deck's claim, not OWASP's, under
  `<Cite k="owasp2026" />`. SQLi remains live where parameterisation is not used; "solved
  architecturally" is exact.
- **Edition year.** Lines 61 and 84 say "the **current** OWASP entry" and "the current
  list"; 2026 reaches the room only via the footer, and `references.md` flags the 2025/2026
  confusion specifically. Put the edition in the body.
- **Sequencing.** Chapter 6 gates Part III and Chapter 8 closes Session 1 correctly, and the
  Ch 8 → Ch 10 seam holds verbatim. But "What you can actually do" — the one slide the room
  should act on immediately — leans on "the diff review from **Chapter 9**" and a protocol
  not introduced until Chapter 12.

## Questions to Probe

1. Is the noise ceiling a correlation or a proportion of variance? "Factor of five" and the
   word "variance" cannot both be right, and `references.md` does not say.
2. Does the four-items slide survive at all once the numbers go? If the structural version is
   the consolidation argument, cut the slide rather than reword it.
3. Does "teach it as testimony" override hard rule 1, and what should `check:cites` do with a
   `[P]` key on a slide? Issue 5 is blocked on this.
4. `chapter-briefs.md` is now wrong in two places the verification work corrected — "Two
   documented incidents, both with primary sources" and "surprisal predicting… neural
   responses". Should the brief be corrected so the next reader does not reintroduce both?
5. `references.md`'s Ch 8 "### Citations" block still carries the superseded `[U]` entries and
   the wrong method description below the corrected block. Intentional history, or a trap?

## Bottom Line

Chapter 6 is close. Its reasoning is sound, the incident-two slide is the best
evidence-discipline teaching in either deck, and its defects are additive: two missing
footers, one uncited protocol claim, one absent demo. Fix line 249 first — it is the summary
slide and it restates the exact error the chapter was rewritten to remove.

Chapter 8 needs two slides rewritten. The noise-ceiling gloss draws the wrong inference from
a reliability statistic, and the four-items slide performs a retraction it does not carry
out, leaving an unwithdrawn claim in bold and substituting a neighbour's argument for its own.

## What this review did not do

Did not read Schrimpf 2021, Goldstein 2022, Greshake 2023 or Cohen 2025 — every claim about
what those papers support comes from `references.md`, which is why issues 2(b) and 10 are
SUSPECTED. Did not build the decks, run `check:cites`, or check the PDF exports. Did not
assess budget or timing. Did not read Chapters 5, 7, 9 or 12 beyond the one line of
`slides/10-memory.md` needed to check the seam, so duplication with Chapters 5 and 7 is
unassessed. Did not edit any file other than this one.

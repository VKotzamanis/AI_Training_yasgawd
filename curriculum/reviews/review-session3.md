# Peer review — Session 3 decks (Chapters 14–19)

Reviewed `slides/14-literature.md`, `15-production.md`, `16-code-and-numerics.md`, `17-critique.md`, `18-governance.md`, `19-judgement.md` against `CLAUDE.md`, `chapter-briefs.md` (Ch 14–19), `architecture.md`, `references.md`.

## Summary

Reasoning is strong and cross-referencing disciplined — every backward reference spot-checked resolves (`14:31`→`05:47`; `16:105`→`07:16`; `18:112`→`01:291` and `04:147–148`; `15:124`/`16:36`→`10:35`). All three thread closures exist and name their origin and development points.

Defects cluster in one place: **claims about the world carried with no citation**. All six decks contain zero `<Cite>` components; Chapters 5 and 7 carry ten and fourteen. Much is craft advice needing no source, but three load-bearing claims are not, one is `[P]`-tagged, and one has an unused `[V]` source. `scripts/check-cites.mjs:14,19` catches none of it — the regex matches only `<Cite k="…">`, so a deck with no citations passes trivially and prose is never inspected.

## Key Issues

### 1. A `[P]` claim on a slide, with an NDA decision resting on it — CONFIRMED

`18:89` — "on a document graph, the code pass is local while the **semantic pass over documents leaves the machine.**" (also `12:87–88`).

`references.md:339` carries exactly this, tagged **[P]**: "semantic pass over documents uses an API — **[P]** confirm against the current repository and pin a version." Hard rule 1 admits only `[V]`.

Not an aside: the next slide tells attendees to write the rule governing sponsor NDAs and confidential geometry, and this sentence is the factual basis for what they run locally. If the behaviour is version- or configuration-dependent, the deck has authorised a breach — the only irreversible failure mode in the six decks.

Fix: verify against the installed version, pin it, promote to `[V]`, add the footer; until then mark `TODO(verify)`.

### 2. The blocked section still asserts policy content — CONFIRMED

`18:25` marks the section "**BLOCKED — needs the list of journals this group actually publishes in**", which is plainly done. The next slide asserts the substance anyway:

- `18:49` "Almost always yes for substantive use, and the threshold differs by publisher."
- `18:51` "Authorship is the usual one — and it is prohibited everywhere"
- `18:50` "Getting this wrong is a desk rejection over formatting."

Empirical claims about policies the deck has just said it lacks; `references.md:352–356` tags every relevant source `[U]`. "Prohibited everywhere" is a universal claim over an unenumerated population. Also `18:31`, "the one most often missing from general guides". The block marker exists to stop the room leaving with instructor-memory policy beliefs; asserting the answers above it defeats it.

Fix: recast as the questions to ask of each policy, not the answers. Keep `18:63`'s argument from the meaning of authorship — definitional, not a policy claim.

### 3. Trust boundary closes on egress only, and claims completeness — CONFIRMED

`18:166` — "**Trust boundary** — trained harmlessness in Chapter 2, hostile input in Chapter 6, channels opened deliberately in Chapter 12, and governed here as a written data rule." `18:15` — "Everything Part II identified as a risk appears here as documented practice."

The closure names its origins but resolves one direction only. A data rule governs what *leaves*. Chapter 6 and `assets/injection-demo/` concern what *comes in*, and deck 18 mentions no injection, untrusted document, or tool-output trust; nothing from Chapters 5 or 7 appears either. So `18:166` names Chapter 6 while resolving nothing from it, and `18:15` asserts completeness the deck lacks.

Fix: one lab-standard bullet on inbound trust — which sources may be read into a session with file access, who approves exceptions — and soften `18:15`.

### 4. Chapter 16's separation holds; the demonstration cannot support the claim — CONFIRMED

Credit first: `16:67–70` is the best-handled claim in the session — "That the gap exists is demonstrable in the room. That it is caused by how much MATLAB appears in training corpora is a **hypothesis** — plausible, widely repeated, and not established on this slide." That is more careful than `chapter-briefs.md:281`, which states the cause as fact ("because of corpus composition"). **The deck is right; correct the brief to match.** The separation never collapses: `16:15–16`, `:47`, `:53`, `:81` assert the gap, never the cause. `:81`'s "prototype in whichever language the tool is strong in" presupposes only the demonstrated half.

The defect is the evidence design. `16:47` states "materially worse"; `16:54` establishes it by "Same task, both languages, side by side, on the day" — one task, one run per condition. `04:147–148` tells this same room: "One run per condition confounds the prompt effect with run-to-run spread." The chapter proposes the design its own course declared invalid, for an unquantified word.

Fix: `16:60`'s `TODO(capture)` should specify several tasks and repeated runs with model ID and date; report what was measured rather than pre-asserting.

### 5. Chapter 19's first test does not follow from Chapter 1 — CONFIRMED

`19:26` — "If the step has never been written down, there is nothing to predict from. You are asking a next-token predictor to be first." `19:46` — "**Novel derivation** follows from Chapter 1. The objective is next-token prediction over what has been written."

The inference proves too much: if next-token prediction could only reproduce steps present in the corpus, the model could emit no sentence not in the corpus — which the course spends eighteen chapters contradicting. The objective does not entail the conclusion. The correct grounding is already in the course and unused: `05:27` — "Where the training data was dense, plausible and true coincide. Where it was thin, they come apart — and nothing in the system detects which regime it is in."

Second slippage: the test is stated as "cannot verify" (`19:27`) but justified as "checking the answer is harder than producing it" — expensive, not impossible. `19:35–36` then applies an absolute ("not a risky instrument, the wrong one") to a cost trade-off.

### 6. The four tests are not exhaustive — CONFIRMED

Missing: **do not use it where the input is untrusted and the output is acted on.** Chapter 6 plus Chapter 12, with a dedicated asset, covered by none of the four. Test 4 governs *egress* — confidentiality. Injection is an *integrity* failure inbound. A task can pass all four and still be the wrong place to point an agent with file access. `architecture.md:76` makes Chapter 6 the gate for all of Part III, so a prohibition list omitting it is a real gap.

Weaker sixth candidate: reproducibility. `18:106` establishes that stochastic output cannot be reproduced by re-running the prompt — distinct from verifiability, since a one-off answer can be verified yet remain unreproducible for a methods section.

### 7. Claims about material that does not exist yet — CONFIRMED

- `19:48` — "**Silent failure** follows from the failure gallery. Every item in it was caught by something." `05:73` shows the gallery is `TODO(produce)`. The survivorship-bias argument is good but cannot be asserted about an unbuilt artefact.
- `14:24` — "You have already seen a fabricated citation from your own field." Same gallery, same TODO.
- `14:113–116` — "You have seen this failure twice in this course already — a prompting result that held on one model family being quoted as general, and a hardware result true on a benchmark being quoted as deployed." The hardware instance is real (`07:551–558`). The prompting instance is in no written deck; `03-control.md` has no such example, and the nearest thing, `05:159`, is a long-context result. Decks 02/06/08 are unwritten, but Chapter 3 is the prompting chapter and it is written.

### 8. Chapter 17 restates a `[V]` finding uncited and drops its scope — CONFIRMED

`17:107–108` — "Chapter 5 said AI-text detectors are unreliable in both directions, and that their false positives fall disproportionately on non-native English writers."

`references.md:161` holds Liang et al. 2023, *Patterns* 4(7):100779, DOI 10.1016/j.patter.2023.100779, **[V]**, key `{#liang2023}`. The deck cites nothing and drops the scope the entry insists on: "detectors as of March 2023 … **the specific percentages are dated.**" Chapter 17 renders it flat present tense about detectors in general — the failure Chapter 14 teaches three slides earlier (`14:105`), on the session's highest-stakes claim for an international group. Fix: `<Cite k="liang2023" />` plus "seven detectors as tested in March 2023".

Minor: `17:112` "unfalsifiable by design — you cannot prove you wrote something" contradicts `17:120` "What protects you is process, not proof: version history, drafts, notes". The second is right.

### 9. Chapter 15's absence claims — SUSPECTED

`15:93–94` — "generated imagery has no provenance and cannot be regenerated deterministically." Both halves are absolutes and I believe both are too strong: content provenance standards for generated images exist, and seeded generation with a pinned model and sampler is reproducible in many implementations. I did not verify either, so this is flagged rather than asserted — but an absence claim needs checking before it ships. Fix: scope to "no provenance you control".

Also `15:74–76` — "This deck follows the same rule. Its computed figures come from a script in the repository." Deck 15 has no figures, only a mermaid diagram. True of the slide set (`assets/figures/gen-figures.py:63,132` labels illustrative inputs), false of "this deck".

### 10. Duplication, Chapters 15 and 16 — CONFIRMED

`15:117` "Ask for the explanation, then **check it against what the code does**, not against what you meant it to do" versus `16:29` "Check the explanation against the code's behaviour, not against its variable names". Both land on the same artefact (`15:124`, `16:36`). Fix: 15 keeps the audience-facing case, 16 the comprehension case, and one references the other. Separately, `18:69–70`'s three non-delegables reappear at `19:66` with nothing added — arguably deliberate in a capstone, flagged so it is a choice.

### 11. Two closures narrower than the threads they close — SUSPECTED

**Truthfulness (Ch 14).** `14:139–141` names Chapters 2 and 5 explicitly and delivers a real procedure (`14:131`) — a genuine resolution, but only for citations. The thread was introduced as a rubric dimension over all output and developed as a structural property. Chapter 14 closes the citable subclass without saying the general problem stays open.

**Verification (Ch 18).** `18:167` closes it "as logging and reproducibility". Every earlier station is a *check* — prompts (Ch 4), drift (Ch 5), sources (Ch 14), arguments (Ch 17). Logging is provenance: it records what you did without testing whether it was right. `18:173` bridges this in one asserted line. Either argue the bridge — a logged prompt is what makes a later check possible — or close on the check itself.

### 12. Empirical-claim inventory

**Needs citation or demonstration:** `18:89` (Issue 1); `18:49–51`, `18:31` (Issue 2); `16:47` (Issue 4); `17:107–108` (Issue 8); `15:93–94` (Issue 9); and `14:133` "This costs about thirty seconds per source" — a number with no basis. Drop or measure it.

**Methodologically incomplete rather than uncited:** `14:47–49`, the PDF extraction failure modes. Two-column interleaving, equation degradation and table structure loss are tool-dependent, and no extractor is named anywhere in the deck — unfalsifiable as stated, unreproducible on a different pipeline. Name the extractor or run it live; the phenomena are real and `14:55` is sound regardless.

**Safely craft advice, no citation warranted:** `14:73–75`, `14:85`, `14:87–95` (the remedy is stated on the slide, which is what makes it safe), `14:107`, `15:26–29`, `15:66`, `15:104–106`, `16:92`, `16:116–117`, `16:136`, `17:67`, `18:125–128` — procedural recommendations whose justification is on the slide.

**Minor precision defects:** `16:106` "A vectorised rewrite changes numerical behaviour at the edges" — imprecise twice: the mechanism is reassociation of floating-point operations and changed reduction order, affecting results throughout rather than "at the edges"; and it *can* change behaviour, not *does*. `16:124` "That sentence has appeared in every chapter of this course" — grep finds "state the check" only in decks 16 and 19.

### 13. Sequencing — clean, one loose constraint

Nothing depends on later material; forward references (`17:98,121,131`) are signposted. But `architecture.md:80` makes "**12 before 14** — retrieval capability before literature work depends on it" non-negotiable, and deck 14 never uses or mentions Chapter 12. Either the deck is missing the retrieval half of literature work, or the constraint is vestigial.

### 14. Is Chapter 19 a capstone? — partly

The four-test slide and "why these four" are genuine synthesis, arguing from the course rather than asserting. The rest is summary: `19:66` restates `18:69–70`; `19:81–84` is a checklist of pointers. And the capstone task at `19:76` has **no stated success criterion**, in a course whose closing line is "state the check before you do the work" (`19:126`) — the one exercise in the session that does not do what the course demands. Fix: "at the end of the hour you can name what you verified, how, and what you could not."

## Questions to Probe

1. **`18:89`** — has the local/remote split been run against the installed version, or carried from documentation? `references.md:339`'s instruction to confirm and pin appears unactioned.
2. **The MATLAB demonstration** — how many tasks, how many runs? What does the deck say when the Python side fails on the day? The `TODO(capture)` fallback has the same n=1 problem.
3. **Why is Chapter 6 absent from the Chapter 18 lab standard** — deliberately out of scope, in which case the closure should say so, or an omission?
4. **Chapter 14's second scope-laundering example** — planned for the unwritten Chapter 2 or 6, or has "twice" drifted from what was built?
5. **Zero citations across six decks** — deliberate for the practice half, or an artefact of drafting before the `Cite` rollout `slides/README.md` calls "the remaining cost"? That decides whether Issues 1, 2 and 8 are three defects or one.

## Bottom Line

The thread closures exist, name their origins, and two of three genuinely resolve. Chapter 16 handles its central claim more carefully than the brief that commissioned it, and that deviation should be pushed back into the brief. What needs work is evidence discipline on the few claims about the world rather than about practice — and one, `18:89`, is `[P]`-tagged and load-bearing for an NDA decision. That is the one item I would not ship unverified. Chapter 19 needs one re-derivation (test 1 from Chapter 5, not Chapter 1) and one addition (untrusted input), after which its four-test slide is the strongest artefact in the session.

## What this review did not do

- Decks for Chapters 2, 6 and 8 do not exist; back-references to them (`14:139`, `18:166`) were checked against the briefs only.
- I did not build or export any deck — no assessment of rendering, click ordering, or whether the mermaid diagram at `15:44` survives PDF export, which matters under the "nothing load-bearing may be interactive-only" rule.
- I did not verify the generated-imagery claims (Issue 9); flagged SUSPECTED for that reason.
- I did not review exercise feasibility against session time, nor the run sheet, reference card, or `assets/` beyond `figures/gen-figures.py`.
- I did not execute `npm run check:cites`; the coverage claim is read from `scripts/check-cites.mjs:14,19`.

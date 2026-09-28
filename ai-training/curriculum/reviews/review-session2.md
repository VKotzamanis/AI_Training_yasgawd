# Peer review — Session 2 decks (Chapters 9–13)

Reviewed: `slides/09-the-agent.md`, `10-memory.md`, `11-orchestration.md`, `12-extension.md`, `13-access.md`
Against: `CLAUDE.md`, `curriculum/chapter-briefs.md` (Ch 9–13), `references.md` (tag definitions; Chapters 9–13 — Instruments), `DECISIONS.md`.
Status: IN PROGRESS — partial file, being extended.

## Summary

The five decks are structurally sound and the thread bookkeeping is largely honest. Three defects are serious enough to stop delivery of the chapters they sit in.

First, Chapter 13's centrepiece derivation does not close dimensionally. As written on the slide, the chain yields byte-hours per token, not bytes per token, and it omits both the residency time and the construction of the byte-hour price. The next slide then claims "the units carry the derivation", which is the claim that will fail live.

Second, evidence discipline is enforced by a build check that only inspects citation *keys*. Every claim on a slide with no `<Cite>` is invisible to it. Chapter 12 has zero citations across nine slides and carries material traceable only to a `[P]` entry (graphify) and a `[U]` entry (Antigravity) — a direct breach of hard rule 1, which the toolchain cannot see.

Third, version-fragility marking is close to inverted. Of roughly thirty flat, version-dependent claims across the five decks, three carry a marker — and two of those three sit on slides containing no version-specific content, while the version floors actually recorded in `references.md` (`v2.1.203+` for ultracode, `v2.1.205` for the checkup) appear on no slide at all.

Chapter 12's blocker is marked, but its accompanying reassurance is false. Chapter 13's blocker is marked but attached to the wrong slide, and the brief item it actually blocks is missing from the deck entirely.

## Key Issues

### 1. The Chapter 13 worked example does not yield bytes per token — CONFIRMED

`13-access.md`, "Worked example: architecture from a price list". The chain as shown:

> "price step at a stated context length" $\Rightarrow$ "extra cost attributable to cached context"
> "$\div$ tokens of context" $\Rightarrow$ "cost per cached token"
> "$\div$ price per byte-hour" $\Rightarrow$ "**bytes per token in the KV cache**"

Worked through as displayed:

- **Step 1 → 2 is unit-inconsistent.** A published price step is a change in currency *per token*. Dividing that by "tokens of context" gives currency per token squared, not "cost per cached token". The step only closes if an unstated multiplication by a token count or a request happened inside step 1. The slide never says what the "extra cost" is *per*.
- **Step 3 leaves a residual time dimension.** $[\$\cdot\text{token}^{-1}] \div [\$\cdot\text{byte}^{-1}\cdot\text{hour}^{-1}] = \text{byte}\cdot\text{hour}\cdot\text{token}^{-1}$. That is byte-hours per token. To reach bytes per token you must divide by the residency time — how long the KV cache is held in device memory while the request is served. **That step is absent from the slide.**
- **The denominator is undefined.** No vendor publishes a "price per byte-hour". It has to be constructed, typically as (accelerator price per hour) ÷ (bytes of HBM per accelerator). That is the assumption the entire result rests on and the first thing a hostile engineer attacks. `CLAUDE.md` Conventions is explicit: "If an equation's denominator is defined non-obviously (see the MACs-vs-FLOPs erratum in Chapter 4), state the definition alongside it." This is exactly that case, and the definition is not there.
- **Which token is never said.** "tokens of context" (cached input), the token the price step is charged per, and the output tokens generated while the cache is resident are three different quantities. The phrase "cost per cached token" merges them silently.

Why it matters: this is the chapter's centrepiece, sold as a demonstration of dimensional analysis, and the very next slide asserts "**Dimensional analysis** — the units carry the derivation, exactly as in Chapter 7." They do not carry, as presented. Working it live in front of five engineers who do dimensional analysis for a living is the worst place to discover that.

Fix: insert the two missing steps (÷ residency time; and the construction of the byte-hour price from an accelerator hourly rate and its memory capacity), and label each intermediate with its units on the slide rather than in prose.

### 2. The 1.7 kB figure is not defined precisely enough to be checkable — SUSPECTED

`13-access.md`: "the answer came out at roughly **1.7 kB per token** — then sanity-checked against plausible head dimensions and KV head counts, which is the step that turns arithmetic into evidence."

The sanity check is claimed but not shown, so I reconstructed it. Under the standard parameterisation — K and V both stored, 2 bytes per element, no latent compression:

bytes/token = 2 (K and V) × n_layers × n_kv_heads × d_head × 2 bytes

Setting that to 1700 B requires n_layers × n_kv_heads × d_head ≈ 425. At 60 layers that is roughly 7 per layer — less than one head of dimension 64. The figure only reconciles if the model compresses KV far beyond ordinary grouped-query attention, **or if 1.7 kB is per layer per token** (60 layers → ~100 kB/token, an unremarkable number).

The slide does not say which. This is the MACs-versus-FLOPs failure mode that Chapter 4 uses as its anchor artefact — an undeclared definition producing a clean factor error — reproduced in Chapter 13. Marked SUSPECTED because I do not have the Pope transcript in front of me and the primary derivation may resolve it.

Fix: state on the slide whether the quantity is whole-model or per-layer, and show the head-count arithmetic rather than asserting it was done. Also state the context length and the price — "a stated context length" states nothing, so nothing on the slide is reproducible even before the pricing goes stale.

The `TODO(verify) before delivery` box is good and correctly scoped to staleness. It does not cover the omission of the inputs, which is a separate problem.

Not a defect, for the record: `<Cite k="pope2026" />` resolves through `sources.json` with `kind: testimony` and `coi: true`, so the footer renders "Expert testimony, not a primary source. COI declared." The `references.md` COI requirement for Chapter 13 is met by the component.

### 3. Chapter 12 puts [P] and [U] material on slides, and the build check cannot see it — CONFIRMED

`12-extension.md` contains **no `<Cite>` element anywhere** across nine slides. `scripts/check-cites.mjs` only inspects `<Cite k="...">` keys; a slide with no citation passes silently. So hard rule 1 — "Only `[V]` may appear in slide content" — is unenforced exactly where it is breached.

- "**Graphing a codebase or a document set**": "Edges are labelled by how they were obtained: **extracted** from the syntax tree, or **inferred**" and "the **semantic pass over documents leaves the machine while the code pass does not**". The only record is `references.md`: "Graphify: ... semantic pass over documents uses an API. — **[P]** confirm against the current repository and pin a version." A `[P]` claim is on a slide, and it is load-bearing: the slide routes it into governance — "which makes it a Chapter 18 data-governance question". A data-governance instruction resting on a partially-verified claim is the worst place for that tag.
- "**Cross-provider retrieval: a licensing asymmetry**": "A second provider reachable from the same session can retrieve sources the first is not licensed to return." The only record is "Antigravity (Google) as the group's Gemini access path — **[U]** *instructor-supplied*."
- The three MCP slides ("The problem a protocol solves", "Host, client, server", "Three things a server can expose") carry no citation and `references.md` has **no MCP entry at all** — only a search term. "Without a common protocol that is N tools times M clients ... A protocol collapses that to N plus M" is a flat claim about a published specification with no source in the file.

Fix: verify graphify against the installed package and move it to `[V]` with a pinned version, or mark the slide `TODO(verify)`; add an MCP specification entry to `references.md` and cite it; and see item 4 for the cross-provider slide.

### 4. Chapter 12's blocker note is marked plainly but overreaches — CONFIRMED

`12-extension.md`, "Hands-on": "**BLOCKED — needs the working Antigravity configuration.** ... **Nothing on the preceding slides depends on it.** The hands-on exercise does, entirely."

The second sentence is false. The cross-provider retrieval slide *is* the Antigravity capability. Its central factual claim — that a second provider is reachable from the same session and returns sources the first cannot — is precisely what the missing configuration would establish. What is true is that no preceding slide needs the configuration *detail*; what is not true is that nothing depends on it.

Why it matters: the reassurance is the sentence a reader uses to decide the chapter is safe to teach as-is. It licenses delivering an unverified claim.

Fix: "The preceding slides state the mechanism; the cross-provider slide's claim is unverified until the configuration is documented. The hands-on exercise depends on it entirely."

On framing, the deck is compliant. "Taught as **a licensing asymmetry with a provenance obligation**. Not as circumvention, and not as a trick", with all three brief caveats present (onward use, source quality, recorded chain). That matches the locked decision in `DECISIONS.md` and the brief. No defect.

### 5. Version-fragility marking is close to inverted — CONFIRMED

Three markers exist across five decks. Two of them sit on slides with nothing version-specific to hedge.

- `09-the-agent.md`, "Session commands worth knowing on day one": "**Version-fragile.** Command names, flags and behaviours change between releases. **These are correct as recorded.**" The slide names no command, flag or behaviour — its three bullets are "Check your setup and configuration", "Check your usage early", "Resume a previous session". "These" has no referent. This is simultaneously a vacuous hedge and a brief gap: the brief requires "core session commands", and an attendee leaves unable to execute any of them.
- `11-orchestration.md`, "Inspecting running work": "**Version-fragile.** The specific commands, flags and **version floors** here are correct as recorded". The slide contains no command, flag or version floor. Meanwhile the ultracode slides two positions earlier — where `references.md` records the floor `v2.1.203+` — carry no marker.
- `13-access.md`'s `TODO(verify)` on pricing is the one marker correctly placed.

Unmarked version-dependent claims, by deck:

**Ch 9** — desktop app and editor extension as the primary entry points; "A browser fallback exists"; "Read-only by default. Nothing is written until you say so"; "Every proposed edit is shown as a **diff** before it is applied"; "Permissions are per action, and can be narrowed or broadened per project"; plan mode producing text before a file is touched; the compact and clear behaviours.
**Ch 10** — "A project instruction file is read into the window at the start of every session"; "in recent versions, memory files and unused components" (floor `v2.1.205` recorded, omitted); the three-level personal/project/local hierarchy; "You can ask the tool to draft its own instruction file"; "Both are standing context that loads **only when needed**". Chapter 10 has **no** version marker anywhere.
**Ch 11** — the subagent definition; hook event names ("before a command runs, when a session starts, when a prompt is submitted"); saved and re-runnable workflows; all three ultracode claims; "`/usage`".
**Ch 12** — MCP primitives; graphify behaviour; cross-provider reachability. **No** version marker anywhere.
**Ch 13** — "A paid chat subscription does not include API access"; "billed against prepaid credit, per token"; caching, batch discounts and subscription-versus-per-token economics.

Fix: one standing version-fragility footer per deck rather than a per-slide note, and put the recorded version floors on the ultracode and checkup slides where `references.md` already holds them.

### 6. The three ultracode claims against the record — one accurate, one narrowed, one unquantified

`references.md` `[V]` entry: "Ultracode: session-scoped setting pairing xhigh reasoning with automatic workflow orchestration; `/effort ultracode`, `claude --effort ultracode` (v2.1.203+), or the bare keyword for a single task. Silently ignored in persistent settings fields; subagents auto-approve edits; significant cost premium."

**Claim 1 — session scope. Accurate.** `11-orchestration.md`: "**It is session-scoped.** Put it in a persistent settings field and it is *silently ignored* — no error, no warning, and you believe it is on for weeks." "No error, no warning" restates "silently"; "for weeks" is a consequence, not a software claim. No overstatement.
But the deck **understates the record by omission**: it never gives `/effort ultracode`, `claude --effort ultracode`, the bare-keyword form, or the `v2.1.203+` floor. In a hands-on chapter, the deck teaches a trap about a setting it never shows how to set — and Chapter 11 is where `references.md`'s most specific recorded detail is discarded.

**Claim 2 — subagents. Understated.** Slide: "**Subagents inside a workflow auto-approve file edits.** The diff-review discipline from Chapter 9 does not hold inside the fan-out." `references.md` records it unqualified: "subagents auto-approve edits". The slide adds a scope the `[V]` record does not contain. If the record's broader form is right, an attendee concludes that a plain subagent — taught two slides earlier on the "Subagents" slide, which carries **no** auto-approve warning — still shows diffs before writing. That is a safety-relevant narrowing in the deck that most explicitly builds on Chapter 9's "Approving a diff you have not read is the whole risk of this chapter".
Note the brief carries the same "inside a workflow" scoping, so the deck is brief-compliant and `references.md` is the file that is ambiguous. Either way, the slide asserts a scope no `[V]` record supports. Resolve against the documentation before delivery and fix whichever file is wrong.

**Claim 3 — cost premium. Neither over- nor understated, but unfalsifiable as written.** Slide: "**It carries a significant cost premium.**" plus "The premium is not a rounding error". `references.md` says only "significant cost premium" with no magnitude. The two amplifications sit under `<Cite k="claudecode-docs" />`, so they read as quantified vendor documentation. In a session whose next chapter closes the cost thread with an invoice, the weakest-evidenced cost claim is delivered with the most confidence.
Fix: state the multiplier if the documentation gives one, or say plainly on the slide that the magnitude is not published.

### 7. Citation footers attribute instructor judgement to vendor documentation — CONFIRMED

`Cite.vue` renders a footer spanning the whole slide, so every claim on that slide inherits the attribution. Several slides mix vendor fact with instructor judgement under one footer:

- `11-orchestration.md`, "Subagents", under `<Cite k="claudecode-docs" />`: "A subagent reasoning from priors returns fluent, ungrounded output that reads exactly like verification" and "**Give a subagent the evidence, not the question.**" That is instructor practice, not documentation.
- `09-the-agent.md`, "The permission model is the safety story", under `<Cite k="claudecode-docs" />`: "**The diff is the artefact of responsibility.** It is the moment the change becomes yours."
- `11-orchestration.md`, "Hooks", under the same key: "Prose in an instruction file is a **request**. A hook is a **guarantee**."

Why it matters: this is the failure the course spends three sessions warning against, in the course's own footers. `CLAUDE.md` requires the citation footer to carry "author, year, venue, identifier" — it does not distinguish which claims on the slide the source covers.

Fix: either split judgement claims onto uncited slides, or add a scope note to the footer ("mechanism from the documentation; the framing is the instructor's").

Related: `11-orchestration.md` "Teach `/usage` early" is the only literal command name in the five decks, appears on a slide with **no** citation footer, and `/usage` does not appear in `references.md` — which records only `/doctor` and `/checkup`. Chapter 9 was careful not to name commands; Chapter 11 names one, unsourced.

Related: `anthropic-support` is defined in `sources.json` and used **nowhere** in the repository. Two claims should be carrying it. `09-the-agent.md`: "A browser fallback exists for a machine that fights the install" — cited to `claudecode-docs`, while the nearest record is "Claude Cowork availability and capabilities, support.claude.com — **[V]**". `13-access.md`: "**A paid chat subscription does not include API access.**" — cited to `claudecode-docs`, while the record is "Paid Claude subscriptions do not include API or Console access; API is billed via prepaid usage credits. — **[V]**", a support-centre fact, not a Claude Code fact. SUSPECTED on the browser fallback (the record is not specific enough to be certain the two refer to the same thing); CONFIRMED on the subscription boundary.

### 8. Chapter 13 contradicts itself inside one bullet — CONFIRMED

`13-access.md`: "API usage is billed against prepaid credit, per token, **with no monthly ceiling protecting you.**"

Prepaid credit *is* a ceiling by construction — you cannot spend past what you have loaded. The clause is true of a postpaid account and false of the prepaid model named one clause earlier. The `[V]` record says "billed via prepaid usage credits" and nothing about an absent ceiling.

Why it matters: the slide's purpose is to make a room of grant-funded researchers understand their financial exposure, and it misstates the direction of that exposure.

Fix: "there is no monthly subscription cap; your exposure is the credit you have loaded, plus whatever auto-reload you enable."

### 9. Chapter 13 drops a brief item, and its blocker points at the wrong slide — CONFIRMED

The brief requires "making a first call and varying parameters". **No slide covers it.** The deck runs: what a key authorises → key hygiene → worked example → local versus frontier → closing the cost thread → where this leaves us.

`DECISIONS.md` item 4 says the reachability question "**Blocks the Chapter 13 exercise**". The deck's blocker note is attached to the local-versus-frontier demo:

> "**TODO(capture)** — needs the local machine reachable from the training room. If it is not, this becomes an instructor demo and keys are distributed afterwards. `DECISIONS.md` item 4."

That is honest about the demo. But the exercise item 4 actually blocks — the attendee's first call against the gateway — is absent from the deck, so its absence is unmarked. Meanwhile the key-hygiene slide promises it in the present tense: "The group's local gateway issues per-user keys with per-user budgets. That is **the mechanism that makes an exercise safe to run in a room**" — an exercise the deck never delivers.

Fix: add the first-call slide with the parameter-varying step, and put the item 4 blocker on it as well as on the comparison demo.

### 10. Chapter 10's cost-of-memory argument ignores caching, which Chapter 13 then teaches — CONFIRMED

`10-memory.md`: "$$\text{cost}_\text{standing} \;\propto\; N_\text{file} \times T_\text{turns}$$" and "A file twice as long costs twice as much, on every turn, forever."

`13-access.md` three chapters later: "**Caching.** Re-sending the same standing context every turn is the cost Chapter 10 made you calculate. Caching is the mitigation, and it has its own price."

Standing context is the canonical cached prefix. Cache reads are billed at a fraction of the base input rate, so the linear-in-turns relation Chapter 10 states as unqualified fact is the uncached bound, not the operative cost. The direction of the argument survives — a bloated file still costs more — but the magnitude does not, and the argument that "a bloated instruction file is an engineering problem, not an untidiness problem" is being carried by a number that is wrong by the cache discount.

Fix: one clause — "before caching; Chapter 13 puts the discount on it." The forward pointer already exists ("Chapter 13 puts a price on the same tokens"); it just needs to admit the relation changes.

Minor, same slide: "$N_\text{file}$ — tokens in the instruction file. $T_\text{turns}$ — turns in the session. **Both dimensionless counts.**" Declaring both dimensionless obscures that the proportionality constant carries currency per token per turn. `CLAUDE.md` requires equations to carry dimensional analysis; this one states the symbols and then flattens their dimensions.

### 11. Chapter 10 tells attendees to put keys in a memory file; Chapter 13 forbids it — CONFIRMED

`10-memory.md`, "The hierarchy": "**Local** — machine-specific paths and **keys**. Never committed."
`13-access.md`, "Key hygiene": "**Environment variables, never source.** A key in a script is a key in your shell history and your editor's autosave." and "**Never in a shared repository.** Not in a private one either — private repositories get shared."

A local instruction file is a file in the project directory. "Never committed" depends entirely on a gitignore entry surviving; the Chapter 13 rule exists precisely because that assumption fails. The two slides give opposite instructions on the same afternoon, and the security-relevant one comes second.

Fix: delete "and keys" from the Chapter 10 bullet. Nothing else on that slide depends on it.

### 12. Chapter 9's contamination demonstration cannot support its own conclusion — CONFIRMED

`09-the-agent.md`, "Demonstration: what contamination looks like":

> "Run one task in a fresh session. Record the answer. Run the same task after a long, unrelated conversation in the same session. Record the answer. Compare."
> "This is Chapter 4's noise floor, met again in a place where it costs you working hours instead of a grading sheet."

One run per arm. Chapter 4's whole contribution is the A-versus-A null strip — measuring run-to-run variance at fixed condition *before* reading any A/B result — and the finding that five cases buy a screen, not a finding. This demonstration is n=1 versus n=1 across a changed condition with no null strip and no pass criterion defined in advance. It invokes Chapter 4 while performing the design Chapter 4 exists to forbid.

The `TODO(capture)` hedge partly rescues it — "The point is not that the second answer is wrong; often it is not. The point is that you could not have predicted which" — but "you could not have predicted which" is itself a claim about variance that a single pair cannot establish.

Why it matters: this is Session 2's first demonstration, in front of an audience whose expertise is experimental design, and Chapter 4 is described in its own brief as the highest-value chapter in Session 1. Undercutting it eight chapters later costs more than the demo is worth.

Fix: run each arm three times and show the spread, or reframe the slide explicitly as an illustration rather than a measurement and say so on the slide.

### 13. Chapter 10 reinstates the analogy Chapter 8 exists to break — CONFIRMED

`10-memory.md` title slide and frontmatter: "### Building the hippocampus Chapter 8 said was missing" and "The model has no hippocampus. **So you have to be its hippocampus.**" Repeated in the closer: "The memory thread closes here: bounded buffer, degradation, missing hippocampus, management, and now a replacement you built."

Chapter 8's brief: "**Run the analogy, then break it.** The break is the content ... The context window is not a hippocampus. It is a buffer that gets discarded." Hippocampal consolidation writes episodic experience into durable memory; a text file re-inserted into a fresh window is re-prompting, not consolidation, and the model's weights remain frozen — which is the exact point Chapter 8 is built to land. The imperative "you have to be its hippocampus" is a rhetorical device and survives. "**Building** the hippocampus" and "a replacement you built" assert that the artefact *is* the missing organ, which reinstates what Chapter 8 dismantles, in a deck title and in a closer.

Compounding it, Chapter 8 is not written and `references.md` records both its primary citations as "**[U]** authors, year, venue and claim all unconfirmed. **Both are load-bearing for the chapter and both are unverified.**" Chapter 10 asserts the content of that unwritten chapter in three places — the frontmatter `info:`, the subtitle, and "Chapter 1 said so; Chapter 8 named what is absent."

Fix: keep the opening line verbatim (it is the assigned handoff) and change the subtitle and closer to describe what the artefact actually is — standing context you own, versioned and shared. The chapter's real argument does not need the organ.

### 14. Sequencing: the handoff line lands one chapter late, and the two planning documents disagree — CONFIRMED

`DECISIONS.md`, Locked: "Chapter 7 before Chapter 8 | Cost before brain comparison | Concrete before abstract; **Session 1 ends on the memory-gap line that opens Session 2**."
`chapter-briefs.md`, Chapter 10: "**Opens on Chapter 8's closing line.**"

These are not the same instruction. Session 2 opens with Chapter 9, whose actual opening is "Session 1 was a system that answers. This one edits your files." The memory-gap line then appears roughly ninety minutes later, at the top of Chapter 10. The decks follow the brief, so this is a defect in the planning documents that the decks inherit — but it means the line `DECISIONS.md` treats as the session hinge is not doing that job, and Chapter 9's own opening does not reference Chapter 8 at all.

Because Chapter 8 does not yet exist, this is cheap to fix now and expensive later: Chapter 8's closing line is quoted verbatim in three places in `10-memory.md` and will have to be changed in all three if the chapter's conclusion shifts when its `[U]` citations are read.

Fix: reconcile `DECISIONS.md` with the brief, and treat Chapter 8's closing line as a single string owned by Chapter 8 rather than duplicated into Chapter 10's frontmatter, subtitle and body.

### 15. Chapter 9 calls compaction "cheap" three slides after invoking Chapter 7 — CONFIRMED

`09-the-agent.md`, "Three moves": "**Compact** — summarise the session so far and continue. **Cheap**, lossy, and the loss is invisible."
Two slides earlier: "Chapter 5 told you what happens to accuracy as it fills, and **Chapter 7 told you what it costs**."

Under Chapter 7's roofline, summarising the whole session is a full-context operation with a KV-fetch term linear in context length — the most expensive single call available at the moment you make it. The charitable reading is "cheap in effort" or "cheap relative to what it saves", but paired with "lossy" the bullet reads as a cost-benefit statement, and this deck has just told the room that cost has an equation.

Fix: "cheap relative to continuing on a full window" or drop the word. The amortisation argument is correct and takes four words.

Note, to the deck's credit: the same slide keeps cost and accuracy properly separated ("Chapter 5 told you what happens to accuracy ... Chapter 7 told you what it costs"), which is `CLAUDE.md` hard rule 3 observed correctly. The context-engineering material meets the brief in full — compact, clear, abandon, all three named, with the judgement about which one to use.

### 16. Chapter 12 has no closer and no handoff — CONFIRMED

`09`, `10`, `11` and `13` each end with a "Where this leaves us" slide and a forward pointer. `12-extension.md` ends on the blocked hands-on box, its last line being "The exercise, once unblocked: connect one server, list what it exposes, call one tool, read one resource, and record where the data went."

So the Chapter 12 → 13 handoff does not exist, and the deck's final impression is a blocker rather than a close. Chapter 12 is also the shortest of the five at nine slides while carrying the largest brief (protocol, host/client/server, three primitives, graphing, cross-provider retrieval, trust boundary).

Fix: add the closer and the pointer into Chapter 13 when the block clears; they do not depend on the Antigravity configuration.

### 17. Duplication between chapters — minor, CONFIRMED

- **The plan-cost argument is made twice.** `09-the-agent.md`: "Plan mode produces the intended change as text, before a single file is touched, and **it is far cheaper to reject a plan than a patch**." `11-orchestration.md`: "**Rejecting a plan costs a minute. Rejecting forty files of edits costs an afternoon** and your patience." Chapter 11's slide does add a scale-specific point ("the plan is the artefact you review — not the diff, which arrives too late and too long"), but the cost asymmetry is the same argument in the same shape. Cut it from one.
- **The checkup appears in both Chapter 9 and Chapter 10.** `09`: "Check your setup and configuration when something behaves oddly, before you debug the thing itself." `10`: "**Run the checkup, live** — The built-in setup check audits configuration". Chapter 10's treatment is the substantive one and the brief assigns it there. Chapter 9's mention adds nothing and, being unnamed, is not actionable.

No other duplication found across the five decks. The thread bookkeeping in the closing boxes is consistent and non-overlapping: memory closes in 10, trust boundary passes through 12 to 18, cost is picked up in 11 and closed in 13.

## Questions to Probe

1. **What is the residency time in the Chapter 13 derivation, and where does the byte-hour price come from?** Both are required for the chain to close and neither is on the slide. If the answer is "Pope does it differently", the slide should show his chain, not a compressed version of it.
2. **Is 1.7 kB per token whole-model or per layer?** The reconstruction in item 2 does not close at whole-model under standard assumptions. This determines whether the sanity check the slide claims to have performed actually passes.
3. **Do subagents auto-approve edits only inside a workflow, or generally?** `references.md` and the brief disagree by omission. The answer changes whether the "Subagents" slide needs its own warning, and it is safety-relevant.
4. **Is the cross-provider retrieval claim verifiable without the Antigravity configuration?** If not, Chapter 12 is blocked on more than its exercise, and the "Nothing on the preceding slides depends on it" line has to go now rather than at the fix.
5. **Was Chapter 12's PDF exported as a finished chapter?** `CLAUDE.md` says to export "whenever a chapter is finished"; `exports/12-extension.pdf` exists for a chapter the deck itself marks BLOCKED. Worth confirming the export convention distinguishes built from finished, or the PDF fallback will present blocked material as complete.

## Bottom Line

Chapters 9, 10 and 11 are deliverable after small fixes: the compaction cost claim, the keys-in-a-memory-file contradiction, the caching qualifier on the cost equation, the misplaced version-fragility notes, and the Chapter 10 hippocampus framing. None of those is structural.

Chapter 13 is not deliverable as written. Its centrepiece derivation does not produce the quantity it claims to produce, and it is the one slide in the five decks guaranteed to be worked through live by people who will catch it. Fix the chain, state the inputs, and add the missing first-call exercise the brief requires.

Chapter 12 needs its evidence base repaired independently of the Antigravity block. The MCP section has no source at all, the graphify material is `[P]` and routed into a governance instruction, and the build check cannot see either problem because the deck contains no citation keys. That last point generalises: `check-cites.mjs` validates the citations that exist and is blind to the claims that have none, so the strongest guarantee in the toolchain is the one most easily evaded by omission.

The brief compliance is otherwise good. Chapter 9's context engineering is treated as a named skill with the accuracy-versus-cost distinction held correctly; Chapter 10's exercise delivers the artefact and the cost-of-memory argument is the right argument; Chapter 11's judgement call is concrete and two-sided; Chapter 12's cross-provider framing is exactly the licensing asymmetry with a provenance obligation that `DECISIONS.md` locked, with all three caveats on the slide.

## What this review did not do

- Did not fetch any vendor documentation. Every version-dependent claim was checked against `references.md` only, so "accurate" above means "consistent with the record", not "true of the current release". The record itself is dated and `DECISIONS.md` item 6 requires re-fetching in the week before delivery.
- Did not read the Pope transcript. Items 1 and 2 are assessed on the slide's own chain and on a reconstruction with stated assumptions; the primary source may resolve item 2.
- Did not review Chapters 1–8 or 14–19, and so did not verify that the incoming threads Chapters 9–13 claim to pick up were actually started where they say. Chapter 8 does not exist, which is checked; the rest is asserted.
- Did not build the decks or run `check-cites.mjs`. The build-check analysis is from reading `scripts/check-cites.mjs`, not from executing it.
- Did not open the exported PDFs, so did not verify that the `v-click` sequencing in the Chapter 13 derivation survives PDF export — which matters, because `CLAUDE.md` says nothing load-bearing may be interactive-only and that derivation is built entirely from `v-click` steps.

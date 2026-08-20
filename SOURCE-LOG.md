# Source log

Every URL fetched while working on this repository, with how it was fetched.
Method is the load-bearing field: `WebFetch` and `gh` return primary text;
a subagent or `agy` returns another model's paraphrase. Distinct from
`references.md`, which tracks citations and their verification status.

- https://aclanthology.org/2024.findings-emnlp.888/ — 2026-08-19 19:13 — WebFetch — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — verify author list/venue/DOI for the persona-prompting null result proposed as a Chapter 4 test claim
- https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/ — 2026-08-19 19:13 — WebFetch — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — verify the chain-of-thought-on-reasoning-models figures proposed as a Chapter 4 test claim
- https://docs.claude.com/en/docs/build-with-claude/extended-thinking — 2026-08-19 19:40 — subagent WebFetch (paraphrase, not primary text read by me) — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — whether a thinking transcript is captured with output, for the eval worksheet blinding procedure
- https://www.anthropic.com/news/visible-extended-thinking — 2026-08-19 19:40 — subagent WebFetch (paraphrase, not primary text read by me) — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — same question, scratchpad design intent
- https://www.emergentmind.com/topics/persona-prompting-pp — 2026-08-19 19:40 — subagent WebFetch (paraphrase, not primary text read by me) — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — whether persona prompts produce first-person self-identification, i.e. a blinding leak
- https://arxiv.org/abs/1706.03762 — 2026-08-19 19:52 — WebFetch — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — confirm title, author list, year and identifier for the Chapter 1 attention citation, upgrading it from [P] to [V]
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12595464/ — 2026-08-19 20:08 — WebFetch — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — test the Chapter 7 brief's claim that neuromorphic hardware is "deployed, engineering-grade"; it is not, and the brief is corrected
- https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2023.1017235/full — 2026-08-19 20:08 — WebFetch — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — establish what organoid computing has actually demonstrated, for the Chapter 7 alternative-substrates slide
- https://arxiv.org/abs/1707.04585 — 2026-08-19 20:12 — WebFetch — session 3f1bda6d-a75b-4340-88ec-9d2b69beb998 — confirm authors/title/identifier for the RevNets citation, which the tightened cite check blocked from a slide at [P]

# Prompts

Prompts for building the training slides. Each file holds the original prompt (where we may reproduce it), our adapted version, and when to use it. The rules they apply are in [`../TEACHING_LOGIC.md`](../TEACHING_LOGIC.md).

| # | Prompt | Use it to | Stage |
|---|---|---|---|
| 04 | [Session plan and time budget](04-session-time-budget.md) | Order topics by question, budget time, mark demos | Plan |
| 05 | [Tutor configuration](05-tutor-configuration.md) | Draft a visual, cause-first teaching sequence for a topic | Plan |
| 07 | [Build a section](07-build-a-section.md) | Run the whole method for one section | Build |
| 06 | [Plain-language term](06-plain-language-term.md) | Explain a difficult term simply, without saying anything false | Build |
| 01 | [Structural metaphor](01-structural-metaphor.md) | Build an analogy that states where it breaks | Build |
| 02 | [Cite your sources](02-cite-your-sources.md) | Check every factual claim against a source | Verify |
| 03 | [Study-question check](03-study-questions-check.md) | Test whether the slides answer what attendees will ask | Verify |

Typical order: 04 → 05 → 07, which calls 06, 01, 02 and 03 along the way.

## Sources and licensing

- Prompts 01, 02, 03, 04 and 06 are adapted from [langgptai/awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts). Its README displays an MIT badge, but the repository has no license file. We quote the short originals with attribution.
- Prompt 05 is inspired by [Mr. Ranedeer AI Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor), which has no license file that we could find. We do not reproduce its text. Our version is written from scratch and keeps only its structure.

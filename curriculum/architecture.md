# Chapter Architecture

Supersedes all earlier drafts. Content inventories are in `chapter-briefs.md`; citations in `../references.md`.

## Two structures at once

**Chapters** are the sequence. Nothing is taught before the thing it depends on.

**Threads** are concepts that cannot live in one chapter. Truthfulness is introduced as a training-time rubric dimension, explained as a structural failure much later, tested somewhere else again, and enforced as a work habit at the end. Teaching it once would waste it.

Where a chapter picks up a thread, its brief says so. That referencing is what stops nineteen chapters reading as a list.

---

## Chapters

### Part I — What it is and how it got that way
| # | Chapter | One line |
|---|---|---|
| 1 | Substrate | What the system computes |
| 2 | Formation | How a predictor became an assistant |
| 3 | Control | Acting on what Formation described |
| 4 | Measurement | How you know any of Chapter 3 worked |

### Part II — Where it fails
| # | Chapter | One line |
|---|---|---|
| 5 | Intrinsic failure | What breaks with nobody attacking you |
| 6 | Extrinsic failure | What breaks when the input is hostile |
| 7 | Physical limits | What it costs to run |
| 8 | Brain and model | The question from Chapter 1, answered |

### Part III — Instruments
| # | Chapter | One line |
|---|---|---|
| 9 | The agent | Working with a system that acts |
| 10 | Memory | Building the hippocampus Chapter 8 said was missing |
| 11 | Orchestration | Delegating beyond one context window |
| 12 | Extension | Reaching outside the session |
| 13 | Access | Keys, endpoints, and what a call costs |

### Part IV — Practice
| # | Chapter | One line |
|---|---|---|
| 14 | Literature | Finding, screening, and citing without fabricating |
| 15 | Production | Documents, figures, and diagrams |
| 16 | Code and numerics | The audience's daily work |
| 17 | Critique | Attacking your own argument before a reviewer does |
| 18 | Governance | Disclosure, data, reproducibility, lab standards |
| 19 | Judgement | When not to use any of this |

---

## Thread map

| Thread | Introduced | Developed | Closed |
|---|---|---|---|
| **Truthfulness** | Ch 2 — a rated rubric dimension | Ch 5 — a structural impossibility | Ch 14 — a verification procedure |
| **Memory & context** | Ch 1 — a bounded buffer | Ch 5 degradation → Ch 8 the missing hippocampus → Ch 9 management | Ch 10 — external memory you build |
| **Cost** | Ch 1 — token as unit of meaning | Ch 7 unit of price → Ch 10 resident context → Ch 11 orchestration premium | Ch 13 — pricing and plan economics |
| **Trust boundary** | Ch 2 — harmlessness as trained behaviour | Ch 6 adversarial input → Ch 12 voluntarily opened channels | Ch 18 — data governance |
| **Verification** | Ch 4 — evaluating prompts | Ch 5 drift → Ch 14 sources → Ch 17 arguments | Ch 18 — logging and reproducibility |

Each thread is flagged at introduction as something that will recur. Each closure refers back explicitly.

---

## Sequencing constraints

Non-negotiable orderings and why:

1. **1 before 2.** You cannot describe what training shaped without describing what is being shaped.
2. **2 before 3.** Technique before mechanism produces cargo-cult prompting.
3. **3 before 4.** You need claims before you can test claims.
4. **4 before 5.** Measurement makes the limitations chapter actionable rather than discouraging.
5. **6 before Part III.** Threat model before capability. By Chapter 12 the room opens channels voluntarily.
6. **7 before 8.** Cost is concrete, the brain comparison is abstract; abstraction lands better second.
7. **8 before 10.** The memory gap must be felt before the fix is offered.
8. **9 before 11.** Single-agent competence before orchestration.
9. **12 before 14.** Retrieval capability before literature work depends on it.
10. **Part IV last.** Every applied chapter draws on at least two threads.

Chapter numbers are referenced by the thread map. Do not renumber without updating it.

---

## Pre-work

Sent one week before Session 1, roughly 60 minutes:

- Install Claude Desktop, sign in, confirm plan
- Complete Anthropic Academy *Claude 101*
- Bring one real, small, non-confidential problem from your own work
- Reply with one line confirming completion

Attendees who skip pre-work will slow the room. Say so plainly in the email.

---

## Contingency

| Risk | Mitigation |
|---|---|
| Attendee cannot install the desktop app | Web fallback |
| Pro usage limit hit mid-session | Pair with a neighbour; teach `/usage` early; heavy blocks before mid-afternoon |
| Ultracode demo burns limits | Demo on one directory; don't leave the session in ultracode |
| Local machine unreachable | Instructor demo; distribute keys afterwards |
| Third-party tool breaks between rehearsal and delivery | Pin versions |
| Wifi saturation | Pre-download demo repositories; offline slides |
| Live demo produces a wrong answer | Keep it. Narrate it. Best teaching moment available. |

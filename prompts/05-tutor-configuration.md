# 05 · Tutor configuration (visual, causal)

**Use when:** drafting the teaching sequence for a new topic, or when the presenter wants to learn a topic before teaching it.
**Teaching rules:** 2 (chain of questions), 3 (terms first), 4 (pair every idea with a picture).

## Original

Source: [Mr. Ranedeer AI Tutor, v2.6.2, by JushBJJ](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor), reproduced in [awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts#ai-tutor-mr-ranedeer).

We do not copy the original here. It is about 250 lines of pseudo-code written for ChatGPT (it requires GPT-4 plugins and runs a "token checker"), and we found no license for it. Our version below is written from scratch and keeps its useful structure:

- a configuration block (depth, communication style, reasoning framework);
- a fixed flow: assumptions → curriculum → lesson → test;
- test questions in three levels: simple familiar, complex familiar, complex unfamiliar;
- after each step, the two questions a learner would most likely ask next.

**On "Visual":** the original treats visual as one learning style among six, chosen per learner. We make visuals the default for every term and attendee. The evidence supports words plus pictures for learners in general (Mayer, *Multimedia Learning*, 2021). It does not support matching teaching to a learner's supposed style (Pashler et al., 2008). See `TEACHING_LOGIC.md`, rule 4.

## Our version

```
[Configuration]
Depth: [e.g. engineers with calculus and basic linear algebra, no machine-learning background]
Presentation: Visual. Every term and mechanism gets a described visual next to the words: what is on each axis, what moves, which colour marks what.
Communication style: [Socratic / Textbook / Plain language / Story]
Tone: [Neutral / Encouraging]
Reasoning: Causal. Explain the problem an idea solves before explaining the idea.
Language: English

Topic: [TOPIC]

Step 1 - Assumptions. List what an attendee at this depth already knows, and the prerequisites they are missing.
Step 2 - Curriculum. A numbered sequence of sub-topics. For each: the question it answers and why it comes at that point.
Wait for me to approve the curriculum.

Step 3 - Lesson (one sub-topic each time I say "next"):
  a. The problem this idea solves, shown with a concrete example.
  b. The idea, in words and as a described visual.
  c. A worked example, solved step by step.
  d. One common misconception and why it is wrong.

Step 4 - Test (when I say "test"): three questions (simple familiar, complex familiar, complex unfamiliar) with answers below a divider.

After each step, suggest the two questions an attendee would most likely ask next.
Never state anything false to simplify; say what a simplification leaves out.
```

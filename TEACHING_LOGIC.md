# Teaching logic for the AI training

This file sets out how we build each section of the training and why. Every slide must survive one question from an attendee: *why are we talking about this now?*

The rules below come from three places: learning-science findings (cited), our own failures (the activation-function section), and a workflow another user reported for an AI-built science explainer. That report is one anecdote with no measured learning outcome, so we borrow its method, not its claims.

## The rules

### 1. Start from what attendees should be able to do

Write 1–3 outcomes per section before any slide exists, phrased as something an attendee can do or explain. "Understand activation functions" is not an outcome. "Explain why a network without activation functions can only fit a straight line" is. The outcomes decide what stays in and what goes. (Backward design: Wiggins & McTighe, *Understanding by Design*, 2005.)

### 2. Order slides as a chain of questions

Each slide answers the question the previous slide raised, and raises the next one. The default order for a technical idea:

1. **Problem**: what goes wrong without this idea? Show it.
2. **Idea**: the smallest fix that solves that problem.
3. **Mechanism**: how the fix works.
4. **Trade-offs**: what the fix costs, and what the next variant fixes in turn.
5. **Where it is used**: only now, the catalogue of variants and real systems.

If a slide cannot name the question it answers, it is in the wrong place or should be cut.

### 3. Define terms before the mechanism that uses them

Attendees cannot follow a mechanism while also decoding its vocabulary. Introduce the key terms first, each with a plain version and a picture (prompt 06). (Pre-training principle: Mayer, *Multimedia Learning*, 3rd ed., 2021.)

### 4. Pair every idea with a picture

Every term and mechanism gets a visual alongside the words: a graph, a diagram, or a step-by-step build. People learn better from words plus relevant pictures than from words alone (multimedia principle, Mayer 2021).

We make this the default **for everyone**. We do not sort attendees into "visual learners" and others: matching teaching to self-reported learning styles has no good evidence behind it (Pashler et al., 2008, *Psychological Science in the Public Interest* 9(3)). Pictures help nearly all learners, and that claim holds up under review.

### 5. One idea per slide; cut decoration

Interesting but irrelevant material reduces learning (seductive-details effect: Harp & Mayer, 1998, *Journal of Educational Psychology* 90(3)). Every element on a slide must serve that slide's question. The slide title states the point ("Stacked linear layers collapse into one"), not the topic ("Linear layers"). Detail belongs in the speaker notes.

### 6. Simplify, but never say anything false

A simplification may leave things out. It may not state something untrue. When we simplify, the speaker notes record what was left out, and the visual should still show the correct picture even where the words do not name it.

Example from the reported explainer: salt water was shown as ions that assemble into a crystal lattice, and the narration never called salt a molecule. The simplification was deliberate and nothing false was said.

### 7. Use analogies that state where they break

An analogy must map structure (processes, constraints), not just surface. It must also say where it stops holding. An analogy with no stated boundary will be stretched by attendees until it misleads them (prompt 01).

### 8. Make it interactive only where the nuance is

A demo earns its place when a static picture hides *how something changes*: a parameter the attendee can vary and watch the effect. Before the reveal, attendees commit to a prediction ("What happens to the output if we stack ten linear layers?"). The demo then confirms or corrects their mental model.

Open decision: PowerPoint cannot run code. Real interactivity means linked HTML demo pages; inside PowerPoint we only have click-by-click builds and Morph transitions.

### 9. Compare candidate explanations before building

For each hard concept, draft 2–3 competing explanations (an analogy, a direct visual, a worked number example) and pick one on purpose. The first idea is rarely the best.

### 10. Verify before anything ships

- **Facts:** every factual claim traces to a primary source (paper, model card, official docs). Claims without a source are removed (prompt 02).
- **Coverage:** list the questions attendees will ask and check that the slides answer them (prompt 03).
- **Layout:** render every slide to an image and inspect it for overlaps, legibility and alignment.
- **Teaching quality is judged by a human.** In the reported explainer, automated reviewers caught layout bugs but missed a confusing Venn diagram; the human caught it. The fix was good once the human named the *problem* without prescribing the solution. We work the same way: Claude checks facts and layout; the presenter judges whether it teaches.

## Worked example: activation functions (outline, not yet fact-checked)

The earlier version failed because it was a catalogue: formula, graph and "used in model X", with no reason given for why any of it matters. Reordered by rule 2:

| # | Question the slide answers | Content | Interactive? |
|---|---|---|---|
| 1 | Why not just stack more layers? | Stacked linear layers compose into one linear function, so depth alone adds nothing. | Yes: attendees predict, then see ten stacked layers still fit only a line. |
| 2 | What breaks the collapse? | A nonlinear function between layers. | Yes: toggle the activation on and the fit bends to the data. |
| 3 | Does the choice of function matter? | Sigmoid saturates, so gradients vanish in deep networks. | Yes: slider for input size shows the gradient shrinking. |
| 4 | What fixed that, and at what cost? | ReLU keeps gradients alive but can leave neurons permanently inactive ("dead"). | Static graph is enough. |
| 5 | What do current LLMs use? | Smooth variants such as GELU and gated variants such as SwiGLU, inside each transformer layer's feed-forward block. | Static diagram of one transformer layer. |
| 6 | Which models use which? | Table: one row per model, each row cited to its paper or model card. | No. |

Softmax appears in attention and at the output, but it does a different job (turning scores into probabilities) and should not be taught as "another activation".

## Prompts

The `prompts/` folder holds the prompts that apply these rules. Start with `prompts/README.md`.

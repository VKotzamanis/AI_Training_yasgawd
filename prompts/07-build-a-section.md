# 07 · Build a section

**Use when:** starting the slides for a new section. This prompt applies every rule in `TEACHING_LOGIC.md` and calls prompts 01–06 at the right points.

Adapted from the logic of a one-shot prompt a user reported for an AI-built science explainer. That prompt named the audience, stated what viewers should understand ("the differences and relationships between those five terms"), and left the craft to the model. The model's workflow added candidate comparison, hard verification gates and visual self-checks; a human review caught the teaching error the automated checks missed. We keep that logic and add human review points.

```
Build the slides for one section of an AI training.

Section topic: [TOPIC]
Audience: [who they are and what they already know]
After this section, attendees should be able to: [1-3 outcomes, each something they can do or explain]
Comes after: [previous section, and the question it leaves open]
Leads into: [next section]
Time: [minutes]
Sources: [papers, model cards and docs to rely on]

Follow TEACHING_LOGIC.md. Work in this order; stop where marked.

1. Storyline. Write the chain of questions this section answers, one per slide, each raised by the one before. Use the default order: problem, idea, mechanism, trade-offs, where it is used. For each slide, say in one sentence why it comes at that point.
   STOP for my review.
2. Terms. List the terms attendees need before the mechanism makes sense. Draft each with prompt 06.
3. Hard concepts. For each, give 2-3 competing explanations: an analogy (prompt 01), a direct visual, and a worked numerical example. Recommend one and say why.
   STOP - I choose.
4. Claims. List every factual claim and check it with prompt 02. Remove or flag any claim without a source.
5. Interactivity. Name the slides where a static picture would hide how something changes. For each demo, specify: what the attendee changes, what they see change, and the prediction they make before the reveal.
6. Slides. One idea per slide; the title states the point; words paired with a visual; no decoration. Detail goes in the speaker notes, including what each simplification leaves out.
7. Checks. Render every slide to an image and inspect it for overlaps, legibility and alignment. Run prompt 03 on the result. Report what failed and what you fixed.
   STOP for my review of whether it teaches.

Never state anything false to simplify it.
```

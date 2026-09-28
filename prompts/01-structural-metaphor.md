# 01 · Structural metaphor

**Use when:** a concept is hard to grasp from its definition alone (activation functions, attention, embeddings, gradient descent).
**Teaching rule:** 7 (analogies that state where they break).

## Original

Source: [awesome-claude-prompts, "Generate high-fidelity structural metaphors using Claude"](https://github.com/langgptai/awesome-claude-prompts#generate-high-fidelity-structural-metaphors-using-claude)

```
Create a high-fidelity structural metaphor for [INSERT CONCEPT] that functions as an isomorphic mapping between domains.

Your metaphor should achieve cognitive transfer - allowing someone to reason about complex problems by working through analogous scenarios in a familiar domain.

### Required Components:

**1. Domain Selection**
- Choose a familiar domain that shares deep structural patterns with your target concept
- Ensure the familiar domain is meaningfully more accessible than the original
- Consider: physical systems, human relationships, natural processes, everyday activities

**2. Structural Mapping**
- Identify core relationships, constraints, and dynamics in both domains
- Create explicit mapping rules for translating between domains
- Preserve mathematical/logical relationships where applicable
- Map not just objects but processes, properties, and interactions

**3. Boundary Definition**
- Specify where the metaphor holds strongly
- Identify areas where it approximates rather than matches perfectly
- Explicitly state where the metaphor breaks down or misleads

**4. Problem-Solving Demonstration**
- Show how a specific challenge in the target domain can be reframed
- Work through the problem in the familiar domain
- Translate the solution back with preserved logical validity

### Quality Criteria:
- **Structural Isomorphism**: Relationships in both domains mirror each other
- **Cognitive Efficiency**: Reduces mental load while preserving accuracy
- **Practical Application**: Enables genuine problem-solving, not just illustration
- **Clear Boundaries**: Explicit about limitations and failure modes
```

The original ends with an example ("AI consciousness … piano resonance"). We dropped it: it is vague, cannot be checked, and fails the prompt's own quality criteria.

## Our version

```
Concept: [CONCEPT]
Audience: [who they are and what they already know]
Place in the talk: follows [question the previous slide raised]; leads into [next question]

Build a structural analogy for the concept.

1. Domain. Propose 3 familiar domains that share the concept's structure, not just its surface, with one sentence each on why it fits. Develop the strongest.
2. Mapping table. Columns: Concept element | Analogy element | Relationship preserved. Map processes and constraints, not only objects. If the concept has an equation, say which part of the analogy each term corresponds to.
3. Boundaries. Where the analogy holds exactly; where it only approximates; where it breaks down. Name at least one misconception the analogy could create and how the slides will prevent it.
4. Worked problem. Pose one question about the concept, answer it inside the analogy, then translate the answer back and check it against the real concept.
5. Visual. Describe one diagram showing the analogy and the concept side by side, with the same colour for each mapped pair.

Rules: every statement about the real concept must be technically correct at the audience's level. Reject any analogy that cannot be checked (e.g. "the model thinks like a brain").
```

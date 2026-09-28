# 06 · Plain-language term

**Use when:** a slide uses a term the audience may not know (token, embedding, logit, gradient, parameter, softmax).
**Teaching rules:** 3 (terms first), 4 (pair with a picture), 6 (simplify, never falsify).

## Original

Source: [awesome-claude-prompts, "Learn complex topics simply"](https://github.com/langgptai/awesome-claude-prompts#learn-complex-topics-simply)

```
Understand the concepts in [text], explain the topics individually, and also explain the whole concept in [text] at the end, like I am an 11-year-old.

Text = [Insert Here]
```

The original stops at the simple version, which invites statements that are false rather than merely incomplete. Our version keeps the simple explanation, then adds a picture, the precise version and a falsehood check.

## Our version

```
Term: [TERM]
Context: it appears on slide [N] of a training on [TOPIC] for [AUDIENCE].

1. Plain version: explain the term in at most three sentences, as to a curious 11-year-old. No jargon; define any technical word you cannot avoid.
2. Picture: describe one simple visual that shows the plain version.
3. What the plain version leaves out: list what is incomplete, then give the precise version in one or two sentences for the real audience.
4. Falsehood check: is anything in the plain version false, not just incomplete? If so, rewrite it until nothing is false, and show the change.
```

# 03 · Study-question check

**Use when:** a section is drafted, to test whether it answers what attendees will ask. Also produces end-of-section quiz questions.
**Teaching rule:** 10 (coverage check).

## Original

Source: [awesome-claude-prompts, "Summarize this PDF document (official example)"](https://github.com/langgptai/awesome-claude-prompts#summarize-this-pdf-document-official-example), from Anthropic's prompt library.

```
Summarize this PDF document in a bullet point outline. Make a markdown table of study questions and answers.
```

We keep only the study-question table. A bullet-point summary is the format we are moving away from.

## Our version

```
Attached: the slides and speaker notes for the section on [TOPIC].
Audience: [who they are and what they already know]
Intended outcomes: [the 1-3 outcomes for this section]

1. List the 10 questions an attendee is most likely to ask during or after this section, ordered from basic to advanced. Include at least two "why" questions and one "when would I not use this?" question.
2. Answer each using only the slides and notes. Table: # | Question | Answered? (Yes / Partly / No) | Slide | Answer from the slides
3. For every "Partly" or "No", say where in the slide sequence the missing content belongs and why there.
4. Check each intended outcome: can an attendee achieve it from these slides alone? Yes / No, with the reason.

Do not summarise the slides.
```

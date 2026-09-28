# 04 · Session plan and time budget

**Use when:** planning a whole session or a section, before any slides exist.
**Teaching rules:** 1 (outcomes first), 2 (chain of questions), 8 (interactivity where the nuance is).

## Original

Source: [awesome-claude-prompts, "Create guest lectures using AI"](https://github.com/langgptai/awesome-claude-prompts#create-guest-lectures-using-ai)

```
Listen carefully, I'm a marketing professor at the Stanford Graduate School of Business.

This Monday, I'm going to a marketing agency full of marketing and sales enthusiasts to give a guest lecture.

I have a time limit of one hour and these are the [topics] people want me to cover.

Your job is to help me to give this guest lecture, create an outline covering all the topics, and mention the time limit for each topic strictly one hour in total.

Finally if you can do anything else for my guest lecture I am happy to take your help.

Topics: [Insert here]
```

## Our version

The original only splits time. Ours also orders topics by the question each one answers and marks where demos belong.

```
I am giving a [N]-minute training session on [TOPIC].
Audience: [who they are and what they already know]
After the session, attendees should be able to: [1-3 outcomes]
Topics: [list]

1. Order the topics so each one answers a question raised by the one before. Write that question for each topic.
2. Give each topic a time budget. The total must be exactly [N] minutes, including [X] minutes of questions.
3. Mark which topics need an interactive demo, and say what a static slide would hide.
4. Flag any topic that does not serve the outcomes; recommend cutting it or moving it to an appendix.

Output a table: # | Topic | Question it answers | Minutes | Demo? | What a static slide would hide
```

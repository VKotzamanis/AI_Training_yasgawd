# 02 · Cite your sources (fact check)

**Use when:** a slide makes a factual claim, such as "Model X uses activation Y" or "method Z reduced error by N %".
**Teaching rule:** 10 (verify before anything ships).

## Original

Source: [awesome-claude-prompts, "Cite your sources"](https://github.com/langgptai/awesome-claude-prompts#cite-your-sources), based on an example from Anthropic's prompt library.

```
You are an expert research assistant. Here is a document you will answer questions about:
[Full text of Matterport SEC filing 10-K 2023, not pasted here for brevity]

First, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.

If there are no relevant quotes, write "No relevant quotes" instead.

Then, answer the question, starting with "Answer:". Do not include or reference quoted content verbatim in the answer. Don't say "According to Quote [1]" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.

Thus, the format of your overall response should look like what's shown between the tags. Make sure to follow the formatting and spacing exactly.
Quotes:
[1] "Company X reported revenue of $12 million in 2021."
[2] "Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%."

Answer:
Company X earned $12 million. [1] Almost 90% of it was from widget sales. [2]

If the question cannot be answered by the document, say so.
```

## Our version

The original answers one question from one document. We check a list of slide claims against several sources.

```
<sources>
[paste papers, model cards or official docs; label each: S1, S2, ...]
</sources>

<claims>
[one claim per line, exactly as it will appear on the slide]
</claims>

For each claim:
1. Find the shortest quotes from the sources that support or contradict it. Number them and tag each with its source label.
2. Give a verdict: Supported / Partly supported / Contradicted / Not in sources.
3. If the verdict is not "Supported", rewrite the claim so the sources support it exactly, or recommend removing it.

Output:
- A table: # | Claim | Verdict | Quotes | Corrected claim
- The numbered quotes

Use only the sources. If a claim is not in them, say "Not in sources"; do not fill the gap from memory.
```

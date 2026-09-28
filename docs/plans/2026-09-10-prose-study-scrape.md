# Prose Study — Scrape, Summarize, Extract Style Rules

> **For agentic workers:** dispatch through the `codex-subagent` skill, one Codex at a time.
> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Read every article on one author's site, produce a one-paragraph index of what
each article covers and where it fits our training, and distil the prose and flow rules
that make his explanations work — so the deck's writing improves by study, not by copying.

**Architecture:** Codex CLI does the network I/O and bulk reading in its own context;
Claude plans, gates, and verifies. Four artifacts, each verified before the next task
starts: a machine-readable article index, the raw corpus on disk, a human-readable
summary index, and a testable style ruleset. A mechanical anti-copy gate runs over the
summaries before anything reaches the deck.

**Tech stack:** `codex exec` (shell network via bypass sandbox), `curl`, `pandoc` or
`readability`, `jq`, Python 3 for the shingle check. Fallback: `agy -p`, then WebFetch.

---

## BLOCKING INPUT — the one thing missing

**The site URL was not in the request.** Everything below is parameterized on `$SITE`.
Task 1 cannot start without it. Nothing else in this plan is blocked.

The quoted line — *"❯ The Plan tab already treats weeks as untrustworthy. And nothing
recalculates it when you miss a session — Boot would say 'week 12 of 12' after six
sessions."* — reads as a product devlog, not a standard LLM-explainer site, so I am not
guessing the domain. A wrong guess costs a full crawl and pollutes `REFERENCES.md`.

---

## Global Constraints

- **Study, don't copy.** No sentence of his prose enters the deck or the supplement.
  Summaries are written from scratch. Enforced mechanically in Task 3, not by intention.
- **Credit.** Every fetched URL gets a line in the project `REFERENCES.md`
  (`- <URL> — <YYYY-MM-DD HH:MM> — <method> — session <id> — <why>`), and the deck carries
  an attribution line naming the author and site.
- **Politeness.** Honour `robots.txt`. One request per second. No concurrent fetches.
- **One Codex at a time.** Machine has 16 GB; the concurrency cap is two subagents and one
  is preferred.
- **Codex writes to disk as it goes.** Every task's output file is appended per article,
  not held in memory and written at the end. A killed agent must leave usable partial work.
- **agy is a paraphrase.** If the fallback fires, mark those rows `agy` in `REFERENCES.md`
  and never quote them as primary text. Find the artifact in
  `~/.gemini/antigravity-cli/scratch/`, copy it into `agy-artifacts/`, and verify it landed.
- **Output root:** `REVIEWD/PROSE-STUDY/`.

---

## Fallback ladder — try in this order, stop at the first that works

| # | Method | Dispatch | When it fires |
|---|---|---|---|
| 1 | Codex + shell network | `codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox` | Default. `curl` needs real network; the workspace sandbox has none. |
| 2 | Codex + live web search | `--sandbox workspace-write --config web_search="live"` | `curl` returns 403 / Cloudflare challenge. Different egress path. |
| 3 | `agy -p` | Gemini, per CLAUDE.md | Both Codex paths blocked. Paraphrase only. |
| 4 | WebFetch, article by article | This session | Last resort. Highest token cost; use only for a handful of key articles. |

A 404 means the page does not exist. Do not walk the ladder for a 404 — fix the URL.

---

## Task 1: Discover the article index

**Files:**
- Create: `REVIEWD/PROSE-STUDY/00-index.json`
- Create: `REVIEWD/PROSE-STUDY/00-robots.txt`

**Produces:** a JSON array `[{url, title, date, slug}]` that Tasks 2–5 iterate over.

- [ ] **Step 1: Read robots.txt**

```bash
curl -sSL --max-time 20 "$SITE/robots.txt" | tee REVIEWD/PROSE-STUDY/00-robots.txt
```

Record every `Disallow` and any `Crawl-delay`. If a path in the ladder below is
disallowed, drop it and say so in the report.

- [ ] **Step 2: Try the machine-readable indexes, in order**

```bash
for p in /sitemap.xml /sitemap_index.xml /feed.xml /rss.xml /atom.xml /index.xml \
         /feed /blog/feed /posts/index.xml; do
  code=$(curl -sSL -o /tmp/probe -w '%{http_code}' --max-time 20 "$SITE$p")
  echo "$code  $p  $(wc -c </tmp/probe) bytes"
done
```

RSS or a sitemap is the win condition: title, URL and date in one fetch, already
structured. Only fall back to scraping an archive page (`/`, `/blog`, `/archive`,
`/writing`, `/posts`) if every probe above 404s.

- [ ] **Step 3: Emit the index**

Parse whichever source responded into `00-index.json`. Slug = last non-empty path segment.

- [ ] **Step 4: CHECK — the index is complete and well-formed**

```bash
jq 'length' REVIEWD/PROSE-STUDY/00-index.json
jq '[.[] | select(.url == null or .url == "" or .title == null or .title == "")] | length' \
   REVIEWD/PROSE-STUDY/00-index.json
jq -r '.[].url' REVIEWD/PROSE-STUDY/00-index.json | sort | uniq -d
```

Expected: count ≥ 1; second command prints `0`; third prints nothing (no duplicate URLs).

**Then stop and report the count before Task 2 runs.** A feed that returns 10 items on a
site with 80 articles means the feed is truncated — a common default — and the archive page
is the real index. Catching that here costs one message; catching it in Task 4 costs the
whole corpus.

---

## Task 2: Fetch the article bodies

**Files:**
- Create: `REVIEWD/PROSE-STUDY/raw/<slug>.md`, one per article
- Create: `REVIEWD/PROSE-STUDY/02-fetch-log.tsv` — `slug<TAB>url<TAB>http_code<TAB>bytes`

**Consumes:** `00-index.json` from Task 1.

- [ ] **Step 1: Fetch and convert, one per second, logging as you go**

```bash
mkdir -p REVIEWD/PROSE-STUDY/raw
jq -r '.[] | [.slug, .url] | @tsv' REVIEWD/PROSE-STUDY/00-index.json |
while IFS=$'\t' read -r slug url; do
  code=$(curl -sSL -o /tmp/page.html -w '%{http_code}' --max-time 30 \
         -A 'AI-Training-study/1.0 (personal curriculum research)' "$url")
  pandoc -f html -t markdown --wrap=none /tmp/page.html \
    -o "REVIEWD/PROSE-STUDY/raw/${slug}.md" 2>/dev/null
  printf '%s\t%s\t%s\t%s\n' "$slug" "$url" "$code" \
    "$(wc -c < "REVIEWD/PROSE-STUDY/raw/${slug}.md")" \
    >> REVIEWD/PROSE-STUDY/02-fetch-log.tsv
  sleep 1
done
```

If the feed already carried full article content, skip the refetch and write the feed
bodies straight to `raw/` — one request instead of eighty.

- [ ] **Step 2: CHECK — every article arrived, and arrived intact**

```bash
jq 'length' REVIEWD/PROSE-STUDY/00-index.json
ls REVIEWD/PROSE-STUDY/raw/*.md | wc -l
awk -F'\t' '$3 != 200 {print "NON-200: " $0}' REVIEWD/PROSE-STUDY/02-fetch-log.tsv
awk -F'\t' '$4 < 500  {print "SUSPICIOUSLY SMALL: " $0}' REVIEWD/PROSE-STUDY/02-fetch-log.tsv
```

Expected: the first two counts match; no NON-200 lines. A file under 500 bytes usually
means the extractor grabbed the nav bar instead of the article — open one by hand and
confirm before accepting it as a genuinely short post.

---

## Task 3: One paragraph per article

**Files:**
- Create: `REVIEWD/PROSE-STUDY/ARTICLE-INDEX.md`
- Read: `ai-training/curriculum/architecture.md` — the 19-chapter map, so "where it fits"
  names a real chapter instead of a guess.

**Consumes:** `raw/*.md`, `00-index.json`, the curriculum map.

- [ ] **Step 1: Write one block per article, appending as you go**

Format, fixed:

```markdown
### <title>
`<url>` · <date>

<2–3 sentences: what the article is about, then where it fits our training — name the
chapter, and the slide if it is that specific. Say "no fit" when there is none; a forced
placement is worse than a gap.>

**Technique worth stealing:** <one clause, or `none`>
```

- [ ] **Step 2: CHECK — coverage**

```bash
jq -r '.[].url' REVIEWD/PROSE-STUDY/00-index.json | while read -r u; do
  grep -qF "$u" REVIEWD/PROSE-STUDY/ARTICLE-INDEX.md || echo "MISSING: $u"
done
```

Expected: no output.

- [ ] **Step 3: CHECK — the anti-copy gate**

This is the check that makes "study, don't copy" enforceable. No 8-word run in any summary
may appear verbatim in the article it summarizes.

```python
# scripts/shingle_check.py — run from the project root
import json, pathlib, re, sys

def shingles(text, n=8):
    w = re.findall(r"[a-z0-9']+", text.lower())
    return {" ".join(w[i:i+n]) for i in range(len(w) - n + 1)}

root = pathlib.Path("REVIEWD/PROSE-STUDY")
index = json.loads((root / "00-index.json").read_text())
blocks = (root / "ARTICLE-INDEX.md").read_text().split("### ")
hits = 0
for entry in index:
    block = next((b for b in blocks if entry["url"] in b), None)
    raw = root / "raw" / f"{entry['slug']}.md"
    if block is None or not raw.exists():
        continue
    overlap = shingles(block) & shingles(raw.read_text())
    for s in sorted(overlap):
        print(f"COPIED [{entry['slug']}]: {s}")
        hits += 1
print(f"\n{hits} copied shingles")
sys.exit(1 if hits else 0)
```

Run: `python3 scripts/shingle_check.py`
Expected: `0 copied shingles`, exit 0. Any hit gets rewritten, not waived.

---

## Task 4: Extract the style rules — the actual point

**Files:**
- Create: `REVIEWD/PROSE-STUDY/STYLE-RULES.md`

**Consumes:** the whole corpus in `raw/`, plus `REVIEWD/CH1_SUPPLEMENT.md` as the
counter-example source.

The index is a by-product. This is the deliverable that changes how the deck reads.

- [ ] **Step 1: Write 10–20 named rules**

Each rule takes exactly this shape:

```markdown
## R<n>. <imperative name>

**Rule:** <one sentence, imperative.>
**Test:** <how to hold a paragraph against it and answer pass or fail.>
**His move, paraphrased:** <describe the technique; do not quote.>
**Our counter-example:** <a real sentence from CH1_SUPPLEMENT.md that fails the test,
quoted, with the rewrite.>
```

Seed rule, already extractable from the line the user quoted:

> **R1. State the present behaviour as fact, then name the failure it produces, then give
> the number that makes the failure undeniable.** His pattern runs claim → concrete failing
> instance → the specific count ("week 12 of 12 after six sessions"). No hedge, no
> metaphor, no "can lead to issues". Test: does the paragraph contain a number or a named
> concrete case? If not, it is an opinion.

- [ ] **Step 2: CHECK — every rule is falsifiable**

Read the **Test:** line of each rule alone, with the rule name covered. If you cannot
answer pass/fail on a sample paragraph using that line by itself, the rule is a mood.
Delete it. Report the count deleted — a ruleset of 8 testable rules beats 20 vague ones.

- [ ] **Step 3: CHECK — the rules discriminate**

Score five paragraphs from `CH1_SUPPLEMENT.md` and five from his corpus against the
ruleset. His should score higher. If they score the same, the ruleset has not captured
what makes his writing work, and Task 4 is not done.

---

## Task 5: Catalogue the interactive patterns

**Files:**
- Create: `REVIEWD/PROSE-STUDY/VIZ-PATTERNS.md`

Only if the site carries interactive explainers. Record the *interaction*, not the code:

| what the reader changes | what updates | what the change teaches | our slide |
|---|---|---|---|

- [ ] **CHECK:** every row's third column names something a participant could *state out
  loud after using it*. A widget that only looks good has an empty third column — record it
  as `decorative` and move on.

---

## Task 6: References and credit

- [ ] **Step 1:** Append one line per fetched URL to the project `REFERENCES.md`, in the
      required format, method `codex-curl` / `codex-websearch` / `agy` / `WebFetch`.
- [ ] **Step 2:** Add the attribution line to the deck's credits slide: author, site, and
      "explanatory approach studied, not reproduced".
- [ ] **CHECK:** `grep -c "$SITE" REFERENCES.md` equals `jq 'length' 00-index.json`.

---

## Self-review against the request

| asked for | task |
|---|---|
| Codex subagent scrapes the site | 1, 2 (ladder step 1) |
| agy if blocked | fallback ladder, step 3 |
| one paragraph per article, 2–3 sentences | 3 |
| where it would fit in our training | 3, against `architecture.md` |
| fix our flow and prose by studying his | 4 — the reason the rest exists |
| visualizations we can adapt | 5 |
| give credit | 6 |

**Not covered, deliberately:** rebuilding any of his visualizations from his source. Task 5
records interaction patterns only; anything we ship is written from scratch.

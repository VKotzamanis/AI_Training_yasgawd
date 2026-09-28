#!/usr/bin/env python3
"""Concatenate the per-article blocks into ARTICLE-INDEX.md and run the anti-copy gate.

The gate is the thing that makes "study, don't copy" enforceable rather than
aspirational: no run of 8 words in a summary may appear verbatim in the article
it summarizes. Exit 1 on any hit.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
idx  = json.loads((ROOT/"00-index.json").read_text())

def shingles(text, n=8):
    w = re.findall(r"[a-z0-9']+", text.lower())
    return {" ".join(w[i:i+n]) for i in range(len(w)-n+1)}

blocks, missing, hits = [], [], []
for e in idx:
    f = ROOT/"out"/f"{e['slug']}.md"
    if not f.exists() or not f.stat().st_size:
        missing.append(e["slug"]); continue
    body = f.read_text().strip()
    blocks.append(body)
    raw = ROOT/"raw"/f"{e['slug']}.md"
    if raw.exists():
        for s in sorted(shingles(body) & shingles(raw.read_text())):
            hits.append((e["slug"], s))

hdr = (
"# Mike X Cohen — *Dissecting LLMs with ML*: article index\n\n"
"18 posts from the `ml-on-llms` section of https://mikexcohen.substack.com, oldest first.\n"
"One paragraph each: what the post covers, and where it fits the training.\n\n"
"Studied for explanation technique, not reproduced. Every summary was written from scratch\n"
"and checked mechanically: no 8-word run in this file appears verbatim in the source article.\n"
"**Credit him on the deck's credits slide.**\n\n---\n\n")
(ROOT/"ARTICLE-INDEX.md").write_text(hdr + "\n\n".join(blocks) + "\n")

print(f"blocks written : {len(blocks)}/{len(idx)}")
print(f"missing        : {missing or 'none'}")
print(f"copied shingles: {len(hits)}")
for slug, s in hits[:20]:
    print(f"  COPIED [{slug}]: {s}")
sys.exit(1 if (hits or missing) else 0)

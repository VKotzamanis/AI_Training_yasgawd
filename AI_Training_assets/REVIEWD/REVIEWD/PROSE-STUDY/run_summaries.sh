#!/usr/bin/env bash
# One Codex call per article, resumable. Each call writes ONE small file via
# codex's own -o flag and then exits, so a kill loses at most the article in
# flight. The previous single-dispatch run was told to append as it went,
# buffered anyway, and left zero output when stopped.
set -uo pipefail
cd "$(dirname "$0")"
TOTAL=$(python3 -c "import json;print(len(json.load(open('00-index.json'))))")

read -r -d '' MAP <<'EOF'
Curriculum (19 chapters, PhD civil/environmental engineers, MATLAB users, marine wave energy):
I  1 Substrate (what the system computes) | 2 Formation | 3 Control | 4 Measurement
II 5 Intrinsic failure | 6 Extrinsic failure | 7 Physical limits | 8 Brain and model (appendix)
III 9 The agent | 10 Memory | 11 Orchestration | 12 Extension | 13 Access
IV 14 Literature | 15 Production | 16 Code and numerics | 17 Critique | 18 Governance | 19 Judgement
Chapter 1's NETWORK & OUTPUT section, in pipeline order:
  slide 8-9 tokenization | 14 the neuron | 15 embedding & hidden state
  | 17 transformer decoder (attention + MLP) | 18 logits, softmax, temperature
  | 19 sampling and variance | 20 the assembled loop
EOF

for i in $(seq 0 $((TOTAL-1))); do
  eval "$(python3 - "$i" <<'PY'
import json,sys,shlex
d=json.load(open('00-index.json'))[int(sys.argv[1])]
for k in ("slug","title","url","date"):
    print(f'{k.upper()}={shlex.quote(str(d[k]))}')
PY
)"
  OUT="out/${SLUG}.md"
  if [ -s "$OUT" ]; then echo "[$((i+1))/$TOTAL] skip  $SLUG"; continue; fi
  echo "[$((i+1))/$TOTAL] write $SLUG"
  codex exec --skip-git-repo-check --sandbox workspace-write \
    -m gpt-5.6-terra --config model_reasoning_effort="low" \
    -o "$OUT" \
    "Read the article at raw/${SLUG}.md (relative to your cwd). It is one post from Mike X
Cohen's Substack series 'Dissecting LLMs with ML', converted from HTML, so ignore the
navigation and subscription boilerplate.

${MAP}

Output EXACTLY this block and nothing else - no preamble, no commentary:

### ${TITLE}
\`${URL}\` · ${DATE:0:10}

<2-3 sentences. First one or two: what the article actually covers. Last sentence: where it
fits the curriculum above - name the chapter number, and the slide number when the fit is
that tight. Write \"No fit.\" plainly when there is none; a forced placement is worse than a gap.>

**Technique worth stealing:** <one clause naming a reusable EXPLANATION move - a demo shape,
an ordering choice, an objection he names head-on. Or: none>

Rules: write every sentence from scratch, never reuse his phrasing, do not quote the article.
An 8-word-shingle check runs against raw/${SLUG}.md afterwards and any overlap is rejected." \
    >/dev/null 2>&1
  if [ -s "$OUT" ]; then echo "    ok  ($(wc -c <"$OUT") B)"; else echo "    FAILED"; fi
done
echo "done: $(ls out/*.md 2>/dev/null | wc -l)/$TOTAL"

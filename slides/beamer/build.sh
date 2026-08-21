#!/usr/bin/env bash
# Build a Beamer deck, run every gate, and report. Run from slides/beamer/.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
export TEXINPUTS="$ROOT:$HOME/texmf/tex/latex/uhtraining:"
deck="${1:-01-substrate}"

echo "=== regenerating the source table from references.md ==="
node "$ROOT/../scripts/gen-sources-tex.mjs" || exit 1

echo "=== frame check: every frame carries a footer, every key is [V] ==="
python3 "$ROOT/check-frames.py" "$ROOT/$deck.tex" || exit 1

cd "$ROOT"
echo "=== building $deck.tex (two passes, for the frame count) ==="
for pass in 1 2; do
  xelatex -interaction=nonstopmode "$deck.tex" >/tmp/uh-$deck.log 2>&1
done
errs=$(grep -cE '^!' /tmp/uh-$deck.log)
over=$(grep -c 'Overfull \\vbox' /tmp/uh-$deck.log)
echo "  LaTeX errors:   $errs"
echo "  Overfull vbox:  $over   (a frame whose content runs into the footline)"
[ "$errs" -gt 0 ] && { grep -nE '^!' -A2 /tmp/uh-$deck.log | head -20; exit 1; }
[ "$over" -gt 0 ] && { grep -oE 'Overfull \\vbox \([0-9.]+pt too high\) detected at line [0-9]+' /tmp/uh-$deck.log; exit 1; }
pdfinfo "$deck.pdf" | grep -E '^Pages|^Page size'
echo "build ok"

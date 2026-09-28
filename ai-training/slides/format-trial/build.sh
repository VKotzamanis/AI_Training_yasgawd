#!/usr/bin/env bash
# Format trial: one pair of representative slides, five ways.
# Run from slides/format-trial/.  Outputs land in out/.
set -euo pipefail
FIG=../../assets/figures
mkdir -p out

# LaTeX resolves \includegraphics relative to the engine's working directory, which is a
# temp dir, so --resource-path does not reach it. Generate an absolute \graphicspath.
ABSFIG="$(cd "$FIG" && pwd)/"
printf '\\graphicspath{{%s}}\n' "$ABSFIG" > out/graphicspath.tex

common=(--from markdown --slide-level=2 --resource-path="$FIG" -V aspectratio:169 -H out/graphicspath.tex)

echo "V1  metropolis"
pandoc "${common[@]}" -t beamer -V theme:metropolis \
  -H head-v1-metropolis.tex --pdf-engine=xelatex \
  -o out/v1-metropolis.pdf sample.md

echo "V2  house, light"
pandoc "${common[@]}" -t beamer -H head-v2-house.tex --pdf-engine=xelatex \
  -o out/v2-house-light.pdf sample.md

echo "V3  house, dark"
pandoc "${common[@]}" -t beamer -H head-v3-dark.tex --pdf-engine=xelatex \
  -o out/v3-house-dark.pdf sample.md

echo "V4  serif, printed-paper"
pandoc "${common[@]}" -t beamer -H head-v4-serif.tex --pdf-engine=xelatex \
  -o out/v4-serif.pdf sample.md

echo "V5  pptx, editable text"
# Raw LaTeX is dropped on the pptx path, so this variant uses its own source.
pandoc --from markdown --slide-level=2 --resource-path="$FIG" \
  -t pptx -o out/v5-editable.pptx sample-office.md

echo "V6  pptx, page images"
python3 pdf2pptx.py out/v2-house-light.pdf out/v6-house-light-images.pptx 200

echo
echo "built:"; ls -la out/

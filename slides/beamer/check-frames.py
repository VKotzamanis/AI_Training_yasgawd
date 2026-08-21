#!/usr/bin/env python3
"""Frame check for the Beamer decks — the LaTeX counterpart of check:cites.

Two rules, both ruled on and both mechanical:

  1. Every frame carries a footer: a \\citesource or a \\provenance.
  2. Every key in a \\citesource resolves, and is tagged [V]. Only [V] may appear on a slide.

Usage: python3 check-frames.py <deck.tex> [<deck.tex> ...]
Exits non-zero if any rule is broken, so the build can gate on it.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "uh-sources.tex"

FRAME = re.compile(
    r"\\begin\{(frame|consoleframe)\}(.*?)\\end\{\1\}", re.S)
KEYS = re.compile(r"\\citesource\{([^}]*)\}")
PROV = re.compile(r"\\provenance(?:\[[^\]]*\])?\{([^}]*)\}")
TITLE = re.compile(r"\\frametitle\{(.*?)\}|\\begin\{(?:frame|consoleframe)\}(?:\[[^\]]*\])?\{(.*?)\}", re.S)
VALID_PROV = {"definition", "derived", "computed", "observation", "schematic", "none"}


def load_sources():
    if not SRC.exists():
        sys.exit(f"check-frames: {SRC} missing — run scripts/gen-sources-tex.mjs first")
    out = {}
    for m in re.finditer(r"\\uhdefsource\{([^}]*)\}\{([^}]*)\}", SRC.read_text()):
        out[m.group(1)] = m.group(2)
    return out


def main(decks):
    sources = load_sources()
    problems = 0
    for deck in decks:
        text = Path(deck).read_text()
        frames = FRAME.findall(text)
        if not frames:
            print(f"  {deck}: no frames found — is this a deck?")
            problems += 1
            continue
        for i, (_env, body) in enumerate(frames, start=1):
            t = TITLE.search(body)
            label = (t.group(1) or t.group(2) or "").strip()[:56] if t else "(untitled)"
            label = " ".join(label.split())
            has_src = KEYS.search(body)
            has_prov = PROV.search(body)
            if not (has_src or has_prov):
                print(f"  {deck}: frame {i} carries no footer — {label}")
                problems += 1
            for m in KEYS.finditer(body):
                for key in (k.strip() for k in m.group(1).split(",") if k.strip()):
                    tag = sources.get(key)
                    if tag is None:
                        print(f'  {deck}: frame {i} cites unknown key "{key}"')
                        problems += 1
                    elif tag != "V":
                        print(f'  {deck}: frame {i} cites "{key}" tagged [{tag}] — only [V] may reach a slide')
                        problems += 1
            for m in PROV.finditer(body):
                word = m.group(1).strip()
                if word not in VALID_PROV:
                    print(f'  {deck}: frame {i} uses unknown provenance "{word}"')
                    problems += 1
        print(f"check-frames — {deck}: {len(frames)} frame(s) checked")
    if problems:
        print(f"check-frames FAILED — {problems} problem(s)")
        sys.exit(1)
    print("check-frames PASSED")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])

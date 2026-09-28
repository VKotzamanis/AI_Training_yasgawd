#!/usr/bin/env python3
"""Version-stamp an exported Beamer deck so PDF comments can be resolved back to source.

The stamp is a hash of the .tex source plus the frame count, written into the PDF's
/Info/Keywords. It travels with the file rather than living in a sidecar that can go
missing, so a stale PDF is detectable instead of silently mis-mapped onto lines that
have since moved.

This is the Beamer counterpart of scripts/pdf-review/stamp-all.mjs, which does the same
job for the Slidev decks. Same mechanism - mutool writes the metadata - so an annotated
PDF from either path can be checked the same way.

Usage:  python3 stamp.py 02-formation
        python3 stamp.py 02-formation --verify
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
FRAME = re.compile(r"\\begin\{(frame|consoleframe)\}")


def stamp_for(deck: str) -> str:
    tex = HERE / f"{deck}.tex"
    src = tex.read_bytes()
    frames = len(FRAME.findall(src.decode("utf-8")))
    h = hashlib.sha256(src).hexdigest()[:16]
    return f"beamer-review v1 | {deck}.tex | frames={frames} | sha256={h}"


def read_stamp(pdf: Path) -> str:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Keywords:"):
            return line.split(":", 1)[1].strip()
    return ""


def main(deck: str, verify: bool) -> None:
    pdf = HERE / f"{deck}.pdf"
    if not pdf.exists():
        sys.exit(f"stamp: {pdf} does not exist - build it first")
    want = stamp_for(deck)

    if verify:
        got = read_stamp(pdf)
        if got == want:
            print(f"stamp: {pdf.name} is current\n  {got}")
            return
        print(f"stamp: {pdf.name} is STALE")
        print(f"  in the pdf: {got or '(none)'}")
        print(f"  source now: {want}")
        sys.exit(1)

    js = HERE / "_stamp.js"
    js.write_text(
        'var doc = Document.openDocument(scriptArgs[0])\n'
        'doc.setMetaData("info:Keywords", scriptArgs[1])\n'
        'doc.save(scriptArgs[0], "incremental")\n'
    )
    try:
        subprocess.run(["mutool", "run", str(js), str(pdf), want], check=True,
                       capture_output=True)
    finally:
        js.unlink(missing_ok=True)

    # grep it back: a script that completes is not a script that wrote
    got = read_stamp(pdf)
    if got != want:
        sys.exit(f"stamp: did NOT persist\n  wanted: {want}\n  got:    {got}")
    print(f"stamp: {pdf.name}\n  {want}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], "--verify" in sys.argv)

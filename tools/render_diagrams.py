#!/usr/bin/env python3
"""Render every Mermaid block under docs/ with mermaid-cli (mmdc) to prove it parses.

    npm install --global @mermaid-js/mermaid-cli
    python tools/render_diagrams.py

Exits 1 if any diagram fails, 2 if mmdc is not installed. Output SVGs go to a temp directory and
are discarded; the site renders diagrams in the browser.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from booklib import DOCS, code_blocks, rel


def main() -> int:
    mmdc = shutil.which("mmdc")
    if not mmdc:
        print("mmdc not found; install @mermaid-js/mermaid-cli to render diagrams")
        return 2
    failures = 0
    total = 0
    with tempfile.TemporaryDirectory() as tmp:
        cfg = Path(tmp) / "puppeteer.json"
        cfg.write_text('{"args": ["--no-sandbox"]}', encoding="utf-8")
        for md in sorted(DOCS.rglob("*.md")):
            for lang, body, start in code_blocks(md.read_text(encoding="utf-8")):
                if lang != "mermaid":
                    continue
                total += 1
                src = Path(tmp) / f"d{total}.mmd"
                src.write_text(body, encoding="utf-8")
                proc = subprocess.run(
                    [mmdc, "-q", "-p", str(cfg), "-i", str(src), "-o", str(src.with_suffix(".svg"))],
                    capture_output=True, text=True,
                )
                if proc.returncode != 0:
                    failures += 1
                    print(f"FAIL {rel(md)}:{start}\n{(proc.stderr or proc.stdout).strip()[:600]}")
    print(f"[diagrams] {total - failures} of {total} rendered")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

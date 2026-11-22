#!/usr/bin/env python3
"""Run every automated check on the book.

    python tools/validate_book.py            # structure, links, references, exercises, generated files
    python tools/validate_book.py --build    # also run `mkdocs build --strict`

Chapter-level checks performed here (published chapters only):
- the sixteen contract sections exist, as H2 headings, in the contract order, and none is a stub
- the chapter is long enough to be a chapter (MIN_CHAPTER_WORDS) and has at least MIN_DIAGRAMS diagrams
- the H1 matches curriculum.yaml
- no placeholder text anywhere under docs/ or in the root documents
- fenced yaml and json blocks parse; fenced mermaid blocks pass a syntax lint
- generated files (curriculum page, bibliography page, exercise index, single-file edition) are current

Passing this script means the book is structurally sound. It does not mean the claims are true:
see research/human-review-checklist.md and research/quality-report.md.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys

import yaml

import build_curriculum
import build_single_file
import check_exercises
import check_navigation
import check_references
from booklib import (
    DOCS,
    REQUIRED_SECTIONS,
    REVIEW_BANNER,
    ROOT,
    Report,
    code_blocks,
    headings,
    iter_chapters,
    rel,
    section,
    strip_code,
    word_count,
)

MIN_CHAPTER_WORDS = 2500
MIN_SECTION_WORDS = 60
MIN_DIAGRAMS = 2
PLACEHOLDER_RE = re.compile(
    r"\b(TODO|TBD|FIXME|XXX|lorem ipsum|coming soon|to be written|placeholder|\[citation needed\])\b",
    re.I,
)
# Words that are legitimate inside prose about placeholders; lines containing these are skipped.
PLACEHOLDER_ALLOW = re.compile(r"placeholder (text|chapter|check)|no placeholder|not .{0,20}placeholder|"
                               r"empty placeholders|PLACEHOLDER_", re.I)
MERMAID_TYPES = (
    "flowchart", "graph", "sequenceDiagram", "stateDiagram-v2", "stateDiagram", "gantt",
    "quadrantChart", "timeline", "pie", "xychart-beta", "classDiagram", "erDiagram", "mindmap",
)
ROOT_DOCS = ["README.md", "CONTRIBUTING.md"]


# Maintainer bookkeeping that must not appear in reader text (CLAUDE.md section 7).
BOOKKEEPING_RE = re.compile(
    r"\bcanon(ical)?\b|\b(disputed claim|research gap|gap) [DG]\d+\b|"
    r"\b(idea level|idea-level|abstract only|metadata only|metadata-only|full text (was not|could not)|"
    r"not read for this book)\b",
    re.I,
)
BOOKKEEPING_DIRS = ("parts", "solutions", "templates", "projects")
BOOKKEEPING_IS_ERROR = False  # switch to True once the readability cleanup is complete


def lint_mermaid(body: str) -> list[str]:
    problems: list[str] = []
    lines = [ln for ln in body.splitlines() if ln.strip() and not ln.strip().startswith("%%")]
    if not lines:
        return ["empty diagram"]
    first = lines[0].strip()
    if not first.startswith(MERMAID_TYPES):
        problems.append(f"unknown diagram type: '{first.split()[0]}'")
    for opener, closer in ("[]", "()", "{}"):
        if body.count(opener) != body.count(closer):
            problems.append(f"unbalanced {opener}{closer}")
    if body.count('"') % 2:
        problems.append("odd number of double quotes")
    if first.startswith(("flowchart", "graph")):
        opened = len(re.findall(r"^\s*subgraph\b", body, re.M))
        closed = len(re.findall(r"^\s*end\s*$", body, re.M))
        if opened != closed:
            problems.append(f"{opened} subgraph(s) but {closed} end(s)")
        for ln in lines[1:]:
            # an unquoted label containing parentheses or a semicolon breaks the Mermaid parser
            for label in re.findall(r"\[([^\]\"]*)\]", ln):
                if re.search(r"[();]", label):
                    problems.append(f"unquoted label with special characters: [{label}]")
    return problems


def check_chapters(rep: Report) -> None:
    for ch in iter_chapters("live"):
        if not ch.path.is_file():
            rep.error(f"{ch.id}: file missing at {rel(ch.path)}")
            continue
        text = ch.path.read_text(encoding="utf-8")
        h1 = [t for lvl, t, _ in headings(text) if lvl == 1]
        expected_h1 = f"Chapter {ch.n} — {ch.title}"
        if h1 != [expected_h1]:
            rep.error(f"{ch.id}: H1 is {h1}, expected ['{expected_h1}']")
        h2 = [t for lvl, t, _ in headings(text) if lvl == 2]
        if h2 != REQUIRED_SECTIONS:
            missing = [s for s in REQUIRED_SECTIONS if s not in h2]
            extra = [s for s in h2 if s not in REQUIRED_SECTIONS]
            if missing:
                rep.error(f"{ch.id}: missing sections: {missing}")
            if extra:
                rep.error(f"{ch.id}: sections outside the contract: {extra}")
            if not missing and not extra:
                rep.error(f"{ch.id}: contract sections are out of order")
        for name in REQUIRED_SECTIONS:
            body = section(text, name)
            if body is not None and word_count(body) < MIN_SECTION_WORDS:
                rep.error(f"{ch.id}: section '{name}' is a stub ({word_count(body)} words)")
        words = word_count(text)
        if words < MIN_CHAPTER_WORDS:
            rep.error(f"{ch.id}: {words} words, minimum is {MIN_CHAPTER_WORDS}")
        diagrams = [b for b in code_blocks(text) if b[0] == "mermaid"]
        if len(diagrams) < MIN_DIAGRAMS:
            rep.error(f"{ch.id}: {len(diagrams)} diagram(s), minimum is {MIN_DIAGRAMS}")
        objectives = section(text, "Learning Objectives") or ""
        if len(re.findall(r"^\s*[-*]\s+", objectives, re.M)) < 3:
            rep.error(f"{ch.id}: Learning Objectives needs at least three bullet items")
        if REVIEW_BANNER in text:
            rep.error(f"{ch.id}: per-page review banners are retired; the site announcement says so")
        rep.note(f"{ch.id}: {words} words, {len(diagrams)} diagrams, {len(h2)} sections")


def check_text_hygiene(rep: Report) -> None:
    files = sorted(DOCS.rglob("*.md")) + [ROOT / f for f in ROOT_DOCS if (ROOT / f).exists()]
    for md in files:
        raw = md.read_text(encoding="utf-8")
        for i, line in enumerate(strip_code(raw).splitlines(), 1):
            if PLACEHOLDER_RE.search(line) and not PLACEHOLDER_ALLOW.search(line):
                rep.error(f"{rel(md)}:{i}: placeholder text: {line.strip()[:80]}")
            if rel(md).split("/")[1:2] and rel(md).split("/")[1] in BOOKKEEPING_DIRS:
                m = BOOKKEEPING_RE.search(line)
                if m:
                    msg = f"{rel(md)}:{i}: maintainer bookkeeping in reader text: {m.group(0)!r}"
                    rep.error(msg) if BOOKKEEPING_IS_ERROR else rep.warn(msg)
        for lang, body, start in code_blocks(raw):
            where = f"{rel(md)}:{start}"
            if lang == "__unterminated__":
                rep.error(f"{where}: unterminated code fence")
            elif lang in ("yaml", "yml"):
                try:
                    list(yaml.safe_load_all(body))
                except yaml.YAMLError as exc:
                    rep.error(f"{where}: invalid YAML block: {str(exc).splitlines()[0]}")
            elif lang == "json":
                try:
                    json.loads(body)
                except json.JSONDecodeError as exc:
                    rep.error(f"{where}: invalid JSON block: {exc}")
            elif lang == "mermaid":
                for problem in lint_mermaid(body):
                    rep.error(f"{where}: mermaid: {problem}")


def run_structure() -> int:
    rep = Report("chapters")
    check_chapters(rep)
    check_text_hygiene(rep)
    return rep.finish()


def run_mkdocs() -> int:
    print("[mkdocs] building with --strict ...")
    proc = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--quiet", "--site-dir", "site"],
        cwd=ROOT, capture_output=True, text=True,
    )
    output = (proc.stdout + proc.stderr).strip()
    if output:
        print(output)
    print(f"[mkdocs] {'ok' if proc.returncode == 0 else 'FAIL'}")
    return 1 if proc.returncode else 0


def main() -> int:
    failures = 0
    failures += build_curriculum.run(check=True)
    failures += run_structure()
    failures += check_navigation.run()
    failures += check_references.run()
    failures += check_exercises.run()
    failures += build_single_file.run(check=True)
    if "--build" in sys.argv:
        failures += run_mkdocs()
    print()
    print("VALIDATION " + ("FAILED" if failures else "PASSED")
          + " (automated checks only; see research/human-review-checklist.md)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

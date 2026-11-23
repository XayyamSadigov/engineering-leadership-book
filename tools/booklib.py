"""Shared helpers for the book tools. Standard library plus PyYAML only."""
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESEARCH = ROOT / "research"
DIST = ROOT / "dist"
CURRICULUM = ROOT / "curriculum.yaml"
BIBLIOGRAPHY = RESEARCH / "bibliography.yaml"
MKDOCS = ROOT / "mkdocs.yml"

# Translations live beside the English page as page.<locale>.md (mkdocs-static-i18n, suffix mode).
# The English checks (contract, nav coverage, bookkeeping) apply to English files only.
TRANSLATION_LOCALES = ("ru",)
TRANSLATION_RE = re.compile(r"\.(?:" + "|".join(TRANSLATION_LOCALES) + r")\.md$")


def is_translation(path: Path) -> bool:
    return bool(TRANSLATION_RE.search(path.name))


def translation_of(path: Path, like: Path) -> Path:
    """The page the i18n plugin serves for a link from `like` to `path`: same-locale file if present."""
    m = TRANSLATION_RE.search(like.name)
    if m and not is_translation(path):
        candidate = path.with_name(path.name[: -len(".md")] + m.group(0))
        if candidate.exists():
            return candidate
    return path

# The chapter writing contract (CLAUDE.md, section "Chapter contract"). Order is enforced.
REQUIRED_SECTIONS = [
    "Why This Matters",
    "Learning Objectives",
    "The Mental Model",
    "Deep Conceptual Explanation",
    "Engineering Organization Example",
    "Decision Framework",
    "Trade-offs",
    "Failure Modes",
    "Enterprise Application",
    "CTO Perspective",
    "Practical Playbook",
    "Case Study",
    "Exercises",
    "Reflection Questions",
    "Key Takeaways",
    "References and Further Reading",
]
EXERCISE_LEVELS = [
    ("Foundational", "F"),
    ("Applied Leadership", "A"),
    ("Executive Decision-Making", "X"),
]
STATUSES = {"planned", "draft", "review", "published"}
# "review": passes automated validation and is visible on the site (the site-wide announcement says
# the book awaits human review), but has not yet
# had the human review in research/human-review-checklist.md. "published": both.
LIVE = {"review", "published"}
REVIEW_BANNER = '!!! warning "Awaiting human review"'
EVIDENCE_CLASSES = {
    "scholarly",
    "industry-research",
    "standard",
    "practitioner",
    "official-documentation",
}
ACCESS_LEVELS = {"full-text", "abstract-only", "official-summary", "metadata-only"}
CITATION_RE = re.compile(r"\]\((?:\.\./)*references/bibliography\.md#([a-z0-9-]+)\)")
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")


@dataclass
class Chapter:
    n: int
    slug: str
    title: str
    status: str
    part_number: int
    part_slug: str
    part_title: str
    part_roman: str
    objectives: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    project: str | None = None

    @property
    def id(self) -> str:
        return f"ch{self.n:02d}"

    @property
    def rel_path(self) -> str:
        """Path relative to docs/."""
        return f"parts/{self.part_slug}/{self.n:02d}-{self.slug}.md"

    @property
    def path(self) -> Path:
        return DOCS / self.rel_path

    @property
    def solutions_rel_path(self) -> str:
        return f"solutions/{self.id}-solutions.md"

    @property
    def solutions_path(self) -> Path:
        return DOCS / self.solutions_rel_path


class _Loader(yaml.SafeLoader):
    """SafeLoader that tolerates mkdocs' python tags (!!python/name:...)."""


def _ignore_unknown(loader: yaml.Loader, suffix: str, node: yaml.Node) -> Any:
    return None


_Loader.add_multi_constructor("tag:yaml.org,2002:python/", _ignore_unknown)


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return yaml.load(fh, Loader=_Loader)  # noqa: S506 - _Loader derives from SafeLoader


def load_curriculum() -> dict[str, Any]:
    return load_yaml(CURRICULUM)


def _forced_live() -> set[int]:
    """Chapter numbers in ELH_TREAT_AS_LIVE (comma-separated) are checked as if in 'review'.

    Lets an author validate a chapter before it is added to curriculum status and the nav:
        ELH_TREAT_AS_LIVE=21 python tools/validate_book.py
    Expect only the "missing from mkdocs nav" errors for that chapter.
    """
    raw = os.environ.get("ELH_TREAT_AS_LIVE", "")
    return {int(x) for x in raw.split(",") if x.strip().isdigit()}


def iter_chapters(status: str | None = None) -> Iterator[Chapter]:
    cur = load_curriculum()
    forced = _forced_live()
    for part in cur["parts"]:
        for ch in part.get("chapters") or []:
            chapter = Chapter(
                n=ch["n"],
                slug=ch["slug"],
                title=ch["title"],
                status="review" if ch["n"] in forced else ch["status"],
                part_number=part["number"],
                part_slug=part["slug"],
                part_title=part["title"],
                part_roman=part["roman"],
                objectives=ch.get("objectives") or [],
                sources=ch.get("sources") or [],
                project=ch.get("project"),
            )
            if status is None or chapter.status == status or (status == "live" and chapter.status in LIVE):
                yield chapter


PENDING_SOURCES = RESEARCH / "pending-sources"


def load_bibliography() -> list[dict[str, Any]]:
    """The verified bibliography plus any per-author pending files awaiting merge.

    research/pending-sources/<name>.yaml holds new entries written by one author (one file per
    author, so parallel authors never edit the same file). The maintainer merges them into
    research/bibliography.yaml and deletes the pending file.
    """
    entries: list[dict[str, Any]] = []
    if BIBLIOGRAPHY.exists():
        entries.extend(load_yaml(BIBLIOGRAPHY) or [])
    if PENDING_SOURCES.is_dir():
        for path in sorted(PENDING_SOURCES.glob("*.yaml")):
            entries.extend(load_yaml(path) or [])
    return entries


def bibliography_ids() -> set[str]:
    return {e["id"] for e in load_bibliography() if isinstance(e, dict) and "id" in e}


def strip_code(text: str) -> str:
    """Return text with fenced code blocks blanked (line count preserved)."""
    out: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        m = FENCE_RE.match(line.strip())
        if fence is None and m:
            fence = m.group(1)[0] * 3
            out.append("")
            continue
        if fence is not None:
            if line.strip().startswith(fence) and line.strip().strip(fence[0]) == "":
                fence = None
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)


def code_blocks(text: str) -> list[tuple[str, str, int]]:
    """Return (language, body, start_line) for each fenced block."""
    blocks: list[tuple[str, str, int]] = []
    fence: str | None = None
    lang = ""
    body: list[str] = []
    start = 0
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        m = FENCE_RE.match(stripped)
        if fence is None and m:
            fence = m.group(1)[0] * 3
            lang = m.group(2).strip().split(" ")[0]
            body = []
            start = i
            continue
        if fence is not None:
            if stripped.startswith(fence) and stripped.strip(fence[0]) == "":
                blocks.append((lang, "\n".join(body), start))
                fence = None
            else:
                body.append(line)
    if fence is not None:
        blocks.append(("__unterminated__", "\n".join(body), start))
    return blocks


def headings(text: str, level: int | None = None) -> list[tuple[int, str, int]]:
    """Return (level, title, line_number) for headings outside code fences."""
    found: list[tuple[int, str, int]] = []
    for i, line in enumerate(strip_code(text).splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if m and (level is None or len(m.group(1)) == level):
            found.append((len(m.group(1)), m.group(2).strip(), i))
    return found


def section(text: str, title: str, level: int = 2) -> str | None:
    """Return the body of the section with this heading, or None."""
    lines = text.splitlines()
    clean = strip_code(text).splitlines()
    start: int | None = None
    for i, line in enumerate(clean):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not m:
            continue
        lvl, name = len(m.group(1)), m.group(2).strip()
        if start is None and lvl == level and name == title:
            start = i + 1
        elif start is not None and lvl <= level:
            return "\n".join(lines[start:i])
    return "\n".join(lines[start:]) if start is not None else None


def word_count(text: str) -> int:
    prose = strip_code(text)
    prose = re.sub(r"<!--.*?-->", " ", prose, flags=re.S)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'%$.,/-]*", prose))


def slugify(title: str) -> str:
    """Approximation of the Python-Markdown toc slug."""
    s = re.sub(r"[`*_]", "", title).lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"[\s]+", "-", s).strip("-")


def nav_files() -> list[str]:
    """All Markdown files referenced from mkdocs.yml nav, relative to docs/."""
    cfg = load_yaml(MKDOCS)
    files: list[str] = []

    def walk(node: Any) -> None:
        if isinstance(node, str):
            if node.endswith(".md"):
                files.append(node)
        elif isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            for value in node.values():
                walk(value)

    walk(cfg.get("nav", []))
    return files


class Report:
    """Collects errors and warnings and prints them in a stable format."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def note(self, msg: str) -> None:
        self.notes.append(msg)

    def finish(self) -> int:
        for msg in self.notes:
            print(f"  info  {msg}")
        for msg in self.warnings:
            print(f"  WARN  {msg}")
        for msg in self.errors:
            print(f"  ERROR {msg}")
        status = "FAIL" if self.errors else "ok"
        print(f"[{self.name}] {status}: {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main_guard(fn) -> None:  # type: ignore[no-untyped-def]
    sys.exit(fn())

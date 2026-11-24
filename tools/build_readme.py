"""Write README.md: the book's front page on GitHub, with a table of contents from curriculum.yaml.

Run after changing chapter titles, templates, or projects:  python tools/build_readme.py
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://xayyamsadigov.github.io/engineering-leadership-book/"
DOCS = ROOT / "docs"


def site_url(doc_path: str) -> str:
    """docs-relative path of a page -> its URL on the site."""
    page = doc_path[:-3]
    if page.endswith("index"):
        page = page[: -len("index")]
    else:
        page += "/"
    return SITE + page


def h1(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return re.sub(r"^#\s+", "", first).strip()


def template_groups() -> list[tuple[str, list[str]]]:
    """Groups and template files in the order of docs/templates/index.md."""
    groups: list[tuple[str, list[str]]] = []
    for line in (DOCS / "templates/index.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            groups.append((line[3:].strip(), []))
        elif groups:
            for f in re.findall(r"\]\(([a-z0-9-]+\.md)\)", line):
                if f not in groups[-1][1]:
                    groups[-1][1].append(f)
    return groups


def main() -> None:
    cur = yaml.safe_load((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    book = cur["book"]
    out: list[str] = []
    w = out.append

    w(f"# {book['title']}\n")
    w(f"**{book['subtitle']}**\n")
    w("An open, evidence-informed textbook on building, leading, scaling, and transforming software")
    w("engineering organizations. Sixty chapters take you from your first team to the CTO's seat, with")
    w("one fictional company, Northstar Technologies, followed through a year of recovery as the running")
    w("case.\n")
    w(
        f"**[Read online]({SITE})** · "
        f"**[EPUB]({SITE}downloads/engineering-leadership-handbook.epub)** · "
        f"**[PDF]({SITE}downloads/engineering-leadership-handbook.pdf)** · "
        f"Русская версия: [онлайн]({SITE}ru/) · "
        f"[EPUB]({SITE}downloads/engineering-leadership-handbook-ru.epub) · "
        f"[PDF]({SITE}downloads/engineering-leadership-handbook-ru.pdf) (60 chapters; solutions, "
        "templates, and projects in English)\n"
    )
    w("> **Status:** complete draft. All chapters, templates, and projects are written and checked by")
    w("> automated validation and independent review; the citations still await a human reviewer.\n")

    w("## What is inside\n")
    w("| | |")
    w("|---|---|")
    inside = [
        (
            "**60 chapters** in 13 parts plus a capstone",
            "Each with a mental model, a worked example, a decision framework, trade-offs, "
            "failure modes, the CTO's view, a playbook, and exercises at three levels",
        ),
        (
            f"**[Worked solutions]({SITE}exercises/)**",
            "For every exercise, with the criteria a good answer meets",
        ),
        (
            f"**[24 templates]({SITE}templates/)**",
            "One-on-ones to board updates, each with a filled-in example",
        ),
        (f"**[8 projects]({SITE}projects/)**", "Practical assignments with rubrics and worked solutions"),
        (
            f"**[Northstar Technologies]({SITE}case-studies/northstar/)**",
            "An 80-engineer company with a quality crisis and a mandate to recover without new "
            "headcount; data files included",
        ),
        (
            f"**[Glossary]({SITE}glossary/)** and "
            f"**[verified bibliography]({SITE}references/bibliography/)**",
            "Every claim labeled by the strength of its evidence",
        ),
    ]
    for left, right in inside:
        w(f"| {left} | {right} |")
    w("")

    w("## Where to start\n")
    w("| You are | Start with |")
    w("|---|---|")
    paths = [
        ("A senior engineer becoming a manager", "path-a-new-engineering-manager"),
        ("A manager with a year or more running a team", "path-b-experienced-engineering-manager"),
        ("Managing managers, or about to", "path-c-engineering-director"),
        ("A director becoming a VP", "path-d-vp-of-engineering"),
        ("Preparing for a CTO role", "path-e-cto-aspirant"),
        ("A sitting CTO or VP with a specific problem", "path-f-cto-reference"),
        ("A tech lead or staff-plus engineer", "path-g-tech-lead-and-staff-plus-engineer"),
        ("Responsible for fixing quality or reliability", "path-h-quality-transformation"),
    ]
    for who, anchor in paths:
        w(f"| {who} | [Path {anchor[5].upper()}]({SITE}learning-roadmaps/#{anchor}) |")
    w("")
    w(
        f"Before any path, read the [Northstar overview]({SITE}case-studies/northstar/) and "
        f"[the year in brief]({SITE}case-studies/northstar/year-in-brief/) (about 20 minutes together).\n"
    )

    w("## Contents\n")
    for part in cur["parts"]:
        w(f"### Part {part['roman']}. {part['title']}\n")
        if part.get("summary"):
            w(f"*{part['summary']}*\n")
        if part["slug"].startswith("14-"):
            for group, files in template_groups():
                links = ", ".join(
                    f"[{h1(DOCS / 'templates' / f)}]({site_url('templates/' + f)})" for f in files
                )
                w(f"- **{group}:** {links}")
            w("")
            continue
        for ch in part.get("chapters", []):
            path = f"parts/{part['slug']}/{ch['n']:02d}-{ch['slug']}.md"
            w(f"{ch['n']}. [{ch['title']}]({site_url(path)})")
        w("")

    w("### Projects\n")
    for f in sorted((DOCS / "projects").glob("p*.md")):
        title = h1(f).split(": ", 1)[-1]
        w(f"{f.name[1]}. [{title}]({site_url('projects/' + f.name)})")
    w("")

    w("## How this book is made\n")
    w("The book was written with AI agents (Claude) working under binding authoring rules")
    w("([`CLAUDE.md`](CLAUDE.md)): every source verified on a fetched page and recorded in")
    w("[`research/bibliography.yaml`](research/bibliography.yaml), no invented quotations or statistics,")
    w("evidence labels on every claim, and automated checks in CI. It has not yet had a full human review")
    w("of its citations; corrections are the most valuable contribution. See")
    w("[`CONTRIBUTING.md`](CONTRIBUTING.md) to report an error or to build the book locally.\n")

    w("## License\n")
    w("Text, templates, and data: [CC BY 4.0](LICENSE-CONTENT.md). Code and configuration: [MIT](LICENSE).")
    w("Northstar Technologies, Halvard Systems, and everyone in them are fictional.")

    (ROOT / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

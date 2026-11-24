#!/usr/bin/env python3
"""Build the EPUB and PDF editions of the book.

    python tools/build_ebooks.py                 # both editions into dist/
    python tools/build_ebooks.py --epub          # EPUB only
    python tools/build_ebooks.py --pdf           # PDF only
    python tools/build_ebooks.py --markdown-only # stop after build/ebook/book-*.md (no pandoc, no node)
    python tools/build_ebooks.py --lang ru       # the Russian edition (pages that have a .ru.md)

Requirements: pandoc 3.x (on PATH, or the pypandoc_binary wheel), Node.js 18+ and npm. The script
installs @mermaid-js/mermaid-cli (which brings puppeteer and its Chromium) into build/ebook/node on
first use and downloads the IBM Plex fonts (SIL Open Font License) into build/ebook/fonts.

Pipeline:
1. Book-order Markdown, from the same nav order as tools/build_single_file.py: an edition note,
   front matter, Parts I-XV with their chapters, projects, the Northstar case pages, references,
   then every worked solution in a final "Solutions" part.
2. Every Mermaid block is rendered once with mermaid-cli (PNG at 2x for EPUB, SVG for PDF) and
   cached by content hash in build/ebook/diagrams/, so rebuilds only render changed diagrams.
3. Links between included pages become in-book links: every heading gets an id prefixed with its
   page's anchor, the same slug MkDocs would give it. Links to pages outside the book become plain
   text. MkDocs admonitions become styled divs; the per-chapter "Awaiting human review" banner is
   dropped and stated once in the edition note.
4. EPUB: pandoc with tools/ebook/epub.css. PDF: pandoc to standalone HTML with
   tools/ebook/print.css, printed by Chromium (tools/ebook/print.cjs), twice when PyMuPDF is
   available so the printed table of contents carries page numbers.

Russian edition (--lang ru): every page that has a translated page.ru.md beside it, in the same
order; pages without a translation (solutions, templates, projects) are left out, and links to them
become plain text. The bibliography stays in its original form so citations remain links. Titles and
labels the script adds come from tools/ebook/ru.yaml and the ru nav_translations in mkdocs.yml.
IBM Plex Sans Condensed has no Cyrillic, so the Russian edition sets its sans-serif text in the
variable IBM Plex Sans, narrowed with font-stretch.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path
from urllib.parse import quote

import yaml

from booklib import DIST, DOCS, FENCE_RE, LINK_RE, MKDOCS, REVIEW_BANNER, ROOT, load_curriculum, load_yaml
from build_single_file import nav_groups, page_anchor

BUILD = ROOT / "build" / "ebook"
ASSETS = Path(__file__).resolve().parent / "ebook"
DIAGRAMS = BUILD / "diagrams"
FONTS = BUILD / "fonts"
NODE_PREFIX = BUILD / "node"
MERMAID_CLI = "@mermaid-js/mermaid-cli@11.4.2"
SLUG = "engineering-leadership-handbook"
SITE = "https://xayyamsadigov.github.io/engineering-leadership-book/"
AUTHOR = "Khayyam Sadigov"  # LICENSE-CONTENT.md
FONT_BASE = "https://github.com/google/fonts/raw/main/ofl/"
FONT_FILES = [
    "ibmplexserif/IBMPlexSerif-Regular.ttf",
    "ibmplexserif/IBMPlexSerif-Italic.ttf",
    "ibmplexserif/IBMPlexSerif-SemiBold.ttf",
    "ibmplexserif/IBMPlexSerif-SemiBoldItalic.ttf",
    "ibmplexsanscondensed/IBMPlexSansCondensed-Regular.ttf",
    "ibmplexsanscondensed/IBMPlexSansCondensed-Italic.ttf",
    "ibmplexsanscondensed/IBMPlexSansCondensed-SemiBold.ttf",
    "ibmplexmono/IBMPlexMono-Regular.ttf",
    # Variable IBM Plex Sans (wdth and wght axes): the Cyrillic sans-serif face of the Russian edition.
    "ibmplexsans/IBMPlexSans[wdth,wght].ttf",
    "ibmplexsans/IBMPlexSans-Italic[wdth,wght].ttf",
]
# Pandoc extensions that Python-Markdown does not have and that would misread the book's prose:
# "$120k and $80k" as math, "~30%" as subscript, "@name" as a citation, "A." as a list marker.
PANDOC_FROM = (
    "markdown-tex_math_dollars-raw_tex-subscript-superscript-citations-fancy_lists"
    "-example_lists-simple_tables-multiline_tables-grid_tables-line_blocks"
    "-yaml_metadata_block-implicit_figures"
)
ROMAN = re.compile(r"^([IVXL]+)\.\s+(.+)$")
ADMONITION = re.compile(r'^(!!!|\?\?\?\+?)\s+([\w-]+)(?:\s+"([^"]*)")?\s*$')
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(?:\{([^}]*)\})?\s*#*\s*$")
CHAPTER_TITLE = re.compile(r"^(?:Chapter|Глава) (\d+) — (.+)$")


class Edition:
    """Language of the edition being built, and the words the script adds around the pages."""

    def __init__(self, lang: str = "en") -> None:
        self.lang = lang
        self.ru = lang == "ru"
        self.slug = SLUG + ("-ru" if self.ru else "")
        self.words = {"part": "Part", "chapter": "Chapter", "introduction": "Introduction",
                      "contents": "Contents", "diagram": "Diagram",
                      "northstar": "Case study: Northstar Technologies", "references": "References"}
        self.part_titles: dict[str, str] = {}
        self.part_summaries: dict[str, str] = {}
        self.meta: dict[str, str] = {}
        if self.ru:
            data = yaml.safe_load((ASSETS / "ru.yaml").read_text(encoding="utf-8"))
            self.words.update(data["strings"])
            self.part_summaries = {str(k): v for k, v in data["parts"].items()}
            self.meta = {k: data[k] for k in ("title", "subtitle", "description")}
            for plugin in load_yaml(MKDOCS).get("plugins", []):
                if isinstance(plugin, dict) and "i18n" in plugin:
                    for language in plugin["i18n"]["languages"]:
                        if language.get("locale") == "ru":
                            for en, ru in language.get("nav_translations", {}).items():
                                m = ROMAN.match(ru)
                                if m and ROMAN.match(en):
                                    self.part_titles[m.group(1)] = m.group(2)

    def source(self, rel_path: str) -> str | None:
        """The file that holds this page's text in this edition, or None to leave the page out."""
        if not self.ru:
            return rel_path
        ru = rel_path[:-3] + ".ru.md"
        if (DOCS / ru).exists():
            return ru
        return rel_path if rel_path == "references/bibliography.md" else None


ED = Edition()


# --------------------------------------------------------------------------------------------
# Book structure
# --------------------------------------------------------------------------------------------

class Page:
    """One source page placed in the book at a heading level (1 = top-level division)."""

    def __init__(self, rel_path: str, level: int, kind: str = "page") -> None:
        self.rel_path = rel_path  # the English path: links between pages use it
        self.source = ED.source(rel_path) or rel_path  # the file read for this edition
        self.level = level
        self.kind = kind  # page | chapter | front | solution


def book_plan() -> list[tuple[str, dict, list[Page]]]:
    """Return [(division title, attributes, pages)] in book order.

    The nav (via build_single_file.nav_groups) decides which pages exist and their order inside a
    group; this function only decides where each group goes in a book.
    """
    cur = load_curriculum()
    parts = {p["roman"]: p for p in cur["parts"]}
    front: list[Page] = []
    numbered: list[tuple[str, dict, list[Page]]] = []
    other: list[tuple[str, dict, list[Page]]] = []
    projects: list[Page] = []
    northstar: list[Page] = []
    references: list[Page] = []
    solutions: list[Page] = []
    project_solutions: list[Page] = []
    seen: set[str] = set()
    skip = {"curriculum.md", "exercises/index.md", "download.md"}

    def take(f: str) -> bool:
        if f in seen or f in skip or not (DOCS / f).exists() or ED.source(f) is None:
            return False
        seen.add(f)
        return True

    for title, files in nav_groups():
        m = ROMAN.match(title)
        if not title or (len(files) == 1 and "/" not in files[0]):
            front += [Page(f, 1, "front") for f in files if take(f)]
        elif m:
            part = parts.get(m.group(1), {})
            pages = [
                Page(f, 2, "chapter" if f.startswith("parts/") else "page") for f in files if take(f)
            ]
            if not pages:
                continue
            roman = m.group(1)
            ptitle = ED.part_titles.get(roman) or part.get("title", m.group(2))
            summary = ED.part_summaries.get(roman, "") if ED.ru else part.get("summary", "")
            numbered.append((
                f"[{ED.words['part']} {roman}]{{.part-num}}[: ]{{.sep}}{ptitle}",
                {"id": f"part-{roman.lower()}", "class": "part", "summary": summary},
                pages,
            ))
        elif title.startswith("Case study"):
            northstar += [Page(f, 2) for f in files if take(f)]
        elif title == "Projects":
            for f in files:
                if take(f):
                    (project_solutions if "/solutions/" in f else projects).append(
                        Page(f, 2, "solution" if "/solutions/" in f else "page"))
        elif title.startswith("Exercises"):
            solutions += [Page(f, 2, "solution") for f in files if take(f)]
        elif title == "References":
            references += [Page(f, 2) for f in files if take(f)]
        else:
            pages = [Page(f, 2) for f in files if take(f)]
            if pages:
                other.append((title, {"id": "div-" + re.sub(r"\W+", "-", title.lower())}, pages))

    # Pages that exist but are not yet in the nav: the glossary and new Northstar pages.
    if take("glossary.md"):
        front.append(Page("glossary.md", 1, "front"))
    for extra in sorted((DOCS / "case-studies" / "northstar").glob("*.md")):
        f = str(extra.relative_to(DOCS))
        if not extra.name.endswith(".ru.md") and take(f):  # Russian pages are not in the English book
            northstar.append(Page(f, 2))

    plan: list[tuple[str, dict, list[Page]]] = [("", {}, front)]
    plan += numbered
    plan += other
    if projects:
        plan.append(("Projects", {"id": "div-projects", "class": "division"}, projects))
    if northstar:
        plan.append((ED.words["northstar"],
                     {"id": "div-northstar", "class": "division"}, northstar))
    if references:
        plan.append((ED.words["references"], {"id": "div-references", "class": "division"}, references))
    if solutions or project_solutions:
        plan.append(("Solutions", {"id": "div-solutions", "class": "division",
                                   "summary": "Worked solutions to the chapter exercises, then to "
                                              "the projects. Try the exercise first."},
                     solutions + project_solutions))
    return plan


# --------------------------------------------------------------------------------------------
# Markdown transformation
# --------------------------------------------------------------------------------------------

def md_slug(text: str) -> str:
    """Python-Markdown's toc slugify (unicode off), applied to the heading's visible text."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_]", "", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def heading_ids(rel_path: str, text: str) -> dict[str, str]:
    """Map every MkDocs anchor on a page to its in-book id."""
    prefix = page_anchor(rel_path)
    ids: dict[str, str] = {}
    fence = None
    for line in text.splitlines():
        stripped = line.strip()
        m = FENCE_RE.match(stripped)
        if fence is None and m:
            fence = m.group(1)[0] * 3
            continue
        if fence is not None:
            if stripped.startswith(fence) and stripped.strip(fence[0]) == "":
                fence = None
            continue
        h = HEADING.match(line)
        if not h:
            continue
        explicit = re.search(r"#([\w-]+)", h.group(3) or "")
        slug = explicit.group(1) if explicit else md_slug(h.group(2))
        base, n = slug, 0
        while slug in ids:
            n += 1
            slug = f"{base}_{n}"
        ids[slug] = f"{prefix}--{slug}"
    return ids


def diagram_alt(body: str) -> str:
    labels = re.findall(r'\["([^"]+)"\]|\[([^\]"]+)\]|\{"?([^}"]+)"?\}|\("([^"]+)"\)', body)
    words = [next(x for x in grp if x) for grp in labels]
    alt = ", ".join(dict.fromkeys(w.strip() for w in words if w.strip()))
    alt = re.sub(r"<br\s*/?>", " ", alt)
    alt = re.sub(r"[\[\]]", "", alt)
    return (ED.words["diagram"] + ": " + alt)[:300] if alt else ED.words["diagram"]


def wrap_tables(lines: list[str]) -> list[str]:
    """Put pipe tables with many columns in a div so the stylesheets can tighten them."""
    out: list[str] = []
    i = 0
    fence: str | None = None
    while i < len(lines):
        m = FENCE_RE.match(lines[i].strip())
        if fence is None and m:
            fence = m.group(1)[0] * 3
        elif fence is not None and lines[i].strip().startswith(fence) and \
                lines[i].strip().strip(fence[0]) == "":
            fence = None
        elif fence is None and (lines[i].lstrip().startswith("|") and i + 1 < len(lines)
                and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1])):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            cols = lines[i + 1].strip().strip("|").count("|") + 1
            cls = "table-xwide" if cols >= 6 else "table-wide" if cols >= 4 else "table-narrow"
            out += ["", f"::: {{.table-wrap .{cls}}}", *lines[i:j], ":::", ""]
            i = j
            continue
        out.append(lines[i])
        i += 1
    return out


class Transformer:
    def __init__(self, pages: list[Page]) -> None:
        self.texts = {p.rel_path: (DOCS / p.source).read_text(encoding="utf-8") for p in pages}
        self.anchors = {f: heading_ids(f, t) for f, t in self.texts.items()}
        self.diagrams: dict[str, str] = {}  # hash -> mermaid source

    def link_target(self, src: str, target: str) -> str | None:
        """In-book href for a link from page src, or None to drop the link."""
        file_part, _, anchor = target.partition("#")
        if not file_part:
            dest_rel = src
        else:
            dest = (DOCS / src).parent / file_part
            if file_part.endswith("/"):
                dest = dest / "index.md"
            try:
                dest_rel = str(dest.resolve().relative_to(DOCS.resolve()))
            except ValueError:
                return None
        if dest_rel not in self.anchors:
            return None
        if not anchor:
            return "#" + page_anchor(dest_rel)
        return "#" + self.anchors[dest_rel].get(anchor, page_anchor(dest_rel))

    def fix_links(self, src: str, text: str) -> str:
        def fix(match: re.Match[str]) -> str:
            label, target = match.group(1), match.group(2)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                return match.group(0)
            href = self.link_target(src, target)
            return f"[{label}]({href})" if href else label
        return LINK_RE.sub(fix, text)

    def page(self, p: Page) -> str:
        src = p.rel_path
        text = re.sub(r"^<!--.*?-->\n+", "", self.texts[src], flags=re.S)
        ids = self.anchors[src]
        used: dict[str, int] = {}
        shift = p.level - 1
        out: list[str] = []
        lines = text.splitlines()
        i = 0
        fence: str | None = None
        mermaid: list[str] | None = None
        first_heading = True
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            m = FENCE_RE.match(stripped)
            if fence is None and m:
                fence = m.group(1)[0] * 3
                if m.group(2).strip().split(" ")[0] == "mermaid":
                    mermaid = []
                else:
                    out.append(line)
                i += 1
                continue
            if fence is not None:
                if stripped.startswith(fence) and stripped.strip(fence[0]) == "":
                    fence = None
                    if mermaid is not None:
                        body = "\n".join(mermaid).strip() + "\n"
                        digest = hashlib.sha256(body.encode()).hexdigest()[:16]
                        self.diagrams[digest] = body
                        out += ["", f"![{diagram_alt(body)}](diagrams/{digest}.@EXT@){{.diagram}}", ""]
                        mermaid = None
                    else:
                        out.append(line)
                elif mermaid is not None:
                    mermaid.append(line)
                else:
                    out.append(line)
                i += 1
                continue

            adm = ADMONITION.match(line)
            if adm:
                title = adm.group(3) if adm.group(3) is not None else adm.group(2).capitalize()
                body: list[str] = []
                i += 1
                while i < len(lines) and (not lines[i].strip() or lines[i].startswith("    ")):
                    body.append(lines[i][4:])
                    i += 1
                while body and not body[-1].strip():
                    body.pop()
                # The home page's status notes (and the Russian note about the website's language
                # switch) are restated once in the edition note.
                drop = line.strip() == REVIEW_BANNER or (src == "index.md" and title.lower().startswith(
                    ("status", "статус", "о русском издании")))
                if not drop:
                    out += ["", f":::: {{.admonition .{adm.group(2)}}}"]
                    if title:
                        out += ["::: {.admonition-title}", title, ":::", ""]
                    out += body + ["::::", ""]
                continue

            h = HEADING.match(line)
            if h:
                hashes, title = h.group(1), h.group(2)
                explicit = re.search(r"#([\w-]+)", h.group(3) or "")
                slug = explicit.group(1) if explicit else md_slug(title)
                n = used.get(slug, 0)
                used[slug] = n + 1
                key = slug if n == 0 else f"{slug}_{n}"
                level = min(6, len(hashes) + shift)
                classes = ""
                if first_heading:
                    hid = page_anchor(src)
                    if src == "index.md":
                        title = ED.words["introduction"]
                    if p.kind == "chapter":
                        cm = CHAPTER_TITLE.match(title)
                        if cm:
                            title = (f"[{ED.words['chapter']} {cm.group(1)}]{{.ch-num}}[ — ]{{.sep}}"
                                     f"{cm.group(2)}")
                    classes = f" .page-title .{p.kind}"
                    first_heading = False
                else:
                    hid = ids.get(key, f"{page_anchor(src)}--{key}")
                out.append(f"{'#' * level} {title} {{#{hid}{classes}}}")
                i += 1
                continue

            # The download pointer on the home page makes no sense inside the book itself.
            if "download.md" in line:
                i += 1
                continue
            out.append(line)
            i += 1
        return self.fix_links_outside_code(src, "\n".join(wrap_tables(out))).strip() + "\n"

    def fix_links_outside_code(self, src: str, text: str) -> str:
        """Rewrite links on the whole page at once, so a link label may span lines."""
        parts = re.split(r"(^[ \t]*(?:```|~~~).*?^[ \t]*(?:```|~~~)[ \t]*$)", text, flags=re.S | re.M)
        return "".join(p if i % 2 else self.fix_links(src, p) for i, p in enumerate(parts))


def edition_note(commit: str, today: str) -> str:
    return f"""# About this edition {{#edition-note .front}}

This is the EPUB and PDF edition of *The Engineering Leadership Handbook*, generated from the
same sources as the website at <{SITE}>. It was built on {today}{f" from commit `{commit}`" if commit else ""}
and is rebuilt every time the book changes, so the website and the downloads always carry the same text.

:::: {{.admonition .warning}}
::: {{.admonition-title}}
Awaiting human review
:::

Every chapter, template, and project in this edition is complete and has passed the book's automated
checks, but none has yet had the human review that checks each cited claim against its source. The
website says so in a notice at the top of every page; this edition says it once, here. Treat the
text as reviewed drafts, and report any claim its citation does not support.
::::

The text is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0);
copyright 2026 {AUTHOR}. Northstar Technologies, Halvard Systems, and every person, number, and dataset
attached to them are fictional. Links to the downloadable data files and other pages that exist only on
the website appear here as plain text; the website has them.
"""


def edition_note_ru(commit: str, today: str) -> str:
    built = f"{today}{f' из коммита `{commit}`' if commit else ''}"
    return f"""# Об этом издании {{#edition-note .front}}

Это EPUB- и PDF-издание русского перевода книги «{ED.meta['title']}». Оно собрано из тех же исходных
файлов, что и сайт <{SITE}ru/>, {built} и пересобирается при каждом изменении книги, поэтому сайт
и файлы для скачивания всегда совпадают.

В издание вошли все 60 глав, вводные страницы, глоссарий и весь кейс Northstar. Решения упражнений,
шаблоны и проекты пока не переведены: они есть в английском издании и на сайте, а ссылки на них здесь
даны обычным текстом. Библиография оставлена в исходном виде, на языке источников.

:::: {{.admonition .warning}}
::: {{.admonition-title}}
Книга ждёт проверки человеком
:::

Все главы прошли автоматические проверки книги, но ни одна ещё не прошла проверку человеком, который
сверяет каждое утверждение с источником. Читайте текст как проверенный черновик и сообщайте о любом
утверждении, которое не подтверждается его источником.

Перевод сделан ИИ-агентами (Claude) в три этапа: перевод, литературная редактура русского текста и
сверка смысла с оригиналом. Человек его пока не вычитывал. При расхождении прав английский оригинал.
::::

Текст распространяется по лицензии Creative Commons Attribution 4.0 International (CC BY 4.0);
© 2026 {AUTHOR}. Northstar Technologies, Halvard Systems, все их сотрудники, цифры и данные вымышлены.
"""


def build_markdown(ext: str) -> tuple[str, dict[str, str]]:
    plan = book_plan()
    pages = [p for _, _, ps in plan for p in ps]
    tr = Transformer(pages)
    commit = ""
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                                capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    today = dt.date.today().isoformat()
    chunks = [(edition_note_ru if ED.ru else edition_note)(commit, today)]
    for title, attrs, ps in plan:
        if title:
            cls = " ".join("." + c for c in attrs.get("class", "division").split())
            chunks.append(f"# {title} {{#{attrs['id']} {cls}}}\n")
            if attrs.get("summary"):
                chunks.append(f"::: {{.part-summary}}\n{attrs['summary']}\n:::\n")
        for p in ps:
            chunks.append(tr.page(p))
    text = "\n\n".join(chunks).replace("@EXT@", ext)
    return text, tr.diagrams


# --------------------------------------------------------------------------------------------
# Tools: node packages, fonts, pandoc, diagrams
# --------------------------------------------------------------------------------------------

def run(cmd: list[str], **kw) -> None:  # type: ignore[no-untyped-def]
    print("+", " ".join(str(c) for c in cmd[:6]), "..." if len(cmd) > 6 else "")
    subprocess.run(cmd, check=True, **kw)


def ensure_node() -> Path:
    mmdc = NODE_PREFIX / "node_modules" / ".bin" / "mmdc"
    if not mmdc.exists():
        npm = shutil.which("npm")
        if not npm:
            sys.exit("npm not found: install Node.js 18+ to render diagrams and print the PDF")
        NODE_PREFIX.mkdir(parents=True, exist_ok=True)
        run([npm, "install", "--prefix", str(NODE_PREFIX), "--no-audit", "--no-fund", MERMAID_CLI])
    return mmdc


def ensure_fonts() -> None:
    FONTS.mkdir(parents=True, exist_ok=True)
    for f in FONT_FILES:
        dest = FONTS / Path(f).name.replace("[wdth,wght]", "-Variable")
        if dest.exists() and dest.stat().st_size > 10_000:
            continue
        print(f"downloading font {dest.name}")
        curl = shutil.which("curl")
        if curl:  # curl honours the system trust store (and corporate proxies) where Python may not
            run([curl, "-fsSL", "--retry", "3", "-o", str(dest), FONT_BASE + quote(f)])
        else:
            with urllib.request.urlopen(FONT_BASE + quote(f), timeout=60) as resp:  # noqa: S310 - fixed URL
                dest.write_bytes(resp.read())


def pandoc_bin() -> str:
    found = os.environ.get("PANDOC") or shutil.which("pandoc")
    if found:
        return found
    try:
        import pypandoc  # type: ignore[import-not-found]
        return pypandoc.get_pandoc_path()
    except (ImportError, OSError):
        sys.exit("pandoc not found: install pandoc 3.x or `pip install pypandoc_binary`")


def render_diagrams(diagrams: dict[str, str], ext: str) -> None:
    """Render uncached diagrams with mermaid-cli, in batches."""
    DIAGRAMS.mkdir(parents=True, exist_ok=True)
    todo = [(h, body) for h, body in diagrams.items() if not (DIAGRAMS / f"{h}.{ext}").exists()]
    print(f"[diagrams] {len(diagrams)} {ext} diagrams, {len(diagrams) - len(todo)} cached")
    if not todo:
        return
    mmdc = ensure_node()
    work = BUILD / "mmdc-work"
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    (work / "puppeteer.json").write_text('{"args": ["--no-sandbox"]}', encoding="utf-8")
    (work / "mermaid.json").write_text(json.dumps({
        "theme": "neutral",
        "themeVariables": {"fontFamily": ("IBM Plex Sans, Arial, sans-serif" if ED.ru else
                                          "IBM Plex Sans Condensed, Arial Narrow, Arial, sans-serif"),
                           "fontSize": "15px"},
        "flowchart": {"htmlLabels": ext == "svg", "useMaxWidth": False},
    }), encoding="utf-8")
    # mermaid-cli keeps every chart of a Markdown input in memory; batches keep it under the
    # default Node heap while still sharing one browser launch per batch.
    batch = 12
    for start in range(0, len(todo), batch):
        chunk = todo[start:start + batch]
        (work / "in.md").write_text(
            "\n\n".join(f"```mermaid\n{body}```" for _, body in chunk) + "\n", encoding="utf-8")
        cmd = [str(mmdc), "-q", "-p", str(work / "puppeteer.json"), "-c", str(work / "mermaid.json"),
               "-i", str(work / "in.md"), "-o", str(work / "out.md"), "-e", ext, "-b", "white"]
        if ext == "png":
            cmd += ["-s", "2"]
        run(cmd)
        for n, (h, _) in enumerate(chunk, 1):
            produced = work / f"out-{n}.{ext}"
            if not produced.exists():
                sys.exit(f"mermaid-cli did not produce diagram {h}")
            shutil.move(str(produced), DIAGRAMS / f"{h}.{ext}")


def metadata(cur: dict) -> Path:
    meta = BUILD / "metadata.json"
    data = {
        "title": cur["book"]["title"],
        "subtitle": cur["book"]["subtitle"],
        "author": AUTHOR,
        "lang": "en-US",
        "rights": "CC BY 4.0. Copyright 2026 " + AUTHOR + ".",
        "date": dt.date.today().isoformat(),
        "description": "An open-source, evidence-informed textbook on building, leading, scaling, "
                       "and transforming software engineering organizations.",
        "identifier": [{"scheme": "URI", "text": SITE}],
    }
    if ED.ru:
        data.update(ED.meta, lang="ru-RU", **{"toc-title": ED.words["contents"]},
                    rights="CC BY 4.0. © 2026 " + AUTHOR + ".",
                    identifier=[{"scheme": "URI", "text": SITE + "ru/"}])
    meta.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return meta


# --------------------------------------------------------------------------------------------
# EPUB
# --------------------------------------------------------------------------------------------

def build_cover(cur: dict) -> Path:
    cover = DIAGRAMS / "cover.png"
    html = BUILD / "cover.html"
    page = (ASSETS / "cover.html").read_text(encoding="utf-8")
    if ED.ru:
        page = sans_for_cyrillic(page.replace('<html lang="en">', '<html lang="ru">'), "{{fonts}}")
    html.write_text(
        page
        .replace("{{title}}", ED.meta.get("title", cur["book"]["title"]))
        .replace("{{subtitle}}", ED.meta.get("subtitle", cur["book"]["subtitle"]))
        .replace("{{author}}", AUTHOR)
        .replace("{{fonts}}", FONTS.as_uri()),
        encoding="utf-8",
    )
    node_print("cover", html, cover)
    return cover


def sans_for_cyrillic(css: str, fonts: str = "@FONTS@") -> str:
    """Point the "Plex Cond" family at the variable IBM Plex Sans, which has Cyrillic, narrowed
    with font-stretch. Works on a stylesheet or on an HTML page with one <style> block."""
    css = re.sub(r'@font-face \{ font-family: "Plex Cond";[^}]*\}\n?', "", css)
    faces = "".join(
        f'@font-face {{ font-family: "Plex Cond"; font-weight: 100 700; font-stretch: 75% 100%;{style} '
        f'src: url("{fonts}/{name}"); }}\n'
        for style, name in (("", "IBMPlexSans-Variable.ttf"),
                            (" font-style: italic;", "IBMPlexSans-Italic-Variable.ttf")))
    extra = ("html { font-stretch: 87.5%; }\n"
             f'nav#TOC::before {{ content: "{ED.words["contents"]}"; }}\n')
    if "<style>" in css:
        return css.replace("<style>", "<style>\n" + faces, 1).replace("</style>", extra + "</style>", 1)
    return faces + css + "\n/* Russian edition */\n" + extra


def build_epub(cur: dict) -> Path:
    text, diagrams = build_markdown("png")
    src = BUILD / "book-epub.md"
    src.write_text(text, encoding="utf-8")
    ensure_fonts()  # before the diagrams, so mermaid-cli can use the fonts once installed
    render_diagrams(diagrams, "png")
    cover = build_cover(cur)
    out = DIST / f"{ED.slug}.epub"
    run([pandoc_bin(), str(src), "-f", PANDOC_FROM, "-t", "epub3", "-o", str(out),
         "--metadata-file", str(metadata(cur)), "--toc", "--toc-depth=2", "--split-level=2",
         "--css", str(ASSETS / "epub.css"), "--epub-cover-image", str(cover),
         "--columns=10000", "--resource-path", str(BUILD), "--syntax-highlighting=none"],
        cwd=BUILD)
    print(f"[epub] {out.relative_to(ROOT)} {out.stat().st_size / 1e6:.1f} MB")
    return out


# --------------------------------------------------------------------------------------------
# PDF
# --------------------------------------------------------------------------------------------

def node_print(mode: str, src: Path, out: Path) -> None:
    ensure_node()
    env = dict(os.environ, NODE_PATH=str(NODE_PREFIX / "node_modules"))
    run(["node", str(ASSETS / "print.cjs"), mode, str(src), str(out)], env=env)


def toc_page_numbers(pdf: Path) -> dict[str, int]:
    """Map heading id -> printed page number, read from the PDF's internal links."""
    import pymupdf as fitz  # type: ignore[import-not-found]

    doc = fitz.open(pdf)
    pages: dict[str, int] = {}
    for page in doc:
        for link in page.get_links():
            name = link.get("nameddest") or link.get("name") or ""
            if link.get("kind") in (fitz.LINK_GOTO, fitz.LINK_NAMED) and name and link.get("page", -1) >= 0:
                pages.setdefault(name, link["page"] + 1)
        if page.number > 40:  # the table of contents is near the front
            break
    return pages


def heading_titles(html: str) -> list[tuple[int, str]]:
    """Every h1-h6 in document order as (level, clean text): the PDF outline's entries."""
    import html as htmllib

    out = []
    for m in re.finditer(r"<h([1-6])\b[^>]*>(.*?)</h\1>", html, flags=re.S):
        text = re.sub(r'<span class="sep">(.*?)</span>', r"\1", m.group(2))
        text = re.sub(r'(<span class="(?:ch|part)-num">.*?</span>)(?!<span class="sep">)', r"\1 ", text)
        text = htmllib.unescape(re.sub(r"<[^>]+>", "", text))
        text = re.sub(r"\s*—\s*", " — ", re.sub(r"\s*:\s*", ": ", text))
        out.append((int(m.group(1)), re.sub(r"\s+", " ", text).strip()))
    return out


def fix_outline(pdf: Path, html: str, max_level: int = 3) -> None:
    """Chromium's outline drops the spaces at line wraps ("EngineeringProductivity") and lists every
    heading level. Replace each title with the heading's text and keep the top three levels."""
    try:
        import pymupdf  # type: ignore[import-not-found]
    except ImportError:
        return
    doc = pymupdf.open(pdf)
    toc = doc.get_toc(simple=False)
    titles = heading_titles(html)
    if len(toc) != len(titles):
        print(f"[pdf] outline has {len(toc)} entries for {len(titles)} headings; left as printed")
        return
    new = []
    for entry, (_, title) in zip(toc, titles):
        if entry[0] <= max_level:
            new.append([entry[0], title, entry[2], entry[3]])
    doc.set_toc(new)
    tmp = pdf.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    tmp.replace(pdf)
    print(f"[pdf] outline rewritten ({len(new)} entries)")


def build_pdf(cur: dict) -> Path:
    text, diagrams = build_markdown("svg")
    src = BUILD / "book-pdf.md"
    src.write_text(text, encoding="utf-8")
    ensure_fonts()  # before the diagrams, so mermaid-cli can use the fonts once installed
    render_diagrams(diagrams, "svg")
    css = BUILD / "print.css"
    print_css = (ASSETS / "print.css").read_text(encoding="utf-8")
    if ED.ru:
        print_css = sans_for_cyrillic(print_css)
    css.write_text(print_css.replace("@FONTS@", "fonts"), encoding="utf-8")
    html = BUILD / "book.html"
    run([pandoc_bin(), str(src), "-f", PANDOC_FROM, "-t", "html5", "-s", "-o", str(html),
         "--metadata-file", str(metadata(cur)), "--toc", "--toc-depth=2",
         "--css", "print.css", "--columns=10000", "--syntax-highlighting=none",
         "--metadata", "document-css=false", "--section-divs"], cwd=BUILD)
    out = DIST / f"{ED.slug}.pdf"
    node_print("pdf", html, out)
    try:
        numbers = toc_page_numbers(out)
    except ImportError:
        numbers = {}
        print("[pdf] PyMuPDF not installed: table of contents printed without page numbers")
    if numbers:
        page_html = html.read_text(encoding="utf-8")

        def number(m: re.Match[str]) -> str:
            n = numbers.get(m.group(2))
            return m.group(0) if n is None else f'{m.group(1)}<span class="toc-page">{n}</span></a>'

        nav_start = page_html.find('<nav id="TOC"')
        nav_end = page_html.find("</nav>", nav_start)
        nav = re.sub(r'(<a href="#([^"]+)"[^>]*>.*?)</a>', number, page_html[nav_start:nav_end],
                     flags=re.S)
        html.write_text(page_html[:nav_start] + nav + page_html[nav_end:], encoding="utf-8")
        node_print("pdf", html, out)
        print(f"[pdf] table of contents numbered ({len(numbers)} entries)")
    fix_outline(out, html.read_text(encoding="utf-8"))
    print(f"[pdf] {out.relative_to(ROOT)} {out.stat().st_size / 1e6:.1f} MB")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--epub", action="store_true", help="build the EPUB only")
    ap.add_argument("--pdf", action="store_true", help="build the PDF only")
    ap.add_argument("--fonts-only", action="store_true",
                    help="download the fonts into build/ebook/fonts and stop (CI installs them)")
    ap.add_argument("--markdown-only", action="store_true", help="write the book Markdown and stop")
    ap.add_argument("--lang", choices=["en", "ru"], default="en",
                    help="edition language (ru: the pages that have a Russian translation)")
    args = ap.parse_args()
    global ED
    ED = Edition(args.lang)
    BUILD.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(exist_ok=True)
    cur = load_curriculum()
    if args.fonts_only:
        ensure_fonts()
        return 0
    if args.markdown_only:
        for ext in ("png", "svg"):
            text, diagrams = build_markdown(ext)
            (BUILD / f"book-{'epub' if ext == 'png' else 'pdf'}{'-ru' if ED.ru else ''}.md").write_text(
                text, encoding="utf-8")
        print(f"[ebooks] wrote {BUILD.relative_to(ROOT)}/book-*.md, {len(diagrams)} diagrams")
        return 0
    both = not (args.epub or args.pdf)
    if both or args.epub:
        build_epub(cur)
    if both or args.pdf:
        build_pdf(cur)
    return 0


if __name__ == "__main__":
    sys.exit(main())

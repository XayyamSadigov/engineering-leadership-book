#!/usr/bin/env python3
"""Navigation, link, and identifier checks.

- every file in the mkdocs nav exists; no file is listed twice
- every published chapter and template is in the nav; planned and draft ones are not
- chapter numbers and slugs are unique and contiguous
- every relative Markdown link in docs/ resolves to a file, and its #anchor to a heading or id
- every Markdown file under docs/ is reachable from the nav (warning)
"""
from __future__ import annotations

import re
from pathlib import Path

from booklib import (
    DOCS,
    LINK_RE,
    LIVE,
    Report,
    headings,
    is_translation,
    iter_chapters,
    load_curriculum,
    main_guard,
    nav_files,
    rel,
    slugify,
    strip_code,
    translation_of,
)

ID_RE = re.compile(r"""(?:id|name)=["']([^"']+)["']""")
ATTR_ID_RE = re.compile(r"\{[^}]*#([A-Za-z0-9_-]+)[^}]*\}")


def anchors_of(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    if path not in cache:
        text = path.read_text(encoding="utf-8")
        found: set[str] = set()
        seen: dict[str, int] = {}
        for _, title, _ in headings(text):
            explicit = ATTR_ID_RE.search(title)
            if explicit:
                found.add(explicit.group(1))
                continue
            slug = slugify(title)
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            found.add(slug if count == 0 else f"{slug}_{count}")
        found.update(ID_RE.findall(text))
        cache[path] = found
    return cache[path]


def run() -> int:
    rep = Report("navigation")
    nav = nav_files()

    dupes = {f for f in nav if nav.count(f) > 1}
    for f in sorted(dupes):
        rep.error(f"mkdocs nav lists {f} more than once")
    for f in nav:
        if not (DOCS / f).is_file():
            rep.error(f"mkdocs nav points to missing file docs/{f}")

    numbers: list[int] = []
    slugs: set[str] = set()
    for ch in iter_chapters():
        numbers.append(ch.n)
        if ch.slug in slugs:
            rep.error(f"duplicate chapter slug: {ch.slug}")
        slugs.add(ch.slug)
        in_nav = ch.rel_path in nav
        if ch.status in LIVE:
            if not ch.path.is_file():
                rep.error(f"{ch.id} is live but {rel(ch.path)} does not exist")
            if not in_nav:
                rep.error(f"{ch.id} is live but missing from mkdocs nav ({ch.rel_path})")
            if ch.solutions_rel_path not in nav:
                rep.error(f"{ch.id} is live but its solutions file is missing from mkdocs nav")
        elif in_nav:
            rep.error(f"{ch.id} has status '{ch.status}' and must not be in the mkdocs nav")
    if len(numbers) != len(set(numbers)):
        rep.error("duplicate chapter numbers in curriculum.yaml")
    if sorted(numbers) != list(range(1, len(numbers) + 1)):
        rep.error("chapter numbers in curriculum.yaml are not contiguous from 1")

    cur = load_curriculum()
    template_ids: set[str] = set()
    for t in cur.get("templates", []):
        if t["id"] in template_ids:
            rep.error(f"duplicate template id {t['id']}")
        template_ids.add(t["id"])
        path = f"templates/{t['file']}"
        if t["status"] in LIVE and path not in nav:
            rep.error(f"template {t['id']} is live but {path} is missing from mkdocs nav")
        if t["status"] not in LIVE and path in nav:
            rep.error(f"template {t['id']} is '{t['status']}' and must not be in the mkdocs nav")

    cache: dict[Path, set[str]] = {}
    md_files = sorted(DOCS.rglob("*.md"))
    link_count = 0
    for md in md_files:
        text = strip_code(md.read_text(encoding="utf-8"))
        for m in LINK_RE.finditer(text):
            target = m.group(2)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):  # http:, mailto:, etc.
                continue
            link_count += 1
            file_part, _, anchor = target.partition("#")
            dest = md if not file_part else (md.parent / file_part).resolve()
            if not dest.exists():
                rep.error(f"{rel(md)}: broken link -> {target}")
                continue
            if dest.is_dir() or dest.suffix != ".md":
                continue
            dest = translation_of(dest, md)
            if anchor and anchor not in anchors_of(dest, cache):
                rep.error(f"{rel(md)}: anchor not found -> {target}")

    nav_set = set(nav)
    for md in md_files:
        if is_translation(md):
            continue
        r = str(md.relative_to(DOCS))
        if r not in nav_set:
            rep.warn(f"docs/{r} is not in the mkdocs nav")

    rep.note(f"{len(nav)} nav entries, {len(md_files)} Markdown files, {link_count} internal links checked")
    return rep.finish()


if __name__ == "__main__":
    main_guard(run)

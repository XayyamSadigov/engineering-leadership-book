#!/usr/bin/env python3
"""Bibliography and citation checks.

- research/bibliography.yaml is structurally valid (required keys, enumerations, unique ids)
- every citation link in docs/ (…/references/bibliography.md#id) points at an existing id
- every source id listed in curriculum.yaml exists in the bibliography
- every published chapter cites at least MIN_CITED distinct sources, and at least one source
  that is not practitioner opinion
- cited sources with no verified fields are reported (error for published chapters)
- every part that has a published chapter has citations

This proves citations are well-formed and traceable. It does not prove a claim is true; that is
the job of research/human-review-checklist.md.
"""
from __future__ import annotations

import re

from booklib import (
    ACCESS_LEVELS,
    CITATION_RE,
    DOCS,
    EVIDENCE_CLASSES,
    Report,
    iter_chapters,
    load_bibliography,
    main_guard,
    rel,
)

MIN_CITED = 5
REQUIRED = ["id", "type", "title", "authors", "year", "evidence_class", "access_level",
            "verified_fields", "verified_via"]
TYPES = {"book", "journal-article", "conference-paper", "report", "web-guide", "standard",
         "blog-post", "magazine-article"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def run() -> int:
    rep = Report("references")
    entries = load_bibliography()
    if not entries:
        rep.error("research/bibliography.yaml is missing or empty")
        return rep.finish()

    by_id: dict[str, dict] = {}
    for i, e in enumerate(entries):
        label = e.get("id", f"entry #{i}") if isinstance(e, dict) else f"entry #{i}"
        if not isinstance(e, dict):
            rep.error(f"{label}: not a mapping")
            continue
        for key in REQUIRED:
            if key not in e:
                rep.error(f"{label}: missing key '{key}'")
        if "id" in e:
            if not ID_RE.match(str(e["id"])):
                rep.error(f"{label}: id must be lowercase letters, digits, and hyphens")
            if e["id"] in by_id:
                rep.error(f"{label}: duplicate id")
            by_id[e["id"]] = e
        if e.get("type") not in TYPES:
            rep.error(f"{label}: type '{e.get('type')}' not in {sorted(TYPES)}")
        if e.get("evidence_class") not in EVIDENCE_CLASSES:
            rep.error(f"{label}: evidence_class '{e.get('evidence_class')}' invalid")
        if e.get("access_level") not in ACCESS_LEVELS:
            rep.error(f"{label}: access_level '{e.get('access_level')}' invalid")
        if not isinstance(e.get("authors"), list) or not e.get("authors"):
            rep.error(f"{label}: authors must be a non-empty list")
        if not isinstance(e.get("verified_fields"), list):
            rep.error(f"{label}: verified_fields must be a list")
        if not isinstance(e.get("verified_via"), list):
            rep.error(f"{label}: verified_via must be a list")
        if e.get("verified_fields") and not e.get("verified_via"):
            rep.error(f"{label}: has verified_fields but no verified_via URL")
        if not (e.get("url") or e.get("doi") or e.get("isbn13")):
            rep.error(f"{label}: needs at least one of url, doi, isbn13")
        year = e.get("year")
        if year is not None and not (isinstance(year, int) and 1900 <= year <= 2100):
            rep.error(f"{label}: year '{year}' is not a plausible integer")
        for claim in e.get("claims") or []:
            if not isinstance(claim, dict) or "text" not in claim or "basis" not in claim:
                rep.error(f"{label}: each claim needs 'text' and 'basis'")

    unverified = {i for i, e in by_id.items() if not e.get("verified_fields")}

    for ch in iter_chapters():
        for sid in ch.sources:
            if sid not in by_id:
                rep.error(f"curriculum.yaml {ch.id}: source id '{sid}' not in bibliography")

    cited_anywhere: set[str] = set()
    for md in sorted(DOCS.rglob("*.md")):
        if md.name == "bibliography.md" and md.parent.name == "references":
            continue
        for sid in CITATION_RE.findall(md.read_text(encoding="utf-8")):
            cited_anywhere.add(sid)
            if sid not in by_id:
                rep.error(f"{rel(md)}: citation to unknown id '{sid}'")

    parts_with_published: dict[int, int] = {}
    for ch in iter_chapters("live"):
        if not ch.path.is_file():
            continue
        cited = set(CITATION_RE.findall(ch.path.read_text(encoding="utf-8")))
        parts_with_published[ch.part_number] = parts_with_published.get(ch.part_number, 0) + len(cited)
        if len(cited) < MIN_CITED:
            rep.error(f"{ch.id}: cites {len(cited)} distinct sources, minimum is {MIN_CITED}")
        known = [by_id[s] for s in cited if s in by_id]
        if known and all(e.get("evidence_class") == "practitioner" for e in known):
            rep.error(f"{ch.id}: every cited source is practitioner opinion")
        for sid in sorted(cited & unverified):
            rep.error(f"{ch.id}: cites '{sid}', which has no verified fields")
    for part, n in parts_with_published.items():
        if n == 0:
            rep.error(f"part {part} has published chapters but no citations")

    for sid in sorted(unverified):
        rep.warn(f"bibliography entry '{sid}' has no verified fields")
    uncited = sorted(set(by_id) - cited_anywhere)
    rep.note(f"{len(by_id)} bibliography entries; {len(cited_anywhere)} cited in docs; "
             f"{len(uncited)} not yet cited")
    return rep.finish()


if __name__ == "__main__":
    main_guard(run)

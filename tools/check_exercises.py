#!/usr/bin/env python3
"""Exercise and solution checks for published chapters.

- the Exercises section has the three levels, in order, each with at least one exercise
- exercise ids are F1.., A1.., X1.. (bold, at the start of a paragraph), unique and sequential
- each exercise is substantive (MIN_EXERCISE_WORDS) and does not just ask for a definition
- no answer text hides in the chapter (no "Solution:" / "Answer:" lines in the Exercises section)
- docs/solutions/chNN-solutions.md exists and has a "## <id>" section for every exercise,
  each at least MIN_SOLUTION_WORDS long, and no solution for an exercise that does not exist
"""
from __future__ import annotations

import re

from booklib import (
    EXERCISE_LEVELS,
    Report,
    headings,
    iter_chapters,
    main_guard,
    rel,
    section,
    word_count,
)

MIN_EXERCISE_WORDS = 40
MIN_SOLUTION_WORDS = 120
MIN_PER_LEVEL = {"F": 2, "A": 2, "X": 1}
EX_RE = re.compile(r"^\*\*([FAX])(\d+)\.\*\*\s", re.M)
RESTATE_RE = re.compile(
    r"^\*\*[FAX]\d+\.\*\*\s+(define|what is|list the|name the|state the definition)\b", re.I
)


def run() -> int:
    rep = Report("exercises")
    total = 0
    for ch in iter_chapters("live"):
        if not ch.path.is_file():
            rep.error(f"{ch.id}: chapter file missing")
            continue
        text = ch.path.read_text(encoding="utf-8")
        ex = section(text, "Exercises")
        if ex is None:
            rep.error(f"{ch.id}: no '## Exercises' section")
            continue
        if re.search(r"^\s*\**(solution|answer)s?\**\s*:", ex, re.I | re.M):
            rep.error(f"{ch.id}: Exercises section appears to contain answers")

        level_titles = [t for lvl, t, _ in headings(ex) if lvl == 3]
        expected = [name for name, _ in EXERCISE_LEVELS]
        if level_titles != expected:
            rep.error(f"{ch.id}: exercise levels are {level_titles}, expected {expected}")
            continue

        ids: list[str] = []
        for name, prefix in EXERCISE_LEVELS:
            body = section(ex, name, level=3) or ""
            found = [(m.group(1), int(m.group(2)), m.start()) for m in EX_RE.finditer(body)]
            if any(p != prefix for p, _, _ in found):
                rep.error(f"{ch.id}: level '{name}' contains exercises with the wrong prefix")
            nums = [n for p, n, _ in found if p == prefix]
            if nums != list(range(1, len(nums) + 1)):
                rep.error(f"{ch.id}: {prefix} exercises are not numbered sequentially: {nums}")
            if len(nums) < MIN_PER_LEVEL[prefix]:
                rep.error(f"{ch.id}: level '{name}' has {len(nums)} exercise(s), "
                          f"minimum is {MIN_PER_LEVEL[prefix]}")
            for idx, (p, n, start) in enumerate(found):
                end = found[idx + 1][2] if idx + 1 < len(found) else len(body)
                chunk = body[start:end]
                ex_id = f"{p}{n}"
                ids.append(ex_id)
                if word_count(chunk) < MIN_EXERCISE_WORDS:
                    rep.error(f"{ch.id} {ex_id}: only {word_count(chunk)} words; "
                              f"exercises must set up a situation (min {MIN_EXERCISE_WORDS})")
                if RESTATE_RE.match(chunk.strip()):
                    rep.error(f"{ch.id} {ex_id}: asks the reader to restate a definition")
        total += len(ids)

        if not ch.solutions_path.is_file():
            rep.error(f"{ch.id}: solutions file missing ({rel(ch.solutions_path)})")
            continue
        sol_text = ch.solutions_path.read_text(encoding="utf-8")
        sol_ids = [t.split()[0].rstrip(".:") for lvl, t, _ in headings(sol_text) if lvl == 2]
        sol_ids = [s for s in sol_ids if re.fullmatch(r"[FAX]\d+", s)]
        for ex_id in ids:
            if ex_id not in sol_ids:
                rep.error(f"{ch.id} {ex_id}: no solution section '## {ex_id}'")
                continue
            title = next(
                t for lvl, t, _ in headings(sol_text)
                if lvl == 2 and t.split()[0].rstrip(".:") == ex_id
            )
            body = section(sol_text, title) or ""
            if word_count(body) < MIN_SOLUTION_WORDS:
                rep.error(f"{ch.id} {ex_id}: solution has {word_count(body)} words "
                          f"(min {MIN_SOLUTION_WORDS})")
        for s in sol_ids:
            if s not in ids:
                rep.error(f"{ch.id}: solution '{s}' has no matching exercise")
        if len(sol_ids) != len(set(sol_ids)):
            rep.error(f"{ch.id}: duplicate solution ids")

    rep.note(f"{total} exercises checked across published chapters")
    return rep.finish()


if __name__ == "__main__":
    main_guard(run)

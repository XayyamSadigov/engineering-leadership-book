# Project status

Last updated: 2026-11-20 (end of session 3: wave 2).

**Summary.** 17 of 60 chapters are written and on the site in `review` status: Part I (chapters 1–4),
Part IV (15–18), and Part V (19–27). Each passed automated validation and an independent cross-chapter
review; none has had human review. **43 chapters, 16 templates, 8 projects, and the capstone are not
written.** Nothing has been committed to git; the GitHub repository does not exist yet.

## Completed

| Area | State |
|---|---|
| Chapters | 1–4, 15–27, each with a solutions file (136 exercises). Status `review` |
| Templates | Engineering quality scorecard, technical debt register, incident review, 90-day quality plan. Status `review` |
| Bibliography | 179 entries (61 scholarly, 16 industry research, 8 standards, 8 official documentation, 86 practitioner); 178 verified |
| Research documents | research plan, reference analysis, source evaluation, evidence matrix (chapters 1–4, 15–27), research gaps (24 open, 2 closed), disputed claims (D1, D4, D6 positions taken), human review checklist, quality report |
| Northstar canon | `index.md`; `baseline-data.md` with extended baseline (standards, debt, tests and pipeline, reliability, incidents, security, management and roles, planning and delivery); `first-quarter.md` (decisions incl. renewal dates, timeline, day 90, starting points for quarter 2); three CSV files |
| Single-file edition | `dist/ENGINEERING_LEADERSHIP_HANDBOOK.md`, about 167,000 words |

## Validation results (2026-11-20)

- `python tools/validate_book.py --build`: **passed**; 1 warning (unverified, uncited Prime Video entry).
- `tools/render_diagrams.py`: 48 of 48 render. Diagrams of chapters 1–4 and 15–18 measured at 390 px.
- `ruff check tools`: clean.
- GitHub Actions have **not** run (no repository).

## How each wave runs (repeat this)

1. Shared brief (scratchpad copy of the wave 2 brief is the template: contract, research rules, legal
   sources only, topic lane for invented facts, no new first-quarter events, validation command) plus a
   per-chapter lane naming what the chapter owns and what it must leave to other chapters.
2. Eight authors in parallel, each writing only its chapter, solutions, and side files
   (`research/pending-sources/`, `research/northstar-additions/`, `research/evidence-matrix-chNN.md`).
   Watch messages: settle shared facts (dates, characters) as canon immediately and tell the affected
   authors.
3. Maintainer merges: dedupe sources by URL as well as id; read all Northstar additions, resolve
   conflicts, write them into the canon pages; integrate status and nav; merge evidence matrices;
   update gaps and disputes; validate; measure diagrams at 390 px.
4. Independent reviewer reads the new chapters against the canon, each other, and earlier parts.
5. Maintainer fixes the canon first, then parallel fixers on disjoint files; validate again.

## Next concrete tasks, in order

1. **Human review** (priorities in `research/quality-report.md`).
2. **Create the GitHub repository**, first commit, enable Pages (source: GitHub Actions).
3. **Wave 3: Parts II and III** (chapters 5–14, ten chapters; run as two groups of five or one wave of
   ten). Chapter 7 needs gap G10 (structured interview validity, Sackett et al. 2022) closed first;
   chapter 14 owns remote work (disputed claim D5).
4. **Project 3** (quality transformation plan): dataset, rubric, worked solution.
5. Wave 4: Parts VII and VIII (33–39) with templates t07, t13, t14. Wave 5: Parts IX and X (40–46).
   Wave 6: Parts XI and XII (47–55). Wave 7: Part VI (28–32). Wave 8: Part XIII (56–59), remaining
   templates and projects, capstone (60).
6. Backlog: PDF and EPUB builds; external link checker; a script that recomputes Northstar aggregates
   from the CSVs during validation; convert plain-text references to now-live chapters into links.

## How to resume

Read `CLAUDE.md`, then this file, then run `.venv/bin/python tools/validate_book.py --build`.

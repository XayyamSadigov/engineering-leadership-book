# Project status

Last updated: 2026-11-20 (session 3: waves 2 and 3, first GitHub publication).

**Summary.** 27 of 60 chapters (Parts I–V, chapters 1–27) are written and on the site in `review`
status. Each passed automated validation and an independent cross-chapter review; none has had human
review. **33 chapters, 16 templates, 8 projects, and the capstone are not written.**

Published at https://github.com/XayyamSadigov/engineering-leadership-handbook (public) with the site at
https://xayyamsadigov.github.io/engineering-leadership-handbook/. Both workflows passed on the first
push. Commits use the GitHub noreply address (repository-local git config), never the work email. A
GitHub token is stored in the macOS keychain for `git push` and API calls; the user was advised to
replace it with a repository-scoped fine-grained token.

## Completed

| Area | State |
|---|---|
| Chapters | 1–27, each with a solutions file (216 exercises). Status `review` |
| Templates | Engineering quality scorecard, technical debt register, incident review, 90-day quality plan. Status `review` |
| Bibliography | 242 entries (105 scholarly); 241 verified |
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
   Verify every arithmetic finding yourself before handing it to fixers (a wrong reviewer "fix" was
   applied once and had to be reverted).
6. Commit (noreply author, no AI attribution) and push; check both workflows.
5. Maintainer fixes the canon first, then parallel fixers on disjoint files; validate again.

## Next concrete tasks, in order

1. **Human review** (priorities in `research/quality-report.md`).
2. **Wave 4: Part VI (28–32) and Part VII (33–36)**, nine chapters. Chapter 28 owns disputed claim D7
   and ADRs; chapter 31 owns D3 (microservices) and gap G11 (Prime Video source).
3. **Project 3** (quality transformation plan): dataset, rubric, worked solution.
4. Wave 5: Parts VIII and IX (37–43) with templates t03, t04, t07, t13, t14. Wave 6: Parts X and XI
   (44–49). Wave 7: Part XII (50–55). Wave 8: Part XIII (56–59), remaining templates and projects,
   capstone (60).
6. Backlog: PDF and EPUB builds; external link checker; a script that recomputes Northstar aggregates
   from the CSVs during validation; convert plain-text references to now-live chapters into links.

## How to resume

Read `CLAUDE.md`, then this file, then run `.venv/bin/python tools/validate_book.py --build`.

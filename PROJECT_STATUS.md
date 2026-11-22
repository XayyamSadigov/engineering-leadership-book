# Project status

Last updated: 2026-11-20 (session 3: waves 2–6).

**Summary.** 49 of 60 chapters (Parts I–XI, chapters 1–49), 13 of 20 templates, and five of eight projects are written and on the site in `review`
status. Each passed automated validation and an independent cross-chapter review; none has had human
review. **11 chapters (50–60, including the capstone), 7 templates, and 3 projects are not written.**

Published at https://github.com/XayyamSadigov/engineering-leadership-book (public) with the site at
https://xayyamsadigov.github.io/engineering-leadership-book/. Both workflows passed on the first
push. Commits use the GitHub noreply address (repository-local git config), never the work email. A
GitHub token is stored in the macOS keychain for `git push` and API calls; the user was advised to
replace it with a repository-scoped fine-grained token.

## Completed

| Area | State |
|---|---|
| Chapters | 1–49, each with a solutions file (392 exercises). Status `review` |
| Templates | t03 EM rubric, t04 director matrix, t07 org design assessment, t08 quality scorecard, t09 debt register, t10 incident review, t13 quarterly review, t14 capacity model, t15 engineering strategy, t16 technology investment business case, t17 stakeholder map, t18 executive update, t20 90-day plan. Status `review` |
| Projects | P1 management operating system, P3 quality transformation plan, P4 redesign of an 80-engineer organization, P5 delivery and reliability scorecard, P6 manager development and succession, each with a worked solution. Status `review` |
| Bibliography | 358 entries, all verified |
| Research documents | research plan, reference analysis, source evaluation, evidence matrix (chapters 1–49), research gaps (47 open, 3 closed), disputed claims D1–D8 (positions taken on all), human review checklist, quality report |
| Northstar canon | `index.md`; `baseline-data.md` with extended baseline (standards, debt, tests and pipeline, reliability, incidents, security, management and roles, planning and delivery, locations, people, hiring, levels and pay, architecture and estate, dependency causes); `first-quarter.md` (decisions incl. renewal dates, timeline, day 90, starting points for quarter 2, quarter 2 results, quarter 3 plan and results, quarter 4 events weeks 40–52, year-2 proposal; counting rules for Core change failure rate, the tier 1 list, and quarter length); `halvard.md` (Halvard Systems, the 500-engineer comparison company); three CSV files |
| Single-file edition | `dist/ENGINEERING_LEADERSHIP_HANDBOOK.md`, about 480,000 words |

## Validation results (2026-11-20)

- `python tools/validate_book.py --build`: **passed**, no warnings.
- `tools/render_diagrams.py`: 135 of 135 render. Diagrams of chapters 1–18 and 28–49 measured at 390 px; chapters 19–27 checked visually.
- `ruff check tools`: clean.
- GitHub Actions: both workflows pass on every push.

## How each wave runs (repeat this)

1. Shared brief (scratchpad copy of the wave 2 brief is the template: contract, research rules, legal
   sources only, topic lane for invented facts, no new first-quarter events, validation command) plus a
   per-chapter lane naming what the chapter owns and what it must leave to other chapters.
2. Eight to ten authors in parallel, each assigned one Northstar team, each writing only its chapter, solutions, and side files
   (`research/pending-sources/`, `research/northstar-additions/`, `research/evidence-matrix-chNN.md`).
   Watch messages: settle shared facts (dates, characters) as canon immediately and tell the affected
   authors.
3. Maintainer merges: dedupe sources by URL as well as id; read all Northstar additions, resolve
   conflicts, write them into the canon pages; integrate status and nav; merge evidence matrices;
   update gaps and disputes; validate; measure diagrams at 390 px.
4. Independent reviewer reads the new chapters against the canon, each other, and earlier parts.
   Verify every arithmetic finding yourself before handing it to fixers (a wrong reviewer "fix" was
   applied once and had to be reverted).
5. Maintainer fixes the canon first, then parallel fixers on disjoint files; validate again.
6. Commit (noreply author, no AI attribution) and push; check both workflows.
7. Never change a decision already sent to parallel authors while they are working: messages arrive
   late and each reversal creates a new round of divergence. Decide once, early. When authors share a
   fact (a calendar, a count), name its owner chapter in the brief and send one FINAL rule to all of
   them if they diverge.
8. Hand review fixes back to the original authors (they keep their context) on disjoint files; give
   findings in earlier chapters to the author with the fewest findings. After merging, tell authors
   which of their proposed facts are now canon, so they stop labeling them as additions.

## Next concrete tasks, in order

1. **Human review** (priorities in `research/quality-report.md`).
2. Wave 7: Part XII (50–55) with t05 (CTO matrix), t11 (risk register), t12 (ADR), P7, P8.
   Open canon decisions to leave open or decide deliberately: the year-2 organization proposal (week
   46), the VP question (week 48), the quality continuation proposal (week 51), the workforce plan, the
   week 34 portfolio forum, the CI target, ADR-0001. Quarter 4 results are not recorded.
3. Wave 8: Part XIII (56–59), t01, t02, t06, t19, P2, capstone (60).
4. Waves of nine agents reach the 5-hour usage limit; resume agents with SendMessage after the reset.
5. Backlog: PDF and EPUB builds; external link checker; a script that recomputes Northstar aggregates
   from the CSVs during validation; convert plain-text references to now-live chapters into links.

## How to resume

Read `CLAUDE.md`, then this file, then run `.venv/bin/python tools/validate_book.py --build`.

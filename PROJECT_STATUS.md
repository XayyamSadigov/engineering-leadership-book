# Project status

Last updated: 2026-11-23 (session 5: readability program phases 1–5, Russian edition started).

**Summary.** The book is fully drafted: all 60 chapters (including the capstone), all 24 templates, and
all 8 projects are written and on the site in `review` status. Each passed automated validation and an
independent cross-chapter review; none has had human review, so nothing is `published`.

Published at https://github.com/XayyamSadigov/engineering-leadership-book (public; renamed from engineering-leadership-handbook on 2026-11-22, the old Pages URL does not redirect) with the site at
https://xayyamsadigov.github.io/engineering-leadership-book/. Both workflows passed on the first
push. Commits use the GitHub noreply address (repository-local git config), never the work email. A
GitHub token is stored in the macOS keychain for `git push` and API calls; the user was advised to
replace it with a repository-scoped fine-grained token.

## Completed

| Area | State |
|---|---|
| Chapters | 1–60, each with a solutions file. Status `review` |
| Templates | t03 EM rubric, t04 director matrix, t07 org design assessment, t08 quality scorecard, t09 debt register, t10 incident review, t13 quarterly review, t14 capacity model, t15 engineering strategy, t16 technology investment business case, t17 stakeholder map, t18 executive update, t20 90-day plan, t05 CTO matrix, t11 risk register, t12 ADR, t01 one-on-one, t02 career development plan, t06 team health assessment, t19 leadership succession plan (all 20). Status `review` |
| Projects | All eight: P1 management operating system, P2 diagnose a low-performing team, P3 quality transformation plan, P4 redesign of an 80-engineer organization, P5 delivery and reliability scorecard, P6 manager development and succession, P7 12-month engineering strategy, P8 CTO technology investment proposal, each with a worked solution. Status `review` |
| Bibliography | 447 entries, all verified |
| Research documents | research plan, reference analysis, source evaluation, evidence matrix (all chapters, templates, projects), research gaps (60 open, 3 closed), disputed claims D1–D10 (positions taken on all), human review checklist, quality report |
| Northstar canon | `index.md`; `baseline-data.md` with extended baseline (standards, debt, tests and pipeline, reliability, incidents, security, management and roles, planning and delivery, locations, people, hiring, levels and pay, architecture and estate, dependency causes); `first-quarter.md` (decisions incl. renewal dates, timeline, day 90, starting points for quarter 2, quarter 2 results, quarter 3 plan and results, quarter 4 events weeks 40–52, year-2 proposal; counting rules for Core change failure rate, the tier 1 list, and quarter length; Part XII facts: the CTO's week, the three-year strategy draft, FY1 financial statements and capitalization policy, risk and SOC 2 status, data and AI, board preparation); executive and board context in `index.md`; `halvard.md` (Halvard Systems, the 500-engineer comparison company, with named product groups and the Part XIII stories: Payroll's recovery, the Commerce outage, the Field Operations reduction, the Corvane acquisition, the platform budget cut); three CSV files |
| Single-file edition | `dist/ENGINEERING_LEADERSHIP_HANDBOOK.md`, about 640,000 words |

## Validation results (2026-11-22)

- `python tools/validate_book.py --build`: **passed**, no warnings.
- `tools/render_diagrams.py`: 171 of 171 render (run with `npx -y -p @mermaid-js/mermaid-cli@11.4.2 sh -c '.venv/bin/python tools/render_diagrams.py'`). Diagrams of chapters 1–18 and 28–49 measured at 390 px; chapters 19–27 checked visually; chapters 50–55, templates, and projects 7–8 measured from rendered SVG widths (scale at 390 px 0.44–1.00, within the range already accepted for chapters 44–49, minimum 0.39); the two widest checked visually. Wave 8 diagrams scale 0.39–1.00, the widest checked visually.
- `ruff check tools`: clean.
- GitHub Actions: both workflows pass on every push.

## How each wave runs (repeat this)

1. Shared brief (`research/wave-brief.md` is the template; replace section 6 per wave: contract, research rules, legal
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

1. **Human review** (priorities in `research/quality-report.md`). Only a person moves an item to
   `published`, recorded in the quality report.
2. Decide the length question: chapters 50–60 run 5,500–7,900 counted words against the 5,000-word
   guide. If they must be cut, cut with the original structure intact (Enterprise Application, Trade-offs,
   and Deep Conceptual Explanation are the usual places).
3. Backlog: PDF and EPUB builds; external link checker; a script that recomputes Northstar aggregates
   from the CSVs during validation; convert remaining plain-text references to chapters into links;
   reread the canon pages as a whole (they grew by appending wave sections) and consider splitting
   `first-quarter.md`, which now carries year 1 through quarter 4 and Part XII facts.

## How to resume

Read `CLAUDE.md`, then this file, then run `.venv/bin/python tools/validate_book.py --build`.

## Readability program (2026-11-22 to 2026-11-23)

- Phases 1–4 done: glossary (96 terms), cast, timeline, quarter 4 briefing, restructured case pages, front
  matter (aa91ba1); reader rules and assessor fixes in all chapters, templates, projects (1698647); missing
  content, four new templates t21–t24, eight new sources (1ec4681). Maintainer bookkeeping in reader text
  399 → 0, now a validator error (`BOOKKEEPING_IS_ERROR = True`).
- Phase 5 re-assessment, same rubric, reports in `research/readability/round2/`: book averages readability
  3.57, clarity 4.28, completeness 4.02, Northstar load 3.33 (round 1: 3.5 / 4.2 / 3.9 / 3.0); book level
  3.6 / 4.0 / 4.0 / 3.4. 45 of 60 chapters still have a score below 4. Target (4.5, none below 4) not met.
- Open decision for the user: option A (targeted fixes), B (A plus trimming each case study to the 5–8 facts
  it needs, a prose "year in brief" page, one engineer-cost rate book-wide, glossary terms for the CTO
  chapters), or C (stop). Summary of findings in `research/readability-assessment.md`, "Round 2".
- In flight: EPUB/PDF pipeline (`tools/build_ebooks.py`, `tools/ebook/`), not yet committed.

## Russian edition, started 2026-11-23

- Infrastructure: `mkdocs-static-i18n==1.3.1`, suffix mode (`page.ru.md` beside `page.md`), Russian under
  `/ru/`, English fallback for untranslated pages, Russian nav translations and site name in `mkdocs.yml`,
  Russian announcement in `overrides/main.html`. Plugin pinned in both workflows, `pyproject.toml`, README.
- `mkdocs.yml` also gained `exclude_docs: !/templates/`: MkDocs always excluded `docs/templates/`, so the
  template library had never been published on the site.
- Validators skip `*.ru.md` for English checks (`booklib.is_translation`); links from Russian pages are
  anchor-checked against the Russian target when one exists.
- Term base and style guide: `research/translation-ru-glossary.md` (binding for translators).
- Translated: index, about, how-to-use, learning-roadmaps, glossary, references/evidence-labels, and all
  seven Northstar pages. Every Russian heading carries the English anchor (`{ #english-slug }`).
- Next: translate chapters, solutions, templates, and projects once their rewrites settle; re-sync the
  translated pages whenever their English sources change (record lags in the term base, section 5).

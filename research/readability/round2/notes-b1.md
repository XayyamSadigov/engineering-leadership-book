# Lane b1 notes: book-level reader aids (round 2)

Scope: Northstar pages (EN and RU), glossary (EN and RU), index, about, how-to-use, learning-roadmaps
(EN and RU), mkdocs.yml, tools/build_curriculum.py. No facts changed; no new case facts.

## Against report a9

| Finding | Status | What was done |
|---|---|---|
| P1 year in brief | done | New `case-studies/northstar/year-in-brief.md` (about 1,150 prose words, four quarter sections, no tables, at most five figures per section) and `.ru.md`. Nav entry after "Company and organization" (RU «Год вкратце»). Linked from index.md, how-to-use.md, learning-roadmaps.md, the Northstar overview's "How to use these pages" box, the timeline, the quarter 4 briefing, and the year 1 record. |
| P1/P12 year 1 record | done | `first-quarter.md` nav entry and H1 now "Year 1 record (reference)" / "Northstar: year 1 record (reference)"; first line says it is a lookup page and points to the year in brief; "so that the chapters agree with each other" removed. All references in owned files say "the year 1 record" (RU «хроника года 1»). File not renamed. Chapters, templates, and projects that still say "first quarter page" or "first-year record" are outside this lane. |
| P2 rates (decision 3) | done in owned files | Glossary engineer-time entry rewritten to the single planning rate; warning cut to one sentence. $800 labeled as Finance's day rate (with the working-days explanation) in the year 1 record's TR-01 row and the quarter 4 briefing. |
| P3 glossary | done | Added: Budget envelope, Operating plan, Run-rate, Value channel and urgency profile, Seat, Velocity and story points, Cycle time, Quality engineer, Re-rating, Severity audit, CISO, Attrition and regretted attrition, Requisition, Vesting, Dependency link, Stock and flow, Reinforcing and balancing loops, Leverage point, Estate, Board pack, Due diligence, Warranty, indemnity, and escrow, Deployable unit, Top-40 customers, Register IDs (INC, DL, ADR, TD, TR, ER). A–Z index at the top (EN and RU). "Incident review" is now the main entry (postmortem and blameless review named as alternatives); "Blameless review" kept as a short pointer so the old anchor still resolves. "Change failure rate" mentions DORA's "change fail rate" once; the DORA metrics entry now says change failure rate. All 17 anchors in brief decision 5 checked in the built HTML, EN and RU. |
| P4 quarter 4 briefing | done | Leads with "The three decisions that drive quarter 4" (year-2 organization, quality continuation, board headline), one paragraph each with stakes; other nine rows in "Other open items" with one plain sentence of what is at stake. Stage names, gates (incl. the week 78 gate), the 87-seat rule (glossary: seat), TR-01 (register IDs), ADR-0001, requisition, budget envelope, and board pack are defined or linked. |
| P5 Chapter 26 | done | Path B order 3 is "19, 21, 22, 23, 26"; B is 15 chapters, about 15/20 weeks, in learning-roadmaps.md and index.md (EN and RU). "(Chapter 26 also helps)" removed from the Path C project table. |
| P6 counts | done | index.md Part XIV row now 24 templates; full-climb length sentence added (59 chapters plus capstone). about.md "an notice" fixed. build_curriculum.py: status line "All 60 chapters are on the site; none has yet completed human review" (computed, with fallbacks), Part XIV row counts templates (24 of 24 templates), project table linked. `ruff check tools` clean. |
| P7 nav grouping | done (nav only) | Templates nav grouped under Your team, Engineering system, Organization and operating system, Executive (RU translations added). `docs/templates/index.md` ("Available now", flat table) is outside this lane. |
| P11 cast | done | Box "The people who drive the story" at the top of cast.md (EN and RU); the rest marked as mattering in only a few chapters (not "one or two", because Helena Marsh and Sofia Alvarez appear in five). |
| Maintainer additions | done | Systems-thinking entries (stock and flow; loops; leverage point), Estate, Top-40 customers, Re-rating, Severity audit, Dependency link, consistent with the inline definitions in Ch 3, 33/34, 53, 55. |

Also: nav translation added for "Download (EPUB, PDF)", which had none.

## Word counts

year-in-brief.md 1,221 (with markup); quarter-4-briefing.md 1,053 to about 1,430; glossary.md 5,058 to
about 7,000; cast.md 1,518 to about 1,640.

## For the maintainer

- `research/translation-ru-glossary.md` (not in this lane) needs the new renderings: «Год вкратце»
  (the year in brief), «хроника года 1» (the year 1 record), «рамки бюджета» (budget envelope),
  «операционный план», «годовой темп» (run-rate), «место» (seat), «заявка на найм» (requisition),
  «вестинг», «канал ценности», «профиль срочности», «инженер по качеству», «переоценка серьёзности»,
  «аудит серьёзности», «связь зависимости», «запас и поток», «усиливающая/балансирующая петля»,
  «точка рычага», «технологический ландшафт» (estate), «пакет для совета директоров» (board pack),
  «разбор инцидента» (incident review, now the main term), «развёртываемая единица», nav headings
  «Ваша команда», «Инженерная система», «Организация и операционная система», «Высшее руководство».
- The dist single-file edition is stale (other lanes are editing chapters); regenerate after merge.
- The year 1 record still carries "(a gap Project 4 asks the learner to find)" in the year-2 proposal
  table; left in place as reader-facing, but it is a spoiler for P4 if you prefer to cut it.
- No fact questions arose.

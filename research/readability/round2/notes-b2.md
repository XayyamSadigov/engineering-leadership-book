# Round 2 notes, lane b2 (templates, projects, project solutions)

Validation: `.venv/bin/python tools/validate_book.py` passes except the stale single-file edition.
Word counts (templates, projects, project solutions, excluding `.ru.md`): 97,272 before, about 100,900 after.
Most of the increase comes from the one-row-per-fact sheets and the 20 new "Minimum version" boxes.

## Findings from a9-book-level.md

| Finding | Status | What changed |
|---|---|---|
| P2 (one rate) | done | Business case: the two-rate table is replaced by one rate, $3,558 an engineer-week; phase 1 is now 12 × $3,558 = about $42,700 (was $48,000 at $4,000). Full consolidation is priced as 2 engineer-years × $185,000 = $370,000. The "92 engineer-weeks" (46 working weeks a year, from Ch 32) is dropped from the template so it no longer implies a second weekly rate. NPV, payback, CD3, and the break-even are unchanged because they rest on $185,000 a year and $3,558 a week. Risk register: $800 is labeled Finance's day rate at first use, with the reason it is higher. P8: the fact sheet row labels it the same way; step 2's caution is now one sentence. P8 solution: conventions row and C2 row relabeled; the figures were rechecked ($85,385 / $135,192 / $172,904 at $3,558; $96,000 / $152,000 / $194,400 at $800; $4,000 ÷ $3,558 = 1.124, so "about 12 percent" holds) |
| P7 (template index) | done | Four groups as specified; "Available now" deleted; all 24 files checked against the groups; one line added about the Minimum version box |
| P8 (Minimum version) | done | Added to the 20 templates that lacked one, placed before "How to fill it in" as in one-on-one.md |
| P9 (fact sheets) | done | P1 to P8: each "Facts your submission must use" table is now a "Project fact sheet", one row per fact (fact, value, week, source). Each time rule is shortened and now points to the sheet. Only facts already in the projects or case pages are used. Where a case page gives no exact week, the row says "By week N" or "Year 1" and invents no date. Sources were corrected where my first guess was wrong (P4 co-change is Ch 35; P6 skip-level counts are Ch 41; P6 week 22 expectations and P4 health check are the year 1 record). The projects index mentions the sheets |
| P10 (capacity model labels) | done | Rows are now "Quarter 2 measured", "Quarter 3 plan (measured: 25%)", and "Quarter 4 plan (not measured)". The quarter 3 team table is labeled as the plan and says measured came in at 25 percent |
| P12 (page names) | done in my files | "the year 1 record" now replaces "first-year record", "quarter 4 record", and "the first quarter (page)" in the templates, P1 and P3 to P8, and the P3 solution |
| P13 / P14 | done in my files | No "change fail rate" was found. Incident-review template: the glossary link now covers only the word "blameless", used as an adjective, and the source's term "postmortems" is given once as their name. 90-day plan risk row: "blameless incident review" |
| P15 (17 units) | done | Business case box: "17 deployable units (Core counts as one; 24 components in all)", linked to `#deployable-unit` |
| Shorthand pattern | done | Weeks are explained at first use in each example. Register IDs (TR, ER, DL, TD) are linked to `#register-ids`, seats to `#seat`, and the continuation and the mandate to their glossary entries. Risk register: SOC 2 options A/B/C are spelled out. Executive update: "the forum" is defined. Business case: "fifth minimum" is replaced. Succession plan: "level 3" is defined (the Ch 2 delegation level: decides after telling the manager). CI, ARR, WIP, DORA, and KEV are expanded where they were bare |
| Decision 1 trims | done | Capacity model: the quarter 1 per-team table is cut to one sentence. The boxes in the career plan, team charter, and team health templates lose incident facts the template does not use. Template boxes now end with the year-in-brief and cast line (decision 2), and keep the timeline link |

## Maintainer item (technical-debt-register.md)

TD-004's decision now matches the year 1 record: automated pipeline checks are due week 7 and landed in week 11, after the week 9 repeat of INC-427. The quarter 2 timing was removed. A short paragraph after the table notes that Chapter 21 adds TD-006 (four CI systems) and TD-007 (flaky Core tests). The other entries were checked against Ch 21's figures (TD-001 principal 2 engineer-years; TD-002 36 engineer-days a year and 40 to move; TD-004 about 25 engineer-days): they are consistent.

## Fact questions for the maintainer

- Team charter: Li Na Zhou was "staff engineer, data and migration". I changed it to "data and integration" to match the cast and every other page.
- Business case: Ch 32 still says the consolidation is "about 92 engineer-weeks at 46 working weeks a year". This is a second weekly convention. Consider "about 2 engineer-years (104 engineer-weeks at the planning rate)" there. If so, "about 80 after phase 1" becomes about 92. I left Ch 32's figure alone (not my file), and the template's opportunity-cost line still says "about 80 engineer-weeks", quoting Ch 32.
- P7 and P8: Greg Tanaka's "4 FTE plus two engineers" alternative is sourced to Ch 49. The year 1 record mentions only the private offer of two engineers. Consider adding the 4-plus-2 option to the record.

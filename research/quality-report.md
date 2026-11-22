# Quality report

The state of the book's quality assurance: what automated validation shows, what has and has not been
reviewed by a person, and the known limitations a reader or reviewer should be aware of.

## Automated validation

Run `python tools/validate_book.py --build`. Last result recorded: **passed**, 2026-11-20, with
chapters 1–49, 13 templates, and projects 1 and 3–6 live (chapters, navigation, references, exercises, generated pages,
single-file edition, `mkdocs build --strict`). No warnings: all 358 bibliography entries are verified. Mermaid: 135 of 135 diagrams render with mermaid-cli 11.
All diagrams of chapters 1–4 and 15–18 measured in a headless browser at 390 px; one squeezed diagram
(chapter 2) fixed. `ruff check tools`: clean. Browser check of all nine Part V chapters at
390 px: no horizontal page overflow; six squeezed left-to-right diagrams redrawn top-to-bottom, and a
phone-width rule added to `CLAUDE.md` section 8.

## How Part V was produced

Chapters 19–26 were written in parallel by eight AI authors under a shared brief, each confined to its
own files (see `CLAUDE.md` section 6a). Each author verified new sources by fetching pages in session
and validated its chapter. The maintainer merged 64 new sources, consolidated Northstar facts into the
canon (`baseline-data.md` extended baseline, new `first-quarter.md`), and resolved conflicts between
authors. A separate AI reviewer, who had not written any chapter, then read all nine chapters against
the canon and the bibliography and reported 23 findings (2 counting errors, conflicting timelines for
two events, inconsistent tier 1 minimums, repetition between chapter 27 and the newer chapters, one
over-reach beyond a source's recorded claim). All 23 were fixed by four parallel fixers and the
maintainer; chapter 27 was cut from about 7,500 to 5,600 counted words.

## Wave 2 (chapters 1–4 and 15–18), 2026-11-20

Same procedure as wave 1, with a revised brief (stay in your topic lane for invented facts, do not
invent first-quarter events, read sources only from legitimate hosts). Authors coordinated directly on
shared facts (renewal dates, Rafael Duarte, a source sample size of 131 versus 214 firms); the
maintainer fixed the renewal dates as canon (accounting integration week 19, bulk ordering week 26)
and merged 44 sources, one duplicate source consolidated. An independent reviewer reported 20
findings (a numeric inconsistency in Priya Raman's time split, introduced by the maintainer's own canon
merge; a claimed one-on-one arithmetic error that was itself wrong, applied, and reverted after a
wave 3 author caught it (30 minutes every two weeks for 14 people is 3.5 hours a week); staff mandates contradicting chapter 27; two unsupported numbers
attributed to a metadata-only source; repetition of manager-effect studies across chapters 1, 2,
and 4). All 20 fixed.

## Wave 3 (chapters 5–14), 2026-11-20

Ten authors in parallel. New brief rules: each chapter assigned one Northstar team; Chapter 14 alone
decides locations, answering other authors on request. Authors resolved most shared facts directly
(names, Customer Experience leads, review cadence, who the script expert is). The maintainer resolved
a name collision (two authors used the same new name), a departures-by-team conflict, Tomasz
Wierzbicki's level, and the flat-headcount rule for promotions to manager. 63 sources merged (242 in
total), one duplicate consolidated. A wave 3 author caught a wrong arithmetic "fix" from the wave 2
review (one-on-one hours in chapter 2); it was reverted. The wave 3 reviewer reported 16 findings
(Bram Verhoeven's timeline placed in quarter 1, two arithmetic errors verified by the maintainer before
fixing, canon facts not merged, repetition of Edmondson, Lencioni, and Scullen et al.); all fixed.
Chapters 7, 9, and 10 end 3 to 15 words over the 5,000-word guide.

## Wave 4 (chapters 28–36), 2026-11-20

Nine authors in parallel. The maintainer changed the shared year-2 reorganization proposal while the
authors were working; messages crossed, and three chapters had to be realigned twice before a final
decision (Chapter 35's current version) was sent to all three. Lesson recorded in PROJECT_STATUS: a
decision sent to parallel authors is not changed in flight. 52 sources merged (293 in total, all
verified); the Prime Video post was read from an archived copy, closing gap G11. Disputed claims D3 and
D7 now have positions. The independent reviewer reported 21 findings (an exercise premise contradicting
the canon, a quarter-2 move that the canon defers to year 2, an Orders split that ignored the chapter
31 co-change data, two different hierarchies for the same 500-engineer example, repetition across
chapters 33–35); arithmetic in the key findings verified by the maintainer; all 21 fixed.

## Wave 5 (chapters 37–43, five templates, projects 3 and 4), 2026-11-20

Seven chapter authors, one templates author, one projects author. All nine hit the 5-hour usage limit
mid-work and were resumed with their context after it reset. Shared quarter-2 and quarter-3 facts (the
director's calendar, skip-levels, quarter-2 results, quarter-3 capacity) needed several rounds of
alignment; the maintainer sent one final rule per shared fact. 36 sources merged (329 in total, all
verified). The reviewer reported 30 findings (a wrong "needed by" date in the chapter 39 example; a lapsed
exemption shown as live in Project 4's data; Billing's pre-week-10 size used in quarter 3; contradictory
skip-level rules; templates written as if quarter-2 results did not exist; repetition of escalation and
skip-levels); the key arithmetic findings were verified by the maintainer; all 30 fixed.

## Wave 6 (chapters 44–49, four templates, projects 1, 5, 6), 2026-11-20

Six chapter authors, one templates author, one projects author. The authors coordinated shared facts
directly; the maintainer settled one conflict (Halvard's product group sizes) with a single final rule
and wrote the merged facts into the canon: quarter 3 results, quarter 4 events, a new `halvard.md`
page, and three counting rules (Core change failure rate windows, the year-1 tier 1 list, quarter
length) that resolved non-integer rates the projects author found. 29 sources merged (358 in total,
all verified). Two independent reviewers reported 48 findings (8 high): chapters set in quarter 4
still using quarter 2 as the latest quarter, the director's year-2 counter contradicting the
continuation proposal, the open VP question settled in passing, a headcount option not framed as an
exception to the 87-seat rule, and a year-2 criterion on the year-1 tier 1 list. Three issues in
earlier chapters (38, 39, 41 and the manager rubric) were confirmed and fixed. The maintainer verified
the reviewers' arithmetic before the fixes; all 48 findings were fixed by the original authors. Two
diagrams squeezed at 390 px (chapters 45 and 48) were redrawn.

## Wave 7 (chapters 50–55, templates t05 t11 t12, projects 7 and 8), 2026-11-22

Six chapter authors (the chapter 53 author also wrote t11), one templates author, one projects author,
working from a reusable brief now kept in `research/wave-brief.md`. The maintainer fixed the shared
Part XII facts in the canon before the authors started (board, ownership, IT under the CFO, week 50
meeting, Victor Lindqvist as CTO throughout Part XII, chapter 52 as sole owner of financial figures),
then merged about 90 proposed facts into a new "Part XII facts (quarter 4)" section of
`first-quarter.md`, correcting one (the week 42 AI-use survey is not the first developer survey). 58
sources merged (416 in total, all verified); gaps G51–G58 and disputes D9 (AI coding assistants) and D10
(three horizons) added. Two independent reviewers reported 50 findings (4 high): Project 8 treating
the new financial statements as non-canon and asking the board for cash Victor had ruled out, chapter
53 giving the corporate register three technology lines instead of one, and chapter 55 contradicting
the week 44 SBOM state. All high and medium findings were verified and fixed by the original authors;
three resolved by canon edits. 155 of 155 diagrams render. The six chapters run 5,500–7,400 counted
words, above the 5,000-word guide.

## Wave 8 (chapters 56–60, templates t01 t02 t06 t19, project 2), 2026-11-22

Five chapter authors (the chapter 56 author also wrote Project 2) and one templates author. Before
launch the maintainer fixed two canon decisions: nobody succeeds Victor Lindqvist as CTO (the capstone
puts the reader in his seat in quarter 4), and each author may add Halvard facts only inside one group.
At merge the maintainer caught a collision the lanes did not prevent (two Halvard groups with the same
field-service business and near-identical names) and had the fourth group renamed Payroll. Halvard's
three unnamed product groups are now named (Field Operations, Insights, Payroll), and a "Part XIII"
section records their stories, the Commerce outage, and the platform budget cut; Northstar gained one
quarter 4 fact (the rules inventory). 31 sources merged (447 in total); gaps G59–G63. Two independent
reviewers reported 38 findings (1 high): chapter 57 invented quarter 2 events around ADR-0001. Also
verified and fixed: a wrong binomial probability (chapter 56), "self-funding" claimed at 7.2 against
8 FTE (chapter 59), statutory thresholds not stated (chapter 58), capstone stages dated before their
inputs; three canon defects fixed (the stress rule's week, the redesign's dating, missing Halvard rows).
171 of 171 diagrams render; the wave 8 diagrams scale at 0.39–1.00 at 390 px. Chapters 56–60 run
6,300–7,900 counted words.

## Human review status

| Item | Status | Self-review | Human review |
|---|---|---|---|
| Chapters 56–60, templates t01 t02 t06 t19, project 2 | review | Author self-review; independent AI review (38 findings, all high and medium fixed) | **Not done** |
| Chapters 50–55, templates t05 t11 t12, projects 7 and 8 | review | Author self-review; independent AI review (50 findings, all high and medium fixed) | **Not done** |
| Chapters 37–43, templates t03 t04 t07 t13 t14, projects 3 and 4 | review | Author self-review; independent AI review (30 findings, all fixed) | **Not done** |
| Chapters 28–36 and solutions | review | Author self-review; independent AI review (21 findings, all fixed) | **Not done** |
| Chapters 5–14 and solutions | review | Author self-review; independent AI review (16 findings, all fixed) | **Not done** |
| Chapters 1–4 and 15–18 and solutions | review | Author self-review; independent AI review (20 findings, all fixed) | **Not done** |
| Chapters 19–26 and solutions | review | Author self-review against the checklist; independent AI cross-chapter review; fixes applied | **Not done** |
| Chapter 27 and solutions | review | As above; trimmed to remove re-teaching of chapters 18–25 | **Not done** |
| Templates t08, t09, t10, t20 | review | Northstar facts rechecked after canon changes | **Not done** |
| Northstar canon pages and data | canon | Aggregates recomputed from CSV; cross-chapter consistency checked by the reviewer | **Not done** |

| Chapter | Counted words | Diagrams | Distinct sources cited |
|---|---|---|---|
| 19 | 4,934 | 2 | 10 |
| 20 | 4,964 | 3 | 12 |
| 21 | 5,094 | 2 | 10 |
| 22 | 4,999 | 3 | 14 |
| 23 | 4,991 | 4 | 17 |
| 24 | 4,998 | 3 | 16 |
| 25 | 4,978 | 3 | 13 |
| 26 | 4,972 | 3 | 14 |
| 27 | 5,609 | 2 | 10 |

## Priorities for the human reviewer

1. Check a sample of findings against their sources, starting with the newest scholarly entries that
   carry specific numbers: `tornhill2022codered`, `ernst2015measure`, `luo2014flaky`,
   `inozemtseva2014coverage`, `just2014mutants`, `mcintosh2014impact`, `rigby2013convergent`,
   `besker2019productivity`, `mantyla2012who`, `decan2018impact`, `meli2019git`.
2. Re-check date-sensitive pages: DORA metrics guide (five metrics, January 2026), SLSA v1.2, NIST SSDF
   1.2 draft, CISA 2025 SBOM draft.
3. Read chapters 24 and 25 as a practicing engineering leader: they make the most specific operational
   recommendations (burn-rate alert parameters, severity definitions, action triage).
4. `allspaw2012blameless` and `mckinsey2023productivity` were read from Wayback Machine copies; `meyer1977institutionalized` from a
   third-party university copy (claims limited to its abstract). Confirm both are acceptable.
5. Decide whether chapter 21 (5,094), chapter 27 (5,609), and chapters 50–60 (5,500–7,900) may stay above the 5,000-word guide.
6. Part XII: check the accounting statements in chapter 52 (ASC 350-40, ASU 2025-06, IAS 38) and the SEC and AICPA statements in chapters 53 and 55 with someone qualified; check the AI-productivity figures in chapter 54 against the studies (D9).
7. Part XIII: have someone qualified check the employment-law statements in chapter 58 (WARN Act, EU Directive 98/59/EC, EEOC waiver guidance); read the capstone (chapter 60) end to end against Projects 1–8.

## Known limitations

- Most practitioner books are cited at idea level only; they were verified bibliographically and not
  read for this project. See `research/source-evaluation.md`.
- Most scholarly sources were read at abstract level only.
- SPACE and DevEx dimension names come from the first author's blog, a GitHub blog, and a vendor page, because the papers' publisher pages returned 403 (gap G5).
- Open research gaps are listed in `research/research-gaps.md` (G1, G3–G20).
- Drafting is AI-assisted throughout. The specific risk is confident prose that a source does not
  support; the citation rules, the independent review, and the human review exist for that reason.
- The GitHub repository named in `mkdocs.yml` does not exist yet; the site's repository widget returns
  404 until it does.

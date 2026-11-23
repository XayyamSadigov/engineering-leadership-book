# Readability, clarity, and completeness assessment (2026-11-22)

Nine independent assessors read the whole book as its target reader would (a strong engineer with no
management, finance, or psychology training), against one rubric (`research/readability/rubric.md`).
Eight read 5 to 10 chapters each in full; one assessed the book as a whole (front matter, navigation,
the Northstar pages, templates, projects, coverage, terminology). Their full reports, with line
numbers and concrete fixes, are in `research/readability/a1`–`a9`; text metrics per chapter are in
`research/readability/metrics.tsv`. Nothing was edited during the assessment.

## Scores (1 to 5)

| Part | Readability | Clarity | Completeness | Northstar load |
|---|---|---|---|---|
| I–II (Ch 1–10) | 3.5 | 4.5 | 3.7 | 3.3 |
| III–IV (Ch 11–18) | 3.8 | 4.2 | 3.9 | 3.2 |
| V (Ch 19–27) | 3.6 | 4.4 | 4.0 | 3.1 |
| VI–VII (Ch 28–36) | 3.7 | 4.4 | 4.6 | 2.7 |
| VIII–IX (Ch 37–43) | 3.1 | 3.7 | 4.0 | 3.0 |
| X–XI (Ch 44–49) | 3.7 | 3.7 | 3.7 | 3.0 |
| XII (Ch 50–55) | 3.3 | 4.2 | 3.8 | 3.0 |
| XIII, XV (Ch 56–60) | 3.0 | 3.8 | 3.6 | 3.0 |
| **Book** | **3.5** | **4.2** | **3.9** | **3.0** |
| Book level (navigation, canon pages, templates, projects) | 3.2 | 3.2 | 3.5 | 2.7 |

"Northstar load" 5 means the case illustrates; 1 means its facts bury the lesson.

**Reading.** The ideas are clear (clarity 4.2): almost every chapter states its mental model early and
builds on it. What makes the book hard is how it is told: undefined vocabulary, a case study that
assumes the reader remembers 50 weeks of story, arithmetic and research hedging in the prose, and
maintainer bookkeeping that leaked into reader text. Chapters 50–60 are measurably harder than 1–49.

| Metric (prose only) | Ch 1–49 | Ch 50–60 |
|---|---|---|
| Counted words per chapter | about 5,100 | 5,700–8,000 |
| Words per sentence | 16.5–19.7 | 19.2–23.3 |
| Sentences over 35 words | 3–11 percent | 8–19 percent |
| Flesch–Kincaid grade | 10.1–12.2 | 11.3–13.5 |

Weakest chapters (sum of the four scores): 60, 41, 48, 45, 4, 23, 25, 32, 34, 38. Northstar load 2:
chapters 13, 23, 25, 32, 34, 36, 40, 41, 48, 50, 51, 57, 60. Strongest: 1, 11, 17, 20, 28, 33, 42, 46,
52, 54, 58.

## Book-wide problems, by impact

1. **No glossary; jargon before definition.** Sev1/Sev2 appears in Chapter 2 and is defined in Chapter
   25; "tier 1" in Chapter 5 (defined in 24); "prevention allocation" in Chapter 3 (27); FTE never
   defined in Parts I–IV; Sev3, escaped defect, release train, Core never defined; NPV and discounting
   used in Chapter 45 without being taught; working capital, depreciation, and discount rate undefined
   in the finance chapter (52); CSF, SSDF, SLSA, SBOM never expanded in Chapter 53. Effect sizes
   (g, d) appear unexplained. Assessor 9 proposes 55 glossary terms.
2. **The story's order does not match the book's order.** Most case studies in Chapters 3–18 are set
   in quarter 2, but quarter 1 is told only in Part V; Chapters 19–26 point to Chapter 27 39 times;
   Chapter 34's case evaluates Chapter 35's proposal; Chapter 13 teaches through facts from 20, 21, 28.
   There is no timeline and no "story so far".
3. **Cast and shorthand without reminders.** Victor Lindqvist, Rajiv Menon, Amara Okafor, the managers,
   and later names appear without roles; incident IDs (INC-404, INC-426) without descriptions; "constraint
   3", "points", "the continuation", ADR-0001, and the list of open quarter 4 decisions used as if
   known. Part XII and the capstone all turn on the same open decisions, defined nowhere in those
   chapters.
4. **Maintainer bookkeeping in reader text.** "Canon" 188 times in chapters and solutions (verified by grep); about 100 access notes; 17 codes such as "disputed claim
   D1", "gap G6", "research gap G8"; access notes ("full text could not be fetched", "idea level",
   "abstract read"); "this fact was added for this chapter". These belong in `research/`, with reader
   text using the evidence labels only.
5. **Arithmetic and research tours in the prose.** "Check:" sums in many chapters; several studies
   walked through before the point is stated; tables of numbers where one number would do. Worst in
   Chapters 16, 37, 38, 40, 41, 48, and 50–60.
6. **Exercises not solvable from their chapter.** About 20 exercises need facts their chapter never
   gives (examples: Ch 1 X2 and Ch 3 X1 need the $185,000 engineer cost first given in Ch 10; Ch 23 F2
   asks about incidents the chapter never describes; Ch 27 A2 asks for a QA transition plan the chapter
   does not teach; Ch 45 F3 needs discounting).
7. **Inconsistent or contradictory guidance.** "Lead time" means commit-to-production in Ch 14–15 and
   commitment-to-customer in Ch 16, without saying so; Ch 46 shows per-quarter thresholds fail by chance
   while Ch 49 makes one an exit criterion; Ch 41 breaks its own "Not yet" rule; "escalation" is a
   healthy mechanism in Ch 39 and a failure pattern in Ch 43; capacity appears in five units priced at
   different rates.
8. **The Northstar pages read as an authoring log.** `first-quarter.md` covers the whole year plus
   finances and the board, in wave order (year 2 before quarter 2), with table cells up to 830
   characters; `baseline-data.md` groups facts by the wave that added them.
9. **Front matter out of date.** The home page and roadmaps still say chapters are published one at a
   time and "Chapter 27 is available now"; no path includes Chapters 28 or 29; project hour estimates
   (10–20) look low.
10. **Length.** Chapters 50–60 average about 7,200 words against about 5,250 for 1–49. The assessors'
    verdicts: Chapter 54 earns its length; 52 and 58 mostly; 50, 51, 53, 55, 56, 57 can lose 600–1,200
    words each (research tours, repeated explanations, Northstar re-tellings); 59 and 60 are
    misallocated rather than too long.

## Missing or thin content

| Item | Where | Size |
|---|---|---|
| Glossary | `docs/glossary.md`, in the nav after "How to use" | about 2,500 words |
| Northstar navigation: year-1 timeline, results by quarter, cast page, "story so far" box per case study | canon pages; 2–3 lines per case study | about 60 boxes |
| "Northstar at the start of quarter 4" briefing (the open decisions) | one canon section, linked from Ch 47–60 | about 600 words |
| Capstone as an assignment: hours and size per stage, a working order consistent with the dates, a per-stage rubric, links to the quarter 4 documents | Ch 60 | about 1,000 words, length-neutral with cuts |
| Inclusion and equity (inclusive hiring, calibration bias, underrepresented engineers) | Ch 7, 8, 11 | 1,500–2,500 words |
| The leader's own sustainability (load, isolation, peer network, coach) | Ch 2, 40, 50 | about 1,500 words |
| Managing up at manager level | Ch 2 or 5 | about 1,000 words |
| Ethics (misleading numbers, unsafe shipping, fairness in reductions) | Ch 39, 55, 58 | about 1,200 words |
| AI in day-to-day management (interviewing, performance evidence) | Ch 7, 9, 18 | about 1,000 words |
| Hiring at scale and onboarding | Ch 7 or 48 | about 1,500 words |
| Scaling without bureaucracy (the growth half of Ch 59's title) | Ch 59 | about 1,000 words |
| Notification-day conversation (Ch 58 promises it, never shows it) | Ch 58 | about 300 words |
| Teaching NPV and discounting | Ch 45 | about 500 words |
| Regular review cycle (Ch 5 sends readers to Ch 9, which covers only underperformance) | Ch 9 | about 800 words |
| Templates: hiring scorecard and interview kit, improvement plan, team charter, new-manager 90-day plan | Part XIV | four templates |

## Recommended plan

| Phase | Work | Effect | Effort |
|---|---|---|---|
| 1. Reader scaffolding | Glossary; Northstar timeline, cast, results-by-quarter pages; the quarter 4 briefing; restructure `first-quarter.md` by period; update front matter and roadmaps | Fixes problems 1, 2, 3, 8, 9 for every chapter at once | 1 wave, about 3 agents |
| 2. Mechanical cleanup, book-wide | Remove maintainer bookkeeping from reader text (canon, D/G codes, access notes); expand acronyms at first use per chapter; add roles at each person's first mention per chapter; define each incident ID where used | Problems 3 and 4 | 1 wave, 8 agents on disjoint parts, scripted checks |
| 3. Per-chapter fixes | The assessors' top problems per chapter (about 120 items): unsolvable exercises, contradictions, units, "story so far" boxes, moving arithmetic into tables; cut Chapters 50–57 by 600–1,200 words each as the assessors specify | Problems 5, 6, 7, 10 | 1–2 waves, 8–9 agents |
| 4. Missing content | The table above, starting with Ch 45 discounting, Ch 59 scaling, Ch 58 notification day, the capstone as an assignment, then inclusion, sustainability, managing up, ethics, AI in management, hiring at scale; four new templates | Completeness | 1–2 waves |
| 5. Re-assessment | Repeat this assessment with the same rubric and compare | Verification | 9 agents |

A validator check could prevent regressions: flag "canon", "D[0-9]"/"G[0-9]" codes, and access notes
in `docs/parts/`, and sentences over 45 words.

## Round 2 (2026-11-23), after phases 1–4

Same rubric, nine fresh assessors; reports in `research/readability/round2/`.

| Part | Readability | Clarity | Completeness | Northstar load |
|---|---|---|---|---|
| Ch 1–10 | 3.40 | 4.30 | 3.80 | 3.60 |
| Ch 11–18 | 3.62 | 4.38 | 4.25 | 3.38 |
| Ch 19–27 | 3.56 | 4.11 | 4.22 | 3.56 |
| Ch 28–36 | 3.78 | 4.44 | 4.00 | 3.11 |
| Ch 37–43 | 3.71 | 4.43 | 4.29 | 3.14 |
| Ch 44–49 | 3.50 | 4.00 | 3.67 | 3.00 |
| Ch 50–55 | 3.33 | 4.33 | 4.00 | 3.50 |
| Ch 56–60 | 3.60 | 4.20 | 3.80 | 3.20 |
| **Book** | **3.57** | **4.28** | **4.02** | **3.33** |
| Book level | 3.6 | 4.0 | 4.0 | 3.4 |

The target (every scale at 4.5, no chapter below 4) is not met: 45 of 60 chapters have at least one score
below 4. Remaining problems, by impact:

1. Case studies still carry more Northstar facts than the lesson needs; no prose story of the year exists
   (only tables). A "year in brief" page of about 1,000 words would serve every chapter.
2. Five engineer-cost rates in use ($3,558 per week, $4,000 per week in the business-case template,
   $800 per day, $46,250 per FTE-quarter, $157,250 per capitalized FTE-year); one rate book-wide is needed.
3. Undefined HR, finance, and legal terms in later chapters (warranty, indemnity, escrow, vesting,
   run-rate, requisition, budget envelope, operating plan, due diligence, CISO, attrition); velocity and
   story points undefined.
4. No chapter links the cast page; templates are not linked from chapters 12–15.
5. Contradictions: Ch 20 "five" tier 1 minimums (four); Ch 21 debt-register IDs; Ch 23 false-red hours;
   Ch 15 planning case undercuts its point; Ch 17 uses cycle-time percentiles Ch 16 never defines.
6. Dense case tables in Ch 30, 38, 41, 48, 52, 53; Ch 59's scaling half is thin; Ch 60 seat-count cell.
7. Small: home page says 20 templates (24); `curriculum.md` generator residue for Part XIV; learning
   paths A–E lack Chapter 26.

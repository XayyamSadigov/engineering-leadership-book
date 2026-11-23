# Round 2 notes, lane c4 (Chapters 28–36 and their solutions)

Assessor report: `a4-ch28-36.md`. Validation: `chapters`, `references`, `exercises` pass. The only
`navigation` errors in this lane are links to `year-in-brief.md` and the round-2 glossary anchor
`#deployable-unit` (both allowed). The remaining failures are elsewhere: the stale single-file edition
and a Chapter 60 solutions anchor from another lane.

Applied in every chapter: the "New to Northstar?" line in the first "Northstar so far" box (P7, cast
link); "the year 1 record" as the link text for `first-quarter.md`; the fixed core/permissions
reminder ("a tier 1 Core module changed by four teams, unowned since baseline") where the thread stays.

## Word counts (validator count)

| Chapter | Before | After |
|---|---|---|
| 28 | 5,313 | 5,313 |
| 29 | 5,085 | 5,018 |
| 30 | 5,090 | 5,186 |
| 31 | 5,317 | 5,476 |
| 32 | 5,316 | 5,436 |
| 33 | 5,196 | 5,197 |
| 34 | 5,027 | 4,885 |
| 35 | 5,380 | 5,541 |
| 36 | 5,445 | 5,513 |

## Findings

| Finding | Status | What changed |
|---|---|---|
| P1 dependency link undefined | Done in chapter text | Defined inline at first use in Ch 28 (case), 33 (moved up to Failure Modes, removed from case), 34 (example), 35 (case list). There is no glossary anchor for it, so it is not linked (see questions) |
| P2 Ch 30 risk register | Done | 5 short columns, owners and incidents in two lines under the table; point first ("owners and responses, not scores"); cost arithmetic as one sentence; Chapter 26 aside cut |
| P3 core/permissions thread | Done | Dropped in Ch 28 and Ch 32 case, Ch 29 example and case; one fixed reminder in Ch 31, 33, 34, 35, 36; "exemption" defined where used (Ch 31, 33, 35) |
| P4 Ch 36 example used early | Done | One-line setup of the 60-engineer example in "Undoing a reorganization" |
| P5 Ch 32 DORA percentages | Done | Claims first, then a 4-row table; unused figures cut; DORA linked and expanded |
| P6 Ch 36 succession table | Partly | Kept all 10 rows (F3 needs every row), cells shortened, cast linked, people introduced in plain sentences after the table, lesson stated first |
| P8 Ch 33 decision paragraph | Done | Rewritten as the director's leaning plus the two facts bearing on B and C, and why each matters |
| P9 Ch 29 example | Done | Conclusion first; cost basis in a note line; core/permissions share and by-team counts cut |
| P10 Ch 34 recount | Done | 6×6 matrix shown with how to read it; span table now carries each manager's key factor (fixes F1 data); riddle replaced by one verdict per move |
| P11 Ch 30 cross-references | Done | Example aside cut to "decided separately (Chapter 32)"; case uses self-contained clauses |
| P12 Ch 32 Bram thread | Done | Bram complication cut from the case; intro explains the QA move |
| P13 Ch 35 chapter pointers | Done | Facts restated (health check, links); test table cells are verdicts with detail below |
| P14 glossary/acronyms | Done | CI (Ch 30, 32), CI/CD, CNCF, spike, modification requests, circuit breaker, change failure rate (31, 32), release train (31), lead time (35), DORA (32), deployable unit (32) |
| P15 repetition, spelling | Done | Ch 35 points to Ch 33 for n(n−1)/2; Ch 34 CTO count cut; one-on-one, every two weeks, program, fulfill (chapters and solutions) |
| Known: Ch 30 $800 | Done | Labeled Finance's day rate with the planning-rate comparison; dense TCO table reduced to four short columns with the derivation in one line |
| Known: Ch 32 "17 units" | Done | Round-2 wording plus glossary link |
| Missing: Ch 31 bounded contexts | Done | ~200-word subsection, labeled practitioner approach and this book's recommendation, no citation; saga and outbox sentences at step 4 |
| Missing: Ch 30 evaluation | Done | "Running an evaluation", five steps |
| Missing: Ch 32 strangler mechanics | Done | "One strangler slice, step by step" with facade, parity checks, switch-off |
| Missing: Ch 35 portfolio, sites, 500 band | Done | Portfolio table and sites rules in "Three inputs"; three 500-band functions after the Halvard example |
| Missing: Ch 36 announcement skeleton | Done | Five-part skeleton, FAQ headings, telling a manager whose scope shrinks |
| Missing: Ch 29 appeal | Done | Appeal goes to the sponsor |
| Missing: Ch 34 matrix | Done | See P10 |
| Case trimming (round-2 decision 1) | Done | Ch 28 (2019 page, review history), 29 (mandate recap, chapter pointers), 30 (case intro, table), 31 (ownership table), 32 (team paragraph, Bram), 33 (INC-405, INC-407, chapter pointers), 34 (Mateo, INC-417, Chapter 5), 35, 36 trimmed |

Solutions updated: ch29 (every two weeks), ch32 (fulfill), ch33 (Customer Experience structure as
given), ch34 (every two weeks), ch35 (program), ch36 (Bram's plan removed; one-on-one).

## Questions for the maintainer

1. A glossary entry "Dependency link (dependency matrix)" with anchor `#dependency-link` would let
   Ch 28, 33, 34, 35 link the term; it is not in the round-2 anchor list, so I defined it inline only.
2. Ch 31's bounded-context subsection cites no source. A verified entry for Evans's *Domain-Driven
   Design* (2003) would let it carry a citation.
3. Ch 35 slightly exceeds 5,500 (5,541) and Ch 36 is at 5,513; both carry phase-4 and round-2
   additions. Trim further if the limit is strict.

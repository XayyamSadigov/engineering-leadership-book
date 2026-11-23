# Lane c7 notes: Chapters 50–55 and their solutions

Assessor report: `research/readability/round2/a7-ch50-55.md`. Word counts are the validator's.

| Chapter | Before | After |
|---|---|---|
| 50 | 5,535 | 5,763 |
| 51 | 5,269 | 5,468 |
| 52 | 6,406 | 6,695 |
| 53 | 6,494 | 6,637 |
| 54 | 5,993 | 6,388 |
| 55 | 6,694 | 6,639 |

All six "Northstar so far" boxes were rewritten to the round-2 form: two or three facts the chapter uses,
the timeline link, and "New to Northstar?" with the year in brief, cast, and quarter 4 briefing. The
repeated "Sev1 and Sev2 fell from 30 to 14" line now appears only where the chapter uses it (50, 55).

## Chapter 50

- P5 (cast link): done, in the box.
- P7 (standard owners, top-40, week 14 story): done. "Standard owners" became "the staff engineers who
  own the pipeline and data standards" (chapter and A2; solutions A2 heading updated). Top-40 glossed at
  first use. The week 14 story is one clause with a pointer to Chapter 51, which tells it in full.
- P14 (Bandiera too vague): done, restated within the abstract-level claim (fit between how the CEO
  spends time and what the firm needs; no single best pattern), labeled research finding, applied to
  CTOs by analogy.
- Glossary links added: budget envelope, CISO, operating plan, board pack, Sev1/Sev2.
- Missing content, CTO–CEO relationship: done, a compact subsection "Agreeing the role with the CEO"
  (about 130 words), tied to X2.

## Chapter 51

- P3 (allocation tangled in undecided proposals): done. Planning basis stated as "79, open, could move by
  one either way"; alternative letters removed from the body (A2 still supplies them). "Converge before
  adding" defined in a clause. TR-07 replaced by "a dependency already on the risk register". The "week
  40–41 finding" reworded as "a sample of corrections earlier in the quarter" (70 of 340 kept; the
  solution to F2 uses it).
- P10 (board presentation barely taught): done. New subsection "The board version" in CTO Perspective:
  a six-part one-page outline and a compact layered roadmap table, labeled illustrative, built only
  from the draft's existing options and decision dates.
- "Estate" defined at first use. Alignment research tour collapsed to one sentence. Planning rate
  labeled as the book's planning rate. Operating plan and budget envelope linked.

## Chapter 52

- P2 (five financial tables in a row): done. Each kept table opens with its one-sentence lesson. The
  balance sheet and cash-flow statement moved into a collapsible note, with the deferred-revenue and
  free-cash-flow sentences kept inline (F1 is still solvable). The six-item cost-of-revenue cell
  reduced to four (sums unchanged: 26.5 + 3.1 + 2.1 + 8.9 = 40.6). $27,750 now shown as $185,000 × 15
  percent. The "Where the $20.3M is" table is now named as the budget's two views side by side.
- P8 (accounting acronyms): done. FASB and GAAP defined in the terms box; codification numbers (ASC
  350-40, ASC 985-20, ASU 2025-06) moved from prose to the References entry.
- P9 (TR-01 before introduction): done; the Decision Framework row now names the work in plain words.
- P15 (fiscal-year labels): done; mapping in the terms box, prose uses year 1 and year 2, FY labels only
  in table headers. "FY−2 to FY1" became "the four years up to and including year 1".
- $800 per engineer-day labeled at first use as Finance's day rate, with the planning-rate sentence. No
  figure in any statement changed. The scenario table cut to four columns (engineer-weeks displaced in
  a line beneath); the year-2 envelope derivation moved under its table.
- Missing content, variance review: done as a three-row illustrative table (plan wrong, conditions
  changed, execution). A populated two-view budget table was not added; the existing $20.3M table is
  now presented as the two views instead, to hold length.
- Glossary links: run rate, budget envelope, operating plan, board pack.

## Chapter 53

- P4 (wall of IDs): done. TR table lost its owner column and INC numbers (each incident kept as a few
  words). The two ER tables merged into one (ID, consequence, grouped sources, owner with role, score).
  Treatments summarized in one sentence; exposures given as short bullets with their one-line
  derivations inline (ER-01 margin and credits basis), so the chapter no longer defers to the
  solutions. "Day 90" renamed "End of quarter 1". Solutions header and the $800 label updated.
- P5 (roles in tables): done (Marcus Oyelaran, Tom Becker, Ines Carvalho given roles).
- P13 (material, SLO links): done.
- Missing content: breach response and continuity, done as a compact subsection (disclosure path,
  tabletop exercise, continuity plan for money paths), replacing the exclusion sentence. Vendor risk
  expanded by a definition of a material vendor and a concentration-versus-switching-cost rule.
- Cuts to pay: NIST roll-up, quantification paragraph, framework purposes, reporting paragraph.
- CISO linked.

## Chapter 54

- P12 (statistical terms): done. Standard error explained under the evidence table (roughly 6 to 46
  percent on the two-standard-error rule); preregistered, preprint, and confounded glossed in place.
- Missing content: "Data strategy beyond readiness" (owner of meaning, product versus by-product, where
  the data team sits, platform choices; about 280 words) and "Agents that act" (permissions, review
  load, attribution; about 120 words), both labeled this book's recommendation. CTO Perspective's data
  paragraph shortened to avoid repetition.
- Data-cascades research tour collapsed. Two long sentences split.

## Chapter 55

- P1 (deal and legal vocabulary): done; a "Deal terms in plain words" note before the findings diagram
  (warranty, indemnity, escrow, closing condition, material adverse effect, copyleft).
- P6 (shorthand): done. Re-rating defined at first use; severity audit glossed; the mandate,
  operational minimums, and Sev1/Sev2 linked.
- P11 (probability table): done. Plain-language point first; Poisson glossed; the all-four-quarters
  column derived in one line; Chapter 46's role stated in a clause.
- Glossary links: operating plan, budget envelope, board pack, due diligence, warranty.
- "Estate" replaced by plain words. Duplicate Keil citation, one trade-off, and repeated case lines cut.
- Missing content, sample board page: not added. F1 asks the reader to write exactly that page, so a
  mock-up in the chapter would give away the answer.

## Patterns

- Week-number density: reduced where touched (Ch 51 case, Ch 55 case, Ch 53 table); not rewritten
  book-wide.
- Every length is under the phase-4 bound of about 6,800; 52, 53, and 55 sit above 6,500 because of
  definitions and the requested additions.

## Questions for the maintainer

1. The glossary would help with entries for "estate", "top-40 customers", "re-rating", and "severity
   audit" (the assessor's pattern list); this lane defined them inline instead.
2. Ch 51's layered roadmap sketch places the ordering API in year 4 "if exercised". It is labeled
   illustrative and follows from the week 78 decision date, but check it reads as a draft, not a plan.
3. Validation: the only errors in this lane are the round-2 glossary anchors that do not exist yet.

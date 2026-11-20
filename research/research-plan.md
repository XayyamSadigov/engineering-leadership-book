# Research plan

## Purpose

Every substantive claim in the book must be traceable to a source the reader can check, or be
labeled honestly as practitioner consensus, expert opinion, or the book's own recommendation. This
plan says how sources are found, verified, recorded, and used.

## Questions the research must answer

The questions follow the curriculum. For each part, these are the claims most likely to be stated
with more confidence than the evidence supports:

| Part | Questions where evidence matters most |
|---|---|
| I Foundations | What is known about the effect of managers on team outcomes? How is managerial output measured? |
| II People | Validity of interview formats; feedback effectiveness; drivers of retention for engineers |
| III Teams | Psychological safety: what was measured, in which settings, with which effect sizes; remote and hybrid collaboration effects |
| IV Execution | What DORA's research design supports and does not; SPACE and DevEx; estimation accuracy; WIP and lead time |
| V Quality | Debt cost estimates; code review outcomes; testing and CI effects on stability; SLO and error-budget practice; blameless review evidence; supply-chain security standards |
| VI Architecture | Evidence on microservices versus monoliths; Conway's law empirical studies; platform engineering outcomes |
| VII Org design | Span of control and layers; team cognitive load; reorganization outcomes |
| VIII Operating system | OKR evidence; meeting effectiveness research |
| IX–XII Director to CTO | Strategy literature (largely practitioner); technology investment and financial practice; governance standards |
| XIII Advanced | Layoff effects on remaining staff; M&A integration outcomes; turnaround evidence |

## Source hierarchy

When sources disagree, prefer them in this order, and say in the text which kind you are using:

1. **Scholarly research**: peer-reviewed studies and meta-analyses. Note the sample, setting, and
   whether the result has been replicated.
2. **Industry research with a published method**: DORA, peer-reviewed or methodologically
   documented industry surveys. Note who funded it and how respondents were recruited.
3. **Standards and frameworks**: NIST, SLSA, AWS Well-Architected. These describe recommended
   practice, not evidence of effect.
4. **Official documentation and engineering handbooks** from established organizations, including
   the free Google SRE books. These are first-hand accounts of practice in one context.
5. **Practitioner literature**: books and essays by experienced leaders. Valuable for mechanisms,
   vocabulary, and failure patterns; not evidence that a practice works in general.

The reading list in the project brief is mostly level 5. The book uses it for ideas and
attribution and looks for level 1–3 evidence wherever a claim is about effect.

## Verification procedure

For every bibliography entry:

1. Find a page from the publisher, journal, DOI resolver, standards body, or author that confirms
   the citation details. Catalog records (Open Library, Library of Congress) are acceptable when
   the publisher site cannot be fetched.
2. Record in `bibliography.yaml` which fields were confirmed (`verified_fields`), which pages
   confirmed them (`verified_via`), and the date (`verified_on`).
3. Record how much of the work was actually read (`access_level`): `full-text`, `abstract-only`,
   `official-summary`, or `metadata-only`. Most books are `metadata-only`: the citation is checked,
   but the book was not read for this project. A chapter that attributes an idea to a
   `metadata-only` source must attribute only the idea the source is widely known for, in the
   book's own words, and must not quote, give page numbers, or report findings.
4. Record `claims`: what the source supports, phrased conservatively, and the `basis` (what was
   read to support the claim).
5. Record discrepancies and access problems in `access_notes` (for example: edition differences,
   conflicting years, blocked publisher pages).

`tools/check_references.py` refuses citations from published chapters to entries with no
verified fields.

## Rules that apply while writing

- No invented quotations, page numbers, statistics, studies, URLs, or DOIs.
- A number from a source is reported with its source, its population, and its date. If the number
  cannot be checked on a fetched page, it is not used.
- Every illustrative number (all Northstar data, all worked examples) is labeled as illustrative.
- Contested topics get a section in `disputed-claims.md` before a chapter takes a position.
- Where evidence is thin, the chapter says so and records a gap in `research-gaps.md`.
- If source access fails, the limitation is recorded and the claim is either removed, qualified,
  or marked for verification in the quality report. It is never filled from memory.

## Status

| Batch | Entries | State |
|---|---|---|
| Brief reading list, books 1–18 | 18 | Verified 2026-11-18 (`_verification/books-a.yaml`) |
| Brief reading list, books 19–35 | 17 | Verified 2026-11-18 (`_verification/books-b.yaml`) |
| Primary research and standards | about 30 | In progress (`_verification/primary-research.yaml`) |
| Per-part targeted searches | — | Before each part is written |

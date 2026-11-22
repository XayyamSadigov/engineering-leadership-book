# Authoring brief for parallel waves (wave 7: Part XII)

This brief is given to every parallel author in a wave. It adds wave-specific lanes to `CLAUDE.md`,
which stays binding. Keep it in the repository so the next wave can reuse it; replace section 6 per
wave.

## 1. Before writing

1. Read `CLAUDE.md` in full (the chapter contract, citation rules, voice, diagram rules, parallel
   authoring rules in section 6a).
2. Read the Northstar canon: `docs/case-studies/northstar/index.md` (including "Executive and board
   context (Part XII)"), `baseline-data.md`, `first-quarter.md` (especially "Quarter 3 results" and
   "Quarter 4"), and `halvard.md`. Use names and numbers exactly.
3. Read one finished chapter of the previous part as a model of depth, tone, and format, for example
   `docs/parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md` and its
   solutions file. Templates: model on `docs/templates/technology-investment-business-case.md`.
   Projects: model on `docs/projects/p5-delivery-and-reliability-scorecard.md` and its solution.
4. Read the chapters your lane cross-references (section 6), at least their Mental Model and
   Northstar sections, so you link to them instead of re-teaching.

## 2. What you may edit

Only your own files: your chapter (or template, or project), its solutions file, and three side files:

- `research/pending-sources/chNN.yaml` (or `t11.yaml`, `p7-p8.yaml`, ...): new sources, same schema as
  `research/bibliography.yaml`. Check `bibliography.yaml` first and reuse existing ids; never add a
  duplicate of an existing entry (check by URL and title as well as id).
- `research/northstar-additions/chNN.md`: every Northstar or Halvard fact you add that is not already
  canon, one table row each, with the arithmetic that checks it against the canon.
- `research/evidence-matrix-chNN.md`: claim, source id, access level, evidence label.

Do **not** edit `curriculum.yaml`, `mkdocs.yml`, the canon pages, `bibliography.yaml`, generated
pages, or anyone else's files. The maintainer integrates.

## 3. Research rules

- Verify every source you cite by fetching a legal page in this session (publisher page, official
  summary, DOI landing page, the author's own site, a standards body). Never use pirated copies or
  shadow libraries. Record `verified_fields`, `verified_via`, `verified_on` (today's date),
  `access_level`, and conservative `claims`.
- Never invent a quotation, statistic, page number, study, URL, or DOI. If it cannot be confirmed on a
  page fetched in the session, leave it out.
- `metadata-only` sources are credited for the idea they are known for, in the book's words; no
  quotation, page number, or reported finding.
- Label evidence strength in the prose with the vocabulary in `docs/references/evidence-labels.md`.
- At least five distinct sources per chapter, not only practitioner literature.
- Thin evidence is admitted in the chapter and listed in your evidence matrix as a gap.
- Google SRE books and *Software Engineering at Google* (CC BY-NC-ND): summarize and cite only.

## 4. Northstar rules

- Every Northstar passage is recognizably fictional. Never put a real company into an invented story.
  Real companies appear only as cited public cases.
- **Setting.** Part XII Northstar passages are set in quarter 4 of the director's first year
  (weeks 40–52). The latest measured results are quarter 3. Quarter 4 outcomes are not recorded: every
  open decision listed in `first-quarter.md` under "Quarter 4" stays open (the year-2 organization,
  the VP question, the quality continuation, the workforce plan, the week 34 portfolio forum, the CI
  target, ADR-0001, the week 50 board meeting). You may show drafts, positions, and analysis; you may
  not record outcomes.
- **Seat.** Victor Lindqvist is the CTO throughout Part XII. Examples either put the reader in his
  seat ("You are Victor Lindqvist in week 47") or have the director drafting CTO-level work for him.
  Nobody else becomes CTO in Part XII.
- No new events in quarters 1–3. New quarter 4 facts only inside your lane (section 6), recorded in
  your additions file, and consistent with the existing quarter 4 calendar.
- Exercise scenarios that are clearly hypothetical ("Suppose a buyer approaches Northstar...") are
  scenarios for the reader, not canon; say so in the exercise.
- Recompute any figure you derive from canon and show the arithmetic in your additions file.

## 5. Validation

```bash
ELH_TREAT_AS_LIVE=NN .venv/bin/python tools/validate_book.py
```

Ignore nav, stale-page, stale single-file, and missing-anchor errors caused by your chapter not being
in the nav yet. Every other error and warning is yours to fix. Mermaid: `flowchart TD`, labels of about
four words, at most four nodes side by side, quote labels with parentheses, colons, or semicolons.
Include the "Awaiting human review" banner directly under the H1, as finished chapters do. No em dashes
in prose.

When you finish, report: files written, word count, number of sources (new and reused), Northstar facts
added, validation result, and anything you could not verify.

## 6. Wave 7 lanes (Part XII: CTO leadership)

Ownership already settled elsewhere (link, do not re-teach): DORA, SPACE, DevEx and metric gaming
(Ch 18); technical debt economics (Ch 21); security and supply chain in the delivery pipeline
(Ch 26); quality transformation (Ch 27); architecture governance and ADR practice (Ch 28); technical
strategy, technology selection, build versus buy (Ch 30); platform engineering (Ch 32); engineering
economics and cost of delay (Ch 45); stakeholder management (Ch 46); the VP role and the VP question
(Ch 47); workforce planning and enterprise governance (Ch 48); multi-year transformation and executive
communication (Ch 49).

| Author | Owns | Northstar lane (new facts allowed only here) |
|---|---|---|
| ch50 | CTO archetypes; CTO, CIO, VP Engineering splits; the CTO's own team and operating rhythm; what only the CTO can do | Victor Lindqvist's job as it is: his calendar, his one direct report, IT under the CFO, what he delegates. Do not answer the VP question (Ch 47) |
| ch51 | Technology strategy derived from business strategy; three-year roadmap with horizons, options, and decision points; coherence tests | A three-year technology strategy that Victor drafts in weeks 46–49 as a discussion item for the week 50 board, outcome open. Use the year-2 proposals as inputs, not results |
| ch52 | Financial statements (income statement, balance sheet, cash flow) read by a technology leader; budgeting; capitalized versus expensed software; investment cases with scenarios | The only author who may add Northstar financial-statement figures (revenue, cost lines, operating income, cash, capitalization policy). Must stay consistent with ARR $140M, gross margin 72 percent, engineering personnel about $16.1M, cloud and tooling $4.2M, 620 employees. Show every derivation |
| ch53 + t11 | Enterprise technology risk register; security strategy with recognized frameworks (NIST CSF 2.0, SSDF, SLSA); regulation through engineering controls; reporting risk to non-specialists. Also the risk register template (`docs/templates/risk-register.md`) | Northstar's compliance and audit status (for example, whether it holds an attestation report and what customers ask for), the audit committee's view of technology risk, security reporting through IT to the CFO. Use the Ch 26 baseline and day-90 security facts exactly |
| ch54 | Data foundations before AI; buy, build, or wait on AI capabilities; governing AI use in engineering; evaluating AI productivity claims with Ch 18's evidence standards | Northstar's data estate and AI usage (Data and Analytics, Farah Haddad, Li Na Zhou), any AI coding-assistant policy, and AI requests from product or sales in quarter 4 |
| ch55 | Communicating technology status and risk to a board; technology due diligence (run or survived); recording executive decisions under uncertainty and disagreement | The week 50 board meeting's preparation and the board members' known concerns (outcome open). Due diligence on Northstar only as a labeled hypothetical scenario |
| templates | t05 CTO competency matrix (`docs/templates/cto-competency-matrix.md`), modeled on t04; t12 architecture decision record (`docs/templates/architecture-decision-record.md`), consistent with Ch 28's ADR practice and ADR-0001, which stays open | No new facts; examples use canon only |
| projects | P7 Design a 12-Month Engineering Strategy (`docs/projects/p7-twelve-month-engineering-strategy.md`, attached to Ch 51); P8 Build a CTO Technology Investment Proposal (`docs/projects/p8-cto-technology-investment-proposal.md`, attached to Ch 52); each with a worked solution in `docs/projects/solutions/p7-solution.md` and `p8-solution.md`; optional data files in `docs/projects/data/` named `p7-*.csv` / `p8-*.csv` | Set in quarter 4; the learner produces the strategy and the proposal. Use canon only; do not depend on facts the ch51 or ch52 authors are adding in parallel |

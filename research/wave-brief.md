# Authoring brief for parallel waves (wave 8: Part XIII and the capstone)

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

## 6. Wave 8 lanes (Part XIII, the capstone, the last templates and project)

Wave 7 changes to read first: the canon now has "Part XII facts (quarter 4)" in `first-quarter.md`
and "Executive and board context (Part XII)" in `index.md`. Victor Lindqvist stays CTO throughout the
book; nobody succeeds him. Every quarter 4 decision stays open book-wide. Where a chapter puts the
reader in the CTO's role, the reader takes Victor's seat in quarter 4.

Halvard rules for this wave: each author may add Halvard facts only inside its assigned group (see
`halvard.md`), set after the planning year described there; the group's starting size is the one in
the tables. Grep `docs/` before naming any new person, so that no name is reused. Halvard's CTO stays
unnamed.

Ownership already settled elsewhere (link, do not re-teach): onboarding and the first 90 days
(Ch 2 and the director's first quarter, Ch 40); feedback and difficult conversations (Ch 6);
performance management and underperformance (Ch 8 and 9); trust and accountability (Ch 11);
decision rights and decision records (Ch 13); incident response and blameless review (Ch 25); quality
transformation (Ch 27); reorganizations, succession (Ch 36); cadences and operating system (Ch 37);
managing managers (Ch 41); leading change and director failure patterns (Ch 43); stakeholder
negotiation (Ch 46); workforce planning (Ch 48); multi-year transformation and executive politics
(Ch 49); the CTO's role, strategy, finance, risk, AI, boards (Ch 50–55).

| Author | Owns | Northstar or Halvard lane (new facts allowed only here) |
|---|---|---|
| ch56 + P2 | Triage of a failing organization in 30 days; reversing quality decline while rebuilding stakeholder trust; keep, coach, or replace decisions about leaders. Also Project 2, Diagnose a Low-Performing Engineering Team (`docs/projects/p2-diagnose-a-low-performing-team.md`, solution `docs/projects/solutions/p2-solution.md`, optional `docs/projects/data/p2-*.csv`) | Northstar at arrival read as a failing organization, using the baseline and quarter 1 canon only (no new quarter 1 events). Halvard's fourth product group (90 engineers) as a second, larger failing organization: you may name its VP and add its facts. P2: Northstar's Billing team at baseline (weeks 1–3), canon data only, plus project-only data marked as such |
| ch57 | Leading through a major incident or public failure, including external communication; disagreeing with executives productively (commit or escalate); reading resistance to change as information | Halvard Commerce (Nadia Brennan's group): a public Checkout outage and its external communication. Northstar: the executive disagreements already in the quarter 4 canon (Greg Tanaka, Rajiv Menon, Amara Okafor) and resistance already recorded in earlier chapters; new quarter 4 facts only if they record no outcome |
| ch58 | Planning a reduction responsibly (selection criteria, communication, continuity of ownership); leading the remaining organization; integrating an acquired engineering team and its technology | Halvard only: a reduction in the second product group (110 engineers) and an acquisition integrated into the third product group (100 engineers); name those groups and their leaders. Northstar appears only in clearly labeled hypothetical exercises; no Northstar reduction or acquisition enters the canon |
| ch59 | Technical transformation with flat or shrinking budget; process that carries load versus process that carries history; removing management overhead safely | Northstar's year 1 under flat headcount, read from the canon; a quarter 4 audit of Northstar's forums and rules (which carry load) is allowed if it records no outcome. Halvard's platform organization (70 engineers) and its six enterprise policies under a budget cut |
| ch60 | The capstone, Chapter 60 (`docs/parts/15-capstone/60-capstone-northstar.md`): ten stages at Northstar, first as Engineering Director (diagnosis, ownership model, scorecard, debt priorities, accountability design, 90-day plan), then in Victor Lindqvist's seat in quarter 4 (12-month strategy, investment case, three-year technology strategy, board communication). It still follows the chapter contract; the stages live mainly in the Practical Playbook and Exercises, each pointing to the chapters, templates, and projects it draws on | Canon only, no new facts. Each stage names its moment in the story and the facts available then. Do not duplicate Projects 3–8: the capstone integrates them and adds what only the whole sequence shows |
| templates | t01 1:1 template (`docs/templates/one-on-one.md`), t02 career development plan (`career-development-plan.md`), t06 team health assessment (`team-health-assessment.md`), t19 leadership succession plan (`leadership-succession-plan.md`); model on existing templates | Examples use canon only (for t19, the week 44 succession table; for t02, the levels and pay canon; for t06, a canon team). No new facts |

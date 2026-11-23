# Round 2 notes, lane c3 (Chapters 19–27)

Applied to every chapter: the "New to Northstar?" line in the first "Northstar so far" box; roles at
first mention in case studies and exercises; "change failure rate" everywhere (DORA's "change fail rate"
named once, in Ch 25); "year 1 record" for `first-quarter.md` links; a one-line lesson at the end of
case studies that lacked one; glossary links for `#renewal-commitments`, `#the-five-constraints`,
`#inc-numbers`, `#register-ids`, `#paved-road`, `#sli-slo-and-sla`, `#blameless-review`, `#recurrence`,
`#prevention-point`, `#technical-debt-principal-and-interest`.

Word counts (validator), before → after: Ch19 5,310 → 5,288; Ch20 5,170 → 5,198; Ch21 5,186 → 5,292;
Ch22 5,045 → 5,286; Ch23 5,314 → 5,341; Ch24 5,516 → 5,539; Ch25 5,421 → 5,529; Ch26 5,504 → 5,538;
Ch27 5,605 → 5,516.

## Findings

| Finding | Status |
|---|---|
| P1 renewal commitments unexplained | Done: glossed and linked at first use in Ch 20, 21, 22, 24, 26, 27; Ch 27 says Orders and Payments and Integrations own them |
| P2 "constraint 5 of the case" | Done: "one of the five fixed conditions" with glossary link. Renaming the canon's "constraints" book-wide is a maintainer decision (not done) |
| P3 INC tables overwhelm | Done: Ch 24 table now counts by loss type, full list in a collapsible note; Ch 23 ten-incident table moved into a collapsible note (F2 updated); Ch 25 table drops the ID column, IDs grouped by prevention point in the note; `#inc-numbers` linked |
| P4 "five" tier 1 minimums | Done: "five tier 1 standards (the four operational minimums plus the auditable-pipeline standard)" |
| P5 10 hours of false reds vs 9 hours red | Done: framed as an upper bound larger than measured red time |
| P6 debt register IDs and units | Done: table shows TD-001–004, 006, 007 in dollars, five columns; TD-006/007 marked new; TD-005 absence explained; engineer-day derivations moved under the table; "74-minute" explained; $800 labeled as Finance's day rate with the planning-rate comparison |
| P7 episodes retold | Done for Ch 23 (quarantine told once, then "the quarantine rule"; QA triage and working-group reintroduction cut; failed rollback kept) and Ch 19 (link to Ch 27 for the week-10 announcement). Ch 21, 22, 27 already used one sentence plus link for the week-9 Sev1 |
| P8 "Part V at a glance" front-loaded | Done: bulleted chapter map, one-sentence quarter summary, timeline and cast links |
| P9 rotation design thin | Done: new "Designing a rotation" subsection in Ch 24 (primary/secondary, shadow and reverse shadow, handoff, escalation, compensation, Billing example); paid for with cuts in Ch 24 |
| P10 CVSS, provenance, acronyms | Done: CVSS sentence (0–10 base score; critical 9.0+, high 7.0–8.9, verified on first.org's CVSS v3.1 specification this session, stated as a definition without a bibliography entry), provenance defined, "abstract supports" phrase replaced, SPDX/CycloneDX parenthesized |
| P11 expand-and-contract before definition | Done: defined in Ch 22 with link to Ch 23 |
| P12 detection/prevention/control point; planning vs scribe | Done: "prevention point" throughout Ch 25 with one sentence relating it to Ch 19's detection point; Google's "planning" role mapped once to the book's "scribe" |
| P13 bookkeeping asides | Done: Ch 24 aside replaced by "the original 15"; Ch 25 aside replaced by "with the total still 30" |
| P14 business case in prose | Done: four-row table, planning rate stated, pessimistic case in one line |
| P15 garbled sentence | Done |
| Missing: first minutes of response (Ch 25) | Done: five-step subsection supporting A1 |
| Missing: load testing (Ch 22) | Done: compact subsection using INC-415 |
| Missing: exemption register example (Ch 20) | Done: two-row table in the case study |
| Exercise gaps | Ch 21 F3 now states 80 engineers; Ch 24 A1 and Ch 25 A1 now taught in the chapter |
| Low: Sev1 recap pattern | Partly: Sev1/Sev2 still defined once per chapter in prose; boxes not expanded |

## Questions and mismatches for the maintainer

1. `docs/templates/technical-debt-register.md` TD-004 says "automated checks in quarter 2", but the year 1
   record and Ch 21/23/25 say the migration check landed in week 11 (quarter 1). The template should
   probably say quarter 1, week 11.
2. The template lists only TD-001 to TD-005; Ch 21 adds TD-006 (four CI systems) and TD-007 (flaky Core
   tests). If the register IDs glossary entry or the template is meant to be complete, add those two.
3. Ch 20's exemption table says auth-svc's compensating control is "None recorded": the case pages give
   none. If one exists, add it to the case.
4. CVSS has no bibliography entry; consider adding the FIRST CVSS v3.1 specification.

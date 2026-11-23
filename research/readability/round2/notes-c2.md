# Round 2 notes, lane c2 (Chapters 11–18)

Report: `a2-ch11-18.md`. Validation: no errors from this lane except the expected ones (links to
`year-in-brief.md`, glossary anchors `#cycle-time` and `#velocity-and-story-points`).

## Word counts (validator)

| Chapter | Before | After |
|---|---|---|
| 11 | 5,340 | 5,391 |
| 12 | 5,302 | 5,376 |
| 13 | 4,994 | 5,021 |
| 14 | 5,389 | 5,393 |
| 15 | 5,301 | 5,415 |
| 16 | 5,085 | 5,336 |
| 17 | 5,197 | 5,395 |
| 18 | 5,178 | 5,261 |

## Applied in every chapter

- First "Northstar so far" box ends with the "New to Northstar?" line (year in brief, cast). Closes P15.
- `first-quarter.md` link text changed to "year 1 record" (Ch 12, 13, 14, 15, 16, 17, 18).
- Change failure rate glossed the same way everywhere: "share of changes that fail in production"
  (Ch 11, 12, 18; Ch 14's gloss was removed along with the figure). Ch 18's DORA table now says "change
  failure rate", and so does ch18-solutions F1. Closes P4.
- Repeated "quarter 1 cut 30 to 21" status removed from case openers in Ch 11, 16, 18 (it stays in boxes).
- Neighbor-chapter preambles cut to one sentence at the end of the opening (Ch 14–18).
- "Is known for" hedges reduced where a plain "argues" keeps the evidence level (Ch 11, 12, 13, 14, 16).
- Engineer-time rate: Ch 11 X2 and Ch 14's departure table now name the $3,558 per engineer-week planning
  rate; ch11-solutions X2 updated. No $800 day rate appears in this lane.

## Per finding

- **P1 (high), Ch 15 capacity case:** done. The 17 committed items summed to about 560 engineer-weeks
  against an assumed 780 (both from the baseline page). The text now says the plan looked slack yet
  failed, puts cross-team items first, explains why 686 > 560 still left little real slack, and points
  to Ch 17's "effort is not completion". By-team delivery table moved to a baseline link.
- **P2 (high), cycle time undefined:** done. New Ch 16 subsection "Flow measures: throughput, cycle time,
  and work item age" with a three-row table, the relation to lead time, and an 85th-percentile example.
  Ch 15 glosses the four Kanban measures and links it; Ch 17's forecasting table links it and
  `glossary.md#cycle-time`. Ch 16 also clarifies Little's "cycle time".
- **P3 (medium), templates:** done. Links to team-charter (Ch 12 playbook), architecture-decision-record
  (Ch 13 recording decisions), team-health-assessment (Ch 14 playbook), capacity-planning-model (Ch 15
  playbook), executive-update (Ch 18 CTO Perspective).
- **P4:** done (see above).
- **P5 (medium), Ch 16 case counts:** done. Pair table moved to the baseline link; each evidence block
  opens with its conclusion; the 43/29/15/12 split is a one-row table.
- **P6 (medium), Ch 15 quarter-2 capacity:** done. States that unplanned work fell from 34 to 31 percent
  in quarter 1 and the model projects 28; prevention allocation glossed consistently with the glossary.
  Per-team prevention shares compressed to "10 percent against 15 to 25".
- **P7 (medium), Ch 18 jargon:** done. Factor analysis / Bayesian SEM sentence replaced; failures column
  dropped; interval column renamed "Plausible range" with a plain explanation; Wilson named nowhere.
  ch18-solutions F3 wording aligned.
- **P8 (medium), Ch 12 knowledge-map setup:** done. One-sentence setup, "3 + Tamsin" cell, asterisk gone;
  ch12-solutions now says Tamsin instead of "the backfill".
- **P9 (medium), week conventions:** done for Ch 15 (week 19), Ch 16 (week 19; weeks 14 to 16),
  Ch 17 (week 26). Did not add a glossary weeks link to every box (boxes kept to four lines).
- **P10 (medium), Ch 13 case:** done. Permissions extraction explained; exemption bullet and the
  "worked as designed" sentence rewritten.
- **P11 (medium), velocity and story points:** done. Defined in Ch 15 with the glossary link; Ch 17 and
  Ch 18 link at first use.
- **P12 (medium), Lenberg and Feldt percentages:** done, figures dropped ("stronger predictor of both").
- **P13 (low), "pawns or players":** glossed.
- **P14 (low):** done. "Document as you go" now has its context; flag-review standard and
  core/order-capture glossed in Ch 11; Rigby "expected loss" rephrased in plain words.
- **P15 (low):** done via the box line.
- **Patterns:** forward references glossed (Sprint Goal and Kanban board in Ch 11, lead time in Ch 13,
  refinement and release train in Ch 16, debt register in Ch 15); calibration distinguished from Ch 8's
  in Ch 17; Ch 18 missing blank line before `## CTO Perspective` fixed; Ch 14 team table labeled as
  baseline headcount (before the week 10 QA move); Ch 13 reference-list access notes removed.
- **Missing content:** added Ch 11 "Asking about safety directly" (paraphrased items, labeled as not a
  validated scale); Ch 12 a full six-item working-agreement set for a hypothetical team; Ch 16 the
  interrupt rotation; Ch 17 "Story points, planning poker, and t-shirt sizes" (no new sources); Ch 18 an
  illustrative CFO answer (hypothetical company).
- **Ch 17 F1 solvability:** the chapter now states Orders takes over core/customer in week 4.
- **Case trimming:** Ch 11 (Payments and Integrations section shortened, status line cut), Ch 12 (Data
  and Analytics opener: dropped 12 percent and the Sev count), Ch 14 (dropped lead time and change
  failure rate figures, notification-svc move), Ch 15 and 16 as above.

## Fact questions for the maintainer

1. `first-quarter.md` says "Billing reserves weeks 1 to 3 for the ledger export". Ch 16 now reads this as
   weeks 14 to 16 (the first three weeks of quarter 2). Please confirm, and consider writing absolute
   weeks in the record.
2. Ch 14's case says Customer Experience "has 15 engineers" and that two quality engineers joined in
   week 10. Is the week-14 headcount 15 or 17? The text leaves it as written.

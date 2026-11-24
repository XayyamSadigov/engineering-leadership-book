# Meaning check, batch 13: chapters 37 and 38

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 11:

1. Every doubt in `editing-ch37.md` and `editing-ch38.md` section 4 and in the translator's notes
   (`notes-t13.md`) gets a verdict.
2. Completeness: headings (37: 27; 38: 25), table lines (37: 62; 38: 60), list items (37: 33; 38: 39),
   ordered items (37: 24; 38: 20), exercises (8 each), Mermaid blocks (37: 3; 38: 2), admonitions
   (37: 2; 38: 4), and relative link targets (49 and 51, identical in order) match the English. No
   wrapped line begins with a number and a period outside a real ordered list. Paragraphs, table rows,
   exercises, reflection questions, takeaways, and reference lines were also checked by eye: nothing is
   missing. All admonitions keep their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar names and numbers were checked against the English.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 8 editor doubts plus the translator's notes checked; 1 editor doubt changed (ch 37 no. 2).
Further fixes from the full read: ch 37 ×2, ch 38 ×3.
Validation: `tools/validate_book.py` passed.

**Run rate.** Neither English chapter uses "run rate". Ch 37's "at the rate from week 16" means the
calendar's weekly load as it stood from week 16, not an annualized financial figure, so the editor's
«недельная нагрузка с недели 16» (both places) is right and no «в темпе» remains in either chapter. Outside
this batch, `baseline-data.ru.md` line 141 renders "Service credits at last quarter's rate" ($410,000 × 4,
an annualization) as «в темпе прошлого квартала»; the term base's run-rate entry («годовой темп
(run-rate)») may fit better there. Not changed (out of scope).

**Target band.** «целевой диапазон» is used in all four places (terms box, «Что обещает план», playbook
step 6, case). The term base should record it in place of notes-t13's «полоса целей».

## Chapter 37

| # | Doubt | Verdict |
|---|---|---|
| 1 | Perlow, 1999: «инженерам, которым приходится ждать своих руководителей» | ok. The English: "Scattered meetings cost the engineers who wait for their managers". |
| 2 | «Очередь выступающих ведёт сопредседатель» | changed. The English: "runs the question order", which is the order in which questions are taken, not a speakers' list. Now «Очерёдность вопросов ведёт сопредседатель…». |
| 3 | A2, «так, чтобы встреча не решала, у кого право на это решение» | ok. The English: "without the meeting deciding who has the decision right". |
| 4 | «Но главная экономия — на операционном разборе» | ok. The English: "The larger saving is in the operational review" (larger than the director's own 2.3 hours). |
| t13 | "most of them on-call leads" refers to attendees | ok. |
| t13 | Kauffeld, "as the abstract reports it" → «в изложении аннотации» | ok; label kept at research finding. |
| t13 | Grove's "operation reviews" → «операционные обзоры» | ok. |
| t13 | skip-levels gloss «встречи с подчинёнными своих руководителей» | ok. |
| t13 | "45 to 90 min" → «От 45 до 90 мин» in the table | ok; numbers verbatim. |

Further fixes:
- Trade-offs, breadth against depth: "a routing rule … replaces the director's presence" had become
  «Присутствие директора заменяет правило маршрутизации», which in Russian word order reads as the
  presence replacing the rule (the reverse). Now «Вместо присутствия директора работает правило
  маршрутизации: что форум сообщает и кому».
- Why this matters: "deciding cross-team disputes" had become «улаживать» (smoothing over). Now
  «разрешать межкомандные споры».

Full read: no other drift. The opening, the related-chapters box, the three scales (80 engineers;
Mankins's 300,000 hours as expert opinion), the objectives, the mental model and loop diagram, the three
practitioner classics (expert opinion), the four components (this book's synthesis), the seven-jobs table
(this book's recommendation; 49 of 60 minutes), the research bullets (Rogelberg et al. and Allen and
Rogelberg as research finding, self-reported and correlational; Kauffeld 92 meetings; Mroz; Perlow et al.
23 and under 10 hours as expert opinion), Perlow 1999 and Gibbs et al., the no-study paragraph, the five
design choices (Lu et al. 65 experiments, Stasser and Titus, the inference caveat; Lencioni), the audit
steps, the info box (week 20; 30 to 21; weeks 19 and 26), the matrix (six topics, TR-01 to TR-09), ADR-0001
and core/permissions, 38 items and 5 decisions, 42 of 60 minutes, 16 attendees and 20 person-hours, the
calendar table (16.3), one-on-one lengths, 9.5 and 25 of 47 hours, the decision diagram, the horizon
table, the business review, four trade-offs, seven failure modes and the accretion loop, the enterprise
default (12 to 16 hours), the three site rules, the CTO section, the 11-step playbook, the charter, the
case (redesign table to 14.0; 20 to 10.5 person-hours; 4.1 to 4.6 hours; Kwame Mensah; week 27 talent
review; Elena Sokolova, Tom Becker, Daniel Cho and Bogotá), all exercises, reflection questions,
takeaways, and references match.

## Chapter 38

| # | Doubt | Verdict |
|---|---|---|
| 1 | «CFO при неизменных операционных расходах» | ok. The English: "A CFO with flat operating expense". |
| 2 | Invisible unfunded list, «пункты, которых нет в списке, будут сделаны» | changed. The English: "Requesters assume unlisted items are coming": items never written down as unfunded. «которых нет в списке» pointed at some existing list. Now «Раз пункты нигде не записаны как непрофинансированные, заказчики считают, что они будут сделаны». |
| 3 | «триггер недели 31 не даёт принять это на веру» | ok. The English: "the week 31 trigger keeps it honest": the fall in unplanned work is checked, not assumed. |
| 4 | «их сводят вручную и помечают это оговоркой» | ok. The English: "from hand-joined numbers, with that caveat beside them". |
| ed. | «пессимистичный сценарий» in the mental model | ok as a translation: the English says "pessimistic case" there. See English problem 1. |
| t13 | "The scorecard becomes a few exposures" → «сжимается до нескольких чисел на виду у совета» | ok; the next sentence ("A board needs four or five numbers") supports the reading. See English problem 2. |
| t13 | "99.9 percent" kept in the OKR table | ok; table numbers verbatim. |
| t13 | "disputed" → «вопрос спорный» | ok; follows the maintainer's decision for "contested". |
| t13 | Locke and Latham, "as the reviews' abstracts report it" | ok; label kept at research finding. |

Note: the editor's verdict on doubt 2 changed only the wording, not the claim; the English table row
("Requesters assume their items are coming") and the failure mode now read consistently.

Further fixes:
- Info box: "near the end of quarter 2" (week 25 of 26) had become «конец квартала 2». Now «ближе к концу
  квартала 2».
- Invisible unfunded list: see doubt 2.
- F3: "A team lead" had become «Техлид». The term base has «тимлид» for team lead and «техлид» for tech
  lead. Now «Тимлид».

Full read: no other drift. The opening, the related-chapters box, why this matters (42 percent; CFO and
CPO), the objectives, the mental model and terms box (13-week quarter, 1 FTE-quarter = 13 engineer-weeks,
10 ÷ 1.25 = 8), the three ideas, the scorecard areas table, the two carried-over rules (Grove credited with
paired indicators), row owner and data steward, about ten entries, DORA's warning (industry research,
99.9 percent by contract), OKRs (Doerr, practitioner consensus), Locke and Latham (research finding),
Ordóñez et al. and the reply (disputed), Stray et al. (research finding: one project, interviews, no
performance outcome; no controlled study found), the recommendation, the bad and good OKRs, the planning
diagram and shortcut table, the unfunded list, the four allocation questions (26 percent trigger), the
Chapter 27 link, the example (info box 30 to 21, 34 to 31 percent; inputs 77 + 3, 22 and 28 percent, 8
from 12 FTE, Platform Operations five engineers; assumptions 22.4 FTE, 3 + 1.5 FTE, 0.6 FTE-quarters, 15 to
35 percent and 1.25, 24 items and 62 FTE-quarters; the capacity table; 35.6, 463, 3.8, 22.6 and 36
percent; 560 engineer-weeks and 43; a third below), the prevention table and its paragraph (week 10, 6 of
11 recurrences, 10 percent, 2 FTE security), the decision loop and sizing table, the guardrails and three
tests, five trade-offs, six failure modes, the enterprise ownership table and calendar, the CTO section
($46,250, $185,000, $814,000), the 10-step playbook, the case (Greg Tanaka, the eight-row scorecard and
stewards, five or more respondents, the six complications, the five decisions), all exercises, reflection
questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 38, The Mental Model, third idea**: "commit what the pessimistic case can deliver" uses a term the
   chapter does not define; the defined term two paragraphs earlier is "cautious case" (also in the
   heading sentence "a promise funded by the cautious case"). Suggest "commit what the cautious case can
   deliver". The Russian mirrors the English («пессимистичный сценарий»).
2. **Ch 38, CTO Perspective**: "The scorecard becomes a few exposures" is unclear ("exposures" usually means
   risk exposure). Suggest "The scorecard shrinks to a few board-level numbers".
3. **Ch 38, Failure Modes, the invisible unfunded list**: "Requesters assume unlisted items are coming" can
   be read as items missing from some list. Suggest "Requesters whose items appear on no list assume they
   are coming".

# Meaning check, batch 11: chapters 35 and 36

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 10:

1. Every doubt in `editing-ch35.md` and `editing-ch36.md` section 4 and in the translator's notes
   (`notes-t12.md`) gets a verdict.
2. Completeness: headings (35: 24; 36: 27), table lines (35: 64; 36: 69), list items (35: 47; 36: 56),
   exercises (8 each), Mermaid blocks (35: 2; 36: 3), admonitions (1 each), and relative link targets
   (identical in order) match the English. No wrapped line begins with a number and a period outside a
   real ordered list (ordered-item counts 18 and 27, as in the English). Paragraphs, table rows,
   exercises, reflection questions, takeaways, and reference lines were also checked by eye: nothing is
   missing. Both "Northstar so far" admonitions keep their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar and Halvard names and numbers were checked against the English
   and, for Priya Raman's condition, against `first-quarter.md` and its Russian page.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 10 editor doubts plus the translator's notes checked; 1 editor doubt changed (ch 36 no. 2) and
1 translator note corrected (ch 35, Priya's condition). Further fixes from the full read: ch 35 ×5,
ch 36 ×5.
Validation: `tools/validate_book.py` passed.

## Chapter 35

| # | Doubt | Verdict |
|---|---|---|
| 1 | Fernwick: CTO and cofounder one person or two | ok as edited. The English says "the cofounder CTO": one person. «CTO (техническому директору) — сооснователю компании, который…» is right. |
| 2 | «дежурит за всю систему» | ok. The English: "is on call for everything". |
| 3 | Case, «ведь» before the colon clause on option D | ok. "would answer a breakage not yet observed: managers get monthly development time, and cross-team decisions are not queuing": the colon clause is the evidence that the breakage is absent. |
| 4 | Opening, «какие будут команды» | ok. "which teams exist" in a design being produced. |
| 5 | «в часовых поясах с общими рабочими часами» | ok. The English: "on one site or in overlapping hours". |
| t12 | Case table, "her stated condition, after week 26, is met" → «её условие, поставленное после недели 26» | fixed. The condition is to take the module after week 26 (`first-quarter.md`: "Priya Raman would accept it after week 26"), not a condition stated after week 26. Now «её условие — после недели 26 — выполнено», matching `first-quarter.ru.md`. |
| t12 | "Signal:" / "Detection:" → «Признак:» / «Как заметить:» | ok. Label choice for the maintainer. |
| t12 | Brackenridge arithmetic cell translated, "8 to 9" → «8–9» | ok; numbers unchanged. |
| t12 | "engineering executive" → «руководитель разработки высшего уровня» | ok. |

Further fixes:
- Nagappan et al.: "made a large share of its edits" had become «заметную долю», which is weaker. Now
  «большую долю».
- Dingsøyr et al.: "meetings and forums in use, changing over time" had become «форумов, состав которых
  менялся», which reads as the forums' membership. Now «набор которых менялся».
- Enterprise application: "measured waste is the cleanest argument" had become «самый весомый довод»
  (weightiest). "Cleanest" means least open to dispute. Now «самый бесспорный довод».
- CTO perspective: "proportionate to the shared estate" had lost "shared". Now «общему технологическому
  ландшафту».
- Case totals: "7 managers (one of them an engineer-turned-manager)" had become «один из них — бывший
  инженер», which fits most managers and loses the point (Mateo is newly promoted). Now «один из них —
  инженер, только что ставший руководителем».

Full read: no other drift. The opening and its cross-references, the three scales (11, 24, 41 days; three
Core modules; three staff engineers), the mental model and loop, the three inputs, Brooks (upper bound),
Conway, Nagappan et al. (research finding, one system, no generalization), the evidence-gap paragraph
(practitioner consensus; this book's recommendation), the band table, Fournier, the sites rules (this
book's recommendation), Larson, GitLab (one company's practice), the sequencing diagram and its
recommendation, the four illustrative organizations (Fernwick 7/7/6; Brackenridge 43 + 5 + 2; Ashgrove
48/40/8/2, three quarters of links, triggers at a third and eight teams; Halvard 62.5, 10.5, 5 VPs, 7
principals, 70 engineers and 14 percent), Dingsøyr et al. (research finding, one case), the three
functions at 500, the decision table and rules, five trade-offs, six failure modes (46 percent, 29 of 86,
QA group), enterprise practices (1.5 FTE), the CTO section, the 12-step playbook, the case (info box,
87 people, 9 then 10 direct reports, the proposal and alternative tables, option C's 9/6 split, 4 links,
58 merge requests, the test table, 21 of 38 merge requests), all exercises, reflection questions,
takeaways, and references match.

## Chapter 36

| # | Doubt | Verdict |
|---|---|---|
| 1 | «только если пройдены все три проверки» | ok. "reorganize only when three tests pass" means all three. |
| 2 | «через два квартала их всё ещё 26» (was «стало только 26») | fixed. The English: "they fell only to 26" (forecast 30 → 18). «всё ещё 26» implies the number had been 26 before; «стало только 26» read as "only 26" (a good result). Now «их число снизилось лишь до 26». |
| 3 | «ощущение справедливости, ценность которого показывают те же данные» | ok. "the sense of fairness, which the same evidence values": de Jong et al.'s procedural justice. |
| 4 | Takeaway on cover | ok. The English has exactly two cover conditions plus "no person should cover two roles"; all three are in the Russian. |
| 5 | Succession summary: Payments counted as covered | ok as a translation: the English counts Orders, Payments and Integrations, and Customer Experience. The edge case is in the English; see English problem 1. |
| t12 | "mobile-bff and mobile boundary" → mobile app | ok; mobile-app is the other component moving with Mobile. |
| t12 | "shadow incidents" → «участвуют в инцидентах как наблюдатели» | ok. |
| t12 | "Payments then falls to its tech lead" → «Тогда Payments переходит к техлиду команды» | ok. |
| t12 | "remote audience of a room" | ok. |
| t12 | "evidence on failure rates is thin" → «данные о доле провалов слабые» | ok. |
| t12 | truck factor glossed «он же bus factor» | ok; follows the maintainer's decision in the term base. |

Further fixes:
- Failure modes, the perpetual reorganization, and reflection question 4: "how many managers a typical
  engineer has had in two years; three or more…" had become «сколько руководителей сменилось», which
  counts changes, not managers (three managers are two changes). Now «сколько руководителей было» in
  both places.
- Coverage rule 3: "or is the main cover for one" had become «не служит основной заменой на ней», which
  points back at the role already held. Now «для другой такой роли».
- Case, Mobile's development action: "a senior mobile engineer" had become «опытный мобильный инженер».
  Now «senior-инженер из мобильной команды», per the term base.
- X2: "Elena Sokolova…, whose team would then fall to an informal tech lead, with Victor above" had
  become «…а над ней будет Victor», where «ней» can read as the team. Now «Elena Sokolova (…) под
  началом Victor, а её команда тогда перейдёт к неформальному техлиду».

Full read: no other drift. The opening (Chapter 58 for layoffs and mergers), the three scales, the
mental model and both diagrams, de Jong et al. (39 longitudinal studies, the intervening factors, the
caution on mergers and well-being), Oreg et al. (79 studies), Mockus (one observational project),
consulting surveys not used, the three tests, Larson (expert opinion), the cost table and the Mockus
risk line, the three rules for finishing, Lencioni and Watkins (expert opinion), the announcement
skeleton and FAQ (this book's recommendation), evolution and its limits, reversal (this book's
recommendation), the dip/misfit split and response table, Berns and Klarner, Rigby et al. (research
finding about code, 15 percent; the manager inference labeled as this book's), the readiness table and
coverage rule, the 60-engineer example (42, 18, 9.6, about 70; 780 and 9 percent; payback 0.75, 2.9, 7),
the decision table and gate diagram, four trade-offs, six failure modes, enterprise application, the CTO
section, the 11-step playbook, the case (info box, proposal, 17 reports, two Sev2 incidents, transition
table 2.5/6/1/7.4/3.8, 21 of 1,040, Mateo's 13 engineer-weeks, the week 45–64 plan, announcement order,
the succession table and its 0/6/4 totals, the week 49 step, Teodora and Sunil), all exercises (Daniel
Cho, Marcus Oyelaran, Teodora Vasquez-Lund, Hannah Lindgren, Victor Lindqvist, Rajiv Menon, Elena
Sokolova), reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 36, Case, succession summary**: Payments and Integrations is counted as covered although its
   only name (the informal tech lead) is also the in-development name for the staff data and
   integration role, and inherits Payments if Elena covers the director. Rule 3 ("neither … is the main
   cover for one") arguably holds, since development is not main cover, but the table's last row makes
   Payments' cover depend on the director's. Suggest a sentence acknowledging this chain, or counting
   Payments as covered "on paper".
2. **Ch 35, Case table**: "her stated condition, after week 26, is met" is ambiguous (stated after week 26,
   or met after week 26). The canon means the condition was to take the module after week 26. Suggest
   "her condition, to take it after week 26, is met".
3. **Ch 35, Case, starting point**: "Northstar's 80 engineers sit in six teams plus 3 staff engineers"
   reads as 80 + 3; the teams hold 77 and the 80 include the staff engineers. Suggest "Northstar's 80
   engineers are 77 in six teams plus 3 staff engineers". The Russian mirrors the English.

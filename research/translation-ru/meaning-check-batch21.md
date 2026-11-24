# Meaning check, batch 21: chapters 55 and 56

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 20:

1. Every doubt in `editing-ch55.md` and `editing-ch56.md` section 4, the term proposals (section 3), and
   the translator's notes (`notes-t22.md`) get a verdict.
2. Completeness: headings (26 each, anchors equal to the slugified English headings), table lines
   (55: 82; 56: 49), list items (55: 57; 56: 37), ordered items (55: 19; 56: 22), exercises (8 each),
   Mermaid blocks (3 each), admonitions (2 each), relative link targets (55: 55; 56: 78, identical in
   order) and citation link texts (55: 26; 56: 37) match the English. Every number in table lines is
   identical to the English (the checker's three hits are trailing commas after "2", "9", "90"). Wrapped
   lines that begin with a number and a period are all items of real ordered lists (41 = 19 + 22). Table
   rows, exercises, reflection questions, takeaways, and reference lines were also checked by eye:
   nothing is missing.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar and Halvard names and numbers were checked against the English. In
   chapter 55 every governance and legal statement (board powers, oversight versus management, the NACD
   advice, the Yahoo/Altaba SEC findings and the Verizon amendment, the deal-terms box, the
   surviving-diligence rules) was checked for strength and hedges.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 10 editor doubts, 6 term proposals, and the translator's notes checked; none led to a change.
Further fixes from the full read: ch 55 ×3, ch 56 ×5.
Validation: `tools/validate_book.py` passed.

## Chapter 55

| # | Doubt | Verdict |
|---|---|---|
| 1 | «…иллюстрирует публичная история взлома Yahoo» (editor added "Yahoo") | **Kept.** The English sentence says only "is a breach", but the next lines ("According to the SEC: Yahoo's security team…") identify it as Yahoo's breach. The addition names what the English names one line later and adds no claim. |
| 2 | «обещанная клиентам надёжность» for "the reliability sold to customers" | ok. The chapter itself defines it as reliability "in their contracts"; "sold" is the contractual promise. |
| 3 | «для решений, которые связывают больше квартала ресурса» | ok. The English "commit more than a quarter of capacity" has the same ambiguity (25 percent of capacity, or capacity for more than a quarter); the Russian keeps it. See English problem 1. |
| 4 | de Wit: «сильнее положительно связаны с результативностью» without a comparator | ok. The English: "found disagreement about the task more positively related to performance in top management teams", also without an explicit comparator. See English problem 2. |
| 5 | «Если факт окажется ложным» | ok; the English "If it proves false" refers to the fact. |
| term | «эксперт в совете» allowed in prose | Not changed; maintainer decision. «член совета — эксперт» is clear where it stands. |
| term | «чем рискует компания» for exposure in prose | Not changed; maintainer decision. Meaning intact. |
| term | «ошибка оценки по исходу (outcome bias)» | ok. |
| t22 | Term list (подверженность риску, член совета, решение до заседания, тезис сделки, компания-цель, data room, гарантия / возмещение убытков / эскроу, условие закрытия сделки, существенное неблагоприятное изменение, копилефт, исход, разногласия по существу задачи, особое мнение, триггеры пересмотра, дата разбора, failure-mode names) | ok; consistent through the chapter. |
| t22 | "Two **standards**" → «по двум **стандартам**» | ok. |
| t22 | Yahoo "failed to maintain controls" → «не было работающих механизмов контроля» | **Fixed** (see below). |
| t22 | Source note inside the documented-practice label | ok. |
| t22 | "Six top-40 renewals", ADR-0001 feminine, F3 "decision framework" as the section's table | ok. |

Further fixes:
- Ethics, three tests: "Would the page lead a careful director to believe something you know is false?"
  had become «…в то, что вы считаете ложным», which weakens "know" to "believe". Now «…поверить в то,
  что, как вы знаете, неправда?»
- Yahoo bullet: "Yahoo had failed to maintain controls ensuring …" had become «У Yahoo не было работающих
  механизмов контроля…», stronger than the SEC's finding (it says the company failed to maintain
  controls, not that it had none). Now «Yahoo не поддерживала механизмы контроля, которые гарантировали
  бы…».
- Case: "The exposure table from the example" had become «Таблицу рисков из примера», which reads as the
  risk register. Now «Таблицу перевода на язык риска из примера».

Governance and legal claims, checked one by one: the board's formal powers (appoints and evaluates the
CEO; approves strategy, the operating plan, major transactions; oversees risk; represents the investor in
a private company); NACD (quantitative terms, at least quarterly, thresholds for between-meeting updates;
practitioner consensus, written for cyber risk); Keil et al. (research finding); the envelope rule and
"asking for cover"; the expert director and the transcript test; Larson 2024 and 2023 (expert opinion;
one vote, not a veto; acquisition thesis; deal-team incentives, sunk cost, unaudited compliance claims);
ISO/IEC 5230 and SBOM (standards); the deal-terms box (warranty, indemnity, escrow, closing condition,
material adverse effect, copyleft); the Yahoo case (documented practice; December 2014 intrusion,
hundreds of millions of accounts, disclosed 2016 during the Verizon sale, $35 million penalty without
admitting or denying; price down $350 million to about $4.48 billion, certain incidents disregarded for
MAE, certain liabilities split); the three surviving-diligence rules (this book's recommendation); Baron
and Hershey (research finding, student subjects); de Wit (correlational research finding); Bezos
(documented practice); Rogers and Blenko (expert opinion). All keep their strength.

Full read: no other drift. The opening, related chapters, three scales, objectives, mental model and
three diagrams, the arrow table, the Northstar example (week 48; 14 = 2 + 12 against 30; 99.89 against
99.9; $60,000; 25 percent; 13 of 15; the translation table; 6 FTE about $1.11M plus $150,000; the Poisson
table and 0.59⁴ ≈ 0.12; the hypothetical diligence table with TR-01, 120 to 180 engineer-days, 12 ledger
tables, ADR-0001, 4 of 10 roles, 14 of 15 SBOM, 0 of 15 provenance; 11-year-old product), the decision
tables, four trade-offs, seven failure modes, the enterprise list, the CTO section and Halvard (five vice
presidents, Chapter 58), the 11-step playbook, the case (weeks 46 to 50; Helena Marsh, Anders Holm,
Natalie Brooks, Samuel Osei, Margaret Lin, David Ferrante, Kwame Mensah, Ines Carvalho; the draft record;
quarter 6, week 78), all exercises (F1 to X2, including F3's 87 seats and option C, A3's Joon Park and
webhook key, X2's 60-engineer target), reflection questions, takeaways, and references match.

## Chapter 56

| # | Doubt | Verdict |
|---|---|---|
| 1 | «Ставить диагноз новому руководителю приходится с их помощью» | ok. The English "has to diagnose through them" means relying on them and their information. |
| 2 | «вывод из кризиса (turnaround) с его кризисным режимом» | ok. The English: "a turnaround's crisis mode 'invites…'"; the crisis mode belongs to the turnaround. |
| 3 | «15 или меньше во втором квартале … выпадало бы» | ok. The conditional matches "If the underlying rate had not changed"; "a split of 15 or fewer" is the second quarter's count. About 1 in 8 is right for 38 events split at random. |
| 4 | «стабильной, но слабой» for "stable and poor" | ok; the contrast is implied in the English. |
| 5 | «первый квартал, когда число не превысило лимита мандата в 15 инцидентов» | ok; same as "at or below the mandate's 15". |
| term | «вывод из кризиса»: avoid «вывод» = conclusion | ok as done by the editor; no clash found in the final text. |
| term | gloss «метрики механизмов» once | Not changed; maintainer decision. The English gives the examples in parentheses at first use, and the Russian keeps them. |
| term | «работать через коучинг» | ok. |
| t22 | Term list (проваливается / деградация / работа ниже возможностей, вывод из кризиса / перенастройка, сортировка, остановить кровотечение, ригидность под угрозой, three loops, способности / доброжелательность / честность, keep/coach/move/replace, два трека / двое часов, журнал обещаний, созвон по инцидентам, график координаторов, направления, failure-mode names) | ok; consistent through the chapter. |
| t22 | Watkins quotation, "the one promise", "senior individual-contributor track" | ok. |

Further fixes:
- Opening: "outages written into contracts" had become «сбои, за которые приходится платить по
  контрактам», which adds payment. Now «сбои, нарушающие условия контрактов».
- Case: "two renewals worth $9M a year named reliability as their concern" had become «…своей главной
  заботой» ("main concern"), an added claim. Now «клиенты указали, что их беспокоит надёжность».
- F3: "is weak evidence about him" had become «слабое доказательство против него лично», which adds a
  direction. Now «слабое доказательство, когда речь о нём самом».
- CTO Perspective: "the rescuer may not be the one to run it afterwards" had become «спасатель не
  обязательно должен потом ею руководить» ("is not obliged to"). Now «спасатель не обязательно подойдёт,
  чтобы руководить ею потом».
- CTO Perspective: the step "converge" had become «консолидировать», which overlaps the preceding "hold
  the gains". Now «выйти на целевой уровень». See English problem 3.

Studies and arithmetic, checked one by one: Watkins 2003 and 2014 (expert opinion; quotation); Trahms et
al. (research finding about the literature); Repenning and Sterman (research finding, case studies and
models); Staw et al. (research finding, review across levels); Smith and Keil (no label, as in the
English); DORA generative culture (industry research); Mayer et al. (expert opinion); Kim et al. 2004;
Dirks and Ferrin (106 studies; research finding); Weick (expert opinion); the findings table (Lazear,
Hoffman and Tadelis: single firms; Theeboom, Jones: mostly willing participants, over months; Mockus:
one project; Felps: review and model); Lencioni (expert opinion). Halvard example: 90 engineers, 11
manager seats (two vacant), Rhys Gallagher 6/50, Beatriz Quintero 5/40, Hiroshi Takeda, Ngozi Adeyemi;
9, 16, 23 (15 + 8); 14, 11, 7; 99.71 against 99.9, 380 against 131 minutes; 3 escalations, $4.2M, week
30; 17 of 90 against 11, 11 from Pay Calculation; 45 percent, 40.5 FTE, $8.3M; 6 of 22; 5 of 12, 4 of 11,
9 of 14; 131,040 minutes, 12 percent, $205,800; seven Sev1 bridges; eight commanders trained in weeks 2
and 3; six stay interviews; day 90: 23 → 15, 11 → 6, 3 → 1, two leavers, 38 = 19 + 19. Northstar case:
99.62 against 99.9; $410,000; $9M; 19 of 30; 40 to 44 percent; 24 components, 11 criticals, 3 exploited;
12 FTE; 54 of 64 pages; 25 percent; weeks 14 and 15; Tomasz Wierzbicki in week 20, 20 percent; the
manager table (Priya Raman 18 of 40 hours, 8/10/12 against 8; Marcus Oyelaran 55 percent; Elena
Sokolova; Daniel Cho 6 of 8; Farah Haddad; Tom Becker 31 of 74); results 30, 21, 17, 14; 99.89; $60,000.
Exercises (F1 52 rules, 1.5 FTE, 143 items; F3 34 percent; A1; A2; A3 five stakeholders; X1 day 120; X2
week 47, 200 words), reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 55, Enterprise Application**: "decisions that commit more than a quarter of capacity" can mean 25
   percent of capacity or a quarter's worth of capacity. The Russian keeps the ambiguity.
2. **Ch 55, Task conflict**: "more positively related to performance in top management teams" has no
   explicit comparator (than in other teams). The intended contrast could be stated.
3. **Ch 56, CTO Perspective**: the steps "stop the bleeding, hold the gains, converge" leave "converge"
   undefined (converge on what?). The Russian reads it as reaching the target level.
4. **Ch 56, Opening**: "outages written into contracts" is compressed; it presumably means outages that
   breach contractual availability.
5. **Ch 55 and 56, overlong source lines** (55: playbook item 10, takeaway 4; 56: several, as notes-t22
   lists). Cosmetic.

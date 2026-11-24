# Meaning check, batch 19: chapters 49 and 50

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 17:

1. Every doubt in `editing-ch49.md` and `editing-ch50.md` section 4 and in the translator's notes
   (`notes-t19.md`) gets a verdict.
2. Completeness: headings (49: 27; 50: 28, anchors identical in order), table lines (49: 47; 50: 65), list
   items (49: 44; 50: 35), ordered items (49: 22; 50: 27), exercises (49: 8; 50: 9), Mermaid blocks (2
   each, node ids unchanged), admonitions (1 each, body indented under the title), and relative link
   targets (49: 54; 50: 62, identical in order) match the English. Paragraph blocks pair one to one (49:
   126; 50: 123). Every number in table lines is identical to the English (four apparent differences are
   trailing commas caught by the token script). Wrapped lines that begin with a number and a period are
   all items of real ordered lists, as in the English. Table rows, exercises, reflection questions,
   takeaways, and reference lines were also checked by eye: nothing is missing.
3. Meaning: every paragraph and table row of both chapters was read side by side with the English.
   Evidence labels were counted and checked one by one (49: research findings 1, this book's
   recommendation 1, illustrative 2, fictional 1; 50: expert opinion 6, research finding 2, this book's
   recommendation 7, illustrative 2, fictional 1; all present in the Russian). Northstar and Halvard names
   and numbers were checked against the English.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 11 editor doubts plus the translator's notes checked; 3 led to a change (ch 49 doubts 3 and 5,
ch 50 doubt 4). Further fixes from the full read: ch 49 ×1, ch 50 ×1.
Validation: `tools/validate_book.py` passed.

## Chapter 49

| # | Doubt | Verdict |
|---|---|---|
| 1 | «программа, вероятно, неверно определила этап» | ok. The English: "A year two that is a list of tools to buy has probably mistaken its stage", i.e. misjudged what the stage is for. |
| 2 | «оставшуюся работу не подкрепляет ни один сбой» | ok. The English: "the remaining work has no outage attached to it". The rebuilt Kotter sentence ("a budget cycle in which nobody declares anything and the allocation shrinks") also keeps the meaning. |
| 3 | Page one, «скользящая сумма инцидентов показывает, что за второй год мы уложимся в 40» | Fixed. The English: "the rolling incident total on course for at most 40 over year 2", a trajectory, not a demonstrated result. Now «скользящая сумма инцидентов идёт к тому, чтобы за второй год уложиться в 40». |
| 4 | Case, «простой за квартал оказался примерно на 13 минут больше допустимого» | ok. The English: "Availability missed by about 13 minutes of downtime in the quarter". Check: 99.9 percent of a 91-day quarter allows about 131 minutes; 99.89 percent is about 144, so about 13 minutes over. Direction and unit right. |
| 5 | «релизы стали меньше, но не безопаснее» | Fixed. The English says "smaller"; «меньше» also reads as "fewer". Now «мельче». |
| 6 | «Поэтому его первый абзац говорит…» | ok. The English links the two sentences implicitly ("a proposal differs because it asks for a decision. Its first paragraph states…"); «Поэтому» states the same link. |
| t19 | "funding an unexplained miss is escalation" → «эскалация приверженности» | ok; the term the chapter introduced earlier. |
| t19 | "do not trade away the floor in the room" → «нижняя планка» | ok. |
| t19 | "the CTO decides whether to sponsor the proposal or present it" | ok; rendered as back it or present it in person. |
| t19 | Table «год 1», «год 3», «предложение по организации на год 2» | ok; glossary rule 6. |
| t19 | New terms (контрольная точка, пересмотр объёма, цена отказа, финансирующие, направление работ, failure-mode names) | ok; consistent through the chapter. |
| ed. | Term proposals: «где на кону реальный результат», «обмен услугами» | ok; both keep the meaning ("real stakes"; Yukl's exchange tactic). |

Further fixes:
- F1: "For each, describe how it could be met on paper…" refers to each of the six exit criteria (the
  worked solution covers all six). The Russian had narrowed it to «Для каждого из этих двух», the two
  quoted examples. Now «Для каждого критерия».

Full read: no other drift. The opening (ninety-day mandate; four skills; two-year continuation), the three
scales, the objectives and related chapters (27, 46; 43, 39, 51), the mental model and stage diagram, the
"partly" branch, the success paradox ($410,000 to $95,000 in quarter 2; Kotter), Staw, Flyvbjerg (optimism
bias versus strategic misrepresentation), Cooper and the book's transfer, the fundable-stage table, exit
criteria and pairing, Rumelt and Kane et al., Dutton and Ashford, Dutton et al. (82 accounts; research
findings about beliefs, not a test), packaging (25 to 18 percent, 5.6 engineers, about $1M), Minto, the
cost of no, Keil et al., the sample page one (week 51; 6 of 80; $150,000; week 56; six of 40 customers;
30 to 14; $410,000 to $60,000; 99.89 against 99.9; $555,000; week 78; $25,000), the decision meeting
(this book's recommendation; two days; objection table), constructive politics (Pfeffer; Lencioni),
Ferris et al. and Munyon et al. (correlational, individual outcomes), Chang et al. (moderate to strong;
weaker for performance; correlations), the three tests, Yukl and Tracey, succession (Berns and Klarner;
Chapter 41), the example (week 45; 8 FTE of 80; $185,000; $46,250; $250,000 discretionary budget; the cost
table $1,017,500 and $1,267,500; 7.5 percent; the value table; $1.64M; change failure rate 31, 22, 23),
the gate diagram and table, five trade-offs, seven failure modes, the enterprise section (50 to 150
engineers), the CTO section (Halvard, five vice presidents, half-yearly gate; Chapter 47), the 11-step
playbook, the case (weeks 45 to 51; the measures table; 13 minutes; week 46 organization decision; stages
table; exit criteria and the 14 tier 1 footnote; the stage 2 reading rule, a third of the time, 40, four
weeks, Victor Lindqvist; open items; the six funders and Greg's week 47 offer; 2 of 6 FTE, $185,000; the
three decisions), all exercises (F1 six criteria; F2 $1,267,500 and $250,000; F3 13 incidents, 99.88
percent; A1; A2 four roles, week 78; A3; X1; X2 three of five VPs), reflection questions, takeaways, and
references match.

## Chapter 50

| # | Doubt | Verdict |
|---|---|---|
| 1 | «Решение, возвращённое один раз, — это одолжение» | ok. The English: "A decision returned once is a favor"; the Russian is as open as the English. |
| 2 | Halvard, «ущерб от него в шесть раз масштабнее» | ok. The English: "does damage at six times the scale". The multiplier is not the five VP groups; it matches Halvard's size against Northstar's (500 against 80 engineers, about 6). See English problem 2. |
| 3 | «организация начинает работать так же долго, как он» | ok. The English: "the organization copies the hours", hours meant literally (the paragraph is about 50-hour weeks). |
| 4 | «даёт направлению своё место»; «Техническое направление задают семь principal-инженеров…» | First ok ("gives direction a home"). Second fixed: the English says "Technical direction runs through seven principal engineers and six enterprise policies", a channel, not an author (policies do not "set" direction). Now «Техническое направление проводят через семь principal-инженеров и шесть корпоративных политик». |
| 5 | Fournier, «прослеживает управленческую карьеру» | ok. The English: "Known for following the management track up to senior executive roles". |
| t19 | Early sign / Detection → «Признак:» / «Как заметить:» | ok; follows the English field names (see English problem 3). |
| t19 | "one-on-one" spelled out in the hours table | ok. |
| t19 | "reaches you only for customer commitments or the director's budget authority" | ok. |
| t19 | Larson 2023c → «худший из двух провалов» | ok; the chapter compares exactly two failures. |
| t19 | New terms (остаток, вердикт, шов, получатель, класс решений, первая/вторая команда, failure-mode names) | ok; consistent through the chapter. |
| ed. | «меры контроля», «высший руководитель», «сигнал без фильтров» | ok. |

Further fixes:
- Shared-decisions table, last column of the questionnaire row: "an evidence library owned by Joon Park,
  with Kwame Mensah as engineering evidence owner" had become «библиотеку доказательств во владении Joon
  Park и Kwame Mensah как владельца…», which reads as a library owned by both. Now «во владении Joon Park,
  а владельцем доказательств со стороны разработки — Kwame Mensah». Text only; the table's numbers are
  unchanged.

Full read: no other drift. The opening (seat, not a job; Victor Lindqvist, quarter 4), related chapters (47;
51 to 55), the three scales, the objectives, the mental model, the residual and the calendar ideas, Drucker
(expert opinion), Bandiera et al. (more than a thousand CEOs; research finding applied by analogy), the
decide/return/name loop, Berray via Vogels (four roles; expert opinion), Medcof, the organization builder
(50 to 400 engineers; Larson 2023a and 2024, expert opinion), the archetype table, the three questions (40
and 150 engineers), Larson 2020, Weill (more than 250 enterprises; research finding), the decision-rights
table and the seams paragraph, the seven "only the CTO" items, Aghion and Tirole, the CEO page (exercise
X2), delegation (Larson 2023c; Mintzberg), the two teams (Larson 2023d, Lencioni 2002), the rhythm diagram
and table, sampling forums, the example (week 47; 87 seats; 14 people under Marta Kowalczyk; Joon Park;
weeks 44 to 46; 20 of 48 hours, 7 recoverable, 2 hours about 4 percent; the hours table; 20.0 and 11.0; 11
rulings, 3/6/2; week 15 escalation path, five working days; Kwame Mensah, Li Na Zhou; week 14 and
ADR-0001; the keep/give/stop table, 7.0; 2 to 9 hours, about 19 percent), the decision diagram and table,
four trade-offs, five failure modes, the enterprise section (one fifth of the week), the CTO section
(Halvard: five VPs, four product groups and a platform organization, seven principal engineers, six
policies), sustainability (48, 14.5, 2, about 50 hours), the 9-step playbook, the first 90 days (Larson
2020; the 1–30/31–60/61–90 table; two traps; exercise A3), the case (no CISO; SOC 2; about 2 hours a week;
the shared-decisions table; three options, 14 people, week 50 audit committee; weeks 48, 50, 51), all
exercises (F1 120 engineers; F2; F3 90 engineers, six decisions; A1 Ines Carvalho; A2 11 requests 3/6/2;
A3 150 engineers, two directors; A4 70 engineers, month five; X1 weeks 48, 50, 51; X2 half the week, 87
seats), reflection questions, takeaways (4 percent), and references match.

## Possible problems in the English (not edited)

1. **Ch 50, Bandiera et al.**: "Its abstract links firm performance to…" is an access note in reader text,
   which CLAUDE.md section 7 asks to fold into the evidence label (same point as batch 17, problem 3 for
   ch 48). The Russian mirrors it («Согласно аннотации»).
2. **Ch 50, CTO Perspective**: "does damage at six times the scale" leaves the multiplier unexplained, and
   it sits next to "six enterprise policies" and "five vice presidents", so a reader may tie it to either.
   If it means Halvard's size against Northstar's (500 against 80 engineers), saying so would remove the
   ambiguity.
3. **Ch 50, Failure Modes**: one entry (shadow architect) has both "Early sign:" and "Detection:", the
   others only "Early sign:"; ch 49 uses "Early sign:" only. Same book-wide label question as notes-t12 and
   batch 17, problem 2.
4. **Ch 49, Decision Framework table**: "funding an unexplained miss is escalation" relies on the reader
   connecting bare "escalation" to "escalation of commitment" four sections earlier, while the book also
   uses "escalation path". The Russian spells out «эскалация приверженности».
5. **Ch 49, F1**: "For each" follows a sentence naming six criteria and quoting two; the solution treats
   all six. "For each of the six" would remove the ambiguity the Russian had fallen into.

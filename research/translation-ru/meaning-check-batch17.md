# Meaning check, batch 17: chapters 47 and 48

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 16:

1. Every doubt in `editing-ch47.md` and `editing-ch48.md` section 4 and in the translator's notes
   (`notes-t18.md`) gets a verdict.
2. Completeness: headings (27 each), table lines (47: 74; 48: 60), list items (47: 29; 48: 31), ordered
   items (47: 19; 48: 18), exercises (47: 9; 48: 8), Mermaid blocks (47: 2; 48: 3), admonitions (47: 2;
   48: 1), and relative link targets (47: 52; 48: 61, identical in order) match the English. Every number
   in table lines is identical to the English (two apparent differences in ch 48 are a trailing comma
   caught by the token script, not a number change). Wrapped lines that begin with a number and a period
   are all items of real ordered lists, as in the English. Table rows, exercises, reflection questions,
   takeaways, and reference lines were also checked by eye: nothing is missing. The admonitions keep
   their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar and Halvard names and numbers were checked against the English.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 11 editor doubts plus the translator's notes checked; 3 led to a change (ch 47 doubt 5, ch 48
doubts 1 and 2), plus the requested sync of the corrected English sentence in ch 47. Further fixes from the
full read: ch 47 ×3.
Validation: `tools/validate_book.py` passed.

## Chapter 47

| # | Doubt | Verdict |
|---|---|---|
| 1 | Upper echelons, «научный результат, но в статусе устоявшейся теории… а не измеренного эффекта в разработке» | ok. The English: "a research finding at the level of established theory about firms' top teams, not a measured effect in engineering". Label strength kept. |
| 2 | Keil, «переносить его за пределы изученных выборок нужно осторожно» | ok. The English: "research finding, from samples that need caution in generalizing". |
| 3 | «руководители отстающего направления говорят, что решения подолгу ждут директора» | ok. The English: "the area's managers say decisions wait on the director"; the area is the one that missed the commitment, and "wait on" means stalled pending the director. |
| 4 | Trade-offs, «Переводить людей стоит, если…» | ok. The English: "Use the first for mismatches expected to outlast a year"; the first is people moves. |
| 5 | X2, «чистый прирост всего на 20 мест» | Fixed. The English is neutral ("allows 20 net additions"); «всего» removed. |
| 6 | F2, "VP of Fulfillment" at Halvard | ok, no change: a hypothetical group, which `halvard.md` allows for exercises. |
| t18 | "the blind spot the director team lacks" → «какого взгляда не хватает команде директоров» | Fixed to match the corrected English ("the strength the director team lacks"): now «какой сильной стороны не хватает команде директоров». |
| t18 | Signal/Detection → «Признак:» / «Как заметить:» | ok; follows the English field names (see English problem 2). |
| t18 | New terms (направление, команда директоров, обзор портфеля, ресурс для инвестиций, поддерживающая работа, разрыв, притязания на ресурс, резерв директоров, VP-передатчик, зависимость от разбиения, время из первых рук) | ok; consistent through the chapter. |

Further fixes:
- Goals: "For a VP the narrowing is the design problem" had become «сужение — это и есть то, что нужно
  спроектировать» (the narrowing is what must be designed). The point is that goal design must counter
  the narrowing. Now «это сужение и есть задача, которую должна решить постановка целей».
- Example, option (b): "with coordination cost" had become «зато добавляется стоимость координации».
  «зато» introduces a compensating advantage, which turns the cost into a benefit. Now «но добавляется».
- Trade-offs: "work moves keep teams intact and add coordination" had the same «зато добавляет
  координацию». Now «но добавляет».

Full read: no other drift. The opening (Halvard of Chapter 35; Northstar's VP question), the three scales,
the objectives and related chapters (40; 41 and 42; 48; 50), the mental model, the two ideas and Chapter
4's "large director", Larson 2023a/2024 (expert opinion), the two role tables (this book's
recommendation; size ranges illustrative), Larson 2018 (four to six; expert opinion, without data),
upper echelons and the modest inference, Locke and Latham and Ordóñez et al., the two kinds of goal,
Larson and Lencioni (first team; expert opinion), the rhythm and decision-rights tables, the conflict
norm, the operating review (60 minutes), Keil et al. (60 percent), Aghion and Tirole, Larson 2023d, both
diagrams, Larson 2023b, Bardolet et al. (archival study and two experiments; research finding about
capital budgets; this book's extension), Staw, the assessment table and the director/allocation/boundary
sequence, the example (Nadia Brennan, VP of Commerce; 130 engineers, 16 managers; Owen Achterberg 5/41,
Selin Kaya 5/40, Joaquín Ferreyra 6/49; run work 32 FTE, 98 investable; six bets, 110 against 98, bets 1
to 5 = 96, 2 FTE reserve; the gap tables; option (c) 94 FTE), both decision tables, the trade-offs (four
enterprise deals, 20 FTE), six failure modes, the enterprise section (80 to 150 engineers), the CTO
section, the 9-step playbook, the case (week 45; 30 to 14 in quarter 3; week 44 draft, week 46 decision,
week 48 recommendation; 87 seats, 79 engineers and 7 managers, span of 10, Alternative D 77 and 9; the
evidence table 25 of 47 hours, 4.7 percent, 10 critical roles, 4 with no cover; Amara Okafor, CPO; four
options), all exercises (F1 220 engineers, two days a week; F3 30 percent; A1 four months, two months; A2
12 FTE; A3 three managers; A4 one quarter; X1; X2 five VPs, 20 net additions, 500 engineers),
reflection questions, takeaways, and references match.

## Chapter 48

| # | Doubt | Verdict |
|---|---|---|
| 1 | Rigby, «сокращало ожидаемые потери до 15 процентов» | Fixed. The English: "cut the expected loss by up to 15 percent", a reduction of at most 15 percent, not a reduction to 15 percent. Now «на величину до 15 процентов». Label (research finding, two projects) kept. |
| 2 | Case, «найм на начальный уровень по умолчанию из варианта B этот риск прямо не закрывает» | Fixed. The English: "B's entry-level default does not obviously reach it" (it is unclear whether it does), not "does not directly". Now «а неочевидно, что найм на начальный уровень по умолчанию из варианта B этот риск закрывает». |
| 3 | «каждое профинансированное место занято все недели года» | ok. The English: "every funded seat is filled every week"; a budget year is meant. |
| 4 | «Повышения переводят людей вверх, хотя никто не уходит» | ok. The English: "Promotions move people up without leaving", i.e. without creating a departure. |
| 5 | «у аппарата CTO был ещё и свой список обязательных правил, который никак не измерялся» | ok. The English: "the CTO's staff kept a further unmeasured list of musts". |
| t18 | Larson primer → «руководителя разработки высшего уровня» | ok. |
| t18 | Šmite "its abstract reports" → «согласно его аннотации» | ok as a translation; see English problem 3. |
| t18 | "Senior and above rises to 325 (65 percent)" as a count | ok. |
| t18 | "about 1 percent of the held-mix payroll of $102.9 million" | ok. |
| t18 | Facts table, "one currency and rounding" → «и валюты и округление — тоже один» | ok. |
| t18 | "Victor wants ledger risk first" → «хочет прежде всего снизить риск по ledger» | ok; the next sentence ("how to buy down the ledger risk") confirms the reading. |
| t18 | Option table numbers verbatim | ok; glossary rule 6. |
| t18 | Term proposal «скамейка подрядчиков» → «резерв подрядчиков» (editor) | Not changed: a term decision for the maintainer, not a meaning issue. |

Further fixes: doubts 1 and 2 above.

Full read: no other drift. The opening (quarterly plans against the stock; Halvard; flat headcount), the
three scales (8 of 80, median 15 weeks, 120 engineer-weeks, about 2.3 engineers), the objectives and
related chapters (38; 34, 20, 59), the mental model and stock-and-flow diagram, governance as a budget,
the six-part table, Larson 2024 (expert opinion), Berman and Knight, the illustrative 60-engineer skill
table, the three absorption limits (this book's recommendation), the vacancy formula, Brooks (expert
opinion), Mockus (research finding, observational), Rigby et al. (Chrome and Avaya; more than three
times), Hoffman and Tadelis (one firm), the level-mix forces, Emanuel et al. (one firm, working paper),
Herbsleb and Mockus (two and a half times; early 2000s), Šmite et al., Kroll et al. (1990 to 2012; 36
practices, 17 challenges), whole ownership and Chapter 14 (Minneapolis and Bogotá, one hour), the three
vendor tests, the externality test, RFC 2119 (standard, as an analogy), DORA change approval (industry
research, survey-based), CNCF (practitioner consensus), DORA 2024 (6 percent; cross-sectional), the
delivery rule and Chapter 44, Meyer and Rowan, the governance diagram, Williamson (theoretical model),
GitLab (documented practice), the example (130, 110, 100, 90 and 70; 62 percent; the level table; both
policy tables; 325, 65 percent; $1,060,000, $102.9 million; 38 hires, four hours, 26 weeks, about 2
senior engineer-years; about 60 contractors on two contracts; the six-policy table), the decision table
and layer diagram, five trade-offs, eight failure modes, the enterprise section (about 100 engineers;
five to eight rules), the CTO section (six policies; week 45, Chapter 47), the 10-step playbook, the case
(weeks 41 to 49; Rajiv Menon, CFO; 87 seats; 39/38/3; Minneapolis 52, Bogotá 16, remote 12; $110,000 and
$168,000; $427,000; 79 engineers; options A to D; Greg Tanaka, VP Sales), all exercises (F1; F2 62 to 65
percent; F3 six rules; A1 Farah Haddad, 11 engineers 4/5/2, about 5 and 6, Yusuf Demir, quarter 3; A2 Tom
Becker, four contractors, nine months, four services, 29 engineer-weeks, GitLab CI; A3 a seventh policy;
X1 quarter 5; X2), reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 47 lines 188 and 452; ch 48 lines 101, 209, 267 to 268, and 548**: overlong unwrapped source
   lines; cosmetic.
2. **Ch 47, Failure Modes**: several "Detection:" fields are countermeasures rather than detectors (for
   example "reallocation requests go only through the director team meeting"). Same book-wide label
   question as notes-t12 for ch 35. The Russian follows the English field names.
3. **Ch 48, Location strategy**: "A review of published global software engineering studies, its abstract
   reports, found…" is an access note in reader text, which CLAUDE.md section 7 asks to fold into the
   evidence label. The Russian mirrors it («согласно его аннотации»).
4. **Ch 47, Playbook item 9**: the continuation line is indented by four spaces (others by three);
   harmless. The Russian is normalised.
5. **Ch 47, Bardolet**: "applying it to engineering capacity is this book's extension" is not bolded as an
   evidence label, unlike the other labels; the Russian mirrors it.

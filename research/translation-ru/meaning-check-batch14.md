# Meaning check, batch 14: chapters 41 and 42

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 13:

1. Every doubt in `editing-ch41.md` and `editing-ch42.md` section 4 and in the translator's notes
   (`notes-t15.md`) gets a verdict.
2. Completeness: headings (41: 26; 42: 25), table lines (41: 59; 42: 31), list items (41: 32; 42: 30),
   ordered items (41: 18; 42: 22), exercises (41: 9; 42: 8), Mermaid blocks (2 each), admonitions
   (41: 1; 42: 2), paragraphs (41: 75; 42: 83), and relative link targets (49 and 46, identical in order)
   match the English. Every number in table lines is identical to the English. No wrapped line begins
   with a number and a period outside a real ordered list. Table rows, exercises, reflection questions,
   takeaways, and reference lines were also checked by eye: nothing is missing. All admonitions keep
   their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar names and numbers were checked against the English.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 10 editor doubts plus the translator's notes checked; 3 editor doubts led to a change (ch 41
no. 4; ch 42 nos. 2 and 3). Further fixes from the full read: ch 41 ×3, ch 42 ×3 (two of them one error
in two places).
Validation: `tools/validate_book.py` passed.

## Chapter 41

| # | Doubt | Verdict |
|---|---|---|
| 1 | Mental model, «достигаются руками других людей» | ok. The English: "arrive late, mixed with the system's, and through other people". |
| 2 | «новый руководитель может появиться, только если чьё-то инженерное место останется без замены» | ok. The English: "a new manager can come only from an engineering seat that is not backfilled". |
| 3 | Trade-offs, «Но место, оставшееся без замены, обходится дороже, и освобождается оно без предупреждения» | ok. The English: "a real cost under flat headcount; a vacancy with no cover costs more, without warning". The semicolon carries the contrast, so «Но» is faithful. |
| 4 | CTO, «Если у CTO все руководители оценены „Уверенно“» | changed. The English: "A CTO who finds every manager rated 'Solid'": the ratings are the directors', which the CTO discovers by asking. «у CTO» could read as the CTO's own reports. Now «Если CTO обнаруживает, что все руководители оценены „Уверенно“…». |
| 5 | Playbook 3, «по письменному правилу из той же главы» | ok. The English: "Run Chapter 40's skip-level rotation … under its written rule"; the rule is chapter 40's. |
| t15 | "One-on-ones held" → «Проведённые встречи один на один» | ok. |
| t15 | "on-site location" → «на территории компании» | ok. |
| t15 | "the senior engineering level the person's skills support" → «тот старший инженерный уровень, на который тянут навыки человека» | ok. |
| t15 | "None yet" → «Пока ничего» | ok; avoids the clash with the rating «Пока нет». |
| t15 | CTO glossed in the CTO Perspective, before X1 and the case | ok. |

Further fixes:
- Opening: "It covers coaching managers through skip-levels, reviews …, and delegated decisions" had
  become «как развивать руководителей». Coaching is the term of the section «Коучинг руководителей по
  трём каналам». Now «как вести коучинг руководителей».
- When a manager is not working out: "the returning manager fills an engineering seat, so plan the seat"
  had become «поэтому его нужно заложить в план», where «его» can point to the manager. Now «поэтому это
  место нужно заложить в план».
- Case info box: "late in quarter 2" (week 24 of 26) had become «конец квартала 2». Now «ближе к концу
  квартала 2», as in batch 13.

Full read: no other drift. The opening, the three scales (one-line job description; Daniel Cho; six
or eight people; flat headcount), the objectives, the mental model and loop diagram, the six-dimension
rubric (this book's recommendation), the four ratings and the three rules, Scullen et al. (research
finding; seven raters, 62 and 53 percent), Smither et al. (24 longitudinal studies, authors' suggestion),
Hoffman and Tadelis and Google re:Work (documented practice), the three channels and four questions, the
five control levels, Marquet and Wiseman (expert opinion), Yukl and Fu, Lacerenza et al. (research
finding as the abstract reports it; 335 samples), Day et al., Hill, Fournier, Zhuo, the bench (Benson et
al.; Ibarra et al.), the cost table (58.5, 19.5, 12, 90 hours; 15 percent of 47; eight leavers, 15 weeks,
$53,000, $3,558, $185,000), 5 of 36 cells, the decision flow and table, the two criteria, the
not-working-out options and five transition steps, four trade-offs, seven failure modes, the enterprise
section, the CTO section, the 10-step playbook, the case (week 22, 36 skip-levels by week 24, 77 team
engineers; the six-row ratings table and its counts 16/4/9/5/2; Marcus's six rows; Daniel's 17 reports
and three cells; Priya 8/10/12 hours and Aisha Bello; Elena; Farah 45 percent; Tom and Bram 31 of 74;
the quarter 3 plans at level 3), all exercises, reflection questions, takeaways, and references match.

## Chapter 42

| # | Doubt | Verdict |
|---|---|---|
| 1 | Enterprise application announces «четыре постоянных элемента», five bold items follow | The Russian mirrors the English, which also says "four standing pieces" and lists five (board, forum, named interfaces, interest map, relationship capital). Not changed; see English problem 1. |
| 2 | CTO, third point: added «Поэтому» | changed. The English places the two sentences side by side ("Third, the CTO's peers answer to the board for their own numbers … Persuasion in their terms, follow-through, and early escalation remain the core tools.") with no connective. «Поэтому» removed. |
| 3 | Crawford et al., «подразделения … работали хуже» | changed. The English: "membership of several teams at once went with lower unit performance". «работали хуже» is vaguer than the measured construct. Now «у подразделений, где сотрудники участвовали в нескольких командах одновременно, результативность была ниже». Still correlational; label kept at research finding as the abstract reports it. |
| 4 | Intro, «которую ни один человек не контролирует целиком» | ok. The English: "work that no one person controls". |
| 5 | Case forecast, «готово к неделе 44, а … — к неделям 45–47» | ok. Start week 34 + 10 weeks = week 44; the weeks are completion forecasts ("forecast weeks 44 to 47" in option 1). |
| t15 | "four standing elements" | see doubt 1. |
| t15 | "nine of the seventeen committed roadmap items" → «обещанных пунктов» | ok. |
| t15 | "Commit the targets too" → «Включите в обязательства и цели» | ok. |
| t15 | "Sofia had co-written the severity definitions" → «участвовала в написании» | ok. |
| t15 | "Chapter 39 records its decisions" → «записываются так, как описано в главе 39» | ok. |
| t15 | "sales operations" → «в отделе продаж (sales operations)»; "quota" → «план продаж» | ok. |

Further fixes:
- Trade-offs, limit against responsiveness: "A small reserved allowance for deal and escalation work,
  single-team only" had become «выделенная только одной команде» (given to one team). The English means
  the allowance covers only single-team work. Now «только для задач одной команды».
- Case, the director's recommendation: "a reserved deal allowance for small single-team requests" had
  become «зарезервировать для одной команды квоту» (the same error). Now «зарезервировать квоту на
  небольшие запросы по сделкам, посильные одной команде».
- Three practical consequences, coalition: "If it feels like ganging up" had become «если со стороны это
  выглядит так», which moves the judgment to outside observers; the English means how the affected party
  experiences it. «со стороны» removed.

Full read: no other drift. The opening and related-chapters box, why this matters (9 of 17, one shipped),
the objectives, the mental model, the two ideas, the portfolio definitions, Little's law (research
finding, a theorem, with the throughput assumption), the 4/8/12 illustration, DORA (industry research,
survey-based and correlational), Reinertsen (expert opinion), the four limit parts (this book's
recommendation), the intake diagram, the dependency table, Herbsleb and Mockus and Cataldo et al. (research
findings as the abstracts report them; the inference is the book's), Cagan and Jones, Fisher and Ury and
Cohen and Bradford (expert opinion), Yukl and Tracey and Higgins et al. (research findings), the escalation
section, the info box (30 to 21 to 17; week 26), the example (17 = 9 + 8; 7 shipped; 75 and 11 percent;
9 quarters; 11/24/41 days; 29 of 86 links, Billing 19), both decision tables, five trade-offs, six failure
modes, the enterprise section, the CTO section, the 10-step playbook, the case (17.6, 8, 4.5, 49.9 FTE;
463 engineer-weeks; the peers table; the four-row portfolio, 265 and 198; week 31, $700,000, 70
engineer-weeks, 7 a week, weeks 33, 34, 36, 44, 45 to 47, 15 to 35 percent; the three options; Amara,
Greg, Sofia, Rajiv, Victor), all exercises, reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 42, Enterprise Application**: "portfolio and cross-functional work needs four standing pieces",
   then five bold items follow (portfolio board, portfolio forum, named interfaces, interest map,
   relationship capital). Suggest "five standing pieces", or recast relationship capital as a separate
   paragraph after the four. The Russian mirrors the English («четыре постоянных элемента»).
2. **Ch 42, Enterprise Application, named interfaces**: "a policy for what it may bypass" is unclear; the
   intended sense is probably "a policy for what may bypass it" (which requests may skip the intake). The
   Russian reads it that way («что допустимо делать в обход него»).
3. **Ch 41, opening**: "coaching an individual in Chapter\n5" wraps the chapter number onto a new line
   (noted by the translator); harmless in rendering.

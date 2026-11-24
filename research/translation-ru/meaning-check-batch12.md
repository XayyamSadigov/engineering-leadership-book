# Meaning check, batch 12: chapters 39 and 40

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 11:

1. Every doubt in `editing-ch39.md` and `editing-ch40.md` section 4 and in the translator's notes
   (`notes-t14.md`) gets a verdict.
2. Completeness: headings (39: 27; 40: 28), table lines (39: 71; 40: 47), list items (39: 23; 40: 33),
   ordered items (39: 23; 40: 19), exercises (39: 9; 40: 8), Mermaid blocks (39: 3; 40: 2), admonitions
   (39: 2; 40: 1), and relative link targets (39: 59; 40: 46, identical in order) match the English.
   Table numbers match cell by cell (the one difference is the comma after "Tier 1" in a report-table
   cell, the checker false positive the translator noted). Ordered-item counts equal the English, so no
   wrapped line begins with a number and a period. Paragraphs, table rows, exercises, reflection
   questions, takeaways, and reference lines were also checked by eye: nothing is missing. All
   admonitions keep their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar names, roles, and numbers were checked against the English, and
   the case arithmetic (hours tables, skip-level coverage, firsthand shares) was recomputed.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched, except that
three doubled chapter numbers in ch 40 were folded into their links. English was not edited.

Totals: 10 editor doubts plus the translator's notes checked; 2 editor doubts changed (ch 40 nos. 3 and
5, plus the wording of no. 4). Further fixes from the full read: ch 39 ×3, ch 40 ×2.
Validation: `tools/validate_book.py` passed.

## Chapter 39

| # | Doubt | Verdict |
|---|---|---|
| 1 | «Отчёты при этом были зелёными по их собственным меркам» | ok. "The reports had been green on their own terms": the reports' own definitions. |
| 2 | «Пороги можно выбрать по-разному; важно каждый раз рассчитывать их одинаково» | ok. The English "computing them the same way" is equally ambiguous; the sense (consistent computation) survives. |
| 3 | «Отчёт не решает ничего из того, что ещё открыто» | ok. "The report decides nothing that is still open": open items are asked for, not settled in the report. Literal and right. |
| 4 | «Делает ли Victor это, кейс оставляет открытым: это вопрос для упражнений» | ok. "whether he does is left open for the exercises". |
| 5 | «Типичные ошибки маршрутизации — разбирать спор на обзоре и принимать решение в отчёте» | ok. The English names both as misroutings. |
| t14 | H1 «отчётность перед руководством» vs body «отчёт(ность) для руководства» | ok. H1 follows the nav title (kept); the body uses «отчёт для руководства» throughout. |
| t14 | "as the abstracts report them" → «в изложении аннотаций» | ok as a translation; see English problem 2. |
| t14 | ADR-0001 feminine; «в записях значились»; X3 «с уровня чуть ниже… до уровня чуть выше»; report-table numbers verbatim | ok. |

Further fixes:
- Why this matters, executive scale: «Для высшего руководства цена ещё выше» added a claim ("the cost is
  even higher") absent from the English ("At executive scale, a CTO who learns…"). Now «На уровне
  высшего руководства CTO, узнавший о срыве обязательства от клиента, уже потерял недели…».
- Failure modes, the report that asks for nothing: "a section that may say 'none', and rarely does" had
  become «допустимо «нет», но лишь изредка», a rule rather than an observation. Now «допустимо «нет», но
  такое бывает редко».
- Case, week 26 report: the English gives Kwame Mensah as "staff engineer, reliability"; the Russian had
  expanded it to «инфраструктура и надёжность» (his cast role). Now «staff-инженер, надёжность», as in
  ch 38's Russian page.

Full read: no other drift. The opening and related-chapters box, the three scales and INC-417, the
mental model and loop, Grove, the review table and the talent and architecture reviews, the three review
rules (this book's recommendation), the mum effect (research findings from models and experiments),
Keil et al. (about fourteen studies, 60 percent), DORA (industry research), the three consequences, the
decision log fields and Drucker, escalation (this book's recommendation; Bezos as documented practice of
one company; Aghion and Tirole), the joint write-up table, the executive report structure and color
definitions, the framing/misleading line and the three steps, the example (illustrative; under 1 percent;
week 7 Sev3 audit; ADR-0001 and the 6/4/2/0 engineer-week table), the decision diagram and weight table,
three trade-offs, seven failure modes, the escalation map, the CTO section, the 8-step playbook, the case
(INC-427, «Читайте таблицы сейчас…», DL-01 to DL-10, core/permissions and tax-svc, week 15 path, the week
26 report with all measures, risks, and decisions), all exercises (Tom Becker, Marcus Oyelaran, Priya
Raman, Ines Carvalho 8 of 14 and 5, Elena Sokolova, Helena Marsh), reflection questions, takeaways, and
references match.

## Chapter 40

| # | Doubt | Verdict |
|---|---|---|
| 1 | CTO «у которого в подчинении несколько директоров» (was «над которым стоят») | ok as edited. The English: "A CTO above several directors". |
| 2 | «Модель спорная» (Williamson) | ok. The English is prose ("It is a disputed model"), not the "contested" evidence label, so «вопрос спорный» does not apply. |
| 3 | Doubled chapter numbers «глава 3 ([глава 3](…))», also 19 and 27 | fixed. Folded into the links: «Такие рычаги ранжирует [глава 3](…)», «…даёт [глава 19](…), а трансформацию качества (…) — [глава 27](…)». The English doubles them too; see English problem 1. |
| 4 | GitLab: «дополняет взгляд руководителя на здоровье команды» | changed. The English says the template serves "a view of team health other than the manager's" (a different view, not an addition to the manager's). Also, it is the template that serves these purposes, not the meeting. Now «Он служит для обратной связи, похвалы и коучинга и даёт взгляд на здоровье команды, отличный от взгляда руководителя». |
| 5 | «Источники сигналов у CTO похожие, только обращается он к ним реже» | fixed. "similar but sparser" means fewer and thinner sources, not used less often. Now «похожие, но скуднее». |
| t14 | "this book's reasoning" → «рассуждение книги» | ok; please add to glossary 4.3, as the editor proposes. |
| t14 | Failure modes as prose, one «Как заметить:» | ok; mirrors the English. |
| t14 | X1 «Вы нужны мне…»; X2 opex rebuild; «Что видят клиенты?»; no lead-in in objectives | ok. |

Further fixes:
- Example, coverage latency: "which is why incident reviews and raw data, which arrive weekly, sit beside
  skip-levels" had become «встречи через уровень дополняют разборы инцидентов и сырые данные: они
  поступают каждую неделю», which reverses who complements whom and leaves «они» ambiguous. Now «Поэтому
  рядом со встречами через уровень стоят разборы инцидентов и сырые данные: они поступают каждую
  неделю».
- Trade-offs, signal against horizon: "The case study's redesign takes signal hours…" had lost
  "redesign". Now «При перестройке календаря в кейсе часы на сигналы берутся…».

Full read: no other drift. The opening, the three scales, objectives, the mental model and channel
diagram, Grove and Larson, the ownership table (this book's recommendation), the three changes
(Fournier), Williamson (theoretical, disputed, narrow point), Milliken et al. (research finding, 40
interviews), the two consequences (this book's reasoning), Floyd and Wooldridge (259 managers in 25
organizations; research findings, self-reported, correlational), the signal-source table (this book's
synthesis), GitLab (documented practice of one organization; no study found), the skip-level rule, the
quality section (Perlow, one team), Mintzberg, the two calendar cuts (a tenth, not a measured
threshold), Watkins, the skip-level cost table (recomputed: 12.75, 25.5, 37.5; weekly by 13), the
0.7 × 0.7 illustration, the decision table and discrepancy diagram, five trade-offs, seven failure modes,
enterprise application (5–10 managers, 40–140 people, fewer than ten individuals), sustainability and
peers, the CTO section (Larson as expert opinion), the 10-step playbook, the case (info box; period
table 25/12/8/4.7/9/9; the 4.5/54/37.5 = 96 sample; Mateo Arango Ríos, Daniel Cho, Elena Sokolova; the
quarter 3 table summing to 48 both ways; 77 engineers, 16 in Bogotá, 8 individuals; 5.5 hours, about 11.5
percent; Sofia Alvarez), all exercises (Tomasz Wierzbicki, Marcus Oyelaran, Victor Lindqvist, Rajiv
Menon), reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 40, "What changes" and "Quality as an organizational property"**: "Chapter 3 ranks such levers
   ([Chapter 3](…))", "Chapter 19 defines quality … ([Chapter 19](…))" and "Chapter 27 owns the
   transformation … ([Chapter 27](…))" name each chapter twice. Suggest linking the first mention and
   dropping the parenthesis, as the Russian now does.
2. **Ch 39, Why bad news travels slowly**: "These are research findings, as the abstracts report them"
   is an access note in reader text, which `CLAUDE.md` section 7 asks to fold into the evidence label.
   Suggest "These are research findings from models and experiments rather than field outcomes".
3. **Ch 39, Case**: Kwame Mensah is "staff engineer, reliability" here but "infrastructure and
   reliability" in the cast and in chapters 22 to 27. Not wrong, but a reader comparing chapters may
   wonder; suggest the cast wording.

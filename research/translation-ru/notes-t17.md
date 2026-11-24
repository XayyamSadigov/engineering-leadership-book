# Translation notes, lane t17 (Chapters 45–46)

Source: English working tree. Files:
`docs/parts/10-business-leadership/45-business-models-and-engineering-economics.ru.md`,
`docs/parts/10-business-leadership/46-stakeholder-management-and-negotiation.ru.md`.

Checks: `validate_book.py` passes (ch45, ch46 headings carry the English anchors; a script confirmed
24/24 anchors in each chapter); every number in every table is copied verbatim from the English table;
prose numbers use the Russian format (NBSP thousands, decimal comma) and were diffed token by token against
the English. Failure-mode fields: English "Signal:" / "Fix:" (ch45) and "Detect it…" (ch46) → «Как
заметить:» / «Что делать:».

## New terms

| English | Русский | Rule | Where |
|---|---|---|---|
| time value of money | стоимость денег во времени | T | ch45 |
| present value | приведённая стоимость (present value) | B | ch45 |
| cost of capital | стоимость капитала | T | ch45 |
| discount factor / annuity factor | коэффициент дисконтирования / коэффициент аннуитета | T | ch45 |
| real options; option value; option premium | реальные опционы; опционная ценность; опционная премия | T | ch45 |
| cash savings / returned capacity ("cash versus capacity") | денежная экономия / возвращённый ресурс («деньги и ресурс») | T | ch45 |
| urgency profiles: long life, peak unaffected / long life, peak affected / short life, peak affected / external deadline | долгая жизнь, пик не затронут / долгая жизнь, пик затронут / короткая жизнь, пик затронут / внешний срок | T | ch45; «профиль срочности» from glossary.ru |
| benefit types (increase / protect revenue, reduce / avoid costs) | рост выручки / защита выручки / снижение затрат / предотвращение затрат | T | ch45; follows glossary.ru «Канал ценности» |
| expansion (revenue) | расширение (expansion) | B | ch45 |
| break-even (value) | точка безубыточности; значение безубыточности | T | ch45 |
| stage (an investment); staging | разбить на этапы; разбивка на этапы, поэтапное инвестирование | T | ch45 |
| accuracy rather than precision | правильность, а не точность | T | ch45 |
| sponsor (of an estimate / item) | спонсор | T | ch45; follows notes-t9 |
| deal allowance | квота для сделок | T | ch45 X1; follows notes-t15 «зарезервированная квота» |
| spreadsheet theater / the sponsor's number / revenue mistaken for value / the free engineer / sunk-cost continuation / option theater / items evaluated in isolation | театр электронных таблиц / число спонсора / выручку принимают за ценность / бесплатный инженер / продолжение ради невозвратных затрат / театр опционов / задачи оценивают по отдельности | T | ch45 failure modes |
| quality floor; the floor | нижняя планка качества; планка | T | ch46; follows notes-t16 |
| tradeable variables | переменные, которыми можно торговаться | T | ch46 |
| repeated games | повторяющиеся игры | T | ch46 |
| power-interest grid | сетка «влияние × интерес» | T | ch46 |
| players / subjects / context setters / crowd | игроки (players) / субъекты (subjects) / задающие контекст (context setters) / толпа (crowd) | B | ch46; the template `stakeholder-map.md` has no Russian page yet; align it when translated |
| position (on the grid) / stance / position (in a negotiation) | место на сетке, положение / отношение / позиция | T | ch46; three English senses kept apart: grid quadrant, recorded attitude, negotiating position |
| negative-avoidance goals | цели избегания | T | ch46 |
| engagement (with a stakeholder) | взаимодействие | T | ch46 |
| standing map / issue map | постоянная карта / карта по вопросу | T | ch46 |
| revisit trigger | условие пересмотра | T | ch46; follows notes-t3 «review trigger» |
| prosocial motive; resistance to yielding; joint outcomes | просоциальный мотив; сопротивление уступкам; совместный результат | T | ch46 |
| reservation price | резервная цена (reservation price) | B | ch46 |
| anchor (first offer) | якорь; поставить якорь | T | ch46 |
| integrative / distributive (approach) | интегративный / распределительный | T | ch46 |
| headline (board page) | главная формулировка | T | ch46 |
| rolling four-quarter total | скользящая сумма за четыре квартала | T | ch46 |
| payroll export; bulk endpoints; backfill | экспорт данных для расчёта зарплаты; эндпоинты массовых операций; заполнение исторических данных (backfill) | T, B | ch46 example |
| the moving floor / everything is the floor / the stale map / splitting the difference on an estimate / yes now, no later / winning the meeting | сдвигающаяся планка / всё — планка / устаревшая карта / делить разницу в оценке пополам / «да» сейчас, «нет» потом / выиграть встречу | T | ch46 failure modes |

## Doubts and choices

1. **Ch45, "top 40" in prose.** Rendered «из топ-40» to keep the number visible; «из первой сороковки»
   was the first draft and was dropped for fidelity to the numeric token.
2. **Ch45, "is managed as a cost center".** Rendered «воспринимают как руководителя центра затрат»
   (sense, not "is managed").
3. **Ch45 tables.** Cells keep English number format, including "1.2 процента ARR", "1.1 года",
   "21.6 инженеро-недели" in ch46; this follows glossary rule 6 but reads oddly next to Russian words.
4. **Ch46 evidence labels.** "Treat the grid as expert opinion" → «**мнением эксперта**»; "All three are
   expert opinion" → «**мнение экспертов**» (plural for three sources; the label function is kept).
5. **Ch46 case, Victor's role.** The English paragraph does not restate "(CTO)" on Victor's first
   mention in the case; the Russian follows the English (his role is in the table just below).

## English problems noticed (not fixed)

- Ch45, CTO Perspective: "two renewals worth $9M in which reliability was the customers' stated concern,
  made this concrete; the harder task…" is one long sentence with an unwrapped line in the source
  (line 439 runs past the usual width). The Russian splits it.
- Ch46, CTO Perspective (line 327) and Mental Model (line 53) also have overlong source lines; cosmetic.
- Ch46, F1: the grid is called "power-interest" in F1 and the references but "interest against power"
  in the text; the Russian uses «интерес × влияние» in the text and «влияние × интерес» where the English
  says power-interest, mirroring the English.

# Translation notes, lane t24 (Chapters 59–60)

Source: English working tree. Files:
`docs/parts/13-advanced-problems/59-transformation-under-constraint-and-scaling-without-bureaucracy.ru.md`,
`docs/parts/15-capstone/60-capstone-northstar.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, citation link
texts, exercise labels, admonition types, Mermaid count and node ids, table rows and every number in
tables identical (ch59 has one row where word order moves two numbers within a cell). The multiset of
numbers in the page matches, except one word form in ch59 ("under 1" working day → «до менее чем
одного»). No wrapped line starts with a number followed by a period. Words (whitespace tokens; NBSP
glues some): ch59 6 828, ch60 7 457.

Failure Modes: both chapters have only "Early sign:" → «Как заметить:» (ch43, ch49, ch51 precedent).

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| standing claims (on capacity) | постоянные притязания на ресурс | T | ch59; «притязания на ресурс» follows notes-t18 |
| carries load / carries history; load-bearing; load | несёт нагрузку / несёт историю; несущий (процесс); нагрузка | T | ch59; «нагрузка» follows first-quarter.ru («с нагрузкой, доказательствами и черновым вердиктом») |
| load test; hidden load | проверка на нагрузку; скрытая нагрузка | T | ch59 |
| management steps | управленческие ступени | T | ch59 |
| watch signal; restore trigger | контрольный сигнал; условие восстановления | T | ch59 |
| suspend, suspension | приостановить, приостановка | T | ch59 |
| verdicts keep / cheapen / instrument / suspend / delete / decide | оставить / удешевить / оснастить измерениями / приостановить / удалить / решить | T | ch59; «оснастить измерениями», «упразднить» (retire) and «сблизить» (converge) follow first-quarter.ru's inventory section |
| sunset (of a rule) | срок действия (sunset); дата истечения | B | ch59 |
| process budget; process ceiling | бюджет на процессы; потолок процессов | T | ch59 |
| capacity is not cash; in-year vs run-rate | ресурс — не деньги; эффект (экономия) текущего года и годовой темп | T | ch59; «деньги и ресурс» follows notes-t17 |
| exit run-rate | годовой темп на выходе из года | T | ch59; follows halvard.ru («темп на выходе из года») |
| across-the-board cut | урезание всем поровну; равномерно по всем направлениям | T | ch59 |
| cost shifting | перекладывание затрат | T | ch59 |
| enabling / coercive formalization | поддерживающая (enabling) / принудительная (coercive) формализация | B | ch59 |
| change advisory board | консультативный комитет по изменениям (change advisory board); комитет по изменениям | B | ch59; follows halvard.ru «комитет по изменениям», although notes-t6 has «консультативный совет по изменениям». One word chosen for the whole chapter so that the Halvard board and the DORA board read as the same thing; the maintainer may unify book-wide |
| compliance pack | пакет соответствия требованиям | T | ch59; follows halvard.ru |
| enterprise policies; auditable pipeline | корпоративные политики; аудируемый пайплайн | T | ch59, ch60; follows halvard.ru |
| legacy deployment tool | legacy-инструмент развёртывания | T | ch59; follows halvard.ru |
| findings past their service levels | находки с просроченным сроком устранения | T | ch59; «находки» per notes-t7; halvard.ru says «замечания» — the maintainer may align |
| the across-the-board cut / counting returned capacity before it returns / cost shifting / the hidden load / removal by neglect / restoring by reflex | урезание всем поровну / ресурс засчитан до того, как вернулся / перекладывание затрат / скрытая нагрузка / отмена через забвение / возврат на рефлексе | T | ch59 failure modes; «на рефлексе» follows notes-t18 |
| capstone | итоговый проект | T | ch60; follows the ru nav title |
| stage (capstone) | этап | T | ch60; where the English uses "stage" for the continuation's own stages (ch49 sense), the Russian adds «продолжения» to avoid a clash: «к этапу 3 продолжения», «на каждый этап продолжения» |
| stage names | Диагностика / Модель владения / Карта показателей / Приоритеты по долгу / Схема подотчётности / План на 90 дней / Стратегия на 12 месяцев / Инвестиционное обоснование / Трёхлетняя технологическая стратегия / Коммуникация с советом директоров | T | ch60; diagram labels shortened |
| hinge; hinge review; hinge facts | поворотная точка (hinge); поворотный разбор, разбор в поворотной точке; факты поворотной точки | B | ch60 |
| commitment register | реестр обязательств | T | ch60 |
| measurement bridge | мост измерений (measurement bridge) | B | ch60 |
| counting rules; trust table; continuity rule | правила подсчёта; таблица доверия; правило непрерывности | T | ch60 |
| facts packet; time rule | пакет фактов; правило времени | T | ch60 |
| threads | нити | T | ch60 |
| capacity envelope; envelope table | рамки ресурса; таблица рамок | T | ch60; follows notes-t20 |
| absorbing line; shock absorber | строка-амортизатор; амортизатор | T | ch60 |
| step-down rule | правило снижения | T | ch60 |
| statuses honored / bridged / revised in writing / revised silently / orphaned / retired | соблюдено / связано мостом / пересмотрено письменно / пересмотрено тихо / осиротело / отменено | T | ch60 |
| Produce / Add / Facts / Assume / Hand forward (stage fields) | Подготовьте / Добавьте / Факты / Допущение / Что передаётся дальше | T | ch60 |
| deliverable; Good enough when; finish line | что сдать; «Достаточно, если»; критерий завершения | T | ch60; Project 3's "deliverables 1 and 2" → «результаты 1 и 2» (P3 has no Russian page yet) |
| integration memo | записка об интеграции | T | ch60 |
| grading aid; sample stage 1 page | пособие по оценке; образец страницы этапа 1 | T | ch60 link texts |
| decision-rights map; CTO lane | карта прав на решения; дорожка CTO | T | ch60 |
| outcome bias | ошибка оценки по результату (outcome bias) | B | ch60 |
| the stapled portfolio / the orphan commitment / hindsight leakage / the CTO doing the director's job / outcome-graded hinge | портфель, сшитый степлером / обязательство-сирота / утечка знания задним числом / CTO делает работу директора / поворотный разбор с оценкой по результату | T | ch60 failure modes; «сирота» follows notes-t20 |
| investor board member | член совета от инвестора | T | ch60 X2 |

Reused: место (seat), годовой темп (run-rate), продолжение, компенсирующая экономия (offset), свободный
бюджет на инструменты, инженер по качеству, кредит-ноты, аудит серьёзности, исключение, бесхозный
модуль, решающий, охват, руководитель руководителей, staff-трек, мерж-реквест / пул-реквест,
актуальность ландшафта, правило на случай стресса, строка о людях, премортем, «отлично / достаточно /
покупать / не делать», эскалация приверженности, ловушка возможностей, Engineering Excellence Day
(English), хроника года 1, «Год вкратце», действующие лица, брифинг квартала 4. Template link texts follow
the ru nav titles of the templates. Bogotá → «Богота» (maintainer decision).

## Doubts and notes on the English (English not changed)

- ch59 F3, A1, A2, A3 and ch60 Mental Model, Deep explanation (capability trap), hinge section, A2, X1:
  several overlong source lines; cosmetic.
- ch59 Example: "Closure rose from 32 percent to 78" — rendered «с 32% до 78%».
- ch59 Halvard: the CTO is unnamed and ungendered (halvard.md); the Russian avoids gendered past-tense
  verbs for the Halvard CTO where it can («По решению CTO её бюджет … урезан»), but "The CTO agreed"
  became «CTO согласился» (default masculine as the neutral form, glossary rule 10).
- ch59 "Instrument" as a verdict: first-quarter.ru uses «оснастить измерениями»; followed, though it is
  long in table cells.
- ch59 "Move up the ladder" (diagram) read as Chapter 20's enforcement ladder; rendered «Вверх по
  лестнице контроля».
- ch59 A3 "name the source you would refuse to use first" read as "the source you would refuse to start
  with"; rendered «источник, с которого вы отказались бы начинать».
- ch60 Example table: "at most 18% by stage 3" refers to the continuation's stage 3, not the capstone's
  stage 3; the same word in a capstone chapter invites misreading. Russian adds «продолжения»; the
  English may want "by the continuation's stage 3". Same in F3 ("fixed per stage").
- ch60 F2 "explain one way a director-stage artifact would mislead" rendered «на одном примере
  объясните»; the list of facts was split off into its own sentence («Факты: …»).
- ch60 Case: Victor's remark "read the tables now and clean it up later" rendered as direct speech in
  «вы» form («Читайте таблицы сейчас, а порядок наведёте потом»).
- ch60 Learning objective 4 has no verb for the three documents in English ("Extend the director's work
  into …"); Russian adds «написать».

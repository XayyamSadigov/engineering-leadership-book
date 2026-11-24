# Translation notes, lane t13 (Chapters 37–38)

Source: English working tree. Files:
`docs/parts/08-management-operating-system/37-cadences-and-leadership-meetings.ru.md`,
`docs/parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, exercise labels,
admonition types, Mermaid count and node ids, table rows and every number in tables identical. Prose
number differences are only the thousands separator ($46 250, 300 000) and the H1 anchor. Failure Modes
use «Как заметить:» / «Что делать:» (both chapters have Signal/Countermeasure fields; some ch37/ch38
entries have no Signal, kept as in English).

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| forum | форум | T | ch37, ch38; follows ch28.ru |
| loop (operating-system loop); home (of a loop) | петля; место («у каждой петли одно место») | T | ch37 |
| homed / duplicated / missing (loop) | есть место / дублируется / места нет | T | ch37 |
| job (of a meeting) | задача (встречи) | T | ch37 |
| the seven jobs: Inform / Operate / Decide / Inspect / Allocate / Develop / Connect | Информировать / Вести текущую работу / Решать / Проверять / Распределять / Развивать / Сплачивать | T | ch37 |
| artifacts / horizons / routing rules | артефакты / горизонты / правила маршрутизации | T | ch37 |
| pre-read | письменные материалы к встрече (pre-read); материалы к встрече | B | ch37, ch38 |
| status round | круг статусов | T | follows baseline-data.ru |
| framed (decision item) | подготовленный (вопрос) | T | ch37 |
| design choices (five) | правила устройства | T | ch37; «решения» avoided (editing pattern 6) |
| leadership (team) meeting | встреча команды руководителей; «встреча руководителей» only in generic prose | T | ch37; follows first-quarter.ru, where «встреча руководителей» is the managers' meeting |
| managers' meeting | встреча руководителей | T | follows first-quarter.ru, baseline-data.ru |
| renewal check-in | сверка по продлениям | T | follows first-quarter.ru |
| product and engineering sync / product sync / Billing and Orders sync | синхронизация продукта и разработки / синхронизация с продуктом / синхронизация Billing и Orders | T | follows first-quarter.ru |
| release working group / staff group | рабочая группа по релизам / staff-группа | T | follows first-quarter.ru |
| delivery review / all-hands | обзор поставки / общее собрание | T | follows first-quarter.ru |
| business review (monthly) / talent review / team review | бизнес-обзор / обзор талантов / обзор команды | T | follows first-quarter.ru |
| topic-by-forum matrix | матрица «тема × форум» | T | ch37 |
| attendee-hours / person-hours | человеко-часы участников / человеко-часы | T | ch37 |
| forum charter | хартия форума | T | ch37; by analogy with «хартия команды» |
| fast path | быстрый путь | T | ch37 |
| process-oriented / mission-oriented meetings (Grove) | процессные / целевые встречи | T | ch37 |
| staff meeting | совещание с подчинёнными | T | follows notes-t11 |
| on-call leads | старшие по дежурствам | T | follows notes-t7 (notes-t8 has «ведущие дежурные»; maintainer may unify) |
| status theater / the meeting that outlived its job / growth by accretion / corridor decisions / the preparation cascade / the empty chair / the measure gamed | театр статусов / встреча, пережившая свою задачу / рост наслоением / решения в коридоре / каскад подготовки / пустой стул / подогнанная метрика | T | ch37 failure modes |
| pre-meetings | «предвстречи» | T | ch37 |
| growth allowance | поправка на рост | T | ch38; follows ch17.ru «объём с поправкой на рост» |
| target band | полоса целей | T | ch38 |
| commitment line | черта обязательств | T | ch38 |
| row owner / data steward; data stewardship | владелец строки / хранитель данных (data steward); хранение данных | B | ch38 |
| direction, not a target | направление, а не цель | T | ch38 |
| paired measure | парная метрика | T | term base «парная метрика» |
| mechanism measures | метрики механизмов | T | follows notes-t8 |
| tax (unplanned work) | налог | T | ch38 |
| payback shapes | профиль окупаемости | T | ch38 |
| envelope | рамки | T | term base «рамки бюджета» |
| investment lines | инвестиционные строки | T | ch38 |
| consolidation target | целевая система CI | T | follows first-quarter.ru, quarter-4-briefing.ru |
| intake (requests made outside the intake) | единый вход | T | follows notes-t10 |
| time sampling | выборка времени | T | follows ch29.ru |
| OKR: objective / key result | цель (objective) / ключевой результат | B for objective | ch38; «(objective)» added where «цель» could be read as "target" |
| investment classes run / grow / improve | поддержание (run) / рост (grow) / улучшение (improve) | B | ch38 |
| "keep the lights on" | «поддержание работы» (keep the lights on) | B | ch38 |
| employee net promoter score | индекс лояльности сотрудников (employee net promoter score) | B | ch38 |
| after-hours pages | вызовы в нерабочее время | T | ch38; «вызов» per notes-t1 |
| trade (recorded trade) | обмен (записанный обмен) | T | ch38 |
| coin-flip promise | обещание с шансами пятьдесят на пятьдесят | T | ch38 |
| the wish list plan / the paper allocation / the invisible unfunded list / scorecard sprawl / key results on mechanism measures / renegotiation by attrition | план-список желаний / распределение на бумаге / невидимый список непрофинансированного / разрастание карты показателей / ключевые результаты на метриках механизмов / пересмотр измором | T | ch38 failure modes |
| disputed (as an evidence-strength word) | вопрос спорный | T | ch38; glossary decision for "contested" applied |

Reused from earlier lanes: операционный разбор, обзор качества, квартальная перезагрузка, список
открытых решений, встреча через уровень (skip-level), массовый заказ, приём заказов, ротация на
прерываниях, хранилище событий развёртывания, выборка времени, ресурс на функции, просадка, принятие
(adoption), ограничители, хроника года 1, «Год вкратце», список действующих лиц.

## Doubts and notes on the English (English not changed)

- ch37 "Its 16 attendees spent about 20 person-hours a week in it, most of them on-call leads, who are
  engineers": "most of them" refers to attendees; rendered so.
- ch37 Kauffeld: "as the abstract reports it" is an access note in prose; rendered «в изложении
  аннотации» (same pattern as notes-t8 to t10). ch38 Locke and Latham "as the reviews' abstracts report
  it" likewise.
- ch37 Grove's "operation reviews" rendered «операционные обзоры», to keep it apart from the book's
  «операционный разбор».
- ch37 "skip-levels (meetings with a manager's reports)": rendered «встречи с подчинёнными своих
  руководителей», which is what the glossary entry means (the director meets the managers' reports).
- ch37 calendar table "45 to 90 min" rendered «От 45 до 90 мин» (numbers verbatim).
- ch38 CTO perspective "The scorecard becomes a few exposures": "exposures" is unusual here; read as
  "a few numbers exposed to the board" and rendered «сжимается до нескольких чисел на виду у совета».
  The English might say "a few board-level numbers".
- ch38 Mental model text says "commit what the pessimistic case can deliver" while the defined term is
  "cautious case"; rendered «пессимистичный сценарий» as written (same in ch27, notes-t8). The English
  may want "cautious".
- ch38 OKR table: "99.9 percent" kept as "99.9 процента" inside the table (table numbers verbatim).
- ch38 "Treat the size of the side effects as **disputed**" rendered «Размер побочных эффектов —
  **вопрос спорный**».
- Word counts (wc -w; no-break spaces glue some tokens): ch37 5 629, ch38 5 540.

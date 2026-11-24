# Translation notes, lane t16 (Chapters 43–44)

Source: English working tree. Files:
`docs/parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.ru.md`,
`docs/parts/10-business-leadership/44-working-with-product.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, exercise labels,
admonition types, Mermaid count, table rows and every number in tables identical. Prose number differences
are only word forms ("day 1", "day 3" → «в первый день», «к третьему дню»; "Sixty" → «60»), «1:1» and
the thousands separator. Failure Modes: ch43 has only "Early sign:" → «Как заметить:»; ch44 has
Signal/Countermeasure → «Как заметить:» / «Что делать:». Words (wc -w; no-break spaces glue some tokens):
ch43 5 269, ch44 5 518.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| carriers (of a change) | носители (изменения) | T | ch43 |
| guiding coalition (Kotter) | направляющая коалиция | T | ch43 |
| short-term wins / small wins (Weick) / early wins (Watkins) | быстрые победы / малые победы / ранние победы | T | ch43 |
| stopping rule; stop rule is met | правило остановки; условие остановки выполнено | T | ch43 |
| escalation of commitment / escalating commitment | эскалация приверженности (escalation of commitment) | B | ch43; «приверженность» chosen over the common «эскалация обязательств» so that it does not collide with «обязательство» (commitment in the forecast/target/commitment triad and in "commitments list"); bare "escalation" stays «эскалация» |
| commitments list | список обязательств | T | ch43 |
| change register | реестр изменений | T | ch43 |
| change load; slack (manager hours) | нагрузка от изменений; запас | T | ch43 |
| pulse (survey) | пульс-опрос | T | ch43 |
| reinforcement / anchoring (Kotter) | закрепление / закрепление в культуре | T | ch43 |
| trust repair; competence / integrity violation | восстановление доверия; нарушение, связанное с компетентностью / с честностью | T | ch43 |
| credibility | доверие (к директору); репутация (in "record becomes credibility") | T | ch43 |
| imposition (impose a change) | директивный путь; ввести директивно | T | ch43 |
| failure patterns: change by announcement / initiative overload / solution before diagnosis / level slip / decision vacuum / promise inflation / escalating commitment / signal isolation | изменение через объявление / перегрузка инициативами / рецепт до диагноза / соскальзывание на уровень ниже / вакуум решений / инфляция обещаний / эскалация приверженности / изоляция от сигналов | T | ch43; «рецепт» instead of «решение» for "solution" (editing pattern 6) |
| failure modes: the launch nobody shaped / the quiet exemption / the activity measure / the redefined target / the silent end / the over-apology | запуск, который никто не обсуждал / тихие исключения / показатель активности / переопределённая цель / тихое завершение / чрезмерное покаяние | T | ch43 |
| Engineering Excellence Day | kept English | E | ch43; follows first-quarter.ru |
| period close; month-end reporting | закрытие периода; отчётность на конец месяца | T | ch43 |
| flaky-test owner list; standing build warnings | список владельцев нестабильных тестов; давно висящие предупреждения сборки | T | ch43 |
| merged (items) | слитые (задачи) | T | ch43; first-quarter.ru has «смёржено» — the maintainer may unify |
| working contract (product–engineering) | рабочий договор | T | ch44 |
| quality floor | нижняя планка качества | T | ch44 |
| head of product | руководитель продукта | T | ch44 |
| feature roadmap / outcome roadmap | дорожная карта функций / дорожная карта результатов | T | ch44; term base «дорожная карта, ориентированная на результат» kept in the H1 and nav |
| bet; release (a bet) | ставка; запустить (ставку) | T | ch44 |
| four product risks: valuable / usable / feasible / viable for the business | ценность / удобство использования / реализуемость / жизнеспособность для бизнеса | T | ch44 |
| feasibility | реализуемость | T | ch44 |
| empowered product teams / feature teams | продуктовые команды с полномочиями (empowered product teams) / фича-команды (feature teams) | B | ch44 |
| build trap | «ловушка разработки» (build trap) | B | follows notes-t3 |
| discovery | discovery (neuter: «продуктовое discovery») | B/E | ch44; term base gloss «продуктовое исследование» not repeated since the H1 uses bare "discovery" |
| online controlled experiments | онлайн-контролируемые эксперименты | T | ch44 |
| continuous experimentation; minimum viable features | непрерывное экспериментирование; минимально жизнеспособные функции | T | ch44 |
| staged rollout | поэтапная раскатка | T | ch44; «раскатка» per notes-t6 |
| instrumentation; instrument | инструментирование; инструментировать | T | ch44 |
| corrected order; ordering-error rate | исправленный заказ; доля ошибочных заказов | T | ch44 |
| idempotency key | ключ идемпотентности | T | ch44 |
| repricing at submission | повторный расчёт цены при отправке | T | ch44 |
| price-list effective dates | даты вступления прайс-листов в силу | T | follows timeline.ru |
| release valve | предохранительный клапан | T | ch44 |
| deal date | дата для сделки | T | ch44; «функция для сделки» per notes-t15 |
| capacity line | линия ресурса | T | ch44 |
| outcome theater / engineering as estimator only / discovery without end / the date that slipped back in / one-sided contract | театр результатов / разработка только как оценщик / discovery без конца / дата, которая вернулась / односторонний договор | T | ch44 failure modes |
| dunning emails; card network; reconciliation exception report | письма-напоминания о просроченной оплате; карточная платёжная система; отчёт об исключениях при сверке | T | ch44 F1 |
| purchase order import | импорт заказов на закупку | T | ch44 A3 |
| account team | команда, которая ведёт клиента | T | ch44 A3 |

Reused: выделение на профилактику, аудит серьёзности, кредит-ноты, ротация на прерываниях, релизный поезд,
спайк (spike), ходячий скелет, ограничители, список непрофинансированного, пакет для совета директоров,
FTE-квартал, доля инцидентов, обнаруженных клиентами, путь эскалации, встреча команды руководителей,
групповая встреча через уровень, хроника года 1, «Год вкратце», действующие лица, брифинг квартала 4.

## Doubts and notes on the English (English not changed)

- ch43 Learning objectives keep the "After this chapter you will be able to:" lead-in («Прочитав эту
  главу, вы сможете:»); ch44 likewise.
- ch43 Why This Matters: "the director's record of changes becomes their credibility" rendered with
  «репутация» there; elsewhere "credibility" is «доверие», which reads better with "recover".
- ch43 "carrying a change … the managers having changed the design": «проект» used for "design" of a
  change («изменили его проект»), in line with ch35.ru «проект организации».
- ch43 Example table "1.0 each" rendered «по 1.0» (number verbatim, word translated).
- ch43 Case: "Day 2 fell on Billing's period-close support" — read as Billing supporting Finance's
  period close; rendered «поддержка закрытия периода в Billing».
- ch43 the closing sentence of the Mental Model diagram note joins two clauses with a semicolon in the
  English; split into two sentences.
- ch44 "Related chapters:" inside Learning Objectives is a plain paragraph in the English (not an
  admonition); kept as a paragraph.
- ch44 Case: "The monthly board pack … still carries one engineering delivery number: committed roadmap
  items delivered" rendered «выполненные обещанные пункты дорожной карты» without adding "share" or "count".
- ch44 A1: "push order latency to about 98.6 percent within 2 seconds" rebuilt as «снизит долю заказов,
  оформленных за 2 секунды, примерно до 98,6 процента» (the English compresses the SLO wording).
- ch44 "Sofia Alvarez (VP Customer Success)" follows cast.ru («VP по работе с клиентами (Customer
  Success)»); the requester column "Customer Success" kept in English as the function's name.
- ch44 Two functions: Cagan's fourth risk is "workable for the business" in the English (Cagan usually
  says "viable"); rendered «жизнеспособна для бизнеса».

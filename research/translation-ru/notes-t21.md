# Translation notes, lane t21 (Chapters 53–54)

Source: English working tree. Files:
`docs/parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.ru.md`,
`docs/parts/12-cto-leadership/54-data-and-ai-strategy.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, citation link
texts, exercise labels, admonition types, Mermaid count and node ids, table rows and every number in
tables identical (ch53 has one checker false positive: "SOC 2," with a comma in the ER-06 row). No wrapped
line starts with a number followed by a period. Prose number differences are only word forms ("year 1/2"
→ «первый/второй год»: ch53 one "1", two "2"; ch54 four "2") and the thousands separator. Words (wc -w;
no-break spaces glue some tokens): ch53 6 965, ch54 6 579.

Failure Modes: both chapters have "Signal:" (+ "Countermeasure:" in ch53) → «Как заметить:» /
«Что делать:», as in the Signal/Countermeasure chapters (notes-t4 onward). Several entries have only one
field; the Russian follows the English.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| control (audit/compliance sense); engineering control; control objective | механизм контроля (control); инженерный механизм контроля; цель контроля | B | ch53, ch54; glossary.ru SOC 2 entry says «контролей компании» — the maintainer may align it. Diagram label shortened to «Инженерный контроль» |
| control readiness | готовность механизмов контроля | T | ch53 |
| accepter (of a risk) | принимающий риск; принимающий | T | ch53; follows glossary.ru «тот, кто принимает риск» |
| acceptance (of a risk); expiry | принятие (риска); срок действия | T | ch53 |
| enterprise technology risk register | корпоративный реестр технологических рисков | T | ch53 |
| roll-up / roll up (risks) | подъём рисков наверх; поднимать наверх | T | ch53 |
| altitude (of register items) | уровень обзора | T | ch53 |
| exposure range (dollar) / exposures | диапазон возможного ущерба / оценки ущерба | T | ch53 |
| exposure (security reporting); exposure measures | уязвимость системы; метрики уязвимости системы | T | ch53; follows notes-t7 |
| amber (rating); the amber square | жёлтый; «Жёлтый квадрат» | T | ch53; «жёлтый» per notes-t14 |
| heat map | тепловая карта | T | ch53 |
| likelihood-impact matrix; resolution (of a matrix) | матрица «вероятность × ущерб»; разрешающая способность | T | ch53 |
| triage (rating for triage) | сортировка | T | ch53 |
| calibrated estimates | калиброванные оценки | T | ch53 |
| independent assurance; missing assurance | источник независимых гарантий; отсутствие гарантий | T | ch53; «гарантии» per notes-t7 |
| tabletop exercise | штабные учения (tabletop exercise) | B | ch53 |
| incident-to-disclosure path; material, materiality | путь от инцидента к раскрытию; существенный, существенность | T | ch53 |
| continuity plan | план непрерывности | T | ch53 |
| cyber insurers | киберстраховщики | T | ch53 |
| scope (PCI); scope boundary; scope review | границы применения; граница применения; проверка границ применения | T | ch53 |
| cardholder data; tokenization | данные держателей карт; токенизация | T | ch53 |
| listed company; annual report | компания, чьи акции торгуются на бирже; годовой отчёт | T | ch53 |
| CPA; AICPA; SEC | CPA (certified public accountant, дипломированный аудитор); AICPA (Американский институт дипломированных бухгалтеров); SEC (Комиссия по ценным бумагам и биржам) | B/E | ch53 |
| CSF Core | ядро (Core) | B | ch53; glossed so that it is not read as Northstar's Core (cf. notes-t7) |
| security snapshot | срез состояния безопасности | T | ch53 |
| phishing click rate; training completion | доля кликов в фишинговых рассылках; доля прошедших обучение | T | ch53 |
| material vendor | существенный вендор | T | ch53 |
| application security role, dotted line | роль по безопасности приложений, пунктирная линия подчинения | T | ch53; «пунктирные линии подчинения» per notes-t11 |
| compliance automation tool; audit fee | инструмент автоматизации compliance; плата аудитору | T | ch53 |
| the amber square / acceptance by default / framework as strategy / activity reporting / evidence by hand | жёлтый квадрат / принятие по умолчанию / фреймворк вместо стратегии / отчётность об активности / доказательства вручную | T | ch53 failure modes |
| data foundations | фундамент данных | T | ch54 |
| owner of meaning | владелец смысла (данных) | T | ch54; follows first-quarter.ru |
| lineage (data) | прослеживаемость (lineage only implied) | T | ch54; «происхождение» avoided, it is taken by provenance (notes-t7) |
| permitted use; data classes | разрешённое использование; классы данных | T | ch54 |
| data cascades | каскады данных (data cascades) | B | ch54 |
| labels; labeled examples | разметка; размеченные примеры | T | ch54 |
| data product / by-product; data contract | продукт данных / побочный продукт; контракт данных | T | ch54 |
| warehouse; catalog | хранилище данных; каталог | T | ch54 |
| low-regret (first stage) | этап, о котором вряд ли придётся пожалеть | T | ch54 |
| AI capability; AI initiative | ИИ-возможность; ИИ-инициатива | T | ch54 |
| frontier; jagged frontier | передний край; зубчатая граница (jagged frontier) | B | ch54 |
| preregistered experiment | эксперимент с предварительной регистрацией | T | ch54 |
| evaluation set | оценочный набор (evaluation set) | B | ch54 |
| inference cost | стоимость инференса | T | ch54 |
| pin (versions) | фиксировать версии | T | ch54 |
| coding assistant; coding agent | ассистент для написания кода, ИИ-ассистент для кода; агент для написания кода | T | ch54; follows first-quarter.ru |
| pull request | пул-реквест | T | ch54; follows ch18.ru |
| least access | минимальные нужные права | T | ch54 |
| hallucinated / invented packages; lockfiles; secret scanning | выдуманные пакеты; lock-файлы; сканирование на секреты | T | ch54 |
| acceptance rate (suggestions) | доля принятых подсказок | T | ch54 |
| AI stance | позиция по ИИ | T | ch54; follows quarter-4-briefing.ru |
| RCT; standard error; preprint | RCT (randomized controlled trial, рандомизированное контролируемое испытание); стандартная ошибка; препринт | B/E | ch54; RCT kept in tables |
| greenfield (task, server) | задача с нуля; сервер, написанный с нуля | T | ch54 |
| bank (a gain) in a plan | заложить в план | T | ch54 |
| hold backfills open / held backfills | держать замены незаполненными / придержанные замены | T | ch54; follows first-quarter.ru |
| workforce plan; headcount plan | план по персоналу; план численности | T | ch54 |
| staggered rollout; waves; confounded | поэтапная раскатка по командам; волны; смешаны | T | ch54 |
| AI RMF functions Govern, Map, Measure, Manage | English, glossed once (управлять, картировать, измерять, обрабатывать) | E | ch54 |
| the pilot without a baseline / AI on unowned data / the headcount pre-commitment / activity metrics as targets / ban and bypass / demo-driven commitments | пилот без исходного уровня / ИИ на бесхозных данных / численность, обещанная заранее / метрики активности как цели / запрет и обход / обязательства из-за демо | T | ch54 failure modes |

Reused: реестр рисков, риск-аппетит, обработка риска (снизить, передать, избежать, принять),
активно эксплуатируемая уязвимость (KEV), компенсирующая мера, исключение, остаточный риск, находки,
пентест, опросник, менеджер секретов, происхождение (provenance), сведения о происхождении, анализ
разрывов, текущий / целевой профиль, библиотека доказательств, владелец доказательств со стороны
разработки, сроки устранения, «не затронуты», служба безопасности, безопасность приложений, продолжение,
контрольная точка, целевая система CI, этап 1 консолидации CI, функции для сделок, группа «достаточно»,
опционная ценность, ключ идемпотентности, даты вступления прайс-листов в силу, раскатка, найм на замену,
покрытие преемниками, ставка, «Год вкратце», действующие лица, брифинг квартала 4.

## Doubts and notes on the English (English not changed)

- ch53 Why This Matters: "reassurance.\nA CTO who…" is a short wrapped line in the source (cosmetic); so
  is the "Material means…" line in the regulation list (overlong) and "### Reporting risk…" follows the
  previous paragraph with no blank line (renders fine). The Russian normalises spacing.
- ch53 Learning objectives call SSDF "the Secure Software Development Framework" but the deep explanation
  says "The SSDF"; both rendered with the English name kept.
- ch53 Example: "ER-03 is accepted meanwhile by exception" — "meanwhile" read as "for now"; rendered «пока
  принят через исключение».
- ch53 Example: "The director collects TR-01 to TR-09, six security findings, four items from Marta's IT
  list, two compliance items, and the reliability record" = 9+6+4+2+1 = 22, matching "22 scattered items".
- ch53 Case: "Joon Park wrote the week 52 date into the record in week 44, with no new signature" kept as
  written; the Russian splits it with dashes («вписал в запись дату — неделю 52 — на неделе 44»).
- ch53 Case: "SOC 2 … $45,000 to $70,000" rendered «$45 000–70 000»; first-quarter.ru writes
  «$45 000–$70 000». Cosmetic; the maintainer may unify.
- ch53 Example table: the ER-01 owner is "Engineering Director" (the role, since the director is unnamed);
  rendered «Директор по разработке».
- ch54 Example: "Month-end revenue differs from Finance's ledger close" rendered «расходится с закрытием
  ledger у финансов»; first-quarter.ru says «с закрытием финансов». Same meaning.
- ch54 Example table and Case: "year-2" inside table cells rendered «год 2» so table numbers stay
  identical; prose uses word forms («второй год»).
- ch54 Case: "It also receives search-svc in week 54" — quarter-4-briefing.ru says the organization change
  takes effect in week 53; week 54 for search-svc is kept as written. The maintainer may check the canon.
- ch54 Evidence table: "RCT means randomized controlled trial" sits in prose before the table; kept there.
- ch54 F4 and the inference example are illustrative arithmetic; numbers unchanged.

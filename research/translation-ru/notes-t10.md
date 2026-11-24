# Translation notes, lane t10 (Chapters 31–32)

Source: English working tree. Files:
`docs/parts/06-technical-leadership/31-service-boundaries-and-ownership.ru.md`,
`docs/parts/06-technical-leadership/32-platform-engineering-developer-experience-and-modernization.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order, link targets, exercise labels, admonition types, Mermaid count, table rows and
table numbers identical; the multiset of numbers in the page matches (differences are only thousands
separators and the H1 anchor). Failure Modes use «Как заметить:» / «Что делать:» where the English has
Signal/Countermeasure fields (ch31); ch32's entries say "Detect it by…", rendered «Как заметить:» too,
since they are the same field. Words (wc -w; no-break spaces glue some tokens): ch31 5 862, ch32 5 677.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| co-change; co-change analysis | совместное изменение; анализ совместных изменений | T | ch31; follows baseline-data.ru, first-quarter.ru |
| coupling; logical coupling; coupling share | связанность; логическая связанность (logical coupling); доля связанности (coupling share) | T, B | ch31 |
| runtime and data coupling | связанность во время выполнения и через данные | T | ch31 |
| boundary strength / step | прочность границы / ступень | T | ch31 |
| package by convention / enforced module / owned module with a contract / separate deployable / service owning its data | пакет по соглашению / модуль с контролем зависимостей / модуль с владельцем и контрактом / отдельная развёртываемая единица / сервис, владеющий своими данными | T | ch31 |
| module / deployment / data / ownership boundary | граница модуля / развёртывания / данных / владения | T | ch31 |
| extraction; extract; consolidation (of services) | выделение; выделить; объединение | T | ch31, ch32; «выделение permissions» follows cast.ru |
| orphan, orphaned; disputed | бесхозный (компонент); спорный | T | ch31; «бесхозный» follows notes-t9 |
| distributed monolith | «распределённый монолит» | T | ch31 |
| entity service | «сервис-сущность» | T | ch31 |
| data nouns | существительные из модели данных | T | ch31 |
| bounded context; domain-driven design | ограниченный контекст (bounded context); предметно-ориентированное проектирование (domain-driven design) | B | ch31 |
| seam | шов | T | ch31, ch32 |
| mirroring hypothesis | «гипотеза зеркалирования» (mirroring hypothesis) | B | ch31 |
| fault isolation; eventual consistency | изоляция отказов; согласованность в конечном счёте (eventual consistency) | T, B | ch31 |
| saga; outbox; relay; dual writes; cutover | сага; «outbox» (исходящая очередь); ретранслятор; «двойная запись» (dual writes); переключение | T, B | ch31, ch32 |
| reconciliation check | проверка сверки | T | ch31 |
| grants (database) | выданные права доступа | T | ch31 |
| component registry; ownership test; ownership check | реестр компонентов; тест владения; проверка владения | T | ch31 |
| interim owner; interim incident lead | временный владелец; временный руководитель по инциденту | T | ch31; incident lead follows notes-t4 |
| open contribution | открытое участие | T | ch31 |
| orphan factory / ownership on paper / extraction by fashion / co-change worship | фабрика бесхозных компонентов / владение на бумаге / выделение по моде / культ совместных изменений | T | ch31 failure modes |
| platform adoption; opt in; non-adopters | принятие (adoption); переходить по своему желанию; неперешедшие (те, кто не перешёл) | B | ch32; «внедрение» avoided as it implies a push |
| feedback loop; loop latency | петля обратной связи; задержка петли | T | ch32 |
| context switch | переключение контекста | T | ch32 |
| flow state | состояние потока | T | ch32 |
| self-service | самообслуживание | T | ch32 |
| single intake; interrupt role | единый вход; роль дежурного по прерываниям | T | ch32; follows ch16.ru, notes-t3 |
| product-run platform / infrastructure queue | платформа, которую ведут как продукт / инфраструктурная очередь | T | ch32 |
| golden cage | «золотая клетка» | T | ch32 |
| cross-sectional (survey) | одномоментное (cross-sectional) | B | ch32 |
| change stability | стабильность изменений | T | ch32 |
| strangler fig; strangle; strangler slice | «фикус-душитель» (strangler fig); вытеснять; срез по схеме душителя, срез | B | ch32 |
| transitional architecture / code | переходная архитектура / переходный код | T | ch32 |
| facade; translation layer | фасад; слой трансляции | T | ch32 |
| parity checks; parity log; parity tests | проверки паритета (parity checks); журнал расхождений; тесты паритета | B | ch32 |
| fitness function | фитнес-функция (fitness function) | B | ch32; follows notes-t4 |
| ratchet | храповик | T | ch32 |
| disposable test databases | одноразовые тестовые базы данных | T | ch32 |
| run cost; toolchain run cost | стоимость эксплуатации; стоимость эксплуатации инструментария | T | ch32 |
| request-days | дней ожидания по запросам | T | ch32 |
| scaffolding (new service) | заготовка (scaffolding) | B | ch32 |
| central funding / showback / chargeback | централизованное финансирование / showback (показ затрат) / chargeback (внутренние списания) | T, B/E | ch32 |
| shadow tooling | теневые инструменты | T | ch32 |
| re-platforming | «перенос на новую платформу» | T | ch32 |
| developer portal; service catalog | портал для разработчиков; каталог сервисов | T | ch32 |
| deployment-event store | хранилище событий развёртывания | T | ch32; follows first-quarter.ru |
| ticket-ops with a portal / adoption by decree / four becomes five / the strangler that never strangles / rewrite by stealth / vanity adoption / the golden cage | тикеты под вывеской портала / принятие указом / из четырёх стало пять / душитель, который никого не душит / скрытое переписывание / принятие напоказ / золотая клетка | T | ch32 failure modes; «напоказ» matches notes-t6, notes-t7 |

Reused from earlier lanes: мерж-реквест, развёртываемая единица, ранбук (runbook), исключение,
руководитель по инциденту, релизный поезд (release train), массовый заказ, интеграция с бухгалтерской
системой, герметичный, пачка, посторонние падения, ограничители, команда содействия (enabling),
выделение на профилактику, свободный бюджет на инструменты.

## Doubts and notes on the English (English not changed)

- ch31 Example: "the requests that changed each module" uses "requests" for merge requests; rendered
  «запросы» after «мерж-реквесты» was introduced, as the English does.
- ch31 Example, point 3: "Platform Operations … made none of the 38" rendered «не внесла ни одного из
  38 изменений» (the 38 are core/permissions merge requests).
- ch31 Case: the table row "Covered by an exemption (a recorded, time-limited waiver)" glosses the
  term; rendered «записанное и ограниченное по сроку разрешение отступить от правил».
- ch31 Decision Framework: the closing sentence "Many proposals stop at … both work inside the
  monolith" is a comma splice in the English; Russian joins with «и оба шага выполняются внутри
  монолита».
- ch32 Failure Modes: entries use "Detect it by…" rather than "Signal:/Countermeasure:", and give no
  countermeasure; rendered with «Как заметить:» only.
- ch32 Example: "The figures come from Northstar's record" rendered «из хроники Northstar» (the year 1
  record page, per the term base «хроника года 1»).
- ch32 Case adoption table: "1 to 2 per product team" rendered «от 1 до 2» (numbers verbatim).
- ch32 Evidence section: "pp. 49–54" (prose) and "pp. 47–55" (references) differ in the English; both
  kept as written (one is the cited span, the other the whole chapter).
- ch32: "industry research, as DORA summarizes it" is an access-like note in reader text; rendered
  «отраслевое исследование в изложении DORA». Khadka: "the abstract reports" rendered «Согласно
  аннотации» (same pattern as notes-t8, notes-t9).

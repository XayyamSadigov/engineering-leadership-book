# Translation notes, lane t8 (Chapters 27–28)

Source: English working tree. Files:
`docs/parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.ru.md`,
`docs/parts/06-technical-leadership/28-architecture-decision-making-and-governance.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order, link targets, exercise labels, admonition types, Mermaid count, table rows and
table numbers identical (ch28 differs only by a dropped comma in one cell: "2, plus contract tests" →
«2 плюс контрактные тесты»). Failure Modes use «Как заметить:» / «Что делать:».
Words (wc -w; no-break spaces glue some tokens): ch27 5 625, ch28 5 538.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| inflow / stock / drain (the stock) | приток / запас / вычерпывать (запас) | T | ch27; «отток» avoided (term base: churn) |
| outcome / lever / investment (quality) | результат / рычаг / инвестиция | T | ch27 |
| shortcuts (loop node) | срезанные углы | T | ch27; follows notes-t5 |
| feature capacity | ресурс на функции | T | ch27 |
| pessimistic case | пессимистичный сценарий | T | ch27; English says "pessimistic", not "cautious" |
| dip (feature capacity) | просадка | T | ch27 |
| ownership inventory | инвентаризация владения | T | ch27 |
| feature freeze / quality sprint / tiger team / standing allocation / team-owned targets | заморозка функций / спринт качества / ударная группа (tiger team) / постоянное выделение / цели во владении команд | T, B for tiger team | ch27 |
| hand-back (central work) | передача обратно | T | ch27 |
| weekly operational review / monthly quality review / quarterly reset | еженедельный операционный разбор / ежемесячный обзор качества / квартальная перезагрузка | T | ch27; «обзор качества» follows first-quarter.ru |
| on-call leads | ведущие дежурные | T | ch27 |
| metric theater / practice mandates / action-item graveyard / silent dip / blame relapse | театр метрик / предписания практик / кладбище действий / тихая просадка / рецидив поиска виноватых | T | ch27 failure modes |
| mechanism measures | метрики механизмов | T | ch27 |
| decider | решающий | T | ch28; follows ch13.ru |
| agreement right | право согласия | T | ch28 |
| comment window | окно для комментариев | T | ch28 |
| reach / reversibility | охват / обратимость | T | ch28 |
| architecture review board; board | комитет по архитектурному ревью (architecture review board); комитет | B | ch28; term base "review board" = комитет по ревью; X1's proper name kept English with gloss |
| forum (of technical leaders) / signer | форум / подписант | T | ch28 |
| formal / real authority | формальная / реальная власть | T | ch28 |
| guardrails | ограничители | T | ch28; follows notes-t3 |
| ivory tower | башня из слоновой кости | T | ch28 |
| overrule; hallway overrule; executive overrule | отменить решение; отмена в коридоре; отмена решения сверху | T | ch28 |
| superseding ADR / superseded | новая ADR, которая заменяет прежнюю / заменена | T | ch28; ADR treated as feminine (запись) |
| ADR statuses proposed / accepted / superseded / rejected | предложена / принята / заменена / отклонена | T | ch28; ADR-0001's "Proposed" and "Accepted (recovered)" kept English as field values, glossed |
| recovered record | восстановленная запись | T | ch28 |
| design doc | дизайн-документ | T | ch28 |
| options paper | записка с вариантами | T | ch28 |
| rubber-stamp board | комитет, утверждающий не глядя | T | ch28; follows notes-t4 «утверждение не глядя» |
| Technology Radar rings Adopt / Trial | кольцо Adopt / Trial | E | ch28 |
| circuit breaker (resilience pattern) | автоматический выключатель (circuit breaker) | B | ch28; Shape Up's «предохранитель» is a different sense |
| read replicas | реплики для чтения | T | ch28 |
| posted-invoice export | экспорт проведённых счетов | T | ch28 |
| ledger (system area) | ledger (Latin) | E | ch28; follows notes-t5 |

## Doubts and notes on the English (English not changed)

- ch27 "spent two afternoons" rendered «две вторые половины дня».
- ch27 "two customers worth $9M in annual recurring revenue": ARR abbreviation not introduced, as the
  English does not use it (same choice as notes-t1).
- ch27 Example table row "(about 13 FTE by quarter 4)" rendered «к кварталу 4», not "Q4".
- ch27 "Expert opinion"-type labels: none; "industry research" for DORA is not bold in the English and
  stays unbolded.
- ch28 "expert opinion (economic theory)" rendered «мнение эксперта (экономическая теория)», bold as in
  the English.
- ch28 Buchgeher: "Their abstract reports" kept as «Согласно аннотации» (the English states the access
  level in prose; translated faithfully).
- ch28 "the providing team" → «команда-поставщик»; "consulted" column → «С кем консультируются».

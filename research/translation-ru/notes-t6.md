# Translation notes, lane t6 (Chapters 23–24)

Source: English working tree. Files: `docs/parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.ru.md`,
`24-reliability-slos-and-operational-readiness.ru.md`. Both pass `tools/validate_book.py` (no build run).
Structural check per chapter against the English: heading anchors in order, link targets, exercise labels,
admonition types, Mermaid count, table rows and table numbers identical.

## New terms (not in the term base; used consistently in these chapters)

| English | Русский | Rule used | Where |
|---|---|---|---|
| batch size | размер пачки (batch size) | B | ch23; «пачка» follows editing-ch02 |
| main branch / main | основная ветка; main (feminine: «main красная») | T | ch23; ch18 already uses «основная ветка» |
| merge (to main) | слияние (в main) | T | ch23 |
| gate (on the delivery path) / manual gate / human gate | контрольная точка / ручная контрольная точка / «Нужен человек?» (table column) | T | ch23; term base has «контрольная точка (gate)» for stage gate |
| commit stage / extended stage | стадия коммита / расширенная стадия | T | ch23 |
| build once | одна сборка | T | ch23 |
| promote (an artifact) | продвигать (артефакт) по окружениям | T | ch23 |
| unrelated failures | посторонние падения; падения по посторонним причинам | T | ch23 |
| false reds / red time | ложные красные (периоды) / красное время | T | ch23 |
| revert (a change) vs rollback | отменить изменение (revert) vs откат | T | ch23; kept distinct on purpose |
| revert first (rule) | правило «сначала отменить» (revert first) | B | ch23 |
| quarantine rule | правило карантина | T | ch23, links to Ch 22 |
| build steward | дежурный по сборке | T | ch23 |
| trunk-based development / trunk | разработка в основной ветке (trunk-based development) / «ствол» (trunk) | B | ch23 |
| release toggle (Hodgson); experiment, ops, permissioning toggles | релизный переключатель (release toggle); переключатели для экспериментов, эксплуатации и управления доступом | B | ch23 |
| code path | путь выполнения кода | T | ch23; glossary.ru «ветками кода» could be aligned (avoids clash with git branches) |
| deploy dark | скрытое развёртывание; развернуть скрыто | T | ch23 |
| tenant | тенант | T | ch23, ch24; not yet in the term base or other ru pages |
| blue-green / rolling deploy / flag rollout | сине-зелёное переключение (blue-green) / последовательное развёртывание (rolling) / раскатка через флаг (flag rollout) | B | ch23 |
| rollout (per tenant, staged store rollout) | раскатка | T | ch23 |
| expand and contract | расширение и сужение (expand and contract) | B | ch23 |
| segregation of duties | разделение обязанностей (segregation of duties) | B | ch23 |
| blast radius | радиус поражения (blast radius) | B | ch23 |
| change advisory board / change board | консультативный совет по изменениям (change advisory board) / совет по изменениям | B | ch23 |
| freeze (code freeze) | заморозка (кода) | T | ch23, ch24 |
| forward fix | исправление вперёд (forward fix) | B | ch23 |
| the cut (release cut) | срез релиза | T | ch23 table |
| regression pass | регрессионный прогон | T | ch23; matches glossary.ru |
| turnaround (review) | скорость ответа на ревью | T | ch23 |
| owner-based reviewers | ревьюеры из числа владельцев кода | T | ch23 |
| rubber-stamp review / the renamed train / flag debt / the untested rollback | ревью для галочки / переименованный поезд / долг по флагам / непроверенный откат | T | ch23 failure modes |
| credit notes | кредит-ноты | T | follows first-quarter.ru, baseline-data.ru |
| quarterly reset | квартальная перезагрузка | T | follows first-quarter.ru |
| user journey / critical user journey | пользовательский сценарий; сценарий (заказа, оплаты) / критический пользовательский сценарий (critical user journey) | B | ch24; «путь заказа или оплаты» kept for "order and payment paths" |
| good events / valid events | хорошие / валидные события | T | ch24 |
| SLI specification / SLI implementation | спецификация SLI / реализация SLI | T | ch24 |
| rolling window | скользящее окно | T | ch24 |
| correctness / freshness (SLI types) | корректность / свежесть | T | ch24 |
| probe; synthetic checks | проба; синтетические проверки | T | ch24 |
| precision / recall / detection time / reset time | точность (precision) / полнота (recall) / время обнаружения / время сброса | B | ch24 |
| multiwindow alerts | многооконные алерты | T | ch24 |
| page (verb/noun) | вызывать дежурного; вызов | T | ch24; «вызов» from notes-t1 |
| cause-based / symptom alerts | алерты по причинам / по симптомам | T | ch24; resolves the open point in notes-t1 (Ch 3) |
| four golden signals | четыре золотых сигнала | T | ch24 |
| context propagation / tail sampling | распространение контекста (context propagation) / хвостовое сэмплирование (tail sampling) | B | ch24 |
| trace / trace ID | трассировка / идентификатор трассировки | T | ch24 |
| Production Readiness Review / Operational Readiness Review | kept in English | E | ch24; proper names of the two companies' processes |
| reporting mode / shadow mode / full policy | режим отчётности / теневой режим / полная политика | T | ch24 |
| dated gap | пробел с датой устранения | T | ch24 |
| arbiter | арбитр | T | ch24 |
| primary / secondary (on-call) | основной / резервный дежурный | T | ch24 |
| shadow / reverse shadow | дежурство «в тени» (shadow) / обратное наблюдение (reverse shadow) | B | ch24 |
| handoff | передача смены | T | ch24 |
| escalation tier | уровень эскалации | T | ch24 |
| paid standby | оплачиваемая готовность | T | ch24 |
| game-day drills | учения (game day) | B | ch24 |
| vanity SLO / SLI shrinkage / 4xx blind spot / permanent freeze / alert accretion / readiness theater / invisible pager | SLO напоказ / усыхание SLI / слепое пятно 4xx / вечная заморозка / нарастание алертов / театр готовности / невидимый пейджер | T | ch24 failure modes |
| invoice reconciliation | сверка счетов | T | ch24 |
| distributor | дистрибьютор | T | ch24 |
| customer success (function) | служба работы с клиентами | T | ch24; Sofia Alvarez's title follows cast.ru («VP по работе с клиентами») |

## Doubts and observations (English not changed)

- Ch 23, Failure Modes: "Flag debt" has no "Signal:" field, only "Countermeasure:"; the Russian follows the
  English (only «Что делать:»). Same in Ch 24 for "The vanity SLO", "The 4xx blind spot", "The permanent
  freeze", "Alert accretion", "The invisible pager".
- Ch 23, Knight Capital: "nobody reviewed the deployment" rendered «само развёртывание никто не проверял»
  (review of the deployment procedure, not code review).
- Ch 23, "lowered tenfold by a mistyped value" and "a rate limit was lowered tenfold by a typo" rendered with
  «опечатка»; fine.
- Ch 24, line 125 of the English starts with a stray leading space (" The SLI types must follow…"); harmless,
  not reproduced in the Russian.
- Ch 24, Why This Matters: "Twenty-four components" kept as words («двадцати четырёх») as in the English.
- Ch 24, "the next work buys reliability" rendered «следующая работа идёт на надёжность» (sense, not image).
- Ch 24, "Its value is a decision made in advance": rendered as the policy's value («Ценность политики…»),
  which is what "Its" refers to.
- Both chapters: "this book's recommendation" without bold in running prose (Ch 24 decision framework,
  "This is the book's recommendation") translated without bold, as in the English.
- Word counts (wc -w; no-break spaces glue some tokens): ch23 5 693, ch24 5 805.

# Translation notes, lane t15 (Chapters 41–42)

Source: English working tree. Files:
`docs/parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.ru.md`,
`docs/parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, exercise labels,
admonition types, Mermaid count, table rows and every number in tables identical. Failure Modes: ch41 has
only "Detection:" → «Как заметить:»; ch42 has Signal/Countermeasure → «Как заметить:» / «Что делать:».
Words (wc -w; no-break spaces glue some tokens): ch41 5 589, ch42 5 251.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| rubric (manager assessment) | рубрика (лист критериев оценки) | T | ch41; term base allows «рубрика» for a scoring sheet; glossed once |
| dimension (of the rubric) | измерение | T | ch41; follows ch09.ru «измерения лестницы» |
| ratings Not yet / Solid / Strong / No evidence / Expectation not set | Пока нет / Уверенно / Сильно / Нет данных / Ожидание не задано | T | ch41; «Уверенно» follows ch07.ru rubric level «Уверенно»; «Пока нет» matches the book's «пока нет»; the template `engineering-manager-rubric` has no .ru page yet and should use the same labels |
| the six dimensions: outcomes in context / operational ownership / people growth / team health / cross-team leverage / running the role | результаты в контексте / ответственность за эксплуатацию / рост людей / здоровье команды / межкомандный рычаг / исполнение роли | T | ch41; short table headers: Результаты / Эксплуатация / Рост людей / Здоровье команды / Рычаг / Исполнение роли |
| evidence item; evidence file | свидетельство, датированный факт; папка свидетельств | T | ch41; «свидетельства» per notes-t2 |
| rating window | окно оценки | T | ch41 |
| rater effects; rater | эффекты оценщика; оценщик | T | follows notes-t2 |
| multisource feedback | обратная связь из нескольких источников | T | ch41 |
| manager artifact review; artifact-review slot | разбор артефактов руководителей; окно для разбора артефактов | T | ch41 |
| delegated decision; stretch decision | делегированное решение; решение на вырост | T | ch41; «задача на вырост» per notes-t14 |
| development focus / plan | фокус развития / план развития | T | ch41 |
| bench (leadership bench); bench action | резерв (резерв руководителей); действие по резерву | T | ch41; notes-t1 «резерв руководителей»; learning-roadmaps.ru says «скамейку руководителей», the maintainer may align it |
| trial assignments | пробные задания | T | ch41 |
| sponsor / sponsorship; over-mentored and under-sponsored | спонсировать / спонсорство; «много менторов и мало спонсоров» | T | ch41 |
| needs analysis; spaced sessions | анализ потребностей; занятия, разнесённые во времени | T | ch41 |
| cohort (internal program) | когорта | T | ch41 |
| return to engineering | возврат в инженеры | T | ch41 |
| interim cover / interim lead | временная замена / временный руководитель | T | ch41 |
| one-on-one recode | повторная разметка встреч один на один | T | ch41 |
| halo from outcomes / "No evidence" rated "Solid" / judging against unset expectations / skip-level shadow channel / director as super-manager / development plans without stretch / bench on paper | ореол от результатов / «Нет данных», оценённое как «Уверенно» / оценка по незаданным ожиданиям / теневой канал встреч через уровень / директор как сверхруководитель / планы развития без задач на вырост / резерв на бумаге | T | ch41 failure modes; «сверхруководитель» per notes-t14 |
| portfolio; initiative; portfolio limit | портфель; инициатива; лимит портфеля | T | ch42 |
| cross-team / single-team (item) | межкомандный / командный (пункт) | T | ch42 |
| slot (in the portfolio) | слот | T | ch42 |
| ranked waiting line | очередь по рангу; ранжированная очередь ожидания | T | ch42 |
| swap (portfolio) | замена | T | ch42; kept apart from ch38's «обмен» (trade) and the influence tactic «обмен» (exchange) |
| the rule at the limit | правило на пределе | T | ch42 |
| portfolio forum | портфельный форум | T | follows quarter-4-briefing.ru |
| reserved allowance (deal work) | зарезервированная квота | T | ch42 |
| heroic / structural version | версия с подвигами / структурная версия | T | ch42 |
| sales engineer | пресейл-инженер | T | ch42 |
| influence tactics: rational persuasion / inspirational appeal / consultation / pressure / coalition / legitimating / exchange / ingratiation | рациональное убеждение / вдохновляющий призыв / консультация / давление / коалиция / легитимация / обмен / снискание расположения (ingratiation) | T, B for ingratiation | ch42 |
| principled negotiation; best alternative to an agreement | принципиальные переговоры; лучшая альтернатива соглашению | T | ch42; the usual Russian rendering of Fisher and Ury |
| interest map | карта интересов | T | ch42 |
| joint decision; joint forum | совместное решение; общий форум | T | ch42 |
| relationship capital | капитал отношений | T | ch42 |
| commitment rule | правило обязательств | T | ch42; ch17.ru has no fixed noun for it |
| deal feature | функция для сделки | T | follows first-quarter.ru, timeline.ru |
| multi-currency price lists / catalog export / customer incident status notifications / automated service-credit statements / purchase approval rules | мультивалютные прайс-листы / экспорт каталога для клиентов / уведомления клиентов о статусе инцидентов / автоматические выписки по сервисным кредитам / правила согласования закупок | T | follows first-quarter.ru, timeline.ru |
| target band | целевой диапазон | T | follows ch38.ru (notes-t13 listed «полоса целей», but ch38.ru prose uses «целевой диапазон») |
| committed items | обещанные пункты | T | follows ch38.ru |
| prospect | потенциальный клиент | T | ch42 |
| quota (sales, CTO perspective) | план продаж | T | ch42 |
| phantom limit / internal work outside the portfolio / hero director / influence as pressure / interests guessed, not asked / evidence in engineering's language | фантомный лимит / внутренняя работа вне портфеля / директор-герой / влияние как давление / интересы угаданы, а не выяснены / доказательства на языке разработки | T | ch42 failure modes |

Reused: встреча через уровень (skip-level), уровни контроля из ch02.ru (Указание … Владение), операционные
минимумы tier 1, интервью об удержании (stay interview), карта знаний, нестабильные тесты, тесты на карантине,
еженедельный операционный разбор и журнал почти-инцидентов (Elena), практическая работа (Priya, follows
timeline.ru), единый вход, связь зависимости, годовой темп (run-rate), ежемесячный бизнес-обзор,
плановый сценарий, хроника года 1, «Год вкратце», действующие лица.

## Doubts and notes on the English (English not changed)

- ch41 Intro: "measuring managerial effectiveness in general is in Chapter 4, and coaching an individual in
  Chapter 5" — wrapped mid-reference ("Chapter\n5;"); harmless. The Russian avoids line-initial numbers.
- ch41 Rubric table: "One-on-ones held" rendered «Проведённые встречи один на один» (not «1:1») so the
  table-digit check stays clean; same in the Daniel Cho table ("84 of 90 one-on-ones").
- ch41 Lacerenza: "on-site location" rendered «на территории компании» (as opposed to off-site).
- ch41 "Offer the senior engineering level the person's skills support" read as "the (most) senior engineering
  level their skills support"; rendered «тот старший инженерный уровень, на который тянут навыки человека».
- ch41 Tom Becker's bench action "None yet" rendered «Пока ничего», to avoid a clash with the rating «Пока нет».
- ch41 X1 and Case: "Victor Lindqvist (CTO)" — CTO glossed once in the CTO Perspective section, which comes first.
- ch42 Why This Matters: "nine of the seventeen committed roadmap items" rendered «обещанных пунктов дорожной
  карты», matching ch38.ru «обещанные пункты».
- ch42 Case table, Amara's position "Commit the targets too" rendered «Включите в обязательства и цели».
- ch42 Case: "Sofia had co-written the severity definitions" — co-written with whom is not said; rendered
  «участвовала в написании», matching cast.ru («Помогала писать определения серьёзности»).
- ch42 Enterprise: "Chapter 39 records its decisions" rendered «Его решения записываются так, как описано в
  главе 39» (the chapter describes the decision log; it does not itself record anything).
- ch42 "sales operations" glossed as «в отделе продаж (sales operations)».
- ch42 CTO Perspective: "quota" (sales) rendered «план продаж».

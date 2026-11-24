# Translation notes, lane t14 (Chapters 39–40)

Source: English working tree. Files:
`docs/parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.ru.md`,
`docs/parts/09-engineering-directorship/40-the-directors-job.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order, link targets, exercise labels, admonition types, Mermaid count, table rows and
every number in tables identical (ch39 differs only by a comma after "Tier 1" in one report-table cell, a
checker false positive). The multiset of numbers in the page matches, except «1:1» in one ch40 diagram
label. Words (wc -w; no-break spaces glue some tokens): ch39 5 929, ch40 5 530.

Failure Modes: ch39 has Signal/Countermeasure fields → «Как заметить:» / «Что делать:» (two entries have
only a countermeasure, as in the English). Ch40 entries are prose; only "Detect it with…" became
«Как заметить:», the other entries stay unlabeled prose, as in the English.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| review (quality / architecture / talent) | обзор (обзор качества / архитектурный обзор / обзор талантов) | T | ch39, ch40; follows the ru nav title of ch39 («Обзоры…»), notes-t2 «обзор талантов», notes-t8 «обзор качества» |
| inspection (of the system) | проверка системы | T | ch39 |
| presenter | докладчик | T | ch39 |
| trial (of the presenter); the review as trial | суд над докладчиком; обзор как суд | T | ch39 |
| mum effect | эффект умолчания (mum effect) | B | ch39, ch40 |
| corroborate; corroboration through structure | перепроверять; перепроверка через структуру | T | ch39 |
| needed by | «нужно к»; дата «нужно к» | T | ch39; follows glossary.ru «Журнал решений» |
| decider; lowest common decider / level / manager | решающий; ближайший общий решающий / уровень / руководитель | T | ch39; follows notes-t8, notes-t11 |
| joint case; joint escalation write-up | совместное обоснование; совместная записка для эскалации | T | ch39; follows glossary.ru «Путь эскалации» |
| clock (of an escalation) | срок; «в ограниченный срок» | T | ch39 |
| backchannel decision / corridor decision | решение в обход пути / решение в коридоре | T | ch39; «в коридоре» follows notes-t8 «отмена в коридоре» |
| escalation as threat / escalation by stamina | эскалация как угроза / эскалация на выносливость | T | ch39 |
| watermelon report | отчёт-арбуз | T | ch39 |
| headline (report section) | главный вывод | T | ch39 |
| status colors green / amber / red | зелёный / жёлтый / красный | T | ch39; «жёлтый» is the usual Russian RAG word |
| framing vs misleading | подача и введение в заблуждение | T | ch39 |
| shaded report | приукрашенный отчёт | T | ch39 |
| log steward (rotating) | хранитель журнала (роль переходит по кругу) | T | ch39 |
| escalation map | карта эскалаций | T | ch39 |
| stretch assignment / ladder fix / flight risk | задача на вырост / исправление карьерной лестницы / риск ухода | T | ch39 |
| fitness checks | проверки фитнес-функций | T | ch39; fitness function per notes-t4 |
| target band (quarterly plan) | целевой диапазон | T | ch39; ch38.ru did not exist when this was written; align with its rendering |
| sign-off (of a plan) | утверждение | T | ch39 |
| final customer acceptance; contractual items | финальная приёмка у клиента; пункты контракта | T | ch39 |
| exposures (what the board needs) | показатели того, чем рискует компания | T | ch39; sense rendering |
| signal source; firsthand signal | источник сигналов; сигнал из первых рук | T | ch39, ch40 |
| direct data / raw data | прямые данные / сырые данные; первичные записи (raw incident records) | T | ch40 |
| source cut / horizon cut (calendar audit) | срез по источнику информации / по горизонту | T | ch40 |
| skip-level rule; skip-level rotation; group skip-level | правило встреч через уровень; ротация встреч через уровень; групповая встреча через уровень | T | ch40 |
| unallocated buffer | нераспределённый резерв | T | ch40 |
| time famine (Perlow) | хроническая нехватка времени (time famine) | B | ch40 |
| managed by summaries / super-manager / data tourist / incident commander in chief / quality delegated / calendar by default / learning stops at day 90 | управляемый сводками / сверхруководитель / турист в данных / главнокомандующий инцидентами / делегированное качество / календарь по умолчанию / обучение заканчивается на Дне 90 | T | ch40 failure modes |
| watch list | список неблагонадёжных | T | ch40 |
| peer network; sustainability | сеть коллег; устойчивость | T | ch40 |
| **this book's reasoning** (evidence label) | **рассуждение книги** | T | ch40; not in glossary 4.3; formed like «синтез книги» |

Reused from earlier lanes: обзор талантов, обзор качества, условие пересмотра, решающий, «пока нет»,
нежелательная текучесть, задокументированная практика, синтез книги, кредит-ноты, сопоставление заказов и
счетов, массовый заказ, интеграция с бухгалтерской системой, режим отчётности, арбитр, форумы (ch37.ru),
еженедельная встреча команды руководителей (ch37.ru), ежемесячный бизнес-обзор, те, кто чинит,
неформальный лид, интервью об удержании (stay interview), проверка здоровья команды, руководитель
разработки высшего уровня.

## Doubts and notes on the English (English not changed)

- ch39 title: the ru nav says «…отчётность перед руководством»; the term base gives "executive
  reporting / executive report" as «отчётность для руководства / отчёт для руководства». H1 follows the
  nav; body text uses the term base («отчёт для руководства»). The maintainer may want one form.
- ch39 "These are research findings, as the abstracts report them": access note in reader text; rendered
  «научные результаты в изложении аннотаций» (same pattern as notes-t8 to t10).
- ch39 Case: ADR-0001 treated as feminine («ADR-0001 оставалась открытой»), per notes-t8.
- ch39 Example: "In week 7 the record showed" rendered «в записях значились» (the incident record).
- ch39 X3: "lifts it from just under the contractual 99.9 percent to just over" rendered with «с уровня
  чуть ниже… до уровня чуть выше».
- ch39 The week 26 report blockquote keeps its table numbers verbatim (`99.86%`,
  `$95,000`), as tables.
- ch40 Learning Objectives has no "After this chapter you will be able to:" lead-in in the English; none
  added.
- ch40 "Larson, 2023 … an engineering executive's job": «руководитель разработки высшего уровня»
  (notes-t1).
- ch40 X1: Victor's quote uses «вы» («Вы нужны мне…»), to avoid «ты» in the book.
- ch40 X2: "flat operating expense (the running cost, mostly salaries)" rebuilt to avoid two parentheses in
  a row; the glossary link keeps «операционные расходы (opex)».
- ch40 Decision Framework table: "What do customers experience?" rendered «Что видят клиенты?».

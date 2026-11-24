# Translation notes, lane t18 (Chapters 47–48)

Source: English working tree. Files:
`docs/parts/11-vp-engineering/47-the-vp-of-engineering.ru.md`,
`docs/parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, exercise labels,
admonition types, Mermaid count and node ids, table rows and every number in tables identical. No
wrapped line starts with a number followed by a period. Words (wc -w; no-break spaces glue some
tokens): ch47 5 764, ch48 5 891.

Failure Modes: ch47 uses "Signal:" + "Detection:" (like ch35), rendered «Признак:» / «Как заметить:»,
following the ch35 precedent (notes-t12, editing-ch35), since there is no countermeasure field. Ch48 has
only "Detect:" → «Как заметить:».

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| area (a director's area) | направление | T | ch47, ch48; follows glossary.ru («карта показателей его направления») |
| director team; director team meeting | команда директоров; встреча команды директоров | T | ch47 |
| portfolio review | обзор портфеля | T | ch47 |
| operating review (VP, monthly) | операционное ревью | T | term base 3.8 |
| first team (Lencioni, Larson) | «первая команда» | T | ch47 |
| shared goal / area goals | общая цель / цели направления | T | ch47 |
| investable capacity; investable | ресурс для инвестиций; «Для инвестиций» (table header) | T | ch47; follows halvard.ru |
| run work | поддерживающая работа | T | ch47; follows halvard.ru |
| gap (funded work vs headcount); gap table | разрыв; таблица разрывов | T | ch47, ch48 |
| reallocation; reallocation trigger | перераспределение; триггер перераспределения | T | ch47 |
| capacity claims | притязания на ресурс | T | ch47 |
| director bench | резерв директоров | T | ch47; «резерв руководителей» per notes-t1 |
| the large director (Ch 4 phrase) | «большой директор» | T | follows ch04.ru |
| pass-through VP | VP-передатчик; уровень-передатчик | T | ch47; «уровень-передатчик» follows notes-t11 |
| director tournament / unreplaced director | турнир директоров / незаменённый директор | T | ch47 failure modes |
| upper echelons theory | теория верхних эшелонов (upper echelons theory) | B | ch47 |
| partition dependence | зависимость от разбиения (partition dependence) | B | ch47 |
| formal / real authority | формальная / реальная власть | T | follows notes-t8 |
| acting (role) / stretch scope | исполняющий обязанности / расширенная область ответственности | T | ch47 |
| product lead | продуктовый лид | T | ch47 |
| merchants (Halvard) | продавцы | T | follows halvard.ru |
| flat-headcount rule | правило «без роста численности» | T | term base «без роста численности» |
| firsthand time | время из первых рук | T | ch47; «сигнал из первых рук» per notes-t14 |
| stock / flow (workforce) | запас / поток | T | term base 3.x |
| time to fill; vacancy weeks | срок закрытия вакансии; недели вакансий | T | ch48 |
| backfill; like-for-like backfill | найм на замену, замена; замена один к одному | T | ch48; «найм на замену» per notes-t1/t2 |
| level mix; senior drift | состав по уровням; сдвиг к старшим уровням | T | ch48 |
| level band; band per domain; senior band | диапазон по уровням; свой диапазон для каждой предметной области; диапазон доли senior | T | ch48 |
| entry level | начальный уровень | T | ch48 |
| absorption (of hires) | способность принять новых людей | T | ch48 |
| rate card | тарифная ставка (rate card) | B | ch48 |
| loading factor | коэффициент нагрузки | T | ch48, glossed as in English |
| sourcing model | модель привлечения людей | T | ch48 |
| offshoring | офшоринг | T | ch48 |
| colocated | в одном месте | T | ch48 |
| follow-the-sun development | разработка «вслед за солнцем» (follow-the-sun) | B | ch48; notes-t3 has the on-call variant |
| abandoned files | брошенные файлы | T | ch48 |
| contractor bench | скамейка подрядчиков | T | ch48 |
| vendor scope | объём работ вендора | T | ch48 |
| three vendor tests: bounded / verifiable / not core knowledge | ограниченность / проверяемость / не ключевые знания | T | ch48 |
| externality; externality test | внешний эффект (экстерналия); тест на внешний эффект | T | ch48 |
| enforcement point | точка контроля | T | ch48 |
| exception path | порядок исключений | T | follows notes-t4 |
| attestation | подтверждения (attestation) | B | follows notes-t4 |
| enterprise policy / rule | корпоративная политика / общекорпоративное правило | T | ch48 |
| CTO's staff | аппарат CTO | T | ch48 |
| common review format | единый формат обзоров | T | ch48 |
| hire ahead | найм на опережение | T | ch48 |
| vacancy underspend | недорасход на вакансиях | T | ch48 |
| budget pack | бюджетный пакет | T | ch48; «пакет для совета директоров» kept for board pack |
| CI consolidation phase 1 | этап 1 консолидации CI | T | ch48; «целевая система CI» per quarter-4-briefing.ru |
| Senior Vice President of Engineering | Senior Vice President of Engineering (старший вице-президент по разработке) | B/E | ch48 X2 |
| backfill by reflex / silent senior drift / rate-card offshoring / the vendor who became the owner / headcount freeze, contractor thaw / policy inflation / governance by attestation / the reflex layer | замена на рефлексе / тихий сдвиг к старшим уровням / офшоринг по тарифной ставке / вендор, ставший владельцем / численность заморожена, подрядчики оттаяли / инфляция политик / управление через подтверждения / уровень на рефлексе | T | ch48 failure modes |

Level names Engineer / Senior / Staff / Principal kept in English as level names (notes-t2).
*The Five Dysfunctions of a Team* glossed once with its published Russian title «Пять пороков команды».

## Doubts and notes on the English (English not changed)

- ch47 "the blind spot the director team lacks" is self-contradictory (a team lacks the perspective
  that covers its blind spot, not the blind spot). Rendered by sense: «какого взгляда не хватает команде
  директоров». The English may want "the perspective the director team lacks".
- ch47 F2 names "Halvard's VP of Fulfillment"; halvard.md lists the groups as Commerce, Field
  Operations, Insights, Payroll and platform, with no Fulfillment. Kept as written; the exercise may
  want "Field Operations" or a note that the group is hypothetical.
- ch47 Failure Modes use Signal/Detection, but several "Detection:" fields are really countermeasures
  ("reallocation requests go only through the director team meeting"). Rendered «Как заметить:» as the
  field name; the maintainer may want one label set book-wide (same point as notes-t12 for ch35).
- ch47 Playbook item 9 continuation line is indented by four spaces in the English (others by three);
  harmless, normalised in Russian.
- ch47 Bardolet: "applying it to engineering capacity is this book's extension" is not bolded as a label
  in the English; kept unbolded.
- ch48 "Larson's primer on the engineering executive's job counts planning…" rendered with
  «руководителя разработки высшего уровня» (notes-t1).
- ch48 "Šmite … its abstract reports" is an access note in reader text; rendered «согласно его
  аннотации» (same pattern as notes-t8 to t14).
- ch48 Example: "Senior and above rises to 325 (65 percent)": rendered as a count («Число инженеров
  уровня Senior и выше растёт до 325 (65%)»).
- ch48 Example: "about 1 percent of the held-mix payroll of $102.9 million" rendered «около 1% фонда
  оплаты труда при сохранённом составе ($102,9 млн)».
- ch48 Case facts table: "one currency and rounding" (ellipsis of "one person could change") rendered
  «и валюты и округление — тоже один».
- ch48 Case: "Victor wants ledger risk first" read as "wants the ledger risk addressed first"; rendered
  «хочет прежде всего снизить риск по ledger».
- ch48 Option table "Saves about $91,000 (level) and $174,000 (location)": numbers kept verbatim in the
  table.

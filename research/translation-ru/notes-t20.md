# Translation notes, lane t20 (Chapters 51–52)

Source: English working tree. Files:
`docs/parts/12-cto-leadership/51-enterprise-technology-strategy.ru.md`,
`docs/parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, citation link
texts, exercise labels, admonition types (ch52 keeps its collapsible `??? note` with indented tables),
Mermaid count and node ids, table rows and every number in tables identical. No wrapped line starts with
a number followed by a period. Prose number differences are word forms ("year two", "the second year"
where the English writes "year 2" in ch51) and the thousands separator. Words (wc -w; no-break spaces
glue some tokens): ch51 5 761, ch52 7 464.

Failure Modes: ch51 has only "Early sign:" → «Как заметить:» (follows notes-t16 for ch43); ch52 has
"Signal:" in one entry and "Detect:" everywhere → «Признак:» / «Как заметить:» (follows notes-t12 for
ch35, notes-t18 for ch47).

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| technology strategy (CTO) / technical strategy (director) | технологическая стратегия / техническая стратегия | T | ch51; follows the ru nav titles of ch30 and ch51 |
| business choices | выборы бизнеса | T | ch51 |
| where to play / how to win | где играть / как выигрывать | T | ch51; follows ch45.ru |
| required capabilities | нужные возможности | T | ch51 |
| guiding policy | направляющая политика | T | follows notes-t9 |
| the four bins: excellent / adequate / buy / not doing | четыре группы: «отлично» / «достаточно» / «покупать» / «не делать» | T | ch51; follows first-quarter.ru («Отлично / Достаточно / Покупать / Не делать», «группы») |
| parity (with competitors) | паритет | T | ch51 |
| operational effectiveness | операционная эффективность | T | ch51 |
| alignment (IT–business) / agility | согласованность (alignment) / гибкость (agility) | B | ch51 |
| deliberate / emergent strategy | преднамеренная / эмерджентная стратегия | T | ch51; glossed «возникающей по ходу дела» once |
| kinds of bet; Strengthen / Extend / Explore | виды ставок; Укрепить / Расширить / Исследовать | T | ch51; table lines «Расширение» / «Исследование» |
| demand and design (what is known) | спрос и устройство решения | T | ch51; «дизайн» avoided (reads as visual design) |
| option / probe / decision point / kill criterion; kill (an option) | опцион / проба / точка решения / критерий закрытия; закрыть опцион | T | ch51; first-quarter.ru uses «пробная проработка» and «исследование» for the two named probes |
| exercise (an option) | исполнить опцион | T | ch51 |
| decision calendar | календарь решений | T | ch51 |
| discovery-driven planning | планирование через открытия (discovery-driven planning) | B | ch51 |
| layered technology roadmap; market drivers | многоуровневая технологическая дорожная карта; рыночные факторы | T | ch51 |
| coherence tests: trace / says no / genericity / arithmetic / stress / reinforcement / premortem | проверки на согласованность: прослеживаемость / отказ / шаблонность / арифметика / стресс / взаимное усиление / премортем | T | ch51 |
| orphans (roadmap items) | пункты-сироты | T | ch51 |
| reliability dividend | дивиденд надёжности | T | ch51 |
| stress case / stress rule; bad year | стрессовый сценарий / правило на случай стресса; плохой год | T | ch51; «правило на случай стресса» follows first-quarter.ru |
| estate currency | актуальность ландшафта | T | ch51; first-quarter.ru table has «Актуальность технологий» |
| capacity envelope | рамки ресурса | T | ch51; by analogy with «рамки бюджета» |
| people lane / people line | раздел о людях / строка о людях | T | ch51; «строка о людях» follows first-quarter.ru |
| Converge before adding | «Сначала сократить, потом добавлять» | T | ch51; follows ch30.ru, since ch51 says the policy extends the director's (ch30) policy. first-quarter.ru writes «сначала сближать, потом добавлять» and glossary.ru names continuation stage 3 «Сближение»; the maintainer may unify |
| Reliability before reach / Money data moves by contract | «Надёжность прежде охвата» / «Денежные данные передаются по контракту» | T | ch51; follow first-quarter.ru |
| ledger posting events | события проводок ledger | T | follows first-quarter.ru |
| multi-currency invoicing and ledger / ordering API / higher availability tier | мультивалютные счета и ledger / API заказов / более высокий уровень доступности | T | follows first-quarter.ru |
| the orphan strategy / everything is strategic / the three-year Gantt chart / funding by hope / options that never die / the CTO's own exception | стратегия-сирота / всё стратегическое / трёхлетняя диаграмма Ганта / финансирование надеждой / бессмертные опционы / исключение для самого CTO | T | ch51 failure modes |
| lens (income statement, balance sheet, cash flow) | ракурс | T | ch52; «линза» avoided as a calque in running prose («через линзу») |
| booking (how an item is booked) | способ учёта; как учитывается | T | ch52 |
| cost of revenue / gross profit / operating income / net income | себестоимость выручки / валовая прибыль / операционная прибыль / чистая прибыль | T | ch52; follow first-quarter.ru finance table |
| research and development (R&D); general and administrative (G&A) | исследования и разработка (R&D); общие и административные расходы (G&A) | B | ch52 |
| deferred revenue; accounts receivable; payables and accrued expenses; accrued compensation; prepaid and other; property and equipment, net; shareholders' equity | отложенная выручка (deferred revenue); дебиторская задолженность; кредиторская задолженность и начисленные расходы; начисленные вознаграждения; предоплаты и прочее; основные средства, нетто; собственный капитал | T, B for deferred revenue | ch52; first-quarter.ru has «…и начисления» for payables; «начисленные расходы» chosen as the standard Russian line name |
| operating / investing / financing (cash flow) | операционный / инвестиционный / финансовый (денежный поток, деятельность) | T | ch52 |
| free cash flow | свободный денежный поток (free cash flow) | B | ch52 |
| amortization / depreciation | амортизация НМА / амортизация ОС (both «амортизация» in prose) | T | ch52; the terms box explains that Russian uses one word; table cells «амортизация НМА», «амортизация ОС» as in first-quarter.ru |
| working capital | оборотный капитал (working capital) | B | ch52 |
| controller | финансовый контролёр (controller) | B | ch52 |
| impairment; write down; write-off | обесценение (impairment); списать стоимость вниз; списание | T, B for impairment | ch52 |
| significant development uncertainty | существенная неопределённость разработки (significant development uncertainty) | B | ch52 |
| internal-use software; software-as-a-service | ПО для внутреннего использования; SaaS (ПО как услуга) | T | ch52 |
| substantially complete | по существу завершено | T | ch52 |
| maintenance (accounting sense) | сопровождение | T | ch52 |
| latest estimate (LE) | последняя оценка (LE, latest estimate) | B | ch52; follows first-quarter.ru «последняя оценка финансов» |
| variance; variance review | отклонение (variance); разбор отклонений | B | ch52 |
| fixed / variable; committed / discretionary | постоянные / переменные затраты; обязательные / дискреционные расходы | T | ch52 |
| padding; slack | запас в оценках; резерв (slack) | T, B for slack | ch52 |
| use-it-or-lose-it | «используй или потеряешь» | T | ch52 |
| rolling forecast; quarterly reforecast | скользящий прогноз; квартальный пересмотр прогноза | T | ch52 |
| committed-use discount | скидка за обязательство по потреблению (committed-use discount) | B | ch52 |
| decisive input | решающий параметр | T | ch52 |
| merit increase | повышение по результатам (merit increase) | B | follows notes-t2; first-quarter.ru has «повышение по заслугам» — the maintainer may unify |
| finance business partner | финансовый бизнес-партнёр | T | ch52 |
| Finance's day rate | дневная ставка финансов | T | follows notes-t9 |
| extended support / free community support | расширенная поддержка / бесплатная поддержка сообщества | T | ch52 |
| remediation service level | срок устранения | T | ch52 |
| growth-equity firm; minority investor | фонд роста (growth equity); миноритарный инвестор | T | follows cast.ru |
| debt refinancing | рефинансирование долга | T | ch52 X2 |
| capitalization drift / the amortization tail and impairment surprise / sandbagging and use-it-or-lose-it / vacancy counted as efficiency / EBITDA mistaken for cash / the single-point case / the unowned variable cost | дрейф капитализации / «хвост» амортизации и внезапное обесценение / запас в оценках и «используй или потеряешь» / вакансии, засчитанные как эффективность / EBITDA, принятая за деньги / обоснование с одной цифрой / переменные затраты без владельца | T | ch52 failure modes |

Reused from earlier lanes and the term base: рамки бюджета, операционный план, годовой темп (run-rate),
пакет для совета директоров, полная стоимость сотрудника, коэффициент аннуитета, ставка
дисконтирования, точка безубыточности, оптимистическое искажение (optimism bias), стратегическое
искажение данных, прогнозирование по референтному классу, спонсор, «жетоны на инновации», «ядро»
стратегии (kernel), продолжение, выделение на профилактику, выделение permissions, массовый заказ,
хранилище событий развёртывания, данные о ставках, ресурс, руководитель разработки высшего уровня.

## Doubts and notes on the English (English not changed)

- ch51 and ch52: several overlong source lines (ch51 lines 23, 250, 369; ch52 lines 124, 151, 406, 533,
  677); cosmetic.
- ch51 A2: "Decision due week 46" for the organization proposal, in an exercise set in week 47. Consistent
  with "none decided" (the decision is overdue), translated as written.
- ch51 Case: "Ines Carvalho … the ledger's currency and rounding still depended on one person" — kept;
  matches baseline facts in first-quarter.ru.
- ch51 Example: "Horizon 3's 2 FTE buy the information" rendered «Горизонт 3 с его 2 FTE покупает
  информацию» to avoid a sentence that opens with a figure.
- ch51 prose uses word forms for "year 2/3" («второй год», «третьего года»); tables keep «Год 2».
  ch52's terms box says prose uses "year 1" and "year 2", so ch52 prose uses label forms («бюджет
  года 2») except "the director's first year" and "year 1 of each option" (A2), which are not labels.
- ch52 Related chapters: 48 and 49 are plain numbers, not links, in the English; kept as text.
- ch52 Case: Victor's note rounds $194,400 to "$194,000"; kept as written.
- ch52 Example: the cost-of-revenue cell groups "Support, success, and services staff 26.5" and "fees and
  other 8.9", while first-quarter.md splits them (18.0 + 8.5; 6.0 + 2.9). The sums agree.
- ch52 "This chapter is not accounting advice": rendered as a plain sentence (no admonition in the
  English).

# Russian edition: term base and style guide

Binding for every translator of the Russian edition (`*.ru.md` beside each English page, served under
`/ru/`). Read it in full before translating a page; add a term here before using a new rendering in a
page. When this file and an already translated page disagree, this file wins and the page is fixed.

The English edition is the source of truth. A Russian page translates its English page as it stands; it
does not add, drop, or "improve" claims, numbers, citations, or evidence labels. If the English page
changes, the Russian page is re-synced or the change is noted at the end of this file under
"Sync debt".

## 1. Site and file mechanics

- One file per page: `docs/<path>/page.ru.md` beside `docs/<path>/page.md` (mkdocs-static-i18n, suffix
  mode). Never move or rename an English file. A page without a `.ru.md` is shown in English on the
  Russian site.
- Nav labels are translated in `mkdocs.yml` under the `ru` language's `nav_translations`, not in the page.
  A new nav entry needs a new translation line there.
- **Anchors.** Every heading in a Russian page carries the English page's anchor as an explicit id:
  `## Компания { #the-company }`. Reasons: MkDocs' default slugifier drops Cyrillic (a Russian heading
  would get an id like `_1`), and links from other pages (`glossary.md#lead-time`) must land on the same
  heading in both languages. Take the id from the built English page (`site/<page>/index.html`) or the
  English link that points at it; keep headings in the English order.
- **Links** keep their English targets: `[Глава 45](parts/.../45-....md#reading-a-business-model)`. The
  i18n plugin sends a link to the Russian page when one exists, otherwise to the English page. Do not
  link to `*.ru.md` explicitly.
- **Citations and the bibliography stay in English**: link text such as `Forsgren et al., 2018`, book and
  paper titles, author names. Translate only the sentence around them. A source title may be glossed in
  Russian in parentheses once, if it helps the reader, never replaced.
- Mermaid diagrams: translate node labels, keep node ids and structure. Keep labels short (Russian runs
  about 20 percent longer than English; abbreviate rather than wrap). Quote labels with punctuation.
- Admonition types (`info`, `warning`, `note`, `tip`) stay; only the quoted title is translated (section 5).
- Front-matter-free Markdown; `{ #id }` needs the `attr_list` extension, which is already on.

## 2. Style rules

1. **Natural Russian for engineers, not a literal translation.** Rebuild sentences: Russian prefers verbs
   to English noun stacks ("the decision log review cadence" → «как часто пересматривается журнал
   решений»). Split long English sentences when Russian gets heavy. Keep the book's voice: direct, concrete,
   short paragraphs, no filler, no bureaucratic register («осуществлять», «данный», «в рамках» are banned
   where a plain verb works).
2. **Address the reader as «вы»**, lowercase, as in technical books. Imperatives in playbooks use the
   polite plural: «Запишите», «Проверьте».
3. **Quotes**: «ёлочки» for first level, „лапки“ for nested. Code, file names, and literal values stay in
   backticks.
4. **Dashes**: the em dash (—) with spaces is allowed and natural in Russian prose (unlike the English
   edition). Use the en dash (–) without spaces for ranges: 50–150 инженеров, недели 1–13. Hyphen only
   inside words (код-ревью, staff-инженер).
5. **Non-breaking spaces** (U+00A0) between a number and its unit or counted noun where a line break
   would strand it (`80 инженеров`, `13 недель`, `12 FTE`) and inside numbers with a thousands separator
   (`$185 000`). Percentages take no space: `99,9%`. Do not chase every case; numbers with units come
   first.
6. **Numbers — one rule.** In running text (paragraphs, list items, headings, admonitions) use Russian
   format: a non-breaking space as thousands separator, a comma as decimal separator: `1 900 тест-кейсов`,
   `2,2 часа`, `$140 млн`. **Inside tables, copy every number exactly as in the English table**
   (`1,900`, `2.2`, `$140M`), whatever the table is about. Rationale: many tables mirror the CSV files in
   `docs/case-studies/northstar/data/`, which win any disagreement; keeping all table numbers verbatim makes
   every table diffable against the English page and the CSVs without judgment calls. Percent sign without a
   space (`47%`, «47 процентов» in prose is also fine). Money: `$185 000` in prose (dollar sign kept, the
   company is American), `$1,2 млн`, `$250 тыс.`; never convert currency.
7. **Dates and weeks**: «неделя 14», «в неделю 26» (the book's week numbers are labels, not dates);
   quarters: «квартал 1» in Northstar labels (matches "quarter 1" as a label), «первый квартал» in prose
   where it reads better. Fiscal year: FY1 stays.
8. **Names stay in Latin script**: people (Victor Lindqvist, Li Na Zhou, Priya Raman), companies
   (Northstar Technologies, Halvard Systems), products and systems (Core, Ledger, Jira, GitHub), team names
   used as proper names (Core team → команда Core). Russian case endings are not attached to Latin names;
   rephrase («у Victor», «команде Core», «директор Halvard»). Real organizations (Google, DORA, NIST, CISA)
   also stay Latin.
9. **Abbreviations** stay as in English when they are the working vocabulary (SLO, ADR, FTE, ARR, PIP,
   OKR, KEV, SBOM, CI/CD); explain them in Russian on first use on a page.
10. **Gender-neutral roles**: Russian role nouns are grammatically masculine (директор, руководитель);
    this is the normal neutral form. When the English page gives a person's pronoun, follow it in verb
    agreement («директор решила» for a named woman).
11. **Evidence labels** are translated with the fixed renderings in section 4 and keep their function:
    every label in the English sentence appears in the Russian one.
12. **Do not translate**: code, CSV column names, field names in templates that readers copy into tools
    (give a Russian gloss in parentheses on first use if needed), incident ids (INC-401), decision ids
    (DL-07), ADR numbers, URLs.

## 3. Term base

Rule codes: **T** translate with the given term; **E** keep in English (Latin script, no translation);
**B** both on first use on each page, Russian first: «бюджет ошибок (error budget)», then the Russian term
alone; **B/E** both on first use, then the English term alone (used where Russian practitioners
overwhelmingly say the English word).

### 3.1 Roles and levels

| English | Русский | Rule | Note |
|---|---|---|---|
| engineering manager (EM) | руководитель разработки (engineering manager, EM) | B | then «руководитель разработки» or EM; not «инженерный менеджер» |
| manager of managers | руководитель руководителей | T | |
| first-line manager | линейный руководитель | T | |
| director (of engineering) | директор по разработке; директор | T | |
| VP of Engineering | VP of Engineering (вице-президент по разработке) | B/E | title stays English in nav |
| CTO | CTO (технический директор) | B/E | |
| CFO, CEO, CPO | CFO, CEO, CPO | E | gloss once: финансовый директор, генеральный директор |
| individual contributor (IC) | индивидуальный исполнитель (IC) | B | |
| senior engineer | senior-инженер | E | hyphenated hybrid is the working norm |
| staff engineer | staff-инженер | E | |
| principal engineer | principal-инженер | E | |
| staff-plus engineer | staff-plus-инженер | E | |
| tech lead | техлид | T | |
| team lead | тимлид | T | |
| architect | архитектор | T | |
| product manager | продакт-менеджер | T | |
| QA engineer | QA-инженер | E | |
| SRE | SRE | E | |
| incident commander | координатор инцидента (incident commander) | B | not «командир» |
| on-call engineer | дежурный инженер | T | |
| direct report | прямой подчинённый | T | |
| skip-level (meeting) | встреча через уровень (skip-level) | B | |
| stakeholder | стейкхолдер | T | «заинтересованная сторона» in formal governance text |
| board (of directors) | совет директоров | T | |
| audit committee | комитет по аудиту | T | |
| successor | преемник | T | |

### 3.2 People management

| English | Русский | Rule | Note |
|---|---|---|---|
| one-on-one (1:1) | встреча один на один (1:1) | B | then «1:1» |
| coaching | коучинг | T | |
| mentorship | менторство | T | |
| feedback | обратная связь | T | |
| difficult conversation | трудный разговор | T | |
| hiring | найм | T | |
| structured interview | структурированное интервью | T | |
| interview loop | цикл интервью | T | |
| work sample | рабочее задание (work sample) | B | |
| rubric | критерии оценки; рубрика | T | «рубрика» only for a scoring sheet |
| career ladder (leveling guide) | карьерная лестница (матрица грейдов) | T | |
| level | уровень; грейд | T | «грейд» in pay and leveling contexts |
| promotion | повышение | T | |
| promotion case | заявка на повышение | T | |
| calibration | калибровка | T | |
| "not yet" | «пока нет» | T | the book's term, keep the quotes |
| compensation | вознаграждение; компенсация | T | «вознаграждение» preferred |
| pay range | вилка оплаты | T | |
| performance management | управление результативностью | T | |
| underperformance | низкая результативность | T | |
| performance improvement plan (PIP) | план улучшения результативности (PIP) | B | |
| retention | удержание | T | |
| attrition | текучесть | T | regretted attrition: нежелательная текучесть |
| stay interview | интервью об удержании (stay interview) | B | |
| exit interview | выходное интервью | T | |
| motivation | мотивация | T | |
| psychological safety | психологическая безопасность | T | |
| accountability | подотчётность; ответственность | T | «подотчётность» when answerability is meant |
| ownership | владение; ответственность | T | «команда-владелец» for owning team |
| delegation | делегирование | T | |
| burnout | выгорание | T | |
| succession coverage | покрытие преемниками | T | |
| single point of knowledge failure | единая точка отказа по знаниям | T | |
| truck factor / bus factor | bus factor | E | gloss once: «сколько людей должно выпасть» |
| onboarding | онбординг | T | |

### 3.3 Teams and organization design

| English | Русский | Rule | Note |
|---|---|---|---|
| high-performing team | высокоэффективная команда | T | |
| team charter | хартия команды | T | |
| working agreement | рабочее соглашение | T | |
| knowledge sharing | обмен знаниями | T | |
| decision rights | права на решения | T | |
| decide / consult / consent / delegate | решить единолично / посоветоваться / согласие / делегировать | T | the four methods; keep the order |
| RACI | RACI | E | |
| team health | здоровье команды | T | |
| dysfunction | дисфункция | T | |
| distributed team | распределённая команда | T | |
| organizational design | организационный дизайн | T | |
| span of control | охват управления (span of control) | B | |
| layer | уровень управления | T | |
| dependency mapping | карта зависимостей | T | |
| Conway's law | закон Конвея | T | |
| reverse Conway maneuver | обратный манёвр Конвея | T | |
| Team Topologies | Team Topologies | E | book title; italic |
| stream-aligned team | потоковая команда (stream-aligned) | B | |
| platform team | платформенная команда | T | |
| enabling team | команда содействия (enabling) | B | |
| complicated-subsystem team | команда сложной подсистемы | T | |
| interaction modes | режимы взаимодействия | T | collaboration: сотрудничество; X-as-a-service: X как сервис; facilitation: фасилитация |
| cognitive load | когнитивная нагрузка | T | |
| interrupt sink | «приёмник прерываний» | T | in quotes on first use |
| reorganization (reorg) | реорганизация | T | |
| transition cost | стоимость перехода | T | |
| headcount | численность (штат) | T | "flat headcount": «без роста численности» |
| workforce planning | планирование персонала | T | |
| product group | продуктовая группа | T | |
| cross-functional | кросс-функциональный | T | |
| influence without authority | влияние без формальной власти | T | |

### 3.4 Execution, planning, capacity

| English | Русский | Rule | Note |
|---|---|---|---|
| delivery | поставка | T | «поставка ценности»; not «доставка» |
| execution | исполнение | T | |
| planning | планирование | T | |
| prioritization | приоритизация | T | |
| roadmap | дорожная карта | T | |
| outcome-based roadmap | дорожная карта, ориентированная на результат | T | |
| outcome / output | результат (outcome) / выпуск (output) | B | when the contrast matters |
| discovery | discovery (продуктовое исследование) | B/E | |
| capacity | ресурс команды; ёмкость | T | "capacity allocation": распределение ресурсов; "capacity of 80 engineers": ёмкость 80 инженеров |
| capacity planning | планирование ресурсов | T | |
| FTE | FTE (полная ставка) | B/E | |
| FTE-quarter | FTE-квартал | T | |
| engineer-week / -day / -year | инженеро-неделя / инженеро-день / инженеро-год | T | |
| planned case / cautious case | плановый сценарий / осторожный сценарий | T | |
| unfunded list | список непрофинансированного | T | |
| unplanned work | незапланированная работа | T | |
| prevention allocation | выделение на профилактику | T | "prevention work": профилактическая работа |
| flow | поток | T | |
| lead time | lead time (время выполнения) | B/E | change lead time: время внесения изменений (change lead time) |
| cycle time | время цикла | T | |
| throughput | пропускная способность | T | items per week |
| work in progress (WIP), WIP limit | незавершённая работа (WIP), лимит WIP | B | |
| Little's law | закон Литтла | T | |
| dependency | зависимость | T | |
| forecast / target / commitment | прогноз / цель / обязательство | T | the triad; keep distinct |
| percentile forecast | процентильный прогноз | T | "85th percentile": 85-й процентиль |
| Monte Carlo simulation | моделирование Монте-Карло | T | |
| predictability | предсказуемость | T | |
| uncertainty | неопределённость | T | |
| estimate | оценка | T | |
| backlog | бэклог | T | |
| sprint | спринт | T | |
| milestone | веха | T | |
| renewal commitment | обязательство по продлению | T | Northstar's two commitments |
| cadence | ритм (cadence) | B | not «каденция» |
| management operating system | операционная система управления | T | |
| scorecard | карта показателей (scorecard) | B | |
| OKR | OKR | E | |
| quarterly planning | квартальное планирование | T | |
| bet | ставка | T | funded bet: профинансированная ставка |
| portfolio | портфель | T | |
| horizons (1, 2, 3) | горизонты (1, 2, 3) | T | |

### 3.5 Measurement

| English | Русский | Rule | Note |
|---|---|---|---|
| metric / measure | метрика / показатель | T | |
| productivity | продуктивность | T | |
| DORA metrics | метрики DORA | T | |
| deployment frequency | частота развёртываний | T | |
| change failure rate | доля неудачных изменений (change failure rate) | B | |
| failed deployment recovery time | время восстановления после неудачного развёртывания | T | |
| deployment rework rate | доля развёртываний-переделок | T | |
| SPACE | SPACE | E | |
| developer experience (DevEx) | опыт разработчиков (DevEx) | B | |
| metric gaming | подгонка метрик (gaming) | B | "how it is gamed": как её подгоняют |
| Goodhart's law / Campbell's law | закон Гудхарта / закон Кэмпбелла | T | |
| baseline | исходный уровень; базовый квартал | T | "baseline quarter": базовый квартал |
| leading / lagging indicator | опережающий / запаздывающий индикатор | T | |
| counter-metric (pair) | парная метрика | T | |

### 3.6 Quality, delivery engineering, reliability

| English | Русский | Rule | Note |
|---|---|---|---|
| software quality | качество ПО | T | |
| engineering excellence | инженерное мастерство | T | |
| engineering standard | инженерный стандарт | T | |
| governance | управление; governance | T | "standards governance": управление стандартами; "corporate governance": корпоративное управление |
| paved road | «асфальтированная дорога» (paved road) | B | |
| review board | комитет по ревью | T | |
| tiering, tier 1 | уровни критичности, tier 1 | B/E | «компонент tier 1» |
| operational minimums | операционные минимумы | T | |
| technical debt | технический долг | T | |
| principal / interest (of debt) | основной долг / проценты | T | |
| debt register | реестр долга | T | |
| refactoring | рефакторинг | T | |
| rewrite | переписывание | T | |
| legacy system | унаследованная система (legacy) | B | "legacy modernization": модернизация legacy |
| monolith / modular monolith | монолит / модульный монолит | T | |
| microservices | микросервисы | T | |
| service boundary | граница сервиса | T | |
| platform engineering | платформенная инженерия | T | |
| testing strategy | стратегия тестирования | T | |
| test pyramid | пирамида тестирования | T | |
| regression (pass, test) | регрессия, регрессионное тестирование | T | |
| test case | тест-кейс | T | |
| flaky test | нестабильный тест (flaky) | B | |
| contract test | контрактный тест | T | consumer-driven contracts: контракты, задаваемые потребителем |
| escaped defect | пропущенный дефект (escaped defect) | B | |
| detection point | точка обнаружения | T | |
| code review | код-ревью | T | |
| CI/CD, pipeline | CI/CD, пайплайн | T | |
| deploy vs release | развёртывание и релиз | T | "deploy" = выкатка is too slangy; use развёртывание |
| release train | релизный поезд (release train) | B | |
| feature flag | фича-флаг | T | |
| canary | канареечный релиз | T | |
| progressive delivery | прогрессивная поставка | T | |
| rollback / hotfix | откат / хотфикс | T | |
| release engineering | релиз-инжиниринг | T | |
| reliability | надёжность | T | |
| SLI, SLO, SLA | SLI, SLO, SLA | E | gloss once: индикатор / целевой уровень / соглашение об уровне сервиса |
| error budget | бюджет ошибок (error budget) | B | |
| error budget policy | политика бюджета ошибок | T | |
| burn rate | скорость расходования бюджета (burn rate) | B | |
| availability | доступность | T | |
| downtime | простой | T | |
| observability | наблюдаемость | T | |
| alert, alerting | алерт, алертинг | T | |
| runbook | ранбук (runbook) | B | |
| on-call (rotation) | дежурство (on-call), график дежурств | B | |
| operational readiness | операционная готовность | T | |
| incident | инцидент | T | |
| severity (Sev1, Sev2, Sev3) | серьёзность (Sev1, Sev2, Sev3) | T | Sev labels stay |
| postmortem | постмортем | T | |
| blameless review | безобвинительный разбор (blameless review) | B | |
| root cause / contributing factor | первопричина / сопутствующий фактор | T | |
| corrective action | корректирующее действие | T | |
| recurrence | повторный инцидент | T | |
| prevention point | точка предотвращения | T | |
| customer-detected share | доля инцидентов, обнаруженных клиентами | T | |
| change failure analysis | анализ неудачных изменений | T | |
| quality transformation | трансформация качества | T | |
| constraint (theory of constraints) | ограничение | T | "the constraint": узкое место, when a single bottleneck is meant |
| capability trap | ловушка возможностей | T | |

### 3.7 Security, risk, compliance

| English | Русский | Rule | Note |
|---|---|---|---|
| software supply chain | цепочка поставки ПО | T | |
| NIST CSF, SSDF, SLSA, SBOM | NIST CSF, SSDF, SLSA, SBOM | E | gloss SBOM once: перечень компонентов ПО |
| known-exploited vulnerability (KEV) | активно эксплуатируемая уязвимость (KEV) | B | |
| vulnerability | уязвимость | T | |
| remediation | устранение | T | |
| risk register | реестр рисков | T | |
| risk appetite | риск-аппетит | T | |
| risk treatment (reduce, transfer, avoid, accept) | обработка риска (снизить, передать, избежать, принять) | T | |
| SOC 2 | SOC 2 | E | |
| compliance | соответствие требованиям (compliance) | B | |
| regulation | регулирование | T | |
| due diligence | due diligence (комплексная проверка) | B/E | |

### 3.8 Money, business, strategy

| English | Русский | Rule | Note |
|---|---|---|---|
| business model | бизнес-модель | T | |
| engineering economics | экономика разработки | T | |
| ARR | ARR (годовая регулярная выручка) | B/E | |
| churn | отток | T | |
| revenue | выручка | T | |
| gross margin | валовая маржа | T | |
| service credits | сервисные кредиты (компенсации по SLA) | B | |
| operating expense (opex) | операционные расходы (opex) | B | |
| capital expenditure (capex) | капитальные затраты (capex) | B | |
| capitalized vs expensed software | капитализация ПО и списание на расходы | T | |
| amortization / depreciation | амортизация | T | |
| EBITDA | EBITDA | E | |
| income statement / balance sheet / cash flow statement | отчёт о прибылях и убытках / баланс / отчёт о движении денежных средств | T | |
| budget | бюджет | T | |
| fully loaded cost | полная стоимость сотрудника | T | |
| cost of delay | стоимость задержки (cost of delay) | B | |
| CD3, WSJF | CD3, WSJF | E | |
| opportunity cost / sunk cost | альтернативные издержки / невозвратные затраты | T | |
| net present value (NPV) | чистая приведённая стоимость (NPV) | B | |
| payback period | срок окупаемости | T | |
| discount rate / hurdle rate | ставка дисконтирования / барьерная ставка | T | |
| business case | бизнес-кейс | T | |
| build versus buy | «разработать или купить» (build vs buy) | B | |
| vendor | поставщик; вендор | T | |
| technology strategy | технологическая стратегия | T | |
| engineering strategy | инженерная стратегия | T | |
| investment decision | инвестиционное решение | T | |
| mergers and acquisitions (M&A) | слияния и поглощения (M&A) | B | |
| layoff / reduction in force | увольнение / сокращение штата | T | |
| order-to-cash | order-to-cash («от заказа до оплаты») | B/E | Northstar's domain |
| renewal | продление (контракта) | T | |
| decision log | журнал решений | T | |
| escalation (path) | эскалация (путь эскалации) | T | |
| operational review / operating review | операционный разбор / операционное ревью | T | keep distinct: weekly director meeting vs monthly VP meeting |
| executive reporting / executive update | отчётность для руководства / отчёт для руководства | T | |
| constructive politics | конструктивная политика | T | |
| transformation | трансформация | T | |
| stage gate, exit criteria | контрольная точка (gate), критерии выхода | T | |
| the mandate | мандат | T | Northstar: «мандат CTO» |
| the five constraints | пять ограничений | T | |
| architecture decision record (ADR) | запись архитектурного решения (ADR) | B | |
| playbook | плейбук | T | |
| template | шаблон | T | |

### 3.9 Evidence and research

| English | Русский | Rule | Note |
|---|---|---|---|
| evidence | доказательства; данные | T | "evidence-informed": опирающийся на исследования |
| peer-reviewed | рецензируемый | T | |
| meta-analysis | метаанализ | T | |
| effect size (d, g) | размер эффекта (d, g) | T | |
| validity coefficient | коэффициент валидности | T | |
| correlational | корреляционный | T | "correlation is not causation": корреляция не означает причинности |
| sample | выборка | T | |
| self-reported | самоотчётный | T | |
| vendor-sponsored | спонсируемый вендором | T | |

## 4. Fixed renderings

### 4.1 The 16 chapter sections (H2, in order)

| English | Русский |
|---|---|
| Why This Matters | Почему это важно |
| Learning Objectives | Цели главы |
| The Mental Model | Ментальная модель |
| Deep Conceptual Explanation | Подробный разбор |
| Engineering Organization Example | Пример из инженерной организации |
| Decision Framework | Как принимать решение |
| Trade-offs | Компромиссы |
| Failure Modes | Типичные провалы |
| Enterprise Application | Применение в крупной организации |
| CTO Perspective | Взгляд CTO |
| Practical Playbook | Практический плейбук |
| Case Study | Кейс |
| Exercises | Упражнения |
| Reflection Questions | Вопросы для размышления |
| Key Takeaways | Главное |
| References and Further Reading | Источники и что почитать |

The mental-model blockquote opens with `> **Ментальная модель:** …`. Chapter H1: `# Глава N — <title>`
with the title exactly as in the `ru` nav translation. Learning objectives keep the capability form:
infinitive verbs («Диагностировать…», «Построить…»).

### 4.2 Exercise levels and numbering

| English | Русский |
|---|---|
| Foundational | Базовый уровень |
| Applied Leadership | Прикладное лидерство |
| Executive Decision-Making | Решения на уровне руководства |

Exercise numbers stay Latin and bold: `**F1.**`, `**A1.**`, `**X1.**`. Solutions headings keep the id:
`## F1 — <краткое название>`, anchors `{ #f1-<english-slug> }` copied from the English solutions page.

### 4.3 Evidence labels

| English | Русский |
|---|---|
| Research finding | Научный результат |
| Industry research | Отраслевое исследование |
| Standard | Стандарт |
| Documented practice | Задокументированная практика |
| Practitioner consensus | Консенсус практиков |
| Expert opinion | Мнение эксперта |
| This book's recommendation | Рекомендация книги |
| Illustrative | Иллюстрация |

Access levels in the bibliography: full text read → прочитан полный текст; abstract or landing page only
→ только аннотация или страница источника; official summary read → прочитано официальное резюме;
bibliographic metadata only → только библиографические данные.

### 4.4 Admonition titles

| English | Русский |
|---|---|
| Northstar so far | Northstar: что уже известно |
| Fictional | Вымысел |
| Related chapters | Связанные главы |
| Terms used in this chapter | Термины этой главы |
| How to use these pages | Как пользоваться этими страницами |
| What you need to know for this case | Что нужно знать для этого кейса |
| Northstar in one paragraph | Northstar в одном абзаце |
| Similar names | Похожие имена |
| Not legal advice | Не юридическая консультация |
| How … is estimated / calculated | Как получена оценка … / Как рассчитано … |

### 4.5 Fixed labels used across pages

| English | Русский |
|---|---|
| Taught in | Подробно: |
| Described on | Описано на странице |
| Unit: | Единица: |
| Week N | неделя N |
| Day 90 | День 90 |
| Quarter N (as a label) | Квартал N |
| Year 2 | Год 2 |
| Path A … H | Маршрут A … H |
| Part I … XV | Часть I … XV |

### 3.x Added in readability round 2 (2026-11-23)

| English | Русский | Rule | Note |
|---|---|---|---|
| the year in brief | «Год вкратце» | T | page title |
| the year 1 record | хроника года 1 | T | the page `first-quarter.md` |
| budget envelope | рамки бюджета | T | |
| operating plan | операционный план | T | |
| board pack | пакет для совета директоров | T | |
| run-rate | годовой темп (run-rate) | B | |
| seat | место | T | 87 seats = 80 engineers, 6 managers, the director |
| requisition | заявка на найм | T | |
| vesting | вестинг | T | |
| value channel; urgency profile | канал ценности; профиль срочности | T | |
| quality engineer | инженер по качеству | T | |
| re-rating; severity audit | переоценка серьёзности; аудит серьёзности | T | |
| dependency link | связь зависимости | T | |
| stock and flow | запас и поток | T | |
| reinforcing / balancing loop | усиливающая / балансирующая петля | T | |
| leverage point | точка рычага | T | |
| estate | технологический ландшафт | T | |
| incident review | разбор инцидента | T | main term; postmortem is the alternative |
| deployable unit | развёртываемая единица | T | |
| Your team; Engineering system; Organization and operating system; Executive | Ваша команда; Инженерная система; Организация и операционная система; Высшее руководство | T | template nav groups |

### 3.y Renderings adopted in chapter translation wave 1 (chapters 1–18)

The translators of chapters 1–18 chose renderings for about 160 terms missing from this base. They are
listed, with their English source terms, in `research/translation-ru/notes-t1.md`, `notes-t2.md`, and
`notes-t3.md`, and are **binding** for later translators exactly as if they stood in this table (read all
three before translating). Decisions taken by the maintainer: cities in Cyrillic (Богота, Миннеаполис);
"bus factor" kept in English, with "truck factor" named once where the English uses it; extra evidence
labels "this book's synthesis" → «синтез книги», "this book's illustration" → «иллюстрация книги»,
"contested" → «вопрос спорный».

## 5. Sync debt

Record here any Russian page that lags its English source, with the English commit it was translated
from. The Russian pages translated in the first pass (front matter, glossary, evidence labels, the
Northstar case) were translated from the working tree of 2026-11-23.

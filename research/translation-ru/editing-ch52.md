# Literary editing notes: chapter 52

File: `docs/parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.ru.md`.
Edited from the Russian text only; the English chapter was not opened. Pre-edit text:
`git show ru-wip:<file>`.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `ru-wip` (NBSP
normalised); link targets, citation link texts, `{ #anchors }`, heading count, exercise labels, admonition
lines, every table line (including the indented tables inside the collapsible `??? note`, whose body stays
indented under its title line) and all three Mermaid blocks are byte-identical. No wrapped line starts
with a number and a period. About 75 sentence-level edits. NBSP 168 → 138: some thirty NBSPs that glued
an amount or label to the following preposition («$185 000⍽на», «$410 000⍽до», «TR-01⍽профинансированным»,
«FY1⍽для», «2025-06⍽о», «BC13⍽об») were moved or dropped (section 2a.8). Failure-mode fields: «Признак:»
(one entry) and «Как заметить:», unchanged. Accounting terms follow notes-t20 and first-quarter.ru;
«повышение по результатам (merit increase)» as instructed.

Section 2a patterns appeared as expected. Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Report lines that "show" an amount

English "shows $185,000 of expense" came through as «показывает … расходов», which in Russian implies a
display, not an accounting effect.

- «Инженеро-год профилактики показывает в этом году $185 000 расходов» → «…даёт в этом году $185 000
  расходов»
- «Полностью капитализированный инженеро-год работы над функцией показывает только накладные расходы» →
  «…даёт только накладные расходы»

### 1.2 Sentences that open with an amount

- «$410 000 базового квартала соответствовали годовому темпу $1,64 млн; $60 000 квартала 3 дают годовой
  темп $240 000.» → «В базовом квартале кредиты составили $410 000, что соответствует годовому темпу
  $1,64 млн; в квартале 3 — $60 000, или $240 000 в годовом темпе.»

### 1.3 Evidence label glued to a possessive ("its known problems are practitioner consensus")

- «Его известные проблемы — **консенсус практиков**: …» → «У бюджетов есть известные проблемы
  (**консенсус практиков**): …» The label keeps its function; the sentence no longer says the problems
  *are* a consensus.

### 1.4 Two-part definition packed into «из-за X, когда…, и из-за Y, когда…»

- «Прогнозы ошибаются из-за оптимистического искажения (optimism bias), когда будущее оценивают
  благосклоннее…, и из-за стратегического искажения данных…, когда затраты занижают…» → «Прогнозы
  ошибаются по двум причинам. Первая — оптимистическое искажение (optimism bias): … Вторая —
  стратегическое искажение данных (…): …»

### 1.5 "Three things." followed by verbless fragments

- «**Что Victor несёт Rajiv.** Три вещи. Сверку $20,3 млн… Строку кредитов… И предупреждение…» → «**С чем
  Victor идёт к Rajiv.** С тремя вещами. Первая — сверка… Вторая — строка кредитов… Третья —
  предупреждение…» («несёт» with accusative fragments read as a calque of "brings".)

### 1.6 Calque «двигает» kept where it is the working word

«Капитализация двигает EBITDA, а не деньги» was left: finance people say it, and the table makes it
concrete. «Рычаг сильнее всего, пока…» (no subject for the lever) → «Влиять на рамки проще всего, пока…».

## 2. Two showcase paragraphs

### 2.1 What the credits bought

**Before.** **Что дали кредиты.** Сервисные кредиты вычитаются из выручки, поэтому каждый доллар кредитов
— это доллар операционной прибыли. $410 000 базового квартала соответствовали годовому темпу $1,64 млн;
$60 000 квартала 3 дают годовой темп $240 000. Разница, около $1,4 млн в год, — это 6,7% операционной
прибыли FY1, и численность при этом не росла. Так выглядит программа качества года 1 в ракурсе CFO.

**After.** **Что дали кредиты.** Сервисные кредиты вычитаются из выручки, поэтому каждый доллар кредитов
— это доллар операционной прибыли. В базовом квартале кредиты составили $410 000, что соответствует
годовому темпу $1,64 млн; в квартале 3 — $60 000, или $240 000 в годовом темпе. Разница, около $1,4 млн в
год, — это 6,7% операционной прибыли FY1, и численность при этом не росла. Так выглядит программа
качества года 1 в ракурсе CFO.

### 2.2 Trade-offs: capitalizing or expensing

**Before.** **Капитализация или списание на расходы.** Капитализация повышает EBITDA, что ценят некоторые
инвесторы и кредиторы, но ценой учёта времени, внимания аудиторов, «хвоста» амортизации и риска
обесценения. Списывать на расходы всё проще, но тогда инвестиции в продукт выглядят меньше, чем есть.
Выбор за финансами; CTO обязан дать точные данные.

**After.** **Капитализация или списание на расходы.** Капитализация повышает EBITDA, и некоторые
инвесторы и кредиторы это ценят. Платить за это приходится учётом времени, вниманием аудиторов,
«хвостом» амортизации и риском обесценения. Списывать всё на расходы проще, но тогда инвестиции в продукт
выглядят меньше, чем есть. Выбор за финансами; CTO обязан дать точные данные.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| списать стоимость вниз (write down) | «снизить балансовую стоимость» | «списать вниз» is a calque; standard Russian accounting says «снижение (уменьшение) балансовой стоимости». Kept in this edit for term-base consistency |
| повышение по результатам (merit increase) | keep; unify first-quarter.ru «по заслугам» to it | instructed |
| два разреза (functional / booking) | keep | «разрез» is the natural Russian budgeting word |
| ракурс (lens) | keep | reads well; «линза» would be a calque |
| ДДС in the Mermaid labels | keep | standard Russian abbreviation for «движение денежных средств»; the table under the diagram names the full report |
| Две защиты (two safeguards) | «две страховки» | used here; «защита» collides with «защищать бюджет» in the same chapter |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Opening:** «из всех руководителей он часто хуже всех умеет читать, где эти деньги отражаются»
   rendered «часто хуже других руководителей понимает, где эти деньги отражаются в отчётности». Check
   that "least able of all executives" is not meant literally as a superlative.
2. **Case, TR-01:** «фреймворке, который на мажорную версию отстал от бесплатной поддержки сообщества»
   rendered «на одну мажорную версию отстал от версий с бесплатной поддержкой сообщества». Assumes "one
   major version behind free community support".
3. **«Бюджетом разработки, как ожидается, владеет CTO»** rendered «Владеть бюджетом разработки, как
   ожидается, должен CTO». Assumes "the CTO is expected to own".
4. **A2: «начальная работа при собственной разработке капитализируется, а интеграции — нет»** rendered
   «…а интеграция — нет» (integration work of the buy and hybrid options). Check the English is not
   "integrations" in another sense.
5. **Enterprise, transition cost:** «Переход занимает квартал и стоит доброй воли инженеров, если учёт
   времени появится без объяснения» split into two sentences; the cost is conditional on the missing
   explanation in both versions.
6. **Mental model, second consequence:** «Глава 45 решает, стоит ли инвестиция своего ресурса» rendered
   «отвечает, стоит ли инвестиция того ресурса, который на неё уйдёт». Same claim.

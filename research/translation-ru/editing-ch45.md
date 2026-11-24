# Literary editing notes: chapter 45

File: `docs/parts/10-business-leadership/45-business-models-and-engineering-economics.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes (apart from the stale `dist/` single file, expected); the sorted list of
numeric tokens is identical before and after (334 tokens, NBSP and line wraps normalised); headings,
`{ #anchors }`, link targets, citation link texts, exercise labels, admonition lines, every table line and
both Mermaid blocks are identical. NBSP count unchanged (105). About 85 paragraph-level edits.
Failure-mode fields were already «Как заметить:» / «Что делать:».

Section 2a patterns appeared as expected (missing connectives, English word order, «который» chains). Only
new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «стоить» in a money chapter: "costs" and "is worth" collide

In a chapter about value and cost, «стоит больше / меньше» reads as either. Where "worth" is meant, use
«ценнее», «ценность», «менее ценным».

- «портфель… одобряет всё, что стоит больше своего фонда оплаты труда, и никогда не спрашивает, не стоило
  ли что-то другое ещё больше» → «портфель будет одобрять всё, что ценнее собственного фонда оплаты труда,
  и ни разу не спросит, не было ли что-то другое ещё ценнее»
- «если B сработает, C будет стоить меньше» → «если B сработает, C станет менее ценным»

### 1.2 Decision rules translated as if the metric acts

- «Чистая приведённая стоимость… принимает положительные значения и отвергает отрицательные» → «Чистая
  приведённая стоимость… даёт простое правило: положительные значения принимают, отрицательные отвергают»
- «Диаграмма — правило маршрутизации» → «Диаграмма показывает, куда направить вопрос»

### 1.3 Ambiguous pronoun after a list of goods

- «их стоимость задержки снизится ещё больше» (credits or statements?) → «стоимость задержки выписок
  снизится ещё больше»
- «два проекта претендуют на одни и те же кредиты» → «два проекта записывают себе в выгоду одни и те же
  кредиты»

### 1.4 Doubled comparatives and a sentence opening with a figure

- «больше чем в десять раз больше этой разницы» → «в десять с лишним раз больше этой разницы»
- «$157 250 за капитализированный FTE-год — это…» (sentence starts with a number) → «Ещё одно число,
  $157 250 за капитализированный FTE-год, — это…»

### 1.5 Mechanical: wrapped citation link text

After re-wrapping, `[Arnold and Yüce,\n2013](…)` splits are legal Markdown but ugly in source and diff. A
small script moved every such break before the opening bracket (11 in this chapter).

## 2. Two showcase paragraphs

### 2.1 Mental model, after the diagram

**Before.** О четырёх видах работы обычно спорят на четырёх разных языках, но приводят они в одно место.
Каждая стрелка — гипотеза с размером и вероятностью; задача директора — сделать их явными и сопоставимыми.
Отсюда два следствия. **Время — это затраты**: функция, которая приносит $10 000 в неделю и выходит на
десять недель позже, потеряла около $100 000. И **цена инженерной работы — то, что она вытесняет**, а не
зарплаты: при фиксированной численности зарплаты платят, что бы вы ни выбрали.

**After.** О четырёх видах работы спорят обычно на четырёх разных языках, но ведут все они в одну точку.
Каждая стрелка — гипотеза, у которой есть размер и вероятность; задача директора — сделать эти гипотезы
явными и сопоставимыми. Отсюда два следствия. Первое: **время — это затраты**. Функция, которая приносит
$10 000 в неделю, но выходит на десять недель позже, теряет около $100 000. Второе: **цена инженерной
работы — то, что она вытесняет**, а не зарплаты. При фиксированной численности зарплаты платят, что бы вы
ни выбрали.

### 2.2 Case: what really moves the answer

**Before.** …Изменение вероятности выигрыша на 5 пунктов стоит около 0,05 × $504 000 = $25 200 маржи в
год — больше чем в десять раз больше этой разницы. Глава 42 показала, что клиенту нужны были надёжная дата
и свидетельства того, что Northstar понимает его процесс согласования, а не ПО к неделе 36. […] А
ценность выписок зависела от того, будут ли кредиты выплачиваться и дальше, — именно это условие поднял
Rajiv: если кредиты останутся на уровне квартала 2, $95 000 в квартал, или ниже, их стоимость задержки
снизится ещё больше.

**After.** …Изменение вероятности выигрыша на 5 пунктов стоит около 0,05 × $504 000 = $25 200 маржи в
год — в десять с лишним раз больше этой разницы. Глава 42 показала: к неделе 36 клиенту нужно было не ПО,
а надёжная дата и свидетельства того, что Northstar понимает его процесс согласования. […] А ценность
выписок зависела от того, будут ли кредиты выплачиваться и дальше; именно на это условие указал Rajiv.
Если кредиты останутся на уровне квартала 2 ($95 000 в квартал) или опустятся ниже, стоимость задержки
выписок снизится ещё больше.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| соглашение (a valuation convention agreed with finance) | «условность» | «соглашение» collides with the negotiation sense in ch 46; applied once |
| правильность, а не точность | keep | the pair works once explained by context |
| квота для сделок | keep | clear in X1 |
| «стоит больше / меньше» for "worth" | prefer «ценнее», «менее ценен» in chapters 45, 52 | see 1.1 |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Case: «У форума недели 34 было три варианта», option 2 «поставить в слот недели 33».** A forum held in
   week 34 cannot fill a week-33 slot. Either the forum is earlier or the slot label differs in the English.
2. **NPV paragraph: «принимает положительные значения и отвергает отрицательные»** rendered as a decision
   rule («положительные значения принимают, отрицательные отвергают»); assumes "NPV accepts positive and
   rejects negative projects".
3. **Opening: «Каждая инженерная неделя тратится на одно вместо другого»** rendered «…потраченная на одно,
   отнята у другого»; same claim, check nothing more specific was meant.
4. **Two safeguards: «пересматривают через квартал-два и сообщают расхождение»** kept as revisiting and
   reporting the gap; assumes the gap is estimate versus outcome.
5. **Enterprise: «Переход занимает квартал… и второй…»** rendered «Переход занимает два квартала: первый…
   второй…»; same arithmetic.

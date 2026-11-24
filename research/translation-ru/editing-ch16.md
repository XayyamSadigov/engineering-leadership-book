# Literary editing notes: chapter 16

File: `docs/parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.ru.md`. Edited from the
Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes. Sorted number tokens and digit atoms are identical to
`git show HEAD:<file>` (249 / 250). Link texts and targets (34), `{ #anchors }` (27), exercise labels,
the admonition, all three Mermaid blocks (labels untouched), table shapes and every number in tables are
identical. One table cell fixed for gender agreement («команда, способная её принять» → «его», the
antecedent is «владение»). Failure-mode fields relabelled «Признак:» / «Противоядие:» → «Как заметить:» /
«Что делать:»; the failure mode «Ком незапланированной работы» renamed «Незапланированная работа одним
числом» («ком» does not carry "lump" in Russian). «ранбук» glossed once as «ранбук (runbook)» per the
term base. NBSP fixes: «главе 23⍽применяет», «квартале 1⍽была», «главы 33⍽и 34» and similar moved to the
label side; «в обещанном квартале 7 из 17» rebuilt so the number no longer looks like a quarter label.

## 1. Patterns new beyond section 2a

### 1.1 «не разрешает компромиссы» and other false friends of "resolve / own"

- «закон не разрешает компромиссы» (reads as "does not permit") → «закон не снимает компромиссов»
- «CTO владеет структурой… CTO владеет политикой срочных запросов» → «на CTO лежит структура…», «за CTO
  политика срочных запросов»
- «очередь, которой никто не владеет и которую никто не измеряет» → «очередь без владельца, которую
  никто не измеряет»

### 1.2 Gerund-subject conditionals («Ускорение X не сдвигает Y»)

Same family as ch08 1.5, frequent in a chapter full of causal claims.

- «Ускорение этих трёх дней почти не сдвигает два месяца.» → «Если ускорить эти три дня, два месяца почти
  не сдвинутся.»
- «улучшение шага, который не является узким местом, не сокращает весь путь» → «если ускорить любой
  шаг, кроме узкого места, весь путь не сократится»
- «Ограничение незавершённой работы 27 задачами и роение… сдвинули бы среднее к 3 неделям» → «Если
  ограничить незавершённую работу 27 задачами, а вокруг заблокированных задач устроить роение…, среднее
  сдвинется к 3 неделям»

### 1.3 Abstract nouns as agents of a rule («Три оговорки сохраняют закон честным»)

- «Три оговорки сохраняют закон честным:» → «Чтобы применять закон честно, помните три оговорки:»
- «Если их не учитывать, проще всего получить впечатление, что закон неверен» → «Если их пропустить,
  проще всего прийти к выводу, будто закон неверен»

### 1.4 Doubled hedges in one sentence

- «lead time упал бы с 76 примерно до 71 дня, то есть примерно на 6 процентов» → «сократился бы с 76
  примерно до 71 дня — это около 6 процентов»

### 1.5 «директор» colliding with the protagonist

In X2 «Один директор предлагает…, другой — …» refers to board members, but in this book «директор» is the
Northstar director. Rendered «Один член совета предлагает…» (see meaning doubt 1).

### 1.6 Stacked genitives with «из … из»

- «двумя парами команд из матрицы зависимостей из кейса» → «…из матрицы зависимостей, приведённой в
  кейсе»
- References: «Мышление в терминах ограничений в форме романа» → «Теория ограничений в форме романа»

## 2. Two showcase paragraphs

### 2.1 Interrupt rotation

**Before.** Они доделывают то, что можно сделать за день, а остальное превращают в тикеты, ранжируемые
вместе со всем прочим, так что роль — это сортировка, а не второй бэклог. Плановую работу им не передают
только потому, что они выглядят свободными. Две привычки не дают роли превратиться в свалку: в тихую
неделю человек улучшает ранбук или автоматизирует самый частый запрос, а команда ежемесячно разбирает
журнал запросов, чтобы найти, что следующим должно убрать самообслуживание.

**After.** То, что можно сделать за день, они доделывают, а остальное превращают в тикеты, которые
ранжируются вместе со всем прочим: роль — это сортировка, а не второй бэклог. Плановую работу им не
передают только потому, что они выглядят свободными. Две привычки не дают роли превратиться в свалку. В
тихую неделю дежурный улучшает ранбук (runbook) или автоматизирует самый частый запрос. А команда раз в
месяц разбирает журнал запросов, чтобы найти, что следующим перевести на самообслуживание.

### 2.2 CTO perspective

**Before.** На этом уровне меняются три вещи. CTO владеет структурой, которая порождает зависимости: …
и только CTO может разменивать их в масштабе всей организации. CTO владеет политикой срочных запросов,
потому что большинство срочных запросов приходит от руководства компании; принимая каждую срочную
просьбу от продаж и CEO, он задаёт долю незапланированной работы организации. И CTO решает, где живёт
запас.

**After.** На этом уровне меняются три вещи. Во-первых, на CTO лежит структура, которая порождает
зависимости: … и только CTO может взвешивать их друг против друга в масштабе всей организации.
Во-вторых, за CTO политика срочных запросов, потому что большинство срочных запросов приходит от
руководства компании: принимая каждую срочную просьбу от продаж и CEO, CTO сам задаёт долю
незапланированной работы в организации. В-третьих, CTO решает, где держать запас.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| роение (swarming) | keep, but as a noun only | the verb «роиться» reads comic; rebuilt as «устроить роение» |
| приёмник прерываний | keep | consistent with the term base; reads fine in quotes |
| правило «перестаньте начинать» | consider «сначала заканчивайте, потом начинайте» | closer to the Kanban slogan Russian practitioners know ("stop starting, start finishing"); kept for consistency |
| самообслуживаемое (окружение) | keep | understood; «окружение с самообслуживанием» is the fallback |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **X2.** «Один директор предлагает…, другой — …» rendered «Один член совета предлагает…». If the English
   means two company directors rather than board members, revert to «один из директоров».
2. **Little, caveat 2.** «закон не разрешает компромиссы» rendered «не снимает компромиссов». If the
   English says the law "does not resolve trade-offs", this is right; if it says something narrower (for
   example "does not tell you which variable to change"), a closer wording is needed.
3. **Case.** «ещё два доказательства» kept; the two items are a dependency count and an unplanned-work
   breakdown, so «ещё два набора данных» may be closer to "evidence" here.
4. **Why this matters, first line.** «история застряла» rendered «задача застряла»; if the English is
   "story" in the user-story sense, the change is harmless, but note it.
5. **Example.** «Измеряйте пропускную способность четыре недели до и после» rendered «четыре недели до
   изменения и после»; check that "after" is also four weeks.

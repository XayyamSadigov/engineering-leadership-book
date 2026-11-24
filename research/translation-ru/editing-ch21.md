# Literary editing notes: chapter 21

File: `docs/parts/05-engineering-quality/21-technical-debt.ru.md`. Edited from the Russian text only; the
English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to the pre-edit copy (216
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition types, Mermaid blocks and
every number in tables are identical. One table word changed: «Не известен» → «Неизвестен» (spelling; twice,
TD-006 and TD-007 rows). Two NBSPs removed from the wrong side of an id («Sev2,⍽две», «TD-005,⍽формат»).
About 70 sentence-level edits; paragraphs that grew past the line width were re-wrapped.

Overall: the translation was accurate and already clean in vocabulary. The section 2a patterns appeared
(missing connectives, English word order, «который» chains, a list signposted only by «Три наблюдения»).
Only patterns new beyond section 2a follow.

## 1. Patterns new beyond section 2a

### 1.1 Three relative clauses stacked on one noun

English "A tangled module that nobody changes, that rarely fails, and that no planned feature needs is
ugly…" came through with three «который». Turn the description into its own sentence.

- «Запутанный модуль, который никто не меняет, который редко падает и который не нужен ни одной
  запланированной функции, уродлив, но почти ничего не стоит.» → «Возьмём запутанный модуль: его никто не
  меняет, он редко падает и не нужен ни одной запланированной функции. Он уродлив, но почти ничего не
  стоит.»
- «Термин появился в отчёте об опыте, который Ward Cunningham представил на OOPSLA в 1992 году, о
  портфельной системе WyCash.» (the «о…» complement is torn from «отчёте») → «Термин появился в 1992 году в
  отчёте об опыте, который Ward Cunningham представил на OOPSLA; речь в нём шла о портфельной системе
  WyCash.»

### 1.2 Mid-sentence parenthetical caveat that carries a whole argument

- «Этот **научный результат** получен в наблюдательном исследовании (возможно, более трудные задачи
  порождают худший код и занимают больше времени), а «качество» здесь — метрика…» → «Это **научный
  результат** наблюдательного исследования: возможно, более трудные задачи сами порождают худший код и
  занимают больше времени. К тому же «качество» здесь — метрика…»
- «Двадцать лет спустя, как сказано в аннотации вступительной статьи к специальному выпуску IEEE
  Software, метафору ввели, чтобы…» (the inserted source makes "twenty years later" attach to the wrong
  event) → «Двадцать лет спустя вышел специальный выпуск IEEE Software, и в аннотации вступительной статьи
  к нему сказано: метафору ввели, чтобы…»

### 1.3 Russian negation word order broken by the English skeleton

- «список растёт, а закрывается почти ничего» → «список растёт, а почти ничего не закрывается»
- «Директор не отклонил предложение.» (reads as a bare report) → «Отклонять предложение директор не
  стал.» (the «не стал» form carries the deliberate choice)

### 1.4 English "If X, it is not Y: it is Z" with a doubled «это»

- «Если основной долг почти нулевой, это не проект: это решение, которое кто-то откладывает.» →
  «Когда основной долг почти нулевой, перед вами не проект, а решение, которое кто-то откладывает.»
- «основной долг — около одного дня, а именно решение о владении» → «основной долг — около одного дня:
  нужно лишь решить, кто владелец»

### 1.5 Calqued nouns where a verb or a plain word works

- «Докладывайте о процентах, а не об инвентаре.» → «…а не о длине списка.»
- «Sev1 — это лежащий путь заказа или оплаты» (slang) → «Sev1 — это остановка пути заказа или оплаты»
- «Популярная операционная форма — WSJF» → «Популярный способ применять её на практике — WSJF»
- «Это означает выплатить весь основной долг сразу» → «То есть выплатить весь основной долг разом»

### 1.6 Three mechanisms announced, then given as unmarked sentences

- «Три механизма помогают доле пережить давление. Она стоит отдельной строкой… О её расходовании…
  А заём из неё…» → «Пережить давление доле помогают три механизма. Первый: … Второй: … Третий: …»

### 1.7 Mechanical: re-wrapping can strand a label number inside link text

After re-wrapping, check that no line ends in «года», «главы», «недели» with the number on the next line;
inside link text use an NBSP («хроники года⍽1»). Found once in chapter 22, none here.

## 2. Two showcase paragraphs

### 2.1 Mental model, first consequence

**Before.** Во-первых, **уродливость — ещё не цена**. Запутанный модуль, который никто не меняет, который
редко падает и который не нужен ни одной запланированной функции, уродлив, но почти ничего не стоит.
Мелкая несогласованность в скрипте миграции, которая даёт о себе знать в каждом втором релизе, выглядит
безобидно, а обходится дорого. Ранжируя по тому, насколько плохо выглядит код, вы ранжируете по основному
долгу, то есть по наименее важному числу.

**After.** Во-первых, **уродливость — ещё не цена**. Возьмём запутанный модуль: его никто не меняет, он
редко падает и не нужен ни одной запланированной функции. Он уродлив, но почти ничего не стоит. А мелкая
несогласованность в скрипте миграции, которая даёт о себе знать в каждом втором релизе, выглядит
безобидно, но обходится дорого. Ранжируя по тому, насколько плохо выглядит код, вы ранжируете по
основному долгу, то есть по наименее важному числу.

### 2.2 Case, what went wrong

**Before.** Что пошло не так: во второй месяц команда Customer Experience потратила всю свою долю на
обновление фронтенд-фреймворка, которого не было в реестре и проценты по которому никто не мог назвать.
Директор оставил это как есть и попросил, чтобы в следующем квартале работа по обновлению сначала попала в
реестр. Так и вышло.

**After.** Что пошло не так. Во второй месяц команда Customer Experience потратила всю долю на обновление
фронтенд-фреймворка. Этого обновления не было в реестре, и назвать проценты по нему никто не мог. Директор
не стал ничего отменять, но попросил, чтобы в следующем квартале работа по обновлению сначала попала в
реестр. Так и сделали.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| проценты временем / проценты риском | keep; allow «проценты в виде времени / риска» in running prose | the instrumental reads oddly in oblique cases («у процентов временем») |
| срезанный угол; срезать угол | keep; allow «упрощение, принятое ради скорости» once where the idiom is unclear | «срезать угол» is understood, but its "shortcut in quality" sense is weaker in Russian than in English |
| верх реестра / верхние записи | keep | colloquial but clear; «верхняя часть реестра» used where a fuller form reads better |
| отношение (interest/principal) | keep | works once defined; do not switch to «коэффициент» |
| Не известен (table) | «Неизвестен» | short adjective without contrast is written as one word |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Four options, "cheapest effective first".** «У каждой записи четыре варианта, от самого дешёвого
   действенного» was rendered «и предпочтение отдают самому дешёвому из действенных», which matches the Key
   Takeaways («сначала пробуйте самый дешёвый действенный вариант»). But the list that follows starts with
   "remove", the most expensive. If the English means the list is ordered, the list order or the wording is off.
2. **"Interest has two parts", then "a third part".** The section announces two parts of interest and then
   adds option cost as «третья часть». Probably in the English too; worth a look.
3. **IEEE Software abstract.** Rebuilt as "twenty years later a special issue appeared; its introduction's
   abstract says the metaphor was introduced to explain refactoring to non-technical stakeholders". Check
   that "twenty years later" refers to the special issue, not to the introduction of the metaphor.
4. **Case, Customer Experience.** «Директор оставил это как есть» → «не стал ничего отменять». Assumes the
   English means the director let the spending stand.
5. **Case, end of quarter.** «изменения… проходили ревью дольше сопоставимых, но модуль затронули всего
   около 30 изменений» → «…выяснилось, что изменения в core/customer проходят ревью дольше сопоставимых, но
   таких изменений было всего около 30». Same facts; check that 30 is the count of changes touching the module.
6. **«Исходные данные Northstar взяты из…»** (was «Цифры Northstar»): meant to separate the Northstar
   baseline inputs from the illustrative estimates. If the English says all Northstar figures come from the
   baseline, the old wording was closer.
7. **References, Kruchten** still says «прочитана только аннотация» (access note in reader text, already
   flagged in notes-t5). Not changed.

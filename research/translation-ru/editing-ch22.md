# Literary editing notes: chapter 22

File: `docs/parts/05-engineering-quality/22-testing-strategy-and-test-architecture.ru.md`. Edited from the
Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to the pre-edit copy (253
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition types, Mermaid blocks and
every table line are identical. One NBSP removed from after an id («INC-427,⍽когда»); NBSPs added between
numbers and counted nouns in edited sentences. About 65 sentence-level edits; paragraphs that grew past
the line width were re-wrapped (one stranded «года / 1» inside link text fixed).

Overall: accurate and readable; the main problems were syntactic. Section 2a patterns appeared (book or
study as grammatical subject, missing connectives, English word order). New patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Dangling adverbial participle (деепричастие with the wrong subject)

- F1: «Опираясь на классификацию пропусков Northstar и инвентаризацию тестов…, один из руководителей
  доказывает, что…» (it is the reader who should rely on the data, not the manager) → «Один из
  руководителей доказывает, что… Ответьте ему данными, опираясь на классификацию пропусков…»

Grep chapters for sentences that open with «Опираясь», «Используя», «Пользуясь» and check the subject.

### 1.2 Verbless noun list after a colon, copied from an English fragment

- «Интеграционный слой велик, но не спроектирован: около 38 из 74 минут пайплайна, большая часть
  нестабильных падений в выборке директора и ни одной контрактной проверки…» → «Интеграционный слой велик,
  но никто его не проектировал: на него приходятся около 38 из 74 минут пайплайна и большая часть
  нестабильных падений в выборке директора, а контрактных проверок нет ни одной…»
- «Переносимый урок касается охвата: изменённые строки в модулях высокого риска, результаты — ревьюерам и
  никаких целей по показателю…» → «Урок, который можно перенести, касается охвата: мутировать изменённые
  строки в модулях высокого риска, показывать результаты ревьюерам и не ставить целей по показателю…»
- «Это доказывает практичность, а не снижение числа дефектов.» → «Это доказывает, что подход практичен,
  но не что он снижает число дефектов.»

### 1.3 Participial phrase between a coined name and its author

- «**Кубок тестирования** (testing trophy) Kent C. Dodds, придуманный для фронтенд-кода, делает самой
  широкой полосой интеграционные тесты и сводит выбор к…» → «**Кубок тестирования** (testing trophy) Kent
  C. Dodds придумал для фронтенд-кода. Самая широкая полоса в нём — интеграционные тесты, а выбор сводится
  к…»
- «Рабочая группа по релизам, которую возглавлял Kwame, с владельцами из команд, на неделе 4 отправила…» →
  «Рабочая группа по релизам во главе с Kwame, куда входили владельцы из команд, на неделе 4 отправила…»

### 1.4 "Shapes", "on volume" and other verbs carried over literally

- «Проверка, которая за минуты проходит на каждом изменении, формирует работу каждого инженера.» →
  «…определяет, как работает каждый инженер.»
- «проявляются только на объёме» → «проявляются только при больших объёмах»
- «Больше всего ручного труда охраняет сквозные сценарии» (labour as subject that guards) → «Больше всего
  ручного труда уходит на охрану сквозных сценариев»
- «Каждый инженер следит за тем, как обходятся с QA-инженерами во время автоматизации.» → «Как обходятся с
  QA-инженерами во время автоматизации, видит каждый инженер.» (theme first; «следит» suggested a duty)

### 1.5 Ambiguous comparative «лучшие» (best / better)

- «Лучшие проверки меняют профиль пропусков, а значит, и следующее вложение» → «Когда проверки становятся
  лучше, меняется профиль пропусков, а с ним и следующее вложение»

### 1.6 Mixed government in one sentence («с помощью X…, а не Y-ом»)

- «Выполняйте требования к доказательствам с помощью автоматических записей… а не ручной контрольной
  точкой» → «Требования к доказательствам закрывайте автоматическими записями… а не ручной контрольной
  точкой»

### 1.7 Term drift inside a chapter

- «Повторные запуски и правило…» next to «перезапуски» everywhere else (notes-t5 fixes «перезапуски») →
  «Перезапуски и правило…»

## 2. Two showcase paragraphs

### 2.1 Example, reading the table

**Before.** Больше всего ручного труда охраняет сквозные сценарии (19 процентов пропусков), а у миграций и
конфигурации (18 процентов) нет ни одной автоматической проверки. Интеграционный слой велик, но не
спроектирован: около 38 из 74 минут пайплайна, большая часть нестабильных падений в выборке директора и ни
одной контрактной проверки, хотя на границы приходится 23 процента пропусков.

**After.** Больше всего ручного труда уходит на охрану сквозных сценариев (19 процентов пропусков), а у
миграций и конфигурации (18 процентов) нет ни одной автоматической проверки. Интеграционный слой велик, но
никто его не проектировал: на него приходятся около 38 из 74 минут пайплайна и большая часть нестабильных
падений в выборке директора, а контрактных проверок нет ни одной, хотя на границы приходится 23 процента
пропусков.

### 2.2 Case, Billing's objection

**Before.** Команде Billing, которой руководит Marcus Oyelaran, принадлежали 38 из 140 тестов, и она
заявила, что ресурса у неё нет. Директор указал на правило бюджета (после срока — исправить или удалить по
решению). Указал он и на 25 процентов ресурса Billing, зарезервированные на профилактику с недели 4.
Команда Billing удалила 15 тестов, дублировавших модульные, и переписала 23 на контейнеризованные базы
данных.

**After.** Команде Billing (руководитель — Marcus Oyelaran) принадлежали 38 из 140 тестов, и она заявила,
что ресурса на них нет. Директор напомнил о правиле бюджета (после срока — исправить или удалить по
решению) и о 25 процентах ресурса Billing, зарезервированных на профилактику с недели 4. В итоге Billing
удалила 15 тестов, дублировавших модульные, а 23 переписала на контейнеризованные базы данных.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| исследовательский сценарий (charter) | «задание на исследование (charter)» | the chapter also uses «сквозной сценарий» and «пользовательский сценарий» (scenario); «сценарий» for charter collides with both. Kept for consistency with `first-quarter.ru.md` |
| показатель мутационного тестирования | «мутационный балл (mutation score)» | the current form is long and appears in tables and takeaways |
| контрольная точка (gate) | keep | reads well; «гейт» is jargon |
| общее достояние (commons) | keep | clear in context |
| «после срока — исправить или удалить по решению» | «после срока тест исправляют или удаляют, и это фиксируется решением» | the compressed phrase appears twice and «по решению» is unclear (whose decision?) |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Boundaries.** «границы, такие как выставление счетов и платёжный шлюз» → «границы, например между
   выставлением счетов и платёжным шлюзом»: read as one boundary (billing to gateway), matching the case.
   If the English lists two separate boundaries, revert.
2. **Regression automation.** «Регрессию в организации легче всего автоматизировать» → «Регрессия — то,
   что в организации легче всего автоматизировать». If the English means "of all manual testing", say so.
3. **Luo et al.** «201 коммит, исправлявший вероятно нестабильные тесты»: kept the reading "fixing likely
   flaky tests" («предположительно нестабильные»). If the English is "commits that likely fixed flaky
   tests", move the hedge.
4. **Case, end.** «Но механизмы сдвинулись» → «Но механизмы изменились». If the English means the leading
   indicators moved, «опережающие показатели сдвинулись» would be more exact.
5. **Elena's condition.** «Billing будет проверять каждое ожидание по смыслу» kept with Billing as the
   reviewer. If Payments reviews Billing's expectations, the subject is wrong.
6. **People (CTO section).** «Каждый инженер следит» read as "every engineer is watching how QA engineers
   are treated", not as a duty.
7. **Combined label** «мнением экспертов и задокументированной практикой» (from notes-t5) kept.

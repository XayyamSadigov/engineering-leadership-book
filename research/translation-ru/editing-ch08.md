# Literary editing notes: chapter 8

File: `docs/parts/02-people-management/08-career-development-promotion-and-compensation.ru.md`. Edited from
the Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `git show HEAD:<file>`
(214 tokens, NBSP normalised); link texts and targets (43), `{ #anchors }`, exercise labels, admonition
types, table rows and every number inside tables are identical; Mermaid blocks untouched. Failure-mode
fields relabelled «Сигнал:» → «Как заметить:», «Исправление:» → «Что делать:». One misplaced NBSP moved to
the label side («квартала 3⍽руководители» → «квартала⍽3 руководители»). Table text edited without touching
numbers (calibration patterns, scope row, two decision-table rows, one pay-table description).

Patterns from section 2a appeared as expected (scale openers «На уровне команды / организации / высшего
руководства» → «Для команды…»; missing connectives; «Решения — в решениях» → «Разборы упражнений — в
решениях»). Only new patterns are listed below.

## 1. Patterns new beyond section 2a

### 1.1 Term-base drift: «кейс» for "promotion case"

The translation used «кейс (на повышение)» about twenty times, while the term base fixes «заявка на
повышение» (chapter 5 already uses it). In this chapter «кейс» also collides with the «Кейс» section and
the Northstar «кейс». Switched throughout where a promotion case is meant.

- «Кейс представляют независимые читатели; выдвинувший только отвечает на вопросы» → «Заявку представляют
  независимые читатели; выдвинувший руководитель только отвечает на вопросы»
- «То, что человек слышит после отклонённого кейса, решает, станет ли «пока нет» планом…» → «От того, что
  человек услышит после отклонённой заявки, зависит, станет ли «пока нет» планом…»
- «Калиброванный цикл занимает недели, поэтому исключительный кейс может ждать полгода» → «Цикл с
  калибровкой занимает недели, поэтому исключительная заявка может ждать полгода»

### 1.2 Spatial calque «через несколько команд» ("across several teams")

- «предметная область через несколько команд» (prose and table) → «предметная область, охватывающая
  несколько команд»
- «Такая лестница повышает тех, кто сидит там, где сходятся зависимости, если руководители не создают
  возможностей сами» → «Если руководители не создают возможностей сами, такая лестница повышает тех, кто
  сидит на пересечении зависимостей» (condition first, point last)

### 1.3 "Liability" / "owns" / "belongs to" rendered with possession verbs

English managerial possession ("the gap is partly the manager's", "the CTO owns the risk", "is a
liability") came through as «принадлежит», «владеет», «обязательство».

- «пробел отчасти принадлежит руководителю» → «за этот пробел отчасти отвечает руководитель»
- «CTO также владеет риском» → «Риск тоже лежит на CTO»
- «Три решения принадлежат CTO» → «Три решения остаются за CTO»
- «HR владеет вилками и рыночными данными; разработка владеет уровнями» → «За вилки и рыночные данные
  отвечает HR, за уровни и свидетельства — разработка»
- «это обязательство с рисками там, где действует закон…» → «становится источником риска там, где…»
  (see meaning doubt 1)

### 1.4 "X does Y to Z" verbs: «проваливает», «растянет», «производит»

- «расплывчатое «пока нет» проваливает второе, а «пока нет» без обязательства — первое» → «Расплывчатое
  «пока нет» не справляется со второй частью, а «пока нет» без обязательства — с первой»
- «Назовите одно задание, которое растянет человека в выбранном им направлении» ("stretch") → «Назовите
  одно задание на вырост в выбранном человеком направлении»
- «Опыт производит свидетельства; должность — результат свидетельств» → «Опыт даёт свидетельства, а
  должность — следствие свидетельств»

### 1.5 Noun-subject consequences («Понижение уровня… даёт сотрудника»)

English "Down-leveling to fit budget produces an underpaid employee…" kept the gerund as subject.

- «Понижение уровня, чтобы уложиться в бюджет, даёт сотрудника, которому недоплачивают… Завышение уровня,
  чтобы выиграть кандидата, даёт человека, которого судят…» → «Если занизить уровень, чтобы уложиться в
  бюджет, получится сотрудник, которому недоплачивают… Если завысить уровень, чтобы выиграть кандидата,
  человека будут судить…»
- «Повышение оклада, которое исправляет разрыв без такой причины, — это корректировка…» → «Если оклад
  повышают, чтобы устранить разрыв, у которого такой причины нет, это корректировка…»

### 1.6 Contrastive pairs joined by «и» where Russian needs «но»

Trade-off sentences ("A does X and Y", where Y is the cost) lose the contrast with «и».

- «Детальные критерии делают решения единообразными и вознаграждают тех, кто оптимизирует под чек-лист» →
  «…единообразными, но вознаграждают тех, кто подстраивается под чек-лист»
- «Рыночная оплата за редкие навыки помогает нанимать и создаёт сжатие» → «…помогает нанимать, но создаёт
  сжатие»

### 1.7 Ambiguous «который» after a compound genitive

- «провести дизайн контракта экспорта из ledger, который предложила Li Na Zhou, через ревью Billing»
  (contract or ledger?) → «Li Na Zhou (…) предложила контракт экспорта из ledger, и Yusuf должен провести
  его дизайн через ревью Billing»

### 1.8 Clashing ordinals across adjacent paragraphs

«На схеме две петли… Первая… Вторая ведёт…» was immediately followed by the paragraph «Вторая идея:…».
Loops renamed «В одной… Другая…» so «Вторая идея» stays unambiguous. Watch for this wherever the mental
model has both "two loops" and "the second idea".

## 2. Two showcase paragraphs

### 2.1 Offer level (noun subjects, run-on)

**Before.** Уровень, выбранный при оффере, важнее стартового оклада: он задаёт вилку, ожидания и дату
первого повышения. Выбирайте его по свидетельствам из карточки найма в сравнении с вашей лестницей
(глава 7), а не по нынешней должности или зарплате кандидата (**рекомендация книги**). Должности в разных
компаниях означают разное, а прежняя зарплата переносит прошлое неравенство вперёд; в некоторых
юрисдикциях о ней запрещено спрашивать. Часто встречаются две ошибки. Понижение уровня, чтобы уложиться в
бюджет, даёт сотрудника, которому недоплачивают за работу следующего уровня, и проблему равенства в
течение года. Завышение уровня, чтобы выиграть кандидата, даёт человека, которого судят по ожиданиям, на
которые его никогда не проверяли. Если свидетельства находятся между двумя уровнями, предложите нижний с
письменной датой пересмотра и скажите, какие свидетельства его изменят.

**After.** Уровень, выбранный при оффере, важнее стартового оклада: он задаёт вилку, ожидания и дату
первого повышения. Выбирайте его, сопоставляя свидетельства из карточки найма с вашей лестницей
(глава 7), а не по нынешней должности или зарплате кандидата (**рекомендация книги**). Должности в разных
компаниях значат разное, а прежняя зарплата переносит в будущее прошлое неравенство; к тому же в
некоторых юрисдикциях о ней запрещено спрашивать. Две ошибки встречаются часто. Если занизить уровень,
чтобы уложиться в бюджет, получится сотрудник, которому недоплачивают за работу следующего уровня, и в
течение года — проблема равенства. Если завысить уровень, чтобы выиграть кандидата, человека будут судить
по ожиданиям, на соответствие которым его никогда не проверяли. Если свидетельства лежат между двумя
уровнями, предложите нижний, письменно назначьте дату пересмотра и скажите, какие свидетельства изменят
решение.

### 2.2 Case: the rewrite

**Before.** Во втором квартале директор и HR-партнёр набросали пять описанных выше измерений для трёх
уровней и проверили их на двадцати инженерах из всех шести команд. Представление Farah об уровне Senior
по масштабу совпало со столбцом Staff в черновике: её команда требовала от Senior стандарта staff. А
измерение операционной ответственности поставило нескольких инженеров Billing выше их должностей: тем,
кто нёс на себе вызовы по ledger, это никогда не засчитывали.

**After.** Во втором квартале директор и HR-партнёр набросали пять описанных выше измерений для трёх
уровней и проверили их на двадцати инженерах из всех шести команд. Оказалось, что Farah понимает масштаб
уровня Senior так, как в черновике описан столбец Staff: её команда требовала от senior-инженеров
стандарта staff. А по измерению операционной ответственности несколько инженеров Billing оказались выше
своих должностей: тем, кто тянул на себе вызовы по ledger, это никогда не засчитывали.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| кейс (promotion case) | «заявка на повышение» everywhere, as the term base already says | applied here; check chapters 4, 29 and the ch08 solutions page for the same drift |
| адвокатство (calibration pattern "advocacy") | «сила защитника» | «адвокатство» is not idiomatic Russian; applied in the table |
| входы (inputs: tenure, tools, effort; EM "manages the inputs") | keep, or «вклад» in prose | understood by engineers, but reads as jargon twice in the chapter |
| текущий журнал (running log) | align with chapter 5's «журнал роста» if that is the same artifact | two names for what looks like one document |
| корректировка для выравнивания оплаты / выравнивающая корректировка | keep both (long form first, short after) | consistent with notes-t2 |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Why this matters, executive paragraph.** «это обязательство с рисками» is almost certainly
   "liability"; rendered «становится источником риска». If the English means a legal liability
   specifically, «юридическая уязвимость» (as in the CTO section) would be closer.
2. **«Различия внутри вилки законны»** kept. If the English is "legitimate" rather than "lawful",
   «правомерны» or «обоснованны» is better; «законны» narrows it to law.
3. **Sunil's history.** «в тот год прибавка при повышении была ограничена 8%, затем около 3% в год»
   rendered «в год повышения прибавка была ограничена 8%, потом оклад рос примерно на 3% в год». Confirm
   that "that year" is the promotion year and the 3% is annual base growth.
4. **Case, opening.** «Одна из двух инженеров, ушедших из Data and Analytics за прошлый год» is now two
   sentences («ушли двое инженеров. Одна из них…»). This states that exactly two left the team; the
   original Russian implied the same.
5. **References, EU directive.** «прочитанный полностью» is an access note in reader text (CLAUDE.md §7
   forbids maintainer bookkeeping). Not changed; the maintainer may fold it into the evidence label.
6. **X2.** «возможное сжатие оплаты»: in this chapter «сжатие» is the compression term (new hires above
   tenured peers), but transparency compresses the *spread* of pay. If the English means the latter,
   «сужение разброса оплаты» would avoid a clash with the defined term.

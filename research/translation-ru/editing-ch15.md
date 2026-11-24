# Literary editing notes: chapter 15

File: `docs/parts/04-execution/15-planning-prioritization-and-delivery-methods.ru.md`. Edited from the
Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes. Digit atoms (sorted) are identical to `git show HEAD:<file>` (302); the
brief's number tokens differ only where two adjacent numbers were separated by reordering («квартал 2
28 процентов» → «на квартал 2 модель прогнозирует 28 процентов»). Link texts and targets (44),
`{ #anchors }` (30), exercise labels, the admonition, both Mermaid blocks, table shapes and every number
in tables are identical. Failure-mode fields relabelled «Признак:» → «Как заметить:», «Противоядие:» →
«Что делать:». One heading reworded, anchor kept: «Что на самом деле говорят методы» → «Что говорят сами
методы»; «Разобранная дорожная карта результатов» → «Пример дорожной карты результатов». Twelve label
numbers had the NBSP on the wrong side («квартале 1⍽отдали», «дню 90⍽оба») and were fixed; «к дню 90»
→ «к Дню 90».

Patterns from section 2a appeared as expected (missing connectives, «решение» → «вывод», «Решения — на
странице решений» → «Разборы упражнений — …»). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Tautologies from English collocations

- «измерять выпущенный выпуск (output) вместо достигнутых результатов» → «измерять выпуск (output)
  вместо достигнутых результатов (outcome)»
- «у CEO можно спросить, так ли это, — вопрос лучше, чем вопрос о том, важна ли просьба CEO» → «— вопрос
  куда полезнее, чем спор о том, важна ли просьба CEO»

### 1.2 "Owns" in managerial prose (extends ch08 1.3 to planning)

- «Пусть стейкхолдеры владеют своими оценками (продажи — ценностью сделки…)» → «Пусть стейкхолдеры сами
  отвечают за свои оценки (продажи — за ценность сделки…)»
- «**Директор владеет правилами портфеля**» → «**Правила портфеля задаёт директор**»
- «**Продукт владеет оценками ценности; разработка — длительностью и процентами.**» → «**За оценки
  ценности отвечает продукт, за длительность и проценты — разработка.**»

### 1.3 "Never a named method" rendered as «никакой метод с названием»

- «фиксированные циклы или никакой метод с названием» → «циклы фиксированной длины или метод без
  названия»
- objectives: «(Scrum, Kanban, циклы фиксированной длины или никакой)» → «— Scrum, Kanban, циклы
  фиксированной длины или работу без метода —»

### 1.4 "X gives a team that…" (consequence as object of «даёт»)

- «Метод, который не подходит работе, даёт команду, которая работает изо всех сил и всё равно вечно
  «отстаёт».» → «Если метод не подходит работе, команда трудится изо всех сил и всё равно вечно
  «отстаёт».»
- «Стоимость задержки, делённая на длительность, даёт ранжирование, которое…» → «Если разделить
  стоимость задержки на длительность, получится ранжирование, которое…»

### 1.5 Present tense left inside a past narrative

- «с двумя клиентами, которых рискует потерять» (the case is told in the past) → «которых рисковала
  потерять»
- «Core перешёл на еженедельные релизы с недели 5 квартала 1» kept as a fact, but rebuilt so the label
  comes first: «С недели 5 квартала 1 Core выпускается еженедельно, так что…»

### 1.6 Sentences opening with a bare numeral

Russian typography avoids starting a sentence with digits. «17 пунктов, на которые взяли обязательство, в
сумме дали…» → «Вместе 17 пунктов, по которым взяли обязательство, требовали…». Also «на которые взяли
обязательство» → «по которым взяли обязательство» throughout (the government of «обязательство по»).

### 1.7 «положить варианты на стол», «в терминах ценности»

- A1: «какие варианты положите на стол» → «какие варианты предложите»
- failure mode: «перепланирования, которые никто не может объяснить в терминах ценности» → «…которые
  никто не может обосновать ценностью»

## 2. Two showcase paragraphs

### 2.1 Why this matters, organization

**Before.** Для организации приоритизация определяет, что приносит бюджет разработки, потому что
отложенная ценность — потерянная ценность. Когда приоритет получает тот, кто эскалировал последним,
организация платит дважды: ценностью работы, которая должна была идти первой, и перепланированием и
брошенной недоделанной работой, которые вызывает каждая эскалация.

**After.** Для организации приоритизация определяет, что даёт бюджет разработки: отложенная ценность —
потерянная ценность. Когда приоритет получает тот, кто эскалировал последним, организация платит
дважды. Сначала — ценностью работы, которая должна была идти первой. Затем — перепланированием и
брошенной на полпути работой, которые тянет за собой каждая эскалация.

### 2.2 Mental model, first idea

**Before.** Каждый метод предполагает, что преобладает своя форма. Команда, у которой треть работы —
прерывания, а живёт она по методу, предполагающему защищённый двухнедельный план, будет срывать план
каждый раз, и виноватыми окажутся люди.

**After.** Каждый метод исходит из того, что преобладает какая-то одна форма. Если у команды треть
работы — прерывания, а живёт она по методу, рассчитанному на защищённый двухнедельный план, план будет
срываться каждый раз, а виноватыми окажутся люди.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| допустить обязательство (admit) | keep | reads oddly at first («допустить первыми»), but the chapter uses it consistently as a gate; a gloss on first use («допустить в план») would help |
| фикция ресурсов | keep | works as a failure-mode name |
| соответствие (trade-off "standardization vs fit") | «соответствие работе» | bare «соответствие» collides with «соответствие требованиям» (compliance) in the term base; applied in the heading |
| петля громкости | keep | the image carries in Russian |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Roadmap cadence.** «держит её честной внутри квартального перезапуска организации»: «её» could be the
   team or the roadmap. Rendered as the roadmap («держит карту честной в промежутках между квартальными
   перезапусками планов организации»).
2. **Two renewal commitments.** «(небольшая до даты, а затем — продление)» rendered «до даты небольшая, а
   затем на кону продление». Check that the English means the whole renewal is at stake after the date.
3. **Reflection 2.** «Какой была бы его стоимость задержки»: whose, the loud or the quiet request? Kept
   ambiguous with the quiet request as the nearest antecedent.
4. **Failure mode «Скорость как мера результативности».** «по ней судят» rendered «по ней судят о
   работе»; if the English means individuals are judged by velocity, «оценивают людей» is closer.
5. **«Массовый заказ… по нескольким площадкам доставки»** kept; if the English is "multiple ship-to
   locations", «с доставкой по нескольким адресам» would be clearer.

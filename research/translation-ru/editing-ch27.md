# Literary editing notes: chapter 27

File: `docs/parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (295
tokens, NBSP normalised); `{ #anchors }`, headings, link targets, citations, exercise labels, the admonition,
every table line and both Mermaid blocks are byte-identical. Failure-mode labels were already «Как заметить:» /
«Что делать:». About 90 sentence-level edits; no NBSP misplacements found.

The wave-1 text was accurate and clean in terms. Section 2a patterns appeared as expected (missing
connectives, English word order, an announced pair of items left unnumbered). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Pronoun gender broken by English "it"

English "it" survives a rebuild and points at a noun of the wrong gender.

- «…и среди них двухчасовая задержка платежей для девяти клиентов. Директор переоценил его серьёзность на
  разборе…» (его → задержка?) → «Среди них была двухчасовая задержка платежей у девяти клиентов. На разборе
  директор пересмотрел серьёзность этого инцидента…»

### 1.2 "For X, the questions are: …" as a nominal frame

- «Для высшего руководства вопросы такие: какая выручка…» → «Высшее руководство спросит о четырёх вещах:
  какая выручка…»
- «Northstar показывает, как это выглядит.» → «Как это выглядит, видно на примере Northstar.»

### 1.3 Two English clauses collapsed into one Russian clause

English "If so, say so, and say what will not happen" was merged into one ungrammatical sentence.

- «Если действительно никто не теряет работу, так прямо и скажите, чего не произойдёт.» → «Если работу
  действительно никто не потеряет, так прямо и скажите: назовите то, чего не произойдёт.»
- «…добавляет давление сроков, а это одна из причин притока.» → «…к тому же усиливает давление сроков, а
  оно — одна из причин притока.»

### 1.4 Mixed noun and infinitive forms after «Что делать:»

Within one failure-modes section some remedies were infinitives, others bare noun lists. Use infinitives
throughout.

- «Что делать: определения серьёзности по влиянию на клиентов, еженедельный аудит выборки решений о
  серьёзности, парные метрики.» → «Что делать: определять серьёзность по влиянию на клиентов, каждую неделю
  проверять выборку решений о серьёзности, держать метрики в парах.»
- «Что делать: меньше действий, у каждого владелец-руководитель, ежемесячный пересмотр» → «Что делать:
  назначать меньше действий, каждому — владельца-руководителя, пересматривать их ежемесячно»

### 1.5 Time-of-day calques

- «провёл с Kwame Mensah две вторые половины дня» ("two afternoons") → «провёл за классификацией инцидентов
  два раза по полдня»

## 2. Two showcase paragraphs

### 2.1 Why this matters, executive questions

**Before.** Для высшего руководства вопросы такие: какая выручка под угрозой, когда ситуация выправится,
сколько это стоит и что будет с обязательствами по дорожной карте. План трансформации должен ответить на все
четыре в цифрах. Планы редко проваливаются из-за того, что не знают нужных практик. Они проваливаются на
последовательности (разбирают бэклог, пока приток продолжается), на измерении (цели выполняют
переклассификацией), …

**After.** Высшее руководство спросит о четырёх вещах: какая выручка под угрозой, когда ситуация выправится,
сколько это стоит и что будет с обязательствами по дорожной карте. План трансформации должен ответить на все
четыре вопроса в цифрах. Проваливаются планы редко из-за того, что авторы не знают нужных практик. Ломаются
они на другом: на последовательности (разбирают бэклог, пока приток продолжается), на измерении (цели
выполняют за счёт переклассификации), …

### 2.2 Case, the first finding

**Before.** На неделе 2 новый директор провёл с Kwame Mensah две вторые половины дня (staff-инженер,
инфраструктура и надёжность), классифицируя инциденты. Когда руководители увидели результат, их удивили две
вещи. Девять из тридцати инцидентов пришли через релизный поезд Core, и именно их восстанавливали дольше
всего. А 11 из 30 оказались повторением сбоев, которые организация уже разбирала, в том числе отказ массовой
загрузки (INC-421), почти в точности повторивший инцидент двумя кварталами раньше.

**After.** На неделе 2 новый директор вместе с Kwame Mensah (staff-инженер, инфраструктура и надёжность)
провёл за классификацией инцидентов два раза по полдня. Результат удивил руководителей дважды. Во-первых,
девять из тридцати инцидентов пришли через релизный поезд Core, и как раз их восстанавливали дольше всего.
Во-вторых, 11 из 30 повторяли сбои, которые организация уже разбирала. Среди них был отказ массовой загрузки
(INC-421) — почти точная копия инцидента двумя кварталами раньше.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| две вторые половины дня (two afternoons) | «два раза по полдня»; changed | the literal form is a calque |
| вычерпывать запас | keep | vivid and consistent with the mental model |
| просадка (feature capacity dip) | keep | reads naturally in planning prose |
| театр метрик, кладбище действий | keep | idiomatic enough in Russian IT usage |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Example, "Three readings".** I added the lead-in «Из модели следуют три вывода.» before «Во-первых…»
   (no new claim). Remove it if the maintainer prefers none.
2. **Failure mode "Practice mandates".** «Пачки растут, или тесты выполняют код…» was
   rendered «В итоге растут пачки либо появляются тесты, которые выполняют код…». I assumed "or" means
   "one of the two outcomes, depending on the mandate". Check.
3. **Director's QA announcement.** «Директор отложил объявление до недели 10, когда двое QA-инженеров уже
   спросили…» was rendered «…и к тому времени двое QA-инженеров уже спросили…». Same facts; check that the
   English does not say the questions caused the announcement.
4. **CTO perspective, «доступность по договору против обязательства».** Rendered «доступность по договору в
   сравнении с обязательством». If the English is "availability against the contractual commitment", the
   better wording is «доступность в сравнении с договорным обязательством».
5. **«Срезанные углы … ; профилактика — это тесты…».** The paragraph says «Обе петли работают в любую
   сторону», but the diagram shows one loop with two branches. Probably in the English too.

# Literary editing notes: chapter 60

File: `docs/parts/15-capstone/60-capstone-northstar.ru.md`. Edited from the Russian text only; the English
chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in the session
scratchpad.

Checks: `validate_book.py` passes; the multiset of numeric tokens is identical before and after (812
digit runs, NBSP normalised; one sentence that briefly repeated «неделя 49» was rebuilt to keep the
count); link targets and their order, citation link texts, `{ #anchors }`, heading lines, exercise labels,
admonition lines, every table line and both Mermaid blocks are byte-identical. The `!!! warning` body
stays indented on its own lines. No wrapped line starts with a number and a period. NBSP 257 → 270.
About 110 sentence-level edits.

Applied as instructed: stages are «этап» throughout; audit "findings" → «замечания» (enterprise section:
«Записи с двумя последними статусами и есть замечания аудита»; «аудита» added because the chapter also
uses «замечание» for Victor's remark). Failure Modes have only «Как заметить:».

Section 2a patterns appeared as expected. Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Assignment text: descriptive present where the reader must act

An assignment states what the reader does. English "Stage 1–6 use only director facts" came through as a
general statement; Russian needs the imperative.

- «на этапах 1–6 используются только факты директора» → «на этапах 1–6 используйте только факты
  директора»
- «Пункты этапа 5, которые заканчиваются на неделе 5, входят как профинансированные намерения» → «…
  включите как профинансированные намерения»
- «В вашей работе рамки должны быть показаны при 80, 79 и 78 инженерах, и должна быть названа строка…»
  → «В своей работе покажите рамки при 80, 79 и 78 инженерах и назовите строку…»

### 1.2 Completion criteria and multi-part tasks packed into one sentence

- «Работа готова, когда каждый этап отвечает своим критериям… у каждой записи реестра есть статус,
  двухстраничная записка… написана и все семь проверок… пройдены» → «Работа готова, когда выполнены
  четыре условия: …; …; …; …» (the criterion label now matches the table header «Достаточно, если»)
- «Объясните, почему…, какие ещё данные…, и как новая схема…» (same in ch59 F3) → one instruction plus
  two direct questions
- X2: one 60-word closing instruction → three imperative sentences («Сопоставьте… Выберите… Решите…»)

### 1.3 «с недели N» read as "starting from week N"

- «на долю исправленных заказов с недели 40 или на таблицу знаний по Orders с недели 14» → «на долю
  исправленных заказов (неделя 40) или на таблицу знаний по Orders (неделя 14)»

### 1.4 «одолжить»: lend or borrow

- «какая строка черновика должна одолжить дополнительные 0,5 FTE и получить их обратно» → «какая строка
  черновика должна на время отдать дополнительные 0,5 FTE, а в кварталах 7 и 8 получить их обратно»

### 1.5 Calque "through the capstone's eyes"

- «Если смотреть глазами итогового проекта, …» (twice) → «С точки зрения итогового проекта…»

### 1.6 Mechanical risk when rewrapping

Rebuilding «подсчёты года 1 сохраняют исходные 15, а отчёты года 2 используют 14» put «14.» at the start
of a wrapped line (Markdown would start a numbered list). Caught by the check; grep every edited file for
`^\s*[0-9]+\.` after rewrapping.

## 2. Two showcase paragraphs

### 2.1 What "done" means

**Before.** **Для кого эта работа и что значит «готово».** Пишите работу для читателя, который может
возразить: […]. Работа готова, когда каждый этап отвечает своим критериям «достаточно» из таблицы ниже, у
каждой записи реестра есть статус, двухстраничная записка об интеграции написана и все семь проверок из
раздела «Как принимать решение» пройдены.

**After.** **Для кого эта работа и что значит «готово».** Пишите для читателя, который может возразить:
[…]. Работа готова, когда выполнены четыре условия: каждый этап отвечает своему критерию «Достаточно,
если» из таблицы ниже; у каждой записи реестра есть статус; двухстраничная записка об интеграции
написана; все семь проверок из раздела «Как принимать решение» пройдены.

### 2.2 Why stage 9 precedes stage 7

**Before.** На схеме этап 9 идёт раньше этапа 7. В квартале 4 Victor пишет черновик трёхлетней стратегии
на неделе 47 и проверяет его на премортеме на неделе 48. Стратегия на 12 месяцев — это слой года 2 той же
стратегии, поэтому её пишут после. План на год 2, написанный без трёхлетней рамки, порождает политики,
которые ничего не решают: над ними нет ничего, что говорило бы, что важнее всего.

**After.** Обратите внимание: на схеме этап 9 идёт раньше этапа 7. В квартале 4 Victor пишет черновик
трёхлетней стратегии на неделе 47, а на неделе 48 проверяет его на премортеме. Стратегия на 12 месяцев —
слой года 2 той же стратегии, поэтому её пишут после. Если писать план на год 2 без трёхлетней рамки,
получатся политики, которые ничего не решают: над ними нет ничего, что говорило бы, что важнее всего.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| замечание (Victor's remark to Elena) | «реплика» or «устное указание» | collides with audit «замечания» now used for "findings" in the same chapter |
| уступки измору | «сокращения под давлением» | «измор» is vivid but «уступка измору» is hard to parse |
| поворотная точка (hinge); поворотный разбор | keep | consistent and clear once glossed |
| Достаточно, если | keep, also in prose | now matches the table header in the "done" paragraph |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Stage 7 «Допущение» and X1: «приняли вы его или отложили»** rendered «приняли вы предложение или
   отложили». Assumes "it" is the week-44 organization proposal, not the decision itself.
2. **F3, last sentence: «напишите два предложения, которые член совета директоров может понять
   неправильно, если ему покажут только 12 и 5,5 FTE»**. Kept literally; as Russian it asks for sentences
   that will be misread. If the English means "two sentences that prevent the misreading" (or "what a
   board member would misread"), the Russian should say so.
3. **X1: «вопрос о VP, после решения которого останется 78»** rendered «…после решения которого
   инженеров останется 78». Assumes 78 is the engineer count if the VP seat is created (as in the table).
4. **Stage 1: «применив дни 1–15 из главы 27»** rendered «следуя плану дней 1–15 из главы 27». Assumes
   chapter 27 gives a days 1–15 plan.
5. **Enterprise: «Последние два статуса и есть находки»** rendered «Записи с двумя последними статусами и
   есть замечания аудита»; «аудита» added to separate the term from Victor's «замечание».
6. **«Метод итогового проекта переносится на любую организацию…, уже без вымысла»** rendered «на любую
   реальную организацию». Same meaning, assumed.

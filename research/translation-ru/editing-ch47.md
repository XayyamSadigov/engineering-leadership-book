# Literary editing notes: chapter 47

File: `docs/parts/11-vp-engineering/47-the-vp-of-engineering.ru.md`. Edited from the Russian text only; the
English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in the
session scratchpad.

Checks: `validate_book.py` passes (only the expected stale `dist/` single-file error); the sorted list of
numbers is identical before and after (286 tokens, NBSP normalised); link targets, `{ #anchors }`, heading
count, exercise labels, admonition lines, citations, every table line and both Mermaid blocks are
byte-identical. NBSP count 71 → 71. About 65 sentence-level edits. Failure-mode fields are «Признак:» /
«Как заметить:» (no countermeasure field in this chapter).

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives,
English word order, «который» chains). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Doubled possessives from English "its own … its own"

- «компания финансирует свои квадратики, а не свои ставки» → «компания финансирует квадратики на
  оргсхеме, а не ставки»

### 1.2 Abstract "behaviours" as the grammatical subject of a norm violation

- «Нарушают её два поведения: повторно открывать решённый вопрос… и критиковать…» → «Нарушают её двумя
  способами: заново открывают решённый вопрос… и критикуют…»
- «Если это повторится, это должно войти в оценку директора» (two «это») → «Если такое повторится, это
  должно отразиться в оценке директора»

### 1.3 "X is a decision, not Y" turned into a noun predicate

The English "a large gap is a decision (…), not a reason to fund…" came through as «разрыв — это решение».
In Russian a gap is not a decision; it calls for one.

- «Большой разрыв… — это решение (перенести работу…), а не повод профинансировать…» → «Большой разрыв… —
  повод решить, перенести работу, перевести людей или перекроить направление, а не профинансировать…»
- «распределение ресурса — решение, которое отличает VP» → «распределение ресурса — определяющее решение VP»

### 1.4 Ranked superlatives stacked before the noun ("highest-leverage, most-deferred decisions")

- «Решения VP с самым большим рычагом и чаще всего откладываемые касаются директоров» → «Самые весомые
  решения VP, которые к тому же чаще всего откладывают, касаются директоров»

### 1.5 An unexpressed «вместо этого» after a negative sentence

- «Работу команд VP видит редко. Вместо этого он решает…» → «Работу команд VP видит редко: его дело —
  решать…»

## 2. Two showcase paragraphs

### 2.1 Conflict in the director team

**Before.** **Конфликт.** Норма такая: спорить на встрече, а за её пределами держаться решения. Нарушают
её два поведения: повторно открывать решённый вопрос с VP наедине и критиковать направление коллеги перед
его стейкхолдерами. Larson объясняет соперничество между коллегами отчасти привычками, усвоенными там, где
захватить существующий ресурс было выгоднее, чем создать новый, а отчасти руководителем, который не
следит за соблюдением норм (…) (**мнение эксперта**). Значит, следите за ними. […] напомните порядок
(решение заново открывают новые данные, и только на встрече). Если это повторится, это должно войти в
оценку директора.

**After.** **Конфликт.** Норма такая: спорить на встрече, а за её пределами держаться принятого решения.
Нарушают её двумя способами: заново открывают решённый вопрос с VP наедине и критикуют направление
коллеги перед его стейкхолдерами. Соперничество между коллегами Larson объясняет отчасти привычками,
усвоенными там, где захватить существующий ресурс было выгоднее, чем создать новый, а отчасти
руководителем, который не следит за соблюдением норм (…) (**мнение эксперта**). Значит, следить за нормами
должны вы. […] напомните порядок (решение открывают заново только при новых данных и только на встрече).
Если такое повторится, это должно отразиться в оценке директора.

### 2.2 Partition dependence and escalation of commitment

**Before.** Это **научный результат** о капитальных бюджетах; перенос его на ресурс разработки —
расширение, которое делает книга. Если VP выделяет каждому директору долю от его собственного плана,
распределение диктует оргструктура. Работа Staw об эскалации приверженности (escalation of commitment), то
есть о склонности вкладывать всё больше в провальный курс, который выбрал сам (…), добавляет вторую
опасность: труднее всего урезать собственные ставки VP.

**After.** Это **научный результат** о капитальных бюджетах; перенос его на ресурс разработки —
расширение, сделанное книгой. Если VP выделяет каждому директору долю от его собственного плана,
распределение диктует оргструктура. Вторую опасность показывает работа Staw об эскалации приверженности
(escalation of commitment): люди склонны вкладывать всё больше в провальный курс, если выбрали его сами
(…). Поэтому труднее всего урезать собственные ставки VP.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| время из первых рук (firsthand time) | keep in the table; in prose prefer «время на личное наблюдение» | «время из первых рук» is a calque; the table already glosses it |
| VP-передатчик / уровень-передатчик | keep | compact and clear; consistent with notes-t11 |
| притязания на ресурс | keep | reads naturally in the director-conflict context |
| «Как заметить:» for fields that are really countermeasures | book-wide decision as in notes-t12 / notes-t18 | e.g. «Как заметить: запросы на перераспределение идут только через встречу команды директоров» is a rule, not a detector |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Upper echelons: «научный результат на уровне устоявшейся теории…»** rendered «**научный результат**,
   но в статусе устоявшейся теории о высших командах фирм, а не измеренного эффекта в разработке». Check
   that the English contrasts "established theory" with "a measured effect in engineering".
2. **Keil: «(научный результат, по выборкам, которые надо обобщать с осторожностью)»** rendered
   «переносить его за пределы изученных выборок нужно осторожно». Assumes the caveat is about generalising
   from the samples.
3. **«руководители направления говорят, что решения ждут директора»** rendered «руководители отстающего
   направления говорят, что решения подолгу ждут директора». Assumes the managers are those of the late
   area and "wait on the director" means delays.
4. **Trade-offs: «Первый способ подходит для несоответствий…»** rendered «Переводить людей стоит, если
   несоответствие… продлится дольше года»: «первый способ» referred to moving people; made explicit.
5. **X2: «20 чистых добавлений»** rendered «чистый прирост всего на 20 мест»; «всего» added for the
   contrast the sentence already implies. Remove if the English is neutral.
6. F2 still names "VP of Fulfillment" at Halvard (see notes-t18); not changed.

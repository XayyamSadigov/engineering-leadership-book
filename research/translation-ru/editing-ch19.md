# Literary editing notes: chapter 19

File: `docs/parts/05-engineering-quality/19-defining-measuring-and-owning-quality.ru.md`. Edited from the
Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to the pre-edit copy
(202 tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition types, both Mermaid
blocks and every table row are byte-identical. One failure-mode name changed («Единственное число» →
«Одно число»). Non-breaking spaces re-applied by rule (number + counted noun, label + number: «глава⍽22»,
«неделе⍽3», «$440⍽000»).

Section 2a patterns appeared as expected (missing connectives, «который» chains, English word order). Only
new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «Зато» where English "but" introduces a cost, not a compensation

«Зато» announces an advantage; for a downside Russian needs «но».

- «Командное владение на бумаге ничего не стоит, зато специальные навыки теряются…» → «…ничего не стоит,
  но специальные навыки теряются…»

### 1.2 Numbers of comparison in mid-sentence

English puts the compared values right after "than"; Russian reads better with the comparison first and
the figures in brackets at the end.

- «…её доля неудачных изменений (21 процент) заметно ниже, чем 29 и 34 процента у двух команд,
  выпускающихся через поезд Core.» → «…а доля неудачных изменений у неё (21 процент) заметно ниже, чем у
  двух команд, выпускающихся через поезд Core (29 и 34 процента).»
- «Руководители Northstar называют покрытие Core, основного монолита, — 41 процент.» → «Руководители
  Northstar называют для Core, основного монолита, покрытие в 41 процент.»

### 1.3 Abstract noun as subject of a "who does what" sentence

- «Только сквозная группа (41) — тот вид дефектов, который лучше всех найдёт отдельная функция
  тестирования…» → «Отдельная функция тестирования лучше других найдёт только дефекты сквозной группы
  (41)…»
- «Самое полезное, на что можно опереться при решении о владении, — классификация…» → «Решать вопрос о
  владении лучше всего с опорой на классификацию…»
- «Поворот в разговор внесли QA-инженеры: …» → «Переломили разговор QA-инженеры.»

### 1.4 «который» relative replaced by «чей»

- «Свойством должен владеть тот, кто принимает решения, которые его меняют.» → «…тот, чьи решения его
  меняют.»

### 1.5 Chapter as an agent that "requires" or "asks"

- «Эта глава требует лишь, чтобы у атрибута было имя и владелец.» → «Здесь достаточно, чтобы у атрибута
  были имя и владелец.» (also fixes the agreement: «были имя и владелец»)

### 1.6 Unintended grammar pun in a name

- Failure mode «Единственное число» ("The single number") reads as the grammatical term "singular" →
  «Одно число».

## 2. Two showcase paragraphs

### 2.1 Why this matters, team and organization

**Before.** Для команды неопределённое понятие качества оборачивается спорами, которые никогда не
заканчиваются: больше тестов, меньше инцидентов, меньше жалоб — и каждое из этого описывает своё
свойство. Побеждает тот, кто громче. / Для организации цена — в том, кто владеет качеством. Если качество
— это «то, что проверяет QA», оно принадлежит тем, кто проводит проверки, а команды, которые пишут код,
узнают о своих дефектах поздно, из вторых рук и пачкой. … Определение, которое живёт в тест-плане, не
поймает того, что этот план никогда не описывал.

**After.** Для команды размытое понятие качества оборачивается бесконечными спорами: что считать
качеством — больше тестов, меньше инцидентов или меньше жалоб? Каждый ответ описывает своё свойство, и
побеждает тот, кто громче. / Для организации цена определяется тем, кто владеет качеством. Если качество —
это «то, что проверяет QA», оно принадлежит проверяющим, а команды, которые пишут код, узнают о своих
дефектах поздно, из вторых рук и сразу пачкой. … Если определение качества живёт в тест-плане, оно не
поймает того, чего в этом плане никогда не было.

### 2.2 Case, the turning point

**Before.** Поворот в разговор внесли QA-инженеры: дефекты сквозных сценариев возникали в основном в
сценариях, которые регрессионный набор не покрывал, потому что никто не сказал им, что эти сценарии
изменились. Их проблема была в дистанции от команд, а не в старании, и услышанное от них подействовало на
руководителей сильнее, чем данные.

**After.** Переломили разговор QA-инженеры. Дефекты сквозных сценариев, рассказали они, возникали в
основном в сценариях, которых регрессионный набор не покрывал: никто не говорил им, что эти сценарии
изменились. Их проблемой была дистанция от команд, а не недостаток старания, и услышанное от них
подействовало на руководителей сильнее, чем данные.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| нормирование (числа дефектов) | keep; avoid the plural «нормировки» | «нормирование» also means rationing; used consistently as «способ нормирования» here |
| открытость клиентам (exposure) | «насколько код на виду у клиентов» in prose where it reads stiffly | «открытость» suggests transparency; kept for consistency |
| ворота релиза (in Failure Modes, "release gate") | «контрольная точка релиза» | the term base has «контрольная точка (gate)»; kept «ворота релиза» here, maintainer's call |
| практичная точка обнаружения (playbook step 2) | «разумная» as elsewhere in the chapter | if the English uses one word ("reasonable") throughout |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **27 escaped defects "built to spec".** «были сделаны точно по спецификации» → «точно соответствовали
   спецификации». Confirm the English means the implementation matched the specification.
2. **Internal quality.** «насколько легко безопасно менять систему» → «насколько легко менять систему без
   риска». Assumes "how easy it is to change safely".
3. **Deployments note under the table.** Added «поэтому» («Развёртывания здесь посчитаны за квартал,
   поэтому их втрое больше, чем в месячном показателе…»): assumes the note explains the unit, not a growth.
4. **Case, 1:1s.** «Четыре ответа указали…» → «Четверо указали…»: assumes one answer per manager.
5. **Evidence section.** «позиция ниже — рекомендация книги» → «дальше — рекомендация книги»; «Команды
   владеют результатами своих изменений с точки зрения качества» → «Качеством своих изменений владеют сами
   команды». Confirm the English is "teams own the quality outcomes of their changes".
6. **Centralized QA for "specialist or mandated" testing.** «для специального тестирования или
   тестирования, независимость которого предписана» → «…и для тестирования…»: same scope, conjunction
   only.

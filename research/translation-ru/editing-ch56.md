# Literary editing notes: chapter 56

File: `docs/parts/13-advanced-problems/56-recovering-a-failing-engineering-organization.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the multiset of numeric tokens is identical before and after (366 tokens,
NBSP normalised); link targets, citation link texts, `{ #anchors }`, heading lines, exercise labels,
admonition lines, every table line and all three Mermaid blocks are byte-identical. One chapter link text
changed case («глава 57» → «главе 57»), target unchanged. No wrapped line starts with a number and a period
(22 numbered-list lines before and after). About 65 sentence-level edits. NBSP 77 → 77. Failure-mode
fields are «Как заметить:» only.

Section 2a patterns appeared as expected, plus the ch53 «стоит» pattern («стоит вам руководителей» →
«потеряете руководителей»; «сколько ресурса оно стоит» → «требует»). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 A defining "if A and if B" split into a sentence fragment

- «…проваливается, если нарушает обязательства… И если при её нынешней траектории разрыв не закроется…» →
  «…проваливается, если выполнены два условия. Она нарушает обязательства… И при нынешней траектории
  разрыв не закроется…»

### 1.2 "Decides whether" rendered as plain causation

- «Из-за неё клиенты продлевают контракты или уходят» (renewing is not caused by failure) → «От неё
  зависит, продлят клиенты контракты или уйдут»

### 1.3 "With the least information you will ever have" calqued

- «предпринимаются при минимуме информации, который у вас когда-либо будет» → «их предпринимают, когда
  информации у вас меньше всего»
- «выпущенная при минимуме информации, который у вас когда-либо будет» → «которую выпускают, когда
  информации у вас меньше, чем будет когда-либо потом»

### 1.4 A term colliding with the same root in the sentence

«Вывод из кризиса» (turnaround) clashes with «вывод» (conclusion) and with «кризисный».

- «назначение… означало вывод, что директора не смогут вести вывод из кризиса» → «за этим стояло
  суждение: директора не смогут одновременно выводить её из кризиса и…»
- «кризисный режим вывода из кризиса» → «вывод из кризиса (turnaround) с его кризисным режимом»

### 1.5 Comparing unlike things ("the all-hands matters less than the managers do")

- «Общее собрание с новым руководителем значит меньше, чем руководители команд» → «Руководители команд
  значат больше, чем общее собрание с новым руководителем»

## 2. Two showcase paragraphs

### 2.1 What "failing" means

**Before.** Словом «проваливается» пользуются вольно. В этой книге у него узкое значение (…). Инженерная
организация проваливается, если нарушает обязательства, на которые рассчитывает кто-то вне разработки:
договорную доступность, корректность данных, сроки для клиентов, регуляторные требования. И если при её
нынешней траектории разрыв не закроется, пока не изменится то, как ею управляют. Это не то же самое, что
**деградация** (организации становится хуже, но, возможно, она ещё укладывается в обязательства) и
**работа ниже возможностей** (…).

**After.** Словом «проваливается» пользуются вольно. В этой книге у него узкое значение (…). Инженерная
организация проваливается, если выполнены два условия. Она нарушает обязательства, на которые рассчитывает
кто-то вне разработки: договорную доступность, корректность данных, сроки для клиентов, регуляторные
требования. И при нынешней траектории разрыв не закроется, пока не изменится то, как ею управляют. Это не
то же самое, что **деградация** (организация становится хуже, но, возможно, ещё укладывается в
обязательства) или **работа ниже возможностей** (…).

### 2.2 Diagnosis at Halvard

**Before.** […] Сильнее всего петля людей в Pay Calculation. Вместе с уходами ушли знания о движке расчёта
зарплаты, а Rhys Gallagher, который девять лет назад построил значительную его часть, сам вёл все семь
созвонов по инцидентам Sev1 в прошлом квартале (это живые созвоны, на которых координируют работу те, кто
чинит). Его руководители говорят, что решения ждут его.

**After.** […] Сильнее всего петля людей в Pay Calculation. С ушедшими людьми ушли и знания о движке
расчёта зарплаты. Rhys Gallagher, который девять лет назад построил значительную часть движка, в прошлом
квартале сам вёл все семь созвонов по инцидентам Sev1 (живых созвонов, где координируют работу те, кто
чинит). Его руководители говорят, что решения ждут его.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| вывод из кризиса (turnaround) | keep, but avoid «вывод» = conclusion anywhere in the chapter | see 1.4 |
| метрики механизмов | gloss once in this chapter («метрики того, работают ли механизмы: разборы вовремя, график координаторов») | the reader meets it in the Example without a definition |
| работать через коучинг | keep | reads naturally; the quoted form «работают через коучинг» in the failure mode works |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«Новому руководителю приходится ставить диагноз через них»** rendered «Ставить диагноз новому
   руководителю приходится с их помощью». Assumes "through them" means relying on their information.
2. **«кризисный режим вывода из кризиса (turnaround)»** rendered «вывод из кризиса (turnaround) с его
   кризисным режимом». Check what the English qualifies as "crisis mode".
3. **«15 или меньше во втором квартале случайно выпадает…»** now in the conditional («выпадало бы»), to
   match «если бы истинная частота не изменилась».
4. **«Поставка была стабильной и слабой»** rendered «стабильной, но слабой»; the contrast is implied.
5. **«Результаты… 14 в квартале 3 — первом квартале на уровне лимита мандата в 15 инцидентов или ниже»**
   rendered «первый квартал, когда число не превысило лимита мандата в 15 инцидентов»: same meaning.

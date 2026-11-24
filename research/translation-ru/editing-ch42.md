# Literary editing notes: chapter 42

File: `docs/parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.ru.md`.
Edited from the Russian text only; the English chapter was not opened. The file was not yet committed, so
the pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numbers (`grep -oE '[0-9][0-9 ,.]*'`, trailing
separators stripped) is identical before and after (231 digit tokens); headings, `{ #anchors }`, link
targets, exercise labels, bold spans, admonition lines and both Mermaid blocks are byte-identical. Two
table cells changed wording only («в терминах финансов» → «на языке финансов», «в его терминах» → «на его
языке»); table structure and numbers untouched. NBSP 69 → 71: «на неделях 4» and «на неделях 32 и⍽33»
got the label NBSP (section 2a item 8). About 50 sentence-level edits. Failure-mode labels «Как заметить:»
/ «Что делать:» were already in place; «целевой диапазон» already used.

Section 2a patterns appeared as expected (missing connectives, «в терминах», the contrast placed last).
Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 "X is when…" definitions

- «Совместное решение — это когда люди, которые несут издержки решения, принимают его вместе, а не когда
  собирают союзников…» → «Совместное решение принимают вместе те, кто несёт его издержки; это не сбор
  союзников…»
- (ch 41) «Спонсорство — это когда старший по положению человек пускает в ход своё влияние…» → «Спонсор —
  старший по положению человек, который пускает в ход своё влияние…»

### 1.2 One verb repeated for two inanimate subjects ("the plan decides…, the limit decides…")

- «План из главы 38 решает, как распределить ресурс…; лимит решает, сколько…» → «План из главы 38
  определяет, как распределить ресурс…; лимит — сколько…»

### 1.3 Detection fields as bare noun lists

- «Как заметить: вежливые кивки, ничего не меняется.» → «Как заметить: все вежливо кивают, но ничего не
  меняется.»
- «Что делать: каждое исключение — это замена, которую решает форум…» → «Что делать: считать каждое
  исключение заменой, которую решает форум…» (infinitive, like the other «Что делать:» fields)

### 1.4 «в терминах» inside tables and asides

Section 2a lists it for prose; this chapter had it four times, two in table cells.

- «Несите CFO доказательства в терминах финансов, а не услуги» → «Приносите CFO не услуги, а
  доказательства на языке финансов»
- «убеждение в их терминах» → «убеждение на их языке»

### 1.5 «когда» for English concessive "when"

- «почему у разработки „в работе всего три вещи“, когда совет директоров видит список из десяти
  ожидающих» → «…, хотя совет директоров видит…»

## 2. Two showcase paragraphs

### 2.1 Little's law in the portfolio

**Before.** [Закон Литтла](…), который объясняет глава 16, связывает средние величины: незавершённая
работа равна пропускной способности, умноженной на время в системе. Он точно выполняется для измеренных
данных за окно, которое начинается и заканчивается с пустой системой, и он описывает компромиссы, а не
разрешает их (…). […] Это **научный результат** (теорема); но предсказание того, что даст более низкий
лимит, вдобавок предполагает, что пропускная способность сохранится.

**After.** [Закон Литтла](…) (его объясняет глава 16) связывает средние величины: незавершённая работа
равна пропускной способности, умноженной на время в системе. Для измеренных данных он выполняется
точно, если окно начинается и заканчивается при пустой системе. При этом закон описывает компромиссы, а
не разрешает их (…). […] Это **научный результат** (теорема). Но чтобы предсказать, что даст более низкий
лимит, нужно ещё допустить, что пропускная способность сохранится.

### 2.2 Case: the one-on-one with Greg

**Before.** Ответ изменил саму задачу: потенциальному клиенту нужна была дата, на которую можно
положиться, и свидетельство того, что Northstar понимает его процесс согласования, а не готовое ПО к
неделе 36. […] Ещё директор предложил диапазон прогноза, который Greg сможет назвать на неделе 35, а
затем обсудил возможную замену с Rajiv, прежде чем кто-либо предложил её на встрече.

**After.** Ответ изменил саму задачу: потенциальному клиенту к неделе 36 нужно было не готовое ПО, а
дата, на которую можно положиться, и свидетельство того, что Northstar понимает его процесс
согласования. […] Ещё он предложил диапазон прогноза, который Greg сможет назвать на неделе 35, а затем,
ещё до того как кто-либо предложил замену на встрече, обсудил её с Rajiv.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| форум, которому принадлежит компромисс / портфель | «форум, который отвечает за этот компромисс», «форум, отвечающий за портфель» | "owns" calque; changed in objectives, the limit rules and the escalation section. The aphorism «директору принадлежат арифметика и процесс, а компромисс — тем, кто несёт издержки» kept |
| версия с подвигами | consider «героическая версия» or «ручной режим» | reads oddly in a table header; kept for consistency with notes-t15 |
| в терминах X | «на языке X» book-wide | calque; see 1.4 |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Enterprise application announces «четыре постоянных элемента»**, but five bold items follow (board,
   forum, named interfaces, interest map, relationship capital). Either the English counts four and the
   fifth is a separate point, or the count is off.
2. **CTO perspective, third point:** added «Поэтому» before «главными инструментами остаются…». Remove if
   the English does not link the peers' accountability to the choice of tools.
3. **Crawford et al.:** «участие сотрудников в нескольких командах сопровождалось более низкой
   результативностью подразделения» rendered «подразделения, где сотрудники участвовали в нескольких
   командах одновременно, работали хуже». Still correlational, but check that "lower unit performance" is
   not a narrower measure.
4. **Intro: «работу, которую не контролирует ни один человек»** rendered «которую ни один человек не
   контролирует целиком»; assumes "no single person controls".
5. **Case forecast:** «неделя 44, или недели 45–47 с учётом роста объёма» rendered «готово к неделе 44, а
   с учётом роста объёма… — к неделям 45–47»; assumes the weeks are completion dates.

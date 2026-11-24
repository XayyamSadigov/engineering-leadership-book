# Literary editing notes: chapter 36

File: `docs/parts/07-organization-design/36-reorganizations-evolution-and-succession.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (297
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, every heading, table line,
admonition line and Mermaid block are byte-identical (the info box body gained one NBSP, «Неделя⍽44»).
NBSP count 55 → 56: added «Неделя⍽44» and «1⍽040» (thousands separator was a plain space), removed the
misplaced one in «На неделе⍽44⍽директор». About 55 sentence-level edits; edited paragraphs re-wrapped at
about 105 characters. Failure-mode labels were already «Как заметить:» (no «Что делать:» field in this
chapter).

Section 2a patterns appeared as expected («На уровне высшего руководства…» opener, missing connectives).
Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Verbal noun as subject where Russian wants a clause

- «перемещение сорока человек за один шаг меняет линии подчинения…» → «если за один шаг переместить сорок
  человек, меняются линии подчинения…»
- «Перевод 12 задач экономит 24 инженеро-недели» → «Если 12 задач станут работой одной команды, это
  сэкономит 24 инженеро-недели»
- «Отмена всего проекта потребовала бы ещё 70 инженеро-недель» → «Отменить весь проект значило бы
  потратить ещё 70 инженеро-недель»

### 1.2 Question announced, then delayed to the end after a colon

- «На вопрос, ответ на который директору нужнее всего, исследования не отвечают: улучшает ли
  реорганизация поставку?» → «Главный для директора вопрос, улучшает ли реорганизация поставку,
  исследования оставляют без ответа.»

### 1.3 "X did not cause it" split from the claim it qualifies

- «Ошибка — на лидере. Люди, которые взяли на себя новые роли, её не вызвали, а руководителю…» → «Ошибка —
  на лидере, а не на людях, которые взяли на себя новые роли. Руководителю…» (two thoughts, two sentences).

### 1.4 Generic «ты»-forms and odd noun phrases

- «небольшими шагами не создашь» → «небольшими шагами не создать»
- «иллюстративную реорганизацию организации» → «иллюстративную реорганизацию из примера этой главы: в
  организации из 60 инженеров она…»
- «внезапная вакансия на которой» → «внезапное освобождение которой»

### 1.5 «является» in negated definitions

- «большинство симптомов… такими не являются» → «у большинства симптомов… причина не в структуре»
- «не является основной заменой для неё» → «не служит основной заменой на ней»

## 2. Two showcase paragraphs

### 2.1 Undoing a reorganization: the worked case

**Before.** Возьмём иллюстративную реорганизацию организации из 60 инженеров, разобранную в примере этой
главы: она перемещает 14 инженеров, стоит около 70 инженеро-недель и прогнозирует, что межкомандных задач
станет не 30, а 18 в квартал. Допустим, через два квартала их стало только 26, и большинство из этих 26
затрагивают один компонент, который новая граница разрезала пополам. Ответ — перенести этот компонент.
Отмена всего проекта потребовала бы ещё 70 инженеро-недель, чтобы вернуться к старой проблеме.

**After.** Возьмём иллюстративную реорганизацию из примера этой главы: в организации из 60 инженеров она
перемещает 14 инженеров, стоит около 70 инженеро-недель и, по прогнозу, сокращает число межкомандных задач
с 30 до 18 в квартал. Допустим, через два квартала их всё ещё 26, и большинство из этих 26 затрагивает один
компонент, который новая граница разрезала пополам. Ответ — перенести этот компонент. Отменить весь проект
значило бы потратить ещё 70 инженеро-недель, чтобы вернуться к старой проблеме.

### 2.2 CTO perspective

**Before.** На уровне высшего руководства вопрос смещается с того, как реорганизовываться, на то, как
часто и кто несёт затраты. Реорганизация каждого директора по отдельности разумна, а вместе они держат
инженеров в состоянии постоянного перехода.

**After.** На этом уровне вопрос уже не в том, как реорганизовываться, а в том, как часто это делать и кто
несёт затраты. По отдельности реорганизация каждого директора разумна, но вместе они держат инженеров в
состоянии постоянного перехода.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| просадка перехода / несоответствие | keep | clear in the list and the takeaways |
| «реорганизация квадратиков» (boxes-only) | keep | vivid and idiomatic |
| «У рекомендации книги три свойства» | «Рекомендация книги сводится к трём правилам» (applied) | the three items are rules, not properties |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«реорганизуйтесь, только если пройдены все три проверки»**: added «все» for clarity; it only makes
   the "all three" reading explicit. Remove if the English allows otherwise.
2. **«через два квартала их всё ещё 26»** (was «стало только 26»): assumes "only fell to 26".
3. **«консультации … укрепляют ощущение справедливости, ценность которого показывают те же данные»** (was
   «которое те же данные считают ценным»): assumes "the same evidence values" refers to the procedural
   justice findings.
4. **Takeaway on cover**: «нужны замена (готовая сейчас или временная) и преемник в развитии» merges
   "an interim or ready-now cover and a successor in development"; check no third condition was lost.
5. **Case, succession summary**: «По правилу покрытия покрыты только Orders, Payments and Integrations и
   Customer Experience, причём две из них — за счёт одного человека в обеих колонках.» By the table only
   Orders (Aisha) and Payments (the tech lead) have one person in both columns; CX has Hannah and Mateo.
   Consistent. But Payments' tech lead is also listed as developing for staff, data and integrations and
   becomes the Payments cover if Elena covers the director; check whether the English rule (no cover for
   two critical roles) should exclude Payments.

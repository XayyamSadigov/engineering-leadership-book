# Literary editing notes: chapter 34

File: `docs/parts/07-organization-design/34-spans-layers-and-dependency-mapping.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (NBSP
normalised); link targets, `{ #anchors }`, exercise labels, every heading, table line, admonition line and
Mermaid block are byte-identical. Two NBSPs disappeared because the sentences starting with a bare number
were rebuilt («77 инженеров под руководителями…», «15 связей с Platform Operations…»). Edited paragraphs
were re-wrapped at about 105 characters. About 55 paragraphs touched, plus the mental-model blockquote.
Failure-mode labels were already «Как заметить:».

Section 2a patterns appeared (missing connectives, «На уровне высшего руководства…» opener, which here also
collided with «уровни» in the next words). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 A sentence that opens with a bare number

English starts sentences with figures; Russian typography avoids it.

- «77 инженеров под руководителями и 3 staff-инженера составляют 80 инженеров Northstar.» → «Всего в
  Northstar 80 инженеров: 77 под руководителями и 3 staff-инженера.»
- «15 связей с Platform Operations — это запросы окружений…» → «Связи с Platform Operations (15) — это
  запросы окружений…»

### 1.2 «X расплачивается Y» for "X costs Y"

- «Узкий охват даёт время на коучинг и расплачивается уровнями» → «Узкий охват даёт время на коучинг, но
  за него платят уровнями»

### 1.3 Exercises phrased as evaluating people instead of their spans

- «Оцените шесть руководителей Northstar по пяти факторам охвата» → «Оцените охват шести руководителей
  Northstar … по пяти факторам»

### 1.4 Dangling infinitive after «ждёт»

- «оно ждёт ближайшей встречи этого руководителя … и времени, нужного, чтобы ввести его в курс дела» →
  «оно ждёт ближайшей встречи этого руководителя …, а потом ещё нужно время, чтобы ввести его в курс дела»

### 1.5 Typed-list conditions written as relative clauses ("Links where…, require…")

- «Связи, в которых другую команду просят сделать рутинную работу (…), требуют самообслуживания; связи, в
  которых по вашим причинам меняется логика другой команды, требуют решения…» → «Если другую команду
  просят сделать рутинную работу (…), нужно самообслуживание. Если по вашим причинам меняется логика
  другой команды, нужно решение…»

## 2. Two showcase paragraphs

### 2.1 Gallup data

**Before.** Опросные данные Gallup ближе всего к исследованию охвата у обычных руководителей, и вывод их
таков: талант руководителя важнее охвата. Для разработки существенны два результата. У руководителей
удалённых и гибридных команд больше подчинённых означало меньшую вовлечённость, а в офисе это почти не
влияло. А у руководителей, которые тратили на собственную исполнительскую работу больше медианных 40%
времени, вовлечённость была ниже, и в больших командах сильнее (…).

**After.** Ближе всего к исследованию охвата у обычных руководителей подходят опросные данные Gallup, и
вывод из них такой: талант руководителя важнее охвата. Для разработки существенны два результата. Первый:
в удалённых и гибридных командах больше подчинённых у руководителя означало меньшую вовлечённость, а в
офисе почти не влияло на неё. Второй: у руководителей, которые тратили на собственную исполнительскую
работу больше медианных 40% времени, вовлечённость была ниже, особенно в больших командах (…).

### 2.2 Step M2

**Before.** **M2** исправляет охват в Orders, но добавляет 4 связи и к тому же преуменьшает свою
стоимость: ниже порога в одну неделю около 58 мерж-реквестов за квартал меняли одновременно приём заказов
и правила ценообразования (глава 31). Каждый из них затрагивал бы двух владельцев.

**After.** **M2** исправляет охват в Orders, но добавляет 4 связи, причём подсчёт занижает его стоимость:
около 58 мерж-реквестов за квартал, каждый ниже порога в одну неделю, меняли одновременно приём заказов и
правила ценообразования (глава 31). После разделения каждый из них затрагивал бы двух владельцев.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| уровень управления / уровень высшего руководства | avoid «на уровне высшего руководства» in this chapter; use «для высшего руководства» | «уровень» is the chapter's term for layer; the opener made «на уровне … уровни» |
| уровень-передатчик | keep | compact and clear |
| переход (decision hop) | keep | works once glossed in the mental model |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Example: «ни один из шести охватов не попадает в диапазон»** (was «все шесть охватов выходят за
   диапазон»). Same meaning; noted only because the table then shows the range per factor, not per person.
2. **M2: «каждый ниже порога в одну неделю»**. Assumes "below the one-week threshold" applies to each merge
   request (each too small to count as a link), not to the total.
3. **Enterprise application: «новые руководители остаются без присмотра»**. If the English says "without
   support" or "without coaching", «без поддержки» is closer.
4. **Case table, M3 «−4 связи»** vs the example table (6 removed, 2 created): already flagged in notes-t11
   as net vs gross; a reader may stumble.
5. **Case: «трения между ними всегда разбирали только на уровне выше обоих руководителей»**. «на уровне»
   was added for readability; the meaning ("escalated above both managers") is unchanged.

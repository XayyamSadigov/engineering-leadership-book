# Literary editing notes: chapter 35

File: `docs/parts/07-organization-design/35-designing-organizations-at-four-scales.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (294
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, every heading, table line,
admonition line and Mermaid block are byte-identical. NBSP count 80 → 79: one misplaced NBSP removed
(«На неделе⍽44⍽директор» → «На неделе⍽44 директор», section 2a item 8). About 60 sentence-level edits;
edited paragraphs re-wrapped at about 105 characters. Failure-mode labels kept as «Признак:» (English
"Signal:") and «Как заметить:»; the chapter has no «Что делать:» field.

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives,
«На уровне высшего руководства…» as an opener, ambiguous «он»). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «стоит» + genitive as "costs" (sibling of ch 25 1.1 and ch 33 1.3)

This chapter prices everything in seats and weeks, so «стоит» appeared six times with a genitive object,
which Russian reads as "is worth" or as broken grammar.

- «каждый из них стоит места инженера» → «каждый из них обходится в одно место инженера»
- «Чего он стоит: лишнего перехода…» → «Во что он обходится: лишний переход…»
- «любой ответ на неё стоит автономии» → «любой ответ на неё оплачивается автономией»
- «Каждая перестройка стоит недель потерянного контекста» → «…обходится в недели потерянного контекста»

Grep: `стоит [а-я]+(а|я|ов|ей|ы)\b` in chapters about cost.

### 1.2 «Проект, который…» as subject of a conditional idea

English "A design that X does Y" was kept as a noun with a «который» clause; Russian wants «Если…».

- «Проект, который подходит только к одному из трёх входов, стоимость координации не убирает» → «Если
  проект подходит только к одному из трёх входов, он не убирает стоимость координации»
- «Проект, в котором появляются руководители руководителей, создаёт людей, которые делают эту работу
  впервые» → «Если в проекте появляются руководители руководителей, значит, появляются люди, которые
  делают эту работу впервые»

### 1.3 Calqued superlatives and qualities: «самый чистый довод», «тонкая база», «время» for "timing"

- «самый чистый довод в пользу ресурса» → «самый весомый довод за выделение ресурса»
- «Доказательная база здесь тонкая» → «…слабая»
- «Для высшего руководства главный вопрос — время» ("timing") → «главное — выбрать момент»

### 1.4 "X are Y, not Z" with the negated part trailing

- «Отметки 20, 50, 100 и 500 — это диапазоны, в которых…, а не пороги» → «…— не пороги, а диапазоны,
  в которых…» (the contrast first, before the long clause).
- «Это выбор, связанный с ландшафтом…, а не целевое значение» → «Эта доля — не целевое значение, а выбор,
  продиктованный ландшафтом…»

### 1.5 «Он» after a sentence with two masculine candidates

- «…проект организации второго года для Victor Lindqvist (CTO). Он должен вступить в силу на неделе 53» →
  «…Проект должен вступить в силу…»

## 2. Two showcase paragraphs

### 2.1 Why this matters, executive level

**Before.** Для высшего руководства главный вопрос — время. Структуры, которые нужны организации из
500 человек, при 50 становятся накладными расходами, а структуры, работающие при 50, при 500 не
выдерживают. Если уровни управления и платформенные группы добавить слишком рано, получится механизм,
который никому не нужен. Если слишком поздно, руководители будут целыми неделями маршрутизировать работу.

**After.** Для высшего руководства главное — выбрать момент. Структуры, которые нужны организации из
500 человек, при 50 превращаются в накладные расходы, а те, что работают при 50, при 500 не выдерживают
нагрузки. Если уровни управления и платформенные группы добавить слишком рано, получится механизм,
который никому не нужен. Если слишком поздно, руководители будут неделями заняты маршрутизацией работы.

### 2.2 Evidence on numbers

**Before.** Популярные ограничения размера группы, заимствованные из антропологии, взяты не из
исследований софтверных организаций, и книга ими не пользуется. Доказательная база здесь тонкая. Отметки
20, 50, 100 и 500 — это диапазоны, в которых практики обычно сообщают об одних и тех же поломках, а не
пороги (…).

**After.** Популярные пределы размера группы пришли из антропологии, а не из исследований софтверных
организаций, и книга ими не пользуется. Доказательная база здесь слабая. Отметки 20, 50, 100 и 500 — не
пороги, а диапазоны, в которых практики обычно сообщают об одних и тех же поломках (…).

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| «Признак:» / «Как заметить:» (Signal / Detection) | keep for this chapter | the brief fixes «Как заметить:»/«Что делать:» book-wide; this chapter's English uses a different pair, so «Признак:» stays for Signal |
| проект организации второго года | allow «проект организации на второй год» in prose | the genitive «второго года» reads as "of the second year's organization"; changed in the opening and the case |
| маршрутизировать (route work) | keep | reads technical but clear to engineers; «распределять» would lose the "pass through a person" sense |
| сбор отдачи (harvest) | keep | works with the English gloss |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Fernwick: «подчиняются CTO (техническому директору) и сооснователю, который…»** read as two people
   with a singular «который». Rendered as one person («CTO — сооснователю компании, который…»). If the
   English means two people ("the CTO and a co-founder"), revert.
2. **«дежурит по всему»** rendered «дежурит за всю систему»; assumes "is on call for everything".
3. **Case, «Уровень (D) ответил бы на поломку, которую пока не наблюдали: руководители получают…»**:
   added «ведь» so the colon clause reads as the evidence that the breakage is absent. Remove if the
   English does not link them.
4. **Opening: «какие команды существуют»** changed to «какие будут команды», assuming "which teams exist"
   refers to the designed state.
5. **Площадки: «или в пересекающихся рабочих часах»** rendered «или в часовых поясах с общими рабочими
   часами»; assumes "overlapping working hours".

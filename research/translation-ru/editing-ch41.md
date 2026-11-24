# Literary editing notes: chapter 41

File: `docs/parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.ru.md`. Edited
from the Russian text only; the English chapter was not opened. The file was not yet committed, so the
pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numbers (`grep -oE '[0-9][0-9 ,.]*'`, trailing
separators stripped) is identical before and after (272 digit tokens); headings, `{ #anchors }`, link
targets, exercise labels, admonition lines, every table line and both Mermaid blocks are byte-identical.
NBSP count 72 → 73: «на неделях 25\nи⍽26» became «на неделях⍽25 и⍽26» (section 2a item 8). About
55 sentence-level edits. Failure-mode field is «Как заметить:» (the chapter has no «Что делать:»).

The translation was accurate and clean; section 2a patterns appeared as expected (missing connectives,
English word order, «the X is the Y, not Z» with the negation trailing). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Tautology from an English adjective and verb with one root

- «Если удастся предотвратить один предотвратимый уход в год» → «Если удастся избежать одного
  предотвратимого ухода в год»

### 1.2 A term that begins with a preposition, after the same preposition

«встреча через уровень» collides with «через» used as "by means of".

- «Через встречи через уровень проверяйте канал руководителя» → «Встречами через уровень проверяйте
  канал руководителя»

### 1.3 "belongs to" / "owns" for rights and responsibilities

- «никогда о причинах: причины принадлежат руководителю» → «никогда о причинах: говорить о них вправе
  только сам руководитель»
- (same in ch 42: «форум, которому принадлежит компромисс» → «форум, который отвечает за этот компромисс»)

### 1.4 English verbless headline sentences opening a paragraph

- «Во что директору обходится такая работа с шестью руководителями.» → «Посчитаем, во что директору
  обходится такая работа с шестью руководителями.»
- «Что это может дать.» → «Что это может дать?»

### 1.5 A parenthetical gloss that separates a number from its noun

- «[Метаанализ](…) (исследование, которое объединяет результаты многих исследований) 24 лонгитюдных
  исследований показал» → «[Метаанализ](…) (так называют исследование, которое объединяет результаты
  многих исследований) по 24 лонгитюдным работам показал»

### 1.6 Abstract "decision about X" as subject or predicate

- «Вывести руководителя из роли — решение о соответствии роли. Принимают его, только когда…» → «Снять
  руководителя с роли — значит решить, что роль ему не подходит. Такое решение принимают, только когда…»
- «Риск регулирует уровень контроля, а не размер решения.» → «Риском управляют через уровень контроля, а
  не через масштаб решения.»

## 2. Two showcase paragraphs

### 2.1 Mental model, after the diagram

**Before.** Петля начинается с письменных ожиданий: оценка по ожиданию, которое никто не высказал,
говорит больше о директоре, чем о руководителе. Заканчивается она перепроверкой, потому что план, который
никто не проверяет, превращается в просто документ. Вторая идея: развивать руководителей и строить
резерв — одна и та же работа. У руководителя, сильного в росте людей, есть люди, способные взять на себя
больше его работы. Место, где такого человека нет, — одновременно пробел в развитии и пробел в
преемственности.

**After.** Петля начинается с письменных ожиданий: оценка по ожиданию, которое никто не высказал,
говорит больше о директоре, чем о руководителе. Заканчивается она перепроверкой, потому что план без
проверки остаётся просто документом. Вторая идея: развивать руководителей и строить резерв — одна и та
же работа. Если руководитель силён в росте людей, рядом с ним есть те, кто способен брать на себя всё
больше его работы. Если такого человека нет, это сразу два пробела: в развитии и в преемственности.

### 2.2 Research on leadership training

**Before.** Метаанализ 335 выборок нашёл улучшения от умеренных до больших в реакциях участников,
усвоенном, поведении на работе и результатах. […] Обучение работало лучше, когда ему предшествовал
анализ потребностей, когда в нём была обратная связь и несколько методов (особенно практика), а занятия
были разнесены во времени, проходили на территории компании и очно (…). Этот **научный результат** в
изложении аннотации касается формальных программ, а не коучинга со стороны директора. Но и он говорит
против одного выездного курса из каталога.

**After.** Метаанализ 335 выборок обнаружил улучшения от умеренных до больших: в реакции участников, в
усвоенном материале, в поведении на работе и в результатах. […] Обучение работало лучше, когда ему
предшествовал анализ потребностей, когда в программу входили обратная связь и несколько методов
(особенно практика), а занятия разносили во времени и проводили очно, на территории компании (…). Этот
**научный результат** (в изложении аннотации) касается формальных программ, а не коучинга со стороны
директора. Но и он говорит против того, чтобы ограничиться одним выездным курсом из каталога.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| встреча через уровень | keep; never put «через» (by means of) right before it, use the instrumental | collision shown in 1.2 |
| практическая работа (hands-on work, Priya) | consider «собственная инженерная работа» or «работа руками» | «практическая» also reads as "practice" in a chapter where practice is a training method |
| «Нет данных» as «вывод об информации директора» | «вывод о собственной осведомлённости директора» | "information" as an object of a finding is a calque |
| резерв vs «скамейка» (learning-roadmaps.ru) | align on «резерв» | already noted in notes-t15 |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Mental model: «доходят через других людей»** rendered «достигаются руками других людей»; assumes
   "delivered through other people".
2. **«новый руководитель может появиться, только если чьё-то инженерное место останется без замены»**
   (was «за счёт инженерного места, на которое не нанимают замену»); assumes "only by not backfilling an
   engineering seat".
3. **Trade-offs: «Вакансия без замены обходится дороже и наступает без предупреждения»** rendered «Но
   место, оставшееся без замены, обходится дороже, и освобождается оно без предупреждения»; added «Но».
   Check that the English contrasts an uncovered vacancy with the bench cost.
4. **CTO perspective: «Если у CTO все руководители оценены как „Уверенно“»**: unclear whether the ratings
   are the directors' or the CTO's own. Kept the ambiguity.
5. **Playbook 3: «по её письменному правилу»** rendered «по письменному правилу из той же главы»; assumes
   "its" refers to the chapter 40 rotation.

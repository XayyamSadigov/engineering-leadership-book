# Literary editing notes: chapter 57

File: `docs/parts/13-advanced-problems/57-crises-executive-disagreement-and-resistance.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the multiset of numeric tokens is identical before and after (NBSP
normalised, and digit runs compared separately); link targets, citation link texts, `{ #anchors }`, heading
lines, exercise labels, admonition lines, every table line and all four Mermaid blocks are byte-identical.
No wrapped line starts with a number and a period. About 50 sentence-level edits. NBSP 73 → 71: two NBSPs
that glued a number to the following word were removed («Недели⍽41–49⍽первого» → «Недели⍽41–49 первого»,
«40⍽за второй год»). The only Failure Modes field is «Как заметить:».

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives,
English word order, «который» chains). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 A passive outcome attached to the wrong subject ("disagreement… then committed or escalated")

The English attaches "commit" and "escalate" to the disagreement; Russian cannot "support" a disagreement.
Give the actions back to the person.

- «чтобы несогласие прозвучало один раз и ясно, а потом было либо поддержано, либо эскалировано» →
  «чтобы несогласие прозвучало один раз и ясно, после чего вы либо поддерживаете решение, либо эскалируете
  вопрос»
- «Если и поддержка, и эскалация исчерпаны» → «Если ни поддержка, ни эскалация не помогли»

### 1.2 "This book" vs a cited book in the same paragraph

After a paragraph about Hirschman's book, a bare «книга» reads as Hirschman's.

- «Для директора… книга добавляет третий, худший вариант, которого у Hirschman нет» → «…эта книга
  добавляет…»

### 1.3 Three «который»-portraits in a row ("A VP who…, a CTO who…, a director who…")

Vary the form: one relative clause, one past participle, one present participle; and put the new
information (what they teach) at the end.

- «CTO, который наказывает несогласного директора, учит…» → «CTO, наказавший несогласного директора,
  учит…»
- «Директор, который называет возражения „сопротивлением“, учит руководителей молча выдавать исключения
  вместо того, чтобы возражать» → «Директор, называющий возражения „сопротивлением“, учит руководителей не
  возражать, а молча выдавать исключения»

### 1.4 Mixed «мы» and «вы» in a checklist

- «…чем мы сами ему способствовали, что изменило бы наше мнение…» (in a «вы» book) → «…чем вы сами ему
  способствовали, что изменило бы ваше мнение…»

### 1.5 A plan or a statement as the subject of a human act ("A plan that… heard no one")

- «План, в котором нельзя указать ни одного изменения, сделанного из-за возражения, никого не услышал» →
  «Если в плане нельзя указать ни одного изменения, сделанного из-за возражения, значит, никого не
  услышали»
- «одно заявление Halvard, обвиняющее партнёра, и другое, признающее собственную причину» → «два заявления
  Halvard: одно обвиняло партнёра, другое признавало, что причина на стороне самой Halvard»

## 2. Two showcase paragraphs

### 2.1 The CTO in the escalation chain

**Before.** В вопросах несогласия CTO находится в середине цепочки эскалации. Вверх его долг высказывать
несогласие обращён к CEO на встрече высшего руководства, а в вопросах честности, и только в них, — к совету
директоров через его комитет по аудиту. Вниз реакция CTO на несогласие директора задаёт климат для
высказываний во всей организации.

**After.** В вопросах несогласия CTO находится в середине цепочки эскалации. Наверх CTO высказывает
несогласие перед CEO на встрече высшего руководства, а в вопросах честности, и только в них, — перед
советом директоров через его комитет по аудиту. А вниз по цепочке климат для высказываний во всей
организации задаёт то, как CTO реагирует на несогласие директора.

### 2.2 Commitment versus conscience

**Before.** **Поддержка против совести.** Поддержка решений, против которых вы выступали, — то, на чём
держится команда высшего руководства; поддержка всего подряд обесценивает ваше несогласие. Граница между
ними — планка, и поэтому её нужно записать до спора.

**After.** **Поддержка против совести.** На поддержке решений, против которых вы выступали, держится
команда высшего руководства; но если поддерживать всё подряд, ваше несогласие обесценивается. Граница
проходит по планке, поэтому её и нужно записать до спора.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| бридж / бридж инцидента | keep; unify with «созвон» (notes-t19, ch50) book-wide | the failure mode «Руководитель на бридже» itself says «подключается к созвону по инциденту»; both read fine once glossed |
| трактовка (сопротивления) | keep | natural, and distinct from «интерпретация» of data |
| молчаливое подчинение / мнимая поддержка | keep both | the first is the concept, the second the failure-mode name; they do not collide |
| высказывание (voice) | keep | in the table header «Форма» it reads well next to «уход», «молчание» |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«Команде высшего руководства стоит знать свои обязанности до того, как этот день наступит»**:
   "this day" has no clear antecedent (the four-day SEC window?). Rendered «заранее, до того как такой день
   наступит». Check the English.
2. **«Сопротивление часто отчасти создаёт сам инициатор…, и оно может быть ресурсом»** rendered «нередко
   отчасти создаёт…, и к тому же оно может быть ресурсом». Assumes two separate claims (Ford et al.).
3. **«Если и поддержка, и эскалация исчерпаны… открыто его принять или уйти»** rendered «Если ни
   поддержка, ни эскалация не помогли». Assumes "exhausted" means "tried and failed"; «открыто его
   принять» (accept openly) kept as is, though the takeaways say the same.
4. **Greg Tanaka: «Выполняет ли разработка это обещание — вот что может превратить его сопротивление в
   поддержку»** rendered «Если разработка будет его выполнять, сопротивление Greg может смениться
   поддержкой». Same modality ("could"); check nothing stronger is meant.
5. **Counter-proposal: «с отчётом вместе с аудитом серьёзности»** rendered «с отчётностью вместе с аудитом
   серьёзности». Assumes "reported alongside the severity audit".
6. ch57 Decision Framework still says «три таблицы» while the second and third tools are a diagram and a
   paragraph (already noted in notes-t23); not changed.

# Literary editing notes: chapter 43

File: `docs/parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.ru.md`. Edited
from the Russian text only; the English chapter was not opened. The file was not yet committed, so the
pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (223
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition blocks and Mermaid
blocks are identical. Changed outside prose: one table header («Слито задач» → «Смёржено задач», per the
Northstar pages) and one heading text, anchor kept («Закрепление: чтобы так просто работали» →
«Закрепление: сделать новое обычным порядком работы»). About 75 paragraph-level edits; edited paragraphs
re-wrapped at about 105 characters. Failure Modes keep «Как заметить:» (the chapter has no «Что делать:»
field). NBSPs added after label words where missing (квартале⍽3, главе⍽42, неделе⍽37).

The translation was accurate. Section 2a patterns appeared as expected (missing connectives, «который»
attached to the wrong noun, English word order). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Echoes and tautologies carried over from English wordplay

- «руководитель меняет практику просто тем, что её меняет» → «руководитель меняет практику напрямую»
- «Каждый блок обходится дёшево по сравнению с изменением, которое организация обходит стороной» (обходится /
  обходит; «блок» is diagram vocabulary) → «Любой из этих шагов дешевле изменения, которое организация
  обходит стороной»

### 1.2 Enumerations that mix noun phrases, clauses and «нет X»

English lists of failures came through with a different syntax in every item.

- «слишком слабое ощущение срочности, нет сильной направляющей коалиции, нет запланированных быстрых
  побед, победу объявляют слишком рано, а изменение не закрепляют в культуре» → one clause per item,
  separated by semicolons: «…срочности; нет сильной направляющей коалиции; не запланированы быстрые
  победы; победу объявляют слишком рано; изменение не закрепляют в культуре»

### 1.3 Paired superlatives calqued from "best placed … worst placed"

- «директор лучше всех может запустить общее изменение и хуже всех видит, как оно приживается» →
  «запустить общее изменение директору проще, чем кому-либо, а увидеть, как оно приживается, — труднее
  всех»

### 1.4 Double «а» in one sentence pair

- «Если нет, у вас слушатели. А слушатели на словах докладывают о выполнении, а несогласие выражают
  обходными путями.» → «Если нет, у вас слушатели. Слушатели докладывают, что всё выполняется, а
  несогласие выражают обходными путями.»

### 1.5 "Read as" and other perception verbs taken literally

- «другие могут прочитать это как фаворитизм» → «остальные могут воспринять это как фаворитизм»
- «Если пройти по петле, получается вот что. Диагнозом был ресурс» → «Если пройти по петле, картина
  такая. Диагноз гласил, что не хватает ресурса»

## 2. Two showcase paragraphs

### 2.1 Why this matters, organization level

**Before.** **В организации** директор лучше всех может запустить общее изменение и хуже всех видит, как
оно приживается. Каждое изменение отнимает у руководителей внимание, а это самый дефицитный ресурс
организации. Если директор запускает изменения быстрее, чем руководители успевают их усвоить, он получает
согласие на встречах и обходные пути в работе.

**After.** **В организации** запустить общее изменение директору проще, чем кому-либо, а увидеть, как оно
приживается, — труднее всех. Каждое изменение отнимает внимание руководителей, самый дефицитный ресурс
организации. Если запускать изменения быстрее, чем руководители успевают их усвоить, на встречах директор
получит согласие, а в работе — обходные пути.

### 2.2 Recovering credibility: the research

**Before.** Доверие руководителей складывается из выполненных обещаний и тратится на нарушенные, а
провалившаяся инициатива тратит его много и сразу. Исследования восстановления доверия дают один вывод,
которым директор может воспользоваться. В двух экспериментальных исследованиях доверие лучше
восстанавливалось, когда сторона извинялась за нарушение, связанное с компетентностью, и отрицала вину за
нарушение, связанное с честностью. […] Речь в этих исследованиях идёт о предполагаемом нарушении, а не о
провалившемся проекте руководителя, так что перенос — вывод этой книги.

**After.** Доверие руководителей копится с каждым выполненным обещанием и тратится с каждым нарушенным, а
провалившаяся инициатива расходует его много и сразу. Из исследований восстановления доверия директор
может взять один вывод. В двух экспериментальных исследованиях доверие восстанавливалось лучше, если за
нарушение, связанное с компетентностью, сторона извинялась, а за нарушение, связанное с честностью,
отрицала вину. […] Эти исследования касаются предполагаемого нарушения, а не провалившегося проекта
руководителя, поэтому перенос их выводов на директора — умозаключение этой книги.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| слитые задачи (merged) | «смёржено», applied in the table header and prose | unify with the Northstar pages, as the notes-t16 translator suggested |
| новая практика ревью замедляет слияния | «замедляет мёржи», applied | same family as «смёржено» |
| носители (carriers) | keep | works once introduced; needs the framing «в этой главе её участники называются носителями» |
| эскалация приверженности | keep | the chapter explains the choice; reads well |
| показатель активности | keep | clear |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **X1: «На этом совещании Amara Okafor уже назвала Excellence Day „потерянной неделей“».** The original
   «где Amara … уже назвала его» had an ambiguous «его» and «где». Read as: Amara said it at (or in the
   forum of) the CTO's staff meeting. If she said it elsewhere, rephrase.
2. **Launch: «Правила: никаких встреч…»** added the frame word «Правила:» to a verbless list; no new
   content.
3. **Diagnosis: «один день раз в четыре недели»** (was «один день из четырёх недель»). Same fact,
   assuming "one day in four weeks".
4. **Self-assessment: «Записка подтолкнула директора проверить по хронике года⍽1, какие типичные провалы
   были в кварталах⍽1 и⍽2»** (was «проверить кварталы 1 и 2 на типичные провалы»). Wording only.
5. **«Поэтому проверкой служит просмотр списка обязательств руководителем»**: «Поэтому» added to link the
   self-judged verdicts to the check. Remove if the English does not connect them.
6. **Trade-offs: «признав ошибку, они ослабят свои позиции»** for "admitting failure will weaken them";
   «авторитет» in the heading keeps the sense.

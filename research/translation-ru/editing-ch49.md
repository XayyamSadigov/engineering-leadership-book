# Literary editing notes: chapter 49

File: `docs/parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.ru.md`. Edited
from the Russian text only; the English chapter was not opened. Pre-edit copy: `git show ru-wip:<file>`.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to the `ru-wip` copy (420
tokens, NBSP normalised); `{ #anchors }`, link targets, exercise labels, admonition lines, every table line
and both Mermaid blocks are byte-identical; NBSP count 123 → 123; no wrapped line starts with a number and a
period. About 80 sentence-level edits; no heading text changed. Failure-mode field is «Как заметить:» only
(the chapter has one field per entry, as in notes-t19).

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives,
English word order, «На уровне…» openers). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «Стоило ли это X» read as "was it worth X"

Same family as editing-ch25 pattern 1.1, but with the genitive: «стоило поддержки» reads as "deserved / was
worth the support", not "cost the support".

- «Стоило ли это поддержки Greg, неизвестно.» → «Не лишился ли он из-за этого поддержки Greg, неизвестно.»

Grep later chapters for «стоило (ли) … + genitive» used as "cost".

### 1.2 Parallel "A program that asks X… A program that asks Y…" subjects

English contrasts two hypothetical programs as subjects; Russian repeats «Программа, которая просит» twice
and loses the contrast. Turn them into two conditions.

- «Программа, которая просит сразу два года, просит руководителей… Программа, которая просит полгода, …
  просит их судить…» → «Если программа просит сразу два года, она просит руководителей… Если она просит
  полгода, …, то предлагает им судить…»
- «CFO, которому показали $1,27 млн, прочитает… Руководитель продаж, которому показали «$250 000», не
  заметит…» → «Если CFO увидит $1,27 млн, он прочтёт… Если руководитель продаж увидит «$250 000», он не
  заметит…»

### 1.3 Tense mismatch inside a joined predicate (future + past)

- «Он одобрит $150 000, только если их компенсирует экономия…, и спросил, когда программа закончится.» →
  «…($4,2 млн). Ещё он спросил, когда программа закончится.»

### 1.4 Gloss-style "X is Y, not Z" where Z is the reader's assumption

Put the denied assumption first, so the sentence ends on the new information.

- «Критерии выхода — это условия, при которых…, а не дашборд программы.» → «Критерии выхода — не дашборд
  программы, а условия, при которых…»

### 1.5 Ambiguous «её / его» after an embedded "program" clause

- «удержит ли её команда руководителей в плохой квартал» (её = программа or команда?) → «не откажется ли
  от неё команда руководителей в плохой квартал»
- «Встраивать преемственность в критерии выхода программы, чтобы она не зависела от своего спонсора» (она
  = преемственность?) → «…, чтобы программа не зависела от спонсора»

## 2. Two showcase paragraphs

### 2.1 Why the cost table misleads

**Before.** Итоговая сумма сама по себе вводит в заблуждение. Численность не растёт, поэтому $1 017 500
ресурса — это выбор того, чем займутся уже работающие инженеры, и платят за него несделанной работой по
дорожной карте. Операционные расходы меняют только $250 000 на инструменты. CFO, которому показали
$1,27 млн, прочитает это как новые деньги. Руководитель продаж, которому показали «$250 000», не заметит,
что 6 инженеров — это 7,5% из 80. Поэтому предложение показывает обе строки всем.

**After.** Сама по себе итоговая сумма вводит в заблуждение. Численность не растёт, поэтому $1 017 500
ресурса — это выбор того, чем займутся уже работающие инженеры, а платят за этот выбор работой по дорожной
карте, которая не будет сделана. Операционные расходы меняются только на $250 000 — на инструменты. Если
CFO увидит $1,27 млн, он прочтёт это как новые деньги. Если руководитель продаж увидит «$250 000», он не
заметит, что 6 инженеров — это 7,5% из 80. Поэтому предложение показывает обе строки всем.

### 2.2 The success paradox

**Before.** **Парадокс успеха.** Первый этап снимает видимую боль. В Northstar сервисные кредиты (…) упали
с $410 000 в базовом квартале до $95 000 в квартале 2, а за оставшейся работой не стоит ни одного сбоя.
Kotter известен предупреждением не объявлять победу слишком рано (…). В многолетней программе это
выглядит как бюджетный цикл, в котором никто ничего не объявляет, а выделенный ресурс сокращается.

**After.** **Парадокс успеха.** Первый этап снимает видимую боль. В Northstar сервисные кредиты (…) упали
с $410 000 в базовом квартале до $95 000 в квартале 2, а оставшуюся работу не подкрепляет ни один сбой.
Kotter известен предупреждением не объявлять победу слишком рано (…). В многолетней программе
преждевременная победа выглядит иначе: никто ничего не объявляет, просто в очередном бюджетном цикле
выделенный ресурс сокращается.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| финансирующие | keep | compact; reads well after the first context («встреча с теми, кто финансирует») |
| «готов сейчас / готов после развития» | keep in quotes when used as a readiness label | in the stage-3 criterion the bare words read as ordinary adjectives; quotes added |
| задание на развитие «с реальными ставками» | «где на кону реальный результат» | «ставки» collides with the book term «ставка» (bet) used throughout this chapter |
| обмен (Yukl's exchange tactic) | «обмен услугами» | bare «обмен с вышестоящими» is unclear; the next sentence already says «не обменивайтесь услугами» |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«программа, вероятно, неверно определила этап»** (was «ошиблась этапом»). Assumes the English says the
   program misjudged which stage it is in or what the stage needs; if it means "is in the wrong stage",
   rephrase.
2. **«оставшуюся работу не подкрепляет ни один сбой»** (was «за оставшейся работой не стоит ни одного
   сбоя»). Assumes "no outage attached to the remaining work", i.e. no fresh pain argues for it.
3. **Page one, «скользящая сумма инцидентов показывает, что за второй год мы уложимся в 40»** (was «идёт к
   тому, чтобы… не превысить 40»). Assumes "on track to stay at or under 40".
4. **Case, «По доступности цель не достигнута: простой за квартал оказался примерно на 13 минут больше
   допустимого»** (was «Доступности не хватило примерно 13 минут простоя за квартал», which reads as if the
   system lacked downtime). Check the English says the quarter missed 99.9% by about 13 minutes.
5. **«релизы стали меньше, но не безопаснее»** kept. If the English says "fewer" rather than "smaller", the
   Russian is ambiguous either way; if "smaller", «мельче» would be sharper.
6. **«Поэтому его первый абзац говорит…»** ("Сначала запрос"): «Поэтому» added, linking "a proposal asks for
   a decision" to "the first paragraph states the ask". Remove if the English keeps them unlinked.

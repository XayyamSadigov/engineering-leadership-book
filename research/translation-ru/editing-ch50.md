# Literary editing notes: chapter 50

File: `docs/parts/12-cto-leadership/50-what-a-cto-actually-does.ru.md`. Edited from the Russian text only;
the English chapter was not opened. Pre-edit copy: `git show ru-wip:<file>`.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to the `ru-wip` copy (269
tokens, NBSP normalised); `{ #anchors }`, link targets, exercise labels, admonition lines, every table line
and both Mermaid blocks are byte-identical; NBSP count 42 → 42; no wrapped line starts with a number and a
period. About 70 sentence-level edits; no heading text changed (the H1 «Чем на самом деле занимается CTO»
matches the nav and is a legitimate use of «на самом деле»). Failure-mode fields: «Признак:» everywhere,
plus one «Как заметить:» (shadow architect), as in notes-t19.

Section 2a patterns appeared as expected («На уровне…» openers, missing connectives). Only new patterns
follow.

## 1. Patterns new beyond section 2a

### 1.1 Plural pronoun for a singular role ("CTOs … their time")

English generic plural survives as «они» after a singular «CTO».

- «Большинство провалов CTO — это провалы в том, как они распоряжаются собственным временем.» →
  «Большинство провалов CTO сводится к тому, как он распоряжается собственным временем.»
- «вердикт в коридоре, который отменяет дизайн команды, или стратегия, объясняющая, почему их сервис…» →
  «…отменяет её дизайн, или стратегию, объясняющую, почему её сервис…»

### 1.2 "Delegated to no one" and other English negative objects

- «CTO, у которого на стратегию уходит 4% недели, делегировал стратегию никому.» → «…по сути отдал
  стратегию в никуда.»
- «Пустая клетка допустима, только если она записана как пустая.» → «…только если её оставили пустой
  намеренно и это записано.»

### 1.3 "X is its audit" / "the role is a residual": a noun predicate where Russian wants a verb

- «делегирование — главный инструмент…, а календарь — его аудит» → «…, а календарь позволяет проверить
  результат»
- «Архетипы описывают, что осталось в конкретной компании; это не типы личности.» → «Архетипы описывают
  этот остаток в конкретной компании, а не типы личности.»
- «Но повторяющееся решение касается отдельного запроса: остаётся ли он у CTO?» → «Но снова и снова решать
  приходится другое: оставить ли у CTO конкретный запрос?»

### 1.4 "Looks absent / looks resistant": adjectival participles as predicates

- «Тот, кто остаётся внутри…, выглядит сопротивляющимся.» → «Если же он остаётся внутри, хотя CEO попросил
  больше внешней работы, кажется, что он сопротивляется.»

### 1.5 Count words carried over from English plurals («большую часть утр»)

- «CTO проводит большую часть утр на дизайн-ревью и единственный утверждает…» → «CTO почти каждое утро
  проводит на дизайн-ревью, и только он утверждает…»

## 2. Two showcase paragraphs

### 2.1 Why this matters, executive scale

**Before.** На уровне высшего руководства CTO — единственный технолог за столом, где решают, куда пойдут
деньги компании, какие риски она примет и в каком направлении будет двигаться. CTO, который тратит это
место на защиту интересов разработки или проводит всю неделю внутри разработки, оставляет компанию без
технического суждения. Большинство провалов CTO — это провалы в том, как они распоряжаются собственным
временем.

**After.** В высшем руководстве CTO — единственный технолог за столом, где решают, куда пойдут деньги
компании, какие риски она примет и в каком направлении будет двигаться. Если CTO тратит это место на защиту
интересов разработки или всю неделю проводит внутри неё, компания остаётся без технического суждения.
Большинство провалов CTO сводится к тому, как он распоряжается собственным временем.

### 2.2 Delegation that holds

**Before.** Лекарство от обоих провалов — опубликованный список классов решений, у каждого из которых есть
владелец. Затем CTO в течение квартала перенаправляет каждый запрос, пришедший не по адресу, причём каждый
раз. Это должно стать привычкой, потому что управленческая работа состоит из коротких, раздробленных и
устных эпизодов (…). Большинство решений доходят до CTO в виде двухминутного вопроса в чате…

**After.** Лекарство от обоих провалов — опубликованный список классов решений, у каждого из которых есть
владелец. А затем целый квартал CTO перенаправляет каждый запрос, пришедший не по адресу, без исключений.
Перенаправление должно стать привычкой, ведь управленческая работа состоит из коротких, раздробленных и
устных эпизодов (…). Большинство решений доходит до CTO в виде двухминутного вопроса в чате…

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| контроли (SOC 2 gloss) | «меры контроля» | aligns with the chapter's own «меры контроля» (notes-t19); applied |
| высший менеджер (org builder) | «высший руководитель» | «менеджер» is not the book's word for a role; applied |
| «нефильтрованный сигнал» | «сигнал без фильтров» | calque; applied |
| вердикт | keep | works well and keeps «решение» free (pattern 6 of section 2a) |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«Решение, возвращённое один раз, — это одолжение»** kept. Unclear whom the favour is to (the asker or
   the owner); if the English says returning once "is a courtesy", the Russian is fine.
2. **Halvard: «ущерб от него в шесть раз масштабнее»** (was «наносит ущерб в шесть раз большего масштаба»).
   Assumes "six times the blast radius"; check whether "six" refers to the groups (five VP groups) or a
   separate multiplier.
3. **«организация начинает работать так же долго, как он»** (was «организация перенимает его часы»).
   Assumes "the organization copies the executive's hours"; if the English means his habits more broadly,
   use «перенимает его режим».
4. **«даёт направлению своё место»** for the monthly technical-direction review, and «Техническое
   направление задают семь principal-инженеров…» (was «идёт через»). Assumes direction is set by them, not
   merely routed through them.
5. **Fournier reference, «прослеживает управленческую карьеру»** (was «проходит управленческий трек»), still
   with the book as subject as notes-t19 describes.

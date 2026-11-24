# Literary editing notes: chapter 23

File: `docs/parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (247 tokens,
NBSP normalised); `{ #anchors }`, link targets, exercise labels, admonition types, every table line and all
Mermaid blocks are byte-identical. One NBSP removed from the wrong side («квартале⍽19» → «квартале 19⍽из⍽30»:
19 is a count, not a label). Failure-mode labels were already «Как заметить:» / «Что делать:».

The wave-1 text was clean in vocabulary and terms; about forty sentences rebuilt. Section 2a patterns appeared
as expected (missing connectives, signposts before an enumerated list). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Tautological subject-predicate pairs ("A waiting change is an unintegrated change")

English definitional identities come through as «X-ющее изменение — это не-Y изменение». Turn them into a
condition or a clause.

- «Ждущее изменение — это неинтегрированное изменение, поэтому ветки живут дольше.» → «Пока изменение ждёт,
  оно не интегрировано, поэтому ветки живут дольше.»
- «Повторное развёртывание предыдущего артефакта работает, только если…, а миграции — обычная причина, по
  которой это не так.» → «Вернуться к предыдущему артефакту можно, только если…, а совместимость обычно
  ломают миграции.»

### 1.2 Bookkeeping verbs from the English authoring layer ("the rule this chapter owns")

"Owns" in the sense of the book's ownership map leaked into prose.

- «Правило, которым владеет эта глава, — сначала отменить» → «Эта глава вводит правило сначала отменить»

### 1.3 "X is the failure that Y prevents" with the incident as subject

The incident id plus a «когда…» clause in subject position delays the predicate.

- «INC-419, когда миграция выполнилась раньше рассчитанного на неё кода, — как раз тот сбой, от которого
  защищает эта дисциплина.» → «Именно от такого сбоя она защищает: в INC-419 миграция выполнилась раньше
  кода, который на неё рассчитывал.»
- «Аргумент за строку о контрактах — INC-405, когда…» → «Строку о контрактах обосновывает INC-405, когда…»

### 1.4 Paper or source as the agent of a verb chain («Статья рассматривает… И она советует…»)

Chapter 2 pattern 1.4 extends to non-research sources: an article, an order, a handbook. Make the author the
subject, and do not repeat «описан… описывает» across two sentences.

- «Статья рассматривает флаги как запасы… И она советует тестировать…» → «Hodgson смотрит на флаги как на
  складские запасы… Ещё он советует тестировать…»
- «Самый дорогой публичный пример описан в материалах регулятора. Приказ… описывает три сбоя.» → «…известен
  из материалов регулятора: приказ… описывает три сбоя.»
- «Исследование ревью в Google, которое Sadowski с коллегами провели по логам…, лучше читать как…» → «А
  работу Sadowski с коллегами о ревью в Google (логи примерно 9 миллионов изменений…) лучше читать как…»

### 1.5 English "Removing X made it worse" (gerund subject)

- «Удаление нового кода с семи правильных серверов только ухудшило дело» → «Когда новый код удалили с семи
  правильно обновлённых серверов, стало только хуже»
- «Отказ от поезда убирает точку координации, по которой…» → «Без поезда исчезает точка координации, вокруг
  которой…»

### 1.6 "Two things matter here. X. And Y." without numbering

When the text announces a count, number the items; a bare «И» for the second one reads as an afterthought.

- «Здесь важны два момента. Пайплайн, который… И Northstar считает…» → «Здесь важны два момента. Первый:
  пайплайн, который… Второй: Northstar считает…»
- «Урок: правило…, — это не механизм контроля, а откат хорош ровно настолько…» → «Урок двойной. Правило… —
  это не механизм контроля. А откат хорош ровно настолько…»

## 2. Two showcase paragraphs

### 2.1 Knight Capital

**Before.** Самый дорогой публичный пример описан в материалах регулятора. Приказ Комиссии по ценным бумагам
и биржам США (SEC) 2013 года по делу Knight Capital описывает три сбоя. […] И само развёртывание никто не
проверял. Заявки с повторно использованным флагом запускали на этом сервере старый код, и примерно за 45 минут
фирма набрала позиции, которые обошлись ей примерно в $460 млн. Удаление нового кода с семи правильных
серверов только ухудшило дело: флаг стал включать старый код и там (…). Уроки, которые выводит из этого
книга: никогда не используйте флаг повторно…

**After.** Самый дорогой публичный пример известен из материалов регулятора: приказ Комиссии по ценным
бумагам и биржам США (SEC) 2013 года по делу Knight Capital описывает три сбоя. […] И само развёртывание
никто не проверял. На этом сервере заявки с повторно использованным флагом запускали старый код, и примерно
за 45 минут фирма набрала позиции, которые обошлись ей примерно в $460 млн. Когда новый код удалили с семи
правильно обновлённых серверов, стало только хуже: флаг начал включать старый код и на них (…). Книга выводит
отсюда такие уроки: никогда не используйте флаг повторно…

### 2.2 Trunk-based development

**Before.** Одна позиция практиков — разрабатывать функции в ветках и сливать их, когда они готовы. Другая —
каждый день сливать небольшие изменения в основную ветку («ствол», trunk) и прятать незаконченную работу за
флагами. DORA сообщает, что по данным её опросов 2016 и 2017 годов показатели поставки и эксплуатации выше у
команд, где не больше трёх активных веток, слияния в trunk ежедневные и нет заморозок кода (…).

**After.** Среди практиков есть две позиции. Одна — разрабатывать функции в ветках и сливать их по
готовности. Другая — каждый день сливать небольшие изменения в основную ветку («ствол», trunk) и прятать
незаконченную работу за флагами. По данным опросов DORA 2016 и 2017 годов, показатели поставки и эксплуатации
выше у команд, где активных веток не больше трёх, в trunk сливают ежедневно, а заморозок кода нет (…).

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| ложные красные (as a noun) | «ложные красные сборки» in prose | a substantivised adjective without a noun reads as jargon; applied once in the note |
| правило «сначала отменить» | keep | reads naturally; bold without quotes in the definition, quotes elsewhere, as in the source |
| продвигать артефакт | keep | standard in Russian CI usage |
| годная (отправная точка) | «хорошая» | «годная» is colloquial; changed |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Bacchelli and Bird.** «изучали ревью с помощью инструментов в Microsoft» read as "tool-based review at
   Microsoft" and rendered «изучали в Microsoft ревью, которое проводят в специальных инструментах». If the
   English means the researchers used tools to study review, revert.
2. **Knight Capital, "seven correct servers".** «правильных» rendered «правильно обновлённых» (the seven that
   did receive the new code). Confirm.
3. **Example, "Three readings"**: I added the signpost «Из таблицы видно три вещи» before «Во-первых…» (no new
   claim). Remove if the English has no such lead-in and the maintainer prefers none.
4. **Case, "Release engineering made the incident longer".** Rendered «Из-за того, как были устроены релизы,
   инцидент затянулся». Same claim, less personified; confirm nothing narrower is meant (for example, the
   release tooling specifically).

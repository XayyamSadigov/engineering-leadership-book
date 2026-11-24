# Literary editing notes: chapter 25

File: `docs/parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.ru.md`. Edited
from the Russian text only; the English chapter was not opened. The file was not yet committed, so the
pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (276
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition lines, every table line,
INC ids, citations and Mermaid blocks are identical. One heading text changed (anchor kept): «Определения
серьёзности, которые сопротивляются занижению» → «…, устойчивые к занижению». About 70 sentence-level edits.
Failure-mode labels were already «Как заметить:» / «Что делать:»; «вопрос спорный» already in place.

The section 2a patterns appeared as expected (missing connectives, English word order, enumerations
announced by a count and then given as bare sentences). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 A Russian idiom that silently reverses the meaning

English "costs trust" came through as «стоит доверия», which in Russian means "deserves trust".

- «Гипотеза текущей минуты им не нужна: отозванное объяснение стоит доверия.» → «Сиюминутная гипотеза им
  ни к чему: объяснение, которое потом пришлось забрать назад, обходится потерей доверия.»

Grep later chapters for «стоит доверия», «стоит времени», «стоит денег» used as "costs".

### 1.2 Ambiguous subject/object with plural nouns ("incidents are produced by systems")

- «**инциденты производят системы, а сообщают о них люди**» (who produces whom?) → «**инциденты
  порождает система, а сообщают о них люди**» (singular verb fixes the subject).
- «В документе сказано, что его результаты — не чек-лист» (ch 26, «его» = Govern or CSF?) → «результаты
  CSF».

### 1.3 The source as speaker, again: «Эссе отвечает», «Эссе заимствует»

Chapter 23 pattern 1.4 applies to essays too. Make the author the subject.

- «Эссе заимствует две идеи из исследований безопасности.» → «Allspaw заимствует из исследований
  безопасности две идеи.»
- «Эссе отвечает, что с инженеров никто не снимает ответственности» → «Allspaw отвечает, что
  ответственности с инженеров никто не снимает»

### 1.4 Trailing «пока…» clause that hides the turn of events

- «На неделе 7 четыре инцидента подряд получили Sev3, в том числе двухчасовая задержка платежей у девяти
  клиентов, пока директор не переоценил их.» → «…получили Sev3, и среди них двухчасовая задержка
  платежей у девяти клиентов. Так продолжалось, пока директор не переоценил эти инциденты.»

### 1.5 Bookkeeping or abstract subjects for human actions

- «Разбор действий на неделе 8 принял новый срок, а временной меры не ввёл.» → «На разборе действий на
  неделе 8 согласились на новый срок, но временной меры не ввели.»
- «Директор ответил механизмом» → «Директор в ответ описал механизм»
- «Классификацию держат честной три правила» → «Честной классификацию делают три правила»

### 1.6 Calqued "the X is the Y" glosses: «это то, чему…», «Довод этот об…»

- «(его ещё называют постмортемом; это то, чему учится организация)» → «(…; на нём организация и
  учится)»
- «Довод этот об информации.» → «Это довод об информации.»

## 2. Two showcase paragraphs

### 2.1 Communication during an incident

**Before.** **Сотрудникам, работающим с клиентами, и руководству** нужно знать последствия, что делается,
что пока неизвестно и когда будет следующее обновление. Гипотеза текущей минуты им не нужна: отозванное
объяснение стоит доверия. Sofia Alvarez, VP Northstar по работе с клиентами, хочет во время инцидентов
честного статуса.

**After.** **Сотрудникам, работающим с клиентами, и руководству** нужно знать, каковы последствия, что
делается, что пока неизвестно и когда будет следующее обновление. Сиюминутная гипотеза им ни к чему:
объяснение, которое потом пришлось забрать назад, обходится потерей доверия. Sofia Alvarez, VP Northstar
по работе с клиентами, во время инцидентов хочет знать честный статус.

### 2.2 Why actions were not closed

**Before.** У того, что в Northstar закрывали только 32% действий, есть структурные причины. Межкомандными
действиями (…) владели инженеры, которые не распоряжаются ресурсами. Действия вне плана команды
проигрывали работе, которая в плане была. Разборы порождали слишком много мелких действий; […] И никто не
проверял повторы. Когда разбирали INC-427, проверка на повтор нашла, что разбор INC-406 (…) рекомендовал
проверки миграций…

**After.** То, что в Northstar закрывали только 32% действий, объясняется устройством процесса.
Во-первых, межкомандными действиями (…) владели инженеры, которые не распоряжаются ресурсами. Во-вторых,
действия вне плана команды проигрывали запланированной работе. В-третьих, разборы порождали слишком много
мелких действий; […] В-четвёртых, никто не проверял повторы. Когда разбирали INC-427, проверка на повтор
показала: ещё разбор INC-406 (…) рекомендовал проверки миграций…

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| определения, которые сопротивляются занижению | «устойчивые к занижению» | the verb calques "resist"; applied in heading, objective and section |
| смягчить последствия vs «смягчать тут нечего» | keep the term; avoid «смягчать» in the "soften wording" sense | collides with the term for mitigate; rendered «смягчать формулировку незачем» |
| те, кто чинит | keep | works in prose and the playbook; a noun form is not needed |
| владелец-руководитель | keep | clear and compact |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Case, week 9: «Разбор вёл инженер, причастный к инциденту».** The chapter's own rule is a neutral
   facilitator from another team for Sev1. If the English says "an engineer not involved in the incident",
   the Russian reverses the meaning. Not changed.
2. **«Отвечают здесь за систему, а не за то, что оказались ближе всего к сбою»** (was «ответственность за
   систему, а не за человека, оказавшегося ближе всего к сбою», which read as "responsible for the
   person"). Check that the English means accountability is not assigned to whoever was nearest.
3. **Example, «пользуясь остальными вопросами диаграммы»** (was «используя последующие вопросы»). Assumes
   "the later questions" means all questions after the first; the next sentence supports this.
4. **Case, «три инцидента оказались пограничными»** (was «оставили на усмотрение»). Assumes the English
   says the new definitions left three cases ambiguous.
5. **Case, «поэтому их подали как обнадёживающие»**: added «поэтому» where the original joined the two
   clauses with «и». Remove if the English does not link small numbers to the cautious framing.

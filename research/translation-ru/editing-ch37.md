# Literary editing notes: chapter 37

File: `docs/parts/08-management-operating-system/37-cadences-and-leadership-meetings.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (263
tokens, NBSP normalised); link targets, `{ #anchors }`, headings, exercise labels, every table line,
admonition line and Mermaid block are identical; NBSP count unchanged (55). Edited paragraphs re-wrapped at
about 105 characters, with link text kept on one line and no wrapped line starting with "N.". About 80
sentence-level edits. Failure-mode labels were already «Как заметить:» / «Что делать:».

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives, «На
уровне высшего руководства…» as an opener, the source as speaker). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 "Run rate" calqued as «в темпе»

- «Сам календарь, в темпе с недели 16, когда начались встречи через уровень…» → «Сам календарь (недельная
  нагрузка с недели 16, когда начались встречи через уровень…)»
- F3: «(таблица календаря, в темпе с недели 16)» → «(таблица календаря, недельная нагрузка с недели 16)»

Grep later chapters for «в темпе» used as a quantity.

### 1.2 "X buys Y" kept as «покупает»

Fine for capacity as money (ch38 keeps it deliberately), wrong when the subject is not a payer.

- «покупает ли выделенный ресурс то, ради чего его выделили» → «приносит ли выделенный ресурс то, ради
  чего его выделили»

### 1.3 Sentence fragments imitating an English list in the opening paragraph

- «В ней показано, как выстроить… Как провести встречу… И как проверить всю систему…» → one sentence with
  semicolons: «Вы узнаете, как выстроить…; как провести…; как проверить…»

### 1.4 "The X who does Y" as a conditional subject («CTO, который…, учит…»)

A sibling of ch33 pattern 1.2: the generic actor with a «который» clause reads as one specific person.

- «CTO, который каждую неделю просит свежий слайд, запускает каскад. Тот, кто каждый месяц просит…» →
  «Если CTO каждую неделю просит свежий слайд, он запускает каскад. Если каждый месяц просит…»
- «CTO, который на совещании с подчинёнными слушает статусы, учит каждого директора ниже делать то же
  самое.» → «Если на совещании с подчинёнными CTO слушает статусы, каждый директор ниже учится делать то же
  самое.»

### 1.5 Missing object after a verb («восстановил по записям»)

- «Директор восстановил по записям недели 14–19 и первым делом построил…» → «Директор восстановил его
  [календарь] по записям за недели 14–19 и первым делом построил…»

## 2. Two showcase paragraphs

### 2.1 What the research supports, older results

**Before.** Два более старых результата касаются устройства ритма. Разбросанные по дню встречи дорого
обходятся инженерам, которые ждут своих руководителей: в одной команде разработчиков продуктивность
выросла, когда изменили то, как группа коллективно распоряжается временем (…). А удалённые организации
сползают ко встречам, если информирование не взяло на себя письмо: у ИТ-специалистов, работавших из дома,
время на встречах выросло, а непрерывного рабочего времени стало меньше (…).

**After.** К устройству ритма относятся два более старых результата. Встречи, разбросанные по дню, дорого
обходятся инженерам, которым приходится ждать своих руководителей: в одной команде разработчиков
продуктивность выросла, когда в группе изменили правила общего распоряжения временем (…). А удалённые
организации, где информирование не перешло в письменную форму, сползают ко встречам: у ИТ-специалистов,
работавших из дома, времени на встречах стало больше, а непрерывного рабочего времени — меньше (…).

### 2.2 The Northstar matrix and its gaps

**Before.** Оба решения до сих пор открыты. Суть в том, что ни у одного форума не было задачи их принять,
поэтому каждое обсуждение заканчивалось без решающего. Те форумы, которые собирались, в основном
информировали. […] Операционный разбор выходил за забронированное время каждую неделю с тех пор, как в него
добавили новые пункты (сначала аудит того, как оценивали инциденты, потом бюджеты ошибок). Его 16 участников
проводили на нём около 20 человеко-часов в неделю, и большинство из них были старшими по дежурствам, то есть
инженерами.

**After.** Оба вопроса до сих пор открыты. Причина в том, что принять их не было задачей ни одного форума,
поэтому каждое обсуждение заканчивалось без решающего. А те форумы, что собирались, в основном
информировали. […] С тех пор как в операционный разбор добавили новые пункты (сначала аудит серьёзности
инцидентов, потом бюджеты ошибок), он каждую неделю выходил за забронированное время. Его 16 участников
проводили на нём около 20 человеко-часов в неделю; большинство из них — старшие по дежурствам, то есть
инженеры.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| аудит того, как оценивали инциденты | «аудит серьёзности инцидентов» (applied) | term base 3.x has «аудит серьёзности» for severity audit |
| «Сплачивать» (job Connect) | keep | reads well in the table and takeaways |
| сменяемый ведущий | «сменный ведущий» (applied) | the usual Russian form |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«инженерам, которым приходится ждать своих руководителей»** (Perlow, 1999; was «которые ждут»). If the
   English says the cost falls on engineers *waiting for* managers, fine; if it means engineers interrupted by
   meetings, the sentence should change.
2. **«Порядок вопросов ведёт сопредседатель»** rendered «Очередь выступающих ведёт…». Assumes the English is
   "runs the queue" (who speaks next), not the order of agenda items.
3. **A2, «так, чтобы встреча не решала, у кого право на это решение»** kept. If the English means "without the
   meeting taking the decision away from its owner", a sharper Russian wording would help.
4. **Case, «Но главная экономия — на операционном разборе»** (was «Большая экономия»). Assumes "the bigger
   saving" (bigger than the director's), not merely "a big saving".

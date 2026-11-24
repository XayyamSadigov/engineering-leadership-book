# Literary editing notes: chapter 38

File: `docs/parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.ru.md`.
Edited from the Russian text only; the English chapter was not opened. The file was not yet committed, so
the pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; every digit run is identical before and after (the only token-level
difference is «квартала 1, 25 процентов» → «квартала 1 — 25 процентов»); link targets, `{ #anchors }`,
headings, exercise labels, every table line, admonition line and Mermaid block are identical; NBSP count
unchanged (123). About 60 sentence-level edits. «Как заметить:» / «Что делать:» and «вопрос спорный» were
already in place.

**Maintainer term decision applied:** "target band" is now «целевой диапазон» (for consistency with
chapter 39), replacing «полоса целей» in all four places: the terms box, «Что обещает план», playbook step 6
(«пометьте работу над ней как целевой диапазон») and the case («включать ли целевой диапазон в
обязательства»). notes-t13 still lists «полоса целей»; the term base should record «целевой диапазон».

Section 2a patterns appeared as expected; only new ones follow.

## 1. Patterns new beyond section 2a

### 1.1 Telegraphic English labels in failure modes and complications

English failure modes often open with a verbless phrase; in Russian it reads as a note to self.

- «**План-список желаний.** Всё, что запросили, с оценкой от численности.» → «В план попадает всё, что
  запросили, а ресурс оценён по численности.»
- «Что делать: фиксированный лимит и удаление строки перед любым добавлением.» → «Что делать: ввести жёсткий
  лимит; прежде чем добавить строку, удалить другую.»
- «Что делать: ключевые результаты — только на результатах, у каждого пара, классификации проходят аудит.» →
  «ставить ключевые результаты только на результаты, каждому давать пару, классификацию проверять аудитом.»

### 1.2 Abstract subjects doing human things («квартальные изменения жертвуют…»)

- «Квартальные изменения плюс письменные триггеры жертвуют частью отзывчивости…» → «Меняя распределение раз
  в квартал и по письменным триггерам, вы жертвуете частью отзывчивости…»
- «Карта показателей организации говорит директору…» → «По карте показателей организации директор… видит…»

### 1.3 Questions announced by a count, then given as fragments

- «**Читатель решает** пять вопросов. Включать ли… Как ответить Marcus… Что будет… Как меняется… И какие
  три OKR…» → one sentence with a colon and semicolons.

### 1.4 Echo words in one sentence

- «описанные ловушки в литературе… уже описаны» (introduced by my first pass, caught) → «ловушки, о которых
  идёт речь, в литературе… уже рассмотрены»
- «предложенную директором, и предлагает» (ch37 X1) → «которую подготовил директор, и предлагает»

## 2. Two showcase paragraphs

### 2.1 Opening paragraph

**Before.** Эта глава о трёх инструментах, которыми директор управляет организацией от квартала к кварталу.
Это карта показателей (scorecard) организации; квартальный план, который заканчивается профинансированными
обязательствами и названными компромиссами; и распределение ресурсов между продуктовой работой, качеством и
платформой. Глава утверждает, что это один механизм: распределение — это бюджет, план его тратит, а карта
показателей показывает, купили ли эти траты то, что обещали.

**After.** Эта глава — о трёх инструментах, которыми директор управляет организацией от квартала к кварталу:
о карте показателей (scorecard) организации; о квартальном плане, итог которого — профинансированные
обязательства и названные компромиссы; о распределении ресурсов между продуктовой работой, качеством и
платформой. Главная мысль главы: это один механизм. Распределение — бюджет, план его тратит, а карта
показателей показывает, принесли ли траты то, что обещали.

### 2.2 Why the good OKR is good

**Before.** Цель называет результат, который узнал бы клиент. Каждый ключевой результат — число, у которого
есть исходный уровень и срок и которое у кого-то есть законное основание сдвигать. Каждая пара берётся из
другого источника данных, так что один и тот же человек не может сдвинуть обе метрики. Обе строки к тому же
стоят в карте показателей, так что ключевые результаты добавляют фокус, не добавляя измерений.

**After.** Цель называет результат, который заметил бы клиент. Каждый ключевой результат — число с исходным
уровнем и сроком, и у кого-то есть законное основание его сдвигать. Каждая пара берётся из другого
источника данных, поэтому один человек не может сдвинуть обе метрики. К тому же обе строки уже есть в карте
показателей: ключевые результаты добавляют фокус, но не добавляют измерений.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| полоса целей | «целевой диапазон» (applied, maintainer decision) | consistency with chapter 39 |
| пессимистичный сценарий (mental model) | «осторожный сценарий» | notes-t13 already flags that the defined term is "cautious case"; left as is pending the English |
| «с динамикой» (investment classes) | rendered «показывают и их динамику» | the bare phrase did not parse in Russian |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«CFO при неизменных операционных расходах»** (was «CFO с операционными расходами без роста»). Assumes
   "a CFO with flat opex".
2. **«Невидимый список непрофинансированного»: «пункты, которых нет в списке, будут сделаны»** kept. If the
   English says customers assume *their* items will be done because no list exists, the Russian is off.
3. **«триггер недели 31 не даёт принять это на веру»** (was «не даёт закрыть на это глаза»). Assumes the
   trigger guards against the forecast simply being assumed.
4. **Case, «их сводят вручную и помечают это оговоркой»**. Assumes the hand-assembled numbers are shown with a
   caveat next to them.

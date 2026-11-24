# Literary editing notes: chapter 59

File: `docs/parts/13-advanced-problems/59-transformation-under-constraint-and-scaling-without-bureaucracy.ru.md`.
Edited from the Russian text only; the English chapter was not opened. The file was not yet committed, so
the pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the multiset of numeric tokens is identical before and after (440
digit runs, NBSP normalised); link targets, citation link texts, `{ #anchors }`, heading lines, exercise
labels, admonition lines and both Mermaid blocks are byte-identical. One table line changed in text only
(«консультативный комитет по изменениям» → «комитет по изменениям»); no table number touched. No wrapped
line starts with a number and a period. NBSP 151 → 156. About 90 sentence-level edits.

Applied as instructed: "change advisory board" is «комитет по изменениям (change advisory board)» at first
use and «комитет по изменениям» after (prose, F3, Halvard table); audit "findings" in the Halvard section
are «замечания» («просроченные замечания по уязвимостям»). Rehearsal "findings" in the Northstar
inventory table stay «находки» (not an audit). Failure Modes have only «Как заметить:».

Section 2a patterns appeared as expected (English word order, missing connectives, «который» chains, a
person with a relative clause as the subject of a result). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Reversible subject and object with an inanimate noun

With inanimate nouns the nominative and accusative coincide, so English SVO order can flip the meaning.

- «выпуск системы определяет её ограничение» (reads as "output determines the constraint") →
  «выпуск системы определяется её ограничением»
- «Так книга читает Meadows, которая ставит правила гораздо выше параметров как точки вмешательства» →
  «Так книга читает Meadows: как точки вмешательства в систему правила у неё стоят гораздо выше
  параметров»

### 1.2 Negated nominalisation with «ничей / ничто»

English "No one's employment changed" / "Nothing costs much" came through as a negated noun phrase.

- «Ничья занятость не изменилась» → «Никто не лишился работы»
- «По отдельности ничто не стоит дорого, поэтому ничему не назначают цену» → «По отдельности всё это
  недорого, поэтому цену ничему не назначают»

### 1.3 Two parallel "Leaders who…" sentences as a contrast

- «Руководители, которые режут ресурс…, получают организацию… Руководители, которые вычищают процессы…,
  убирают механизмы контроля…» → «Если резать ресурс…, получится организация… Если вычищать процессы без
  разбора, вместе с ними уйдут механизмы контроля…»

### 1.4 Abstract "the answer is…" framing

- «Ответ не в отказе от процессов… Ответ в том, чтобы у каждого добавления были свой выход и своя цена»
  → «Отказываться от процессов не нужно… Нужно, чтобы у каждого нового процесса была цена и был
  предусмотрен выход»

## 2. Two showcase paragraphs

### 2.1 Why this matters, executive level

**Before.** Для высшего руководства урезание бюджета означает выбор: сокращать работу или ресурс, которым
её делают. Руководители, которые режут ресурс равномерно по всем направлениям и сохраняют все процессы,
получают организацию, которая исполняет те же ритуалы меньшим числом людей. Руководители, которые
вычищают процессы без разбора, убирают механизмы контроля, на которых держались надёжность, безопасность
или обязательства перед клиентами. Мастерство руководителя в том, чтобы понять, где что, до сокращения,
а не после инцидента.

**After.** Для высшего руководства урезанный бюджет — это выбор: сокращать работу или ресурс, которым её
делают. Если резать ресурс равномерно по всем направлениям и сохранить все процессы, получится
организация, которая исполняет те же ритуалы меньшим числом людей. Если вычищать процессы без разбора,
вместе с ними уйдут механизмы контроля, на которых держались надёжность, безопасность или обязательства
перед клиентами. Мастерство руководителя — разобраться, где что, до сокращения, а не после инцидента.

### 2.2 The removal that failed at Halvard

**Before.** Одна отмена прошла неудачно. Сгенерированный дашборд соответствия требованиям показывал
находки по уязвимостям с просроченными сроками устранения, но на него никто не смотрел. А ежемесячный
пакет был ещё и единственной встречей, на которой VP вместе разбирали эти находки. Число находок с
просроченным сроком устранения по всей Halvard выросло в квартале 2 с 12 до 31. […]

**After.** Одна отмена прошла неудачно. Сгенерированный дашборд соответствия требованиям показывал
замечания по уязвимостям с просроченным сроком устранения, но его никто не смотрел. А ежемесячный пакет
был ещё и поводом для единственной встречи, на которой VP вместе разбирали эти замечания. В квартале 2
число просроченных замечаний по всей Halvard выросло с 12 до 31. […]

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| оснастить измерениями (verdict "instrument") | keep in tables; in prose allow «начать измерять» | long in table cells and in the playbook list |
| несущее нагрузку / несущее историю | keep | the pair works once the mental model introduces it |
| «находки» for rehearsal findings | keep, distinct from audit «замечания» | rehearsals are not audits |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«Пункты без нагрузки либо старше (чек-лист)»** rendered «либо появились раньше». Assumes "older"
   means the checklist predates the year-1 additions.
2. **«Gwen Abernathy… руководит двумя директорами: Developer Platform (…) и Infrastructure (…)»**
   rendered «директорами: по Developer Platform (…) и по Infrastructure (…)». Assumes each director heads
   that area.
3. **«По решению CTO её бюджет…»** («её» could be Gwen's or the organization's) rendered «бюджет
   организации». Check that the cut applies to the platform organization.
4. **«Некоторые процессы существуют потому, что стейкхолдер потерял доверие после сбоя»**: whose trust
   (in the team?) is not said; kept as «утратил доверие».
5. **«Ответ в том, чтобы у каждого добавления были свой выход и своя цена»** rendered «у каждого нового
   процесса была цена и был предусмотрен выход». Assumes "exit" means a planned way to retire it.

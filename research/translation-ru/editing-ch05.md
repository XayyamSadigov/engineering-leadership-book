# Literary editing notes: chapter 5

File: `docs/parts/02-people-management/05-one-on-ones-coaching-and-mentorship.ru.md`. Edited from the
Russian text only; the English chapter was not opened.

Checks against `git show HEAD:<file>`: the sorted list of numeric tokens is identical; `{ #anchors }`, link
targets, exercise labels, admonition types, Mermaid node ids, edges and labels, table structure and every
number in the tables are identical; `tools/validate_book.py` passes. Table headers reworded in two tables
(«Чьи знания движут процессом» → «На чём держится помощь», values made parallel: «Знания помогающего»,
«Знания самого человека»; «Склоняет к…» → «В пользу…»). «Bogotá» → «Богота» per the maintainer's decision
in glossary section 3.y (cities in Cyrillic), matching the Northstar pages. Non-breaking spaces added on the
label side («неделе⍽19», «квартала⍽2», «главы⍽9») and between numbers and units.

General impression: the cleanest of the chapters seen so far in vocabulary. The work was syntax: the
three «На уровне…» openers (section 2a.2 again), long sentences that chain a cause and a consequence with
commas, «имеет»-constructions, and a few polysemy traps.

## Patterns new beyond glossary section 2a

### 1. One sentence carrying a whole causal chain with commas

Russian wants the loop broken into steps, one per sentence or clause.

- «В петле вырождения руководитель начинает с вопроса «над чем работаешь?», получает статус, доступный в
  других местах, встреча кажется накладным расходом, её отменяют, и подчинённый усваивает…» → «…начинает
  с вопроса «над чем работаешь?» и получает статус, который и так есть в других местах. Встреча начинает
  казаться накладным расходом, её отменяют, и подчинённый усваивает…»
- «Встреча 1:1 по видео лишается случайных контактов в коридоре, которые заполняют пробелы у тех, кто
  работает в одном офисе, поэтому она несёт на себе больше функций канала, и переносить её стоит в
  последнюю очередь.» → «Тем, кто работает в одном офисе, пробелы заполняют случайные разговоры в
  коридоре. У встречи 1:1 по видео такой подпитки нет, поэтому на ней лежит больше работы канала, и
  переносить её стоит в последнюю очередь.»

### 2. «имеет X» for English "has X"

- «руководитель, который проводит каждую встречу 1:1 и ничего не узнаёт, имеет безупречную статистику и
  сломанный канал» → «У руководителя, который проводит каждую встречу 1:1 и ничего не узнаёт, безупречная
  статистика и сломанный канал.»
- «человек может иметь хороших менторов и всё равно оставаться незамеченным» → «у человека могут быть
  хорошие менторы, а его всё равно не замечают»

### 3. Polysemy inside one sentence

- «Считайте сигналы вырождения по своим заметкам, а сюрпризы… считайте самым сильным сигналом» (count /
  consider) → «Подсчитывайте сигналы вырождения по своим заметкам. Самый сильный из них — сюрпризы…»
- «лучшей оценке» (F3: better review or higher rating?) → «более качественная оценка» (see doubts)

### 4. Questions to the report packed into one sentence with semicolons

- «задайте один из вопросов: что больше всего раздражает в твоей неделе; какой работы ты хочешь больше
  через год; что я делаю такого, что тебе мешает» → «задайте один из таких вопросов: «Что за неделю
  раздражало тебя больше всего?», «Какой работы тебе хотелось бы больше через год?», «Что я делаю такого,
  что тебе мешает?»» (quoted speech keeps «ты»; the book's own voice stays «вы»)

### 5. "Two points": announce, then number them

- «Важнее всего два момента. Решать, о чём встреча, должен подчинённый… А руководитель — хуже всех
  расположенный человек для того, чтобы судить…» → «Важнее всего здесь два вывода. Первый: решать, о чём
  встреча, должен подчинённый… Второй: хуже всех судить о том, работает ли встреча, может как раз
  руководитель…»
- «Традиция практиков согласна с первым моментом.» → «С первым выводом согласна и традиция практиков.»

### 6. Participial phrase for an attribute Russian packs into a compound

- «встречи с мобильными инженерами в Bogotá, проходившие по видео, часто переносились» → «видеовстречи с
  мобильными инженерами в Боготе часто переносились»
- «двух инженеров по качеству, которые присоединились к команде и теперь подчиняются Daniel, не
  включили, потому что они пришли слишком недавно» (said twice) → «Двух инженеров по качеству, которые
  теперь тоже подчиняются Daniel, не включили: они пришли в команду слишком недавно.»

### 7. "Fix" as a noun clause: «Сохраняют запись помощником»

- «Общая повестка, фактические наблюдения и отсутствие сюрпризов на оценке сохраняют запись помощником.»
  → «Запись остаётся помощником, если повестка общая, наблюдения фактические, а на оценке нет сюрпризов.»
- «Процесс повышений, требующий датированных конкретных фактов, показывает, какие руководители ведут
  записи.» → «Если процесс повышений требует конкретных датированных фактов, становится видно, какие
  руководители ведут записи.»

## Two showcase paragraphs

### 1. The two loops of the mental model

**Before.** У канала две петли. В здоровой подчинённый приносит темы, руководитель что-то узнаёт и
заметно действует, и в следующий раз подчинённый приносит темы потруднее. В петле вырождения руководитель
начинает с вопроса «над чем работаешь?», получает статус, доступный в других местах, встреча кажется
накладным расходом, её отменяют, и подчинённый усваивает, что настоящие разговоры происходят где-то ещё.

**After.** У канала две петли. В здоровой петле подчинённый приносит темы, руководитель узнаёт новое и
заметно действует, и в следующий раз подчинённый приносит темы потруднее. В петле вырождения руководитель
начинает с вопроса «над чем работаешь?» и получает статус, который и так есть в других местах. Встреча
начинает казаться накладным расходом, её отменяют, и подчинённый усваивает, что настоящие разговоры идут
где-то ещё.

### 2. Coaching evidence and its limit

**Before.** Это **научные результаты**, касающиеся в основном программ коучинга. Мы не нашли метаанализа
коучинга со стороны собственного руководителя, поэтому вопрос, получает ли тот же эффект руководитель,
который ещё и определяет зарплату, остаётся открытым. С тем, кто их оценивает, люди менее откровенны в
разговоре о своих слабостях.

**After.** Это **научные результаты**, но относятся они в основном к программам коучинга. Метаанализа
коучинга со стороны собственного руководителя мы не нашли. Поэтому открыт вопрос, добивается ли того же
эффекта руководитель, который вдобавок определяет зарплату: о своих слабостях люди менее откровенны с
тем, кто их оценивает.

## Term proposals

| Current | Proposal | Reason |
|---|---|---|
| текущий документ (running document, notes-t1) | «сквозной документ» or «живой документ» | «текущий» reads as "the current one" (as opposed to an old one), not "kept running". Kept for consistency |
| закрытие обязательства («начинается с его закрытия») | «отчёт о выполнении» in prose | "closing" an item is tracker jargon; kept where the playbook speaks of «закрывать обязательства» |
| ослабители (diminishers, notes-t1) | check the published Russian edition of *Multipliers* before fixing | «ослабитель» is not a natural Russian noun; notes-t1 already flags this |
| Заметное выполнение обещаний (heading) | «Выполненные обещания на виду» | applied; the noun phrase read as a calque |
| Ротация более глубоких вопросов (heading) | «Глубокие вопросы по очереди» | applied; «ротация» is jargon here |

## Meaning doubts (not changed in meaning; check against the English)

1. **«петля обратной связи… медленная, общая и отфильтрованная».** «общая» probably renders the
   attribution problem of chapter 2 ("shared"), or "noisy" (the link anchor is `slower-and-noisier`). As
   Russian, «общая» reads as "general". Kept; propose «зашумлённая» or «с размытой атрибуцией» once the
   English is checked.
2. **Info box: «Неделя 19…, начало квартала 2 (недели 14–26)».** Week 19 is the middle of weeks 14–26,
   not the start. Kept.
3. **F3 «записи, которые должны были бы привести к лучшей оценке».** "Better review" (more evidence-based)
   or "higher rating"? Rendered «более качественная оценка», which assumes the first.
4. **Grove: «из-за того, чему она учит руководителя».** Rendered «благодаря тому, что на ней узнаёт
   руководитель». Same idea if the English is "because of what it teaches the manager"; check.
5. **Enterprise: «даёт сигнал, которого не дадут самооценки».** Whose self-ratings? Presumably the
   managers'. Left unspecified as in the source.
6. **«Человеко-часы» in the example table** stays (two participants of different roles). If the English
   says "engineer-hours", the term base wants «инженеро-часы».

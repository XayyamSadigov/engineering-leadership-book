# Literary editing notes: chapter 18

File: `docs/parts/04-execution/18-measuring-engineering-productivity.ru.md`. Edited from the Russian text only;
the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `git show HEAD:<file>`
(190 tokens, NBSP normalised); link targets and link texts (46), `{ #anchors }` (27), exercise labels,
admonition types, Mermaid blocks and every number inside tables are identical. One table cell reworded
(«Устойчиво ли людям?» → «Устойчив ли темп для людей?»). Failure-mode labels relabelled to «Как заметить:» /
«Что делать:». NBSPs fixed on the label side («главы 54,⍽будут» → «главы⍽54, будут», «квартала 2,⍽готовя»,
«квартал 1⍽перевёл»). Trade-off heading «Купить против построить» → «Покупка против собственной разработки»
(term base: «разработать или купить»).

Section 2a patterns appeared as expected; only new ones follow.

## 1. Patterns new beyond section 2a

### 1.1 «руководство» = the DORA guide and «руководство» = leadership in one chapter

The chapter uses "the guide" (DORA's metrics guide) and "leadership" side by side; both became «руководство».
A sentence such as «когда руководство утверждает, что скорость и стабильность — не компромисс» reads as
"when management claims". Name the guide where it is meant.

- «Его текущее руководство (январь 2026 года) перечисляет…» → «В текущем руководстве DORA (январь
  2026 года) перечислены…» (also fixes «Его» for DORA)
- «Поэтому, когда руководство утверждает…» → «Поэтому утверждение руководства DORA, что…, читайте так:»

### 1.2 Cataphoric «Это …» before the thing it points to

- «Это общие правила измерения поставки, а глава 27 применяет их… Предпочитайте…» (the rules come after)
  → «Общие правила измерения поставки таковы. Предпочитайте… Глава 27 применяет эти правила к качеству…»
- «Таблица делает каждое измерение применимым.» → «Таблица ниже переводит каждое измерение в практику.»

### 1.3 Calqued idioms in the argument

- «Ответ „разработку нельзя измерить“ приглашает выбрать метрику кого-то другого» → «…означает, что
  метрику выберет кто-то другой»
- «будут обсуждать в его терминах» → «будут мерить этим числом»
- «не дают опросу превратиться в голосование о популярности» → «…в конкурс популярности»
- «Вопрос приходит в финансовой форме» → «Вопрос звучит на языке финансов»

### 1.4 Article/paper as grammatical subject that "claims"

Same family as ch02 1.4, but with «Статья… утверждает / Ответ… утверждает / Пост… называет» three
sentences in a row.

- «Статья Nicole Forsgren, Margaret-Anne Storey и коллег… в аннотации утверждает, что…» → «Nicole
  Forsgren, Margaret-Anne Storey и их коллеги… утверждают в аннотации своей статьи, что…»
- «Ответ Orosz и Beck утверждает, что…» → «Orosz и Beck в ответной статье утверждают, что…»
- «Пост Forsgren называет пять измерений» → «Пять измерений перечислены в посте Forsgren» (theme first)

### 1.5 One sentence carrying a story with a «после чего» tail

- «…около года они были полезны, затем их превратили в оценку, стали использовать при оценке
  результативности и сводить по руководителям, после чего давление и торг привели к тому, что компания
  знала меньше, чем раньше.» → three sentences: «Около года опросы приносили пользу, затем их превратили в
  оценку: результаты стали учитывать при оценке результативности и сводить по руководителям. Начались
  давление и торг, и в итоге компания знала меньше, чем раньше.»

### 1.6 Same verb twice in a list of reasons

- «атрибуция не работает, …, а инструмент перестаёт работать» → «…, а сам инструмент портится»
- «соблазняют сильнее всего и сильнее всего вводят в заблуждение» → «соблазнительнее и обманчивее всего»

## 2. Two showcase paragraphs

### 2.1 Why this matters, executive level

**Before.** **Для руководства компании** вопрос приходит в финансовой форме. Разработка — часто крупнейшая
статья операционных расходов, которую CFO (финансовый директор) не может объяснить построчно. У продаж
есть выполнение квоты; почему у разработки нет выработки на инженера? Вопрос законный. Ответ «разработку
нельзя измерить» приглашает выбрать метрику кого-то другого; подсчёт активности на инженера уничтожает ту
самую информацию, которую должен давать. Третий ответ: измеряйте систему, парами, ради улучшения, и
переводите результат в то, что руководству нужно решить.

**After.** **Для руководства компании** вопрос звучит на языке финансов. Разработка — часто крупнейшая
статья операционных расходов, и CFO (финансовый директор) не может разложить её построчно. У продаж есть
выполнение плана; почему у разработки нет выработки на инженера? Вопрос законный. Ответ «разработку
нельзя измерить» означает, что метрику выберет кто-то другой; подсчёт активности на инженера уничтожает
ту самую информацию, которую должен давать. Есть третий ответ: измеряйте систему, парами показателей,
ради улучшения, и переводите результат в решения, которые предстоит принять руководству.

### 2.2 The 2023 dispute, the reply

**Before.** Ответ Orosz и Beck утверждает, что большинство новых показателей находятся на стороне усилий
и выпуска в цепочке, что измерение отдельных людей меняет поведение и что фреймворк, скорее всего,
навредит инженерной культуре (…). Их самое сильное доказательство — рассказ Beck об опросах разработчиков
в Facebook: около года они были полезны, затем их превратили в оценку, стали использовать при оценке
результативности и сводить по руководителям, после чего давление и торг привели к тому, что компания
знала меньше, чем раньше. Они же признают правоту руководства: тем, кто отказывается отвечать, навяжут
чужой ответ.

**After.** Orosz и Beck в ответной статье утверждают, что большинство новых показателей относятся к
звеньям усилий и выпуска, что измерение отдельных людей меняет их поведение и что фреймворк, скорее
всего, навредит инженерной культуре (…). Самый сильный их довод — рассказ Beck об опросах разработчиков в
Facebook. Около года опросы приносили пользу, затем их превратили в оценку: результаты стали учитывать при
оценке результативности и сводить по руководителям. Начались давление и торг, и в итоге компания знала
меньше, чем раньше. При этом авторы признают, что в одном руководство право: тем, кто отказывается
отвечать, навяжут чужой ответ.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| руководство (DORA guide) | «руководство DORA» or «руководство по метрикам DORA» on each use where leadership is also in play | see 1.1 |
| пути подгонки | «способы подгонки» | «пути» is a calque of "ways"; changed in the playbook and takeaways |
| Купить против построить | «Покупка против собственной разработки» | term base «разработать или купить»; «построить» is a calque of "build" |
| выпуск (output) vs «Core выпускается поездом» | keep both, watch | the chain term «выпуск» and the verb «выпускать» (release) meet in one chapter; context resolves it here |
| инструментирование | keep; «сбор телеметрии» as a fallback in prose | understood by engineers, but heavy |
| выполнение квоты (sales) | «выполнение плана (продаж)» | «квота» reads as an allocation in Russian business usage; changed here |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Cross-reference after the dispute.** «Вопрос спорный, и позицию книги излагает следующий раздел», but
   the next section is the gaming table; the book's position is in the section after it («Почему книга
   отказывается…»). Kept «в следующем разделе»; the English may say "below" or "the section after next".
2. **«Данные по этому вопросу противоречивы, и такова позиция книги»** (end of the DORA-limits section)
   reads oddly; rendered «…противоречивы, и такое прочтение — позиция книги». If the English is "This is
   contested; this is the book's reading", «Вопрос спорный» would be the fixed rendering.
3. **Case, the request.** «в присланной ему статье консалтинговой компании»: «ему» can be the board or
   Rajiv. Kept ambiguous as in the source; please check who received the article.
4. **Enterprise, ownership.** «Один человек, часто staff-инженер вместе с платформенными инженерами,
   владеет определениями» contradicts itself (one person, together with others). Kept.
5. **DevEx paragraph.** «…и её исправление — решение» rendered «…и её исправление — вопрос решения». If
   the English means "fixing it is the decision (to make)", fine; if "the fix", reword.
6. **Data plumbing.** «отправляет одно и то же событие развёртывания» rendered «событие развёртывания
   одного и того же формата» (a shared schema). Confirm.
7. **Case.** «четыре сервиса на shell-скриптах»: probably "deployed by shell scripts"; kept literal.

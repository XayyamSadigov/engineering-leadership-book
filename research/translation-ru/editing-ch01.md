# Literary editing notes: chapter 1

File: `docs/parts/01-foundations/01-what-engineering-management-is.ru.md`. Edited from the Russian text
only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `git show HEAD:` (194
tokens); link targets (41), `{ #anchors }` (27), exercise labels, admonition types, Mermaid node ids, table
structure and every table number are unchanged (scripted diff). Mermaid labels and headings untouched.
Non-breaking spaces moved to the label side («Глава⍽2 посвящена», «главе⍽3», «недели⍽1»; removed from
«Sev1⍽и», «1:1⍽формально»).

Overall: accurate, clean vocabulary; the English skeleton showed mostly in long hypothetical subjects,
pronouns with unclear antecedents, and book titles used as grammatical subjects. Patterns already in
glossary 2a (scale openers, missing connectives, «Решения — в решениях») recurred and were fixed the same
way; below are the ones new beyond 2a.

## 1. Patterns (new beyond glossary 2a)

### 1.1 Long hypothetical subject → «Допустим…» or «Если…»

English packs a scenario into the subject ("A manager with fifteen reports who holds… spends…"). Russian
states the condition first.

- «Руководитель с пятнадцатью прямыми подчинёнными, который еженедельно проводит с каждым 30-минутную
  встречу один на один (1:1), тратит на одно это семь с половиной часов — почти пятую часть…» →
  «Допустим, у руководителя пятнадцать прямых подчинённых и с каждым он еженедельно проводит 30-минутную
  встречу один на один (1:1). Только на это уходит семь с половиной часов, почти пятая часть…»
- «Роль, которая отдаёт техническое направление техлиду, и календарь, где треть часов занимают ревью
  дизайна, противоречат друг другу» → «Если по роли техническое направление отдано техлиду, а треть часов
  в календаре занимают ревью дизайна, одно противоречит другому»
- «Определение роли, которое отдаёт техническое направление техлиду, тратящему 90 процентов времени на
  фичи, на деле не отдаёт его никому» → «Если по определению роли техническое направление отдано техлиду,
  который тратит 90 процентов времени на фичи, на деле оно не отдано никому»

### 1.2 Pronoun whose antecedent is the wrong noun

English "he/she/it" after a list or an aside lands on the nearest Russian noun of the same gender.

- After the four archetypes, ending with «Правая рука…»: «Он отмечает, что большинство компаний…» (reads
  as "the right hand notes") → «По наблюдению Larson, большинство компаний…»
- «Роль директора подчиняется той же логике… Её результат — результат всей организации и коллег, на
  которых она влияет» (the role influences peers?) → «Результат директора — это результат всей организации
  плюс результат коллег, на которых он влияет»

### 1.3 Book title as grammatical subject («*X* известна тем…»)

For metadata-only sources the book says a work "is known for" an idea. Calqued, the italic title becomes
the subject and the author dangles in the genitive. Keep «известна» (it carries the evidence level), but
lead with the theme or the author.

- «*The Effective Executive* Peter Drucker известна более ранней версией той же дисциплины» → «Более ранняя
  версия той же дисциплины известна по книге Peter Drucker *The Effective Executive*»
- «*The Manager's Path* Camille Fournier, известная тем, что проводит читателя… рассматривает…» → «Camille
  Fournier в книге *The Manager's Path*, известной тем, что она проводит читателя…, рассматривает…»
- «*An Elegant Puzzle* Will Larson известна тем, что…» → «Книга Will Larson *An Elegant Puzzle* известна
  тем, что…»

### 1.4 Same-root tautology the English did not have

- «Двухнедельный календарь Jo, восстановленный по календарю и истории чатов» → «Две недели Jo,
  восстановленные по календарю и истории чатов, — это 80 рабочих часов»
- «[координатора инцидента] — того, кто координирует реагирование» → «того, кто управляет реагированием»
- «Опасен третий случай: о нём ничто не сигналит» → «Опасен третий вариант: он ничем себя не выдаёт»

### 1.5 Nominal labels in Failure Modes

«Обнаружение:» repeated four times reads as a form field. Replaced with «Как заметить:» (and in chapter 3
«Противодействие:» with «Что делать:»). «Сигнал:» kept: it is short and verbal enough.

- «Обнаружение: спросите: «Что в команде стало иначе благодаря этому?»» → «Как заметить: задайте вопрос
  «Что в команде стало иначе благодаря этому?»» (also removes the double colon)

### 1.6 Ambiguous genitive of a role

- «Вы — директор Marcus Oyelaran.» (reads as "You are director Marcus Oyelaran") → «Вы директор, Marcus
  Oyelaran подчиняется вам.»

### 1.7 Grammar slips

- «мобильный релиз с изменением в вебе уже дважды конфликтовали» (agreement) → «мобильный релиз уже дважды
  конфликтовал с изменениями в вебе»
- «Отличать… и размещать…» among perfective objectives («Разделить», «Объяснить», «Написать») →
  «Отличить… и разместить…»

### 1.8 «Данные… реальны» and other literal predicates

- «Данные о том, что руководители влияют на результаты, реальны.» → «Между тем данные о влиянии
  руководителей на результаты вполне реальны.»
- «Вывод о текучести напоминает…» (after «вывод» used one sentence earlier) → «Данные о текучести
  напоминают…»

## 2. Two showcase paragraphs

### 2.1 Three jobs, competing for one week (hypothetical subject, rhythm)

**Before.** Поскольку горизонты разные, занятый руководитель смещается к работе с самой быстрой обратной
связью — к поставке. За год этот дрейф виден в календаре раньше, чем в текучести или в архитектуре,
которую никто не выбирал. […] Кроме того, работы конкурируют за один дефицитный ресурс — неделю
руководителя. Руководитель с пятнадцатью прямыми подчинёнными, который еженедельно проводит с каждым
30-минутную встречу один на один (1:1), тратит на одно это семь с половиной часов — почти пятую часть
40-часовой недели, и это ещё до найма, обратной связи и последующих действий.

**After.** Из-за разницы в сроках занятой руководитель сползает к работе с самой быстрой обратной связью,
то есть к поставке. За год этот дрейф проявляется в календаре раньше, чем в текучести или в архитектуре,
которую никто не выбирал. […] Кроме того, работы борются за один дефицитный ресурс — неделю
руководителя. Допустим, у руководителя пятнадцать прямых подчинённых и с каждым он еженедельно проводит
30-минутную встречу один на один (1:1). Только на это уходит семь с половиной часов, почти пятая часть
40-часовой недели. А ведь есть ещё найм, обратная связь и последующие действия.

### 2.2 Evidence, Hoffman and Tadelis (one 60-word sentence → three)

**Before.** На кадровых данных и опросах сотрудников крупной высокотехнологичной компании Hoffman и
Tadelis в аннотации рабочего доклада сообщают, что навыки управления людьми, измеренные опросами, сильно
и отрицательно связаны с текучестью, причём дизайн исследования поддерживает причинную интерпретацию; но
на другие результаты эти навыки стабильно не влияли.

**After.** Hoffman и Tadelis изучили кадровые данные и опросы сотрудников крупной высокотехнологичной
компании. В аннотации рабочего доклада они сообщают: навыки управления людьми, измеренные опросами,
сильно и отрицательно связаны с текучестью, и дизайн исследования поддерживает причинную интерпретацию.
Устойчивого влияния на другие результаты эти навыки не показали.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| «Обнаружение:» / «Противодействие:» in Failure Modes | «Как заметить:» / «Что делать:» as fixed labels book-wide | verbal, reads as advice rather than a form; applied in chapters 1 and 3 |
| руководитель, повышенный внутри (команды) | вырос(ла) до руководителя внутри (команды) | repeats the chapter 2 proposal; applied here to Priya |
| техническое направление | keep, but watch | in «кто задаёт направление вебу» and «техническое направление у…» it is fine; as a job name it can read as "a technical department". «техническое руководство» is the alternative if the maintainer wants one |
| с рычагом (audit mark) | keep | awkward as an adjective, but it is a fixed label repeated in chapters 1, 3, solutions |
| выпуск (output, in research summaries) | keep | correct for economics papers; never use it near «релиз» |

## 4. Meaning doubts (not changed in meaning; check against the English)

1. **Why This Matters, organization.** «ни в одной команде одну и ту же часть работы не закрывает один и
   тот же человек» rendered «в разных командах одну и ту же часть работы закрывают разные люди». If the
   English means "different roles cover the same job in each team", this is right; if it means "nobody
   covers the same part consistently", it narrows.
2. **Lazear et al.** «работников сервисной сферы, опирающейся на технологии» is ambiguous (is the firm or
   the work technology-based?). Rendered «работники сферы услуг опираются в работе на технологии».
   «При отдельной нормировке» kept as is; the phrase is unclear in Russian and probably in the source.
3. **Ines's quote (A3).** «только так меня кто-то слушает насчёт Core» → «иначе меня насчёт Core никто не
   слушает». Same meaning; check the English tense.
4. **A1.** «Вы — директор Marcus Oyelaran» interpreted as "you are Marcus's director" (the reader is the
   director throughout). Confirm.
5. **Jo example.** «Ari получает область решений, которую раньше делил с Jo» → «Ari берёт на себя…»
   (gains vs takes on: the cost framing suggests extra load for Ari).
6. **Trade-offs heading.** «Единообразие против соответствия» → «Единообразие против соответствия
   команде»; assumes the English is "fit" (to the team).
7. **The six managers' paragraph** («Priya, восемь месяцев назад повышенная внутри Orders…») now opens
   «Priya выросла до руководителя внутри Orders восемь месяцев назад»; fact unchanged.

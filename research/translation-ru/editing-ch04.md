# Literary editing notes: chapter 4

File: `docs/parts/01-foundations/04-the-leadership-ladder.ru.md`. Edited from the Russian text only; the
English chapter was not opened.

Checks against `git show HEAD:<file>`: the sorted list of numeric tokens is identical; `{ #anchors }`, link
targets, exercise labels, admonition types, Mermaid node ids and edges, table structure and every number in
the tables are identical; `tools/validate_book.py` passes. Mermaid labels and headings unchanged. Non-breaking
spaces moved to the label side («глава⍽8», «главы⍽47 и⍽50», «Неделя⍽1», «упражнение⍽A1»); stray ones after
a token removed («Sev1⍽и», «1:1⍽со» → «встречи⍽1:1 со»).

General impression: accurate and clean in vocabulary. What made it read as a translation: chapter numbers
as grammatical subjects at the head of the sentence, «что…, что…, и что…» chains after a reporting verb,
noun lists where Russian wants verbs, and a few Latin-name agreement slips.

## Patterns new beyond glossary section 2a

### 1. «Глава N разбирает X» with the chapter as the opening subject

English "Chapter 1 covers X" puts known material last. Russian puts the topic first and the chapter number
at the end, where it is the new information.

- «Глава 1 разбирает идею Andrew Grove о том, что результат руководителя — это результат организации…» →
  «Идею Andrew Grove о том, что результат руководителя — это результат организации, на которую он
  влияет, разбирает глава⍽1»
- «Глава 2 приводит данные об отборе при повышении» → «Данные об отборе при повышении приводит глава⍽2»
- «Глава 8 разбирает карьерные лестницы и повышения, глава 29 — роли staff-plus, а главы 40, 47 и 50 —
  роли…» → «Карьерные лестницы и повышения разбирает глава⍽8, роли staff-plus — глава⍽29, роли
  директора, VP и CTO — главы⍽40, 47 и⍽50.»

### 2. «утверждает, что…, что…, и что…»: a reporting verb with stacked object clauses

- «Charity Majors утверждает, что менеджмент — это смена профессии, а не повышение, что работа эта очень
  прерывистая и что осознанные переходы… делают людей лучше» → «Charity Majors утверждает три вещи:
  менеджмент — это смена профессии, а не повышение; работа эта сплошь состоит из прерываний; осознанные
  переходы… делают людей лучше в обоих делах»
- «Larson утверждает, что CEO, коллеги… и инженерная организация видят каждый свою верную, но неполную
  версию проблемы, и работа руководителя высшего уровня — свести их вместе…» → two sentences: «…видят
  каждый свою версию проблемы, верную, но неполную. Работа руководителя высшего уровня — свести эти
  версии вместе…»

### 3. Lists of verbal nouns after «называет ядром»

- «Larson называет ядром работы staff-инженера задание технического направления, менторство и
  спонсорство, инженерный взгляд при принятии решений, исследование новых направлений и координацию,
  которая двигает проекты вперёд, — при меньшем объёме программирования, чем раньше» → «Ядро работы
  staff-инженера, по Larson, таково: задавать техническое направление, заниматься менторством и
  спонсорством, привносить инженерный взгляд в решения, исследовать новые направления и координировать
  работу так, чтобы проекты двигались вперёд. Программирования при этом меньше, чем раньше»

### 4. English elliptic conditionals «Слишком рано — и…»

Fine in a slogan, awkward as an explanation of a decision.

- «Слишком рано — и появляется посыльный; слишком поздно — и новые руководители остаются без присмотра.» →
  «Если ввести уровень слишком рано, появится передаточное звено; если слишком поздно, новые руководители
  останутся без присмотра.»
- «Читайте результат как долю, а не как вердикт.» → «Смотрите на результат как на долю, а не как на
  вердикт.» (also: «читать» a number is an English metaphor; it is kept only where it means reading text)

### 5. "Detected by…" rendered as «Обнаруживается…» plus a dangling noun

- «Обнаруживается по календарю: доля времени, отведённая решениям, которые может принимать только этот
  уровень.» → «Выявляется по календарю: смотрите, какая доля времени уходит на решения, доступные только
  этому уровню.»
- «Обнаруживается, когда у команд с лучшим рейтингом ещё и больше всего пропущенных дефектов» →
  «Выявляется, когда у лидеров рейтинга ещё и больше всего пропущенных дефектов»

### 6. Latin names that cannot take case endings: agreement and case slips

- «Northstar в том виде, в каком её застаёт директор» → «Northstar такая, какой её застаёт директор»
  (keep the gender of «компания» in every agreeing word)
- «Orders и Billing выпускают большинство изменений внутри Core» → «Большинство изменений команд Orders и
  Billing… приходится на Core» (a Russian head noun «команд» carries the case)
- «у Victor Lindqvist, CTO, руководитель разработки — директор» → «разработкой для CTO Victor Lindqvist
  руководит директор»

### 7. Viewpoint calques: «С этой точки зрения», «Через призму»

- «С этой точки зрения Daniel Cho — самый сильный руководитель» → «При таком взгляде сильнейший
  руководитель — Daniel Cho»
- «Два взгляда ранжируют по-разному, и второй отделяет…» → «Два взгляда дают разный порядок. Второй
  отделяет…»

## Two showcase paragraphs

### 1. The staff-plus track (noun list, «он также отмечает»)

**Before.** Трек staff-plus существует для того, чтобы к техническому лидерству вёл не только путь через
управление людьми. Larson называет ядром работы staff-инженера задание технического направления,
менторство и спонсорство, инженерный взгляд при принятии решений, исследование новых направлений и
координацию, которая двигает проекты вперёд, — при меньшем объёме программирования, чем раньше (…). Он
также отмечает, что в некоторых компаниях нет модели технического лидерства и каждого опытного инженера
подталкивают к менеджменту (…).

**After.** Трек staff-plus нужен для того, чтобы путь к техническому лидерству не лежал только через
управление людьми. Ядро работы staff-инженера, по Larson, таково: задавать техническое направление,
заниматься менторством и спонсорством, привносить инженерный взгляд в решения, исследовать новые
направления и координировать работу так, чтобы проекты двигались вперёд. Программирования при этом
меньше, чем раньше (…). Ещё он отмечает, что в некоторых компаниях модели технического лидерства нет и
каждого опытного инженера подталкивают к менеджменту (…).

### 2. Case: Rafael's question (subject-first skeleton, rhetorical question buried mid-paragraph)

**Before.** Rafael Duarte, senior-инженер в Orders, проиграл роль руководителя Orders Priya Raman (глава
2); с недели 2 он делит владение ревью для core/order-capture. После первого квартала он спрашивает
директора, пробовать ли снова пойти в менеджмент или двигаться к staff-инженеру. […] Два касаются
Northstar, и Northstar не проходит ни по одному: нет ни вакансии, ни определённой роли staff-инженера, и
не назван путь назад из менеджмента. Однажды проиграв эту роль, тянется ли он к самой работе или к
должности?

**After.** Роль руководителя Orders, на которую претендовал Rafael Duarte, senior-инженер этой команды,
досталась Priya Raman (глава⍽2); с недели⍽2 он делит владение ревью для core/order-capture. После первого
квартала он спрашивает директора: попробовать снова пойти в менеджмент или двигаться к роли
staff-инженера? […] Два касаются Northstar, и по обоим Northstar не проходит: нет ни вакансии, ни
определённой роли staff-инженера, и путь назад из менеджмента не назван. Rafael однажды уже проиграл эту
роль. Что его тянет: сама работа или должность?

## Term proposals

| Current | Proposal | Reason |
|---|---|---|
| область ответственности (scope) | allow «зона ответственности» as a variant | about 25 uses in the chapter; the long form makes table cells and lists heavy. Kept as is here |
| определённая роль / определённый мандат (defined) | «описанная роль», «чётко определённый мандат» | «определённый» also means "a certain"; «определённая роль staff-инженера» can read as "some particular role". Kept for consistency |
| руководитель разработки высшего уровня (engineering executive) | keep, but allow «руководитель высшего уровня» after first use | the chapter already does this; record it as the rule |
| посыльный (manager-of-managers layer that only relays) | «передаточное звено» | idiomatic Russian for a layer that only passes messages; applied here |
| проиграл роль | «роль досталась другому», «ему предпочли X» | «проиграть роль» is a calque of "lost the role to"; applied in the case and in A1 |

## Meaning doubts (not changed in meaning; check against the English)

1. **Decision framework vs case: 3 + 3 or 4 + 2?** The framework says «Первые три описывают человека и
   работу; последние три — организацию», but the case says «Четыре критерия касаются самого Rafael… Два
   касаются Northstar». The sixth criterion (motive check) is about the person, so the case looks right and
   the framework sentence may be wrong in the English or the translation.
2. **«Мера, снятая в этом квартале, засчитывает заслуги предыдущему руководителю».** Kept as «Замер этого
   квартала засчитывает заслуги предыдущему руководителю». If the English means "credits the current
   manager with the previous manager's work", the Russian should say so.
3. **Case opening «одно решение, принятое в квартале 2».** The case only poses Rafael's question; no
   decision is taken. If the English says "one decision in quarter 2" (to be made), «принятое» is wrong.
4. **«в прошлом квартале это было 7 из 17 пунктов».** Edited to «команды выполнили 7 из 17 пунктов,
   взятых в обязательства». Confirm that 7 is the delivered count and that it is aggregated across teams.
5. **Trade-offs: «зависят от суждения и контекста оценивающего».** Edited to «требуют от оценивающего
   суждения и знания контекста». If the English means the evaluator's own context biases the result, the
   edit loses that.
6. **VP failure mode «нет влияния на уровне коллег»** → «нет влияния среди коллег». If "peer-level
   influence" means influence among executive peers, «среди коллег в высшем руководстве» would be exact.
7. **Exercise A3 last sentence.** «Скажите, как руководителю разрешать разногласие со staff-инженером…»:
   kept the manager as the one who resolves it. If the English asks how such disagreements get resolved
   (a process), the Russian narrows it.

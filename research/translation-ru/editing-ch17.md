# Literary editing notes: chapter 17

File: `docs/parts/04-execution/17-predictability-and-managing-uncertainty.ru.md`. Edited from the Russian text
only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `git show HEAD:<file>`
(294 tokens, NBSP normalised); link targets (35), `{ #anchors }` (27), exercise labels, admonition types,
Mermaid blocks, the `text` code block and every number inside tables are identical. Link text changed once
(«Хроника года 1» → «хроника года 1», mid-sentence). One table cell reworded (planning poker, «Что это»).
Failure-mode labels «Признак:» / «Противоядие:» → «Как заметить:» / «Что делать:»; heading «Торг за
оценку» → «Торг вокруг оценки». About fifteen NBSPs moved to the label side («неделе 4⍽принимает» →
«неделе⍽4 принимает», «квартале 2,⍽умножает», «глава 37⍽встраивает», «строку 1⍽одним»); «к дню 90» →
«к Дню⍽90» (fixed label).

Section 2a patterns appeared as expected (scale openers «На уровне команды / организации / руководства» →
«Для команды…»; missing connectives; «Решения — на странице» → «Разборы упражнений»). Only new patterns
follow.

## 1. Patterns new beyond section 2a

### 1.1 Reflexive «свой» with no antecedent ("in their quarter")

"Committed items delivered in their quarter" came through as «в своём квартале», where nothing in the
sentence owns the quarter. Use the meaning: the promised quarter.

- «Какую долю пунктов с обязательством мы поставили в своём квартале…?» → «…в обещанном квартале…?»
- «В Northstar в своём квартале выходили примерно четыре из десяти пунктов» → «В Northstar в обещанном
  квартале выходили примерно четыре пункта с обязательством из десяти»

### 1.2 "Three readings matter" and other English signposts for a numbered list

- «Важны три прочтения. Первое:…» (after a table) → «Из таблицы следуют три вывода. Первый:…»
- «Выход из петли и организует главу:» → «Выход из этой петли задаёт план главы:»
- Intro: a bare list of three infinitives after «как отвечать честно:» → «Для этого нужно три вещи:…»

### 1.3 Compressed English predicates that Russian cannot hold

- «Третье: моделирование уже реальности.» ("the simulation is narrower than reality") → «Третий: диапазон
  моделирования уже реального.» (same fix in Key Takeaways)
- «…какую вероятность несёт дата через восемь недель» → «…какова вероятность успеть к дате через восемь
  недель»
- «какое решение питает каждый из них» → «на какое решение работает каждый из них»

### 1.4 Quotation as subject, predicate at the end

"'X?' and 'Y?' are outside-view questions" put two long questions before the verb.

- «„Какую долю…?“ и „Насколько выросли…?“ — это вопросы взгляда снаружи.» → «Взгляд снаружи задаёт
  вопросы вроде „Какую долю…?“ и „Насколько выросли…?“.»
- «Давление „возьмите обязательство по цели“ — это давление дать обещание, которое…» → «Когда на вас
  давят: „возьмите обязательство по цели“, — от вас требуют обещания, которое…»

### 1.5 Ambiguity from homonyms the translation created

- «Некоторые практики отказываются от оценок» (practices or practitioners?) → «Некоторые
  специалисты-практики обходятся без оценок»
- «другие функции добавляют свои запасы» (departments) next to «от двух функций с датами» (features) in
  the same section → «другие подразделения закладывают свои запасы»
- «Чего стоило бы перенести самое трудное неизвестное на следующую неделю?» reads as "postpone" → «Чего
  стоило бы заняться самым трудным неизвестным уже на следующей неделе?» (see doubt 3)

### 1.6 Chained relative/participial description of a method

- «…превратил взгляд снаружи в метод под названием прогнозирование по референтному классу
  (reference-class forecasting) из трёх шагов: выбрать…» → «…превратил взгляд снаружи в метод —
  прогнозирование по референтному классу (reference-class forecasting). Метод состоит из трёх шагов:…»
- «„надбавки…“, основанные на перерасходе прошлых проектов того же типа и растущие по мере снижения
  терпимости к перерасходу» → «Их размер брали из перерасхода прошлых проектов того же типа, и чем меньше
  перерасхода готовы были допустить, тем больше была надбавка.»

## 2. Two showcase paragraphs

### 2.1 Mental model, the loop

**Before.** Наиболее вероятная оценка становится обещанием без поправки на разброс исходов, поэтому её
срывают примерно в половине случаев, даже если сама оценка была хорошей. Каждый срыв снижает доверие, а
сниженное доверие приносит давление в пользу дат, которые звучат приемлемо, и сдвигает следующую оценку
раньше. Обзор Jørgensen называет это оцениванием при конфликтующих целях: когда оценка должна ещё и
понравиться руководителю или выиграть тендер, реализм проигрывает (…).

**After.** Наиболее вероятная оценка превращается в обещание без поправки на разброс исходов, поэтому её
срывают примерно в половине случаев, даже если сама оценка была хорошей. Каждый срыв подрывает доверие.
Чем меньше доверия, тем сильнее давят в пользу дат, которые звучат приемлемо, и следующая оценка
сдвигается ещё раньше. В обзоре Jørgensen это названо оцениванием при конфликтующих целях: если оценка
должна ещё и понравиться руководителю или выиграть тендер, реализм проигрывает (…).

### 2.2 Example, reading the simulation

**Before.** Важны три прочтения. Первое: точечный план отстоит от медианы моделирования не больше чем на
неделю, как и должно быть; моделирование добавляет то, что означает медиана, — шанс 50 процентов.
Второе: 44 задачи весьма вероятно будут сделаны к неделе 26, но версия на 55 задач, которой, согласно
истории, стоит ожидать, укладывается только примерно в пяти прогонах из шести: риск для продления — в
росте объёма, а не в пропускной способности. Третье: моделирование уже реальности.

**After.** Из таблицы следуют три вывода. Первый: точечный план расходится с медианой моделирования не
больше чем на неделю, как и должно быть; моделирование добавляет понимание того, что значит медиана, —
шанс 50 процентов. Второй: 44 задачи к неделе 26 весьма вероятно будут сделаны. Но версия на 55 задач —
а именно её, судя по истории, и стоит ожидать — укладывается в срок лишь примерно в пяти прогонах из
шести. Риск для продления — в росте объёма, а не в пропускной способности. Третий: диапазон
моделирования уже реального.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| пункт (дорожной карты) с обязательством | keep; allow «обещанный пункт» in prose after first use | the full form appears ~15 times and makes sentences long |
| в своём квартале (committed items) | «в обещанном квартале» | see 1.1; check chapters 15, 16, 27 for the same phrase |
| Торг за оценку | «Торг вокруг оценки» | «торг за» means bargaining to obtain something |
| упорядочивать (неопределённую работу) | «выстраивать» in prose; either is fine | «упорядочивать» repeated five times; varied here, the meaning is the same |
| бизнесовая неопределённость (playbook) | «неопределённость в бизнесе» | «бизнесовый» is colloquial |
| руководитель продукта (F1) | «продакт-менеджер» if the English is "product manager" | the term base fixes «продакт-менеджер»; not changed |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Walking skeleton, Cockburn.** «описывает тонко связанную работающую архитектуру» was unclear; now
   «описывает его как тонкую, связанную и работающую архитектуру». Confirm the English adjectives.
2. **Playbook step 7.** «Если эти люди на критическом пути, сократите объём»: read as the people doing the
   onboarding (consistent with the Brooks section) and rendered «Если эти наставники стоят на критическом
   пути». If the English means the added people, revert.
3. **Reflection question 5.** «перенести самое трудное неизвестное на следующую неделю» read as "bring it
   forward to next week" («заняться… уже на следующей неделе»). If the English means something else,
   adjust.
4. **Story points paragraph.** «Некоторые практики отказываются от оценок» read as practitioners (the
   #NoEstimates camp), not practices.
5. **Why this matters, organization.** «другие функции» read as other departments («подразделения»).
6. **Case.** «Greg Tanaka использовал несколько дат в открытых сделках» → «назвал несколько этих дат в
   открытых сделках»: assumes the dates are the roadmap dates just mentioned.
7. **Example, assumption 1.** «пять инженеров Orders и два веб-инженера Customer Experience, половина
   численности Orders»: seven people are said to be half of Orders (14 in `teams.csv`), so the seven
   include the two Customer Experience engineers. Arithmetic consistent; wording kept.

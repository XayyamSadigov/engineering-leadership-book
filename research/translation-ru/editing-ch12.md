# Literary editing notes: chapter 12

File: `docs/parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.ru.md`.
Edited from the Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the digit sequence (sorted) is identical to `git show HEAD:<file>`, and
the sorted number tokens differ only in trailing punctuation; link targets, citation link texts,
`{ #anchors }`, exercise labels, admonition types, Mermaid ids and edges, table shapes and every number in
tables are identical (scripted diff). No heading or Mermaid label changed. Failure modes now use the
labels «Как заметить:» / «Что делать:» (were «Сигнал:» / «Противодействие:»). Label numbers now carry a
non-breaking space after the word («Неделя⍽14, начало квартала⍽2», «на неделе⍽4»).

## 1. Patterns new beyond glossary section 2a

### 1.1 «который понимает один человек» for "only one person understands"

The chapter used «понимает / понятный одному человеку» five times for a script or system. In Russian
«понимать скрипт» sounds like reading comprehension. Use «разбираться в».

- «развёртывание shell-скриптами, которое понимает один человек» → «…в котором разбирается один человек»
- «один скрипт, понятный одному человеку, развёртывает…» → «один скрипт, в котором разбирается один
  человек, развёртывает…»
- A2: «Единственный инженер инфраструктуры, который понимает общий скрипт» → «…который разбирается в
  общем скрипте»

### 1.2 "Firstly / Secondly" findings as neuter ordinals after a masculine noun

«Отсюда три вывода. Первое: … Второе: … Третье: …» — the noun is «вывод», so the ordinals must agree.
Same in ch02. Fixed to «Первый: … Второй: … Третий: …». Where no noun precedes, use «Во-первых, …
Во-вторых, …» (the bus-factor conclusions, split into their own paragraph).

### 1.3 Evidence label glued to the citation with a colon

English "…(Source): documented practice, one company's self-report." came through as «(…):
**задокументированная практика**, самоотчёт одной компании». Russian reads the colon as introducing an
explanation of the preceding sentence. Make the label its own sentence.

- «(…): **задокументированная практика**, самоотчёт одной компании.» → «(…). Это **задокументированная
  практика**, о которой одна компания сообщает сама.»
- «Это **мнение эксперта** близко ложится на четыре вопроса хартии.» (label as attributive noun phrase)
  → «Это **мнение эксперта**, и оно близко ложится на четыре вопроса хартии.»

### 1.4 Hypothetical setup packed into a participial subject

- «У ранбука, который обучающийся написал после вызова, разобранного в паре, а эксперт поправил, есть
  известный читатель…» → «Допустим, вызов разобрали в паре, после этого обучающийся написал ранбук, а
  эксперт его поправил. У такого ранбука есть известный читатель…»
- «Четыре часа парной работы в неделю от каждого из трёх экспертов — примерно 0,3 FTE» → «Если каждый из
  трёх экспертов тратит на парную работу четыре часа в неделю, это примерно 0,3 FTE»

### 1.5 Sentence opening with a lowercase code name

«export-svc развёртывается общим shell-скриптом…» starts a Russian sentence with a lowercase Latin token.
Add the generic noun: «Сервис export-svc развёртывается…». In X1 the same fix: «Это компонент tier 2:…»
instead of a second sentence starting with «search-svc —».

### 1.6 "Decisions it raises" in a case → «вопросы»

Extends 2a.6. «Черновик поставил перед директором три решения» and «описывает черновик и решения,
которые тот поднимает» → «три вопроса», «вопросы, которые тот ставит». The three items were then turned
into actual questions with question marks, which also removed «является ли…».

## 2. Two showcase paragraphs

### 2.1 Mental model, second paragraph

**Before.** Поэтому тест для любого командного документа один: назовите момент, когда его кто-то
прочитает. Хартию читают, когда приходит запрос, который, возможно, не относится к команде; соглашение
— на ретроспективе, где его проверяют; ранбук (runbook) — во время того вызова, для которого он
написан. Документ без такого момента деградирует, а как только люди узнают, что он устарел, они
перестают к нему обращаться, даже когда он верен.

**After.** Отсюда единственный тест для любого командного документа: назовите момент, когда его кто-то
прочитает. Хартию читают, когда приходит запрос, который, возможно, не к этой команде; соглашение — на
ретроспективе, где его проверяют; ранбук (runbook) — во время того самого вызова, для которого он
написан. Документ без такого момента ветшает. А узнав однажды, что он устарел, люди перестают к нему
обращаться, даже когда он верен.

### 2.2 Engineering example, the shell-script paragraph

**Before.** Развёртывание shell-скриптами устроено иначе: один скрипт, понятный одному человеку,
развёртывает auth-svc, webhooks, document-store и export-svc. Это bus factor, равный 1, сразу для
четырёх сервисов. INC-416 показал эту связанность: изменение скрипта сломало откат для всех четырёх.
Здесь распространение знаний — неверный первый шаг. Долговечное решение — убрать скрипт, перейдя на
стандартный пайплайн (глава 23); работа со знаниями лишь прикрывает месяцы до этого.

**After.** С развёртыванием shell-скриптами всё иначе: один скрипт, в котором разбирается один человек,
развёртывает auth-svc, webhooks, document-store и export-svc. Это bus factor, равный 1, сразу для
четырёх сервисов. Насколько они связаны, показал INC-416: изменение скрипта сломало откат у всех
четырёх. Начинать здесь с распространения знаний — ошибка. Долговечное решение — убрать скрипт и
перейти на стандартный пайплайн (глава 23), а работа со знаниями лишь прикрывает месяцы до этого
перехода.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| рабочие соглашения, соблюдение которых команда обеспечивает сама (heading, objective) | keep in the heading; in prose «соблюдать его участники требуют друг от друга» | the nominal «обеспечивать соблюдение» is bureaucratic; used once in prose now |
| предложение знаний ("supply of knowledge", CTO section) | «запас знаний» or rephrase | «предложение» collides with "sentence/proposal"; kept for meaning, flagged |
| момент использования ("point of use") | keep | recurring term of the chapter (heading «Записать в момент использования»); consistent |
| маршрутизация (работы, ревью) | keep | ties to «правило маршрутизации» of chapter 3 |
| «владеет» in «два списка «владеет»» | changed to «владеем» | matches the charter row label «Владеем» in the case table |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Why this matters, executive paragraph.** «риск для баланса, который никогда не появляется в
   балансе» (a pun on "balance-sheet risk") rendered «риск для активов компании, который никогда не
   отражается в балансе». Check that "balance-sheet risk" means risk to the company's assets, not
   financial-reporting risk.
2. **Rigby et al.** «снижало ожидаемые потери до 15%» kept as is; Russian «до» is ambiguous between
   "to 15%" and "by up to 15%". Same ambiguity as before the edit. «В плохом случае» rendered «В неудачном
   случае»: if the English says "worst case", «в худшем случае» is better.
3. **Staff-инженеры как распространители.** «превращать повторяющиеся ответы в документы с владельцами
   и ревью силами других» kept: unclear whether "reviews by others" is a second output (others do the
   reviews) or a property of the documents (reviewed by others).
4. **Trade-off «Записанная хартия против гибкости».** «будут цитировать команде, когда помочь было бы
   удобно»: who quotes the charter to whom (the team to refuse others, or others at the team) is unclear
   in the Russian; kept the ambiguity.
5. **Working agreement 4** «остальные планируют без него»: "without him" (the person on interrupt duty) or
   "without them" (the requests)? Kept literally.
6. **Case, export-svc question.** «учитывая, что он относится к tier 3» rendered «с учётом того, что
   export-svc относится к tier 3»: kept neutral; if the English is concessive ("even though"), «хотя»
   would be sharper.

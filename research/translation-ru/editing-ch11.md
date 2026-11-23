# Literary editing notes: chapter 11

File: `docs/parts/03-high-performing-teams/11-high-performance-trust-safety-and-accountability.ru.md`.
Edited from the Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens (197) is identical to
`git show HEAD:<file>` (NBSP normalised); link targets, citation link texts, `{ #anchors }`, exercise
labels, admonition types, Mermaid node ids and table shapes and numbers are identical (scripted diff).
Failure Modes now use «Как заметить:» / «Что делать:»; two entries that had no labels («Безопасность как
щит», «Безопасность измеряют, а не строят») were split into failure + sign + remedy without adding
content. One table cell: «Защищайте; не стандартизируйте до потери» → «Защищайте; не задушите
стандартизацией». The thousands separator in «1 118» was a plain space; now U+00A0 (glossary rule 5).

As in chapter 10, the translation was accurate; the edits are syntax and a few genuine ambiguities. Only
patterns beyond glossary section 2a and the chapter 6 and 10 notes are listed.

## 1. New patterns

### 1.1 Nominative = accusative: who broke what

Russian neuter nouns and «это» have the same form in subject and object, so a literal word order can flip
the meaning.

- «признать «это сломало моё изменение»» (reads as "this broke my change") → «признать «это сломалось из-за
  моего изменения»»
- Watch the same trap with «решение», «изменение», «правило» as both subject and object in quoted speech.

### 1.2 Homonyms with fixed terms: «совет директора» / «совет директоров»

«Черновик совета директора состоял из трёх частей» — in a book where «совет директоров» (board) is a term,
«совет директора» (the director's advice) is misread. → «Директор набросал рекомендацию из трёх частей.»
Likewise «эффективность команды» for team efficacy collides with «высокая эффективность» (performance),
the chapter's title term: → «Вера команды в свои способности (эффективность команды)».

### 1.3 Participle phrase as conditional subject → «если»

English "Candor rewarded with results makes…; a problem raised and ignored teaches…" was rendered with
participles. Russian wants two conditions.

- «Откровенность, вознаграждённая результатом, делает команду откровеннее; проблема, которую подняли и
  проигнорировали или за которую наказали, учит молчанию.» → «Если откровенность приносит результат,
  команда становится откровеннее. Если проблему подняли, а её проигнорировали или наказали за неё,
  команда учится молчать.»
- «Предложение, которое игнорируют, когда его делает один человек, и принимают, когда его повторяет
  другой, учит первого замолчать.» → «Если предложение игнорируют, пока его высказывает один, и принимают,
  когда его повторяет другой, первый учится молчать.»

### 1.4 "The test is not X. It is Y." split across two sentences

- «Тест на безопасность — не то, насколько приятны встречи. А то, куда плохие новости приходят первыми…» →
  «Безопасность проверяется не тем, насколько приятны встречи, а тем, куда плохие новости приходят
  первыми…» (a sentence starting with «А то, куда» has no predicate)

### 1.5 Coined verbal adjectives: «проговариваемыми», «защитимо»

- «Безопасность делает проблемы проговариваемыми, но не видимыми.» → «Безопасность позволяет говорить о
  проблемах, но не делает их видимыми.» (also in Key Takeaways, kept identical)
- «— защитимо» → «— это утверждение можно отстоять»

### 1.6 Sentence starting with a numeral

«17 почти-инцидентов — сигнал безопасности» → «Записанные 17 почти-инцидентов — сигнал безопасности»;
«Её 64 флага и настройки платёжного шлюза правили…» → «Свои 64 флага и настройки платёжного шлюза
команда правила…» (object first as theme, but a word in front of the numeral).

## 2. Two showcase paragraphs

### 2.1 Comfort, liking and silence

**Before.** **Симпатия — не безопасность.** В команде, которая любит своего руководителя, критика
руководителя может ощущаться как предательство друга, поэтому опасения остаются невысказанными или идут в
обход руководителя. **Отсутствие конфликтов — тоже не безопасность.** Месяцы ревью дизайна без
разногласий обычно означают, что разногласия стали дорогими; конфликт разобран в главе 6. Тест на
безопасность — не то, насколько приятны встречи. А то, куда плохие новости приходят первыми и сколько
времени им на это нужно.

**After.** **Симпатия — не безопасность.** Если команда любит своего руководителя, критиковать его может
казаться предательством друга, и опасения либо остаются невысказанными, либо идут в обход руководителя.
**Отсутствие конфликтов — тоже не безопасность.** Если месяцами на ревью дизайна нет разногласий, обычно
это значит, что не соглашаться стало дорого (о конфликте — глава 6). Безопасность проверяется не тем,
насколько приятны встречи, а тем, куда плохие новости приходят первыми и сколько времени им на это нужно.

### 2.2 Case: the director's reading of Orders

**Before.** Директор считал, что проблемой Orders был не страх: никого не наказывали, потому что Priya
сама брала инциденты на себя. Команде было комфортно, но своими результатами она не владела, а её
откровенность заканчивалась на руководителе. Скопировать ритуал значило добавить встречу; добавит ли она
безопасности, зависело от того, верят ли инженеры Orders, что Priya хочет слышать, что её решения были
неверны.

Черновик совета директора состоял из трёх частей. Первое: Priya наедине просит каждого senior-инженера
назвать одно решение, которое ей следовало принять иначе, и действует по одному ответу до появления
каких-либо новых встреч.

**After.** По мнению директора, проблема Orders была не в страхе: никого не наказывали, потому что Priya
сама брала инциденты на себя. Команде было комфортно, но своими результатами она не владела, а её
откровенность заканчивалась на руководителе. Скопировать ритуал значило добавить встречу. А прибавит ли
она безопасности, зависело от того, верят ли инженеры Orders, что Priya действительно хочет слышать о
своих неверных решениях.

Директор набросал рекомендацию из трёх частей. Первая: Priya наедине просит каждого senior-инженера
назвать одно её решение, которое следовало принять иначе, и действует по одному из ответов ещё до того,
как появятся какие-либо новые встречи.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| эффективность команды (team efficacy) | «вера команды в свои силы» (коллективная эффективность) | collides with «высокая эффективность» (performance); used once here with both in the text |
| высказывание (voice) | «готовность высказываться (voice)» | «высказывание» first reads as "a statement"; the chapter already says «готовность высказываться» in prose |
| «Приятная, небезопасная вверх» | «Приятная, но молчит наверх» | the current label is a calque and hard to parse; kept for diagram consistency |
| ручка (dial) | keep; «регулятор» as alternative | works in the mental model once the image is set |
| авторские (decision-table names) | «рекомендация книги» | the other evidence labels are fixed in glossary 4.3; «авторские» is the only free form left. Kept per notes-t2 |
| почти-инцидент (near miss) | keep | reads well, glossed on first use |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«это сломало моё изменение»** rendered «это сломалось из-за моего изменения». Confirm the English is
   "my change broke this".
2. **Edmondson 1999 row.** «Эффективность команды (вера в её способности)» = team efficacy, not team
   performance? Rendered «Вера команды в свои способности (эффективность команды)».
3. **Skip-level paragraph.** «верните его с разрешения инженера и поработайте с руководителем как коуч» —
   «верните» had no addressee; rendered «Верните его руководителю команды». Check.
4. **Orders after the transition.** «скажет ли теперь команда Priya то, что сказала новичку» — «новичку» is
   read as the new director (the case says the seniors spoke to him first). Rendered «новому директору».
5. **Payments case.** «Около двух лет команда … проводила» (past) next to present-tense description;
   rendered «проводит». If the English is past ("had run"), revert.
6. **Research table, Google row, «Чего не показывает»: «Рецензирования»** → «Не прошло рецензирования».
   Check the English cell is "peer review".
7. **F1** says «каждое из трёх утверждений», but the quote has four sentences (the safety claim plus three
   supports). Probably fine; check the English count.
8. **Payments gap.** «два из шести её инцидентов … были изменениями конфигурации» → «были вызваны
   изменениями конфигурации». Same fact, but check "were config changes".
9. **CTO paragraph.** «задаёт безопасность организации эффективнее, чем её сможет восстановить любая
   программа обучения» → «задаёт уровень безопасности в организации сильнее, чем потом сможет восстановить
   любая программа обучения». Check that "sets … more than any training can restore" is the sense.

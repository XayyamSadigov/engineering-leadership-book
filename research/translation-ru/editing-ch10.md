# Literary editing notes: chapter 10

File: `docs/parts/02-people-management/10-motivation-retention-and-senior-engineers.ru.md`. Edited from the
Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens (186) is identical to
`git show HEAD:<file>` (NBSP normalised); link targets, citation link texts, `{ #anchors }`, exercise
labels, admonition types, Mermaid node ids and table shapes and numbers are identical (scripted diff).
Failure Modes now use «Как заметить:» / «Что делать:» instead of «Сигнал:» / «Противодействие:», and each
«Что делать» is an imperative. One Mermaid label changed: «Предложить решение, не деньги» → «Исправить
причину, не деньгами» («решение» = solution/decision, 2a.6). One table header: «Как отказывает» → «Где
подводит». Label NBSPs added after «главе», «неделе», «квартале» (2a.8).

The translation was accurate and clean in vocabulary. Below are only the patterns not already in glossary
section 2a or the chapter 6 notes.

## 1. New patterns

### 1.1 English reduced clause as subject → «если»

English "A question that only asks X misses Y" / "An organization that records one reason doesn't see Z"
came out as a noun subject with a «который» clause and a verb of perception. Russian wants the condition
first.

- «Вопрос на выходном интервью, который звучит только как «чем вы были недовольны?», упускает первый
  тип.» → «Если на выходном интервью спрашивать только «чем вы были недовольны?», уходы первого типа
  останутся незамеченными.»
- «Организация, которая записывает одну причину ухода, выбранную из выпадающего списка в последний
  день, не видит этих скоплений…» → «Если организация записывает одну причину ухода, выбранную в
  последний день из выпадающего списка, она этих скоплений не видит…»

### 1.2 List of indirect questions as the subject of a nominal predicate

«Могут ли…, кто…, исправляет ли… — решения высшего руководства.» The reader holds three clauses waiting
for a verb and gets a noun. Close with a pronoun and a verb.

- «Могут ли руководители делать контрпредложения, кто их утверждает и исправляет ли бюджет недоплату
  проактивно — решения высшего руководства.» → «…исправляет ли бюджет недоплату заранее — всё это
  решает высшее руководство.»
- «То, как это будет воспринято, решает объяснение причин и того, что эксперт получает взамен» → «Как
  это будет воспринято, зависит от того, объясните ли вы причины и что эксперт получит взамен»

### 1.3 Two alternatives packed into one sentence with inner dashes

«либо вы недоплачивали — тогда исправьте…, — либо покупаете время — тогда используйте…» — four dashes in
one sentence. Announce the fork, then one sentence per branch.

- → «Если вы готовы заплатить эту сумму только из-за оффера, возможны два случая. Либо вы недоплачивали —
  тогда исправьте это для всех в таком же положении. Либо вы покупаете время — тогда потратьте его на
  то, чтобы устранить зависимость.»

### 1.4 Calqued adjectives: "ranked", "transferable", "proactively"

- «ранжированный список «главных причин…»» → «рейтинг «главных причин…»»
- «Переносимое предупреждение: …» → «На другие условия переносится одно предупреждение: …»
- «исправляет ли бюджет недоплату проактивно» → «…заранее»

### 1.5 "Costs months of X" as a noun chain

- «Каждый нежелательный уход стоит месяцев пустующего места и выхода на полную продуктивность» →
  «…стоит месяцев: пока место пустует и пока новый человек выходит на полную продуктивность»
- «Отпустить человека стоит месяцев и риска» → «Отпустив человека, вы платите месяцами и риском»

### 1.6 «Ваши реакции:» and similar English list lead-ins

«Ваши реакции:», «Сигналы, которые может наблюдать руководитель:» read as headings of a form. → «Ваши
действия:», «Что может заметить руководитель:».

## 2. Two showcase paragraphs

### 2.1 Counter-offers: the evidence

**Before.** Контрпредложение — улучшенные условия, которые предлагают, чтобы удержать человека,
подавшего заявление об уходе или получившего внешний оффер. Доказательств мало. Единственное
рецензируемое исследование, которое нашли авторы книги, — о 650 преподавателях исследовательских
университетов США — описывает предложения об удержании как дискреционные и часто несправедливые. Женщины
и преподаватели из расовых меньшинств реже получали их, а желание уйти и сообщение об этом руководству
были связаны с получением предложения (…). Об инженерах оно ничего не говорит, как и о том, остались ли
удержанные. Широко повторяемые цифры… исходят от рекрутинговых компаний с нераскрытыми методами; эта
книга их не повторяет, и доказательства скудны. Переносимое предупреждение: контрпредложения
вознаграждают тех, кто просит, а не обязательно тех, кому недоплачивают, или самых ценных.

**After.** Контрпредложение — улучшенные условия для человека, который подал заявление об уходе или
получил внешний оффер; цель — его удержать. Доказательств здесь мало. Авторы книги нашли единственное
рецензируемое исследование — о 650 преподавателях исследовательских университетов США. По его данным,
предложения об удержании делаются на усмотрение руководства и часто несправедливо. Женщины и
преподаватели из расовых меньшинств получали их реже, а получение предложения было связано с тем, хотел
ли человек уйти и сообщал ли об этом руководству (…). Об инженерах исследование ничего не говорит, как и
о том, остались ли в итоге удержанные. Популярные цифры… исходят от рекрутинговых компаний, которые не
раскрывают методику; книга их не повторяет. Доказательства здесь скудны. На другие условия переносится
одно предупреждение: контрпредложения вознаграждают тех, кто просит, а не обязательно тех, кому
недоплачивают, и не обязательно самых ценных.

### 2.2 Why this matters, executive level

**Before.** На уровне высшего руководства удержание — это строка затрат и строка рисков. Каждый
нежелательный уход стоит месяцев пустующего места и выхода на полную продуктивность; дороже всего терять
тех экспертов, с которыми советуются обо всём, но которые ничем не владеют. А то, как компания обходится
с контрпредложениями, говорит каждому инженеру, является ли заявление об уходе способом получить
прибавку.

**After.** Для высшего руководства удержание — это строка затрат и строка рисков. Каждый нежелательный
уход стоит месяцев: пока место пустует и пока новый человек выходит на полную продуктивность. Дороже
всего терять экспертов, с которыми советуются обо всём, но которые ничем не владеют. А по тому, как
компания обходится с контрпредложениями, каждый инженер понимает, можно ли получить прибавку заявлением
об уходе.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| способность (capability: «ledger как способность», «отслеживайте уходы по способностям») | «область экспертизы» or «компетенция команды» in prose | «способность» in Russian is a personal trait; «уходы по способностям» reads as "by talent". Kept for consistency with other chapters |
| пути принятия решения (unfolding model) | «пути к решению уйти» | the bare phrase sounds like decision theory; the chapter means paths to quitting |
| интервью об удержании (stay interview) | keep | works; «разговор об удержании» already used once in the table as a natural variant |
| обзор талантов (talent review) | keep | glossed on first use in the decision table |
| решатель (solver) | keep | Larson's term; glossed in English once |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Hom et al.** «потеря двух из трёх экспертов по ledger обходится не вдвое дороже потери одного» —
   kept literally. If the English says "more than twice", say so: as written, a reader may read "less".
2. **Exit-data table.** «Руководители, которых оценивают по результатам, подсказывают ответы» — "results"
   of what (retention numbers, the interviews)? Kept vague.
3. **Ines.** «Её полная переработка core/customer … не профинансирована» → «Её проект полной переработки
   …». Check that "her rewrite" is a proposal she owns, not work already under way.
4. **Counter-offer bullet.** «проигранное решение» → «проигранный спор о решении». Check that the
   English means a decision that went against the person.
5. **Retention interviews in Billing.** «Двое назвали эскалации…; один, Tomasz Wierzbicki, добавил…» — the
   Russian (before and after) does not say whether Tomasz is one of the two. Kept neutral.
6. **Unfolding table.** «иногда за несколько недель» → «иногда уже через несколько недель» (after the
   event). If "within weeks" refers to the whole path to leaving, adjust.
7. **Stay interview.** «что одно вы бы изменили» → «какую одну вещь вы бы изменили»: same meaning.

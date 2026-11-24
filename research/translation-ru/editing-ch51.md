# Literary editing notes: chapter 51

File: `docs/parts/12-cto-leadership/51-enterprise-technology-strategy.ru.md`. Edited from the Russian text
only; the English chapter was not opened. Pre-edit text: `git show ru-wip:<file>`.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `ru-wip` (NBSP
normalised); link targets, citation link texts, `{ #anchors }`, heading count, exercise labels, admonition
lines, every table line and all three Mermaid blocks are byte-identical. No wrapped line starts with a
number and a period. About 60 sentence-level edits. NBSP 131 → 121: ten misplaced NBSPs that glued a
number to the following preposition («34⍽до», «$150 000⍽на», «ADR-0001⍽к», «22%⍽вместо») were moved or
dropped, per section 2a.8. Failure-mode fields are «Как заметить:» only (as in the translation).

The translation was accurate and clean; section 2a patterns (word order, missing connectives) appeared as
expected. Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Appositive inserted between commas in place of a colon or parentheses

English parenthetical appositions ("…, 25%, …", "the reverse failure, technology nobody chose, is more
common") came through as comma-separated inserts that a Russian reader parses as a list.

- «останется на уровне квартала 3, 25%, она займёт…» → «останется на уровне квартала 3 (25%), она
  займёт…»
- «Но обратный провал, технологии, которых бизнес никогда не выбирал, встречается чаще.» → «Но обратный
  провал встречается чаще: технологии, которых бизнес никогда не выбирал.»

### 1.2 "X, and never Y" lists of who absorbs a shortfall

- «Недостачу покрывает горизонт 2, который падает до 7,6 FTE, и никогда профилактика или горизонт 3.» →
  «Недостачу покрывает горизонт 2, который сокращается до 7,6 FTE, но никогда не профилактика и не
  горизонт 3.» (Same fix in the case: «…горизонт 2, но никогда не горизонт 3 и не профилактика».)

### 1.3 Hidden subject: "the strategy depends on X" where an assumption is meant

- «Значит, стратегия зависит от того, что незапланированной работы станет меньше» → «Значит, стратегия
  держится на допущении, что незапланированной работы станет меньше» (the next clause already calls it
  «этому допущению»).

### 1.4 Nouns of action that Russian prefers as a clause

- «Вы вписываете в черновик отмену своих слов» → «Вы прямо пишете в черновике, что отменяете то
  указание»
- «чтобы квартал, который морит голодом горизонт 3, был видимым решением» → «тогда квартал, оставивший
  горизонт 3 без ресурса, будет виден как решение»

### 1.5 «прочтение» for "my reading" of business choices

«Запишите своё прочтение и попросите CEO его поправить» sounds like literary criticism. Used «запишите,
как вы их понимаете» / «своё понимание», and the CEO note «моё прочтение; поправьте» → «как я это
понимаю; поправьте». Applied in all four places for consistency.

## 2. Two showcase paragraphs

### 2.1 Example: the bad year

**Before.** **Плохой год расписан заранее.** Если незапланированная работа весь второй год останется на
уровне квартала 3, 25%, она займёт около 19,8 FTE, на 2,4 больше плана. Недостачу покрывает горизонт 2,
который падает до 7,6 FTE, и никогда профилактика или горизонт 3. Горизонт 3 с его 2 FTE покупает
информацию, от которой зависят решения по годам 3 и 4. Урезав их, компания сэкономит 2,5% ресурса и будет
принимать эти решения вслепую.

**After.** **Плохой год расписан заранее.** Если незапланированная работа весь второй год останется на
уровне квартала 3 (25%), она займёт около 19,8 FTE, на 2,4 больше плана. Недостачу покрывает горизонт 2,
который сокращается до 7,6 FTE, но никогда не профилактика и не горизонт 3. Горизонт 3 с его 2 FTE
покупает информацию, от которой зависят решения по годам 3 и 4. Урезав его, компания сэкономит 2,5%
ресурса и будет принимать эти решения вслепую.

### 2.2 Why this matters, executive level

**Before.** Ответить на него может только CTO. У CTO без письменной технологической стратегии она всё
равно есть: это сумма запросов, которые первыми дошли до разработки. Совет директоров узнаёт, какой она
была, когда компания теряет продление или когда её обнаруживает due diligence (комплексная проверка)
покупателя.

**After.** Ответить на него может только CTO. Если CTO не написал технологическую стратегию, она у него
всё равно есть: это сумма запросов, которые первыми дошли до разработки. Какой она была, совет
директоров узнаёт, когда компания теряет продление или когда эту стратегию обнаруживает due diligence
(комплексная проверка) покупателя.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| «Сначала сократить, потом добавлять» | keep (as instructed; matches ch30) | first-quarter.ru «сначала сближать…» and glossary.ru stage «Сближение» still differ; maintainer to unify there |
| выборы бизнеса | keep | plural «выборы» reads as "elections" in isolation, but the chapter frames it at first use; «стратегические выборы бизнеса» would be clearer in nav or headings if ever needed |
| опцион / исполнить опцион / закрыть опцион | keep | consistent with ch45; reads naturally once glossed |
| «моё прочтение» | «как я это понимаю» | see 1.5 |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Opening sentence:** «Техническая стратегия директора определяет, как строит инженерная
   организация» rendered «как инженерной организации строить системы». "Systems" is my object for the
   intransitive «строит»; check the English says "how the engineering organization builds".
2. **Halvard paragraph, last sentence:** «Стратегия Halvard, которая даёт каждой группе одинаковую долю
   горизонта 2, позволила распределять ресурс оргструктуре» rendered «…уже отдала распределение ресурса
   оргструктуре». Assumes the English is "has let the org chart allocate" about a strategy (generic or
   hypothetical); if the English is conditional ("would let"), use «отдаст».
3. **Preface to the four bins:** «Четыре группы вынуждают идти на те компромиссы, о которых пишет
   Porter» kept with «те самые»; no change in meaning.
4. **Example, «Платформа сохраняет 4,5 FTE квартала 3»** rendered «За платформой остаются 4,5 FTE, как в
   квартале 3». Assumes "Platform keeps its quarter-3 4.5 FTE".
5. **Case, Amara's objection**: «70 из 340 проверенных ошибок были повторными отправками» kept; the
   sample is of corrections, the 340 are errors checked. Wording only.

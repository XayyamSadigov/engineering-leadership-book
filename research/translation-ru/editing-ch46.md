# Literary editing notes: chapter 46

File: `docs/parts/10-business-leadership/46-stakeholder-management-and-negotiation.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes (apart from the stale `dist/` single file, expected); the sorted list of
numeric tokens is identical before and after (263 tokens, NBSP and line wraps normalised); headings,
`{ #anchors }`, link targets, citation link texts, exercise labels, admonition lines, every table line and
both Mermaid blocks are identical. NBSP count unchanged (73). About 80 paragraph-level edits. Failure-mode
field is «Как заметить:» (the chapter has no «Что делать:»).

Only patterns new beyond section 2a follow.

## 1. Patterns new beyond section 2a

### 1.1 Triple relative clause in a definition

- Mental model: «обмен переменными, цену которых вы определили заранее, вокруг планки, которую вы записали
  до встречи, с людьми, с которыми встретитесь снова» → «обмен переменными, цену которых вы определили
  заранее. Обмен идёт вокруг планки, записанной до встречи, и с людьми, которых вы снова увидите в
  следующем квартале.»

### 1.2 Generalised "a director who…" repeated as subject

- «Директор, который выиграл одну встречу давлением, проигрывает три следующие. А директор, который один раз
  уступил…» → «Это повторяющиеся игры: кто выиграл одну встречу давлением, проигрывает три следующие. А кто
  однажды уступил…»

### 1.3 Nominal research summaries ("the side that made the first offer obtained")

- «реже вступали в конфронтацию и больше занимались совместным поиском решений. Они достигали более высокого
  совместного результата» → «реже шли на конфронтацию и чаще искали решение вместе. Совместный результат у
  них был выше»
- «участвовали ли испытуемые в рамках учебного задания» → «было ли участие для испытуемых учебным заданием»

### 1.4 "X makes Y" with an abstract subject in trade-off paragraphs

- «Проектный треугольник обменивает объём, время и стоимость» → «В проектном треугольнике объём, время и
  стоимость обменивают друг на друга»
- «Это избавляет от двух честных воспоминаний о разных сделках» → «Запись избавляет от ситуации, когда
  стороны честно помнят две разные сделки»
- «Слои различают два теста» → «Отличить один слой от другого помогают два теста. Первый: … Второй: …»

### 1.5 Pronoun with no visible owner in the playbook

- «прежде чем читать их число» → «прежде чем увидите число другой стороны»

## 2. Two showcase paragraphs

### 2.1 Anchoring research

**Before.** В аннотации описаны три эксперимента: сторона, которая делала первое предложение, получала
лучший результат, а первые предложения сильно предсказывали итоговые цены. Преимущество исчезало, когда
другая сторона сосредотачивалась на альтернативах оппонента, … (…). Отсюда правило: подготовившись, первым
делайте конкретное предложение. Если кто-то уже поставил якорь (…), не спорьте от его числа. Вернитесь к
своей цели, которую вы задали по данным до того, как услышали его число, и к тому, что он будет делать,
если вы не договоритесь.

**After.** В аннотации описаны три эксперимента: сторона, сделавшая первое предложение, добивалась лучшего
результата, а первые предложения хорошо предсказывали итоговые цены. Преимущество исчезало, если другая
сторона сосредоточивалась на альтернативах оппонента, … (…). Отсюда правило: подготовьтесь и первым
сделайте конкретное предложение. Если кто-то уже поставил якорь (…), не спорьте, отталкиваясь от его
числа. Вернитесь к собственной цели, заданной по данным ещё до того, как вы услышали его число, и к тому,
что он будет делать, если вы не договоритесь.

### 2.2 Pre-meetings trade-off

**Before.** Разговоры один на один перед групповым решением избавляют от публичных сюрпризов и позволяют
людям менять позицию, не теряя лица. Но они превращаются в лоббизм, когда тот, кого решение задевает
сильнее всех, узнаёт последним. Пусть тот, кто несёт затраты, узнаёт первым.

**After.** Разговоры один на один перед групповым решением избавляют от публичных сюрпризов и позволяют
людям менять позицию, не теряя лица. Но если тот, кого решение задевает сильнее всех, узнаёт о нём
последним, такие разговоры превращаются в лоббизм. Пусть первым узнаёт тот, кто несёт затраты.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| «сильно предсказывали» (strongly predicted) | «хорошо предсказывали» | «сильно» with «предсказывать» is unidiomatic; keeps the correlational sense |
| «ведёт себя плохо» (a target that behaves badly) | «работает плохо» | a target does not "behave" in Russian |
| интерес × влияние / влияние × интерес | keep both, as notes-t17 says | mirrors the English |
| «предложение в торге» (an estimate is not a bid) | keep; avoid «ставка», which is the glossary term for bet | |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Enterprise 2: «решают об исключениях со сроком действия»** rendered «решают об исключениях, и каждое
   исключение действует ограниченный срок»; assumes "time-limited exceptions".
2. **Alternatives: «его реалистичные альтернативы — …»** now «реалистичных альтернатив у него три»; the
   count only names the three listed.
3. **Case: «Это давление уже есть»** rendered «И это давление уже проявилось» (the cited example is from
   week 7); check the English tense.
4. **Example: «один рост объёма съедает всё…»** rendered «одно разрастание объёма»; assumes a single
   typical 20% growth.
5. **Case, Victor's role** is not restated in the case paragraph (noted in notes-t17); still so.

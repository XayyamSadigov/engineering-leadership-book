# Literary editing notes: chapter 44

File: `docs/parts/10-business-leadership/44-working-with-product.ru.md`. Edited from the Russian text only;
the English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in the
session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (275
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, every heading, table line,
admonition block and Mermaid block are identical. About 70 paragraph-level edits; edited paragraphs
re-wrapped at about 105 characters. Failure Modes keep «Как заметить:» / «Что делать:».

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives,
noun lead-ins, «который» in mid-sentence). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «В терминологии этой книги» (sibling of «в терминах»)

- «В терминологии этой книги продакт-менеджер отвечает за то…» → «В этой книге принято такое разделение:
  продакт-менеджер отвечает за то…, а руководитель разработки — за то…»

### 1.2 A long relative clause wedged inside a question

- «спрашивает, должна ли доля инцидентов, обнаруженных клиентами (…), которая в кварталах 1 и 2 держалась
  на 29 процентах, стать результатом на её дорожной карте или остаться показателем разработки» → statement,
  fact, question: «спрашивает о доле инцидентов, обнаруженных клиентами (…). В кварталах⍽1 и⍽2 эта доля
  держалась на 29⍽процентах. Стать ли ей результатом на дорожной карте продакт-менеджера или остаться
  показателем разработки?»

### 1.3 Chronology inverted by English "after"

- «Greg Tanaka назвал дистрибьютору неделю 46 … после того, как на неделе 39 Orders оценила работу» →
  «На неделе⍽39 Orders оценила … и после этого Greg Tanaka назвал дистрибьютору неделю⍽46»
- «Прогноз Orders при старте на неделе 40 ставит завершение между неделями 44 и 46» → «Если начать на
  неделе⍽40, Orders прогнозирует завершение между неделями⍽44 и⍽46»

### 1.4 Technical homonyms: «клиент» as client app versus customer

In a chapter full of customers, «в двух клиентах» (web and mobile clients) reads as "in two customers".

- «Переделка единиц измерения в двух клиентах (10)» → «в двух клиентских приложениях (10)»

### 1.5 «стоит» for the value of a prospect (sibling of ch 25 1.1, ch 35 1.1)

- «Этот клиент стоит около $300 000 в год» → «Сделка с этим клиентом оценивается примерно в $300⍽000 в год»

### 1.6 Pronoun pointing at the wrong noun at the end of a long sentence

- «…что должно быть записано в договоре…, чтобы при этом не сделать Greg его врагом» → «…причём так,
  чтобы Greg не стал врагом договора»

## 2. Two showcase paragraphs

### 2.1 Opening

**Before.** Большую часть того, что строит инженерная организация, решают до того, как инженер это увидит.
Знание разработки о том, что дёшево, что рискованно и что уже сломано, приходит слишком поздно, чтобы
изменить варианты, и единственным рычагом остаётся оценка трудозатрат, вокруг которой и разгорается спор.

**After.** Большую часть того, что строит инженерная организация, решают ещё до того, как это увидит
инженер. Разработка знает, что дёшево, что рискованно и что уже сломано, но это знание приходит слишком
поздно, чтобы повлиять на варианты. Единственным рычагом остаётся оценка трудозатрат, и спор разгорается
вокруг неё.

### 2.2 The working contract: two clauses explained

**Before.** **Нижняя планка качества** — единственное право вето у разработки, поэтому держите её
достаточно узкой, чтобы её можно было отстоять. Планку, которая охватывает всё, выторгуют по пункту за
пунктом (глава 46). **Внешние даты** — источник большинства конфликтов: дата, названная до оценки объёма,
— это обязательство, взятое за разработку без её участия, а глава 17 объясняет, почему обязательства
берут по осторожному краю прогноза. Договор делает это правило общим, а не личной жалобой разработки.

**After.** **Нижняя планка качества** — единственное право вето у разработки, поэтому держите её
достаточно узкой, чтобы её можно было отстоять. Если планка охватывает всё, её выторгуют пункт за пунктом
(глава⍽46). **Внешние даты** — источник большинства конфликтов. Дата, названная до оценки объёма, — это
обязательство, взятое за разработку без её участия, а почему обязательства берут по осторожному краю
прогноза, объясняет глава⍽17. Договор превращает это правило из личной жалобы разработки в общее.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| онлайн-контролируемые эксперименты | «контролируемые онлайн-эксперименты» | the hyphenated form reads as "online-controlled"; not changed (term from notes-t16, also in References) |
| линия ресурса (capacity line) | keep, but avoid «строка» nearby | collides with «отдельной строкой» (budget line) in the trade-offs paragraph; both kept as they stand |
| контрфактическая выгода | keep with a short gloss on first use | glossed once in the trade-offs: «её видно только в сравнении с тем, что случилось бы без discovery» |
| discovery (neuter) | keep | reads naturally after «продуктовое discovery» |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **List of features: «Эти пункты не входят в три межкомандные инициативы, которыми ограничен портфель из
   главы⍽42»** (was «…инициативы, число которых ограничивает портфель»). Assumes "the three cross-team
   initiatives the chapter 42 portfolio cap allows".
2. **Trade-offs: the gloss on «контрфактическая»** is explanatory only. Remove if the maintainer prefers
   the glossary to carry it.
3. **Step 3: «Третий ограничитель важен: если…»** names which guardrail the last sentence explains
   (abandoned carts). Assumes the English sentence refers to that guardrail.
4. **A3: «Сделка с этим клиентом оценивается примерно в $300⍽000 в год»**. Assumes "worth about $300,000 a
   year" describes the prospective deal.
5. **Case, weeks 40–41: «Keiko и директор переводят список в дорожную карту результатов»** (was «проводят
   перевод»). Same fact, made explicit.
6. **«Перенести сам метод труднее»** for the original «Сам метод переносится хуже» ("travels less well").

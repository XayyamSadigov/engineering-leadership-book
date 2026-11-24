# Literary editing notes: chapter 54

File: `docs/parts/12-cto-leadership/54-data-and-ai-strategy.ru.md`. Edited from the Russian text only; the
English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in the
session scratchpad.

Checks: `validate_book.py` passes; the numeric tokens are identical before and after (same multiset of
`[0-9]+([.,][0-9]+)?` tokens; the looser `[0-9][0-9 ,.]*` grep differs only because «недели 42 34 из 41»
used to fuse two adjacent numbers into one token, and the sentence was reordered); link targets, citation
link texts, `{ #anchors }`, heading lines, exercise labels, admonition lines, every table line and both
Mermaid blocks are byte-identical. No wrapped line starts with a number and a period. About 45
sentence-level edits. NBSP 69 → 81 (label numbers attached to the word before them). Failure-mode field is
«Как заметить:» throughout, unchanged.

Section 2a patterns appeared as expected. Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Sentences that open with a bare numeral, several in a row

The survey paragraph had four sentences starting with digits («41 человек…», «17 вставляли…», «34 из 41…»),
and one wrapped line ended in a stranded «17». Put the theme first and the count last.

- «41 человек пользуется ИИ-ассистентом для кода хотя бы раз в неделю, 29 из них — на личных или бесплатных
  аккаунтах. 17 вставляли код Northstar в чат-инструмент, 6 — данные клиентов.» → «Хотя бы раз в неделю
  ИИ-ассистентом для кода пользуется 41 человек, из них 29 — на личных или бесплатных аккаунтах. Код
  Northstar вставляли в чат-инструмент 17 человек, данные клиентов — 6.»
- «В опросе недели 42 34 из 41 еженедельного пользователя говорят…» (two numbers collide) → «В опросе недели
  42 из 41 еженедельного пользователя 34 говорят…»

### 1.2 "This does not mean X. It means Y." copied as «Это не значит… Это значит, что…»

- «Это не значит, что программа управления данными должна предшествовать всему остальному. Это значит, что
  для конкретных данных… нужна короткая проверка готовности» → «Отсюда не следует, что… Следует другое:
  конкретным данным… нужна короткая проверка готовности»

### 1.3 Adjective calques on processes: «ускоренный код», «ускоренное написание кода»

English "faster code" / "faster coding" became an adjective on the product. Russian attaches speed to the
action.

- «Ускоренный код сначала упрётся в ревью» → «Ускоренно написанный код сначала упрётся в ревью»
- «ускоренное написание кода просто выстраивается в очередь перед ним» → «ускоренно написанный код просто
  встаёт в очередь перед ним»
- «дойдёт ли до клиентов больше кода, написанного быстрее, безопасно» → «дойдёт ли до клиентов безопасно код,
  которого теперь пишут больше и быстрее»

### 1.4 A noun phrase as the subject of an event ("a competitor's demo becomes a customer date")

- «Демо конкурента превращается в дату для клиента по функции с высокой стоимостью ошибки.» → «После демо
  конкурента клиенту обещают дату по функции с высокой стоимостью ошибки.»
- «Выборка недель 40–41 нашла 340 ошибок» → «В выборке недель 40–41 нашлось 340 ошибок»

## 2. Two showcase paragraphs

### 2.1 The AI-use survey

**Before.** Ответили 63 из 80 инженеров. 41 человек пользуется ИИ-ассистентом для кода хотя бы раз в
неделю, 29 из них — на личных или бесплатных аккаунтах. 17 вставляли код Northstar в чат-инструмент, 6 —
данные клиентов. 34 из 41 еженедельного пользователя говорят, что ИИ делает их быстрее. Политики по ИИ нет.
На неделе 41 опросник по безопасности, присланный клиентом из топ-40 к продлению, спрашивал, использует ли
Northstar генеративный ИИ и попадают ли данные клиентов к ИИ-провайдерам.

**After.** Ответили 63 из 80 инженеров. Хотя бы раз в неделю ИИ-ассистентом для кода пользуется 41
человек, из них 29 — на личных или бесплатных аккаунтах. Код Northstar вставляли в чат-инструмент
17 человек, данные клиентов — 6. Из 41 еженедельного пользователя 34 говорят, что ИИ делает их быстрее.
Политики по ИИ нет. На неделе 41 клиент из топ-40 прислал к продлению опросник по безопасности:
использует ли Northstar генеративный ИИ и попадают ли данные клиентов к ИИ-провайдерам?

### 2.2 Data cascades and the readiness check

**Before.** ИИ-проекты проваливаются из-за данных чаще, чем из-за моделей. В интервью с 53 практиками ИИ
92% сообщили о каскадах данных (data cascades): проблемах с данными, которые нарастают ниже по цепочке,
проявляются поздно и которых часто можно было избежать (…). […] Это не значит, что программа управления
данными должна предшествовать всему остальному. Это значит, что для конкретных данных, которые использует
инициатива, нужна короткая проверка готовности.

**After.** ИИ-проекты проваливаются из-за данных чаще, чем из-за моделей. Из 53 практиков ИИ, с которыми
провели интервью, 92% рассказали о каскадах данных (data cascades): проблемах с данными, которые нарастают
ниже по цепочке и проявляются поздно, хотя часто их можно было избежать (…). […] Отсюда не следует, что
программа управления данными должна предшествовать всему остальному. Следует другое: конкретным данным,
которые использует инициатива, нужна короткая проверка готовности.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| ИИ-возможность (AI capability) | allow «ИИ-функция» or «применение ИИ» in prose | «возможность» reads as "opportunity"; kept for consistency with notes-t21 |
| волны смешаны с реорганизацией (confounded) | «эффекты волн неотделимы от реорганизации» | «смешаны» is opaque to a non-statistician; the next clause already explains it, so kept |
| каким инструмент ощущается | «каким инструмент кажется пользователю» | «ощущается» is a calque of "feels"; kept, as the takeaways repeat it |
| то, что скоро станет товаром (commodity) | «массовым товаром» (applied) | bare «товар» loses the "commodity" sense |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **CTO perspective: «Отвечать клиентам правдиво на основе письменной политики, а не опроса о том, что
   инженеры делают на практике».** Reads as if the survey were a poor basis for answers, while the chapter
   uses the survey as the honest baseline. If the English means "not a guess about what engineers do", the
   Russian should say so. Not changed.
2. **«Над таблицей стоят три правила»** kept. Assumes "above the table" means the rules take precedence
   over the rows.
3. **Example: «план потеряет работу двух инженеров в год, когда…»** rendered «план недосчитается двух
   инженеров в тот год, когда…». Check that "in a year" means "in the year when", not "per year".
4. **CTO perspective: «CTO говорит, что измеряла каждая из них, где…»** rendered «CTO объясняет, что и где
   измеряла каждая цифра»: wording only.
5. Case: search-svc in week 54 vs the organization change in week 53 (see notes-t21): not touched.

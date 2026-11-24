# Literary editing notes: chapter 24

File: `docs/parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (284 tokens,
NBSP normalised); `{ #anchors }`, link targets, exercise labels, admonition types, every table line and all
Mermaid blocks are byte-identical. NBSP placement around labels was already correct. Failure-mode labels were
already «Как заметить:» / «Что делать:».

About thirty-five sentences rebuilt. Section 2a patterns and the chapter 23 patterns (source as repeated
subject, gerund subjects) recurred. Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 "Questions you knew in advance to ask" (embedded object clause)

English stacks a clause inside a relative clause; Russian cannot hold «которые вы знали, что нужно задать».

- «Мониторинг отвечает на вопросы, которые вы заранее знали, что нужно задать, например четыре золотых
  сигнала…» → «Мониторинг отвечает на вопросы, известные заранее: например, о четырёх золотых сигналах…»

### 1.2 «Она… Она… Она…»: one source carried through a paragraph by a pronoun

Three or more sentences starting with «Она» (the workbook chapter) blur who says what and, after a second
feminine noun, become ambiguous («Книга… описывает проверку… Она охватывает…»).

- «Она называет минимальный состав… Она перечисляет источники… и говорит, что…» → «Там же назван минимальный
  состав… Перечислены и источники…, а дежурства…, по мнению авторов, должны оплачиваться»
- «…Production Readiness Review — проверку перед тем, как… Она охватывает архитектуру» → «Проверка
  охватывает архитектуру»

### 1.3 "Whether X — policy; whether Y — not": ellipsis that flips meaning

«оправдывает ли это резервный маршрут — нет» reads as the answer "no" to the question, not as "this is not a
policy question".

- «Должно ли это замораживать релизы — вопрос политики; оправдывает ли это резервный маршрут — нет.» →
  «Должно ли это замораживать релизы — вопрос политики. А вот оправдывает ли это резервный маршрут — вопрос
  уже не политики.»

### 1.4 Wrong aspect or verb for refusal and adaptation

- «Она отказалась от правила заморозки» ("gave up", implies she had held it) → «Она не согласилась на
  правило заморозки»
- «политика бюджета, подогнанная под сервис» («подогнать» implies fudging, clashing with «подгонка
  метрик») → «рассчитанная на сервис»

### 1.5 Number at the start of a sentence

- «15 компонентов, предложенных в tier 1, сильно не дотягивают…» → «Компоненты, предложенные в tier 1 (их
  15), сильно не дотягивают…»

### 1.6 Predicate nouns that hide the verb ("readiness theater… become either permanent or ignored")

- «заморозка проблемного сервиса становится либо вечной, либо игнорируемой» → «…либо становится вечной,
  либо её перестают замечать»
- «Распределение нагрузки на квартал обойдётся временем…» → «Если распределить нагрузку, на квартал
  придётся заплатить временем…»

## 2. Two showcase paragraphs

### 2.1 Observability

**Before.** SLO говорят вам, **что** пользователям плохо; от наблюдаемости зависит, как быстро вы узнаете,
**почему**. Мониторинг отвечает на вопросы, которые вы заранее знали, что нужно задать, например четыре
золотых сигнала из книги SRE: задержка, трафик, ошибки и насыщение (…). Наблюдаемость — это способность
задавать новые вопросы о сбоях, которых никто не предвидел; таково **мнение экспертов**, авторов из компании —
поставщика инструментов наблюдаемости (…).

**After.** SLO говорят вам, **что** пользователям плохо; от наблюдаемости зависит, как быстро вы узнаете,
**почему**. Мониторинг отвечает на вопросы, известные заранее: например, о четырёх золотых сигналах из книги
SRE (задержка, трафик, ошибки и насыщение) (…). Наблюдаемость — это способность задавать новые вопросы о
сбоях, которых никто не предвидел. Таково **мнение экспертов** — авторов из компании, которая продаёт
инструменты наблюдаемости (…).

### 2.2 On-call load (workbook chapter)

**Before.** Глава воркбука о дежурствах (on-call) ставит цель — не больше двух инцидентов за 12-часовую
смену. Она называет минимальный состав: восемь инженеров для круглосуточного графика на одной площадке или
по пять на площадку при нескольких площадках. Она перечисляет источники нагрузки вызовами (…) и говорит,
что дежурства в нерабочее время должны оплачиваться (…).

**After.** Глава воркбука о дежурствах (on-call) ставит цель — не больше двух инцидентов за 12-часовую
смену. Там же назван минимальный состав: восемь инженеров для круглосуточного графика на одной площадке или
по пять на площадку при нескольких площадках. Перечислены и источники нагрузки вызовами (…), а дежурства в
нерабочее время, по мнению авторов, должны оплачиваться (…).

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| мнение экспертов (plural) | keep here | the glossary label is «мнение эксперта»; plural is right for three authors, but the maintainer may want the fixed form |
| ревью как разговор | «ревью-разговор» where a noun is needed | used once in the readiness lessons; avoids «владение ревью как разговором» |
| посильна в долгую | «посильна на длинной дистанции» | «в долгую» is colloquial; changed |
| несут вызовы | «принимают вызовы» | "carry pages"; «нести вызовы» is a calque; changed once, «несут нагрузку» kept |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **INC-413 replay, "whether it justifies a fallback route is not".** Read as "is not a policy question" (the
   fallback is warranted regardless). If the English says the opposite (it does not justify one), the Russian
   must change.
2. **INC-413 replay, "3.7 times the budget".** «съело бы примерно в 3,7 раза больше бюджета» rendered «в 3,7
   раза больше, чем весь бюджет»: assumes 890 failures against a budget of 240 (ratio 3.7), consistent with the
   note.
3. **Error-budget policy example.** «кроме самых срочных (P0) проблем и исправлений безопасности» rendered
   «кроме исправлений самых срочных (P0) проблем и исправлений безопасности». Confirm P0 refers to issue fixes.
4. **A2, auth-svc.** «его автор ушёл» is ambiguous (the author of the scripts or of the service); kept.
5. **Rotation, escalation tier.** «Эксперты стоят за графиком дежурств» rendered «стоят за основным графиком
   как отдельный, явно названный уровень эскалации»: "named tier" read as an explicitly designated tier.

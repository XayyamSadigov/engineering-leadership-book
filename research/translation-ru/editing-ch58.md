# Literary editing notes: chapter 58

File: `docs/parts/13-advanced-problems/58-layoffs-reductions-and-mergers.ru.md`. Edited from the Russian text
only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in
the session scratchpad.

Checks: `validate_book.py` passes; the multiset of numeric tokens is identical before and after (NBSP
normalised, and digit runs compared separately); link targets, citation link texts, `{ #anchors }`, heading
lines, exercise labels, admonition lines, every table line and all three Mermaid blocks are byte-identical.
The "Не юридическая консультация" box is byte-identical (not touched). No wrapped line starts with a number
and a period. About 55 sentence-level edits. NBSP 73 → 76: label numbers now attach to the word before them
(«На неделях⍽1 и⍽2 каждая…», «к месяцу⍽6», «к месяцу⍽9», «Итоги месяца⍽6»). The only Failure Modes field
is «Как заметить:». Tone: the notification-day passages were kept plain and direct; no softening words were
added.

Section 2a patterns appeared as expected (missing connectives, English word order). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «стоит» + genitive for "costs", again (see editing-ch53, 1.1)

- «Сокращение стоит выходных пособий, юридических расходов, времени руководителей…» → «Сокращение обходится
  в выходные пособия, юридические расходы, время руководителей…»
- «нарушенное обещание „только один“ стоит больше доверия, чем сам второй раунд» → «…подрывает доверие
  сильнее, чем сам второй раунд»
- «Два лишних ухода… стоят около $215 000» → «…обходятся примерно в $215 000»

### 1.2 «является» hidden in "looks fair but is not"

- «Это выглядит справедливо, но справедливым не является: ослабляет команды, которые понесут стратегию» →
  «Это выглядит справедливо, но по сути несправедливо: такое сокращение ослабляет команды, которым предстоит
  реализовать стратегию»

### 1.3 Abstract nouns as the agent of a check ("Legal review asks…, fairness asks…")

- «Юридическая проверка спрашивает, можно ли защитить список, а справедливость — правилен ли он» →
  «Юридическая проверка отвечает на вопрос, можно ли защитить список, а проверка на справедливость —
  правилен ли он»

### 1.4 "Don't say X" lists rendered as noun fragments

The list of things a manager must not say came through as bare noun phrases («Что-либо о
результативности… И обещания…»). In Russian a prohibition needs «ничего», «никаких».

- «Что-либо о результативности, если она не была заявленным критерием, — это противоречит…» → «Ничего о
  результативности, если она не была заявленным критерием: это противоречит…»
- «И обещания о будущих раундах или повторном найме.» → «И никаких обещаний о будущих раундах или
  повторном найме.»

### 1.5 «с результативностью которых их руководители» → «с чьей результативностью»

A «которых» clause with a second possessive is heavy; «чей» fixes both.

- «убрать людей, с результативностью которых их руководители так и не поработали» → «убрать людей, с чьей
  результативностью руководители так и не поработали»

## 2. Two showcase paragraphs

### 2.1 The ownership check (example, step 3)

**Before.** По первому черновику руководителей у пяти компонентов не осталось бы никого ни с тем, ни с
другим опытом, включая сервер лицензий tier 1. Два выбора в команду поддержки меняют, и это закрывает два
из этих компонентов. Остальные три меняются реже раза в квартал: три уходящих инженера соглашаются на
оплачиваемый двухнедельный контракт на передачу дел…

**After.** В первом черновике руководителей у пяти компонентов, включая сервер лицензий tier 1, не осталось
бы никого ни с тем, ни с другим опытом. Отбор в команду поддержки меняют в двух местах, и это закрывает два
компонента из пяти. Остальные три меняются реже раза в квартал: три уходящих инженера соглашаются на
оплачиваемый двухнедельный контракт на передачу дел…

### 2.2 What not to say in the conversation

**Before.** Затем слушайте. […] Трёх вещей говорить не надо. «Мне тоже тяжело» — это поворачивает разговор
к руководителю. Что-либо о результативности, если она не была заявленным критерием, — это противоречит
названной причине и создаёт юридические риски. И обещания о будущих раундах или повторном найме.

**After.** Затем слушайте. […] Трёх вещей говорить не надо. «Мне тоже тяжело»: это переводит разговор на
руководителя. Ничего о результативности, если она не была заявленным критерием: это противоречит названной
причине и создаёт юридические риски. И никаких обещаний о будущих раундах или повторном найме.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| оставшиеся (survivors) | keep | glossed once; reads naturally and humanely |
| сокращение в рассрочку | keep | vivid and clear as a failure-mode name |
| уровень как понижение | keep | short; the body explains it |
| выпуск (output), «падение выпуска», «потерянный выпуск» | consider «объём работы» in prose | «выпуск» (term base, output) reads like manufacturing outside the outcome/output contrast; kept for consistency |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«касается последствий, а не техники»** rendered «а не методов проведения». Assumes "technique" means
   how to carry a reduction out, not technology.
2. **«вредит установкам и здоровью»** (Sverke) rendered «вредит отношению к работе и здоровью». Assumes
   "attitudes" are work attitudes (satisfaction, commitment), as in that meta-analysis.
3. **«Два выбора в команду поддержки меняют»** rendered «Отбор в команду поддержки меняют в двух местах».
   Assumes "two picks are changed".
4. **«Imani письменно обязуется, что у команды поддержки Classic есть трёхлетний мандат…»** rendered
   «письменно закрепляет за командой… трёхлетний мандат». Assumes a written commitment, not a description.
5. **«действия по ним касаются ранбуков»** rendered «корректирующие действия по их итогам». Assumes the
   English means review actions (corrective actions).
6. **F1: «ответ…, который Imani Okonkwo отправила финансам»** rendered «отправляет». The exercise asks the
   reader to write the reply, so present tense; check that the English is not a hypothetical "would send".
7. **«Скажите об этом один раз, письменно, до решения, по тесту…»** rendered «…письменно и до решения,
   следуя тесту…». Wording only.

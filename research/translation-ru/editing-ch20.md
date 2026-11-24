# Literary editing notes: chapter 20

File: `docs/parts/05-engineering-quality/20-engineering-standards-and-their-governance.ru.md`. Edited from
the Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to the pre-edit copy
(222 tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition types, all three
Mermaid blocks and every table row are byte-identical. The translation had **no non-breaking spaces at
all**; 69 were added by rule (number + counted noun, label + number: «глава⍽28», «неделе⍽4»,
«tier⍽1», «$185⍽000», «2⍽300»). Table numbers left as in English (`2,300`).

Section 2a patterns appeared as expected. Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 "Make a property true" calque

- «Стандарты позволяют организации сделать несколько свойств истинными везде…» → «…обеспечить несколько
  свойств везде…»
- «Одно и то же свойство можно сделать истинным пятью способами» → «…можно обеспечить пятью способами»

### 1.2 Three definitions packed into one sentence with parentheses

- «Стандартами управляет некоторое сочетание гильдий (добровольных сообществ…, которые…), советов (групп
  с правами на решения, которые…) и назначенных владельцев…» → «Стандартами управляет то или иное
  сочетание трёх органов. **Гильдии** — добровольные сообщества практиков: … **Советы** — группы с
  правами на решения… **Назначенные владельцы** отвечают за отдельные стандарты.»

### 1.3 "Instead" / "these" whose referent was lost in translation

- «В выборке из 40… в 38 были отмечены все пункты чек-листа, причём 11 из них меняли…» (of 38 or of 40?)
  → «…причём в 11 таких мерж-реквестах продакшен-код меняли…» (no new number introduced)
- «…поверх тех 25 процентов… Вместо этого директор засчитал эту работу внутри выделения.» → «Поэтому
  директор засчитал эту работу в счёт выделения, а не сверх него.» (see doubt 3)

### 1.4 Inanimate subject given a human verb

- «Какие из ваших стандартов могут сформулировать своё назначение одним предложением?» → «Назначение
  каких из ваших стандартов можно сформулировать одним предложением?»
- «Утверждение… должно быть правдой» kept (idiomatic); «То, какие системы относятся к tier 1, говорит о
  том…» → «Список систем tier 1 показывает…»

### 1.5 Literal "went badly"

- «Две вещи пошли плохо.» → «Две вещи пошли не так.»

## 2. Two showcase paragraphs

### 2.1 Why this matters, cost at scale

**Before.** Масштаб делает плохие стандарты ещё и дорогими. Правило, которое отнимает у каждого инженера
десять минут в неделю, обходится организации из 80 человек примерно в 690 часов в год — больше трети
инженеро-года (при допущении, что в инженеро-годе около 1 840 рабочих часов), — и это ещё до вопроса,
что оно предотвращает. … А страница из 52 обязательных правил, которые никто не соблюдает, приучает
инженеров к тому, что слово «обязательно» — для красоты, и это ослабляет те немногие правила, которые
действительно важны.

**After.** С ростом масштаба плохие стандарты становятся ещё и дорогими. Правило, которое отнимает у
каждого инженера десять минут в неделю, обходится организации из 80 человек примерно в 690 часов в год.
Это больше трети инженеро-года (если считать, что в инженеро-годе около 1 840 рабочих часов), и это ещё
до вопроса о том, что правило предотвращает. … А страница из 52 обязательных правил, которые никто не
соблюдает, приучает инженеров к тому, что «обязательно» пишут для красоты. От этого слабеют и те немногие
правила, которые действительно важны.

### 2.2 Case, what went wrong

**Before.** Две вещи пошли плохо. Первая проверка в Jenkins была запущена без вычистки накопившихся
нарушений в Core, в первый же день дала 180 падений сборки и через несколько часов была отключена;
вернулась она через две недели и ломала сборку только на новых нарушениях.

**After.** Две вещи пошли не так. Первую проверку в Jenkins запустили, не вычистив накопившиеся нарушения
в Core. В первый же день она дала 180 падений сборки, и через несколько часов её отключили. Вернулась она
через две недели и ломала сборку только на новых нарушениях.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| сделать (свойство) истинным | «обеспечить (свойство)» | calque of "make true"; add to section 2a |
| театр соответствия | keep | reads naturally next to «театр безопасности» |
| механизм обеспечения | keep, but «обеспечение соблюдения» on first use | bare «обеспечение» can read as "provisioning" |
| утверждение не глядя | keep | idiomatic for "rubber stamping" |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Opening.** «потому что так делает инструмент или привычка» → «потому что так устроен инструмент или
   так велит привычка»: wording only.
2. **19 mandatory standards.** «каждое либо проверяется, либо проверяется выборочно, либо отражается в
   отчётности» → «проверяется — сплошь или выборочно — либо отражается…». If "checked" in the English
   means "checked by a tool", «автоматически» would be more exact than «сплошь».
3. **Marcus Oyelaran, "instead".** Read as: rather than add runbook work on top of the 25 percent
   prevention allocation, the director counted it inside it. Rendered «в счёт выделения, а не сверх него».
4. **Measuring.** «доля соответствующих стандарту» → «доля соответствия стандарту»: assumes "compliance
   rate", whatever the unit.
5. **Tiering.** «публичное соответствие компонентов уровням» → «публичный список того, какой компонент к
   какому уровню относится»: assumes "a public mapping of components to tiers".
6. **Info box tense.** «Директор классифицировал… и публикует…» mixes past and present; kept as in the
   translation.

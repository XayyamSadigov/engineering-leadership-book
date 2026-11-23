# Literary editing notes: chapter 13 (pilot)

File: `docs/parts/03-high-performing-teams/13-decision-making-in-teams.ru.md`. Edited from the Russian
text only; the English chapter was not opened. Checks: the sorted list of numbers is identical before and
after; link targets, `{ #anchors }`, exercise labels, admonition types, Mermaid node ids and every number
in the tables are unchanged; `tools/validate_book.py` passes.

General impression: the translation was accurate and already clean in vocabulary. What made it read as a
translation was syntax: English word order, noun stacks, «который» clauses, and paragraphs whose logic
relied on juxtaposition. Most edits are rebuilt sentences, not new words.

## Patterns

### 1. English word order: new information first, theme last

Russian puts the known thing first and the new thing at the end of the sentence.

- «Это решение к концу первого квартала директора всё ещё оставалось открытым.» →
  «К концу первого квартала директора этот вопрос так и оставался открытым.»
- «Второй: межкомандные решения ждали дольше всех (медиана 8 дней)…» →
  «Второй: дольше всех ждали межкомандные решения (медиана 8 дней)…»
- «Глава 37 (операционная система управления) описывает ритм, в котором эти решения пересматриваются.» →
  «В каком ритме эти решения пересматривают, описывает глава 37 (операционная система управления).»

### 2. Clumsy object clauses and pronoun chains copied from English

- «Работа ждёт решения, о котором никто не знает, что оно за ним» →
  «Работа стоит в ожидании решения, хотя никто не знает, что она его ждёт»
- «…младший инженер, который знает потребителя ниже по цепочке, говорит вам наедине, что этот дизайн его
  сломает» (whose «его»?) → «…младший инженер, знакомый с потребителем ниже по цепочке, говорит вам
  наедине, что этот дизайн сломает того потребителя»
- «Проверки прав, встроенные сейчас в core/customer, в квартале 2 выносят из него, внутри Core.» →
  «В квартале 2 проверки прав, которые сейчас встроены в core/customer, выносят из этого модуля, не
  выходя за пределы Core.»

### 3. Calques: «в терминах», «играть роль», «голос / право голоса», «факты на столе»

- «В терминах DACI директор — Approver.» → «По модели DACI директор — Approver.»
- «Канал коммуникации роли не играл» → «От канала коммуникации это не зависело»
- «даёт участникам (Contributors) голос, но не право голоса при решении» (two senses of one word
  collide) → «Участники (Contributors) могут высказаться, но решающего голоса у них нет»
- «Факты на столе:» → «Известные факты:»
- «Каждая из четырёх частей ломается узнаваемо.» → «Нехватка каждой из четырёх частей проявляется
  по-своему.»

### 4. Bureaucratic register and nominal style

- «чек-лист, который лицо, принимающее решение, применяет к такой рекомендации» → «чек-лист, по которому
  тот, кто принимает решение, проверяет такую рекомендацию»
- «Группа, при отсутствии обоснованных возражений» → «Группа, если нет обоснованных возражений»
- «Выдвигают возражения, которые показывают вред» → «Возражают, указывая на вред»

### 5. Missing connectives: logic left to juxtaposition

- «За скорость платят при исполнении…» (after a list of speeds) → «Но за скорость платят при
  исполнении…»
- «Ведите его четыре недели, перепроектируйте права на решения и остановитесь.» (after the gaming
  warning) → «Поэтому ведите журнал четыре недели, перестройте права на решения и на этом остановитесь.»
- «Какая бы команда ни владела модулем, большинство изменений придут из других команд» (a conclusion from
  17 of 38) → «Значит, какая бы команда ни владела модулем, большинство изменений придёт из других команд»

### 6. One long sentence where Russian wants two, and questions packed into one

- «Kahneman… Всерьёз ли рассматривались альтернативы, выслушали ли несогласных, есть ли у команды интерес
  в исходе?» → three short questions: «Всерьёз ли рассматривали альтернативы? Выслушали ли несогласных?
  Есть ли у команды интерес в определённом исходе?»
- «Согласие задаёт другой вопрос: „Может ли каждый с этим жить, а если нет, то какой вред это
  причиняет?“» → «„Может ли каждый с этим жить? Если нет, то какой вред это причинит?“»
- The 120-word hidden-profiles paragraph (one study plus the meta-analysis) was split into two
  paragraphs, one source each.

### 7. Grammar slips the translation left

- «у каждого кандидата в владельцы» → «у каждого кандидата во владельцы»
- «изменения, которое каждая из двух команд считала проверенной другой» (agreement) → «…считала
  проверенным другой»
- «обязательство после того, как тебя выслушали» (sudden «ты» in a «вы» book) → «обязательство после
  того, как человека выслушали»

### 8. Ambiguity specific to this chapter: «решение»

In a chapter about decisions, «решение» also means "solution" and "answer". Avoid it in the second sense.

- «Решения — на странице решений к главе 13.» → «Разборы упражнений — на странице с решениями к главе 13.»
- «…а затем ставит перед читателем решение в начале квартала 2» → «…ставит перед читателем выбор…»
- «Обходное решение снимает острую боль» → «Обходной путь снимает острую боль» (also aligns with the
  term used in the diagram and the case).

### 9. Non-breaking spaces on the wrong side of a label number (mechanical, recurring)

The translation glued week, quarter, chapter and level numbers to the *following* word. Labels attach to
the word before them; the next word must be free to wrap. (Below, `⍽` marks U+00A0.)

- «Неделя 14,⍽начало квартала 2. В квартале 1⍽директор…» → «Неделя⍽14, начало квартала⍽2. В
  квартале⍽1 директор…»
- «из главы 2⍽это уровень 4⍽или 5» → «из главы⍽2 это уровень⍽4 или⍽5»
- «к дню 90⍽оставался» → «к Дню⍽90» (also the fixed label «День 90» from glossary 4.5)

Fourteen such misplacements were fixed in this chapter; expect the same in chapters 1–18 and grep for
`[0-9],?\xa0[а-я]` after «неделе/квартале/главы/tier».

## Three showcase paragraphs

**1. Why this matters, team level**

Before:
> На уровне команды медленные или неясные решения — это скрытая очередь. Работа ждёт решения, о котором
> никто не знает, что оно за ним; инженеры строят на допущениях, которые потом отменят; один и тот же спор
> возвращается, потому что прошлый никто не записал. Это видно в lead time (сколько времени проходит от
> запроса до поставки), а не в отчётах по спринтам.

After:
> На уровне команды медленные или неясные решения — это скрытая очередь. Работа стоит в ожидании решения,
> хотя никто не знает, что она его ждёт; инженеры строят на допущениях, которые потом отменят; старый спор
> возвращается, потому что в прошлый раз итог никто не записал. Всё это видно по lead time (сколько
> времени проходит от запроса до поставки), а не по отчётам о спринтах.

**2. Decision rights: DACI and RAPID sources**

Before:
> Плейбук Atlassian по DACI настаивает на одном Driver и одном Approver, даёт участникам (Contributors)
> голос, но не право голоса при решении, и фиксирует итог в общем документе (…). В описании RAPID от Bain
> сказано, что роль Agree, предназначенную для обязательных требований вроде юридических, следует
> назначать скупо. В идеале у каждого решения один решающий (…). Rogers и Blenko в статье, где они
> представили этот подход, утверждают, что результативность зависит от того, насколько быстро принимаются
> правильные решения и насколько последовательно они исполняются (…). Это **задокументированная
> практика** вендора ПО и консалтинговой фирмы. Ни один из источников не приводит доказательств того, что
> инструмент улучшает результаты, и книга таких доказательств не нашла.

After:
> Плейбук Atlassian по DACI настаивает на одном Driver и одном Approver. Участники (Contributors) могут
> высказаться, но решающего голоса у них нет, а итог фиксируется в общем документе (…). Bain в описании
> RAPID советует назначать роль Agree скупо: она нужна для обязательных требований, например юридических.
> В идеале у каждого решения один решающий (…). Rogers и Blenko в статье, где представили этот подход,
> утверждают: результативность зависит от того, насколько быстро принимают правильные решения и насколько
> последовательно их исполняют (…). Это **задокументированная практика** вендора ПО и консалтинговой
> фирмы. Доказательств того, что инструмент улучшает результаты, не приводит ни один из источников, и
> книга таких доказательств тоже не нашла.

**3. Case: reading it as decision avoidance**

Before:
> Хроника не говорит, почему решение осталось открытым, и этот кейс не придумывает объяснения. Но все
> элементы петли уклонения налицо. Владельцев компонентов назначает директор, поэтому ни в одной
> десятидневной очереди staff-инженеров этого вопроса нет. Исключение снизило риск, а вместе с ним и
> срочность. Оно заканчивается, когда решение принято, поэтому вынудить решение не может. Десятидневная
> очередь своё дело сделала: выдала исключение вовремя. Но срок был нужен самому решению о владении, и его
> даёт только предел в два квартала.

After:
> Хроника не объясняет, почему решение осталось открытым, и кейс объяснений не придумывает. Но все
> элементы петли уклонения налицо. Владельцев компонентов назначает директор, поэтому в десятидневные
> очереди staff-инженеров этот вопрос не попадает. Исключение снизило риск, а вместе с ним и срочность.
> Действует оно, пока решение не принято, поэтому подтолкнуть к решению не может. Десятидневная очередь
> свою задачу выполнила: исключение выдано вовремя. Но срок был нужен самому решению о владении, а его
> задаёт только предел в два квартала.

## Term proposals

- **«посоветоваться» as a method name.** As a noun-like label it breaks syntax («перейти на
  „посоветоваться“»). Proposal: keep the verb in tables and lists, but allow «способ с консультацией» in
  running prose where a noun is needed. Kept as is in this pilot for consistency.
- **«решить единолично»** reads well; no change.
- **«уровень сервиса для решений» (decision service level).** Long and repeated a dozen times. Proposal:
  after first use, allow the short «срок ответа» or «SLA на решения» where context is clear. Kept the full
  term in this pilot.
- **«не согласен, но действую».** Works; in prose it needs a framing noun («принцип „не согласен, но
  действую“»), which I added once in the trade-offs section.
- **«ранбук»**: the term base asks for «ранбук (runbook)» on first use on a page; this chapter never
  glosses it. Not changed (mechanical gloss, maintainer's call).
- **«записи архитектурных решений»**: the term base asks for «запись архитектурного решения (ADR)» on first
  use; the chapter never shows "ADR". Not changed.
- **«человеко-дней»** in the illustrative example: the term base has «инженеро-день» for engineer-day. If
  the English says "engineer-days", change it; if "person-days", keep.

## Meaning doubts (not changed; please check against the English)

1. **«смоделированных групп»** (Stasser and Titus). Unclear what "simulated" refers to: the groups were
   real participants deciding on simulated candidates. If the English says "simulated groups", the Russian
   is faithful but odd; if it says "in a simulated decision", the Russian is wrong.
2. **«минимальные обязательства для компонентов tier 1»** (info box) and **«минимальными требованиями к
   дежурствам»** (Kwame Mensah). Both look like the term-base concept "operational minimums" →
   «операционные минимумы». If so, both should use the term.
3. **«ни в одной десятидневной очереди… этого вопроса нет» / «может превратить его в решение, которого
   никто не ждёт»**: I kept "nobody is waiting for it" literally; if the English means "nobody is
   accountable for waiting time", a sharper wording would help.
4. **Diagram label «Владелец области смотрит»** changed to «изучает» and **«Истечение: пересмотр»** to
   «Срок истёк: пересмотр»: wording only.

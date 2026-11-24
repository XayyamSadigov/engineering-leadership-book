# Literary editing notes: chapter 31

File: `docs/parts/06-technical-leadership/31-service-boundaries-and-ownership.ru.md`. Edited from the Russian
text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in
the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (NBSP
normalised); link targets, `{ #anchors }`, every table line, the admonition title line, exercise labels and all
three Mermaid blocks are identical. About 40 sentence-level edits. Failure-mode labels were already «Как
заметить:» / «Что делать:». The translation was clean; most edits are word order, connectives, and «который»
tails (section 2a). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Comparative split across a long clause («лучше подходит X …, чем Y»)

English "X is usually better than Y" with a long X left «чем множество сервисов» stranded at the end.

- «…организации меньше чем примерно на 100 инженеров обычно лучше подходит хорошо разбитый на модули монолит с
  несколькими сервисами, выделенными по ясным причинам, чем множество сервисов.» → «…обычно лучше подходит не
  множество сервисов, а хорошо разбитый на модули монолит с несколькими сервисами, выделенными по ясным
  причинам.»
- «большинство компаний скорее переписывали код, чем разделяли существующий» → «предпочитали переписать код, а
  не разделить существующий»

### 1.2 Metaphorical verbs calqued from English ("buy", "drift", "split attention")

- «Две последние ступени покупают независимое развёртывание…, а платят за них…» → «Две верхние ступени дают
  независимое развёртывание…, но платить за это приходится…»
- «внимание двух команд раздваивается» → «внимание обеих команд разрывается между ними»
- «ставили в заслугу как раз общую инфраструктуру» → «объясняли успех как раз общей инфраструктурой»

### 1.3 A "the X that…, the Y that…" pair of relative clauses as subject

- «Шов, который подсказывает предметная область, но который история пересекает каждую неделю, — ещё не
  граница» → «Если предметная область подсказывает шов, а история пересекает его каждую неделю, это ещё не
  граница»
- «Кластер, который видно в истории, но которому предметная область не может дать имени, часто лишь…» → «А
  кластер, который виден в истории, но не имеет имени в предметной области, часто лишь…»

### 1.4 Indirect-question lists after «решить» that lose their structure

- «Директор должен в квартале 2 решить, принять ли предложение, изменить его или отклонить, что станет поводом
  для пересмотра и как закроются три пробела во владении.» → «В квартале 2 директору предстоит решить три
  вопроса: принять предложение, изменить или отклонить его; что станет поводом для пересмотра; как закрыть три
  пробела во владении.»

## 2. Two showcase paragraphs

### 2.1 What the evidence supports

**Before.** Исследования выше изучают организации, которые уже мигрировали, и сообщают о мотивах, трудностях и
выгодах в самооценке участников. […] Пока платформа не может дать каждому сервису пайплайн, мониторинг и график
дежурств, организации меньше чем примерно на 100 инженеров обычно лучше подходит хорошо разбитый на модули
монолит с несколькими сервисами, выделенными по ясным причинам, чем множество сервисов.

**After.** Исследования выше изучают организации, которые уже мигрировали, и описывают мотивы, трудности и
выгоды со слов самих участников. […] Пока платформа не может дать каждому сервису пайплайн, мониторинг и график
дежурств, организации меньше чем примерно на 100 инженеров обычно лучше подходит не множество сервисов, а
хорошо разбитый на модули монолит с несколькими сервисами, выделенными по ясным причинам.

### 2.2 Domain seams and change data

**Before.** Шов, который подсказывает предметная область, но который история пересекает каждую неделю, — ещё не
граница: код так не устроен, и перенос шва становится отдельным проектом. Кластер, который видно в истории, но
которому предметная область не может дать имени, часто лишь случайный след того, кто вёл работу.

**After.** Если предметная область подсказывает шов, а история пересекает его каждую неделю, это ещё не граница:
код так не устроен, и перенос шва становится отдельным проектом. А кластер, который виден в истории, но не имеет
имени в предметной области, часто лишь случайный след того, кто вёл работу.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| бесхозность под маской | «замаскированная бесхозность»; changed | "orphaning in disguise"; the noun phrase reads better |
| готовый нарратив | «готовая история»; changed | «нарратив» is jargon; the CTO section already uses «история» for the same idea |
| сдвинуть границу / перенос шва | keep | consistent with the diagram label «Сначала сдвинуть границу» |
| модуль с контролем зависимостей | keep | long but exact; the diagram already uses it |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«компоненты остаются без хозяина предсказуемыми путями, и инвентаризация Northstar это подтверждает»** (was
   «показывает»). Assumes the English says the inventory illustrates, not proves.
2. **«любое изменение согласуют в одном разговоре»** (was «решается одним разговором»). Same meaning, assumed.
3. **«перенос шва становится отдельным проектом»**: kept literally. If the English means "making the code match
   the seam is its own project", a clearer rendering would be «перестроить код под этот шов — отдельный проект».
4. **Opening: «три компонента со спорным владением или вовсе без владельца»** compresses «владение которыми до
   сих пор оспаривается или которые так и остались без владельца». The case lists one undecided, one disputed and
   one orphaned; check that "undecided" is covered by the English wording too.

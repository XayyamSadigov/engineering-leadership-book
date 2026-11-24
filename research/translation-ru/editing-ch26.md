# Literary editing notes: chapter 26

File: `docs/parts/05-engineering-quality/26-security-and-software-supply-chain-quality.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (256
tokens, NBSP normalised); link targets, `{ #anchors }`, exercise labels, admonition lines, every table line,
INC ids, citations and Mermaid blocks are identical. About 70 sentence-level edits. Failure-mode labels were
already «Как заметить:» / «Что делать:».

Section 2a patterns and the chapter 25 notes cover most of what was fixed (counted lists given as bare
sentences: SLSA's two features, the three SBOM areas, the three secrets properties). Only new patterns
follow.

## 1. Patterns new beyond section 2a

### 1.1 A term that collides with another term in the base

"Outflow" in the stock-and-flow passage came through as «отток», which the term base reserves for churn.

- «Отток редко упирается в знания о безопасности.» → «Поток исправлений редко упирается в знания о
  безопасности.»

### 1.2 Broken parallelism: «X становится Y, который можно…, а не конкурировать»

The English "becomes A rather than competing with B" lost its grammar.

- «устранение уязвимостей становится объёмом работы, который можно спланировать внутри программы
  качества, а не конкурировать с ней» → «устранение уязвимостей превращается в объём работы, который
  планируют внутри программы качества, а не в соперника этой программы»

### 1.3 «A, то есть B, делает…» with an appositive gloss before the predicate

- «Well-Architected Framework от Amazon Web Services (AWS), то есть руководство вендора, ставит
  безопасность…» → «Well-Architected Framework — руководство вендора, Amazon Web Services (AWS). Оно
  ставит безопасность…»
- «Манифест…, написанный в 2020 году группой практиков, среди которых Adam Shostack, строит…» →
  «Манифест… написала в 2020 году группа практиков, среди них Adam Shostack. Он строит…»

### 1.4 Repeated root in one sentence ("accountable for whether… who is accountable")

- «отвечает за то, знает ли организация, …и кто за это отвечает» → «с него спрашивают, знает ли
  организация, …и кто за это отвечает»
- «Эти показатели показывают…» → «Эти показатели говорят о том…»
- «ротацию репетируют, поэтому ротация утёкшего ключа занимает минуты» → «…поэтому заменить утёкший ключ
  удаётся за минуты»

### 1.5 «в терминах X» survived in a playbook step

- «отчитывайтесь перед CTO в терминах уязвимости системы» → «…на языке уязвимости системы»

## 2. Two showcase paragraphs

### 2.1 Opening paragraph

**Before.** Эта глава смотрит на безопасность так же, как остальные главы части V смотрят на надёжность:
как на атрибут качества самого ПО и системы, которая его производит, со своими владельцами, бюджетом
ресурсов и показателями, которые трудно подогнать. Она написана для руководителя разработки, который не
обязан быть специалистом по безопасности, но отвечает за то, знает ли организация, что у неё работает,
как это туда попало и кто за это отвечает.

**After.** Эта глава рассматривает безопасность так же, как остальные главы части V рассматривают
надёжность: как атрибут качества самого ПО и системы, которая его производит. У этого атрибута есть свои
владельцы, бюджет ресурсов и показатели, которые трудно подогнать. Глава написана для руководителя
разработки. Специалистом по безопасности он быть не обязан, но с него спрашивают, знает ли организация,
что у неё работает, как это туда попало и кто за это отвечает.

### 2.2 Secrets and certificates

**Before.** Три свойства важнее выбора инструмента. Секреты хранятся в менеджере секретов и подставляются
во время выполнения. У каждого секрета и сертификата есть владелец и алерт об истечении срока. Ротацию
репетируют, поэтому ротация утёкшего ключа занимает минуты. INC-425 не был атакой. Это была дата
истечения, у которой не было владельца.

**After.** Три свойства важнее выбора инструмента. Первое: секреты хранятся в менеджере секретов и
подставляются во время выполнения. Второе: у каждого секрета и сертификата есть владелец и алерт об
истечении срока. Третье: ротацию репетируют, поэтому заменить утёкший ключ удаётся за минуты. INC-425 не
был атакой: это была дата истечения, за которую никто не отвечал.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| уязвимость системы (exposure) | keep, but watch density | the chapter uses it about 15 times next to «уязвимость» (a CVE); readable once defined, but «насколько система уязвима» helps in a few sentences |
| supply-chain-атака | «атака на цепочку поставки ПО» | hybrid compound; changed once (X2), matches the term base |
| Кейс-стади (as a subject) | «исследование (кейс-стади)» | indeclinable loanword as sentence subject reads awkwardly; changed once |
| сообщите продукту | «продуктовой стороне» | «продукт» as a department is slang; changed once |
| Слова о серьёзности | «названия уровней серьёзности» | changed once (CVSS paragraph) |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **CSF paragraph, «результаты CSF — не чек-лист»** (was «его результаты», ambiguous between Govern and
   CSF). Resolved to CSF from the References line («Core… не является чек-листом»). If the English says
   "its outcomes" about the Core specifically, «результаты ядра CSF» would be more exact.
2. **«Вместо этого CSF предлагает…»**: «Вместо этого» added as a connective between "not a checklist" and
   the profiles. Remove if the English does not frame profiles as the alternative.
3. **Trade-offs, «вызывает раздражение»** (was «обиду»). Assumes English "resentment"; «обида» was
   accurate but odd in an organizational context.
4. **Champions research, «Это научные результаты, но каждый получен в одной организации»**: «но» added.
   The label and the single-organization caveat are unchanged.
5. **auth-svc case**: the long sentence was split, keeping the director as the agent of both the access
   restriction and the exception. Confirm the English does not assign the restriction to Kwame Mensah.

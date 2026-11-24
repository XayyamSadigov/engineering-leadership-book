# Literary editing notes: chapter 48

File: `docs/parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.ru.md`. Edited
from the Russian text only; the English chapter was not opened. The file was not yet committed, so the
pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes (only the expected stale `dist/` single-file error); the sorted list of
numbers is identical before and after (330 tokens, NBSP normalised); link targets, `{ #anchors }`, heading
count, exercise labels, admonition lines, citations, every table line and all three Mermaid blocks are
byte-identical. NBSP count 66 → 66. About 45 sentence-level edits. The failure modes use only «Как
заметить:», as in the translation.

The chapter needed fewer edits than chapter 47: its prose is mostly lists and short rules. Only new
patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Kinship metaphors calqued from English ("parent of")

- «План персонала — это родитель модели ресурсов с более дальним горизонтом.» → «План персонала — это
  надстройка над моделью ресурсов, с более дальним горизонтом.»

### 1.2 «если только X не и есть Y» (calque of "unless X is itself Y")

The double particle «не и» is ungrammatical in Russian.

- «Предписывайте результаты, а не инструменты, если только инструмент не и есть механизм контроля.» →
  «…кроме случаев, когда инструмент и есть механизм контроля.» (heading line and key takeaway)

### 1.3 Contrast pairs joined by «и» where Russian needs «но»

English "X is cheap and blind to context; Y sees context and creates a queue" keeps «и»; Russian reads it as
two advantages.

- «Проверка в пайплайне дешёвая и не видит контекста; ревью человеком видит контекст и создаёт очередь.» →
  «Проверка в пайплайне дешева, но не видит контекста; ревью человеком видит контекст, но создаёт очередь.»
- «экономит на каждом месте и отнимает время на каждой задаче» → «экономит на каждом месте, но отнимает
  время…»

### 1.4 A quoted rule used as the subject of «должно побеждать»

- «А «каждая команда пользуется пайплайн-продуктом X» должно побеждать за счёт того, что этот продукт
  лучше.» → «А «каждая команда пользуется пайплайн-продуктом X» — уже нет: продукт должен побеждать за счёт
  того, что он лучше.»

### 1.5 Contracts and documents as agents holding people

- «Продлённый контракт держит единственных людей, которые понимают сервис.» → «По продлённому контракту
  работают единственные люди, которые понимают сервис.»

### 1.6 "Where things stand" rendered literally

- «**Где всё стоит сейчас.**» → «**Положение дел.**» (the form already used in
  `quarter-4-briefing.ru.md`)

## 2. Two showcase paragraphs

### 2.1 Why this matters, organization level (closing sentences)

**Before.** Каждый найм на замену — это ещё и выбор уровня, площадки и формы занятости. Если такие выборы
делает по одному тот руководитель, от которого кто-то ушёл, они всё равно складываются в стратегию
персонала. Просто она ничья.

**After.** Каждый найм на замену — это ещё и выбор уровня, площадки и формы занятости. Если каждый такой
выбор делает тот руководитель, от которого ушёл человек, выборы всё равно складываются в стратегию
персонала. Просто она ничья.

### 2.2 Mandate platforms or not

**Before.** **Предписывайте результаты, а не инструменты, если только инструмент не и есть механизм
контроля.** Белая книга CNCF о платформах говорит, что платформы не должны рассчитывать на указания сверху,
чтобы их принимали (…). В отчёте DORA за 2024 год респонденты, которых обязали использовать платформу
исключительно и на всём жизненном цикле, сообщали о пропускной способности на 6 процентов ниже (…).
«Каждое изменение в продакшене проходит через пайплайн с журналом аудита и откатом» — это политика. А
«каждая команда пользуется пайплайн-продуктом X» должно побеждать за счёт того, что этот продукт лучше.

**After.** **Предписывайте результаты, а не инструменты, кроме случаев, когда инструмент и есть механизм
контроля.** Белая книга CNCF о платформах говорит, что платформы не должны рассчитывать на то, что их
станут использовать по указанию сверху (…). В отчёте DORA за 2024 год респонденты, которых обязали
пользоваться только платформой и на всём жизненном цикле, сообщали о пропускной способности на 6 процентов
ниже (…). «Каждое изменение в продакшене проходит через пайплайн с журналом аудита и откатом» — это
политика. А «каждая команда пользуется пайплайн-продуктом X» — уже нет: продукт должен побеждать за счёт
того, что он лучше.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| скамейка подрядчиков (contractor bench) | consider «резерв подрядчиков» | «скамейка» was dropped for «резерв» in leadership chapters (notes-t15, editing-ch41) |
| найм на опережение | keep | clear |
| способность принять новых людей (absorption) | keep in prose; «Способность команды принять людей» as the paragraph label works | |
| risk «из хвоста распределения» | allow «редкий, но тяжёлый риск» in prose | the statistical phrase is opaque for the target reader; kept as is |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Rigby: «сокращало ожидаемые потери до 15 процентов»** is ambiguous in Russian: "reduced losses to
   15%" or "by up to 15%". Not changed; please fix the preposition against the English («на» / «до»).
2. **Case: «начальный уровень по умолчанию из варианта B до этого риска явно не дотягивается»** rendered
   «найм на начальный уровень по умолчанию из варианта B этот риск прямо не закрывает». Assumes "does not
   directly address the ledger risk".
3. **«бюджет исходит из того, что каждое профинансированное место занято каждую неделю»** rendered «…занято
   все недели года». Same meaning; check that the English means the full year.
4. **«Повышения поднимают людей вверх без ухода»** rendered «Повышения переводят людей вверх, хотя никто не
   уходит». Assumes "without anyone leaving".
5. **Example: «у сотрудников аппарата CTO был ещё один, никак не измеряемый список»** rendered «у аппарата
   CTO был ещё и свой список обязательных правил, который никак не измерялся».

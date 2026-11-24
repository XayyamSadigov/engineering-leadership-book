# Literary editing notes: chapter 28

File: `docs/parts/06-technical-leadership/28-architecture-decision-making-and-governance.ru.md`. Edited from the
Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy
was kept in the session scratchpad.

Checks: `validate_book.py` passes; the numbers are identical before and after (the numeric-token count differs
by one only because «43, 30 из них» became «43, причём 30 —», which splits one token in two); `{ #anchors }`,
headings, link targets, citations, exercise labels, the admonition, every table line and all three Mermaid
blocks are byte-identical. Failure-mode labels were already «Как заметить:» / «Что делать:». About 80
sentence-level edits.

Section 2a patterns appeared (unnumbered pairs after «два вывода» / «два факта», «который» chains, missing
connectives). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Dative-subject definitions with a «который» tail

English "A decision that stays inside one team and can be undone in a week needs only…" became a dative noun
phrase with a relative clause. A condition reads better.

- «Решению внутри одной команды, которое можно отменить за неделю, хватит сообщения коммита.» → «Если решение
  не выходит за пределы одной команды и отменить его можно за неделю, хватит сообщения коммита.»
- «Руководитель, которому не хватает информации, который перегружен или вынужден решать срочно, в итоге
  утверждает…» → «Если руководителю не хватает информации, если он перегружен или должен решать срочно, он в
  итоге утверждает…»

### 1.2 Tautology from the term «решающий» ("the decider decides")

- «решающий домена … решает в течение десяти рабочих дней» → «решение принимает решающий домена … в течение
  десяти рабочих дней»
- «три–пять рабочих дней, после которых решающий решает» → «…после чего решающий принимает решение»
  (the Mermaid label «Решающий решает» was left as is: short and clear in a diagram).

### 1.3 A bare noun as a list opener ("Signals: …")

- «Сигналы: медианное время до решения, …» → «На что смотреть: медианное время до решения, …»

### 1.4 Source paraphrase squeezed into a parenthetical

- «Короткие записи Nygard (контекст, решение, статус, последствия; хранятся пронумерованными в репозитории;
  устаревшие заменяют, а не удаляют) нужны для того, чтобы…» → «Nygard описал короткие записи: контекст,
  решение, статус, последствия. Их хранят в репозитории под номерами; устаревшие не удаляют, а заменяют.
  Смысл в том, чтобы…»

### 1.5 Term drift inside the chapter

- «как совет, пропускная способность которого ниже…» (in a section about the architecture board) → «комитет»,
  per the term base ("review board" = комитет по ревью).

## 2. Two showcase paragraphs

### 2.1 Why this matters, executive scale

**Before.** Для высшего руководства управление архитектурой — это вопрос скорости под видом вопроса качества.
Комитет по ревью, созданный, чтобы останавливать плохие дизайны, часто даёт более медленные команды и те же
дизайны, только построенные в обход комитета. Отсутствие управления даёт быстрые команды и систему, которую
никто не может изменить. Задача в том, чтобы на каждое решение приходилось ровно столько контроля, сколько
нужно, и не больше.

**After.** Для высшего руководства управление архитектурой — вопрос скорости, который выглядит как вопрос
качества. Комитет по ревью, созданный, чтобы останавливать плохие дизайны, часто приводит к тому, что команды
работают медленнее, а дизайны остаются прежними, только строят их в обход комитета. Без управления команды
быстры, но систему никто не может изменить. Задача — дать каждому решению ровно столько контроля, сколько
нужно, и не больше.

### 2.2 Position of the book, two consequences

**Before.** Из этого следуют два вывода. Автор межкомандного предложения не должен быть его единственным
утверждающим. А право согласия руководителя касается ресурса и сроков, а не дизайна: возражение по ресурсу,
которым блокируют неугодный дизайн, — это техническое вето, которого у руководителя нет.

**After.** Из этого следуют два вывода. Первый: автор межкомандного предложения не должен быть единственным,
кто его утверждает. Второй: право согласия руководителя касается ресурса и сроков, а не дизайна. Если
возражением по ресурсу блокируют неугодный дизайн, это техническое вето, а его у руководителя нет.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| решающий | keep; avoid «решающий решает», use «решение принимает решающий» | tautology in running prose |
| поддерживать журнал живым | «не давать журналу заглохнуть»; changed | the calque "keep alive" reads oddly with «журнал» |
| утверждение не глядя (as a state of a board) | «комитет стал утверждать не глядя»; changed in objectives and takeaways | «превратился в утверждение не глядя» is a noun-for-person mismatch |
| автоматический выключатель (circuit breaker) | keep | glossed in place |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«как следят, чтобы они оставались верными»** (Jansen and Bosch paragraph) rendered «чтобы они оставались
   в силе». If the English means "enforced" rather than "still valid", «как следят за их соблюдением» is closer.
2. **Trade-offs, «Право согласия … — плата за это».** Kept «плата». If the English means the agreement right
   compensates the manager, «компенсация» would be clearer.
3. **Key takeaway, «запускайте их через код-ревью»** rendered «заводите их по триггеру из код-ревью»,
   matching the trigger rule in the ADR section. Check that the English means the code-review trigger.
4. **References, Nygard: «Исходная запись решения».** Unclear: the original ADR blog post, or the original
   decision-record format? Left as is.
5. **Buchgeher: «Согласно аннотации»** is an access note in reader text (already flagged in notes-t8). Not
   changed.
6. **Board section intro.** The sentence about chapter 20 says «Глава 20 показывает…» and then links
   «([глава 20](…))» again; the doubled reference is in the original wording. Consider dropping one.

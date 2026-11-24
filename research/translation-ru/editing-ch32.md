# Literary editing notes: chapter 32

File: `docs/parts/06-technical-leadership/32-platform-engineering-developer-experience-and-modernization.ru.md`.
Edited from the Russian text only; the English chapter was not opened. The pre-edit copy was kept in the session
scratchpad (file not yet committed).

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (NBSP
normalised); link targets, `{ #anchors }`, every table line, the admonition title line and all Mermaid blocks are
identical. One link text changed with its target kept: «[Глава 20](…) говорит» → «Согласно [главе 20](…)». About
35 sentence-level edits. Failure modes have only «Как заметить:» (no countermeasure in the source, per notes-t10).

## 1. Patterns new beyond section 2a

### 1.1 "This chapter uses / ranks / reads" as an impersonal agent

- «Эта глава использует два из трёх измерений как правило выбора.» → «Здесь два из трёх измерений служат
  правилом выбора.»
- «В этом примере ранжируется работа, которую…» → «Ниже ранжирована работа, которую…»
- «Эта глава опирается на них, не пересказывая заново.» → «Здесь мы опираемся на них, не пересказывая.»

### 1.2 "The rule the book recommends:" as a noun-phrase opener

- «Правило, которое рекомендует книга: предписывайте…» → «Книга рекомендует правило: предписывайте…»
- «Правило выбора, которое рекомендует книга:» → «Книга рекомендует такое правило выбора:»

### 1.3 One sentence carrying an author's three claims plus a concession inside dashes

- «Fowler утверждает, что планы замены проваливаются, потому что…; что существующее поведение…; что мелкие
  шаги… Он настаивает на переходной архитектуре — коде, который…, хотя люди сопротивляются ему…, — и
  предупреждает…» → «Доводы Fowler таковы: планы замены проваливаются…; существующее поведение…; мелкие шаги…
  Он настаивает на переходной архитектуре, хотя люди сопротивляются ей как пустой трате сил. Это код, который…
  Ещё Fowler предупреждает…»

### 1.4 Passive "is paid for on every change" and "X begs the question"

- «74-минутный пайплайн … оплачиваются на каждом изменении, каждой командой» → «За 74-минутный пайплайн …
  платят при каждом изменении, в каждой команде»
- «Одно лишь принятие напрашивается на вопрос «и что?»» → «Покажете одно лишь принятие — услышите «и что?»»

## 2. Two showcase paragraphs

### 2.1 Why this matters, team and organization

**Before.** 74-минутный пайплайн или шестидневное ожидание тестового окружения оплачиваются на каждом изменении,
каждой командой, каждую неделю. Небольшие сокращения здесь дают больший накопленный эффект, чем большая часть
работы над функциями. […] Без замещающего сигнала платформенная команда может быть занятой и бесполезной или
полезной, но не способной это показать.

**After.** За 74-минутный пайплайн или шестидневное ожидание тестового окружения платят при каждом изменении, в
каждой команде, каждую неделю. Даже небольшое сокращение здесь в сумме даёт больше, чем большая часть работы над
функциями. […] Если ничем его не заменить, платформенная команда может оказаться занятой, но бесполезной, или
полезной, но неспособной это показать.

### 2.2 Feedback loops

**Before.** Если она настолько длинная, что приходится переключиться на другую задачу, добавляется цена
переключения и становится рационально укрупнять пачки изменений, а чем крупнее пачка, тем выше риск каждого
изменения. Правило выбора, которое рекомендует книга:

**After.** Если же она так длинна, что приходится переключаться на другую задачу, к ожиданию добавляется цена
переключения, а укрупнять пачки изменений становится рационально. Чем крупнее пачка, тем выше риск каждого
изменения. Книга рекомендует такое правило выбора:

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| общая машинерия | «общее хозяйство»; changed | «машинерия» reads as a calque of "machinery" |
| выстраивайте последовательность вокруг обязательств | «очерёдность»; changed | "sequence" in the planning sense |
| дежурный по прерываниям за единым входом | keep (term from ch16) | slightly heavy, but a fixed rendering |
| платформа дрейфует к полноте | «тянется к полноте»; changed | «дрейфовать» is a calque of "drift" |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«…проходит ту же проверку, что и внутренняя работа, или не проходит её»** rendered «проверяют так же, как
   внутреннюю разработку». The pass-or-fail emphasis is dropped; restore it if the English stresses it.
2. **«Обычный компромисс: … платформа как явно самый дешёвый способ этого результата добиться»** (was «явно
   дешевле как способ … соответствовать»). Assumes "clearly the cheaper way to comply".
3. **«Ожидание ревью … стоит в списке, чтобы платформа не записала его себе в заслугу»** (was «не даёт
   платформе приписать его себе»). Assumes "claim credit for it".
4. **DORA hypothesis list: «платформы строят как раз организации, у которых уже есть проблемы»** (was
   «проблемные организации»). Check that the English means struggling organizations are the ones building
   platforms.
5. **Payback sentence** still glosses itself («срок окупаемости — два года, то есть за два года экономия
   возвращает затраты»); the repetition is in the original wording. Consider dropping the gloss.

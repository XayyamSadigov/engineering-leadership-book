# Literary editing notes: chapter 30

File: `docs/parts/06-technical-leadership/30-technical-strategy-and-technology-selection.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (266 tokens,
NBSP normalised); link targets, `{ #anchors }`, heading order, exercise labels, admonition lines, every table
line, TR and INC ids, citations and Mermaid blocks are identical. About 50 sentence-level edits. Failure-mode
labels were already «Как заметить:» / «Что делать:»; no "contested" label in this chapter.

The section 2a patterns appeared as expected (missing «а»/«но» between contrasted clauses, English word
order). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Grammar slip that reverses negation: «…пересматривает его никто»

- «Его ведут ради аудита, а пересматривает его никто.» → «Его ведут ради аудита, но никто не
  пересматривает.» Russian needs «не» with «никто»; grep later chapters for «никто» without «не».

### 1.2 Sentence opening with a digit or a lowercase identifier

- «19 из 30 инцидентов Sev1 и Sev2 базового квартала (63%) запустили…» → «Из 30 инцидентов Sev1 и Sev2
  базового квартала 19 (63%) запустили…»
- «tax-svc — сервис Billing уровня tier 1 без ранбука… — рассчитывает налог…» → «Речь о tax-svc: этот
  сервис Billing уровня tier 1 рассчитывает налог…, но у него нет ранбука (runbook), а алертинг неполный.»

### 1.3 Calqued abstract nouns as objects of «наследовать / подверженность»

English "inherit the project's health", "exposure to project health" came through literally.

- «наследуете работу по обновлениям и здоровье проекта» → «наследуете работу по обновлениям и зависимость
  от здоровья проекта и всего, от чего он сам зависит»
- «работой по обновлениям и подверженностью здоровью проекта» → «…и зависимостью от здоровья проекта»
- «к чему сходиться» (converge) → «к каким технологиям сводить ландшафт»

### 1.4 A three-part "argues that A; that B; and that C" in one sentence

Russian «утверждает, что…; что…; и что…» is heavy. Announce the count and give three sentences (as the
chapter already does for McKinley).

- «Он утверждает, что согласованные действия — самая важная часть; что направляющие политики должны…; и
  что многие письменные стратегии проваливаются…» → «…и утверждает три вещи. Самая важная часть —
  согласованные действия. Направляющие политики должны… А многие письменные стратегии проваливаются…»

### 1.5 Elliptic comparative split across a semicolon

- «Решения… дороже свободного бюджета на инструменты идут к CFO…; дешевле — решает директор…» → «Решения…,
  которые дороже свободного бюджета на инструменты, уходят к CFO… Более дешёвые принимает директор…»

### 1.6 Your-your-your from English possessives in instructions

- «Проверка концепции… использует ваши данные, ваши способы отказа и ваши точки интеграции.» → «Проверку
  концепции… проводите на своих данных, своих способах отказа и своих точках интеграции.»

## 2. Two showcase paragraphs

### 2.1 The strategy loop

**Before.** Петля важнее прямоугольников. Стратегия, которую однажды написали и убрали в папку, — просто
документ. Стратегия, диагноз которой пересматривают, когда реестр рисков или решение о выборе технологии
вскрывает что-то новое, — инструмент управления. Larson предлагает оценить эффект примерно через два месяца
после публикации; книга рекомендует раз в квартал перечитывать диагноз, сверяя его с реестром.

**After.** Петля важнее прямоугольников. Стратегия, которую однажды написали и убрали в папку, — просто
документ. Если же диагноз пересматривают всякий раз, когда реестр рисков или решение о выборе технологии
вскрывает что-то новое, стратегия становится инструментом управления. Larson предлагает оценить эффект
стратегии примерно через два месяца после публикации; книга рекомендует раз в квартал перечитывать диагноз,
сверяя его с реестром.

### 2.2 Case, the order path

**Before.** Вариант B ставит API вендора на путь заказа. Предложенный для пути заказа SLO (…) — 99% отправок
в пределах 2 секунд. Для этого нужны кэшированные ставки на случай отказа, а это дополнительная разработка,
которой нет в таблице, и контракт с доступностью не ниже собственных 99,9% Northstar.

**After.** Вариант B ставит API вендора на путь заказа. Предложенный для пути заказа SLO (…) — 99% отправок
в пределах 2 секунд. Чтобы его выдержать, нужны кэшированные ставки на случай отказа (дополнительная
разработка, которой нет в таблице) и контракт с доступностью не ниже собственных 99,9% Northstar.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| подверженность (exposure) | keep in the register definition; «зависимость от» where the object is "project health" | «подверженность здоровью» is not Russian |
| содержимое ставок (rate content) | «сами ставки» in prose | «вести содержимое ставок» reads as a calque; table and term-base entry untouched |
| укомплектованность людьми (staffing, criterion) | «наличие людей» | heavy bureaucratic noun; left as is pending a decision |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«ни одна политика не говорила, к чему сходиться»** rendered «к каким технологиям сводить ландшафт».
   Assumes "converge on" means reducing the set of technologies, as policy 1 suggests.
2. **«Даты… иногда как минимальные»** rendered «иногда лишь как нижнюю границу» (Adoptium "not before").
3. **«ни одна не ведёт содержимое ставок»** rendered «ни одна не поддерживает сами ставки». Assumes
   "maintains rate content" means keeping the rate data current.
4. **Info box «изменений во владении, серьёзности…»**: same unclear phrase as chapter 29; not changed.
5. **Example, day rate vs weekly rate**: reordered to «Эта ставка выше плановой ставки книги ($3 558 за
   инженеро-неделю) в пересчёте на день». Same claim.

# Literary editing notes: chapter 40

File: `docs/parts/09-engineering-directorship/40-the-directors-job.ru.md`. Edited from the Russian text
only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in
the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (NBSP
normalised); link targets, `{ #anchors }`, headings, exercise labels, admonition lines, every table line
and Mermaid blocks are unchanged. About 45 sentence-level edits; edited paragraphs re-wrapped at about 105
characters. Failure Modes are prose, as noted in notes-t14; the one «Как заметить:» stays.

Section 2a patterns appeared as expected (missing connectives, source as speaker: «Теоретическая модель
Williamson утверждает», «Классическая статья Mintzberg показывает» → the author as subject). Only new
patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 A term collides with an ordinary word in the same chapter

The chapter uses «эффект умолчания» (mum effect) as a term; a few paragraphs later "the default" came
through as «умолчание», which now reads as "the silence".

- «Но, по мнению книги, умолчание выбрано верно» → «…вариант по умолчанию выбран верно»

Grep chapters that carry a term for the same root used in its everyday sense.

### 1.2 Hierarchy preposition reversed

- «CTO (технический директор), над которым стоят несколько директоров» (directors above the CTO) → «у
  которого в подчинении несколько директоров»

### 1.3 «Директор, который X, Y» as a generic subject (ch 35 1.2, now with a person)

Six instances; English "A director who X does Y" wants «Если директор X…» or a gerund.

- «Директор, который решил проблему одной команды, произвёл одно исправление.» → «Решив проблему одной
  команды, директор вносит одно исправление.»
- «Директор, который заполняет неделю проблемами этой недели, тратит единственного человека…» → «Если
  директор заполняет неделю проблемами этой недели, он тратит впустую единственного человека…»
- «Директор, который говорит с клиентами, рискует стать вторым продакт-менеджером.» → «Разговаривая с
  клиентами, директор рискует…»

### 1.4 Colloquial or flat renderings of evaluative words

- «Если встречи регулярны и прозрачны, это здорово» ("healthy" read as "great!") → «это здоровая практика»
- «результат руководителя есть результат организации… — на этом уровне становится буквальным» → «На этом
  уровне его надо понимать буквально»
- «Часы, потраченные на то, чтобы слушать, не тратятся на год» → «…не уходят на работу с горизонтом в год»

## 2. Two showcase paragraphs

### 2.1 The mental model, first idea

**Before.** Известное определение Andrew Grove — результат руководителя есть результат организации, на
которую он влияет (…) — на этом уровне становится буквальным. Директор, который решил проблему одной
команды, произвёл одно исправление. Директор, который изменил правило владения, распределение ресурсов или
петлю обзоров, изменил то, что производит каждая команда.

**After.** Andrew Grove известен определением: результат руководителя — это результат организации, на
которую он влияет (…). На этом уровне его надо понимать буквально. Решив проблему одной команды, директор
вносит одно исправление. Изменив правило владения, распределение ресурсов или петлю обзоров, он меняет то,
что производит каждая команда.

### 2.2 Trade-offs: raw data or context

**Before.** Первичные записи об инцидентах ловят то, что сводка смягчила, например серьёзность, которая не
соответствует ущербу, но подталкивают к тому, чтобы перепроверять каждое решение задним числом. Компромисс —
небольшая регулярная выборка.

**After.** Первичные записи об инцидентах ловят то, что сводка смягчила, например серьёзность, которая не
соответствует ущербу. Но они же подталкивают перепроверять задним числом каждое решение. Компромисс —
небольшая регулярная выборка.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| рассуждение книги (evidence label) | add to glossary 4.3 | used here; formed like «синтез книги» |
| список неблагонадёжных (watch list) | keep | strong, but the English wording is meant to sting |
| «период прихода» | «первые месяцы в должности» | calque; changed in the failure mode |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **CTO perspective: «над которым стоят несколько директоров»** changed to «у которого в подчинении
   несколько директоров». Treated as a grammar slip; check that the English says "a CTO with several
   directors".
2. **«Модель спорная»** (Williamson). If the English uses the evidence label "contested", the book's
   rendering is «вопрос спорный». Not bold here, so left as prose.
3. **«Такие рычаги ранжирует глава⍽3 ([глава⍽3](…))»**, and the same doubled pattern for chapters 19 and 27.
   Kept, to keep the number list identical; if the English does not repeat the number, fold the plain text
   into the link.
4. **GitLab practice: «даёт взгляд на здоровье команды помимо взгляда руководителя»** rendered «дополняет
   взгляд руководителя на здоровье команды». Assumes "in addition to", not "independent of".
5. **«Источники сигналов у CTO похожие, но реже»** rendered «…похожие, только обращается он к ним реже».
   Assumes "used less often".

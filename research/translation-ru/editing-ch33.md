# Literary editing notes: chapter 33

File: `docs/parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (NBSP
normalised); link targets, `{ #anchors }`, exercise labels, every heading, table line, admonition line and
Mermaid block are byte-identical; NBSP count unchanged (77). Edited paragraphs were re-wrapped at about
105 characters. About 60 paragraphs touched. Failure-mode labels were already «Как заметить:» (the chapter
has no «Что делать:» field).

The translation was accurate and clean. Section 2a patterns appeared as expected (missing connectives,
«На уровне высшего руководства…» as an opener, «который» chains). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «Книга» with two referents

The chapter discusses another book (*Team Topologies*) and uses «книга» for this book's own position. When
both appear in one paragraph, «Книга разделяет…» reads as this book.

- «*Team Topologies* заимствует его для команд. Книга разделяет внутреннюю нагрузку…» → «*Team Topologies*
  переносит его на команды. Её авторы различают три вида нагрузки…»

Grep later chapters for «Книга» right after a sentence naming another book.

### 1.2 Repeated subject with a «который» definition («CTO, который… CTO, который…»)

- «CTO (технический директор), который реорганизует компанию ради удобства схемы подчинения, меняет и
  то, какие части…» → «Реорганизуя компанию ради удобства схемы подчинения, CTO (технический директор)
  заодно решает, какие части…»
- «Граница, которая разделяет работу, меняющуюся вместе, превращает инженерные решения в межкомандные»
  (ch 34) → «Если граница разделяет работу, которая меняется вместе, инженерные решения становятся
  межкомандными»

### 1.3 «стоит» meaning "is worth" next to cost talk

Pattern 1.1 from chapter 25 has a sibling: «не стоит» meaning "not worth" in a sentence about costs reads
as "does not cost".

- «Каждое изменение границы стоит недель… Если изменение не стоит квартала неразберихи…» → «…обходится в
  недели… Если изменение не оправдывает квартала неразберихи…»

### 1.4 The same word as label and as definition («тенденция … тенденцией»)

- «Наблюдение Конвея верно как сильная тенденция… Считайте его тенденцией, которой нужно управлять, а не
  законом.» → «Наблюдение Конвея описывает сильную тенденцию… Управляйте этой тенденцией и не принимайте
  её за закон.»

### 1.5 «это то, что…» variants in the reference list

- «Исходное эссе: короткое, и это рассуждение, а не исследование.» → «Исходное эссе: короткое рассуждение,
  а не исследование.»
- «Откуда понятие когнитивной нагрузки пришло в исследованиях обучения.» → «Источник понятия когнитивной
  нагрузки в исследованиях обучения.»

## 2. Two showcase paragraphs

### 2.1 Reverse Conway maneuver

**Before.** Если система копирует организацию, спроектируйте ту организацию, которую система должна
скопировать. Это **обратный манёвр Конвея**, и *Team Topologies* известна тем, что его продвигает (…).
Логика здесь последовательна, а доказательств пока нет. Сравнение MacCormack касается новых продуктов,
созданных разными организациями, а не фирмы, которая перестраивается вокруг уже существующего кода.
Существующая система сопротивляется: команды, выстроенные по потокам создания ценности, которые все
проходят через один общий модуль, по-прежнему координируются на этом модуле.

**After.** Если система копирует организацию, спроектируйте ту организацию, которую система должна
скопировать. Это **обратный манёвр Конвея**, и именно его продвижением известна *Team Topologies* (…).
Логика стройная, а доказательств пока нет. MacCormack с соавторами сравнивали новые продукты, созданные
разными организациями, а не фирму, которая перестраивается вокруг уже существующего кода. Существующая
система сопротивляется. Если все потоки создания ценности проходят через один общий модуль, команды,
выстроенные по этим потокам, всё равно координируются на нём.

### 2.2 The director's plan for Orders

**Before.** Директор склоняется к тому, чтобы в квартале 2, пока идёт работа над массовым заказом,
структурных изменений не делать. Отложить core/permissions (D) в любом случае. К передаче search-svc (B)
и разделению Orders (C) вернуться после того, как массовый заказ будет выпущен на неделе 26.

**After.** Директор склоняется к такому плану: в квартале 2, пока идёт работа над массовым заказом,
структуру не менять; core/permissions (D) отложить в любом случае; к передаче search-svc (B) и разделению
Orders (C) вернуться после того, как массовый заказ выйдет на неделе 26.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| работа команды содействия (count noun: «одна или несколько работ команды содействия», A3) | allow «участие команды содействия» or «задача содействия» as the countable form | «работа» does not pluralise naturally; kept in A3 for consistency |
| учебная нагрузка (germane) | keep; reads well in tables and the decision framework | notes-t11 raised «релевантная» as an alternative; «учебная» is clearer to engineers |
| сортировка срочного (ch 34, triage) | keep | reads naturally in both places |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Case, Kwame Mensah's release working group.** Kwame Mensah's role is not given at first mention in
   this chapter (CLAUDE.md asks for it). Not added: it would be a new fact on the page.
2. **«договорённостей, основанных на отношениях»** (Colfer and Baldwin, "relational contracting"?). If the
   English means relational contracts, «неформальных долгосрочных договорённостей» is the usual Russian
   rendering. Left as is.
3. **Failure mode «Платформа — „приёмник прерываний“»: «На исходном уровне Northstar…»** means the
   baseline quarter. Elsewhere the chapter says «в базовом квартале»; consider unifying.
4. **Case, option B: «одного решения мало, нужно согласие этой команды»** (was «нужно согласие этой
   команды, а не только решение»). Assumes "decision" means the director's decision.
5. **Takeaway on Conway: «хотя реальные исключения есть»** kept; check that the English says the exceptions
   are real rather than "rare".

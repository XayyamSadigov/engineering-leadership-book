# Literary editing notes: chapter 39

File: `docs/parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.ru.md`.
Edited from the Russian text only; the English chapter was not opened. The file was not yet committed, so
the pre-edit copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (NBSP
normalised); link targets, `{ #anchors }`, headings, exercise labels, admonition lines, every table line
(including the week 26 report tables) and Mermaid blocks are unchanged. About 40 sentence-level edits;
edited paragraphs re-wrapped at about 105 characters. Failure-mode labels were already «Как заметить:» /
«Что делать:».

The translation was accurate and fairly clean. Section 2a patterns appeared as expected (missing
connectives, ambiguous «он», «решение» meaning "the first thing to decide"). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 A Russian word with the opposite connotation

English "a long clock teaches stamina" (a bad thing) came through as «учит выносливости», which Russian
reads as praise. Sibling of ch 25 1.1 («стоит доверия»).

- «Длинный учит выносливости.» → «Длинный приучает спорить на выносливость.» (also ties it to the failure
  mode «Эскалация на выносливость»)

### 1.2 Tautology from a repeated root

- «перепроверяйте через структуру (…), а не через проверки тех, кто отчитывается» → «…а не устраивайте
  проверки тем, кто отчитывается»
- «уход одного человека остановит компонент tier 1, то есть такой, чей сбой останавливает заказы» →
  «…такой, при сбое которого встают заказы или платежи»
- «Показатели, которые не меняются, показаны» → «…не выброшены, а показаны» (contrast first, ch 35 1.4)

### 1.3 Absence calqued as location: «директора почти нигде нет»

- «В организации из 50–150 инженеров директора почти нигде нет. Всё, что он знает, приходит через
  обзоры…» → «…директор почти нигде не бывает лично. Всё, что он знает, он узнаёт из обзоров…»
- «Northstar к приходу директора демонстрирует каждый из этих провалов» → «К приходу директора в Northstar
  налицо все эти провалы»

### 1.4 «Кроме того» opening a sentence that actually contrasts

- «Кроме того, эскалация передаёт полномочия, но не передаёт информацию.» → «Но эскалация передаёт
  полномочия, а информацию — нет.»

## 2. Two showcase paragraphs

### 2.1 Why this matters, organization level

**Before.** В организации из 50–150 инженеров директора почти нигде нет. Всё, что он знает, приходит через
обзоры и отчёты, а пишут их те самые люди, о чьей работе идёт речь. […] У разногласий между командами нет
естественного владельца. Поэтому они либо затухают неразрешёнными, либо поднимаются наверх через того, кого
руководство охотнее слушает.

**After.** В организации из 50–150 инженеров директор почти нигде не бывает лично. Всё, что он знает, он
узнаёт из обзоров и отчётов, а пишут их те самые люди, о чьей работе идёт речь. […] У разногласий между
командами нет естественного владельца. Поэтому они либо глохнут нерешёнными, либо доходят наверх через
того, к кому руководство охотнее прислушивается.

### 2.2 Example: corroboration through structure

**Before.** Директор прочитал описание самого инцидента, а не смотрел на счётчик, переоценил его серьёзность
и добавил в операционный разбор еженедельный аудит выборки оценок серьёзности. По собственным меркам отчёты
были зелёными. Аудит делает повторную проверку рутиной, поэтому он не бросает подозрения ни на одну команду.

**After.** Директор не стал смотреть на счётчик, а прочитал описание самого инцидента, переоценил его
серьёзность и добавил в операционный разбор еженедельный аудит выборки оценок серьёзности. Отчёты при этом
были зелёными по их собственным меркам. Аудит превращает перепроверку в рутину, поэтому подозрение не падает
ни на одну команду.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| дата «нужно к» | keep | declines badly («до даты „нужно к“»), but it matches the glossary page and the log field name |
| «отчётность перед руководством» (H1) vs «отчёт для руководства» (body) | one form book-wide | already raised in notes-t14; the body form reads better |
| совместное обоснование / совместная записка для эскалации | keep both | the heading names the document, the prose names the content; readers follow |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Example: «По собственным меркам отчёты были зелёными»** rendered «Отчёты при этом были зелёными по их
   собственным меркам». Assumes "by their own definitions" refers to the reports (or teams), not the
   director.
2. **«Пороги — дело выбора»** rendered «Пороги можно выбрать по-разному; важно каждый раз рассчитывать их
   одинаково». «их» may mean the colors rather than the thresholds; kept ambiguous as in the original.
3. **«Отчёт не решает ничего из того, что ещё открыто»** (after the week 26 report). Unclear whether the
   English means "does not pretend to settle anything still open". Not changed.
4. **Case: «Делает ли Victor это, кейс оставляет открытым: это вопрос для упражнений»** (was «остаётся
   открытым вопросом для упражнений»). Wording only.
5. **«Типичные ошибки маршрутизации — разбирать спор на обзоре и принимать решение в отчёте»** (was «спор
   поднимают на обзоре, а решение принимают в отчёте»). Assumes both are named as errors.

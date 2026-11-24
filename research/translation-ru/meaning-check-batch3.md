# Meaning check, batch 3: chapters 15, 16, 17, 18

A bilingual check of the literary edit against the English source (2026-11-24). For each chapter: every
doubt listed in `editing-chNN.md` section 4 gets a verdict, then the results of a spot-check covering the
mental model, a research passage, the case study, the exercises, and the takeaways, plus a mechanical
count of evidence labels. Fixes are minimal and keep the editor's style. Anchors, links, and numbers are
untouched. English was not edited. Possible problems in the English are listed at the end.

Totals: 24 doubts checked, 6 fixed (ch 15 ×1, ch 16 ×2, ch 17 ×1, ch 18 ×2); 4 further fixes from the
spot-checks (ch 15, ch 16, ch 17 ×2; none in ch 18). Validation: `tools/validate_book.py` passed.

## Chapter 15

| # | Doubt | Verdict |
|---|---|---|
| 1 | "keeps it honest, inside the organization's quarterly reset" | ok. "It" is the roadmap. «в промежутках между квартальными перезапусками» is a fair reading of "inside". |
| 2 | "little until the date, then the renewal" | ok. The renewal itself is what is lost after the date, so «а затем на кону продление» is right. |
| 3 | Reflection 2: "What would its cost of delay have been" | ok. The English is equally ambiguous; "would have been" points to the displaced quiet request, which is also the nearest antecedent in the Russian. |
| 4 | Velocity failure mode: "Compared across teams or used to judge them" | fixed: «по ней судят о работе» → «по ней оценивают сами команды». "Them" is the teams, not work in general or individuals. |
| 5 | "order files of up to 20,000 lines across delivery sites" | ok. «по нескольким площадкам доставки» renders "delivery sites"; "across" implies more than one. |

Further fixes:
- Kuhrmann et al.: "no method or practice guaranteed or prevented agility". «не гарантировали гибкости и не мешали ей» → «… и не исключали её». «Не мешали» claims no negative effect at all, which is broader than "did not prevent".

Spot-check (mental model and volume loop, the evidence section, prioritization as economics, case: methods table, how the 17 items were chosen, renewal commitments, decision for quarter 2, F1–F3, A1–A4, X1–X2, takeaways): otherwise no drift. Labels match.

## Chapter 16

| # | Doubt | Verdict |
|---|---|---|
| 1 | X2: "One director proposes…; another proposes…" | fixed: «Один член совета предлагает» → «Один из директоров предлагает». The English does not say whether these are board members or company directors; after «Совет директоров» the Russian now keeps the same ambiguity instead of choosing. |
| 2 | Little: "the law does not settle trade-offs" | ok. «не снимает компромиссов» matches "does not settle". |
| 3 | Case: "two more pieces of evidence" | fixed: «ещё два доказательства» → «ещё два набора данных». «Доказательство» reads as "proof", stronger than "evidence"; the two items are a dependency count and a breakdown. |
| 4 | "a story stalls" → «задача застряла» | ok |
| 5 | "Measure throughput four weeks before and after" | ok. The English implies four weeks on each side, and so does the Russian. |

Further fixes:
- Takeaways: "the quality program can only address failure recovery". «справится только с восстановлением после сбоев» → «может повлиять только на восстановление после сбоев». «Справится» promises success; the English limits only the scope.

Spot-check (mental model, Little's law with its cautions and WIP limits, case with both tables and the four decisions, F1–F3, A1–A3, X1–X2, takeaways): otherwise no drift. "Two infrastructure engineers rotate weekly as the interrupt role" is rendered as the two alternating; the English allows that reading. Labels match.

## Chapter 17

| # | Doubt | Verdict |
|---|---|---|
| 1 | Cockburn: "a thinly connected functioning architecture" | fixed: «как тонкую, связанную и работающую архитектуру» → «как работающую архитектуру, где компоненты соединены лишь тонкими связями». "Thinly" modifies "connected"; the edit had split them into three separate adjectives. |
| 2 | Playbook 7: "If the onboarders are on the critical path" | ok. The onboarders are the people introducing the newcomers, as the editor read it. |
| 3 | Reflection 5: "move the hardest unknown to next week" | ok. In context it means bringing it forward, as rendered. |
| 4 | "Some practitioners drop estimates" | ok. The English says practitioners; the Russian has «специалисты-практики». |
| 5 | "other functions" → «подразделения» | ok |
| 6 | "used several dates in open deals" → «назвал несколько этих дат» | ok. The dates are those of the 17 committed items just mentioned. |
| 7 | "five Orders engineers and two Customer Experience web engineers, half of Orders' headcount" | ok. The Russian follows the English (see the English problems below). |

Further fixes:
- Case: "All 17 items went to sales and customer success as committed". «ушли в продажи и к клиентам» → «ушли в продажи и в службу по работе с клиентами». Customer success is a department (Sofia Alvarez's), not the customers; the edit said the items went to customers.
- Jørgensen: "experts' uncertainty ranges are far too narrow". «слишком узкие» → «явно слишком узкие», restoring "far".

Spot-check (mental model and loop, the estimation research with Buehler, Griffin, and Ross and Halkjelsvik and Jørgensen, the walking skeleton, case, F1–F3, A1–A3, X1–X2, takeaways): otherwise no drift. Labels are present; "This book's recommendation" is bolded once in each language.

## Chapter 18

| # | Doubt | Verdict |
|---|---|---|
| 1 | "the next section states the book's position" | ok as a translation. The English points to the wrong section (see the English problems below). |
| 2 | "The evidence on this is contested, and that is the book's position" | ok. «Данные по этому вопросу противоречивы, и такое прочтение — позиция книги» keeps both clauses. The label is unbolded prose in the English, so «противоречивы» is acceptable (as in chapter 14). |
| 3 | Case: "a consultancy article he was sent" | fixed: «в присланной ему статье консалтинговой компании» → «в статье консалтинговой компании, которую прислали Rajiv». In the English "he" can only be Rajiv (the board is "it"); in Russian «ему» could also attach to «совет директоров». |
| 4 | "One person, often a staff engineer with platform engineers, owns definitions" | ok. The Russian follows the English (see the English problems below). |
| 5 | DevEx: "fixing it is a decision" | fixed: «её исправление — вопрос решения» → «… — вопрос управленческого решения». «Вопрос решения» could read as "a matter of finding a solution"; the English means it is within a manager's power to decide. |
| 6 | "Every pipeline emits the same deployment event" | ok. The fields in parentheses show a shared format, so «событие развёртывания одного и того же формата» is right. |
| 7 | "the four shell-script services" | ok. The cast confirms services deployed by shell scripts, and `baseline-data.ru.md` uses the same wording. |

Spot-check (mental model and gaming loop, how the DORA research was produced, the SPACE illustration label, the 2023 dispute, why the book refuses individual scoring, case including the measurement-set table and its Excluded row, F1–F3, A1–A3, X1–X2, takeaways): no further drift. Labels match, including "this book's illustration" → «иллюстрация книги».

## Possible problems in the English (not edited)

1. **Ch 18, The 2023 dispute**: "the next section states the book's position". The next section is "How each metric is gamed, and its pair"; the position is in the section after it ("Why the book refuses individual productivity scoring"). Suggest "a later section" or naming it.
2. **Ch 18, end of "How the research was produced"**: "The evidence on this is contested, and that is the book's position." The position is the reading in the previous sentences, not the fact that the evidence is contested. Suggest "This is contested; the reading above is the book's position."
3. **Ch 18, Enterprise Application**: "One person, often a staff engineer with platform engineers, owns definitions" names one owner and then a group. Suggest "One person, often a staff engineer supported by platform engineers".
4. **Ch 17, Engineering Organization Example, assumption 1**: "five Orders engineers and two Customer Experience web engineers, half of Orders' headcount". Seven people equal half of Orders' 14 only as a count; five of them are from Orders. Suggest "seven engineers, equal to half of Orders' headcount".
5. **Ch 16, X2**: "One director proposes…; another proposes…" does not say whether these are board members or company directors. Northstar has one engineering director, so board members seem intended; the author should confirm.
6. **Ch 16, Case**: "Two infrastructure engineers rotate weekly as the interrupt role" allows two readings (the two alternate, or a pair is on duty each week). Tom Becker's objection that "the rotation fragmented the two engineers' weeks" fits either.
7. **Ch 15, Reflection question 2**: "What would its cost of delay have been" does not say whether "its" is the loud or the quiet request. The quiet one seems intended.

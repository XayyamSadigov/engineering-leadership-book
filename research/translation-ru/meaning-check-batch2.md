# Meaning check, batch 2: chapters 8, 9, 10, 11, 12, 14

A bilingual check of the literary edit against the English source (2026-11-23). For each chapter: every
doubt listed in `editing-chNN.md` section 4 gets a verdict, then the results of a spot-check covering the
mental model, a research passage, the case study, the exercises, and the takeaways, plus a mechanical
count of evidence labels. Fixes are minimal and keep the editor's style. Anchors, links, and numbers are
untouched. English was not edited. Possible problems in the English are listed at the end.

Totals: 39 doubts checked, 5 fixed (ch 8 ×2, ch 9 ×1, ch 12 ×2); 4 further fixes from the spot-checks
(ch 9, 10, 11, 12). Validation: `tools/validate_book.py` passed.

## Chapter 8

| # | Doubt | Verdict |
|---|---|---|
| 1 | "liability" → «становится источником риска» | ok. The legal sense is carried by "where equal pay law applies". |
| 2 | "Differences within a band are legitimate" | fixed: «Различия внутри вилки законны» → «Различия внутри вилки обоснованны» |
| 3 | Sunil: "capped at 8 percent that year, then about 3 percent a year" | ok. "That year" is the promotion year, and 3% is the annual raise after it. |
| 4 | "One of two engineers who left" → two sentences | ok |
| 5 | References: «прочитанный полностью» | ok as a translation. The English line itself says "read in full" (see the English problems below). |
| 6 | X2 "possible pay compression" | fixed: «возможное сжатие оплаты» → «возможное сужение разброса оплаты». The X2 solution and the Cullen paragraph show that this means narrowing (transparency compresses pay), which the Russian Cullen paragraph already renders as «сузит разброс оплаты». |

Spot-check (mental model, why one manager's judgment is not enough with its Castilla, Benson, and Rivera
findings, calibration, offer level, case, all eight exercises, takeaways): no further drift. Evidence
labels match the English.

## Chapter 9

| # | Doubt | Verdict |
|---|---|---|
| 1 | "Once people distrust these choices, they are hard to reverse" → «переломить ситуацию трудно» | ok. In the English, "they" can refer to the choices or to the distrust. The Russian covers the intended sense (lost trust is hard to win back). |
| 2 | "sometimes a job" → «а иногда и места работы» | ok |
| 3 | Mager and Pipe: "if the person's job truly depended on the task" | ok. The Russian follows the English, which says "job" (see the English problems below). |
| 4 | "Rotating the Jenkins interrupts added load" (past tense) | ok. The English is also in the past tense (see the English problems below). |
| 5 | 13 h × 3 = 39 h; 3.1 × 3 ≈ 9 engineer-weeks | ok |
| 6 | "a reduction in force used to remove people whose managers never acted" | fixed: «избавиться от людей, с которыми их руководители так и не поработали» → «избавиться от людей, чьи руководители так и не приняли мер». The English means the managers never acted on performance. |

Further fixes:
- Forced distribution: "The simulation does not report effects on cooperation…" «Влияния на сотрудничество… симуляция не показывает» → «О влиянии на сотрудничество… симуляция ничего не сообщает». «Не показывает» read as "found no effect", which is a stronger claim than "does not report".

Spot-check (mental model, rater-effects research, forced distribution, engineering example tables, case,
F1–F4, A1–A3, X1–X2, takeaways): otherwise no drift.

## Chapter 10

| # | Doubt | Verdict |
|---|---|---|
| 1 | Hom: "losing two of three ledger experts is not twice the cost of losing one" | ok. The Russian is as ambiguous as the English (see the English problems below). Not changed, so as not to add a claim. |
| 2 | "Managers who are scored on results coach the answers" | ok. The English is equally unspecific. |
| 3 | "Her full redesign of core/customer … is not funded" → «Её проект полной переработки» | ok. It is her proposal; only a first slice is funded. |
| 4 | "a lost decision" → «проигранный спор о решении» | ok |
| 5 | Tomasz: "Two named…; one, Tomasz Wierzbicki, also said…" | ok. The English leaves open whether Tomasz is one of the two, and so does the Russian. |
| 6 | "starts the person looking, sometimes within weeks" | ok. "Within weeks" times the start of the search after the event, and the Russian says the same. |
| 7 | "what one thing you would change" | ok |

Further fixes:
- Self-determination theory: the evidence label "**contested**" was rendered «**оспаривается**». It now uses
  the fixed rendering: «— **вопрос спорный**, и статья сама это отмечает».

Spot-check (mental model and table, decision paths, embeddedness, the SDT passage, counter-offers, case,
exercises, takeaways): no other drift. All labels are present.

## Chapter 11

| # | Doubt | Verdict |
|---|---|---|
| 1 | "my change broke this" → «это сломалось из-за моего изменения» | ok |
| 2 | Edmondson row, team efficacy | ok. The English says "Team efficacy (belief in the team's ability)". |
| 3 | Skip-level: "send it back with the engineer's permission" → «Верните его руководителю команды» | ok |
| 4 | "what it had told a newcomer" → «новому директору» | ok. The newcomer is the new director (seniors spoke to "the new director"). |
| 5 | "For about two years … had held" → «проводит» | ok. The English mixes the past perfect with the present tense ("presents", "speaks"). The Russian present matches the rest of the paragraph. |
| 6 | Google row: "Peer review" → «Не прошло рецензирования» | ok |
| 7 | F1 "each of the three claims" (four sentences) | ok. The English also says three; the first sentence is the conclusion, and the three claims support it. |
| 8 | "were configuration changes" → «были вызваны изменениями конфигурации» | ok |
| 9 | CTO: "defines … more effectively than any training program can repair" | ok as a rendering. The English sentence is awkward (see the English problems below). |

Further fixes:
- F2 (c): "dates renegotiated two weeks early". «даты пересматривают за две недели» could read as "within two weeks", so it is now «… за две недели до срока».

Spot-check (mental model, research table and the paragraph after it, Lenberg and Feldt, Orders and Payments
example, case, exercises, takeaways): otherwise no drift.

## Chapter 12

| # | Doubt | Verdict |
|---|---|---|
| 1 | "balance-sheet risk that never appears on a balance sheet" | ok. It means a real risk to company value, not a reporting risk. |
| 2 | Rigby: "reduced expected loss by up to 15 percent"; "In a bad case" | fixed: «снижало ожидаемые потери до 15%» → «снижало ожидаемые потери максимум на 15%». "Bad case" (not "worst"), so «В неудачном случае» stays. |
| 3 | "owned documents and reviews by others" | ok. The English is equally ambiguous, so the ambiguity is kept. |
| 4 | "will be quoted back at the team when it would be convenient to help" | ok. «будут цитировать команде» follows the English. |
| 5 | Working agreement 4: "the rest plan without it" | fixed: «остальные планируют без него» → «остальные планируют свою работу без поправки на запросы». "It" is the interrupt work, not the person on duty. |
| 6 | export-svc: "since it is tier 3" | ok. The English "since" is causal, and «с учётом того, что» keeps it. |

Further fixes:
- X2: "what decision he should expect it to inform". The edit had «какое решение, по замыслу Victor, оно должно помогать принимать», which shifts the judgment to Victor's intent. It is now «какое решение, по вашему мнению, оно может помочь ему принять».

Spot-check (mental model, Mathieu and Rapp, Project Aristotle and Lencioni, Rigby, Staff engineers, case and
charter table, exercises, takeaways): otherwise no drift. Labels match.

## Chapter 14

| # | Doubt | Verdict |
|---|---|---|
| 1 | Reflection question 1: "who would have heard about it later than they did?" | ok. The Russian follows the English exactly. The English question may be inverted (see the English problems below). |
| 2 | Bogotá "at most one hour from Minneapolis" → time difference | ok. The async section ("sites are an hour apart", contrasted with Chicago and Kraków seven hours apart) and F2 ("one hour away in time") confirm a time difference. |
| 3 | "At organization scale" opener dropped | ok. The scale is still stated. |
| 4 | "A contributing factor; nobody ever set him expectations…" → «При этом» | ok. The semicolon in the English is explanatory, not "because". The takeaway "never told what was expected" is consistent with that reading. |
| 5 | Trade-off: single office, «к тому же» before the RCT clause | ok. In the English, the RCT clause is a further cost of one office (it forgoes the retention gain from home days). |

Spot-check (mental model, research table and the book's position, hypothetical Chicago and Kraków team,
case and diagnosis, options table, exercises, takeaways): no drift found. Labels are present ("contested" in
the position paragraph is unbolded prose in the English and is rendered «Данные противоречивы»: acceptable).

## Possible problems in the English (not edited)

1. **Ch 8, References, Directive (EU) 2023/970**: "read in full" is an access note in reader text, which CLAUDE.md §7 forbids. Ch 12 has a similar note in prose, "the abstract reports" (Mathieu and Rapp).
2. **Ch 8, X2**: "pay compression" means narrowing of pay, as in the Cullen paragraph and the X2 solution. The same chapter defines **compression** as new hires paid above tenured peers. The English term clashes with its own definition. Suggest "narrower pay spread".
3. **Ch 9, Mager and Pipe**: the test is given as "if the person's job truly depended on the task". The classic formulation is "if their life depended on it". Check against the source; a paraphrase is acceptable if intended.
4. **Ch 9, Case Study**: "Rotating the Jenkins interrupts added load…" is in the past tense, but it describes Tom's not-yet-approved proposal. "Would add" seems intended, unless rotation had already started as a trial.
5. **Ch 9, Why This Matters**: "Once people distrust these choices, they are hard to reverse": "they" is ambiguous between the choices and the distrust.
6. **Ch 10, Hom et al.**: "losing two of three ledger experts is not twice the cost of losing one" can be read as "less than twice". The collective-turnover point suggests "more than twice".
7. **Ch 11, CTO Perspective**: "defines the organization's safety more effectively than any training program can repair" mixes two verbs. Perhaps "damages the organization's safety more than any training program can repair".
8. **Ch 11, Payments case**: mixes the past perfect ("had held") with the present tense ("presents") in one description.
9. **Ch 14, Reflection question 1**: "If … made with everyone remote, who would have heard about it later than they did?" If the intent is to expose proximity bias, "sooner" may be meant. As written, it asks who benefits from colocation, which is also defensible. The author should confirm.

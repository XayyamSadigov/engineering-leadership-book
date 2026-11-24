# Meaning check, batch 4: chapters 19, 20, 23, 24

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). These chapters were translated in this wave, so the check went further than for an edit
alone:

1. Every doubt in `editing-chNN.md` section 4 and in the translators' notes (`notes-t4.md`, `notes-t6.md`)
   gets a verdict.
2. Completeness: a script split both files into H2/H3 sections and counted paragraphs, list items, table
   rows, admonitions, and code blocks per section. All counts and anchors match in all four chapters
   (19: 25 sections; 20: 26; 23: 26; 24: 28). A paragraph-level length ratio flagged four paragraphs, and
   each was read; none had an omission.
3. Meaning: every paragraph of all four chapters was read side by side with the English, not only a sample.
   That covered the mental model, the research passages, the Northstar examples and case, all exercises,
   reflection questions, takeaways, and reference lines. Evidence labels were checked one by one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 21 doubts checked, 1 fixed (ch 20). Further fixes from the full read: ch 19 ×1 (terminology),
ch 20 ×1 (label bolding), ch 23 ×1, ch 24 ×6. Validation: `tools/validate_book.py` passed.

## Chapter 19

| # | Doubt | Verdict |
|---|---|---|
| 1 | 27 defects "built exactly as specified" → «точно соответствовали спецификации» | ok |
| 2 | Internal quality "how easy the system is to change safely" → «без риска» | ok |
| 3 | Note "Deployments in the quarter are three times the baseline monthly figure", with «поэтому» | ok. The note explains the unit (quarter versus month), not growth. |
| 4 | "Four answers named the QA group" → «Четверо указали» | ok. Each manager gave one answer. |
| 5 | "the position here is this book's recommendation" → «дальше — рекомендация книги»; "Teams own the quality outcomes of their changes" → «Качеством своих изменений владеют сами команды» | ok. The label is kept and bolded as in the English. "Quality outcomes" is slightly compressed but the claim is the same. |
| 6 | Central QA "for specialized or independently mandated testing" | ok |
| t4 | Part V list: "pricing technical debt" → «как оценить технический долг в деньгах»; "merge to customer" → «от слияния кода до клиента» | ok |
| t4 | Two failure modes without a Signal field | ok. The Russian follows the English. |

Further fixes:
- "customer success lead" (Garvin paragraph) and "head of customer success" (F1): «службы успеха клиентов»
  → «службы работы с клиентами». This is terminology, not meaning: chapter 24 (`notes-t6.md`) and `cast.ru.md`
  use «работа с клиентами» for Sofia Alvarez's function, and «успех клиентов» appeared nowhere else.

Full read: no drift. The Garvin approaches and dimensions, Mäntylä et al. (fix rate is not detection
effectiveness), the Firefox study, the ISO/IEC 25010 "standard" label, the detection-point table, the
normalization table with its note, the 1:1 scene, and the week-3 session all match. "Complete user-facing
alerts" is rendered «полный набор алертов по видимым пользователю симптомам», which is fair given the
operational minimums.

## Chapter 20

| # | Doubt | Verdict |
|---|---|---|
| 1 | Opening "because a tool or a habit makes it happen" | ok |
| 2 | "each checked, sampled, or reported per component" → «проверяется — сплошь или выборочно —» | fixed: «сплошь» → «автоматически». The 19 are 9 tool-checked, 5 sampled in review, and 5 tier 1 standards reported per component, so "checked" means checked by a tool. |
| 3 | Marcus Oyelaran: "The director counted it inside the allocation instead" | ok. Instead of runbook work counting as process on top of the 25 percent, it was counted inside it. «в счёт выделения, а не сверх него» is right. |
| 4 | "share compliant" → «доля соответствия стандарту» | ok |
| 5 | "a public mapping of components to levels" | ok |
| 6 | Info box mixes past and present | ok. The English mixes them too ("has classified … and is publishing"). |
| t4 | "compliance theater" → «театр соответствия» | ok for meaning; the term choice is the maintainer's call, as the note says. |
| t4 | Decision diagram "Ever wrong?" → «Ошибается?» | ok |

Further fixes:
- Governance bodies: "Three design choices, this book's recommendation, keep governance out of it". The
  Russian had bolded «(**рекомендация книги**)»; the English label is unbolded prose here. Unbolded to match.

Full read: no drift. RFC 2119 and Schwartz (rules versus guidance), Sadowski et al. (effective false
positive, the 3,954/640 fix-it week, the 10 percent thresholds), Johnson et al. (research finding, small
qualitative sample), Meyer and Rowan ("this book's analogy"), the tiering and SLSA passage, the queue
arithmetic, the Northstar build-system table and triage (14 kept, 17 guidance, 21 retired, 19 mandatory),
the exemption-register table, the day-90 table, and all exercises match.

## Chapter 23

| # | Doubt | Verdict |
|---|---|---|
| 1 | Bacchelli and Bird "studied tool-based review at Microsoft" → review done in dedicated tools | ok. That is what the English means (modern, tool-based code review), not tools used by the researchers. |
| 2 | Knight Capital "seven correct servers" → «правильно обновлённых» | ok. The seven had received the new code. |
| 3 | Added signpost «Из таблицы видно три вещи» | ok. The English has "First… Second… Third" with no lead-in; the signpost adds no claim. Keep or drop at the maintainer's taste. |
| 4 | "Release engineering made it longer" → «Из-за того, как были устроены релизы, инцидент затянулся» | ok. The next sentences give the mechanism (the train rollback failed against the migrated schema), and nothing narrower is meant. |
| t6 | Knight Capital "nobody reviewed the deployment" → «само развёртывание никто не проверял» | ok |
| t6 | "Flag debt" without a Signal field | ok. The Russian follows the English. |

Further fixes:
- CI evidence (Vasilescu et al.): "is associated with integrating more contributions" → «принимает больше
  внешних вкладов»: dropped «внешних». The English does not limit the finding to outside contributors, so
  the word narrowed the claim.

Full read: no drift. Rigby and Bird (66 to 150 percent), McIntosh et al. (up to two and five defects),
the evidence labels (observational research findings, Sadowski as documented practice, smaller changes as
practitioner consensus, DORA as industry research and correlational), the pipeline-properties table, the
false-red note, trunk-based development and its two exceptions, Hodgson and Rahman et al., the SRE workbook
canary passage, DORA change approval and segregation of duties, the lead-time decomposition, the release
strategy table, the staged playbook, the case (the week-9 Sev1 and the interim rule), and all exercises
match.

## Chapter 24

| # | Doubt | Verdict |
|---|---|---|
| 1 | INC-413: "whether it justifies a fallback route is not [a policy question]" | ok. The English has the same elliptical form; «вопрос уже не политики» keeps it. |
| 2 | "about 3.7 times the payment budget" → «в 3,7 раза больше, чем весь бюджет» | ok. 890 failures against 240 is about 3.7 times the budget. The Russian «в N раз больше» conventionally means N times as much. |
| 3 | Example policy "other than the most urgent (P0) issues and security fixes" | ok. P0 refers to fixes for P0 issues, as in the Workbook policy. |
| 4 | A2: "its author has left" (author of the scripts or the service) | ok. The English is equally ambiguous; kept. |
| 5 | "Experts sit behind the rotation as a named escalation tier" | ok |
| t6 | "Its value is a decision made in advance" → «Ценность политики…» | ok. "Its" is the policy. |
| t6 | "the next work buys reliability" → «следующая работа идёт на надёжность» | ok |

Further fixes:
- Implementing SLOs: «Ещё авторы советуют … и по умолчанию предлагает» → «предлагают» (agreement).
- Observability: "**What to instrument first** (this book's recommendation)". The Russian had bolded the
  label; the English does not. Unbolded to match (the translators' note says this was intended).
- CTO perspective, People: «Её место — в наборе политик CTO» had no antecedent to agree with (дежурства,
  вопрос) → «Этому вопросу место в наборе политик CTO».
- Reflection 2: "and what are they afraid of missing?" → «что, по его мнению, можно пропустить?» lost the
  fear; now «и что он боится пропустить?».
- Reflection 5: "Is there a way your customers are hurt that none of your dashboards would show?" had become
  «Можете ли вы навредить клиентам так…» (whether you could harm them). Now «Страдают ли ваши клиенты от
  чего-то, чего не покажет ни один дашборд?».
- Takeaways: "a freeze … becomes permanent or ignored" → «либо её перестают замечать» → «либо её
  игнорируют». "Ignored" means people disregard the freeze, not that they fail to notice it.

Full read: no other drift. The SLI/SLO/SLA definitions and owners, the customer-detected table and INC
note, the error-budget policy (20 percent postmortem rule, documented practice with no outcome data), the
six conditions where budgets fail, the burn-rate table and the 14.4 derivation, the observability passage
("expert opinion" of vendor authors), the readiness reviews at Google and AWS, the on-call research
(research findings from outside software), the rotation elements (practitioner consensus), the SLO design
and both replays with their note, the readiness bar, the case (the reporting-mode policy, notification-svc
to tier 2, 47 to 29 percent), and all exercises match.

## Possible problems in the English (not edited)

1. **Ch 24, Engineering Organization Example, INC-413 replay**: "Whether that should freeze releases is a
   policy question; whether it justifies a fallback route is not." The elliptical "is not" can read as
   "does not justify one". Suggest "…is an engineering question, and the answer is yes" or similar.
2. **Ch 24, A2**: "deployed by shell scripts that one person understands, its author has left" does not
   say whose author (the scripts' or the service's) and sits oddly beside "one person understands". If the
   one person who understands the scripts is still there, "its original author has left" would be clearer.
3. **Failure Modes without a Signal field** (also noted by the translators): ch 19 "The platform that owns
   nothing" and "Ranking by exposure"; ch 20 "Warning wallpaper" and "Standards instead of ownership"
   (which has no Countermeasure either); ch 23 "Flag debt"; ch 24 "The vanity SLO", "The 4xx blind spot",
   "The permanent freeze", "Alert accretion", "The invisible pager". The other entries have one, so the
   author may want to make them consistent.

# Meaning check, batch 22: chapters 57 and 58

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 21:

1. Every doubt in `editing-ch57.md` and `editing-ch58.md` section 4, the term proposals (section 3), and
   the translator's notes (`notes-t23.md`) get a verdict.
2. Completeness: headings (57: 26; 58: 27, anchors equal to the slugified English headings), table lines
   (57: 55; 58: 64), list items (57: 38; 58: 35), ordered items (57: 17; 58: 25), exercises (8 each),
   Mermaid blocks (57: 4; 58: 3), admonitions (2 each), relative link targets (57: 66; 58: 64, identical
   in order) and citation link texts (57: 37; 58: 41) match the English. Every number in table lines is
   identical to the English. No wrapped line begins with a number and a period outside a real ordered
   list. Table rows, exercises, reflection questions, takeaways, and reference lines were also checked by
   eye: nothing is missing.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Halvard and Northstar names and numbers were checked against the English. In
   chapter 58 every legal statement (the "not legal advice" box, the EEOC guidance and its group
   disclosure rule, the WARN Act and EU directive rows, counsel's advice at the EU site, the
   conversation script and the "do not say" list) was checked for strength, hedges, and conditions.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched; the "Не
юридическая консультация" box is unchanged. English was not edited.

Totals: 13 editor doubts, 8 term proposals, and the translator's notes checked; one doubt (ch 57 no. 4)
led to a change. Further fixes from the full read: ch 57 ×3, ch 58 ×3.
Validation: `tools/validate_book.py` passed.

## Chapter 57

| # | Doubt | Verdict |
|---|---|---|
| 1 | «заранее, до того как такой день наступит» for "before the day" | ok. "The day" is the day a disclosure obligation arises; the Russian keeps the reference without inventing one. |
| 2 | «нередко отчасти создаёт…, и к тому же оно может быть ресурсом» | ok. The English makes two claims ("is often partly the change agent's doing, and it can be a resource"), both credited to Ford et al. |
| 3 | «Если ни поддержка, ни эскалация не помогли» for "after commitment and escalation are both exhausted" | ok. The takeaway ("if you cannot commit and escalation has failed") confirms the reading; «открыто его принять или уйти» matches "accept it openly or leave". |
| 4 | Greg: «сопротивление Greg может смениться поддержкой» | **Fixed.** The English "whether engineering keeps that promise would turn his resistance into support" names the promise as the deciding factor ("would", not "could"). Now «От того, будет ли разработка выполнять это обещание, и зависит, сменится ли сопротивление Greg поддержкой». |
| 5 | «с отчётностью вместе с аудитом серьёзности» | ok; "reported with the severity audit". |
| 6 | «три таблицы» in the Decision Framework | ok; translated as written. See English problem 1. |
| term | бридж / созвон | Not changed; maintainer decision. Both are glossed and read clearly here. |
| term | трактовка, молчаливое подчинение / мнимая поддержка, высказывание (voice) | ok. |
| t23 | Term list (треки, бридж, ответственный руководитель, SCCT, инструктирующая / адаптирующая информация, кластеры, отрицать / преуменьшать / восстанавливать, приписанная ответственность, высказывание / уход / молчание, поддержать решение, условие пересмотра, планка, трактовки, карточка кризисных ролей, резервный канал, failure-mode names, «вывод книги») | ok; consistent through the chapter. |
| t23 | Halvard figures (8,600, 64 percent, 1,500 a minute, about 168,000), mental-model sentence, X2 "general counsel" | ok. |

Further fixes:
- GitLab case: "down for about 18 hours after backups turned out to have been failing silently" had
  become «…потому что резервные копии, как выяснилось, давно и незаметно не создавались», which adds
  "for a long time" and turns "failing" into "not created". Now «…около 18 часов: как выяснилось,
  резервное копирование незаметно давало сбои».
- Commit-or-escalate table: "The same executive overrides the same process every quarter" had become
  «…отменяет один и тот же процесс» ("abolishes"). Now «…действует в обход одного и того же процесса».
- Example: "up to about $4.6 million of sales" had lost "about". Now «примерно до $4,6 млн продаж».

Claims checked one by one: the SEC rule (standard; "must generally", four business days after judging
materiality); Stribblehill (documented practice); Weick (research finding, a single case) and the
book's inference from it; Cook (no label, as in the English); Coombs (research finding, mostly scenario
readers; four points, the three clusters, history as intensifier, rebuild for preventable and for
accidental with history, no mixing, over-accommodation); the book's reading on provider-caused outages;
Kim et al. (research finding, two experiments); Atlassian and GitLab (documented practice; 883 sites,
775 customers, up to 14 days, about 41 hours; about 18 hours, names redacted in future); Milliken et al.
(research finding, exploratory); Detert and Burris (research finding, one restaurant chain); Hirschman,
Grove (expert opinion); Bezos (documented practice); de Wit (116 studies, research finding,
correlational); the escalation table and the reading table (this book's recommendation); Ford et al.
and Piderit (expert opinion); Oreg et al. (79 studies, research finding). Example: 130 and 41
engineers; 99.95 percent, 10 and 25 percent credits, 99.0, 5 percent threshold; the timeline 14:05 to
17:55; 168,000, 65,000 of 112,000, 99.54 percent and 200 minutes, $380,000 on $3.8 million, $71 average
order; 11 minutes late against 15; about 2,300 tickets against 150 a day; options $380,000, $470,000
(15 percent, 140 merchants), $760,000 (20 percent). Case: weeks 41 to 49; 14 against 15; the counter (40
over year 2, 99.9 percent, two quarters above 12); about two quarters of five at a true average of 9;
the floor; the five-pushback table (7,800 corrected orders in 28 days, 1.3 percent; 5 of 17 dates; 64,
41, 23 engineers); Greg's two engineers and five working days. Exercises (F1 to X2, including A2's week
51, 95 minutes, three of the 40 largest, twelve commanders trained in weeks 4 and 5; X1's two hours a
week measured in weeks 44 to 46), reflection questions, takeaways, and references match.

## Chapter 58

| # | Doubt | Verdict |
|---|---|---|
| 1 | «касается последствий, а не методов проведения» for "technique" | ok; "technique" is how a reduction is carried out. |
| 2 | Sverke: «вредит отношению к работе и здоровью» for "harms attitudes and health" | **Fixed** (see below). The meta-analysis covers job attitudes and organizational attitudes; «к работе» alone was narrower. |
| 3 | «Отбор в команду поддержки меняют в двух местах» for "Two sustaining selections change" | ok. |
| 4 | «письменно закрепляет за командой… трёхлетний мандат» for "commits in writing that… has" | ok; a written commitment, as in the English. |
| 5 | «корректирующие действия по их итогам касаются ранбуков» for "with actions on the runbooks" | ok; the actions are the reviews' actions. |
| 6 | F1: «который Imani Okonkwo отправляет финансам» for "sent" | ok. The example narrates Imani's written rejection in the present tense; the exercise asks the reader to write that reply. No hypothetical is meant. |
| 7 | «письменно и до решения, следуя тесту…» | ok; wording only. |
| term | оставшиеся, сокращение в рассрочку, уровень как понижение | ok. |
| term | выпуск (output) vs «объём работы» in prose | Not changed; maintainer decision. «падение выпуска», «потерянный выпуск» are understandable in context. |
| t23 | Term list (сокращение / увольнение, оставшиеся, выходное пособие и отказ от претензий, критерии отбора, несоразмерное влияние, проверка владения, день уведомления, команда поддержки, контракт на передачу дел, юрист по трудовому праву, вытеснение (bumping), WARN Act gloss, директива ЕС, EEOC, Министерство труда США, люди / продукт / платформа / политики, сохранить / отложить / интегрировать поэтапно / поглотить, тезис и модель сделки, failure-mode names) | ok; consistent through the chapter. |
| t23 | Not-legal-advice box | ok; same strength and conditions: law differs by country, state, sometimes city and changes; the chapter shows kinds of obligations and does not say what applies to you; counsel for every reduction and acquisition, per jurisdiction, before the plan is fixed. |
| t23 | "Four families of criteria" with an EEOC list of three; the ungrammatical rolling-layoff sentence rendered by sense | ok in Russian; see English problems 2 and 3. |
| t23 | Step 5 (three separated, four roles affected), "flat titles", CTO gloss placement | ok. |

Further fixes:
- Sverke: «вредит отношению к работе и здоровью» → «вредит отношению людей к работе и к компании, а также
  их здоровью», within what the source says (job and organizational attitudes, health).
- Notice and consultation: "may be unlawful in some places and merely unkind in others" had become
  «…просто жестоким» ("cruel"), harder than "unkind". Now «…просто нечутким».
- Truck factor: "would leave the project in serious trouble" had become «поставит проект в серьёзное
  положение», which is unclear Russian. Now «создаст проекту серьёзные проблемы».

Legal and people statements checked one by one: EEOC (standard, guidance without the force of law; the
three criteria; the waiver definition; "must disclose the ages and job titles of those selected and not
selected in the unit", introduced "for example", for group age-claim waivers); "HR and counsel must
review … before it is final"; the three fairness checks and the lawful-but-wrong moves (this book's
recommendation); WARN (standard; "broadly 100 or more full-time workers, per site"; smaller layoffs
within 90 days "can be aggregated"; at least 60 days' written notice; states add laws); the EU directive
(standard; thresholds "such as" 10 over 30 days at 21 to 99 workers; through national law; consult in
good time aiming at agreement; effective no earlier than 30 days after notifying the authority); counsel
advising EU consultation "under national law and Halvard's policy" though below thresholds; the
notification-day table (access changes after each conversation, never before); the manager's script
(news first, one-line reason, next steps), "never a comparison with a named colleague", and the three
"do not say" items (illustrative; wording approved per jurisdiction); the survivors' note; the director's
commit-or-escalate duty and support for managers. None is softened or hardened.

Studies and arithmetic: Datta et al. (review); Trevor and Nyberg, Brockner et al. 1987 and 1990, Sverke
et al., de Jong et al. (research findings); Avelino et al. (65 percent of 133, truck factor 2 or less),
Rigby et al., Mockus (research findings in limited settings); King et al. (research finding); Puranam,
Paruchuri (with the book's inference to software), Graebner, Ranft and Lord (research findings, limited
samples); Haspeslagh and Jemison, Larson (expert opinion); Conway. Example: Imani Okonkwo, 110 engineers,
14 manager roles (one vacant), Mateo Rinaldi 5/38, Ruth Halloran 5/40, Tobias Engel 4/32; 15 percent,
about 17; FTE 2 + 4 + 3 + 5 = 14; 32 → 14, 18 roles, 4 placed, 14 separated, managers 4 → 2; 38 → 40,
40 → 42, 110 → 96, 12 manager roles; Leah Marchetti; 21 components, three tier 1, 12 months, two
quarters, five gaps, two closed, three transition contracts; 6/7/1, $2,795,000, $698,750, 3.0 months;
11 US and 3 EU, four EU roles, five weeks. Enterprise: 5 departures, about 21 against 12 percent, 2.9 a
quarter for 96; 3 of 5 from the 14; incidents 2 → 4, one Sev1; 71 and 38 percent; then 3 departures,
about 12.5 percent, 2 incidents, 54 percent; $215,000 against $2.8 million. Case: Henrik Sørlie, 100
engineers, Esther Castellanos, Kenji Iwasaki; Corvane 34 engineers and 4 managers, Dalia Ferraz; 11
services, rotation of eight, 6 of 11 with truck factor 1 or 2, 7 engineers; 22 engineer-quarters, about
$1.18 million; months 5, 6, 9; 11/19/4, about $7.0 million; two of seven key engineers, one moved to
Staff; 32 of 34, a key engineer in month 4, feature in month 5, four services first. Exercises (F1 to
X2, including X1's week 50, 10 percent, $1.67 million of $16.73 million, nine seats at $185,000, 87 seats
= 80 + 6 + 1; X2's 20 engineers and a third of the roadmap), reflection questions, takeaways, and
references match.

## Possible problems in the English (not edited)

1. **Ch 57, Decision Framework**: "Use the three tables together" introduces one table, one diagram, and
   one paragraph. "three tools" would fit. The Russian keeps «три таблицы».
2. **Ch 58, Selection criteria**: "Four families of criteria are common" is followed by an EEOC list of
   three; the fourth (skills) appears only in the table. The sentence could say the table adds skills.
3. **Ch 58, Failure Modes, "The rolling layoff"**: "each below a notice threshold, which they can be
   aggregated to cross anyway" is ungrammatical; presumably "though they can be aggregated to cross it
   anyway". The Russian renders the sense.
4. **Ch 57, References**: Edmondson, 1999 is listed but not cited in the chapter text.
5. **Ch 57, The Mental Model**: the paragraph after the first diagram has an overlong source line (the
   "incident bridge" gloss); ch 58 lines 275, 293, 461 likewise. Cosmetic.

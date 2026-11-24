# Meaning check, batch 23: chapters 59 and 60

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 22:

1. Every doubt in `editing-ch59.md` and `editing-ch60.md` section 4, the term proposals (section 3), and
   the translator's notes (`notes-t24.md`) get a verdict.
2. Completeness: headings (59: 26; 60: 37, anchors equal to the slugified English headings), table lines
   (59: 70; 60: 85), list items (59: 33; 60: 68), ordered items (59: 18; 60: 16 against the English 17,
   see English problem 1), exercises (59: 9; 60: 10), Mermaid blocks (2 each), admonitions (2 each),
   relative link targets (59: 61; 60: 104, identical in order) and citation link texts (59: 20; 60: 14)
   match the English. Every number in table lines is identical to the English; the only differences are
   trailing commas and, in ch 59's Northstar inventory, one row where word order moves "3 of 15" before
   "13 of 15" inside the cell. No wrapped line begins with a number and a period outside a real ordered
   list. Table rows, exercises, reflection questions, takeaways, and reference lines were also checked by
   eye: nothing is missing.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar and Halvard names and numbers were checked against the English. In
   chapter 60 every instruction, stage field (Produce / Add / Facts / Assume / Hand forward), deliverable,
   hour estimate, week constraint, facts-packet group, check, and "good enough" criterion was compared
   for strength: imperatives stay imperatives, "only", "exactly", "at least", "never", and "not
   available" are kept, and nothing is added.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched; the `!!!
warning` body stays on its own indented lines. English was not edited.

Totals: 11 editor doubts, 7 term proposals, and the translator's notes checked; three doubts (ch 59
no. 3; ch 60 nos. 1 and 3) led to a change, and the ch 60 term proposal for Victor's remark was
applied. Further fixes from the full read: ch 59 ×3, ch 60 ×2.
Validation: `tools/validate_book.py` passed.

## Chapter 59

| # | Doubt | Verdict |
|---|---|---|
| 1 | «Пункты без нагрузки либо появились раньше (чек-лист)» for "older" | ok. The checklist's origin in the table is "Before arrival", so "older" means it predates year 1; «появились раньше» says that. |
| 2 | «директорами: по Developer Platform (…) и по Infrastructure (…)» | ok. "runs two directors: Developer Platform (5 managers, 38 engineers) and Infrastructure (…)" names each director's area. |
| 3 | «По решению CTO бюджет организации…» | **Clarified.** "The CTO cut its budget" refers to the platform organization (the previous sentence's subject), not Halvard. Now «бюджет платформенной организации», so the reader cannot take it as the whole company. |
| 4 | «стейкхолдер утратил доверие» | ok. The English does not say in whom ("a stakeholder lost trust after a failure"); the Russian is equally open. |
| 5 | «у каждого нового процесса была цена и был предусмотрен выход» for "each addition carry its own exit and its own price" | ok. "Addition" is any added process, and "exit" is the sunset described in the next bullet. |
| term | оснастить измерениями; несущее нагрузку / несущее историю; «находки» for rehearsal findings vs audit «замечания» | ok, keep. The Halvard vulnerability "findings" are «замечания» and match halvard.ru; the Northstar rehearsal "findings" are not an audit. |
| t24 | Term list (постоянные притязания, несёт нагрузку / историю, проверка на нагрузку, скрытая нагрузка, управленческие ступени, контрольный сигнал, условие восстановления, приостановить, the six verdicts, срок действия (sunset), бюджет и потолок процессов, ресурс — не деньги, эффект текущего года / годовой темп, урезание всем поровну, перекладывание затрат, поддерживающая / принудительная формализация, комитет по изменениям, пакет соответствия, failure-mode names) | ok; consistent through the chapter. |
| t24 | «с 32% до 78%»; «до менее чем одного»; Halvard CTO ungendered except «CTO согласился»; «Вверх по лестнице контроля» | ok. The diagram label reads the ladder as Chapter 20's enforcement ladder, which the "Cheaper mechanism exists? yes" branch implies. |
| t24 | A3 «источник, с которого вы отказались бы начинать» | **Fixed** (see below). |

Further fixes:
- Halvard policies: "A proposed company-wide rule must first say which policy it serves" had become
  «…прежде всего называет политику» (descriptive). Now «…должен прежде всего назвать политику».
- F1: "Northstar's ten-item pull request checklist" had lost "Northstar's"; the chapter also has
  Halvard examples. Now «Чек-лист пул-реквеста Northstar из десяти пунктов».
- A3: "name the source you would refuse to use first" had become «источник, с которого вы отказались бы
  начинать», which implies the source is used later. The worked solution's "The source to refuse
  first" is cutting the prevention allocation, which is never to be used ("never prevention"). Now
  «назовите источник, от которого вы откажетесь прежде всего». See English problem 2.

Claims checked one by one: Goldratt and Cox ("known for", practitioner consensus, "not a research
finding"); Meadows (this book's reading, expert opinion); Adams et al. (research finding, eight
experiments, the red-tape explanation untested); Reinertsen (argues, no label); Adler and Borys (expert
opinion, conceptual, not an empirical test); Sutton and Rao ("known for", practitioner argument); DORA
(industry research, survey-based, correlational; "associated with worse delivery performance", "no
evidence that formal external review lowers change failure rates"; does not prove removal safe, shifts
the burden of proof); Project Oxygen (documented practice, one company, self-reported); Lee and
Edmondson (expert opinion, "little is known"); Harter (industry research, "suggests"); Larson (expert
opinion, six to eight and four to six, a range not a rule); the four growth practices and the decision
framework (this book's recommendation; thresholds are judgment). Worked example: 120 → 200 engineers;
11 forums, 4 approvals, 6 reports, 18 rules, about 9 FTE, 7.5 percent; ceiling 8 percent, 16 FTE; 1.5,
2.5 → 0.3, about 6 FTE; two duplicates in the first quarter; 13 FTE, 6.5 percent, 21 rules. Northstar
example: 80 engineers, 87 seats, $250,000; 12 and 8 FTE; 34/31/28/25 percent; 7.2 against 8.0 FTE,
$1.33M, $1.48M, $1.4M, 0.8 FTE short, $185,000; 1,900 → 450 deleted → about 600, 546/104/442 days, 1.9
engineer-years; seven QA engineers, fifth constraint; 52 standards, 21, 17, 14; 65 actions, 42; 32 → 78
percent by quarter 2; four CI systems 1.5 against 0.5, 1.0 FTE future; 128 engineer-days. Halvard: Gwen
Abernathy, 5/38 and 4/32, 10 percent, $18.0M → $16.2M, $1.8M in-year; 1.7 FTE, 3 days, 41 of 3,000, 6
clashes, 19 approved incidents; 0.4 FTE; 20 days and 840 hours; 13 hours, one meeting in three;
$205,800, $14.4M, $3.6M, 1,840 hours; the funding table, $486,800 short and $616,400 over; 4/2/1.5/0.5
FTE; 23 services, 46 engineer-weeks; 62 engineers, 9 → 8 managers, 7.8 → 6.9 → 7.75; the board
suspended for quarter 2, wait under 1 day, incidents 5 and 4 against 4.75, 9 clashes; findings 12 → 31,
the 20-minute review. Case: weeks 50 and 51; Samuel Osei, Rajiv Menon, $150,000, $4.2M, 22 percent; the
inventory rows (3 and 13 of 15; weeks 7, 10, 11; week 9 Sev1; week 39 lapse; 38 of 40, 11 falsely; 1.5
against 0.5); about 1 FTE not yet available; week 52. Exercises (F1 to X2, including A3's 5 percent,
$16.73M, 87 seats, $4.2M, about 8 leavers a year), reflection questions, takeaways, and references
match.

## Chapter 60

| # | Doubt | Verdict |
|---|---|---|
| 1 | Stage 7 «Допущение» and X1: «приняли вы предложение или отложили» for "whether you decided it or deferred it" | **Fixed** in both places. "It" is Victor's week-46 organization decision, and "decided" covers any choice among the proposal and alternatives B, C, D (the next clause asks for the envelope "under the alternatives"). «приняли предложение» narrowed it to accepting the week-44 proposal. Now «приняли вы это решение или отложили его». |
| 2 | F3: «два предложения, которые член совета директоров может понять неправильно» | ok. The worked solution gives exactly that: two sentences that a board member would misread ("Prevention falls from 12 FTE to 5.5"; "Prevention costs $254,375 a quarter") and why. |
| 3 | X1: «вопрос о VP, после решения которого инженеров останется 78» | **Fixed.** "the VP question that would leave 78" means 78 engineers if the VP seat is created (table: 79 → 78 "with a VP"); «после решения» suggested any answer leaves 78. Now «вопрос о VP (если создать это место, инженеров останется 78)». |
| 4 | Stage 1: «следуя плану дней 1–15 из главы 27» | ok. Chapter 27's playbook has a "Days 1–15: diagnose" phase. |
| 5 | Enterprise: «Записи с двумя последними статусами и есть замечания аудита» for "The last two are the findings" | ok. The hinge review is the "commitment audit" (stage heading; objective "audit it honestly"), so «замечания аудита» is within the English and separates the term from Victor's remark. |
| 6 | «на любую реальную организацию» for "without the fiction" | ok; same meaning. |
| "done" | «Работа готова, когда выполнены четыре условия: …» | ok. The English lists exactly four conjuncts (every stage meets its "good enough" criteria; a status for every register entry; the two-page memo written; all seven checks pass). Nothing is added or loosened; «критерий «Достаточно, если»» is the table column "Good enough when". |
| term | замечание (Victor's remark) → «реплика» | **Applied** in four places: the CTO Perspective («отменяет свою прежнюю реплику»), the case (×2: «отменой реплики Victor недели 14», «превратила бы реплику»), and the takeaway «реплики высшего руководства». «Замечание» now appears only as «замечания аудита». |
| term | уступки измору → «сокращения под давлением» | Not changed; maintainer decision. «урезают измором» (thread table) and «будут урезаться измором» (reflection 6) carry "by attrition" in the sense of gradual erosion; «сокращения под давлением» would drop the gradualness. |
| term | поворотная точка / поворотный разбор; «Достаточно, если» | ok, keep. |
| t24 | Term list (итоговый проект, этап / этап продолжения, stage names, поворотная точка, реестр обязательств, мост измерений, правила подсчёта, таблица доверия, правило непрерывности, пакет фактов, правило времени, нити, рамки ресурса, строка-амортизатор, правило снижения, the six statuses, the stage fields, что сдать / «Достаточно, если» / критерий завершения, записка об интеграции, failure-mode names, член совета от инвестора) | ok; consistent through the chapter. |
| t24 | «к этапу 3 продолжения» (example table) and «на каждый этап продолжения» (F3) | ok; the English "stage" there is the continuation's stage. See English problem 3. |
| t24 | F2 split into «Факты: …»; Victor's remark as direct speech; objective 4 adds «написать» | ok; no change in meaning. |

Further fixes:
- Trade-offs: "The measurement bridge buys both, at the price of reporting two numbers for a quarter"
  had become «цена этому — два числа в квартальном отчёте» (every quarterly report). Now «цена этому —
  квартал, за который приходится показывать два числа».
- Trade-offs: "write stages 1 to 6 thinly" had become «кое-как» ("sloppily"). Now «скупо».

Assignment terms checked one by one: about 75 to 100 hours, short path about 45 to 55, P3 core version
about 10 to 12 hours; the four-project table (P5 and P7 "Skip", P8 core version or three candidates);
the short path (stages 2 and 4 to ten entries, stage 9 to two pages, stage 8 to three candidates,
counting rules, hinge and memo at full depth); the seven-step working order with weeks 1 and 2, 3 to 5,
4, 4, 40, 47 and 48, to 49, to 50; the stage 6 draft at the end of week 2; the facts packet (four
groups, "except the baseline sections listed below", hinge facts open to the hinge and stages 7 to 10,
week 49 to stages 8 and 10 only, nothing from week 50 on); the five closed baseline entries; the
13-row hours / deliverable / "good enough" table; "Before you start" (director facts only; seven
register columns; assumptions labeled as yours with the value that would change the recommendation;
never a Northstar fact); every stage's Produce / Add / Facts / Assume / Hand forward, including stage
2's 24 components and "do not restructure teams here", stage 3's baseline with no targets and the two
unmeasurable rows, stage 4's 143-item list, 120 to 180 engineer-days and 1.5 FTE, stage 5's CTO lane and
Anders Holm, stage 6's funded intentions and step-down rule, the hinge's "at least one" reasonable-and-
bad and one lucky decision, stage 9's three or four policies and "not available", stage 7's envelope at
80/79/78 and the line at 77, stage 8's "exactly" and break-even, stage 10's "write nothing about the
meeting's outcome"; the assembly instructions (ten artifacts, the register, a two-page memo, one early
commitment chosen on what was knowable in week 4); the seven pass-or-fail checks. None is stricter or
looser than the English.

Claims checked: Rumelt (expert opinion); Repenning and Sterman (research finding, mostly outside
software); Staw ("known for", expert opinion); DORA metrics guide (industry research); Baron and Hershey
(research finding, students, medical decisions and gambles); the decision flow (this book's
recommendation); example and case (illustrative). Figures: 7/23 → 9/21, total 30; 2 of 9 (22 percent)
against 31 percent; 15 and 14; 90 and 91 days; 12 → 8 → 6 and 5 → 5.5 FTE; 34 percent of 80 = 27.2,
31, 22 planned and 25 actual (20 FTE), at most 18 percent, 22 percent of 79 = 17.4; $185,000 ÷ 4 =
$46,250; the seven-line envelope; 25 percent → 19.75 FTE, 2.35 over, horizon 2 10.0 → 7.65; 87 seats,
77 to 80, the four week-44 options; Helena Marsh week 46, Victor's week-47 draft, eight documents.
Case: 38 merge requests, 17 from Orders, none from Platform Operations; Priya Raman after week 26; week
39 lapse; week 44 proposal; week 46 decision unrecorded; ADR-0001 in week 14 by Li Na Zhou, the
three-option table, Elena Sokolova, week 19, 29 of 46 pipelines, seven of 11 loads, week 47 policy,
week 60. Exercises (F1 to X3, including F2's eight facts with their weeks, F3's 6 against 5.5 and
quarters 5 to 8, A2's Margaret Lin and four measures, X2's five board members and their concerns),
reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 60, Stage 1, "Produce"**: the wrapped line "  15. If you have done Project 3, reuse it." begins
   with a number and a period. Python-Markdown renders it as a new list item: the page reads "Chapter
   27's days 1 to" followed by a bullet "If you have done Project 3, reuse it.", losing "15". Rewrap so
   "15." does not start the line. (This is also why the ordered-item count is 17 in English and 16 in
   Russian.) The Russian is unaffected.
2. **Ch 59, A3**: "name the source you would refuse to use first" can be read as "the source you would
   not start with" or "first, name the source you would refuse to use". The solution means the source
   to refuse outright (the prevention allocation). "and name the source you would refuse to use at all"
   would remove the ambiguity.
3. **Ch 60, Example table and F3**: "at most 18% by stage 3" and "fixed per stage" refer to the
   continuation's stages, in a chapter whose own "stages" are the capstone's. "by the continuation's
   stage 3" would prevent misreading. The Russian adds «продолжения».
4. **Ch 60, Learning Objectives**: objective 4 ("Extend the director's work into a 12-month strategy…")
   has no verb for producing the documents; minor.
5. **Overlong source lines** (cosmetic): ch 59 F3, A1, A2, A3; ch 60 the mental-model blockquote, the
   capability-trap paragraph, the hinge section, A2, X1.

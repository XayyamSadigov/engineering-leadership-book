# Meaning check, batch 20: chapters 53 and 54

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 18:

1. Every doubt in `editing-ch53.md` and `editing-ch54.md` section 4, the term proposals (section 3), and
   the translator's notes (`notes-t21.md`) get a verdict.
2. Completeness: headings (27 each), table lines (53: 65; 54: 44), list items (53: 48; 54: 41), ordered
   items (53: 36; 54: 34), exercises (53: 9; 54: 9), Mermaid blocks (53: 3; 54: 2), admonitions (1 each),
   relative link targets (53: 54; 54: 71, identical in order) and citation link texts match the English.
   Every number in table lines is identical to the English (the one checker hit, "SOC 2," in the ER-06
   row, is a false positive). Wrapped lines that begin with a number and a period are all items of real
   ordered lists, as in the English. Table rows, exercises, reflection questions, takeaways, and
   reference lines were also checked by eye: nothing is missing.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar and Halvard names and numbers were checked against the English. In
   chapter 53 every regulatory and security statement (SOC 2, the SEC 2023 rules, NIST CSF 2.0, SSDF,
   SLSA, PCI DSS, NIST IR 8286, SP 800-30, Open FAIR) was checked for strength, hedges, and official
   names; in chapter 54 every study result and computed claim (figure, direction, unit).

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 9 editor doubts, 8 term proposals, and the translator's notes checked; 1 led to a change (ch 53
doubt 1). Further fixes from the full read: ch 53 ×3, ch 54 ×4.
Validation: `tools/validate_book.py` passed.

## Chapter 53

| # | Doubt | Verdict |
|---|---|---|
| 1 | «не запрещайте матрицы, но и не останавливайтесь на них» | **Fixed.** The English: "So stop at matrices less often rather than banning them." The edit made it "never stop at them", stronger than "less often". Now «Поэтому не запрещайте матрицы, а реже останавливайтесь на них.» |
| 2 | «Добавьте к ним проверку того, кто классифицирует находки (глава 18)» | ok. The English really says "Pair them with a check on whoever classifies the findings"; «кто» is faithful, not a slip. The English elsewhere says "audits the teams' classifications" and "classification audit"; see English problem 2. |
| 3 | «Но при любом подчинении в службе остаются два человека, и проблема ёмкости не решается» | ok. The English: "Neither placement fixes a two-person function's capacity." |
| 4 | «просит посвятить сессию на заседании комитета на неделе 50 технологическим рискам» | ok. The English: "asks … for a technology risk session at the committee's week 50 meeting". |
| term | «уязвимость системы» → «подверженность атакам» | Not changed: a term decision for the maintainer (notes-t7 rendering). Meaning is intact, but the collision with «уязвимость» (vulnerability) in the same sentences is real; "Report exposure" in the reporting section and the takeaway read slightly as "report vulnerabilities". |
| term | «уровень обзора» → «уровень обобщения» | Not changed; maintainer decision. The English "Altitude" is explained in the same item (business consequences above, causes below), so the meaning survives. |
| term | «принимающий», «подъём рисков наверх» | ok. |
| t21 | Term list (механизм контроля, принимающий риск, диапазон возможного ущерба, штабные учения, путь от инцидента к раскрытию, границы применения, ядро (Core), CPA, AICPA, SEC, etc.) | ok; consistent through the chapter. Official names stay in English: NIST Cybersecurity Framework, Secure Software Development Framework, SLSA, Supply-chain Levels for Software Artifacts, PCI Data Security Standard, Trust Services Criteria, Open FAIR, NIST IR 8286 Rev. 1, NIST SP 800-30 Rev. 1. |
| t21 | ER-03 "accepted meanwhile by exception" → «пока принят через исключение» | ok. |
| t21 | 22 scattered items = 9 + 6 + 4 + 2 + 1 | ok. |
| t21 | Joon Park's week 52 date | ok; the edit now reads «На неделе 44 Joon Park вписал в запись дату, неделю 52, но новой подписи не было», same facts. |
| t21 | «$45 000–70 000» versus first-quarter.ru «$45 000–$70 000» | Cosmetic; maintainer may unify. |
| t21 | ER-01 owner "Engineering Director" → «Директор по разработке» | ok. |

Further fixes:
- ER-06 table cell: "Missing assurance costs deals and renewals" was «Отсутствие гарантий стоит сделок и
  продлений», the «стоит» + genitive pattern the editor flagged in prose (reads "is worth deals"); the
  table was left byte-identical by the edit. Now «Из-за отсутствия гарантий компания теряет сделки и
  продления». No numbers in the cell.
- Example: "Victor's own 2 hours a week on security reviews" had become «на вопросы безопасности». Now «на
  проверки безопасности», matching chapter 50's «Проверки безопасности от клиентов».
- Case: "The cash would compete with the $150,000 of tooling in the continuation …, which Rajiv wants
  offset inside the $4.2M cloud and tooling budget" had become «а Rajiv хочет, чтобы эти расходы
  компенсировались…», where «эти расходы» could be read as the SOC 2 cash. Now «а эти $150 000 Rajiv хочет
  компенсировать внутри бюджета $4,2 млн…».

Regulatory and security claims, checked one by one: SOC 2 (an examination of controls relevant to the
five categories, performed by an independent CPA under the AICPA's Trust Services Criteria; a revision
proposed, "check its status"); the SEC 2023 rules (listed companies, material incidents, "generally"
within four business days of deciding materiality, the reasonable-investor definition, board oversight in
the annual report, private companies not bound); PCI DSS (baseline requirements for anyone who stores,
processes, or transmits cardholder data or could affect its security; scope first); NIST CSF 2.0 (six
functions, Govern at the center, profiles, Core not a checklist); SSDF (four groups); SLSA v1.2 (Build
and Source tracks; Build L2 as signed provenance generated by the build service); the privacy-law
disclaimer ("evidence here is thin"). Evidence labels: Quinn et al. (standard), the four treatments
(practitioner consensus), the three acceptance rules and the security-strategy form (this book's
recommendation), Cox (research finding), Open FAIR (standard), Hubbard and Seiersen (expert opinion),
Joint Task Force (standard), the three frameworks (standards), the breach-readiness and reporting rules
(this book's recommendation), vendor concentration (this book's recommendation). All keep their strength.

Full read: no other drift. The opening, related chapters (26, 30, 48 as plain text, 55), the three scales,
objectives, the mental model and both diagrams, the risk-appetite example (7 days, compensating control,
CTO signature; board or audit committee sets it), the obligations table, the breach paths, the four
reporting rules ($1.17M), the example (week 43; Rajiv Menon, Margaret Lin, Marta Kowalczyk, Joon Park; 12
risks, rating 12 = 3 × 4, four reviews; TR-01 to TR-09; the week-44 snapshot table; 476 hours, 0.26 FTE;
Greg Tanaka's $310,000 prospect, 12 months; the ER table with owners and scores; $1.17M, 72 percent,
$842,000, $240,000 to $380,000; $96,000 to $194,400; the three observations), the decision tables and the
three SOC 2 tests, four trade-offs, five failure modes (fields as in the English), the enterprise section,
the CTO section (CISO), Halvard, the 12-step playbook, the case (three appetite lines; the auth-svc
exception; five target outcomes; $45,000 to $70,000, $30,000, 0.5 + 0.5 FTE, $185,000, $150,000 in $4.2M;
11 of 34; options A, B (week 78 gate), C; the reporting-line options; week 48; Helena Marsh), all exercises
(F1 to X3, including A1's weeks 51, 52, 65 and X3's 60 vendor engineers and over 200 items), reflection
questions, takeaways, and references (proposed 2027 revision) match.

## Chapter 54

| # | Doubt | Verdict |
|---|---|---|
| 1 | CTO perspective, «на основе письменной политики, а не опроса о том, что инженеры делают на практике» | ok. The English: "from a written policy, not a survey of what engineers happen to do". The Russian follows it; the tension the editor sees (the survey is also the honest baseline) is in the English. See English problem 3. |
| 2 | «Над таблицей стоят три правила» | ok. The English: "Three rules sit above the table"; the Russian keeps both readings (position and precedence), as the English does. |
| 3 | «план недосчитается двух инженеров в тот год, когда…» | ok. The English: "the plan loses two engineers' work in a year when six of the 40 largest customers renew"; "in a year when" is "in the year when", not "per year". |
| 4 | «CTO объясняет, что и где измеряла каждая цифра» | ok. The English: "The CTO says what each measured, where, and what the company would have to observe". |
| 5 | search-svc in week 54 versus the organization change in week 53 | ok. The canon (`first-quarter.md`, transition plan) says "reporting lines week 53, search-svc week 54"; no conflict. |
| term | ИИ-возможность → «ИИ-функция» / «применение ИИ» in prose | Not changed; maintainer decision. Meaning intact. |
| term | «волны смешаны с реорганизацией» | ok; the next clause explains it, as in the English. |
| term | «каким инструмент ощущается» | Not changed; maintainer decision. |
| term | «массовым товаром» (commodity) | ok. |
| t21 | Term list (фундамент данных, владелец смысла, прослеживаемость, каскады данных, зубчатая граница, оценочный набор, стоимость инференса, придержанные замены, etc.) | ok; consistent through the chapter. |
| t21 | "Finance's ledger close" → «закрытием ledger у финансов» | ok. |
| t21 | «год 2» in table cells, word forms in prose | ok. |
| t21 | RCT gloss before the table | ok, mirrors the English. |

Further fixes:
- Data foundations: "Most of what the test finds is worth fixing" had become «Почти всё…» ("almost
  all"), stronger than "most". Now «Большую часть того, что находит проверка, стоит исправить».
- Evidence section heading-paragraph: "Vendors are involved and the evidence ages fast" had become
  «Вендоры заинтересованы…», which imputes a motive the English does not state (it says vendor-employed
  authors and a vendor-run DORA). Now «Вендоры причастны к исследованиям, а данные быстро стареют».
- Case, proposal 2: "It compares team-level deployment frequency, lead time, … escaped defects, and a
  developer experience survey" had become «… пропущенные дефекты на уровне команд и опрос…», so
  "team-level" seemed to qualify only escaped defects. Now «На уровне команд сравниваются частота
  развёртываний, … пропущенные дефекты, а также опрос об опыте разработчиков».
- Key takeaway: "a slowdown in one close to a mature product company's" had lost "one" (a single study),
  so the slowdown read as a general finding. Now «и замедление в одном случае, близком к условиям зрелой
  продуктовой компании».

Studies and arithmetic, checked one by one: DORA 2025 (industry research); Sambasivan et al. (53
practitioners, 92 percent; qualitative research finding); Sculley et al., Storer and DeBellis; the
readiness table; Dell'Acqua et al. (preregistered, 758 consultants, 12.2 percent more tasks, 25.1 percent
faster inside the frontier, 19 percent less likely correct outside; research finding); the inference
example (4 × $0.01 = $0.04; 500,000 orders a month → $240,000 a year; illustrative); the EU AI Act
(Regulation (EU) 2024/1689, four risk levels, chatbot and generative-output duties, phase-in 2025 to 2028,
dates moved once; standard); NIST AI RMF (voluntary; Govern, Map, Measure, Manage); Perry et al. (earlier
model; research finding); Spracklen et al. (at least 5.2 and 21.7 percent, one large sample; research
finding); the evidence table (55.8; 26.08 with SE 10.3 and 4,867 developers; about 21 with a wide interval
and 96 engineers; 19 percent slower, forecast 24, believed 20, 16 developers and 246 tasks; 1.5 and 7.2
percent; DORA correlational industry research); the standard-error reading (roughly 6 to 46 percent);
METR as a small preprint; Ziegler et al. (research finding); Campbell. Example: 46 pipelines, 29 on read
replicas, 12 ledger tables, ADR-0001; 212 tables, 38 described; 11 of 91 nights, 7 from Core; 0.3 to 0.6
percent, two days; 14 tables; 400 corrections, 340 errors; the survey (63 of 80; 41, 29; 17, 6; 34 of 41);
the requests table; the cause table (130/85/70/35/20; 59 and 35 percent; 14 engineer-weeks); 35 percent,
28 of 80; +8.4, +7.3, −5.3 FTE; 1.4 million lines, 11 years; median 21 working hours; 23 percent; $370,000
at $185,000; $38,400 for 80 seats at $40. Case: weeks 53 to 58 and 59 to 64; $9,600; 3 engineer-weeks,
about $10,700; Li Na Zhou, Kwame Mensah, Joon Park, Rajiv Menon, Greg Tanaka, Amara Okafor, Farah Haddad
(«фактически архитектор данных», as in the cast page). Exercises (F2 55 percent; F3 83 percent; F4
120,000 tickets, 3 calls at $0.015, 2 minutes at $40 an hour, 60 percent; A1 about 30 analysts, 14
tables, six respondents; X2 four product groups, 25 percent, about 60 contract engineers), reflection
questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 53, Why This Matters and regulation list**: a short wrapped line ("reassurance.") and an overlong
   unwrapped line ("Material means …"); "### Reporting risk to non-specialists" follows the previous
   paragraph with no blank line. Cosmetic (as notes-t21 reports).
2. **Ch 53, "Reporting risk to non-specialists"**: "Pair them with a check on whoever classifies the
   findings" reads as checking the person, while the security-strategy paragraph says the security function
   "audits the teams' classifications" and the playbook and enterprise table say "classification audit".
   "A check on how findings are classified" would match the rest of the chapter.
3. **Ch 54, CTO Perspective**: "from a written policy, not a survey of what engineers happen to do" can be
   read as disparaging the survey, which the example and playbook use as the honest baseline. The intended
   point (answer from the governed policy, not from describing ungoverned practice) could be stated
   directly.
4. **Ch 54, case proposal 2**: "about 3 engineer-weeks of analysis, about $10,700" leaves open whether
   $10,700 is the analysis cost (3 × $3,558) or the total with licenses; the Russian keeps the same
   ambiguity.
5. **Ch 53, Learning Objectives versus Deep Explanation**: SSDF is named in full in the objectives and as
   "the SSDF" later; harmless (notes-t21).

# Meaning check, batch 18: chapters 51 and 52

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 17:

1. Every doubt in `editing-ch51.md` and `editing-ch52.md` section 4, the term proposal for "write down"
   (`editing-ch52.md` section 3), and the translator's notes (`notes-t20.md`) gets a verdict.
2. Completeness: headings (51: 27; 52: 25), table lines (51: 62; 52: 108), list items (51: 55; 52: 52),
   ordered items (51: 37; 52: 22), exercises (8 each), Mermaid blocks (3 each), admonitions (51: 1;
   52: 3, including the collapsible `??? note`, whose body stays indented under its title line), and
   relative link targets (51: 68; 52: 56, identical in order) match the English. Every number in table
   lines is identical to the English. Wrapped lines that begin with a number and a period are all items of
   real ordered lists, as in the English. Table rows, exercises, reflection questions, takeaways, and
   reference lines were also checked by eye: nothing is missing.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar and Halvard names and numbers were checked against the English. In
   chapter 52 every accounting statement (capitalization criteria, amortization, impairment, deferred
   revenue, working capital, free cash flow, EBITDA) and every computed claim (figure, direction, unit)
   was checked.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 11 editor doubts, the "write down" proposal, and the translator's notes checked; 1 led to a change
(the "write down" term). Further fixes from the full read: ch 51 ×1, ch 52 ×3.
Validation: `tools/validate_book.py` passed (see the end of this file).

## Chapter 51

| # | Doubt | Verdict |
|---|---|---|
| 1 | Opening, «как инженерной организации строить системы» | ok. The English: "decides how the engineering organization builds"; the added object is harmless. |
| 2 | Halvard, «уже отдала распределение ресурса оргструктуре» | ok. The English is present perfect, not conditional: "has let the org chart do the allocating". |
| 3 | «те самые компромиссы, о которых пишет Porter» | ok. The English: "The four bins force Porter's trade-offs." |
| 4 | «За платформой остаются 4,5 FTE, как в квартале 3» | ok. The English: "Platform keeps quarter 3's 4.5 FTE." |
| 5 | Case, «70 из 340 проверенных ошибок» | ok. The English: "70 of the 340 errors sampled were duplicate submissions". |
| t20 | Term list (выборы бизнеса, четыре группы, опцион / проба / точка решения / критерий закрытия, дивиденд надёжности, актуальность ландшафта, рамки ресурса, «Сначала сократить, потом добавлять», etc.) | ok; consistent through the chapter. «Сначала сократить…» versus first-quarter.ru «сначала сближать…» stays a maintainer decision, not a meaning issue. |
| t20 | "Early sign:" → «Как заметить:» | ok; follows notes-t16. |
| t20 | A2 "Decision due week 46" in a week-47 exercise | ok, translated as written (the decision is overdue). |
| t20 | "year 2/3" as word forms in prose, «Год 2» in tables | ok. |

Further fixes:
- Example, "fall by 7.3 FTE (22.9 to 15.6), which goes mostly to horizons 2 and 3" had become «почти всё
  высвободившееся уходит в горизонты 2 и 3» ("almost all"), stronger than "mostly". Now «высвободившийся
  ресурс уходит в основном в горизонты 2 и 3».

Full read: no other drift. The opening (director's technical versus CTO's technology strategy; weeks 46 to
49, week 50 board), related chapters (30, 45, 49), the three scales, objectives, the mental model and its
table, Lafley and Martin and Rumelt (expert opinion), Porter (expert opinion), the four-step derivation
and the four bins, McKinley (expert opinion), Gerow, Chan and Reich, Tallon and Pinsonneault (correlational
research findings; this book's recommendation), Mintzberg and Waters, the horizons table and Blank (expert
opinion), the option fields, Phaal, the decision diagram and its rules (this book's recommendation), the
seven coherence tests (Klein, expert opinion; Flyvbjerg), the example (79 engineers, $185,000, weeks 53 to
208, prevention 5.5 FTE from 6/6/5/5, the allocation table, 7.3 FTE, 19.8 FTE and 2.4 more, horizon 2 to
7.6 FTE, 2.5 percent, $1.85M, $370,000, $150,000, Rajiv Menon), the decision diagram and table (10
FTE-quarters, about 3 percent), five trade-offs, six failure modes, the enterprise section, the CTO
section (Larson 2024; Kane et al., expert opinion), the board version (six items; the roadmap table),
Halvard (500 engineers, four groups, 70-engineer platform; Bardolet et al., research finding), the
11-step playbook, the case (six of 40 customers, $7.0M ARR, quarters 5 to 8; Helena Marsh; the bins
table; four policies; Elena Sokolova, week 14; ADR-0001 by week 60; the option table, $3,558 per
engineer-week; gates at weeks 56, 78, 104; Kwame Mensah, Li Na Zhou, Ines Carvalho; the stress rule and
people line by week 104; Amara Okafor, 1.1 percent; Greg Tanaka; $150,000), all exercises (F2 120 to 180
engineer-days; F3 22 and 15 percent; A2 79/80/78/77, 87 seats, $100,000; X2 31 and 9 percent), reflection
questions, takeaways, and references match.

## Chapter 52

| # | Doubt | Verdict |
|---|---|---|
| 1 | Opening, «часто хуже других руководителей понимает» for "the executive least practiced at reading" | ok. "Least practiced of all executives" and «хуже других руководителей» carry the same comparison; the hedge "often" is kept. |
| 2 | TR-01, «на одну мажорную версию отстал от версий с бесплатной поддержкой сообщества» | ok. The English: "a major version past free community support"; same fact (out of free support by one major version). |
| 3 | «Владеть бюджетом разработки, как ожидается, должен CTO» | ok. The English: "The engineering budget is the part a CTO is expected to own" (the part of Larson's annual plan). |
| 4 | A2, «а интеграция — нет» | ok. The English: "the integrations are not", the integration work of the buy and hybrid options (80 and 70 engineer-days). |
| 5 | Enterprise, transition cost split into two sentences | ok. The English: "The transition costs a quarter, and engineers' goodwill if time tracking arrives without its purpose"; the goodwill cost stays conditional. |
| 6 | Mental model, «стоит ли инвестиция того ресурса, который на неё уйдёт» | ok. The English: "whether an investment is worth its capacity". |
| term | "written down" → «списать стоимость вниз» (editor proposes «снизить балансовую стоимость») | Fixed. The English: "the asset is impaired, which means written down". Now «то есть снижают его балансовую стоимость», the standard Russian accounting term. This was the only occurrence in the Russian pages; notes-t20's term line should be read with the new rendering. |
| t20 | Accounting terms (себестоимость выручки, валовая / операционная / чистая прибыль, R&D, G&A, отложенная выручка, дебиторская задолженность, кредиторская задолженность и начисленные расходы, начисленные вознаграждения, основные средства нетто, собственный капитал, амортизация НМА / ОС, оборотный капитал, свободный денежный поток, обесценение, списание, сопровождение) | ok; standard Russian terms, used consistently. The terms box explains that Russian has one word for amortization and depreciation; the EBITDA gloss «прибыль до вычета процентов, налогов и амортизации» follows from it. |
| t20 | "Signal:" / "Detect:" → «Признак:» / «Как заметить:» | ok; follows notes-t12 and notes-t18. |
| t20 | Victor's note rounds $194,400 to "$194,000" | ok, kept as in the English. |
| t20 | Cost-of-revenue cell grouping versus first-quarter.md | ok; table copied verbatim, sums agree. |
| t20 | Related chapters 48 and 49 as plain text | ok; mirrors the English. |
| t20 | «повышение по результатам (merit increase)» versus first-quarter.ru «по заслугам» | Not changed: a term decision for the maintainer. |
| t20 | Mermaid label «Решающий параметр» for "Decisive input, break-even" | ok; label shortened per glossary section 1, and the prose and playbook name the break-even. |

Further fixes:
- Why This Matters: "cannot tell when an accounting presentation makes an investment look cheaper than it
  is" had become «не заметит, что… инвестиция выглядит дешевле», which presupposes it always does. Now
  «не заметит, когда…».
- Case, decisive input: "a tier 1 framework with no upstream fixes" had become «без исправлений от
  разработчиков», which a reader could take as Northstar's own engineers. Now «без исправлений от его
  разработчиков» (the framework's maintainers).
- Reflection question 1: "who controls engineering's story" had become «кто рассказывает историю
  разработки» (who tells it), weaker than "controls". Now «в чьих руках история разработки».

Accounting and arithmetic, checked one by one: the cash-versus-booking mental model; the path table
(nothing until in service, then amortization over three years; investing outflow; operating cash flow
looks higher); the income-statement line table; ARR versus revenue; deferred revenue as a liability and
cash stopping before revenue; operating, investing, financing; non-cash add-backs; free cash flow as
operating cash flow minus capital spending including capitalized software; the three FASB questions
(standard, in the book's words) and the capitalizable / expensed table; internal-use rules for SaaS; the
2025 update replacing the stages; impairment, the zero-value presumption, write-off; IAS 38; Aboody and
Lev (old, correlational research finding); Larson 2023b (expert opinion); the four effects (EBITDA up by
the full capitalized amount; operating income up only while capitalization grows); Franklin et al.
(practitioner consensus); Larson 2023a (expert opinion); the two views; budget, forecast, target (this
book's recommendation); fixed, variable, committed, discretionary, seats and dollars; the variance table
(26 engineer-weeks); Flyvbjerg (this book's recommendation for the transfer), Kahneman et al.; the
scenario table; booking and decisive input. Example: the income statement (145.0, 40.6, 104.4, 72
percent, 16.4, 46.0, 21.0, 21.0 and 14.5 percent, 23.9, 16.8 after 1.4 interest income and 25 percent
tax), the $20.3M table (13.7, 2.4 at about 15.3 FTE-years and $157,250, 3.1, 1.1), 85 percent of
$185,000, $2.1M amortization, the credits ($410,000 → $1.64M a year; $60,000 → $240,000; about $1.4M, 6.7
percent), deferred revenue $55M and 39 percent, free cash flow $17.5M against $20.7M, the full balance
sheet and cash-flow tables (equity up 16.8, exactly net income), the capitalization test ($1.8M, $2.1M,
$2.4M, $2.4M; −0.3, −2.4, −2.4, none; EBITDA 10 percent), Calder Ridge Partners (two seats), Victor's
three points ($185,000 against $27,750). Decision table, the Northstar policy and its diagram, the
work-item table, the two safeguards, five trade-offs, seven failure modes, the enterprise section, the CTO
section, the 10-step playbook, Project 8, the case (TR-01 since quarter 2; 120 to 180 engineer-days; $800
a day, about 230 days, $3,558; the envelope table 16.73, −0.43, 16.31, 4.2; $16.10M + 3 percent $0.483M +
$0.15M; $150,000 inside $4.2M; 15 to 35 percent; the scenario table; 24, 38, about 49 engineer-weeks;
$96,000 to $194,400 expensed in FY2; $60,000 a year, new money; 7 days; $61,100 a year from $152,000 ÷
2.487; 1 in 10 of $611,000; Joon Park, Ines Carvalho, Amara Okafor; 40 engineer-days; about 38
engineer-weeks), all exercises (F1 20.7 and 16.8; F2 140 tests, six engineer-weeks, two hypothetical
items; F3; A1 $150,000 in $4.2M; A2 120/80/70 engineer-days, $150,000 and $45,000, 0.5/0.15/0.25 FTE; A3 2
of 6 in quarters 5 and 6; X1; X2 $102.9M, 18 to 28 percent), reflection questions, takeaways, and
references (ASU 2025-06, ASC 350-40 and 985-20, paragraphs 350-40-25-12A and 350-40-35-3, BC13, periods
after December 15, 2027) match.

## Possible problems in the English (not edited)

1. **Ch 51 lines 23, 250, 369; ch 52 lines 124, 151, 406, 533, 677**: overlong unwrapped source lines;
   cosmetic (as notes-t20 reports).
2. **Ch 52, income-statement table, EBITDA row**: "Adds back amortization, so capitalization raises it"
   omits depreciation, although the EBITDA cell below adds back both (2.1 + 0.8). Accurate for the point
   made (capitalization), but slightly incomplete as a definition.
3. **Ch 52, cash-flow table**: "Also free cash flow, since there is no financing" ties free cash flow to
   the absence of financing; free cash flow is 20.7 − 2.4 − 0.8 = 17.5 regardless, and only its equality
   with the change in cash depends on zero financing. A reader may misread the reason.
4. **Ch 52, "When a project stalls"**: "The standard presumes uncompleted software is worth zero" states
   the presumption without its trigger (it applies once completion is no longer probable). The paragraph's
   opening supplies the context, so the risk is small.
5. **Ch 52, Related chapters**: 48 and 49 are plain numbers while 45 is a link; the Russian mirrors it.
6. **Ch 51, A2**: "Decision due week 46" in a week-47 exercise; consistent with "none decided", but a
   reader may take it for a typo.

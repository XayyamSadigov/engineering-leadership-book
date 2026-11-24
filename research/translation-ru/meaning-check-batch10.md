# Meaning check, batch 10: chapters 33 and 34

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 and 9:

1. Every doubt in `editing-ch33.md` and `editing-ch34.md` section 4 and in the translator's notes
   (`notes-t11.md`) gets a verdict.
2. Completeness: headings (33: 26; 34: 24), table lines (33: 63; 34: 59), exercises (8 each), Mermaid
   blocks (3 each), admonitions (1 each), and relative link targets (34 each, identical in order) match the
   English. List items match in ch 33. In ch 34 the Russian counted one extra "list item": a wrapped
   paragraph line began with «86. По строке…», which Markdown can read as an ordered list starting at 86.
   Fixed (see below). Paragraphs, table rows, exercises, reflection questions, takeaways, and reference
   lines were also checked by eye: nothing is missing. Both "Northstar so far" admonitions keep their body
   indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English: openings, mental
   models and diagrams, research passages, the Northstar examples and cases, all tables, exercises,
   reflection questions, takeaways, and reference lines. Evidence labels were checked one by one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 10 editor doubts plus the translator's notes checked; 1 editor doubt changed (ch 33 no. 3).
Further fixes from the full read: ch 33 ×1, ch 34 ×4 (one of them a rendering hazard).
Validation: `tools/validate_book.py` passed.

## Chapter 33

| # | Doubt | Verdict |
|---|---|---|
| 1 | Kwame Mensah's role not given at first mention | ok for the translation: the English gives no role either ("Kwame Mensah's release working group"), so adding one would put a fact on the Russian page that the English lacks. English problem 1. |
| 2 | «договорённостей, основанных на отношениях» for "relational contracts" | ok. It renders the economic sense (agreements sustained by the relationship) without adding "long-term"; «неформальных долгосрочных» would add a claim. Kept. |
| 3 | Failure mode, «На исходном уровне Northstar…» | fixed: → «В базовом квартале Northstar…». "At Northstar's baseline" refers to the baseline-quarter figures (46 percent, 29 of 86), as elsewhere in the chapter. |
| 4 | Case, option B: «одного решения мало, нужно согласие этой команды» | ok. "B needs that team's agreement, not only a decision": the decision is the director's. |
| 5 | Takeaway «хотя реальные исключения есть» | ok. The English says "with real exceptions". |
| t11 | "for reporting convenience" → «ради удобства схемы подчинения» | ok; reporting lines is the plausible reading. |
| t11 | "emphasizes keeping teams together" → «настаивает на том, чтобы команды не разбивали» | ok; "emphasizes" is slightly softer than «настаивает», but the contrast with Conway is preserved. |
| t11 | Learning objective "say which kind of load" → «называть» | ok. |
| t11 | germane → «учебная» | ok; the English glosses it as "spent on learning". |
| editor 3 | «участие команды содействия» as countable form (A3) | no change needed for meaning; «одну или несколько работ команды содействия» matches "one or more enabling engagements". Term choice for the maintainer. |

Further fix:
- Learning objectives: "state how strong the evidence for each direction is" had become «оценивать,
  насколько сильны», which turns a statement into an assessment and duplicates the next verb's sense.
  Now «называть, насколько сильны».

Full read: no other drift. The opening and its four cross-references, the three scales, the mental model
and loop diagram, Conway (expert opinion), MacCormack et al. (research finding, forward direction), Colfer
and Baldwin (142 studies, partial mirroring, breaking the mirror, open projects not supporting), Cataldo et
al. (research finding from one study), Herbsleb and Mockus (two and a half times; the inference to one
site), the reverse Conway maneuver and this book's recommendation, both team-type tables, the five "thin"
bullets (practitioner consensus), Sweller (research finding about individual learners), Team Topologies on
load (expert opinion), the "label the transfer" passage, the load table, team size (28 and 120 pairs,
Dunbar not used, five to nine engineers as this book's recommendation), the Northstar example (16 people,
seven components across six domains, the knowledge-map table, the capacity table, 2.6 engineers, Ines
Carvalho), the decision diagram and table, five trade-offs, six failure modes, enterprise practices (38
merge requests on core/permissions), the CTO section, the playbook, the case (Tom Becker, team-type table,
INC-412, 29 of 86, 46 percent, 20 to 14 percent by week 18, the option table, Victor Lindqvist, Rafael
Duarte), all exercises, reflection questions, takeaways, and references match.

## Chapter 34

| # | Doubt | Verdict |
|---|---|---|
| 1 | «ни один из шести охватов не попадает в диапазон» | ok. "every one of the six spans is outside the range". |
| 2 | M2: «каждый ниже порога в одну неделю» | ok. "below the one-week threshold, about 58 merge requests… changed both": the merge requests are each too small to be a link; the point is that the link count misses them. |
| 3 | «новые руководители остаются без присмотра» | ok. The English says "leaves new managers unsupervised". |
| 4 | Case table M3 «−4 связи» vs example table 6 removed, 2 created | ok as a translation (numbers verbatim). Net vs gross in the English; English problem 2. |
| 5 | «разбирали только на уровне выше обоих руководителей» | ok. "has only ever been handled above both managers". |
| t11 | Graicunas "writing in the 1930s" → «в 1930-х годах» | ok. |
| t11 | F1 parenthesis lists table facts, not the five factors | ok as translated; English problem 3. |
| t11 | Rajiv Menon glossed «CFO, финансовый директор» | ok. |

Further fixes:
- Example, "Where the links are": a re-wrapped line began «86. По строке видно…». A line starting with a
  number and a period can render as an ordered list item. Re-wrapped so the number stays on the line above,
  glued with a no-break space («таких связей⍽86.»).
- Trade-offs, stability against fit: "can beat a better one changed twice a year" had become «лучше
  правильной», which claims the other boundary is right, not merely better. Now «лучше более удачной».
- Case option table, M1 status: "Not pursued" had become «Отклонено», the same word as M3's "Rejected";
  the English distinguishes the two. Now «Не взят в работу: ухудшает…».
- Reflection question 1: "what stopped happening at that size that you only noticed later?" presupposes
  the late noticing; the Russian had turned it into a yes/no question («и заметили ли вы это только
  потом?»). Now «Что при таком размере перестало происходить, а вы заметили это только потом?».

Full read: no other drift. The opening (span, layers, dependencies), the three scales (11 versus 41 days,
seats under flat headcount), the mental model and diagram, Graicunas (history, not evidence), Rajan and Wulf
(research finding about the top of large firms), Gallup/Harter (industry research: self-reported,
correlational, all occupations), Larson (expert opinion), the eight-to-ten default and the five-factor
table (this book's recommendation), the twelve and five limits, the latency table (illustrative; 2.5, 1,
3.5, about 7), Williamson (expert opinion, economic theory; disputed), the 80/64/51 illustration, the
boundary research (Conway, Cataldo, Sosa et al. as research finding), the three design steps, the
Northstar example (span table, 77 plus 3, nine direct reports, about eight managers, $370,000 and $185,000,
the matrix and link-classification tables, 15 and 23 links, the candidate-move table and verdicts, the
week 9 Sev1, the contract alternative), the decision diagram and layer table, five trade-offs, four
failure modes, enterprise practices, the CTO section, the nine-step playbook, the case (situation,
INC-427, weeks 19 and 26, the option set, 27 and 48 links, the layer option table, week 44), all exercises
(Priya Raman, Marcus Oyelaran, Victor Lindqvist, Rajiv Menon, Helena Marsh), reflection questions,
takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 33, Case**: Kwame Mensah appears with no role ("Kwame Mensah's release working group"). CLAUDE.md
   section 7 asks for each person's role at first mention. Suggest "Kwame Mensah (staff engineer,
   infrastructure and reliability)", per the cast page; the Russian should then gain «(staff-инженер,
   инфраструктура и надёжность)».
2. **Ch 34, Case option table**: M3 shows "−4 links" (net: 6 removed, 2 created) while M1 "−4" is gross
   (0 counted created). Suggest "net −4 links" for M3, or "−6 / +2".
3. **Ch 34, F1**: the parenthesis "(first year as manager, sites, informal leads, hands-on work, recent
   changes)" lists facts from the span table, not the five span factors, and can read as if it named
   the factors. Suggest "using the facts in the span table (…)".

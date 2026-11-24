# Meaning check, batch 9: chapters 31 and 32

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batch 8:

1. Every doubt in `editing-ch31.md` and `editing-ch32.md` section 4 and in the translator's notes
   (`notes-t10.md`) gets a verdict.
2. Completeness: a script split both files into H1/H2/H3 sections and counted paragraphs, list items,
   table rows, admonitions, blockquotes, code blocks, and exercises per section. All anchors match the
   English headings in order (31: 29 sections; 32: 27). Table rows, list items, admonitions, Mermaid
   blocks, and exercises match in every section. The only count differences (ch 31 references; ch 32
   learning objectives, example, takeaways, references) are line-wrap artifacts of list continuations,
   checked by eye: no paragraph, list item, table row, exercise, or reference line is missing. Both
   "Northstar so far" admonitions keep their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English: openings, mental
   models and diagrams, research passages, the Northstar examples and cases, all tables, exercises,
   reflection questions, takeaways, and reference lines. Evidence labels were checked one by one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 9 editor doubts plus the translator's notes checked; 4 editor doubts changed (ch 31 no. 1 and
no. 3; ch 32 no. 1 and no. 3). Further fixes from the full read: ch 31 ×1, ch 32 ×2.
Validation: `tools/validate_book.py` passed.

## Chapter 31

| # | Doubt | Verdict |
|---|---|---|
| 1 | «инвентаризация Northstar это подтверждает» | fixed: → «инвентаризация Northstar их показывает». The English "Northstar's inventory shows them" exhibits the three routes; «подтверждает» turns an illustration into confirmation. |
| 2 | «любое изменение согласуют в одном разговоре» | ok. "one conversation settles any change". |
| 3 | «перенос шва становится отдельным проектом» | fixed: → «код так не устроен, и перестроить его под этот шов — отдельный проект». In "the code has not been shaped that way, and moving it is a project", the seam is proposed by the domain and stays; what has to move is the code. The English antecedent is loose (note 2). |
| 4 | Opening «три компонента со спорным владением или вовсе без владельца» | ok. The English says only "three components still disputed or orphaned"; the case table's "owner undecided" (core/permissions) is a sub-case the English opening also folds in. |
| t10 | "requests" for merge requests → «запросы» | ok; follows the English. |
| t10 | "made none of the 38" → «не внесла ни одного из 38 изменений» | ok. |
| t10 | Exemption gloss «записанное и ограниченное по сроку разрешение отступить от правил» | ok, matches "a recorded, time-limited waiver". |
| t10 | Comma splice joined with «и оба шага выполняются внутри монолита» | ok (note 3). |

Further fix:
- CTO perspective: "A CTO should be able to say at any time how many components lack a clear owner" had
  become «должен в любой момент знать», which drops the reporting duty ("say"). Now «должен в любой
  момент суметь назвать».

Full read: no other drift. The four bundled boundaries, the five-step strength ladder and its table,
Lewis and Fowler ("practitioner description, not evidence"), Fritzsch, Taibi, Lenarduzzi and Wang
(research findings in narrow, self-reporting samples), Fowler's Monolith First (expert opinion, labeled by
its author), Kolny (documented practice, self-reported, one service), the "under about 100 engineers"
recommendation, Gall and Zimmermann (signal, not a threshold), coupling share and its three blind spots,
Conway and Skelton and Pais, the four-case table, bounded contexts and the workshop, ownership without
orphans and the three routes, the five-step database split and the worked sample, the Northstar co-change
tables (numbers verbatim), the four readings, both decision tables and the decision diagram, the five
trade-offs, the six failure modes, the registry, rules and loop, the $185,000 and $18,500 figures, the
ten-step playbook, the case (three gaps, Priya Raman, Tom Becker, Ines Carvalho's proposal table, Rafael
Duarte, Marcus Oyelaran, weeks 19 and 26), all exercises, reflection questions, takeaways, and references
match.

## Chapter 32

| # | Doubt | Verdict |
|---|---|---|
| 1 | «проверяют так же, как внутреннюю разработку» | fixed: → «проходит ту же проверку, что и внутренняя разработка, или не проходит её». The English "passes the same test as internal work, or fails it" stresses that buying can fail the test too. |
| 2 | «платформа как явно самый дешёвый способ этого результата добиться» | ok. "a platform that is plainly the cheaper way to comply", where "comply" means meeting the mandated outcome. |
| 3 | «стоит в списке, чтобы платформа не записала его себе в заслугу» | fixed: → «чтобы платформа не считала его своим». "Review wait belongs to the product teams…; listing it stops the platform claiming it" follows "belongs to" and the table's Owner column, so it is about claiming the loop, which includes the credit; «в заслугу» narrowed it to credit only (note 5). |
| 4 | «платформы строят как раз организации, у которых уже есть проблемы» | ok. "troubled organizations being the ones that build platforms". |
| 5 | Payback gloss «то есть за два года экономия возвращает затраты» | ok, keep. The English glosses itself: "a two-year payback, meaning the saving takes two years to repay the cost". |
| t10 | Failure modes rendered «Как заметить:» only | ok; the English gives "Detect it by…" and no countermeasure (note 4). |
| t10 | "Northstar's record" → «хроника Northstar» | ok; term base. |
| t10 | "1 to 2 per product team" → «от 1 до 2» | ok; table numbers verbatim. |
| t10 | pp. 49–54 in prose vs pp. 47–55 in references | ok, both kept (note 6). |
| t10 | «отраслевое исследование в изложении DORA», «Согласно аннотации» | ok as translations; the access notes are in the English (note 1). |

Further fixes:
- Two ideas for honest modernization: "automated checks that guard an architectural property on every
  build (the fitness functions…) act as a ratchet" had been split into a sentence with no predicate
  («Вторая: автоматические проверки, которые… (фитнес-функции…).») followed by «Они работают как
  храповик». Rejoined: «…([Ford et al., 2017](…)), работают как храповик: старая форма не отрастает
  обратно.»
- Case, closing: "whether to approve the roadmap and target as drafted" had become «утверждать ли…
  в виде черновика», which reads as approving a draft rather than approving it unchanged. Now «в том виде,
  в каком их предлагает черновик».

Full read: no other drift. The opening and its ownership map, the 74-minute and six-day loops, the
monopoly-supplier argument, Core's 1.4 million lines and constraint 3, the mental model and product cycle
diagram, Bottcher (expert opinion), CNCF (practitioner consensus), Team Topologies, the product-run versus
queue table, the DORA 2024 table (industry research, cross-sectional, self-reported; numbers verbatim) and
its three hypotheses, the golden cage, the DevEx framework and the four-step selection rule (this book's
recommendation), the 2025 capability note, the adoption-gaming table, Fowler's strangler fig (expert
opinion), Spolsky (expert opinion from a handful of cases), Khadka et al. (research finding, abstract
level) and the "no controlled evidence" admission, the five-step slice, the modernization diagram and
rewrite conditions, the loop table and readings, the 17 deployable units and build systems per team, the
run-cost arithmetic ($185,000, $370,000, two-year payback), both decision tables, the five trade-offs, the
seven failure modes, the enterprise section, sizing and the funding table, the CTO section, the playbook,
the case (Tom Becker, Kwame Mensah, Bram Verhoeven, 39/29/26 engineer-weeks, 92 and 80 engineer-weeks,
weeks 19 and 26, the revised adoption table, Ines Carvalho's Core page, 38 merge requests), all exercises
(the $180,000 portal and $250,000 budget, Helena Marsh as CEO), reflection questions, takeaways, and
references match.

## Possible problems in the English (not edited)

1. **Access notes in reader text.** Ch 32: "industry research, as DORA summarizes it" and, for Khadka,
   "the abstract reports". CLAUDE.md section 7 asks for access limits to be folded into the evidence
   label. Suggest dropping the phrases; the Russian follows the English and should be re-synced.
2. **Ch 31, Drawing boundaries from the business domain**: "the code has not been shaped that way, and
   moving it is a project" has a loose antecedent ("it" = the boundary or the code). Suggest "and
   reshaping the code to fit it is a project".
3. **Ch 31, Decision Framework**, last sentence: comma splice ("…'settle ownership first,' both work
   inside the monolith"). Suggest a semicolon or "and both".
4. **Ch 32, Failure Modes** give only "Detect it by…" with no countermeasure, unlike ch 31 and the
   book's usual Signal/Countermeasure pattern. Not wrong, but inconsistent.
5. **Ch 32, Example**: "listing it stops the platform claiming it" is ambiguous between claiming the loop
   and claiming credit. Suggest "listing it, with its owner, stops the platform claiming it or the credit
   for it".
6. **Ch 32**: DORA 2024 is cited as pp. 49–54 in prose and pp. 47–55 in references. Probably the cited
   span versus the whole chapter; a reader may take it as an inconsistency. Consider "Platform chapter
   (pp. 47–55)" in references and leaving the prose as is, or aligning both.

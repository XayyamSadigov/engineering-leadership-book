# Meaning check, batch 5: chapters 21 and 22

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batch 4:

1. Every doubt in `editing-ch21.md` and `editing-ch22.md` section 4 and in the translator's notes
   (`notes-t5.md`) gets a verdict.
2. Completeness: a script split both files into H1/H2/H3 sections and counted paragraphs, list items,
   table rows, admonitions, blockquotes, and code blocks per section. All counts and anchors match
   (21: 25 sections; 22: 29).
3. Meaning: every paragraph of both chapters was read side by side with the English. That covered the
   mental model, the research passages, the Northstar examples and cases, all exercises, reflection
   questions, takeaways, and reference lines. Evidence labels were checked one by one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 14 doubts checked, 1 changed (ch 21 no. 6). Further fixes from the full read: ch 21 ×1, ch 22 ×2
(one structural). Validation: `tools/validate_book.py` passed.

## Chapter 21

| # | Doubt | Verdict |
|---|---|---|
| 1 | Four options "cheapest effective first", list starts with "remove" | ok. The English reads "Every entry has four options, cheapest effective first: **remove** … **reduce** … **contain** … **accept**". The list is not in cost order, so "cheapest effective first" can only mean the preference rule, which the Key Takeaways confirm ("try the cheapest effective option first"). «предпочтение отдают самому дешёвому из действенных» renders that meaning and matches the takeaway. The English wording is the problem (see below). |
| 2 | "Interest has two parts", then "a third part" | ok. The English does the same; the Russian follows it (see below). |
| 3 | IEEE Software: "twenty years later" | ok. In the English "Twenty years later" goes with the special issue's abstract (2012, twenty years after 1992), not with the introduction of the metaphor. |
| 4 | "The director let it stand" → «Директор не стал ничего отменять» | ok |
| 5 | "only about 30 changes had touched it" | ok. 30 is the number of changes that touched core/customer. |
| 6 | "Northstar figures come from the baseline" → «Исходные данные Northstar взяты из…» | fixed: → «Данные о Northstar взяты из…». The English does not separate inputs from estimates, so «исходные» narrowed the claim (and echoed «исходного уровня» in the same line). |
| 7 | Kruchten reference "read at abstract level only" | ok as a translation. The access note is in the English reader text (see below). |
| t5 | "**research** about the literature" → «**исследование** литературы»; "research finding with a narrow base" → «научный результат с узкой базой» | ok. Strength unchanged. |

Further fixes:
- Case: "the migration checks (TD-004) of Li Na Zhou" had become «которые предложила Li Na Zhou». The
  English does not say she proposed them; the register template names her as the builder ("automated
  ordering and table-lock checks in the pipeline (Li Na Zhou, staff engineer)"). Now «за которые отвечала
  Li Na Zhou».

Full read: no other drift. Cunningham (metaphor, not evidence), Fowler (expert opinion), Li et al.
(research about the literature, a decade old), Ernst et al. (research finding about perception), Besker
et al. (narrow base, self-report), Tornhill and Borg (observational research finding, one tool's
measure), the "evidence is thin" paragraph, the WSJF attribution to SAFe, the assumptions and the priced
register, the three observations, the decision table, the trade-offs, the six failure modes, the 10 to 20
percent share (this book's recommendation), the CTO section, the playbook, the case, and all exercises
match. The table cell "None known" → «Неизвестен» is close enough (no trigger is known).

## Chapter 22

| # | Doubt | Verdict |
|---|---|---|
| 1 | "boundaries such as invoicing and the payments gateway" → «границы, например между выставлением счетов и платёжным шлюзом» | ok. The case and A1 treat invoicing to the payments gateway as one boundary with one contract, so the one-boundary reading is the likely intent. The English list is ambiguous (see below). |
| 2 | "Regression is the most automatable work in the organization" → «Регрессия — то, что в организации легче всего автоматизировать» | ok. The English compares with all work in the organization, not only manual testing. |
| 3 | Luo et al.: "201 commits fixing likely flaky tests" | ok. The Russian follows the English hedge placement (see below on the English). |
| 4 | "The mechanisms had moved" → «Но механизмы изменились» | ok. The English means the mechanisms (pipeline failures, red main, contracts, rehearsals, manual pass), as in the table above it, not "leading indicators". |
| 5 | Elena's condition: "on condition that Billing reviewed every expectation for meaning" | ok. Billing is the reviewer in the English. |
| 6 | "Every engineer watches how QA engineers are treated during automation" → «видит каждый инженер» | ok. An observation, not a duty. |
| 7 | "**expert opinion and documented practice**" → «**мнением экспертов и задокументированной практикой**» | ok. Both labels kept. |

Further fixes:
- **Structural**: the collapsible note "How the $53,000 is estimated" had its body re-wrapped onto the
  `??? note "…"` title line with no indentation. MkDocs would render an empty note followed by a loose
  paragraph. Body restored under the title with four-space indentation; text unchanged. (A scan of every
  `*.ru.md` in `docs/parts/` found no other admonition with this defect.)
- Pyramid: "argues for many fast unit tests" had become «Она требует много быстрых модульных тестов»
  (demands). Now «Она советует иметь много…», which keeps the advisory strength.

Full read: no other drift. Fowler, Dodds, Schaffer, and Google's 80/15/5 guideline; size versus scope and
hermeticity; Robinson's consumer-driven contracts; Memon et al. (industry research, one company,
association); Luo and Parry; Micco and Bender (documented practice, not benchmarks); Inozemtseva and
Holmes (research finding, generated suites); Just et al. (research finding, narrow population); Petrović
et al. (practicality, not defect reduction); exploratory testing (practitioner consensus); the migration
practices (this book's recommendation); load testing (practitioner consensus); the escape table, the
$53,000 note, the reallocation table; the decision table; the trade-offs and failure modes; the
enterprise, CTO, and playbook sections; the case with its day-90 table; and all exercises match.

## Possible problems in the English (not edited)

1. **Ch 21, Prioritizing debt against features**: "Every entry has four options, cheapest effective first:
   remove, reduce, contain, accept". The list then starts with the most expensive option, so the phrase
   reads as a sort order that the list does not follow. Suggest "Every entry has four options; choose the
   cheapest one that works:" or reorder the list (accept, contain, reduce, remove).
2. **Ch 21, Measuring interest**: "Interest has two parts, and a register should record both", then "A
   third part, option cost". Suggest "Interest has two main parts…" or announce three parts and say option
   cost is recorded against the feature.
3. **Ch 21, References, Kruchten et al.**: "read at abstract level only" is an access note in reader text,
   which CLAUDE.md section 7 asks to fold into the evidence label. Same in the prose: "the abstract of an
   IEEE Software special issue's introduction says…".
4. **Ch 22, Contracts at boundaries**: "boundaries such as invoicing and the payments gateway" reads as two
   boundaries. If one boundary is meant (as in the case), "boundaries such as the one between invoicing and
   the payments gateway" would be exact.
5. **Ch 22, Flaky tests, Luo et al.**: "201 commits fixing likely flaky tests". My recollection of the
   paper's abstract is "commits that likely fix flaky tests" (the hedge is on the fix, not on the tests).
   I did not fetch the abstract this session, so please confirm before changing it.
6. **Ch 22, Petrović citation**: the link text says 2022 and the bibliography entry has year 2022, but
   the id is `petrovic2021mutation` (already noted in `notes-t5.md`). Harmless for readers; the id could
   be renamed for consistency.

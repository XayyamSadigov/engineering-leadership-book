# Meaning check, batch 8: chapters 29 and 30

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batch 7:

1. Every doubt in `editing-ch29.md` and `editing-ch30.md` section 4 and in the translator's notes
   (`notes-t9.md`) gets a verdict.
2. Completeness: a script split both files into H1/H2/H3 sections and counted paragraphs, list items,
   table rows, admonitions, blockquotes, and code blocks per section. All anchors match the English
   headings in order (29: 28 sections; 30: 25). Every count is identical in every section except one
   planned difference: in ch 29 "What the evidence covers" the English first paragraph is split into two
   in Russian (shared leadership; truck factor), as the translator noted. No paragraph, list item, table
   row, exercise, or reference line is missing. Both "Northstar so far" admonitions keep their body
   indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English: mental models and
   diagrams, research passages, the Northstar examples and cases, all tables, exercises, reflection
   questions, takeaways, and reference lines. Evidence labels were checked one by one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 10 editor doubts plus the translator's notes checked; 3 editor doubts changed (ch 29 no. 2,
ch 30 no. 3 and no. 4; the box fix covers both chapters) and 1 translator note (Rafael Duarte). Further
fixes from the full read: ch 29 ×4, ch 30 ×3.
Validation: `tools/validate_book.py` passed.

## Chapter 29

| # | Doubt | Verdict |
|---|---|---|
| 1 | Roaming critic: «На ревью человек отказывает без объяснения причин» | ok. The English "Review comments that reject without reasons" are the critic's own comments; the failure-mode line ("Rejections without reasons") and the coaching plan (her rejections must state a reason) confirm it. |
| 2 | Info box: «После изменений во владении, серьёзности…» | fixed: → «После изменений во владении, в оценке серьёзности и перехода на еженедельные релизы». The English "ownership, severity, and weekly release changes" refers to quarter 1's published severity definitions and the severity audit (timeline weeks 3 and 7); «в оценке серьёзности» covers both and is no longer a bare noun. Same fix in ch 30. Chapter 28's box (line 486 of its `.ru.md`) has the same old wording and should get the same edit. |
| 3 | «заслугу за них staff-инженер делит с командами» for "shared with teams" | ok. Domain outcomes are produced jointly, so they cannot be credited to the staff engineer alone; attribution is the point of the sentence. |
| 4 | Ines's eight hours «как и в базовом квартале» | ok. The English says "unchanged from the baseline figure", and the coaching plan repeats "against the baseline's eight hours", hours per week as in the table. |
| 5 | Solver reordered: «берётся за трудные задачи одну за другой… и глубоко в них погружается» | ok, same claim. |
| t9 | "truck factor" rendered «truck factor (он же bus factor)» | ok; follows the term base. |
| t9 | Evidence paragraph split in two | ok; the "Both support only a weak claim" sentence and its label stay with Wang and Gren and Ralph. |
| t9 | "mostly free at staffeng.com" | ok as a translation; access-like note is in the English (note 1). |
| t9 | "a floor for staff engineers" → «Для staff-инженеров это нижняя граница» | ok. |
| t9 | Rafael Duarte "shares core/order-capture review ownership" → «вместе с ней отвечает…» | fixed. The year 1 record (week 2) says Rafael Duarte and Aisha Bello own core/order-capture reviews; Ines is not a co-owner. Now «с Rafael Duarte, senior-инженером Orders, одним из тех, кто отвечает за ревью core/order-capture». The English is ambiguous (note 2). |

Further fixes:
- Decision framework, disagreement-rule test: "know … how to appeal" had become «как обжаловать его
  решение», which makes only the staff engineer's decisions appealable; the rule lets either loser
  appeal. Now «как подать апелляцию».
- CTO perspective: "given that their knowledge is concentrated by design" had become «если знания
  намеренно сосредоточены», a condition instead of a stated fact. Now «ведь знания намеренно
  сосредоточены именно у них».
- Case, decision 2: "This chapter takes up what follows" had become «Эта глава начинается с того, что
  было потом», which reads as a narrated past event. Now «Эта глава разбирает, что дальше».
- A1: "bulk ordering" had become «оптовых заказов» (wholesale), against the book-wide «массовый заказ»
  (year 1 record, cast, other chapters). Now «для массового заказа».

Full read: no other drift. The opening bet and the two shapes, the mental model (the editor's «с ним
только советуются» matches "only inform" and the scope list's "only consulted on"), the loop diagram,
Wang et al. and Gren and Ralph (research finding, correlational or qualitative, "weak claim"), Avelino et
al. (open source, not companies), expert opinion and this book's recommendation for the rest, Larson's
four archetypes and table, Reilly, the five-part scope (this book's recommendation), reporting line,
snacking/preening/chasing ghosts, the partnering rules, de Wit et al. and Bendersky and Hays, the
disagreement diagram and the one-appeal rule, the critic and hero sections (Wiseman, Kluger and DeNisi
"the authors' theory", Ryan and Deci, Reilly's glue), the principal table (this book's synthesis,
unbolded as in English) and both cautions, the measures table, the time-sample table and its arithmetic
(numbers verbatim), the cost basis, the design-review counts, both decision tables, the six trade-offs,
the six failure modes, the enterprise and CTO sections, the nine-step playbook, the case with the
standing-scope table and coaching plan, all exercises, reflection questions, takeaways, and references
match.

## Chapter 30

| # | Doubt | Verdict |
|---|---|---|
| 1 | «к каким технологиям сводить ландшафт» for "what to converge on" | ok. Policy 1 "Converge before adding" makes the reduction reading explicit. |
| 2 | «иногда лишь как нижнюю границу» for "sometimes as minimums" | ok. Adoptium states end-of-availability as "at least" a month, which the next clause renders «не раньше». |
| 3 | «ни одна не поддерживает сами ставки» for "none maintains rate content" | fixed: → «ни одна не обновляет сами ставки». «Поддерживает» also reads as "supports (as a feature)"; the English means keeping the rate data current, which is "the hard part" of the next clause and what option C buys. |
| 4 | Info box «изменений во владении, серьёзности…» | fixed as in ch 29. |
| 5 | Day rate vs weekly rate reordered | ok, same claim ("Per day it is higher than the book's planning rate of $3,558 per engineer-week"). |
| t9 | "**standard**, vendor guidance" for AWS Well-Architected | ok as a translation; the label is the English one (note 3). |
| t9 | "as the abstract reports it" → «в изложении аннотации» | ok as a translation; access note in reader text is in the English (note 1). |
| t9 | F2 "from year 3" → «с третьего года» | ok. |

Further fixes:
- Decision diagram: "Build minimal, revisit" had become «Минимум; вернуться позже», which dropped
  "build" and leaves the branch's action unclear. Now «Разработать минимум, вернуться».
- Trade-offs: "McKinley's argument is that…" had become «McKinley доказывает», which turns expert
  opinion into proof. Now «McKinley утверждает».
- A2: "what evidence … would make you reverse it" had become «пересмотреть решение» (reconsider), weaker
  than reversing. Now «отменить решение».

Full read: no other drift. Rumelt's kernel and bad-strategy signs, Larson's three claims (both expert
opinion), the loop and its review rhythm, diagnosis/policy/action rules, director versus staff level, the
two build-buy questions (this book's recommendation, a synthesis), TCO definition, Opara-Martins et al.
(research finding, survey-based), Kula et al. (research finding in open-source projects) and Decan et
al., OpenSSF Scorecard (hygiene signal, not proof), McKinley (expert opinion, widely shared), the radar,
Richards and Ford, AWS (standard, vendor guidance), the five evaluation steps (this book's
recommendation), the register and its three kinds with Adoptium and Avelino, the Northstar diagnosis,
three policies and actions, the scoring rule, the TR-01 to TR-09 table (numbers verbatim) with owners and
incidents, the day-rate arithmetic, the decision diagram and both tables, the four trade-offs, the seven
failure modes, the enterprise and CTO sections, the playbook, the case (TCO table verbatim, the four
unlisted factors, SLO, budget share), all exercises, reflection questions, takeaways, and references
match.

## Possible problems in the English (not edited)

1. **Access notes in reader text.** Ch 29 references, Larson: "mostly free at staffeng.com" (and "largely
   free online" in the evidence section); ch 30, Opara-Martins: "as the abstract reports it". CLAUDE.md
   section 7 forbids notes on how a source was accessed in reader text. Suggest dropping them and letting
   the bibliography carry access. The Russian follows the English and should be re-synced if it changes.
2. **Ch 29, Case Study, decision 2**: "Rafael Duarte, a senior engineer in Orders who shares
   core/order-capture review ownership" does not say with whom; the year 1 record (week 2) gives Aisha
   Bello. Suggest "who co-owns core/order-capture reviews with Aisha Bello" or "one of the two owners of
   core/order-capture reviews".
3. **Ch 30, Technology selection**: "**standard**, vendor guidance" for the AWS Well-Architected
   Framework. Vendor guidance is closer to documented practice or practitioner consensus than to a
   standard; consider relabeling.
4. **Ch 28/29/30 info boxes**: "after ownership, severity, and weekly release changes" leaves "severity
   changes" unexplained for a reader who opens the chapter cold. Suggest "after ownership changes,
   severity definitions, and weekly releases".

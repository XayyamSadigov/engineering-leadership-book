# Meaning check, batch 16: chapters 45 and 46

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 15:

1. Every doubt in `editing-ch45.md` and `editing-ch46.md` section 4 and in the translator's notes
   (`notes-t17.md`) gets a verdict.
2. Completeness: headings (45: 25; 46: 24), table lines (45: 56; 46: 34), list items (45: 34; 46: 30),
   ordered items (45: 20; 46: 30), exercises (8 each), Mermaid blocks (2 each), admonitions (1 each),
   paragraphs per section, and relative link targets (46 and 45, identical in order) match the English.
   Every number in table lines is identical to the English (two apparent differences in ch 45 are a
   trailing comma caught by the token script, not a number change). Wrapped lines that begin with a number
   and a period are all items of real loose ordered lists, as in the English. Table rows, exercises,
   reflection questions, takeaways, and reference lines were also checked by eye: nothing is missing. The
   admonitions keep their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar names and numbers were checked against the English.
4. Arithmetic: every computed claim was recomputed and compared with the prose in both languages (which
   figure, which direction, which unit). Ch 45: the discount factors and annuity factor 2.487; the NPV
   example (+$48,700, "about half" of the undiscounted $100,000 gain); the A/B/C table (expected benefit,
   NPV, cost of delay without A's upkeep, payback); A at 0.25 ($101,000, NPV about $2,000); B cash only
   (about −$100,000); the renewal term (0.15 × $1.17M × 72% ≈ $126,000, B passes A); 23 smaller
   customers per top-40 customer; the case note ($4,800 gained, $7,000 lost, net about $2,000 for
   queueing; 0.05 × $504,000 = $25,200, more than ten times the net); the engineer-week rate ($3,558,
   $46,250, $800, $157,250). Ch 46: the effort and forecast ranges (÷ 4.5; 20 percent growth eats the
   shortcut's 5 engineer-weeks); the Poisson table (59/12, 24/<1, 11/<1 percent), "two quarters of five",
   "one year in eight"; P(Poisson(36) ≤ 40) ≈ 0.78; 2 to 3 FTE = 26 to 39 engineer-weeks. All correct in
   the English and carried over unchanged in the Russian.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 10 editor doubts plus the translator's notes checked; none led to a change. Further fixes from
the full read: ch 45 ×2, ch 46 ×2.
Validation: `tools/validate_book.py` passed (stale `dist/` single file ignored, as instructed).

## Chapter 45

| # | Doubt | Verdict |
|---|---|---|
| 1 | Case, «У форума недели 34 было три варианта», option 2 «в слот недели 33» | Russian ok: it mirrors the English ("The week 34 forum had three options … Swap it into the week 33 slot"). The English is inconsistent; see English problem 1. |
| 2 | NPV, «даёт простое правило: положительные значения принимают, отрицательные отвергают» | ok. The English: "accepts positive values and rejects negative ones". |
| 3 | Opening, «Каждая инженерная неделя, потраченная на одно, отнята у другого» | ok. The English: "Every engineering week is spent on one thing instead of another"; nothing more specific. |
| 4 | Two guards, «через квартал-два пересматривают и сообщают о расхождении» | ok. The English: "revisited a quarter or two later, with the variance reported"; the variance is estimate versus outcome (cf. failure mode "compare estimates with outcomes"). |
| 5 | Enterprise, «Переход занимает два квартала: первый… второй…» | ok. The English: "costs a quarter teaching the one-pager and a second discovering how wrong the first estimates were". |
| t17-1 | "top 40" in prose → «из топ-40»; table and A1 use «40 крупнейших клиентов» | ok. |
| t17-2 | "is managed as a cost center" → «для них — руководитель центра затрат» | ok in meaning: the CFO and CEO treat such a CTO as a cost-center head. |
| t17-3 | Table cells keep English number format | ok; glossary rule 6. |
| t17 | "convention to agree with finance" → «условность» (editor) | ok. |
| t17 | New terms (present value, annuity factor, real options, urgency profiles, benefit types, failure-mode names) | ok; consistent through the chapter. |

Further fixes:
- Why This Matters, team scale: "a manager who cannot say what a piece of work is worth" had become
  «сколько стоит работа» (what it costs), the very costs/worth clash the editor flagged in this chapter.
  Now «чего стоит работа».
- Playbook step 2: "Map large items to the four channels, with an amount" had become «для каждого канала
  укажите сумму» (an amount per channel). The amount belongs to each item. Now «для каждой укажите сумму».

Full read: no other drift. The opening, the three scales ($5.0M, 34 percent of 80 engineers, $410,000;
$9M, $250,000, about a year), the objectives and related chapters, the mental model and channel diagram,
Arnold and Yüce (four benefit types; Maersk Line; urgency profiles; accuracy rather than precision;
documented practice, about $100M, $210,000 a week, 38 weeks, nearly $8M), Teece, Lafley and Martin,
Reinertsen, Greenlaw et al., the book's rate paragraph, cash versus capacity (shown twice, labeled), sunk
cost (60 and 40 percent), discounting and the two tables, Dahlquist and Knight (four weaknesses of
payback; sensitivity to the rate), Dixit and Pindyck (publisher's summary), Sullivan et al. (abstract),
the three real-options rules (this book's recommendation), the routing diagram and Berman and Knight, the
info box (week 31; 30 to 17; $410,000 to $95,000; Greg Tanaka, VP Sales), the example (illustrative;
1,900 distributors; 99.9 percent; the measures table; A, B, C inputs and results; Rajiv Menon, Sofia
Alvarez), the decision table and two guards, four trade-offs, seven failure modes, the enterprise
section, the CTO section, the 10-step playbook, the case (fictional; weeks 31 to 34; three slots; 70
engineer-weeks, $700,000, week 36; forecast weeks 44 to 47; the note table; the missing input for option
3; three reader questions), all exercises (F1 $6M, 10 to 8 percent, 75 percent, 12 weeks, six people;
F2 $249,000; F3 $300,000, $200,000, $250,000; A1 week 42, week 60; A3 nine items, three times, 30
percent; X1 49.9 of 80 FTE; X2 400 engineers, four quarters), reflection questions, takeaways, and
references match.

## Chapter 46

| # | Doubt | Verdict |
|---|---|---|
| 1 | Enterprise 2, «каждое исключение действует ограниченный срок» | ok. The English: "named owners who decide exceptions with an expiry". |
| 2 | Alternatives, «реалистичных альтернатив у него три» | ok. The English lists exactly three ("to accept and record a disagreement, to escalate jointly, or to let the decision be made without engineering's evidence"). |
| 3 | Case, «И это давление уже проявилось» | ok. The English: "The pressure already exists: in week 7 a two-hour payment delay rated Sev3 had to be re-rated"; the week-7 event is the evidence that the pressure is present. |
| 4 | Example, «одно разрастание объёма» | Fixed. The English: "scope growth alone consumes what the shortcut saves"; «одно» could read as "a single growth". Now «одно лишь разрастание объёма». Arithmetic: 20 percent of 25 engineer-weeks is the 5 the shortcut saves. |
| 5 | Case, Victor's role not restated | ok. The English paragraph does not restate it either; the map table just below gives "Victor Lindqvist (CTO)". |
| t17-4 | "expert opinion" → «мнением эксперта» (grid), «мнение экспертов» (three sources) | ok; label strength kept. |
| t17 | «интерес × влияние» in the text, «влияние × интерес» for "power-interest" (F1, references) | ok; mirrors the English (see English problem 3). |
| t17 | Grid roles with English glosses (players, subjects, context setters, crowd) | ok. |
| t17 | "position" / "stance" / negotiating position kept apart (место на сетке / отношение / позиция) | ok; the map table and playbook follow it. |
| t17 | «предложение в торге» for "offer" in the estimate failure mode | ok. |

Further fixes:
- Opening: "without quietly giving up the minimum quality" had become «не сдавая понемногу» (little by
  little). "Quietly" means without saying so, which is the chapter's point (a written floor, explicit
  trades). Now «не сдавая втихую».
- Example: doubt 4 above.

Full read: no other drift. The three scales (pipe; five or six executives, one meeting against the next
three; the CEO and the board, the simple target), the objectives and related chapters, the mental model
and loop diagram, Eden and Ackermann (one illustrative case; three points; about a third of goals turn
out to be strategies), Bryson (review), the grid as expert opinion, the floor and Alvidrez (documented
practice), quality above the floor, the two tests, De Dreu et al. (28 studies; research finding;
moderated by class-exercise participation; the lesson as this book's recommendation), Galinsky and
Mussweiler (three experiments; research finding, single-issue price negotiations), Fisher and Ury
(expert opinion), the five-part no, Scott, Stone et al., Grove (all expert opinion), the no-with-a-path
diagram, the example (45 engineers, six-engineer team, 30 engineer-weeks, 4.5 a week, 20 percent; the
option table; weeks 6 and 7; product chooses B), both decision tables, five trade-offs, six failure modes
(the added «Как заметить:» on "Yes now, no later" only labels the English detection sentence), the
enterprise section, the CTO section and Watkins (expert opinion), the 11-step playbook, the case (week
41; 30 to 14, 99.89 percent, $60,000, 8 of 80 FTE; weeks 41 to 44, week 45; the eight-row map with Helena
Marsh, Rajiv Menon, Amara Okafor, Sofia Alvarez, Greg Tanaka, Kwame Mensah; the Poisson table; the floor;
both alternatives; the four-part counter with 40, 36, 78 percent, 6 and 5 FTE, 2 to 3 FTE, trigger above
12; the sequence in weeks 42 and 44), all exercises (F2's eight items; F3 3 engineer-weeks, three weeks;
A1 Marcus Oyelaran, weeks 43, 47, 48 or 49, week 10; A2 week 48; A3 a third of the dates; X2 week 43),
reflection questions, takeaways, and references match.

## Possible problems in the English (not edited)

1. **Ch 45, Case Study (and its source in ch 42 and the year 1 record)**: the case is "set in weeks 31 to
   34", "the next slots open in weeks 33 and 34", and "The week 34 forum had three options", one of which
   is to "Swap it into the week 33 slot". A forum held in week 34 cannot fill a slot that opens in week
   33 (the note even prices the swap as shipping "one week earlier"). The same "week 34 portfolio forum"
   appears in Chapter 42 (case study, A3, X1) and in `first-quarter.md` ("the week 34 portfolio forum's
   outcome is open"), while Chapter 42 says slot 3 frees "at about week 33". Either the forum is held in
   week 32 or 33, or it should be called "the portfolio forum" without a week; fixing it means changing
   chapters 42 and 45 and the year 1 record together. The Russian mirrors the English.
2. **Ch 45, CTO Perspective (line 439) and ch 46, Mental Model (line 53), CTO Perspective (line 327),
   Case (lines 371 and 422), A1 (lines 464 and 465)**: overlong unwrapped source lines; cosmetic.
3. **Ch 46, terminology**: the grid is "interest against power" in the text but "power-interest" in F1
   and the references (noted by the translator). Harmless; the Russian follows each place.
4. **Ch 46, What can be traded**: "quality appears as a fifth variable" after a triangle of three
   (scope, time, cost → capacity). The count only works against the objectives' list of five (scope,
   date, capacity, sequencing, quality); a reader may stumble. The Russian mirrors it.

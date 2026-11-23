# Round 2 notes, lane c1 (Chapters 1–10 and solutions)

Validator: `.venv/bin/python tools/validate_book.py`. The only errors in this lane are the new glossary
anchors `#attrition-and-regretted-attrition` (Ch 4, Ch 10) and `#vesting` (Ch 8), which the book-level
agent is writing. Navigation errors in other lanes and the stale single-file edition are not from this lane.

## Applied in every chapter

- First "Northstar so far" box ends with the "New to Northstar?" line (year in brief, cast).
- Exercises preamble links the baseline page and the cast page (P1).
- Roles at first mention for executives in exercises (Victor Lindqvist (CTO), Rajiv Menon (CFO),
  Helena Marsh (CEO), Greg Tanaka (VP Sales)).
- `first-quarter.md` called "the year 1 record" in reader text.
- "Pull request" changed to "merge request" (Ch 4, 5, 7; ch04 solutions).
- No $800 day rate, $4,000 rate, "17 units", "postmortem", or "canon" in this lane (checked).
- Each case ends with a one- or two-line lesson or open choice.

## Per chapter (words before → after, validator count)

| Ch | Before | After | Findings closed |
|---|---|---|---|
| 1 | 5184 | 5240 | P2 done (1.75× normalization added to the Lazear bullet, within the abstract claim; F3 now solvable). P12 done (Sam → Ari). P8 done (Ch 1 named as the one calendar audit; Ch 3 and 4 add a column). Case: staff-mandate list cut to a link |
| 2 | 5502 | 5495 | "Best engineer" stub merged into the identity subsection with one concrete line. Case trimmed: INC-411/429, the quarter plan, and core/customer ownership cut |
| 3 | 4898 | 4986 | P13 partly: box moved to just after the mental-model quote so it no longer splits the stock/loop explanation; "gain", "paradigms", "subordinate" glossed. Capability-trap and Perlow paragraphs split, point first. 2.3 engineer-years arithmetic shortened. Playbook step 7 now adds a leverage column to Ch 1's audit. Ines's eight hours quoted once (case), not twice |
| 4 | 5111 | 5126 | P10 done (1.4 FTE aside cut; attribution point kept in one sentence). P15 done (regretted attrition linked). P8 done (level column added to Ch 1's audit). Case: first-quarter detail shortened, staff mandates kept in one clause (A3 needs them) |
| 5 | 4953 | 5196 | P7 done (box moved to the Engineering Organization Example, which now opens with a pointer to the case). New subsection "Three situations the design must handle": first one-on-one, the report who brings nothing, remote and cross-time-zone (missing content). Skip-level linked |
| 6 | 5294 | 5420 | P5 done (status bullet split, "moderated" replaced, old idea first, process conflict its own paragraph at the left margin; indentation bug gone). P6 done (template uses Lee, the sample-conversation name). New subsection "Receiving feedback, and giving it upward". Skip-level linked. Case trimmed to the facts the diagnosis uses (dependency counts, regression pass, 126/180 cut) |
| 7 | 5493 | 5475 | P4 done ("what .42 buys" moved directly after the table; table cut to four rows; arcsin method moved to the F3 solution). Rubric row added and the hiring-scorecard template linked (missing content); reference checks added to the funnel. Ch 3 arithmetic removed from Why This Matters. Backfill timeline compressed to one line |
| 8 | 5377 | 5519 | P9 done (new "The career conversation" subsection, links the career-development-plan template). P14 done (bias table now before the countermeasures; "below" reference removed). Bias research tour collapsed into three takeaway-first bullets. EU directive sentence split. Vesting linked. Case trimmed |
| 9 | 5440 | 5533 | P7 done (example opens with pointer; case no longer retells the reconstruction). P11 done (red-build and flaky-test figures cut to one clause; A2's rule now linked to the overview's constraints). New subsection "When the answer is exit" (missing content). Rater-effects and Felps paragraphs shortened, point first |
| 10 | 5275 | 5494 | P3 partly (see below). Motivation table (need, what erodes it, what to change) added. Talent review defined; regretted attrition linked (P15). P7 done (example prices the offer the case ends with; case no longer repeats it). Ines paragraph trimmed |

## Not done, and why

- **P3, the four unfolding-model paths.** `lee1994unfolding` is abstract-only, and the abstract does not
  set out the paths. Describing them would raise evidence strength. The chapter now says it does not
  reproduce them and gives a two-row working split labeled as this book's recommendation, not the
  model's categories. Likewise the turnover meta-analyses' abstracts name no predictors, so the chapter
  now says it lists none. Exercise F1 and its solution were reworded to match. A maintainer who can read
  the full paper could replace the split with the real paths.
- **P13, glossary entries** for stock, flow, reinforcing loop, balancing loop, leverage point: the
  glossary is outside this lane. Terms are defined in-chapter at first use.
- **Repetition across chapters** (manager-effect evidence, Peter Principle, super-engineer): left as
  one-line cross-references; adding the ownership rows to CLAUDE.md is a maintainer decision.
- Ch 8 (5,519) and Ch 9 (5,533) sit just above 5,500 after the required additions.

## Solutions changed

- ch04: "pull requests" → "merge requests".
- ch07: arcsin method added to F3.
- ch10: F1 question gloss reworded (no longer cites "decision paths").

## Fact questions for the maintainer

- None blocking. The Ch 9 A2 constraint is the overview's fifth constraint; linked rather than restated.

# Readability brief, round 2 (option B)

Goal: no chapter with any score below 4 on the rubric (`research/readability/rubric.md`), every high finding
in `research/readability/round2/` closed, and the Northstar load lowered book-wide. This brief adds to
`research/readability-brief.md` (all its rules still bind: facts do not change, evidence strength does not
increase, the chapter contract stays, length targets hold, do not commit). Read CLAUDE.md, both briefs, and
the round-2 report for your lane in full before editing.

## Decisions fixed for every agent (do not deviate)

1. **Case studies carry only what the lesson needs.** In each chapter's Case Study and Engineering
   Organization Example, keep the 5 to 8 Northstar facts the lesson actually uses. Replace the rest with a
   link (year in brief, year 1 record, baseline data, quarter 4 briefing) or cut them. A case ends with a
   one- or two-line statement of the open choice or the lesson. Option tables have at most four short
   columns; derivations go under the table as one line, or into the solutions file.
2. **"Northstar so far" boxes** (each chapter's first one) end with this line, adapted to the relative path:
   `New to Northstar? Read [the year in brief](../../case-studies/northstar/year-in-brief.md) and the
   [cast](../../case-studies/northstar/cast.md).` Chapters 44–60 add `the [quarter 4
   briefing](../../case-studies/northstar/quarter-4-briefing.md)` to that line.
   `year-in-brief.md` is a new page written in this round; link it even if it does not exist yet.
3. **One rate for engineer time.** The book's planning rate is **$3,558 per engineer-week**
   ($185,000 ÷ 52), which is also $46,250 per FTE-quarter. Wherever a chapter, template, or project uses
   **$800 per engineer-day**, keep the number (it feeds case figures such as TR-01's $96,000 to $194,400)
   but label it at first use in that file as **Finance's day rate** ($185,000 ÷ about 230 working days) and
   say once that it is higher per day than the planning rate because Finance counts only working days.
   $157,250 per capitalized FTE-year stays, labeled as the capitalized share (85 percent) of $185,000.
   No other rate is allowed: the business-case template's $4,000 per week becomes $3,558. Chapter 45 states
   the convention once in a short paragraph.
4. **Names for things.** "Change failure rate" everywhere (mention DORA's "change fail rate" only in the
   glossary and once in Ch 25). "Incident review" is the book's term; "postmortem" stays in Ch 25's title and
   first paragraph as the alternative name; "blameless" is an adjective. The page
   `first-quarter.md` is called **"the year 1 record"** in reader text (the file name does not change).
   "17 deployable units (Core counts as one; 24 components in all)" at first use of "17 units" in a file.
5. **New glossary entries** (written in this round by the book-level agent; link them even if they do not
   exist yet, with exactly these anchors): `#budget-envelope`, `#operating-plan`, `#board-pack`,
   `#due-diligence`, `#ciso`, `#attrition-and-regretted-attrition`, `#value-channel-and-urgency-profile`,
   `#quality-engineer`, `#register-ids`, `#velocity-and-story-points`, `#deployable-unit`, `#run-rate`,
   `#requisition`, `#warranty-indemnity-and-escrow`, `#vesting`, `#seat`, `#cycle-time`. Define the term in
   a clause at first use per chapter as before, and link once.
6. **Contradictions are errors to fix**, and the fix must agree with the Northstar case pages. If a fix
   needs a fact that the case pages do not have, do not invent it: write it in your lane's notes file
   (below) for the maintainer.
7. **Solutions follow their chapter.** When you change an exercise, a case fact's wording, or a rate label,
   update the matching `docs/solutions/chNN-solutions.md`.

## Process

- Edit only the files your lane names. Do not edit `mkdocs.yml`, `docs/glossary.md`, the Northstar pages,
  or any `*.ru.md` unless your lane names them.
- Do not spawn subagents or forks.
- Validate with `.venv/bin/python tools/validate_book.py`. Ignore errors caused only by the not-yet-existing
  `year-in-brief.md` and the new glossary anchors listed above, and stale generated pages; fix everything else
  you cause.
- Write `research/readability/round2/notes-<lane>.md`: per chapter, what you changed against each finding
  (finding id, done or not and why), word counts before and after, and any fact questions for the maintainer.
- Final report to the maintainer: under 300 words.

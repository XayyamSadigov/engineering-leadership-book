# How to use this book

## Choosing what to read

You do not need to read the book front to back. The [learning roadmaps](learning-roadmaps.md) give a
path for each role (new manager, experienced manager, director, VP, CTO aspirant, sitting CTO, staff-plus
engineer) and one for a quality transformation, each with a working order and a time estimate. If you
have one problem in front of you, go to its chapter.

A chapter takes about 30 to 45 minutes to read, and one to two hours with an exercise. The roadmaps
assume about four hours a week: one chapter, one exercise, and one reflection question.

## Reading a chapter

Every chapter follows the same sixteen-section structure, so you can find the same kind of material in
the same place:

| Section | What you get | If you are short of time |
|---|---|---|
| Why This Matters | The problem at team, organization, and executive scale | Read |
| Learning Objectives | What you will be able to do | Read |
| The Mental Model | The one or two ideas that organize the chapter | Read |
| Deep Conceptual Explanation | The full treatment, with research | Skim the subsection headings |
| Engineering Organization Example | A worked example with numbers | Read |
| Decision Framework | How to choose among approaches | Read |
| Trade-offs | What each choice costs | Read |
| Failure Modes | How the approach goes wrong, and the early signals | Read |
| Enterprise Application | The topic at 50 to 150 engineers | Read if that is your scale |
| CTO Perspective | The topic at executive scale | Read if that is your scale or your goal |
| Practical Playbook | Steps you can act on | Read, then use |
| Case Study | Northstar, or a sourced real case | Read |
| Exercises | Three levels of applied work | Do at least one |
| Reflection Questions | Questions about your own organization | Pick one |
| Key Takeaways | The operational principles | Read |
| References and Further Reading | Where to go deeper | As needed |

Specialist terms (finance, reliability, organizational design) are defined the first time they appear
in each chapter and collected in the [glossary](glossary.md).

## Evidence labels

Chapters say what kind of support a claim has: research finding, industry research, standard,
documented practice, practitioner consensus, expert opinion, this book's recommendation, or
illustrative. The labels are explained on the [evidence labels](references/evidence-labels.md) page.
Claims without a label are the book's own reasoning.

## Exercises

Each chapter has exercises at three levels:

- **Foundational (F):** apply the chapter's ideas to a defined situation, usually Northstar data.
- **Applied Leadership (A):** handle a realistic leadership situation with people, constraints, and
  incomplete information.
- **Executive Decision-Making (X):** make and defend a decision at director, VP, or CTO level.

Every exercise is written to be answerable from its chapter plus the Northstar pages listed below. Solutions are on
separate pages. Most exercises have more than one defensible answer; the solutions show one worked
answer and the criteria any good answer meets. Write your answer before reading the solution. The
value is in the attempt.

## The Northstar case study

[Northstar Technologies](case-studies/northstar/index.md) is a fictional company with 80 engineers,
a declining quality record, and an executive mandate to improve reliability without adding headcount.
In the story you are its new Engineering Director, and the story runs through your first year (52
weeks). A few later chapters, Project 8, and the later stages of the capstone put you in the CTO's seat
instead.

**Read the overview first.** The [Northstar overview](case-studies/northstar/index.md) takes about
fifteen minutes and introduces the company, the people, the six teams, and the mandate. Every chapter
assumes it. Then read [the year in brief](case-studies/northstar/year-in-brief.md) (about six minutes),
which tells the whole year as a story: what was tried, what worked, what failed, and what is still
open.

**The book's order is not the story's order.** Chapters are ordered by topic, and each sets its case at
the week that suits the topic. Most chapters in Parts I to IV are set in quarter 2; Part V (quality)
goes back to the first 90 days; Parts VI to XI move through quarters 2 to 4; the CTO and advanced
chapters (Parts XII and XIII) and the capstone are set in quarter 4, when the year-2 decisions are
being made. You do not need to have read earlier chapters to follow a case. Each chapter's first
Northstar passage opens with a short "Northstar so far" box that says which week it is and what has
happened. These pages fill in the rest:

| Page | Use it when |
|---|---|
| [The year in brief](case-studies/northstar/year-in-brief.md) | You skipped earlier chapters and want the story so far |
| [Cast](case-studies/northstar/cast.md) | You meet a name and need the person's role and team |
| [Timeline](case-studies/northstar/timeline.md) | You want to know what happened before the week a chapter is set in |
| [Quarter 4 briefing](case-studies/northstar/quarter-4-briefing.md) | You read Chapters 47 to 60, which turn on decisions still open at year end |
| [Baseline data](case-studies/northstar/baseline-data.md) | You want the starting numbers and the small CSV files to do the analysis yourself |
| [Year 1 record](case-studies/northstar/first-quarter.md) | You need an exact figure, week, or decision from the year |

Outcomes in quarter 4 are deliberately left open: where a chapter says the CTO has not decided yet,
that is the point of the exercise.

[Halvard Systems](case-studies/northstar/halvard.md), a fictional company of 500 engineers, appears from
Chapter 34 on, where Northstar is too small to show a problem (several directors, several VPs).

## Using the templates

The [template library](templates/index.md) contains working documents with filled-in Northstar
examples. Adapt them; remove fields you will not use.

## Using the projects

The eight [projects](projects/index.md) each put you in a role at Northstar and ask for the documents a
real leader would produce. A full project takes about 18 to 35 hours after the reading; each has a
shorter core version of about 8 to 12 hours. The roadmaps say which project suits which path.

## Reading offline

The whole book is also available as one Markdown file, `ENGINEERING_LEADERSHIP_HANDBOOK.md`, in the
repository's `dist/` directory and at the root of this site.

# Assessment: the book as a whole (front matter and navigation, Northstar case pages, templates, projects, book-level completeness, terminology)

Read as the target reader: a strong software engineer with no management, finance, or psychology
training. English pages only. Read in full: docs/index.md, about.md, how-to-use.md,
learning-roadmaps.md, download.md, glossary.md, the generated curriculum.md (structure and every
entry pattern), the mkdocs.yml nav; Northstar index, cast, timeline, year-in-brief,
quarter-4-briefing, first-quarter (year 1 record; skimmed in its lower quarter-4 subsections),
baseline-data (first half in full, extended baseline by headings and samples), halvard (first half
in full); templates index plus one-on-one, incident-review, technical-debt-register,
engineering-quality-scorecard, capacity-planning-model, technology-investment-business-case,
executive-update, performance-improvement-plan; projects index plus P2, P3, P5, P8, and the P2 and
P5 solutions. Terminology checked by grep across all English pages.

## Scores
| Item | Words (approx.) | Readability | Clarity | Completeness | Northstar load | One-line verdict |
|---|---|---|---|---|---|---|
| 1. Front matter and navigation (index, about, how-to-use, roadmaps, download, glossary, curriculum, nav) | 18,300 | 4 | 4 | 4 | 3 | Clean, well-ordered entry pages and excellent roadmaps, let down by six slightly different "read this first" rules, a reader-hostile generated curriculum page, and a glossary that defines story bookkeeping but not SRE or observability |
| 2. Northstar case pages (overview, cast, timeline, year in brief, Q4 briefing, year 1 record, baseline, Halvard) | 23,900 | 3 | 4 | 4 | 3 | The overview and the year in brief are model orientation; the four reference pages are dense lookup tables that restate the same results and leak bookkeeping (three money rates, register IDs, "not recorded") |
| 3. Templates (index plus 8 read in full) | 13,700 read of 42,600 | 4 | 4 | 4 | 3 | Consistent, honest, usable structure with a "Minimum version" box; the finance-heavy examples (capacity, business case) and the "not recorded" cells weaken the examples that most need to teach |
| 4. Projects (index, P2, P3, P5, P8, P2 and P5 solutions) | 24,000 | 3 | 4 | 4 | 2 | Very well engineered as assignments (time rules, fact sheets, gaps, pass/fail criteria, rubrics, core versions); heavy fact sheets, undefined statistics in solutions, and a P3 answer spoiled by the book's own orientation advice |
| 5. Book-level completeness (senior engineer to CTO) | n/a | n/a | n/a | 4 | n/a | Unusually broad; missing the leader's own sustainability, organization-level equity, disaster recovery and privacy at CTO level, landing and leaving executive roles, culture as a deliberate artifact, and vendor teams; no project at first-line or staff scope |
| 6. Terminology consistency (grep) | n/a | n/a | 4 | n/a | n/a | Core terms are stable (Sev1, change failure rate, one-on-one, engineer-week, incident review); friction comes from confusable meeting names, nav versus curriculum naming, and a few synonyms (pessimistic/cautious, head of product/product lead) |

Averages over scored cells: readability 3.5, clarity 4.0, completeness 4.0, Northstar load 2.75.

## Top problems (most impact on the reader first, at most 15)

### P1 (high) docs/case-studies/northstar/year-in-brief.md:23 — The book's own orientation advice spoils Project 3
- What the reader experiences: every path tells the reader to read the year in brief before
  starting (learning-roadmaps.md:29-33, how-to-use.md:69-73, index.md:77-79), and Path H puts
  Chapter 27 first (learning-roadmaps.md:217). Both reveal Project 3's central deliverable (the named
  constraint). P3 then says "Do not read the year 1 record until you have submitted" (p3-quality-transformation-plan.md:40),
  too late: the answer is already known.
- Example: "Your diagnosis is that the bottleneck is the Core release train" (year-in-brief.md:23).
- Fix: add a spoiler warning at the top of the year in brief and in Path H ("If you plan to do
  Project 3, do it before reading this page and Chapter 27's case study"). In P3, move the warning to
  the first paragraph and list every page that gives the answer (year in brief, timeline, Ch 27 case,
  capacity template example). Consider reordering Path H so P3 comes before Chapter 27's case study.

### P2 (high) docs/learning-roadmaps.md:29-39 — Six different "read this first" rules
- What the reader experiences: the reader is told different prerequisites in different places and
  cannot tell what is required. index.md:43-45 says how-to-use plus the overview; how-to-use.md:69-73
  says overview then year in brief; learning-roadmaps.md:29-33 says overview, year in brief, and the
  timeline before any path; Path A (line 39) says the overview only; Path C (line 88) overview plus
  timeline; Path D (line 117) timeline plus Q4 briefing; each project and template repeats its own
  version. For a new manager who came for one-on-ones, 20 to 30 minutes of fictional setup before
  Chapter 1 is also a real barrier.
- Example: "Before you start any path, read the Northstar overview (about fifteen minutes) and the
  year in brief (about six), and glance at the timeline." (learning-roadmaps.md:29-31) versus "Before
  you start: the Northstar overview (15 minutes)." (line 39).
- Fix: state one rule once, on how-to-use: "Required: the overview (15 min). Recommended before
  Part V or later: the year in brief (6 min). Everything else is lookup." Make every other page link
  to that rule instead of restating it, and make each path's "Before you start" an addition to it.

### P3 (high) docs/glossary.md:891-990 and 396-397 — The glossary defines story bookkeeping but misses core field terms
- What the reader experiences: a 7,000-word glossary has entries for "Register IDs", "ADR-0001",
  "INC numbers", "The continuation", and "Not yet", but nothing for terms in chapter titles or used on
  dozens of pages: observability (Chapter 24's title), microservice and modular monolith (Chapter
  31's title), SRE (17 pages), flaky test (25 pages), backfill (33 pages), premortem, Kanban and
  Scrum, toil, and the statistics used in solutions (Poisson and Wilson intervals). It also carries
  maintainer text.
- Example: "Anchor for links: `#severity-sev1-sev2-sev3`." (glossary.md:396-397).
- Fix: delete the anchor sentence. Add short entries for observability, microservices and modular
  monolith, SRE, flaky test, backfill, premortem, Kanban and Scrum, and one entry "Small counts and
  intervals" covering why 21 to 17 incidents is noise. Move the Northstar shorthand section to the
  cast or overview page, or cut it to the five entries a chapter reader actually needs (mandate, five
  constraints, Core, weeks and quarters, renewal commitments).

### P4 (medium) docs/curriculum.md:6, 38 and docs/templates/index.md:57 — The curriculum page reads like a build report
- What the reader experiences: the page a reader opens to see what the book covers shows raw
  citation keys as link text, the same status line under all 60 chapters, and a stale paragraph
  about planned chapters that no longer exist. The template index promises a mapping the curriculum
  does not contain.
- Example: "Primary sources: [grove1983high](references/bibliography.md#grove1983high),
  [fournier2017manager](...)" (curriculum.md:38); "The curriculum lists all twenty-four templates with
  the chapters that use them." (templates/index.md:57), while the curriculum's template table has only
  a Status column.
- Fix: in tools/build_curriculum.py, render sources as "Grove, 1983", drop the per-chapter status line
  (one sentence at the top suffices), delete the "Planned chapters" sentence, and add a "Used in"
  column to the template table (the data is already in each template's header).

### P5 (medium) docs/case-studies/northstar/quarter-4-briefing.md:86-89 — Three money rates leak into reader pages
- What the reader experiences: the reader learns one rate ($185,000 a year, $3,558 an engineer-week),
  then meets Finance's $800 day rate, then a $157,250 capitalization rate, each with a paragraph on why
  they differ. The explanations appear on the Q4 briefing, in the glossary (208-216), and in P8's fact
  sheet (136-137). It reads as an internal consistency patch, not a lesson.
- Example: "Finance's day rate is $185,000 ÷ about 230 working days. It is higher per day than the
  book's planning rate of $3,558 per engineer-week because Finance counts only working days."
- Fix: on reader pages, convert Finance's TR-01 scenarios once into engineer-weeks at the planning
  rate and drop the day rate. Keep the capitalization rate only in Chapter 52 and P8, where
  capitalization is the lesson.

### P6 (medium) docs/templates/executive-update.md:115-120, 147-151 — "Not recorded" hollows out the examples
- What the reader experiences: the example meant to show a model executive update has all four
  commitment rows reading "not recorded", followed by an apology. Similar endings ("The director's
  decision on Tom's draft is not recorded", performance-improvement-plan.md:100; "whether Daniel
  adopts the draft is not recorded", one-on-one.md:132-133) appear in 11 of 24 templates. The
  convention protects story continuity at the cost of the teaching example.
- Example: "The commitments table still says not recorded for all four initiatives ... A real update
  would fill those cells first" (executive-update.md:148-150).
- Fix: allow template examples to fill cells with values marked **illustrative**, as the 1:1 and
  capacity examples already do for other figures. Keep "not recorded" for the story pages and
  exercises, where open outcomes are the point.

### P7 (medium) docs/templates/technology-investment-business-case.md:185-219 — The finance example outruns the reader
- What the reader experiences: an engineer with no finance training meets a YAML block of
  unexplained arithmetic: a CD3 of 0.034, a break-even computed as "182082 x 1.331 / 52" (1.331 is
  1.1 cubed, the three-year discount factor, never said), an undefined "optional Kanban class" of
  service, and NPV figures without the cash-flow table behind them.
- Example: "break_even: about $4,660 a week   # 182082 x 1.331 / 52, arriving in year 3".
- Fix: move the arithmetic out of the YAML into a three-row cash-flow table (year, flow, discount
  factor, present value) with one sentence saying what 1.331 is. Delete `class_of_service` or define
  it. Keep the YAML to filled values only.

### P8 (medium) docs/projects/solutions/p5-solution.md:41-56, 236 — Undefined statistics, and the book grades its own chapter "weak"
- What the reader experiences: the solution reads quarter-to-quarter changes with Poisson and Wilson
  intervals and standard deviations, none defined anywhere in the book, and then scores Chapter 38's
  case-study scorecard 47 of 100, "weak". A reader who just learned from Chapter 38 does not know
  which to trust.
- Example: "conditional on 38 incidents, 17 is 0.65 standard deviations below an even split"
  (line 53); "Total 47, weak." (line 236).
- Fix: add a short boxed explanation (what an interval on a small count means, and how to get one
  from a calculator or spreadsheet), or link a new glossary entry. Reframe section 9 as "Chapter 38's
  scorecard is a sketch; here is what finishing it takes", and add one line in Chapter 38's case study
  saying the proposal is deliberately incomplete and Project 5 finishes it.

### P9 (medium) mkdocs.yml:432-437 — Projects come after the capstone, with solutions one click away
- What the reader experiences: the capstone (Chapter 60) reuses project outputs, yet the nav lists
  Projects after it. Within Projects, each solution sits directly under its project, so the answer is
  the next item in the sidebar.
- Example: nav order "XV. Capstone" (line 432), then "Projects" (line 434) with "Project 1 solution"
  at line 437 directly after Project 1.
- Fix: put Projects before XV. Capstone. Group the eight solutions in a "Project solutions" subsection
  after all projects, as the chapter solutions are grouped separately.

### P10 (medium) docs/curriculum.md vs mkdocs.yml nav — The same items carry different names
- What the reader experiences: names change between the sidebar, the curriculum, and the indexes, so
  the reader wonders whether they are the same thing.
- Example: Part XIV is "Templates and playbooks" in the nav but "Practical Management Systems and
  Playbooks" in the curriculum; Project 1 is "Management operating system" in the nav but "P1: Build
  an Engineering Management Operating System" in the curriculum; "Incident review" versus "Incident
  review template"; the template is "1:1 template" (templates/one-on-one.md:1) while the book says
  "one-on-one" 264 times and "1:1" nowhere else.
- Fix: one canonical title per item in curriculum.yaml, used by the nav, the curriculum, and every
  index. Rename the template "One-on-one template".

### P11 (medium) docs/glossary.md:755-762 — Three near-identical meeting names
- What the reader experiences: "operational review" (the director's weekly meeting, 70 uses),
  "operating review" (the VP's monthly meeting, defined in the glossary) and "operations review"
  (Elena Sokolova's team meeting, 25 uses, e.g. templates/engineering-manager-rubric.md:91) are three
  different meetings, and only two are distinguished.
- Example: "Weekly 30-minute operations review, two years old at baseline" (engineering-manager-rubric.md:91).
- Fix: rename the team-level one ("Payments' weekly on-call review") everywhere, and add a line to
  the glossary entry naming all three.

### P12 (medium) docs/case-studies/northstar/index.md:127, 105, 166 — The overview's first read has gaps
- What the reader experiences: the page every reader must read uses a `flowchart LR` system diagram
  with four subgraphs, unreadable at phone width; introduces "Joon Park's two-person security
  function" (line 105) without saying who he is; and uses Sev1 and Sev2 (lines 166, 174) and service
  credits without a definition or glossary link on the page.
- Example: "Joon Park's two-person security function is part of the 14. Northstar has no CISO".
- Fix: redraw the diagram `TD` (clients, edge, Core, services as stacked groups); write "Joon Park
  (IT security lead)"; link Sev1/Sev2, service credits, and CISO to the glossary at first use.

### P13 (low) docs/templates/technical-debt-register.md:41, 120, 130 — Undefined term and unkept promises
- What the reader experiences: "standing share" is used three times before it is explained at line
  148 ("the 10 to 20 percent standing share"). The PIP template credits "the five properties of a fair
  plan" (performance-improvement-plan.md:154) that it never lists, and its example has three
  expectations where step 4 requires four to six.
- Example: "A team decides within its own components and standing share" (line 41).
- Fix: define standing share in step 7 ("a fixed 10 to 20 percent of team capacity reserved for debt").
  List the five properties in the PIP intro or drop the reference; add a fourth expectation to the
  example or say why three suffice.

### P14 (low) docs/case-studies/northstar/quarter-4-briefing.md:76-86 — The open-items table packs a page into each cell
- What the reader experiences: cells of 40 to 70 words with option letters, rates, weeks, and dollar
  ranges; the reader looking for "what is open" gets the detail first.
- Example: TR-01 row: "120, 190, or 243 engineer-days ($96,000 to $194,400 at Finance's day rate of
  $800), expensed. One open critical vulnerability waits on it".
- Fix: one short line per item ("Whether to pay for the Core framework migration; about $100,000 to
  $195,000") with a link to the year 1 record for detail.

### P15 (low) docs/projects/p3-quality-transformation-plan.md:4 and p5-delivery-and-reliability-scorecard.md:140 — Small internal contradictions
- What the reader experiences: P3 opens "It is your first week" but the Timing paragraph says "You
  submit the plan at the end of your second week". P5 refers to "policy A or B" without having
  labeled the two error-budget policies.
- Example: "whether Victor will choose policy A or B" (p5:140).
- Fix: say "weeks 1 and 2" in P3's opening and projects index; in P5 constraint 6 write
  "reporting mode (A) or enforced with Victor arbitrating (B)".

## Patterns across your scope
- **Orientation repeated with drift**: index, how-to-use, roadmaps (general and per path), the
  Northstar index, year in brief, every project, and every template's "Northstar so far" box restate
  what to read first, each slightly differently. Book-wide rule: state the reading prerequisites once
  (how-to-use) and link to them everywhere else.
- **Maintainer bookkeeping in reader text**: glossary anchor note, curriculum status lines and raw
  citation keys, "these pages are right and the chapter has a defect" (northstar/index.md:12-13),
  the day-rate reconciliation paragraphs, and "not recorded" in teaching examples. Rule: reader pages
  carry no text whose purpose is internal consistency; push it into the YAML or research files.
- **The same results table in five places**: baseline to quarter 3 figures appear in the timeline
  (99-112), the year 1 record (day 90, Q2, Q3 tables), the Q4 briefing (33-39), the year in brief, and
  P5/P8 fact sheets. Rule: one canonical results table (timeline) and links elsewhere; repetition here
  costs reading time and invites drift.
- **Wide tables at phone width**: the debt register example (9 columns of sentences), the quality
  scorecard (9 columns), the timeline (two columns of link lists), P5 solution's scorecard (9 columns).
  Rule: at most five columns of prose; move long cells to a list under the table.
- **Statistics and finance in solutions without definitions**: Poisson and Wilson intervals,
  standard deviations, discount factors, capitalization. Rule: any method a solution uses must be
  taught in a chapter or defined in the glossary.
- **Week-pinned references without a reminder**: "the week-31 trigger", "the week-32 Core change
  failure checkpoint in the week-26 report", "the week 78 gate". Rule: every week reference carries
  three words of what it is the first time it appears on a page.

## Missing or thin content
- **The leader's own sustainability**: no treatment of the manager's or director's energy, isolation,
  or burnout (0 pages mention self-care; burnout appears only for engineers). Ch 2 or Ch 40;
  1,000 to 1,500 words.
- **Equity at organization scale**: inclusion is covered at team level (Ch 7 inclusive hiring, Ch 11
  inclusion), but not representation in the hiring funnel, promotion and pay-equity audits, or what a
  director measures. Ch 8 and Ch 48; a section of about 1,000 words each.
- **Disaster recovery and business continuity** (recovery time and recovery point objectives, backup
  testing): 0 pages. **Privacy and data-protection regulation**: GDPR appears nowhere. Ch 53 and Ch 24;
  a section each.
- **Getting, starting, and leaving senior roles**: interviewing for a director, VP, or CTO role,
  negotiating the mandate before accepting, and handing over when leaving. Ch 4 or Ch 50;
  about 1,500 words.
- **Culture and values as a deliberate artifact** (writing culture, engineering values, rituals): no
  chapter owns it; it is scattered across Ch 11 and Ch 14. A section in Ch 40 or Ch 50.
- **Vendor and contractor teams**: Halvard has 60 vendor engineers and Northstar's workforce plan
  lists a fixed-scope vendor contract, but there is no guidance on managing outsourced work. Ch 48;
  a section.
- **Projects for Paths A and G**: both paths end with practice sets because no project is set at
  first-line or staff scope (learning-roadmaps.md:51-56, 201-205). Two shorter projects (8 to 12
  hours): "Your first 90 days as a team manager" and "Write and land a cross-team technical decision".
- **Glossary entries**: observability, microservices and modular monolith, SRE, flaky test, backfill,
  premortem, Kanban and Scrum, toil, small-count intervals, and the leadership roles themselves
  (engineering manager, director, VP, CTO).

## What works well (keep)
- **The orientation layer**: the Northstar overview plus the six-minute year in brief is the best
  part of the case. The year in brief is plain, causal, and honest about failures.
- **The roadmaps**: role-based paths with reasons for the order, time estimates with the calculation
  shown, and a problem-indexed Path F.
- **Template structure**: Used in, Owner, Cadence, Minimum version, How to fill it in, Template, YAML,
  Example, What to notice, Common mistakes, Review questions, Evidence with labels. The 1:1 and
  incident review templates are excellent: the example shows the failure the template prevents.
- **Project design**: time rules, a fact sheet with weeks and sources, "Facts you do not have",
  pass/fail acceptance criteria, weighted rubrics, core versions with rescaled points, and solutions
  that show a weak submission scored against the rubric. P2's diagnosis and its peer-comparison
  method are a model of teaching judgment.
- **Honest evidence handling**: the evidence-labels page, labels in templates, and statements such as
  "No study gives a correct prevention share".
- **Terminology care where it matters most**: lead time's two senses, local versus DORA change
  failure rate, incident review versus postmortem, and calibration's two senses are each explained in
  the glossary.
- **The cast page's tip box** naming the dozen people who drive the story and telling the reader not
  to memorize the rest.

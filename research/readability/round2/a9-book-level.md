# Assessment: book level (front matter and navigation, Northstar case pages, templates and projects, book-level completeness, terminology)

Read in full: `docs/index.md`, `about.md`, `how-to-use.md`, `learning-roadmaps.md`, the glossary's structure
and about 60 percent of its entries, `curriculum.md` (head, Part XIV, Part XV, projects), the `mkdocs.yml`
nav; Northstar `index.md`, `cast.md`, `timeline.md`, `quarter-4-briefing.md`, plus the structure and sample
sections of `first-quarter.md`, `baseline-data.md`, `halvard.md`. Templates read in full: one-on-one,
performance-improvement-plan, engineering-quality-scorecard, capacity-planning-model,
technology-investment-business-case, new-manager-90-day-plan, risk-register, team-charter (plus the
template index and a structural grep of all 24). Projects read in full: index, P2, P8, P4 (to the
trade-offs), P6 (problem and constraints), plus the section structure of all 8 projects and 8 solutions.
Completeness and terminology come from `curriculum.md`, every chapter's H3 list under Deep Conceptual
Explanation, `wc -w`, and term greps across chapters, solutions, templates, projects, and case pages.

## Scores
| Item | Words (approx.) | Readability | Clarity | Completeness | Northstar load | One-line verdict |
|---|---|---|---|---|---|---|
| 1. Front matter and navigation | 15,000 (index 900, about 550, how-to 1,000, roadmaps 2,500, glossary 5,100, curriculum 5,000) | 4 | 4 | 4 | 4 | A new reader can tell where to start, which path fits, and how long it takes. The faults are small: stale counts, one chapter missing from the "full climb", and glossary gaps in the CTO vocabulary. |
| 2. Northstar case pages | 22,100 (first-year record 7,500, baseline 5,800, Halvard 2,800, timeline 1,850, overview 1,600, cast 1,500, Q4 briefing 1,050) | 3 | 4 | 4 | 3 | Easy to find things in, but most of it is ledger tables written to keep the chapters consistent. Nowhere is the year told as a story, and the quarter 4 briefing packs twelve open decisions into one table. |
| 3. Templates (24) and projects (8 plus solutions) | 97,000 (templates 41,000, projects 24,000, solutions 31,000) | 4 | 4 | 4 | 3 | Very consistent and usable. Workload is explicit (hours, core version, pass/fail criteria, weighted rubric). The worked examples and the "facts you must use" tables lean hard on the case's shorthand. |
| 4. Book-level completeness | 345,000 in chapters | 3 | 4 | 4 | 3 | Covers the ground broadly and the progression holds. Chapter length tracks the template rather than the topic, and the load peaks in Parts XII–XIII. A few expected topics are thin or scattered. |
| 5. Terminology consistency | n/a (grep) | 4 | 4 | 4 | 4 | Terms are consistent overall (Sev1, skip-level, engineer-week, one-on-one). The main exceptions: several rates for pricing engineer time, three names for an incident review, and four names for the first-year record page. |

## Top problems (most impact on the reader first, at most 15)

### P1 (high) docs/case-studies/northstar/first-quarter.md:1 — The case that every chapter assumes is never told as a story
- What the reader experiences: how-to-use.md:69–71 says every chapter assumes the Northstar overview, and the
  chapters are out of story order. To catch up, the reader has three options. The overview (good, but it stops
  at arrival). A 70-row timeline table (timeline.md:20–90). Or the 7,500-word "director's first year" page, a
  ledger of "Decision | Detail | Chapter" rows written so that chapters stay consistent, not so that a reader
  understands. Nowhere does a reader get the year's arc in prose: what was tried, what worked, what failed,
  and why the quarter 4 decisions are open.
- Example: "Each row names the chapter that tells that part of the story, so that the chapters agree with
  each other." (first-quarter.md:9–10). This states the author's purpose. The page header then opens with
  a 24-row table of decisions such as "Prevention allocation, quarter 1 | 12 FTE in total: Billing 25
  percent, Orders and Payments and Integrations 10 percent ...".
- Fix: add a page of 800 to 1,200 words, "The year in brief" (four short sections, one per quarter, with
  no tables and at most five numbers each), and link it from index.md, how-to-use.md, and every "Northstar
  so far" box. Rename the first-year page's nav entry to "Year 1 record (reference)" and say in its first
  line that it is a lookup page.

### P2 (high) docs/templates/technology-investment-business-case.md:118–123 — The book prices an engineer's time several different ways, then warns readers not to mix them
- What the reader experiences: an engineer-week is $3,558 (÷52) in Chapter 45 and most of the book, and $4,000
  (÷46 working weeks) in this template. An engineer-day is $800 (÷230) in Chapters 21, 30, and 52. There is
  also $46,250 per FTE-quarter, and $157,250 per FTE-year for capitalized work. The glossary
  (glossary.md:121–127) has to warn that "five engineer-days cost more than one engineer-week in those
  chapters", and P8 tells the learner that "mixing them is the most common arithmetic error in this project"
  (p8:181–183). In other words the book creates the trap it then warns about. A reader who meets two rates
  inside one worked example, as this template has at lines 120–123, stops trusting the numbers.
- Example: "Effort, per engineer-week | $185,000 a year ÷ 46 working weeks | about $4,000" next to "Saving,
  per calendar week | $185,000 a year ÷ 52 weeks | about $3,558".
- Fix: choose one convention for the whole book: $3,558 per engineer-week, and $712 per engineer-day at
  five days a week. Recompute the $800-a-day cases (TR-01's $96,000 to $194,400 recurs in Ch 30, Ch 52, the
  risk register, the Q4 briefing, and P8), or label $800 explicitly as Finance's own rate wherever it appears.
  Then cut the glossary warning and P8's step 2 caution down to one sentence.

### P3 (high) docs/glossary.md:3–8 — The glossary misses the vocabulary of the CTO chapters and has no A–Z entry point
- What the reader experiences: the glossary is strong for delivery, reliability, and people terms (about 110
  entries, grouped by subject). It is missing terms that the Part XI–XIII chapters, the quarter 4 briefing,
  and P8 use constantly: budget envelope, operating plan, board pack, due diligence (in Ch 55's title), CISO,
  attrition and regretted attrition, value channel and urgency profile (defined only inside the business-case
  template), quality engineer (the role the QA engineers move into), and TR-01 or ER-xx (register IDs that
  the Northstar shorthand section leaves out, although it covers INC and ADR-0001). There is also no
  alphabetical list, so a reader must guess which of eight subject groups holds a term ("use your browser's
  search").
- Example: quarter-4-briefing.md:55 "TR-01 funding | The Core framework migration (TR-01 on the technology
  risk register): 120, 190, or 243 engineer-days ($96,000 to $194,400), expensed" — this line uses the
  glossary terms "expensed" and "engineer-day", while "TR-01" and "the envelope" in the next section are
  undefined.
- Fix: add the ten entries above (about 600 words). Add a one-line A–Z index of term links at the top
  of the page, or at least list the eight group headings with anchors.

### P4 (medium) docs/case-studies/northstar/quarter-4-briefing.md:42–55 — The entry page for Parts X–XIII is a 12-row table of open decisions in shorthand
- What the reader experiences: index.md and how-to-use.md send readers who start at Parts X–XIII here. The core
  of the page is one table with 12 rows and four columns. The rows mix strategic choices (year-2 org, VP) with
  details (CI target, TR-01 funding, security reporting line), and they use the case's private vocabulary
  ("stage 2 'Hold'", "week 78 gate", "ADR-0001", "the 87-seat rule", "Alternatives B, C, D"). A reader cannot
  tell which three decisions matter most.
- Example: "Quality continuation | Stage 2 "Hold" (quarters 5–6, 6 FTE, $150,000 tooling) and stage 3
  "Converge" (quarters 7–8, 5 FTE); no headcount request | Management, inside the board's budget envelope;
  executives took positions in weeks 46–47 | Requested by week 51".
- Fix: lead with "The three decisions that drive quarter 4" (year-2 organization, quality continuation,
  board headline), one short paragraph each. Move the other nine rows into a second table headed "Other open
  items", and give each row one plain sentence of what is at stake.

### P5 (medium) docs/learning-roadmaps.md:21 — The "full climb" from manager to CTO leaves out Chapter 26 (security)
- What the reader experiences: the roadmap says paths A to E "form one climb ... so no chapter appears twice".
  Across the five paths the climb covers 58 chapters plus the capstone. Chapter 26 (security and supply chain)
  is in none of them. It appears only as "Chapter 26 also helps" beside Project 3 (line 104), and in Paths F
  and H. A reader who follows the promised climb to the CTO path then meets Chapter 53 (security strategy)
  without the team-level chapter it builds on.
- Example: "Paths A to E form one climb: each assumes the one before it, so no chapter appears twice."
- Fix: add Chapter 26 to Path B, order 3 ("19, 21, 22, 23, 26"), and update the counts in learning-roadmaps.md
  and index.md:32 (B becomes 15 chapters). Alternatively, state that the climb omits it and why.

### P6 (medium) docs/index.md:9 — Stale counts and generator residue on the first pages a reader sees
- What the reader experiences: the home page says "All 60 chapters, 20 templates, 8 projects" (line 9) and
  "20 templates" again (line 58). The template index and the nav list 24. The curriculum page opens with "0
  of 60 chapters are published, and 60 more are on the site awaiting human review" (curriculum.md:6) and
  shows "XIV ... | templates | 0 of 0" (curriculum.md:23). Part XIV has 24 templates on the site. The
  curriculum's project table (curriculum.md:834ff) has no links. about.md:36 reads "every page carries an
  notice". Each of these is small, but together they make the front door look unfinished.
- Fix: change "20" to "24" in index.md:9 and :58. Change the build_curriculum.py wording to "All 60 chapters
  are on the site; none has yet completed human review". Make the Part XIV row count templates (24 of 24).
  Link the project table. Fix "an notice".

### P7 (medium) docs/templates/index.md:12–41 — The template library is a flat, unordered list
- What the reader experiences: 24 templates are listed in roughly the order they were written: quality first,
  then people templates mixed with CTO ones, then four added at the end. The heading "Available now" is left
  over from an earlier state. Path F calls this library "designed for" the CTO reference reader, and that
  reader has to scan all 24 rows to find the three for their level.
- Fix: group the table under four headings: Your team (1:1, career plan, team health, team charter, PIP,
  hiring scorecard, new manager plan), Engineering system (quality scorecard, debt register, incident
  review, ADR, 90-day quality plan), Organization and operating system (org design, QER, capacity model,
  EM rubric, director matrix, succession, stakeholder map, executive update), and Executive (strategy,
  business case, risk register, CTO matrix). Delete "Available now". Apply the same grouping to the nav.

### P8 (medium) docs/templates/*.md — "Minimum version" exists in 4 of 24 templates, and is missing in the heaviest ones
- What the reader experiences: the 1:1, ADR, CTO matrix, and risk register templates tell the reader what
  to use on day one. The capacity model (three example tables plus a cautious case), the business case (a
  45-line YAML block), the 90-day quality plan, the succession plan, and the org design assessment do not.
  Those are exactly the templates a working manager is most likely to drop for being too big.
- Fix: add a three-line "Minimum version" admonition to the other 20, using the existing pattern (one-on-one.md:20–23).

### P9 (medium) docs/projects/p8-cto-technology-investment-proposal.md:72–85, 136–145 — The time rule and "facts you must use" tables send learners on a canon hunt
- What the reader experiences: the projects are well designed: same nine sections, hours stated, core
  version with rescaled rubric, pass/fail acceptance criteria. But in P8 the learner has to collect facts
  dated week 47 or earlier from five anchors on the first-year page, the briefing ("which also mentions later
  weeks, which stay off limits"), and the case studies of Chapters 30, 45, 49, and 52. The facts table is a
  wall of about 60 numbers in six cells. P2:119–127 and P4's facts table do the same at a smaller scale. A
  good share of the 28 to 35 hours goes on finding facts rather than deciding.
- Example: "Economics | $185,000 per engineer-year; $46,250 per FTE-quarter; about $3,558 per engineer-week
  ($185,000 ÷ 52); $800 per engineer-day in Chapter 30's tax-svc case; gross margin 72 percent; discount rate
  10 percent; ARR $140M; ..."
- Fix: give each project a one-page "Project fact sheet" (a CSV or a page) with every permitted fact as one
  row, its week, and its source. Then the time rule is enforced by the sheet, not by the learner. Split each
  facts table into one row per number.

### P10 (medium) docs/templates/capacity-planning-model.md:86–90 — The example's quarter 3 and 4 rows are plans, but the labels do not say so
- What the reader experiences: the example labels quarter 1 as "plan" and "measured". Quarters 3 and 4 are
  just "Quarter 3: 22%" and "Quarter 4: 18%". The timeline (timeline.md:107) and the Q4 briefing give quarter 3
  unplanned work as a measured 25 percent, and quarter 4 is never measured. A reader cross-checking against
  the case thinks one of the pages is wrong.
- Fix: label the rows "Quarter 2 measured", "Quarter 3 plan (measured: 25%)", and "Quarter 4 plan (not
  measured)".

### P11 (medium) docs/case-studies/northstar/cast.md:63–85 — Many named people and no core cast
- What the reader experiences: the cast page lists about 45 Northstar names and 20 Halvard names, all at the
  same visual weight. A reader who meets "Teodora Vasquez-Lund" or "Bram Verhoeven" cannot tell whether they
  matter, and the page cannot answer "who do I need to remember?". The page's own warning about similar names
  (Owen versus Tamsin Achterberg, Mateo Rinaldi versus Mateo Arango Ríos) shows the load.
- Fix: open the page with a box, "The ten people who drive the story" (Victor, Amara, Rajiv, Greg, the six
  managers, and the three staff engineers grouped as one line). Mark everyone else as appearing in one or two
  chapters.

### P12 (medium) docs/case-studies/northstar/first-quarter.md — One page goes by four names
- What the reader experiences: the same page is "The director's first year" (nav and H1), "the first
  quarter page" (glossary.md:708, :722), "[the first quarter]" (p8:113, p4 Starting Dataset), "the
  first-year record" (P4, P6), and "Northstar's quarter 4 record" (risk-register.md:110–111). The file is
  named `first-quarter.md` but covers all four quarters. Readers searching for "first quarter" expect weeks
  1 to 13.
- Fix: use "the year 1 record" everywhere and rename the file to `year-1-record.md`, with a redirect.

### P13 (low) docs/parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md:253–453 — "Change failure rate" and "change fail rate" mixed, including in the chapter that owns the term
- What the reader experiences: 45 files say "change failure rate" and 7 say "change fail rate" (Ch 23 five
  times, Ch 25, the Ch 38 scorecard row, and three solution pages). Ch 25:241 explains that DORA uses "change
  fail rate", but Ch 23 switches between the two without saying so.
- Fix: use "change failure rate" throughout, and mention DORA's term once in the glossary entry.

### P14 (low) docs/parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md — Three names for the review after an incident
- What the reader experiences: Ch 25's title says "Postmortems" (21 files use the word), the template is
  "Incident review" (29 files), and the glossary entry is "Blameless review" (10 files). The glossary does say
  they are the same thing, but a reader moving between Ch 25, the template, and the scorecard row
  "Recurrence ... Review records" has to piece that together.
- Fix: choose "incident review" as the book's term (it matches the template and the operating-system
  chapters). Keep "postmortem" in Ch 25's title and first paragraph as the alternative name, and use
  "blameless" only as the adjective.

### P15 (low) docs/templates/technology-investment-business-case.md:108 and Ch 32:454 — "17 units" against "24 components"
- What the reader experiences: the overview and the data files count 24 components. The business case template
  and Ch 32 say "17 units" without explanation (deployable units: Core counted once, services, frontends; the
  only definition is in baseline-data.md:389).
- Fix: write "17 deployable units (Core counts as one; 24 components in all)" at first use in each place, and
  add "deployable unit" to the Northstar shorthand in the glossary.

## Patterns across your scope
- **Reference pages written for consistency, not for reading.** The first-year record, the timeline, the Q4
  briefing, and parts of the baseline are tables whose purpose is to keep 60 chapters consistent (and they do).
  Book-wide rule: every reference page opens with a short prose paragraph saying what it is for and what to
  read first, and the case gets one prose narrative page (P1).
- **The case's shorthand leaks into stand-alone material.** INC-416, TR-01, ER-03, "the continuation", "stage 2
  Hold", "the 87-seat rule", "17 units", and the week numbers appear in template examples and project briefs
  that are supposed to be usable on their own. Rule: any template example or project brief defines each
  case-specific code at first use in that file, or links it to a glossary entry.
- **Money conventions multiply.** Several rates for engineer time (P2). Rule: one rate book-wide, set out in
  Chapter 45 and the glossary. Any exception is labeled as someone else's rate (for example "Finance's
  day rate") at every use.
- **Generator and status residue.** "Available now", "0 of 0", "0 of 60 ... 60 more", "20 templates". Rule:
  the generated pages and the home page are checked against the actual counts by `validate_book.py`.
- **Strong structural consistency.** All 24 templates share the same sections (Used in, Owner, Cadence, how
  to fill it in, template plus YAML, Northstar example with a "so far" box, common mistakes, review questions,
  evidence). All 8 projects share the same nine sections. Keep this. Close the remaining gaps: "Minimum
  version" (P8), and solution endings that vary (P4's solution has no "other defensible answers" section,
  P3's has no "weak submission" section, although the projects index promises both).

## Missing or thin content
- **A first-line manager project, and a staff-engineer project.** learning-roadmaps.md:50 and :200 admit that
  no project is set at either scope, so Paths A and G end in practice sets. Path A is the largest audience.
  Add a "P0: Run your team's first quarter" (one-on-ones, a team charter, a hiring scorecard, a PIP decision)
  built on the Customer Experience or Orders data, at about 10 to 14 hours. Optionally add a staff-engineer
  project built on ADR-0001.
- **Engineering culture as a deliberate topic.** Culture is discussed in pieces (Ch 6 feedback across
  cultures, Ch 11 safety, Ch 25 blameless culture, Ch 43 reinforcement) but no chapter or section treats "how
  a director or CTO shapes engineering culture and values, and how to tell whether it changed". Add about
  1,500 words as a section in Ch 43 or Ch 50.
- **Organization-wide communication.** All-hands meetings, writing to 80 or 500 engineers, and announcing
  decisions appear only in passing (5 chapters mention all-hands). Ch 49 covers executive communication
  upward only. Add about 1,200 words to Ch 37 or Ch 43 on communicating to the whole organization.
- **The leader's relationship with their own manager above the first level.** "Managing up" is a subsection
  of Ch 2 (new manager). Directors and VPs managing a CTO or CEO get no equivalent; Ch 46 covers peers and
  stakeholders. Add about 1,000 words to Ch 40 or Ch 47.
- **The leader's own sustainability above the first level.** Ch 2 has "Your own load and sustainability"
  and Ch 10 covers burnout in reports. The isolation and load of the director, VP, and CTO jobs are not
  covered. About 800 words in Ch 40 or Ch 50.
- **Hiring leaders.** Ch 7 is about hiring engineers, and Ch 47's "Staffing the director team" covers part
  of the topic. Assessing and hiring managers and directors from outside (scorecards for leaders, reference
  checks, executive search) is thin. About 1,000 words in Ch 41 or Ch 47.
- **Succession is filed under reorganizations.** It is taught in Ch 36 (a reorg chapter) and touched in Ch 41,
  Ch 48, and Ch 49. A reader looking for it would try Ch 41 first. At minimum add a pointer at the top of Ch 41,
  or move the section.
- **Length balance.** Chapters 1–51 all fall within 5,150 to 5,830 words (±6 percent), whatever the scope of
  the topic: Ch 30 (strategy, selection, and build versus buy, four subsections) is as long as Ch 5
  (one-on-ones). Chapters 52–59 run 6,200 to 7,150 and the capstone 7,700. So the heaviest reading, which also
  carries the densest quarter 4 material, comes at the end, when the "30 to 45 minutes a chapter" estimate
  (how-to-use.md:10) is least true. Consider trimming Parts XII–XIII toward 6,000 and letting a few
  broad-scope chapters (30, 51, 54) run longer.
- **Total reading time.** No page states the cost of the whole book: A–E alone is about 58 chapters, roughly
  60 weeks of reading at the stated pace, plus projects and the capstone. Add one sentence on index.md.
- **Glossary entries** listed in P3: about ten entries, 600 words.

## What works well (keep)
- **The home page's "Where to start" table** (index.md:29–38): role, path, chapter count, and weeks in one
  place, with the same table repeated in the roadmaps. The roadmaps explain how the times are calculated and
  give a "why in this order" column for every step.
- **How-to-use's "If you are short of time" column** (how-to-use.md:18–35). It tells a busy reader exactly
  which sections to read and which to skim.
- **Honest handling of the case's non-linearity.** The "book order is not story order" warning, the "Northstar
  so far" box in 59 of 60 chapters (Ch 58 uses Halvard), and the reference-page table in how-to-use.md:81–86
  that says when to use the cast, timeline, briefing, and baseline.
- **The Northstar overview** (index.md) is a model case introduction: one table of company facts, one of
  people's wants, one of teams, a system list, and five numbered constraints. Fifteen minutes is realistic.
- **Baseline-data's "How the numbers were produced, and what is wrong with them"** table teaches data
  skepticism before any number is used.
- **Templates are usable without the book.** Each states owner and cadence, numbered steps, a field table
  plus YAML, "common mistakes", and review questions, and closes with evidence labels that separate research
  from the book's own recommendation. The 1:1, PIP, team charter, and new-manager 90-day plan are excellent
  on their own.
- **Projects make workload and standards explicit**: hours for full and core versions, numbered deliverables,
  a time rule, pass/fail acceptance criteria, a weighted rubric with excellent, adequate, and weak described,
  and a solution that shows other defensible answers.
- **Terminology discipline is high for the core vocabulary.** "Sev1", "skip-level", and "engineer-week" have
  no variants in the whole corpus. "One-on-one" is used in 60 files, and "1:1" only in the template title.
- **The ownership map works.** Topics touched in several chapters (succession, decision records,
  dependencies, risk registers) are cross-referenced to one owning chapter rather than re-taught.

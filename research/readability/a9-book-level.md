# Assessment: book as a whole (front matter and navigation, Northstar canon, templates and projects, book-level completeness, terminology)

Method: front matter, `mkdocs.yml` nav, the four Northstar pages, and the template and project indexes read in full. Templates read in full: engineering-quality-scorecard, technical-debt-register, incident-review, ninety-day-quality-plan, one-on-one, technology-investment-business-case, cto-competency-matrix (to the example), risk-register (to the template), plus the index. The other 12 were skimmed by heading structure. Projects read in full: P2. Read in part (framing, constraints, deliverables): P4, P5, P8. All 8 projects and solutions were checked by heading structure. Chapters were checked through `wc -w`, H3 headings, Case Study openings, and grep. They were not read in full.

## Scores

| Item | Words (approx.) | Readability | Clarity | Completeness | Northstar load | One-line verdict |
|---|---|---|---|---|---|---|
| 1. Front matter and navigation | 8,600 (curriculum.md 5,000) | 4 | 3 | 2 | 4 | Well written and short. But it has no glossary, no story timeline, no staff-plus path, and it says things about publication status that are out of date. |
| 2. Northstar canon (index, baseline, first-quarter, halvard) | 16,300 | 2 | 2 | 4 | 2 | `index.md` is good. The other pages are a continuity log built up wave by wave: out of order, mislabeled, with table cells up to 830 characters. |
| 3a. Templates (20) | 33,000 | 3 | 4 | 4 | 3 | Usable and honest. Two generations of templates differ in structure and length, and the examples carry canon provenance and arithmetic. |
| 3b. Projects (8) and solutions | 54,000 | 3 | 4 | 4 | 2 | Very consistent structure with rubrics. The workload is understated, and the "time rule" and canon framing are heavy going. |
| 4. Book-level completeness and progression | 337,000 (chapters) | 3 | 3 | 3 | 2 | The core is broad. The order of the story does not match the order of the book. Inclusion, the leader's own sustainability, ethics, managing up, and hiring at scale are missing or thin. Late chapters run 40% longer. |
| 5. Terminology consistency | n/a | 4 | 3 | 4 | 3 | Core terms are very consistent. The trouble is several capacity units with different rates, and a few names that are nearly the same for different things. |

## Top problems (most impact on the reader first)

### P1 (high) docs/case-studies/northstar/first-quarter.md:7 and chapters 4–18: the story's order is not the book's order
- What the reader experiences: someone reading front to back meets Northstar's quarter 2 in Parts I–IV, and only reaches quarter 1 (weeks 1–11) in Part V, chapters 19–27. Case Study openings bear this out. Ch 4, 5, 8–16 and 18 are set in quarter 2 "after the director's first 90 days". Ch 19–27 are set in weeks 2–11. From Chapter 3 on, early chapters lean on quarter 1 decisions that the reader has not seen yet.
- Example (ch03:440–441): "Two decisions recorded in the canon bear on this loop. Billing receives the largest share of the prevention allocation (25 percent) and two of the seven QA engineers." In Chapter 3 the reader does not know what a prevention allocation is, why QA engineers are moving, or what "the canon" means.
- Fix: (a) Add a one-page "Northstar at a glance" timeline (weeks 1–52 × the chapter set in each period) and put it on the Northstar index. (b) Open every Case Study with a two- or three-line "Story so far" box giving the week, who "you" are, and the one or two earlier decisions the case depends on, each linked. (c) Tell readers in how-to-use and in the roadmaps to read the Northstar overview and the Q1 summary (about 20 minutes) before Chapter 2.

### P2 (high) Book-wide: no glossary, and jargon used chapters before it is defined
- What the reader experiences: the target reader has no management or finance training, yet meets operational and finance shorthand long before the chapter that owns it. First uses: "tier 1" at ch05:466 (defined in Ch 24); "prevention allocation" at ch03:441 (Ch 27); "Sev1" at ch02:409 (Ch 25); "FTE" at ch15:215 (never defined in Parts I–IV); "FTE-quarters" at ch27:244; "skip-level" at ch06:345; "WIP" at ch03:182 (Ch 16).
- Example (ch02:409): "the same failure mode returned as INC-421, a Sev1 that a customer reported first."
- Fix: add `docs/glossary.md` (term list at the end of this report). Put it in the nav right after "How to use this book". Link each term at its first use in each Part. The `def_list` and `abbr` markdown extensions would also allow hover definitions.

### P3 (high) docs/case-studies/northstar/first-quarter.md:1, 107, 129, 206: mislabeled page, out of chronological order
- What the reader experiences: the page is titled "the director's first quarter" but covers all of year 1, the year-2 proposal, Part XII finances, risk, data and AI, board prep, and the Chapter 59 inventory (6,800 words). "Year 2 proposal (quarter 4)" (line 107) comes before "Quarter 2 results" (line 129). Facts are packed into table cells of up to 830 characters (lines 17, 30, 161–164, 190–203, 215–218, 229–231). Finding a single fact ("what was unplanned work in Q3?") means scanning several tables. Each section is labeled by the Part or chapter that added it ("Part XII facts", "Added when Part XII ... was written"), which is authoring history, not reader structure.
- Example (line 208): "Added when Part XII (Chapters 50–55) was written."
- Fix: split the page into `year-1-timeline.md` (one master table: week, event, chapter), `q1.md`, `q2.md`, `q3.md`, `q4.md` (each with decisions, results, open situations), and `company-finance-and-board.md` (the FY1 statements, board, risk, data facts). Put a "results by quarter" table (Sev1/2, availability, credits, unplanned %, tier 1 readiness for baseline through Q3) at the top of the timeline page. Replace long cells with bullet lists under sub-headings.

### P4 (high) docs/case-studies/northstar/baseline-data.md:141–352: extended baseline in authoring order, organized by chapter
- What the reader experiences: "Extended baseline by topic" runs Ch 20, 21, 22–23, 24, 25, 26, then 1–4, 15–18, 14, 5–13, 28–33, 34, 37–39. Headings name chapters, not topics, so a reader who wants "pay bands" or "hiring process" has to know which chapter added it. The page is 5,300 words with no table of contents of facts.
- Example (line 141): "These facts were added when Part V was written."
- Fix: reorder by topic in book order: People and management, Hiring and pay, Planning and delivery, Quality and pipeline, Reliability and incidents, Security, Architecture and platform, Organization and dependencies, Management system. Drop the chapter numbers from headings (keep a "Used in" line). Add a "where to find a fact" index at the top.

### P5 (medium) Book-wide: author vocabulary ("canon", provenance disclaimers) in reader-facing text
- What the reader experiences: "canon/canonical" appears about 250 times: 19 in templates, 84 in projects and solutions, 27 in Part XIII, 25 in the capstone, 21 in Part XII. Examples open with paragraphs on which facts are canon, which are illustrative, and which outcomes are "open". That is continuity management, not teaching.
- Example (one-on-one.md:136–139): "Every fact below is canon, from the baseline data, the first quarter page, and the case studies of Chapters 5 and 14. The layout of the entry, and Daniel's choice of what to write in it, are illustrative and written for this template; the canon leaves Daniel with a draft..."
- Fix: one book-wide rule. Examples carry only the "**Fictional.**" label and a link. "The canon" becomes "the case record" or is dropped. Provenance and "outcome open" notes go into an HTML comment or `research/`. P2's time-rule paragraph (p2:47–58) shrinks to two sentences.

### P6 (medium) docs/case-studies/northstar/index.md:35–60: no cast of characters
- What the reader experiences: the people table names 13 people. The chapters use about 35 more: Aisha Bello, Rafael Duarte, Mateo Arango Ríos, Hannah Lindgren, Tamsin Achterberg, Teodora Vasquez-Lund, Tomasz Wierzbicki, Sunil Varghese, Yusuf Demir, Bram Verhoeven, Keiko Ashworth, Joon Park, Marta Kowalczyk, six board members, Halvard's VPs, and others. They are scattered across baseline cells and chapter text. A reader who skipped a chapter cannot tell who Tomasz is.
- Fix: add a "Cast" page (name, role, team, location, first chapter, one-line arc), grouped by team, with Halvard in a separate section. Link names to it at first mention in each chapter.

### P7 (medium) docs/index.md:8–12, docs/learning-roadmaps.md:5–6, 83, docs/curriculum.md table: publication statements are out of date or contradictory
- What the reader experiences: the home page says chapters "are published one at a time" and "the site navigation shows only published material". In fact 0 chapters are published and all 60 are in the nav awaiting review. The roadmaps say "Chapter 27 and its templates are available now" (line 83) and that unpublished chapters are listed for completeness. The curriculum summary row reads "XIV ... templates | 0 of 0" even though 20 templates are live. The curriculum page opens with "0 of 60 chapters are published", which reads as if the book were empty.
- Fix: rewrite the home page box as "All 60 chapters are drafted and on the site; each carries a banner until a human reviewer has checked it." Delete roadmaps line 83 and the planned-chapter caveat. Fix the generator row for Part XIV ("20 of 20 templates").

### P8 (medium) docs/learning-roadmaps.md: path gaps and a mismatched project
- What the reader experiences: Path A (new EM) ends with Project 2, which casts the reader as Engineering Director and applies Chapter 56. Chapter 56 is not in Path A. No path includes Chapter 28 (architecture governance) or Chapter 29 (staff and principal engineers), although the home page names staff engineers as an audience. P7 relies on Chapters 29 and 38, which are not in Path C. No path tells the reader to read the Northstar overview first. Schedules are given per path, but no chapter states its reading time, and chapters run 5,000 to 8,250 words.
- Fix: add Path F (tech lead and staff-plus engineers: 1, 3, 4, 13, 28, 29, 30, 31, 32, 20, 46). Give Path A a project at EM scope, or tell Path A readers to read Ch 56 first. Add "Before you start: Northstar overview (15 min)" to every path. Show estimated reading minutes on each chapter's H1 line or in the curriculum.

### P9 (medium) mkdocs.yml nav: the case study is buried after Part V, and Halvard is unlinked
- What the reader experiences: "Case study: Northstar Technologies" sits between Part V and Part VI, but Chapter 2 already uses it. Halvard Systems (used in Ch 34–60) is not linked from the Northstar index, the home page, or how-to-use, so readers meet it cold in Chapter 34 or 35. Templates are listed in authoring-wave order (scorecard first, 1:1 seventeenth), not by role or task.
- Fix: move the case study section right after "Learning roadmaps". Add a Halvard paragraph and link to the Northstar index and to how-to-use. Order templates in the nav and index by role (EM: 1:1, career plan, team health, incident review; Director: ...; VP/CTO: ...).

### P10 (medium) docs/parts/12-*/ and 13-*/: late chapters are much longer and carry the most case detail
- What the reader experiences: chapters 1–49 sit in a tight band of 4,993–5,427 words (Ch 27 is 5,766). Chapters 50–60 average about 7,200 words: Ch 57 8,253, Ch 56 8,178, Ch 55 7,938, Ch 58 7,845, Ch 53 7,470, Ch 52 7,088. The extra length coincides with Q4 canon detail (weeks 40–51 drafts, positions, "outcome open").
- Fix: target 6,000 words or fewer for 52–59. Move week-by-week executive positions into the Q4 canon page and cite them in one line. Consider splitting Ch 58 (layoffs versus M&A are two topics) and Ch 57 (crisis versus executive disagreement versus resistance).

### P11 (medium) docs/templates/: two generations of templates, and an index that does not help choose
- What the reader experiences: the wave-1 templates (engineering-quality-scorecard 925 words, technical-debt-register 859, incident-review 800, ninety-day-quality-plan 821) are short. Three of them lack "How to fill it in". All four lack "Common mistakes" and/or "Review questions". The 90-day plan and debt register have no Cadence line. The other 16 run 1,370–2,990 words with a full structure (purpose, evidence paragraph, steps, table, YAML, example, mistakes, questions). The 1:1 template (2,037 words, three parts plus a 37-line YAML) is heavy for something a new EM copies on day one. The blank template starts at line 58–134, after evidence paragraphs.
- Fix: one skeleton for all templates: header, a one-paragraph purpose, the blank template, how to fill it in, the example, common mistakes, review questions, and evidence at the end. Bring the wave-1 four up to it. Give the heaviest (1:1, CTO matrix, ADR, risk register) a "minimum version" box at the top.

### P12 (medium) docs/templates/technology-investment-business-case.md:125–132, 202–212: arithmetic that buries the lesson
- What the reader experiences: the example prices effort at $185,000 ÷ 46 ≈ $4,000 per week and benefit at $185,000 ÷ 52 ≈ $3,558 per week. That is two rates for an "engineer-week" in one paragraph. The "What to notice" paragraph is about 170 words of chained NPV arithmetic and ends with a correction of a ratio in Chapter 21. The lesson (counted NPV is negative, so say so and name the uncounted value) is excellent but hard to find.
- Example (line 211–212): "Chapter 21's interest-to-principal ratio of 0.75 for TD-006 counts all 1.5 FTE; on the 1 FTE actually saved it is 0.5, the correction Chapter 32 makes."
- Fix: put the arithmetic in a three-row table (3-, 4-, and 5-year NPV; break-even). Cut the "What to notice" paragraph to its first two sentences plus the break-even. Delete the cross-chapter correction.

### P13 (medium) docs/projects/index.md:11 and each project's intro: workload understated, scope unbounded
- What the reader experiences: projects state 10–20 hours. But P4 asks for a document of about 12 pages with 9 deliverables, every number recomputed twice, and a spreadsheet. P8 asks for 10 deliverables and lists 7 chapters as prerequisites (Ch 52, 45, 49, 46, 48, 30, 38). For a working leader, 25–40 hours is more realistic. No project offers a smaller version.
- Fix: state the prerequisite reading separately ("assumes Chapters X, Y read"). Re-estimate the hours. Add a "core submission" (3–4 deliverables, about 6 hours) and an "extended submission" (all deliverables), so the rubric can be applied to either.

### P14 (low) Book-wide: too many capacity units, at different rates
- What the reader experiences: engineer-days (22 files), engineer-weeks (46), FTE, FTE-quarters (14), and engineer-years (16) appear together, priced at $800 a day (first-quarter.md:266), $3,558 a week (÷52), about $4,000 a week (÷46), and $185,000 a year, plus $157,250 as the capitalization rate. Readers have to convert between units in every finance passage.
- Fix: a glossary entry and one convention box (in Ch 45, repeated in the glossary): what each unit means, 1 FTE-quarter = 13 engineer-weeks, which rate applies to effort and which to benefit, and why.

### P15 (low) Terminology: near-identical names for different things, and a few stray variants
- What the reader experiences:
  - "change fail rate" (13 uses: ch18, ch23, ch25, ch38, ninety-day-quality-plan.md) against "change failure rate" (67 uses).
  - "postmortem" (29), "incident review" (40), and "blameless review" (19) for the same artifact. Ch 25's title says "Postmortems" but the template is "Incident review".
  - "operational review" (the director's weekly forum, Ch 27/37) and "operations review" (Payments and Integrations' team practice, ch11:411) are different things with nearly the same name.
  - "scorecard" means a hiring scorecard in Ch 7 (19 uses) and a quality or organization scorecard elsewhere.
  - "decision log" (organization, Ch 39) and "decision record" (ADR, Ch 28) are distinct concepts with near-identical names. Ch 13's "Recording decisions" adds a third.
  - "QA engineers" becomes "quality engineers" at week 10. This is correct, but the change is never flagged to a reader who comes in at a later chapter.
  - Strays: "Sev1-2" and "Sev1/Sev2" (one each), "T1" (3), "MTTR" (1).
- Fix: standardize on "change failure rate". Use "incident review" as the artifact name and "blameless" as the adjective, and keep "postmortem" only when quoting sources. Rename the Payments practice "team operations huddle" (or similar). Use "hiring scorecard" in Ch 7. Add glossary entries that separate decision log, decision record (ADR), and decision rights.

## Patterns across your scope

- **The canon written as a log, not a reference.** Northstar pages, template examples, and project framings record when and by which wave a fact was added, and whether an outcome is "open". Book-wide rule: reader-facing pages are organized by time (story) or by topic (facts), never by authoring wave. Provenance goes to `research/`.
- **"You" is always the director.** From Ch 2 on, case studies are told from the director's chair, even in the EM chapters: Ch 5 reviews Daniel Cho's one-on-ones; Ch 9 has Tom Becker's plan reviewed. A Path A reader watches managers instead of practicing being one. Rule: in Parts II–IV, frame at least one exercise and the Case Study's question from the manager's seat (Priya, Daniel, Marcus).
- **Director content before the director chapter.** Part V (Ch 19–27) runs the director's mandate, capacity trade, and operating rhythm. Part IX (Ch 40, "The Director's Job") comes 13 chapters later and partly re-explains it (Ch 40's "Quality as an organizational property" against Ch 19 and 27). Rule: Part V's opener points to Ch 40's mental model in one paragraph, or Ch 40 moves ahead of Part V in Path B and is cross-linked.
- **The same mechanism taught in several places.** Worth checking that later chapters cross-reference rather than re-teach:
  - decision records: Ch 13 "Recording decisions", Ch 28 ADRs, Ch 39 decision log.
  - decision rights: Ch 12, 13, 28, 50.
  - succession: Ch 36 "Succession coverage", Ch 41 "Building the bench", Ch 47 "Staffing the director team", Ch 49 "Successors as part of the program", plus a template and P6.
  - information distortion upward: Ch 39 "Why bad news travels slowly" and Ch 40 "How information degrades on the way up".
  - risk registers: Ch 30 and Ch 53.
  - portfolio: Ch 42 "portfolio as a queue" and Ch 47 "portfolio as an allocation problem"; CD3 in Ch 15 and Ch 45.
  - turnaround: Ch 14 "Coaching, restructuring, or leadership change" and Ch 56 "Keep, coach, move, or replace".
  - change: Ch 27, 43, 49, 57, 59.
  - metric pairing and gaming: Ch 18 (owner), 19, 20, 26, 27, 29, 32, 38.
  - capacity allocation: Ch 27, 38, 48, 59.
  Rule: the ownership map in CLAUDE.md section 9 should be extended to these topics and enforced the same way.
- **Arithmetic in prose.** It appears in template examples (business case), canon cells, and late chapters. Rule: any calculation with more than two operations goes in a table, and the prose states only the conclusion.
- **Length creep.** Templates (800 → 3,000 words) and chapters (5,200 → 8,250) grew with later waves. Rule: set length caps per artifact type and enforce them in `validate_book.py`.

## Missing or thin content

- **Glossary** (high): none exists. Put it in `docs/glossary.md`, with nav after "How to use". About 2,500 words. Proposed 55 terms, grouped:
  - *Money and business:* ARR; churn and renewal; gross margin; operating expense (opex) vs capital expense; fully loaded cost; capitalized vs expensed software (ASC 350-40); EBITDA; deferred revenue; NPV; discount/hurdle rate; payback; cost of delay; CD3 / WSJF; opportunity cost and sunk cost; service credits; business case.
  - *Capacity:* FTE; FTE-quarter; engineer-week / engineer-day / engineer-year; capacity model; planned vs cautious case; unplanned work; prevention allocation; WIP and WIP limit; Little's law.
  - *Delivery and quality:* DORA four keys (deployment frequency, lead time for changes, change failure rate, time to restore); SPACE; DevEx; release train; trunk-based development; feature flag (deploy vs release); contract test; flaky test; escaped defect; technical debt (principal, interest); paved road.
  - *Reliability and incidents:* Sev1/Sev2/Sev3; tier 1 / tier 2 and the operational minimums; SLI / SLO / SLA; error budget; incident commander; incident review (blameless); recurrence; corrective action; customer-detected share.
  - *Security and risk:* SBOM; SSDF; SLSA; known-exploited vulnerability; risk register; risk appetite; SOC 2; audit committee.
  - *People and organization:* span of control; layer; skip-level; calibration; level/ladder; staff-plus archetypes; structured interview and work sample; hiring scorecard; stay interview; psychological safety; Conway's law / reverse Conway; team types (stream-aligned, platform, enabling, complicated-subsystem); cognitive load; decision rights; decision log vs ADR; RACI; escalation path; OKR; operating review vs operational review; succession coverage (ready-now, interim cover).
- **Northstar navigation aids** (high): a year-1 timeline (weeks × events × chapters), a results-by-quarter table, a cast page, and a "Story so far" box per Case Study. Northstar pages plus about 60 boxes of 2–3 lines.
- **Inclusion and equity** (medium-high): "diversity" appears once (Ch 11), "gender" only in Ch 8's pay-equity section, "inclusion" once in another sense. There is nothing on inclusive hiring and sourcing, bias in calibration beyond Ch 8, underrepresented engineers' promotion rates, accommodations, or building inclusive distributed teams. Where: sections in Ch 7, 8, 11, 14, and 48, or one new chapter in Part II or III. About 3,000–5,000 words.
- **The leader's own sustainability** (medium): "burnout" appears in passing only (Ch 5, 9, 18). There is nothing on the leader's load, isolation, decision fatigue, building a peer network, or using a coach or mentor. Where: a section in Ch 2 (EM), Ch 40 (director calendar), and Ch 50 (CTO), or a short Part I chapter. About 1,500–2,500 words.
- **Managing up at EM level** (medium): "your own manager" appears only in Ch 46. The director-to-CTO relationship is covered (Ch 39, 46, 49), but an EM learning to work with their manager (expectations, bad news, asking for help, disagreeing) is absent. Where: Ch 2 or Ch 4. About 1,200 words.
- **Ethics** (medium): one mention (Ch 38). Missing: pressure to present misleading numbers (the board headline dispute in Ch 55 is a natural case), responsibilities when asked to ship something unsafe, fairness in reductions, AI and data ethics, and when to escalate outside the chain. Where: Ch 57 (executive disagreement), Ch 54, Ch 58. About 1,500 words in total.
- **AI in day-to-day management** (medium): AI is concentrated in Ch 54 (CTO strategy) and a mention in Ch 18. Missing at EM and director level: interviewing when candidates use assistants (Ch 7), assessing performance and promotion evidence when code is AI-assisted (Ch 8, 9), the junior pipeline and level mix (Ch 48), team norms (Ch 12). About 400–600 words in each of those chapters.
- **Hiring at scale and onboarding** (medium): Ch 7 is team-level selection and Ch 48 is the workforce plan. No H3 anywhere covers recruiting operations (funnel, sourcing, recruiter partnership, employer brand, interviewer training load) or onboarding engineers and new managers, although "onboarding" appears in 12 chapters. Where: a section in Ch 7 or Ch 48, plus a section in Ch 12 or Ch 36. About 2,000 words.
- **International teams and employment context** (low): Ch 6 "Feedback across cultures", Ch 14 distributed teams, and time zones in 3 chapters. Employment law appears in Ch 7, 9, 58. This is adequate but thin for working across countries (works councils, notice regimes, pay bands by market beyond Bogotá). Where: Ch 14 and Ch 58 sidebars. About 800 words.
- **Leader's career moves** (low): evaluating and interviewing for a director, VP, or CTO role, negotiating one's own offer, and leaving a role well. Where: Ch 4 or Ch 50. About 1,000 words.
- **Missing templates** (medium): a hiring scorecard and interview kit (Ch 7), an expectations or improvement plan (Ch 9; Tom Becker's plan for Bram Verhoeven is the obvious example), a team charter and working agreement (Ch 12), a new-manager 90-day plan (Ch 2), a reorganization communication plan (Ch 36), and a reduction checklist (Ch 58). Each 800–1,500 words.
- **VP part thin relative to its role in the subtitle** (low): 3 chapters (47–49), and Northstar has no VP, so the VP job is shown mostly through Halvard. Consider a VP-seat exercise set or one more chapter (managing directors through the first year).

## What works well (keep)

- **The uniform 16-section chapter contract** and how-to-use's "If you are short of time" column. A reader can always find the playbook, the exercises, and the takeaways.
- **The evidence labels page.** It is clear, short, and states how much weight to give each label and what each access level means. It is a real differentiator; link it from every chapter's first labeled claim.
- **The learning roadmaps' format**: who the path is for, prerequisites, ordered chapters with a "why in this order" column, a schedule, and Path E's "If you need to… go to" table.
- **Northstar `index.md`.** It is concise (1,500 words), and the company, people, team table, system, situation, and five binding constraints are exactly what a reader needs. Keep it as the entry point and model the other pages on it.
- **baseline-data.md's "How the numbers were produced, and what is wrong with them" table.** It teaches data skepticism by example.
- **Core terminology discipline.** "Sev1" (261 uses, no SEV-1 or P1 variants), lowercase "tier 1", "unplanned work", "engineer-weeks", "skip-level", and "one-on-one" (1:1 only in the template name) are uniform across 60 chapters.
- **The templates' later standard**: Used in / Owner / Cadence header, claims labeled by evidence, "Common mistakes", "Review questions", a YAML block, and examples that leave decisions open. The business case's honest negative NPV and the scorecard's "Paired with / Gaming risk and audit" columns are exemplary. The incident review is short enough to use tomorrow.
- **Project design.** All 8 projects share the same 9 sections, the time rule, binding constraints, pass/fail acceptance criteria, and a weighted rubric with excellent, adequate, and weak descriptors. Solutions include "other defensible answers" and "what a weak submission looks like". P2's competing-hypotheses-with-disconfirming-evidence structure is a model.

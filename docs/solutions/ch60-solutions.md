# Chapter 60 solutions — Capstone: Transforming Northstar Technologies

Worked solutions for the [chapter 60 exercises](../parts/15-capstone/60-capstone-northstar.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer, the
criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional. Where an exercise is hypothetical, its consequences are judgments, not canon facts, and the
canon still records no outcome for any quarter 4 decision.

## F1 — The first ten register entries

| Entry | Relied on by |
|---|---|
| Severity definitions based on customer impact, with the baseline re-rated under them and the original ratings kept | Stages 3, 5, 10 |
| Tier 1 population: the 15 components on the order or payment path, frozen for year-1 comparisons | Stages 2, 3, 10 |
| Period length: the baseline is a 90-day quarter, the director's quarters are 13 weeks (91 days); availability allowances per period | Stages 3, 10 |
| Change failure rate: failures within 72 hours per release, and what counts as a release when cadence changes | Stages 3, 10 |
| Customer-detected share: first detection by a customer, over all Sev1 and Sev2 | Stage 3 |
| Recurrence: a failure mode already reviewed once | Stages 3, 5 |
| Unplanned work: the two-week sample, its four categories, and who classifies | Stages 6, 7, 8 |
| Availability: the synthetic probe, its single region, and the uncovered mobile path | Stages 3, 10 |
| Ownership rule: every component exactly once; exemptions at most two quarters, each with an owner of its expiry | Stages 2, 7 |
| Prevention allocation with a step-down rule | Stages 6, 7, 8, 9 |

**Most likely to need revision, with bridges.** The change failure rate, because moving Core from
fortnightly to weekly releases changes the denominator: report the old and new definitions side by side
for the first quarter after the change, and never pool releases of different cadence in one rate. The
tier 1 list, because ownership decisions move components between tiers: freeze the year-1 list for
year-1 comparisons and start a new series at the year boundary. Availability, because extending the probe
to the mobile path will lower the number: run old and new probes in parallel for one quarter and report
both.

A good answer writes definitions, not targets, and ties each to a later stage. The weak answer lists
goals ("halve incidents") or copies the week-3 definitions from the first-quarter page, which the time
rule keeps closed until the hinge.

## F2 — Sorting facts by stage

| Fact | Story date | Earliest stage |
|---|---|---|
| Orders knowledge table | Week 14 | After the hinge (stages 7 to 10) |
| Baseline co-change pairs | Baseline quarter | Stage 1 |
| 7,800 corrected orders | Week 40 | Stages 7 to 10 |
| Bogotá cost of about $110,000 | Quarter 4 | Stages 7 to 10 |
| Security questionnaire asking for an SBOM | Week 3 | After the hinge under the capstone rule |
| Finance's FY1 latest estimate | Week 46 | Stages 7 to 10 |
| Billing ledger knowledge table | Start of quarter 2 (describes the baseline) | After the hinge; stage 1 may state the gap it would reveal only as an assumption |
| document-store gap in the week-44 proposal | Week 44 | Stages 7 to 10 |

Three entries need care. The Orders knowledge table sits on the baseline page but is dated week 14, and
the Billing ledger knowledge map, also on the baseline page, was built at the start of quarter 2; a week-4
ownership decision that cites "only two Orders engineers can change core/customer safely" looks
prescient and teaches nothing. The questionnaire is a week-3 event in the story, so a director could in
principle know it before the week-4 plan, but it lives on the first-quarter page, which the capstone keeps
closed so that your stage 1 to 6 choices are yours. A defensible answer treats it as an assumption ("a
renewal customer may ask for supply-chain evidence") rather than a fact.

The clearest misuse is a stage 3 scorecard with a corrected-order row and a 1.3 percent baseline. It
would read as foresight; in the story, correctness had no measure until Data and Analytics defined one in
week 40. The good stage 3 answer instead names invoice and order correctness as unmeasured rows. The weak
answer sorts by which page a fact appears on rather than by its date.

## F3 — Lending the extra half FTE

At $46,250 per FTE-quarter: 12 FTE costs $555,000 a quarter, 8 FTE $370,000, 6 FTE $277,500, 5 FTE
$231,250, and the draft's 5.5 FTE $254,375. Over year 2 the continuation's 6 + 6 + 5 + 5 = 22 FTE-quarters
($1,017,500) matches 5.5 × 4, but in quarters 5 and 6 it needs 0.5 FTE more than the draft gives prevention,
and in quarters 7 and 8 it needs 0.5 FTE less.

**Who lends.** One defensible answer is horizon 2, for the same reason the week-48 stress rule makes it the
shock absorber: it holds options rather than commitments to today's customers. Horizon 2 then runs at 9.5
FTE in quarters 5 and 6 and 10.5 in quarters 7 and 8, averaging the draft's 10.0. Borrowing from estate
currency (2.0) instead cuts a quarter of that line for half a year and delays the work the estate risks need;
borrowing from product for today's customers puts the loan on Amara Okafor's roadmap directly.

**Amara's condition.** A fixed allocation per stage fixes the loan too: stage 2 plans horizon 2 at 9.5 and
stage 3 at 10.5, written down in advance. That is a gain in predictability, but it removes horizon 2's
freedom to flex within a stage while the stress rule still takes overruns from it. At 25 percent unplanned
work on 79 engineers, quarters 5 and 6 would leave horizon 2 at 9.5 − 2.35 = 7.15 FTE. The answer should say
that the fixed figure is the plan, and that overruns are reported against it, not hidden by re-planning.

**Two misreadable sentences.** "Prevention falls from 12 FTE to 5.5" reads as a program being wound down,
or as a 54 percent saving that can be spent on features; in fact the step-down is meant to follow evidence
that capability holds. "Prevention costs $254,375 a quarter" reads as new money; it is the time of existing
engineers inside flat headcount. The weak answer repeats the example's annual reconciliation and never
names a lender.

## A1 — Assigning core/permissions in week 4

**For Orders, on week-4 facts.** Orders made 17 of the 38 baseline changes, the most of any team.
customer and permissions are the strongest co-change pair in Core (67 percent of the smaller module's
requests), and core/customer was going to Orders in the same week, so splitting the pair across owners
creates a boundary where change does not respect one. **Against.** Orders was carrying the bulk-ordering
renewal commitment with 5 of its 14 engineers and a first-year manager who still spent 18 hours a week on
code and review; adding a tier 1 module with no alerts or on-call raises the risk to the week-26 date.
Platform Operations had the adjacency to auth-svc but no engineer who had changed Core code.

**Plausible consequences by week 44 (judgments, not canon).** The quarter 2 permissions extraction led
by Ines Carvalho would have had an owning team to land in, rather than an exemption. The exemption would
not have lapsed at week 39, and the year-2 proposal would not have been the first document to resolve the
question. Orders would have needed an on-call rotation and alerts for the module, adding to Priya Raman's
load during bulk ordering, while her hands-on time rose from 8 to 10 to 12 hours a week, against a cap of
8, at the week 16, 20, and 24 checks. The tier 1 readiness count might have moved earlier or later; the canon does not say which two of
the 15 still missed the minimums at quarter 3, so any claim about the count is an assumption.

A good answer separates the week-4 argument from the hindsight trace and labels every consequence. The
weak answer states canon outcomes for a hypothetical, or argues only from the week-26 risk without the
co-change evidence.

## A2 — The measurement note for Margaret Lin

**Sev1 and Sev2 incidents (30, 21, 17, 14).** The baseline's 30 were rated before written definitions;
under the week-3 definitions they would be 9 Sev1 and 21 Sev2 rather than 7 and 23, and the total is
unchanged. Since week 7 a weekly severity audit checks ratings against the definitions. Conclude: the total
is comparable across all four quarters; the Sev1 split is not, unless the re-rated baseline is used.

**Core change failure rate (31, 22, 23 percent).** The baseline counts 4 of 13 fortnightly releases over 26
weeks; quarter 1 counts 2 of the 9 weekly releases from week 5 and excludes the two fortnightly releases of
weeks 1 to 4; quarter 2 counts 3 of 13. Failures are linked by hand, so the true rate may be higher.
Conclude: releases are smaller and no safer since quarter 1; the counts are too small for a trend.
Quarter 3's rate is not recorded; the note says so rather than carrying 23 percent forward.

**Tier 1 readiness (3, 8, 11, 13 of 15).** Counted against the four operational minimums on the original
list of 15 for all of year 1; year 2 will report against the current 14, after notification-svc moved to
tier 2. The fifth minimum, an auditable pipeline with automated rollback, is tracked separately. Conclude:
real progress on presence of the minimums; a runbook drill would show whether they work.

**Availability (99.62 percent, not recorded, 99.86, 99.89).** A synthetic probe from one region that does
not cover the mobile path. The baseline quarter is 90 days; the director's quarters are 91 days, where 99.9
percent allows about 131 minutes and quarter 3 had about 144. Quarter 1 was not recorded. Conclude: below
contract in every measured quarter, narrowly in quarter 3, with the mobile path unmeasured.

A good note states the gap in quarter 1 availability rather than hiding it. The weak note presents four
clean trend lines.

## A3 — From the debt register to quarter 4

| Entry | Quarter 4 status |
|---|---|
| TD-001 Core release process | Reduced: weekly releases from week 5; manual regression about 600 cases in a day at day 90 |
| TD-002 shell-script deploys | Partly open: CI consolidation phase 1 was on the quarter 2 platform roadmap, but in week 44 two script services still kept secrets in plain files, and auth-svc's known-exploited critical sits under an exception "until the migration" |
| TD-003 shared modules | core/customer and core/scheduler owned from week 4; core/permissions open until the year-2 proposal |
| TD-004 migration practice | Reduced: the pipeline check landed in week 11 |
| TD-005 webhook versioning | Not recorded in the canon; a good answer says so rather than guessing |

**Core framework migration (TR-01).** The canon gives cost scenarios of 120, 190, and 243 engineer-days
($96,000, $152,000, $194,400), expensed, and one open Core critical waiting on it. It gives no interest
figure: no incidents are attributed to the framework. Stage 8 must state an assumption about exposure
(for example, the chance of a critical with no patch in a year) and its break-even.

**CI consolidation.** Four CI systems cost about 1.5 FTE a year against about 0.5 for one, so the interest
is about 1.0 FTE, roughly $185,000 a year, derived from canon. The target choice (DL-10) is open; the
continuation releases $100,000 only if a target is chosen, at the week-78 gate.

**ADR-0001.** Interest the canon supports: 7 of quarter 3's 11 failed or partial warehouse loads traced to
Core schema changes, which is the same coupling to tables. Attributing the two days a month of manual
revenue reconciliation to it would be a judgment.

**What the week-4 register should have recorded:** interest in time units for each entry, the owner of the
decision as well as of the code, and a trigger date. The weak answer prices principal only.

## A4 — The hinge review

| Commitment | Reasonable then? | Status at week 40 |
|---|---|---|
| Week-3 severity definitions | Yes | Honored and strengthened in writing: the week-7 creative ratings led to the weekly severity audit; the baseline re-rating was bridged |
| Tier 1 list of 15 | Yes | Bridged: year-1 counts keep 15, year-2 reports use 14 |
| Quarter 1 prevention allocation | Yes | Revised in writing to 8 FTE in quarter 3; the canon records no step-down rule tying the reduction to evidence |
| QA engineers into product teams | Yes | Honored, announced in week 10, later than it should have been |
| No decision-rights map | Unclear; nothing was decided | Orphaned: the week-14 remark on ADR-0001 filled the gap until Victor reversed it in week 47 |

**The migration check, judged apart from its outcome.** In the baseline, three incidents were triggered by
database migrations, and migrations were tested against an empty schema only. The check was promised after
INC-427 and scheduled for week 7. Was relying on the tool alone reasonable on week-3 information? A strong
answer argues not: an interim rule that no release carries a ledger migration with code that depends on it
cost almost nothing and was available in week 3, yet it was adopted only after the week-9 Sev1. That
judgment would hold even if no incident had occurred. The information that would have changed the decision
is already in the baseline: the migration-triggered incidents and the recurrences in Billing.

A good review also names one decision that worked partly by luck; reasonable candidates are hard to prove
from the canon, so the answer should say what evidence would distinguish luck from skill. The weak review
grades every decision by its result.

## X1 — One year-2 envelope at three seat counts

**The week-46 decision.** This answer assumes it was deferred to week 48 alongside the VP question,
because both change the seat count; under the main proposal the 79 column applies. An answer that assumes
the decision was made states which column follows and keeps the others as contingencies.

Apply the stress rule from the week 48 premortem consistently: a lost seat, like an unplanned-work overrun, comes out of horizon 2,
never prevention or horizon 3. This is one defensible position.

| Line (FTE) | 80 engineers | 79 (draft) | 78 (VP takes a seat) |
|---|---|---|---|
| Unplanned work, 22% | 17.6 | 17.4 | 17.2 |
| Prevention | 5.5 | 5.5 | 5.5 |
| Platform | 4.5 | 4.5 | 4.5 |
| Estate currency | 2.0 | 2.0 | 2.0 |
| Product for today's customers | 37.6 | 37.6 | 37.6 |
| Horizon 3 | 2.0 | 2.0 | 2.0 |
| Horizon 2 (remainder) | 10.8 | 10.0 | 9.2 |

Checks: 80 − 69.2 = 10.8; 79 − 69.0 = 10.0; 78 − 68.8 = 9.2. At quarter 3's actual 25 percent, unplanned
work is 20.0, 19.75, and 19.5, overruns of 2.4, 2.35, and 2.3, leaving horizon 2 at 8.4, 7.65, and 6.9. If 77 becomes possible (alternative D, or C with a VP), unplanned
work is about 16.9, horizon 2 is 77 − 68.5 = 8.5, and an overrun of about 2.35 leaves about 6.2; the
answer should say whether horizon 2 can absorb a fourth seat or product for today's customers must.

**Documents that must change.** The continuation states that its quarterly 6, 6, 5, 5 averages 5.5 and names
which line lends 0.5 FTE in quarters 5 and 6. The board page's capacity line shows horizon 2 as the shock
absorber, so a bad quarter is not read as a broken roadmap promise to Amara Okafor. The investment package
fits this table. Each author is told in writing, and the envelope enters the decision log.

**Not decided this week:** the organization decision, if your assumption is that it was deferred; the VP
recommendation (due this week, and taken as a position, not a canon outcome); ADR-0001 (proposed for week 60), the CI
target (week 78), the SOC 2 option, and the auth-svc exception (before week 50). The weak answer picks one
seat count and leaves the others to "later".

## X2 — The board page

| Director | Concern | Year-1 artifact that answers it |
|---|---|---|
| Anders Holm | Dependence on a few people | Stage 5: incident commanders, standard owners, staff engineer mandates; the week-44 succession table (10 critical roles, none ready now, 6 interim, 4 none) |
| Natalie Brooks | A buyer's diligence | Stages 4 and 9: the debt and risk registers; unsupported Core framework, no SOC 2 report, auth-svc's exception, signed provenance on 0 of 15 tier 1 components |
| Samuel Osei | Flat headcount and the roadmap | Stages 6 and 7: unplanned work 34 to 25 percent, 7.2 FTE returned, one envelope with horizon 2 as buffer |
| Margaret Lin | Measures mean the same thing | Stages 1 and 3: counting rules and bridges (exercise A2) |
| David Ferrante | Payment path, availability miss, framework | Stage 3's SLOs and availability definition; stage 4's TR-01 entry; stage 9's policy on money data |

**Headline.** One defensible choice is the director's counter: at most 40 Sev1 and Sev2 over year 2 as a
rolling four-quarter total, reported with the severity audit, 99.9 percent every quarter, and a reopening
trigger at two consecutive quarters above 12. The reasoning: at counts near 10, quarter-to-quarter noise
can break a per-quarter threshold of "below 10" without any real change (an assumption about count
variability, not a canon fact), and a rolling total pairs naturally with the audit Margaret Lin will ask
about. Choosing Victor's headline is also defensible if the page states that a single quarter above 10 will
be explained, not hidden.

**David Ferrante's offer.** Accept it as input, through the chair, as a scoped session with the staff
engineers on a written pre-read, so a director does not become a shadow decision maker. The weak answer
picks a headline without mapping the concerns, or records what the board decided.

## X3 — The one week-4 commitment to change

One strong answer changes stage 5: a decision-rights map with a CTO lane and a rule that every open
decision and every exemption has an owner of its next step and a date in the decision cadence.

**Knowable in week 4?** Yes. The baseline records no decision records anywhere, decisions made "by Victor
Lindqvist in unrecorded conversations", disputes reaching him in conversation, and three Core modules
changed by four teams and owned by none. Nothing about the choice depends on later events.

**Effect on stage 9 (hypothetical).** ADR-0001 would have had a decider in week 14. If the contract
option had been chosen, it cost 5 of Billing's 6 reserved engineer-weeks, about 5 × $3,558 = $17,790 of
capacity, and was ready by week 19, the same date as reading the tables. Victor's week-47 policy would then
confirm a decision rather than reverse a remark, and the ledger posting events option would rest on a
decided base.

**Effect on stage 2 and stage 10 (hypothetical).** The core/permissions exemption would have had an owner
of its expiry, so it could not lapse silently at week 39, and Anders Holm's question would meet a record
showing who decides what.

**Why not simply the worst outcome?** The week-9 Billing Sev1 was the most visible failure, but changing
"the migration check" after the fact rewards hindsight. The decision-rights gap is chosen because it was
visible in week 4 and touches the most threads. The weak answer picks whatever went worst.

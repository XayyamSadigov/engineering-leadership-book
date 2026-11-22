# Project 7: Design a 12-Month Engineering Strategy

It is weeks 46 to 48, late in quarter 4 of your first year as Engineering Director at Northstar
Technologies, the fictional company of the [case study](../case-studies/northstar/index.md). The
twelve-month mandate ends with this quarter. Quarter 3, the latest measured quarter, came in at 14 Sev1
and Sev2 incidents (the first quarter at or below the mandate's 15), 99.89 percent availability on the
contractual paths (about 13 minutes short of the 99.9 percent commitment), $60,000 of service credits,
and unplanned work at 25 percent. Year 2 (quarters 5 to 8, weeks 53 to 104) is being decided one document
at a time: the year-2 organization proposal, the engineering page of the board plan, the VP question, the
quality continuation, the workforce plan. Above them, Victor Lindqvist (CTO) is drafting a three-year
technology strategy: in week 47 he sorts technology into excellent, adequate, buy, and not doing, sets four
policies, and asks you for its year-2 inputs. Each of these is a reasonable document. None of them says what
engineering will do in year 2 under Victor's direction, or why the year-2 pieces add up. Your job in this
project is to write that document for him: a 12-month engineering strategy, the year-2 layer beneath his
draft, that the other year-2 decisions can be tested against.

The project applies [Chapter 51](../parts/12-cto-leadership/51-enterprise-technology-strategy.md), which shows how a CTO derives technology strategy from business
strategy and lays out a multi-year roadmap; this project is the 12-month engineering layer beneath it. It also
uses [Chapter 30](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md) for
the strategy kernel and the week-14 strategy draft,
[Chapter 29](../parts/06-technical-leadership/29-staff-and-principal-engineers.md) for staff engineers as
owners of policies, [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
for capacity allocation, and Chapters
[45](../parts/10-business-leadership/45-business-models-and-engineering-economics.md) to
[49](../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md) for
economics, negotiation, the VP question, workforce and governance, and staged transformation. The
templates are the [engineering strategy](../templates/engineering-strategy.md), the
[capacity planning model](../templates/capacity-planning-model.md), the
[quarterly engineering review](../templates/quarterly-engineering-review.md), and the
[executive update](../templates/executive-update.md). It takes about 14 to 20 hours.

## Problem Statement

Northstar has had a written technical strategy since week 14. The draft in
[Chapter 30](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md) and the
[template example](../templates/engineering-strategy.md#example-northstar-week-14-draft) diagnosed three
problems (change is unsafe, the estate ages unwatched, knowledge is concentrated) and set three guiding
policies, each tested against a decision waiting in the decision log: the CI consolidation target (DL-10),
the tax-svc build, buy, or hybrid choice (DL-09), and the Core framework migration (TR-01). By week 47 the
canon records none of the three as decided. The diagnosis was sound; the policies decided nothing.

The situation has also moved. Incidents have more than halved, so the argument that funded prevention in
year 1 (outages and credits) is weaker, and Greg Tanaka (VP Sales) argues that the prevention engineers
should move to deal features. The customer harm that is now most visible is correctness: in week 40 a
top-40 distributor complained about time spent correcting orders, and Data and Analytics found 7,800
corrected orders in the last 28 days of quarter 3, 1.3 percent of submissions. Six of the 40 largest
customers renew in quarters 5 to 8. Year 2 may bring a new team structure, a VP above the director, and
less prevention capacity, all inside the same 87 seats.

A year-2 strategy therefore has four jobs. It must diagnose today rather than week 14. It must choose where
engineering will be excellent and where adequate is enough (the kind of explicit choice
[Lafley and Martin, 2013](../references/bibliography.md#lafley2013playing) are known for asking of a
business, applied here to an engineering organization; **expert opinion**). It must set a few policies
that decide the open questions the same way every time. And it must fund its actions inside flat
headcount, holding whatever Victor Lindqvist and the executive team decide on the items still open.

Your task is to write the strategy: a diagnosis of no more than three findings, two to four guiding
policies, coherent actions by quarter with owners and dates, a capacity envelope, what engineering will
not do, review triggers, and a short scorecard; plus a one-page summary for Victor and an evaluation of
the week-14 draft against what happened to it.

## Scenario and Constraints

**Your position.** Engineering Director, drafting CTO-level work for Victor Lindqvist, who approves it.
The three staff engineers (Ines Carvalho, Kwame Mensah, Li Na Zhou) are co-authors. The managers, Amara
Okafor (CPO), and Rajiv Menon (CFO) read it before Victor does. The executive team meets in week 49 and
the board in week 50.

**The time rule.** Use facts dated week 47 or earlier: the quarter 3 results, the week-40 corrected-order
analysis, the week-42 draft counter for the board page, the week-44 organization proposal, the week-45
continuation proposal, the executives' positions from weeks 46 and 47, Helena Marsh's week 46 confirmation
of the business choices, Victor Lindqvist's week 47 three-year strategy draft
([Chapter 51's case study](../parts/12-cto-leadership/51-enterprise-technology-strategy.md#case-study)), and Finance's week 46 latest estimate for fiscal year 1
([Chapter 52](../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md)).
Quarter 4 results do not exist yet. Victor's week 48 premortem and the week 49 executive meeting are after
the time rule. The canon records no outcome for any decision due in weeks 46 to 51; treat each as open.

**Constraints.** These are binding.

1. **The kernel, and short.** No more than three findings and two to four guiding policies. At most about
   six pages, plus the one-page summary.
2. **Flat headcount.** 87 seats for the whole engineering organization; backfills allowed, no net
   additions, no headcount request (Victor will not take one to the board). State the seat count you plan
   on: 80 engineers today, 79 under the main organization proposal, 78 if a VP takes a seat.
3. **No Core rewrite** (constraint 3 on the [Northstar overview](../case-studies/northstar/index.md)).
4. **Open decisions stay open.** The year-2 organization, the VP question, the continuation (6 FTE, or 4
   FTE plus two engineers on deal features), the workforce plan, the week 34 portfolio forum, the CI
   target, ADR-0001, tax-svc, and the board's envelope. You may recommend; you must show how the strategy
   changes under each outcome you consider plausible.
5. **No new cash assumed.** The $150,000 of tooling in the continuation needs Rajiv Menon's approval with an
   offset in the $4.2M cloud and tooling budget. The strategy must work if it is declined.
6. **Owners who are not you.** Every guiding policy has a named owner who decides exceptions within a stated
   time. The director may own at most one.
7. **Consistent with the board page and Victor's draft.** The strategy either fits the director's week-42
   draft counter and Victor's week 47 draft or says
   where it departs and why.

## Starting Dataset

Use these sources:

- [Northstar overview](../case-studies/northstar/index.md), including "Executive and board context (Part
  XII)"; [baseline data](../case-studies/northstar/baseline-data.md), especially the extended baseline on
  architecture, estate, and people; and [the first quarter](../case-studies/northstar/first-quarter.md),
  especially the year 2 proposal, "Quarter 3 results", "Quarter 4", and "Part XII facts (quarter 4)" for
  Victor's week 47 draft (four groups, four policies, draft allocation, options and decision weeks) and
  Finance's fiscal year 1 figures.
- The week-14 strategy draft and the technology risk register TR-01 to TR-09 in
  [Chapter 30](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md), and the
  [engineering strategy template](../templates/engineering-strategy.md) with its example.
- [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
  for the quarter 3 capacity plan; [Chapter 45](../parts/10-business-leadership/45-business-models-and-engineering-economics.md)
  for the economic assumptions; [Chapter 46](../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md#case-study)
  for the board page and the draft counter; [Chapter 47](../parts/11-vp-engineering/47-the-vp-of-engineering.md#case-study)
  for the VP options; [Chapter 48](../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md)
  for workforce and governance; [Chapter 49](../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md#case-study)
  for the continuation and the executives' positions.

**Project data.** Two files, both **derived from the canon**, not new:
[`p7-year1-readings.csv`](data/p7-year1-readings.csv) gathers the measures the canon reports for the
baseline quarter and quarters 1 to 3, and [`p7-open-decisions.csv`](data/p7-open-decisions.csv) lists the
open decisions with their decider, due date, and the options the canon records. Blank cells mean the canon
does not record the value; do not fill them with estimates presented as readings.

**Facts your submission must use.**

| Area | Facts |
|---|---|
| Year-1 results | Sev1 and Sev2 30, 21, 17, 14; availability 99.62 percent, not recorded, 99.86, 99.89 (about 144 of 131,040 minutes unavailable; 99.9 allows about 131); credits $410,000, not recorded, $95,000, $60,000; unplanned work 34, 31, 28, 25 percent; tier 1 at the four minimums 3, 8, 11, 13 of 15 |
| Correctness | 8 of the 14 baseline customer-detected incidents were correctness failures; invoice correctness SLO (99.99 percent) defined but dependent on reconciliation; week 40: 7,800 corrected orders of about 600,000 (1.3 percent); sample of 400: 340 errors (price changes 130, wrong unit 85, duplicate submissions 70 with no idempotency key, wrong delivery site 35, other 20) |
| Estate and knowledge | Four build systems, CI target open; Core framework past free community support (120 to 180 engineer-days to migrate); register TR-01 to TR-09; ledger currency and rounding changed safely by one person at baseline; 10 critical roles, none with a ready-now successor, 4 with no cover; core/permissions exemption lapsed at week 39 |
| Organization | Main proposal: 79 engineers, 7 managers, the director; alternatives B, C, D; about 21 engineer-weeks of transition cost; document-store has no owner in the proposal; VP recommendation due week 48 |
| Capacity | Quarter 3 plan: unplanned 22 percent planned and 28 cautious, prevention 8 FTE, platform 4.5, product 49.9 planned and 45.1 cautious; continuation: 6 FTE in quarters 5 and 6, 5 FTE in quarters 7 and 8 |
| Commitments in play | Draft board counter: at or below 40 Sev1 and Sev2 over year 2 as a rolling four-quarter total, 99.9 percent every quarter, two consecutive quarters above 12 reopen prevention; continuation gates in weeks 56, 78, and 104 |
| Victor's week 47 draft | Business choices confirmed in week 46: mid-market distributors with the largest 40 mattering most; trusted with money; cross-border growth moved to year 3. Excellent: financial correctness, availability of order and payment paths, accounting and bank integration, safe weekly change. Adequate: ordering screens, internal reporting, Core module structure. Buy: tax content, CI and observability tooling, corporate business systems. Not doing for three years: Core rewrite, multi-region active-active, customer-specific code branches, a new tier 1 runtime or datastore without retiring one. Policies: reliability before reach; money data moves by contract or events, never tables (ADR-0001 by week 60); converge before adding; stage anything above 10 FTE-quarters. Year-2 allocation on 79 engineers: unplanned 17.4, prevention 5.5, platform 4.5, estate currency 2.0, product for today's customers 37.6, horizon 2 10.0, horizon 3 2.0. The CI target is chosen at the week 78 gate |
| Stakeholders | Helena Marsh: six of the 40 largest customers renew in quarters 5 to 8. Rajiv Menon: operating expense flat, any new cash offset. Greg Tanaka: prevention engineers to deal features; a private offer in week 47 that the director declined. Amara Okafor: allocation fixed per stage. Sofia Alvarez: customer incident notifications kept |
| Money | $185,000 per engineer-year; $46,250 per FTE-quarter; about $3,558 per engineer-week; gross margin 72 percent; discount rate 10 percent; top-40 customers about $1.17M ARR each |

**Facts you do not have.** Quarter 4 results; the outcome of the week 46 organization decision, the VP
recommendation, the continuation, the workforce plan, the week 34 forum, and the board meeting; whether the
deployment-event store, CI consolidation phase 1, or a general invoice reconciliation job is running;
quarter 3 change failure rate, recurrences, and customer-detected share; any committed-delivery figure
after the baseline quarter; and how Victor will revise his draft after week 47. Treat each as a gap with an action, not a value.

## Required Deliverables

One strategy document of no more than about six pages, a one-page summary, and your spreadsheet.

1. **Evaluation of the week-14 draft.** For each of its three policies: the decision it was tested against,
   what happened to that decision by week 47, and whether the policy should be kept, rewritten, or
   dropped. Say why the draft decided so little.
2. **Diagnosis.** No more than three findings, each with numbers from the canon and the business
   consequence, written for year 2 rather than copied from week 14.
3. **Strategic choices.** Where engineering will be excellent in year 2, where adequate is enough, and what
   waits for year 3, mapped to the four groups in Victor's week 47 draft, with any departure from it stated
   and argued.
4. **Guiding policies.** Two to four, each with the finding it answers, its cost (the freedom it removes),
   its owner and exception time, one year-1 decision it would have settled, and one open decision it
   settles now.
5. **Coherent actions by quarter.** Enforcements, escalations, and transitions for quarters 5 to 8, each with
   an owner, a due week, and a capacity estimate labeled as yours.
6. **Capacity envelope.** Engineers, unplanned work (planned and cautious), prevention, platform,
   transition, and product for each quarter, at your chosen seat count, with the effect of the other seat
   counts and of the 4-plus-2 option.
7. **What we will not do.** At least three options ruled out, including one that a senior person wants.
8. **Branches.** For each open decision, how the strategy changes under each plausible outcome.
9. **Scorecard and review triggers.** Five to seven measures, each with its pair, that tell Victor whether
   the strategy is working; and the observable conditions that reopen it.
10. **One-page summary** for Victor Lindqvist, and the order in which you will workshop the draft.

## Step-by-Step Instructions

1. **Grade the week-14 draft first.** Open [`p7-open-decisions.csv`](data/p7-open-decisions.csv) and find each
   of the draft's test decisions. A policy whose test decision is still open after 33 weeks tells you
   something about the policy, not only about the decision.
2. **Rebuild the readings.** From [`p7-year1-readings.csv`](data/p7-year1-readings.csv), recompute what you
   will cite: the incident change with its uncertainty, the availability gap in minutes, credits annualized,
   unplanned work in FTE and dollars, the corrected-order error rate.
3. **Write the diagnosis** as causes, not symptoms. Ask what makes year 2 hard that did not make year 1 hard.
4. **Make the choices explicit.** Name what engineering will be excellent at, and what it will accept as
   adequate. A choice that disappoints nobody is not a choice.
5. **Draft policies and test them** against a past decision and an open one. Check that a team could tell
   whether a proposal complies ([Larson, 2023](../references/bibliography.md#larson2023engstrategy)).
6. **Turn each policy into actions,** at least one enforcement per policy, and give every escalation a date.
7. **Price the actions** against the capacity envelope. Plan from the cautious case, as
   [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
   does, and expect your own estimates to be optimistic
   ([Buehler et al., 1994](../references/bibliography.md#buehler1994exploring)).
8. **Write the branches** for each open decision. If an outcome would break a policy, the policy is too
   dependent on one person's choice.
9. **Choose the scorecard and the triggers.** Reuse the board page's measures where you can, so that the
   strategy and the board report do not disagree.
10. **Run the coherence checks** (below), then write the one-page summary last.

```mermaid
flowchart TD
    E["Year-1 evidence"] --> D["Diagnosis"]
    D --> C["Choices"]
    C --> P["Guiding policies"]
    P --> A["Actions by quarter"]
    A --> K{"Fits capacity?"}
    K -->|No| C
    K -->|Yes| B{"Holds every branch?"}
    B -->|No| P
    B -->|Yes| S["Summary for Victor"]
```

The two loops are where most drafts change: actions that do not fit the cautious case send you back to
the choices, and a policy that breaks under one executive decision sends you back to rewrite it.

**Coherence checks.** Every policy answers a finding; every finding has a policy; every action traces to a
policy; the capacity rows sum to the seat count; every "will not do" line disappoints a named person; and
every policy would have settled a real year-1 decision.

## Explicit Trade-offs

| Trade-off | The tension at Northstar |
|---|---|
| Reliability against deal features | Incidents are down and Greg Tanaka wants the prevention engineers; six top-40 renewals in quarters 5 to 8 and an availability miss of 13 minutes say reliability is not finished |
| Availability against correctness | The contract and the board measure availability; customers now feel corrections, which no availability measure sees |
| A strategy that decides against one that waits | Writing policies that settle the CI target or ADR-0001 takes a position before Victor decides; leaving them open repeats week 14 |
| Convergence against capacity | Finishing the CI consolidation and the framework migration costs capacity the continuation is cutting from 8 FTE to 6 and 5 |
| One plan against branches | A strategy written for one organization outcome is simple and fragile; one written for four is robust and hard to read |
| Stability against learning | Allocations changed rarely let teams plan ([Larson, 2023](../references/bibliography.md#larson2023planning)); the trigger at two quarters above 12 changes them on evidence |
| Even shares against focus | Spreading prevention across all teams is easy to defend; allocations tend to drift toward equal shares by unit whatever the need ([Bardolet et al., 2011](../references/bibliography.md#bardolet2011capital)) |
| Writing it with the staff engineers against writing it fast | Co-authors make policies enforceable and take weeks; the board is in week 50 |

## Acceptance Criteria

A submission is accepted only if all of these hold.

1. The diagnosis has no more than three findings, each with at least one number traceable to the canon.
2. There are two to four guiding policies, each with a cost, an owner other than the director (at most one
   owned by the director), an exception time, and the finding it answers.
3. Each policy is tested against a real year-1 decision and settles at least one decision open in week 47.
4. Every action has an owner, a due week, and a policy it serves; every policy has at least one enforcement.
5. The capacity envelope sums to the stated seat count in every quarter, uses a cautious case, and shows the
   other seat counts and the 4-plus-2 option.
6. "What we will not do" names at least three options, one of them wanted by a named senior person.
7. Every open decision in the time window has a branch, and no outcome after week 47 is recorded as fact.
8. The scorecard has five to seven paired measures and is consistent with the board page or explains why not.
9. The evaluation of the week-14 draft says what happened to each of its test decisions.
10. No fact is invented about the canon; estimates and assumptions are labeled as yours.

## Evaluation Rubric

Weights total 100. A strong pass is 75 or more with no criterion weak.

| Criterion | Weight | Excellent | Adequate | Weak |
|---|---|---|---|---|
| Diagnosis | 20 | Three or fewer causes specific to year 2, each with recomputed numbers and a business consequence; correctness and concentration seen, not only incidents | Findings with numbers, partly copied from week 14 | Goals or symptoms ("improve quality"); no numbers |
| Choices and policies | 20 | Explicit excellent and adequate areas; policies applicable, costly, owned, tested against past and open decisions | Policies with owners; tests thin | Slogans that cost nothing; the director owns everything |
| Actions and roadmap | 15 | Enforcements, escalations with dates, and transitions by quarter; each traced to a policy | Dated actions, some untraced | A project list with no enforcement |
| Capacity and economics | 15 | Envelope from the cautious case at a stated seat count; actions priced; seat-count and 4-plus-2 effects shown | Envelope present; one case only | No numbers, or plans that exceed the seats |
| Uncertainty and open decisions | 10 | Every open decision branched; incident changes read with intervals; nothing after week 47 treated as known | Branches for the main decisions | Open decisions assumed settled |
| Measurement and triggers | 10 | Paired measures shared with the board page; triggers observable without a meeting | Measures without pairs, or triggers without data sources | No way to tell if the strategy works |
| Evaluation and communication | 10 | Honest grading of the week-14 draft; a summary Victor can read in two minutes; a workshop order that reaches the people the policies constrain | Summary present | No evaluation; summary restates the document |

## Solution

The worked solution, with the week-14 draft graded, the capacity envelope computed at three seat counts,
and one complete strategy, is in [Project 7 solution](solutions/p7-solution.md).

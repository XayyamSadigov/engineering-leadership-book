# Northstar: the director's first quarter

!!! warning "Fictional"
    Everything on this page is invented for the book. See the note on the
    [Northstar overview](index.md).

The chapters of Part V each tell part of one story: the Engineering Director's first 90 days at
Northstar. This page is the canonical record of that story, so that the chapters agree with each
other. The starting state is on the [baseline data](baseline-data.md) page. Weeks are counted from
the director's first day.

## Decisions that hold for the rest of the book

| Decision | Detail | Chapter |
|---|---|---|
| Constraint | The Core release train | 27 |
| Renewal commitments | Bulk ordering (Orders; asynchronous order files up to 20,000 lines across delivery sites; 5 Orders and 2 Customer Experience web engineers) due at the end of quarter 2 (week 26 from the director's first day). Accounting-system integration (Payments and Integrations; new erp-sync connector with daily reconciliation of posted invoices; 4 engineers) due at the end of week 6 of quarter 2 (week 19). Both are on track at day 90 and neither is due in quarter 1 | 15, 17 |
| Director's role definition | Purpose: reliability and delivery of the whole organization. People: develop the six managers, give the staff engineers mandates. Delivery: own cross-team commitments and the capacity model. Technical: ensure cross-team decisions have an owner. Not doing: running a team's planning, responding to incidents, writing production code | 1 |
| Prevention allocation, quarter 1 | 12 FTE in total: Billing 25 percent, Orders and Payments and Integrations 10 percent (renewal commitments), other teams 15 percent, computed on baseline team sizes (11.55 FTE), plus 15 percent of the three staff engineers (0.45 FTE); 2 FTE of it earmarked for security work | 27, 26 |
| Severity definitions | Published week 3, written by the director with Kwame Mensah and Sofia Alvarez. Sev1: the order or payment path unavailable for any customer, or any wrong financial record visible to customers | 25 |
| Baseline re-rating under the new definitions | INC-401 and INC-427 would be Sev1, making the baseline 9 Sev1 and 21 Sev2. The baseline page keeps the original ratings; the total of 30 is unchanged | 25 |
| Tier 1 list | The 15 proposed tier 1 components are used for all counts in quarter 1. notification-svc moves to tier 2 and to Orders from quarter 2. Reporting rule: year 1 readiness counts (quarters 1 to 4) keep the original list of 15 so that quarters compare; year 2 reports use the current list of 14 | 24 |
| Tier 1 minimums | Four operational minimums are measured: owning team, complete user-facing alerts, runbook, on-call rotation. The fifth enterprise minimum, deployment through an auditable pipeline with automated rollback, is a standard tracked separately (Chapter 20) | 20, 24, 27 |
| Standards | 52 rules triaged: 14 kept as mandatory (9 tool-checked, 5 by review), 17 turned into guidance, 21 retired; plus 5 tier 1 minimums (owner, user-facing alerts, runbook, on-call, auditable pipeline with automated rollback) | 20 |
| Standard owners | Kwame Mensah: operational minimums and pipelines. Ines Carvalho: Core code. Li Na Zhou: data, migration, and configuration. Decisions within 10 working days; exemptions recorded with expiry of at most two quarters | 20 |
| Remediation service levels for vulnerabilities | Known-exploited or critical on internet-facing tier 1: 7 days. Other critical: 30 days. High: 90 days | 26 |
| Proposed SLOs (28-day window) | Order submission 99.9 percent; order latency 99 percent within 2 seconds; payment reaching a final state within 60 seconds 99.9 percent; invoice correctness 99.99 percent once reconciliation exists | 24 |
| Error budget policy | Reporting mode for the quarter: budgets published weekly, any incident consuming more than a fifth of a journey's budget gets a tracked review; Victor Lindqvist arbitrates | 24 |
| Ownership | Week 4: core/customer to Orders, core/scheduler to Billing. auth-svc to Platform Operations; webhooks to Payments and Integrations. core/permissions stays tier 1 but its owner (Orders or Platform Operations) is still undecided at day 90, covered by a recorded exemption | 21, 26, 20 |
| QA engineers | Move into product teams as quality engineers: 2 Orders, 2 Billing, 2 Customer Experience, 1 Payments and Integrations, each reporting to the team's manager (so Priya Raman has 16 reports from week 10, Daniel Cho 17). Announced week 10. Two chose the 600-case weekly regression subset; all seven triaged the manual suite with the teams, and five also automated cases | 19, 27, 22, 23 |
| Flaky tests | Release working group led by Kwame Mensah, with owners from the teams: the 40 worst quarantined in week 4, 140 by day 90, each with an owner and a fix-or-delete deadline | 21, 22, 23 |
| Migration check | Promised after INC-427 (Li Na Zhou, due week 7); slipped; after the week 9 Sev1 an interim rule applied; landed week 11 | 25, 21, 23 |
| Incident commanders | 12 trained in weeks 4 and 5: the six managers, three staff engineers, three senior engineers | 25 |
| Corrective actions | 65 open actions triaged: 14 kept (with 9 duplicates merged into them), 42 dropped with a reason; every kept action has a manager owner | 25 |

## Timeline

| Week | Event | Chapter |
|---|---|---|
| 2 | Incident classification with Kwame Mensah; one-off security scan of all 24 components; Priya Raman agrees a time budget (hands-on work capped at 8 hours a week) and delegates: Aisha Bello leads bulk-ordering implementation, Rafael Duarte and Aisha Bello own core/order-capture reviews, Rafael Duarte takes the open bulk-upload test action | 27, 26, 2 |
| 3 | Severity definitions published; standards page reviewed (39 of 52 rules unobservable); a renewal customer sends a security questionnaire asking for an SBOM and SSDF evidence | 25, 20, 26 |
| 4 | Capacity model agreed with Victor Lindqvist and Amara Okafor; Core main below 10 percent red time; first 40 flaky tests quarantined; core/customer and core/scheduler get owners | 27, 23, 21 |
| 5 | First weekly Core release | 23 |
| 6 | payments-gateway flag changes move to reviewed, validated merge requests | 23 |
| 7 | Four consecutive incidents rated Sev3, one of them a two-hour payment delay for nine customers; the director re-rates it and adds severity audit to the weekly review | 27 |
| 8 | A contract test catches a payments-gateway rounding change; security audit finds 2 of 7 "not affected" closures unanalysed | 22, 26 |
| 9 | Sev1 in Billing: credit notes applied twice. Rollback fails because a migration had already changed the schema; restored by a forward fix. The pipeline check promised after INC-427 had slipped. Interim rule: no release may contain a ledger migration and code that depends on it | 27, 23, 25 |
| 10 | QA transition announced; migration rehearsal mandatory for tier 1 data | 27, 22 |
| 11 | Pipeline check for unfinished migrations lands | 25 |

## Day 90

| Measure | Baseline quarter | Transformation quarter | Chapter |
|---|---|---|---|
| Sev1 and Sev2 incidents | 30 | 21 | 27 |
| of which via Core releases | 9 | 4 | 27 |
| Recurrences | 11 of 30 | 5 of 21 | 25 |
| Customer-detected share | 47% | 29% | 27 |
| Core releases | 2 per month | 11 in the quarter (weekly from week 5) | 27, 23 |
| Core change failure rate | 31% (4 of the 13 releases in the 26 weeks before the director arrived) | 22% (2 of the 9 weekly releases from week 5; the two fortnightly releases of weeks 1–4 are not counted, because the measure was redefined with the weekly cadence) | 27 |
| Core main branch red | 22% of working hours | 9% over the last four weeks | 23 |
| Pipeline failures unrelated to the change | 9% | 4% | 22 |
| Flaky tests quarantined | — | 140 | 22, 23 |
| Manual regression before a release | 1,900 cases over 3 days | about 600 cases in 1 day; 1,100 of 1,900 cases triaged (400 automate, 450 delete, 250 exploratory charters) | 23, 22 |
| Contract-tested tier 1 boundaries | 0 | 4 | 22 |
| Corrective action closure | 32% | 70% (26 of 37) | 25 |
| Tier 1 components meeting the four operational minimums (owner, complete alerts, runbook, on-call) | 3 of 15 | 8 of 15 (runbooks 11 of 15) | 20 |
| Unplanned work | 34% | 31% | 27 |
| Components with dependency scanning | 8 of 24 | 20 of 24 in the pipeline; the 4 script services by weekly scheduled scan | 26 |
| Open critical vulnerabilities | 11 (3 known-exploited) | 3, all under recorded exceptions (1 known-exploited, mitigated) | 26 |
| Live credentials in git history | 9 | 0 | 26 |
| Certificates with owner and expiry alerting | 0 of 34 alerted | 34 of 34 | 26 |
| Renewal commitments | — | both on track | 27 |

## Starting points for quarter 2

These are situations at the start of quarter 2 that later chapters present as decisions for the
reader. Their outcomes are deliberately not fixed.

| Situation | Chapter |
|---|---|
| Rafael Duarte asks whether to pursue management again or the staff track; there is no open manager role | 4 |
| Flow changes for the accounting integration: Billing reserves weeks 1 to 3 for the ledger export; Li Na Zhou proposes a ledger-export contract; Platform Operations runs a two-person interrupt rotation with a single intake and self-service test environments; Payments and Integrations lowers its WIP limits. A re-sample in week 5 of quarter 2 (week 18) shows environment waits falling from about 6 days to 2, and requests from other teams falling from 20 to 14 points of Platform Operations capacity | 16 |
| Forecast for bulk ordering: 44 backlog items at the director's arrival, historically growing 15 to 35 percent | 17 |
| Rajiv Menon asks for an output-per-engineer figure by team for next year's budget pack, with Helena Marsh's support | 18 |
| The director's proposed delivery measurement set and a shared deployment-event store (about six engineer-weeks from the prevention allocation) | 18 |
| Permissions extraction from core/customer, led by Ines Carvalho, funded for quarter 2; core/permissions still without an owner (Priya Raman would accept it after week 26; Tom Becker sees it next to auth-svc but cannot support Core Java) | 21, 13 |
| Stay interviews: Ines Carvalho (week 14; the permissions extraction she leads is funded, the rest of her redesign is not) and the three ledger engineers (weeks 14–15); in week 20 Tomasz Wierzbicki reports an outside offer 20 percent above base | 10 |
| Daniel Cho's one-on-ones reviewed (weeks 14–19: 84 of 90 held, 55 mainly status, news in 11); team health check for Customer Experience in week 16, facilitated by Elena Sokolova (mobile 4 red of 10 indicators); in week 17 Mateo Arango Ríos tells the director he has done a lead's job for over a year | 5, 14 |
| Priya Raman asks whether Orders should adopt Payments and Integrations' operations review and near-miss log | 11 |
| Billing ledger knowledge map built; Data and Analytics drafts a team charter (search-svc ownership open) | 12 |
| Proposal to run the next two backfills as a structured hiring pilot (scorecard, work sample, facilitated debrief) | 7 |
| Tom Becker's draft expectations plan for Bram Verhoeven, drafted at the start of quarter 2 from a reconstruction of the baseline quarter | 9 |
| Ladder rewrite drafted (five dimensions, three levels); first calibrated promotion cycle at the start of quarter 3 (9 nominated, 5 promoted, 4 "not yet"); six underpaid US Senior Engineers identified | 8 |
| ADR-0001, Northstar's first decision record, opened by Li Na Zhou in week 14: how integrations read posted ledger data. Options: read the tables (ready by week 19), a versioned export contract (5 of Billing's 6 reserved engineer-weeks; ready by week 19), or ledger posting events (about week 24). Li Na recommends the contract. Victor Lindqvist told Elena Sokolova in passing to "read the tables now and clean it up later". Nobody's decision rights are mapped | 28 |
| Standing scopes for the three staff engineers drafted; a coaching plan for Ines Carvalho with checkpoints in weeks 20 and 26 | 29 |
| A technical strategy draft (three policies: converge before adding; own order-to-cash logic, buy what changes for outside reasons; every tier 1 component on supported versions with two people who can change it) and a technology risk register TR-01 to TR-09; the tax-svc build, buy, or hybrid decision (three-year costs $373,500, $597,250, $329,750) | 30 |
| Ines Carvalho's Core boundary proposal from co-change analysis: keep all eight modules in Core in quarter 2, carry out the permissions extraction inside Core, enforce module dependencies in the build; Rafael Duarte argues for extracting order-capture; Marcus Oyelaran wants no boundary work before week 19 | 31 |
| Platform roadmap drafted by Tom Becker and Kwame Mensah: about 29 engineer-weeks of planned capacity; self-service environments, the deployment-event store, and CI consolidation phase 1 (the four shell-script services); GitLab CI proposed as the consolidation target, decision open | 32 |
| Orders' structure options (Orders carries seven components and bulk ordering; about 2.6 engineers of capacity left for everything else in quarter 2) | 33 |
| Span table and dependency analysis; the only boundary change made in quarter 2 is a Billing-owned order-to-invoice contract with contract tests on both sides (no people move); the analysis feeds the week 44 year-2 proposal | 34 |


The flat-headcount constraint counts the whole engineering organization (87 people). Promoting an
engineer into a new manager role is allowed only if that engineer's seat is not backfilled.

## Year 2 proposal (quarter 4)

In week 44 the director drafts a year-2 organization proposal for Victor Lindqvist, effective at the
start of quarter 5 (week 53). The CTO decides; the outcome is open (Chapters 35 and 36).

| Element | Proposal |
|---|---|
| Customer Experience | Splits into Web (Daniel Cho; 9 web engineers and 2 quality engineers, 11) and Mobile (Bogotá; Mateo Arango Ríos as manager, his engineering seat not backfilled; 5 engineers; mobile-app and mobile-bff with their own on-call rotation) |
| core/permissions | Moves to Orders (Priya Raman's condition, after week 26, is met) |
| search-svc | Moves from Orders to Data and Analytics |
| Developer Platform | Platform Operations renamed and run as an internal product; Tom Becker and the same five engineers |
| Totals | 79 engineers, 7 managers, the director (87); the director has 10 direct reports |
| Alternatives in the draft | B: keep Customer Experience whole with two subteams (80 engineers, 6 managers). C: also split Orders into Order Capture and Catalog and Pricing and grow the platform to 8 (78 engineers, 8 managers). D: two managers of managers (77 engineers, 9 managers) |
| Transition plan | Decision week 46, announcement week 51, reporting lines week 53, search-svc week 54, all handoffs by week 57, review week 64; about 21 engineer-weeks of transition cost, excluding Mateo's seat |
| Gap in the proposal | document-store is not assigned an owner, although the transition plan requires every component to appear exactly once in the ownership register by week 57 (a gap Project 4 asks the learner to find) |
| Succession coverage (week 44) | 10 critical roles; none with a ready-now successor; 6 with interim cover; 4 with none (Billing manager, Data and Analytics manager, the core-domain and the data-and-integration staff roles) |

The core/permissions exemption recorded in quarter 1 reached the two-quarter maximum at the end of
quarter 3 (week 39) with the ownership decision still open; it lapsed without renewal, which is the
decision avoidance Chapter 13 describes. The year-2 proposal is the first document to resolve it.


## Quarter 2 results and the operating system (weeks 14–26)

| Measure | Quarter 1 | Quarter 2 |
|---|---|---|
| Sev1 and Sev2 incidents | 21 | 17 (3 Sev1, 14 Sev2) |
| of which via Core releases | 4 | 2 |
| Recurrences | 5 of 21 | 3 of 17 |
| Customer-detected share | 29% | 29% (5 of 17) |
| Core releases | 11 | 13 (weekly) |
| Core change failure rate | 22% | 23% (3 of 13) |
| Unplanned work | 31% | 28% |
| Tier 1 meeting the four operational minimums | 8 of 15 | 11 of 15 |
| Corrective-action closure | 70% (26 of 37) | 78% (21 of 27) |
| Availability, contractual paths | not recorded | 99.86% |
| Service credits | not recorded | $95,000 |

| Fact | Detail | Chapter |
|---|---|---|
| Renewal commitments at week 26 | The accounting integration has been live for the renewal customer since week 19, with daily reconciliation of posted invoices (no ledger read path is named; ADR-0001 stays open). Bulk ordering's 44 contractual items are complete and the release candidate is in final acceptance, forecast to ship by the end of week 26 | 39 |
| The director's quarter 2 calendar | Recurring meetings: weekly operational review (booked 30 minutes, averaging 75), weekly 60-minute managers' meeting, weekly renewal check-in and product and engineering sync, weekly Billing and Orders sync from week 14, the release working group, a fortnightly staff group, one-on-ones (managers 45 minutes, staff engineers and Victor Lindqvist 30), monthly quality reviews, delivery review, and all-hands, and the quarterly reset: about 16.3 hours a week from week 16; about 25 hours of a 47-hour week in meetings | 37 |
| Skip-levels | None in weeks 1–15. From week 16, individual skip-level conversations, four a week, 30 minutes (44 by week 26); Mateo Arango Ríos's week-17 conversation was the director's first with a mobile engineer. No group skip-levels before quarter 3 | 37, 40, 41 |
| The director's firsthand time | Weeks 14–15 measured at 4.7 percent of the director's hours | 40 |
| Organization decision log | Opened week 14, backfilled from quarter 1 decisions (DL-01 to DL-10); ADR-0001, tax-svc, and the CI target are open | 39 |
| Escalation path | Published week 15: five working days for the parties, then a joint written case decided by the director within five working days and logged; to Victor Lindqvist only for customer commitments or the director's budget authority | 39 |
| Reports to Victor Lindqvist | The week 26 report is the first written report since the day-90 report; proposed monthly from quarter 3 | 39 |
| Manager expectations | A one-page written expectation on the rubric's six dimensions in week 22; draft ratings of the six managers in week 24 | 41 |
| Priya Raman's hands-on time | 8, 10, and 12 hours a week at the week 16, 20, and 24 checks (cap 8) | 41 |

## Quarter 3 (weeks 27–39)

| Fact | Detail | Chapter |
|---|---|---|
| Capacity plan | Planned: unplanned work 22% (17.6 FTE), prevention 8 FTE (Billing 2.5, Orders 2.0, Customer Experience 1.5, Payments and Integrations 1.0, Data and Analytics 1.0), platform 4.5, product 49.9. Cautious: unplanned 28% (22.4 FTE), product 45.1. Committed about 35.6 FTE-quarters of estimated effort (about 463 engineer-weeks), targets 3.8, unfunded 22.6 of Amara Okafor's 62. A bulk-ordering support reserve of 8 engineer-weeks in weeks 27–30 | 38 |
| Cross-team portfolio | At most three cross-team initiatives in progress (a one-quarter trial): multi-currency price lists and catalog export (Greg Tanaka's two deal features), customer incident status notifications (Sofia Alvarez), automated service-credit statements (Rajiv Menon, waiting until about week 33). In week 31 Greg Tanaka asks for a third deal feature, purchase approval rules; the week 34 portfolio forum's outcome is open | 42 |
| Operating system redesign | Proposed for week 27: a hard 45-minute operational review, a weekly 75-minute leadership team meeting replacing the managers' meeting and product sync, a monthly business review, a quarterly talent review | 37 |
| Engineering Excellence Day | Launched by the director in week 27 without the managers or Amara Okafor; Fridays of weeks 28, 32, 36; participation 64, 41, 23 engineers; 71 items merged, none touching the priced debt register; one Sev3 from a core/scheduler change; stopped in week 37 after a one-page note to the managers | 43 |
| Skip-level rotation | Proposed: two groups of three a week plus one individual slot, covering all 77 team engineers in the quarter | 40 |

### Quarter 3 results

| Measure | Quarter 2 | Quarter 3 | Chapter |
|---|---|---|---|
| Sev1 and Sev2 incidents | 17 (3 Sev1) | 14 (2 Sev1, 12 Sev2); the first quarter at or below the mandate's 15 | 49 |
| Availability, contractual paths | 99.86% | 99.89% (about 144 of 131,040 minutes unavailable; 99.9% allows about 131) | 49 |
| Service credits | $95,000 | $60,000 | 49 |
| Unplanned work | 28% | 25% (20 FTE of 80), between the planned 22% and the cautious 28% | 49 |
| Tier 1 meeting the four operational minimums | 11 of 15 | 13 of 15 | 49 |
| Level mix, week 40 | 44 Engineers, 33 Seniors, 3 Staff (on arrival) | 39 Engineers, 38 Seniors, 3 Staff after five promotions to Senior in the quarter 3 cycle | 48 |

Quarter length: the baseline quarter is the 90-day calendar quarter before the director arrived; the
director's quarters are 13 weeks (91 days, 131,040 minutes), so availability allowances from quarter 1
on use 91 days (99.9 percent allows about 131 minutes). These are the latest measured figures
available to anyone in quarter 4. Quarter 4 results are not
recorded; any chapter set in weeks 40–52 uses quarter 3 as the latest quarter.

## Quarter 4 (weeks 40–52)

None of the decisions below has a recorded outcome. Chapters set in quarter 4 leave each of them open.

| Week | Fact | Chapter |
|---|---|---|
| — | Economic assumptions: gross margin 72 percent; Finance's discount rate 10 percent a year; one engineer-week costs about $3,558 ($185,000 ÷ 52); average ARR per customer about $74,000; the 40 largest customers about $1.17M each | 45 |
| — | Bogotá engineers cost about $110,000 a year fully loaded, including the office, which puts the US-based average at about $202,000 ((87 × $185,000 − 16 × $110,000) ÷ 71) | 48 |
| — | Keiko Ashworth, one of Amara Okafor's three product managers, is the product manager for the ordering area (Orders and Customer Experience's ordering screens), Minneapolis. The other two cover billing and payments, and data and customer reporting | 44 |
| 39–40 | Orders sizes price-list effective dates at 14 engineer-weeks in week 39; Greg Tanaka then gives an existing distributor week 46 as the date. Orders forecasts weeks 44 to 46 from a week 40 start | 44 |
| 40 | A top-40 distributor complains, via Sofia Alvarez, about time spent correcting orders. Data and Analytics defines a corrected order (cancelled and re-entered, amended, or credited for an ordering error within 72 hours): 7,800 of about 600,000 submissions in the last 28 days of quarter 3 (1.3 percent). A sample of 400 corrections in weeks 40–41 finds 340 errors (about 1.1 percent of orders): price changes 130, wrong unit 85, duplicate submissions 70 (no idempotency key on order submission), wrong delivery site 35, other 20 | 44 |
| 41 | Victor Lindqvist asks for the engineering page of the year-2 board plan, due week 45, proposing the headline "Sev1 and Sev2 incidents below 10 per quarter" with flat headcount | 46 |
| 41 | Rajiv Menon asks for a year-2 workforce plan with the budget pack. The director drafts a working contract with product and sends it to Amara Okafor | 48, 44 |
| 42 | Amara Okafor answers the working contract with three conditions (named discovery engineers only if paid from the product line; no external date before sizing only if deal requests are sized within five working days; no replacement of ordering items by an outcome target while the board pack reports roadmap items delivered) | 44 |
| 42 | The director's counter for the board page (a draft): Sev1 and Sev2 at or below 40 over year 2 as a rolling four-quarter total, reported with the severity audit; 99.9% availability every quarter; prevention funded as in the continuation proposal (6 FTE in quarters 5–6, 5 FTE in quarters 7–8) with flat headcount; two consecutive quarters above 12 reopen the prevention allocation | 46, 49 |
| 44 | Year-2 organization proposal (see above); decision week 46 | 35, 36 |
| 45 | Victor Lindqvist asks whether Northstar needs a VP of Engineering in year 2 or whether the director grows into the role; recommendation due week 48. A VP takes one of the 87 seats, so engineers fall from 79 to 78 under the main proposal | 47 |
| 45 | The director drafts a two-year continuation of the quality program: stage 2 "Hold" (quarters 5–6, 6 FTE prevention, $150,000 of tooling, gate week 78) and stage 3 "Converge" (quarters 7–8, 5 FTE, $100,000 of tooling only if a CI target is chosen, gate week 104), after a stage 1 gate in week 56; no headcount request; "VP or second layer" listed as an open question. One-on-ones with executives weeks 46–47, executive team meeting week 49, decisions requested by week 51 | 49 |
| 46–47 | Executive positions on the continuation: Victor supports staging; Helena Marsh focuses on renewals (six of the 40 largest customers renew in quarters 5 to 8); Rajiv wants operating expense flat and the $150,000 offset in the $4.2M cloud and tooling budget; Greg Tanaka wants the prevention engineers on deal features and in week 47 privately offers support in exchange for two engineers outside the portfolio forum, which the director declines and writes into the proposal as an option; Amara wants the allocation fixed per stage; Sofia wants customer incident notifications kept | 49 |
| 49 | Workforce plan draft to Victor and Rajiv with four options (A like-for-like, B shaped backfills, C two requisitions held ahead, which would need an exception to the 87-seat rule, D a fixed-scope vendor contract) and the rule "no customer date without an engineering estimate and a named owner"; Greg Tanaka objects to the rule. The recommendation is left open | 48 |
| 50 | Quarter 4 board meeting: the year-2 operating plan and budget envelope for approval, with the engineering page drafted in weeks 41–45. Its outcome is not recorded | 55 |

## Part XII facts (quarter 4)

Added when Part XII (Chapters 50–55) was written. Everything here is set in quarter 4, and none of it
records the outcome of an open decision: drafts, positions, and measurements only.

### The CTO's job (Chapter 50)

| Fact | Detail |
|---|---|
| Victor Lindqvist's average week, weeks 44–46 | 48.0 hours. Work only the CTO can do, 20.0: executive team and CEO one-on-one 3.0; fortnightly one-on-ones with Amara Okafor, Rajiv Menon, Greg Tanaka, and Sofia Alvarez 1.0; the director 0.5; largest customers' technical relationships 5.0; board preparation 4.0; year-2 decision reviews 4.5; uninterrupted strategy work 2.0 (about 4 percent). Delegable, 11.0: customer security reviews 2.0, sales calls on open deals 3.5, Sev1 bridges and customer incident calls 2.0, unrecorded technical rulings 3.5. Other, 17.0: engineering forums 1.5, recruiting and external 1.0, email, administration, and travel 14.5 |
| Informal technical requests, weeks 44–46 | 11: 3 genuinely the CTO's (a top-40 customer's request for a dedicated environment; technical terms of a vendor renewal affecting product and IT; a top-40 customer's request to review architecture direction before renewal), 6 belonging under the director's escalation path, 2 belonging to standard owners (Kwame Mensah, Li Na Zhou) |
| Customer security questionnaires | Addressed to Victor; Joon Park drafts answers from IT's records; engineering supplies evidence ad hoc |
| Victor's week 47 draft (not implemented) | Keep, give, stop list freeing 7.0 hours a week for strategy (2.0 to 9.0); a table of decisions shared with IT; three options for the IT seam (write the table and keep IT under the CFO, move IT under the CTO, wait for the risk and security design), none chosen |

### Three-year technology strategy (Chapter 51)

Year 2 is weeks 53–104, year 3 weeks 105–156, year 4 weeks 157–208.

| Week | Fact |
|---|---|
| — | Northstar has no written statement of where it plays and how it wins; the year-2 operating plan draft states financial targets and the renewals focus |
| 46 | Victor sends Helena Marsh his reading of the business choices. She confirms two (mid-market distributors with the largest 40 mattering most; trusted with money) and moves growth into larger cross-border distributors to year 3 as a board question |
| 47 | Victor's draft sorts technology into four groups: excellent (financial correctness, availability of order and payment paths, accounting and bank integration, safe weekly change), adequate (ordering screens, internal reporting, Core module structure), buy (tax content, CI and observability tooling, corporate business systems), not doing for three years (Core rewrite, multi-region active-active, customer-specific code branches, a new tier 1 runtime or datastore without retiring one). Four policies: reliability before reach; money data moves by contract or events, never tables (a stated reversal of the week 14 remark, proposing ADR-0001 be decided by week 60); converge before adding; stage anything above 10 FTE-quarters |
| 47 | Draft allocation on 79 engineers, years 2 / 3 / 4: unplanned work 17.4 / 14.2 / 12.6 (22, 18, 16 percent); prevention 5.5 / 3.0 / 3.0; platform 4.5 / 5.0 / 5.0; estate currency 2.0 / 1.5 / 1.5; product for today's customers 37.6 / 37.3 / 35.9; horizon 2 10.0 / 14.0 / 16.0; horizon 3 2.0 / 4.0 / 5.0 |
| 47 | Draft options and decision weeks: ledger posting events (60, depends on ADR-0001); higher availability tier for top accounts (4 engineer-week study, 70); multi-currency invoicing and ledger (6 engineer-week probe, 78); ordering API for distributors' largest buyers (78); Core order-capture extraction (104). The CI target to be chosen at the week 78 gate |
| 48 | 90-minute premortem with the director and the three staff engineers; Victor adds the stress rule (an unplanned-work overrun comes out of horizon 2, never prevention or horizon 3) and a people line (by week 104, at least two people can safely change each "excellent" area) |
| 49 | At the executive team meeting, Amara Okafor's objection moves ordering correctness to "excellent"; Greg Tanaka's objection to "no customer-specific code branches" (two open deals) is recorded and the line kept; Victor confirms to Rajiv Menon nothing beyond the continuation's $150,000 |
| 50 | The draft is Victor's one board agenda item, for discussion, not approval. The board's response is not recorded |

### Finances (Chapter 52)

Fiscal year 1 (FY1) is weeks 1–52; FY0 is the year before the director arrived; FY2 starts in week 53.
Northstar reports under US GAAP with an outside audit. Most contracts are billed annually in advance.
Service credits reduce subscription revenue. Figures are Finance's week 46 latest estimate for FY1
(quarters 1–3 actual, quarter 4 forecast), in $M.

| Income statement, FY1 | $M | Balance sheet | End FY0 | End FY1 |
|---|---|---|---|---|
| Subscription revenue (net of credits) | 140.0 | Cash | 56.0 | 73.5 |
| Professional services revenue | 5.0 | Accounts receivable | 17.0 | 17.5 |
| Total revenue | 145.0 | Prepaid and other | 3.0 | 3.0 |
| Cost of revenue (support 18.0, services 8.5, payment and data fees 6.0, production hosting 3.1, amortization 2.1, other 2.9) | 40.6 | Capitalized software, net | 4.4 | 4.7 |
| Gross profit (72 percent) | 104.4 | Property and equipment, net | 2.4 | 2.4 |
| Research and development (engineering personnel expensed 13.7, development tooling 1.1, product management 1.6) | 16.4 | Total assets | 82.8 | 101.1 |
| Sales and marketing | 46.0 | Payables and accrued | 6.0 | 6.2 |
| General and administrative (including IT) | 21.0 | Accrued compensation | 7.0 | 7.3 |
| Operating income (14.5 percent) | 21.0 | Deferred revenue | 54.0 | 55.0 |
| EBITDA (adds amortization 2.1, depreciation 0.8) | 23.9 | Total liabilities (no debt) | 67.0 | 68.5 |
| Interest income | 1.4 | Shareholders' equity | 15.8 | 32.6 |
| Income tax (25 percent) | 5.6 | | | |
| Net income | 16.8 | | | |

| Fact | Detail |
|---|---|
| Cash flow, FY1 | Operating 20.7 (net income 16.8, amortization and depreciation 2.9, working capital 1.0); capitalized software −2.4; equipment −0.8; financing 0; free cash flow 17.5 |
| Cloud and tooling split | The $4.2M is $3.1M production hosting (cost of revenue) and $1.1M development tooling (R&D) |
| Equity | Low for the company's age because of losses in its early growth years; no distributions |
| Capitalization policy | ASC 350-40 (Northstar's software is provided as a service). Coding and testing on budget-authorized projects that add functionality is capitalized from weekly project codes; maintenance, incident work, prevention, refactoring, and training are expensed. Rate $157,250 per FTE-year (85 percent of $185,000; overhead excluded). Straight-line amortization over three years, company policy. Finance applies the current guidance and is assessing ASU 2025-06 |
| Capitalized engineering cost | FY−2 $1.8M, FY−1 $2.1M, FY0 $2.4M, FY1 $2.4M (about 15.3 FTE-years) |
| FY2 engineering budget draft, weeks 46–48 | Personnel $16.73M at 87 full seats (3 percent merit, $0.15M promotion and market reserve), $16.31M after expected vacancy; cloud and tooling $4.2M flat. Outcome open |
| TR-01 cost scenarios | 120, 190, and 243 engineer-days ($96,000, $152,000, $194,400 at $800 a day); expensed, since it adds no functionality. Funding open |

### Risk, security, and compliance (Chapter 53)

| Week | Fact |
|---|---|
| — | Northstar holds no SOC 2 report or other independent attestation; the annual penetration test is its only external assurance. Card payments use the processor's hosted fields and tokens, so Northstar stores no card numbers; the card data scope has not been reviewed since the integration was built |
| — | Finance keeps the corporate risk register: 12 risks on a five-by-five matrix, reviewed by the audit committee twice a year. Technology is one line, "Cyber attack or IT outage" (owner Marta Kowalczyk, score 12, amber), unchanged at its last four reviews |
| — | Joon Park's quarterly report to Marta Kowalczyk covers penetration test findings, phishing click rate, and training completion |
| 42 | Greg Tanaka reports a prospect worth about $310,000 a year whose terms require a SOC 2 report within 12 months of signing |
| 43 | Margaret Lin asks for a technology risk session at the audit committee's week 50 meeting. Victor asks the director to draft an enterprise technology risk register with Marta Kowalczyk and Joon Park for his review in week 48 |
| 44 | Security snapshot: 20 components scanned in the pipeline and 4 weekly; 2 open criticals, both under exceptions (auth-svc, known-exploited and restricted at the load balancer, under the exception the director recorded in quarter 1 "until the migration", to which Joon Park added a week 52 date in week 44 without a new signature; one Core item waiting on TR-01); 9 highs past the 90-day service level; tier 1 with an SBOM per build 14 of 15 (all but auth-svc); tier 1 with signed provenance 0 of 15; 2 script services with secrets in plain files |
| 44 | Joon Park's tally over the trailing four quarters: 34 security questionnaires (11 asked for an independent assurance report, 6 for an SBOM or SSDF evidence), about 14 hours each of IT security and engineering time |
| 47 | The director's draft register ER-01 to ER-09 (22 candidate items consolidated), three draft appetite lines, a draft security strategy with five year-2 outcomes, and SOC 2 options A (audit in year 2), B (readiness in quarters 5–6, decision at week 78), C (evidence library only), with illustrative audit quotes of $45,000–$70,000 a year, a compliance tool at about $30,000 a year, and year-1 internal effort of about 0.5 FTE in engineering and 0.5 FTE in IT; B recommended. Marta Kowalczyk objects to moving security out of IT; three reporting options are recorded without a recommendation |
| 48 | Victor keeps the nine risks and three lines and says he will either sign the auth-svc exception before week 50 or have auth-svc restricted further. Outcomes open |

### Data and AI (Chapter 54)

| Week | Fact |
|---|---|
| 41 | Farah Haddad's warehouse inventory: 46 nightly pipelines, 29 reading Core tables directly through read replicas; 212 tables, 38 described, no dataset with a named owner of meaning; the nightly load failed or loaded partially on 11 of quarter 3's 91 nights (7 traced to Core schema changes); month-end revenue differs from Finance's close by 0.3 to 0.6 percent, reconciled by hand in about two days a month; customer personal data in 14 unclassified tables |
| 41 | A top-40 customer's renewal questionnaire asks about generative AI in development and in the product and whether customer data reaches AI providers |
| 42 | An anonymous AI-use survey, separate from the developer-experience survey: 63 of 80 respond; 41 use an AI coding assistant weekly, 29 of them on personal or free accounts; 17 have pasted Northstar code into a chat tool; 6 have pasted customer data; 34 of the 41 weekly users say AI makes them faster. No AI policy exists |
| 43–45 | Requests: Greg Tanaka, an AI order assistant for two open deals; Amara Okafor, AI order checking; Sofia Alvarez, the support tool's summarization add-on; Rajiv Menon, whether assistants let the workforce plan hold two backfills open |
| 47 | The director's one-page AI position for Victor: an interim AI-assisted engineering policy, a staggered coding-assistant trial in quarter 5 (three teams weeks 53–58, three weeks 59–64), order checking with non-AI fixes first, the order assistant deferred with a trigger, support summaries subject to terms review, no backfills held open on AI. All decisions open |

### Board preparation (Chapter 55)

| Week | Fact |
|---|---|
| 46–48 | Victor gathers directors' concerns in calls: Anders Holm, whether the gains depend on a few people; Natalie Brooks, what a buyer's technology diligence would find (a readiness question; no transaction is planned); Samuel Osei, whether flat headcount can carry the roadmap; Margaret Lin, whether measures mean the same thing every quarter; David Ferrante, the payment path, the availability miss, and Core's unsupported framework, with an offer to review the architecture himself |
| 48 | The draft engineering page carries both reliability headlines side by side (Victor's "below 10 per quarter" and the director's week 42 counter); the choice is open |
| 49 | The board pack goes to directors at the end of week 49 |
| 50 | Helena Marsh presents the year-2 operating plan and budget envelope for approval; Victor's agenda item is the three-year technology strategy, for discussion. The audit committee's technology risk session is held the same week. Outcomes not recorded |

### Rules and processes inventory (Chapter 59)

| Week | Fact |
|---|---|
| 50–51 | The director drafts for Victor an inventory of the organization-wide rules and standing processes created or inherited in year 1, with load, evidence, and a draft verdict for each (keep, instrument, decide, retire, converge). It excludes the meeting calendar, whose redesign (drafted week 22, reviewed week 24, proposed for week 27) has no recorded outcome. Findings: the ten-item pull request checklist is still in Core's merge request template; nobody records what the tier 1 migration rehearsals find. It does not find the $150,000 offset, and the capacity it identifies (about 1 FTE from build consolidation) is not yet available. Whether Victor uses it, and every verdict, is open |

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
| Tier 1 list | The 15 proposed tier 1 components are used for all counts in quarter 1. notification-svc moves to tier 2 and to Orders from quarter 2 | 24 |
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
| Core change failure rate | 31% | 22% | 27 |
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

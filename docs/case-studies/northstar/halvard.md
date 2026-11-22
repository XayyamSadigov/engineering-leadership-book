# Halvard Systems: the comparison company

Halvard Systems is the book's second fictional company. It is used where Northstar is too small to
show a problem: organizations of several hundred engineers, several vice presidents, and an
executive layer above them. Like Northstar, it is invented, and every number on this page is an
assumption for teaching, not a benchmark. The people are listed on the [cast](cast.md) page.

## Shape

Used in Chapter 35.

| Fact | Value |
|---|---|
| Business | A multi-product software company |
| Engineers | 500 |
| First-line managers | about 63 (assumed 8 engineers per manager) |
| Directors | about 11 at the planning year (assumed 6 managers per director); 12 are described once the groups are named (Commerce 3, Field Operations 3, Insights 2, Payroll 2, platform 2), plus Streaming after the Corvane acquisition |
| Vice presidents | 5: four product groups and one platform organization |
| Platform organization | 70 engineers (14 percent), because of Halvard's estate of shared services |
| Principal engineers | 7: one per VP group, plus two in a technical direction function |
| Layers | Three management layers (manager, director, VP) between an engineer and the CTO. The CTO is not named |

## Product groups

Used in Chapters 47 and 48.

| Group | Engineers | Detail |
|---|---|---|
| Commerce | 130 | VP Nadia Brennan; 16 first-line managers, 3 directors: Owen Achterberg (Checkout: 5 managers, 41 engineers), Selin Kaya (Catalog and Search: 5 managers, 40 engineers), Joaquín Ferreyra (Merchant Tools: 6 managers, 49 engineers) |
| Second product group: Field Operations | 110 | VP Imani Okonkwo (Chapter 58) |
| Third product group: Insights | 100 | VP Henrik Sørlie (Chapter 58) |
| Fourth product group: Payroll | 90 | VP Ngozi Adeyemi (Chapter 56) |
| Platform organization | 70 | See above |
| Total | 500 | 130 + 110 + 100 + 90 + 70 |

Commerce's year goals: growth in enterprise merchants and fewer failed checkouts. Its run work is
assumed at 32 FTE (Checkout 12, Catalog and Search 8, Merchant Tools 12), leaving 98 FTE investable
(Chapter 47).

## Workforce

Used in Chapter 48.

| Fact | Value |
|---|---|
| Level mix at the start of the planning year | Engineer 190, Senior 245, Staff 58, Principal 7 (500) |
| Planning assumptions | Attrition 12 percent (60 a year); promotions 8 percent of Engineers to Senior, 3 percent of Seniors to Staff |
| Fully loaded cost | Engineer $170,000, Senior $215,000, Staff $270,000, Principal $330,000; payroll at the held mix about $102.9 million |
| Contractors | About 60 vendor engineers on two contracts, outside the 500 |
| Enterprise policies | Six, each owned by a principal engineer: one owning team per production component; tier 1 operational minimums; an auditable pipeline with rollback; vulnerability remediation service levels; a tracked review for every Sev1; no customer date without an estimate and an owner |

Exercises sometimes pose other Halvard situations (a VP of Fulfillment with two directors, a plan for
20 net additions, an SVP layer, two groups with separate deployment platforms, three VPs running
transformation programs). Those are scenarios for the reader and are not part of Halvard's record.

## The year after the planning year

Chapters 56–59 tell four stories set after the planning year above, each inside one group: Payroll
(Chapter 56), Commerce (Chapter 57), Field Operations and Insights (Chapter 58), and the platform
organization with the enterprise policies (Chapter 59). Each group's starting size is the one in the
tables above. Unlike Northstar's quarter 4, these stories record outcomes. No company-wide headcount
after these events is stated.

### Payroll: a failing group and its new VP (Chapter 56)

| Fact | Value |
|---|---|
| Group | The fourth product group, named Payroll: payroll and time-tracking software for customers' hourly workforces. Weeks count from Ngozi Adeyemi's first day |
| Leaders | VP Ngozi Adeyemi, hired from outside after her predecessor left; principal engineer Hiroshi Takeda |
| Pay Calculation | Director Rhys Gallagher; 6 manager seats, 50 engineers. He has been about nine years at Halvard, built much of the pay calculation engine, and ran all 7 Sev1 bridges in the quarter before she arrived |
| Time and Attendance | Director Beatriz Quintero; 5 manager seats, 40 engineers |
| Manager seats | 11, 2 vacant at arrival |
| State at arrival: incidents | Sev1 and Sev2 rising 9, 16, 23 a quarter (last quarter 15 in Pay Calculation, 8 in Time and Attendance; 14 change-induced, 11 customer-detected, 7 Sev1) |
| State at arrival: customers | Pay-run path availability 99.71 percent against a 99.9 percent contract; 3 of the 10 largest customers in formal escalation, one ($4.2M ARR) renewing in week 30 |
| State at arrival: people and delivery | 17 departures in 12 months (11 from Pay Calculation, including two managers); unplanned work 45 percent (40.5 FTE); 6 of 22 committed roadmap items delivered in two quarters |
| State at arrival: standards | Tier 1 minimums met by 5 of 12 tier 1 components; tracked reviews for 4 of 11 Sev1s; 9 of 14 customer dates given before an estimate |
| State at arrival: reporting | Time and Attendance had reported its integration roadmap on track for three months before it slipped by a quarter |
| Day-30 promise to the CTO | A weekly incident count with severity audit, every Sev1 reviewed on time, no customer date without an estimate; explicitly not yet a reorganization, a rewrite, or a group-wide process |
| Day 90 | Sev1 and Sev2 from 23 to 15 (not yet distinguishable from chance); customer-detected from 11 to 6; escalations from 3 to 1; 2 departures |
| Not recorded | Availability for the quarter, the week 30 renewal, any decision about Rhys Gallagher or Beatriz Quintero |

Weeks 1–4:

- an incident commander rotation of 8, trained by Rhys Gallagher;
- every Sev1 reviewed within 10 working days with a manager-owned action (Hiroshi Takeda owns the
  standard);
- weekly written status to the three escalated customers, sent by customer success leads;
- no customer date without an estimate and an owner, with Ngozi Adeyemi signing exceptions;
- stay conversations with the six engineers who hold most knowledge of the pay calculation engine.

### Commerce: the Checkout outage (Chapter 57)

| Fact | Value |
|---|---|
| People | Ingrid Solberg (staff engineer in Checkout, incident commander); Mireille Dubois (Halvard's head of communications) |
| Checkout | About 9,000 merchants, 8,600 taking cards through it; cards are 64 percent of attempts. Two Sev1 incidents in the two quarters before the outage |
| Contract | 99.95 percent monthly availability; credits of 10 percent of the month's checkout fees below 99.95 and 25 percent below 99.0; a minute is unavailable when more than 5 percent of attempts fail |
| Standards before | First customer notice within 15 minutes of declaring a Sev1, but status posts needed a vice president's approval. Routing configuration changed through an admin console outside the auditable pipeline; nodes cache it for up to 60 minutes |
| Impact: failures | 1,500 attempts a minute; 168,480 failed card attempts; about 112,000 sessions, 65,000 never completed (about $4.6M of merchant sales at $71, an upper bound) |
| Impact: support and contract | About 2,300 tickets in three hours against 150 a day; 200 unavailable minutes, 99.54 percent for the month; contractual credits $380,000 (10 percent of $3.8M) |
| Afterwards | Merchant message at 20:00; the macro corrected to every recipient the next morning |
| Compensation | Options $380,000, $470,000 (credits plus 15 percent of the $0.6M monthly checkout fees of the 140 merchants with live promotions), $760,000; the CTO approved $470,000 |

The outage, on a Tuesday (times UTC):

| Time | Event |
|---|---|
| 14:05 | Change |
| 14:10 | Failures begin |
| 14:18 | Merchant complaint |
| 14:23 | Alert |
| 14:26 | Sev1 declared |
| 14:44 | Nadia Brennan joins the bridge |
| 14:50 | She moves to an executive channel |
| 14:52 | First status post (11 minutes late) |
| 15:20 | Support macro wrongly blaming "a third-party payment provider" sent to about 1,100 tickets |
| 15:35 | Cause found |
| 15:41 | Revert |
| 16:05 | Status names Halvard's own change |
| 17:00 | Full failure ends |
| 17:30 | Error rate under 5 percent |
| 17:55 | Normal |

### Field Operations: the reduction (Chapter 58)

| Fact | Value |
|---|---|
| Group | The second product group, named Field Operations: software for scheduling and dispatching field technicians. VP Imani Okonkwo; HR business partner Leah Marchetti |
| Directors | Mateo Rinaldi (Dispatch, 5 managers, 38 engineers), Ruth Halloran (Mobile Workforce, 5 manager roles with one vacant, 40), Tobias Engel (Classic Scheduler, 4 managers, 32) |
| Decision | End new development on Classic Scheduler (on-premises, license revenue declining for three years); honor support contracts for three more years; move customers to Dispatch. Finance's first proposal, 15 percent across all three teams (about 17 engineers), was rejected |
| Plan: sustaining team | A 14-FTE sustaining team (security 2, tier 1 operations 4, escalations 3, migration tooling 5) for 21 components, 3 of them tier 1 |
| Plan: roles | 18 roles end; 4 people placed in vacancies (2 Dispatch, 2 Mobile Workforce); 14 engineers separated (6 Engineer, 7 Senior, 1 Staff; 11 in the US, 3 at an EU site where consultation adds 5 weeks) |
| Plan: resulting shape | Classic managers 4 to 2. Field Operations becomes 96 engineers (40, 42, 14) and 12 managers |
| Money | $2,795,000 a year removed; one-time cost assumed at 25 percent ($698,750), payback 3.0 months |
| Cheaper sources checked first | None of Halvard's vendor contracts staffs Field Operations; its four open requisitions were used to place affected people |
| Consultation | Halvard consults employee representatives before any dismissal as policy; at the EU site this follows counsel's reading of national law. The 4 EU roles are below the collective-redundancy directive's thresholds and the 11 US separations below WARN's |
| Ownership check | The first draft left 5 of 21 Classic components uncovered, including the tier 1 license server; two selections changed, and 3 departing engineers took paid two-week transition contracts for 3 low-change components |
| Managers | Of the two Classic manager roles that ended, one manager filled Mobile Workforce's vacant manager role and one was separated |
| Results: first quarter after | 5 voluntary departures (3 from the sustaining team), Classic Sev1 and Sev2 from 2 to 4, understanding scores 71 percent favorable elsewhere against 38 in Classic. All four Classic incidents got blameless reviews; excess attrition cost about $215,000 |
| Response | A written three-year mandate and 3 internal transfers from Dispatch (Dispatch to 37, Classic back to 14) |
| Results: second quarter | 3 departures, Classic incidents back to 2, Classic score 54 percent |

### Insights: the Corvane acquisition (Chapter 58)

| Fact | Value |
|---|---|
| Group | The third product group, named Insights: reporting and forecasting products. VP Henrik Sørlie; directors Esther Castellanos (Reporting, 6 managers, 52 engineers) and Kenji Iwasaki (Forecasting, 6 managers, 48) |
| Corvane | 34 engineers and 4 managers building a streaming event analytics engine; founder and CTO Dalia Ferraz. 11 production services (2 tier 1) on another cloud provider with its own pipeline and an on-call rotation of 8; 6 services known by one or two people, concentrated in 7 key engineers |
| Deal | Thesis: ingest Halvard's event volumes within two quarters, keep Corvane's customers, embed the engine in Reporting within six months. The CTO had the migration estimate (22 engineer-quarters, about $1,182,500) added to the deal cost |
| Integration: structure | Corvane becomes Streaming, a third Insights unit led by Dalia Ferraz as director (Insights 134 engineers, 16 managers at close) |
| Integration: enterprise policies | Phased in: Sev1 review and remediation service levels from day 1, ownership register in week 1, tier 1 minimums by month 6, auditable pipeline by month 9, the estimate-and-owner rule from close |
| Integration: leveling | In month 2: 11 Engineer, 19 Senior, 4 Staff ($7,035,000 a year); one key engineer moved from Senior to Staff, one stayed Senior with a written development plan |
| Month 6 | Insights at 132 engineers; 32 of 34 remain (one key engineer left in month 4); one Sev1 in Corvane services; first embedded feature in month 5; a decision record to migrate the four costliest services first and revisit the rest a year later |

### Platform organization: the budget cut (Chapter 59)

| Fact | Value |
|---|---|
| People and shape | VP of Platform Gwen Abernathy; principal engineer Arjun Mehta (owns the tier 1 minimums and auditable pipeline policies). Two unnamed directors: Developer Platform (5 managers, 38 engineers) and Infrastructure (4 managers, 32) |
| The cut | A 10 percent cut for the year under a company cost program, from about $18.0M ($14.4M of people at $205,800 average plus $3.6M of internal cloud, licenses, and vendor support) to $16.2M. Measured at exit run-rate, reported quarterly. Separate from the Field Operations reduction |
| Funding | About 8 departures left unfilled ($1,646,400 run-rate), tool consolidation ($420,000 a year), legacy tool retired at mid-year ($350,000 a year): run-rate $2,416,400 against the $1.8M cut. Deployment Tools merges into CI and CD; managers 9 to 8 |
| Change board evidence | Of about 3,000 requests in four quarters, 41 sent back (35 for missing form fields, 6 for clashing with another change on the same shared system); its clash detection replaced by an automated change calendar that flagged 9 clashes in quarter 2 |
| Tier 1 attestation | Quarterly spreadsheet for 210 tier 1 components: about 840 hours a year of owning teams' time and 20 days of platform compilation |
| Compliance pack detail | Two platform engineers, four days a month, compiled by hand from four tools |
| Platform leadership meeting | Weekly, 13 people (VP, 2 directors, 9 managers, principal), 60 minutes, about 40 minutes of status; decisions recorded in about one meeting in three |
| Duplicate tools | Licenses renew at the start of quarter 2; consolidation saves $420,000 a year and about 1.5 FTE of operations |
| Legacy tool migration | Moving its 23 services to the standard pipeline costs product groups about 46 engineer-weeks (2 each) |
| In-year funding | $1,313,200 ($823,200 from unfilled seats, $315,000 from consolidation, $175,000 from retiring the legacy tool), $486,800 short of the in-year $1.8M; the run-rate exceeds the cut by $616,400 |
| Deployment Tools team | A manager and 6 engineers (4 maintained the legacy tool); on the merge, its manager chooses the staff track or the next manager vacancy |
| Director layer | Both directors kept despite Finance's question about a single director for 8 managers; review if either area falls below three managers |
| Corvane and the platform | Corvane's onboarding (Chapter 58) was funded in the deal and staffed by Streaming's engineers; platform support sits inside the CI and CD team's roadmap |
| Working-hours assumption | 1,840 hours per engineer-year (230 days × 8) |
| Results: change board | Suspended in quarter 2 and then deleted: median wait under 1 working day, change-triggered Sev1 and Sev2 at 5 and 4 a quarter against about 4.75 before |
| Results: compliance pack | Replacing the compliance pack with a dashboard raised findings past their service level from 12 to 31 in quarter 2; a monthly 20-minute review with each VP's delegate was restored |

Overhead found in the platform organization:

- a weekly change advisory board: 12 people, 90 minutes, about 60 requests a week, about 1.7 FTE in
  all; it had approved all 19 change-triggered Sev1 and Sev2 incidents in platform components;
  median wait 3 working days;
- a monthly compliance pack (0.42 FTE);
- a quarterly tier 1 attestation spreadsheet;
- duplicate artifact repositories and a self-hosted log store;
- a legacy deployment tool for 23 services under exemptions, kept by 4 engineers with $350,000 a
  year of vendor support.

# Glossary

This page defines the terms the book uses most, in plain words, for a reader with an engineering
background and no training in management, finance, or psychology. Terms are grouped by subject; the
A–Z index below links every entry. Each entry gives the meaning the book uses, the unit where there is
one, and a link to the chapter section that teaches it in full. Where two chapters use a word in
different senses, the entry gives both and says which chapter uses which. Northstar and Halvard
entries describe the book's fictional companies, not real ones.

## A–Z index

**A:** [ADR-0001](#adr-0001), [Architecture decision record (ADR)](#architecture-decision-record-adr), [ARR](#arr), [Attrition and regretted attrition](#attrition-and-regretted-attrition), [Audit committee](#audit-committee)

**B:** [Blameless review](#blameless-review), [Board pack](#board-pack), [Budget envelope](#budget-envelope)

**C:** [Calibration](#calibration), [Capability trap](#capability-trap), [Capitalized versus expensed software](#capitalized-versus-expensed-software), [Career ladder](#career-ladder), [CD3 and WSJF](#cd3-and-wsjf), [Change failure rate](#change-failure-rate), [CISO](#ciso), [Cognitive load](#cognitive-load), [Constraint](#constraint), [Contract test](#contract-test), [Conway's law and the reverse Conway maneuver](#conways-law-and-the-reverse-conway-maneuver), [Core](#core), [Cost of delay](#cost-of-delay), [Customer-detected share](#customer-detected-share), [Cycle time](#cycle-time)

**D:** [Decision log](#decision-log), [Decision rights](#decision-rights), [Dependency link](#dependency-link), [Deployable unit](#deployable-unit), [Developer experience (DevEx)](#developer-experience-devex), [Discount rate and hurdle rate](#discount-rate-and-hurdle-rate), [DORA metrics](#dora-metrics), [Due diligence](#due-diligence)

**E:** [EBITDA](#ebitda), [Effect size (d, g)](#effect-size-d-g), [Engineer-week, engineer-day, engineer-year](#engineer-week-engineer-day-engineer-year), [Error budget and burn rate](#error-budget-and-burn-rate), [Escalation path](#escalation-path), [Escaped defect](#escaped-defect), [Estate](#estate), [Evidence labels](#evidence-labels)

**F:** [Feature flag](#feature-flag), [Forecast, target, and commitment](#forecast-target-and-commitment), [FTE](#fte), [FTE-quarter](#fte-quarter), [Fully loaded cost](#fully-loaded-cost)

**G:** [Gross margin](#gross-margin)

**H:** [Halvard Systems](#halvard-systems), [Horizons](#horizons)

**I:** [INC numbers](#inc-numbers), [Incident commander](#incident-commander), [Incident review](#incident-review)

**K:** [Known-exploited vulnerability (KEV)](#known-exploited-vulnerability-kev)

**L:** [Layer](#layer), [Lead time](#lead-time), [Leverage point](#leverage-point), [Little's law](#littles-law)

**M:** [Meta-analysis](#meta-analysis), [Metric gaming (Campbell's law, Goodhart's law)](#metric-gaming-campbells-law-goodharts-law)

**N:** [Net present value (NPV)](#net-present-value-npv), [NIST CSF](#nist-csf), [Northstar Technologies](#northstar-technologies), [Not yet](#not-yet)

**O:** [OKR](#okr), [Operating expense](#operating-expense), [Operating plan](#operating-plan), [Operational review and operating review](#operational-review-and-operating-review), [Opportunity cost and sunk cost](#opportunity-cost-and-sunk-cost)

**P:** [Paved road](#paved-road), [Percentile forecast and Monte Carlo simulation](#percentile-forecast-and-monte-carlo-simulation), [Performance improvement plan (PIP)](#performance-improvement-plan-pip), [Planned case and cautious case](#planned-case-and-cautious-case), [Prevention allocation](#prevention-allocation), [Prevention point](#prevention-point), [Psychological safety](#psychological-safety)

**Q:** [Quality engineer](#quality-engineer)

**R:** [Re-rating](#re-rating), [Recurrence](#recurrence), [Register IDs](#register-ids), [Reinforcing and balancing loops](#reinforcing-and-balancing-loops), [Release train](#release-train), [Renewal commitments](#renewal-commitments), [Requisition](#requisition), [Risk appetite](#risk-appetite), [Risk register](#risk-register), [Run-rate](#run-rate)

**S:** [SBOM](#sbom), [Scorecard](#scorecard), [Seat](#seat), [Service credits](#service-credits), [Severity (Sev1, Sev2, Sev3)](#severity-sev1-sev2-sev3), [Severity audit](#severity-audit), [Single point of knowledge failure](#single-point-of-knowledge-failure), [Skip-level](#skip-level), [SLI, SLO, and SLA](#sli-slo-and-sla), [SLSA](#slsa), [SOC 2](#soc-2), [SPACE](#space), [Span of control](#span-of-control), [SSDF](#ssdf), [Staff-plus engineer](#staff-plus-engineer), [Stay interview](#stay-interview), [Stock and flow](#stock-and-flow), [Structured interview](#structured-interview), [Succession coverage](#succession-coverage)

**T:** [Team charter and working agreement](#team-charter-and-working-agreement), [Team types and interaction modes](#team-types-and-interaction-modes), [Technical debt (principal and interest)](#technical-debt-principal-and-interest), [The continuation](#the-continuation), [The five constraints](#the-five-constraints), [The mandate](#the-mandate), [Tier 1](#tier-1), [Tier 1 operational minimums](#tier-1-operational-minimums), [Top-40 customers](#top-40-customers), [Transition cost](#transition-cost)

**U:** [Unfunded list](#unfunded-list), [Unplanned work](#unplanned-work)

**V:** [Validity coefficient](#validity-coefficient), [Value channel and urgency profile](#value-channel-and-urgency-profile), [Velocity and story points](#velocity-and-story-points), [Vesting](#vesting)

**W:** [Warranty, indemnity, and escrow](#warranty-indemnity-and-escrow), [Weeks, quarters, and years](#weeks-quarters-and-years), [Work in progress (WIP) and WIP limit](#work-in-progress-wip-and-wip-limit)

## Money and business

### ARR

Annual recurring revenue: the annualized value of the subscription contracts in force at a moment. It
is a run rate, not revenue earned over a period, so it differs from the revenue line whenever the
business grows or shrinks. Churn is ARR lost when customers do not renew or buy less; in a
subscription business, reliability shows up at renewal rather than at delivery. Unit: dollars per year.
Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#reading-a-business-model)
and [Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Gross margin

The share of revenue left after the costs of delivering the service (hosting, support, payment fees,
service credits). Cloud cost and incident load reduce it directly. Unit: percent of revenue. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#reading-a-business-model).

### Service credits

Money a provider refunds or deducts from an invoice when it misses a contractual commitment such as
availability. Credits are netted against revenue, so a dollar of credit avoided is worth a full dollar.
Unit: dollars. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#reading-a-business-model).

### Operating expense

The running costs of the business that appear in the income statement in the period they occur:
research and development (most engineering salaries), sales and marketing, and general and
administrative costs. When a CFO asks for "flat operating expense", this is the line meant. Unit:
dollars per year. Taught in
[Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Operating plan

The company's plan for the coming year: its financial targets, headcount, and budget, usually approved
by the board before the year starts. Engineering's part is a page of the plan and a share of its budget.
At Northstar the board is asked to approve the year-2 operating plan in week 50. Taught in
[Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-engineering-budget).

### Budget envelope

The total spending limit the board approves with the operating plan. Decisions inside the envelope
stay with management; anything outside it goes back to the board or the CFO. At Northstar the year-2
organization, the quality continuation, and the workforce plan are all decided inside the envelope.
Unit: dollars per year. Taught in
[Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-engineering-budget).

### Run-rate

A current amount projected forward as if it continued for a full year. A cost's run-rate is what a full
year at today's level would cost, which differs from this year's actual spend whenever something
changes mid-year: a seat left empty from month six saves half its cost this year and all of it in the
run-rate. ARR is the revenue run-rate of contracts in force. Unit: dollars per year. Taught in
[Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Capitalized versus expensed software

Expensing records a cost in the income statement when it occurs. Capitalizing records qualifying
software work as an asset and spreads its cost over its useful life as amortization, a yearly non-cash
charge. Which work qualifies is set by accounting standards (ASC 350-40 for internal-use and cloud
software in the US, IAS 38 under IFRS) and decided by finance; capitalization changes reported profit,
not cash or capacity. Taught in
[Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#capitalized-versus-expensed-software).

### EBITDA

Earnings before interest, tax, depreciation, and amortization. Because it adds amortization back,
capitalizing more software raises EBITDA by the full capitalized amount, which makes capitalization a
board topic wherever a company is valued on EBITDA. Unit: dollars. Taught in
[Chapter 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Fully loaded cost

The full yearly cost of employing one person: salary plus benefits, payroll taxes, and the other costs
that come with a seat. Northstar's average is $185,000 per engineer per year, the rate the book uses to
convert capacity into money. Unit: dollars per engineer-year. Introduced on the
[Northstar overview](case-studies/northstar/index.md#the-company) and used in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#opportunity-cost-and-sunk-cost).

### Cost of delay

The value lost per unit of time while a piece of work is not done: revenue not earned, cost not saved,
risk not retired. Its shape matters: some items lose a steady amount each week, others lose nothing until
a deadline and then a great deal. Unit: dollars per week. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#cost-of-delay-definition-shape-and-origin)
and [Chapter 15](parts/04-execution/15-planning-prioritization-and-delivery-methods.md#prioritization-as-economics).

### CD3 and WSJF

Two ways to rank work by cost of delay. CD3 (cost of delay divided by duration) uses estimated money and
time; WSJF (Weighted Shortest Job First, from the SAFe framework) uses relative scores for the same
ratio. Fixed-date items are not ranked this way; they are scheduled backward from their date. Taught in
[Chapter 15](parts/04-execution/15-planning-prioritization-and-delivery-methods.md#prioritization-as-economics).

### Value channel and urgency profile

Two labels the book's business case attaches to each benefit. The **value channel** says how the
benefit reaches the company: increase revenue, protect revenue, reduce costs, or avoid costs. The
**urgency profile** says how its value changes with delay, from long-lived benefits whose peak is not
affected by a slip to work whose value drops sharply after a fixed date. Together they make cost of
delay comparable across items. Defined in the
[technology investment business case](templates/technology-investment-business-case.md) template.

### Opportunity cost and sunk cost

Opportunity cost is the value of the best alternative a choice gives up. With fixed headcount, the
opportunity cost of a project is the value of the work those engineers would otherwise have done, usually
the cost of delay of the displaced item, not their salary. A sunk cost is money or effort already spent
that cannot be recovered; it should not influence what to do next. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#opportunity-cost-and-sunk-cost).

### Net present value (NPV)

The value today of a project's future cash inflows minus the value today of its outflows, after
discounting later money (see the next entry). Positive means the project earns more than the company's
required return. The simpler payback period (time to recover the initial cost) ignores the time value
of money and everything after the payback date. Unit: dollars. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#a-common-frame-payback-net-present-value-and-options).

### Discount rate and hurdle rate

The yearly rate used to shrink future money to its value today, because a dollar later is worth less
than a dollar now. In theory it is the firm's cost of capital; in practice use the rate finance sets, its
hurdle rate (Northstar uses 10 percent). Unit: percent per year. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#a-common-frame-payback-net-present-value-and-options).

## Capacity and planning

### FTE

Full-time equivalent: one person's full working time, used to count capacity regardless of how it is
split between people (two people at half time are 1 FTE). Most capacity tables in the book are in FTE
averaged over a quarter. Unit: FTE. Taught in
[Chapter 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#funding-the-work).

### FTE-quarter

One FTE for one quarter of 13 weeks, so 1 FTE-quarter equals 13 engineer-weeks (62 FTE-quarters are 806
engineer-weeks in Chapter 38). It measures the size of a body of work, where FTE measures a rate of
capacity. Unit: FTE-quarters. Taught in
[Chapter 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#engineering-organization-example).

### Seat

One funded position in the headcount, whether filled or vacant. Headcount limits are counted in seats:
Northstar's engineering organization has 87 (80 engineers, 6 managers, and the director), and the
"87-seat rule" means a new role, such as a VP or a new manager, costs an existing seat, usually an
engineer's. A seat left empty saves money but not work. Described on the
[Northstar overview](case-studies/northstar/index.md#executive-and-board-context) and taught in
[Chapter 48](parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md#what-a-workforce-plan-contains).

### Engineer-week, engineer-day, engineer-year

One engineer's working week, day, or year, used to size work. The book's planning rate is $185,000 per
engineer-year, which is about $3,558 per engineer-week ($185,000 ÷ 52) and $46,250 per FTE-quarter.
Where a case uses $800 per engineer-day, that is Finance's day rate ($185,000 ÷ about 230 working days);
it is higher per day than the planning rate because Finance counts only working days. The capitalization
rate of $157,250 per FTE-year is the capitalized share (85 percent) of $185,000. Do not mix the day rate
and the week rate in one calculation. Taught in
[Chapter 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#opportunity-cost-and-sunk-cost).

### Planned case and cautious case

The two capacity scenarios a quarterly plan sets. The planned case assumes unplanned work stays at its
measured level; the cautious case assumes it comes in higher (22 and 28 percent of capacity in
Northstar's quarter 3 plan). The organization commits only what the cautious case can absorb and labels
the rest as targets. Taught in
[Chapter 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#quarterly-planning-at-organization-level).

### Unfunded list

The written list of requested items that the quarterly plan does not fund. It turns "engineering is
slow" into an explicit, shared choice of these items over those. Taught in
[Chapter 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#quarterly-planning-at-organization-level).

### Unplanned work

Work that enters a team's queue after it has decided what to work on and displaces something planned.
The book classifies it into four sources: failure recovery, requests from other teams, toolchain and
environment breakage, and expedited business requests. A team that receives many other teams' requests
and failures is an interrupt sink. Unit: percent of capacity, or FTE. Taught in
[Chapter 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#unplanned-work-visible-and-classified).

### Prevention allocation

Capacity reserved, explicitly and per team, for work that removes the sources of incidents and unplanned
work, rather than funded from whatever slack is left. At Northstar it was 12 FTE in quarters 1 and 2 and
8 FTE in quarter 3. Unit: FTE. Taught in
[Chapter 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#funding-the-work).

### Work in progress (WIP) and WIP limit

Work in progress is everything started and not finished, including items blocked or waiting for review.
A WIP limit caps how many items may sit in each stage of a board. Unit: items. Taught in
[Chapter 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#littles-law-and-work-in-progress).

### Little's law

For a stable system, average lead time equals average work in progress divided by average throughput.
It is a theorem about averages: less work in progress means shorter waits only if throughput holds.
Taught in
[Chapter 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#littles-law-and-work-in-progress).

### Forecast, target, and commitment

A forecast is a probability statement about when work will finish, owned by the team. A target is an
outcome leadership wants. A commitment is a promise of defined scope by a date to someone who will rely
on it, made from the cautious end of the forecast (the 85th or 95th percentile). Taught in
[Chapter 17](parts/04-execution/17-predictability-and-managing-uncertainty.md#forecasts-targets-and-commitments).

### Percentile forecast and Monte Carlo simulation

Throughput is the number of items a team finishes per week. A Monte Carlo simulation repeats a random
experiment many times, here drawing past weeks of throughput, to produce a range of possible finish
dates. A percentile forecast reads that range: "85th percentile, week 30" means 85 percent of simulated
runs finished by week 30. Taught in
[Chapter 17](parts/04-execution/17-predictability-and-managing-uncertainty.md#forecasting-from-throughput).

### Velocity and story points

Story points are a team's relative size for a backlog item ("this is about twice that one"), not a unit
of time. Velocity is the number of points a team finishes per sprint. Both help a team expose
disagreement about scope; neither converts to dates reliably, and comparing them across teams invites
gaming, because each team's points mean something different. Taught in
[Chapter 17](parts/04-execution/17-predictability-and-managing-uncertainty.md#story-points-planning-poker-and-t-shirt-sizes).

### Cycle time

The elapsed time from when someone starts work on an item to when it is done, for finished items. It is
the team's slice of lead time and excludes the wait before work starts. Read it as a percentile ("85
percent of items finish within 9 days"), not an average. Unit: days. Taught in
[Chapter 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#flow-measures-throughput-cycle-time-and-work-item-age).

## Delivery and quality

### Lead time

The book uses two senses, and each chapter says which. **Change lead time** (DORA's "lead time for
changes") is the time from commit to running in production; Northstar's team table and Chapters 14, 15,
and 18 use this sense (Core's median was 19 days at baseline). **Lead time** in Chapter 16 is the time
from when the organization commits to a piece of work to when customers can use it, which is longer and
includes the waits before any code is written. Unit: days. Taught in
[Chapter 18](parts/04-execution/18-measuring-engineering-productivity.md#what-the-dora-metrics-measure)
and [Chapter 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#where-lead-time-accumulates).

### DORA metrics

Delivery metrics published by DORA (DevOps Research and Assessment, now part of Google Cloud). Many
dashboards show "four keys"; the current guide lists five: change lead time, deployment frequency
(deployments per period), failed deployment recovery time, change failure rate, and deployment rework
rate.
They describe one delivery system at a time and say nothing about whether the right things were built.
Taught in
[Chapter 18](parts/04-execution/18-measuring-engineering-productivity.md#what-the-dora-metrics-measure).

### Change failure rate

The share of deployments or releases that fail. DORA calls it "change fail rate" and counts deployments
needing immediate intervention, such as a rollback or hotfix. Northstar counts a release as failed if a hotfix, rollback, or linked
incident follows within 72 hours, which is a different, local definition. Unit: percent. Taught in
[Chapter 23](parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#change-approval-and-pipeline-outcomes)
and [Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#classifying-change-failures-to-find-the-prevention-point).

### SPACE

A framework that treats developer productivity as several dimensions: satisfaction and well-being,
performance, activity, communication and collaboration, and efficiency and flow. The book uses it as a
checklist so that a measure set does not cover only one dimension. Taught in
[Chapter 18](parts/04-execution/18-measuring-engineering-productivity.md#space-a-checklist-of-dimensions).

### Developer experience (DevEx)

How developers experience their daily work and its friction, usually measured along feedback loops,
cognitive load, and flow state, combining surveys with system data. It points at causes a manager can
change. Taught in
[Chapter 18](parts/04-execution/18-measuring-engineering-productivity.md#developer-experience-devex).

### Escaped defect

A defect found by a customer after release rather than by any check before it. Northstar counts
customer-reported bug tickets confirmed as defects (212 in the baseline quarter, 38 percent of them
regressions of behavior that used to work) and classifies each by its detection point: the earliest step
at which a reasonable check would have caught it. Unit: count per quarter. Taught in
[Chapter 19](parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md#detection-points-tell-you-who-should-own-a-check).

### Quality engineer

A quality specialist who sits in a product team and owns test strategy for the team's risk areas, does
exploratory testing, coaches developers, and builds automation, rather than running every check
personally. At Northstar the seven QA engineers became quality engineers in product teams from week
10. Taught in
[Chapter 19](parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md#the-four-ownership-models) and
[Chapter 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#changing-roles-without-losing-the-people).

### Technical debt (principal and interest)

The accumulated cost of design and code that no longer fits the work. Principal is the cost of removing
it; interest is the recurring cost of living with it, in engineering time and in risk such as
incidents. The book's rule: use the metaphor to communicate and the economics to decide. Unit: interest
in hours per period. Taught in
[Chapter 21](parts/05-engineering-quality/21-technical-debt.md#measuring-interest-instead-of-ugliness).

### Paved road

The supported default way to build and run a service: a template with health checks, logging, and alerts,
and a shared pipeline that runs the agreed checks. Teams on it meet most standards without thinking.
Taught in
[Chapter 20](parts/05-engineering-quality/20-engineering-standards-and-their-governance.md#paved-roads-before-review-boards).

### Contract test

A test at a boundary between services. In consumer-driven contracts, each consumer states the parts of a
provider's interface it relies on as executable expectations, and the provider runs them in its own
build, so a breaking change fails there with the consumer named. Taught in
[Chapter 22](parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md#contracts-at-boundaries).

### Feature flag

A runtime switch between code paths. It separates deploying (moving code to production) from releasing
(exposing behavior to users), and every flag is a source of risk to manage and later remove. Flags enable
progressive delivery, such as a canary that sends a small share of traffic to the new version first.
Taught in
[Chapter 23](parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#flags-separating-deploy-from-release).

### Release train

A release that leaves on a fixed schedule carrying every change that is ready. Northstar's Core shipped on
a two-week train, each preceded by a three-day manual regression pass of about 1,900 test cases; it moved
to weekly from week 5 of the first quarter. Taught in
[Chapter 23](parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#practical-playbook).

## Reliability and incidents

### Severity (Sev1, Sev2, Sev3)

The rating that sets the response to an incident and later becomes a measure. The book's rules: define
levels by observable customer impact, include a class for wrong data, let anyone raise severity, and
let only the incident commander lower it, with a recorded reason. Northstar's written Sev1 (week 3) is
"the order or payment path unavailable for any customer, or any wrong financial record visible to
customers"; Sev2 and Sev3 are progressively narrower, and the headline count is Sev1 plus Sev2. Anchor
for links: `#severity-sev1-sev2-sev3`. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#severity-definitions-that-resist-reclassification).

### Re-rating

Changing an incident's severity after the fact. Lowering a rating drops the incident out of the Sev1
and Sev2 count, which is why the book lets anyone raise severity but only the incident commander lower
it, with a recorded reason. A headline that re-rating could deliver is misleading. At Northstar the
director re-rated a two-hour payment delay that had been rated Sev3 (week 7). Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#severity-definitions-that-resist-reclassification) and
[Chapter 55](parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#ethics-at-board-level-the-misleading-headline-and-disclosure).

### Severity audit

The weekly check that incidents were rated correctly against the written severity definitions.
Northstar added it to the weekly review in week 7, and the director's proposed board headline is
reported with it so that the incident count is protected from re-rating. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#severity-definitions-that-resist-reclassification).

### Tier 1

The highest of three tiers that assign each component obligations by business impact. At Northstar a
component is tier 1 if it is on the order or payment path, decided outside the owning team (15
components in year 1). Tier 2 and tier 3 carry lighter obligations, for example business-hours on-call
and simpler alerts. Taught in
[Chapter 20](parts/05-engineering-quality/20-engineering-standards-and-their-governance.md#tiering)
and [Chapter 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#operational-readiness).

### Tier 1 operational minimums

The four conditions every tier 1 component must meet at Northstar: a named owning team, complete
user-facing alerts, a runbook for known failures, and an on-call rotation. A fifth requirement,
deployment through an auditable pipeline with automated rollback, is tracked separately as a pipeline
standard. At baseline 3 of 15 tier 1 components met all four. They are the core of operational readiness:
whether people who did not build a service can run it safely. Taught in
[Chapter 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#operational-readiness).

### SLI, SLO, and SLA

A service level indicator (SLI) is a precisely defined measure of some aspect of a service, such as the
share of successful payment attempts. A service level objective (SLO) is the target for an SLI, owned by
engineering and product. A service level agreement (SLA) is a contract that attaches consequences, such
as service credits, to missing a commitment. Northstar's SLA promises 99.9 percent availability per
quarter on the order and payment paths, about 2.2 hours of allowed downtime in 90 days. Taught in
[Chapter 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#sli-slo-sla).

### Error budget and burn rate

The error budget is the unreliability an SLO allows over its window (100 percent minus the target). An
error budget policy, agreed in advance, says what happens when it runs out, such as pausing feature
releases. Burn rate is how fast the budget is being spent; a burn rate of 1 spends exactly the budget
over the window. Taught in
[Chapter 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#error-budgets-as-a-decision-mechanism)
and [Chapter 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#alerting-on-the-budget).

### Incident commander

The person who coordinates an incident: holds the overall state, assigns work, and decides, but does not
debug. Other roles cover operations (changing the system), communications, and planning. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#roles-separate-coordinating-from-fixing).

### Incident review

The structured review held after an incident to understand how it happened and what to change. Other
names for it are postmortem and blameless review; this book says incident review. A good review is
blameless: it looks for contributing factors without blaming an individual or team, so that people keep
reporting what actually happened. The book prefers several contributing factors to a single "root
cause", which stops the search at the last step before failure. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#blameless-review-and-its-critics);
the format is the [incident review template](templates/incident-review.md).

### Blameless review

An [incident review](#incident-review) conducted without blaming individuals. In this book "blameless"
is an adjective, and the review itself is called an incident review.

### Recurrence

An incident whose failure mode was seen before. Northstar had 11 recurrences among 30 Sev1 and Sev2
incidents at baseline, and closed 32 percent of its corrective actions (follow-up tasks from reviews).
Pair closure with recurrence, because trivial actions inflate closure. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#follow-up-actions-and-recurrence).

### Prevention point

The earliest step at which a reasonable, affordable control would have stopped or contained a change
failure: follow-through on an earlier review, a test or contract, a rollout control, or detection and
recovery. Classifying failures this way shows where to invest. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#classifying-change-failures-to-find-the-prevention-point).

### Customer-detected share

The share of incidents first reported by a customer rather than caught by monitoring. The chapters
compute it over Sev1 and Sev2 incidents (47 percent at baseline, 14 of 30); the
[quality scorecard template](templates/engineering-quality-scorecard.md) computes it over Sev1 to Sev3.
Say which. Unit: percent. Taught in
[Chapter 19](parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md#choosing-measures-and-how-each-misleads).

## Security, risk, and compliance

### NIST CSF

The NIST Cybersecurity Framework 2.0, which organizes security outcomes under six functions: Govern,
Identify, Protect, Detect, Respond, and Recover. Use it for gap analysis from your own systems, not as a
checklist to answer row by row. Taught in
[Chapter 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#frameworks-as-maps-not-checklists).

### SSDF

The Secure Software Development Framework (NIST SP 800-218): secure development practices in four
groups (prepare the organization, protect the software, produce well-secured software, respond to
vulnerabilities) that fit into an existing life cycle. Taught in
[Chapter 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#frameworks-as-maps-not-checklists).

### SLSA

Supply-chain Levels for Software Artifacts: a standard with levels on two tracks, Build and Source, that
describe how far you can prove which reviewed source and which build produced a running artifact.
Taught in
[Chapter 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#supply-chain-integrity-with-slsa).

### SBOM

Software bill of materials: a machine-readable list of a product's components, their versions, and their
relationships. Generated at build time, it answers "are we affected by this vulnerability?" in minutes.
Taught in
[Chapter 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#software-bills-of-materials).

### Known-exploited vulnerability (KEV)

A vulnerability that attackers are known to be using, as listed in CISA's Known Exploited
Vulnerabilities catalog. The book's suggested remediation service level for these is 7 days, ahead of
severity scores alone. Taught in
[Chapter 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#dependencies-and-remediation).

### Risk register

A list of risks, each stated as cause, event, and consequence, with an owner, an accepter, a rating, a
treatment, an early indicator, and a review date. An engineering register covers what one organization
can fix; an enterprise register states risks as business consequences and feeds the company's register.
Taught in
[Chapter 30](parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md#the-technology-risk-register)
and [Chapter 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#what-an-enterprise-technology-risk-register-is).

### Risk appetite

A statement of what kinds and amounts of risk the company is willing to carry in pursuit of its goals.
A risk can be reduced, transferred, avoided, or accepted; acceptance must be explicit, by someone with
the authority, and for a stated period. Taught in
[Chapter 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#treatment-decisions-and-who-may-make-them).

### CISO

Chief information security officer: the executive who owns security strategy, risk, and response for the
whole company. Whether a company of Northstar's size needs one, and where security reports, is a CTO
and board question. Northstar has no CISO; its two-person security function sits inside corporate IT,
which reports to the CFO. Taught in
[Chapter 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#security-strategy-with-recognized-frameworks).

### SOC 2

An examination by an independent, licensed accountant of a company's controls relevant to security,
availability, processing integrity, confidentiality, or privacy. Large customers often require a report
in their contracts. Taught in
[Chapter 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#regulation-and-contracts-through-engineering-controls).

### Audit committee

A committee of the board that oversees financial reporting and risk, including technology and security
risk where there is no technology committee. Taught in
[Chapter 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#what-an-enterprise-technology-risk-register-is)
and [Chapter 55](parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#what-a-board-does-with-technology).

## People and careers

### Skip-level

A conversation between a manager's manager and people two levels down. The book's rule: themes go back
to the direct manager, quotes never, so the skip-level checks the system without becoming a back
channel. Taught in
[Chapter 40](parts/09-engineering-directorship/40-the-directors-job.md#building-your-own-signal-sources).

### Structured interview

An interview in which every candidate gets job-relevant questions and each answer is rated against a
written rubric before any discussion. A work sample, in which the candidate does a piece of the real job
under observation, is a common part of a structured loop. Taught in
[Chapter 7](parts/02-people-management/07-hiring-and-structured-interviews.md#what-structure-means).

### Career ladder

A document (also called a leveling guide) that states, for each level, the scope and impact expected and
the behaviors that produce them. It serves the engineer, the manager giving feedback, the promotion
committee, and whoever sets pay ranges. Taught in
[Chapter 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#what-a-ladder-is-for).

### Calibration

Two senses. In careers, a meeting in which managers review promotion cases together against the same
criteria, so a level means the same in every team (Chapter 8). In forecasting, the property that a team
saying "85 percent sure" is right about 85 percent of the time (Chapter 17). Taught in
[Chapter 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#calibration-what-it-fixes-and-what-it-breaks).

### Not yet

The book's term for a declined promotion case delivered as a plan: the decision first, the gap tied to
the ladder, and what would change the answer. Taught in
[Chapter 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#a-not-yet-that-can-be-used).

### Performance improvement plan (PIP)

A formal, time-bound process with written expectations and support for someone not meeting the bar.
Many organizations read it as the first step of an exit, which defeats its purpose. Taught in
[Chapter 9](parts/02-people-management/09-performance-management-and-underperformance.md#the-improvement-process).

### Stay interview

A structured conversation with someone you want to keep: what keeps you here, what would make you leave,
and what one thing you would change. Taught in
[Chapter 10](parts/02-people-management/10-motivation-retention-and-senior-engineers.md#exit-data-stay-data-and-system-data).

### Attrition and regretted attrition

Attrition is the share of people who leave over a period, usually a year. Regretted attrition counts
only the departures the organization would have prevented if it could; whether a departure is regretted
should be decided in a talent review before anyone resigns, not afterwards. An organization-wide rate
can hide a team or a capability losing far more. Unit: percent per year. Taught in
[Chapter 10](parts/02-people-management/10-motivation-retention-and-senior-engineers.md#what-the-turnover-research-supports) and
[Chapter 48](parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md#attrition-vacancy-and-knowledge).

### Requisition

An approved request to hire into a specific seat. A requisition says what the seat is for and what to
look for; holding requisitions open ahead of departures is one of the workforce plan options at
Northstar, and it needs an exception to the 87-seat rule. Taught in
[Chapter 48](parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md#what-a-workforce-plan-contains).

### Vesting

Equity such as stock options or restricted stock units becomes the employee's own over time, usually in
stages over several years; until it vests, leaving forfeits it. Vesting dates shape when people leave
and are a fairness question in reductions. Taught in
[Chapter 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#total-compensation-and-choosing-a-level-at-offer).

### Psychological safety

People's perception of the consequences of taking interpersonal risks at work, such as admitting a
mistake or saying a date is not real. It is not the absence of standards; high-performing teams combine
it with high accountability. Taught in
[Chapter 11](parts/03-high-performing-teams/11-high-performance-trust-safety-and-accountability.md#what-psychological-safety-is).

### Staff-plus engineer

A senior individual contributor (staff, principal, or above) whose job is technical leadership beyond
their own work. Common archetypes are tech lead, architect, solver, and right hand, each with a different
scope and typical failure. Taught in
[Chapter 29](parts/06-technical-leadership/29-staff-and-principal-engineers.md#archetypes)
and [Chapter 1](parts/01-foundations/01-what-engineering-management-is.md#where-staff-plus-engineers-sit).

### Single point of knowledge failure

An area of a team's work that only one person can do safely. The truck factor (or bus factor) is the
smallest number of people whose sudden absence would leave a project in serious trouble. Taught in
[Chapter 12](parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md#single-points-of-knowledge-failure).

### Succession coverage

Whether each critical role has someone who could take it over. Readiness is ready now, ready with
development, interim only, or none; coverage is adequate when a role has someone ready now or interim
plus someone in development, and the cover does not hold another critical role. Taught in
[Chapter 36](parts/07-organization-design/36-reorganizations-evolution-and-succession.md#succession-coverage).

## Organization design

### Span of control

The number of people who report directly to one manager. There is no universal right number; it depends
on how much each report needs from the manager. Taught in
[Chapter 34](parts/07-organization-design/34-spans-layers-and-dependency-mapping.md#why-there-is-no-universal-span).

### Layer

A level of management between an engineer and the person who can decide for the whole organization.
Each added layer costs decision latency and information lost on the way up. Taught in
[Chapter 34](parts/07-organization-design/34-spans-layers-and-dependency-mapping.md#what-a-layer-costs).

### Dependency link

One work item of a week or more in which one team needed another, counted per quarter. A matrix of
dependency links between teams shows where boundaries cost coordination: read across a row for what a
team asked of others, down a column for what others asked of it. Northstar's baseline quarter had 86,
29 of them received by Platform Operations. Unit: links per quarter. Taught in
[Chapter 34](parts/07-organization-design/34-spans-layers-and-dependency-mapping.md#from-dependency-map-to-boundary-design).

### Conway's law and the reverse Conway maneuver

Conway's law: organizations produce system designs that copy their communication structures. The reverse
Conway maneuver designs the organization you want the system to copy; its logic is sound, its evidence
thin. Taught in
[Chapter 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#what-conway-argued-and-the-evidence-since)
and [Chapter 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#the-reverse-conway-maneuver-and-its-evidence-gap).

### Team types and interaction modes

The *Team Topologies* vocabulary: stream-aligned, platform, enabling, and complicated-subsystem teams,
interacting by collaboration (for a set period), X-as-a-service, or facilitation. It is a taxonomy,
not a tested model. Taught in
[Chapter 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#team-types-and-interaction-modes-as-vocabulary).

### Cognitive load

The mental effort a task demands. Applied to teams, a team's responsibilities should fit the load it can
carry. Taught in
[Chapter 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#cognitive-load-origin-and-transfer).

### Team charter and working agreement

A team charter states the team's purpose, boundaries, interfaces, and decision rights. A working
agreement is the set of rules the team enforces on itself, such as review times or on-call swaps.
Taught in
[Chapter 12](parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md#what-a-team-charter-is-and-what-the-evidence-says).

### Decision rights

Who may make which decisions, by what method, and on what record. The book names four methods: decide,
consult, consent, and delegate; role models such as RACI (Responsible, Accountable, Consulted, Informed)
assign them per decision. Taught in
[Chapter 13](parts/03-high-performing-teams/13-decision-making-in-teams.md#four-methods-defined)
and [Chapter 13](parts/03-high-performing-teams/13-decision-making-in-teams.md#decision-rights-made-explicit).

### Transition cost

The capacity lost while people rebuild context, relationships, rotations, and planning rhythm after a
reorganization. Price it before deciding. Unit: engineer-weeks. Taught in
[Chapter 36](parts/07-organization-design/36-reorganizations-evolution-and-succession.md#pricing-the-transition).

## Strategy and governance

### Architecture decision record (ADR)

A short document recording one significant technical decision: its context, the options, what was
chosen, and why, so successors neither accept nor reverse it blindly. Taught in
[Chapter 28](parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#architecture-decision-records).

### Decision log

The organization's record of decisions that belong to no code repository (ownership, capacity splits,
severity definitions), each with decider, options, status, a "needed by" date, and a review trigger.
Northstar's entries are numbered DL-01 onward. Taught in
[Chapter 39](parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md#the-decision-log).

### Escalation path

The route for moving a disagreement to someone with authority over both parties. A clean escalation is
joint (one written case from both sides), goes to the lowest common manager, runs on a clock, and ends
in the decision log. Paging a more experienced incident responder is a different mechanism. Taught in
[Chapter 39](parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md#escalation-paths).

### Operational review and operating review

Two different meetings. The operational review is the director's weekly meeting on incidents,
follow-ups, error budgets, and dated forecasts (Chapters 37 and 39). The operating review is a VP's
monthly meeting with each director on the area's scorecard, funded bets, and staffing (Chapter 47).
Taught in
[Chapter 37](parts/08-management-operating-system/37-cadences-and-leadership-meetings.md#what-the-system-is-made-of)
and [Chapter 47](parts/11-vp-engineering/47-the-vp-of-engineering.md#the-operating-review).

### Scorecard

A short set of measures reviewed on a fixed cadence, covering several areas (outcomes, quality,
delivery, commitments and investment, people) because one can improve while the organization gets
worse. Each measure is paired with another that exposes gaming. Taught in
[Chapter 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#the-organization-scorecard).

### OKR

Objectives and key results: a qualitative objective paired with a few measurable results that would show
it was reached. Taught in
[Chapter 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#what-the-research-says-about-goals-and-about-okrs).

### Horizons

Three kinds of bet: horizon 1 improves the existing business, horizon 2 extends it to new customers or
markets, and horizon 3 creates options for the future. The book treats them as kinds of bet, not as
delivery windows. Taught in
[Chapter 51](parts/12-cto-leadership/51-enterprise-technology-strategy.md#horizons-as-kinds-of-bet-not-as-years).

### Constraint

The one step that limits a system's output; improving anything else does not raise output. Find it with
data on incidents, escaped defects, and the pipeline rather than opinion. Taught in
[Chapter 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#constraints)
and [Chapter 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#finding-the-constraint).

### Capability trap

A loop in which pressure leads people to cut improvement time, capability erodes, performance falls, and
pressure rises further. Taught in
[Chapter 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#the-capability-trap).

### Stock and flow

A stock is anything you could count at a moment, such as engineers who can safely change the ledger. A
flow is a rate that fills or drains it, such as engineers trained per quarter or resignations per year.
A stock changes only through its flows, so it moves slowly, and a large stock can hide an inflow that has
stopped. Taught in
[Chapter 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#stocks-flows-and-slow-change).

### Reinforcing and balancing loops

A reinforcing loop feeds its output back as input, so change in either direction amplifies itself (fewer
people able to respond means more pages per expert and less time to teach). A balancing loop acts on the
gap between a goal and the current state, so it pulls a system toward a level, often one nobody chose.
Taught in
[Chapter 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#feedback-loops).

### Leverage point

A place in a system where an intervention changes its behavior. Changing parameters (numbers such as a
stipend or an allocation) is the weakest kind; changing information flows, rules, goals, and beliefs is
usually stronger. Taught in
[Chapter 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#leverage-points).

### Estate

The full set of systems a technology organization runs: its applications, services, data stores,
infrastructure, and tools. Strategy and risk work is about the estate as a whole, not one system at a
time. Taught in
[Chapter 30](parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md#the-technology-risk-register) and
[Chapter 51](parts/12-cto-leadership/51-enterprise-technology-strategy.md#deliberate-and-emergent-strategy).

### Board pack

The papers a board receives before each meeting: the CEO's report, financials, and items for decision.
Engineering figures usually reach the board through it, so what the pack says and how consistently it
says it each quarter matters more than the meeting. At Northstar the CEO's monthly pack carries the
engineering figures. Taught in
[Chapter 55](parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#what-a-board-does-with-technology).

### Due diligence

The investigation a buyer or investor makes before a deal to check what it is buying. Technology due
diligence looks at the estate, its risks, the people who hold critical knowledge, licenses, and
security, and each finding changes the price, the terms, the integration plan, or the decision to walk
away. Taught in
[Chapter 55](parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#technology-due-diligence).

### Warranty, indemnity, and escrow

Deal terms that turn due diligence findings into money. A warranty is the seller's written promise that
a fact is true; if it proves false, the buyer can claim damages. An indemnity is the seller's agreement
to pay if a named problem later costs the buyer money. Escrow is part of the price held back by a third
party for a period to pay such claims. This is not legal advice. Taught in
[Chapter 55](parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#technology-due-diligence).

## Evidence and research

### Evidence labels

The words the book uses to say how strong the support for a claim is: research finding, industry
research, standard, documented practice, practitioner consensus, expert opinion, this book's
recommendation, and illustrative. Most industry research is correlational: it shows that two things move
together, not that one causes the other. Explained on the
[evidence labels](references/evidence-labels.md) page.

### Meta-analysis

A study that pools the results of many studies on one question, usually correcting for known
distortions, to estimate an average effect. It is only as good as the studies it pools and the settings
they cover. Taught in
[Chapter 7](parts/02-people-management/07-hiring-and-structured-interviews.md#what-selection-research-measures).

### Effect size (d, g)

A number for how large a difference is, measured in units of the spread of the outcome rather than in raw
units, so studies with different scales can be compared. Cohen's d and Hedges' g are two common forms;
Chapter 6 reports feedback's average effect as d = 0.41 and calls it moderate. Taught in
[Chapter 6](parts/02-people-management/06-feedback-conflict-and-difficult-conversations.md#what-the-feedback-research-shows).

### Validity coefficient

In hiring research, the correlation between scores on a selection method and later job performance: 0
means no prediction and 1 perfect prediction. It is an average across studies, not the validity of your
own interview loop. Taught in
[Chapter 7](parts/02-people-management/07-hiring-and-structured-interviews.md#what-selection-research-measures).

### Metric gaming (Campbell's law, Goodhart's law)

The more a measure is used to make decisions about people, the more pressure bends both the number and
the activity it was meant to track; the popular version, "when a measure becomes a target", is called
Goodhart's law. The book pairs every metric with how it is gamed and a second measure that exposes it.
Taught in
[Chapter 18](parts/04-execution/18-measuring-engineering-productivity.md#how-each-metric-is-gamed-and-its-pair).

## Northstar shorthand

### Northstar Technologies

The book's running fictional case: an order-to-cash software company of about 620 people with 80
engineers in six teams, $140M of ARR, and a 99.9 percent availability contract. Described on the
[Northstar overview](case-studies/northstar/index.md).

### Halvard Systems

The book's second fictional company, with about 500 engineers and several vice presidents, used where
Northstar is too small to show a problem. Described on the
[Halvard page](case-studies/northstar/halvard.md).

### The mandate

The CTO's one-sentence brief to the new director: halve Sev1 and Sev2 incidents and meet the 99.9
percent commitment within twelve months, with no net headcount growth, without dropping the two renewal
commitments. Described on the
[Northstar overview](case-studies/northstar/index.md#the-situation-when-you-arrive).

### The five constraints

The rules that hold throughout the case: (1) headcount flat at 80 engineers; (2) the two renewal
commitments keep their dates; (3) no funded rewrite of Core; (4) $250,000 of discretionary tooling
without a business case; (5) any plan that changes the QA engineers' work says what they do next.
"Constraint 3" means the third. Described on the
[Northstar overview](case-studies/northstar/index.md#constraints-that-hold-throughout-the-book).

### Renewal commitments

The two customer commitments the largest renewals depend on: a bulk-ordering feature and an
accounting-system integration, both due in the first two quarters (weeks 19 and 26). Described on the
[Northstar overview](case-studies/northstar/index.md#constraints-that-hold-throughout-the-book).

### Core

Northstar's Java monolith: about 1.4 million lines in eight major modules, three of which (customer,
permissions, scheduler) were changed by four teams and owned by none at baseline. It ships on the
release train; the other fourteen services deploy independently. Described on the
[Northstar overview](case-studies/northstar/index.md#the-system).

### Deployable unit

Something that is built and deployed as one piece. Northstar has 24 components but 17 deployable units,
because Core's modules ship together and count as one. "17 units" in the book means 17 deployable units
(Core counts as one; 24 components in all). Described in the
[baseline data](case-studies/northstar/baseline-data.md#technical-debt-tests-and-the-pipeline).

### Top-40 customers

Northstar's 40 largest customers, which together produce about a third of revenue, about $1.17M of ARR
each. Several renewals and complaints in the case come from this group. Described on the
[Northstar overview](case-studies/northstar/index.md#the-company).

### Weeks, quarters, and years

Week 1 is the director's first week. Quarter 1 (the "transformation quarter") is weeks 1 to 13, quarter
2 weeks 14 to 26, quarter 3 weeks 27 to 39, quarter 4 weeks 40 to 52. The "baseline quarter" is the
quarter before the director arrived. Year 2 is weeks 53 to 104 (quarters 5 to 8); fiscal year 1 (FY1)
matches weeks 1 to 52. Quarter 3 is the latest measured quarter; quarter 4 decisions are open. Described
in the [year 1 record](case-studies/northstar/first-quarter.md).

### INC numbers

Northstar's incident identifiers. INC-401 to INC-430 are the 30 Sev1 and Sev2 incidents of the baseline
quarter, listed in the
[incident file](case-studies/northstar/data/incidents-last-quarter.csv); chapters name each one with a
few words on what happened.

### Register IDs

Short identifiers for items in Northstar's registers and logs. INC- is an incident (see
[INC numbers](#inc-numbers)); DL- is an entry in the organization's decision log; ADR- is an architecture decision record;
TD- is an item on the technical debt register (Chapter 21); TR- is an item on the technology risk
register drafted in quarter 2 (TR-01 is the Core framework migration); ER- is an item on the enterprise
technology risk register drafted in week 47 (ER-01 to ER-09). The number is a label, not a ranking.
Described on the [year 1 record](case-studies/northstar/first-quarter.md).

### ADR-0001

Northstar's first architecture decision record, opened by Li Na Zhou (staff engineer, data and
integration) in week 14: how integrations should read posted ledger data, by reading the tables, through a
versioned export contract, or from ledger posting events. It was still open at week 26. Described on
the [year 1 record](case-studies/northstar/first-quarter.md); the ADR format is taught in
[Chapter 28](parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#architecture-decision-records).

### The continuation

The director's two-year proposal, drafted in week 45, to continue the quality program after year 1:
stage 2 "Hold" (quarters 5 and 6, 6 FTE of prevention, $150,000 of tooling, gate in week 78) and stage 3
"Converge" (quarters 7 and 8, 5 FTE, $100,000 of tooling only if a CI target is chosen, gate in week
104), after a stage 1 gate in week 56, with no headcount request. Each stage ends at a gate where written exit criteria decide whether the next is funded. Taught in
[Chapter 49](parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md#stages-gates-and-exit-criteria).

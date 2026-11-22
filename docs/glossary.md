# Glossary

This page defines the terms the book uses most, in plain words, for a reader with an engineering
background and no training in management, finance, or psychology. Terms are grouped by subject; use
your browser's search to find one. Each entry gives the meaning the book uses, the unit where there is
one, and a link to the chapter section that teaches it in full. Where two chapters use a word in
different senses, the entry gives both and says which chapter uses which. Northstar and Halvard
entries describe the book's fictional companies, not real ones.

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

### Engineer-week, engineer-day, engineer-year

One engineer's working week, day, or year, used to size work. The book prices an engineer-year at
$185,000 and an engineer-week at about $3,558 ($185,000 over 52 weeks). Some chapters (21, 30, 52)
price an engineer-day at about $800 ($185,000 over 230 working days), so five engineer-days cost more
than one engineer-week in those chapters; compare like with like. Taught in
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
(deployments per period), failed deployment recovery time, change fail rate, and deployment rework rate.
They describe one delivery system at a time and say nothing about whether the right things were built.
Taught in
[Chapter 18](parts/04-execution/18-measuring-engineering-productivity.md#what-the-dora-metrics-measure).

### Change failure rate

The share of deployments or releases that fail. DORA counts deployments needing immediate intervention,
such as a rollback or hotfix. Northstar counts a release as failed if a hotfix, rollback, or linked
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

### Blameless review

A review after an incident (also called a postmortem) that looks for contributing factors without
blaming an individual or team, so that people keep reporting what actually happened. The book prefers
several contributing factors to a single "root cause", which stops the search at the last step before
failure. Taught in
[Chapter 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#blameless-review-and-its-critics).

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

### Weeks, quarters, and years

Week 1 is the director's first week. Quarter 1 (the "transformation quarter") is weeks 1 to 13, quarter
2 weeks 14 to 26, quarter 3 weeks 27 to 39, quarter 4 weeks 40 to 52. The "baseline quarter" is the
quarter before the director arrived. Year 2 is weeks 53 to 104 (quarters 5 to 8); fiscal year 1 (FY1)
matches weeks 1 to 52. Quarter 3 is the latest measured quarter; quarter 4 decisions are open. Described
on the [first quarter page](case-studies/northstar/first-quarter.md).

### INC numbers

Northstar's incident identifiers. INC-401 to INC-430 are the 30 Sev1 and Sev2 incidents of the baseline
quarter, listed in the
[incident file](case-studies/northstar/data/incidents-last-quarter.csv); chapters name each one with a
few words on what happened.

### ADR-0001

Northstar's first architecture decision record, opened by Li Na Zhou (staff engineer, data and
integration) in week 14: how integrations should read posted ledger data, by reading the tables, through a
versioned export contract, or from ledger posting events. It was still open at week 26. Described on
the [first quarter page](case-studies/northstar/first-quarter.md); the ADR format is taught in
[Chapter 28](parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#architecture-decision-records).

### The continuation

The director's two-year proposal, drafted in week 45, to continue the quality program after year 1:
stage 2 "Hold" (quarters 5 and 6, 6 FTE of prevention, $150,000 of tooling, gate in week 78) and stage 3
"Converge" (quarters 7 and 8, 5 FTE, $100,000 of tooling only if a CI target is chosen, gate in week
104), after a stage 1 gate in week 56, with no headcount request. Each stage ends at a gate where written exit criteria decide whether the next is funded. Taught in
[Chapter 49](parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md#stages-gates-and-exit-criteria).

# Northstar baseline data

!!! warning "Fictional"
    Every number here was invented for this book. See the note on the
    [Northstar overview](index.md).

This page is the measured state of Northstar's engineering organization in the quarter before you
arrive. Chapters, exercises, projects, and the capstone all start from it. The raw files are small
enough to open in a spreadsheet:

- [`data/teams.csv`](data/teams.csv): one row per team
- [`data/components.csv`](data/components.csv): 24 components with ownership, tier, and operational readiness
- [`data/incidents-last-quarter.csv`](data/incidents-last-quarter.csv): all 30 Sev1 and Sev2 incidents

## How the numbers were produced, and what is wrong with them

A baseline is only useful if you know how it was measured. Northstar's measurement is uneven, and
part of the diagnostic work is deciding which numbers to trust.

| Measure | Source | Known weakness |
|---|---|---|
| Deployments, lead time | Pipeline logs from four CI systems, joined by hand | The four shell-script services log nothing; their numbers are estimates from chat history |
| Change failure rate | Releases followed within 72 hours by a hotfix, rollback, or incident linked to the release | Linking is manual; unlinked failures are missed, so the true rate is higher |
| Incidents | Incident tracker | Severity is assigned by the on-call engineer with no written definition before this quarter |
| Escaped defects | Customer-reported bug tickets confirmed as defects | Depends on support triage; duplicates were removed by hand |
| Unplanned work | Two-week sample of ticket types per team, checked with each manager | A sample, not a census; teams classify differently |
| Availability | Synthetic checks on the order and payment paths | Checks run from one region and do not cover the mobile path |

## Delivery and stability

| Measure | Core monolith | Services and frontends |
|---|---|---|
| Deployment frequency | 2 releases per month | median 3 deployments per week per service |
| Lead time for changes, commit to production (median) | 19 days | 3 days |
| Change failure rate | 31 percent of releases | 18 percent of deployments |

| Measure, whole organization | Value |
|---|---|
| Sev1 incidents last quarter | 7 |
| Sev2 incidents last quarter | 23 |
| Time to restore service, median | 3 hours 10 minutes |
| Time to restore service, 90th percentile | 14 hours |
| Availability, contractual paths | 99.62 percent (commitment: 99.9 percent) |
| Service credits paid | $410,000 |
| Committed roadmap items delivered in quarter | 7 of 17 (41 percent) |
| Unplanned work, share of engineering capacity | 34 percent |

At 99.62 percent, the contractual paths were unavailable for about 8.2 hours of a 90-day quarter.
A 99.9 percent commitment allows about 2.2 hours.

## By team

| Team | Engineers | Deployments per month | Median lead time (days) | Change failure rate | Sev1 and Sev2 | Escaped defects | Unplanned work |
|---|---|---|---|---|---|---|---|
| Orders | 14 | 11 | 18 | 29% | 7 | 51 | 36% |
| Billing | 13 | 8 | 21 | 34% | 8 | 58 | 41% |
| Payments and Integrations | 12 | 22 | 4 | 21% | 6 | 31 | 33% |
| Customer Experience | 15 | 26 | 6 | 17% | 4 | 44 | 28% |
| Data and Analytics | 11 | 11 | 5 | 12% | 2 | 19 | 24% |
| Platform Operations | 12 | 14 | 3 | 15% | 3 | 9 | 46% |
| Staff engineers | 3 | | | | | | 20% |
| **Total** | **80** | | | | **30** | **212** | **34%** |

Read this table with care. Orders and Billing ship most of their changes through the Core release
train, so their lead time and failure rate describe the train more than they describe the teams.
Platform Operations has the highest unplanned share because other teams' failures arrive there as
interrupts.

## Incidents

Thirty Sev1 and Sev2 incidents, classified by what triggered them:

| Trigger | Count | Share |
|---|---|---|
| Core release train | 9 | 30% |
| Configuration change | 5 | 17% |
| Database migration | 3 | 10% |
| Service deployment | 2 | 7% |
| **Change-induced, subtotal** | **19** | **63%** |
| Third-party dependency or capacity | 6 | 20% |
| Latent defect exposed by data or load | 4 | 13% |
| Not determined | 1 | 3% |

| Other facts about the same 30 incidents | Value |
|---|---|
| First detected by a customer | 14 (47 percent) |
| First detected by monitoring | 11 |
| First detected by an engineer who happened to notice | 5 |
| Median time to detect when a customer reported it | 108 minutes |
| Median time to detect when monitoring caught it | 6 minutes |
| Recurrences of a failure mode seen before | 11 (37 percent) |
| Median time to restore, incidents triggered by the release train | 4 hours 50 minutes |

Post-incident follow-up over the last two quarters: 96 corrective actions were recorded and 31
were closed (32 percent). No action has an owner above the level of the engineer who wrote it.

## Escaped defects

212 customer-reported defects were confirmed last quarter. 81 of them (38 percent) were
regressions: behavior that had worked in an earlier release.

Each defect was classified by the earliest point at which a reasonable check would have caught it:

| Earliest practical point of detection | Count | Share |
|---|---|---|
| Unit-level logic | 57 | 27% |
| Integration or contract between components | 49 | 23% |
| End-to-end or user-interface flow | 41 | 19% |
| Data migration or configuration | 38 | 18% |
| Requirement misunderstood; built as specified | 27 | 13% |

## Build and test

| Measure | Value |
|---|---|
| Core main-branch pipeline duration | 74 minutes |
| Core pipeline runs that fail for reasons unrelated to the change (flaky tests, infrastructure) | 9 percent |
| Share of working hours in which the Core main branch is red | 22 percent |
| Automated tests in Core | about 11,400; line coverage 41 percent |
| Manual regression suite | about 1,900 cases; 3 days per release; 7 QA engineers |
| Components with a written runbook | 7 of 24 |
| Components with complete alerting | 3 of 24 |
| Components with no on-call rotation | 8 of 24 |
| Components proposed as tier 1 (order or payment path) | 15 of 24 |

Line coverage is recorded because Northstar's managers quote it. It says how much code the tests
execute. It does not say whether the tests would fail if the code were wrong.

## Money

Used in the economic models in this book. All figures are annual unless stated.

| Item | Value | Derivation |
|---|---|---|
| Cost of one engineer-year | $185,000 | given |
| Engineering capacity spent on unplanned work | 27.2 engineer-years, about $5.0M | 80 × 34% × $185,000 |
| Service credits at last quarter's rate | $1.64M | $410,000 × 4 |
| Revenue in renewals where reliability is the stated concern | $9M | two customers |
| QA time spent on the manual regression pass | about 2.4 engineer-years, about $440,000 | 7 people × 3 days × 26 trains = 546 person-days ÷ 230 working days; excludes developer time spent fixing what the pass finds |

## Extended baseline by topic

These facts were added when Part V was written. Each was checked against the data files and the
figures above. They describe the same baseline quarter.

### Engineering standards (Chapter 20)

| Fact | Value |
|---|---|
| Written standards | One wiki page, "Engineering Standards", written in 2019 by a principal architect who left in 2021; 52 rules (24 code style and naming, 10 testing, 8 API and data, 6 operations, 4 security), all worded "must", none with intent, scope, owner, exemption path, or review date |
| Coverage rule | "Every module must have at least 70 percent line coverage"; never met (Core is at 41 percent) |
| Rules checked by a tool anywhere | 13 of 52; none checked identically in all four build systems |
| Standing warnings in the Core Jenkins build | about 2,300 (style checker in warning-only mode, 2019 configuration) |
| Engineering Practices Guild | Voluntary, monthly, no decision rights; average attendance 5 at the last six meetings |
| Pull request checklist | 10 items; in a sample of 40 merged pull requests, 38 had every box ticked, and 11 of those 38 changed production code with no test change while "tests added or updated" was ticked |
| Exemptions | No process; none ever recorded |
| Tier 1 operational minimums (owner, runbook, complete alerts, on-call) | 3 of 15 meet all four. Clear owner 11 of 15, runbook 6 of 15, complete alerts 3 of 15, on-call 12 of 15 |

### Technical debt (Chapter 21)

| Fact | Value |
|---|---|
| Existing debt list | Wiki page of 143 items from a "tech debt week" eighteen months earlier; 9 closed; none with owner or cost |
| Effort to run four CI systems | about 1.5 FTE of Platform Operations infrastructure time per year |
| Core pipeline runs | about 1,000 a month, branches and main |
| Proposed core/customer redesign | Ines Carvalho, about three engineer-years (not funded; see constraint 3) |

### Tests and pipeline (Chapters 22 and 23)

| Fact | Value |
|---|---|
| Core automated tests by kind | about 9,800 in-process unit tests, 1,350 tests against one shared Core test database, 250 browser UI tests |
| Core pipeline stages (74 minutes) | build and package 6, unit tests 9, shared-database tests 38, UI tests 21 |
| Flaky tests | about 140 tests, almost all using the shared test database, cause most failures unrelated to the change |
| Contract tests between Core and services | none |
| Migration and configuration checks before release | none; migrations are tested against an empty schema only |
| Merges into Core main | about 85 a week; the full pipeline runs on every merge |
| Core review rule | one approval from any engineer; no owner-based assignment |
| Median wait for first review on a Core merge request | 21 working hours |
| Core feature branches older than 30 days | 11; Core has no runtime feature flags |
| payments-gateway flags and settings | 64 entries in one configuration file edited directly on the configuration server without review; 23 older than a year |
| Shell-script deploys | one script shared by webhooks, auth-svc, document-store, and export-svc (the script broken in INC-416) |

### Reliability (Chapter 24)

| Fact | Value |
|---|---|
| Traffic | about 600,000 order submissions and 240,000 payment attempts per 28 days |
| Invoice and ledger reconciliation | no automated reconciliation exists |
| Correctness failures among customer-detected incidents | 8 of the 14 (wrong amounts or data, which an availability measure would not see) |

### Incidents (Chapter 25), derived from the incident file

| Fact | Value |
|---|---|
| Total restoration minutes | 9,558; the 11 recurrences account for 4,920 (51 percent) |
| Median restoration, recurrences versus first occurrences | 290 versus 160 minutes |
| Recurrences first detected by customers | 8 of 11 |
| Recurrences by team | Billing 6, Orders 3, Customer Experience 1, Payments and Integrations 1 |
| Open corrective actions | 65 (96 recorded, 31 closed) |

### Security (Chapter 26)

| Fact | Value |
|---|---|
| Security function | Two people in IT, outside engineering, led by Joon Park (IT security lead); annual external penetration test; no application security role |
| Dependency scanning in the pipeline | 8 of 24 components (the six GitLab CI services, non-blocking; the two frontends, untriaged); 6 of 15 tier 1 components |
| Open critical vulnerabilities in dependencies | 11 (Core 5, auth-svc 2, document-store 1, webhooks 1, frontends 1, GitLab CI services 1); 3 of them on CISA's Known Exploited Vulnerabilities catalog; 58 open highs; oldest critical disclosed 19 months earlier |
| Credentials in git history | 26 credential-like strings in 7 repositories; 9 confirmed live, 3 of them production |
| Secrets for the four shell-script services | in a plain file on the shared build host |
| TLS certificates | 34; 7 with no known owner; 5 expiring within 90 days; none with expiry alerting |
| Webhook signing keys | never rotated |
| SBOMs and threat modeling | none |

### Management and roles (Chapters 1–4)

Managers' time, reconstructed by each manager from two weeks of calendar and chat history:

| Team | Manager | People | Delivery | Technical | Other | Technical direction lives with |
|---|---|---|---|---|---|---|
| Orders | Priya Raman | 15% | 35% | 45% | 5% | Priya, who still writes code |
| Billing | Marcus Oyelaran | 15% | 55% | 15% | 15% | Nobody; decided during incidents |
| Payments and Integrations | Elena Sokolova | 35% | 35% | 15% | 15% | A senior engineer acting as informal tech lead (no one at Northstar holds the title) |
| Customer Experience | Daniel Cho | 45% | 35% | 5% | 15% | Two informal leads, web and mobile |
| Data and Analytics | Farah Haddad | 25% | 20% | 45% | 10% | Farah, as the team's data architect |
| Platform Operations | Tom Becker | 25% | 50% | 10% | 15% | Tom and the release process |

| Fact | Value |
|---|---|
| Manager job description | One shared line written years earlier: "lead a team of engineers to deliver high-quality software"; no manager-specific review criteria |
| Manager reviews | Once a year, on their teams' roadmap delivery only |
| Written levels | One wiki page with three individual-contributor levels (Engineer, Senior Engineer, Staff Engineer); the Staff Engineer paragraph states no scope, mandate, or expected output. No formal tech lead role |
| Staff engineers at baseline | Default problem-solvers: Ines Carvalho consulted on most Core changes without owning decisions (about 8 hours a week of unscheduled questions); Kwame Mensah pulled into the largest incidents; Li Na Zhou answering integration questions for whoever asks first |
| Priya Raman | Seven years at Northstar; promoted from inside Orders eight months before the director arrived, with no management training, after the previous manager left. Wrote much of the bulk upload path. In her first month as manager a bulk-upload failure occurred; she fixed it herself and took the follow-up test as her own action, which was never done (the failure mode recurred as INC-421). Two weeks before the director arrived her 40-hour week held 18 hours of coding and review, and she reviewed about 15 of Orders' roughly 25 weekly Core merge requests. Her one-on-ones were nominally weekly and mostly cancelled. In her first month the bulk-upload failure was fixed by her over a weekend |
| Orders senior engineers | Rafael Duarte (applied for the Orders manager role and lost to Priya) and Aisha Bello |
| Billing on-call load (reconstructed afterwards from the paging tool) | 180 pages in the quarter; 126 handled first by the three ledger engineers; 64 after hours, 54 of those by the same three; 61 needed no action |
| Billing ledger expertise | Four ledger-experienced responders a year before arrival; one resigned about nine months before; the backfill started 15 weeks later and was not yet on the rotation |
| Attrition | 8 engineers left in the 12 months before arrival (10 percent), all backfilled; median 15 weeks from resignation to the replacement's first day |
| Earlier responses to Billing on-call load | A higher on-call stipend, an alert added after each serious incident, and a request to "document as you go" with no time allocated |

### Planning and delivery (Chapters 15–18)

| Team | Delivery method at baseline |
|---|---|
| Orders | Two-week Scrum aligned to the release train; Sprint Goal met in 2 of the last 6 sprints |
| Billing | Two-week Scrum aligned to the release train; Sprint Goal met in 1 of the last 6; scope changed mid-sprint in all 6 |
| Payments and Integrations | Kanban with WIP limits per stage; weekly replenishment with the product manager |
| Customer Experience | Two-week sprints; one board for web and mobile |
| Data and Analytics | No named method; quarterly project list and a request queue triaged twice a week |
| Platform Operations | Interrupt-driven ticket queue; QA schedule set by the release train |

| Fact | Value |
|---|---|
| How the 17 committed items were chosen | 31 candidates collected by product managers; in a two-hour meeting four executives (Amara Okafor, Greg Tanaka, Sofia Alvarez, Victor Lindqvist) each distributed 100 points; no value estimates on any item |
| Renewal commitments | Agreed late in the baseline quarter as renewal conditions; dates and staffing in [the first quarter](first-quarter.md) |
| Sizing against capacity | About 560 engineer-weeks committed against an assumed 780 (1,040 less a 25 percent allowance); actual unplanned work left about 686 |
| Dates given to customers before sizing | 5 of 17, including Greg Tanaka's two deal features |
| Cross-team items | 9 of 17. Of the 7 delivered, 6 were single-team; of the 10 missed, 8 were cross-team |
| Committed and delivered by team | Orders 4 and 1; Billing 3 and 0; Payments and Integrations 3 and 2; Customer Experience 4 and 2; Data and Analytics 2 and 2; Platform Operations 1 and 0 |
| Reasons for the 10 misses | 4 scope growth after start, 3 blocked on another team, 2 displaced by incidents, 1 deprioritized |
| Roadmap record, four quarters | 6 of 15, 8 of 18, 7 of 16, then 7 of 17: 28 of 66 (42 percent) |
| Orders weekly throughput, 26 weeks before arrival (planned items finished) | 6, 4, 7, 3, 5, 8, 2, 6, 5, 4, 7, 6, 0, 5, 9, 4, 6, 3, 5, 7, 4, 6, 2, 8, 5, 6 (total 133, mean 5.1); recent features grew 15 to 35 percent in item count between start and delivery |
| Cross-team dependencies | 164 work items of a week or more; 61 needed another team; 86 dependency links; Platform Operations received 29, Billing 19, Orders 18, Payments and Integrations 10, Customer Experience 6, Data and Analytics 4 |
| Dependency links by pair (requesting → providing) | Orders → Billing 9, Payments 2, Customer Experience 3, Data 1, Platform 8. Billing → Orders 6, Payments 5, Customer Experience 1, Data 2, Platform 7. Payments → Orders 1, Billing 4, Customer Experience 1, Platform 5. Customer Experience → Orders 8, Billing 3, Payments 2, Data 1, Platform 6. Data → Orders 2, Billing 2, Payments 1, Platform 3. Platform → Orders 1, Billing 1, Customer Experience 1 |
| Lead time by dependencies (median) | none 11 days (103 items); one 24 days (42); two or more 41 days (19) |
| Standing orders feature (shipped in the baseline quarter) | 76 days from intake to release on its critical path: 53 waiting, 23 working |
| Unplanned work by category, share of total | Failure recovery 43 percent, requests from other teams 29, toolchain and environments 15, expedited requests 12 |
| Unplanned work by category and team (points of team capacity: failure recovery / requests from other teams / toolchain and environments / expedited) | Orders 18/8/6/4; Billing 24/7/6/4; Payments 15/9/3/6; Customer Experience 12/6/4/6; Data 6/12/3/3; Platform Operations 14/20/10/2; staff engineers 8/10/2/0. Totals match the team table; the organization total computes to 27.3 FTE against 27.2 from the rounded overall 34 percent |
| Delivery numbers at baseline | Assembled by one Platform Operations engineer, about two days a month, in a spreadsheet joining the four CI systems' logs |
| Engineering figures in the CEO's monthly board pack | Committed roadmap items delivered, and the Sev1 and Sev2 count |
| Developer surveys | None in the two years before arrival |

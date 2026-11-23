# Timeline

!!! warning "Fictional"
    Everything on this page is invented for the book. See the note on the
    [Northstar overview](index.md).

This page shows the Engineering Director's first year at Northstar on one page: what happened in
each week, where the full record is, and which chapter tells it. The second table gives the headline
results quarter by quarter. Weeks are counted from the director's first day. Each quarter is 13 weeks:
quarter 1 is weeks 1–13, quarter 2 weeks 14–26, quarter 3 weeks 27–39, and quarter 4 weeks 40–52.
People are listed on the [cast](cast.md) page. For the same year told as a story, read
[the year in brief](year-in-brief.md).

## Week by week

The "Record" column links to the section of [the year 1 record](first-quarter.md) or
another page that holds the details.

### Quarter 1: ownership, severity, and the release train

| Week | Event | Record | Chapter |
|---|---|---|---|
| Before week 1 | The baseline quarter: 30 Sev1 and Sev2 incidents, 99.62 percent availability, $410,000 in service credits, 34 percent unplanned work | [baseline](baseline-data.md) | [19](../../parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md), [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) |
| 1 | You join as Engineering Director. The CTO's mandate: halve Sev1 and Sev2 incidents and meet 99.9 percent within twelve months, with flat headcount and both renewal commitments kept | [overview](index.md#the-situation-when-you-arrive) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) |
| 2 | Incident classification with Kwame Mensah; one-off security scan of all 24 components; Priya Raman caps her hands-on work at 8 hours a week and delegates | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [26](../../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md), [2](../../parts/01-foundations/02-from-individual-contributor-to-leader.md) |
| 3 | Severity definitions published; standards page reviewed (39 of 52 rules unobservable); a renewal customer's security questionnaire arrives | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md), [20](../../parts/05-engineering-quality/20-engineering-standards-and-their-governance.md), [26](../../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md) |
| 4 | Capacity model agreed with Victor Lindqvist and Amara Okafor; first 40 flaky tests quarantined; core/customer and core/scheduler get owners | [quarter 1](first-quarter.md#timeline-of-quarter-1), [decisions](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md), [21](../../parts/05-engineering-quality/21-technical-debt.md) |
| 4–5 | 12 incident commanders trained | [decisions](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 5 | First weekly Core release | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md) |
| 6 | payments-gateway flag changes move to reviewed, validated merge requests | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md) |
| 7 | A two-hour payment delay rated Sev3 is re-rated; severity audit joins the weekly review. The promised migration check falls due and slips | [quarter 1](first-quarter.md#timeline-of-quarter-1), [decisions](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 8 | A contract test catches a payments-gateway rounding change; 2 of 7 "not affected" security closures found unanalysed | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [22](../../parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md), [26](../../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md) |
| 9 | Sev1 in Billing: credit notes applied twice, rollback fails; interim rule on ledger migrations | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md), [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 10 | QA transition announced: the seven QA engineers join product teams as quality engineers; migration rehearsal mandatory for tier 1 data | [quarter 1](first-quarter.md#timeline-of-quarter-1), [decisions](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [19](../../parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md), [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [22](../../parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md) |
| 11 | Pipeline check for unfinished migrations lands | [quarter 1](first-quarter.md#timeline-of-quarter-1) | [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 13 | Day 90: Sev1 and Sev2 from 30 to 21; both renewal commitments on track | [day 90](first-quarter.md#day-90) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) |

### Quarter 2: the renewals and the operating system

| Week | Event | Record | Chapter |
|---|---|---|---|
| 14 | Li Na Zhou opens ADR-0001 (how integrations read ledger data); organization decision log opened; Ines Carvalho's stay interview; weekly Billing and Orders sync starts | [starting points](first-quarter.md#starting-points-for-quarter-2), [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [28](../../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md), [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md), [10](../../parts/02-people-management/10-motivation-retention-and-senior-engineers.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md) |
| 14–15 | Stay interviews with the three ledger engineers; the director's firsthand time measured at 4.7 percent | [starting points](first-quarter.md#starting-points-for-quarter-2), [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [10](../../parts/02-people-management/10-motivation-retention-and-senior-engineers.md), [40](../../parts/09-engineering-directorship/40-the-directors-job.md) |
| 14–19 | Daniel Cho's one-on-ones reviewed (84 of 90 held, 55 mainly status) | [starting points](first-quarter.md#starting-points-for-quarter-2) | [5](../../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md) |
| 15 | Escalation path published | [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md) |
| 16 | First individual skip-levels; Customer Experience team health check; Priya Raman's hands-on time at 8 hours | [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [starting points](first-quarter.md#starting-points-for-quarter-2) | [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md), [14](../../parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.md), [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md) |
| 17 | Mateo Arango Ríos tells the director he has done a lead's job for over a year | [starting points](first-quarter.md#starting-points-for-quarter-2) | [5](../../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md), [14](../../parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.md) |
| 18 | Flow re-sample: environment waits fall from about 6 days to 2 | [starting points](first-quarter.md#starting-points-for-quarter-2) | [16](../../parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md) |
| 19 | Accounting integration live for the renewal customer | [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md) |
| 20 | Tomasz Wierzbicki reports an outside offer 20 percent above base; first checkpoint of Ines Carvalho's coaching plan; Priya at 10 hours | [starting points](first-quarter.md#starting-points-for-quarter-2), [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [10](../../parts/02-people-management/10-motivation-retention-and-senior-engineers.md), [29](../../parts/06-technical-leadership/29-staff-and-principal-engineers.md), [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md) |
| 22 | One-page written expectations for the managers; meeting calendar redesign drafted | [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [rules inventory](first-quarter.md#rules-and-processes-inventory) | [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md) |
| 24 | Draft ratings of the six managers; calendar redesign reviewed; Priya at 12 hours | [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [rules inventory](first-quarter.md#rules-and-processes-inventory) | [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md) |
| 26 | Bulk ordering complete and forecast to ship by the end of the week; first written report to Victor since day 90; second coaching checkpoint for Ines | [quarter 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [starting points](first-quarter.md#starting-points-for-quarter-2) | [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md), [29](../../parts/06-technical-leadership/29-staff-and-principal-engineers.md) |

### Quarter 3: capacity, portfolio, and the first quarter at target

| Week | Event | Record | Chapter |
|---|---|---|---|
| 27 (start of quarter 3) | First calibrated promotion cycle (9 nominated, 5 promoted); operating system redesign proposed; Engineering Excellence Day launched; bulk-ordering support reserve for weeks 27–30 | [starting points](first-quarter.md#starting-points-for-quarter-2), [quarter 3 plan](first-quarter.md#the-quarter-3-plan) | [8](../../parts/02-people-management/08-career-development-promotion-and-compensation.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md), [43](../../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md), [38](../../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md) |
| 28, 32, 36 | Engineering Excellence Days, with 64, 41, and 23 engineers taking part | [quarter 3 plan](first-quarter.md#the-quarter-3-plan) | [43](../../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md) |
| 31 | Greg Tanaka asks for a third deal feature, purchase approval rules | [quarter 3 plan](first-quarter.md#the-quarter-3-plan) | [42](../../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md) |
| About 33 | Automated service-credit statements due to start | [quarter 3 plan](first-quarter.md#the-quarter-3-plan) | [42](../../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md) |
| 34 | Portfolio forum on the third deal feature (outcome not recorded) | [quarter 3 plan](first-quarter.md#the-quarter-3-plan) | [42](../../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md) |
| 37 | Engineering Excellence Day stopped | [quarter 3 plan](first-quarter.md#the-quarter-3-plan) | [43](../../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md) |
| 39 | The core/permissions exemption lapses; Orders sizes price-list effective dates at 14 engineer-weeks, and Greg Tanaka then gives a customer week 46 | [quarter 3 results](first-quarter.md#quarter-3-results), [quarter 4](first-quarter.md#calendar-of-quarter-4) | [13](../../parts/03-high-performing-teams/13-decision-making-in-teams.md), [44](../../parts/10-business-leadership/44-working-with-product.md) |

### Quarter 4: drafts, positions, and open decisions

Nothing in quarter 4 has a recorded outcome. See the [quarter 4 briefing](quarter-4-briefing.md).

| Week | Event | Record | Chapter |
|---|---|---|---|
| 40 | Level mix 39 Engineers, 38 Seniors, 3 Staff; a top-40 distributor complains about correcting orders | [quarter 3 results](first-quarter.md#quarter-3-results), [quarter 4](first-quarter.md#calendar-of-quarter-4) | [48](../../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md), [44](../../parts/10-business-leadership/44-working-with-product.md) |
| 40–41 | A sample of 400 corrected orders finds 340 errors | [quarter 4](first-quarter.md#calendar-of-quarter-4) | [44](../../parts/10-business-leadership/44-working-with-product.md) |
| 41 | Victor asks for the board plan's engineering page; Rajiv Menon asks for a workforce plan; working contract sent to Amara; Farah Haddad's warehouse inventory; a customer asks about AI | [quarter 4](first-quarter.md#calendar-of-quarter-4), [data and AI](first-quarter.md#data-and-ai-chapter-54) | [46](../../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md), [48](../../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md), [44](../../parts/10-business-leadership/44-working-with-product.md), [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md) |
| 42 | Amara's three conditions; the director's counter for the board page; AI-use survey; a prospect requires SOC 2 | [quarter 4](first-quarter.md#calendar-of-quarter-4), [data and AI](first-quarter.md#data-and-ai-chapter-54), [risk](first-quarter.md#risk-security-and-compliance-chapter-53) | [44](../../parts/10-business-leadership/44-working-with-product.md), [46](../../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md), [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 43 | Margaret Lin asks for a technology risk session; Victor asks for an enterprise technology risk register | [risk](first-quarter.md#risk-security-and-compliance-chapter-53) | [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 43–45 | Four executives ask for AI features or answers | [data and AI](first-quarter.md#data-and-ai-chapter-54) | [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md) |
| 44 | Year-2 organization proposal; security snapshot; 34 security questionnaires tallied | [year-2 proposal](first-quarter.md#the-year-2-organization-proposal-week-44), [risk](first-quarter.md#risk-security-and-compliance-chapter-53) | [35](../../parts/07-organization-design/35-designing-organizations-at-four-scales.md), [36](../../parts/07-organization-design/36-reorganizations-evolution-and-succession.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 44–46 | Victor's week measured (48 hours, 2 of strategy); 11 informal technical requests | [CTO's job](first-quarter.md#the-ctos-job-chapter-50) | [50](../../parts/12-cto-leadership/50-what-a-cto-actually-does.md) |
| 45 | VP of Engineering question raised; quality continuation drafted; engineering board page due | [quarter 4](first-quarter.md#calendar-of-quarter-4) | [47](../../parts/11-vp-engineering/47-the-vp-of-engineering.md), [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md), [46](../../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md) |
| 46 | Year-2 organization decision due; Victor's business choices to Helena Marsh; Finance's FY1 estimate | [year-2 proposal](first-quarter.md#the-year-2-organization-proposal-week-44), [strategy](first-quarter.md#three-year-technology-strategy-chapter-51), [finances](first-quarter.md#finances-chapter-52) | [35](../../parts/07-organization-design/35-designing-organizations-at-four-scales.md), [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [52](../../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md) |
| 46–47 | Executive one-on-ones and positions on the continuation | [quarter 4](first-quarter.md#calendar-of-quarter-4) | [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md) |
| 46–48 | FY2 engineering budget draft; Victor gathers board directors' concerns | [finances](first-quarter.md#finances-chapter-52), [board](first-quarter.md#board-preparation-chapter-55) | [52](../../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md), [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) |
| 47 | Victor's strategy draft and his keep, give, stop draft; the director's risk register, SOC 2 options, and AI position; Greg Tanaka's private offer, declined | [strategy](first-quarter.md#three-year-technology-strategy-chapter-51), [CTO's job](first-quarter.md#the-ctos-job-chapter-50), [risk](first-quarter.md#risk-security-and-compliance-chapter-53), [data and AI](first-quarter.md#data-and-ai-chapter-54), [quarter 4](first-quarter.md#calendar-of-quarter-4) | [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [50](../../parts/12-cto-leadership/50-what-a-cto-actually-does.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md), [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md), [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md) |
| 48 | VP recommendation due; strategy premortem; Victor reviews the risk register; draft board page carries two headlines | [quarter 4](first-quarter.md#calendar-of-quarter-4), [strategy](first-quarter.md#three-year-technology-strategy-chapter-51), [risk](first-quarter.md#risk-security-and-compliance-chapter-53), [board](first-quarter.md#board-preparation-chapter-55) | [47](../../parts/11-vp-engineering/47-the-vp-of-engineering.md), [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md), [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) |
| 49 | Executive team meeting; workforce plan draft; board pack sent | [quarter 4](first-quarter.md#calendar-of-quarter-4), [strategy](first-quarter.md#three-year-technology-strategy-chapter-51), [board](first-quarter.md#board-preparation-chapter-55) | [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md), [48](../../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md), [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) |
| 50 | Board meeting and the audit committee's technology risk session (outcomes not recorded) | [quarter 4](first-quarter.md#calendar-of-quarter-4), [board](first-quarter.md#board-preparation-chapter-55) | [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 50–51 | Rules and processes inventory drafted | [rules inventory](first-quarter.md#rules-and-processes-inventory) | [59](../../parts/13-advanced-problems/59-transformation-under-constraint-and-scaling-without-bureaucracy.md) |
| 51 | Decisions requested on the continuation; planned announcement of the year-2 organization | [quarter 4](first-quarter.md#calendar-of-quarter-4), [year-2 proposal](first-quarter.md#the-year-2-organization-proposal-week-44) | [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md), [36](../../parts/07-organization-design/36-reorganizations-evolution-and-succession.md) |
| 52 | Date on the auth-svc security exception | [risk](first-quarter.md#risk-security-and-compliance-chapter-53) | [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |

## Results by quarter

The baseline quarter is the 90-day quarter before the director arrived; the director's quarters are
13 weeks. Quarter 3 is the latest measured quarter: quarter 4 results are not recorded, so chapters
set in weeks 40–52 use quarter 3 figures. "n.r." means not recorded.

| Measure | Baseline | Quarter 1 | Quarter 2 | Quarter 3 |
|---|---|---|---|---|
| Sev1 and Sev2 incidents (mandate: 15 or fewer) | 30 | 21 | 17 | 14 |
| of which Sev1 | 7 (9 under the week 3 definitions) | n.r. | 3 | 2 |
| of which via Core releases | 9 | 4 | 2 | n.r. |
| Recurrences | 11 of 30 | 5 of 21 | 3 of 17 | n.r. |
| Customer-detected share | 47% | 29% | 29% | n.r. |
| Availability, contractual paths (commitment 99.9%) | 99.62% | n.r. | 99.86% | 99.89% |
| Service credits | $410,000 | n.r. | $95,000 | $60,000 |
| Unplanned work | 34% | 31% | 28% | 25% |
| Tier 1 meeting the four operational minimums | 3 of 15 | 8 of 15 | 11 of 15 | 13 of 15 |
| Core releases | 2 per month | 11 | 13 | n.r. |
| Core change failure rate | 31% | 22% | 23% | n.r. |
| Corrective-action closure | 32% | 70% | 78% | n.r. |

Sources: [day 90](first-quarter.md#day-90), [quarter 2 results](first-quarter.md#quarter-2-results), [quarter 3 results](first-quarter.md#quarter-3-results), and the
[baseline data](baseline-data.md).

## Year 2 and later

- Year 1 is weeks 1–52. In Finance's terms it is fiscal year 1 (FY1); FY0 is the year before the
  director arrived.
- Year 2 is weeks 53–104 (quarters 5–8, FY2), year 3 weeks 105–156, and year 4 weeks 157–208.
- The year-2 organization proposal takes effect at the start of quarter 5 (week 53), with all
  handoffs by week 57 and a review in week 64.
- The quality continuation has gates in weeks 56, 78, and 104.

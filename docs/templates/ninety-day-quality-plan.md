# 90-day quality transformation plan

**Used in:** Chapter 27, Project 3, capstone stage 7.
**Owner:** the engineering director.
**Audience:** the director's managers and staff engineers (working plan); the CTO and head of product
(summary on page one).

A plan for the first 90 days of a quality transformation in an organization of 50 to 150 engineers.
Its job is to get from opinions to a named constraint, an agreed capacity trade, and a measurable
reduction in defect inflow. It does not try to finish the transformation.

## Page one: the summary

```markdown
## Quality plan, <period>

**Mandate:** <one sentence, in the words of whoever gave it>
**Constraint:** <the mechanism producing most of the damage, with the evidence>
**Parallel workstreams:** <usually detection and ownership>
**Capacity trade:** <prevention allocation by quarter; feature capacity effect; pessimistic case>
**Protected commitments:** <roadmap items that keep their dates>
**What we will stop:** <work dropped to fund this>
**How we will know by day 90:** <three to five mechanism measures with baselines>
**Decisions needed from leadership:** <specific, with dates>
```

## Workstreams

| Workstream | Lead | Goal by day 90 | Measures | Risks |
|---|---|---|---|---|

## Timeline

| Days | Milestone | Owner | Done when |
|---|---|---|---|
| 1–15 | Diagnosis complete | | Incidents and defects classified; pipeline measured; ownership inventory built; interviews held |
| 15–30 | Plan agreed | | Constraint named; capacity model agreed with CTO and product; severity definitions published; scorecard baseline live |
| 30–60 | Inflow reduction under way | | Constraint work shipping; tier 1 alerting live; actions list cut to owned items |
| 60–90 | Consolidate and report | | Trend reviewed; next-quarter targets set; backlog draining started; report to CTO |

## Risks and pre-commitments

Write down in advance what you will do when these happen; they usually do.

| Risk | Early signal | Pre-agreed response |
|---|---|---|
| Severity reclassification | Shift toward lower severities without fewer customer escalations | Weekly audit; director re-rates in the review |
| Roadmap commitment slips | Product review shows protected item at risk | Move prevention capacity off that team for the remainder of the quarter |
| A major incident during the plan | Sev1 on a tier 1 path | Blameless review led by the team; director briefs executives on mechanism, not person |
| Central work becomes permanent | No receiving team named for a deliverable | No central deliverable starts without a receiving team and hand-back date |

## Example: Northstar

**Fictional.** See the [Northstar case study](../case-studies/northstar/index.md).

**Mandate:** halve Sev1 and Sev2 incidents and meet the 99.9 percent availability commitment within
twelve months, with no net headcount growth, keeping the two renewal commitments.

**Constraint:** the Core release train. Evidence: 9 of 30 incidents last quarter, median restoration
of almost five hours against about three overall, 31 percent change fail rate, 19-day median lead
time.

**Parallel workstreams:** detection (14 of 30 incidents found by customers) and ownership (8 of 24
components disputed, shared, or orphaned).

**Capacity trade:** 12 FTE of prevention in quarters 1 and 2, 8 in quarter 3, 6 in quarter 4. Feature
capacity 41.6 FTE in quarter 1 against 52.8 today, recovering to about 59.6 by quarter 4 in the
planned case and about 53 in the pessimistic case.

**Protected commitments:** bulk ordering (Orders) and the accounting integration (Payments and
Integrations).

**What we will stop:** the three-day manual regression pass, replaced over two quarters by automated
checks on the paths it covered; the separate weekly status meetings of the six teams, replaced by the
weekly operational review; three roadmap items moved from quarter 1 to quarter 2 by agreement with
the CPO.

**How we will know by day 90:** Core change fail rate (baseline 31 percent), Core release frequency
(2 per month), customer-detected share (47 percent), tier 1 readiness (3 of 15), action closure rate
(32 percent).

| Workstream | Lead | Goal by day 90 |
|---|---|---|
| Release train | Kwame Mensah, with two QA engineers and one Orders engineer | Weekly Core releases; automated checks for the 200 highest-value regression cases; deploy separated from release for new risky features |
| Detection | Elena Sokolova (Payments has the strongest alerting practice) | User-facing alerts on all tier 1 paths |
| Ownership | Engineering Director | Named owner and on-call for every tier 1 component; disputed cases decided |
| Migration and configuration safety | Li Na Zhou | Migration ordering check in the pipeline; configuration changes reviewed and flagged |
| Core boundaries and contracts | Ines Carvalho | Contract tests on the three most-changed module boundaries |

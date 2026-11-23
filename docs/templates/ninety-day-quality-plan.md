# 90-day quality transformation plan

**Used in:** [Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md)
(quality transformation at enterprise scale), [Project 3](../projects/p3-quality-transformation-plan.md),
[capstone](../parts/15-capstone/60-capstone-northstar.md) stage 7.
**Owner:** the engineering director. The working plan is for the director's managers and staff
engineers; page one is the summary for the CTO and head of product.
**Cadence:** written in the first 30 days of a quality transformation; progress reviewed weekly in the
operational review; reported to the CTO at day 90, when the next quarter's plan replaces it.

A plan for the first 90 days of a quality transformation in an organization of 50 to 150 engineers.
Its job is to get from opinions to a named [constraint](../glossary.md#constraint) (the mechanism
producing most of the damage), an agreed capacity trade, and a measurable fall in defect inflow. It
does not try to finish the transformation. The capacity trade is a
[prevention allocation](../glossary.md#prevention-allocation): engineering time set aside, in
[FTE](../glossary.md#fte), for work that stops failures arriving.

## How to fill it in

1. **Write the mandate in the words of whoever gave it.** If it has no number, agree one before the
   plan goes further.
2. **Diagnose before you name the constraint** (days 1–15). Classify last quarter's incidents and
   escaped defects by mechanism, measure the pipeline, build the ownership inventory, and interview the
   managers. Name one constraint and give the evidence in numbers.
3. **Pick at most two parallel workstreams**, usually detection and ownership, because they make every
   later fix visible and assignable.
4. **Price the capacity trade** by quarter, with a planned case and a cautious case (see the
   [capacity planning model](capacity-planning-model.md)). Show product what feature capacity it gives
   up, and get the trade agreed in writing before the quarter starts.
5. **Name what keeps its date and what stops.** Protected commitments are the roadmap items the
   business cannot move. "What we will stop" pays for the plan; a plan with no stops is unfunded.
6. **Choose three to five mechanism measures with baselines**, each paired with a measure that shows
   gaming (see the [engineering quality scorecard](engineering-quality-scorecard.md)).
7. **Write the pre-commitments.** For each likely risk, record the early signal and the response you
   agree now, while nobody is under pressure.

## Template

### Page one: the summary

```markdown
## Quality plan, <period>

**Mandate:** <one sentence, in the words of whoever gave it>
**Constraint:** <the mechanism producing most of the damage, with the evidence>
**Parallel workstreams:** <usually detection and ownership>
**Capacity trade:** <prevention allocation by quarter; feature capacity effect; cautious case>
**Protected commitments:** <roadmap items that keep their dates>
**What we will stop:** <work dropped to fund this>
**How we will know by day 90:** <three to five mechanism measures with baselines>
**Decisions needed from leadership:** <specific, with dates>
```

### Workstreams

| Workstream | Lead | Goal by day 90 | Measures | Risks |
|---|---|---|---|---|

### Timeline

| Days | Milestone | Owner | Done when |
|---|---|---|---|
| 1–15 | Diagnosis complete | | Incidents and defects classified; pipeline measured; ownership inventory built; interviews held |
| 15–30 | Plan agreed | | Constraint named; capacity model agreed with CTO and product; severity definitions published; scorecard baseline live |
| 30–60 | Inflow reduction under way | | Constraint work shipping; tier 1 alerting live; actions list cut to owned items |
| 60–90 | Consolidate and report | | Trend reviewed; next-quarter targets set; backlog draining started; report to CTO |

### Risks and pre-commitments

Write down in advance what you will do when these happen; they usually do.

| Risk | Early signal | Pre-agreed response |
|---|---|---|
| Severity reclassification | Shift toward lower severities without fewer customer escalations | Weekly audit; director re-rates in the review |
| Roadmap commitment slips | Product review shows protected item at risk | Move prevention capacity off that team for the remainder of the quarter |
| A major incident during the plan | Sev1 on a tier 1 path | Blameless review led by the team; director briefs executives on mechanism, not person |
| Central work becomes permanent | No receiving team named for a deliverable | No central deliverable starts without a receiving team and hand-back date |

## Example: Northstar, the director's first quarter

!!! info "Northstar so far"
    Week 4 of the Engineering Director's first year at Northstar Technologies, a fictional company with
    80 engineers in six teams. The baseline quarter had 30 Sev1 and Sev2 incidents and 99.62 percent
    availability; the capacity model has just been agreed with Victor Lindqvist (CTO) and Amara Okafor
    (CPO). See the [timeline](../case-studies/northstar/timeline.md) and the [cast](../case-studies/northstar/cast.md).

**Mandate:** halve Sev1 and Sev2 incidents and meet the 99.9 percent availability commitment within
twelve months, with no net headcount growth, keeping the two renewal commitments.

**Constraint:** the release train of [Core](../glossary.md#core), Northstar's monolith. Evidence: 9 of
30 incidents last quarter, median restoration of almost five hours against about three overall, a 31
percent [change failure rate](../glossary.md#change-failure-rate), and a 19-day median
[lead time](../glossary.md#lead-time).

**Parallel workstreams:** detection (14 of 30 incidents found by customers) and ownership (8 of 24
components disputed, shared, or orphaned).

**Capacity trade:** 12 FTE of prevention in quarters 1 and 2, 8 in quarter 3, 6 in quarter 4.

| Feature capacity | FTE |
|---|---|
| Today | 52.8 |
| Quarter 1 | 41.6 |
| Quarter 4, planned case | about 59.6 |
| Quarter 4, cautious case | about 53 |

**Protected commitments:** bulk ordering (Orders) and the accounting integration (Payments and
Integrations), the two features promised to renewal customers.

**What we will stop:** the three-day manual regression pass, replaced over two quarters by automated
checks on the paths it covered; the separate weekly status meetings of the six teams, replaced by the
weekly operational review; three roadmap items moved from quarter 1 to quarter 2 by agreement with
the CPO.

**How we will know by day 90:** Core change failure rate (baseline 31 percent), Core release frequency
(2 per month), customer-detected share (47 percent), [tier 1](../glossary.md#tier-1) readiness (3 of
15), action closure rate (32 percent).

| Workstream | Lead | Goal by day 90 |
|---|---|---|
| Release train | Kwame Mensah (staff engineer, infrastructure), with two QA engineers and one Orders engineer | Weekly Core releases; automated checks for the 200 highest-value regression cases; deploy separated from release for new risky features |
| Detection | Elena Sokolova (manager, Payments and Integrations, the strongest alerting practice) | User-facing alerts on all tier 1 paths |
| Ownership | Engineering Director | Named owner and on-call for every tier 1 component; disputed cases decided |
| Migration and configuration safety | Li Na Zhou (staff engineer, data and integration) | Migration ordering check in the pipeline; configuration changes reviewed and flagged |
| Core boundaries and contracts | Ines Carvalho (staff engineer, Core domain) | Contract tests on the three most-changed module boundaries |

What to notice: the plan names one constraint and two supporting workstreams, not ten initiatives.
Every stop is specific, so product can see what pays for the prevention time.

## Common mistakes

- **The quality sprint.** A fix-it fortnight closes many tickets while the inflow is unchanged. Make
  inflow (new defects, change failure rate) the primary outcome.
- **Naming several constraints.** Five "top priorities" means none. Name one, and say why the others
  wait.
- **The silent dip.** Prevention is funded by quietly taking feature capacity; product finds out when
  dates slip. Present the capacity model before the quarter and get the trade agreed in writing.
- **Practice mandates instead of inflow targets.** Sign-off for every change, or a coverage target,
  grows batches and tests that assert nothing. Give every gate an expiry date and measure its effect.
- **The tiger team that never leaves.** Central work with no receiving team becomes a permanent
  bottleneck. Every engagement ends with the owning team operating the result.
- **Counting incidents alone.** Counts fall as more incidents are rated Sev3. Pair them with
  customer-detected share and service credits, and audit severity weekly.

## Review questions

1. What evidence would show the named constraint is the wrong one, and when will you look?
2. Which protected commitment is most at risk, and which pre-commitment applies if it slips?
3. What did the plan stop, and has anyone quietly started it again?
4. Which day-90 measure could improve without the mechanism improving, and what is it paired with?
5. Which central deliverable has no receiving team or hand-back date?

## Evidence and references

The method is [Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md),
with the capacity arithmetic in Chapter 38.

- [Goldratt and Cox, 1984](../references/bibliography.md#goldratt1984goal): constraint thinking, the
  idea behind naming one constraint.
- [Meadows, 2008](../references/bibliography.md#meadows2008thinking): stocks, flows, and feedback
  loops, the vocabulary for defect inflow and backlog.
- [Humble and Farley, 2010](../references/bibliography.md#humble2010continuous): the case for small
  batches and an automated pipeline, which underlies the release-train constraint.
- [Forsgren, Humble, and Kim, 2018](../references/bibliography.md#forsgren2018accelerate): the DORA
  research behind change failure rate and lead time as measures.
- [Campbell, 1979](../references/bibliography.md#campbell1979assessing): the source usually credited
  for the problem of indicators that become targets, and so for pairing every measure.

The 90-day structure, the two-workstream limit, and the pre-commitment table are **this book's
recommendation**.

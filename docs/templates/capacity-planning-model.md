# Capacity planning model

**Used in:** [Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md)
(funding quality work), [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
(quarterly planning and capacity allocation).
**Owner:** the engineering director; managers supply team figures; the head of product agrees the
result.
**Cadence:** built before quarterly planning; updated monthly with measured unplanned work.

A capacity model says how much engineering time exists, how much of it is already spoken for by
[unplanned work](../glossary.md#unplanned-work), how much is deliberately spent on
[prevention](../glossary.md#prevention-allocation) and platform work, and what is left for roadmap
commitments. Capacity is counted in [FTE](../glossary.md#fte) (full-time equivalent engineers). Its job is to make the trade visible before commitments are made, so that a
dip in feature capacity is a decision rather than a surprise. It is a planning instrument, not a
forecast: every row rests on an assumption, and the model is only as honest as the unplanned-work
sample behind it.

!!! tip "Minimum version"
    On day one, fill the organization table for the coming quarter: engineers, measured unplanned work,
    prevention, and the feature capacity left. Add the per-team table and the cautious case before
    commitments are made, and the monthly revisions once the quarter starts.

## How to fill it in

1. Count capacity in FTE per team, for the quarter. Exclude
   managers. Subtract known absences (parental leave, open seats) rather than assuming everyone is
   present.
2. Measure unplanned work per team with the same sampling rules every quarter (Chapter 16): a
   two-week sample of work by category, checked with the manager. Record the method next to the
   number.
3. Set the prevention allocation (and any platform allocation) explicitly, per team, with the
   reason for each team's share.
4. Feature capacity is what remains. Show it per team and in total, and its change from the
   baseline.
5. Add a [cautious case](../glossary.md#planned-case-and-cautious-case) in which unplanned work falls more slowly than planned. Present both.
6. Each month, replace planned unplanned work with the measured figure, and say what the difference
   does to commitments.

## Template

**Organization, by quarter**

| Quarter | Engineers | Unplanned work | Prevention | Feature capacity | Change from baseline |
|---|---|---|---|---|---|
| Baseline | | % = FTE | 0 | FTE | — |
| Quarter 1 | | | | | |

**Team, for one quarter**

| Team | Engineers | Unplanned (%, FTE) | Prevention (FTE, reason) | Feature capacity (FTE) | Commitments (FTE) | Slack |
|---|---|---|---|---|---|---|

Assumptions block, kept with the model and reviewed monthly:

```yaml
model:
  quarter: ""
  weeks: 13
  engineers: 0
  unplanned_measurement: ""     # sampling method and date
  cost_per_engineer_year: 0
  assumptions:
    - ""
  teams:
    - name: ""
      engineers: 0
      unplanned_pct: 0
      prevention_fte: 0
      commitments_fte: 0
  cautious_case:
    unplanned_pct: 0
    feature_fte: 0
  revisions:
    - {date: "", change: "", effect_on_commitments: ""}
```

## Example: Northstar, quarters 1 to 4

!!! info "Northstar so far"
    Northstar Technologies is a fictional company with 80 engineers. In week 4 of the Engineering
    Director's first year, the director agreed this model with Victor Lindqvist (CTO) and Amara Okafor
    (CPO) to fund a quality program inside flat headcount. See the
    [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Assumptions: 80 engineers; unplanned work at 34 percent (27.2 FTE) at baseline; prevention of 12 FTE
in quarters 1 and 2, 8 in quarter 3, and 6 in quarter 4.

| Quarter | Unplanned work | Prevention | Feature capacity | Change from baseline |
|---|---|---|---|---|
| Baseline | 34% = 27.2 FTE | 0 | 52.8 FTE | — |
| Quarter 1 plan | 33% = 26.4 FTE | 12 FTE | 41.6 FTE | −21% |
| Quarter 1 measured | 31% = 24.8 FTE | 12 FTE | 43.2 FTE | −18% |
| Quarter 2 measured | 28% = 22.4 FTE | 12 FTE | 45.6 FTE | −14% |
| Quarter 3 plan (measured: 25%) | 22% = 17.6 FTE | 8 FTE | 54.4 FTE | +3% |
| Quarter 4 plan (not measured) | 18% = 14.4 FTE | 6 FTE | 59.6 FTE | +13% |

Cautious case: unplanned work falls only to 26 percent by quarter 4, leaving 53.2 FTE of feature
capacity, roughly the baseline. The year's prevention is 38 [FTE-quarters](../glossary.md#fte-quarter)
(9.5 engineer-years), about $1.76M at $185,000 per engineer-year.

Quarter 1's 12 FTE of prevention was split by where the incidents come from and where the
[renewal commitments](../glossary.md#renewal-commitments) (features promised to customers who renew)
sit: Billing 25 percent of its engineers, Orders and Payments and Integrations 10 percent, the others 15
percent.

**Quarter 3 plan by team.** Quarter 3 (weeks 27 to 39) splits the 54.4 FTE of feature capacity into a
platform line of 4.5 FTE and 49.9 FTE of product capacity. The platform line is 3 FTE of Platform
Operations planned work plus 1.5 FTE in product teams for pipeline migrations, held until the CI
target is decided. Teams are as after week 10, when the seven QA engineers moved into product teams.
The per-team unplanned figures are illustrative: the case gives only the total, so 2.0 FTE is Platform
Operations' interrupt rotation and the other 15.6 FTE is spread in proportion to each team's baseline
rate and headcount. The table uses the 22 percent plan; measured unplanned work came in at 25 percent.

| Team | Engineers | Unplanned (FTE) | Prevention (FTE) | Platform (FTE) | Product (FTE) |
|---|---|---|---|---|---|
| Orders | 16 | 3.7 | 2.0 | | 10.3 |
| Billing | 15 | 3.9 | 2.5 | | 8.6 |
| Payments and Integrations | 13 | 2.8 | 1.0 | | 9.2 |
| Customer Experience | 17 | 3.1 | 1.5 | | 12.4 |
| Data and Analytics | 11 | 1.7 | 1.0 | | 8.3 |
| Platform Operations | 5 | 2.0 | 0 | 3.0 | 0 |
| Staff engineers | 3 | 0.4 | 0 | | 2.6 |
| Pipeline migrations, held | | | | 1.5 | −1.5 |
| **Total** | **80** | **17.6** | **8.0** | **4.5** | **49.9** |

Each row sums to the team's engineers, and the columns sum to 80. Billing keeps the largest prevention
share (6 of the 11 baseline recurrences); Orders' share rises because bulk ordering, the renewal feature
due at the end of quarter 2, no longer holds its capacity.

| Cautious case, quarter 3 | FTE |
|---|---|
| Engineers | 80 |
| Unplanned work stays at quarter 2's 28 percent | −22.4 |
| Prevention | −8.0 |
| Platform line | −4.5 |
| Product capacity | 45.1 (4.8 below plan) |
| After the 0.6 FTE bulk-ordering support reserve | 44.5 |

The plan commits only what the cautious case can absorb after dividing by 1.25 for scope growth, about
35.6 FTE-quarters of estimated effort, and labels the rest as targets or unfunded.

## Common mistakes

- **Planning against total headcount.** Committing 80 engineers of roadmap when a third of them are
  on unplanned work is how Northstar's baseline delivered 7 of 17 items.
- **Hiding the dip.** If the head of product learns of the quarter 1 drop in month three, it reads as
  a failure rather than a decision.
- **Unplanned work as a guess.** Without a sample, the largest row in the model is opinion.
- **Uniform allocation.** Prevention should follow inflow and commitments, not fairness.
- **Never revising.** A model not updated monthly is a promise, not a plan.
- **Precision theater.** One decimal place of FTE is arithmetic, not accuracy; say so.

## Review questions

1. Which assumption, if wrong, changes the commitments the most?
2. Does measured unplanned work match the plan, and what moved it?
3. Which team's prevention share is no longer justified by its inflow?
4. What is committed against the cautious case, and what is only a target?
5. What would we stop if unplanned work rose by five points next month?

## Evidence and references

The method is in [Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md)
(funding prevention) and [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
(planning against the cautious case); measuring unplanned work is
[Chapter 16](../parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md).

- [Kim, Behr, and Spafford, 2013](../references/bibliography.md#kim2013phoenix): *The Phoenix Project*,
  a novel useful for explaining unplanned work to non-engineers.

No study gives a correct prevention share. The model's structure, the cautious case, and the 1.25
scope-growth divisor are **this book's recommendation**; the per-team figures in the example are
**illustrative**.

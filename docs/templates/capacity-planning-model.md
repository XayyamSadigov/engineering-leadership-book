# Capacity planning model

!!! warning "Awaiting human review"
    This template has passed the book's automated validation and an editorial self-review, but not yet
    the human review in which each cited claim is checked against its source. Treat it as a reviewed
    draft. Corrections are welcome; see the repository's CONTRIBUTING file.

**Used in:** Chapter 27 (funding quality work), Chapter 38 (quarterly planning and capacity
allocation).
**Owner:** the engineering director; managers supply team figures; the head of product agrees the
result.
**Cadence:** built before quarterly planning; updated monthly with measured unplanned work.

A capacity model says how much engineering time exists, how much of it is already spoken for by
unplanned work, how much is deliberately spent on prevention and platform work, and what is left for
roadmap commitments. Its job is to make the trade visible before commitments are made, so that a
dip in feature capacity is a decision rather than a surprise. It is a planning instrument, not a
forecast: every row rests on an assumption, and the model is only as honest as the unplanned-work
sample behind it.

## How to fill it in

1. Count capacity in full-time-equivalent engineers (FTE) per team, for the quarter. Exclude
   managers. Subtract known absences (parental leave, open seats) rather than assuming everyone is
   present.
2. Measure unplanned work per team with the same sampling rules every quarter (Chapter 16): a
   two-week sample of work by category, checked with the manager. Record the method next to the
   number.
3. Set the prevention allocation (and any platform allocation) explicitly, per team, with the
   reason for each team's share.
4. Feature capacity is what remains. Show it per team and in total, and its change from the
   baseline.
5. Add a pessimistic case in which unplanned work falls more slowly than planned. Present both.
6. Each month, replace planned unplanned work with the measured figure, and say what the difference
   does to commitments.

## Template

**Organization, by quarter**

| Quarter | Engineers | Unplanned work | Prevention | Feature capacity | Change from baseline |
|---|---|---|---|---|---|
| Baseline | | % = FTE | 0 | FTE | — |
| Q1 | | | | | |

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
  pessimistic_case:
    unplanned_pct: 0
    feature_fte: 0
  revisions:
    - {date: "", change: "", effect_on_commitments: ""}
```

## Example: Northstar, quarters 1 to 4

**Fictional.** The organization-level model is Chapter 27's, from the
[Northstar first quarter](../case-studies/northstar/first-quarter.md). Assumptions: 80 engineers;
unplanned work at 34 percent (27.2 FTE) at baseline; prevention of 12 FTE in quarters 1 and 2, 8 in
quarter 3, and 6 in quarter 4.

| Quarter | Unplanned work | Prevention | Feature capacity | Change from baseline |
|---|---|---|---|---|
| Baseline | 34% = 27.2 FTE | 0 | 52.8 FTE | — |
| Q1 plan | 33% = 26.4 FTE | 12 FTE | 41.6 FTE | −21% |
| Q1 measured | 31% = 24.8 FTE | 12 FTE | 43.2 FTE | −18% |
| Q2 | 28% = 22.4 FTE | 12 FTE | 45.6 FTE | −14% |
| Q3 | 22% = 17.6 FTE | 8 FTE | 54.4 FTE | +3% |
| Q4 | 18% = 14.4 FTE | 6 FTE | 59.6 FTE | +13% |

Pessimistic case: unplanned work falls only to 26 percent by quarter 4, leaving 53.2 FTE of feature
capacity, roughly the baseline. The 38 FTE-quarters of prevention cost about $1.76M at $185,000 per
engineer-year (38 ÷ 4 × $185,000 = $1,757,500).

**Quarter 1 by team.** 12 FTE of prevention, sized by where the inflow comes from and where the
renewal commitments sit: Billing 25 percent; Orders and Payments and Integrations 10 percent; the
others, including the staff engineers, 15 percent. Teams as at the start of the quarter.

| Team | Engineers | Share | Prevention (FTE) |
|---|---|---|---|
| Orders | 14 | 10% | 1.40 |
| Billing | 13 | 25% | 3.25 |
| Payments and Integrations | 12 | 10% | 1.20 |
| Customer Experience | 15 | 15% | 2.25 |
| Data and Analytics | 11 | 15% | 1.65 |
| Platform Operations | 12 | 15% | 1.80 |
| Staff engineers | 3 | 15% | 0.45 |
| **Total** | **80** | | **12.00** |

**Quarter 3 by team.** Chapter 38 plans quarter 3 (weeks 27 to 39) from this model and splits the
54.4 FTE into a platform line of 4.5 FTE (3 FTE of Platform Operations planned work, plus 1.5 FTE in
product teams for pipeline migrations, held until the consolidation target is decided) and 49.9 FTE
of product capacity. Its prevention split by team is used here unchanged. Teams are as after week 10,
when the seven QA engineers moved into product teams.

The per-team unplanned figures are this template's illustrative assumption; Chapter 38 gives only
the total. Platform Operations' two interrupt-rotation engineers count as its unplanned work (2.0
FTE). The other 15.6 FTE is spread in proportion to each team's baseline unplanned rate × its
quarter 3 headcount (24.2 FTE before scaling, so each is multiplied by 15.6 ÷ 24.2 ≈ 0.645, rounded
so the column sums).

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

Check: unplanned 3.7 + 3.9 + 2.8 + 3.1 + 1.7 + 2.0 + 0.4 = 17.6; prevention 2.0 + 2.5 + 1.0 + 1.5 +
1.0 = 8.0; product 10.3 + 8.6 + 9.2 + 12.4 + 8.3 + 2.6 − 1.5 = 49.9; and 17.6 + 8.0 + 4.5 + 49.9 =
80.0. Platform plus product is 54.4 FTE, the quarter 3 feature capacity above. Billing keeps the
largest prevention share (6 of the 11 baseline recurrences); Orders' share rises because bulk
ordering no longer holds its capacity; Platform Operations' planned work is the platform line.

Cautious case, for the planning conversation: if unplanned work stays at quarter 2's measured 28
percent (22.4 FTE, Chapter 39), product capacity is 80 − 22.4 − 8.0 − 4.5 = 45.1 FTE, 4.8 FTE below plan, and
44.5 FTE after the 0.6 FTE bulk ordering support reserve. Chapter 38 commits only what the cautious
case can absorb after dividing by 1.25 for scope growth (about 35.6 FTE-quarters of estimated
effort), and labels the rest as targets or unfunded.

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

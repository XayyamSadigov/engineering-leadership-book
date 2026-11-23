# Technology investment business case

**Used in:** [Chapter 45](../parts/10-business-leadership/45-business-models-and-engineering-economics.md)
(engineering economics and cost of delay), [Chapter 52](../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md)
(financial statements and budgeting), [Project 8](../projects/p8-cto-technology-investment-proposal.md).
**Owner:** the leader asking for the money or capacity; finance checks the arithmetic, and the
decider is named in the ask.
**Cadence:** once per investment, before the decision; revisited at each checkpoint the case
commits to and on its review date, and closed with a short look-back comparing actual cost and
benefit with the case.

A business case turns a technical proposal into a decision a non-engineer can make: what problem it
solves, what the options cost, what each returns, what waiting costs, and what would change the
answer. Its job is not to win the money. A case that hides its weakest assumption usually gets
approved once and distrusted afterwards.

Four terms carry the template. [Cost of delay](../glossary.md#cost-of-delay) is the value lost for
each week a benefit arrives late, in dollars per week. [CD3](../glossary.md#cd3-and-wsjf) is cost of
delay in thousands of dollars per week divided by duration in weeks, a ranking for ordering work. Each
benefit is assigned one **value channel**: increase revenue, protect revenue, reduce costs, or avoid
costs. And each item has one of four **urgency profiles**: long life, peak unaffected; long life, peak
affected; short life, peak affected; external deadline. An external-deadline item is scheduled backward
from its date with a margin, not ranked by CD3.

!!! tip "Minimum version"
    On day one, write four things: the problem in the decider's terms, three options (do nothing, a
    partial option, the full proposal) with their one-time and run costs, the cost of delay per week, and
    the ask with one stop condition. Add NPV, the decisive input, and uncounted benefits before the decision.

## How to fill it in

1. **State the problem in the decider's terms.** Money, risk to revenue, risk to customers, or time
   to market. The technology appears in the options, not in the problem statement.
2. **Always include "do nothing" and a cheaper partial option.** A case with one option is a request,
   not a decision.
3. **Price costs fully.** Engineering time at [fully loaded cost](../glossary.md#fully-loaded-cost), cash spend, run cost after the work,
   and the opportunity cost: the item displaced, with its own cost of delay.
4. **Count benefits by channel, with a formula and an owner for each factor.** New revenue counts at
   gross margin, avoided service credits at 100 percent, saved engineering time at the capacity rate
   and labeled *capacity*, not cash. Name the benefits you cannot count; do not price them.
5. **Compute cost of delay per week,** name its urgency profile, and say what a quarter's slip costs.
6. **Compute payback and three-year [NPV](../glossary.md#net-present-value-npv)** (net present value:
   future flows discounted at finance's [hurdle rate](../glossary.md#discount-rate-and-hurdle-rate)) with the timing assumptions written down.
7. **Find the decisive input** and the value at which you would recommend a different option.
8. **Write the ask last.** One decision, one decider, one date, checkpoints that would stop the
   spend, and a review date for checking the estimate against what happened.

## Template

| Section | Contents |
|---|---|
| Problem | What it costs today, with evidence; who bears the cost |
| Options | At least three, including do nothing and a partial option |
| Costs | One-time (engineering, cash), recurring run cost, opportunity cost |
| Benefits | Value channel, formula, factor owners, probability; uncounted benefits named |
| Cost of delay | Dollars per week, urgency profile, CD3, cost of a quarter's slip |
| Returns | Payback and three-year NPV, with timing assumptions |
| Risks | What could make it fail or cost more; mitigation and owner |
| Decisive input | The least certain input and its break-even value |
| The ask | Decision, decider, date, funding, checkpoints and stop conditions, review date |

```yaml
case:
  title: ""
  prepared_by: ""
  decider: ""
  decision_by: ""
  assumptions:
    cost_per_engineer_year: 0
    capacity_rate_per_week: 0     # cost per engineer-year / 52
    hurdle_rate: 0
    gross_margin: 0
problem:
  statement: ""
  current_cost: []                # each with number and source
options:
  - id: O1
    name: do nothing
    one_time_cost: 0
    annual_run_cost: 0
benefit:
  value_channel: ""               # increase revenue / protect revenue / reduce costs / avoid costs
  formula: ""
  factor_owners: {}
  probability: 0
  label: ""                       # cash / capacity
  uncounted: []
opportunity_cost: {displaced_item: "", its_cost_of_delay_per_week: 0}
cost_of_delay:
  per_week: 0
  urgency_profile: ""             # long life, peak unaffected / long life, peak affected /
                                  # short life, peak affected / external deadline
  class_of_service: ""            # optional Kanban class, kept separate
  duration_weeks: 0
  cd3: 0                          # per_week in $k / duration_weeks
  quarter_slip_cost: 0
returns: {payback: "", npv_3y: 0, timing: ""}
risks:
  - {risk: "", likelihood: "", mitigation: "", owner: ""}
decisive_input: {input: "", base: "", break_even: "", effect: ""}
ask:
  decision: ""
  funding_source: ""
  checkpoints:
    - {when: "", evidence: "", stop_if: ""}
  review_date: ""
```

## Example: Northstar, CI consolidation

!!! info "Northstar so far"
    Quarter 2 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Northstar builds and deploys its 17 [deployable units](../glossary.md#deployable-unit) (Core counts as one; 24 components in all) on
    four different CI (continuous integration) systems, and a shared deploy script broke rollback for
    four services in INC-416. Tom Becker (Platform Operations manager) and Kwame Mensah (staff engineer,
    infrastructure) draft the case for Victor Lindqvist (CTO). Weeks count from the director's first week. See the
    [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

The run costs, effort, and rates come from the [baseline data](../case-studies/northstar/baseline-data.md)
and Northstar's economic assumptions (10 percent hurdle rate, 72 percent gross margin). The option
structure, timing, checkpoints, and risks are illustrative. Which CI system to consolidate onto is an
open decision, and so is whether Victor funds the work; the case picks neither.

**Rate.** One rate prices both the effort and the saving: $3,558 an
[engineer-week](../glossary.md#engineer-week-engineer-day-engineer-year) ($185,000 a year ÷ 52), the
book's planning rate. Larger efforts are priced in engineer-years at $185,000.

**Costs and saving.**

| Item | Derivation | Value |
|---|---|---|
| Run cost, four systems | 1.5 FTE × $185,000 | $277,500 a year |
| Run cost, one system | 0.5 FTE × $185,000 | $92,500 a year |
| Saving | difference, all of it capacity | $185,000 a year |
| Full consolidation | about 2 engineer-years × $185,000 | about $370,000 |
| Phase 1 | about 12 engineer-weeks × $3,558 | about $42,700 |
| Payback | $370,000 ÷ $185,000 | 2.0 years of saving after completion |

| Option | One-time | Run cost after | Counted saving a year | What it leaves |
|---|---|---|---|---|
| O1. Do nothing | $0 | $277,500 | $0 | Four systems; the shell-script path that broke rollback in INC-416 |
| O2. Phase 1 only (template with rollback, four shell-script services) | about $42,700 | not counted; assume unchanged | $0 counted | Three systems; auth-svc gains an auditable pipeline |
| O3. Full consolidation onto one system, staged | about $370,000 | $92,500 | $185,000 capacity | One system, after more than two further quarters |

```yaml
case:
  title: Consolidate four CI systems onto one
  prepared_by: Tom Becker and Kwame Mensah, for the Engineering Director
  decider: Victor Lindqvist
  decision_by: week 16
  assumptions:
    cost_per_engineer_year: 185000
    capacity_rate_per_week: 3558
    hurdle_rate: 0.10
    gross_margin: 0.72           # not used: no revenue benefit is counted
problem:
  statement: Four ways to build and deploy 17 units raise run cost, block comparable delivery data,
    and leave tier 1 services without an auditable pipeline with automated rollback
  current_cost:
    - about 1.5 FTE a year of Platform Operations time, about $277,500
    - 2 of 30 baseline Sev1 and Sev2 incidents in ci-cd (INC-416 broken rollback; INC-428 all Jenkins deploys failed)
    - Platform Operations must know all 4 systems; product teams 1 to 2 each
options:
  - {id: O3, name: "full consolidation, staged; phase 1 in quarter 2", one_time_cost: 370000, annual_run_cost: 92500}
benefit:
  value_channel: reduce costs
  formula: (run cost of four systems - run cost of one) x 185000 / 52
  factor_owners: {run_cost_today: Tom Becker, run_cost_after: Kwame Mensah, principal: Tom Becker}
  probability: 1.0               # saving arrives only on completion; stall risk handled by checkpoints
  label: capacity, not cash
  uncounted:
    - auditable pipeline with automated rollback, which every tier 1 service needs
    - comparable delivery data across teams
    - lower cognitive load; less dependence on one Jenkins responder
opportunity_cost:
  displaced_item: about 80 engineer-weeks after phase 1, mostly product teams migrating their own services
  its_cost_of_delay_per_week: not estimated; Amara Okafor to name the displaced items
cost_of_delay:
  per_week: 3558
  urgency_profile: long life, peak unaffected
  class_of_service: standard
  duration_weeks: 104            # illustrative: staged over about two years
  cd3: 0.034                     # 3.558 / 104
  quarter_slip_cost: 46254       # 13 x 3558, capacity
returns:
  payback: 2.0 years of saving after completion
  npv_3y: -182082
  timing: effort at end of years 1 and 2; full saving in year 3 only
risks:
  - {risk: "Stalls after phase 1; four systems become five", likelihood: medium, mitigation: "Retire each old system by date, not by adoption", owner: Tom Becker}
  - {risk: "Migration breaks a renewal path", likelihood: low, mitigation: "erp-sync (accounting integration, due week 19) untouched before then; Core Jenkins not before quarter 3", owner: Kwame Mensah}
decisive_input:
  input: value of the uncounted benefits (lead-time drag, incident risk), same timing as the saving
  base: 0 counted
  break_even: about $4,660 a week   # 182082 x 1.331 / 52, arriving in year 3
  effect: no run-cost value reaches NPV 0 in 3 years (it would need about 2.3 FTE saved, more than
    the 1.5 FTE spent today); on run cost alone NPV turns positive only in year 5
ask:
  decision: Approve phase 1 inside the quarter 2 platform roadmap; decide the target system separately; decide phases 2 and later at week 26 on phase 1 evidence
  funding_source: existing capacity and licenses; no new cash
  checkpoints:
    - {when: week 26, evidence: "template has run one service in production for a month", stop_if: "rollback untested or shell-script services not moved"}
    - {when: week 39, evidence: "units migrated since week 14 and their change failure rate", stop_if: "no unit migrated by a product team"}
  review_date: week 52
```

**Returns.** NPV at 10 percent, with $185,000 of effort at the end of each of years 1 and 2 and the
full saving from year 3 on:

| Horizon | Cumulative NPV |
|---|---|
| 3 years | about −$182,000 |
| 4 years | about −$55,700 |
| 5 years | about +$59,100 |

For the case to break even in three years, the uncounted benefits (lead-time drag and incident risk
the pipeline removes) must be worth about $4,660 a week from year 3 ($182,082 × 1.331 ÷ 52).

What to notice: on counted benefits alone the three-year NPV is negative and payback comes two years
after completion. The honest version of this case says that, labels the saving as capacity rather
than cash, and puts the uncounted benefits, especially the auditable pipeline tier 1 services need,
in front of the decider by name, with the $4,660 a week they would have to be worth.

## Common mistakes

- **Counting the whole current cost as the saving.** The saving is run cost before minus after.
- **Capacity presented as cash.** Saved engineer time is redeployed, not returned to finance; say so.
- **No "do nothing" option.** Without it the decider cannot see what the money buys.
- **Uncounted benefits converted into dollars to close the gap.** Name them instead.
- **Ranking a deadline item by CD3.** Schedule it backward from the date.
- **Sensitivity on the wrong inputs.** Vary the least certain numbers, not the robust ones.
- **An ask with no stop condition or review date.** Without them nobody checks the estimate.

## Review questions

1. Which single input, if wrong, would change the recommended option?
2. What will the people doing this work not do, and what does that cost per week?
3. If the decision slips a quarter, what is lost, and is that loss written in the ask?
4. Which checkpoint would you actually stop at, and who has the authority to stop?

## Evidence and references

Engineering economics is [Chapter 45](../parts/10-business-leadership/45-business-models-and-engineering-economics.md);
this template uses its definitions and gives only the fields. Budgets and financial statements are
Chapter 52.

- [SAFe, WSJF](../references/bibliography.md#safe-wsjf): the framework's relative form of CD3, Weighted
  Shortest Job First.
- [Reinertsen, 2009](../references/bibliography.md#reinertsen2009principles): the book widely credited
  with cost of delay as a decision tool.
- [Arnold and Yüce, 2013](../references/bibliography.md#arnold2013blackswan): the four benefit types
  this template calls value channels.

Using cost of delay and value channels to order work is **practitioner consensus**, not precise
valuation. The field set and the rule that uncounted benefits are named, not priced, are **this
book's recommendation**.

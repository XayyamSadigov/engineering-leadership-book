# Engineering quality scorecard

**Used in:** [Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md)
(design and use), [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
(scorecards in the operating system), [Project 5](../projects/p5-delivery-and-reliability-scorecard.md).
**Owner:** the engineering director, with one scorecard per team rolled up into one for the organization.
Each row has a row owner, who explains its movement, and a data steward, who owns its definition.
**Cadence:** updated weekly from systems; reviewed monthly per team; reset quarterly.

A quality [scorecard](../glossary.md#scorecard) is a short table of about ten measures that tells
leaders whether quality is improving and what to decide next. It is for learning and decisions, not
for rating individuals or ranking teams. Every measure has a paired measure that exposes its likely
gaming, a definition precise enough that two people would compute the same number, and a data source.
Build one when you start a quality program, before setting any targets.

!!! tip "Minimum version"
    On day one, write four to six rows: availability, Sev1 and Sev2 incidents, change failure rate with
    deployment frequency as its pair, and unplanned work, each with a definition, a source, and a
    baseline. Add gaming audits, row owners, and the remaining rows in the first month.

## How to fill it in

1. **Start from outcomes.** Begin with what the organization is accountable for (availability
   commitments, customer impact), then work back to the delivery mechanisms that drive them.
2. **Keep it to ten measures or fewer.** If a measure has not changed a decision in two quarters, drop
   it.
3. **Write the definition, source, and gaming risk first.** Do this for each measure before collecting
   any data. See [metric gaming](../glossary.md#metric-gaming-campbells-law-goodharts-law).
4. **Pair every measure.** Choose a pair whose movement would expose gaming of the first. Change
   failure rate pairs with deployment frequency: a team that stops deploying to protect its failure
   rate becomes visible.
5. **Record a baseline for one full quarter** before setting any targets. Most rows carry a direction,
   not a target.
6. **Prefer measures computed by systems.** Pipeline logs and alert timestamps beat human judgment.
   Audit every measure that depends on human classification, severity above all.
7. **Show the trend and the distribution**, not just the latest value.
8. **Name a row owner and a data steward** for each measure. The person who answers for a number
   should not also be able to redefine it.

## Template

| # | Measure | Definition | Source | Baseline | Current | Direction | Paired with | Gaming risk and audit |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

Header for each team's scorecard:

```yaml
team: ""
manager: ""
components_owned: []        # from the ownership inventory
tier_1_components: []
period: ""                  # for example 2027-Q1
baseline_period: ""
prevention_allocation_pct: 0
notes: ""
```

## Example: Northstar, organization level

!!! info "Northstar so far"
    Quarter 1 of the director's first year. The baseline column is measured data from the quarter before
    the director arrived; the "Current" column is an illustrative mid-quarter reading. See the
    [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Terms used below: [Sev1 and Sev2](../glossary.md#severity-sev1-sev2-sev3) are the two highest
incident severities; [tier 1](../glossary.md#tier-1) components are those on the order and payment
paths; Core is Northstar's shared application.

| # | Measure | Definition | Source | Baseline | Current | Direction | Paired with | Gaming risk and audit |
|---|---|---|---|---|---|---|---|---|
| 1 | Availability, contractual paths | Successful synthetic checks ÷ total checks, order and payment paths, per quarter | Synthetic monitoring | 99.62% | 99.81% | up | 2, 6 | Checks moved or loosened; any change to checks needs director sign-off |
| 2 | Sev1 and Sev2 incidents | Count per quarter under written, customer-impact severity definitions | Incident tracker | 30 | 11 at mid-quarter | down | 3 | Downgrading severity; weekly audit of every Sev3 that touched a tier 1 path |
| 3 | Customer-detected share | Sev1–Sev3 incidents first reported by a customer ÷ all Sev1–Sev3 | Incident tracker, support tickets | 47% | 31% | down | 2 | Incidents opened retroactively to look monitored; compare alert timestamp to first ticket timestamp |
| 4 | Change failure rate, Core | Core releases followed within 72 hours by hotfix, rollback, or linked incident ÷ Core releases | Pipeline and incident tracker | 31% | 24% | down | 5 | Unlinked incidents; staff engineer reviews links weekly |
| 5 | Deployment frequency, Core | Core production releases per month | Pipeline | 2 | 4 | up | 4 | Empty releases; count only releases with at least one change |
| 6 | Time to restore, 90th percentile | 90th percentile of incident start to service restored, Sev1 and Sev2, rolling two quarters | Incident tracker | 14 h | 9 h | down | 2 | Declaring restoration early; restored means the customer path works, checked by synthetic monitoring |
| 7 | Recurrence | Incidents matching a failure mode in a previous review ÷ all Sev1 and Sev2 | Review records | 37% | 27% | down | 8 | Describing failure modes differently; staff engineer assesses matches |
| 8 | Action closure | Review actions closed by due date ÷ actions due | Review records | 32% | 61% | up | 7 | Closing actions without doing them; sample of closed actions verified monthly |
| 9 | Unplanned work | Share of team capacity on unplanned work, two-week sample per team | Ticket sampling | 34% | 32% | down | — | Inconsistent classification; same sampling rules each quarter |
| 10 | Tier 1 readiness | Tier 1 components with owner, alerts, runbook, on-call ÷ tier 1 components | Ownership inventory | 3 of 15 | 6 of 15 | up | 3 | Runbooks that exist but do not work; quarterly runbook drill on two components |

What to notice: only availability carries a target, because a contract sets 99.9 percent. Every
other row has a direction and a pair. Row 9 has no pair, so its audit (the same sampling rules every
quarter) carries the whole load.

## Common mistakes

- **Line coverage as a target.** It rewards tests that execute code without checking it. Use the
  [escaped defect](../glossary.md#escaped-defect) classification to direct testing instead.
- **Counts of activity.** Bugs closed, incident reviews written, and tests added measure effort, not
  quality.
- **Individual engineers' numbers.** People stop reporting honestly once the scorecard can hurt them.
- **Ranking teams against each other.** Teams with different systems and risk profiles are not
  comparable, and ranking invites gaming.
- **Targets on every row.** A target is safe only if hitting it by any means would be welcome. Most
  quality measures fail that test.
- **Unpaired measures.** An incident count without customer-detected share rewards downgrading
  severity.
- **Rows that never change a decision.** Two quarters without a decision means the row should go.

## Review questions

Use these in the monthly quality review.

1. Which measures moved, and what do we believe caused it?
2. Which paired measures moved in the opposite direction, and what does that suggest?
3. What did the [prevention allocation](../glossary.md#prevention-allocation) buy this month?
4. Which classification decisions were audited, and what did the audit find?
5. Which row has not changed a decision in two quarters?
6. What decision does this scorecard require from the director?

## Evidence and references

- The idea that an indicator used for decisions gets bent is usually credited to
  [Campbell, 1979](../references/bibliography.md#campbell1979assessing) (**expert opinion**); it is
  why every row has a gaming risk and an audit.
- Paired indicators are usually credited to [Grove, 1983](../references/bibliography.md#grove1983high)
  (**practitioner consensus**).
- DORA's research, summarized in [Forsgren, Humble, and Kim, 2018](../references/bibliography.md#forsgren2018accelerate),
  reports that speed and stability tend to move together, and the
  [DORA metrics guide](../references/bibliography.md#dora-metrics-guide) defines the delivery rows
  and warns that using its metrics as goals invites gaming (**industry research**; survey-based and
  correlational).
- The ten-row limit, the two-quarter drop rule, and the row owner and data steward roles are **this
  book's recommendation**.

The design rules are in [Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#scorecard-design-rules);
how the scorecard fits the operating system is in
[Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md).

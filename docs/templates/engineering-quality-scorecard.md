# Engineering quality scorecard

**Used in:** Chapter 27 (design and use), Chapter 38 (scorecards in the operating system), Project 5.
**Owner:** the engineering director, with one scorecard per team rolled up into one for the organization.
**Cadence:** updated weekly from systems; reviewed monthly per team; reset quarterly.

A scorecard is for learning and decisions. It is not an individual performance instrument, and it is
not a ranking of teams. Every measure on it has a paired measure that exposes its most likely gaming,
a definition precise enough that two people would compute the same number, and a data source.

## How to fill it in

1. Start from the outcomes the organization is accountable for (availability commitments, customer
   impact) and work back to the delivery mechanisms that drive them.
2. Keep it to ten measures or fewer. If a measure has not changed a decision in two quarters, drop it.
3. For each measure, write the definition, the source, and the gaming risk before collecting any data.
4. Record a baseline for one full quarter before setting any targets.
5. Prefer measures computed by systems. Audit every measure that depends on human classification.
6. Show the trend and the distribution, not just the latest value.

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

**Fictional.** Values are from the [Northstar baseline](../case-studies/northstar/baseline-data.md).
"Current" shows a fictional mid-quarter reading.

| # | Measure | Definition | Source | Baseline | Current | Direction | Paired with | Gaming risk and audit |
|---|---|---|---|---|---|---|---|---|
| 1 | Availability, contractual paths | Successful synthetic checks ÷ total checks, order and payment paths, per quarter | Synthetic monitoring | 99.62% | 99.81% | up | 2, 6 | Checks moved or loosened; any change to checks needs director sign-off |
| 2 | Sev1 and Sev2 incidents | Count per quarter under written, customer-impact severity definitions | Incident tracker | 30 | 11 at mid-quarter | down | 3 | Downgrading severity; weekly audit of every Sev3 that touched a tier 1 path |
| 3 | Customer-detected share | Sev1–Sev3 incidents first reported by a customer ÷ all Sev1–Sev3 | Incident tracker, support tickets | 47% | 31% | down | 2 | Incidents opened retroactively to look monitored; compare alert timestamp to first ticket timestamp |
| 4 | Change fail rate, Core | Core releases followed within 72 hours by hotfix, rollback, or linked incident ÷ Core releases | Pipeline and incident tracker | 31% | 24% | down | 5 | Unlinked incidents; staff engineer reviews links weekly |
| 5 | Deployment frequency, Core | Core production releases per month | Pipeline | 2 | 4 | up | 4 | Empty releases; count only releases with at least one change |
| 6 | Time to restore, 90th percentile | 90th percentile of incident start to service restored, Sev1 and Sev2, rolling two quarters | Incident tracker | 14 h | 9 h | down | 2 | Declaring restoration early; restored means the customer path works, checked by synthetic monitoring |
| 7 | Recurrence | Incidents matching a failure mode in a previous review ÷ all Sev1 and Sev2 | Review records | 37% | 27% | down | 8 | Describing failure modes differently; staff engineer assesses matches |
| 8 | Action closure | Review actions closed by due date ÷ actions due | Review records | 32% | 61% | up | 7 | Closing actions without doing them; sample of closed actions verified monthly |
| 9 | Unplanned work | Share of team capacity on unplanned work, two-week sample per team | Ticket sampling | 34% | 32% | down | — | Inconsistent classification; same sampling rules each quarter |
| 10 | Tier 1 readiness | Tier 1 components with owner, alerts, runbook, on-call ÷ tier 1 components | Ownership inventory | 3 of 15 | 6 of 15 | up | 3 | Runbooks that exist but do not work; quarterly runbook drill on two components |

## What not to put on it

- Line coverage as a target. Use the escaped-defect classification to direct testing instead.
- Counts of activity: bugs closed, postmortems written, tests added.
- Individual engineers' numbers.
- Comparisons that rank teams with different systems and risk profiles against each other.

## Review questions for the monthly quality review

1. Which measures moved, and what do we believe caused it?
2. Which paired measures moved in the opposite direction, and what does that suggest?
3. What did the prevention allocation buy this month?
4. Which classification decisions were audited, and what did the audit find?
5. What decision does this scorecard require from the director?

# Technical debt register

**Used in:** [Chapter 21](../parts/05-engineering-quality/21-technical-debt.md) (debt economics),
[Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md)
(prioritizing internal quality), [Project 3](../projects/p3-quality-transformation-plan.md).
**Owner:** each team keeps its entries; staff engineers review cross-cutting entries; the director
reviews the top of the register quarterly.
**Cadence:** entries added when found; spending reported monthly against named entries; the top of the
register reviewed and re-ranked once a quarter, before planning.

A debt register records the **recurring cost** of a technical shortcut, not opinions about code
quality. [Technical debt](../glossary.md#technical-debt-principal-and-interest) has a principal (the
effort to remove it) and interest (what it costs every period you keep it). An entry that cannot say
what it costs, in whose time or in which risk, is a complaint and belongs in a different list. Use the
register to decide which debt to pay down, with whose capacity, and in what order.

## How to fill it in

1. **Enter only items with a cost.** Each entry needs a stated interest estimate and its source (an
   incident, tickets, a measured slowdown). Small fixes made during feature work need no entry.
2. **Name the component and its owner** from the ownership inventory. Debt in a component with no
   owner cannot be scheduled, so the first action is an ownership decision.
3. **Record interest in two parts.** Time: recurring engineering time, in engineer-days or
   engineer-weeks per period. Risk: incidents, security exposure, or customer impact it causes or
   makes likely.
4. **Estimate the principal as a range**, for example "4 to 8 engineer-weeks".
5. **Name the trigger**: the date or threshold at which interest jumps (a departing expert, a renewal,
   a volume peak, an end-of-life date). Write "none known" if there is none.
6. **List the options, cheapest effective first.** Remove (pay the principal), reduce (pay part of it
   to cut most of the interest), contain (stop it spreading), or accept (record that the interest is
   tolerable, with a review date).
7. **Rank.** Divide annual interest (time plus a conservative money value for risk) by principal.
   Above 1, the fix pays back within a year if the estimates hold. Move any entry with a near trigger
   to the top regardless of ratio.
8. **Record the decision**, who made it, and when. A team decides within its own components and
   standing share; cross-team debt, or debt larger than a team's quarterly share, goes to the director.

## Template

| Field | Meaning |
|---|---|
| ID | Stable identifier, for example `TD-014` |
| Component | Where the debt lives, from the ownership inventory |
| Owner | The team that owns the component |
| Description | What the shortcut is, in one or two sentences |
| Interest: time | Recurring engineering time it costs, with the evidence |
| Interest: risk | Incidents, security exposure, or customer impact it causes or makes likely |
| Principal | Estimated effort to remove it, as a range |
| Trigger | When the cost will rise sharply |
| Options | Remove, reduce, contain, or accept; cheapest effective option first |
| Decision | What was decided, by whom, on what date |
| Review date | When the decision will be revisited |

```yaml
- id: TD-000
  component: ""
  owner: ""
  description: ""
  interest_time: ""        # for example "about 6 engineer-days per quarter: evidence ..."
  interest_risk: ""        # for example "contributed to INC-xxx and INC-yyy"
  principal: ""            # for example "4 to 8 engineer-weeks"
  trigger: ""              # or "none known"
  options: []
  decision: ""
  decided_by: ""
  decided_on: ""
  review_date: ""
```

## Example: Northstar, top five entries

!!! info "Northstar so far"
    Quarter 1, week 4 of the Engineering Director's first year at Northstar Technologies, a fictional
    company. The baseline quarter had 30 Sev1 and Sev2 incidents; Core, the shared application, ships
    every two weeks after a manual regression pass. See the [timeline](../case-studies/northstar/timeline.md)
    and the [cast](../case-studies/northstar/cast.md).

Incident IDs refer to `incidents-last-quarter.csv` in the
[Northstar data](../case-studies/northstar/baseline-data.md). The ones named here: INC-406 (a ledger
index migration locked a table), INC-416 (a shared deploy script change broke rollback for four
services), INC-417 (payments posted to the wrong accounting period after a release), INC-418 (a webhook
format changed without versioning), INC-424 (a long migration let replicas serve stale balances), and
INC-427 (credit notes applied twice after a release).

| ID | Component | Owner | Description | Interest: time | Interest: risk | Principal | Trigger | Decision |
|---|---|---|---|---|---|---|---|---|
| TD-001 | Core release process | Platform Operations (proposed) | Two-week release train with three-day manual regression; all Core changes ship together | Developers wait a median 19 days for production feedback; about 2.4 engineer-years a year of QA time on the manual pass | 9 of 30 incidents last quarter; slowest to restore | 2 quarters for a 4-person working group | Renewal reviews in 2 quarters | Remove incrementally: weekly releases in quarter 1, automated regression for top paths, deploy separated from release |
| TD-002 | Deploy scripts for auth-svc, webhooks, document-store, export-svc | Platform Operations | Hand-maintained shell scripts on one build host, understood by one engineer | About 3 engineer-days per month of manual deploy work; rollback broke in INC-416 | [Single point of knowledge failure](../glossary.md#single-point-of-knowledge-failure) on a [tier 1](../glossary.md#tier-1) service (auth) | 6 to 10 engineer-weeks to move onto the standard pipeline | Departure of the one engineer | Remove in quarter 1, starting with auth-svc |
| TD-003 | core/customer, core/permissions, core/scheduler | none (shared by four teams) | Shared modules with no owner; changes coordinated by chat | Coordination and review delays on every change touching them | No alerts or on-call; recurring contributor to Core release failures | Ownership decision: 1 day; boundaries and contract tests: 1 quarter | — | Assign owners in month 1: core/customer to Orders and core/scheduler to Billing (week 4); core/permissions disputed between Orders and Platform Operations, decision pending under an exemption; contract tests in quarter 2 |
| TD-004 | Core migration practice | Billing | Schema migrations and code changes ship in the same release with no ordering or duration checks | Manual data repairs after INC-406, INC-417 (partly), INC-424, INC-427 | 3 incidents last quarter triggered by migrations, 2 of them recurrences | 4 to 6 engineer-weeks for migration checks in the pipeline | Year-end ledger volumes | Reduce in quarter 1: migration review checklist now, automated checks in quarter 2 |
| TD-005 | Webhook payload format | Payments and Integrations | No versioning of outbound webhook formats | Customer integration breakages handled as support escalations | INC-418; contractual exposure with integration partners | 3 engineer-weeks | Next format change | Contain: freeze format changes until versioning ships in quarter 2 |

What to notice: TD-001 and TD-003 are not code at all; they are a process and an ownership gap, and
both cost more than any single module. TD-005 is contained rather than removed, because freezing the
format costs nothing and stops the interest.

## Common mistakes

- **Registering every disliked piece of code.** The register becomes long, nobody reads it, and the
  expensive entries disappear among the cheap ones. Archive entries without an interest estimate and an
  owner.
- **Recording principal but not interest.** Large refactors look important; small, costly irritants
  are ignored. Rank by interest over principal.
- **No decision field.** A register without decisions is an inventory of regret.
- **No owner.** Debt in shared components (TD-003) is usually the most expensive and least owned.
- **The rewrite pitch.** Removing debt by rewriting a component carries the full principal and delivers
  nothing until finished. Ask for a first slice that cuts measurable interest within one quarter.
- **Silent borrowing.** The standing share is spent on features under deadline pressure. Report
  spending against named entries each month, and record any borrowing with a payback date.
- **Interest inflation.** Once capacity follows estimates, estimates rise. Pair self-reported interest
  with pipeline, ticket, and incident data, and spot-check the top entries each quarter.

## Review questions

1. Which of the top five entries moved since the last review, and did its interest fall?
2. Which entry has a trigger inside the next two quarters, and is it funded?
3. Which entries sit in components with no owner, and who will decide ownership?
4. How much of the standing share went to named entries last month, and where did the rest go?
5. Which interest estimate rests only on self-report, with no system data behind it?

## Evidence and references

The method is [Chapter 21](../parts/05-engineering-quality/21-technical-debt.md); Chapter 27 places
debt work inside the prevention allocation.

- [Cunningham, 1992](../references/bibliography.md#cunningham1992wycash): the origin of the debt
  metaphor, and of interest as the danger.
- [Fowler, 2009](../references/bibliography.md#fowler2009debtquadrant): prudent versus reckless,
  deliberate versus inadvertent debt; useful when entries start to read as blame.
- [Tornhill and Borg, 2022](../references/bibliography.md#tornhill2022codered): the abstract reports
  code health linked to defects and issue time across 39 codebases; a model for measuring interest
  where changes actually happen.
- [SAFe, WSJF](../references/bibliography.md#safe-wsjf): the framework's definition of cost of delay
  over job size, which the ranking rule borrows.

The interest-over-principal ranking, the trigger override, and the 10 to 20 percent standing share
are **this book's recommendation**; no study identifies a correct share.

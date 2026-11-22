# Technical debt register

**Used in:** Chapter 21 (debt economics), Chapter 27 (prioritizing internal quality), Project 3.
**Owner:** each team keeps its entries; staff engineers review cross-cutting entries; the director
reviews the top of the register quarterly.

A debt register records the **recurring cost** of a technical shortcut, not opinions about code
quality. An entry that cannot say what it costs, in whose time or in which risk, is a complaint and
belongs in a different list.

## Fields

| Field | Meaning |
|---|---|
| ID | Stable identifier, for example `TD-014` |
| Component | Where the debt lives, from the ownership inventory |
| Owner | The team that owns the component |
| Description | What the shortcut is, in one or two sentences |
| Interest: time | Recurring engineering time it costs, with the evidence (incidents, tickets, measured slowdowns) |
| Interest: risk | Incidents, security exposure, or customer impact it causes or makes likely |
| Principal | Estimated effort to remove it, as a range |
| Trigger | When the cost will rise sharply (a deadline, a volume threshold, an end-of-life date) |
| Options | Remove, reduce, contain, or accept; with the cheapest effective option first |
| Decision | What was decided, by whom, on what date |
| Review date | When the decision will be revisited |

A simple prioritization that most teams can apply consistently: rank by annual interest (time plus a
conservative money value for risk) divided by principal, then move any entry with a near trigger date
to the top regardless of ratio.

## Template

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

**Fictional.** Incident ids refer to `incidents-last-quarter.csv` in the
[Northstar data](../case-studies/northstar/baseline-data.md).

| ID | Component | Owner | Description | Interest: time | Interest: risk | Principal | Trigger | Decision |
|---|---|---|---|---|---|---|---|---|
| TD-001 | Core release process | Platform Operations (proposed) | Two-week release train with three-day manual regression; all Core changes ship together | Developers wait a median 19 days for production feedback; about 2.4 engineer-years a year of QA time on the manual pass | 9 of 30 incidents last quarter; slowest to restore | 2 quarters for a 4-person working group | Renewal reviews in 2 quarters | Remove incrementally: weekly releases in Q1, automated regression for top paths, deploy separated from release |
| TD-002 | Deploy scripts for auth-svc, webhooks, document-store, export-svc | Platform Operations | Hand-maintained shell scripts on one build host, understood by one engineer | About 3 engineer-days per month of manual deploy work; rollback broke in INC-416 | Single point of knowledge failure on a tier 1 service (auth) | 6 to 10 engineer-weeks to move onto the standard pipeline | Departure of the one engineer | Remove in Q1, starting with auth-svc |
| TD-003 | core/customer, core/permissions, core/scheduler | none (shared by four teams) | Shared modules with no owner; changes coordinated by chat | Coordination and review delays on every change touching them | No alerts or on-call; recurring contributor to Core release failures | Ownership decision: 1 day; boundaries and contract tests: 1 quarter | — | Assign owners in month 1: core/customer to Orders and core/scheduler to Billing (week 4); core/permissions disputed between Orders and Platform Operations, decision pending under an exemption; contract tests in Q2 |
| TD-004 | Core migration practice | Billing | Schema migrations and code changes ship in the same release with no ordering or duration checks | Manual data repairs after INC-406, INC-417 (partly), INC-424, INC-427 | 3 incidents last quarter triggered by migrations, 2 of them recurrences | 4 to 6 engineer-weeks for migration checks in the pipeline | Year-end ledger volumes | Reduce in Q1: migration review checklist now, automated checks in Q2 |
| TD-005 | Webhook payload format | Payments and Integrations | No versioning of outbound webhook formats | Customer integration breakages handled as support escalations | INC-418; contractual exposure with integration partners | 3 engineer-weeks | Next format change | Contain: freeze format changes until versioning ships in Q2 |

## Common mistakes

- Registering every disliked piece of code. The register becomes long, nobody reads it, and the
  expensive entries disappear among the cheap ones.
- Recording principal but not interest. Large refactors look important; small, costly irritants are
  ignored.
- No decision field. A register without decisions is an inventory of regret.
- No owner. Debt in shared components (TD-003) is usually the most expensive and least owned.

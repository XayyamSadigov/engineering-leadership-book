# Organizational design assessment

**Used in:** [Chapter 33](../parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md)
(team types and cognitive load), [Chapter 34](../parts/07-organization-design/34-spans-layers-and-dependency-mapping.md)
(spans, layers, and dependency mapping), [Chapter 35](../parts/07-organization-design/35-designing-organizations-at-four-scales.md)
(designing organizations at four scales), [Project 4](../projects/p4-redesign-an-80-engineer-organization.md).
**Owner:** the engineering director, with each manager supplying the team rows.
**Cadence:** once a year, and before any proposed reorganization; refreshed when a team's scope
changes.

An organizational design assessment describes the current structure as evidence, before anyone draws
a new chart. It answers four questions. Are the [spans](../glossary.md#span-of-control) (people per
manager) workable? Where does work cross team lines? What has no owner? Which team carries more
[cognitive load](../glossary.md#cognitive-load) than it can hold? Options come last, each with its
[transition cost](../glossary.md#transition-cost).

## How to fill it in

1. Fix the date and the strategy question the structure must serve (for example: "meet the
   availability commitment without headcount growth").
2. Fill the team inventory from HR and the ownership inventory, not from memory. Count quality,
   infrastructure, and specialist engineers where they report.
3. Score each manager's span against the factors in Chapter 34 (other work, change, experience mix,
   interdependence, location), and give a target range per manager.
4. Build the dependency matrix for one quarter: requesting team by providing team, work items of a
   week or more. Classify the heaviest links by what changed.
5. List every component without a clear owner, on-call rotation, or two people who can change it.
6. For each team, count domains, components, and the capacity left after unplanned work,
   commitments, and prevention (the arithmetic in Chapter 33).
7. Write two to four options, including "no structural change". For each, recount the links and
   spans and state the transition cost in engineer-weeks and seats.

## Template

**Team inventory**

| Team | Manager | People | Span target | Closest team type | Components (tier 1) | Domains | On-call rotations | Unplanned work |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

**Dependency matrix** (rows request, columns provide; one quarter)

| Requesting ↓ / Providing → | Team A | Team B | Team C | Total requested |
|---|---|---|---|---|
| Team A | — | | | |
| Total received | | | | |

**Ownership gaps**

| Component | Tier | Gap (no owner, disputed, no on-call, one capable person) | Interim cover | Decision owner and date |
|---|---|---|---|---|

**Options**

| Option | Change | Spans after | Links removed / created | Seats | Transition cost | Risks and trigger to revisit |
|---|---|---|---|---|---|---|

One record per team, so that the assessment can be regenerated next year:

```yaml
team:
  name: ""
  manager: ""
  people: 0
  span_target: [8, 10]       # from the five span factors
  team_type: ""              # stream-aligned, platform, enabling, complicated subsystem (see glossary: team types)
  components: []
  tier_1_components: []
  domains: 0
  unplanned_work_pct: 0
  capacity_left_engineers: 0 # after unplanned work, commitments, prevention
  dependencies:
    requested: 0
    received: 0
  gaps: []
  as_of: ""
```

## Example: Northstar, quarters 2 to 4 (inventory as of quarter 2; options as of week 44)

!!! info "Northstar so far"
    Northstar Technologies is a fictional company: 80 engineers (3 of them staff engineers), six
    managers, and an Engineering Director, 87 people held flat by the CTO's mandate. In week 10 the seven QA engineers moved into product teams; in week 44 the director drafts a year-2
    organization for Victor Lindqvist (CTO) to decide. See the
    [timeline](../case-studies/northstar/timeline.md) and the [cast](../case-studies/northstar/cast.md).

**Strategy question:** can the structure carry the reliability mandate and both renewal commitments
at flat headcount (87 people)?

**Team inventory, after week 10** (seven QA engineers moved into product teams):

| Team | Manager | People | Closest type, and where untrue | Components |
|---|---|---|---|---|
| Orders | Priya Raman | 16 | Stream-aligned; six domains, seven components | order-capture, catalog, pricing-rules, pricing-svc, search-svc, core/customer, notification-svc (from quarter 2) |
| Billing | Marcus Oyelaran | 15 | Stream-aligned; ledger behaves like a complicated subsystem with three experts | invoicing, ledger, scheduler, tax-svc, invoice-render |
| Payments and Integrations | Elena Sokolova | 13 | Stream-aligned; two streams | payments-gateway, bank-connectors, erp-sync, webhooks |
| Customer Experience | Daniel Cho | 17 | Organized by channel; two sites | web-app, mobile-app, mobile-bff |
| Data and Analytics | Farah Haddad | 11 | Mixed; 12 points of capacity on other teams' requests | reporting-api, export-svc, warehouse pipelines |
| Platform Operations | Tom Becker | 5 | Platform in name; interrupt sink | ci-cd, cloud infrastructure, release train, auth-svc |
| Staff engineers | Director | 3 | Enabling, perhaps | none |

The rows total 80 engineers. The director has nine direct reports: six managers and three staff
engineers.

**Spans.** By the five factors every span is outside its range: Daniel at 17 across two sites,
Priya at 16 in her first year, Billing at 15, Payments and Integrations at 13, Farah at 11 while
still her team's data architect, and Tom at 5, too small to fill a manager's job.

**Dependency matrix, baseline quarter** (86 links, items of a week or more):

| Requesting ↓ / Providing → | Ord | Bil | Pay | CX | Data | Plat | Total |
|---|---|---|---|---|---|---|---|
| Orders | — | 9 | 2 | 3 | 1 | 8 | 23 |
| Billing | 6 | — | 5 | 1 | 2 | 7 | 21 |
| Payments and Integrations | 1 | 4 | — | 1 | 0 | 5 | 11 |
| Customer Experience | 8 | 3 | 2 | — | 1 | 6 | 20 |
| Data and Analytics | 2 | 2 | 1 | 0 | — | 3 | 8 |
| Platform Operations | 1 | 1 | 0 | 1 | 0 | — | 3 |
| **Received** | **18** | **19** | **10** | **6** | **4** | **29** | **86** |

The heaviest pair is Orders and Billing, 15 links; 6 of Orders' 9 were order-to-invoice mapping
changes in core/invoicing. Platform Operations receives a third of all links, most of them test
environments.

**Ownership gaps:**

| Component | Tier | Gap | Interim cover |
|---|---|---|---|
| core/permissions | 1 | No owner | Recorded exemption; Priya Raman would accept it after week 26 |
| search-svc | 2 | Owned by Orders, where 0 engineers can change it safely | Its authors in Data and Analytics |
| document-store | 2 | Orphaned; shared shell-script deploy | None |
| notification-svc | 2 | Moved to Orders; 3 have committed to it, none has operated it | None |

**Cognitive load of Orders.** After unplanned work, the renewal feature, and prevention, Orders has
about 2.6 engineers left for everything else: the rest of the roadmap, the
[tier 1 operational minimums](../glossary.md#tier-1-operational-minimums) on core/customer, and the
permissions extraction.

| Orders, one quarter | Engineer-weeks |
|---|---|
| Capacity (14 engineers × 13 weeks) | 182 |
| Unplanned work (36 percent) | −65.5 |
| Bulk ordering (renewal commitment) | −65 |
| Prevention | −18.2 |
| **Left** | **33.3** (about 2.6 engineers) |
 Among its four tier 1 components, core/customer has two engineers who
can change it safely and core/pricing-rules four; search-svc (tier 2) has none.

**Options** (the year-2 proposal of week 44 is option A):

| Option | Change | Seats | Transition cost and risk |
|---|---|---|---|
| A. Year-2 proposal | Customer Experience splits into Web (Daniel, 11) and Mobile (Mateo Arango Ríos, 5); core/permissions to Orders; search-svc to Data and Analytics; Platform Operations becomes Developer Platform | 79 engineers, 7 managers; one seat | About 21 engineer-weeks; Orders 16, Billing 15, Payments 13 stay above range; director at 10 reports |
| B. Customer Experience whole, two subteams | No new manager | 80 engineers, 6 managers | Daniel stays at 17 |
| C. A, plus Orders split and the platform grown to 8 | Order Capture; Catalog and Pricing | 78 engineers, 8 managers | About 4 new links and about 58 co-changing merge requests a quarter cross owners |
| D. Two managers of managers | A layer over order-to-cash | 77 engineers, 9 managers | 27 links resolved one level down; 48 links gain a hop; a peer promoted over peers |

Every option totals 87 people: engineers plus managers plus the director. The quarter 2 alternative to moving people was cheaper: a Billing-owned
order-to-invoice contract with contract tests on both sides.

## Common mistakes

- **Drawing the chart first.** Options come after the matrix and the gaps, not before.
- **Counting links but not recounting them.** A move that removes six links and creates five is not
  worth a reorganization.
- **Ignoring seats.** Under flat headcount every new manager is an engineer who stops building.
- **Leaving out "no structural change".** It is often the right option for one more quarter. At
  Northstar, a Billing-owned contract cut the heaviest dependency without moving anyone.
- **Filling the inventory from memory.** Team sizes and components come from HR and the ownership
  inventory; memory undercounts specialists and orphaned components.

## Review questions

1. Which strategy question does each option answer better than the current structure?
2. Which spans does each option leave out of range, and why is that acceptable?
3. Which links does each option create that the current matrix cannot see?
4. Who owns every tier 1 component on day one of the new structure?
5. What evidence, on what date, would make us reverse the change?

## Evidence and references

The method is in Chapters 33 to 35.

- [Conway, 1968](../references/bibliography.md#conway1968committees): systems copy the communication
  structure of the organization that builds them; an argument rather than a study.
- [Colfer and Baldwin, 2016](../references/bibliography.md#colfer2016mirroring): a review of studies on
  how far product structure mirrors organization structure, and when it does not.
- [Cataldo, Herbsleb, and Carley, 2008](../references/bibliography.md#cataldo2008congruence): faster
  resolution when coordination matches dependencies; the reason for the dependency matrix.
- [Skelton and Pais, 2019](../references/bibliography.md#skelton2019team): team types, interaction
  modes, and team cognitive load as vocabulary (**practitioner consensus**).
- [Larson, 2018](../references/bibliography.md#larson2018sizing): practitioner benchmarks for span
  sizes (**expert opinion**).

The four-part structure, the five span factors, and the rule that options carry seats and transition
cost are **this book's recommendation**.

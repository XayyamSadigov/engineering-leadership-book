# Project 4 solution: Northstar's year-2 organization

This is one worked answer to [Project 4](../p4-redesign-an-80-engineer-organization.md). It treats the
director's week-44 proposal in [Chapter 35](../../parts/07-organization-design/35-designing-organizations-at-four-scales.md)
as a submission to be tested, not as the answer. The conclusion is that the proposal is the right
shape, fails one acceptance criterion as written, and needs five amendments. Alternatives B, C, and D
are evaluated with their strongest case. All Northstar facts are fictional; estimates marked as this
solution's are assumptions, not canon.

## 1. Starting state, checked twice

From [`p4-week44-roster.csv`](../data/p4-week44-roster.csv):

| Team | Manager | Engineers | Sites | Components |
|---|---|---|---|---|
| Orders | Priya Raman | 16 | Minneapolis 14, remote 2 | 7 |
| Billing | Marcus Oyelaran | 15 | Minneapolis 12, remote 3 | 5 |
| Payments and Integrations | Elena Sokolova | 13 | Minneapolis 7, Bogotá 5, remote 1 | 4 |
| Customer Experience | Daniel Cho | 17 | Minneapolis 9, Bogotá 6, remote 2 | 3 |
| Data and Analytics | Farah Haddad | 11 | Minneapolis 4, Bogotá 5, remote 2 | 3 |
| Platform Operations | Tom Becker | 5 | Minneapolis 3, remote 2 | 4 |
| Staff engineers | director | 3 | Minneapolis 3 | none |

**By team:** 16 + 15 + 13 + 17 + 11 + 5 + 3 = 80 engineers. **By site:** 52 + 16 + 12 = 80. Plus 6
managers and the director: 87. Components: 7 + 5 + 4 + 3 + 3 + 4 = 26 owned, plus core/permissions and
document-store unowned, 28 in all (the 24 in the components file plus warehouse pipelines, ci-cd, cloud
infrastructure, and the release train).

**Dependency links, rechecked.** Outgoing: Orders 23, Billing 21, Payments 11, Customer Experience 20,
Data 8, Platform 3, total 86. Incoming: Platform 29, Billing 19, Orders 18, Payments 10, Customer
Experience 6, Data 4, total 86. Among Orders, Billing, and Payments: 9 + 6 + 2 + 1 + 5 + 4 = 27. Among
Customer Experience, Data, and Platform: 1 + 6 + 3 + 1 = 11. Between the two groups: 86 − 27 − 11 =
48, matching Chapter 34.

## 2. Breakage register

| Breakage | Evidence | Cheaper answer tested | Verdict |
|---|---|---|---|
| Customer Experience is two products on two sites under one manager | Span 17; one board and sprint for web and mobile; mobile red on 4 of 10 health indicators in week 16; 6 of the last 8 retrospective actions about web; two of four baseline Sev2 at the mobile-bff and mobile boundary; Mateo doing lead work unrecognized for over a year | Subteams with Mateo and Hannah as tech leads (alternative B) | Not enough on its own: it fixes the board and recognition, not a 17-person span across sites, and leaves Bogotá's six mobile engineers with a Minneapolis manager whose one-on-ones were mostly status (55 of 84) |
| core/permissions has no owner | Tier 1; 38 merge requests from four teams in the baseline quarter; exemption recorded in quarter 1 | Exemption renewal | Fails the standard: exemptions expire after at most two quarters. This one reached the maximum at week 39 and lapsed without renewal |
| document-store has no owner | Orphaned since baseline; one open critical vulnerability at baseline; two callers, invoice-render (Billing) and core/order-capture (Orders) | None tried in the canon | Needs an owner; ownership, not structure |
| search-svc ownership is nominal | Owned by Orders, written by engineers in Data and Analytics; 0 Orders engineers can change it safely (week 14); INC-407 with nobody on call | Fund Orders' learning | Learning is unfunded in Orders (about 2.6 engineers left in quarter 2); move it to its authors |
| Orders is overloaded | Span 16 for a first-year manager; seven components across six domains | Tech leads inside Orders; moving search-svc out | Partly enough for year 2; the split stays as a triggered option |
| Platform is still a queue | Five engineers, two on rotation; requests down from 20 to 14 points | Self-service and a product statement | Enough for now: rename and a product, no growth until consolidation proves adoption |
| Orders and Billing friction | 15 links, the heaviest pair; blame in reviews | Billing-owned order-to-invoice contract (quarter 2) | Left alone deliberately until its effect is measured |
| Director's span | 9 reports, 10 under the proposal | Staff mandates reduce coaching load | Acceptable; trigger named for a layer |

The deliberate non-answer is the Orders and Billing pair. Moving the mapping (Chapter 34's M3) removes
the most links and puts invoice correctness in the team that did not build it. The contract is
cheaper and already in place; the year-2 design waits for evidence.

## 3. Options with arithmetic

**Z. Do nothing.** 80 engineers, 6 managers, director: 87. Spans 16, 15, 13, 17, 11, 5; director 9.
Seats converted: 0. People moved: 0. It leaves core/permissions and document-store unowned, which
breaks constraint 3 and the exemption rule. Z fails the project's constraints, so it is a baseline,
not a candidate.

**A. Chapter 35's proposal.** Orders 16 (takes core/permissions, gives up search-svc), Billing 15,
Payments 13, Web 11 (Daniel Cho: 9 web and 2 quality engineers), Mobile 5 (Mateo Arango Ríos, his seat
not backfilled), Data 11 (takes search-svc), Developer Platform 5, staff 3.

- By team: 16 + 15 + 13 + 11 + 5 + 11 + 5 + 3 = 79 engineers.
- By role: 80 engineers − 1 converted seat = 79; 6 + 1 = 7 managers; 79 + 7 + 1 = 87.
- Director reports: 7 + 3 = 10. Seats: 1, about $185,000 a year, 1.25 percent of capacity.
- People changing manager: 6 (Mateo and five mobile engineers). Components changing owner: 2.

**B. Keep Customer Experience whole with two subteams.** Same as A except Customer Experience stays at
17 under Daniel Cho, with Hannah Lindgren and Mateo as named tech leads of web and mobile. This
solution assumes B keeps A's two component moves; Chapter 35 does not say.

- 16 + 15 + 13 + 17 + 11 + 5 + 3 = 80 engineers; 6 managers; 87. Director 9. Seats 0. People
  changing manager 0.

**C. A plus an Orders split and a larger platform.** Order Capture 9 (Priya Raman), Catalog and
Pricing 6 (a manager from Orders, seat not backfilled), platform 8 with one transfer each from Billing,
Payments, and Data.

- 9 + 6 + 14 + 12 + 11 + 5 + 10 + 8 + 3 = 78 engineers. Check by role: 80 − 2 seats = 78; 8 managers;
  78 + 8 + 1 = 87. Director 8 + 3 = 11. Seats 2, about $370,000 a year.
- People changing manager or team: A's 6, plus 6 Catalog and Pricing engineers and their new manager,
  plus 3 transfers: about 16.

**D. A plus two managers of managers.** An order-to-cash group (Orders, Billing, Payments) and an
experience-and-platform group (Web, Mobile, Data, Developer Platform), each led by an engineer promoted
from within, seats not backfilled.

- 79 − 2 = 77 engineers; 7 + 2 = 9 managers; 77 + 9 + 1 = 87. Director 2 + 3 = 5. Seats 3 (Mateo
  plus two), about $555,000 a year, 3.75 percent of capacity.

| | Z | A | B | C | D |
|---|---|---|---|---|---|
| Engineers | 80 | 79 | 80 | 78 | 77 |
| Managers | 6 | 7 | 6 | 8 | 9 |
| Director reports | 9 | 10 | 9 | 11 | 5 |
| Largest span | 17 | 16 | 17 | 14 | 16 |
| Seats converted | 0 | 1 | 0 | 2 | 3 |
| People moved | 0 | 6 | 0 | about 16 | 6 plus two leads |
| Unowned components | 2 | 1 (document-store) | 1 | 1 | 1 |

The last row is the finding Chapter 35's draft does not show: A, as written, places 23 of the 24
components in the components file and leaves document-store out. It fails acceptance criterion 2.

## 4. Dependency overlay

All 86 baseline links are between existing teams, so they cross a boundary today and under every
option. What differs is which new boundaries each option creates and which links it moves.

| Option | Links moved inside a boundary | New boundaries | Cannot count |
|---|---|---|---|
| A | None of the 86. search-svc's move turns some of Customer Experience's 2 "search-svc or pricing-svc" links into Data links | Web and Mobile; core/permissions reviews (21 of 38 merge requests from three other teams now need Orders) | Web to Mobile links; how the 2 search or pricing links split |
| B | As A | None for people; subteams share a manager | Same, but cheaper to discover inside one team |
| C | As A | Order Capture and Catalog and Pricing: about 4 work items a quarter and about 58 co-changing merge requests (53 percent of 110) if pricing-rules goes with Catalog and Pricing | Platform transfers' effect on the 29 links into Platform |
| D | 27 links settle inside the order-to-cash group, 11 inside the other | Group boundary: 48 links gain a hop to a manager of managers | Whether disputes actually move down a level |

Recount for C's seam: keeping pricing-rules with Order Capture keeps the 53 percent pair together and
leaves Catalog and Pricing with catalog and pricing-svc. The 4 work items that touched both order
capture and pricing, catalog, or search do not all cross, but the count does not say how many would.

## 5. Evaluation of the proposal and the alternatives

**A's strengths.** It makes one structural move where the evidence is strongest and settles two
recorded disputes by assignment. It costs one seat. It recognizes Mateo, who has done the work for over
a year, and puts the first manager in Bogotá, where 16 engineers work with no local manager. The
transition is small: about 21 engineer-weeks, about 2 percent of 1,040 (Chapter 36: 2.5 + 6 + 1 + 7.4 +
3.8 = 20.7).

**A's weaknesses, honestly.**

1. **document-store is left out.** Fix: assign it to Billing, whose invoice-render is the heavier
   caller (it stores rendered invoices), with a pages check after one quarter; branch to Orders if
   Billing's after-hours load rises.
2. **Orders gets heavier, not lighter.** It keeps 16, loses one zero-knowledge component (search-svc)
   and gains a tier 1 module that two of its engineers will learn from scratch, and whose other 21
   merge requests a quarter now queue on its reviewers. The proposal relies on a trigger to revisit C.
   It should also use Chapter 35's cheaper answer: name Aisha Bello and, if he chooses the staff
   track, Rafael Duarte as tech leads, and give core/permissions an owner-based review rule with one
   named reviewer each from Customer Experience and Billing, so the 21 do not wait on Priya's team
   alone.
3. **Mobile becomes a six-person rotation in one city.** Five engineers plus Mateo carry mobile-app
   and mobile-bff on call. The transition plan names backup cover; the proposal should say whose
   (for example, two named Web engineers trained on mobile-bff, the component where two of the baseline
   Sev2 incidents sat), and for how long.
4. **The new manager has no cover and no developer.** The succession table has Mateo as Customer
   Experience's development candidate; promoting him leaves Mobile with nobody. The plan adds a step in
   week 49; the proposal should name who develops Mateo (Elena Sokolova, whose team also spans
   Minneapolis and Bogotá, is a reasonable choice) and a senior mobile engineer to run Mobile's
   planning as a development action.
5. **Data and Analytics takes load it may not have room for.** It already gives 12 points of capacity
   to other teams' requests, and Farah Haddad holds two roles. search-svc should move only with the
   team charter accepting it, and with Sunil Varghese co-owning warehouse architecture as the
   succession actions propose.

**B: the strongest case.** Zero seats, zero people moved, fully reversible, and it answers
recognition: Mateo gets the lead title and authority over mobile's board. If Victor Lindqvist will not
release a seat, B is the right branch, not a failure. Its weakness is the span and the site: Daniel
stays at 17 across two cities, and the red indicators came under exactly that arrangement. B is this
solution's fallback.

**C: the strongest case.** It fixes the second-worst span, halves Orders' domains, and the platform
transfers are funded by measured waste (four CI systems at about 1.5 FTE against about 0.5 for one).
Its costs: two seats; about 16 people moved; a new boundary through the most coupled part of Core
unless the seam is redrawn; and a second split before the first has settled. This solution's estimate
of C's transition cost, using Chapter 36's method (assumptions: 6 Catalog and Pricing engineers at 0.5
each, 3.0; 16 Orders engineers separating board and cadence at 10 percent for 2 weeks, 3.2; 3 platform
transfers ramping at 3 each, 9.0, with 0.6 of handoff each, 1.8; management: Priya 0.8, the new
manager 1.6, Tom Becker 1.6, three losing managers 0.2 each, 0.6), is about 21.6 on top of A's 21, so
about 43 engineer-weeks, roughly twice A. Verdict: deferred, not rejected. Triggers below.

**D: the strongest case.** The director at 10 reports includes two first-year managers (Priya and
Mateo) and a manager of 16; a manager of managers over order-to-cash would settle the Orders and
Billing friction one level down, where it has only ever been handled above both managers. Against it:
three seats; a layer between the director and the reliability work; 48 links gain a hop; two
first-time managers of managers with nobody to develop them; and, in the director's own assessment,
the managers are getting monthly development time and decisions are not queuing. D answers a breakage
not yet observed: Chapter 35's premature layer. Victor's "we will be 100 in two years" is a headcount
formula while growth is unapproved. The cost of moving to D later is one more reorganization; the cost
of D now is three seats every quarter until then.

## 6. Recommendation: A, amended

A with five amendments: document-store to Billing; tech leads and a shared review rule for Orders and
core/permissions; named backup cover for Mobile's rotation; a developer and a development candidate
for Mobile's manager; search-svc conditional on Data's charter. The arithmetic is unchanged: 79
engineers, 7 managers, the director, 87.

**Ownership table under the recommendation.**

| Team | Components | Tier 1 among them |
|---|---|---|
| Orders | core/order-capture, core/catalog, core/pricing-rules, core/customer, core/permissions, pricing-svc, notification-svc | order-capture, pricing-rules, customer, permissions, pricing-svc |
| Billing | core/invoicing, core/ledger, core/scheduler, tax-svc, invoice-render, document-store | invoicing, ledger, tax-svc |
| Payments and Integrations | payments-gateway, bank-connectors, erp-sync, webhooks | payments-gateway, bank-connectors |
| Web | web-app | web-app |
| Mobile | mobile-app, mobile-bff | both |
| Data and Analytics | reporting-api, export-svc, search-svc, warehouse pipelines | none |
| Developer Platform | auth-svc, ci-cd, cloud infrastructure, release train | auth-svc |

Count: 7 + 6 + 4 + 1 + 2 + 4 + 4 = 28, every component once. Tier 1: 5 + 3 + 2 + 1 + 2 + 0 + 1 = 14,
which is the 15 proposed tier 1 components less notification-svc, moved to tier 2 in quarter 2.

**Transition cost.** Chapter 36's 20.7 engineer-weeks, plus this solution's estimate for the
amendments: document-store ramp-up for 2 Billing engineers at 1 each (2), review-rule setup for
core/permissions (2 reviewers at 0.5, 1), Marcus Oyelaran at 5 percent for 4 weeks (0.2): about 24
engineer-weeks, about 2.3 percent of a quarter's 1,040. Mateo's seat (about 13 engineer-weeks a
quarter) is counted separately as the seat.

**Plan.** Chapter 36's week-by-week plan holds (decision 46, announcement 51, reporting lines 53,
search-svc 54, core/permissions readiness 53 to 56, all handoffs 57, review 64), with document-store
moving in week 55 after core/permissions settles, so Billing and Orders do not absorb new tier 1
work in the same week. What does not change: pay, levels, the ledger rotation, the weekly Core
release, and membership of every other team.

**Staff mandates (summary).** Ines Carvalho: Core module boundaries and the permissions extraction;
decides module dependency rules, advises on team boundaries. Kwame Mensah: operational minimums,
pipelines, and Developer Platform's technical direction; decides pipeline standards. Li Na Zhou: data,
migration, configuration, and integration contracts; decides migration and contract standards, advises
on search-svc's place in Data and Analytics. Each reports to the director and has a named development
successor from the week-44 table.

**Developer Platform product statement.** One way to build, test, and deploy, and test environments
without a ticket. Measures: share of deployable units on the consolidation target, and median wait
for an environment. It refuses component ownership beyond auth-svc and the delivery path.

## 7. Succession, redone for seven teams

The week-44 count: 10 roles, 0 ready now, 6 interim, 4 none. The recommendation adds Mobile manager
as an eleventh critical role.

| Role | Change under the recommendation |
|---|---|
| Customer Experience becomes Web | Hannah Lindgren stays interim cover; Mateo leaves the development column, so Web has interim cover and no development candidate |
| Mobile (new) | No interim cover at announcement; the amendment names a senior mobile engineer as development candidate, which is development, not interim cover |
| Orders | Unchanged: Aisha Bello interim; tech lead roles make the development real |
| Billing | Still none; the Teodora Vasquez-Lund management-trial question is the only action |

Count after the change, if the development action is in place by week 51: 11 roles, 0 ready now, 6
interim, 5 with none (Billing, Data and Analytics, Mobile, and the two staff roles). Count again by
column: interim covers are Orders, Payments, Web, Platform, infrastructure staff, director, which is 6;
6 + 5 = 11. The design opens one gap. That is the honest price of recognizing Mateo, and the reason
the week-49 redo in Chapter 36 matters.

## 8. Decisions, inputs, branches, triggers

| Input | Branch |
|---|---|
| Victor will not release a seat | B with the same component moves and amendments; revisit in two quarters |
| Mateo does not want the role | B with Mateo as mobile tech lead; no other Bogotá candidate exists, so no Mobile team |
| Rafael Duarte chooses management | He becomes Orders' development candidate and the natural Catalog and Pricing manager if C is triggered |
| Data's charter refuses search-svc | search-svc stays with Orders under an exemption of one quarter with a funded learning plan |
| The order-to-invoice contract has not shortened waits | Reopen M3 at the two-quarter review; do not add a layer for it |
| Tomasz Wierzbicki left after his week-20 offer | Billing's ledger cover is thinner; do not add document-store to Billing; give it to Orders |

**Evidence at the week-64 review and after two quarters:** Mobile's health indicators against the
week-16 check; Mobile after-hours pages per person; Web to Mobile dependency links, counted for the
first time; core/permissions passing the four operational minimums by week 56 and its merge-request
wait; Orders' lead time and on-call load against the quarter before; the director's monthly time per
manager.

**Triggers.** For C: Orders' median lead time or after-hours pages rising for two consecutive months
after week 57, or core/permissions merge requests waiting longer than core/order-capture's. For D:
approved headcount growth, or manager development sessions falling below monthly for two quarters, or
cross-team decisions waiting on the director for more than a week. For a platform transfer: the
consolidation phase 1 adopted by the four shell-script services, and the redundant CI cost measured.

## How the rubric applies

**Chapter 35's draft, scored as a submission:** breakages 13 of 15 (strong evidence, cheaper answers
mostly implicit); arithmetic 10 of 15 (all totals right, document-store missing, which fails
acceptance criterion 2); dependency fit 12 of 15 (Chapter 34's overlay supports it; the core/permissions
review load is noted but not answered); options 17 of 20 (B, C, D with real costs and named triggers);
transition 9 of 10 (Chapter 36's estimate and plan); people 11 of 15 (succession done, but the plan
discovered Mobile's gap after the proposal rather than designing for it); triggers 9 of 10. Total 81,
a strong design that would not pass until the component is placed. This solution's amendments target
exactly the lost points.

**A weak submission** looks like this:

> "At 80 engineers we have outgrown a flat structure. We propose two directors, each with three or
> four teams of about ten, aligned to product lines: Ordering and Money. Platform Operations is
> disbanded and its engineers join product teams. Managers will be hired as needed. This will improve
> productivity by 20 percent."

Against the rubric: structure justified by a headcount number (breakages weak); "hired as needed"
breaks flat headcount and the arithmetic is absent (arithmetic weak); product lines drawn without the
co-change data or the 86 links, and disbanding the platform returns its 29 incoming links to every
team (dependency weak); one option, no alternatives (options weak); no transition cost (transition
weak); no names, no succession, no mention of Bogotá (people weak); a productivity promise no
evidence supports (triggers weak). It fails acceptance criteria 1, 2, 3, 4, and 6.

**An adequate submission** reproduces the proposal with correct arithmetic, mentions B and D briefly,
and gives the transition plan, but does not notice document-store, does not redo succession, and
assumes Victor approves the seat. It scores around 60.

**What separates excellent from adequate:** completeness checked by counting (every person, every
component, every link), the strongest case written for the options rejected, and an explicit branch for
every decision someone else owns.

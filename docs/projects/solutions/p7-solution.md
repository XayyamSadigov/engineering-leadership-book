# Project 7 solution: Northstar's year-2 engineering strategy

!!! warning "Awaiting human review"
    This solution has passed the book's automated validation and an editorial self-review, but not yet
    the human review in which each cited claim is checked against its source. Treat it as a reviewed
    draft. Corrections are welcome; see the repository's CONTRIBUTING file.

This is one worked answer to [Project 7](../p7-twelve-month-engineering-strategy.md). It starts by grading
the week-14 strategy draft in [Chapter 30](../../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md),
because the most useful lesson for year 2 is in what happened to it: its diagnosis held, and none of the
three decisions its policies were tested against is recorded as made 33 weeks later. The year-2 strategy
below therefore keeps the diagnosis short, puts correctness next to availability, and gives every policy a
decider and a date. It is this solution's recommendation, one defensible answer among several. All
Northstar facts are fictional; estimates marked as this solution's are assumptions, not canon.

## 1. What the week-14 draft decided

| Week-14 policy | Test decision | Status at week 47 | Verdict |
|---|---|---|---|
| P1. Converge before adding | CI consolidation target (DL-10) | Open. GitLab CI was proposed in quarter 2; the continuation proposal makes the target a stage 2 decision | Keep the rule; give the decision a decider and a date |
| P2. Own order-to-cash logic; buy what changes for outside reasons | tax-svc build, buy, or hybrid (DL-09) | Open in the week-26 decision log; no later outcome recorded | Keep as a selection rule inside the new P3; decide tax-svc by a date |
| P3. Supported versions and two people for every tier 1 component | Core framework migration (TR-01) | No funding decision recorded; 120 to 180 engineer-days still unscheduled. Two of the three ledger engineers were promoted to Senior, which recognizes the concentration without reducing it | Keep, with capacity attached and a deadline |

**Why so little was decided.** The diagnosis was right and the policies passed the template's tests. Four
things were missing. First, the escalation action gave the director ten working days to decide
*exceptions*, but the test decisions were not exceptions; they were choices nobody had to make by a date.
Second, no decider was mapped: ADR-0001 sat open from week 14 for the same reason ([Chapter 28](../../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md)).
Third, the transitions had owners but no capacity: the staff engineers owned policies while their time
went to the permissions extraction, the quality program, and the year-2 proposal. Fourth, the draft never
entered the operating system: its review in week 26 is not recorded, and nothing in the monthly business
review asked about it. Will Larson calls coherent actions the most important part of a strategy, and sorts
them into enforcements, escalations, and transitions
([Larson, 2023](../../references/bibliography.md#larson2023engstrategy); **expert opinion**). The week-14
draft had all three kinds; its escalations had no clock.

## 2. Readings the strategy rests on

From [`p7-year1-readings.csv`](../data/p7-year1-readings.csv), each recomputed.

| Reading | Computation | Use in the strategy |
|---|---|---|
| Sev1 and Sev2, baseline to quarter 3 | 30 to 14, −53 percent. Poisson 95 percent interval for 14: 7.7 to 23.5. Conditional on 44 incidents, 14 is 2.4 standard deviations below an even split ((14 − 22) ÷ √11) | The fall from baseline is real; quarter 2 to quarter 3 (17 to 14) is 0.5 standard deviations and cannot be told from noise |
| Availability gap, quarter 3 | 0.0011 × 131,040 = about 144 minutes against about 131 allowed; 13 minutes over | One INC-413-class payment outage (150 minutes) would exceed a whole quarter's allowance on its own |
| Credits | $60,000 × 4 = $240,000 a year against $1.64M at baseline | The cash case for prevention has mostly been collected; what remains is renewals and capacity |
| Unplanned work | 25 percent of 80 = 20 FTE, about $925,000 a quarter (20 × $46,250); baseline 27.2 FTE | 7.2 FTE recovered, about $1.33M a year of capacity, if the samples compare |
| Corrected orders | 7,800 ÷ 600,000 = 1.3 percent; errors 1.3 × 340 ÷ 400 = about 1.1 percent, about 6,630 orders per 28 days | Duplicates alone: 7,800 × 70 ÷ 400 = about 1,365 corrections per 28 days, from a missing idempotency key |
| Renewals at stake | 6 × $1.17M = about $7.0M ARR, 5 percent of $140M | All six renew while prevention is at 6 and then 5 FTE |
| Rolling target | At a true average of 9 a quarter, a year totals 40 or fewer about 78 percent of the time; at 10, about 54 percent; at 12, about 14 percent | The board counter's 40 is achievable only if the quarter 3 level improves further, not if it holds |

## 3. The strategy

**Scope and horizon.** All 24 components in [`components.csv`](../../case-studies/northstar/data/components.csv),
the four build systems, and the 87 engineering seats; quarters 5 to 8 (weeks 53 to 104). Planned at 79
engineers (the main organization proposal), with the effect of 80 and 78 shown.

### Diagnosis

| ID | Finding | Evidence | Consequence |
|---|---|---|---|
| D1 | The reliability gains are real and rest on capacity that is being withdrawn | 30 to 14 incidents; availability still 13 minutes short; prevention 12, 8, then 6 and 5 FTE; Core change failure rate flat at 22 and 23 percent and still linked by hand | Six top-40 renewals (about $7.0M ARR) fall in the quarters when prevention is lowest, and the board page promises 99.9 percent every quarter |
| D2 | Correctness is now the largest customer harm and the least measured | 8 of 14 baseline customer-detected incidents were correctness failures; 1.1 percent of orders wrong in quarter 3; no idempotency key; no confirmed invoice correctness data | A wrong financial record is a Sev1 under the week-3 definitions, and a top-40 distributor is already complaining; availability measures do not see it |
| D3 | Change still depends on a few people and old parts, and decisions about them do not get made | Four build systems; Core framework past free support; ledger currency and rounding with one safe changer at baseline; 4 of 10 critical roles with no cover; ADR-0001, the CI target, and tax-svc open for 33 weeks; core/permissions exemption lapsed in week 39 | One departure or one unpatchable vulnerability turns routine change into an incident, and year 2 adds a reorganization on top |

### Strategic choices

- **Excellent:** correctness and availability on the order-to-cash paths (order submission, pricing,
  invoicing, ledger, payments), and safe weekly change on those paths. This is where Northstar's contracts,
  credits, and renewals sit.
- **Adequate is enough, or bought:** the build and deploy tooling itself (one standard system, bought, no
  bespoke pipelines), internal reporting outside the money paths, and developer tooling beyond the 4.5 FTE
  platform line.
- **Waits for year 3:** Core boundary redesign (order-capture extraction, the rest of the core/customer
  redesign), decided at the week 104 gate as the continuation proposal already says.

**Against Victor's week 47 draft.** The choices follow his four groups: his "excellent" list (financial
correctness, availability of order and payment paths, accounting and bank integration, safe weekly change)
is the first bullet, with order submission and pricing added because the week-40 data puts ordering
correctness among the largest harms; his "buy" group holds the CI tooling; his "not doing" list matches the
will-not-do table below. His four policies map onto these three: reliability before reach is P1; money data
by contract or events, never tables, is a stricter form of P2; converge before adding is P3; staging above 10
FTE-quarters is already met by the continuation's two gates. **One departure:** his draft chooses the CI
target at the week 78 gate; this strategy recommends week 60. The stage 3 exit criterion (tier 1 through an
auditable pipeline with automated rollback by week 104) needs about 20 engineer-weeks in each of quarters 7
and 8 on the chosen system; a choice at week 78 leaves no lead time before quarter 7 starts in week 79, so
the criterion would in practice move to year 3. If Victor keeps week 78, the strategy says so and moves the
criterion openly (see Branches).

### Guiding policies

| ID | Policy | Answers | Cost | Owner, exceptions | Past decision it settles | Open decision it settles |
|---|---|---|---|---|---|---|
| P1 | **Reliability capacity is a line, not a favor.** Prevention is fixed for each stage (quarters 5 and 6, then 7 and 8) and changes only at a gate or when a written trigger fires. Any request to move it goes to the portfolio forum as a priced option | D1 | Greg Tanaka loses informal access to engineers; Amara Okafor cannot borrow prevention mid-stage | Engineering Director; exceptions by Victor Lindqvist within 5 working days | Engineering Excellence Day (week 27) took capacity outside the plan without the managers or Amara Okafor; under P1 it would have gone through the plan or not run | Greg Tanaka's week-47 private offer: no. His 4-plus-2 alternative is legitimate as a written option to the executive team |
| P2 | **A wrong financial record is an outage.** Any change that creates or alters an order, price, invoice, ledger entry, or payment ships with a check from a short published list (idempotency on submission, reconciliation, a contract test at the boundary, a migration rehearsal). Deal features on these paths are sized with the check included | D2 | Deal features on pricing and ordering take longer; "ship, then reconcile" is no longer allowed | Li Na Zhou (data, migration, and configuration standards); exceptions within 10 working days, recorded with expiry | The week-9 credit-note Sev1: the interim rule (no release with a ledger migration and code that depends on it) was this policy applied after the incident | ADR-0001: reading the ledger tables has no contract at the boundary, so it fails P2; the decision is between the export contract and posting events |
| P3 | **Converge and pair before adding, and decide on a clock.** No new runtime, datastore, or build system on a tier 1 component without retiring one; buy what changes for outside reasons; every tier 1 component and critical role has a second person by week 104; every cross-team technical decision has a named decider and a decision date within 10 working days of being opened | D3 | Pairing time comes from feature work; teams lose tool choice; decisions are made before everyone feels ready | Kwame Mensah; exceptions within 10 working days; deciders mapped by the director | ADR-0001, opened in week 14 with no decider, would have had one and a date by about week 16 | The CI target: decided by week 60 with a named decider. tax-svc: decided by week 60, with the hybrid option as the default under "buy what changes for outside reasons" |

The director owns one policy (P1), because capacity allocation is the director's decision with the CPO.
P2 and P3 are owned by staff engineers whose existing standards they extend (the
[first quarter](../../case-studies/northstar/first-quarter.md) page's standard owners), which is how
[Chapter 29](../../parts/06-technical-leadership/29-staff-and-principal-engineers.md) turns expertise into
owned decisions.

### Coherent actions by quarter

Capacity is in engineer-weeks; estimates are this solution's unless a source is named. Prevention buys 78
engineer-weeks a quarter at 6 FTE and 65 at 5 FTE.

| Quarter | Action | Kind | Policy | Owner | Due | Engineer-weeks |
|---|---|---|---|---|---|---|
| 5 | Publish the year-2 prevention line per stage; route all requests through the forum | Enforcement | P1 | Director | Week 53 | 0 |
| 5 | Idempotency key on order submission, if not already shipped in quarter 4 (about 4 in Chapter 44's sizing) | Transition | P2 | Priya Raman | Week 58 | 4 |
| 5 | Confirm whether a general invoice reconciliation job runs; if not, build it so the invoice correctness SLO has data | Transition | P2 | Marcus Oyelaran, steward Li Na Zhou | Week 60 | 12 |
| 5 | Publish the correctness check list; add it to the definition of done for the five money-path components | Enforcement | P2 | Li Na Zhou | Week 56 | 0 |
| 5 | Every component in the ownership register exactly once, including document-store | Enforcement | P3 | Director | Week 57 | in the transition cost |
| 5 | Map deciders and dates for ADR-0001, the CI target, and tax-svc; decide all three | Escalation | P3 | Director, Victor Lindqvist for ADR-0001 | Week 60 | 0 |
| 5 | Last tier 1 minimums (14 of 14 on the current list) | Transition | P3 | Kwame Mensah | Week 78 | 10 |
| 5 to 6 | Second responders for ledger period close and currency and rounding (TR-07) | Transition | P3 | Marcus Oyelaran | Week 78 | 13 a quarter |
| 5 | Scope the Core framework migration (TR-01); add a mobile-path synthetic check | Transition | P3, P2 | Ines Carvalho; Kwame Mensah | Week 65 | 4 + 1 |
| 6 to 7 | Core framework migration, base case 150 engineer-days (canon range 120 to 180) | Transition | P3 | Ines Carvalho | Week 91 | 15 a quarter |
| 6 | Correctness checks on the pricing path (price change between draft and submit) | Transition | P2 | Priya Raman | Week 78 | 10 |
| 6 | Stage 2 gate | Escalation | P1 | Victor Lindqvist | Week 78 | 0 |
| 7 to 8 | Tier 1 deployed through an auditable pipeline with automated rollback, on the chosen CI target | Transition | P3 | Tom Becker | Week 104 | 20 a quarter |
| 8 | Stage 3 gate; year-3 boundary decision | Escalation | P1, P3 | Victor Lindqvist | Week 104 | 0 |

The rest of each quarter's prevention goes to corrective actions from incident reviews: 34 engineer-weeks
in quarter 5 (78 − 4 − 12 − 10 − 13 − 4 − 1), 40 in quarter 6 (78 − 13 − 15 − 10), and 30 in quarters 7
and 8 (65 − 15 − 20 in quarter 7; quarter 8 also holds 15 for gate evidence and rehearsals). Expect the
named items to grow; the corrective-action line is the buffer.

### Capacity envelope at 79 engineers

Unplanned work is planned at quarter 3's planned 22 percent (the same 17.4 FTE as Victor's draft) and the
cautious case at quarter 3's measured 25 percent. The platform line stays at 4.5 FTE (an assumption; the canon fixes it only for quarter 3). The
organization transition costs about 21 engineer-weeks, 1.6 FTE-quarters, placed in quarter 5.

| Quarter | Unplanned, planned (cautious) | Prevention | Platform | Transition | Product, planned (cautious) |
|---|---|---|---|---|---|
| 5 | 17.4 (19.75) | 6 | 4.5 | 1.6 | 49.5 (47.1) |
| 6 | 17.4 (19.75) | 6 | 4.5 | 0 | 51.1 (48.75) |
| 7 | 17.4 (19.75) | 5 | 4.5 | 0 | 52.1 (49.75) |
| 8 | 17.4 (19.75) | 5 | 4.5 | 0 | 52.1 (49.75) |

Check, quarter 5: 17.38 + 6 + 4.5 + 1.62 + 49.5 = 79.0; cautious 19.75 + 6 + 4.5 + 1.62 + 47.13 = 79.0.
Commitments are made from the cautious column, which in every quarter is above quarter 3's cautious
product capacity of 45.1. Prevention for the year is 22 FTE-quarters, about $1,017,500 of capacity (22 ×
$46,250).

**Against Victor's draft allocation.** His year-2 line on 79 engineers is unplanned 17.4, prevention 5.5,
platform 4.5, estate currency 2.0, and product 49.6 (37.6 for today's customers, 10.0 horizon 2, 2.0
horizon 3). This envelope averages prevention 5.5 ((6 + 6 + 5 + 5) ÷ 4), and its average product plus
transition, 51.2 + 0.4 = 51.6, equals his product plus estate currency, 49.6 + 2.0. The difference is where
TR-01 sits: this strategy pays it from prevention in quarters 6 and 7, his draft from the estate-currency
line. Under his split, about 1 FTE of prevention is freed in those quarters for corrective actions.

**Other seat counts.** At 80 engineers (alternative B) each quarter gains about 0.8 FTE of product after
the unplanned share (planned 50.3 in quarter 5 if B's transition cost equalled the main proposal's; the
canon does not cost B's transition). At 78 (a VP takes a seat) each quarter loses about 0.8 (quarter 5
planned 48.7). The
strategy holds at all three; only product capacity moves.

**The 4-plus-2 option.** Prevention falls to 4 FTE (52 engineer-weeks) in quarters 5 and 6, and two
engineers (about $185,000 of capacity) go to deal features through the forum. The strategy keeps the
idempotency key, the reconciliation job, the tier 1 minimums, and the ledger second responders, and
moves the Core framework migration to quarters 7 and 8, pushing the auditable-pipeline work past week
104. The stage 2 exit criteria are unchanged; stage 3's pipeline criterion moves to year 3. This is the
trade the executive team is choosing between, written in its own terms.

### What we will not do

| Option | Who wants it | Reason |
|---|---|---|
| Move prevention engineers to deal features outside the portfolio forum | Greg Tanaka (week 47) | P1; the same trade is available inside the forum as a priced option |
| A quarterly "below 10" headline | Victor Lindqvist (week 41) | At a true average of 9 it is missed about two quarters in five by chance, which pushes on the severity rating; the rolling 40 measures the same ambition |
| Extract order-capture, or fund the rest of the core/customer redesign, before week 104 | Rafael Duarte; Ines Carvalho | D3 says pair and converge first; boundary work is the year-3 option at the week 104 gate |
| Rewrite Core | Nobody openly; it returns in every incident review | Constraint 3; the diagnosis points at change safety and correctness, not the codebase |
| Add a build system or runtime on tier 1 for a new feature | Any team under deadline | P3 |

### Branches

| Open decision | Outcome | What changes in the strategy |
|---|---|---|
| Year-2 organization (week 46) | Main proposal | As written; Mobile owns the mobile-path synthetic check and its on-call |
| | B | Customer Experience keeps both subteams; the mobile check's owner is Daniel Cho; product capacity +0.8 FTE |
| | C or D | 78 or 77 engineers; product falls by 0.8 or 1.6 FTE a quarter; P3's second-person rule is easier with a second management layer (D) |
| VP (recommendation week 48) | VP hired | 78 engineers; the VP becomes the sponsor and P1's owner; the strategy is re-read in the VP's first month (a review trigger) |
| | No VP | As written |
| Continuation (decisions by week 51) | 6 FTE, $150,000 approved | As written |
| | 4 FTE plus 2 | As in "The 4-plus-2 option" above |
| | $150,000 declined | No tooling purchase is assumed by any action above; the stage 3 pipeline work then depends on the $100,000 tied to the CI target, which becomes the binding decision |
| CI target | Chosen by week 60 (this strategy) | Quarters 7 and 8 as written |
| | Chosen at the week 78 gate (Victor's draft) | The pipeline work starts late in quarter 7; the stage 3 pipeline criterion moves to year 3, recorded as a re-scope, not a miss |
| | Not chosen | P3 forbids new pipeline work beyond the existing systems; the stage 3 pipeline criterion is reported as missed, not redefined |
| ADR-0001 | Export contract or posting events | Either satisfies P2; the choice is the decider's |
| | Read the tables | Ruled out by Victor's draft policy (contract or events, never tables); under P2 alone it could only be an exception with an expiry |
| Board envelope (week 50) | As planned | As written |
| | Smaller | Product capacity takes the cut first; P1 keeps prevention unless Victor records an exception |

### Scorecard and review triggers

| Measure | Direction or target | Pair | Why it is here |
|---|---|---|---|
| Sev1 and Sev2, rolling four-quarter total | At or below 40 over year 2 (the board counter) | Severity audit result; customer-detected share | Same number as the board page |
| Availability, contractual paths, per quarter | 99.9 percent, set by contract | SLO budget consumed, order and payment journeys | Mandatory stage 2 criterion |
| Corrected-order error rate (Data and Analytics definition, sampled each quarter) | Down from about 1.1 percent | Orders per distributor; order latency SLO | D2's outcome; guards against fewer corrections from fewer orders |
| Unplanned work share | Within the 25 percent cautious band; toward 18 percent by week 104 | Prevention spent against plan | D1 and the stage 3 criterion |
| Tier 1 at the minimums, then through an auditable pipeline | 14 of 14 by week 78; all tier 1 by week 104 | Change failure rate by component | D3 and stages 2 and 3 |
| Critical roles with no cover | 0 of 10 by week 78 | Share of after-hours pages carried by the top three responders | D3 |
| Open technical decisions past their decision date | 0 | Decisions reversed within two quarters | P3; the lesson of week 14 |

**Review triggers.** Two consecutive quarters above 12 Sev1 and Sev2 (the counter's trigger; at a true
average of 10 this fires about 4 percent of the time in a given pair of quarters, at 12 about 18 percent);
any stage 2 quarter below 99.9 percent; a corrected-order error rate in quarter 6 no lower than the week-40
reading; a top-40 renewal flagged at risk for reliability or correctness by Sofia Alvarez; any change in
the seat count (a VP, or the flat-headcount constraint lifted); a board envelope below the plan; any
register item at score 9 with no funded response.

## 4. Coherence check

| Test | Result |
|---|---|
| Every policy answers a finding | P1 to D1, P2 to D2, P3 to D3 |
| Every finding has a policy | Yes, one each |
| Every action traces to a policy | Yes (table above); the corrective-action buffer serves P1 |
| Capacity sums to the seats | 79.0 in every quarter, both cases |
| Every "will not do" disappoints someone named | Greg Tanaka, Victor Lindqvist, Rafael Duarte, Ines Carvalho |
| Every policy would have settled a year-1 decision | Engineering Excellence Day, the week-9 Sev1, ADR-0001 |
| Fits the board counter | Same measures and trigger; adds correctness, which the counter lacks |

## 5. Workshop order and the summary for Victor

The order follows who the policies constrain most: the three staff engineers as co-authors (week 46);
Marcus Oyelaran, Priya Raman, and Elena Sokolova, whose teams carry P2 (week 47); Amara Okafor, because P1
fixes the allocation she asked to have fixed, and Greg Tanaka, because P1 closes the route he offered, in
person before he reads it (week 47); Rajiv Menon, to confirm no new cash is assumed (week 48); Victor
Lindqvist with the summary (end of week 48), before the executive team meets in week 49.

> **Year-2 engineering strategy: summary for Victor Lindqvist (draft, week 48)**
>
> Year 1 more than halved serious incidents (30 to 14 a quarter) and missed 99.9 percent by about 13
> minutes in quarter 3. Year 2 is harder for three reasons: the gains rest on prevention capacity that
> falls from 8 to 6 and then 5 FTE while six of our 40 largest customers renew; customers now feel wrong
> orders more than outages (1.1 percent of orders in quarter 3), which nothing on the board page measures;
> and change still depends on a few people and old parts, with three technical decisions open since week
> 14.
>
> Three policies: prevention is a fixed line per stage, moved only at a gate or a trigger; a wrong
> financial record is treated as an outage; converge and pair before adding, and every technical decision
> gets a decider and a date. Excellent at correctness and availability on the money paths; adequate on
> tooling; Core boundary work waits for year 3.
>
> It needs no headcount and no new cash, holds under each year-2 organization option and with or without a
> VP, sits under your week 47 draft, and uses the board page's measures plus one for corrected orders.
> Decisions I need from you: ADR-0001 by week 60, as your draft proposes; tax-svc by week 60; and the CI
> target by week 60 rather than at the week 78 gate, because otherwise the stage 3 pipeline criterion moves
> to year 3.

## 6. Other defensible answers

- **Two policies.** Folding P3's decision clock into the operating system instead of a policy is
  defensible if the decision log already enforces dates; the draft above keeps it as policy because week
  14 showed that it does not.
- **Correctness as the headline.** A strategy that leads with D2 and treats availability as a floor is
  defensible given the week-40 data, provided it keeps 99.9 percent as a contractual target.
- **Planning on 4-plus-2.** Recommending Greg Tanaka's option is defensible if the submission prices it, lists
  the criteria that move to stage 3, and keeps P1 (the trade goes through the forum).
- **Planning at 78 seats.** Assuming a VP is defensible if the branch for "no VP" is shown.

## What a weak submission looks like

> "Vision: world-class engineering. Goals for year 2: zero Sev1 incidents, 99.99 percent availability,
> double deployment frequency, migrate to microservices, adopt AI tools, improve morale. Principles: quality
> first, move fast, own your code. The director will drive all initiatives. Headcount: we will ask the
> board for 10 more engineers to deliver this."

Against the rubric: goals instead of a diagnosis, and no numbers from the canon (diagnosis weak); policies
that cost nothing and decide nothing, all owned by the director (choices and policies weak); no dated
actions or enforcement (actions weak); a headcount request that breaks a binding constraint and no
envelope (capacity weak); open decisions ignored (uncertainty weak); targets that invite gaming, with no
pairs and no correctness measure (measurement weak); no evaluation of week 14 (evaluation weak). It fails
acceptance criteria 1 to 9.

**An adequate submission** rewrites the week-14 diagnosis with quarter 3 numbers, keeps its three policies,
adds a capacity table at 80 engineers, and lists the board counter's measures. It scores in the 60s. **What
separates excellent from adequate** is noticing why week 14 decided nothing and fixing that, seeing
correctness in the week-40 data, and writing the branches so that the strategy survives whatever Victor and
the executive team decide in weeks 46 to 51.

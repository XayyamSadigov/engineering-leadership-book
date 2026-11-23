# Chapter 31 solutions — Service Boundaries: Microservices, Modular Monoliths, and Ownership

Worked solutions for the [chapter 31 exercises](../parts/06-technical-leadership/31-service-boundaries-and-ownership.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Two definitions of coupling

**Recomputation.** Average-based coupling is co-changes divided by the mean of the two modules'
change counts.

| Pair | Co-changes | Mean of counts | Average-based | Chapter's share (smaller module) |
|---|---|---|---|---|
| customer and permissions | 22 | (33 + 38) / 2 = 35.5 | 62% | 67% |
| order-capture and invoicing | 38 | (250 + 230) / 2 = 240 | 16% | 17% |
| ledger and order-capture | 5 | (170 + 250) / 2 = 210 | 2% | 3% |

These three keep their order under both definitions, but other pairs do not. scheduler and invoicing
falls from 60 percent (27 of 45) to about 20 percent (27 of 137.5), below invoicing and ledger (70 of
200 = 35 percent). The definitions answer different questions. The smaller-module share asks how
dependent the smaller module is on its partner, which is the question for "should this small module
live with, or be owned by, the team that owns its partner?" The average penalizes asymmetric pairs
and asks whether the two modules form one unit overall, which suits "should these two be merged?"

**What neither shows.** The incidents between Orders and Billing (INC-417, INC-427, and the week 9
Sev1) travel through shared tables and runtime behavior; ledger and order-capture changed together
only 5 times. A good answer says co-change is one input and pairs it with incident data and the data
model. The weak answer picks one definition as "correct" or reads 3 percent as "no coupling."

## F2 — Rewriting the Prime Video slide

**A rewrite.** "In 2023 a Prime Video team reported moving one service, a monitor for the audio and
video quality of live streams, from serverless components (Step Functions, Lambda, frames passed
through S3) into a single process on containers. The first design hit a scaling limit at about 5
percent of expected load; after the move the team reported infrastructure costs down by over 90
percent. The authors conclude the choice has to be made case by case."

**Evidence for:** a network or orchestration boundary inside a high-volume, data-heavy loop can
dominate cost and limit scale; folding components back into one process can be the right move; the
components can stay the same while the deployment boundary changes. **Not evidence for:** Amazon or
Prime Video abandoning microservices, monoliths being cheaper in general, or any result beyond one
service. It is one self-reported account with no published cost method.

**Relevance to Northstar.** Mostly indirect. Core is already a monolith, so the case says nothing
about whether to split it. It is relevant to any future extraction whose calls would be chatty, and
as a reminder to check whether any of the fourteen services exchange data in tight loops. The weak
answer swaps one slogan for the other ("monoliths are back").

## F3 — The ownership test on six components

The test has four parts: the owner carries the pager, reviews changes, holds the runbook, and keeps
dependencies current. From `components.csv` and the case study:

| Component | Owner now | Fails on available data | Information still needed |
|---|---|---|---|
| core/customer | Orders (week 4) | At baseline: no runbook, no alerts, no on-call | Whether Orders added it to its rotation and wrote a runbook in quarter 1; who reviews other teams' changes (18 of 33 came from three other teams) |
| core/scheduler | Billing (week 4) | Same baseline gaps | Same; also whether Data and Analytics' occasional changes reach a Billing reviewer |
| notification-svc | Orders from quarter 2 | No runbook, no alerts, no on-call; most commits from Orders and Billing | Handover date, who in Orders reviews Billing's changes, dependency state |
| export-svc | Data and Analytics | No runbook, no alerts, no on-call; deployed by a shell script only one Platform Operations engineer understands, so the owner cannot ship its own fixes | Whether tier 3 justifies leaving it off on-call (a defensible yes), and a date to move it off the script |
| search-svc | Disputed (nominal Orders) | No on-call, no runbook; authors in another team | Who changed it last quarter, who is paged today |
| document-store | None | Fails every part | Callers, traffic, vulnerability status, who can deploy it |

A good answer separates "fails" from "unknown" and does not assume the day 90 results (8 of 15 tier 1
components meeting the four minimums) apply to these specific components; the case does not say
which eight. It also notes that tier matters: export-svc at tier 3 may reasonably have no on-call,
but no component should be undeployable by its owner. The weak answer marks every component with a
listed owner as passing.

## A1 — Platform Operations' permissions service

**Evaluation against the decision path.** Different change reason? Partly: permissions logic changes
with the rules of who may do what, and Tom Becker's argument that it belongs with identity is a real
design argument. Low co-change? No. customer and permissions changed together in 22 of customer's 33
changes (67 percent), and permissions also changed together with order-capture 11 times in the baseline quarter (11 of permissions' 38 changes). The path stops at "move boundary
first", which is exactly the funded permissions extraction inside Core. One owning team? No, the
ownership decision is open. The path stops there too.

**What a service would do now.** Every one of those co-changes would become a coordinated change
across a network boundary, made mostly by teams who do not own the service (Platform Operations made
none of the 38 changes). Permission checks also sit in the request path of tier 1 flows, so a new
service adds a runtime dependency on the order and payment paths.

**What to ask Tom to bring back:** the list of callers and call volumes, the latency and availability
budget for a remote check, who would make the changes (with names from Orders and Customer
Experience), and the result of the in-Core extraction at the end of quarter 2. **Effect on ownership.**
The analysis shows that any owner of permissions needs Core review capacity and a working relation
with Orders; it does not decide between Orders and Platform Operations, which is Chapter 13's
decision. The weak answer rejects the proposal as "fashion" without engaging with the identity
argument, or accepts it because Platform Operations would finally own something.

## A2 — The orphaned document-store

**Options.** (1) Assign to Billing, whose invoice-render is a main caller. (2) Assign to Orders,
the other caller. (3) Merge it into invoice-render and give order attachments another home. (4) Retire
it by moving storage to a managed object store run under the platform, with Platform Operations as
owner of the platform service. (5) Keep it in the director's office as interim owner, with an
incident lead, until a set date.

**One defensible choice.** Interim ownership now (option 5, with a named incident lead and a deadline
in week 20), then assign to Billing from week 20, after the accounting integration ships, on two
conditions: Platform Operations moves its deployment off the shared shell script first, and the open
critical vulnerability is closed or under a recorded exception before handover. Billing's on-call
load is the real objection; the transfer should come with a check that document-store adds few pages.
Option 4 is a strong alternative if a managed store is cheap and the platform team has capacity.

**The message** names the decision, the date, the conditions, and the reason (the main caller should
own the component that fails with it), acknowledges Marcus Oyelaran's load with the deferral, and
thanks Priya Raman without making her the arbiter. **Transition cost:** a few engineer-weeks of
Platform Operations time for the pipeline move, a runbook, and alerts. The weak answer assigns it to
whoever objects least, or leaves it orphaned "until after the renewals" without an interim owner.

## A3 — Extracting order-capture

**Against the framework.** Change pattern: order-capture changes with pricing-rules in 58 of 110
pricing-rules changes and with catalog in 15, so a service of order-capture alone would split Orders'
own cluster; at minimum the three Orders modules would go together. Cross-team co-changes would then
cross a network: invoicing 38, customer 12 (now Orders-owned, so it could move too), permissions 11,
scheduler 8. Excluding customer, that is about 57 a quarter, about four a week, each needing a
compatible interface change and coordinated releases with Billing. Data: Core's modules share one
schema, so the extraction needs a data split first, the costliest step. Release constraint: Core now
releases weekly and change failure fell from 31 to 22 percent, which weakens the strongest motive.

**What to tell Rafael.** Not in quarter 3, with reasons. Bulk ordering's asynchronous processing of
order files up to 20,000 lines may have a genuinely different runtime profile; that piece, not
order-capture as a whole, is the better candidate to watch. **Evidence that would change the answer:**
a breakdown of Orders' lead time showing the weekly train still dominates, a runtime need (scaling or
isolation) that Core cannot meet, and a falling cross-team co-change rate on the seam after contract
tests. A strong answer turns the proposal into a measurement plan with a revisit date. The weak
answer either approves it to motivate a strong senior engineer or rejects it without numbers.

## X1 — The board question

**One page for Victor Lindqvist.**

*Position.* Northstar runs a modular monolith (Core, eight modules) and fourteen services extracted
for specific reasons. We extract or consolidate component by component, when change patterns, team
ownership, runtime needs, and our platform justify it. We are not "moving to microservices" and not
"going back to the monolith."

*Evidence.* Neither style has controlled outcome evidence across companies; studies of migrations
report maintainability and scalability as motives and finding service boundaries as a major
difficulty. The Prime Video case is one service that cut costs by removing a data-heavy network
boundary; it supports case-by-case decisions, which is our approach.

*Our data.* Core's change history shows most coupling inside modules owned by one team; the main
cross-team seam is about three shared changes a week, which we are addressing with contracts, not a
split. Three components still lack a settled owner; that is the larger risk.

*Cost.* Each service carries a recurring operations cost (assume a tenth of an engineer, about $18,500
a year, plus cloud); folding services into Core would save little and re-couple their release
schedules to Core's.

*What would change it.* A component with a distinct runtime need, low coupling, one owner, and a
platform that can run it.

A good answer is short, honest about evidence, and uses Northstar's numbers. The weak answer argues
for one style to satisfy whichever board member is louder.

## X2 — Deciding the boundary proposal

**One defensible decision: adopt with three modifications.**

1. **Sequencing.** The build-enforced module rules start in week 20, after the accounting integration
   ships, meeting Marcus Oyelaran's concern; in weeks 14 to 19 Ines Carvalho runs them in report-only
   mode to measure violations.
2. **The Orders and Billing seam.** The contract on order-capture and invoicing is combined with the
   ledger-export contract Li Na Zhou already proposed for quarter 2, so Billing builds one contract
   discipline, not two.
3. **Deadlines.** search-svc and document-store have owners by the end of quarter 2 (week 26); the
   core/permissions decision follows Chapter 13 and must close before its exemption lapses, before the end of quarter 3.

**Rafael Duarte** gets a written answer: no extraction in quarter 2 or 3, a lead-time breakdown for
Orders, and a named revisit (below). **Revisit triggers:** customer and permissions coupling above 40
percent at the end of quarter 2 (the extraction did not work); Orders' lead time dominated by waiting
for the train; any module showing a runtime need Core cannot meet. **Report to Victor Lindqvist:**
components without a settled owner (three at the start of the quarter), module-rule violations
trend, coupling after the permissions extraction, and whether any extraction case has met the
criteria.

Defensible alternatives: rejecting module enforcement during both renewals, or approving a scoped
spike on bulk-order processing. The weak answer adopts the proposal without dates, or lets "no
extraction" become "no decision" on the three ownership gaps.

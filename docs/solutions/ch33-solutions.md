# Chapter 33 solutions — Conway's Law, Team Topologies, and Cognitive Load

Worked solutions for the [chapter 33 exercises](../parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Classifying Northstar's teams

**A worked classification.**

| Team | Label | Supporting fact | Contradicting fact |
|---|---|---|---|
| Orders | Stream-aligned | Owns the order-capture journey end to end in Core | Six domains, including search and notifications that are not ordering |
| Billing | Stream-aligned | Invoice to ledger is one flow of value | Ledger knowledge sits with three experts, like a complicated subsystem inside the team |
| Payments and Integrations | Stream-aligned | Owns payments end to end, deploys 22 times a month | Customer integrations (erp-sync, webhooks) are a second stream |
| Customer Experience | Channel team | Owns web, mobile, and mobile-bff | Most of its changes need Orders (8 dependency links) |
| Data and Analytics | Mixed | Owns customer reporting and exports | 12 points of capacity go to other teams' requests |
| Platform Operations | Platform | Owns CI/CD and infrastructure | 46 percent unplanned, 29 of 86 links received: a request queue |
| Staff engineers | Enabling | Kwame Mensah's release working group facilitated flaky-test ownership | Ines Carvalho's unscheduled questions are a dependency; they also govern standards |

**The costliest mismatch.** A strong case is Platform Operations: every team's lead time passes through
it, and its interrupt load blocks the capabilities that would remove the interrupts. A defensible
alternative is Orders' scope, because it sits on a tier 1 path and a renewal commitment. What would
prove you wrong: if the week 18 re-sample showed requests falling fast without any capability work, the
queue was the problem, not the team type.

**Weak answer:** a label per team with no contradicting fact. The exercise is about where labels lie.

## F2 — notification-svc and congruence

**Explanation.** Conway's observation predicts that a component is designed by the communication of
the people who change it. notification-svc was changed mostly by Orders and Billing and owned by
Customer Experience, which ran it with no runbook, no alerts, and no on-call. In congruence terms, the
technical dependency (Orders' and Billing's code depends on templates and variables in the service)
created a coordination requirement between the committers and the operators that no channel met. A
renamed variable is exactly the change that crosses that gap unnoticed, and customers detected INC-412.

**What the move to Orders fixes.** The main committer becomes the operator, so changes and their
consequences meet in one team's review and on-call. Orders can add alerts on blank renders.

**What it does not fix.** Billing still commits to it, so the Orders–Billing gap moves inside the
service rather than disappearing. A strong answer proposes an interface (template contracts, a test
that renders every template with each caller's variables) or a defined interaction mode with Billing,
and notes that the move adds a domain to Orders' load, with nobody who has operated the service.

**Weak answer:** "ownership is now clear, so the problem is solved."

## F3 — The team-size argument

**What the cited research is about.** Numbers attributed to Dunbar come from research on the size of
social groups, not software teams. Applying a threshold from that research to an engineering team is a
transfer the chapter declines to make, and a hard limit of 15 has no software-specific evidence behind
it that this book could verify.

**The arithmetic.** Communication pairs grow as *n*(*n*−1)/2: 8 people have 28, 15 have 105, 16 have
120. The step from 15 to 16 adds 15 pairs; the step from 8 to 15 adds 77. If the argument were really
about communication cost, Billing at 15 would be nearly as overloaded as Orders at 16. The
threshold draws a line where none exists.

**What to use instead.** Two tests from the chapter: can everyone review and be on call for the whole
scope, and is the stand-up coordination rather than status? Billing fails the first at 15 (ledger on-call
rests on three experts); Orders fails it at 16 because of six domains. The limit passes a team the real
test fails. Also separate team
from reporting group: 16 reports is a span question (Chapter 34).

**Weak answer:** accepting or rejecting the 15 with no reasoning about scope.

## A1 — Billing's cognitive load

**Inventory.** Five components: core/invoicing (tier 1, 4 baseline Sev1 and Sev2 incidents),
core/ledger (tier 1, 3), tax-svc (tier 1, 1), invoice-render (tier 2, 0), and core/scheduler (tier 2,
since week 4). The 8 incidents match Billing's baseline count. Billing is 13 engineers and two quality
engineers, with 41 percent unplanned work at baseline and weeks 1 to 3 of quarter 2 reserved for the
ledger export.

**Load by kind.** Intrinsic load is concentrated rather than broad: the ledger knowledge map shows
period close with 2 responders and 1 engineer able to change it safely, currency and rounding with 1
and 1. The 180 pages, 126 handled first by three ledger engineers, show that the concentrated knowledge
also concentrates operational load. Extraneous load came from release-train failures and migrations,
now falling. Germane load is unfunded: Tamsin Achterberg can respond alone only on credit notes.

**Top risk.** Period close and currency, one person deep, on tier 1 financial records.

**One move.** Not a new team type: a time-boxed spreading effort (Chapter 12) for period close and
currency, pairing the backfill and one other engineer with the experts, funded from prevention, with
an exit criterion of three engineers able to change each area safely. Transition cost: slower ledger
work for a quarter. A complicated-subsystem ledger team is defensible later; now it would create an
interface on every billing change.

**Weak answer:** moving core/scheduler away without addressing the ledger.

## A2 — Platform Operations as a platform

**Interaction modes.** X-as-a-service with all product teams for environments and pipelines, through
one intake; collaboration with a time limit with whichever team pilots each new capability (for
example Payments and Integrations, the most disciplined, for pipeline templates); facilitation from
Kwame Mensah's working group where teams adopt a new practice. Ad hoc requests outside the intake
should be visibly exceptions.

**First two capabilities.** Self-service test environments (already started; finish and measure the
wait) and a standard pipeline with automated rollback for the four script-deployed services, since
shell-script deploys understood by one person are the riskiest extraneous load. A strong answer ties
each to demand data from the dependency matrix (Chapter 16) rather than to what the platform team
would most like to build.

**auth-svc.** It is a tier 1 product service, not a platform capability. Either keep it under a written
exemption with an end date while a product team is chosen, or treat it as a complicated subsystem with a
named owner and an interface. Leaving it as background work for five infrastructure engineers on an
interrupt rotation is the weakest option.

**What to measure.** Requests from other teams (20 to 14 points by week 18, aim lower), environment
wait, and how many capabilities are used without a ticket.

**Weak answer:** "rename it Platform and add a product manager," with no capability list.

## A3 — Ines Carvalho as enabling

**Engagement 1: permissions extraction with Orders.** Team: Orders, which owns core/customer.
Capability: Orders engineers able to change and review core/customer and the extracted permissions
code. Exit criterion: by an agreed week, two more Orders engineers can change core/customer safely (the
knowledge count rises from 2 to at least 4) and Orders reviews its own core/customer changes. She leads
the design; Orders engineers do much of the code with her.

**Engagement 2: Core review practice.** Her unscheduled questions (about eight hours a week) become a
scheduled office hour plus written design notes on recurring questions, with the goal of reducing the
questions, not answering them faster. The baseline fact that two Orders engineers stopped proposing
designs after unexplained rejections matters: facilitation means explaining, not ruling.

**Week 20 check.** Count unscheduled questions (falling?), Orders' knowledge count for core/customer,
and whether Orders engineers are proposing designs again. If questions have not fallen, the office hour
became a queue.

**Defensible alternatives.** Some would keep her on the extraction alone and route Core questions to
Rafael Duarte and Aisha Bello, the Orders senior engineers who already own order-capture reviews.

**Weak answer:** calling her work "enabling" with no team, no capability, and no exit.

## X1 — Orders' structure

**One worked recommendation.** Do D at once (no core/permissions before week 26). Decide B now but
execute it at the next structural review, the year-2 proposal, once Data and Analytics' charter accepts
search-svc; quarter 2 changes one boundary only, the order-to-invoice contract, and moves no people.
Reconsider C at the same review, after bulk ordering ships, with the data.

**Sequencing and costs.** B moves a component nobody in Orders can change (knowledge count 0) to the
team that holds its authors. Cost: a handover of perhaps two to three engineer-weeks across both teams,
an on-call rotation set up in Data and Analytics, and added load on a team already carrying 12 points
of requests, which the charter must accept explicitly. It touches nothing on the bulk-ordering path.
C before week 26 would disrupt the five engineers on bulk ordering; after week 26 it is a real option.
Under flat headcount, a second manager means an engineer's seat not backfilled, about 13 engineer-weeks
a quarter, roughly two fifths of the 33.3 the assessment left for non-commitment work. That price has to buy
a lasting reduction in load.

**Measures.** Knowledge counts per component, Orders' unplanned share, Sev1 and Sev2 incidents in
Orders' components, and whether core/customer gets the tier 1 minimums.

**Alternatives.** A defensible answer recommends C directly after week 26, arguing that six domains
and 16 reports will not shrink otherwise. Another keeps search-svc in Orders and funds learning (A).
Either must show the arithmetic and the transition cost. Linking C to Rafael Duarte's career question is
reasonable only as a consideration; the structure must be justified by the work.

**Weak answer:** a split justified by headcount or by giving someone a manager role.

## X2 — The reverse Conway proposal

**Assessment.** The forward direction is supported: MacCormack and colleagues found different
organizational forms produced differently modular products, and congruence research shows coordination
matching dependencies speeds work. The reverse maneuver as Victor states it is not supported for an
existing system: no evidence read for this chapter shows a reorganization breaking apart an existing
monolith on its own. With no Core rewrite funded, four value-stream teams would all still change
customer, permissions, and the release train. Colfer and Baldwin's point about partial mirroring
suggests the better aim is knowledge boundaries wider than ownership boundaries, not a cleaner chart.

**Cost.** All six teams' boundaries change at once: on-call handovers for many of the 24 components, lost context,
a throughput dip during quarter 3, renegotiated relationships, and probably attrition risk. Chapter 36
covers this cost.

**Instead, or first.** Fund the code work that makes the target cheaper (the permissions extraction is
the pilot), use co-change data to find which modules actually cluster by stream, move single components
where congruence is clearly broken (search-svc, notification-svc), and reconsider team boundaries when
a module has a clean interface. Leave Customer Experience's structure to Chapter 14's recheck.

**Weak answer:** accepting the proposal because "Conway's law says so," or rejecting it without
offering a path to the architecture Victor wants.

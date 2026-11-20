# Chapter 16 solutions — Flow: Lead Time, Dependencies, and Unplanned Work

Worked solutions for the [chapter 16 exercises](../parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Applying Little's law

**Estimate.** Average lead time = work in progress ÷ throughput = 30 ÷ 6 = 5 weeks. The manager's
"about two weeks" is not wrong about what it measures; it measures something else.

**The discrepancy.** "Two weeks in development" is time in one stage. Little's law, applied to the
whole system, counts every item started and not delivered: the 9 blocked items, items waiting for
review, items waiting for a release. If roughly 2 of the 5 weeks are development, about 3 weeks are
waiting. The blocked items alone are 30 percent of work in progress.

**What to verify first.** (1) That the 30 is a true count of everything started and not delivered,
not only the "in progress" column. (2) That throughput of 6 a week is a stable average over several
weeks, not one good week. (3) That the team is roughly in a steady state: if work in progress has
been rising, the law applied to a short window will understate lead time for items started now.
(4) That you are comparing like with like: the law gives a mean; if the manager quotes a median, a
few very old items can open a gap.

**A good answer** separates stage time from system time and names the blocked items as the lever.
**The weak answer** declares the manager wrong without checking how work in progress was counted.

## F2 — The regression pass is not the main lever

**The arithmetic.** In the standing-orders map, regression is 3 days of work inside a lead time of 76.
Cutting it to 1 day saves 2 days, about 3 percent. It might also reduce the chance of missing a train
(part of the 9-day wait), so a generous estimate is 3 to 5 days.

**Comparisons.** Planning the Billing change in the same cycle as Orders would turn a 14-day wait into
2 or 3 days, saving about 11. A self-service test environment saves about 5. A weekly train saves
about 4 or 5. Each is larger than the regression change alone, and the first is larger than all the
release-related changes together.

**What the colleague gets right.** A three-day manual pass is costly and Chapter 23 shows it is the
precondition for a weekly train, so shortening it matters for the release path. It also costs QA
capacity, not only calendar time.

**What they get wrong.** "Pure waste" confuses work time with wait time. The map shows that waits, not
work, are 53 of the 76 days, and that the largest waits are queues at other teams. Optimizing a work
step barely moves lead time.

**A good answer** uses the wait breakdown and compares at least two alternatives quantitatively.
**The weak answer** accepts or rejects the proposal without numbers.

## F3 — Classifying unplanned work

| Item | Category | Countermeasure owner |
|---|---|---|
| Hotfix after a Core release | Failure recovery | Owning team, through the quality program (Chapter 27) |
| Customer Experience asks for a new order API field | Request from another team | Orders manager; long term, the dependency review (contract or ownership) |
| Broken shared test database | Toolchain and environment | Platform Operations, or whoever owns the test infrastructure |
| Sales director wants a demo environment tomorrow | Expedited business request | Whoever owns the expedite policy (director or CTO), and Platform Operations for self-service |
| Customer-reported invoice error | Failure recovery | Billing |
| Pipeline change after a build tool upgrade | Toolchain and environment, if the upgrade was forced; planned work if scheduled | Platform Operations |

Two items deserve comment. The API field request may be legitimate planned work for Customer
Experience but is unplanned for Orders: classification is from the receiving team's point of view.
The pipeline change shows that a category depends on whether the work was known when the team
planned; a scheduled upgrade is planned work.

**A good answer** classifies from the receiver's viewpoint, distinguishes owners of the work from
owners of the countermeasure, and notes the ambiguous cases. **The weak answer** labels everything
"bug" or "support".

## A1 — The interrupt sink that cannot invest

**What to learn first.** Which request types dominate Platform Operations' 20 points of requests from
other teams, how long each takes, who sends them, and which planned projects are slipping. Ask Tom
what he has already tried and what he believes would help; he may have a better idea than
self-service environments.

**Data to bring.** The dependency matrix (Platform Operations receives 29 of 86 links, more than any
team); the unplanned breakdown (46 percent, of which 20 points are other teams' requests and 10 are
toolchain breakage across four build systems); the standing-orders map, where a 1-day environment task
cost 6 days of waiting on another team's feature.

**What to offer.** A funded rotation so the self-service work is planned capacity, not squeezed from
interrupts; explicit deferral of one or two of his planned projects, agreed with you and visible to
the CTO; a temporary limit on what other teams may request outside the intake; and credit for the
reduction in others' lead time, not only his own roadmap.

**What not to accept.** "We are too busy to fix the cause of being busy", left standing for another
quarter. The loop in the chapter is exactly this: full teams build queues, which create more
interrupts.

**A good answer** treats Tom's constraint as real, trades something concrete for the investment, and
measures the result by the request queue. **The weak answer** orders the work without freeing capacity.

## A2 — The WIP limit meets a sales escalation

**Response.** Do not lift the limit for the sales request by default. First establish whether the
prospect's integration is in fact more valuable than what Payments and Integrations has in progress. If it is, it should
replace an item, not join the pile; if it is not, it waits.

**To the sales director.** Explain that the team is finishing committed work, including the
accounting-system integration a renewal depends on, and that starting another item now would delay everything in progress, including it. Give
an honest estimate of when it could start, and offer to take the trade-off to the CPO if they believe
it should displace committed work.

**To Elena.** Back the limit publicly. Ask whether the team is at the limit because items are blocked
on other teams; if so, the limit is doing its job by exposing those dependencies, and you need to help
clear them. Ask whether the limit is set at a level the team can sustain.

**What it says about the expedite policy.** If there is no policy, the escalation went to you because
nobody else could decide. Write one: who may expedite, how many expedited items may be in flight, and
how expedites are reported. A promise to a prospect made without engineering is itself an upstream
process problem.

**A good answer** protects the limit while allowing a deliberate swap. **The weak answer** either
caves or refuses without offering a path.

## A3 — Choosing the dependency pairs

**First pair: everyone to Platform Operations** (29 inbound links, the largest column). The requests are
mostly environments, access, and pipeline changes. These recur and have the same shape each time, so
the answer is **remove**, through self-service. Transition cost: Platform Operations builds the
self-service capability while still absorbing requests, a temporary drop in its planned throughput;
requesting teams must learn the new tools.

**Second pair: Orders and Billing** (9 links Orders to Billing, 6 back, 15 in total). These are mostly
invoicing fields Orders needs to add. The change reason is Orders' business, but Billing owns
invoicing for good reasons (financial correctness, a high incident load). Moving ownership would add
load to Orders and split invoicing knowledge. The better answer is **loosen**: an order-to-invoice
contract with contract tests, so most changes no longer need a Billing release. Transition cost:
Billing and a staff engineer define the contract; for a quarter both teams carry the old and new paths.

The case study made a similar choice for Payments and Integrations and Billing (9 links), because the
accounting integration ran through that boundary that quarter; picking it here is equally defensible.
Another is Customer Experience to Orders (8 links), especially if the API
changes are frequent; the likely answer there is also a versioned contract.

**A good answer** reads the matrix, uses the decision sequence (recurs, same reason to change,
contract possible), and names who pays the transition. **The weak answer** proposes a weekly
dependency meeting for all pairs.

## X1 — Six more engineers for Payments and Integrations

**What six engineers would change.** With the integration due at the end of week 6 of quarter 2 and
four engineers already on it, almost nothing before the date. Later, possibly the team's throughput on work it can do alone, after a
ramp-up of a quarter or more, during which existing engineers spend time onboarding them. It would also
break the flat-headcount constraint.

**What they would not change.** The standing-orders map puts most waiting in queues at other teams
(Billing, Platform Operations, Customer Experience) and in intake and release, and the integration
depends on the same kinds of queue: Billing's ledger data and Platform Operations' test environments.
More people in Payments and Integrations do not shorten a Billing queue. Little's law says lead time is work in progress over throughput; if
new engineers start more items, work in progress rises with throughput and lead time does not fall.
The research on distributed work suggests that more people involved in an item tends to lengthen its
calendar time, not shorten it.

**What to ask for instead.** Reserved Billing capacity for the posted-invoice export in the first
weeks of the quarter; Platform Operations' self-service environments; a WIP limit and an expedite freeze on
Payments and Integrations for the duration; and the CEO's help in keeping new integration requests
from sales away from the team until the commitment ships.

**A good answer** respects the CEO's intent (the renewal), quantifies where the time goes, and offers a
faster alternative. **The weak answer** says "Brooks's law" and stops there.

## X2 — One measure for the board

**Recommendation.** Median lead time from commitment to customer availability, for items of a stated
size class, reported with its 85th percentile and paired with throughput.

**Why lead time.** It is what customers and the CPO feel, it includes the cross-team waits that
throughput hides, and it responds to the levers this chapter describes. Throughput alone rewards
splitting items and starting easy work, and says nothing about how long any customer waits.

**How it is gamed.** Moving the start of the clock later (committing only when work is nearly done),
splitting items so they look small, and excluding blocked or abandoned items. Countermeasures: define
commitment as the roadmap or plan entry, report the percentile so the tail is visible, report
throughput alongside (splitting raises throughput visibly), and audit a sample of items each quarter.

**Alternative.** A predictability measure (share of committed items delivered in the quarter
promised, 41 percent at Northstar's baseline) is closer to what the board cares about, and Chapter 17
treats it. It is gamed by committing to less; pair it with throughput.

**A good answer** chooses, names at least two gaming routes, and pairs the measure. **The weak answer**
proposes story points or deployment count.

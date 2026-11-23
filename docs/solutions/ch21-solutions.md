# Chapter 21 solutions — Technical Debt: Identification, Economics, and Prioritization

Worked solutions for the [chapter 21 exercises](../parts/05-engineering-quality/21-technical-debt.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Is the payments module debt?

**Is it debt?** In Cunningham's sense, debt is a shortcut whose cost is the interest paid while it
stays. The module may contain shortcuts (untested retry logic is one), but the evidence offered is
about its size and appearance. It was changed twice in a year, both times without incident. On the
data given, its time interest is close to zero: almost no work flows through it. It is dormant debt.

**What interest it might still charge.** Risk interest is the open question. Untested retry logic in
a payments path can duplicate or drop payments under failure, and the cost of one such incident could
be large. So the honest framing is: low time interest, unknown risk interest.

**What to ask for before deciding.** Incidents and support tickets involving the module; whether any
planned feature will touch it in the next two quarters (option cost); and a targeted look at the
retry logic. A sensible decision is probably **reduce**: add tests around retry behavior (days, not
six weeks) and **accept** the rest with a review date, revisited if the roadmap moves into the module.

**Criteria for a good answer:** separates time interest from risk interest; uses change frequency as
evidence; proposes a small option before the full cleanup. **Weak answer:** approves or rejects the
six weeks on the basis of how the code looks.

## F2 — Classifying Northstar's debt

| Fact | Kind | Interest it charges | Data that would measure it |
|---|---|---|---|
| 17 of 24 components without a runbook | Documentation | Longer restores, more escalation to the few people who know | Time to restore for incidents on components with and without runbooks; escalation counts |
| auth-svc deployed by scripts one person understands | Infrastructure and knowledge | Manual deploy time; risk of an unmaintainable tier 1 service if that person leaves | Hours per deploy; failed or rolled-back deploys; INC-416 (a shared deploy-script change that broke rollback for four services) shows the risk |
| Core main branch red 22 percent of working hours | Test (and partly infrastructure) | Blocked merges, reruns, waiting, distrust of the suite | Pipeline logs: red time, reruns, share of failures unrelated to the change (9 percent) |
| core/scheduler shared by four teams, no owner | Architecture and knowledge | Coordination on every change; nobody on call; slow diagnosis | Changes touching the module and their review wait; incidents involving it |

A good answer notices that most of the list is not code debt, and that a code scanner would find none
of it. It also sees that one fact can be two kinds (auth-svc is both infrastructure and knowledge
debt), and that the right response to the scheduler is an ownership decision before any technical
work. The runbook entry's interest is probably concentrated in tier 1 components; a good answer
prioritizes those rather than demanding seventeen runbooks.

**Weak answer:** labels everything "code debt" or lists the kinds without saying how the interest
would be measured.

## F3 — The 23 percent argument

**What the source measured.** Besker, Martini, and Bosch surveyed 43 developers over time, with 16
interviews, and found that developers reported wasting on average 23 percent of their development
time because of technical debt. The journal version validated the finding on a separate dataset whose
size the abstract does not give. The measure is **self-reported** time, averaged across respondents.

**What it can support.** That developers in that study experience debt as a large drag, that extra
time often goes to additional testing, and that debt is commonly forced on developers by schedule.
It is a reason to take debt seriously and to measure it.

**What it cannot support.** Applying 23 percent to Northstar's 80 engineers (18.4 engineers) assumes
that the sample represents Northstar, that self-reports equal actual time, and that all of that time
could be recovered. None of those holds. It also risks double-counting with Northstar's 34 percent
unplanned work, which is a different measure with different causes.

**What Northstar should measure instead.** System data at the point of change: pipeline reruns and
red-branch time (TD-007), manual deploy time (TD-002), incidents by trigger and component (TD-001,
TD-004), and cycle times for changes touching suspect modules. Self-report can point at candidates;
system data prices them.

**Weak answer:** accepts the 18 engineers, or dismisses the study entirely. A good answer keeps the
finding and refuses the extrapolation.

## A1 — Responding to the core/customer redesign

**In the meeting.** Agree with what is true: the module is hard to change and has no owner, and Ines
knows it better than anyone (she is the staff engineer for the Core domain). Then move the question from "is it bad?" to "what does it cost, and
where?" Say plainly that you are not rejecting the proposal and that you will not fund three
engineer-years without knowing the interest, because Northstar has a standing rule against funding a
Core rewrite and the register ranks by cost, not conviction. Ask Ines to lead the measurement.

**In the next quarter.** Assign an owner first (core/customer to Orders, as in TD-003); without one,
no data and no follow-through. Tag every change touching the module and record review wait, rework,
and incidents. Ask Ines to propose the first slice that would remove the most interest, so that if the
data supports investment, there is something fundable in one quarter.

**What you avoid.** Rejecting the proposal publicly would tell the staff engineers that technical
judgment does not count. Funding it on conviction would teach every team that the most persuasive
pitch wins capacity. The measurement quarter gives Ines a path to win on evidence.

**Criteria:** owner before investment; measurement with a deadline; a sliced alternative; respect for
the person. **Weak answer:** "we can't afford it" with no route forward, or approval because two
managers support it.

## A2 — Explaining the standing share to the CPO

**What to show.** The priced top of the register: TD-004 (about $82,000 a year in incident risk for
about $20,000 of work) and TD-007 (about $54,000 a year of lost engineering time for about $20,000).
Then the large entries, TD-001 and TD-006, as separately funded decisions. The point is that debt work
is ranked by return, like features, and that the top items pay back within months.

**The framing.** Debt work is not an extra claim on capacity. It is paid out of the 12 FTE
prevention allocation Amara Okafor (CPO) already agreed, and the question is only how that allocation
is split. Say so first: no team loses more feature capacity than the allocation already took, and
the renewal teams (Orders, and Payments and Integrations) stay at 10 percent.

**Why part of it should go to debt.** Much of what causes incidents is debt. Seven of Billing's eight
baseline incidents came through Core releases or migrations. TD-004 (migration practice) prevents
incidents directly; TD-007 (flaky tests) recovers about $54,000 a year of engineering time and
restores trust in the pipeline that guards releases. Spending the
allocation only on fixing individual incidents treats symptoms while the interest keeps accruing.
Propose a named slice for the top register entries, mostly from Billing's 25 percent where the
interest lands, and leave the rest for incident follow-ups and other prevention work.

**What you will not give up.** The debt slice being a visible line in the plan, and the migration and
flaky-test fixes, which directly reduce incidents that threaten the renewals.

**Monthly reporting.** Which register entries the slice moved, the interest removed (red-branch time,
migration incidents), and any borrowing with its payback date.

**Criteria:** numbers with assumptions; debt stated as part of the prevention allocation, not on top
of it; a reason, from the register, for giving debt a slice; the renewal commitments protected. **Weak answer:** an appeal to engineering best practice, or a percentage without entries.

## A3 — Diagnosing allocation failures

**Two teams spending on unregistered items.** Either the register is too hard to enter (so teams
skip it), or the items have no measurable interest (so teams avoid stating it), or the teams do not
believe the register drives decisions. Ask which. If entering an item takes more than a few minutes,
simplify the entry. If the items are upgrades or improvements the team values, ask them to register
the interest after the fact and see whether it holds up.

**One team spending none because the manager borrows it.** The share is not protected; borrowing is
silent. The manager is responding rationally to feature pressure that nobody has traded off
explicitly. Talk to the manager and the product lead together: what pressure, which dates, and was the
borrowing a decision anyone would have endorsed?

**Redesign without a permission process.** Keep team autonomy within the share. Add two things: a
monthly one-line report per team naming the register entries moved, and a rule that borrowing is
recorded with a payback date and reported in the same review. Do not add approval steps for spending
the share on registered items; that would recreate the bottleneck the share exists to avoid.

**Criteria:** distinguishes the two patterns' causes; fixes visibility rather than adding gates.
**Weak answer:** central approval of all debt work, or ignoring the problem because the total share
was "spent".

## X1 — CI consolidation against a revenue feature

**Common frame.** Both cost about two engineer-years. The feature's cost of delay is $60,000 a month,
$720,000 a year. TD-006's time interest is about 1.5 FTE, about $278,000 a year, or about $23,000 a
month, plus benefits not priced in the chapter: comparable pipeline metrics, one place to fix rollback
(INC-416), and faster later work such as automated regression for
Core.

**Decision.** On these numbers, fund the feature first. Its cost of delay is roughly two and a half
times TD-006's priced interest, and the debt's interest does not jump at a known date.

**What would reverse it.** If the feature's cost-of-delay estimate is soft (an unvalidated sales
forecast) and TD-006's unpriced risk is large: for example, if consolidation is a prerequisite for
the release-train work that protects $9M of renewals, then TD-006 inherits part of that cost of delay
as option cost. A good answer asks for that dependency explicitly. Also: if a trigger appears (an
unsupported CI system reaching end of life), the ranking flips.

**What to tell the losing team.** The ranking and its inputs, what would change it, and when it will
be revisited. Consider whether a slice of TD-006 (moving the four shell-script services, overlapping
TD-002) can go into standing capacity now.

**Weak answer:** picks the debt because "debt always comes first", or the feature because "revenue
always wins", without comparing numbers.

## X2 — One number for the board

**Proposal.** Two numbers, on one slide, with a trend line:

1. **Total annual interest on the top ten register entries**, in money, with its main components
   (engineering time, incident risk). This answers whether debt is getting cheaper to carry.
2. **Interest removed this quarter per unit of debt capacity spent**, which answers whether the
   debt budget is producing returns.

Optionally, as context: the share of Sev1 and Sev2 incidents whose trigger traces to a registered
debt entry.

**How directors would game them.** Interest can be lowered by under-estimating it or by dropping
inconvenient entries from the top ten. Interest removed can be inflated by over-estimating it at
entry and then "removing" it. The incident share can be lowered by classifying triggers away from
registered debt.

**Prevention.** Tie interest estimates to system data wherever possible; have staff engineers
spot-check the top entries each quarter; keep removed entries visible with their before-and-after
data; and audit trigger classification the same way Northstar's weekly review audits severity. Do not rank
directors on the numbers; use them to decide funding.

**Criteria:** few numbers; each with its gaming described; audit mechanism stated. **Weak answer:**
register size or a static-analysis score, both of which reward deleting entries or tuning the tool
rather than reducing cost.

# Chapter 45 solutions — Business Models, Engineering Economics, and Investment Decisions

Worked solutions for the [chapter 45 exercises](../parts/10-business-leadership/45-business-models-and-engineering-economics.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional,
and every number below depends on the stated assumptions.

## F1 — Pricing a retention feature

**The arithmetic.** Cutting churn from 10 to 8 percent on a $6M segment retains $120,000 of ARR a
year. At 75 percent gross margin that is $90,000 a year of margin, about $1,700 for each week of the
year. The feature costs 6 × 12 = 72 engineer-weeks.

**The shape matters more than the first number.** A week of delay does not just postpone $1,700; it
lets about $2,300 of ARR ($120,000 ÷ 52) churn that would have stayed, and a churned customer usually
stays gone. If retained customers would have stayed three more years, a week of delay costs closer to
3 × $1,700 = about $5,200 of margin (undiscounted). So the profile is **long life, peak affected**:
the loss is permanent, not shifted. A good answer gives the range ($1,700 to $5,200 a week) and says
which end it believes and why.

**Assumptions to test first.** (1) That the feature, rather than price, support, or reliability,
explains two points of churn: check exit interviews and churn reasons for the last year. (2) That the
segment's churn would otherwise stay at 10 percent. A useful additional check is whether a smaller
first release (a staged option) could capture most of the retention.

**Weak answer:** $120,000 ÷ 52 = $2,300 a week, at revenue rather than margin, with no shape and no
named assumption.

## F2 — What the prevention package really costs

**The staff engineer is wrong** because capacity is not free when it is fixed. The 70 engineer-weeks
will be spent on something; spending them on the package means not spending them on the next best
item. That forgone value is the cost.

**The analyst is wrong in a different way.** $249,000 (70 × $3,558) is what the capacity costs in
salary, but with flat headcount none of it is incremental cash: Northstar pays those salaries
whatever it chooses. Treating it as the cost invites approving anything worth more than payroll,
without asking whether something else was worth more still.

**The cost in this chapter's terms** is the opportunity cost: the value of the best alternative
displaced. In week 31, that might be purchase approval rules (an expected $227,000 a year in the
chapter's example) or the lowest-ranked committed item the package would push out.

**What belongs in the investment case:** both, labeled. The $249,000 is the consistent yardstick used
for every option so that NPVs are comparable; the opportunity cost names the displaced item and its
cost of delay. A strong answer adds that if the package created no need to displace anything (for
example, it used capacity already reserved for prevention in the quarter's allocation), the relevant
comparison is with other prevention candidates, not with features.

**Weak answer:** picking one of the two positions.

## F3 — Payback against NPV

**Investment 1.** Cash flows: −$300,000, then $200,000 in years 1 and 2. Payback: 1.5 years. NPV at 10
percent: 200,000 × 0.9091 + 200,000 × 0.8264 = $181,800 + $165,300 = $347,100, minus $300,000 = about
**+$47,000**.

**Investment 2.** Cash flows: −$300,000, then 0, then $250,000 in years 2, 3, and 4. Cumulative cash
reaches $250,000 at the end of year 2 and $500,000 at the end of year 3, so payback is 2 + 50/250 =
**2.2 years**. NPV: 250,000 × (0.826 + 0.751 + 0.683) = 250,000 × 2.261 = $565,200, minus $300,000 =
about **+$265,000**.

**What the methods prefer.** Payback prefers investment 1; NPV prefers investment 2 by more than five
times. Payback ignores everything after the cutoff, which is exactly where investment 2 earns.

**The judgment.** Payback is not useless: it is a crude proxy for risk, and software benefits four
years out are genuinely uncertain. The right move is to test that worry directly: drop year 4
entirely, and investment 2's NPV is 250,000 × 1.577 − 300,000 = about $94,000, still higher. A good
answer reports both measures, says why they disagree, and tests the horizon rather than using payback
as a hidden risk adjustment.

**Weak answer:** choosing investment 1 because "it pays back faster" with no NPV.

## A1 — Adding renewal protection to the comparison

**Assumptions (illustrative).** The top-40 customer's ARR is about $1.17M (canon average). Without
action, the probability of losing it at the week 60 renewal is 30 percent; the prevention package, if
it addresses the failures this customer has suffered, cuts that to 20 percent. A ten-point reduction
is worth 0.10 × $1.17M × 72 percent = about **$84,000 a year** of margin. Lost revenue is valued at
margin, because the delivery costs disappear with the customer.

**Rebuilt B.** Expected annual benefit 0.6 × $285,000 + $84,000 = about $255,000. NPV over three years
at 10 percent: $255,000 × 2.487 − $249,000 = about **+$386,000**, now above A's $315,000. Cost of delay
rises to about $4,900 a week, level with A.

**The bigger change is the shape.** The renewal term makes B partly a **deadline item**: its benefit
depends on improvements the customer can see before the renewal conversation, perhaps by week 52 to
56. B should be scheduled backward from that date, not just ranked.

**Criteria for a good answer.** It checks that B's work actually targets the failures this customer
raised (ask Sofia Alvarez for the account's incident history); it avoids double-counting credits the
customer already received; it states the probability shift as a claim someone owns and can be checked
at week 60; and it notes the forum still has to weigh A, whose sponsor will argue his own probability.

**Weak answer:** "reliability matters for renewals" with no number, or a number with no owner.

## A2 — Staging a rewrite proposal

**Diagnosis.** "Flexibility for future pricing models" is an option claim with no exercise in sight:
no pricing change is planned. By the chapter's third rule, its value is close to zero until a
foreseeable change would use it. The six-month rewrite is also hard to reverse.

**A staged alternative.**

1. **Stage 1, two to three weeks.** Measure the current cost of change: lead time and defect rate of
   the last few billing changes, co-change history, and the incidents attributable to the component.
   Ask product and finance to list pricing changes they consider likely in the next year, with rough
   value.
2. **Stage 2, only if stage 1 justifies it.** Build a seam for one pricing rule (a strangler-style
   extraction) behind which the next actual pricing change is made.
3. **Stage 3.** Continue extraction only as real pricing changes arrive, each paying for its share.

**Evidence that funds stage 2:** either a committed pricing change with a stated value, or measured
change costs high enough that a cheaper path to the next changes pays back within the horizon.

**What a good answer avoids.** It does not dismiss the team lead: the measurement in stage 1 may
show real interest being paid, which turns the proposal into a debt case (Chapter 21). It also prices
the first stage, which is the option premium.

**Weak answer:** approve or reject the six months whole.

## A3 — Correcting inflated estimates

**Read the data carefully first.** Nine items is a small sample, and the median ratio of three hides
the spread; one or two lost deals can dominate. But the direction is clear, and reliability items
being within 30 percent shows the method can be calibrated.

**Process changes.**

- Sales estimates name the deal, its stage, and the probability source (pipeline-stage history from
  the sales system rather than the sponsor's judgment).
- A neutral reviewer (finance or revenue operations) signs off inputs on items above the large-item
  threshold.
- Until the record improves, sales-sponsored values are ranked at a calibration factor derived from the
  track record (for example, divided by two), published openly, and reviewed every quarter.
- Every sponsor category's variance is published, including engineering's, so the rule is not seen as
  aimed at one function.

**What to say to the VP of Sales.** Lead with his interest: his requests win more often when their
numbers are believed. Show the nine items, ask which estimates he would defend in hindsight, and
offer the path back: as realized values converge, the calibration factor goes away.

**Criteria.** A good answer neither bans sales estimates nor accepts them unchecked, treats the
correction as temporary and symmetric, and recognizes that reliability estimates may also be biased
(conservatively) in ways worth checking.

**Weak answer:** a private decision to discount sales items without telling anyone, which fails the
moment it is discovered.

## X1 — Sizing Northstar's deal allowance

**One defensible proposal.** Reserve about 2 FTE for the quarter (about 26 engineer-weeks, roughly 4
percent of the quarter 3 plan's 49.9 FTE of product capacity), split between the two teams most
often asked, with a rule:

- Only single-team requests of at most 6 engineer-weeks.
- A written cost-of-delay line: deal ARR, stage, probability source, margin, urgency profile.
- Admission if its CD3 beats the lowest-ranked committed item; otherwise it joins the normal queue.
- Unused allowance returns to the target band at mid-quarter.

**Opportunity cost.** About 26 × $3,558 = $92,500 of capacity, but the real cost is the target items
that will not be attempted, roughly the value of the weakest targets in the plan. State them by name.

**Assumptions to declare.** That small deal requests arrive often enough to use 26 weeks (check
Greg Tanaka's last two quarters of requests), and that they are genuinely single-team (cross-team
requests stay in Chapter 42's portfolio and its limit).

**Evidence after two quarters.** Utilization of the allowance; win rate and realized ARR of deals it
served against their estimates; whether admitted items would have ranked high anyway (in which case
the allowance adds nothing); and its effect on unplanned work. Shrink if under-used or if estimates
prove inflated; remove if served deals do not convert better than unserved ones.

**Criteria.** Any size is defensible if it is derived from request history, has an admission rule
using the chapter's frame, names the displaced work, and has a review with removal conditions.

**Weak answer:** a size chosen because it "feels reasonable", with no rule and no review.

## X2 — Defending the reliability allocation

**What the CFO's analysis omits.** Valuing reliability only by credits avoided misses (1) revenue
protection at renewal, weighted by concentration; (2) capacity returned from unplanned work, valued at
the capacity rate; (3) tail risk, the large outage that has not happened yet, which credits history
cannot show; and (4) the dynamic: reliability is maintained by continuing investment, and the four
good quarters are partly the result of the allocation the CFO wants to cut.

**How to value it.** Renewal term: at-risk ARR among accounts that have raised reliability × an
estimated probability shift × margin. Capacity term: the unplanned-work share now against before, at
the capacity rate. Tail term: one or two named scenarios (for example, a multi-day outage on the
order path) with a rough probability and a cost including credits, churn, and the response effort.
Present ranges, not points.

**What to accept.** The CFO has a fair point: as credits fall, the marginal dollar of reliability
work returns less. A strong answer accepts a staged shift (say a quarter of the allocation rather
than half), with tripwires agreed in advance: error budget burn, unplanned-work share, customer-detected
incident share, and escalations from the largest accounts. If a tripwire is crossed, the allocation
returns automatically.

**Criteria.** The answer uses the CFO's units, concedes what is true, proposes an experiment rather
than a standoff, and makes the reversal condition explicit before anyone has a stake in it.

**Weak answer:** "reliability is not optional", which concedes the economic argument by not making it.

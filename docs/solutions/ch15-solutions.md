# Chapter 15 solutions — Planning, Prioritization, and Delivery Methods

Worked solutions for the [chapter 15 exercises](../parts/04-execution/15-planning-prioritization-and-delivery-methods.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — The team that never meets its Sprint Goal

**Diagnosis.** The Scrum Guide's Sprint assumes the team can commit to a Sprint Goal and protect most
of the Sprint for it. A team spending 40 percent of its time on unplanned work cannot. Missing five
Sprint Goals in six is the predictable result of a method whose assumption the work violates, not
evidence of poor estimation. Better estimates of the planned work would not help, because the
planned work is not what consumes the sprint.

**What to change first.** Two defensible paths. Keep sprints but subtract a measured interrupt budget
(about 40 percent) before planning, set one Sprint Goal that fits the remainder, and put one or two
people on an interrupt rotation so the rest can finish. Or move to Kanban with an explicit interrupt
lane, a WIP limit, and work item age as the daily signal, which fits continuous arrival. Either way,
also ask where the interrupts come from; reducing them is worth more than any method change.

**Criteria.** A good answer ties the diagnosis to the method's stated assumption, quantifies the
interrupt load, and treats estimation training as the wrong lever. **Weak answer:** "run Scrum
properly", or more planning ceremonies.

## F2 — Re-ranking with a retention risk

**Calculation.** Two customers worth $600,000 a year, with a one-in-three risk of leaving without the
feature: expected annual value at risk about $200,000, or about $3,800 a week. The original $2,000 a
week already included "a rough retention value", so a careful answer replaces that part rather than
adding to it. Taking support savings as about half of the original figure gives roughly $4,800 a week;
adding the full $3,800 to $2,000 gives $5,800. Either way, with a two-week duration, CD3 is 2.4 to 2.9,
well above P1's 1.27.

**New order:** P2, P1, P4, P3. With $5,800 a week for P2, total cost of delay is 5.8×2 + 3.8×5 +
4.3×11 + 1×19, about $97,000, against about $107,000 for the previous economic order with P2's new
value. The ranking change is worth about $10,000; the larger point is that P3 stays last.

**Criteria.** States the assumptions, avoids double counting, notices that the conclusion holds across
the plausible range, and notes that retention risk is often step-shaped (it hits at the renewal date),
so the date may matter more than the weekly average. **Weak answer:** adds numbers without asking what
the original estimate contained.

## F3 — "Scrum teams deliver 40 percent faster"

**What the claim can support.** A vendor survey can show that respondents who say they use Scrum also
report faster delivery. It cannot show that Scrum caused it: teams that adopt Scrum may differ in
size, product, maturity, and investment, and self-reported speed is not measured lead time. Vendor
sponsorship adds a reason to ask how the sample was drawn.

**What the research says.** The systematic reviews in the chapter found a thin evidence base:
Dybå and Dingsøyr concluded that more and better studies were needed, and the Kanban review reports
benefits from case studies without controlled comparisons. The Kuhrmann survey found that most
organizations run hybrids and that practices affect perceived agility more than method labels. That
cuts against any claim that one label produces a fixed speed-up.

**What would change the view.** A study with measured outcomes (lead time, change failure rate) for
comparable teams before and after a change, ideally with a comparison group, or a pilot in your own
organization with a baseline and measured results.

**Criteria.** Separates correlation from cause, asks about the sample and measure, and proposes a
local test. **Weak answer:** dismissing the claim because it comes from a vendor, without saying what
evidence would be better.

## A1 — Billing and the sprint it cannot keep

**Learn first.** What "the team likes the rhythm" means: the review with product, the retrospective,
the sense of finishing? Which of those parts are valuable, and which are rituals? Where do the
mid-sprint changes come from: incidents (Billing had 8 Sev1 and Sev2 incidents and 41 percent
unplanned work), Core train regressions, or product changing its mind?

**Data to bring.** Six of six sprints changed mid-sprint, one Sprint Goal met in six, 41 percent
unplanned work, and the canon fact that Core now releases weekly, so the two-week train that set the
sprint length no longer exists.

**Options.** (1) Keep two-week sprints but plan only about 55 percent of capacity, with an interrupt
rotation and a single Sprint Goal. (2) Kanban for delivery, keeping a fortnightly review and
retrospective for the rhythm the team values. (3) One-week sprints aligned to the weekly train. Marcus
should choose, with an agreed measure (goal attainment or work item age) and a review after six weeks.

**Criteria.** Separates the rhythm the team values from the plan it cannot keep; does not impose a
method. **Weak answer:** ordering Kanban, or accepting the status quo because the team likes it.

## A2 — Replying to a third deal commitment

**The reply** should be warm, fast, and specific. Something like: "Glad the deal is moving. Orders'
next six weeks are reserved for bulk ordering, which the renewal depends on, so nothing can be added
there without moving the renewal date, and I won't do that. To rank this for the rest of the quarter
I need three things from you: the deal's annual value, how much of the decision depends on this
feature, and the date by which the prospect needs it. Engineering will give you a duration range by
Thursday. If it ranks above the current next items, I'll show you which one it displaces and we can
decide together with Amara. Please don't give the prospect a date until we have."

**Criteria.** Protects the fixed-date renewal item; asks for a value estimate owned by the
requester; offers a fast, transparent ranking rather than a refusal; names the trade (what is
displaced); and addresses the already-mentioned date, perhaps by offering a decision date instead.
**Weak answer:** a flat no, which teaches Sales to escalate, or a yes, which repeats the baseline
quarter's overcommitment.

## A3 — A cadence for Data and Analytics

**Keep** what works: the request queue triaged twice a week (it gives requesters a fast answer) and
the quarterly project list (warehouse work is genuinely project-shaped). Data and Analytics has the
lowest change failure rate and unplanned share in the organization; do not fix what is not broken.

**Add** three things. A WIP limit and service classes for the queue (for example, same-week for
customer-facing report defects, standard for new reports) with work item age reviewed weekly.
Fixed-time cycles with an appetite for the warehouse projects, say six weeks, with a checkpoint at
the midpoint and a rule that unfinished projects are re-shaped or re-bet rather than silently
extended. A monthly roadmap review with product in the now, next, later format, so that requests
from other teams see the ranking.

**Capacity.** Reserve about a quarter of capacity for the queue, based on the 24 percent unplanned
share, and plan projects against the rest.

**Criteria.** Respects the existing strengths, fits two work shapes with two mechanisms, and states
the capacity split. **Weak answer:** imposing Scrum for uniformity.

## X1 — CTO approval of every customer-facing date

**Decision: change it.** The problem the CEO is solving is real: in the baseline quarter, five of 17
committed items had customer dates before engineering sized them, and only 7 of 17 shipped. But CTO
approval of every date makes the CTO a bottleneck and invites Sales to avoid the process by speaking
vaguely to customers.

**A better rule:** any external date requires an engineering estimate as a range and reserved
capacity, approved by the responsible director within two working days; the CTO approves only items
above a size threshold or that displace an existing commitment. Each quarter the executive team
admits a short list of fixed-date commitments. Forecasts may be shared with prospects only as
ranges, labeled as forecasts.

**Rationale paragraph:** "We lose more deals by missing dates than by giving them a few days later.
This rule makes every date we give one we expect to keep, and keeps the decision close to the team
that has to deliver it."

**Criteria.** Acknowledges the CEO's goal, addresses Greg's concern with a fast service level, and
designs a rule that will be followed. **Weak answer:** accepting the rule as written, or rejecting it
to keep Sales happy.

## X2 — One method for every team

**Recommendation.** Standardize the interface, not the method. Every team reports, in one format,
what is committed in the next four to six weeks, what is at risk, what is ranked next with its cost of
delay, throughput and cycle time, and unplanned share. Inside, teams choose: Payments and
Integrations' Kanban works; Platform Operations' interrupt load would wreck sprints.

**What comparison he can get:** trends within each team, capacity spent on unplanned work, and
delivery against commitments. **What he cannot get:** a meaningful comparison of story points or
velocity across teams, under any method, because units differ and comparison invites inflation
(Chapter 18). A common method does not make teams with different work comparable.

**Transition cost.** Each team forced to change method loses several weeks of output while habits
re-form, during quarters when the two renewal commitments must keep their dates. Changing four or five
teams at once would hit both renewal teams.

**Criteria.** Understands Victor's underlying need (visibility and comparability), gives him most of
it, explains what is impossible, and prices the transition. **Weak answer:** agreeing to Scrum
everywhere, or refusing without offering a common reporting interface.

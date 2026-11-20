# Chapter 49 solutions — Multi-Year Transformation, Executive Communication, and Constructive Politics

Worked solutions for the [chapter 49 exercises](../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Gaming the stage 2 exit criteria

| Criterion | Met on paper while the problem remains | Pairing check |
|---|---|---|
| Sev1+Sev2 at most 12 a quarter | Incidents rated Sev3 that meet the Sev1 or Sev2 definition | The weekly severity audit against the week 3 definitions, sampled by someone outside the owning team |
| 99.9% in each quarter | Measuring availability on a narrower path, or excluding "planned" downtime | The contractual definition, unchanged, and the service-credit total as a cross-check |
| Credits at most $25,000 | Credits negotiated away commercially rather than earned by uptime | Credits paired with availability; a fall in credits without a rise in availability is a signal |
| 14 of 14 tier 1 (current list) meeting the minimums | Runbooks that exist but are stale; on-call rotations of one person | A quarterly drill on two random tier 1 components using only the runbook |
| Every component in the register once | A team named as owner that has never changed or operated the component | Each owner's last change and last page for the component |
| No critical role without cover | A name written in the interim column with no agreement or preparation | The named person confirms, and has done one piece of the role's work in the stage |

**Which two to make mandatory.** A good answer picks the ownership register and succession cover,
because they are the stage's reason to exist: incidents and availability measure whether gains held,
while ownership and cover are what makes them hold without the director. Picking the tier 1 minimums
is defensible, since it is closest to reliability. The weak answer makes all six mandatory, which turns
every gate into a pass-or-stop decision and pushes the team toward gaming the weakest criterion.

## F2 — One set of facts in three currencies

**Rajiv Menon.** "Stage 2 adds $150,000 to operating expense. Year 2's $250,000 discretionary tooling budget is
already committed, so this falls outside it and needs your approval. The other $555,000 is 6 existing engineers for two quarters; headcount and payroll do not
change. Credits fell from $410,000 to $60,000 a quarter; the stage aims at $25,000 or less." Most likely
misread: "$705,000 total" if it appears anywhere, so the paragraph never states it without the split.

**Greg Tanaka.** "Stage 2 keeps 6 of 80 engineers, 7.5 percent, on reliability for quarters 5 and 6.
An option moves 2 of them to your deal features; the proposal shows what that defers. New spending
is $150,000 of tooling." Misread risk: "only 6 engineers" read as trivial, so state the deferred criteria
next to it.

**Helena Marsh.** "Six of our largest 40 customers renew in quarters 5 to 8. Incidents are at 14 a
quarter against 30; availability is 99.89 percent against a 99.9 contract. Release failure rates fell from 31 to 22
percent in quarter 1 and have not moved since (23 percent), on too few releases to call a trend. Stage 2 costs $150,000 in new spending plus 6 engineers' time." Misread risk: 99.89
percent sounds like success; give the minutes over.

A good answer keeps every number identical across versions. The weak answer changes the conclusion
("small" for one reader, "essential" for another).

## F3 — A mandatory miss at the week 56 gate

**What the rule requires.** Incidents: 14 in quarter 3 and the supposed 13 in quarter 4, both at most 15, so the
incident criterion is met for two consecutive quarters. Availability: 99.88 percent in a 91-day quarter
means 0.12 percent of 131,040 minutes, about 157 minutes, against about 131 allowed, so the criterion
(99.9 percent in a full quarter) has not been met in any quarter. A mandatory criterion is missed, so
there is no default continuation. The framework asks whether the cause is understood: if yes, re-scope
with a short gate (four weeks, week 60); if no, stop and review.

**What to write.** One page: the miss stated first, with minutes; which incidents consumed the minutes;
whether they share a cause; what stage 2 work addresses that cause; the re-scope proposed (for example,
moving a pipeline or detection item earlier); and the criterion unchanged.

**Re-scope versus goalposts.** A legitimate re-scope changes the plan and keeps the criterion. Moving
the goalposts changes the criterion: switching to an annual average, excluding one incident as
"exceptional", or measuring the order path alone. The weak answer argues that 99.88 is "close enough",
which is true commercially but spends the credibility the gate exists to protect.

**Criteria.** A good answer states that a mandatory criterion is missed, applies the written rule
rather than a new one, quantifies the miss in minutes, and keeps the criterion unchanged.

## A1 — Accepting the back-channel offer

**Consequences.** Amara Okafor finds two engineers working on a feature outside her plan and the
portfolio forum; she now has reason to distrust both the allocation she was promised and the director.
Rajiv Menon sees the prevention allocation reported as 6 FTE while 4 do the work, which undermines every
later cost statement. The portfolio forum's process (Chapter 42) is shown to be negotiable by
private arrangement, so other executives start negotiating privately too: exactly the
perceived politics that the Chang et al. meta-analysis associates with lower satisfaction and commitment.
The director's credibility, the program's working capital, is spent on a single meeting's support.
When it leaks, and it usually does through the engineers doing the work, Greg Tanaka loses less than
the director: he asked; the director agreed.

**What to say.** "I want your support, and I think your case for the deal features is strong
enough to make in the open. I'll put the 4 FTE option in the proposal with its cost and what it defers,
so the whole team can choose it. I can't move engineers outside the forum; that would break the
allocation I'm asking Amara and Rajiv to trust."

A good answer refuses the trade while taking the interest seriously. The weak answer either accepts or
lectures Greg about ethics, which loses the relationship without serving his interest.

## A2 — Succession cover from the program's own work

One defensible set of assignments:

| Role with no cover | Assignment from stage 2 | Delivery risk | How to price it |
|---|---|---|---|
| Billing manager | A senior Billing engineer runs the Billing tier 1 minimums workstream and attends the operations review as Billing's representative | Billing has the highest incident history; slower closure of its remaining tier 1 gaps | One extra review checkpoint; about 1 engineer-week of the manager's coaching time |
| Data and Analytics manager | A senior engineer in Data and Analytics leads the ownership register reconciliation across teams | Cross-team work for someone without positional authority | Director sponsorship at the leadership meeting; schedule slack of two weeks |
| Core-domain staff role | A senior Core engineer co-owns Core code standards decisions with Ines Carvalho for the stage | Slower standards decisions | Allow the 10-day decision window to stretch in the first month |
| Data-and-integration staff role | A senior engineer pairs with Li Na Zhou on migration and configuration standards and the CI target analysis | The CI target decision may slip | Make the decision date a stage 2 criterion with a buffer |

Assignments that reach interim cover by week 78 need the candidate to have done part of the role's
work, not watched it. The names are left to the reader; choosing them needs the managers' input. The
weak answer names successors in a table with no work attached, which meets the criterion on paper only
(see F1).

## A3 — Bundling the two decisions

**Decline.** Executive attention is the scarce resource (Dutton and Ashford). The organization decision
is about structure and people, and has an announcement in week 51; the continuation is about money and
capacity. Bundled, each becomes a bargaining chip for the other. An executive who dislikes the split of
Customer Experience may vote down the continuation, and vice versa, and the discussion ends with two
half-decisions. If one is rejected, the other carries the stain.

**Reply.** "I'd like to keep them separate. The organization decision needs the team's full attention
on people, and the continuation needs a clean discussion of money and capacity. Coupling them risks
trading one against the other. I'll bring the continuation to the week 49 meeting, after your decision,
and I'll show how it uses the new structure."

A defensible alternative is to agree if Victor insists, with each item voted separately and the
continuation framed as independent of the structure chosen. The weak answer agrees to save time without
considering coupling.

## X1 — Victor Lindqvist's decision

One worked decision:

1. **Approve stage 2 at 6 FTE**, conditional on the week 56 stage 1 gate, with the gate rule as written.
2. **Approve the $150,000 conditionally on an offset**, with the director and Rajiv Menon to identify it
   in the cloud and tooling budget by week 53; if none is found, the tooling scope shrinks and the
   affected exit criterion moves to stage 3.
3. **Decline the 4 FTE option for quarter 5**, and put Greg's deal features through the portfolio forum
   for quarter 6, with a re-check at the week 56 gate.
4. **Log** the decision, the conditions, and Greg Tanaka's dissent.

**What would make 4 FTE better.** You would need to believe that the gains are robust (change failure
rate falling, not flat at 22 to 23 percent), that the six renewals are not reliability-sensitive, and
that the deals depending on those features are worth more than the reliability risk to renewals among
the largest 40 customers. Today the evidence supports none of those, but a strong answer states how the evidence at week
56 could change that. Choosing 4 FTE is defensible if the quarter 4 data shows change failure rate
falling. The weak answer splits the difference (5 FTE) without a reason, which satisfies no one's
interest.

## X2 — Halvard's company-level gate

**Process.** One gate every half-year for all programs, held by the CTO with the five vice presidents
and finance. Each program brings a two-page document in the same format: stage, ask in FTE-quarters
and dollars, five to seven paired exit criteria, the gate rule, and the cost of no. Funding is given one
stage at a time; no program gets a full year at once, except for a named long-lead commitment.

**The twice-re-scoped program.** Two re-scopes means the cause is either not understood or not
addressable within the program. Stop and review: an independent review (a staff engineer or director
from another group) re-runs the diagnosis, and the program returns only with a rewritten stage. This is
the escalation-of-commitment guard; a third re-scope would be funding a hope.

**Against advocacy contests.** Same format, same criteria types, criteria agreed before stages start,
written pre-reads read before the meeting, and a finance partner who checks costs. The CTO publishes
decisions and reasons in the decision log, so groups see that funding follows evidence. A strong answer
notes that vice presidents will still lobby; the aim is that lobbying produces evidence in the shared
format, not private exceptions. The weak answer adds a scoring formula that the vice presidents then
learn to game.

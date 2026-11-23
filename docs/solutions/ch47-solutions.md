# Chapter 47 solutions — The VP of Engineering: Managing Directors and the Portfolio

Worked solutions for the [chapter 47 exercises](../parts/11-vp-engineering/47-the-vp-of-engineering.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Which decisions are unowned

**Diagnosis.** With three directors and 220 engineers, the decisions that move capacity between areas
(headcount by area, ownership of shared services, disputes between directors) are VP decisions in the
chapter's role table. Today the founder CTO takes them by default, at the cost of technical strategy,
which is the CTO's own job. The breakage is not that the CEO lacks a peer for the CTO; it is that the
VP decisions have no owner below the CTO.

**Recommendation.** Two defensible designs. (1) A VP of Engineering who owns allocation across the three
areas, director staffing, area boundaries, and the operating rhythm, while the CTO keeps technical
strategy and the external face; write the split down. (2) If the CTO prefers to keep running directors,
make that explicit, and move technical strategy work to a principal engineer or a technical direction
group. Hiring a "CTO-level peer" without naming decisions recreates the same ambiguity at a higher
salary.

**Criteria.** The answer lists the specific unowned decisions, assigns each, and tests the design
against the shape table (three directors whose claims conflict weekly is the classic case for the CTO
and VP split).

**Weak answer:** "Hire a VP because companies of 220 have one", with no decisions named.

## F2 — Partition dependence at Fulfillment

**What the theory predicts.** Bardolet, Fox, and Lovallo report that allocations tend toward equality
over the units a firm is divided into, so they vary with structure rather than with need. A fixed
50/50 split for three years while goals moved from warehouse integrations to delivery tracking is the
pattern: the two directors' areas, not the goals, determined the shares. The study concerns capital
budgets; applying it to engineering capacity is the chapter's extension, so treat it as a hypothesis
to test.

**Evidence to collect.** The group's goals each year; the bets funded under each director and their
outcomes; demand for each area measured independently (delivery-tracking backlog, incidents, customer
requests); and whether any work was declined in one area while the other funded lower-value items.
If one area's lowest-ranked funded bet would rank below the other's highest unfunded bet, the split is
not following value.

**Changing the process.** Size and rank bets across the group before mapping them to directors; compute
each area's gap; decide large gaps explicitly (move work, move people, or change the ranking); write
triggers for revisiting.

**Criteria.** The answer explains the mechanism, proposes a test rather than assuming bias, and changes
the order of the process. **Weak answer:** "Split 60/40 instead", which keeps allocation by org chart.

## F3 — Rewriting directors' goals

**Problems with the originals.** "Ship the checkout redesign" is an output, not an outcome; it invites
shipping on time whatever the conversion or failure rate does, and neglects reliability. "Improve team
morale" has no measure and no owner of a result, so it will be reported as done. "Reduce incidents in
Catalog by 30 percent" is measurable but narrows focus to incident counts: a director can reduce
reported incidents by reclassifying them, or by freezing change, and neglect the roadmap (Chapter 18
covers gaming).

**Rewritten.** Checkout area goals: failed-checkout rate from the current level to a stated target by
quarter 4; new payment methods live for a named merchant segment. Catalog area goals: customer-impacting
incidents down 30 percent with change volume held, and enterprise catalogs adopted by a stated number of
merchants. Each director's people goal: engagement or regretted attrition in the area, with a measure.
Shared goal for all three: group-wide availability of the checkout path at the target, or every area
off the deprecated deployment path by quarter 3.

**Criteria.** Outcomes with measures; at most three area goals; one identical shared goal; a counter
measure where a goal can be gamed. **Weak answer:** adding measures to the original outputs without a
shared goal.

## A1 — A green report and a late bet

**First, corroborate before confronting.** Nadia checks a second source: the bet's own milestones,
the onboarding team's board or lead time, and a conversation with the product lead for onboarding. She
asks Joaquín's managers in her skip-level conversations what is blocking them, without framing it as a
check on Joaquín. Keil and colleagues advise exactly this corroboration, and warn that aggressive
auditing breeds more misreporting.

**Then the conversation.** In the next operating review (or sooner, one-on-one), Nadia states what she
heard and from whom, asks Joaquín for his view, and listens for why the report was green: a stale
measure, optimism about recovery, or fear of what red would cost. She separates the problem (a late bet)
from the reporting (four months green). For the bet: a re-forecast with a range, and a decision on
scope or capacity. For the reporting: an agreement that amber is expected and will not be punished,
and a leading measure added to his scorecard.

**What she must not do.** Reward the late news with a public rebuke or a new audit regime, which teaches
every director to hide the next problem better.

**Criteria.** Corroboration, a private conversation before any escalation, separation of the delivery
problem from the reporting problem, and a structural fix to the scorecard. **Weak answer:** taking the
outside report at face value and reprimanding Joaquín, or ignoring it because the review says green.

## A2 — Selin's surplus

**The arithmetic.** Investable capacity: Checkout 29, Catalog and Search 32, Merchant Tools 37 (98).
Funded bets 1 to 5 land as 32, 20, and 44 (96), leaving gaps of −3, +12, and −7 and 2 FTE reserve.

- **Option (a), move a team of about 8 to Merchant Tools:** Catalog and Search 24 against 20 (+4),
  Merchant Tools 45 against 44 (+1), Checkout still −3, which the 4 spare and the reserve can cover by a
  work move. Cost: a team changes director and context (Chapter 36's transition cost), borne by that
  team and Selin.
- **Option (b), move work:** a Catalog and Search team builds the merchant-facing parts of bets 2 and 4;
  people stay. Cost: coordination across two directors, borne by both and by the bets' lead times.
- **Option (c), fund search relevance above bet 4:** Catalog and Search 34 against 32 (−2), Merchant
  Tools 28 against 37 (+9), Checkout −3; total funded 24 + 30 + 18 + 8 + 14 = 94. Cost: reporting
  version 2 is not built, borne by merchants and the sales team that wanted it, and Merchant Tools has
  idle capacity to redeploy.

**The response to Selin.** Acknowledge that search is hers to own, then separate ownership from funding:
an area owns its components, but the group funds bets by rank. If she believes search relevance ranks
above bet 4, the argument goes to the director team meeting with evidence of value, not to the
allocation by default.

**Criteria.** Correct arithmetic for each option, a named bearer of each cost, and a forum where all
directors hear the case. **Weak answer:** agreeing because the surplus "belongs" to her area.

## A3 — The unavailable director

**Test before acting.** Larson advises testing first impressions before acting on them. In the first
month the VP has three managers' reports and an area meeting its goals. Tests: what "unavailable and
slow" means in observable terms (decisions waiting, one-on-ones cancelled, response times); whether the
goals are being met because of the director or despite them (are managers deciding things above their
level?); and the director's own account, including load and context the managers may not see.

**Evidence that would justify a change.** Use the chapter's four kinds of evidence (outcomes and
system health, skip-level signals, managers' growth, peer conduct), and first rule out allocation and
boundary problems, though here the area is meeting its goals, so those are unlikely. Look for a
pattern across sources, not three anecdotes: decisions the
managers needed that waited weeks, a team health or engagement signal declining, a manager considering
leaving, and no change after clear, specific feedback with a date. Meeting goals does not settle it,
because a capable manager team can carry an absent director for a while, and that is precisely the
failure the VP must not let run for a year.

**Meanwhile.** Set written expectations (how the director will be judged, response times for decisions
the managers bring); agree a short-term fix such as a weekly decision slot; review in 60 days with a
decision date. Keep the managers' trust by not undermining the director publicly.

**Criteria.** Tested impressions, observable evidence, explicit expectations, a decision date.
**Weak answer:** replacing the director in month one on hearsay, or ignoring it because the numbers are
green.

## A4 — A director who undercuts a team decision

**First, check the facts.** A product lead's account is one source. Before acting, Nadia confirms two
things directly: what the director has been telling his product partners, and whether engineers in
his area are working on the delayed change. Both are observable in a day (ask the partners; look at
the area's board or recent merge requests). Acting on hearsay would teach the team that the VP
manages by rumor.

**The one-on-one, within the week.** If confirmed, name both behaviors and their cost without a
lecture: "We decided together to delay the API change. Telling your partners leadership overruled you
makes the other directors' commitments look optional, and staffing it anyway spends capacity the team
assigned elsewhere." Then restate the route: if he has new evidence that the delay is wrong, he brings
it to the next director team meeting and the decision can be reopened there. Ask what made him go
around the meeting; the answer may show that he felt unheard, or that the decision missed a cost his
area carries.

**Changes to the team's process.** Look for what made the side route attractive. Was the decision
recorded with its reason? Did the director state his objection in the room, and was it answered? If
not, tighten the practice: written options a day ahead, the decision and its reason in the log, and
an explicit question before closing ("does anyone not commit to this?"). Nadia does not announce the
incident to the team; she restates the norm for everyone at the next meeting.

**If it recurs,** it goes into the director's half-year assessment as evidence on peer conduct, which
the shared goal makes part of the job.

**Criteria.** A good answer verifies first, addresses the behavior privately and specifically,
separates the director's disagreement (legitimate, with a route) from the way he acted on it, and
checks whether the team's process invited it. The weak answers are to ignore it because the director
delivers, which tells every director that decisions are negotiable in private, or to reprimand him in
the meeting, which turns a norm into a public trial.

## X1 — Does Northstar need a VP in year 2?

Several recommendations are defensible; the quality is in the reasoning and its conditions.

**One worked recommendation: the director grows into the role, with triggers (options 2 and 4).**
Northstar has one director. A VP above that director would manage one person, the pass-through layer
the chapter warns against, and under the flat rule the seat costs one engineer (79 to 78, about 1.3
percent of the 79 engineers in the main proposal). The VP decisions that exist at Northstar (annual allocation with Amara Okafor, manager
staffing and the bench, the operating rhythm, engineering's input to year-2 planning) should be
delegated to the director in writing, which also gives Victor Lindqvist the time he wants for
technical strategy.

**Dependence on week 46.** If Victor approves the main proposal, the director's span of 10 is the real
risk; the recommendation should name the relief (staff engineers' mandates, a monthly operating review
per manager instead of weekly status, delegation of the portfolio forum's preparation). If he approves
alternative D, two managers of managers make the director's job VP-shaped already, at two seats. If
headcount growth is approved, the case for a second director, and then a VP, strengthens.

**Triggers to revisit.** Approved growth beyond about 100 engineers; a second director role; the
director's span above 10 for two quarters; or Victor's strategy work still crowded out after one half.

**Criteria.** Names the decisions, costs the seat, ties the answer to the open week-46 decision, and
states what would change it. **Weak answer:** "the board expects a VP", or "hire a VP to reduce the
director's load", which adds a layer above one person.

## X2 — Twenty seats across five VPs

**Process.** Each VP brings the same evidence: their group's bets beyond current capacity, sized and
ranked, with value estimates written by the product partner; run work as a share of capacity, measured;
and what they would stop if they received nothing. The CTO's staff merges all bets into one ranking
across groups before mapping to groups, to counter partition dependence (five groups otherwise receive
four seats each).

**Who is in the room.** All five VPs together, with product and finance partners, in one planning
session; the CTO decides contested ranks. Each VP hears the others' cases.

**Preventing private escalation.** State in advance that requests made outside the session will be
brought into it, and keep that promise the first time it is tested. Larson warns that if private
headcount escalations are rewarded, they become the real process and the joint plan a fiction. Record
the allocation, its reasoning, and its triggers in the decision log.

**Arithmetic check.** 20 seats on 500 engineers is 4 percent growth. If two VPs' top bets rank highest,
they may receive most of the 20; that outcome is legitimate if the ranking produced it in the room.

**Criteria.** One ranking before mapping, shared evidence, an open forum, a stated rule on private
requests, and triggers. **Weak answer:** four seats each, or most seats to the VPs who asked first.

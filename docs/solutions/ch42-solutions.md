# Chapter 42 solutions — Cross-Functional Dependencies, Portfolio Management, and Influence Without Authority

Worked solutions for the [chapter 42 exercises](../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Estimating time in progress and setting a limit

**Arithmetic.** Five finished in two quarters is about 0.83 a month (5 ÷ 6). With 11 in progress,
Little's law gives an average time in progress of 11 ÷ 0.83, about 13 months. Adding 4 more, if
throughput stays the same, raises it to 15 ÷ 0.83, about 18 months.

**A limit.** If sponsors can accept about four months from start to finish, the first estimate is
0.83 × 4, about 3 or 4 in progress. Propose 4, below today's 11, and say how the other 7 will be
ranked and when each could expect a slot.

**Assumptions to state.** The law relates averages over a stable period; this organization is not
stable (in-progress count rising). Throughput is assumed to hold, or rise, when fewer initiatives run;
that is the claim to test. Initiatives differ in size, so "one initiative" is a coarse unit.

**What to measure.** Initiatives finished per month, age of each in-progress initiative, and how many
initiatives each shared specialist or team is working on, for two months before and after.

**Weak answer:** treating 13 months as a forecast for any one initiative, or setting the limit at 11
"to start with", which never binds.

## F2 — Classifying influence tactics

1. **"The WIP policy doesn't allow it"** is legitimating: an appeal to rules. Yukl and Tracey found it
   among the least effective tactics. Expect the VP Sales to go around the director to someone who can
   change the policy.
2. **Asking the CPO which initiative she would pause** is consultation: inviting the target into the
   decision. Among the most effective tactics; it also puts the trade-off with the person who owns
   product ranking.
3. **Asking the CTO to tell sales to wait** is an upward appeal to authority combined with a coalition
   aimed at a peer. It may win the immediate decision, but the research associates both coalition and
   pressure-style tactics with low commitment, and the VP Sales will remember who went over his head.
4. **Showing the CFO the credits still being paid** is rational persuasion, in his terms. Most used
   upward and among the most effective.

**A strong answer** notes that the abstract-level findings concern commitment and effectiveness
ratings, not decision outcomes, and that the same act can be received differently (consultation that
is really a disguised verdict lands as pressure). **Weak answer:** labeling all four "influence" and
ranking them by personal taste.

## F3 — Sales engineers' direct requests

**Heroic version.** Data and Analytics engineers answer each message as it arrives; when two collide,
someone escalates to Farah Haddad or the director, who picks one. The engineers who answer fastest
become the sales team's default, and their planned work slips. Nothing shows in any report.

**Structural version.** One intake for sales data requests, with a named counterpart in sales
operations who triages and ranks them; a response target (for example, two working days to answer
"when"); a small reserved allowance in Data and Analytics for these requests, sized from the count; and
self-service for the most frequent request types.

**Evidence to collect first.** Fourteen requests in the quarter: their types, how long each took, who
answered, which planned items slipped, and how many deals each was tied to. Data and Analytics'
baseline already shows 12 points of capacity going to other teams' requests, so the pattern is not new.

**With Greg Tanaka**, lead with his interest: faster, more reliable answers for his sales engineers.
The intake is the offer, not a restriction. **Weak answer:** telling engineers to stop answering sales
messages, which removes the help without replacing it.

## A1 — The multi-currency slip

**Conversation with Greg first, before he hears it elsewhere.** State the slip, the cause (the one
Billing engineer who can change currency and rounding safely was pulled into an incident), the new
forecast as a range, and what is being done. Ask what the prospect actually needs by when; a revised
date given early with a credible plan may preserve the deal better than a promise to recover.

**Portfolio change.** Options: protect that engineer from incident response for the rest of the
initiative (with a named alternate for ledger incidents), accept the slip, or pause another initiative
that also needs Billing. Do not add people to the Billing part; the constraint is knowledge, not hours.

**The structural problem.** Currency and rounding knowledge is held by one person (1 of the Billing
ledger engineers can respond alone and change it safely). Any initiative touching it is hostage to
incidents. The fix is a knowledge-spreading plan (pairing a second engineer on this initiative is the
cheapest one) and a portfolio rule that no two concurrent initiatives depend on the same single expert.

**Weak answer:** promising to "recover the two weeks", or treating the incident as bad luck rather than
a predictable consequence of a single point of knowledge.

## A2 — Sofia Alvarez's escalation bypass

**Her interests.** Fewer escalations reaching customers unanswered; credibility with the customers her
team faces; honest status during incidents. Her request is a position; the interest is a guaranteed
fast path when it really matters.

**What you can accept.** A severity-based escalation intake with response targets, consistent with
the severity definitions she co-wrote; a defined expedite class for customer-impacting defects, capped
and reported monthly; a named engineering counterpart for customer success.

**What you cannot accept.** A bypass into "any team's work" without triage: it is an uncapped expedite
right, and Chapter 16 shows expedites raise everyone's work in progress and unplanned share.

**Evidence.** Escalations by kind over the last two quarters, how many were Sev1 or Sev2 under the
definitions, how quickly each was answered, and the expedited share of unplanned work (12 percent of
the baseline total).

**Tactic.** Consultation: ask her to co-design the expedite class. **Weak answer:** a flat no citing the
intake policy.

## A3 — Interest map for Rajiv Menon

**Position on the swap.** Likely to oppose moving service-credit statements to quarter 4 if credits are
still being paid; indifferent if they are not.

**Interests.** Flat operating expense, credits stopping, predictable spending he can explain to the
board, and an answer to his open request for a measure of engineering output.

**Evidence he trusts.** Dollars: credits paid this year against last, cost of the initiative
(50 engineer-weeks at the planning rate of $3,558 per engineer-week, $185,000 a year ÷ 52, is about $178,000),
the revenue at stake in the prospect, and the risk to the multi-currency deal date.

**What to offer.** Early, unvarnished information before the forum; a clear statement of what the swap
costs his priority; capacity reporting by category in his terms. **What not to offer:** a trade on his
output-per-engineer request ("support the swap and we'll give you the figure"), which mixes a
measurement decision with a portfolio decision.

**Why exchange is poor here.** Yukl and Tracey found exchange ineffective with superiors, and Rajiv,
though not the director's manager, is an executive above the director's level. Rational persuasion in
finance's terms is the tactic that fits.

## X1 — The week 34 forum decision

**One defensible recommendation: option 1, queue it,** with the scoping sessions and a forecast range of
weeks 44 to 47 for Greg to give the prospect.

**Options and costs.** (1) Queue: no displacement; approval rules finish around weeks 44 to 47; cost
borne by Greg's prospect, which waits. (2) Swap: about one week earlier; service-credit statements
(50 engineer-weeks) move to quarter 4; cost borne by Rajiv and by customers receiving credits.
(3) Break the limit: no earlier finish expected, Orders on three cross-team initiatives, risk to the
multi-currency date already in an open deal; cost borne by Greg's other deal and the limit's
credibility.

**What would change it.** Option 2 becomes defensible if credits are no longer being paid (low cost of
delay for statements) and the prospect's decision truly depends on a week. Option 3 is defensible only
if the prospect's value dwarfs everything else and another cross-team initiative can be paused.

**Criteria for a good answer:** costs in engineer-weeks and dates, a named bearer for each, a
recommendation, and a revisit trigger. Several answers are defensible; an answer that chooses option 2
with Rajiv's agreement is strong. **Weak answer:** recommending option 3 because the deal is large,
without addressing the open deal it puts at risk.

## X2 — Explaining the limit to the CEO

**The explanation.** Engineering finishes about one cross-team initiative a month. With three in
progress, each takes about three months; with ten, about ten. Starting all ten would not deliver more;
it would deliver everything later. The baseline quarter is the evidence: nine cross-team items
committed together, one delivered.

**The risk of raising the limit.** Shared constraints (the currency and rounding expert, Platform
Operations, Billing) would be split further; committed dates in open deals would slip; and the
organization would return to commitments with an 11 percent record.

**What to offer.** The ranked waiting line with expected start dates and costs of delay, so the
executive team chooses the order; a monthly forum where any executive can propose a swap at a stated
cost; a small reserved allowance for urgent single-team deal and escalation work; and a review of the
limit at quarter end against throughput, so it is a tested setting, not a dogma.

**Criteria:** arithmetic with stated assumptions, an honest account of what the limit costs, and an
offer that gives the CEO control of the order. **Weak answer:** defending the limit as engineering
best practice, which is legitimating and invites the CEO to overrule it.

# Chapter 11 solutions — High Performance: Trust, Psychological Safety, and Accountability

Worked solutions for the [chapter 11 exercises](../parts/03-high-performing-teams/11-high-performance-trust-safety-and-accountability.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Three claims about safety

**"Nobody has been fired for an outage in five years."** This is evidence about one severe
consequence, not about safety. Safety concerns the perceived interpersonal risk of speaking: being
embarrassed, ignored, or quietly sidelined counts as much as being fired. A team can fire nobody and
still mock the person whose change broke production.

**"We never argue in meetings."** This is weak evidence, and possibly evidence against. Months
without disagreement in design discussions usually mean disagreement has become costly, or no real
decisions are being made.

**"We don't do deadlines because they stress people out."** This confuses interpersonal risk with
performance risk. Removing commitments removes accountability, not fear; it describes a comfortable
team, not a safe one.

**Evidence to ask for:** near misses recorded last quarter and who wrote them; the share of incidents
found by customers; the last time someone told the lead a decision of theirs was wrong and what
happened; how commitments are made and whether slips are announced early.

A good answer treats each claim separately and asks for behavior. The weak answer accepts the first
claim as proof of safety, or rejects the third because "deadlines are always good", without
distinguishing an agreed commitment from an imposed date.

## F2 — Classifying four teams

**(a) Fearful (low safety, accountability present).** Green dashboards with customers finding the
outages suggest information is not flowing upward. The observation that would change it: whether
engineers knew about the risks beforehand. If nobody could have known, the problem may be detection
(weak alerting) rather than safety, and the team may be closer to coasting or simply under-instrumented.

**(b) Comfortable (high safety, low accountability).** Candid retrospectives with an action list that
never shrinks is the signature. The deciding observation: whether the actions have named owners and
dates. If they do and still lapse, accountability is the problem; if they have no owners, the system
never asked for accountability.

**(c) Learning (high on both).** Logged near misses and early renegotiation are the two best
behavioral signals. Check sustainability before declaring it a model: after-hours load and whether
one person carries the review or on-call burden.

**(d) Coasting, or a team without mandate.** Doing only what is assigned can reflect low engagement or
a manager who takes every decision. Ask whether proposals were ever accepted; Chapter 2's
super-engineer pattern produces this behavior without anyone being disengaged.

A good answer names a disconfirming observation for each; the weak answer labels without saying what
would change the label.

## F3 — "Google proved it"

**The first sentence overstates three ways.** Project Aristotle is a company report on 180 teams,
not a peer-reviewed study, and the re:Work guide lists five dynamics, with dependability (reliable,
on-time quality work) second, so it does not support safety as a substitute for accountability.
Edmondson (1999) studied 51 teams in one manufacturing company and found safety associated with
learning behavior, which mediated its association with performance: correlational and outside software. Lenberg and Feldt found, in 38 software teams with self-assessed
performance, that norm clarity was a stronger predictor than safety. None of this is "proof", and
"number one driver" is a causal claim no cited study makes.

**The plan is worse than the sentence.** Safety surveys measure perceptions reported by the people
whose manager is rewarded for the result. Tying a bonus to the score invites managers to signal the
desired answer and teams to give it, destroying the instrument. It also rewards one dial and ignores
the other.

A better plan uses survey results diagnostically (Chapter 14), tracks behavioral signals, and develops
managers' reactions to bad news. The weak answer debates the evidence and accepts the bonus, or
rejects the evidence wholesale and concludes safety does not matter.

## A1 — Should Orders copy the operations review?

**Recommendation:** yes to the outcomes, not first to the meeting. Sequence:

1. **Weeks 1 to 2, no new meeting.** Priya asks each of Orders' senior engineers privately for one
   decision she should have made differently and acts visibly on at least one. This tests the
   specific weakness (candor toward the manager) at almost no cost.
2. **Week 3.** Start the near-miss log; it costs minutes per entry. Move every open follow-up action
   from Priya's name to an engineer's, with an agreed date.
3. **Week 4 onward.** A 30-minute weekly review run by a rotating engineer, agenda chosen by the team,
   possibly folded into an existing ceremony to cut the eight hours a week.

**Measure after a quarter:** near misses logged and by whom; risks to the bulk-ordering date raised
before the checkpoint rather than at it; follow-up actions closed; whether any engineer has
disagreed with Priya in a team setting.

**Change course if** the log stays empty after six weeks (the ritual is not producing candor; return
to the manager's behavior) or if the review becomes a status meeting Priya runs.

The bulk-ordering deadline argues for low-cost steps first, not for postponing; a team that hides
risk is the larger threat to the date. The weak answer copies Elena's ritual wholesale, or refuses it
because of the deadline without addressing the safety gap.

## A2 — The strong engineer who misses commitments

**Where:** in private, between Elena and the engineer, not in the operations review. The review is
for the system; a repeated individual pattern is a management conversation. Raising it in the review
would teach the team that the review is where people get named.

**What is said:** the specific pattern (three commitments in two months, none flagged in advance),
its effect on the team, and the expectation, which is early renegotiation rather than never missing.
Then ask what is happening: overload, unclear scope, a personal matter, or disagreement with the
commitments. The answer decides the response; a capacity problem is a system fix.

**What the team should see:** not the conversation, but its result: the engineer's next commitments
renegotiated early, and the team's norm restated in general terms ("a slip announced early is fine;
a late surprise is not"). Elena should also tell the tech lead that raising it was right and that it
is being handled.

**Why this preserves safety:** safety governs how people are treated when they speak; the engineer's
missed commitments are performance, not speech. Ignoring them would turn the team comfortable. If the
pattern continues, it enters performance management (Chapter 9).

The weak answer either leaves it alone "to protect the culture" or raises it in the review.

## A3 — Inheriting a fearful team

**Days 1 to 15: change your reactions, not their process.** Stop the public naming at once and say so
explicitly to the team. In each first one-on-one, ask what nearly went wrong recently, and respond
to the first piece of bad news with thanks and a question about what the person needs.

**Days 15 to 30: make the system the subject.** Re-read the last two customer-found incidents with
the team, asking what made them possible rather than who. Start a near-miss log, and write the first
entry yourself about a mistake of your own.

**Days 30 to 60: rebuild accountability on new terms.** Commitments with owners and agreed dates,
early renegotiation explicitly welcomed, follow-up actions owned by engineers.

**Leave alone:** whatever produces the low change failure rate, until you know whether it is
discipline or under-reporting.

**Expected order of signals:** first, private disclosures in one-on-ones; then near-miss entries,
usually from the most senior or newest engineers; then earlier risk reports on commitments; last,
fewer customer-found incidents, which may take more than a quarter. The change failure rate may
**rise** at first as failures previously hidden get linked to releases. Warn your manager that this
is a sign of honesty, not decline.

The weak answer runs a safety workshop in week 1 or measures success by the change failure rate.

## X1 — Bonuses tied to incident counts

**Do not support it as proposed.** Helena Marsh (CEO) wants accountability; at Northstar, severity is assigned by people, and the first quarter
already saw four consecutive incidents rated Sev3 in week 7, one of them a two-hour payment delay for
nine customers. A bonus tied to the count rewards exactly that reclassification, and rewards teams for
not declaring incidents at all. Under-reporting is the outcome the organization can least afford:
47 percent of baseline incidents were found by customers.

**What it would do:** severity debates turn into pay negotiations; near misses and early warnings drop;
the managers of teams that own dependency-heavy components (three of Payments and Integrations' six
incidents were third-party) are penalized for what they do not control.

**What to propose instead:** accountability for the system and follow-through, which Chapter 27
defines: each manager answers for operational minimums on their components, closure of the
follow-up actions they own, and recurrence by broad category. Severity is audited independently, as
the director did from week 7. Report the incident count to the CEO as an organization outcome, not a
manager score.

**What to say to Helena Marsh:** she is right that managers should answer for reliability; the
question is which measure survives being paid on. The weak answer accepts the bonus "with
safeguards" without naming the reclassification incentive.

## X2 — Mandating Elena's review everywhere

Victor Lindqvist (CTO) is right that the practice works; the question is what to mandate.

**Standardize the outcomes, not the ritual.** Every team, from next quarter: a near-miss record anyone
can write in; every follow-up action and commitment with one owner and an agreed date; a weekly
point at which at-risk commitments and open actions are reviewed by the team. How each team does it
is its own choice: a separate meeting, a part of an existing ceremony, or an asynchronous review.

**Why not the same agenda:** Elena's review works partly because her team chose it and runs it.
Imposed, it becomes a status meeting held for the director. Teams differ: Data and Analytics has
little operational load; Billing's on-call burden needs a different agenda.

**Cost:** a 30-minute weekly meeting for 80 engineers is 40 engineer-hours a week, about one full-time
engineer, roughly $185,000 a year at Northstar's cost. Folding it into existing ceremonies cuts most
of that, which is another reason not to mandate a new meeting.

**How to know within two quarters:** per team, near misses recorded (rising first), commitments
renegotiated before rather than at the deadline, follow-up action closure, recurrences by category,
and customer-detected share. Watch for gaming: near-miss logs padded with trivia, or reviews held but
not run by the team.

**What to tell Victor:** the practice is worth spreading; the mandate should be on what the practice
achieves. The weak answer either mandates the exact agenda or leaves it entirely optional with no
expected outcome.

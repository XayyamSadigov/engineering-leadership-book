# Chapter 9 solutions — Performance Management and Underperformance

Worked solutions for the [chapter 9 exercises](../parts/02-people-management/09-performance-management-and-underperformance.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Four missed commitments

**The new joiner.** Most likely skill and context, possibly an unclear expectation: three months is
short for a complex codebase, and asking many questions is evidence of effort. Confirm by pairing on
one task and seeing whether the work improves quickly. Change your mind if peers who joined at the same
time with the same onboarding deliver comfortably and the questions repeat without learning.

**The engineer on the new rotation.** Most likely a system cause. The timing is the evidence: the gap
started when the load changed. Confirm by measuring their on-call hours against peers and against the
plan's assumptions. Change your mind if peers on the same rotation deliver normally.

**The engineer who reviews well and lets implementation drift.** Selective effort suggests will, or a
role-fit question (they may be heading toward a design-heavy role). Confirm in a direct conversation
about what they want. Change your mind if implementation drifts for a reason they can name, such as
being pulled into every review.

**The backend engineer on mobile.** Role fit, with a skill component. Confirm by asking whether they
chose the move and how they performed before it. A good answer notes that more than one cause can
apply to each engineer. The weak answer assigns a cause from the description alone without naming
evidence that could disprove it.

## F2 — Rewriting the expectations

A rewrite is good if someone who does not know the person could check it at week 8.

- **"Show more ownership"** becomes: "For the two services you own, every alert in the period has an
  acknowledged response and a follow-up item within two working days; you present one improvement
  proposal for each at the team review by week 6." Support: the manager clears one day a week of other
  work and attends the review.
- **"Communicate better with stakeholders"** becomes: "For your current project, a written status
  goes to the product manager every Friday, including risks, and any date change is raised within one
  working day of your knowing it." Support: a template and one example from a peer.
- **"Improve code quality"** becomes: "Your merge requests pass CI on the first run in at least four
  of five cases, and review comments of the 'missing tests' kind fall to none in the last four weeks."
  Support: pairing with a senior engineer for two sessions a week for three weeks.
- **"Be a team player"** must be grounded in behavior: "Reviews assigned to you are completed within
  one working day; you take your share of the interrupt rotation without swaps unless agreed."

The weak answer replaces adjectives with other adjectives ("demonstrate proactive ownership") or with
raw counts (number of commits), which Chapter 18 rejects as performance measures.

## F3 — Ranking by last year's ratings

The ratings cannot support a fine-grained ranking. Scullen, Mount, and Goff found that in their data
idiosyncratic rater effects accounted for 62 and 53 percent of rating variance and the ratees' actual
performance for 21 and 25 percent. Their ratings were developmental ratings of managers, so the numbers
do not transfer exactly, but the direction is a warning: a rating given by one manager tells you a good
deal about that manager. On a single-rater team, everyone shares the same rater, which removes
between-rater differences but not the rater's idiosyncratic view of each person, and a coarse scale
compresses most people into one or two bands, so a "ranking" would mostly break ties by noise.

The ratings can support a coarse statement: someone rated below expectations with documented examples
is a weak candidate for a reward. A better basis for conference places is the purpose of the places:
who would learn something they will bring back, who has a talk accepted, who is moving into a new area.
Ask people to propose themselves with a short reason, and rotate across the year. The weak answer
either accepts the ratings as objective or rejects all evidence and allocates by seniority.

## F4 — A review for a strong performer

**One worked outline.**

| Part | Content |
|---|---|
| What she did | Led the migration that removed the weekly manual step (state the hours or errors it saved, from the record); mentored a new hire to independence (name the milestone, such as first on-call shift alone); raised two design risks that other teams then fixed (name them and the effect) |
| How, by ladder dimension | Delivery and ownership: carried the migration end to end. Influence and growth of others: the mentoring and the cross-team risk calls. One honest development point, for example that the risk calls came as review comments rather than as a proposal she led |
| Growth | The cross-team design goal is not met. Say so plainly, and say whose part it was: if no such design was available, the gap is partly the manager's |
| Next period | Lead one named cross-team design through review by another team; continue mentoring. Your commitments: assign the design, find a sponsor in the other team, check at three months |

**Criteria for a good answer.** Every outcome has evidence and an effect, not adjectives. The unmet
goal is stated without hedging and without implying a performance problem. The next period names a
specific opportunity and what the manager will do to create it, which is the sponsorship half of the
review. Nothing in it is new to her.

**The weak answer** is all praise ("excellent year, keep it up"), which tells a strong performer that
nobody is thinking about her growth, or one that treats the missed growth goal as a criticism of her
when the opportunity was never offered.

## A1 — Tom's first conversation with Bram

**What to say about the gap.** Specific facts, with dates: requests aging past the team's normal
response time, the Jenkins upgrade postponed three times. The impact: two colleagues have been picking
up his work. Say it plainly: this is serious and it has to change.

**What to say about your own part.** Tom has two things to own: he moved tickets without telling Bram
why, and he wrote "meets expectations" four months ago. Saying so is not a concession; it is the only
way the conversation is credible and it removes the "why didn't you tell me" objection before it is
raised.

**What to learn.** Ask what is going on, and listen for each cause: where his time goes (which
leads to the interrupt reconstruction), what he finds hard (GitLab CI), what changed (the shelved
consolidation), and anything personal that he chooses to share. Agree to reconstruct his time
together before deciding anything.

**What not to commit to.** No promise that nothing formal will follow, no promise to revive the
consolidation project, no specific plan yet. A good answer separates the facts from Tom's
interpretation ("checked out"), which should not be said. The weak answer either opens with a formal
plan, or is so gentle that Bram leaves without knowing there is a problem.

## A2 — The QA engineer in Billing

**Diagnosis.** This is first a role-fit and skill question created by the organization. The engineer
did the manual regression role well for years; the move in week 10 changed the role to one that
rewards automation skill, and only five of the seven QA engineers automated cases during the
transition; this engineer was not one of them. Check the system too: flaky tests may come from the shared Core test database
rather than from the engineer, and Billing's unplanned share was 41 percent at baseline.

**Response.** Marcus should stop the routing-around immediately and talk to the engineer directly. Then
offer a real development path: pairing with an experienced automation engineer, a narrow first
automation scope, and an explicit timeline (one quarter). At the same time, make the valued work
official: exploratory test charters were one of the outcomes of the manual-suite triage, and that
work can be a recognized part of the role.

**What the organization owes.** Northstar's standing rule (the fifth of its five constraints) says any
plan that changes the QA engineers' work must say what they do next. The organization changed this person's role; it owes training time
and patience before any formal process. A formal plan only follows if, after real support, the
engineer neither develops the skill nor accepts a reshaped role. The weak answer treats the struggle
as an individual performance problem from the start.

## A3 — Week 6 of Bram's agreement

**Reading the evidence.** Three of the expectations are met or on track (acknowledgment, runbook,
upgrade planned) and one is partly met (two-day answers about 70 percent). The trend matters more
than the snapshot: if the answer rate was low at week 2 and has risen each week, the plan is working;
check whether the misses are concentrated in GitLab CI tickets, which would point to the remaining
skill gap. The upgrade slip needs a reason: if a Core incident consumed the planned days, that is a
system cause; if it slipped without notice, that is the old pattern.

**At week 8.** If the trend continues and the upgrade is done, close the agreement and say so, with a
light check at week 12. If the answer rate is still around 70 percent but rising and the gap is specific,
one extension of four weeks with that single expectation is defensible. If the upgrade slips again
silently, move to a formal plan with HR.

**To the colleague.** Do not discuss Bram's plan. Say that the situation is being addressed, that the
reassignments have stopped, and thank them for the work they absorbed, which should also be recognized
in their own review. Acknowledge that Tom let it go on too long. The weak answer either shares details
or dismisses the fairness concern.

## X1 — Forced distribution under flat headcount

**Recommendation.** Do not adopt a permanent annual cull.

**The strongest case for it.** Scullen, Bergey, and Aiman-Smith's simulation found that a forced
distribution system with firing could noticeably improve average workforce potential. If the audit in
exercise X2 is right, Northstar's reviews are inflated, so some forcing mechanism
would make managers act.

**Why not.** The same simulation found that most of the improvement comes in the first several years,
and that it depends on how many are fired and on voluntary turnover. Northstar's attrition was 10
percent with a median of 15 weeks from resignation to replacement's first day. Exiting another 8
engineers a year would roughly double the vacancy load, and under flat headcount each vacancy is lost
capacity for months. The simulation models workforce potential, not cooperation; Northstar's problems
(shared modules nobody owns, cross-team items missing their quarter) need more cooperation, not
competition. And the ranking would rest on single-manager ratings with large rater effects.

**Instead.** Calibrated reviews with examples, managers trained and expected to act within weeks, the
diagnosis note for every formal plan, and a one-time review of everyone described as struggling.
Measure: plans started, their outcomes, time from first concern to decision, and regretted attrition.
Each can be gamed (plans started late, outcomes recorded generously), so the director samples cases.

## X2 — Fixing an inflated review system

**Diagnosis.** Six struggling engineers and zero below-expectations ratings means the problem is
mostly in the system: managers have no tools, no support, and no expectation that they act, and an
honest rating would single them out.

**Quarter 1 of the change.** Leave the scale alone. Ask each manager to write, for each of the six, the
one-paragraph gap statement from the Practical Playbook, then run the diagnosis order with the
director and HR. Expect system causes in some cases (Platform Operations' interrupt load, the QA role
change), and fix those first. Train the six managers on the improvement process, with one worked case.

**Quarter 2.** Introduce a ratings calibration with examples: each rating comes with two pieces of
evidence, and managers review each other's ratings in a structured meeting. At baseline Northstar
calibrated nothing; keep this process separate from the promotion calibration Chapter 8 describes, or
run it alongside that one once it exists, so that ratings and promotions are not decided in one meeting. Publish the distribution to managers but
set no quota.

**Avoiding overcorrection.** No target share below expectations; a quota would turn a measurement
correction into forced distribution. Watch for a sudden spike of formal plans with weak diagnosis
notes.

**Cost.** About two hours per manager per struggling engineer in quarter 1, two days of calibration per
cycle across managers and director, HR time, and some attrition, which is part of the point. The weak
answer imposes a distribution or a ratings rewrite without changing what managers do every week.

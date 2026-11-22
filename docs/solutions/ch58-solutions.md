# Chapter 58 solutions — Layoffs, Reductions, and Mergers and Acquisitions

Worked solutions for the [chapter 58 exercises](../parts/13-advanced-problems/58-layoffs-reductions-and-mergers.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional, and nothing here is legal advice: every real reduction needs employment counsel for each
jurisdiction involved.

## F1 — Why a spread cut fails Field Operations

**What the proposal cuts.** Fifteen percent of each team, rounded: Dispatch 38 × 0.15 = 5.7, about 6
(38 to 32); Mobile Workforce 40 × 0.15 = 6 (40 to 34); Classic Scheduler 32 × 0.15 = 4.8, about 5 (32 to
27). Total 17.

**What survives.** Every commitment. Classic Scheduler keeps 27 engineers and, unless someone decides
otherwise, its feature roadmap, which the strategy has just ended. Dispatch, the product the strategy
depends on, loses 6 engineers in the same quarter it starts receiving Classic's customers. The group is
smaller, still doing everything, and weakest exactly where load will rise.

**The reply.** "The executive decision is to stop new development on Classic Scheduler and move its
customers to Dispatch. A cut of 15 percent in every team keeps 27 engineers on a product we have decided
not to grow and removes 6 from the product that will receive its customers. I propose instead to start
from the work that stops. Classic's remaining work (security, operations of three tier 1 components,
escalations, and migration tooling) needs about 14 engineers. That removes 18 Classic roles; four
affected people can fill approved vacancies in Dispatch and Mobile Workforce, so 14 engineers leave. The
annual saving is about $2.8 million, roughly 80 percent of what 17 separations would remove (about $3.5 million
at Halvard's average of about $205,800 an engineer, $102.9 million ÷ 500). The gap is the price of not weakening Dispatch, and the four
filled vacancies avoid hiring cost the plan does not count. Dispatch is not weakened while it absorbs
the migration."

**Criteria.** A good answer does the arithmetic, names the commitments that would survive, and connects
the cut to the strategy. The weak answer argues that across-the-board cuts are "unfair" without showing
what they do to the work.

## F2 — A repeatable ownership check

**Procedure.**

1. **Inventory.** Export every production component the group owns from the component register, with tier.
2. **Change history.** For each component, list every person with a merged change in the last 12 months
   (repository history, including configuration and infrastructure repositories).
3. **Operational history.** List every person who responded to a page or incident for the component in the
   last two quarters (paging tool and incident records).
4. **Covered.** A component is covered if at least one person who remains appears in step 2 or step 3; a
   tier 1 component needs at least two remaining people, at least one from each list.
5. **Review.** The owning director and a principal engineer from outside the team review the result, because
   the team's own manager drew up the draft list.
6. **Gaps.** For each gap: change a selection if the selection criteria allow it (component history is
   already a criterion), or fund a paid transition with a named recipient and a review of the handover
   material; recheck after every change.

**Satisfied on paper while the knowledge is lost.** A remaining engineer has one trivial change on the
component, a version bump made by a bot under their name, so the component counts as covered. A pairing
check catches it: ask the named person to explain the component's last incident or to make a small
change with nobody's help before notification day, or at least list what they have actually done on it.

**Criteria.** Data sources named, a threshold that is stricter for tier 1, an outside reviewer, and a loop
back into selection. The weak answer says "ask managers who knows what", which is how the five gaps were
missed in the first draft.

## F3 — The notification-day sequence

| When | What | Who |
|---|---|---|
| Day -1, afternoon | Managers of affected people briefed: names, criteria, severance terms, scripts, questions they may and may not answer | Imani Okonkwo, Leah Marchetti, counsel |
| Day -1, evening | Calendar invitations sent to affected people for 15-minute meetings the next morning, with neutral titles; no other change | HR |
| Day 0, 08:30–10:30 | Individual conversations: the person's own manager with HR present, in person or by video; written terms handed over; questions answered | Managers, HR |
| Day 0, after each conversation | Access changes for that person, never before | IT, triggered by HR |
| Day 0, 11:00 | Field Operations meeting: the reason, the work that stops, the criteria, the numbers, whether more rounds are planned, what happens to Classic's customers | Imani Okonkwo with all three directors |
| Day 0, 11:30 | Written note to the group, then the CTO's short company note | Imani, Halvard's CTO |
| Day 0, afternoon | Team meetings with each manager; the new ownership map shared in draft | Managers |
| Days 1–10 | Skip-levels with every team; final ownership map; Classic roadmap closed and open customer requests answered | Imani, directors |

The EU site follows its own timeline after consultation, and the plan says so in the group meeting rather
than pretending that site is decided.

**The step that matters most.** Access before conversation. An affected person who discovers the news
through a failed login learns that the company valued process over them, and survivors who hear that
story conclude the same about themselves. Every other mistake on the day can be explained; that one is
remembered.

**Criteria.** Affected people hear first and individually, access follows conversations, the most senior
leader speaks the same morning, and the plan covers the following week. The weak answer sends a company
email at 09:00 and holds conversations afterwards.

## A1 — Tobias Engel and the sustaining team

**What he says.** In the first week, a meeting with the eleven remaining engineers in which Tobias states
plainly what the team's mandate is, for how long, and how the departures change the plan. He does not
promise "no more changes"; he says what he knows and what he will say when he knows more. This addresses
the insecurity findings (Sverke et al.; de Jong et al.) and the explanation finding (Brockner et al.,
1990): uncertainty is high and the decision matters to them, which is where clear explanation has the
most effect.

**What he changes.** He asks Imani for a written three-year mandate for the sustaining team and a named role
in the migration, so the team is visibly part of the strategy rather than its leftover. He fills the three
vacancies by internal transfer from Dispatch, choosing people who will receive the migrated customers, which
builds a bridge between the two teams. He rebalances the on-call rotation immediately, because eleven people
covering three tier 1 components is the operational risk most likely to cause the next departure.

**What he measures.** Weekly: on-call pages per person, incidents on Classic components, and progress on the
migration tooling. Monthly: a two-question pulse (do you understand the team's mandate; do you expect to be
here in six months). He asks Imani for the result of the reduction's two-quarter review to be shared with the
team.

**Criteria.** Each action is tied to a finding, the operational risk is handled first, and nothing is
promised that Tobias cannot keep. The weak answer is a morale event or retention bonuses alone; Trevor and
Nyberg's moderators point to embedding and procedural fairness, not to money by itself.

## A2 — An allegation that selection was retaliatory

**The next 48 hours.** Thank the engineer, say you will take it seriously, and do not argue the decision or
disclose any individual's circumstances. Write down what was said. Tell Leah Marchetti and, through her,
counsel the same day; an allegation of retaliation is a legal matter as well as a trust matter, and the
engineering leader should not investigate it alone. Do not contact the separated engineers yourself.

**The next month.** HR and counsel review the selection record for the two people against the written
criteria: which sustaining roles they were considered for, the skill and component-history evidence, and
the performance records used. If the record shows the criteria were applied as written, the review
documents that. If it shows a manager's judgment that the criteria do not support, the company has a problem
that it must address with counsel, possibly including the affected people.

**What you say to the engineer.** "I've passed this to HR and legal, because if it were true it would be
serious, and they can review the record properly. I can't discuss individuals, but the criteria were written
before names were discussed and are on the internal page. If you see anything else that worries you, come to
me or to Leah." Then follow up when the review closes, saying that it was done, without details.

**Criteria.** Escalation to HR and counsel, no private investigation, no disclosure, no dismissal of the
concern, and a follow-up. The weak answer reassures the engineer that "the process was fair" before anyone
has checked, which is exactly how survivors learn that raising concerns is pointless.

## A3 — Leveling without the acquired leader

**Consequences.** Seven key engineers placed at Senior, some below people they used to lead, lose status and
centrality in the combined firm, the condition under which Paruchuri and colleagues report the largest
productivity losses. Over the first quarter, expect the strongest of them to start looking elsewhere; the
market knows what they did. Corvane's on-call rotation of eight depends heavily on those seven; one or two
departures would leave its two tier 1 services with a rotation too thin to sustain, just as Halvard's Sev1
policy starts applying. The thesis assumption about embedding the engine in Reporting by month 6 depends on
the same people, because six of the eleven services have a truck factor of 1 or 2 concentrated in them. By the
second quarter the deal could have bought a codebase without the people who can change it.

**The calibration rule.** "Acquired engineers are leveled in a calibration that includes the acquired company's
technical leader, using evidence of what each person actually did (code reviewed, incidents led, systems
designed), within 60 days of close. Any placement below the person's previous scope is reviewed by the
receiving VP before it is communicated, and comes with a written development plan and a review date."

**Criteria.** The answer links leveling to status loss, to the on-call rotation, and to the thesis, and the rule
includes the acquired leader and evidence. The weak answer treats ladder consistency as the overriding value
without pricing the people it would lose.

## X1 — A hypothetical board request at Northstar

This is a scenario for the reader; no reduction is part of the Northstar canon, and the quarter 4 decisions stay
open.

**The arithmetic.** The base is the canon's FY2 personnel draft, $16.73 million at 87 full seats (not the year 1
figure of $16.1 million). Ten percent is about $1.67 million; at $185,000 a seat, that is 9.0 seats. The 87-seat
organization would become 78.

**Whether a reduction is the right tool.** Victor's first step is to ask what the board wants to stop. Northstar's
reliability is a commercial property written into contracts, six of the 40 largest customers renew in quarters 5
to 8, and the draft board page proposes Sev1 and Sev2 targets with prevention funded at flat headcount. A
nine-seat cut taken without stopping work would land on the prevention allocation first, because it is the only
capacity not tied to a customer date.

**Which work would stop.** Victor would present options framed as work, for example: stopping or deferring named
roadmap commitments (which needs Amara Okafor and Greg Tanaka in the room), reducing the quality continuation from
6 FTE to fewer (which changes the stage 2 gate in the open continuation proposal), or not backfilling departures
(which interacts with the open workforce plan options). Each option shows its effect on the open decision without
choosing it.

**The ownership check.** It would have to cover every tier 1 component and especially Billing, where three people
carry most pages, and the components the staff engineers know best. A cut that removed any of those people would
break the continuity the year's work has built.

**What he would need to believe.** That revenue or margin pressure is real and not answerable by the vacancy and
vendor options in the workforce plan; that the work that stops is worth less than its cost; and that the remaining
organization can hold reliability through the renewals.

**Criteria.** Correct arithmetic, the request reframed as work, links to the open decisions without deciding them,
and the ownership check named. The weak answer picks nine names or a percentage per team.

## X2 — A second acquisition planned as full absorption

**What the CTO requires before supporting it.**

1. **A written thesis** with the assumptions that must hold, including what the overlap with Forecasting means:
   which product survives for which customers.
2. **An integration plan by dimension.** Absorption may be right for the product if the acquired product replaces
   part of Forecasting's roadmap, but the plan must say how much autonomy the acquired engineers need to keep
   their capability, and the research on early structural integration and status loss argues against absorbing
   people, product, platform, and policy all in one quarter.
3. **The Forecasting engineers.** About a third of Forecasting's roadmap overlaps. The plan must say what those
   engineers will do: move to the acquired product, take other Insights work, or face a reduction. If a reduction
   is possible, it must be planned with this chapter's method and costed in the deal, and the company must not let
   rumors run for months.
4. **The costs in the deal model.** Platform migration, duplicated tooling until it is done, retention arrangements
   for key people, severance if any, and the attrition likely in both Forecasting and the acquired team.
5. **A review of the Corvane outcome.** What the preserve approach cost and bought is the company's own evidence.

**When to oppose.** If the thesis depends on "savings early" that come only from cutting Forecasting engineers
whose work the deal makes redundant, the deal is a reduction with a purchase price attached and should be judged
as one. If the integration cost was not in the price, the CTO says so in the decision record, given that
engineering usually has one vote, not a veto.

**Criteria.** Thesis, per-dimension plan, a decision about the overlapping people, full costs, and a stated
condition for opposition. The weak answer supports or opposes the deal on instinct, or accepts "absorb in a quarter"
without asking what it destroys.

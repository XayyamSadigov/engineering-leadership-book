# Chapter 46 solutions — Stakeholder Management and Negotiation

Worked solutions for the [chapter 46 exercises](../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Two grids, moving positions

**Year-2 reliability commitment.** Players: Victor Lindqvist (owns the ask), Amara Okafor (the price
may fall on her roadmap). Context setter: Rajiv Menon (high power, low interest unless cost or capacity
moves). Subject: Sofia Alvarez (high interest in honest severity, little power over the target). Crowd:
Greg Tanaka. Subjects: the six managers.

**Capacity split between product and prevention.** Players: Amara, Victor, and now Rajiv, because the
split is how he reads whether the money goes to the right places (Chapter 18's request and Chapter 38's
reporting question). Greg moves from crowd to player or strong subject, because deal features come out
of product capacity. The managers remain subjects, but with sharper interests: Marcus Oyelaran's
prevention share is at stake.

**What changes in engagement.** Rajiv gets a one-to-one before the capacity decision, not a briefing
after it. Greg is consulted on which deal work would move, not told afterward.

**Criteria:** positions justified by power over this decision and interest in it, not by seniority; at
least two moves explained; engagement changes stated. **Weak answer:** one grid reused for both
decisions, with every executive in the player quadrant, which removes the point of mapping.

## F2 — Floor or preference

Apply the two tests: written, owned, and applied to every team; and set before the current request.

| Item | Classification | Reason |
|---|---|---|
| Severity definitions | Floor | Published week 3 with owners |
| Migration rehearsal, tier 1 data | Floor | Mandatory since week 10 |
| Tier 1 runbook | Floor | One of the four operational minimums |
| On-call for every tier 1 component | Floor | Another operational minimum |
| Two reviewers on every merge request | Check the standards | Floor only if it is among the 14 mandatory rules; otherwise a preference |
| 80 percent line coverage | Preference | Not a published rule; coverage targets are easily gamed |
| No Friday deploys | Preference | A team habit, not an organization rule |
| Preferred framework | Preference | A technology choice for the team and the standard owners |

**What to do with preferences:** they become priced variables in the negotiation, or proposals to the
standard owners for the next review, not things the manager refuses in the meeting. **Criteria:** uses
the tests rather than intuition; checks Northstar's written standards for the review rule. **Weak answer:**
accepting all eight as the floor, which teaches product that engineering's "non-negotiable" means
"preferred".

## F3 — Rewriting the reply to Greg

A worked reply:

"Greg, I understand the prospect needs to see this working before they decide. We can't build the
integration change by Friday: it is about three engineer-weeks and the team's next opening is in three
weeks, and starting now would push back another item already committed to a customer.
Two paths: for Friday's demo we can configure the existing connector to show the flow (half a day of one
engineer, I'll confirm by tomorrow noon), and we can start the real change in three weeks with a date by
the end of that week. If the prospect's decision depends on the production change rather than the demo,
tell me and I'll take it to Amara as a priority question."

**Criteria:** names Greg's interest; a plain no early; a reason in his terms; at least one concrete path
with a date; what would change the answer and who decides. **Weak answer:** a softer refusal ("we'll
try") that Greg hears as yes, or a lecture on the team's workload, which is not his problem.

## A1 — Credit-note change against the rehearsal rule

**Interests.** Amara: keep a promise to a renewal customer. Marcus: keep his team out of the next
week-9-style Sev1. The customer: correct, itemized invoices from a date it can rely on.

**Floor.** Rehearsal for tier 1 data has been mandatory since week 10, after a Sev1 in which a migration
made rollback impossible. It is not Marcus's preference.

**Alternatives.** Amara's: escalate to Victor Lindqvist, which the published path allows because a
customer commitment is involved. Marcus's: hold the rule and accept the escalation.

**Options to price.** (1) Rehearsed release, forecast week 48 or 49. (2) Re-sequence other Billing work
to bring the rehearsal forward; ask what it displaces and whether it gains a week. (3) Ask what the
customer needs in week 47: if it is invoices from a billing period that starts later, the
rehearsed date may meet the interest. (4) Sofia Alvarez or Amara tells the customer now that the date
moves a week for a safety check, which may be acceptable to a customer whose stated concern is
reliability.

**Marcus's opening:** "Amara, I know the customer was promised week 47 and I want to help you keep
faith with them. We can't skip the rehearsal; it is the rule we set after the credit-note Sev1. Can we
look at what the customer needs on the 47th? If it is the next billing run, the rehearsed release may
still make it, and I can tell you by Thursday."

**Criteria:** floor named as an organization rule; interest explored before options; escalation treated
as legitimate, not a threat. **Weak answer:** skipping the rehearsal "this once", or a flat no with no path.

## A2 — Greg's anchor

**In the meeting:** do not argue with week 48 and do not offer a counter-date; you have no forecast. Ask
what the prospect needs on what date and why (the interest), and what Greg will do if engineering
cannot commit (his alternative: telling the prospect a later date, or losing the deal). Say when he
will have a forecast range: "by Wednesday, sized with Orders". The anchoring research suggests the
advantage of a first offer falls when the other side focuses on their own target and the opponent's
alternatives, so that is where your attention goes.

**Before the next meeting:** size the work, set your own target range from the data, price options
(full scope, a first slice that meets the prospect's evaluation, a later date) and send them in writing
before the next meeting, so that your proposal is the concrete number on the table. If the work crosses
the portfolio limit, use Chapter 42's forum; this exercise is about the conversation, not that decision.

**Avoid:** "week 48 is impossible" (an argument from his number), "we'll see what we can do" (a hedged
yes), and any date you have not sized. **Criteria:** separates interest from position, prepares a
target independent of the anchor, commits to a date for the forecast. **Weak answer:** splitting the
difference between week 48 and an unsized guess.

## A3 — Coaching a manager who always says yes

**Diagnosis first.** In a one-to-one, review the last ten requests: which were accepted, which were
sized before acceptance, and which missed. Ask what makes no hard; the answers often concern the
relationship with the product manager or a fear of seeming unhelpful (Chapter 6 covers the
conversation).

**Six weeks.** Week 1: the manager writes the floor for their team and checks it against the standards.
Weeks 1–2: every new request is sized before an answer, with a 48-hour rule. Weeks 2–3: rehearse the
five-part no on two real requests, with the director observing one product conversation. Weeks 3–6: the
manager brings priced options to each planning negotiation; the director reviews one per week and
steps out of the rest.

**Evidence it is working:** the share of requests answered with options rather than a bare yes; dates
met for commitments made in the period; the product manager's view (asked directly, with the manager's
knowledge); unplanned work trending down over the following quarter, a slower signal.

**Criteria:** starts from evidence, builds skill on real requests, measures behavior and results.
**Weak answer:** telling the manager to "push back more", which usually produces refusals without paths.

## X1 — The response to Victor

**Decision:** counter, in writing, after a one-to-one in which you ask what the board most needs. Do not
accept "below 10 per quarter" as written: at a true average of 9, a quarter meets it with probability
about 0.59 and four quarters running with 0.587⁴ ≈ 0.12 (Poisson assumption, stated); at 12 a quarter,
about 0.24 per quarter; at quarter 3's 14, about 0.11. The trend so far is 30, 21, 17, 14 per quarter.

**The page:** (1) Sev1 and Sev2 at or below 40 for year 2, reported quarterly as a rolling four-quarter
total, with the severity audit result beside it; at 36 expected a year, the total is 40 or below about
78 percent of the time. (2) Contractual availability at or above 99.9 percent every quarter, with
service credits. (3) Price: prevention at 6 FTE in quarters 5–6 and 5 FTE in quarters 7–8, flat headcount; holding
quarter 3's 8 FTE would cost 26 to 39 engineer-weeks a quarter of product capacity (2 to 3 FTE × 13). (4) Trigger: two consecutive quarters above 12 reopen the
allocation.

**Not traded:** the severity definitions and their audit, and the rule that no manager is judged on
their team's count. **Conversations:** Victor first; Amara before Rajiv, because the trigger could take capacity back from her plan;
Sofia on the audit.

**Defensible alternatives:** accept a quarterly 10 as a stretch aim while committing the annual figure;
or propose customer-impact minutes instead of counts if the data exists. **Weak answer:** accepting
because he is the CTO, or refusing without an alternative that solves his board problem.

## X2 — Helena's hallway question

**In the moment:** be honest and avoid both a promise and a contradiction of Victor. For example: "We've
gone from 30 to 21 to 17 to 14 a quarter. Below ten every single quarter is a hard promise, because counts that
small swing by chance. Victor and I are working out the commitment this week, and I'd rather give you a
number we can keep than one that sounds good. You'll have it from him for the board page." This
answers her question truthfully, names the uncertainty, and routes the decision to its owner.

**Afterward:** tell Victor the same day, in full, including what you said. Use it as the opening for
your one-to-one: the CEO is already asking, which raises the cost of a number missed in quarter 1 of
year 2.

**What to avoid:** "Yes, we can" (misleads the CEO and commits Victor to a fragile number); "No, that's
unrealistic" (contradicts your manager to his boss); presenting your counter-proposal to Helena before
Victor has seen it (going around him). **Criteria:** truthful about uncertainty, loyal to the process
without hiding information, prompt disclosure to Victor. Several wordings are defensible. **Weak
answer:** deflecting entirely ("ask Victor"), which leaves the CEO without the honest signal she asked for.

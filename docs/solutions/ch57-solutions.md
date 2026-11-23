# Chapter 57 solutions — Crises, Executive Disagreement, and Resistance to Change

Worked solutions for the [chapter 57 exercises](../parts/13-advanced-problems/57-crises-executive-disagreement-and-resistance.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Classifying the Checkout outage

**Classification.** The failure was caused by Halvard's own change, made by a person through a console.
In Coombs's clusters it sits between a technical-error accident (accidental cluster) and a human-error
accident (preventable cluster). The classification matters less than it seems, because the one intensifier
on record points the same way: Checkout had two Sev1 incidents in the previous two quarters (crisis
history). Prior relational reputation is not given; if merchants already saw Checkout as unreliable, that
would intensify attribution further. Under SCCT's guidelines, an
accidental crisis with a crisis history calls for rebuild strategies, and so does a preventable crisis.
Either way: apology, compensation where harm was largest, and visible corrective action.

**Departures from that strategy.**

| Time | Departure | Kind |
|---|---|---|
| 14:18 to 14:23 | Merchants knew before Halvard did | Policy before the day (alerting on aggregate error rate, not on card success) |
| 14:44 | VP on the bridge asking for estimates | Judgment under pressure, corrected by the IC within six minutes |
| 14:52 | First notice 11 minutes past Halvard's own standard | Policy (VP approval required for Sev1 posts) |
| 15:20 | Macro blames a third-party provider | Process (macros written from bridge chat) and the absence of a rule that no cause is stated until confirmed |
| 16:05 | Correct cause stated, contradicting the macro | Process: no single owner for customer statements |

The 20:00 message, the next-morning correction, and the compensation choice were consistent with a
rebuild strategy.

**Criteria for a good answer.** It classifies with the intensifiers, not the cluster alone; it sees that
most departures were set up by policy and process before the day; it treats the 15:20 macro as the
decisive failure because it mixed a deny strategy with the later rebuild.

**Weak answer.** Blaming the support lead who wrote the macro. The lead relayed a true observation (the
processor was returning errors) through a channel that had no rule against stating causes. Blaming that
person repeats the failure the chapter warns against, inside the company.

## F2 — Rewriting two messages and the correction

**First status post (14:52, or better, 14:41).** "Card payments at Halvard Checkout are failing for many
merchants since about 14:10 UTC. Wallet and other payment methods are working. Shoppers whose card payment
failed have not been charged. You do not need to take any action on failed orders now; we will provide a
list of affected checkouts once service is restored. We do not yet know the cause. Next update by 15:15
UTC."

**Support macro (15:20).** "Thank you for reporting this. We are aware that card payments are failing at
checkout and our engineers are working on it. Failed card payments were not charged. We have not yet
confirmed the cause and will not guess at it. Status updates at [status page] every 30 minutes; next by
15:45 UTC."

**The correction.** "Yesterday at 15:20 UTC our support team told some of you that a third-party payment
provider caused the checkout failure. That was wrong. We sent it before we knew the cause, which was a
change Halvard made to how card payments are routed. Our payment provider's systems were working
normally. We are sorry for the outage and for the incorrect message. Our review, including what we are
changing, will be published by [date]."

**What changed and why the quote matters.** The improved version names the provider's innocence
explicitly, because the provider was harmed by the first message, and it gives the review date. The
correction must quote or closely restate the wrong statement because the integrity question is about
what was said; a general "the cause was our change" leaves readers of the macro to notice the
contradiction themselves.

**Criteria.** Instructing information first; known and unknown separated; no cause; a time for the next
update; the correction specific. **Weak answer.** Status posts that say "we are investigating an issue
affecting some customers", which contains nothing a merchant can act on.

## F3 — Testing the readings of Northstar's pushback

| Pushback | Reading | Evidence that would show it wrong | If another reading were right |
|---|---|---|---|
| Amara's three conditions (week 42) | Interest | Amara holds the conditions even if the board pack stops counting roadmap items | A content reading: she doubts outcome targets work; test with one ordering outcome as a trial |
| Amara's objection on ordering correctness (week 49) | Content | The 1.3 percent corrected-order rate proves to be mostly customer-side errors | An interest reading: she wanted roadmap protection; then "excellent" status would be over-investment |
| Greg's objection to the estimate rule (week 49) | Interest, partly process | Engineering estimates already arrive in five days and Greg still objects | A person reading becomes plausible only then; even so, raise the pattern in the forum, not privately |
| Marta's objection on security (week 47) | Content | No "not affected" decision has ever been checked by IT security | Interest (turf): then the dotted-line option meets the substance at lower cost |
| Excellence Day decline (quarter 3) | Process and capacity | Teams with no period-close conflict and full manager support also dropped out | Content: engineers did not value the work at all; the pulse (29 of 52 wanted their own time) argues against this |

**Most tempting person problem.** Greg Tanaka, because his objections repeat and one came with a
private offer the director declined. The danger is that labeling him loses the information every
objection carries: sales has no fast, reliable path to an engineering answer. Treating him as the problem
leaves that gap in place, and the next sales leader will push through it the same way.

**Criteria.** Each reading has a falsifying test; the answer names its own bias. **Weak answer.**
Assigning readings with no way to be wrong, which turns the diagnostic into a label.

## A1 — Committing to a headline you argued against

**The note to Victor, same day.** "I argued for a four-quarter window because of chance variation, and
I still think it is the better commitment. It is your page and your call, and I will deliver against it
as if it were mine. Three things I would ask: that the page shows the severity audit beside the count;
that the floor stays as written (definitions change only through their owners, the audit continues, no
manager assessed on their team's count); and that we review the headline with you if two of the first
three quarters of year 2 miss it, so that we can decide together whether to change the target or the
investment."

**To the six managers.** "Victor has chosen 'below 10 a quarter'. I argued for a different form; the
decision is made, and it is ours now. Nothing about how we rate incidents changes. If anyone feels
pressure to rate an incident lower than the definition says, tell me or Kwame Mensah directly."

**Revisit trigger.** Two misses in the first three quarters, or any quarter where the audit finds a
rating disputed between the team and the definition's owner.

**When to stop committing.** If the count were reported to the board with incidents re-rated against the
definitions, or if Victor asked for ratings to be changed to meet the target. That is an integrity
question: first raise it with Victor directly and in writing; if unresolved, take it to Helena Marsh,
and on reported figures the audit committee chair is the last resort.

**Criteria.** The commitment is real (owned in front of the managers), the floor is restated, the
trigger is measurable. **Weak answer.** "I'll tell the managers this is Victor's number", which is silent
compliance announced in advance.

## A2 — A hypothetical Northstar public outage

This scenario is the reader's, not part of the case.

**First 15 minutes.** The incident commander (from the 12 trained in weeks 4 and 5) declares Sev1 under
the week 3 definitions, since the order path is unavailable for all customers. A communications role
sends the first notice from a template: order submission is failing, orders not confirmed were not
received, customers should hold resubmission until the next update, cause unknown, next update in 30
minutes.

**Leadership track.** The director opens an executive channel and takes the incident commander's
30-minute updates. Sofia Alvarez's team calls the three affected top-40 customers before they call in,
with the same facts as the status page. Victor Lindqvist does not join the bridge. He calls the three
customers' executive sponsors after Sofia's team has reached the operational contacts, and he is the
one person who may promise anything beyond the contract, which in the first hours should be nothing but
a review date.

**Hours 2 to 4.** After restoration, a restoration notice with what customers must still do (for
example, check orders submitted between the failure times). Within 24 hours, an apology under Victor's
name and the date of the review. The public post that preceded Northstar's first message is not answered
directly; the status page is.

**Criteria.** One owner of statements; instructing information first; Victor visible on customer
calls and absent from the bridge; no cause stated. **Weak answer.** Victor runs the bridge because he
knows the system best, which is both a role collapse and the delegable work [Chapter 50](../parts/12-cto-leadership/50-what-a-cto-actually-does.md) already counted.

## A3 — Turning Greg Tanaka's objection into a proposal

**What the objection carries.** Deals close on dates. In the baseline quarter 5 of 17 dates were given
before sizing, which means sales had no reliable path to an estimate when a customer asked. The rule as
drafted keeps the floor (no date without an estimate and a named owner) and contains a promise (estimates
within five working days). Greg's resistance is a bet that engineering will not keep the promise.

**The one-page proposal.**

1. **The floor stays.** No customer date without an engineering estimate and a named owner.
2. **The promise becomes measured.** Sizing requests enter one intake (the product manager for the area;
   Keiko Ashworth for ordering). An estimate with a range and confidence is returned within five working
   days. Reported monthly at the business review: requests, median and worst days to estimate.
3. **A fast path.** For deals in final negotiation, a rough range within two working days, labeled
   "order of magnitude, not a date"; sales may say "we will confirm a date within a week".
4. **When engineering misses.** A miss is logged and reviewed by the director with Greg; two misses in a
   quarter put sizing capacity on the leadership team agenda. The floor does not lapse because
   engineering was slow.
5. **Review after one quarter**, with Greg, on the data.

**Criteria.** The floor is kept, the promise is measurable, the consequence of a miss falls on
engineering's process rather than on the rule. **Weak answer.** Removing the rule for "strategic deals",
which recreates the baseline, in which 5 of 17 dates were given before sizing.

## X1 — Northstar's executive crisis policy

**The policy, in Victor's seat in week 49.**

| Decision | Owner | Basis |
|---|---|---|
| First notice for a customer-visible Sev1 | Incident commander's communications role, from a pre-approved template | Within a fixed time of declaration, no executive approval |
| Customer statements after the first notice | One named owner per incident: the director by default, Victor if a top-40 customer is affected | Same facts as the status page; no cause until confirmed |
| Compensation beyond contractual credits | Victor, with Rajiv Menon for amounts above a set threshold | Tied to measured harm and to the company's recent incident history |
| Public review | Published within ten working days, owned by the director | Timeline, impact, contributing factors, corrections, dated commitments, no names |
| Victor's incident time | Customer executive calls and decisions above; never the bridge | His two hours a week move from bridges to customers |

**What goes to Helena Marsh.** The compensation principle and threshold, because credits reduce
subscription revenue and touch renewals she owns, and the rule that customer statements may say "our
change caused this", because it binds the company's voice. Template wording goes to legal once, not per
incident.

**Criteria.** Speed of the first notice protected from approvals; a single statement owner; compensation
rules set before the day; Victor's time moved to what only he can do. **Weak answer.** A policy in which
every Sev1 statement is approved by Victor, which recreates Halvard's 14:52.

## X2 — Halvard's CTO and the general counsel

This scenario is the reader's, not part of the case.

**Decision.** The review says the outage was caused by a routing change Halvard made, and includes the
15:20 macro and its correction. Legal reviews wording so that it describes facts without characterizing
contractual liability; it does not remove facts merchants already know.

**Justification.** The integrity risk outweighs the contract risk. Merchants received two contradicting
statements, and the payment provider's own status page contradicted the first. A review that omits the
macro leaves the integrity question open, and trust-repair research suggests that is the violation an
apology repairs least well. The contract risk is bounded: credits are defined in the contract
($380,000 at the 10 percent tier), and the facts are already public.

**Company-wide policies.** First notices from pre-approved templates without executive approval in all
four product groups and the platform organization; one named owner for customer statements per incident;
no cause in any customer-facing channel until the incident commander confirms it; configuration that can
change production routing goes through the auditable pipeline policy, with no console exemption;
compensation rules tied to the contract, with goodwill beyond it decided by the CTO; public reviews
within a fixed number of days.

**Criteria.** The decision handles the joint escalation on its merits, protects both parties' legitimate
concerns, and turns one group's improvisation into policy. **Weak answer.** Siding with legal to minimize
admissions, or with Nadia without giving legal a wording role; either loses one party's legitimate
interest.

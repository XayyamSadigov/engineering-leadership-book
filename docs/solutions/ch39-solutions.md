# Chapter 39 solutions — Reviews, Decision Logs, Escalation, and Executive Reporting

Worked solutions for the [chapter 39 exercises](../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Routing four items

**Flat customer-detected share, third month.** This starts in a **review**: it is a fact about the
system that needs interpretation before anyone decides anything. The weekly operational review asks
which incidents customers found and why alerts missed them. Three flat months is also a **risk** for the
executive report, because the mandate depends on detection, but it goes there with the review's
reading, not as a raw number.

**Tom Becker and Marcus Oyelaran on ledger test environments.** A disagreement between two teams about
a recurring responsibility: the **escalation path**, after five days of trying. The joint case should
include the baseline demand data (Billing sent Platform Operations 7 links, 4 of them test environments
with ledger data). It ends in the **log**.

**auth-svc exemption expiry.** A dated item in the **log**: the expiry is the review trigger. The steward
should have raised it weeks before, so the question is whether auth-svc has left the scripts. If not,
the domain owner (Kwame Mensah) decides on renewal under the standards process, within the two-quarter
maximum.

**A renewal customer asks for a feature by week 30.** A capacity conflict with a customer commitment:
the director with the product lead, and the **executive report** if it moves quarter 3 commitments.

The weak answer sends everything to the executive report, or treats routing as filing. The point is
that each channel produces a different kind of output.

## F2 — Rewriting a green status

**What is missing.** No forecast, no date, no definition of "green", no scope figure, no owner of the
"minor risk", no change since last month, and "team morale" is not status. "Being managed" says
nothing about how.

**Questions to send back.** What does the forecast say for the contractual items and for current
scope, at 50 and 85 percent? How many items are in scope now, against the 44 agreed? What is the scope
risk exactly, who owns it, and at what point would it become a request to me? What changed since
the last report?

**Rewritten entry** (assumptions marked): "Bulk ordering, due week 26. Green for contractual scope: the
44 contractual items forecast at 93 percent by week 26 (from Chapter 17's exercise A3). Current scope 60
items, 62 percent by week 26 (from Chapter 17's exercise A3). Risk: the 16 added items; owner Priya Raman; I will ask you to
re-label them as targets if the 85 percent forecast for contractual scope drops below the date
(assumption: this is the agreed trigger). Change since last report: scope grew from 55 to 60
(assumption)."

The weak answer adds adjectives. A strong one replaces them with a forecast, a scope count, and a
trigger.

## F3 — The core/permissions log entry

| Field | Content |
|---|---|
| Id, date, title | DL-04 (part): owner of core/permissions; open since the week 4 ownership decisions |
| Decider and method | The record does not say who decides. Chapter 13 frames the director as Approver; the director must write that down |
| Options | Orders (made 17 of 38 baseline changes; Priya Raman would accept after week 26) or Platform Operations (next to auth-svc; made none; cannot support Core Java) |
| Status | Open, past any reasonable date |
| Needed by | Before the exemption lapses: exemptions last at most two quarters, so before the end of quarter 3. The director should set an earlier date, because the permissions extraction is changing the module now |
| Review trigger | After the decision: a change in who makes most of the module's changes, or the extraction finishing |

**Empty fields and how to fill them.** The decider: write it down, with the method (decide after
consulting Priya Raman, Tom Becker, Ines Carvalho, and Kwame Mensah). The "needed by": choose it and
announce it. Priya Raman's condition (after week 26) has been met by the start of quarter 3, which
removes the stated reason to wait; the entry should say so.

Criteria: the entry does not decide the owner (the case leaves it open), it does not invent a
decider the record lacks, and it makes the cost of further delay visible. The weak answer fills every
field with confident text the facts do not support.

## A1 — A Billing–Orders dispute under the escalation path

**Design.** Five working days for Priya Raman and Marcus Oyelaran to settle it, with Ines Carvalho
(Core code) invited as the domain's staff engineer. If unsettled, a joint case to the director,
decided within five working days, logged, and sent to both teams. Given the history, the director
should also set the first meeting, because the record shows these two do not start conversations: the
INC-417 thread had no manager response at all.

**Joint case template.** The decision needed in one sentence; the facts both agree on (here, the baseline
order-to-invoice links: 6 of Orders' 9 links to Billing were mapping changes in core/invoicing); each
side's option and reasons, written by that side; what each option costs the other team; the cost of no
decision by a date; and what both will do once decided. The Billing-owned order-to-invoice contract
from Chapter 34 is the obvious frame: the question may be who changes the contract, not who changes
the mapping.

**If one escalates alone.** Do not decide. Thank them, ask for the joint case, and tell the other
manager the same day that the question has reached you. Deciding on one side's account rewards the
unilateral route and recreates "Victor said".

The weak answer decides the technical question itself. The exercise asks for the mechanism; a
director who answers the mapping question has become the router.

## A2 — An architecture review that inspects decisions

**Chair and roles.** Not Ines Carvalho as sole chair, given her rejection pattern: 8 of 14 proposals
rejected, 5 without a reason. Rotate the chair among the three staff engineers, or have the director
chair while the staff engineers own the content. Ines attends as a domain owner, with the same rules as
everyone.

**Why it lapsed.** The review is a restart: Northstar has held none since 2021, and nothing replaced it. Ask
why it stopped before reviving it, or the same cause will stop it again.

**Before the meeting.** Each proposal arrives as a short decision record with options and a named
decider, two working days ahead. Written comments are due a day before; a rejection without a written
reason is not accepted.

**What the meeting decides.** It does not approve designs that sit within one team's authority. It
checks cross-team records: is there a decider, is there a date, were the consulted parties consulted,
is there a review trigger. It can send a record back for missing reasons, and it names deciders where
none exist.

**Measures at two months.** Proposals submitted by Orders engineers (two had stopped proposing
designs); share of rejections with written reasons (target: all); median days from proposal to
decision; records with review triggers. The coaching plan for Ines (Chapter 29) has its own
checkpoints; the review should not become a second, public coaching plan.

The weak answer bars Ines, which loses Core's deepest expertise and turns a system problem into a
person problem.

## A3 — "Just use the replicas"

**With Elena Sokolova, day one.** Thank her for raising it; that is the behavior you want. Agree that
her team does nothing irreversible on the feed until the log says so. Ask what she needs by when, so
the "needed by" date is real, and whether the feed falls under ADR-0001's scope (it reads posted ledger
data, so it probably does).

**With Victor Lindqvist, day one or two, privately.** Not "you broke the process". Explain the
mechanism: ADR-0001 is open in the log, the remark landed as a decision for one team and nobody else
heard it, and the old pattern (decisions in unrecorded conversations) is what the log exists to end.
Offer two routes: he sends such questions back through the path, or, if he wants to decide ADR-0001
himself, he is named as decider in the log and decides with the written options in front of him.
Either is legitimate; an unrecorded corridor answer is not.

**With the log.** Add the feed as a consumer to ADR-0001's context, record the date it is needed, and
note that a direction was given informally and is not a decision. Do not record it as Victor's
decision, and do not suppress it either.

The weak answers are compliance (use the replicas because the CTO said so) or confrontation in a
public channel. Both damage the system the director is trying to build.

## X1 — Five figures for the board

**Choice.** (1) Contractual availability on the order and payment paths against 99.9 percent, with
service credits. (2) Customer commitments: delivered and at risk, with dates. (3) Sev1 and Sev2
incidents, shown with customer-detected share so a fall from reclassification is visible. (4)
Engineering capacity by category (product, prevention, platform, unplanned), quarterly, from Chapter
38's scorecard. (5) One people measure: regretted attrition, or knowledge concentration on tier 1
components.

**Left out.** Core change failure rate and corrective-action closure: they are mechanism measures the
CTO and director manage; the board cannot act on them and would turn them into targets. Committed
roadmap items delivered as a single percentage: replaced by named commitments.

**Protecting the directors' reports.** Tell directors which figures go to the board and that their
reports are not reformatted board packs. Keep the board figures computed from systems, not from
directors' prose. Never show a director's report to the board verbatim, and never ask a director to
defend a board number in a way that rewards smoothing it. Keil and colleagues' finding that powerful
sponsors reduce candor applies to boards too.

The weak answer adds more numbers. A strong one chooses exposures the board can act on.

## X2 — After a surprise slip

**What to change.** First, the reporting contract, not the people: written color definitions computed
from forecasts, a "when did you first know?" review of this slip, and a trigger for same-day notice
when a customer commitment's forecast crosses the date. Second, corroboration through structure:
delivery forecasts computed from the planning system that the CTO can see directly, skip-level
conversations with the teams involved, and product partners' views. Third, the CTO's own behavior:
the first red report after this one must be met with questions and options, not blame, or the next
director will hide it longer.

**The audit option.** Weekly audited status from all three directors costs each director and their
managers several hours a week, slows reporting, and signals that every director is suspected because of
one. Keil and colleagues report that aggressive auditing can create a cycle of distrust and more
misreporting. It also treats the problem as dishonesty when it may be a forecasting gap: green for four
months may have been the director's honest belief.

**Criteria.** A good answer finds out why the report was green (no forecast, a forecast ignored, or
news withheld) before choosing a remedy, because each has a different fix. Defensible alternatives
include a time-limited weekly report for the one organization involved. The weak answer is
organization-wide surveillance.

## X3 — Availability "excluding maintenance"

**What to send.** Both figures, side by side, with the definition of each: availability as the
contract defines it (just under 99.9 percent) and availability excluding the planned window (just
over), with a note that the contract does not exclude planned maintenance. The contractual figure leads,
because it is the one the customer can check against its own records and the one that decides
service credits.

**What to say to the CTO.** Start with what the request is for: a better story for the renewal
meeting. Offer the legitimate version of that story: the trend over the quarters, the cause of the
miss, what changes next quarter, and the fact that most lost minutes were planned and announced.
That is framing. Presenting the excluded figure as "availability" to a customer whose contract
counts the window is misleading, and it is the customer's number as much as yours.

**If the CTO insists.** Say in writing that you believe the figure would mislead the customer and why,
and decline to send it under your name. Because the number bears on a contract and on service credits,
suggest involving finance or legal before anyone sends it. Do not quietly comply, and do not go around
the CTO to the customer.

**Criteria.** A good answer separates framing from misleading by the reader-fairness test, offers the
CTO a real alternative, and keeps a written record. Defensible variations: proposing that the
contract's treatment of planned maintenance be renegotiated openly at the renewal. The weak answers
are silent compliance ("it's the CTO's call") and public confrontation before trying the side-by-side
version.


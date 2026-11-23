# Chapter 37 solutions — The Management Operating System: Cadences and Leadership Meetings

Worked solutions for the [chapter 37 exercises](../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Auditing a managers' meeting

**Claimed job:** usually "align the leadership team", which is not a job in the chapter's sense
because it names no output. **Actual job:** inform. Seven status reports of about six minutes take 42
of 60 minutes, and 3 decisions in 31 items over six weeks is one decision every two meetings.

Through the audit diagram: the meeting has no single named job (split or stop). Once split, the
informing part fails "changes anything?" and goes to a written update with a fixed format and a
deadline before the meeting. The deciding part, if decisions really are needed weekly, becomes a
shorter leadership meeting with framed items and a named decider for each.

**What to measure afterward:** decisions recorded per week, decisions reopened in another forum,
minutes spent on status (should be near zero), and whether managers read the written updates
(questions asked on them). Note how each can be gamed: trivial items framed as decisions, reopening
done informally.

**Weak answer:** shortening the round to three minutes each. It keeps the wrong job and saves only
time.

## F2 — Placing loops in horizons

- **Error budget for order submission:** the signal moves in days, and the reporting-mode policy
  (Chapter 24) publishes it weekly. Home: the weekly operational review, discussed only when an
  incident consumed more than a fifth of the budget.
- **Moving a component between teams:** structural, slow to act on, with transition cost. Home: the
  quarterly reset, prepared in the leadership meeting.
- **Share of capacity spent on debt entries:** spending moves over weeks; Chapter 21 asks for monthly
  reporting alongside features. Home: the monthly business review.
- **Forecast calibration across teams:** needs several weeks of forecasts to judge. Monthly business
  review; the weekly forecast refresh for dated items stays in the operational review.
- **A Sev1 follow-up due next Tuesday:** weekly operational review.
- **Ownership of a disputed shared module:** a cross-team decision; the weekly leadership meeting,
  with the decider named under the decision-rights map of Chapter 13.

A good answer justifies each by signal speed and action speed, not by habit. A weak answer puts
everything in the weekly meeting "to be safe", which recreates the overloaded operational review.

## F3 — Recomputing the quarter 2 calendar

Changed lines: operational review from 1.25 to 0.5 hours (30 minutes). Staff group from 0.5 to 1.0
(60 minutes weekly). Manager one-on-ones from 4.5 to 3.0 (6 × 0.5); the staff and CTO one-on-ones stay
at 1.5 and 0.5, so the one-on-one line becomes 5.0 instead of 6.5.

Starting from the rate from week 16 (16.31), new total: 16.31 − 0.75 + 0.5 − 1.5 = 14.56, about 14.6 hours a week. Check by adding: 0.5 + 1.0 +
0.75 + 1.0 + 0.5 + 0.75 + 1.0 + 5.0 + 2.0 + 1.125 + 0.375 + 0.25 + 0.31 = 14.56.

**Cost in signal.** Squeezing the operational review back to 30 minutes without removing the status
that crept in means incidents and follow-ups get less time, not status; the fix is removing content,
not shortening the booking. Shorter manager one-on-ones cut the time for development and for news
(Chapter 5); with a recently promoted manager such as Priya Raman, and with Daniel Cho, whose
one-on-ones were reviewed in quarter 2, that is a poor place to save. A weekly staff group doubles a forum whose job has not grown.

A strong answer notices that this alternative saves about as many director hours as the chapter's
redesign while making every forum worse.

## A1 — Ending the renewal check-in

**Recommendation (one defensible answer):** the check-in does not end on the calendar; it ends on a
condition. Bulk ordering is due at the end of week 26. Rule: the check-in continues weekly until the
feature is delivered and has run a defined period in production without a Sev1 or Sev2 attributable
to it (for example two weeks), then stops; if the date is at risk, it continues until a new date is
agreed with Amara Okafor and the customer, and its job is narrowed to that one commitment.

**What to know first:** the current forecast for bulk ordering (Chapter 17's method from the 44-item
backlog and historical growth), the customer's acceptance criteria, and whether the accounting
integration (due week 19) needs any follow-up after delivery.

**What not to accept:** keeping the check-in open-ended "because renewals matter", or folding renewal
status into the leadership meeting as a standing status item, which reintroduces the round.

Elena Sokolova's objection is valid as stated; the chapter's own failure mode (the meeting that
outlived its job) argues for an end condition, not an end date chosen in advance. Weak answer: siding
with whichever person argued last.

## A2 — The first four weeks of the leadership meeting

**Pre-read** (posted by the previous working day at noon): per team, three lines (what changed, what
is at risk, what you need from this group), plus the open-decisions list with each item's decider and
due date.

**Agenda, 75 minutes:** questions on the pre-read (10); up to two framed decisions (35); one topic for
discussion that is not yet a decision (20); commitments recap (10): each decision, its owner, and what
every member tells their team.

**ADR-0001 and similar items** come in as a framing item: "who decides how integrations read posted
ledger data, by when?" The meeting can route the question to Victor Lindqvist or to the decision-rights
map work of Chapter 13; it must not quietly decide the decision right by discussing the options until
consensus appears.

**Remote participants and staff engineers:** everyone joins individually on video even from the room,
questions on the pre-read are taken in written order, and each staff engineer owns the technical
framing of at least one item per month. Rotate the facilitator after week 4.

Criteria: status is gone, decisions are framed before the meeting, and the meeting ends with recorded
commitments. Weak answer: an agenda with "updates from each team" as item one.

## A3 — Routing platform demand

Requests from other teams took about 20 percent of Platform Operations' capacity at baseline and
about 14 percent by the week 18 re-sample (the team also received 29 of the 86 cross-team dependency
links on the [baseline page](../case-studies/northstar/baseline-data.md)). The demand is continuous; a monthly
forum is the wrong place for individual requests but the right place for the pattern.

**Routing without a new meeting:** individual requests go through the single intake and the
two-person interrupt rotation already in place (Chapter 16 explains both), with a service level per request type.
Requests that miss their service level or need a trade-off between teams appear on the open-decisions
list for the weekly leadership meeting. The monthly business review looks at the aggregate: volume by
requesting team, waiting time, and which requests self-service could remove.

**How to know in six weeks:** median wait per request type against the service level, the number of
requests escalated to the leadership meeting (should be small), and the share of Platform Operations
capacity on requests.

Gaming risk: teams may stop logging requests and ask engineers directly. Spot-check by asking
Platform engineers about unlogged work. Weak answer: a weekly platform sync, which is the accretion
failure mode.

## X1 — The CTO's business review

**Load:** a monthly 60-minute review costs four executives an hour, but the real cost is preparation.
If each manager prepares a slide and the director assembles them, that is roughly six manager-hours
and three director-hours a month, plus a weekly note of perhaps an hour.

**Recommendation:** accept the monthly review but feed it from artifacts that already exist: the
monthly business review's outputs and the scorecard (Chapter 38), not new slides. Ask Victor to replace
the weekly note with the existing pre-read of the leadership meeting, shared with him, so nothing is
written twice. The review's one job should be stated: allocate or escalate at company level (money,
customer commitments, headcount questions for Rajiv Menon), not re-inspect teams.

**Preventing a cascade:** fix the input format, forbid pre-meetings to prepare it, and set a time
budget for its preparation that the director reports after two months.

A strong answer welcomes the executive loop, which Northstar lacks, while refusing a second reporting
chain. Chapter 39 owns the content of the executive report. Weak answer: accepting both requests as
asked, or refusing them to protect the calendar.

## X2 — Decisions without explanations

**Diagnosis:** the deciding loop works, but the cascade does not. Decisions are made and logged, yet
engineers hear outcomes without reasons, which suggests the commitments recap is skipped or that
managers relay only the decision. It may also mean decisions are being made by the leadership team
that teams expected to be consulted on.

**What to change:** make "what each member tells their team, and why" an explicit output, add the
reasoning to the decision log entry, and check after a few weeks in skip-levels whether engineers can
state the reason for two recent decisions. Review which decisions should involve the affected teams
before being made (Chapter 13).

**What to leave alone:** the decision cadence and the written pre-read, which are producing the
intended result.

**How the evidence could mislead:** skip-levels are a small, self-selected sample; four decisions a
week may include trivial items; reopened decisions may have fallen because disagreement went
underground rather than because decisions improved. Check for decisions made in the log but not
followed in practice.

Weak answer: concluding the meeting decides too fast and slowing it down.

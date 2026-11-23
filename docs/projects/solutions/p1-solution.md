# Project 1 solution: Northstar's quarter 3 operating system

This is one worked answer to [Project 1](../p1-management-operating-system.md). It treats the
director's week-22 redesign in [Chapter 37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md)
as a submission to be tested, not as the answer. The conclusion is that the redesign is the right
shape, homes every loop in its own matrix, misses four loops its matrix does not list, fails two
acceptance criteria as written, and needs five amendments. Every recommendation here is this
solution's, one defensible answer among several. All Northstar facts are fictional; estimates marked
as this solution's are assumptions, not facts from the case.

People named, with roles (see the [cast](../../case-studies/northstar/cast.md)): Victor Lindqvist (CTO),
Amara Okafor (CPO), and the engineering managers Priya Raman (Orders), Marcus Oyelaran (Billing), Elena
Sokolova (Payments and Integrations), Daniel Cho (Customer Experience), and Tom Becker (Platform
Operations); the staff engineers Kwame Mensah, Ines Carvalho, and Li Na Zhou; and Mateo Arango Ríos,
Customer Experience's informal mobile lead in Bogotá.

## 1. The quarter 2 system, recomputed twice

From [`p1-quarter2-forums.csv`](../data/p1-quarter2-forums.csv), at the rate from week 16.

**Director's hours, by forum:** 1.25 + 1.0 + 0.75 + 1.0 + 0.5 + 0.75 + 0.5 + 4.5 + 1.5 + 0.5 + 2.0 +
1.125 + 0.375 + 0.25 + 0.31 = 16.31.

**By category:** one-on-ones 6.5 (4.5 + 1.5 + 0.5); skip-levels 2.0; weekly forums 5.25 (1.25 + 1.0 +
0.75 + 1.0 + 0.5 + 0.75); the fortnightly staff group 0.5; monthly forums 1.75 (1.125 + 0.375 + 0.25);
the quarterly reset 0.31. Total 16.31, which Chapter 37 rounds to 16.3. The two methods agree.

**Attendee-hours a week** (hours × attendees; one-on-ones and skip-levels count two people):

| Forum | Calculation | Person-hours |
|---|---|---|
| Operational review | 1.25 × 16 | 20.0 |
| Managers' meeting | 1.0 × 7 | 7.0 |
| Renewal check-in | 0.75 × 6 | 4.5 |
| Product and engineering sync | 1.0 × 5 | 5.0 |
| Billing and Orders sync | 0.5 × 3 | 1.5 |
| Release working group | 0.75 × 8 | 6.0 |
| Staff group | 0.5 × 4 | 2.0 |
| One-on-ones | 6.5 × 2 | 13.0 |
| Skip-levels | 2.0 × 2 | 4.0 |
| Quality reviews | 1.125 × 5 | 5.625 |
| Delivery review | 0.375 × 13 | 4.875 |
| All-hands | 0.25 × 87 | 21.75 |
| Quarterly reset | 0.31 × 9 | 2.77 |
| **Total** | | **98.0** |

Check by horizon: weekly forums 44.0 (20 + 7 + 4.5 + 5 + 1.5 + 6), staff group 2.0, one-on-ones and
skip-levels 17.0, monthly 32.25 (5.625 + 4.875 + 21.75), quarterly 2.77: 98.0. About 7.5 of the
operational review's 20 person-hours belong to the six on-call leads (6 × 1.25), engineers whose
attendance is the cost Chapter 37 points to.

**A typical manager:** operational review 1.25, managers' meeting 1.0, one-on-one 0.75, their quality
review 0.19 (45 minutes a month ÷ 4), delivery review 0.375, all-hands 0.25, reset 0.31: 4.125, about
4.1. Priya Raman adds the renewal check-in (0.75) and the Billing and Orders sync (0.5): 5.375, about
5.4. Marcus Oyelaran adds the sync: 4.625, about 4.6. These match Chapter 37.

## 2. The matrix, extended

Chapter 37's six rows, plus seven loops its matrix does not list. "Appears" and "resolved" are read
from Northstar's record up to week 22.

| Loop | Appears in | Resolved in | Status |
|---|---|---|---|
| Renewal status | Six forums | Renewal check-in | Duplicated |
| Incident follow-ups due | Four forums | Operational review | Duplicated |
| Platform requests and environment waits | Managers' meeting, product sync, delivery review | Nowhere | Missing |
| Cross-team decisions ([ADR-0001](../../glossary.md#adr-0001) on how integrations read ledger data; the core/permissions owner) | Managers' meeting, staff group, Billing and Orders sync | Nowhere | Missing |
| Technology risk register | None | Nowhere | Missing |
| Promotion calibration | One-on-ones | Nowhere | Missing |
| *Open log entries past "needed by"* | Nowhere (log opened week 14) | Nowhere | Missing |
| *Executive reporting to Victor Lindqvist* | His one-on-one, ad hoc | Nowhere; no written report since day 90 | Missing |
| *Manager assessment and development* | One-on-ones; expectations written week 22 | Nowhere | Missing |
| *Error budget policy* (reporting mode or enforced) | Operational review reads budgets weekly | Nowhere; Victor is arbiter with no slot | Missing |
| *Exemptions approaching expiry* (core/permissions at week 39) | Nowhere | Nowhere | Missing |
| *Quarterly capacity and priorities* | Quarterly reset | Quarterly reset | Homed |
| *The operating system itself* | Nowhere | Nowhere | Missing |

Thirteen loops: one homed, two duplicated, ten missing. Chapter 37's matrix finds four missing; the
extension finds six more, and five of the six are slow loops (monthly or quarterly). That is the
pattern to expect: weekly forums collect fast topics, and the slow ones, which nobody's week forces,
fall through.

## 3. The design

Each loop gets one home, matched to its horizon (Chapter 37's horizon table).

| Forum | Job | Loops it homes | Cadence and length | Members | Owner | Review date |
|---|---|---|---|---|---|---|
| Operational review | Operate | Incidents, follow-ups due, error budget readings, severity audit, release and platform exceptions | Weekly, hard 45 minutes | 14: director, managers, Kwame Mensah, six on-call leads; Ines Carvalho and Li Na Zhou optional | Director | Week 33 |
| Leadership team meeting | Decide | Cross-team decisions, escalations, open log entries past "needed by", exemptions within four weeks of expiry; manager artifact review slot | Weekly, 75 minutes | 11: director, six managers, three staff engineers, Amara Okafor or a product manager she names | Director | Week 33 |
| Product trades | Decide | Roadmap trades inside the quarterly plan | Every two weeks, 45 minutes | Director, Amara Okafor | Director and CPO | Week 39 |
| Monthly business review | Inspect | Delivery and flow, forecast calibration, debt spending, technology risk register, platform demand trend | Monthly, 120 minutes | 13 (this solution assumes the delivery review's attendees) | Director | Week 39 |
| Team quality reviews | Inspect | One team's quality system (Chapter 27) | Monthly per team, 45 minutes | Director, manager, staff engineers | Each manager | Unchanged |
| Written report to Victor Lindqvist | Inform, in writing | Executive reporting; open decisions he owns, including the error budget policy | Monthly, two pages | Director writes | Director | Week 39 |
| Quarterly reset | Allocate | Capacity, priorities, structure; 30 minutes auditing the operating system | Quarterly, 4.5 hours | 9 | Director | Each quarter |
| Talent review | Allocate | Promotion calibration; manager assessments (Chapter 41) | Quarterly, 3 hours, first in week 27 | 7: director and managers | Director | Week 39 |
| Staff group | Develop and decide | Staff mandates, technical standards | Every two weeks, 60 | Director, staff engineers | Director | Unchanged |
| Billing and Orders sync | Connect | The pair's friction, after the order-to-invoice contract | Monthly, 30 | 3 | Director | Week 39 |
| One-on-ones and skip-levels | Develop, connect | People | Unchanged hours; skip-levels as two groups of three plus one individual | | Director | Quarterly |
| All-hands | Inform and connect | Context for everyone | Monthly, 60 | All | Director | Unchanged |

**Fates of the quarter 2 forums.** Managers' meeting and product sync: merged into the leadership team
meeting, with a fortnightly product-trades remainder. Delivery review: replaced by the business review.
Release working group: kept under Kwame Mensah; the director stops attending, and exceptions route to
the operational review. Renewal check-in: ends under a rule, not a date (section 6). Billing and Orders
sync: monthly. One new forum, the talent review, joins the quarterly reset week and names the loop it
takes out of one-on-ones (constraint 2).

**The written report replaces conversation, not a meeting.** It is the one change to what Victor
receives, and it is his call (constraint 6). The proposal to him: a monthly two-page report built on
Chapter 39's structure, drawn from the scorecard and the leadership pre-reads, so that no manager
prepares anything new for it beyond 30 minutes a month.

## 4. The leadership team meeting

**Pre-read.** Each manager and staff engineer posts a written update by noon on the previous working
day, in five fixed parts: commitments with status (Chapter 39's color definitions), one risk, one
surprise, requests to other teams, decision items. Amara Okafor or her delegate posts product changes
in the same format. The director reads all of them before the meeting and opens with questions.

**Agenda, 75 minutes.**

| Minutes | Item |
|---|---|
| 0–10 | Questions on the written updates; no recital |
| 10–50 | Up to three framed decision items |
| 50–70 | Manager artifact review: one manager, one artifact (a quarter plan, an incident review, a promotion packet), peers ask "what would you change?" |
| 70–75 | Closing: each decision, its decider, its owner, and what each member tells their team; log entries confirmed |

The artifact slot is where Chapter 41 places manager development; 13 weeks give each of the six managers
two slots, with one week spare.

**A decision item arrives framed:** the question, options, recommendation, the decider and who is
consulted, "needed by", and the cost of delay. The meeting does not decide who holds the decision
right. For DL-08 to DL-10, which have no named decider, the director names one outside the meeting and
records it, because the decision-rights map is the director's (Chapter 28); the meeting then hears the
case. The decider decides in the room or by a stated date, and nothing counts until it is in the log.

**Staff engineers and product** take part as contributors, not spectators: a staff engineer presents any
decision item in their standing scope, and product owns the "cost of delay" line for any item touching
a customer date.

## 5. Routing rules

1. **Exceptions upward.** The release working group, the platform rotation, and each team's operations
   review report exceptions to the operational review in its fixed agenda; trends go to the business
   review.
2. **Decisions downward.** Every decision is in the log within one working day, and a short summary is
   posted the same day in a channel every engineer can read (section 7).
3. **Fast path.** A decision with a cost of delay measured in days is made by its decider, logged, and
   reported at the next meeting. If the fast path is used more than twice in a quarter for the same
   kind of decision, that kind needs a standing owner.
4. **Escalations** follow the published path (five working days, joint written case, director within
   five days) and end in the log; the leadership meeting hears the case only when the decision affects
   more than the two parties.
5. **Platform demand** (Tom Becker's objection) never waits for the monthly review. Requests go to the
   single intake the platform rotation already runs. Any request blocked more than five working days
   appears as an exception in Tom's pre-read; a conflict between two teams' requests becomes a decision
   item that week. The monthly review sees only the trend (environment wait, points of capacity on
   other teams' requests).
6. **Log hygiene.** Open entries are reviewed in the leadership meeting when they pass "needed by", and
   any exemption within four weeks of expiry is listed in the pre-read. core/permissions' exemption
   expires at week 39, so it appears on the list in week 35 at the latest.

## 6. The three objections and Bogotá

**Elena Sokolova: do not end the renewal check-in while bulk ordering may slip.** She is right that a
date is the wrong end rule; Chapter 37's draft fails acceptance criterion 6 as written. This
solution's rule: the check-in ends at the first meeting after bulk ordering is generally available and
two weeks have passed with no Sev1 or Sev2 attributed to it. Until then it continues, shortened to 30
minutes and limited to the bulk-ordering acceptance list. Renewal status for the accounting
integration, live since week 19, moves to the pre-read in week 27 either way.

**Tom Becker: platform requests cannot wait a month.** Also right: by Chapter 37's own horizon table,
a signal that moves in days does not belong to a monthly forum. Rule 5 answers it without a meeting.

**Daniel Cho: are Bogotá engineers served by a meeting held in a Minneapolis room?** Every member of
the leadership meeting works in Minneapolis, so the meeting itself is not where Bogotá is served or
lost. The cascade is. Three changes: the same-day written decision summary, read by everyone; each
manager tells their team within two working days, and Daniel's mobile engineers hear it in a meeting
held for Bogotá, not appended to a web stand-up; and the all-hands runs with every participant on
their own screen (the format Chapter 36 later uses for announcements), with a Bogotá engineer
presenting at least once a quarter. Whether this reaches Bogotá is an input this solution does not
have; the first skip-level groups ask it directly.

## 7. Cost, recomputed twice

**Director's recurring hours.** Operational review 0.75, leadership meeting 1.25, product trades 0.375,
renewal check-in 0 (or 0.5 while it continues), Billing and Orders sync 0.125, release working group 0,
staff group 0.5, one-on-ones 6.5, skip-levels 2.0, quality reviews 1.125, business review 0.5 (120
minutes ÷ 4), all-hands 0.25, reset 0.35 (4.5 ÷ 13), talent review 0.23 (3 ÷ 13).

- By line: 0.75 + 1.25 + 0.375 + 0.125 + 0.5 + 6.5 + 2.0 + 1.125 + 0.5 + 0.25 + 0.35 + 0.23 = 13.955,
  about 14.0; 14.5 while the check-in continues.
- By category: one-on-ones 6.5, skip-levels 2.0, weekly forums 2.0 (0.75 + 1.25), fortnightly 0.875
  (0.375 + 0.5), monthly 2.0 (0.125 + 1.125 + 0.5 + 0.25), quarterly 0.58 (0.35 + 0.23): 13.955.

Both methods give 14.0, under the 16-hour constraint even with the renewal branch. Recurring
preparation is counted separately, as this solution's estimate: reading ten pre-reads (about 0.5
hours a week), the monthly report (4 hours a month, 1.0 a week), and Chapter 41's manager assessment
(12 hours a quarter, about 0.9 a week): about 2.4 hours a week. A design that counted only meetings
would hide these.

**Attendee-hours.** This solution's design, with its assumptions (business review at 13 people, as the
delivery review; release working group at 7 without the director; skip-levels as two groups of three
at 45 minutes and one individual conversation at 30):

| Change from quarter 2 | Person-hours a week |
|---|---|
| Operational review 20.0 → 10.5 (0.75 × 14) | −9.5 |
| Managers' meeting and product sync removed | −12.0 |
| Leadership meeting (1.25 × 11) | +13.75 |
| Product trades (0.375 × 2) | +0.75 |
| Renewal check-in ended | −4.5 |
| Billing and Orders sync monthly (1.5 → 0.375) | −1.125 |
| Release working group without the director (6.0 → 5.25) | −0.75 |
| Skip-levels 4.0 → 7.0 (6 in groups, 1 individual) | +3.0 |
| Delivery review replaced by business review (4.875 → 6.5) | +1.625 |
| Reset lengthened (2.77 → 3.12) | +0.35 |
| Talent review (3 × 7 ÷ 13) | +1.62 |
| **Net** | **−6.78** |

98.0 − 6.78 = 91.2. Summed directly: 10.5 + 13.75 + 0.75 + 0.375 + 5.25 + 2.0 + 13.0 + 7.0 + 5.625 +
6.5 + 21.75 + 3.12 + 1.62 = 91.24. The organization saves only about 7 person-hours a week. What changes
is who spends them: on-call engineers get back 3 hours a week (6 × 0.5), and the hours move from
listening to deciding. Writing the pre-read adds about 3.3 person-hours a week (10 writers at 20
minutes), which this solution counts as preparation, not meeting time.

**Managers.** Typical: operational review 0.75, leadership meeting 1.25, one-on-one 0.75, quality
review 0.19, business review 0.5, all-hands 0.25, reset 0.35, talent review 0.23, pre-read 0.33: 4.6,
against 4.1. Adding two artifact-review preparations a quarter at an hour each (this solution's
estimate, 0.15 a week) gives about 4.75. Priya Raman: 4.75 + 0.125 = about 4.9 once the check-in ends,
against 5.4; about 5.4 while it continues (+0.5). Marcus Oyelaran: about 4.9, against 4.6. The
managers' hours do not fall; Chapter 37 says the same, and the design should be sold to them as hours
moved toward deciding, not hours returned.

## 8. Transition and the week-33 check

**Announcement in week 25,** after the week-24 review: what stops, what replaces it, the pre-read
format, the routing rules, and the review date. The first pre-read is due in week 27.

| Measure at week 33 | Quarter 2 reading | How it misleads | Cross-check |
|---|---|---|---|
| Decisions per leadership meeting | 5 in 6 managers' meetings | Trivial items framed as decisions | Read the log: decisions with a cost of delay |
| Decisions reopened | 2 of 5 | Reopening moves to corridors | Count "Victor said" and hallway reversals reported in one-on-ones |
| Log entries past "needed by" | DL-04, DL-08 to DL-10 open | Dates set far away | Every new "needed by" checked against the cost-of-delay line |
| Operational review length | 75 against 30 booked | Items moved offline to keep 45 | Follow-ups due that slip a week |
| Pre-reads on time | None existed | On time but unread | The director's opening questions cite them |
| Loops resolved in their home | 1 of 13 | Resolved on paper | Recount the matrix from six weeks of notes |
| Director and attendee hours | 16.3 and 98.0 | Hours flat while decisions move | Both columns, not one |

**Trigger for redesign:** fewer than one decision per meeting on average over weeks 27 to 32, or the
operational review over 45 minutes in three of six weeks, or more than one log entry past "needed by"
without a recorded reason. Any of these goes to the reset's 30-minute audit.

**Inputs and branches.** Bulk ordering slips: the check-in continues under its rule. Managers reject the
pre-read: run it for six weeks as a trial and count decisions; without it the meeting reverts to a
status round. Victor declines a written report: keep it as the director's own monthly writing for the
one-on-one, because the reset and the business review need the same content. Bogotá hears nothing
through the cascade: move one leadership meeting a month to a time and format where Mateo Arango Ríos
or another Bogotá engineer presents mobile's items.

## 9. Evaluation of Chapter 37's redesign

**Strengths.** It homes all six rows of its matrix, cuts the director's recurring load from 16.3 to
14.0 and the operational review from about 20 to 10.5 person-hours, turns the status round into a
pre-read, adds the talent review the promotion cycle needed, puts the operating system's own audit in
the reset, and does not decide ADR-0001 or the core/permissions owner. Its honest finding that
managers' load rises from 4.1 to 4.6 is the kind of arithmetic most redesigns leave out.

**Weaknesses, honestly.**

1. **The renewal check-in ends by date.** Fails acceptance criterion 6. Fix: section 6's rule.
2. **Four loops missing from its matrix are missing from its design:** executive reporting, manager
   assessment and the artifact slot (Chapter 41 places it in the weekly managers' meeting, which the
   redesign removes without moving the slot), the error budget policy, and exemptions approaching expiry.
   The core/permissions exemption reaches its two-quarter maximum at week 39 (known at week 22); a
   design with a log-hygiene rule would list it in week 35.
3. **Platform demand is homed at the wrong horizon,** as Tom Becker says.
4. **Bogotá is not addressed,** as Daniel Cho says. Fails acceptance criterion 8.
5. **Attendee-hours are computed only for the operational review,** so the leadership meeting's growth
   from 7 to 11 people and the pre-read's writing cost are invisible.

**Scored against the rubric:** diagnosis 12 of 15 (strong matrix, not extended); loop coverage 14 of 20;
leadership meeting 11 of 15 (pre-read and open-decisions list; no closing routine or artifact slot);
cost 12 of 15 (director and managers, not attendee-hours); routing 5 of 10; stakeholders 8 of 15
(objections recorded, deliberately left open by the chapter); transition 5 of 10 (the reset audit, no
week-33 measures). Total 67: adequate, and it would not pass until the check-in has an end rule and
Bogotá has an answer. The five amendments in sections 3 to 8 target exactly the lost points.

**Other defensible answers.** Keeping the managers' meeting and the product sync separate, with a
written pre-read in each, scores as well if the matrix shows no decision made twice. Making the
operational review fortnightly is defensible once error budgets are enforced, not while incidents
still number more than one a week. A director who cuts one-on-ones with staff engineers to fortnightly
to fund the business review can stay within 16 hours; the cost is the staff mandates' development, and
the submission must say so.

## What a weak submission looks like

> "Too many meetings. We will cancel the managers' meeting, the product sync, and the renewal check-in,
> move everything to Slack, and hold a single weekly leadership meeting of two hours with everyone who
> needs to be there. This will save about five hours a week."

Against the rubric: no inventory, no attendee cost, no matrix (diagnosis weak); loops are not listed,
so the cross-team decisions and the risk register stay homeless, now in chat (loop coverage weak); a
two-hour meeting "with everyone who needs to be there" is the status round made longer (leadership
meeting weak); five hours asserted, not computed, and it ignores that "everyone" means more engineers
in the room (cost weak); no routing (weak); the renewal check-in ends with bulk ordering still due and
nobody asked Elena Sokolova (stakeholders weak); no review date (transition weak). It fails acceptance
criteria 1, 2, 3, 6, 7, 8, and 9.

**An adequate submission** reproduces Chapter 37's redesign with correct arithmetic, answers the
objections briefly, and names a review date. It scores in the 60s. **What separates excellent from
adequate** is counting what others pay (attendee-hours, managers' writing, the preparation below
Victor), extending the matrix to the slow loops nobody's week forces, and an end rule for every forum
created for a commitment.

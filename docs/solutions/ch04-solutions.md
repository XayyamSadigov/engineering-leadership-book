# Chapter 4 solutions — The Leadership Ladder: Senior Engineer to CTO

Worked solutions for the [chapter 4 exercises](../parts/01-foundations/04-the-leadership-ladder.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Deployments are not a manager ranking

**A reply to the CEO.** "Deployment counts tell us how each team ships, not how well each manager
manages. Customer Experience deploys 26 times a month because it owns services and frontends that
deploy independently. Billing deploys 8 times because most of its code ships through the Core release
train every two weeks, which neither Marcus nor any single manager controls; the baseline notes that
Billing's lead time and failure rate describe the train more than the team. Customer Experience also
has 44 escaped defects with 15 engineers under one manager across two platforms, so its numbers are
not obviously a success. To judge the managers I would look at four things over two quarters: their
teams' agreed outcomes in context, team health (regretted attrition, upward feedback, on-call
concentration; Billing has three people carrying most pages), people growth, and what each manager has
fixed beyond their own team."

**Criteria.** A good answer separates team activity from managerial output, names at least one
system factor (the release train, the type of components), and proposes evidence over a horizon
longer than a quarter.

**Weak answer.** Swapping deployments for another single number, such as incident count, and ranking
again. Any single team metric inherits the attribution problem.

## F2 — Reading a director's calendar

**Classification.** Of about 16 hours listed:

| Item | Hours | Level it belongs to |
|---|---|---|
| Reviewing pull requests in one team | 6 | Senior engineer or tech lead |
| Planning session with one team | 2 | Engineering manager |
| Debugging an incident as an individual responder | 3 | Senior engineer |
| Four one-on-ones with managers | about 4 | Director |
| Budget session with the CFO's analyst | 1 | Director |

About 11 of the 16 hours go to work of lower levels (9 of them two levels down), and about 5 to work
only a director can do.

**What the pattern predicts.** Previous-level gravity: the work gives fast feedback and feels
productive. Over two quarters, the managers learn that the director will step into their teams, so
they escalate instead of deciding; the one team receiving the reviews gets attention the other five
do not; the budget and structural decisions get one hour a week and are made late or by others. The
director also becomes a single point of failure in incidents, which Northstar's incident-commander
training was meant to avoid.

**Criteria.** The answer classifies by level, not by value (debugging can be useful), and predicts
second-order effects on the managers.

**Weak answer.** "The director should stop all technical work." Some hands-on exposure is legitimate;
the problem is the share and the choice of work that substitutes for the director's own decisions.

## F3 — A tech lead definition for Northstar

**One paragraph.** "The tech lead is a senior or staff engineer accountable for the technical
decisions of one team: how the team's work is designed and broken down, which technical risks are
taken, and what the team's components must meet to be operable. The tech lead decides within the
team's scope and the engineering standards, and escalates cross-team decisions to the relevant staff
engineer. Horizon: the next few weeks to the current quarter. Primary output: sound technical decisions
that the team executes, and engineers who can make them without the tech lead. The engineering manager
remains accountable for people (hiring, growth, performance), delivery commitments, and team health;
the two agree priorities together and the manager arbitrates if they disagree on staffing."

**One per team?** Not mechanically. A tech lead per team of six to ten engineers (this book's
recommendation) suggests Customer Experience, with nine web and six mobile engineers, may need two, one per platform,
while Data and Analytics (11) may need one. A team with no candidate should not invent one; the
manager and a staff engineer cover the gap while someone grows into the role.

**Criteria.** Clear decision rights, a stated boundary with the manager, and a link to the staff
engineers. **Weak answer:** a definition that lists tasks ("runs stand-ups, reviews code") with no
decision rights.

## A1 — Rafael Duarte's track question

**What to learn first.** What he wants to be accountable for, in his words; which parts of his
current work energize and drain him; what he has already tried (has he given hard feedback, run
one-on-ones, led a decision across teams?); and why now. Because he lost the Orders manager role to Priya Raman and
said nothing about his career afterwards (Chapter 2), ask directly how he sees that decision now: is he
drawn to managing, or to the title he was refused? Ask what he has learned from the review ownership
of core/order-capture he has held since week 2.

**What you can honestly offer.** No manager opening exists and Priya is staying, so a management
role is not on the table this quarter. The staff role has no definition, so you cannot
promise a target. Say both plainly. What you can offer: a formal tech lead role for core/order-capture,
which extends the review ownership he already holds, if Northstar adopts the definition from F3, and a management trial that does not
need an open team, such as leading a two- or three-person project with one-on-ones for a new hire, or
acting manager during a planned absence, with written terms (length six to twelve months, evidence to
be reviewed, return role).

**What to fix in the organization.** Define the tech lead and staff roles (scope, sponsor, outputs),
and state a return path from management. Without those, the conversation is advice, not a choice.

**Criteria.** The answer starts with questions, is honest about constraints, offers a trial with
terms, and recognizes the organizational defect.

**Weak answer.** Recommending a track on the strength of his technical record (the Peter Principle
error Benson and colleagues describe in another setting), or offering management as consolation for
the earlier decision. A trial must not put him in competition with Priya inside Orders.

## A2 — Reviewing the six managers

**Evidence for two managers.**

| Area | Marcus Oyelaran, Billing | Priya Raman, Orders |
|---|---|---|
| Unit outcomes | Billing's incidents, recurrences, and unplanned work against the quarter-1 plan, read with the release train's change | Orders' incidents and delivery of the bulk-ordering commitment, in context |
| Team health | On-call pages per person (three people carried most); regretted attrition; anonymous upward feedback | Same, plus whether she still owns technical work she should have handed off |
| People growth | Who can now handle ledger incidents who could not; a credible successor | Whom she has developed in her first year as manager |
| Leverage | Ownership of core/scheduler taken on in week 4; corrective actions closed | Ownership of core/customer taken on; cross-team decisions that held |

**Separating manager from system.** For each outcome, ask which mechanism moved it. A fall in
Billing's release-borne incidents after weekly Core releases is mostly the release train's change; a
spread of on-call load from three people to more would be the manager's.

**Avoiding ranking.** Review each manager against their own context and agreed goals, write the
review with the manager, and calibrate only promotion decisions across managers (Chapter 8).

**Criteria.** Evidence in all four areas, explicit attribution, and a horizon of two quarters.
**Weak answer:** a single scorecard applied identically to all six and sorted.

## A3 — Mandates for the staff engineers

**One defensible proposal.** Each scope turns the first quarter's transformation mandate (Chapter 27)
into standing ownership that outlasts the quality program.

| Staff engineer | Scope | Sponsor | Two outcomes for two quarters |
|---|---|---|---|
| Kwame Mensah | Reliability and delivery pipelines across tier 1 | Director | All 15 tier 1 components meet the four operational minimums; one pipeline path for Core with automated rollback |
| Ines Carvalho | Core architecture and its shared modules | Director, with the Orders and Billing managers | A decided owner and interface plan for core/permissions; a staged plan for core/customer within no-rewrite constraints |
| Li Na Zhou | Data integrity, migrations, configuration | Director | Migration rehearsal and checks used by every tier 1 data change; reconciliation design for invoice correctness |

**Reporting.** Keep them reporting to the director for now: there is no manager-of-managers layer,
their scopes cross teams, and the director needs their signal. Revisit if a senior-manager layer is
created.

**Disagreements.** Inside the staff engineer's domain (a standard, an architecture decision), the
staff engineer decides, within the ten-day rule, and the manager may escalate to the director with a
written case. On staffing and delivery dates, the manager decides. Both record the decision.

**Criteria.** Outcomes, not activities; scopes that do not overlap; a disagreement rule. Chapter 29
develops the archetypes. **Weak answer:** "advise the teams on best practice", which is the
mandate-less role again.

## X1 — A VP Engineering for Northstar?

**Recommendation.** Not now. With 80 engineers, six managers, and one director, a VP above the
director would add a layer with no distinct decisions: the VP and director would share one
organization, one portfolio, and one set of managers. The ladder's title-inflation failure mode
applies: the role would later block hiring for a real need or force an awkward restructuring.

**If created anyway,** it must have decisions the director does not: the full engineering portfolio
and budget, the leadership bench across several directors, and engineering's place in company
planning. That presupposes more than one director, which Northstar does not have.

**Instead.** Address Victor's real needs. If the board expects a named engineering leader below the
CTO, clarify the director's scope and title publicly. If Victor wants time for technical strategy,
delegate operating decisions to the director in writing (budget within limits, staffing, operating
reviews) and give the staff engineers a strategy role that reports into his agenda. Revisit when
engineering approaches two directors' worth of organization.

**Criteria.** The answer ties the role to decisions, not to market convention, and offers an
alternative that meets the underlying need. Larson's observation that titles are used inconsistently
supports defining the role by responsibility.

**Weak answer.** Creating the role because peer companies have one.

## X2 — Evaluating the director after a year

**Evidence and weights.** Victor should judge over the full year, with the trend more than the
endpoint, across the four areas scaled up.

- **Organizational outcomes:** incidents, availability against 99.9 percent, service credits, and
  the renewal commitments, read with their mechanisms (release train changes, ownership, detection).
  A fall in incidents is good evidence only if mechanism measures moved too.
- **Health:** regretted attrition across engineering. One strong manager leaving is a signal to
  investigate (exit interview, upward feedback), not a verdict.
- **Bench:** are the six managers stronger, is there a successor for the director, are tech leads
  emerging?
- **Leverage and clarity:** two staff engineers unsure of their mandate is a defect the director owns,
  and the evaluation should say so.

**Separating director from system.** Ask which decisions the director made (allocation, ownership,
the release cadence, the QA transition) and whether the outcomes moved where those decisions should
have moved them, and when. Credit external luck and penalize unaddressed drift separately.

**Criteria.** Multi-area, year-long, mechanism-aware, and explicit about the staff-mandate gap.
**Weak answer:** "incidents fell, so the director succeeded", or the reverse from one departure.

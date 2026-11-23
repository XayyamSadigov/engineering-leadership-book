# Performance improvement plan

**Used in:** [Chapter 9](../parts/02-people-management/09-performance-management-and-underperformance.md)
(performance management and underperformance), [Chapter 6](../parts/02-people-management/06-feedback-conflict-and-difficult-conversations.md)
(the conversations that come before it), [Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)
(when the person underperforming is a manager).
**Owner:** the manager writes and runs the plan; HR reviews it before it starts; the person receives
every version and every weekly note.
**Cadence:** written only after specific feedback has not closed the gap within a few weeks; runs six to
ten weeks with a written check-in every week; ends with a recorded decision on the end date.

A [performance improvement plan](../glossary.md#performance-improvement-plan-pip) (PIP) is a short,
dated, written agreement that states the gap between what someone's role requires and what they deliver,
the expectations that would close it, the support the manager provides, and what happens at the end. Its
purpose is to find out, fairly, whether the person can meet the bar with support. A plan that both sides
read as the first step of an exit cannot do that. Many teams use a lighter first stage, an expectations
agreement with HR informed but not running it, and move to a formal plan only if that stage fails; this
template serves both.

## How to fill it in

1. **Check that this is not the first time.** The person has heard the concern, with examples, and was
   told plainly that it is serious. If not, have that conversation first and restart the clock.
2. **Diagnose the cause** before writing anything: system (overload, access, unclear ownership), skill,
   will, or role fit. Compare with peers who have the same load and tools.
3. **Remove system causes first**, or write the plan so that it measures the system too.
4. **Write four to six expectations a third party could check**: the outcome, not the activity; the level
   set against the person's level and peers; the evidence both sides will look at.
5. **Write the manager's support** as commitments with dates: protected time, a pairing partner,
   training. A plan whose support is not delivered is void.
6. **Set the end date** six to ten weeks out, and write both outcomes now: what closes the plan, and what
   happens if it is not met (a role change if a real one fits, or an exit).
7. **Involve HR**, and through HR employment counsel, before the plan starts. Stop and take advice if a
   health, disability, family, or other protected circumstance appears.
8. **Hold a weekly check-in** and write the note the same day: each expectation met or not, with
   evidence; the support delivered. Share the note with the person.
9. **Decide on the end date** against the written criteria, record the decision, and say it out loud,
   including when the plan succeeds.

## Template

| Field | Contents |
|---|---|
| Person, role, level, manager | |
| Stage | Expectations agreement (HR informed) or formal plan (HR involved) |
| Earlier feedback | Dates and content of the conversations that came before |
| The gap | Expectation, result, dates, examples; facts, not adjectives |
| Cause found | System, skill, will, or role fit, with the evidence |
| System changes made first | What the manager changed before the plan started |
| Expectations | Four to six, each with the evidence that will show it met |
| Manager's support | Commitments with dates |
| Weekly check-ins | Day and time; who writes the note |
| End date and outcomes | Date; what closes the plan; what follows if it is not met |
| Team effects | What colleagues are told, and how work they absorbed is rebalanced |

```yaml
plan:
  person: ""
  role_level: ""
  manager: ""
  stage: ""                    # expectations agreement / formal plan
  hr_contact: ""
  earlier_feedback: []         # {date, summary}
  gap: ""
  cause: ""                    # system / skill / will / role fit, with evidence
  system_changes: []
  expectations:
    - {expectation: "", evidence: ""}
  support:
    - {commitment: "", due: ""}
  start: ""
  end: ""
  outcome_if_met: ""
  outcome_if_not_met: ""
weekly_notes:
  - {week: 0, met: [], not_met: [], support_delivered: [], shared_with_person: true}
decision: {date: "", result: "", reasons: ""}
```

## Example: Northstar, Tom Becker's draft for Bram Verhoeven

!!! info "Northstar so far"
    Week 14 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Tom Becker manages Platform Operations, now five infrastructure engineers since the seven QA
    engineers moved to product teams in week 10. Bram Verhoeven, a Senior Engineer there for six years,
    built Core's Jenkins pipeline. See the [timeline](../case-studies/northstar/timeline.md) and the
    [cast](../case-studies/northstar/cast.md).

For three quarters Bram's tickets aged and a Jenkins upgrade he owned slipped three times. Tom quietly
moved 31 of his 74 tickets in the baseline quarter to two colleagues, and Bram's last annual review said
"meets expectations". A reconstruction of six weeks showed nearly half his hours went to unassigned Core
pipeline interrupts, and the tickets he let age were mostly for a CI system he had never been trained on.
He had also stopped believing his planned work mattered after his build-consolidation proposal was
shelved. The director's decision on Tom's draft is not recorded.

| Field | Tom's draft |
|---|---|
| Stage | Expectations agreement, HR informed, not running it; a formal plan only if eight weeks do not close the gap |
| Earlier feedback | None in writing; the last review said "meets expectations", so any record begins now |
| The gap | Assigned tickets aging silently; the Jenkins upgrade postponed three times |
| Cause found | Mainly system (unassigned interrupts) and skill (an untrained CI system), with a will component after the shelved proposal |
| System changes made first | Core Jenkins interrupts go to the team's shared intake and rotate; Bram is the escalation point, not the first responder |
| Support | Two weeks pairing with the colleague who knows GitLab CI best; then Bram takes his share of those tickets |
| Expectations, eight weeks, checked weekly | Assigned tickets acknowledged within one working day and answered within two, or handed back with a reason; the Jenkins upgrade planned with a date and done; a written runbook for the Core pipeline |
| Team effects | The two colleagues told the reassignments stop and the situation is being addressed, without details |

What to notice: the draft fixes the system before judging the person, and every expectation can be
checked from the ticket queue or a document. Its weak point is the team: rotating the interrupts loads
the other four engineers, two of whom just covered Bram's tickets for nine months.

## Common mistakes

- **The plan as an exit formality.** If the decision is already made, the plan is dishonest and often
  legally risky.
- **Skipping the diagnosis.** A plan for a system problem fails the person and leaves the cause in
  place.
- **Expectations nobody else could judge.** "Be more proactive" can only be judged by the manager who
  already formed a view.
- **Support that never arrives.** The pairing partner is busy and the training is next quarter; the
  person is then measured against a plan the manager broke.
- **Inconsistency.** A plan for a gap another engineer was never told about is unfair and exposes the
  organization.
- **Managing around the problem for months.** Quiet reassignment hides the gap from the person and
  loads the people who absorb it.

## Review questions

1. When and how was the person first told, in specific terms, that the gap is serious?
2. Which cause did you rule out, and with what evidence?
3. Could someone who does not know the person tell at the end whether each expectation was met?
4. Which support commitment is behind schedule this week?
5. What happens on the end date if the plan is met, and has the person heard you say it?

## Evidence and references

The method is [Chapter 9](../parts/02-people-management/09-performance-management-and-underperformance.md);
the conversations that precede a plan are Chapter 6.

- [Pulakos and O'Leary, 2011](../references/bibliography.md#pulakos2011broken): performance management
  reduced to formal steps, disconnected from the daily guidance that decides whether it works; a position
  paper (**expert opinion**).
- [Mager and Pipe, 1997](../references/bibliography.md#mager1997analyzing): known for the test of a skill
  gap (could the person do it if their job depended on it?) and for diagnosing before acting (**expert
  opinion**).
- [Gilbert, 1978](../references/bibliography.md#gilbert1978human): known for the argument that most
  performance deficits come from the environment rather than the individual (**expert opinion**).

The four causes, the five properties of a fair plan, and the six-to-ten-week length are **this book's
recommendation**. Employment law differs by country and contract; this template is not legal advice.

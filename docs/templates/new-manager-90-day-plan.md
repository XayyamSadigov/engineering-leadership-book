# New manager's 90-day plan

**Used in:** [Chapter 2](../parts/01-foundations/02-from-individual-contributor-to-leader.md) (from
individual contributor to leader), [Chapter 5](../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md)
(first one-on-ones), [Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)
(the manager's manager, who agrees the plan).
**Owner:** the new manager writes it; their own manager agrees the day-90 criteria and the time budget
and checks them monthly.
**Cadence:** written in the first two weeks of a new management role; reviewed at days 30, 60, and 90;
closed with a written report against the day-90 criteria.

A new manager's 90-day plan turns a promotion into a deliberate transition. It lists the engineering work
the new manager hands over, agrees what success looks like at day 90 and a weekly time budget, and
sequences three phases: learn (days 1 to 30), delegate (30 to 60), and check (60 to 90). Use it for every
first-line manager, especially one promoted from inside the team, because the engineer's fast feedback
loop is still available and still rewarding, and without a plan the new manager drifts back into the
old job.

!!! tip "Minimum version"
    In week 1, write three things: the handover list with a new owner for each item, three day-90
    criteria agreed with your manager, and a weekly time budget with a cap on hands-on work. Add the
    delegation levels and leading indicators by day 30.

## How to fill it in

1. **List everything assigned to you as an engineer** (reviews, on-call, follow-up actions, features) and
   give each a new owner who agrees, or close it.
2. **Agree the day-90 criteria** with your manager in writing: three to five observable outcomes, not
   "settled in".
3. **Agree a weekly time budget** with a cap on hands-on work and some unallocated hours, because
   escalations will fill the week. Keep hands-on work off the critical path.
4. **Days 1 to 30, learn.** A first [one-on-one](one-on-one.md) with every report (what they want, what
   gets in their way, what you should not change); a map of
   [single-person areas](../glossary.md#single-point-of-knowledge-failure), including yourself; last
   quarter's incidents and escaped defects for your components.
5. **Days 30 to 60, delegate.** Two outcomes delegated at an explicit level of control, with checkpoints
   and dates. Two owners for every area where you were the required reviewer. One visible change in how
   the team works, chosen from what the one-on-ones raised.
6. **Days 60 to 90, check.** Count the leading indicators (decisions waiting for you, single-person areas,
   one-on-ones held), compare your calendar with the budget, and ask your reports what you should do more
   of and less of.
7. **Report at day 90** against the criteria, including what has not worked.

The five levels of control: 1, you decide; 2, the delegate recommends and you decide; 3, the delegate
decides after telling you; 4, the delegate acts and informs you; 5, the delegate owns the area.

## Template

| Field | Contents |
|---|---|
| Manager, team, start date | |
| Own manager | Who agrees the criteria and checks the budget |
| Handover list | Each engineering item, its new owner, and the date |
| Day-90 criteria | Three to five observable outcomes |
| Weekly time budget | Hours by activity, the hands-on cap, unallocated hours |
| Days 1 to 30: learn | One-on-ones, single-person map, incident and defect review, a peer manager to learn from |
| Days 30 to 60: delegate | Two delegations with level, checkpoint, and date; reviewer owners; one visible change |
| Days 60 to 90: check | Leading indicators; calendar against budget; feedback from reports |
| Day-90 report | Date and audience |

```yaml
plan:
  manager: ""
  team: ""
  start: ""
  own_manager: ""
handover:
  - {item: "", new_owner: "", agreed: false, date: ""}
day_90_criteria: []
time_budget:
  hands_on_cap_hours: 0
  unallocated_hours: 0
  activities: []               # {activity, hours}
delegations:
  - {outcome: "", owner: "", level: 0, checkpoint: "", due: ""}
leading_indicators:
  decisions_waiting: 0
  single_person_areas: 0
  one_on_ones_held_of_scheduled: ""
checks: {day_30: "", day_60: "", day_90: ""}
```

## Example: Northstar, Priya Raman's reset in week 2

!!! info "Northstar so far"
    Week 2 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Priya Raman has managed Orders, 14 engineers, for eight months, promoted from inside the team
    without management training. Orders owns bulk ordering, a feature promised to a renewal customer for
    the end of quarter 2. See the [timeline](../case-studies/northstar/timeline.md). New to Northstar?
    Read [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Priya never had a 90-day plan, so this example shows the plan as a reset she and the director could
write in week 2 (weeks count from the director's first week). The calendar figures, the four changes, and their levels come from the case; the layout
and the day-90 criteria are illustrative. In her first month a bulk upload failure reached customers;
she fixed it herself and assigned the follow-up test to herself. It was never done, and the same failure
returned as INC-421, a Sev1 in which a bulk upload dropped every line beyond row 500.

| Weekly hours | Before (measured) | Agreed budget |
|---|---|---|
| Coding and code review | 18 | 8 (cap) |
| One-on-ones | 2 (about a third held) | 4 |
| Coaching delegated work | 0 | 4 |
| Unallocated | 0 | 5 |
| Everything else (product, incidents, planning, hiring, feedback, admin) | 20 | 19 |
| **Total** | **40** | **40** |

| Handover and delegation | Owner | Level |
|---|---|---|
| Implementation lead for bulk ordering | Aisha Bello (Senior Engineer) | 3: tells Priya before any API or schema change; weekly design checkpoint |
| Review ownership for core/order-capture | Rafael Duarte and Aisha Bello (Senior Engineers) | 4: Priya reviews a sample of their reviews for a month |
| The open bulk-upload test action | Rafael Duarte | 4, due before the next Core release with upload changes |

| Day-90 criteria (illustrative) | Evidence |
|---|---|
| Hands-on work at or below 8 hours a week | Calendar and review history |
| No Orders decision waits more than two days for Priya | Count of decisions waiting, checked monthly |
| Two reviewers other than Priya for every Orders component | Review history |
| One-on-ones held as scheduled | The one-on-one record |

What to notice: the plan hands over the riskiest item, the renewal feature, while there is still a long
runway, and Priya keeps design authority through the weekly checkpoint. The time budget is the measure
to watch: Northstar's record shows her hands-on time at 8, 10, and 12 hours at the week 16, 20, and 24
checks, which a monthly check against the cap makes visible early.

## Common mistakes

- **Keeping the hardest work.** The team learns that hard problems belong to the manager, and every
  meeting stops the critical path.
- **Being the required reviewer.** Every change waits for the busiest person on the team.
- **No unallocated time.** A budget with no slack is broken by Tuesday, and the hours lost are usually
  one-on-ones.
- **Delegating without a level.** "Take this" leaves the delegate guessing what they may decide.
- **Day-90 criteria that cannot be checked.** "Settled into the role" cannot fail.
- **Fixing it yourself over the weekend.** The follow-up action then has no owner who has time for it.

## Review questions

1. Which item from your engineering job still has your name on it?
2. Which decision waited for you this week, and should it have?
3. How many hours of hands-on work did you do last week, against the cap?
4. Which delegation's level is unclear to the person holding it?
5. What did your reports say you should do less of?

## Evidence and references

The method is [Chapter 2](../parts/01-foundations/02-from-individual-contributor-to-leader.md).

- [Hill, 2019](../references/bibliography.md#hill2019becoming): *Becoming a Manager* follows nineteen new
  managers through their first year; the publisher's summary presents the move as a psychological
  adjustment learned mainly from experience.
- [Watkins, 2003](../references/bibliography.md#watkins2003first): *The First 90 Days*, known for
  deliberate learning, explicit expectations with one's own manager, and early wins in a transition
  (**expert opinion**, written for executives).
- [Yukl and Fu, 1999](../references/bibliography.md#yukl1999determinants): the abstract reports that
  managers delegated more to competent subordinates and were reluctant to give up control over important
  decisions (**research finding**). It is why the plan delegates important work at level 2 or 3 rather
  than withholding it.
- [Fournier, 2017](../references/bibliography.md#fournier2017manager): *The Manager's Path*, known for
  staying close enough to the technology to judge while staying off the critical path (**expert
  opinion**).

The three phases, the time budget, and the day-90 report are **this book's recommendation**.

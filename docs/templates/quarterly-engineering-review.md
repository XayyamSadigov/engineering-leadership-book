# Quarterly engineering review

**Used in:** [Chapter 37](../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md)
(the quarterly cadence), [Chapter 38](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
(scorecards and capacity allocation), [Chapter 39](../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md)
(reviews and executive reporting).
**Owner:** the engineering director; each manager supplies the team section.
**Cadence:** once a quarter, in the last two weeks of the quarter, before next quarter's planning.

The quarterly review compares what the organization said it would do with what happened, explains
the difference by mechanism, and ends with decisions for the next quarter. It is not a status
meeting and not a celebration. A review that produces no decision, no changed allocation, and no
retired [scorecard](../glossary.md#scorecard) measure has been run as a ritual. Keep the document to
about four pages; the first page is the executive summary and is the only page some readers will see.

!!! tip "Minimum version"
    For the first review, write one page: last quarter's commitments copied verbatim, five scorecard
    measures with a one-line reading, what went wrong, and at most three decisions for next quarter. Add
    capacity plan against actual and the team sections the following quarter.

## How to fill it in

1. Copy the commitments and targets from last quarter's review verbatim, before looking at results.
   Rewriting them afterwards is the most common way a review stops being honest.
2. Pull the scorecard from systems, not from managers' summaries. Mark any figure that depends on
   human classification and say whether it was audited.
3. For each measure that moved, state the mechanism you believe moved it and the evidence. "The
   team worked hard" is not a mechanism.
4. Put the capacity plan next to the capacity actuals. Unplanned work that came in above plan is
   the usual reason commitments slipped; show it rather than explain it away.
5. List what went wrong as plainly as what went right, with the response.
6. End with decisions: each with an owner, a date, and the option you recommend.
7. Circulate two working days before the meeting. The meeting discusses the decisions, not the data.

## Template

Page one, the executive summary:

```markdown
## Quarterly engineering review, <quarter>

**Mandate or objective:** <in the words of whoever set it>
**Headline:** <one sentence: the main result and the main gap>
**Commitments:** <delivered / at risk / missed, with the count>
**Outcome measures:** <three to five, baseline → this quarter → target>
**What we learned:** <two or three mechanisms, with evidence>
**What went wrong:** <named, with the response>
**Capacity next quarter:** <prevention, unplanned, feature; change from this quarter>
**Decisions needed:** <numbered; owner, date, recommended option>
```

Machine-readable header, kept with the review so that next quarter can diff it:

```yaml
review:
  quarter: ""                 # for example 2027-Q1
  prepared_by: ""
  circulated: ""              # date
  meeting: ""                 # date
  attendees: []
  previous_review: ""         # link
capacity:
  engineers: 0
  unplanned_pct_plan: 0
  unplanned_pct_actual: 0
  prevention_fte_plan: 0
  prevention_fte_actual: 0
commitments:
  - {item: "", team: "", due: "", status: ""}   # on track / at risk / delivered / missed
decisions_needed:
  - {id: D1, question: "", owner: "", due: "", recommendation: ""}
```

Sections after page one:

| Section | Contents | Source |
|---|---|---|
| Scorecard | Each measure: baseline, last quarter, this quarter, target, paired measure, audit note | [Engineering quality scorecard](engineering-quality-scorecard.md) |
| Commitments | Each committed item: team, due date, status, reason for any slip, classified (scope growth, dependency, displaced by incidents, deprioritized) | Planning record |
| Capacity | Plan against actual: unplanned, prevention, feature, by team | [Capacity planning model](capacity-planning-model.md) |
| Incidents and risk | Sev1 and Sev2 count, recurrences, customer-detected share; top risks with owner and trend | Incident tracker, risk register |
| People | Attrition (regretted or not), open roles, promotions, on-call concentration | HR system, paging tool |
| What went wrong | Each event, the mechanism, the response, whether the response is complete | Reviews |
| Decisions | Numbered, as in the header | |

## Example: Northstar, end of quarter 1

!!! info "Northstar so far"
    Week 13 of the Engineering Director's first year at Northstar Technologies, a fictional company with
    80 engineers. In quarter 1 the director named Core's release train as the main source of incidents,
    moved Core to weekly releases, published severity definitions, and agreed a
    [prevention allocation](../glossary.md#prevention-allocation) of 12 FTE. See the
    [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Figures come from the [day-90 results](../case-studies/northstar/first-quarter.md#day-90). Quarter 1
roadmap delivery by item is not recorded, so it is left out rather than invented. Weeks count from the
director's first week.

**Mandate:** halve Sev1 and Sev2 incidents and meet the 99.9 percent commitment within twelve
months, with no net headcount growth, keeping the two renewal commitments.

**Headline:** Sev1 and Sev2 incidents fell from 30 to 21 and Core releases went weekly; unplanned
work fell only from 34 to 31 percent, so most of the capacity payback is still ahead.

**Commitments:** both renewal commitments on track (accounting integration due week 19, bulk
ordering due week 26); neither was due in quarter 1.

| Measure | Baseline quarter | Quarter 1 | Reading |
|---|---|---|---|
| Sev1 and Sev2 incidents | 30 | 21 | −30 percent; the twelve-month goal is 15 or fewer |
| of which via Core releases | 9 | 4 | The named constraint is moving |
| Recurrences | 11 of 30 | 5 of 21 | 37 → 24 percent |
| [Customer-detected share](../glossary.md#customer-detected-share) | 47% | 29% | Severity audited weekly from week 7 |
| Core releases | 2 per month | 11 in the quarter | Weekly from week 5 |
| Core change failure rate | 31% | 22% | Paired with release frequency |
| Core main branch red | 22% | 9% (last four weeks) | 140 flaky tests quarantined |
| Corrective action closure | 32% | 70% (26 of 37) | Every kept action has a manager owner |
| Tier 1 at four operational minimums | 3 of 15 | 8 of 15 | Runbooks 11 of 15 |
| Open critical vulnerabilities | 11 (3 [known-exploited](../glossary.md#known-exploited-vulnerability-kev)) | 3, under recorded exceptions | 1 known-exploited, mitigated |
| Unplanned work | 34% | 31% | Plan was 33% |

**Capacity, plan against actual** (80 engineers; actual prevention assumed equal to plan, since it
was allocated by team and not tracked separately):

| FTE | Plan | Actual |
|---|---|---|
| Unplanned work | 26.4 (33%) | 24.8 (31%) |
| Prevention | 12 | 12 |
| Feature capacity (the remainder) | 41.6 | 43.2 |

The 1.6 FTE above plan is within the sampling error of a two-week ticket sample, so the review does
not bank it.

**What we learned.** The release train was the constraint: train-triggered incidents fell from 9 to
4 once releases were weekly and smaller. Severity definitions are read creatively under scorecard
pressure: four consecutive Sev3 ratings in week 7 included a two-hour payment delay for nine
customers.

**What went wrong.**

| Event | Mechanism | Response | Complete? |
|---|---|---|---|
| Week 9 Sev1, credit notes applied twice | Migration and dependent code in one release; the promised pipeline check had slipped from week 7 | Interim rule, then the check landed in week 11 | Yes |
| QA transition anxiety | Plan existed but was announced in week 10 | Announced with each engineer's destination team | Late; noted for the director's own review |
| Severity under-rating in week 7 | Pressure from the scorecard | Re-rated; severity audit added to the weekly review | Ongoing |

**Decisions needed for quarter 2:**

| ID | Question | Owner | Due | Recommendation |
|---|---|---|---|---|
| D1 | Owner for core/permissions, still under a recorded exemption | Director | Before the exemption expires | Decide by quarter 2's end; Priya Raman accepts it after week 26 |
| D2 | Fund the deployment-event store (about six engineer-weeks) from the prevention allocation | Director, Tom Becker | Week 14 | Fund it: delivery numbers still take two days a month by hand |
| D3 | Prevention allocation in quarter 2 | Director, Victor Lindqvist, Amara Okafor | Week 14 | Hold at 12 FTE as agreed; re-check unplanned work monthly |

## Common mistakes

- **Rewriting targets after the fact.** Copy them first, then look at the results.
- **Reporting activity as outcome.** "140 flaky tests quarantined" is a mechanism; "main branch red
  9 percent" is the result it bought. Show both, labeled.
- **Banking noise.** A 1.6 FTE improvement measured by a two-week sample is not yet capacity you can
  commit.
- **Decisions without owners or dates.** A list of concerns is not a decision list.
- **Leaving out the director's own mistakes.** If the review names only teams' failures, the teams
  will stop reporting theirs.

## Review questions

1. Which commitments changed after they were made, and who agreed to the change?
2. For each measure that improved, what is the evidence for the mechanism we credit?
3. Which classified figures (severity, unplanned work, defect origin) were audited, and how?
4. Where did capacity go that the plan did not expect?
5. What will we stop next quarter to fund what we start?

## Evidence and references

The method is in [Chapter 37](../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md)
(the quarterly cadence) and Chapter 39 (executive reporting).

- [Grove, 1983](../references/bibliography.md#grove1983high): meetings as managerial work, and reviews
  as the place where decisions are made (**expert opinion**).
- [Stasser and Titus, 1985](../references/bibliography.md#stasser1985pooling) and
  [Lu, Yuan, and McLeod, 2012](../references/bibliography.md#lu2012hiddenprofiles): their abstracts
  report that groups underuse information only some members hold (**research finding**), the case for a written pre-read circulated
  before the meeting.
- [Campbell, 1979](../references/bibliography.md#campbell1979assessing): the source usually credited
  for the problem of indicators that become targets, which is why classified figures are audited.

The four-page limit, the order of the sections, and copying targets before reading results are
**this book's recommendation**.

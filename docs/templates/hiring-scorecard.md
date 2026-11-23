# Hiring scorecard and interview kit

**Used in:** [Chapter 7](../parts/02-people-management/07-hiring-and-structured-interviews.md) (hiring
and structured interviews), [Chapter 48](../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md)
(workforce planning, where backfills are decided).
**Owner:** the hiring manager writes the scorecard with two engineers from the team; a facilitator from
another team runs the debrief; the recruiter keeps the kit and the post-hire check dates.
**Cadence:** one scorecard per role, written before the first candidate; reused for every candidate in
that search; checked against each hire at six and twelve months; reviewed yearly.

A hiring scorecard says what a role must achieve in its first year and which attributes that requires.
The interview kit maps each attribute to the session that measures it, with questions, rubrics, and a
decision rule agreed before the first candidate. Together they make a
[structured interview](../glossary.md#structured-interview): every candidate gets the same questions,
scored on the same scale, against the same attributes. Use it for every hire and every backfill,
because the common alternative, a loop that ends with "would I work with this person", measures the
interviewers' confidence more than the candidate.

!!! tip "Minimum version"
    For the next search, write three first-year outcomes, four attributes with the must-haves marked, the
    session that measures each, and a decision rule, all before the first candidate. Add full rubrics, the
    debrief protocol, and the six-month check before the second search.

## How to fill it in

1. **Write three to five first-year outcomes** with two engineers from the team. For a backfill, start
   from what the leaver actually did, including on-call and the work nobody wrote down.
2. **Derive four to six attributes** those outcomes require. Mark which are must-haves. An attribute is
   observable ("changes a schema on a live database safely"), not a trait ("strong engineer").
3. **Map attributes to sessions.** Each session measures one or two named attributes; must-haves are
   measured twice, by different people.
4. **Build the work sample** from realistic material in your own codebase, secrets removed, doable well
   in 60 to 90 minutes. Try it on two current engineers before any candidate sees it.
5. **Write a rubric per attribute**: what a poor, borderline, solid, and outstanding answer looks like,
   with an example of each.
6. **Set the decision rule** before the first candidate, for example "no must-have below solid, and at
   least two attributes outstanding or solid with evidence". Share it with the panel.
7. **Run the debrief by protocol.** Each interviewer rates alone and submits notes before seeing anyone
   else's. The facilitator reveals all ratings together, discussion goes attribute by attribute, and the
   hiring manager speaks last. Keep the original ratings.
8. **Set the six-month check** when the offer is accepted: two people rate the hire against the same
   scorecard, plus time to first independent production change and, where the role has it, time to
   joining on-call.

## Template

**The scorecard**

| Field | Contents |
|---|---|
| Role and level | Title, level, team, location, and whether it is a backfill |
| First-year outcomes | Three to five, each observable at twelve months |
| Attributes | Four to six; must-haves marked |
| What the job really involves | On-call, the hard parts, what the leaver did that nobody listed |
| Decision rule | Agreed before the first candidate |
| Post-hire check | Six- and twelve-month dates; who rates; which milestones |

**The interview kit**

| Session | Length | Attributes measured | Interviewer | Questions or task | Rubric link |
|---|---|---|---|---|---|

**One rubric row per attribute**

| Attribute | Poor | Borderline | Solid | Outstanding |
|---|---|---|---|---|

```yaml
role: {title: "", level: "", team: "", backfill: false}
outcomes: []                 # three to five, observable at twelve months
attributes:
  - {name: "", must_have: true, sessions: []}
sessions:
  - {name: "", minutes: 0, attributes: [], interviewer: "", material: ""}
decision_rule: ""
debrief: {facilitator: "", hiring_manager_speaks: last, originals_kept: true}
candidate_ratings:           # one block per candidate, written before the debrief
  - {interviewer: "", attribute: "", rating: "", evidence: ""}
post_hire: {six_month: "", twelve_month: "", milestones: []}
```

## Example: Northstar, the next Billing ledger backfill

!!! info "Northstar so far"
    Week 14 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Billing has the most incidents, and three ledger engineers carry most of its on-call pages. The last
    ledger backfill took 15 weeks and, about 24 weeks after starting, the new hire was not yet on call.
    See the [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Before the director arrived, each manager ran a loop of an algorithm puzzle, an unstructured "team chat",
and a manager conversation, with a debrief in which the hiring manager spoke first. Nobody had written
down that a ledger role needed money movement, rounding, or on-call, so no session measured them. In week
14 the director proposes running the next two backfills as a structured pilot; whether it goes ahead is
not recorded. Marcus Oyelaran is the Billing manager. The scorecard and costs below are illustrative.

| Field | Entry |
|---|---|
| Role | Billing ledger engineer; backfill |
| Attributes | 1. Correctness of money movement (idempotency, rounding, double-entry), must-have. 2. Safe schema change on a live database, must-have. 3. Diagnosing a production failure. 4. Working across team boundaries. 5. Code quality in a large Java codebase |
| What the job involves | Joining the Billing on-call rotation for ledger incidents; period close; migrations on a shared schema |
| Debrief | Facilitator from another team; Marcus speaks last |
| Post-hire check | Six months: two people rate against the scorecard; time to first independent ledger change and to joining on-call |

| Session | Length | Attributes |
|---|---|---|
| Work sample: review a ledger migration with planted defects | 90 min | 1, 2, 5 |
| Debugging on recorded production logs | 60 min | 3, 1 |
| Behavioral interview | 60 min | 4, 2 |
| Hiring-manager conversation | 45 min | 4 |

| Cost, engineer-hours | Hours |
|---|---|
| One loop (4.25 interview, 2.0 write-up, 2.5 debrief) | 8.75 |
| Per hire, steady state (four loops, twelve phone screens) | about 47 (1.2 engineer-weeks) |
| One-time design of scorecard, work sample, and rubrics | about 24 |

What to notice: both must-haves are measured twice, in different sessions, by different people. The
old loop measured neither. At eight backfills a year the steady-state cost is roughly 0.2 of an engineer,
small enough to test even though Northstar has no data yet on how much better the loop selects.

## Common mistakes

- **Writing the scorecard after the interviews.** The attributes then describe the candidate you liked.
- **Traits instead of attributes.** "Smart" and "culture fit" cannot be rated against a rubric.
- **Puzzles as the technical session.** Unfamiliar puzzles under observation measure stress as much as
  skill. Use a work sample from the real job.
- **The hiring manager speaks first.** Later speakers anchor on the first strong view. Ratings go in
  alone and are revealed together.
- **"Will need some ramp" as a debrief note.** A gap found in the loop needs a ramp plan with time
  allocated, or it is a reason not to hire.
- **No post-hire check.** A process that never compares its ratings with later performance cannot
  improve.

## Review questions

1. Which first-year outcome would the leaver recognize from their own work?
2. Which must-have is measured only once, and by whom?
3. Was the decision rule written before the first candidate, and did the panel apply it?
4. In the last debrief, did any rating change after discussion, and was the original kept?
5. At the six-month check, which attribute did hires turn out weakest on, and which session should have
   caught it?

## Evidence and references

The method is [Chapter 7](../parts/02-people-management/07-hiring-and-structured-interviews.md).

- [Sackett et al., 2023](../references/bibliography.md#sackett2023revisiting): structured interviews top
  the revised list of predictors, with a mean validity of .42 and a wide credibility interval
  (**research finding**).
- [Campion, Palmer, and Campion, 1997](../references/bibliography.md#campion1997review): the abstract
  identifies 15 components of interview structure, covering both what is asked and how answers are
  evaluated (**research finding**).
- [Google re:Work](../references/bibliography.md#rework-structured-interviewing): vetted questions,
  recorded feedback, rubrics from poor to outstanding, and interviewer training (**documented
  practice**).
- [Dana, Dawes, and Peterson, 2013](../references/bibliography.md#dana2013belief): unstructured
  interviews produced confident impressions even from random answers, in a student grade-prediction
  task (**research finding**).
- [Lorenz et al., 2011](../references/bibliography.md#lorenz2011social): the abstract reports that
  seeing others' estimates made groups converge and grow more confident, in estimation tasks rather than
  hiring (**research finding**). It is the reason for hidden ratings in the debrief.

No peer-reviewed study tests how well specific software interview formats predict performance. The
work-sample design, the debrief protocol, and the decision rule are **this book's recommendation**.

# Director competency matrix

**Used in:** [Chapter 4](../parts/01-foundations/04-the-leadership-ladder.md) (the leadership ladder),
[Chapter 40](../parts/09-engineering-directorship/40-the-directors-job.md) (the director's job).
**Owner:** the director (self-assessment) and the director's manager (assessment); the two are
compared, not averaged.
**Cadence:** self-assessment every two quarters; formal assessment once a year.

A director leads 50 to 150 engineers through managers. This matrix rates eight competencies on
evidence, for a self-assessment and the manager's assessment. Their output is an organization whose
system produces the outcome, so the matrix assesses that system and the director's part in it,
not the director's personal heroics. Each cell describes evidence someone else could check: a
document, a decision record, a measure, a changed behavior in a manager. A competency without
evidence is rated "No evidence", never filled with impression.

!!! tip "Minimum version"
    For a first self-assessment, rate only the three competencies most at stake this period, each with
    two pieces of evidence and one piece of contrary evidence, and pick one development goal with a
    check. Rate all eight at the formal annual assessment.

## How to fill it in

1. Collect evidence first, for the whole period, from records: reviews, decision logs, scorecards,
   promotion packets, calendars. Do not start from the levels.
2. For each competency, write the two or three strongest pieces of evidence and the strongest piece
   of contrary evidence. A self-assessment with no contrary evidence is not finished.
3. Rate against the level descriptions: **Not yet**, **Solid**, **Strong**. Rate **No evidence**
   when the period holds none, including when the outcome is not yet due; do not rate on intentions.
   The vocabulary matches the [Engineering Manager rubric](engineering-manager-rubric.md).
4. Pick at most two competencies to develop next period, each with one observable change.
5. Share the self-assessment with your manager before their assessment, and discuss the gaps
   between the two, not the average.

## Template

The matrix:

| Competency | Not yet | Solid | Strong |
|---|---|---|---|
| **1. Organizational outcomes** | Reports activity; outcomes move only where the director intervenes personally | Outcome measures agreed with the CTO, baselined, and moving; misses explained by mechanism | Outcomes hold when the director is absent for weeks; teams set and meet their own targets |
| **2. Own signal sources** | Learns of problems from escalations and managers' summaries | Has signals independent of reports (raw incident data, skip-levels, audits of classified figures) and acts on them | Signals are designed into the operating system; others find problems before the director does |
| **3. Developing managers** | Fixes managers' problems for them; no written expectations | Each manager has written expectations, feedback on evidence, and a development goal | Managers handle problems that used to escalate; a successor is identified for each critical role |
| **4. Talent system** | Promotions and pay decided case by case; attrition read from HR dropdowns | Calibrated levels and promotions; structured hiring; attrition analyzed by cause | Regretted attrition and pay gaps fall; hiring outcomes are tracked and improve |
| **5. Organization design and ownership** | Ownership gaps and spans unknown or tolerated | Every tier 1 component owned; spans and dependencies measured; changes carry a transition plan | Structure changes ahead of strain, with triggers stated in advance |
| **6. Capacity and portfolio** | Commitments made without a capacity model; slips explained afterwards | One capacity model agreed with product and the CTO, updated monthly, with a cautious case | Allocation shifts by evidence during the quarter without renegotiating trust |
| **7. Technical decision governance** | Cross-team decisions made in chat or by whoever builds first | Decision owners and rights defined; decisions recorded; standards have owners and deadlines | Decisions hold; reversals are deliberate and cheap |
| **8. Executive and cross-functional partnership** | Advocates for engineering; surprises peers with bad news | Brings trade-offs early, in the peers' terms; answers incidents with mechanism, not names | Peers bring problems to the director before deciding |

Record per period:

```yaml
assessment:
  director: ""
  period: ""                 # for example 2027-Q1 to 2027-Q2
  type: self                 # self or manager
  ratings:
    - competency: ""
      rating: ""             # not_yet, solid, strong, no_evidence
      evidence: []
      contrary_evidence: []
  development_goals:
    - competency: ""
      observable_change: ""
      check_date: ""
```

## Example: Northstar, director self-assessment at the end of quarter 2

!!! info "Northstar so far"
    Week 26 of the Engineering Director's first year at Northstar Technologies, a fictional company with
    80 engineers under six managers. Quarter 1 changed ownership, severity definitions, and the release
    train; quarter 2 delivered the renewal features. The director reports to Victor Lindqvist (CTO). See
    the [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Evidence comes from [the year 1 record](../case-studies/northstar/first-quarter.md) up to the
[quarter 2 results](../case-studies/northstar/first-quarter.md#quarter-2-results); weeks count from the
director's first week. People named:
Daniel Cho, Priya Raman, Elena Sokolova, and Tom Becker are engineering managers; Bram Verhoeven and
Tomasz Wierzbicki are engineers; Amara Okafor is the CPO.

| Competency | Rating | Evidence | Contrary evidence |
|---|---|---|---|
| 1. Outcomes | Solid | Sev1 and Sev2 30 → 21 in quarter 1 and 21 → 17 in quarter 2; Core releases weekly from week 5; unplanned work 34 → 31 → 28 percent | Availability 99.86 percent in quarter 2, below the 99.9 percent contract ($95,000 in credits); Core change failure rate flat at 23 percent in quarter 2 |
| 2. Signal sources | Solid | Re-rated a Sev3 in week 7 and added severity audit; recoded attrition early in quarter 2 and found career conversations and on-call load alongside pay; reviewed Daniel Cho's one-on-ones (84 of 90 held, 55 mainly status) | Delivery numbers still assembled by hand; the deployment-event store is only proposed |
| 3. Developing managers | Solid | Time budget with Priya Raman in week 2 (hands-on capped at 8 hours); six managers trained as incident commanders; every kept corrective action has a manager owner; Elena Sokolova facilitating another team's health check | Tom Becker's plan for Bram Verhoeven was drafted from a reconstruction, after a year of "meets expectations"; succession not yet mapped |
| 4. Talent system | No evidence (first calibrated cycle due in quarter 3) | Ladder rewrite drafted; first calibrated cycle set for the start of quarter 3; six underpaid US Senior Engineers identified; structured hiring pilot proposed | Tomasz Wierzbicki reported an outside offer 20 percent above base in week 20, before any pay correction landed |
| 5. Design and ownership | Solid | Week 4 ownership decisions (core/customer, core/scheduler, auth-svc, webhooks); span and dependency analysis; Billing-owned order-to-invoice contract instead of moving people | core/permissions still under an exemption; document-store orphaned; Orders left with about 2.6 engineers of free capacity |
| 6. Capacity and portfolio | Strong | Capacity model agreed in week 4 with Victor Lindqvist and Amara Okafor, with a cautious case; both renewal commitments on track at day 90; accounting integration live week 19; bulk ordering in final acceptance at week 26 | Prevention spend by team was allocated, not tracked |
| 7. Decision governance | Not yet | Standard owners with a 10-working-day decision rule | Migration check slipped from week 7 to week 11 and a Sev1 came first; [ADR-0001](../glossary.md#adr-0001) (how integrations read ledger data) opened with nobody's decision rights mapped, while the CTO gave a contrary instruction in passing |
| 8. Executive partnership | Solid | Quarter 1 dip agreed with the CPO in advance; answered the CEO's week 9 "who made the change" with the mechanism | QA transition announced in week 10, after anxiety had spread; the CFO's output-per-engineer request still open |

**Development goals for quarters 3 and 4:**

1. *Decision governance:* map decision rights for cross-team technical decisions with Victor
   Lindqvist and the staff engineers, and close ADR-0001 under them. Check: the next three
   cross-team decisions each have a named decider and a record.
2. *Developing managers:* identify interim cover and a development path for each critical role.
   Check: a succession table exists before the year-2 organization proposal.

## Common mistakes

- **Rating the plan.** "Ladder drafted" is not a working talent system. Rate it No evidence.
- **No contrary evidence.** If every row is flattering, the matrix was filled from memory.
- **Rating the director's own work instead of the organization's.** A director who personally
  rescued three incidents has shown the opposite of competency 2.
- **Averaging self and manager ratings.** The gap is the useful information.
- **Too many development goals.** Two, each with a check, beat eight aspirations.

## Review questions

1. Which ratings would a skip-level engineer dispute, and with what evidence?
2. Where did the director act personally when a manager should have?
3. Which competency, if it stayed at its current rating for a year, would most endanger the mandate?
4. What will the director stop doing to make room for the two development goals?

## Evidence and references

The director's job is [Chapter 40](../parts/09-engineering-directorship/40-the-directors-job.md); the
ladder of roles is Chapter 4. The CTO version is the [CTO competency matrix](cto-competency-matrix.md).

- [Grove, 1983](../references/bibliography.md#grove1983high): a manager's output is the output of the
  organization they influence (**expert opinion**), which is why the matrix rates the system, not
  heroics.
- [Larson, 2019](../references/bibliography.md#larson2019elegant): management as system design
  (**expert opinion**).
- [Williamson, 1967](../references/bibliography.md#williamson1967hierarchical): the classic model of
  information lost across layers, behind competency 2 (own signal sources).

The competencies and level descriptions are **this book's recommendation**; no study validates a
director competency model.

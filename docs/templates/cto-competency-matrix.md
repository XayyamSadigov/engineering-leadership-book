# CTO competency matrix

**Used in:** [Chapter 4](../parts/01-foundations/04-the-leadership-ladder.md) (the leadership ladder), [Chapter 50](../parts/12-cto-leadership/50-what-a-cto-actually-does.md) (what a CTO actually does),
[Chapter 55](../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) (boards and executive decision-making).
**Owner:** the CTO (self-assessment) and the CEO (assessment); the two are compared, not averaged.
Where the board reviews executives, the CEO brings the comparison, not the CTO's own ratings alone.
**Cadence:** self-assessment every two quarters; formal assessment once a year, before the operating
plan for the next year is set.

A CTO's output is technology decisions the rest of the company acts on: a strategy the executive team
funds, risks the board understands, a leadership bench that runs engineering without the CTO in the
room. The matrix assesses that output and the CTO's part in it. It extends the
[Director competency matrix](director-competency-matrix.md) one level up, with the same rule: each cell
describes evidence someone else could check (a decision record, a board paper, a budget line, a
succession table, a changed behavior in a direct report). A competency without evidence is rated
"No evidence", never filled with impression.

The CTO title covers different jobs, so the matrix has a weighting step: the same nine competencies
apply to every CTO, but the kind of CTO the company needs decides which ones count most.

!!! tip "Minimum version"
    Write the two-sentence archetype statement, weight the nine rows, and rate only the High-weight
    rows, each with one piece of evidence and one piece of contrary evidence. Add the rest at the
    formal annual assessment.

## How to fill it in

1. **Name the archetype first.** Write two sentences on what the company needs from its CTO in the
   coming year, and mark each competency High, Medium, or Low weight. The CEO does the same
   independently. A disagreement about weights is a disagreement about the job, and it is settled
   before anyone is rated ([Chapter 50](../parts/12-cto-leadership/50-what-a-cto-actually-does.md#archetypes-what-the-company-needs-at-the-top) owns the archetypes and the CTO,
   CIO, and VP Engineering splits).
2. **Collect evidence for the whole period from records,** not memory: board papers, the executive
   team's decision log, budgets and their variances, risk reports, succession tables, the CTO's
   calendar, and what direct reports and executive peers would say. Do not start from the levels.
3. **For each competency, write the two or three strongest pieces of evidence and the strongest piece
   of contrary evidence.** A self-assessment with no contrary evidence is not finished.
4. **Rate against the level descriptions:** **Not yet**, **Solid**, **Strong**, or **No evidence**
   when the period holds none, including when the outcome is not yet due. The vocabulary matches the
   [Director competency matrix](director-competency-matrix.md) and the
   [Engineering Manager rubric](engineering-manager-rubric.md). Do not rate intentions or drafts.
5. **Separate the CTO's work from the organization's.** A result the director's organization produced
   is evidence for the CTO only through what the CTO did: set the mandate, funded it, removed an
   obstacle, held a line with peers. Write that link, or do not count the result.
6. **Pick at most two competencies to develop,** both from the High-weight rows unless a Low-weight
   row is Not yet and dangerous. Each gets one observable change and a check date.
7. **Share the self-assessment with the CEO before their assessment,** and discuss the gaps between
   the two, starting with the weights.

## Template

The matrix:

| Competency | Not yet | Solid | Strong |
|---|---|---|---|
| **1. Company outcomes through technology** | Reports engineering activity; technology goals are engineering's goals | Technology outcomes agreed with the CEO in business terms (revenue protected, cost, risk), baselined, and moving; misses explained by mechanism | Executive peers plan their own goals on the technology outcomes; the CTO's targets survive a bad quarter without being rewritten |
| **2. Technology strategy and direction** | Direction lives in conversations; no written strategy above the director level | A written strategy derived from the business strategy, with choices it says no to and dated decision points; the executive team has funded it | Teams make consistent technology choices without asking; the strategy is revised on its own triggers, not on the CTO's mood |
| **3. Capital allocation and financial stewardship** | Asks for money by function; cannot state what engineering costs per outcome | Investment cases with options, scenarios, and stated assumptions; budget variances explained; capacity presented as capacity, not cash | Finance uses the CTO's numbers without rework; investments are stopped at their checkpoints when the evidence says so |
| **4. Technology risk, security, and compliance** | Learns of technology risk from incidents, auditors, or customers' questionnaires | A technology risk register with owners and treatment decisions, reported to the audit committee or board in their terms; security accountability placed in one named role | Risk appetite is stated and used to decide; the board's questions are answered before they are asked |
| **5. Decision governance at executive scale** | Decides in conversations; overrules in hallways; nobody knows which decisions are the CTO's | Decision rights written down; the CTO's own decisions recorded with options and review triggers; overrules made through superseding records | Decisions below the CTO hold; reversals are deliberate, visible, and cheap |
| **6. Leadership bench and organization** | Direct reports' problems solved by the CTO; no succession for the CTO's reports | Each direct report has written expectations and a development goal; critical roles have interim cover; structure changes come with a transition plan | A ready-now successor exists for each direct report, including the CTO's own role; the organization's shape changes ahead of strain |
| **7. Executive team and board** | Represents engineering's interests; surprises peers and the board with bad news | Brings trade-offs early in the peers' terms; the board receives a technology picture that matches the data | Peers bring problems to the CTO before deciding; the board trusts the CTO's red items |
| **8. Customers and market** | Technology choices made without customer or competitive evidence | Owns the technical relationship with the customers who matter most; feeds what they need into the strategy and the portfolio | Technology is a reason customers buy or renew, and the CTO can show it |
| **9. Own signal sources and operating rhythm** | Learns from the one report below; written reporting irregular | Signals independent of reports (raw incident and delivery data, skip-level conversations, customer calls) on a fixed rhythm; the CTO's calendar matches the High-weight rows | Problems are found by the CTO's system before they reach the CEO; the rhythm runs when the CTO is away |

Record per period:

```yaml
assessment:
  cto: ""
  period: ""                 # for example 2027-H1
  type: self                 # self or ceo
  archetype_statement: ""    # two sentences: what the company needs from its CTO this year
  weights:                   # high, medium, low; agreed with the CEO before rating
    company_outcomes: ""
    strategy: ""
    capital_allocation: ""
    risk_security_compliance: ""
    decision_governance: ""
    leadership_bench: ""
    executive_and_board: ""
    customers_and_market: ""
    signals_and_rhythm: ""
  ratings:
    - competency: ""
      rating: ""             # not_yet, solid, strong, no_evidence
      evidence: []
      contrary_evidence: []
      cto_contribution: ""   # how the CTO's own action links to the evidence
  development_goals:         # at most two
    - competency: ""
      observable_change: ""
      check_date: ""
```

## Example: Northstar, CTO self-assessment in week 48

!!! info "Northstar so far"
    Week 48 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Victor Lindqvist (CTO) has one direct report, the director, and reports to Helena Marsh (CEO). Sev1
    and Sev2 incidents fell from 30 a quarter to 14 in quarter 3; most quarter 4 decisions are drafts.
    See the [timeline](../case-studies/northstar/timeline.md), the [cast](../case-studies/northstar/cast.md),
    and the [quarter 4 briefing](../case-studies/northstar/quarter-4-briefing.md).

You are Victor, filling in the matrix for the year. Work whose outcome is not recorded (the three-year
strategy draft, the enterprise risk register, the year-2 organization, ADR-0001, the week 50 board)
appears as **Pending (not rated)**: a draft is not evidence until it has been decided and acted on.
The ratings and weights are illustrative.

**Archetype statement.** Northstar needs a CTO who sets technical direction for an 11-year-old
order-to-cash platform whose reliability is written into contracts, and who carries the technical
relationship with the largest customers. Corporate IT and the two-person security function report to
Rajiv Menon (CFO), so the infrastructure-manager model does not apply. Who is accountable for security
is an open question this assessment flags and does not answer.

| Competency | Weight | Rating | Evidence | Contrary evidence |
|---|---|---|---|---|
| 1. Company outcomes | High | Solid | Week 1 mandate stated as outcomes; Sev1 and Sev2 30 → 21 → 17 → 14; service credits $410,000 → $60,000 a quarter | 99.9 percent not met in any quarter (99.89 in quarter 3); the results came from the director's organization, and Victor's part is the mandate and the funding |
| 2. Strategy and direction | High | Not yet | A director-level technical strategy from quarter 2. Pending: Victor's three-year strategy draft, weeks 46–48 | No company-level technology strategy adopted in year 1; about 2 of 48 hours a week on strategy; the CI target still open |
| 3. Capital allocation | Medium | Solid | Capacity model agreed in week 4; mandate delivered without headcount growth | Baseline roadmap chosen by points with no value estimates; Rajiv Menon's request to offset the continuation's $150,000 is open |
| 4. Risk, security, compliance | High | Not yet | Commissioned an enterprise risk register after the audit committee chair's week 43 request. Pending: its nine risks and three appetite lines | Estate risks found by the director, not by a register Victor owns; 34 security questionnaires answered ad hoc; no SOC 2 report; no named owner of security across IT and engineering |
| 5. Decision governance | High | Not yet | Week 15 escalation path; the year-2 organization reaches him as a written proposal with a decision date. Pending: reversing his week 14 "read the tables" remark | The week 14 remark landed as an instruction while ADR-0001, the open decision on how integrations read ledger data, had no decider; 3.5 hours a week of unrecorded technical rulings |
| 6. Leadership bench | Medium | Not yet | The director's role has a written definition | Week 44 succession table: 10 critical roles, none with a ready-now successor; no successor for the director |
| 7. Executive team and board | High | No evidence | The week 50 board is the first test in the period | Proposed a "below 10 per quarter" incident headline in week 41 with flat headcount; the draft board page carries his headline and the director's counter side by side |
| 8. Customers and market | High | Solid | Owns the largest customers' technical relationships; both renewal features delivered | Availability below the contractual 99.9 percent; six of the 40 largest customers renew in quarters 5 to 8 |
| 9. Signals and rhythm | Medium | Not yet | Customer relationships, Sev1 bridges, and security reviews about 9 hours a week | 11 informal technical requests in three weeks, 8 of them delegable; the week 26 report was the first written report since day 90 |

What to notice: four of the six High-weight competencies are Not yet or No evidence, and the two Solid
High-weight rows rest mostly on the director's organization. That is competency 6's problem in another
form: Victor's results run through one person with no successor.

**Development goals for quarters 5 and 6:**

1. *Decision governance:* every CTO-level decision in the year-2 cycle recorded with decider, options
   rejected, and a review trigger. Check, week 56: the decision log holds a record for each, and no
   team reports acting on an unrecorded instruction.
2. *Risk, security, compliance:* the enterprise risk register owned at CTO level, with the security
   reporting question put to the CEO and CFO as a decision. Check, week 65: each risk has an owner and a
   recorded treatment, and the reporting option is decided.

## Common mistakes

- **Claiming the director's results.** Engineering outcomes are the CTO's evidence only through the
  CTO's own action; write the link or leave the result out.
- **Skipping the weights.** Without them, a CTO hired as an external-facing technologist is marked down
  for not running infrastructure, and the conversation is about the wrong job.
- **Rating the plan.** A draft strategy, a proposed board headline, or a pending recommendation is No
  evidence until it has been decided and acted on.
- **Only executive peers as sources.** Peers see the CTO in meetings; direct reports and the
  organization's records show whether decisions held below.
- **No contrary evidence.** If every row is flattering, the matrix was filled from memory.
- **Averaging self and CEO ratings.** The gap, especially on weights, is the useful information.
- **Development goals in Low-weight rows** chosen because they are easy to improve.

## Review questions

1. If the CTO were away for a quarter, which High-weight competencies would visibly degrade, and which
   would hold?
2. Which of the CTO's decisions this period would a director describe as made in a hallway?
3. Does the CEO weigh the competencies as the CTO does? If not, which job is the CTO actually doing?
4. Which risk would the board learn about from someone other than the CTO?
5. What will the CTO stop doing to make room for the two development goals?

## Evidence and references

The CTO archetypes and the CTO, CIO, and VP Engineering splits are
[Chapter 50's](../parts/12-cto-leadership/50-what-a-cto-actually-does.md#archetypes-what-the-company-needs-at-the-top).

- [Larson, 2023a](../references/bibliography.md#larson2023executive-job): defines the engineering
  executive as the person responsible for all of engineering, whatever the title, and notes that
  companies use the titles inconsistently.
- [Vogels, 2007](../references/bibliography.md#vogels2007ctoroles): summarizes Tom Berray and Raj
  Sampath's four CTO models (infrastructure manager, technology visionary and operations manager,
  external-facing technologist, and big thinker) and says the role differs with the company. That is
  **expert opinion**, not a study; the weighting step comes from it.
- [Larson, 2024](../references/bibliography.md#larson2024primer): Larson's writing on engineering
  executives, credited here for the general idea behind the competency list.
- [Larson, 2023b](../references/bibliography.md#larson2023balancing): the argument that the
  executive's job is the company's problem rather than engineering's advocacy.
- [NIST, 2024](../references/bibliography.md#nist2024csf): the Cybersecurity Framework 2.0's emphasis
  on governance, behind competency 4 (**standard**).

The competency list is **this book's recommendation**. No study validates any CTO competency model,
this one included.

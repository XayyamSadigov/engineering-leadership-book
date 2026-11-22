# Leadership succession plan

!!! warning "Awaiting human review"
    This template has passed the book's automated validation and an editorial self-review, but not yet
    the human review in which each cited claim is checked against its source. Treat it as a reviewed
    draft. Corrections are welcome; see the repository's CONTRIBUTING file.

**Used in:** Chapter 36 (reorganizations, organizational evolution, and succession), Chapter 41
(managing and developing engineering managers, where the bench is grown), Chapter 12 (knowledge maps,
the input for concentrated-knowledge roles), Chapter 55 (what the board asks about key-person risk);
Project 6 builds one.
**Owner:** the leader the critical roles report to (the director, for managers and staff engineers),
reviewed with the managers and HR. The CTO sees the rows for the top roles.
**Cadence:** reviewed twice a year; redone whenever a reorganization is drafted, a critical role holder
resigns, or a candidate moves.

A succession plan answers one question for every critical role: if the person in it left next week, who
would keep it running, and who is being developed to take it over? A **critical role** is one whose
sudden vacancy would stop a team, a system, or a class of decisions: every manager, every staff engineer,
the director, and the holders of concentrated knowledge on tier 1 systems. The readiness scale and the
coverage rule below are Chapter 36's
([Chapter 36](../parts/07-organization-design/36-reorganizations-evolution-and-succession.md#succession-coverage));
how to grow the names in the plan is Chapter 41's
([Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)).

Succession is a process, not an event. A review of five decades of CEO succession research notes that
studies have mostly treated it as an event, contrary to practice, which treats it as continuous
([Berns and Klarner, 2017](../references/bibliography.md#berns2017succession)); that is a **research
finding** about chief executives, used here only for the framing. For code, a study of Chrome and a
project at Avaya found that having designated successors reduced expected loss from developer turnover
by as much as 15 percent ([Rigby et al., 2016](../references/bibliography.md#rigby2016turnover)), a
**research finding** about files and their authors; that prepared successors also reduce the cost of
losing a manager is this book's inference. Firms tend to promote on current performance even when other
traits predict managerial success better
([Benson, Li, and Shue, 2019](../references/bibliography.md#benson2019promotions), **research finding**
on sales workers), so candidates are selected on evidence of managerial work, created through trial
assignments. The fields and the review rules are **this book's recommendation**.

The plan is confidential to the director, HR, and the CTO. The candidates themselves are told they are
developing toward broader work, and what that work is; they are not told they are the heir.

## How to fill it in

1. **List the critical roles,** including the director's own and any person whose knowledge of a tier 1
   system is held by one or two people (Chapter 12's knowledge map). Leave out roles whose vacancy would
   slow work without stopping it.
2. **Rate cover for each role on Chapter 36's scale:** ready now (could hold the role for three months
   or more from next week, with support), ready with development (could hold it in 6 to 18 months, given
   named development work), interim only (could keep it running for a few weeks while a decision is
   made), or none.
3. **Base every rating on evidence of the role's work,** not of engineering excellence: has the person
   run planning, led an incident review, owned a hiring loop, facilitated a health check? If not, the
   rating is a guess; write "none" or "interim" and create the evidence.
4. **Apply the coverage rule** (Chapter 36): a role is covered when it has at least one person ready now
   or interim and at least one in development, and the cover neither holds another critical role nor is
   primary cover for one. A person covering two roles is coverage on paper only.
5. **Count twice:** roles with ready-now cover, with interim cover, with none; and how many roles each
   person appears in.
6. **Give every gap a development action, an owner, and a date.** A trial assignment that is real
   management work, a sponsor, and the delegation level (Chapter 2) at which the candidate acts.
7. **Record whether each candidate has been asked.** A named successor who has never been asked whether
   they want the role is succession theater.
8. **Note the cost,** in engineer-weeks, of each development action: the candidate's time comes from
   delivery.
9. **Redo the plan against any proposed chart** before the chart is announced. A reorganization that
   promotes a development candidate leaves their old role, and their new one, to be covered.

## Template

| Field | Meaning |
|---|---|
| Critical role | Role and current holder |
| Why critical | What stops if it is vacant next week |
| Ready now | Name, or none |
| Interim only | Name, or none; note if they hold or cover another critical role |
| In development | Names, with the part of the role each covers |
| Covered by the rule? | Yes / no, and which condition fails |
| Development action | Trial assignment, sponsor, delegation level |
| Owner and date | Who makes the action happen; check date |
| Candidate asked? | Yes / no, date, and what they said |
| Cost | Engineer-weeks a quarter the action takes from delivery |

```yaml
plan:
  owner: ""
  date: ""
  reviewed_with: []        # managers, HR
  next_review: ""
roles:
  - role: ""
    holder: ""
    why_critical: ""
    ready_now: []
    interim: []
    interim_holds_other_critical_role: false
    in_development:
      - {name: "", covers: ""}
    covered: false
    failing_condition: ""  # no interim or ready-now / no one in development / cover holds another role
    actions:
      - {trial_assignment: "", sponsor: "", delegation_level: 0, owner: "", check: "", engineer_weeks_per_quarter: 0}
    candidates_asked:
      - {name: "", asked: false, date: "", response: ""}
counts:
  roles: 0
  ready_now: 0
  interim: 0
  none: 0
  covered_by_rule: 0
  people_in_more_than_one_role: []
```

## Example: Northstar, the week 44 succession table

**Fictional.** The ten roles, the names in each column, and the counts are the week 44 ratings recorded
in Chapter 36 and on the [first quarter](../case-studies/northstar/first-quarter.md) page; they are the
director's fictional judgments. The development actions are the ones proposed in Chapter 41's quarter 3
plans and Chapter 36's case study, all with outcomes open. The layout, the coverage-rule column, and the
rows marked "none recorded" are this template's reading of those sources. Nothing here records an
outcome.

**Context.** Week 44 of the director's first year. The year-2 organization proposal, drafted the same
week, would split Customer Experience and make Mateo Arango Ríos Mobile's manager; Victor Lindqvist
decides in week 46. In week 45 Victor asks whether Northstar needs a VP of Engineering in year 2. Writing
the reorganization plan raised the question the proposal had not asked: if a name on the chart left,
who would step in?

| Critical role | Ready now or interim | In development | Covered by the rule? | Development action (proposed) and owner |
|---|---|---|---|---|
| Orders (Priya Raman) | Aisha Bello, interim | Aisha Bello; Rafael Duarte if he chooses management | Yes, by one person in both columns | Aisha runs Orders' quarter 3 planning at level 3 and is named interim cover; Priya Raman |
| Billing (Marcus Oyelaran) | None | None | No: no cover, no one in development (Teodora Vasquez-Lund covers ledger knowledge, not management) | A senior engineer takes one named piece of Marcus's job; Teodora asked, without commitment, about a management trial; Marcus Oyelaran and the director |
| Payments and Integrations (Elena Sokolova) | Informal tech lead, interim | Same person | Yes, by one person, who is also in development for the data-and-integration staff role | The informal tech lead represents the team in cross-team planning; Elena Sokolova |
| Customer Experience (Daniel Cho) | Hannah Lindgren, interim | Mateo Arango Ríos | Yes, though each covers half the team | Hannah and Mateo as half-team covers, with a sponsorship action each; Daniel Cho |
| Data and Analytics (Farah Haddad) | None | Sunil Varghese, architecture half only | No: no cover; Farah holds two roles (manager and data architect) | Sunil leads one warehouse design decision at level 3 and co-owns warehouse architecture with Farah; Farah Haddad |
| Platform Operations (Tom Becker) | Kwame Mensah, interim | None | No: Kwame holds a critical role; no one in development | None yet; Tom Becker |
| Staff, core domain (Ines Carvalho) | None | Aisha Bello, Rafael Duarte (order capture); Teodora Vasquez-Lund (ledger) | No: no cover; nobody covers the whole domain | None recorded |
| Staff, infrastructure (Kwame Mensah) | Bram Verhoeven, Core Jenkins only | None | No: no one in development; Bram's expectations plan is open | None recorded |
| Staff, data and integration (Li Na Zhou) | None | Sunil Varghese (warehouse); the Payments informal tech lead (integration) | No: no cover; split development | None recorded |
| Director | Elena Sokolova, interim | Elena Sokolova | No: Elena holds a critical role; if she acts, Payments falls to its informal tech lead | Elena chairs the operations review during the director's two weeks of leave; the director |

**Counts.** Ready now: 0 of 10. Interim: 6 (Orders, Payments and Integrations, Customer Experience,
Platform Operations, staff infrastructure, director). None: 4 (Billing, Data and Analytics, the
core-domain and data-and-integration staff roles). Covered by the rule: 3 (Orders, Payments and
Integrations, Customer Experience), two of them by one person in both columns. People in more than one
role: Aisha Bello (Orders and core domain), Rafael Duarte (Orders and core domain, both conditional or
partial), Sunil Varghese (Data and Analytics and data and integration), the Payments informal tech lead
(Payments and data and integration), Kwame Mensah (holds infrastructure, covers Platform Operations),
Elena Sokolova (holds Payments, covers the director).

What to notice: the table changes the reorganization. Promoting Mateo Arango Ríos removes Customer
Experience's development candidate and creates a Mobile manager role with no cover, in a site where
nobody else leads; Chapter 36's director therefore plans to redo the table in week 49 with seven teams,
before any announcement. The three staff rows have names in development and no recorded action, which
is how succession theater starts. Missing from the ten rows altogether are the concentrated-knowledge
holders Chapter 36 says belong here: in the baseline counts of Billing's ledger knowledge, currency
and rounding had one person who could respond alone and one who could change it safely. The VP question would also
change the director row: a VP takes one of the 87 seats. When Anders Holm, the board chair, asks whether
the year-1 gains depend on a few people (Chapter 55), these counts are the honest answer, together with
the continuation proposal's requirement that no critical role be without cover by week 78, a proposal
whose status is undecided.

## Common mistakes

- **Names in boxes.** A successor with no trial assignment since they were named is a guess filed as a
  plan.
- **One person covering two roles.** Counted once per role, they make coverage look double what it is.
  Count people as well as roles.
- **The heir apparent.** One successor, publicly named; others stop developing, and the heir leaves when
  the role does not open. Keep more than one name in development where possible.
- **Selecting on engineering excellence.** The best engineer is not evidence of the best manager; create
  evidence of managerial work before rating anyone ready.
- **Titles only.** A table of managers and staff engineers misses the one engineer who can change the
  ledger's rounding code safely.
- **Not redoing it for a reorganization.** Every promotion in a new chart opens a role, and the new role
  needs cover too.
- **Never asking the candidate.** A plan built on someone who does not want the role fails the day it is
  used.

## Review questions

1. If the holder of each critical role resigned tomorrow, who would run it on Monday, and have they
   ever done any part of it?
2. Which person appears in more than one row, and what happens to both roles if they leave?
3. Which gap has no development action, owner, and date?
4. Which knowledge, held by one or two people on a tier 1 system, is missing from the table?
5. What does the proposed chart do to this table?

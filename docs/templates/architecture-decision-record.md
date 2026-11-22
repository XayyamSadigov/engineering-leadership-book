# Architecture decision record

**Used in:** [Chapter 13](../parts/03-high-performing-teams/13-decision-making-in-teams.md) (decision-making in teams), [Chapter 28](../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md) (architecture
decision-making and governance), [Chapter 39](../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md) (decision logs), [Chapter 55](../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#deciding-under-uncertainty-and-disagreement)
(recording executive decisions).
**Owner:** the proposer writes the record; the named decider signs it and owns its review trigger and
any automated check; the domain's staff engineer keeps the log in order.
**Cadence:** one record per architecturally significant decision, opened before building starts;
the log is reviewed quarterly for fired review triggers and for cross-team changes that have no record.

An architecture decision record (ADR) is a short document, kept in the repository next to the code,
that says what was decided, by whom, why, what else was considered, and when to reopen it. Nygard's
original proposal holds a title, context, decision, status, and consequences (including the negative
ones), numbered, with reversed decisions marked superseded rather than deleted, so that successors need
not accept or reverse old decisions blindly ([Nygard, 2011](../references/bibliography.md#nygard2011adr)).
The ADR community site calls the collection of a project's records its decision log and points to
several templates ([adr.github.io](../references/bibliography.md#adr-github-io)); MADR (Markdown
Architectural Decision Records), for example, adds decision drivers, considered options with
pros and cons, and a "Confirmation" section on how compliance with the decision will be checked
([MADR](../references/bibliography.md#madr-template)). Keeping records in source control rather than a
wiki is **practitioner consensus**
([Thoughtworks, Lightweight ADRs](../references/bibliography.md#thoughtworks-radar-lightweight-adr)),
not evidence of effect.

Chapter 28 owns the practice: which decisions need a record, who decides, comment windows, and how a
log stays alive ([Chapter 28](../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#architecture-decision-records)).
Chapter 13 owns the fields a successor needs ([Chapter 13](../parts/03-high-performing-teams/13-decision-making-in-teams.md#recording-decisions)).
This template combines them: Nygard's fields, Chapter 13's successor fields (decider and method,
options rejected, assumptions, review trigger), and Chapter 28's governance fields (agreement rights,
comment window, automated check). The additions are **this book's recommendation**. Mining open source
repositories, Buchgeher and colleagues found ADR adoption low and many logs holding only a handful of
records ([Buchgeher et al., 2023](../references/bibliography.md#buchgeher2023adr); **research finding**
at abstract level, open source only, no outcome measure). The template cannot fix a log nobody
maintains; the trigger in Chapter 28's practice does that.

## How to fill it in

1. **Check that it needs a record.** Use Chapter 28's test: would reversing it need another team's
   work, a data migration, or a coordinated release? If not, a commit message is enough.
2. **Title it as the question,** not the answer: "How integrations read posted ledger data", not
   "Use the export contract". The title must stay true whichever option wins.
3. **Name the decider before writing the options.** One person, never "the team" or "the forum".
   If nobody holds the decision right, write that in the record and escalate the gap; do not proceed
   as if someone did. Name who holds agreement rights and on what (capacity and dates, not design).
4. **Write the context with evidence and a date the decision is needed by.** Incidents, effort
   estimates, consumers, deadlines. A "needed by" date earlier than the record's opening date is
   itself a finding.
5. **List at least two real options, including the status quo,** each with effort by team, readiness
   against the deadline, and its main risk. An option nobody would choose is padding.
6. **Write consequences for every option, both sides.** What each team takes on, what each loses. The
   negative consequences of the recommended option are the part a successor most needs.
7. **State assumptions and a review trigger.** The assumptions are what would make the decision wrong;
   the trigger is the observable signal that reopens it.
8. **Name a check if the decision can be silently undone,** with an owner: a contract test, a grant
   check, a dependency rule in the build (a fitness function, in Chapter 28's terms).
9. **Open the comment window** (three working days inside a team, five across teams), record the
   input that arrives, including input from executives, then decide. Silence means proceed.
10. **Move the status; never rewrite the decision.** Accepted, Rejected, or Superseded by a new record.
    An overrule, including one from the CTO, is a superseding record that states the trade-off.

## Template

| Field | Contents |
|---|---|
| Number and title | ADR-NNNN, the question in plain words |
| Status | Proposed, Accepted, Rejected, or Superseded by ADR-NNNN; with the date of each change |
| Decider | One named person and why they hold the right; or "not named" with the gap escalated |
| Agreement rights | Who, on what (capacity and dates only), by when |
| Consulted | Teams and people whose written input is required |
| Needed by | The date after which not deciding costs something, and what it costs |
| Context | The problem, with evidence and consumers |
| Options | At least two, including the status quo: effort by team, readiness, main risk |
| Recommendation | The proposer's choice and reasoning, marked as a recommendation |
| Decision | The option chosen, by whom, on what date; blank while Proposed |
| Consequences | For the chosen option (or each option while Proposed): what each team takes on and loses |
| Assumptions | What would have to change for the decision to be wrong |
| Review trigger | The signal that reopens it, and who watches for it |
| Check | The automated test or rule that enforces it, and its owner; "none needed" with a reason |
| Recorded input | Comments received in the window, including executives', with dates |

```markdown
# ADR-NNNN: <the question>

- Status: Proposed | Accepted | Rejected | Superseded by ADR-NNNN   (date of each change)
- Decider: <one name>, because <mandate or role>
- Agreement rights: <name>: capacity and dates only, by <date>
- Consulted: <teams and people>; comment window <start> to <end>
- Needed by: <date>; cost of not deciding by then: <what is lost>

## Context
## Options
## Recommendation
## Decision
## Consequences
## Assumptions
## Review trigger
## Check
## Recorded input
```

```yaml
adr:
  number: ""                 # ADR-0001
  title: ""                  # the question
  status: proposed           # proposed, accepted, rejected, superseded
  status_history: []         # [{status: "", date: ""}]
  superseded_by: ""
  decider: {name: "", basis: ""}
  agreement_rights: []       # [{name: "", scope: "capacity and dates", by: ""}]
  consulted: []
  comment_window: {opens: "", closes: ""}
  needed_by: {date: "", cost_of_waiting: ""}
  options:
    - {id: A, summary: "", effort_by_team: {}, ready_by_deadline: "", main_risk: ""}
  recommendation: {by: "", option: "", reasoning: ""}
  decision: {option: "", date: ""}
  consequences: []
  assumptions: []
  review_trigger: {signal: "", watched_by: ""}
  check: {description: "", owner: ""}
  recorded_input: []         # [{who: "", date: "", input: ""}]
```

## Example: Northstar ADR-0001, still Proposed

**Fictional.** This is ADR-0001 written out in the template, as the record stands in quarter 4. The
facts come from the canon ([first year](../case-studies/northstar/first-quarter.md),
[baseline data](../case-studies/northstar/baseline-data.md)) and from the estimates in
[Chapter 28's case study](../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#case-study)
and the week 47 input from [Chapter 51](../parts/12-cto-leadership/51-enterprise-technology-strategy.md),
with its status in the organization decision log taken from
[Chapter 39](../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md).
ADR-0001 is open in the canon, and this example keeps it open: the Decision field is blank and no
option is chosen. The assumptions are the example's wording of the proposer's case.

```markdown
# ADR-0001: How integrations read posted ledger data

- Status: Proposed (week 14). Still Proposed in quarter 4.
- Decider: not named. No decision-rights map exists; logged as DL-08, decider "Not yet named".
  Li Na Zhou holds the data standards domain but wrote the proposal; Billing provides the
  interface and has no technical lead.
- Agreement rights: not mapped. Candidates: Marcus Oyelaran (Billing capacity), Elena Sokolova
  (the week 19 date), on capacity and dates only.
- Consulted: Billing, Payments and Integrations, Data and Analytics; comment window not opened.
- Needed by: the middle of week 14, so that Billing's reserved weeks 14 to 16 are spent on the
  chosen option. The record was opened in week 14, so it was late on the day it opened.

## Context
The new erp-sync connector for the accounting-system renewal commitment (due end of week 19)
needs posted invoices for daily reconciliation. The older erp-sync connectors and the warehouse
pipelines already read 12 core/ledger tables directly through the read replicas. INC-424
(replicas serving stale balances after a migration) shows the replicas can lag, and every ledger
migration changes an interface nobody has written down. Billing has reserved 6 engineer-weeks
(two engineers, weeks 14 to 16).

## Options
| Option | Billing effort | Payments effort | Ready by week 19? | Main risk |
|---|---|---|---|---|
| A. Read the tables (status quo) | 1 engineer-week | 3 | Yes | Every ledger migration can break three consumers silently |
| B. Versioned export contract | 5 engineer-weeks | 2, plus contract tests | Yes, about one week of slack | Billing owns a new interface with no technical lead |
| C. Ledger posting events | about 16 engineer-weeks, with Platform Operations | 4 | No; about week 24 | New infrastructure on the renewal's critical path |

## Recommendation (Li Na Zhou, proposer)
B for the new connector; the warehouse pipelines move to the export in quarter 3; C deferred
under the review trigger below.

## Decision
(blank: no decider has decided)

## Consequences
- A: no new work for Billing; a third silent consumer of ledger tables; nothing written down
  about what the connector depends on.
- B: Billing takes on a versioned public interface, runs consumers' contract tests, and answers
  for breakages, without a technical lead; Data and Analytics must migrate the warehouse
  pipelines; ledger migrations stop breaking the new connector silently.
- C: the cleanest long-term interface; misses week 19, and about 10 engineer-weeks beyond
  Billing's reservation must come from Billing or Platform Operations after week 16.

## Assumptions (proposer's case)
- Posting volume stays within what a daily export handles.
- No third consumer of posted ledger data appears this quarter.
- Billing can staff ownership of a new interface.

## Review trigger
A third consumer of posted ledger data, or posting volume above a threshold to be agreed.
Watched by: the decider, once named.

## Check
If B is accepted: a weekly check that no new database grant gives a non-Billing service read
access to ledger tables, owned by the decider. If A is accepted: none possible, which is a
consequence of A.

## Recorded input
- Week 14, Victor Lindqvist to Elena Sokolova, in passing: "read the tables now and clean it up
  later". Recorded as input on the week 19 risk, not as the decision.
- Week 19: the accounting integration went live for the renewal customer with daily
  reconciliation of posted invoices. No ledger read path is named in this record.
- Week 47, Victor Lindqvist, draft three-year technology strategy (not yet adopted): "money data
  moves by contract or events, never tables", a stated reversal of the week 14 remark; proposes
  that ADR-0001 be decided by week 60. Recorded as input; the strategy is a discussion item for
  the week 50 board. The Decision field stays blank: a policy in a draft strategy does not decide
  this record, and the decider is still not named.
```

What to notice: the hardest field is the decider, and leaving it blank honestly is better than
writing "the team". The record also shows the worst state an ADR can reach: the work it governs
shipped in week 19 while the record stayed Proposed, so the system holds a decision the log does not.
Whoever is eventually named decider must first find out which read path the connector actually uses,
then either accept that option on the record, with its consequences, or supersede it with a plan. The
CTO's remark is in the record as dated input, which keeps his concern about the date visible without
letting a hallway sentence become the decision (Chapter 28's executive overrule failure). His week 47
written position reverses the remark, and it does so for the team only because it is in the record:
a later executive view replaces an earlier one when both are dated in the same place, not when the
second is said in a different meeting.

## Common mistakes

- **No decider, or a group as decider.** The record becomes a meeting summary that nobody can close.
- **Title states the answer.** It biases the comment window and becomes false if the decision changes.
- **Only the chosen option's benefits.** Consequences without costs are advocacy; successors need the
  costs to judge whether the trade still holds.
- **Edited instead of superseded.** Rewriting an accepted record destroys the history the log exists
  to keep.
- **Written after the build.** A record opened once the code has shipped documents, it does not decide;
  say so in the status, as the example does.
- **Executive input left out.** An instruction given in passing that is not in the record still steers
  the work, invisibly.
- **No review trigger or check.** The decision then drifts without anyone noticing it has been undone.

## Review questions

1. Could a new engineer, reading only this record, tell who decided, why, and what would reopen it?
2. Which consequence of the chosen option would its decider least like to see written down? Is it there?
3. What change to the code could silently undo this decision, and what would catch it?
4. If the "needed by" date passes without a decision, who notices, and what happens to the work?
5. Did anyone senior to the decider give an instruction on this question outside the record?

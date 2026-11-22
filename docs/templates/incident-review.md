# Incident review

**Used in:** Chapter 25 (incident response and blameless review), Chapter 27 (recurrence and action
closure), Chapter 57 (crises).
**Owner:** the team that owns the affected component; facilitated by someone not directly involved.
**When:** every Sev1 and every Sev2 that touched a tier 1 path, within five working days.

The purpose of a review is to change the system so that the same failure is less likely or less
damaging. It looks for contributing causes, not for a person to blame. People who were involved are
the best source of information about how the system allowed the failure, and they will only give an
accurate account if they are not at risk for doing so.

## Template

```markdown
# Incident review: <INC-id> — <one-line summary>

| | |
|---|---|
| Severity | |
| Date and duration | start, detected, mitigated, restored (times with time zone) |
| Customer impact | who, how many, what they could not do, for how long |
| Detected by | customer / monitoring / engineer |
| Owning team | |
| Facilitator | |
| Review date | |

## Summary
Three to five sentences a non-engineer can follow.

## Timeline
Times, events, and what people knew at each point. Record decisions and the information behind them.

## Contributing causes
What about the system (code, pipeline, process, monitoring, ownership, documentation, staffing)
made this possible, and what made it worse or longer. More than one cause is normal.

## What went well
Things that limited the damage and should be kept.

## Recurrence check
Has this failure mode, or a close variant, been reviewed before? Link the earlier review. If yes,
why did the earlier actions not prevent it?

## Actions
At most five. Each has an owner (a manager for anything cross-team), a due date, and a statement of
which contributing cause it addresses.

| # | Action | Addresses cause | Owner | Due | Status |
|---|---|---|---|---|---|

## Open questions
What we still do not understand, and who is finding out.
```

## Example: Northstar INC-427

**Fictional.** From `incidents-last-quarter.csv` in the
[Northstar data](../case-studies/northstar/baseline-data.md).

| | |
|---|---|
| Severity | Sev2 |
| Duration | Detected 120 minutes after release; restored after about 18 hours; data repair completed day 3 |
| Customer impact | Credit notes applied twice for 37 distributors; incorrect balances on statements sent that day |
| Detected by | Customer (a distributor's finance team) |
| Owning team | Billing |

**Summary.** Release 24.26 of Core shipped a change to credit-note processing together with a schema
migration on the ledger. The new code ran before the migration had finished on all partitions and
treated unmigrated rows as unprocessed, applying their credit notes a second time. No alert covers
ledger balance anomalies, so a customer noticed first.

**Contributing causes.**

1. Code and migration shipped in the same release with no ordering or completion check (debt
   register TD-004).
2. The migration's duration on production volumes was not known in advance; the staging dataset is
   about one fiftieth of production.
3. No monitoring on ledger invariants (for example, credit notes applied more than once).
4. The two-week release batched this change with about 170 others, slowing diagnosis.

**Recurrence check.** Yes. INC-406 and INC-424 were also migration-related in the ledger, and the
INC-406 review recommended migration checks. That action had no owner above the engineer who wrote
it and was never scheduled.

**Actions.**

| # | Action | Addresses | Owner | Due |
|---|---|---|---|---|
| 1 | Pipeline check that blocks code depending on an unfinished migration | 1 | Li Na Zhou (staff engineer) with Billing | 6 weeks |
| 2 | Run migrations against a production-sized copy before release and record duration | 2 | Marcus Oyelaran | 4 weeks |
| 3 | Alert on ledger invariant violations | 3 | Marcus Oyelaran | 2 weeks |
| 4 | Track migration-related incidents as a named category on the scorecard | recurrence | Engineering Director | next review |

## Facilitator checklist

- [ ] The timeline records what people knew, not only what happened.
- [ ] No sentence names a person as the cause.
- [ ] Every action addresses a stated contributing cause.
- [ ] Cross-team actions are owned by a manager.
- [ ] The recurrence check was done against earlier reviews, not from memory.
- [ ] The review is linked from the incident record and from the scorecard.

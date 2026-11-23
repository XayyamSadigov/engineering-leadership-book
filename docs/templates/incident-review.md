# Incident review

**Used in:** [Chapter 25](../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md)
(incident response and blameless review),
[Chapter 27](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) (recurrence
and action closure), [Chapter 57](../parts/13-advanced-problems/57-crises-executive-disagreement-and-resistance.md)
(crises).
**Owner:** the team that owns the affected component; facilitated by someone not directly involved.
**Cadence:** every Sev1, and every Sev2 that touched a tier 1 path, reviewed within five working days.
Recurrence and action closure are read monthly across all reviews.

An incident review is a written account of one serious incident that changes the system so the same
failure is less likely or less damaging. It looks for contributing causes, not for a person to blame:
a [blameless review](../glossary.md#blameless-review). People who were involved know best how the
system allowed the failure, and they give an accurate account only if they are not at risk for doing
so. Use it after every incident that meets your trigger, defined in advance with the
[severity](../glossary.md#severity-sev1-sev2-sev3) levels.

## How to fill it in

1. **Decide the trigger before you need it.** Severity and the [tier 1](../glossary.md#tier-1) paths
   set which incidents get a review. Do not decide case by case after the fact.
2. **Pick a facilitator from outside the incident.** The facilitator runs the meeting and writes the
   record; the owning team supplies the facts.
3. **Build the timeline first, from logs and chat.** Record what people knew and decided at each
   point, not only what happened. Times carry a time zone.
4. **Write the summary for a non-engineer.** Three to five sentences: what broke, who was affected,
   for how long.
5. **List contributing causes across the whole system.** Code, pipeline, process, monitoring,
   ownership, documentation, and staffing. Record the trigger (the last step) as a plain fact, then
   ask why it could reach production and why nothing caught it sooner. More than one cause is normal.
6. **Run the recurrence check against earlier reviews.** Search the records, do not rely on memory. If
   the same failure mode appeared before, say why the earlier actions did not prevent it. A
   [recurrence](../glossary.md#recurrence) is the clearest sign that actions are not working.
7. **Write at most five actions.** Each names the cause it addresses, an owner, and a due date. A
   manager owns anything that crosses teams, because only managers control capacity.
8. **Link the review** from the incident record and the quality scorecard, and track the actions to
   closure in the weekly review.

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

## Example: Northstar, INC-427 (credit notes applied twice)

!!! info "Northstar so far"
    The baseline quarter, just before the director's week 1. Northstar had 30 Sev1 and Sev2 incidents
    that quarter; 11 were recurrences. This review is one of them, from the incident data. See the
    [timeline](../case-studies/northstar/timeline.md) and the [cast](../case-studies/northstar/cast.md).

[INC numbers](../glossary.md#inc-numbers) identify incidents in Northstar's records. INC-427 is the
Billing incident in which credit notes were applied twice.

| | |
|---|---|
| Severity | Sev2 |
| Duration | Detected 120 minutes after release; restored after about 18 hours; data repair completed day 3 |
| Customer impact | Credit notes applied twice for 37 distributors; incorrect balances on statements sent that day |
| Detected by | Customer (a distributor's finance team) |
| Owning team | Billing |

**Summary.** Release 24.26 of Core, the shared application, shipped a change to credit-note
processing together with a schema migration on the ledger. The new code ran before the migration had
finished on all partitions. It treated unmigrated rows as unprocessed and applied their credit notes a
second time. No alert covers ledger balance anomalies, so a customer noticed first.

**Contributing causes.**

1. Code and migration shipped in the same release with no ordering or completion check (debt
   register TD-004).
2. The migration's duration on production volumes was not known in advance; the staging dataset is
   about one fiftieth of production.
3. No monitoring on ledger invariants (for example, credit notes applied more than once).
4. The two-week release batched this change with about 170 others, slowing diagnosis.

**Recurrence check.** Yes. INC-406 and INC-424 were also migration failures in the ledger, and the
INC-406 review recommended migration checks. That action had no owner above the engineer who wrote it
and was never scheduled.

**Actions.**

| # | Action | Addresses | Owner | Due |
|---|---|---|---|---|
| 1 | Pipeline check that blocks code depending on an unfinished migration | 1 | Li Na Zhou (staff engineer) with Billing | 6 weeks |
| 2 | Run migrations against a production-sized copy before release and record duration | 2 | Marcus Oyelaran (Billing manager) | 4 weeks |
| 3 | Alert on ledger invariant violations | 3 | Marcus Oyelaran | 2 weeks |
| 4 | Track migration-related incidents as a named category on the scorecard | recurrence | Engineering Director | next review |

What to notice: the review lists four causes where a single-cause review would list one. The
recurrence check shows why the earlier review failed: its action had no owner who controlled
capacity, which is why actions 1 and 2 name a staff engineer and a manager.

## Common mistakes

- **One root cause.** Analysis stops at the first satisfying answer, usually a person or the last
  step. List the trigger as a fact and keep asking what let it through.
- **A person as the cause.** "The engineer mistyped the value" ends the inquiry and teaches everyone to
  leave details out of the next review.
- **Too many small actions.** Ten actions get none done. Cap them at five, each tied to a cause.
- **Cross-team actions owned by engineers.** An engineer cannot schedule work in another team's plan.
  A manager owns it, or it will not happen.
- **Recurrence checked from memory.** People forget earlier reviews; search the records.
- **Actions closed quietly.** Closure rises when actions are trivial or marked "won't do". Dropping an
  action is legitimate; dropping it silently is not.
- **A review nobody reads again.** If the review is not linked from the scorecard and its actions are
  not tracked weekly, it is a document, not a change.

## Review questions

1. Does the timeline record what people knew at each point, not only what happened?
2. Does any sentence name a person as the cause?
3. Does every action address a stated contributing cause, and does a manager own each cross-team one?
4. Was the recurrence check done against earlier reviews, and if this is a repeat, does the review say
   why the earlier actions failed?
5. Which actions marked most important are overdue, and who has been told?
6. Are reviews getting more detailed over time, or shorter? Shorter reviews can mean people have
   stopped telling the whole story.

## Evidence and references

- [Lunney and Lueder, Postmortem Culture](../references/bibliography.md#google2017postmortem)
  describe blameless postmortems that seek contributing causes without indicting anyone, and
  recommend setting review triggers in advance (**practitioner consensus**).
- [Allspaw, 2012](../references/bibliography.md#allspaw2012blameless) gives the information argument:
  people who expect blame leave out what they saw, and the failure recurs (**expert opinion**).
- [Cook, 1998](../references/bibliography.md#cook1998complex) argues that failures in complex systems
  have several contributors, each insufficient alone, which is why the template asks for several
  causes (**expert opinion**, from safety science).
- The outcome evidence is thin. No peer-reviewed study measures the effect of blameless review on
  software incidents. Healthcare reviews ([Murray et al., 2023](../references/bibliography.md#murray2023just);
  [van Marum et al., 2022](../references/bibliography.md#vanmarum2022barriers)) and
  [Edmondson, 1999](../references/bibliography.md#edmondson1999psychological) support the mechanism
  (fear suppresses reporting), not the outcome (fewer incidents).
- The five-action cap, manager ownership of cross-team actions, and the recurrence check are **this
  book's recommendation**. Measure them locally through recurrence and action closure.

The method, including severity definitions and change failure classification, is in
[Chapter 25](../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md).

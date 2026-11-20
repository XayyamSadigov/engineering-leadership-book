# Chapter 25 solutions — Incidents, Postmortems, and Change Failure Analysis

Worked solutions for the [chapter 25 exercises](../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Re-rating seven incidents

**Worked re-rating** against the case study's Sev1 definition (order or payment path unavailable for
any customer, or any wrong financial record visible to customers):

| Incident | Original | Re-rated | Reasoning |
|---|---|---|---|
| INC-401 multi-currency invoice totals rounded wrongly | Sev2 | Sev1 | Wrong invoices reached customers |
| INC-409 duplicate invoices | Sev1 | Sev1 | Wrong financial records |
| INC-414 tax rate table missing an effective date | Sev2 | Judgment | Sev1 if invoices went out with wrong tax, or if orders for that jurisdiction were blocked |
| INC-422 PDF invoices missing the tax breakdown | Sev2 | Judgment | Amounts may be right but the document may be legally incomplete |
| INC-424 replicas served stale balances | Sev2 | Judgment | Depends on whether customers saw the stale balances, and for how long |
| INC-425 card processor certificate expired | Sev1 | Sev1 | Card payments on the payment path failed |
| INC-427 credit notes applied twice | Sev2 | Sev1 | Wrong balances on customer statements |

**Information needed.** For INC-414, whether any invoice was issued with the wrong tax. For INC-422,
whether an invoice without the breakdown is valid in that region. For INC-424, whether stale balances
reached a customer-facing screen or API and whether anyone acted on them.

**Wording that settles it.** Something like: "Sev1 includes any financial document or balance delivered
to a customer that is wrong or legally incomplete; a display lag under N minutes that is corrected
without customer action is Sev2." The second clause keeps Sev1 meaningful. A good answer proposes a
threshold and admits it is a judgment. The weak answer re-rates by duration ("it lasted long, so Sev1"),
which reintroduces the inconsistency the definitions exist to remove.

## F2 — Rewriting the INC-430 review

**Trigger (fact).** A configuration change lowered the payments-gateway rate-limit threshold tenfold
because of a mistyped value. Detected by monitoring in 2 minutes; restored in 40.

**Contributing factors.**

1. Rate-limit settings have no range validation; any number is accepted.
2. The change review shows the new value but does not flag a change of an order of magnitude against
   the old one.
3. Configuration is applied to all tenants at once, with no staged rollout.
4. The same team had INC-410 (a feature flag enabled for all tenants instead of one), so configuration
   changes on this service have a pattern, not a one-off.

**What went well.** Monitoring caught it in two minutes; rollback was fast.

**Actions.** Schema validation with bounds for rate-limit and similar numeric settings; a pipeline
warning on large relative changes; staged rollout for configuration on tier 1 services. Owner: the
Payments and Integrations manager, with a staff engineer for the shared guard library.

**Hindsight bias** is in "did not double-check": it assumes the error was obvious at the time. The
facilitator should ask how the value is entered, what the reviewer saw, how often such values change,
and whether similar slips have happened before. "Remind engineers to be careful" is the weak answer:
it addresses nobody's system and will not change the next typo.

## F3 — Classifying the release-train incidents

The nine release-train incidents are INC-401, 403, 409, 411, 415, 417, 421, 422, and 427. The chapter
assigns seven to logic and regression tests, INC-427 to migration safety, and INC-415 to load testing
or canary rollout.

**Likely disagreements.**

- **Recurrences.** Six of the nine (401, 409, 411, 417, 421, 427) are flagged as recurrences. Under the
  diagram's first question they may belong in "follow-through gap", not "test gap". The review history
  decides it: was there an earlier review, and did it produce an action? INC-421 is described as the
  same failure mode as an incident two quarters earlier, so it is the strongest candidate.
- **INC-409** (duplicate invoices from a retried batch job) could be a design gap (no idempotency) rather
  than a test gap. A review would say whether retries were a known risk.
- **INC-403** (legacy price lists) might be a test-data gap rather than a logic gap.

**Does it change the leverage?** Partly. If most recurrences are follow-through gaps, the first-month
priority moves further toward closing existing actions, which is the chapter's conclusion. If INC-409 is
a design gap, it adds a small case for design review of batch jobs. A strong answer says which
disagreements matter for the decision and which do not. The weak answer treats classification as an
exercise in labels and never asks what decision it informs.

## A1 — The first twenty minutes

**In order.**

1. **Declare Sev1** (wrong financial records) and say so in the channel, with a time stamp.
2. **Assign roles.** Marcus knows the ledger; make him operations lead formally, and say you are
   incident commander. Name a communications lead and a scribe.
3. **Stop the damage before diagnosing.** Ask operations whether posting can be paused or the release
   rolled back. Every minute adds wrong postings to repair later.
4. **Set the cadence:** customer-facing updates every 30 minutes through the communications lead.

**To the CEO**, privately: "Sev1 declared at 10:4x. Payments are posting to the wrong period. We are
stopping further postings now. Next update at 11:15. The review will show what the system allowed; naming
someone now slows the fix." **To Sofia:** the three customers get an account-level answer as soon as
impact is known, then the 30-minute cadence; ten-minute updates would pull the commander away from the
incident. **To Marcus:** he is the right person to lead the fix, and you will handle everyone else.

A good answer protects the responders' attention and the information the review will need. The weak
answer has the commander debugging, or answers "who shipped this?" with a name.

## A2 — Responding to Elena Sokolova

**What you tell Elena.** The triage kept actions on recurring or expensive failure modes. Payments and
Integrations had 1 of the 11 recurrences; Billing had 6. Fewer kept actions reflects her team's
discipline, not a judgment that its reviews were worse. Dropping an action from the central list does
not forbid the work: her team can still schedule it in its own plan.

**Re-check one thing.** Two of her team's incidents (INC-410 and INC-430) were configuration slips on
the payments-gateway. If any of her dropped actions was a configuration guard, it addresses a pattern,
not a one-off, and should be restored. Saying so shows the triage had criteria and can be corrected.

**What you tell her engineers**, ideally in person: why the list was cut, what the criteria were, that
well-written actions are what made the triage possible, and how they can propose an action back onto
the list. A good answer keeps the incentive to write honest reviews alive. The weak answer either
restores everything to placate her (defeating the triage) or defends the cut without explaining it.

## A3 — The formal warning request

**Decision:** no formal warning. The engineer worked inside a system that had no checklist item for
migration ordering and an action from the first incident that was never done. The second occurrence is
evidence that the organization failed to act, not that the engineer was reckless.

**Where the boundary sits.** It would be different if an agreed, explained control existed and the
engineer bypassed it deliberately, or misrepresented what happened in the review. Neither is true here.

**Accountability still applies.** The engineer helps design the ordering check and leads the review. The
manager is accountable for the unfinished action from the first incident; that conversation is the one
to have. **To the manager**, privately: the warning would punish the person who exposed the gap and teach
the team to hide the next one. **To the team**: the principle in writing, not the case details.

A strong answer distinguishes honest error inside a weak system from deliberate violation, and moves
accountability to follow-through. The weak answer issues the warning "to show standards matter", or
says nothing to the manager and lets resentment grow.

## X1 — The customer's demand for a named person

**Decision:** send a preliminary written report within 48 hours, and the full report within the
contractual five business days, after the internal review. Do not name an individual. Say why: the
company, not a person, is responsible to the customer, and the CTO signs the report.

**Outline of the customer document.**

1. What happened, in plain language, and when.
2. Impact on this customer: affected records, duration, what they need to check.
3. What Northstar did to restore service and correct data, with status.
4. Contributing factors in system terms (no ordering check, no invariant alert).
5. Actions with dates, and how the customer will see that they landed.
6. A named executive contact and an offer of a call with the CTO.

**Protecting the internal review.** The customer document is written from the review but is not the
review. The internal document keeps its candor. A good answer treats the customer's anger as legitimate
and answers it with specifics and commitments. The weak answers are naming the engineer to satisfy the
customer (which destroys the next review's candor) or sending a vague statement late (which loses the
renewal).

## X2 — Bonuses on closure and zero recurrences

**Recommendation:** oppose as designed, and propose a modified form.

**How each number is gamed.** Closure above 80 percent: managers write fewer and smaller actions, close
actions as done before they are verified, or close them as "won't do" quietly. Zero recurrences: failure
modes are described too narrowly to match, severities drift down so fewer events are reviewed, and
incidents go undeclared. The second number is an absolute, like the "zero Sev1" goal in Chapter 27, and
it attacks the honesty of the data the whole system depends on.

**Alternative.** Keep executive accountability for follow-through without paying for the numbers:

- The director reviews the top-priority actions monthly with each manager; managers are assessed on the
  quality of follow-through decisions (interim controls, explicit drops, escalations), with an audit
  sample.
- Organization-level recurrence trend and closure of top-priority actions go to the CTO and board, with
  definitions and paired measures.
- If Victor wants a compensation link, attach it at director level to the organization-wide trend, where
  one manager cannot move it by relabeling.

A good answer predicts the gaming concretely and offers Helena a visible sign of seriousness. The weak
answer either accepts the proposal or rejects it without an alternative.

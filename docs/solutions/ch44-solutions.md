# Chapter 44 solutions — Working with Product: Discovery and Outcome-Based Roadmaps

Worked solutions for the [chapter 44 exercises](../parts/10-business-leadership/44-working-with-product.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Grouping the billing and payments list

**One grouping.**

| Outcome | Items | Measure | Guardrail |
|---|---|---|---|
| Distributors get paid sooner | Dunning emails, payment retry dashboard | Days sales outstanding for distributors using Northstar collection, or share of invoices paid by due date | Complaints from distributors' customers about reminder volume; unsubscribe rate |
| Invoices are right the first time | Reconciliation exception report | Share of invoices corrected or credited after issue | Time finance staff spend on exceptions should not rise |
| Win a named prospect | One more card network | The deal itself | Payment success rate on existing networks |

The invoice PDF redesign has no stated problem. Park it and ask the requester what changes for the
customer if it ships; if the answer is "fewer calls asking what a line means", it joins the second
outcome with a support-contact measure.

**Dates.** Only the card network might carry a date that survives, and only if Greg Tanaka gave it
after sizing or the prospect has a real decision date. If it was given before sizing, renegotiate it
within the week. None of the other items has a contractual or event date.

A good answer notes that the payments area touches tier 1 paths, so every guardrail list includes the
relevant SLO. The weak answer gives each feature its own "outcome" (for example "dunning emails sent"),
which is output renamed.

## F2 — "Product owns what, engineering owns how"

**What the split leaves out.** It puts feasibility after the decision. Of the four product risks, value
and viability sit with product, but feasibility (including operational risk and cost) is only useful
while options are open. The split also leaves nobody responsible for instrumentation, so no one will
know whether the "what" worked.

**A Northstar example.** The duplicate-order warning: the request was a sensible "what", but an engineer
reading the order records found 58 of 70 duplicates were mobile retries after timeouts. The right
change was an idempotency key, which a specification written without that finding would never have
contained. Another defensible example is the 27 baseline defects classified as "requirement
misunderstood; built as specified".

**A clause.** "Before an option is chosen for any item over two engineer-weeks, the named engineer for
the area records feasibility and operational risk, and the causes found in production data, in the
discovery note. The product manager decides; the note is attached to the decision."

A good answer keeps product's decision right intact and adds engineering's information earlier. A weak
answer reverses the split ("engineering should decide what") or treats feasibility as an estimate.

## F3 — How corrected orders could fall without distributors being better off

1. **Abandonment.** The repricing prompt makes buyers give up instead of submitting a wrong order.
   Corrections fall; so do orders. Guardrail: order volume per distributor and carts abandoned at the
   prompt, compared with the same weeks before the change.
2. **Definition drift.** Someone narrows the definition (for example, amendments made by Northstar
   support no longer count, or the window shrinks from 72 hours). Audit: freeze the definition for the
   quarter and have Data and Analytics confirm the query is unchanged.
3. **Displacement.** Errors move to a channel the measure does not see: distributors fix them by phone,
   or credits are issued as manual adjustments in the accounting system. Audit: support contacts tagged
   as ordering errors and manual credit notes, sampled monthly.

Seasonal mix is a fourth possibility: fewer price-list changes in weeks 40 to 48 would lower price
mismatches without any bet working.

**Before reporting,** ask Data and Analytics to rerun the 400-order sample method on a new sample, check
the share of customer changes of mind (60 of 400 at baseline), and report the guardrails beside the
outcome. A weak answer trusts the drop because it matches the prediction; a prediction-matching result
deserves the same audit as a disappointing one.

## A1 — Week 46: one bet worked, the outcome barely moved

**First, is this a failure?** No. Only the idempotency key has shipped. If it removed about 52 of the
340 sampled errors, the expected rate is about 1.105 × 288 ÷ 340 = 0.94 percent. A reading of 1.0 is
close to that: the error rate comes from a sample of corrections, so a 0.1-point move is within
sampling noise, not only 28-day noise. The other bets have not shipped yet. Say so in the
review before anyone concludes the approach failed.

**Repricing.** At about 98.6 percent within 2 seconds, synchronous repricing would breach the proposed
99 percent objective, which is part of the quality floor. Do not ship it as designed. Options:

- **Detect, don't reprice.** Compare the cart's price-list version with the current one at submission
  (a cheap lookup) and reprice only when they differ. Most submissions see no change, so latency falls
  back toward today's.
- **Refresh carts asynchronously** when a price list changes, using the effective-dates work.
- **Fund a cache** in pricing-svc: more capacity and a new consistency risk in a tier 1 path.

Recommend the first option, subject to a short measurement of how often versions differ. Evidence
needed: the share of the 96 stale-price cases caused by scheduled list changes (which effective dates,
due week 46, may remove anyway) and the latency of the version check. A weak answer drops repricing
entirely, or ships it and asks for an SLO exemption.

## A2 — Customer-detected share as a product outcome

**Where it belongs.** Both, with different owners. The customer-detected share (29 percent in quarters 1
and 2, 5 of 17 in quarter 2; quarter 3's share is not recorded) is on the director's scorecard, paired
with contractual availability. Engineering therefore owns the measure and its definition. But some of the bets that would move it are product
work: incident status notifications for distributors, in-product error reporting, and alerting on
correctness failures that customers see first (8 of 14 customer-detected baseline incidents were wrong
amounts or data).

**An outcome entry.** Outcome: customers learn of payment-path problems from Northstar first. Measure:
customer-detected share of Sev1 and Sev2 incidents on the billing and payments paths. Baseline: the
quarter 2 figure for those paths. Target: a direction and a review date rather than a number, because
14 Sev1 and Sev2 incidents in quarter 3, fewer still on these paths, are too few for a percentage target to mean much. Guardrails: alert volume per
on-call engineer and false-page rate, so detection is not bought with noise. Bets: reconciliation
alerts (engineering), status notifications (product; a quarter-3 portfolio initiative), and an error
report link (product).

**Ownership.** The director owns the measure; the product manager owns the product bets and ranks them
against her other work. A weak answer hands the whole measure to product, which invites it to be
reclassified quietly, or refuses product any role, which loses the customer-facing bets.

## A3 — A date given before sizing, after the contract

**Greg first, alone.** Ask what the prospect actually needs by year end: software, a date it can rely
on, or evidence that Northstar understands its purchase-order process. Chapter 42's week 31 conversation
is the model. Do not open with the contract.

**Size it fast.** Honor engineering's side of the contract: a sizing and forecast range within five
working days. If the range fits "before year end" at the cautious end, the problem disappears. If it
does not, give Greg two or three priced options (smaller scope by year end, full scope later, or a
discovery session with the prospect now).

**Amara.** Tell her before she hears it elsewhere, with the options. The contract is hers as much as
yours; ask how she wants sales told about it.

**The account team.** Through Greg, not around him: a revised commitment, or a reduced scope, early.

**The contract.** Add a lightweight path, not a penalty: sales may say "we will confirm a date within
five working days", and the date log records every external date with its source. Review the log
monthly with Greg present. A weak answer escalates to Victor Lindqvist immediately or lets the date
stand to keep the peace; both teach sales the contract does not matter.

## X1 — What the board pack shows

**Recommendation.** Do not remove the roadmap measure in quarter 4; change it in two steps.

- **Quarter 4:** keep "committed items delivered", but count only commitments (contractual, event, and
  sized deal dates), with scope written down. Add one outcome (ordering corrections) as a pilot, with
  baseline, target, and guardrails.
- **Quarter 5:** three outcomes, each one line (baseline, current, target, review date, bets shipped),
  plus the commitment list with on-time delivery. Retire the old count only after the board has seen
  both for a quarter.

**A quarter where two of three outcomes do not move.** Present it as designed: each outcome lists bets
shipped and bets stopped, and why. "We stopped repricing because it would have breached our latency
objective, and found a cheaper version" is information a board can use. Kohavi's experience that ideas
are often mispredicted is a reasonable thing to say to a board, labelled as experience from very large
web companies.

**What not to change.** The Sev1 and Sev2 count stays, and dated commitments stay visible. A CTO who
removes every number the board knows in one quarter looks like they are hiding something. A weak
answer replaces output with outcomes overnight, or keeps the old count and adds outcomes on top
without changing what "committed" means.

## X2 — Funding discovery under flat headcount

**The cost.** 0.6 FTE is about 0.6 × $185,000 = $111,000 a year, about three-quarters of a percent of
80 engineers.

**Evidence from quarter 4 alone.** In the ordering area, 2 engineer-weeks of discovery turned 16
engineer-weeks of requested features (the 6-week warning and the 10-week unit rework) into 13 of bets
aimed at the measured causes. Net of the discovery cost that saves 1 engineer-week (16 − 13 − 2), about
$3,600. More important, the 13 are expected to address about 46 percent of ordering errors, where the
original list addressed the symptom of one cause. The case is effectiveness, not capacity saved. One
quarter in one area is not proof; it is enough to justify a two-quarter trial.

**What to collect.** Per area and quarter: discovery hours; options changed by an engineer's finding;
engineer-weeks of requested work replaced or killed; defects classed "requirement misunderstood" (27 of
212 at baseline); and outcome movement.

**Stop condition.** Stop, or shrink to one area, if after two quarters fewer than one significant
option per area per quarter was changed by an engineer's finding, or if "requirement misunderstood"
defects do not fall. Fund it from the product line, as Amara proposed, so it is visible as a product
investment rather than an engineering overhead. A weak answer argues from the books' authority, or
promises a return the organization cannot measure.

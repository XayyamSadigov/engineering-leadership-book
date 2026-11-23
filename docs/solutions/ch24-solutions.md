# Chapter 24 solutions — Reliability Engineering: SLOs, Error Budgets, Observability, and Operational Readiness

Worked solutions for the [chapter 24 exercises](../parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Two budgets, one incident

**Arithmetic.** A 90-day quarter has 129,600 minutes. At 99.9 percent the contract allows 0.1 percent
of them: about 130 minutes, or 2.2 hours. The internal order journey assumes 600,000 valid submissions
per 28 days, so 99.9 percent allows 600 failed submissions.

**An incident that splits them.** A partial outage is the clearest case. INC-403 failed order
submission only for customers with legacy price lists. If the synthetic probe's test account does not
use a legacy price list, the contract measure records zero minutes of downtime, while the request-based
SLI, assuming 10 percent of submissions failed for 380 minutes, records about 565 failures, 94 percent
of the 28-day budget.

The reverse also works: a total outage of 90 minutes at 3 a.m., when almost no distributors are
ordering, consumes about 70 percent of the quarter's contractual minutes and only a handful of failed
submissions.

**Which better reflects customers?** For the partial outage, the request-based SLI: real customers
could not order, and the probe was blind. For the night outage, the request-based SLI again, because
almost nobody was affected, though the contract will still pay credits. A strong answer concludes that
Northstar needs both: one to manage the service, one to settle the contract, and a plan to bring the
contract's measurement closer to the users' experience at the next renewal. The weak answer picks one
measure and declares the other wrong.

## F2 — What the SLIs would have seen

The 16 incidents detected by monitoring (11) or an engineer (5) sort into three groups.

**Clearly spends budget (5).** INC-402 (bank latency, pool exhausted), INC-413 (partner bank outage),
INC-425 (expired card-processor certificate), and INC-430 (rate limit lowered tenfold) all hit the
payment final-state SLI, provided throttled requests count as bad. INC-415 (memory regression,
restarts under load) hits order availability and latency.

**Possibly, depending on SLI design (5).** INC-404 (auth token change dropped mobile sessions) shows
only if authentication failures on mobile-bff are not filed as client errors. INC-410 (flag enabled for
all tenants) depends on what the flag did. INC-406 (ledger table locked) and INC-419 (pricing rules
evaluated against the old schema) may surface as order or payment errors, or as silent wrong results.
INC-422 (PDF invoices missing tax breakdown) appears only if reconciliation checks rendered documents.

**Not seen (6).** INC-407 (search), INC-423 (exports), INC-416 and INC-428 (the deploy pipeline),
INC-420 (CDN degradation, invisible to a load-balancer SLI because the failure happens before traffic
reaches it), and INC-424 (replicas serving stale balances, a freshness failure).

**What it suggests.** Three gaps: a freshness SLI on balances, client-side or multi-region probe
measurement for the web edge, and a decision about whether the delivery pipeline deserves an internal
SLO for engineers as users. A good answer also notices how often the outcome depends on the 4xx and
throttling classification. The weak answer counts only "yes" and stops.

## F3 — A slow, small burn

**Burn rate.** The error ratio is 0.5 percent against a budget of 0.1 percent: a burn rate of 5.

**Budget consumed.** Two hours at burn rate 5 spends 5 × 120 minutes of budget-equivalent time out of
40,320 minutes in 28 days: about 1.5 percent of the budget.

**Which alerts fire.** None. The one-hour page needs 14.4; the six-hour page needs an average of 6 over
six hours, and two hours at 5 averages under 2 over six hours; the three-day ticket needs an average of
1 over 72 hours, and two hours at 5 averages about 0.14. If the burn continued unchanged, the six-hour
page would still never fire (5 is below 6), and the three-day ticket would fire after about 14.4 hours
(5 × h ÷ 72 ≥ 1).

**Was it right?** For the organization, yes: 1.5 percent of the budget does not justify waking
someone, and the design deliberately trades a little recall for precision. For the distributors, the
answer is more nuanced. At about 6 attempts per minute, roughly 4 payments failed in the two hours.
If they were retried automatically, nobody noticed; if not, those customers have a real problem that
the SLO will not surface. A strong answer separates "should this page?" from "should anyone follow
up?" and suggests a daily report of failed payments for customer success. The weak answer says the
alerting is broken because it missed a real failure.

## A1 — Spreading Billing's pager

**Learn first.** How many pages, at what hours, for which components, over the last quarter; which
pages needed the ledger experts and which only felt as if they did; what the runbooks cover; and what
the engineer who asked to leave is experiencing. The baseline does not record pages per shift, so
measuring it is the first action.

**A plan over two quarters.**

1. Immediately, take the engineer who asked off primary duty for a fixed period, and say so publicly.
   Keep them as an escalation contact for ledger issues only during business hours, by agreement.
2. Build a rotation from all 13 Billing engineers: 24/7 primary and secondary. Thirteen exceeds the
   Workbook's single-site minimum of eight, so the constraint is knowledge, not headcount.
3. Pair: each new engineer shadows the experts for two shifts before taking primary.
4. Write runbooks for the top ledger and invoicing failure modes (INC-406, a ledger migration that
   locked a table; 409, duplicate invoices; 417, payments in the wrong period; 424, stale balances on
   replicas; 427, credit notes applied twice), with the experts as
   authors, and test them in a game day.
5. Delete or demote cause-based pages; move Billing's journeys to burn-rate alerts.

**Measure.** Pages per shift, after-hours pages per person, share of pages escalated to the three
experts, and median restore time for Billing incidents.

**Cost.** Pairing time, slower first responses for a quarter, and the experts' time writing runbooks
(roughly a few days each). Say this to Marcus Oyelaran (Billing manager) and to product up front.

**Tell the engineer** that the request is reasonable, what changes and when, and that asking was the
right thing to do. The weak answer keeps the three experts on call "until the runbooks are done", which
is how the arrangement became permanent.

## A2 — Readiness review for auth-svc

**Conclusion: not ready, and running in production anyway.** The review cannot block a service already
in use; it can only rank and own the gaps. Against the tier 1 bar, auth-svc has a nominal team with no
real owner, partial alerting, no runbook, a deploy path one person understands, and no evidence of a tested rollback.

**What blocks what.**

- No new features on auth-svc until it has a named owning team, an SLO with burn-rate alerting on
  login success, and a reproducible pipeline deploy with tested rollback. Security fixes are exempt.
- Owner: a decision in the review, not a negotiation. Platform Operations is the natural owner given
  that its infrastructure engineers already run it; the alternative is Customer Experience, whose
  frontends depend on it most. Pick one with a review date.
- On-call: five infrastructure engineers is below the Workbook's single-site minimum of eight. Options
  are to merge auth-svc into a wider platform rotation, add staff-engineer cover, or accept
  business-hours plus best effort temporarily. State the risk (INC-404 shows auth changes drop mobile
  sessions).

**Escalate to the CTO** the staffing trade-off (whether to accept below-minimum on-call for a tier 1
service for a defined period) and the knowledge risk of a service one person understands. Kwame Mensah (staff engineer, infrastructure and reliability)
should own the migration off the shell scripts as part of CI consolidation.

The weak answer fails the review and stops. A review that only says "no" to a running tier 1 service
produces nothing; the value is the ranked, owned list of gaps.

## A3 — Keeping the budget visible

**What she is right about.** A budget that is red every week tells product managers nothing new and
can feel like blame. Sales quoting it to customers is a real problem: the budget is an internal
decision tool, and the contract figure is what customers are owed.

**What you will not change.** The budget stays published internally every week. Reporting mode was
agreed precisely because the journey is below target, so a red budget is expected and is not a
breach of the agreement. Hiding it removes the main evidence that the recovery program is working.

**What you will change.**

- Show the trend and the recovery path, not only the red number: budget spent per week against the
  previous four weeks, and which causes are shrinking.
- Split spend by cause: Northstar changes, dependencies, latent defects. Product managers can then see
  which part their roadmap affects.
- Restrict circulation to engineering and product leadership; agree with Greg Tanaka that customer
  explanations come from customer success, using the contract figure.
- Add the date and condition at which the full policy starts, so the budget points toward an end
  state.

**Avoiding the excuse.** A red budget does not excuse a missed date unless the policy says so, and in
reporting mode it does not. The weak answer either stops publishing (losing the evidence) or refuses
to change anything (losing the CPO).

## X1 — A request for 99.95 percent

**What the numbers say.** 99.95 percent per quarter allows about 65 minutes. Last quarter's measured
figure was 99.62 percent, about 492 minutes, on a measurement that excludes mobile. Including mobile
will probably make the measured figure worse before anything improves. Committing now means paying
credits on day one.

**What you tell the CEO.** That a yes this week would be a promise the company cannot measure or keep,
and the credit exposure is likely to exceed the benefit for at least two quarters; that there is a
version of yes that protects the renewal.

**Conditions you could accept.**

1. Measurement first: within one quarter, contractual measurement extended to the mobile path and a
   second region, reported to the customer monthly.
2. A staged commitment: 99.9 percent including mobile from a stated quarter, rising to 99.95 percent
   only after Northstar has run at or above that level internally for two consecutive quarters.
3. Transparency the customer values: monthly SLO reports per journey, and incident communication
   commitments.

**What you need to know first.** The customer's real pain (likely the correctness failures, which no
availability number covers), the credit formula and cap, how much of the $9M the customer represents,
and whether the other renewal customer will ask for the same terms.

The weak answers are a flat yes to save the deal, or a flat no that ignores the commercial stakes.

## X2 — Ending out-of-hours cover for tier 2

**Context from the data.** The eight tier 2 components are catalog, scheduler, search-svc,
invoice-render, erp-sync, reporting-api, webhooks, and document-store. Four of them (scheduler,
search-svc, webhooks, document-store) already have no on-call rotation, so the saving is smaller than
it looks; export-svc, tier 3, has none either. Tier 2 incidents last quarter include INC-407 (search,
nobody on call), INC-408 (month-end reporting), INC-411 (catalog import), and INC-418 (webhook
signatures breaking customer integrations).

**Risks of accepting.** Customer integrations (webhooks, erp-sync) and scheduled jobs often run
overnight; an overnight failure becomes a morning backlog and possibly a customer escalation. Tier 2
problems can cascade into tier 1 paths. Ending compensation can also be read by engineers as a cut in
pay for work they will still be called for informally.

**Risks of rejecting.** Paying for cover that is rarely used, and diluting attention from tier 1.

**Data to ask for.** After-hours pages per tier 2 component over two quarters, customer impact of
those incidents, which components feed tier 1 journeys, and the actual compensation cost.

**A defensible amendment.** Move to business-hours cover for components whose out-of-hours failures
can wait (search, reporting, document-store), keep or add cover for those with overnight customer
impact (webhooks, erp-sync, scheduler), and fix the gaps that create pages. Tell engineers plainly: no
unpaid informal on-call; anyone paged out of hours is compensated.

The weak answer accepts the saving without looking at which components carry overnight customer
traffic.

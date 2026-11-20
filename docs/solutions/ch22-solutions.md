# Chapter 22 solutions — Testing Strategy and Test Architecture

Worked solutions for the [chapter 22 exercises](../parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Where the next ten engineer-weeks go

**The data does not support the manager's claim.** Customers find bugs in the UI because the UI is
where customers are, not because the defects originate there. Classified by earliest practical detection
point, only 41 of 212 escapes (19 percent) are end-to-end flow defects, and that layer already has about
250 browser tests and a 1,900-case manual pass. The layers with the worst ratio of escapes to investment
are integration or contract (49 escapes, 23 percent, and no contract tests) and migration or configuration
(38 escapes, 18 percent, and nothing automated).

**A reasonable allocation:** about five engineer-weeks on consumer-driven contracts for the two or three
busiest tier 1 boundaries, about four on migration rehearsal and configuration validation, and about one
on a mutation-testing pilot in invoicing to see how much of the 57 unit-level escapes come from code that
tests execute but do not check. Browser tests get nothing new; if anything, the slowest and flakiest
should be reviewed for deletion.

**Evidence to change course after a quarter:** the share of new escapes classified as boundary or
migration defects (should fall), contract failures caught in provider pipelines (should be non-zero), and
migration-triggered incidents. A strong answer admits one quarter of escapes is a noisy sample. The weak
answer accepts "customers see it in the UI" as a statement about where defects come from.

## F2 — Retries and the real problem

**The arithmetic.** About 17 runs a day at 9 percent gives about 1.5 spurious red runs a day. If a flaky
failure has, say, a 70 percent chance of passing on each retry, three retries make a red run from a
genuinely flaky test rare. Measured red-main time and measured non-change failures would indeed fall
sharply, probably by more than half, as the team lead says.

**What it does to the real problem:** nothing, and worse than nothing. Flaky tests stay flaky, and new
ones are added unseen because nothing is red. Real failures in non-deterministic code (a race condition,
for instance) also pass on retry and ship. Feedback slows, because a test that fails for real now runs
up to four times before anyone hears about it. Google's published account describes both effects
(Micco, 2016).

**A better proposal:** keep retries only as a two-week stopgap, count every retried pass as a flaky
result on the dashboard, quarantine the worst tests with named owners and deadlines, and set a target
such as non-change failures below 4 percent in one quarter and below 2 percent in two, measured without
retries. A good answer separates the reported metric from the underlying rate. The weak answer either
accepts retries as a fix or forbids them without offering anything for the next two weeks.

## F3 — Replying to the CFO on coverage

**A model reply.** "Line coverage tells us what share of Core's code is executed when tests run. It does
not tell us whether any test would fail if that code were wrong. Research on large Java systems found
only a low to moderate relationship between coverage and how well test suites detect faults, once suite
size is accounted for, and recommended against using coverage as a target (Inozemtseva and Holmes,
2014). Teams given a coverage target tend to write tests that execute code without checking it, and the
number rises while quality does not. Instead I will report monthly the share of escaped defects caught
before customers in each category, our flaky-test rate, and the results of mutation testing on changed
code in the invoicing and ledger modules, which measures whether tests detect deliberately introduced
faults. I will commit to one coverage-related thing: no high-risk module will have code paths that no
test executes at all."

**Criteria:** plain language, no jargon without definition, a replacement measure the CFO can follow,
and an honest statement that the research has limits (open-source systems, mutants as a proxy). The weak
answer agrees to 80 percent because it is easy to report, or refuses without offering anything.

## A1 — Getting the first contract in place

**Learn first.** Ask Elena what "blocked" has cost her before: probably a shared integration environment
that failed for reasons outside her control. Ask Marcus which payment fields his invoicing code relies on;
he may find that the list is short.

**Design.** Billing (the consumer) owns its expectations; they live in Billing's repository and describe
only the fields and behavior invoicing actually uses. Payments and Integrations (the provider) runs them
in its pipeline. A failing contract blocks the provider's merge, and the provider team decides: change its
code, or open a conversation with Billing within one working day. Disputes go to Ines Carvalho, who owns
contract-test standards, with a two-day decision limit.

**The trade.** To Elena: Billing reviews each expectation for meaning, not just shape, so her team is not
blocked by trivial or wrong checks, and contracts replace part of the shared-environment testing she
dislikes. To Marcus: the first expectations are written by Ines with one Billing engineer, charged to
Billing's prevention allocation, so the cost is bounded.

**Criteria:** names an owner for a failing contract, a decision rule, and a time limit; starts narrow. The
weak answer imposes contracts by mandate and leaves the failure-handling undefined, so the first red
contract is simply disabled.

## A2 — Triaging the manual suite

**Categories.** Automate (stable, high-value flows where the expected result is unambiguous); explore
(cases that need judgment, such as usability, unusual data, or new features, converted into time-boxed
charters); delete (duplicates of automated checks, features no customer uses, cases nobody can explain);
keep for now (cases that need automation not yet possible, with a review date).

**Process.** The QA engineers propose a category for each case, with the owning team's engineer agreeing.
Tom Becker and the relevant staff engineer decide contested cases weekly. Deletions above a threshold (say,
any case touching invoicing or payments) need the owning manager's sign-off. The role change from Chapter 19
is announced before triage starts, not after; otherwise the people doing the triage are being asked to
delete their own jobs.

**Keeping releases safe.** The pass shrinks only when automated equivalents are green in the pipeline for
two consecutive releases. The case-to-test mapping is kept so that a later escape can be traced to a
decision.

**Measuring exploration.** Charters record time spent and issues found, and issues are classified by
severity. Charters that find nothing for a quarter are retired or redirected. A good answer measures
exploration without turning issue counts into a target. The weak answer automates everything that can be
scripted and treats exploration as optional.

## A3 — A flakiness policy

**Policy (summary).** Measure: share of Core main-branch runs that fail and then pass on the same commit
with no change, plus retries counted as failures, weekly. Budget: below 2 percent, with an interim target
of 4 percent this quarter. Owner: a rotating flakiness owner in Platform Operations who runs detection and
quarantine; each quarantined test is owned by the team that owns the module it tests. Quarantine: automatic
for any test that flakes more than a threshold in a week; the owning team gets a deadline of two weeks.
The quarantine list is capped (say at 150 tests for Core); when it is full, a new quarantine requires a
fix or a deletion first.
Past the deadline, the test is fixed or deleted by the team's manager, recorded with a reason. Breach: if
the suite is over budget for two consecutive weeks, the teams with the most quarantined tests spend their
next prevention capacity on restoring it. New tests run repeatedly before they join the gate.

**The objection.** Priya Raman's team (or Elena's) is protecting a renewal date and owns many flaky tests.
The policy handles it in two ways: deletion is an allowed outcome, so a team can clear its debt quickly by
deleting duplicates; and the prevention allocation exists for exactly this work, so the policy spends
capacity already agreed rather than new capacity. If the renewal date is genuinely at risk, the director
can grant a dated exception, recorded and visible.

**Criteria:** a precise measure, an owner, consequences, and an exception path. The weak policy says
"flaky tests must be fixed promptly".

## X1 — The manual-regression clause

**Decision: do not accept the clause as written, and offer the evidence the customer is actually asking
for.** The customer wants assurance that releases will not break their business. A contractual manual gate
would lock the release train into large batches, which is the mechanism behind the incidents that made
them nervous; Chapter 27 shows the three-day pass caught none of the nine train-triggered incidents.

**What to offer.** A reliability commitment on outcomes they care about (availability on the order and
payment paths, already 99.9 percent contractually), a quarterly report on change failure rate and
escaped defects affecting them, documented automated regression coverage of their critical flows, a named
exploratory test charter for every significant change to features they use, and early access to
significant changes behind flags in a staging tenant.

**To the CEO.** "The clause would make our releases bigger and slower, and big releases are where our
incidents come from. We are offering the customer stronger evidence than a manual pass would give, tied to
outcomes. If they insist, we can accept a scoped version: human exploratory testing of changes to their
critical flows before release, which we do anyway." Sofia Alvarez should be in the customer conversation.

**Criteria:** separates the customer's need from the mechanism they proposed, ties back to the batch-size
mechanism, and has a fallback. The weak answer accepts the clause to close the deal, or refuses without
an alternative.

## X2 — Hermetic tests or migration safety

**Recommendation: option B, migration rehearsal and configuration validation**, on the baseline data.
Migration and configuration changes caused 8 of 30 Sev1 and Sev2 incidents (5 configuration, 3
migration), and 38 of 212 escaped defects (18 percent) have no automated check today. Incidents are what
the CTO's mandate and the renewals are about, and every incident prevented on the order or payment path
protects service credits and the $9M at risk.

**What you give up.** Option A would cut about 25 minutes from a 74-minute pipeline and most of the 9
percent non-change failures, which matters for developer time and for trust in the suite. That cost
continues for two more quarters. Mitigate partially with the cheap flakiness measures (owner, quarantine,
admission checks), which do not need four engineers.

**Leading indicator within six weeks.** The number of migrations and configuration changes that fail
rehearsal or validation before release. If it is zero after six weeks of real traffic, either the checks
are too weak or the risk was overestimated, and you should revisit the choice. A defensible alternative
answer picks A, arguing that a trusted, fast suite is the foundation for every later investment; it must
then explain how the migration and configuration risk is handled meanwhile. The weak answer chooses on
which problem is more annoying to engineers.

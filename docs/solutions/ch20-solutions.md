# Chapter 20 solutions — Engineering Standards and Their Governance

Worked solutions for the [chapter 20 exercises](../parts/05-engineering-quality/20-engineering-standards-and-their-governance.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — The coverage rule

**Recommended: retire the rule as a mandatory standard.** Apply the chapter's three tests. Does
violating it harm someone outside the team? Not directly: low coverage in a module is the owning team's
risk, and the harm to others arrives through defects, which are measured elsewhere. Can a tool check it
without false alarms? Yes, but the check measures execution, not whether tests would fail when code is
wrong (the Northstar baseline says exactly this). Has anyone acted on it? No: Core has sat at 41
percent for years.

What replaces it is not a different coverage number. A defensible replacement is a **should** in the
guidance page, with intent stated: "New and changed code on tier 1 paths should have tests that would
fail if the behavior changed." Verification is a sampled review of new tests for meaningful assertions,
tied to the escaped-defect classification (Chapter 19 shows that 27 percent of escaped defects were
catchable at unit level and 23 percent at integration boundaries).

An answer that keeps the rule is also defensible if it rewrites it fully: intent (reduce regressions on
tier 1 paths), scope (changed lines on tier 1 components, not whole modules), level, owner (Ines
Carvalho for Core), verification (pipeline report on changed-line coverage, plus sampling), exemption
path, and review date. The weak answer lowers the target to 50 percent, which keeps every defect of
the original rule and makes it easier to game.

## F2 — Placing five standards on the ladder

| Standard | Rung | False alarm cost | Missed violation cost |
|---|---|---|---|
| (a) Formatter | Paved road plus build gate (run the formatter in the pipeline; fail on diffs) | Near zero; formatters are deterministic | Low; review noise |
| (b) Backward-compatible migrations | Human review, sampled, with an automated check for the mechanically detectable cases (dropped columns, renamed fields) as a review-time warning | Moderate; a noisy check is ignored | High; Northstar had 3 migration-triggered incidents and 38 escaped defects from migrations and configuration |
| (c) Structured logs with request id | Paved road (template and logging library do it), with a check in the readiness review | Low | Moderate; slower diagnosis across teams |
| (d) Consumer review of API changes | Automated contract tests where they exist; human review otherwise | Moderate; blocks a change unnecessarily | High; breaks other teams |
| (e) No secrets committed | Build gate (secret scanner) plus pre-commit hook | Some; scanners have false positives, so allow a reviewed suppression | Very high; external exposure |

A good answer notices that (e) is the hardest case: the harm is high enough to gate even though
scanners are not perfectly precise, so the answer must include a fast, recorded suppression path.
That is the exception to "gate only on what is never wrong", and it should be stated as one. The weak
answer puts everything in code review.

## F3 — What the merge request sample shows

**What it shows.** Completion is near universal (38 of 40) and does not depend on the content of the
change: 11 of the 38 ticked "tests added or updated" without any test change. The checkbox measures
willingness to tick boxes. It is a small sample, but the error is not subtle: more than a quarter of
the fully ticked requests carried a false attestation on the item most related to quality.

**What it does not show.** It does not show that the 11 changes needed tests (some may have been
configuration or refactoring with existing coverage), or that engineers are dishonest. The more likely
explanation is that the checklist has become a ritual, which is the decoupling the chapter describes.

**The manager's argument** confuses completion with effect. A measure that is almost always satisfied
and unrelated to what it claims to measure carries no information.

**Replacement.** Remove the box and let the pipeline report, on each merge request, whether test files
changed alongside production code. Reviewers see the fact rather than an attestation. Where a change
needs no tests, the author says why in one line. Then sample a few requests per month to see whether
reviews engage with that report. The weak answer adds a second checkbox or makes the reviewer co-sign.

## A1 — The mobile exemption request

**Do not grant a permanent exemption; do take the request seriously.** Daniel Cho (Customer Experience manager) is right that app store
releases cannot be rolled back like a service deployment. He is asking for an exemption from the
**tool-level wording** of the standard, which is a sign that the standard was written about a mechanism
(automated rollback) rather than its intent (a bad change can be contained quickly and every production
change is traceable).

A good answer rewrites the standard's intent and scope so that mobile can meet it in its own way:
every release goes through the pipeline and is recorded (auditability applies unchanged); "rollback"
for mobile means staged rollout, a remote kill switch or feature flags for risky features, and a
server-side ability to disable a broken client path through mobile-bff. Until those exist, grant a
**time-limited exemption** for the rollback clause only, with a compensating control (staged rollout
to a small share of users for every release) and an expiry of two quarters, owned by Daniel.

The criteria: the audit part is not exempted; the exemption has an expiry and a compensating control;
the standard is improved so the next request does not arise. The weak answers are "rules are rules"
(which forces silent non-compliance) and a permanent blanket exemption (which removes mobile from the
standard entirely, including the auditability nobody disputes).

## A2 — The guild as library approval board

**The problem is real.** A vulnerable dependency is a legitimate reason for a standard, and the guild
members' motivation is an asset.

**The proposal would become a queue.** Northstar has 80 engineers across 24 components and six teams,
four build systems, and services that deploy several times a week. If even a few new libraries are
proposed per week across Java, JavaScript, and mobile, a weekly volunteer meeting with other jobs will
fall behind, and the chapter's arithmetic applies: once arrivals exceed decisions per meeting, the
backlog grows without limit. Teams will then add libraries without asking, which is worse than today
because the board will believe it has control it lacks. Review by committee also tends to check what
is easy to see (licence, popularity) rather than what matters (known vulnerabilities, maintenance).

**Offer instead:** an automated dependency scan in each pipeline that fails on known critical
vulnerabilities, starting as a warning while existing findings are cleared; a short guidance page on
choosing dependencies; a named owner (Kwame Mensah or Li Na Zhou, by stack) for exemption decisions
within ten working days; and the guild's role as the place that reviews the scan's not-useful reports
and proposes changes. This gives the guild real influence without decision rights over individual
changes. The weak answer either accepts the board or dismisses the concern.

## A3 — The tier change request

**Who decides:** not Priya Raman (Orders manager), and not the director alone on opinion. Tier is assigned by a business
criterion stated in advance, at Northstar "on the order or payment path", and confirmed by someone
outside the owning team (the standard owner, Kwame Mensah, with the director as escalation).

**Apply the criterion.** Pricing rules determine what an order costs. If a bad pricing rule change
can stop orders or misprice them, the component is on the order path regardless of whether it is
"configuration". Configuration changes caused 5 of Northstar's 30 incidents, so the argument that
configuration is lower risk runs against the data. The likely decision is that core/pricing-rules stays
tier 1.

**Handle it well.** Acknowledge the real issue under the request: Orders now owns obligations
(runbook, complete alerts) it lacks capacity for. Offer to count that work against Orders' prevention
allocation (10 percent of Orders' capacity in quarter 1, protected for the renewal commitment), and if needed agree
a short exemption with an expiry for the runbook while alerts come first.

**Watch for tier deflation** across the organization in the following month: count tier change
requests, check whether they cluster after the announcement, and publish the decisions and reasons so
that the criterion becomes visible. The weak answer approves the request to avoid conflict, or refuses
it without engaging the capacity problem.

## X1 — The security review statement

**Advice: do not make the unqualified statement.** It is false: four services deploy by shell script,
including auth-svc, a tier 1 component that sits on the login path of both frontends. A customer
security review may ask for evidence, and a false statement discovered during a renewal does more
damage than the gap itself. The customer's stated concern is reliability; being caught overstating
controls converts a reliability concern into a trust problem.

**What to say instead:** "Every tier 1 production change except one goes through an auditable pipeline,
and that one is under a recorded exemption with a migration completing at the end of quarter 2.
Here is the evidence." That statement is true, specific, and shows governance working.

**Evidence to bring:** pipeline records for a sample of recent tier 1 deployments; the standards
register entry with intent, scope, and verification; the exemption register entry for auth-svc with
its compensating controls and expiry; and the migration plan. If the customer asks about the three
tier 2 and tier 3 script-deployed services, answer plainly.

**The broader point** for a CTO: enterprise minimums are worth little unless the CTO can show system
evidence for them, and reporting exemptions is a strength in a review, not a weakness. The weak answer
makes the statement and hurries the migration, hoping nobody asks.

## X2 — Standards for an acquired organization

**Standardize immediately** only the enterprise minimums that protect shared customers and the
company's external commitments: tier assignment by Northstar's business criterion, named owners and
on-call for tier 1 components, auditable pipelines for production changes, tracked reviews for Sev1
incidents, and security minimums such as secret scanning. Give a timeline (for example two quarters)
with exemptions recorded in the same register, because the acquired organization will not meet them on
day one. These are the properties a CTO must be able to report truthfully for the whole company.

**Leave alone** its code standards, tools, and internal practices, unless and until code or teams are
shared. Forcing Northstar's Core style rules or CI choice onto a well-run organization destroys value
for consistency nobody needs yet.

**Its council** keeps governing its internal standards, with one change: it maps its mandatory set to
Northstar's enterprise minimums and reports compliance in the same format. If it works well, it is a
model, not a problem; the chapter's warning is about councils that approve individual cases and become
queues, and a council that has not become one should be watched, not dismantled.

**Later cases** are decided by the boundary rule: when a standard concerns something that crosses
between the two organizations (shared services, shared customers, shared on-call), the enterprise
version applies; otherwise local standards stand. The weak answers are "everything Northstar's way by
next quarter" and "nothing changes".

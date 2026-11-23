# Chapter 32 solutions — Platform Engineering, Developer Experience, and Legacy Modernization

Worked solutions for the [chapter 32 exercises](../parts/06-technical-leadership/32-platform-engineering-developer-experience-and-modernization.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Which requests become self-service

**Rank by the selection rule.** Test environments come first: about 25 a month, each a multi-day
wait (about 6 days at baseline) that blocks testing, and one of the few request types that is
standardized enough to automate. Pipeline variable changes on GitLab CI (about 12) come second: small,
frequent, and safe to delegate with guardrails (validation, audit log, review for secrets). Production
log access (about 15) can become self-service only with access policy behind it: role-based access
granted by the team's manager and logged, not a free-for-all, because logs can hold customer data.

**Not self-service.** Help debugging failed Jenkins builds (about 20) is not a self-service candidate as
written; it is a symptom. The right response is to reduce the cause (flaky tests, unclear error
output, the Jenkins knowledge concentrated in Bram Verhoeven) and to improve the feedback the pipeline
gives, which DORA's capability page links to positive user experience. Service scaffolding (2 a month)
is too rare to justify building a generator now; a written template is enough.

**What to know first:** how long each request type takes to fulfil, how many are repeats from the
same team, and which ones block work.

**Weak answer:** automating by volume alone, which would put Jenkins debugging first and build a
"self-service" form that still routes to a person.

## F2 — Adoption from 35 to 65 percent

**What the number could mean.** Of 17 deployable units, 35 percent is 6 (the GitLab CI services that
were there before the project) and 65 percent is 11, so five units moved. If they were the four shell-
script services plus one Jenkins service, that is real progress on the riskiest path.

**What it could not mean.** It says nothing about whether the template is better, whether teams moved
voluntarily, or whether loops got shorter. It counts units, not deployments: a rarely deployed service
counts the same as payments-gateway.

**How it could rise without improvement:** migration by decree; counting a unit as migrated when only
its build runs on the template while deploys still use the old script; moving the easiest units first.

**Two measures to require beside it:** the change failure rate and deployment frequency of migrated
units before and after (did the move make changes safer?), and the units left on each old system with
a switch-off date (is "four becomes five" happening?). A survey item on cognitive load by team is a
reasonable third.

**A good answer** reports the baseline of 6 explicitly. **The weak answer** accepts 65 percent as
success, or rejects the figure without proposing what to report instead.

## F3 — Rewriting invoice-render

**Classification.** invoice-render is tier 2, a single service, with no runbook and no alerts. It fits the
last row of the modernization table only if its behavior can be pinned down by tests before the rewrite
starts. "Nobody understands it" is a reason to doubt that: the engineer would be specifying behavior they
do not yet know, which is exactly Spolsky's warning about discarding embedded fixes.

**Recommendation:** treat it first as improve-in-place. Spend one or two weeks writing characterization
tests that capture current rendering for a sample of real invoices (including currencies and credit
notes), add alerts and a runbook (operational work Billing owes anyway), and only then decide. If the
tests show the service is small and its behavior is now specified, a time-boxed rewrite becomes a
reasonable candidate, with the old service running in parallel and outputs compared before cutover.

**What to ask for before agreeing:** the parity test set, the cutover and rollback plan, the date the
old service is deleted, and why a different language is worth the cost to Billing's on-call (who will
support it at 3 a.m.).

**Weak answers:** approving because the service is small, or refusing because "we never rewrite". A
small, specifiable component is the case where rewriting can be right.

## A1 — The mandate request

**Response.** The director should take the problem seriously (running four systems costs about 1.5 FTE
a year and keeps the script path one engineer understands) and decline the tool mandate as asked.

**What to mandate:** the outcome. Deployment of tier 1 services through an auditable pipeline
with automated rollback is already a standard (Chapter 20). Set a date for tier 1 services to meet it,
by any compliant path. Also mandate that the shell-script path is switched off by a date, because it is a
known risk, not a preference.

**What not to mandate:** that every team use the template by quarter 4. DORA's 2024 data associate
exclusive mandated platform use with lower throughput, and a mandate would remove the signal of whether
the template is good. It would also land on Orders and Billing during the bulk-ordering push.

**What to offer Tom instead:** make the template the cheapest way to comply (pairing on each team's
first migration, templates for each service type), publish monthly units left per old system and the
reasons from non-adopters, and agree a review at the end of quarter 3. If teams with no good reason
still have not moved by then, a deadline becomes defensible.

**Weak answer:** granting the mandate to back the platform team, or refusing with nothing offered.

## A2 — export-svc stays on the scripts

**Weigh the reasons.** Data and Analytics' objection is legitimate: 12 percent of its capacity already goes
to other teams, and export-svc is tier 3 and rarely changes. But the cost of its staying is not borne by
Data and Analytics. While export-svc uses the shared script, the script path, its secrets on the build
host, and the knowledge concentrated in one Platform Operations engineer all remain.

**Options:** (1) Platform Operations migrates export-svc itself, since a rarely changing tier 3 service
is a small job once the template exists, with Data and Analytics reviewing; (2) defer to quarter 3 with a
date; (3) mandate. Option 1 is the strongest: the beneficiary of retiring the path pays for the last
step, and the request does not compete with Data and Analytics' queue. It costs Platform Operations
perhaps a week from its 29 engineer-weeks.

**How others read it.** Other teams will see whether "voluntary" means the platform team does the
work for reluctant teams. Make the rule explicit: Platform Operations pairs on first migrations and will
migrate low-change tier 3 services itself when that is cheaper than waiting.

**Weak answer:** forcing the migration without addressing the team's capacity, or exempting export-svc
indefinitely and leaving the script path alive.

## A3 — Re-platforming core/order-capture

**Against constraint 3.** It is not a rewrite of all of Core, but re-implementing a tier 1 module on the
order path as a new service is a large replacement of the most business-critical code. As proposed (30
percent of a 16-person team, about 4.8 engineers or 62 engineer-weeks a quarter, for two quarters) it risks becoming the
stealth rewrite the chapter warns about.

**The framework.** The module changes often and fails often, so "leave alone" is out. The question is
whether it can be made cheap to change in place first: owner-based review, contract tests at its
boundaries with pricing-svc and invoicing, runtime flags, and the hermetic test work. Look at which of
Orders' incidents a new service would actually have prevented; many were release-train and
migration-borne, which the platform and pipeline work addresses directly.

**Conditions for approving a version:** a specific seam and first slice (for example, order validation
or bulk file intake, which Orders now knows well), transitional routing with a removal date, parity
tests against production behavior, a measure of success (Orders' change failure rate and lead time for
that slice), and a stop point after one quarter with value kept.

**Weak answers:** approving because Orders has the most incidents, or rejecting because "no rewrite"
without recognizing that a sliced extraction is allowed.

## X1 — Buying a developer portal

**Decision: defer, and pilot cheaply.** At $180,000 a year the portal takes 72 percent of the
$250,000 discretionary budget, leaving $70,000 for everything else. Anything more needs the CFO.

**Against the chapter's tests.** Which loop does it shorten? A service catalog and scaffolding help
with orientation and new services, but scaffolding requests are rare (2 a month in F1's intake), and
its long loops are environments and the Core pipeline. The deployment-event store's dashboards can be
built on existing tools. A portal could also become ticket-ops with a nicer face if the actions behind
it are still manual.

**What would change it:** evidence that teams struggle to find owners, runbooks, and dependencies (a
real problem at Northstar given disputed ownership), and that a portal would be used. Run a quarter with
a thin, free catalog (a maintained page or an open-source portal on existing infrastructure) and
measure use by team.

**Renewal criteria if bought later:** weekly active use across most product teams, repeat use of
self-service actions, and measurable reduction in requests to Platform Operations, reported against
the baseline. A tool that only the platform team opens should not be renewed.

**Weak answer:** buying because the market says platforms need portals, or declining without a test.

## X2 — The board asks about replacing Core

**Position.** State plainly that a full rewrite is not recommended, and why: Core carries every order and
invoice for about 1,900 customers; a rewrite would take engineers from teams already constrained by
flat headcount, pay nothing until cutover, and concentrate all risk there. Say honestly that the case
rests on expert opinion and Northstar's own constraints, not on research proving rewrites fail.

**Evidence of progress to show:** Core lead time and change failure rate trends since the baseline
(19 days and 31 percent; 22 percent at day 90); modules with clear owners; slices extracted and
transitional code removed; changes still requiring core/permissions after its extraction; CI systems
retired; incidents via Core releases over time (9 at baseline, 4 at day 90). The competitor's stack is
not itself evidence of anything about Northstar's customers.

**What would change your mind:** the runtime or core libraries reaching end of support with no viable
upgrade path; incremental work stalling (no slices completed for several quarters, lead time flat); or a
product direction Core's model cannot support, such as a new business line. Name these in writing so
the position is falsifiable.

**A good answer** is short, shows trends against the baseline, and commits to revisiting. **The weak
answer** is a defensive essay, or agreement driven by the competitor's announcement.

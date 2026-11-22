# Chapter 53 solutions — Risk, Governance, Regulation, and Security Strategy

Worked solutions for the [chapter 53 exercises](../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional; the week 44 snapshot and the draft register are the chapter's additions.

## F1 — Splitting the one corporate technology line

**Splitting "Cyber attack or IT outage."** The one canonical line splits into at least three
statements. (a) "Because a known-exploited
vulnerability in auth-svc can only be mitigated at the load balancer until the service leaves its
shell-script deploy, an attacker may bypass the restriction and reach customer sessions, which would
expose customer accounts on the order path." Owner Tom Becker; accepter Victor Lindqvist; indicator:
days the item has been open past the 7-day service level, and any change to the load balancer rule.
(b) "Because two script services still keep production secrets in a plain file on the shared build host and no tier 1 artifact has
signed provenance, a compromised build host could ship altered code to production." Owner Kwame Mensah;
accepter Victor; indicator: script services with plain-file secrets (2) and tier 1 components at SLSA
Build L2 (0 of 15). (c) "Because employee identities are managed by IT and production roles are granted by engineering, a
compromised employee account could reach production systems." Owner Marta Kowalczyk; accepter Rajiv
Menon; indicator: production roles held by accounts without strong authentication.

**The two missing lines.** The corporate register says nothing about risks that are neither attacks
nor outages. The two clearest gaps come from engineering's TR register.

*An unsupported platform*: "Because the Core framework is past community support (TR-01), a critical
disclosure may have no patch, which would leave a tier 1 path exposed or force an emergency migration
costing $96,000 to $194,400 on Finance's scenarios (120 to 243 engineer-days)." Owner Ines Carvalho; accepter Victor; indicator: Core criticals
held open by the framework (1 in week 44) and days since the last available patch.

*Knowledge concentrated in one person*: "Because ledger currency and rounding (TR-07), the Jenkins
controller (TR-02), and the shell-script deploys (TR-06) each depend on one person, that person's
absence during an incident could leave a tier 1 path or financial correctness without anyone able to
respond." Owners per system (Marcus Oyelaran, Tom Becker); accepter Victor; indicator: people able to
respond alone on each system, recounted quarterly. Choosing financial correctness (TR-07, TR-09) as one
of the two missing lines is equally defensible, since it is a Sev1 consequence the corporate register
does not mention.

A good answer names causes from the canon, separates owner from accepter, and picks indicators that move
before the event, and notices that the corporate register's single line omits whole categories of
technology risk. The weak answer rewords the line ("Risk of cyber attack due to threats"), keeps one
owner for everything, and proposes no missing lines.

## F2 — Four risks scored 12

All four score 3 × 4 or 4 × 3, so the matrix says they are equal. Cox's analysis predicts why that
misleads: matrices have poor resolution (they assign identical ratings to risks of very different
sizes), their inputs are interpreted differently by different raters, and their categories do not
support allocating money between risks. Here the four have different consequence types (customer
financial error, a platform that cannot be patched, lost sales, an identity compromise), different
owners, different trends, and treatment costs that differ by an order of magnitude.

What the committee should see, per risk: one sentence of consequence; the exposure entry (ER-05 has a
priced treatment of $96,000 to $194,400 on Finance's scenarios; ER-06 has at least one $310,000 deal and 476 hours a year of
questionnaires; ER-02 and ER-08 are honestly "not quantified"); the trend; the treatment decision and
who accepts the residual; and whether it is inside the proposed appetite.

Which to discuss first: ER-06, because it is the only one of the four that needs a decision from
executives now (attestation options A, B, or C) and it is worsening as renewals approach. ER-02 is a
strong alternative, because a customer-visible financial error is a Sev1 by Northstar's definition and
the risk sits on two one-person systems. The weak answer re-scores the four until they differ, which
keeps the false precision and adds argument about the decimals.

## F3 — Obligations, controls, evidence

| Obligation | Control | Evidence from | Owner | True on paper, failing in fact |
|---|---|---|---|---|
| 99.9 percent availability | SLOs and error budget policy; tier 1 minimums | Synthetic checks; incident tracker | Engineering Director, with team owners | Checks from one region miss the mobile path (a known baseline weakness), so availability reads high while mobile users fail |
| Change management under an attestation | Every tier 1 change reviewed and deployed through an auditable pipeline | Repository and pipeline logs | Kwame Mensah (pipelines), teams | Reviews exist but are rubber stamps, as in the baseline pull request checklist where ticked boxes were false; sample reviews against diffs |
| Card data protection | Card numbers handled only by the processor's hosted fields and tokens; scope boundary documented | Network and access configuration; annual scope review | Joon Park, with Elena Sokolova | A logging change captures request bodies containing card data; the scope document stays unchanged |
| SBOM and SSDF evidence | SBOM generated per build; remediation service levels | Build artifacts; scanner and exception records | Kwame Mensah; Joon Park | SBOMs cover 14 of 15 tier 1 components, and the one missing (auth-svc) is the one with the known-exploited item |

A good answer names a system, not a person, as the evidence source, and finds a gap for each control.
The weak answer lists policies ("we have a change management policy") as evidence. Where an answer
treats card scope differently, for example by assuming payments-gateway is inside the cardholder data
environment, that is defensible if the reasoning is stated; the point is that the scope has not been
reviewed.

## A1 — Extending the auth-svc exception

**Who may approve.** The residual risk is a known-exploited critical on an internet-facing tier 1
component: under the chapter's acceptance rules that is CTO level, and an expired acceptance escalates
rather than renewing at the same level. If the draft appetite line 2 is adopted in week 50, the
extension also breaches its one-quarter limit (the exception has already run since quarter 1), so
Victor would have to report it to the audit committee as outside appetite. If the line is not adopted,
the acceptance still belongs to Victor, because the director accepted it originally and the rules say
expiry escalates.

**Required before approval.** Evidence the compensating control works (a test from outside showing the
vulnerable endpoint is unreachable), detection on the restricted path, a named owner and a dated plan for
moving auth-svc to an auditable pipeline that does not depend on all of phase 1 (moving auth-svc first
is an option), and the capacity to do it. Thirteen weeks (52 to 65) is acceptable only with that plan.

**What the committee is told.** The item by name, the control, the new expiry, and why the fix slipped.
A good answer escalates, conditions, and discloses. The weak answer renews quietly because "the
control has held for months", which is the exception that never ends.

## A2 — Replacing the security report

For Marta Kowalczyk and Rajiv Menon, monthly:

| Measure | How it is gamed | Paired with |
|---|---|---|
| Criticals and known-exploited items open past service level, by component and age | Downgrades; "not affected" without analysis | Joon Park's monthly sample audit of closures and downgrades |
| Exceptions by age and accepter level | Renewal under a new date | Exceptions older than one quarter listed by name |
| Tier 1 coverage: SBOM per build, auditable pipeline, signed provenance | Counting components with the tool installed but output unused | Share of findings with an owner's decision within service level |
| Secrets in plain files; certificates with owner and alerting | Inventory omits hard cases | Expiry and leaked-credential incidents |
| Questionnaire hours and attestation requests | Under-recording time | Deals where assurance was raised, from Greg Tanaka's pipeline |

Penetration test findings stay as context, reported as findings open past their due date, not as a
count. Phishing click rate and training completion move to an appendix: they are activity measures and
improve with easier simulations.

For the audit committee, twice a year: the risks outside appetite first; three exposure measures with
trend (known-exploited open past 7 days, exceptions older than one quarter, tier 1 control coverage);
and what is accepted, by whom, until when.

A good answer pairs each measure with a check run by someone other than the classifier. The weak answer
adds exposure measures but keeps the activity measures at the top, where they will be read.

## A3 — Greg Tanaka's SOC 2 commitment

**Reply to Greg (sketch).** "I can't confirm a SOC 2 report within 12 months yet, and I don't want you
to promise it, because if we miss it the prospect has grounds to leave and we have taught them our
commitments are soft. Here is what we can offer now: a completed security questionnaire with evidence
from our systems (scanning on all 24 components, SBOMs for 14 of 15 tier 1 components, remediation
service levels and their record, our latest external penetration test summary), and a call with Joon
Park and me. Whether Northstar pursues an attestation is a decision Victor takes to the executive team,
with options in front of the audit committee in week 50. If they approve an audit in year 2, I will tell
you the earliest date we can commit to, and you can offer it then. Can you ask the prospect whether a
signed commitment to start the audit by a date, with a right to terminate if it slips, would satisfy
procurement?"

The reply follows Chapter 48's rule that no customer date is given without an estimate and an owner, and
offers Greg something usable now. A good answer names who decides and when, and proposes contract
language that matches what is true. The weak answers are a flat "no" with nothing to offer, and "yes"
to keep the deal, which commits Northstar to a cost the executive team has not approved.

## X1 — Victor's SOC 2 decision

**Costs (illustrative, from the case).** A: cash $75,000 to $100,000 a year plus about 1 FTE of internal
effort in year 1 (about $185,000 of capacity), with an audit started in year 2. B: readiness work in
quarters 5 and 6, roughly half that effort (about $92,500 of capacity) plus the tool if bought, and an
audit decision at the week 78 gate. C: the evidence library only, a fraction of an FTE. The status quo
costs 476 hours a year of questionnaires, about 0.26 FTE or $48,100 of capacity (0.26 × $185,000),
plus Victor's own time, plus unknown deal friction. The prospect is worth $310,000 a year, about $223,000
of gross margin at 72 percent.

**A defensible proposal.** B, presented to the executive team with the $150,000 continuation ask, since
both compete for the same tooling budget and Rajiv Menon will want one view. To the audit committee,
Victor presents ER-06 with the options and his recommendation, and asks the committee to note it rather
than decide it, because it sits inside management's budget envelope.

**What would make A right.** Victor would need to believe that more than one deal or renewal of
meaningful size depends on a report within about a year, that readiness gaps (auth-svc's pipeline,
signed provenance, the evidence library) can close before the audit window, and that the cash can be
found without cutting the prevention allocation. Two more prospects making a report a condition of
signature would be the evidence. A good answer states costs in capacity and cash separately and names
the switching evidence. The weak answer chooses A "because enterprise customers expect it" without
checking readiness, which buys a year of evidence collection for controls that do not yet run.

## X2 — Where Joon Park's function should report

**A defensible recommendation (about 250 words).** "Keep security's independent audit role in IT, and
create an application security role in engineering with a dotted line to Joon Park. Today's placement
sees corporate systems well and product risk poorly: the security function cannot direct the teams that
change code, and its report to Marta lists activity, not exposure. Moving the whole function under me
would give it authority and context, but it would remove the only check on engineering's own 'not
affected' decisions that does not report to me, which is Marta's point and a fair one. Creating a head of
security reporting to you would fix independence and authority at once, but at Northstar's size it adds
an executive to a two-person function and does not add capacity. The hybrid adds capacity where the risk
is (the build path and tier 1 services), keeps audit independent, and needs one seat. Under the 87-seat
rule that seat comes out of engineering, so it competes with the workforce plan. In two quarters I
would expect: exposure measures in the monthly report; the sample audit of classifications run by
IT security every month; questionnaires answered from the evidence library without reaching me; and the
auth-svc item closed or escalated on time. If those do not happen, the placement is not the problem."

A good answer weighs independence against authority, names the capacity constraint, and sets checkable
expectations. Recommending a move under the CTO is also defensible if it keeps an independent audit,
for example through an external firm. The weak answer argues from organizational charts at other
companies and never mentions who audits engineering.

## X3 — Halvard's enterprise register

**Roll-up rules.** Each vice president keeps a group register, reviewed monthly by the group's
directors. An item reaches the enterprise register only if its consequence crosses groups, touches a
customer contract or revenue at renewal, financial correctness, or a legal obligation, or needs an
accepter above the vice president. Items with the same consequence are grouped under one enterprise
risk with a sources column listing the group items, so the roll-up stays auditable.

**Vendor risk.** The 60 vendor engineers on two contracts become one enterprise risk per contract only
where a vendor holds production access or knowledge no employee has; otherwise vendor items stay in the
group registers. Each such risk names the employee who owns the contract outcome.

**Acceptance.** Group items inside appetite are accepted by directors; tier 1 and financial risks by vice
presidents; risks outside appetite by the CTO, and reported to the audit committee. Halvard's
remediation service level policy, owned by a principal engineer, supplies one appetite line directly.

**Under a dozen lines without hiding.** Group by consequence; publish the full group registers to the
CTO's staff; and audit the roll-up quarterly by sampling ten group items and checking each maps to an
enterprise line or a recorded reason it does not. A good answer makes the filter explicit and auditable.
The weak answer caps the register at twelve by dropping items, which is hiding risk by design.

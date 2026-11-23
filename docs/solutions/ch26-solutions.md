# Chapter 26 solutions — Security and Software Supply-Chain Quality

Worked solutions for the [chapter 26 exercises](../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Security controls that failed as availability incidents

**INC-404 (auth-svc, token lifetime).** The control is session token lifetime, a security setting that
trades exposure against user convenience. The gap is change management: the setting lived in a
production configuration file on a script-deployed, orphaned service, with no review, no staged
rollout, and no owner who understood the mobile client's dependence on it. A useful leading measure:
the share of tier 1 security-relevant configuration that is version-controlled and deployed through a
reviewed pipeline (for auth-svc, zero).

**INC-418 (webhooks, signature format).** The control is message signing, which lets customers verify
that events come from Northstar. The gap is contract and ownership: the service was orphaned "by
default", and a change to a customer-facing security contract shipped without versioning or a threat
modeling question ("what breaks for verifiers if this changes?"). Leading measure: customer-facing
contracts with explicit versioning, or design changes on trust boundaries reviewed with the four
questions.

**INC-425 (payments-gateway, expired certificate).** The control is TLS authentication to the card
processor. The gap is inventory and ownership of access material: nobody owned the expiry date.
Leading measure: certificates with an owner and expiry alerting, which at baseline was zero of 34.

A good answer notices that all three are ownership and change problems, not knowledge problems, and
that none would appear in a vulnerability count. The weak answer proposes "more security training".

## F2 — Replacing a vanity security report

**Total vulnerabilities found** rises when coverage improves and falls when scanning is narrowed or
findings are suppressed, so it can improve while exposure grows. Replace with open criticals past
service level, by age, paired with scanning coverage of tier 1 components.

**Scans run** measures activity. Teams can run more scans that nobody reads. Replace with the share of
findings that received an owner's decision (fix, exception, not affected) within a week.

**Training completion** can reach 100 percent with click-through modules and no change in code.
Replace, if anything, with an outcome tied to design: share of trust-boundary design changes that had
a threat-modeling conversation, sampled for quality.

**Findings closed** rewards closing easy items and "not affected" decisions. Pair with a sample audit
of not-affected and downgrade decisions, and report time from disclosure to fix in production
(median and 90th percentile) rather than counts.

Criteria for a good answer: each replacement measures exposure or coverage, each has a named pairing,
and the answer predicts that honest measurement will make some numbers worse at first. The weak answer
keeps the counts and adds targets.

## F3 — SLSA levels at Northstar

Assumptions to state: the Jenkins controller is self-managed and generates no provenance; GitLab CI
and GitHub Actions can generate provenance but are not configured to; source for all components is in
Git; protected branches exist on some repositories but not consistently.

| CI group | Components (tier 1) | Build level today | Source level today |
|---|---|---|---|
| Jenkins | 12 (8: six Core modules, pricing-svc, tax-svc) | L0 | L1, perhaps L2 on Core |
| GitLab CI | 6 (4) | L0, L1 within reach | L1 to L3 depending on branch protection |
| GitHub Actions | 2 (2) | L0, L2 within reach on a hosted platform | L1 to L3 |
| Shell scripts | 4 (1: auth-svc) | L0 | Effectively below L1 for what is deployed: the build host can build a working copy with local edits, so the artifact cannot be tied to a revision |

The single change that raises the most tier 1 components by one Build level is provenance generation
for the Core build (or moving it onto a platform that generates provenance), because one artifact
carries six tier 1 modules, and with pricing-svc and tax-svc that is eight of fifteen. A strong answer
notes that the most dangerous gap is still auth-svc, even though it is one component, and that "most
components raised" and "most risk removed" are different objectives. The weak answer assigns levels
without stating assumptions, or quotes the retired SLSA 1–4 ladder.

## A1 — The Core criticals Billing owns

Start with evidence, not the argument. Ask for: the vulnerable library and function; whether the
affected code path is reachable from any input an external party controls (including files uploaded
by customers and messages from partners, not only HTTP); whether the issue is in the KEV catalog; and
what a compensating control would look like (disable the feature, validate input upstream, isolate the
parser).

A defensible decision: if not KEV-listed and not reachable from external input, approve an exception
for one quarter, with the upgrade scheduled into Billing's prevention allocation for the following
quarter and staged behind the release-train improvements so it ships in a smaller batch. If
reachable, apply a compensating control within the service level and keep the exception short. Record
the decision in the exemption register: owner (Marcus Oyelaran, Billing manager), reason, compensating control, expiry, and who
reviewed the reachability analysis (someone outside Billing, such as Joon Park, the IT security lead, or a staff engineer).

Marcus is right about two things worth saying out loud: a rushed framework upgrade could cause the
ledger incident the vulnerability never would, and his team's allocation is already the largest. The
weak answer either orders the fix in 30 days regardless of risk, or accepts "internal-only" without
checking it.

## A2 — A champion role that is not nominal

Eligibility: any engineer with at least six months on the team and interest; avoid making it a
default duty of the most senior person, who is usually already overloaded. Selection: volunteers
first, confirmed by the manager; the Visma study's distinction between voluntary and assigned
champions suggests motivation differs, so prefer volunteers and accept an assigned champion only with
an explicit conversation about the role.

Time: about 10 percent, protected in planning as part of the team's prevention allocation. Duties:
triage the team's new findings weekly with the manager; join design reviews that cross trust
boundaries and run the four threat-modeling questions; be the first contact for the security
function. Connection: a monthly session with Joon Park's function, a shared channel with a response
expectation, and a named counterpart for escalation, because the e-commerce case study found champions
without support stalled.

Signals after two quarters: champions are named in design review records; time from finding to owner
decision has fallen in their teams; attendance at the monthly session holds; and champions can name a
change they caused. Signal of failure: the role exists only on a list. The weak answer creates the
role with a channel and no time.

## A3 — Answering "confirm alignment with NIST SSDF"

Do not answer "yes". The SSDF is a set of practices, not a certification, and a blanket confirmation
would be a claim Northstar cannot evidence at day 30.

A good structure follows the four practice groups. **Prepare the Organization**: describe the
remediation policy, ownership assignment, and security capacity earmark, with dates. **Protect the
Software**: state what is true (source in version control, protected branches on some repositories,
secrets rotation completed for live leaked credentials) and what is in progress (moving secrets out of
plain files, pipeline consolidation for script-deployed services). **Produce Well-Secured Software**:
describe dependency scanning coverage (8 of 24 at baseline, with the plan and date for full coverage)
and threat modeling starting on new designs. **Respond to Vulnerabilities**: give the service levels
and say honestly that the record begins this quarter.

Decline to claim SBOMs for the whole product; offer a date for tier 1. Offer a quarterly update. The
criteria: every claim is backed by evidence that could be shown on request, and gaps are named with
dates. The weak answer overclaims to protect the renewal, which converts a sales risk into a contract
and trust risk.

## X1 — Buying a platform or building the pipeline

Recommendation (one defensible answer): spend the quarter on pipeline consolidation and SBOM
generation with existing tools, and defer the platform decision by one quarter.

Reasoning: the questionnaire problem is an evidence problem, and evidence comes from pipelines. A
platform layered on four CI systems and four script-deployed services will scan more, but it cannot
produce provenance for artifacts built on a shared host, and it cannot rotate secrets or assign owners.
It would also consume $180,000 of the $250,000 discretionary budget, leaving little for the quality
program's other tooling needs. What you give up: faster scanning coverage and a polished report for
customers this quarter, and possibly some findings a commercial tool would catch that open-source
scanners miss.

What would change your mind: if the consolidation slips so that tier 1 coverage is still under
two-thirds by the end of the quarter; if a renewal customer requires a specific attestation format
the platform provides and existing tools cannot; or if the open-source tools prove too noisy for teams
to triage. A strong answer treats the platform as a possible later step once there is one pipeline to
attach it to. The weak answer frames it as "buy versus build" without asking what problem the
questionnaire actually exposes.

## X2 — "SLSA Level 4 by year end"

**In the meeting (about 110 words):** "I share the concern, and I want to commit to something we can
deliver and show you. SLSA's current version doesn't have a single Level 4 for all software; it has a
Build track that tops out at Level 3 and a Source track with a Level 4 for two-person review. Today
most of our software is at Build Level 0, because four different build systems produce no record of
how artifacts were made. I'll come back with a target by tier: our order and payment path first, with
dates, and the evidence you'll see each quarter. Committing to the top level everywhere by year end
would mean either missing it or redefining it."

**Follow-up note.** Propose tracking: share of tier 1 artifacts with signed build provenance (Build
L2) and an SBOM per build; share of tier 1 repositories with enforced branch protection (Source L3);
open critical vulnerabilities past service level and the exception count; and secrets and
certificates with owner and expiry alerting. Explain that tier 1 targets are set first because that
is where exposure and revenue sit, and that lower tiers follow the standard pipeline. Criteria: the
answer corrects the framework without condescension, commits to trends with dates, and links the
measures to customer and revenue exposure. The weak answer accepts the commitment, or refuses without
an alternative.

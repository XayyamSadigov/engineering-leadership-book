# Chapter 48 solutions — Capacity Strategy, Workforce Planning, and Enterprise Governance

Worked solutions for the [chapter 48 exercises](../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Vacancy and ramp-up

**Vacancy.** 8 departures × 15 weeks = 120 engineer-weeks; 120 ÷ 52 = 2.3 engineers missing on an
average day. At $185,000 fully loaded, 2.3 × $185,000 = about $427,000 of approved budget unspent.

**Ramp-up (one defensible assumption).** Each new hire works at half capacity for their first 12
weeks: 8 × 12 × 0.5 = 48 engineer-weeks, about 0.9 FTE. Teaching costs a colleague three hours a
week for those 12 weeks: 8 × 12 × 3 = 288 hours, about 7 forty-hour weeks, roughly 0.1 FTE. Effective
missing capacity is then about 2.3 + 0.9 + 0.1 = 3.3 FTE, a little over 4 percent of 80 engineers.
Answers with different ramp-up assumptions are fine if the assumption is stated and the arithmetic is
shown.

**Which input to measure better.** The strongest answer picks time to fill. The 15-week median rests
on few events, and Tamsin Achterberg's hire shows its parts: 3 weeks waiting for approval, 6 sourcing
and screening, 1 offer, 5 notice. The approval wait is entirely internal and is the cheapest weeks to
remove; Rajiv Menon will ask why approval takes three weeks for a seat already in the budget. A good
answer also notes that the attrition rate is from 8 events in one year, so the plan should show a
range (for example 6 to 10 departures). The weak answer reports 2.3 FTE as a fact and treats the
departures as evenly spread, ignoring that one ledger departure costs more than the average.

## F2 — Projecting the mix drift

**Year 2, like-for-like.** Start 175, 253, 65, 7. Departures at 12 percent: Engineer 21 (21.0), Senior
30 (30.4), Staff 8 (7.8), Principal 1 (0.8); 60 in total. Promotions: 8 percent of 175 = 14 Engineers
to Senior, 3 percent of 253 = 8 Seniors to Staff. End: Engineer 175 − 21 − 14 + 21 = 161; Senior
253 − 30 − 8 + 14 + 30 = 259; Staff 65 − 8 + 8 + 8 = 73; Principal 7. Total 500. Senior and above:
339, 68 percent.

**Year 2, hold the mix.** Unchanged at 190, 245, 58, 7 (62 percent), with the same hiring rule.

**Cost gap after two years.** Like-for-like has 29 fewer Engineers, 14 more Seniors, 15 more Staff:
−29 × $170,000 + 14 × $215,000 + 15 × $270,000 = $2,130,000 a year, roughly double the first year.

**When it becomes a problem.** Not at a percentage but when either of two things happens: the number
of Staff engineers exceeds the scopes that need Staff work with a written mandate (Chapter 29), so
titles outrun work; or the entry-level pipeline is too thin to produce future Seniors. Staff growing
from 58 to 73 in two years should trigger that check.

**Where rising seniority may be right.** The platform organization, which runs shared infrastructure
for 430 other engineers, may need more senior depth. Evidence to ask for: incidents and their
complexity, the knowledge map for tier 1 platform components, and whether its work is mainly design
and operation rather than feature volume. By contrast, a feature-heavy product group such as
Commerce (130 engineers) is where entry-level hiring with named mentors is most likely to pay off.

**Criteria.** Both policies projected with the arithmetic shown, the drift costed, a trigger tied to
work rather than a ratio, and a named group with evidence. The weak answer picks a single
organization-wide target ratio without saying why.

## F3 — Applying the externality test

| Rule | Passes? | Owner, enforcement point, and measure |
|---|---|---|
| Common branching strategy | No | Directors or teams; branching affects one team's flow, and harms others only through outcomes covered by other policies |
| Tier 1 alerting and on-call | Yes | Principal owner for operations; quarterly sample of alerts and rotations, and the paging tool; share of tier 1 components meeting both |
| One approved front-end framework | No, as a mandate | The platform or design-system team makes the supported framework the easiest road; adoption should be earned |
| Vulnerability remediation service levels | Yes | Security owner; scanner in the shared pipeline; findings past deadline by severity |
| No customer date without an estimate | Yes | VP of product and engineering jointly; planning tool records the estimate and owner; dates given before sizing |
| Weekly retrospectives | No | Teams and their managers |

A strong answer explains the front-end case carefully. It can be argued that a shared framework
affects other groups (shared components, hiring, security patching), which is a real externality. The
better answer still separates the outcome that matters (supported, patched dependencies; accessible,
consistent customer interfaces) from the tool. If the tool is truly the control, for example because
only one framework can be security-patched centrally, a mandate can be defended, but the reason has
to be stated. The weak answer keeps everything because each rule "sounds sensible", which is how
policy inflation starts.

## A1 — Two Data and Analytics backfills

**First, what to know.** What the two leavers owned and who else can change it safely (the knowledge
map); whether either owned the month-end reporting path, which the baseline says was built by one
person; the team's current level mix (at baseline 6 Engineers and 5 Seniors, plus the Bogotá data
engineer promoted in quarter 3, so plausibly 5 and 6 before these departures); and where the team's
work sits. Data and Analytics is split 4, 5, and 2 across Minneapolis, Bogotá, and remote, so
Chapter 14's warning about fragmented ownership applies.

**One worked decision.** Seat 1: if a leaver held knowledge that fewer than three people have,
backfill at Senior where the work sits and name a successor now. Seat 2: hire at Engineer level, in
Bogotá if the work it covers is owned by the Bogotá cluster and a Senior there can mentor, otherwise
in Minneapolis. Both decisions are recorded with their reason.

**Yusuf Demir.** A vacancy is not a promotion criterion. His evidence plan (lead the ledger-export
contract design through Billing review) continues; filling a Senior seat with him now would undercut
the calibrated process Chapter 8 built. Farah can, however, give him the design work the leavers did,
which is good evidence for the next cycle.

**Criteria.** The answer asks about knowledge before level, does not choose location on cost alone,
and keeps promotion separate from backfill. The weak answers are to approve the request as stated, or
to move both seats to Bogotá because they are cheaper.

## A2 — Contractors for CI consolidation

**The three tests.** Bounded: partly. Moving four services onto a pipeline has an end, but only once
the target is chosen, and GitLab CI as the target is still an open decision. A contractor cannot make
that decision. Verifiable: yes, if acceptance is defined (each service deploys and rolls back through
the new pipeline, with a rehearsed rollback). Not core knowledge: this is the weak test. The deploy
path for auth-svc, webhooks, document-store, and export-svc is operational knowledge that Northstar
must keep; today one Platform Operations engineer understands the script. A contractor who learns it
and leaves recreates the single point of knowledge.

**Size check.** Four contractors for nine months is about 156 engineer-weeks. The platform roadmap
planned about 29 engineer-weeks of capacity for three items, of which phase 1 is one. A good answer
asks why the proposal is five times larger than the roadmap estimate.

**Decision and conditions (one defensible answer).** Support a smaller contract only after the CI
target is decided, with: a Platform Operations engineer paired on every service; runbooks and a
rehearsed rollback as acceptance criteria; Platform Operations owning every pipeline from day one;
contractor spend reported in full-time equivalents beside headcount; and funding confirmed against
the actual vacancy underspend, which shrinks if option C is chosen. The weak answer approves because
the money is "already in the budget", or refuses vendors on principle.

## A3 — The customer-date rule

**What the rule protects.** Northstar's committed roadmap delivery was 41 percent in the baseline
quarter, and 5 of 17 dates were given before sizing, including Greg Tanaka's two deal features. A date
given without an estimate is a promise engineering did not make and often cannot keep; at Northstar
missed promises reach renewals.

**Engineering's side of the bargain.** An estimate within five working days, given as a range with a
confidence level (Chapter 17), and a named owner. If engineering misses the five days, Greg may give
a date and engineering owns the consequence: the rule binds both sides.

**Exception path.** For a deal that cannot wait five days, Amara Okafor and the director can jointly
approve a date the same day, recorded with its risk and the work it displaces. Exceptions are reviewed
monthly; if they become routine, the service level is too slow.

**The conversation.** Start from Greg's interest (closing deals with credible dates), not the rule.
Show what happened to the dates given before sizing last year, and ask which of his two deals would
be hurt by a five-day wait. Criteria for a good answer: it treats the rule as a delivery policy with a
service level, not a veto, and it offers a fast path. The weak answers are to exempt sales entirely,
which leaves the rule empty, or to enforce it without any service level, which makes engineering the
bottleneck Greg says it is.

## X1 — Northstar's year-2 workforce plan recommendation

Several recommendations are defensible. One worked answer:

**Recommendation.** Combine three parts. (1) Option B's level rule, with an explicit exception: ledger
knowledge areas (period close, currency and rounding) are backfilled at Senior and get a named
successor, whatever the band says. (2) Option C, limited to one requisition held ahead for a ledger
role. It needs an explicit, dated exception to the 87-seat rule (a peak of 88 seats, 81 engineers),
which the plan asks Victor Lindqvist and Rajiv Menon to grant, proposing that the exception be
measured as average engineering headcount at or below 80 over the year and that it expire at the end
of year 2. (3) Option B's location rule only for teams
with a Bogotá cluster and a Senior there to mentor. Defer option D until a quote exists and Core test
coverage for the affected paths is assessed. If a VP is added in year 2 (Victor's open week-45
question), that seat also counts against the 87, so the plan should show the effect on engineers.

**Both branches of the year-2 proposal.** If the Mobile team is approved, the plan starts at 79,
Mateo Arango Ríos becomes Bogotá's first manager, and the location rule can apply to mobile seats. If
not, the plan starts at 80 and Bogotá seats stay in Payments and Data clusters only. The arithmetic
is shown for both.

**What each executive accepts.** Rajiv grants a dated exception to the 87-seat rule (a brief peak of 88 seats) in exchange for about 1 FTE of
recovered capacity and a lower risk of losing ledger knowledge; Victor Lindqvist accepts that ledger
backfills cost more and that location savings are smaller and slower than the rate card suggests.

**Measures at the end of quarter 5.** Vacancy weeks and time to fill (with the approval wait reported
separately), level mix by team, the ledger knowledge map counts, average headcount, contractor FTE,
and how many requisitions recorded the reason for their level and location.

**Criteria.** The plan works under both branches, states its assumptions, protects the known tail
risk, and asks each executive for something explicit. The weak answer picks the cheapest option (B)
without addressing the ledger, or the safest (C) without addressing the board pack.

## X2 — A layer between the CTO and the VPs

**Use the layer diagram.** The coordination need named is the CTO's load: five groups and a policy
set. Decision rights: which decisions reach the CTO that belong with a VP? A CTO with five VP reports
has a narrow span by Chapter 34's standards, so the span is not the problem; the content of the
CTO's week is. Tool or policy: the six policies each have a principal owner and measures from system
data; if the CTO is personally interpreting policies, the owners lack authority. Shared forum: a
monthly business review in which every VP reports the same scorecard replaces many one-off
conversations.

**Decision (one defensible answer).** Refuse the layer for now. Instead: delegate policy
interpretation and exceptions to the principal owners, with the CTO hearing only exceptions above two
quarters; set a common VP review format; give the CTO a chief of staff or technical program role for
cross-group follow-through if the load is administrative. Record the trigger for revisiting: more than
eight direct reports, or decisions waiting on the CTO beyond an agreed time for two quarters running.

**What the layer would cost.** A fourth level between an engineer and the CTO, a hop on every
cross-group decision, and a senior salary. Williamson's control-loss idea (expert opinion) and
GitLab's practice of keeping one span range to avoid an extra layer both argue for trying the cheaper
mechanisms first.

**Criteria.** The answer diagnoses the actual load before choosing structure, and leaves a measurable
trigger. The weak answers accept the layer because a VP proposed it, or reject it without removing the
load that prompted it.

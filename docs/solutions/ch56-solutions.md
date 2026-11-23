# Chapter 56 solutions — Recovering a Failing Engineering Organization

Worked solutions for the [chapter 56 exercises](../parts/13-advanced-problems/56-recovering-a-failing-engineering-organization.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Sorting Northstar's findings by triage

| Finding | Placement | Reason |
|---|---|---|
| 11 open criticals, 3 known-exploited | Act this week | Exploitable exposure is irreversible harm: once exploited, nothing undoes it. Act means triage and mitigation (restrict, patch, or record an exception with an owner and a date), not a full program |
| Three ledger engineers carrying 54 of 64 after-hours pages (counts reconstructed later from the paging tool; at arrival the team table says three people carry most pages) | Act this week | Key-person risk with knowledge nobody else holds (currency and rounding known by one person; period close changed safely by one). One colleague has already resigned after three weekends of pages |
| Missing severity definitions | Early win | A few days of work with Kwame Mensah and Sofia Alvarez; makes every later incident count comparable and answers customer success's integrity doubt |
| 52-rule standards page | Defer | Nobody follows it; changing it now changes nothing customers see. A "not yet" item with a quarter 1 date |
| Four CI systems | Plan this quarter only where they touch the constraint | The Core pipeline (Jenkins) is on the release-train constraint; consolidating all four is a multi-quarter effort and goes on the "not yet" list |
| 143-item debt list | Defer | No owners, no costs. It becomes useful only after the constraint is known and items are priced (Chapter 21) |

**Where reasonable leaders disagree.** The four CI systems. One leader puts the shell-script services
(auth, webhooks, document store deployed by a script one person understands) in "act this week",
because that is also key-person risk on tier 1 components. That is defensible if the action is small:
document the script and pair a second person, not consolidate.

**A good answer** applies the irreversible-harm test literally and keeps the "act this week" list
short. **The weak answer** puts six items in "act this week", which is the hero arrival in a table, or
puts the ledger engineers under "plan this quarter" because their problem is people rather than code.

## F2 — What 23 to 15 can support

**What the count supports.** Over two quarters there were 38 incidents. If the underlying rate had not
changed, an even split would be 19 and 19, with a standard deviation of about 3.1 (the square root of 38
× 0.5 × 0.5). Fifteen is about 1.3 standard deviations below 19; a drop at least this large would occur
about one time in eight by chance, and a split at least this uneven in either direction about one time
in four (exact binomial: 0.13 one-sided, 0.26 two-sided). The direction is encouraging, and
the count alone cannot show a turnaround. One quarter after three rising quarters (9, 16, 23) is also
too short to call the trend reversed.

**What to put beside it.** Mechanism measures with more events or less noise: Sev1 reviews completed
within ten working days (a process Ngozi controls), the share of Sev1 bridges run by someone other than
Rhys Gallagher, customer-detected share (11 of 23 to 6 of 15, 48 to 40 percent, also a small count),
open escalations (3 to 1), departures in the quarter (2, about 9 percent annualized against 18.9), and
availability on the pay-run path against 99.9 percent, which the chapter does not report for the
quarter and which the CTO must not imply.

**The two sentences.** "The Payroll group has stopped getting worse: incidents fell from 23 to 15 and two of
three escalated customers have closed their escalations, though one quarter of counts this small could
still be chance. What has changed for certain is how incidents are handled, every Sev1 now reviewed on
time and command spread across eight people, and we will call it a turnaround when two more quarters
confirm it."

**The weak answer** reports "incidents down 35 percent" (8 ÷ 23 = 34.8 percent) as a turnaround.

## F3 — Marcus Oyelaran at day 30

**Reading at day 30: keep and fix the system.** Billing's numbers are the worst in the organization (8 of
30 Sev1 and Sev2 incidents, 58 escaped defects, 41 percent unplanned work, 0 of 3 committed items
delivered), but the evidence points mostly at the system. Five of Billing's 8 incidents came through the
Core release train and 2 through database migrations, which were tested only against an empty schema;
all eight Core modules share one schema; core/scheduler was unowned and co-changed with invoicing in 60
percent of the smaller module's requests. The chapter's test asks whether peers with the same system do
better. Orders, also on the train, had a 29 percent change failure rate and 7 incidents, so Billing is
worse but not in a different category.

**Why 34 percent is weak evidence about him.** Billing ships most changes through the fortnightly Core
train, so its change failure rate describes the train and the shared schema more than the team, and the
rate is computed on a handful of releases with manual linking that misses failures. It is a property of
a system Marcus does not control.

**What would move him to "coach" by day 90.** Evidence about his own work once the system fixes land:
whether he sets technical direction instead of leaving it to incidents (baseline: "nobody; decided
during incidents"), whether he spreads the ledger on-call load, whether his sprint scope stops changing
mid-sprint (changed in all of the last 6) once interrupts fall. A skill gap in technical direction with
willingness to work on it means coach, with a dated checkpoint.

**What would move him to "replace".** An integrity finding (for example, under-reporting severity after
the week 3 definitions), harm to people, or no change in his own behavior after the system fixes and a
fair coaching period. None of these is in the baseline evidence.

**A good answer** separates system from person with comparisons. **The weak answer** replaces the
manager with the worst numbers in the first month.

## A1 — The ledger engineers' load in weeks 2 to 4

**Actions.**

1. **Week 2, Marcus Oyelaran with the three engineers:** take them off first response for low-value
   pages. The paging tool's history, pulled this week (Chapter 3 records that on-call load was not
   tracked and had to be reconstructed), shows that of Billing's 180 pages, 61 needed no action; silencing or rerouting those is a few
   engineer-days of alert tuning, owned by Billing with the help of Kwame Mensah (staff engineer, reliability).
2. **Week 2, the director:** a 30-minute conversation with each of the three, separately, to ask what
   would make them stay and what they would stop doing. This is the stay interview that Northstar held
   in weeks 14 and 15, moved to week 2.
3. **Weeks 2 to 4, Marcus:** pair Tamsin Achterberg (the ledger backfill) and one other Billing engineer with the ledger
   engineers on currency and rounding first (one person can respond alone and one can change it
   safely) and then on period close (one person can change it safely): the ledger's single points of
   failure. Credit notes, where Tamsin can already respond, is where her after-hours shadowing starts.
   Cost: about 1 engineer-week a week across the four people, from Billing's
   prevention share.
4. **Week 3:** a secondary on-call position for ledger pages held by a non-ledger engineer who
   escalates only if needed, so the three are not first responders after hours.
5. **Week 4:** put ledger knowledge coverage into the capacity model as part of Billing's 25 percent
   prevention share, with a measure (people who can respond alone per ledger area).

**Cost.** Roughly 2 to 3 engineer-weeks across weeks 2 to 4 plus the alert tuning, inside the
prevention allocation; no headcount, no change to the renewal teams.

**Telling them.** To Marcus first, privately: the load is a system failure, not his, and the plan is
his to run. To the three engineers: what you heard, what changes this week, and what you cannot promise
(pay changes go through the normal process).

**A good answer** acts on the load in week 2 and is honest about what it cannot fix. **The weak answer**
raises the on-call stipend again, which the baseline shows was already tried.

## A2 — Beatriz Quintero's green status

**Diagnosis.** Start from the system and skill explanations before integrity. The research on silence and
bad news (Smith and Keil; Milliken and colleagues) predicts exactly this behavior in a group under
threat: three customers in escalation, a vice president gone, and a reporting format with no place for
uncertainty. If Beatriz was asked directly and misstated what she knew, it is an integrity problem.
If she reported "green" because the format asked for a color, the team believed the date, or red had
been punished before, it is a system problem with a skill component (reading early signs of slip).

**The opening.** "I want to understand the integration slip, not assign blame for it. Walk me through
what you knew in each of the three months and what the status report let you say. I need to hear about
slips earlier than I did here, and I want to know what would make that safe and easy for you."

**The system change.** Replace colors with a forecast date and its range, updated weekly, plus the top
risk to the date. A widening range is visible before a slip. Ngozi reacts to the first red report by
helping, in front of the other managers.

**What would make it integrity.** Evidence that she knew of the slip and reported otherwise when asked,
or altered numbers. Then it moves to Chapter 9's process, regardless of her other results.

**A good answer** tests the system and skill explanations first, names what would make it an integrity
issue, and changes the reporting. **The weak answer** treats a misleading status as either a minor
style issue or as dishonesty without asking what she knew.

## A3 — The stakeholder trust track at Northstar

| Stakeholder | Doubts most | Evidence that moves them | One behavioral promise |
|---|---|---|---|
| Helena Marsh (CEO) | Ability | Renewal customers stop raising reliability; outage calls fall | "You will get a short written note on reliability for the two renewal accounts every two weeks" |
| Rajiv Menon (CFO) | Ability | Service credits falling, explained by cause | "Every credit-bearing incident gets a written cause and action within ten working days" |
| Amara Okafor (CPO) | Benevolence | Her committed items protected in the capacity model | "No change to your committed items without telling you first, with the trade-off in writing" |
| Greg Tanaka (VP Sales) | Benevolence | His two deal features sized and placed in the plan, even if not where he wants | "Every deal request gets an estimate within an agreed number of working days" |
| Sofia Alvarez (VP Customer Success) | Integrity | Customers hear about incidents from Northstar first | "You will hear about a customer-visible Sev1 or Sev2 from engineering before a customer tells you" |

**Conflict check.** Greg's promise (estimates within a fixed time) and Amara's (no change to committed
items without notice) can collide when a deal request displaces a roadmap item. Resolve it by
promising Greg an estimate, never a date, and routing any displacement through Amara with the trade-off
written. Rajiv's and Sofia's promises reinforce each other.

**A good answer** gives each executive a different kind of evidence and checks the promises against
each other. **The weak answer** promises everyone outcomes ("fewer incidents, faster delivery"), which
the quality track cannot deliver on the trust clock.

## X1 — Moving Rhys Gallagher (hypothetical)

**Decision.** Support the move, with conditions. The evidence at day 120 is behavioral and specific:
the commander rotation exists, so the system fix landed, and he still overrides managers on
pay calculation engine changes. That rules out "the system explains it". Two managers threatening to leave
is a cost the group, which already lost 17 people in a year, two of them managers, cannot absorb.

**Evidence to require.** The written expectation Ngozi gave him at day 30 and its checkpoint; at least
three dated examples of overrides after the checkpoint, from more than one manager; his own account of
them; and whether he was offered help (a coach, a peer director) to change. Without a written
expectation, the move is premature: give him one, with a 30-day checkpoint, first.

**Cost.** The pay calculation engine's builder may leave rather than accept the move; the principal role
must be real (a technical mandate over the engine and its standards, as Halvard's principals have), not
a demotion in disguise. A new director must be found; an interim from inside the group has the same
knowledge gap the departures created. Mockus's finding on organizational change and defects argues for
doing it once, quickly, and with the commander rotation stable.

**Announcement.** Rhys announces it with Ngozi, framed by what he will own; no criticism in public.

**A good answer** requires a prior written expectation. **The weak answer** moves him on the managers'
threat alone, or keeps him because he is irreplaceable.

## X2 — Victor Lindqvist's answer to David Ferrante

"Yes, by one definition: at arrival engineering was breaking its reliability commitments. Availability
was 99.62 percent against 99.9 in the contracts, credits were $410,000 a quarter, and two renewals worth
$9M named reliability. Delivery was poor but stable: dates were broken, but the trend
was flat.

Recovered: Sev1 and Sev2 incidents ran 30, 21, 17, 14 over four quarters, credits fell to $60,000, and
customers now detect 29 percent of incidents rather than 47 (quarter 1 and 2 readings). The accounting
integration has run for the renewal customer since week 19, and bulk ordering reached final acceptance
in week 26.

Not recovered: availability was 99.89 percent in quarter 3, still under 99.9, about 144 minutes down
against about 131 allowed. Core's release failure rate did not improve between quarters 1 and 2 (22 and 23
percent, small counts). Four critical roles have no cover, which is Anders Holm's question about
dependence on a few people.

What I would not yet claim: that quarter 4 will hold, or that the improvement is permanent. Quarter 4
data arrives after the board meeting." (About 170 words.)

**A good answer** separates reliability from delivery, uses only week 47 facts, and names the
availability miss before the director finds it. **The weak answer** claims the mandate is met ("incidents
halved") without the availability miss, or uses quarter 4 results that do not exist yet.

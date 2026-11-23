# Career development plan

**Used in:** [Chapter 8](../parts/02-people-management/08-career-development-promotion-and-compensation.md)
(career development, promotion, and compensation),
[Chapter 5](../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md) (growth and
sponsorship in one-on-ones), [Chapter 10](../parts/02-people-management/10-motivation-retention-and-senior-engineers.md)
(retention, where a missing career conversation shows up in exit data),
[Chapter 4](../parts/01-foundations/04-the-leadership-ladder.md) (choosing between the management and
individual-contributor tracks), [Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)
(development goals for managers and the leadership bench).
**Owner:** the engineer owns the goal and the evidence; the manager owns the commitments to create the
opportunities the evidence needs.
**Cadence:** written after every promotion decision ("promoted" or "not yet") and at least twice a year
otherwise; progress checked monthly in the one-on-one; a mid-point check halfway to the review date.

A career development plan turns a [career ladder](../glossary.md#career-ladder) into a next step for
one person. It names the target, the
ladder dimension where the gap is, the evidence that would close it, the situation in which that
evidence can be produced, and who creates that situation. The last field is the one most plans omit.
If the gap is cross-team influence and the person's role offers no cross-team work, the gap is partly
the manager's, and the plan says so.

It is also the written form of a usable ["not yet"](../glossary.md#not-yet), the promotion decision
that says what is missing and how to close it. Sponsorship, a senior person using their influence on
someone's behalf, is different from advice; a person can be well mentored and still not sponsored.

A development plan is not a performance plan. If the question is whether someone meets their current
level, use Chapter 9's process, not this one
([Chapter 9](../parts/02-people-management/09-performance-management-and-underperformance.md)).

## How to fill it in

1. **Write the target in the engineer's words,** with a horizon: the next level on the same track, a
   change of track (Chapter 4), a broader role at the same level, or depth in the current one. Not
   everyone wants promotion; a plan for mastery is a plan.
2. **Place current evidence against each ladder dimension** at the target level. Use dated artifacts,
   not adjectives. Mark each dimension "at target", "gap", or "no evidence yet".
3. **Pick at most two gaps.** A plan with five gaps is a list of everything, and none moves.
4. **For each gap, write the evidence that would close it:** observable, achievable within the role or
   one move away, and checkable by a reader from another team. "Lead the next ingestion design through
   review by another team" can be done; "show more leadership" cannot.
5. **Name the opportunity and who creates it.** Usually the manager; often a staff engineer or a peer
   manager. If no such opportunity exists on the team, say so and name the move that would provide one.
6. **Choose the mode of help** for each gap: directing, coaching, mentoring, or sponsoring (Chapter 5),
   and name the helper. Gaps in scope and influence usually need sponsorship, not advice.
7. **Record the dependencies:** decisions or projects the evidence relies on that nobody in the plan
   controls, and a fallback for each.
8. **Set the mid-point check and the review date,** normally the next calibrated cycle.
9. **State what the plan does not promise:** no level or pay change is implied by completing it; the
   decision stays with calibration. Pay position in the band is handled separately, on Chapter 8's
   three grounds.
10. **At each check, add a line to the review log:** what happened, what changed, and what the manager
    did or did not do.

## Template

| Field | Meaning |
|---|---|
| Person, level, track, team | Current facts |
| Target and horizon | In the engineer's words; next level, track change, broader role, or depth |
| Trigger | Why this plan now: a "not yet", a career conversation, a role change |
| Dimension placement | For each ladder dimension: at target / gap / no evidence yet, with the dated evidence |
| Gaps chosen (at most two) | Dimension, what the target level requires, what was seen |
| Evidence that would close each gap | Observable, achievable, checkable by another team |
| Opportunity and who creates it | The situation that lets the evidence happen; the person who makes it happen and by when |
| Mode of help and helper | Directing / coaching / mentoring / sponsoring; named person |
| Dependencies and fallback | What the evidence relies on that the plan does not control; the alternative |
| Manager's commitments | What the manager will do, with dates |
| Mid-point check, review date | Dates; the review is normally the next calibrated cycle |
| Not promised | Plain statement that completion does not decide the level |
| Review log | Dated lines at each check |

```yaml
plan:
  person: ""
  level: ""
  track: ""              # individual contributor / management
  team: ""
  manager: ""
  written: ""
  trigger: ""            # not yet / career conversation / role change
  target: {in_their_words: "", horizon: ""}
dimensions:              # use your ladder's dimensions
  - {name: scope, placement: "", evidence: []}            # at_target / gap / no_evidence_yet
  - {name: technical_judgment, placement: "", evidence: []}
  - {name: delivery_and_ownership, placement: "", evidence: []}
  - {name: operational_responsibility, placement: "", evidence: []}
  - {name: influence_and_growth_of_others, placement: "", evidence: []}
gaps:                    # at most two
  - dimension: ""
    required_at_target: ""
    seen: ""
    closing_evidence: ""
    opportunity: {what: "", created_by: "", by_date: ""}
    help: {mode: "", helper: ""}   # directing / coaching / mentoring / sponsoring
    dependencies:
      - {depends_on: "", fallback: ""}
manager_commitments:
  - {item: "", by_date: ""}
midpoint_check: ""
review_date: ""
not_promised: "Completing this plan does not decide the level; calibration does."
review_log:
  - {date: "", what_happened: "", changes: "", manager_did: ""}
```

## Example: Northstar, Yusuf Demir after a "not yet" (quarter 3)

!!! info "Northstar so far"
    Week 27 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Sev1 and Sev2 incidents fell from 30 a quarter to 17 in quarter 2, and the first calibrated promotion
    cycle has just run on a ladder rewritten in quarter 2. See the [timeline](../case-studies/northstar/timeline.md)
    and the [cast](../case-studies/northstar/cast.md).

The layout, the dependency and fallback analysis, and the wording of the fields are illustrative. The
check results are not recorded.

**Context.** At the start of quarter 3, in Northstar's first calibrated cycle, managers nominated nine
engineers for Senior; five were promoted and four received "not yet". Yusuf Demir, a data engineer in
Data and Analytics in Minneapolis with three years at Northstar, was one of the four. The ladder is the
quarter 2 rewrite: five dimensions at three levels (Engineer, Senior Engineer, Staff Engineer). Farah
Haddad, his manager, gave the decision with all five parts.

| Field | Entry |
|---|---|
| Person, level, track, team | Yusuf Demir; Engineer; individual contributor; Data and Analytics (Farah Haddad) |
| Target and horizon | Senior Engineer at the next calibrated cycle |
| Trigger | "Not yet" for Senior, start of quarter 3 |
| Dimension placement | Influence and growth of others: gap. The other four dimensions were not named as gaps in calibration; their evidence is in his packet, not reproduced here |
| Gap chosen | Influence beyond the team, which Senior requires; seen: excellent pipelines that only his own team uses |
| Evidence that would close it | Lead the design of the ledger-export contract Li Na Zhou proposed, through review by Billing, and bring one Billing engineer up to speed on it |
| Opportunity and who creates it | Farah Haddad assigns him the design |
| Mode of help and helper | Sponsorship: Farah asks Li Na Zhou, staff engineer for data and integration, to sponsor the design |
| Dependencies and fallback | The contract is one of three options in ADR-0001, the open architecture decision on how integrations read ledger data (read the tables, a versioned export contract, ledger posting events), open since week 14 with nobody's decision rights mapped. The design and its Billing review are evidence of cross-team influence whichever option is chosen, but if the decision goes elsewhere the plan needs a second cross-team design to lead. Fallback: name it at the mid-point check |
| Manager's commitments | Assign the design; ask Li Na Zhou to sponsor it |
| Mid-point check, review date | Check at three months (about week 40); review at the next calibrated cycle |
| Not promised | Completing the design does not decide the level; calibration does |
| Review log | Not recorded |

What to notice: the gap is tied to one ladder dimension, the evidence is something a Billing engineer
could confirm, and the commitment belongs to the manager, not the engineer. Yusuf said it was the first
time anyone had told him what Senior meant, which is the plan's first effect. The dependency row matters
most: the evidence sits inside an architecture decision nobody has made, so naming a fallback in advance
protects his next cycle from someone else's open decision.

## Common mistakes

- **Gaps in adjectives.** "Show more ownership" gives the person nothing to do; name the artifact a
  reader from another team would check.
- **No opportunity in the plan.** The engineer is told to show cross-team impact on a team that has
  none. The manager's commitment is the field that makes the plan fair.
- **Five gaps.** Choose at most two; the rest wait for the next plan.
- **Mentoring where sponsorship is needed.** Advice does not create a design review in front of another
  team; a sponsor does.
- **An implied promise.** "Do this and you'll be promoted" takes the decision away from calibration and
  turns the next "not yet" into a broken promise.
- **Mixing development with underperformance.** A plan for someone below their current level belongs in
  Chapter 9's process, with its own terms.
- **No review log.** A plan nobody checks becomes a document; the mid-point check is where a missing
  opportunity gets caught in time.

## Review questions

1. Could a reader from another team confirm each piece of closing evidence without asking you?
2. Which opportunity in the plan does not yet exist, and who will create it by when?
3. What does the evidence depend on that nobody in the plan controls?
4. Does the engineer describe the target in the same words as the plan?
5. If this person resigned next month, would the exit interview say they had a career conversation in
   the last six months?

## Evidence and references

The ladder, calibration, the five parts of a usable "not yet", and pay are
[Chapter 8's](../parts/02-people-management/08-career-development-promotion-and-compensation.md)
subject; this template is the written form of those five parts, extended to people who were not
nominated.

- [Scott, 2017](../references/bibliography.md#scott2017radical): *Radical Candor*, known for pairing
  care for the person with a direct statement of the gap (**expert opinion**).
- [Ibarra, Carter, and Silva, 2010](../references/bibliography.md#ibarra2010promotions): survey research
  on high-potential graduates found that a person can be well mentored and still not sponsored
  (**industry research** about MBA graduates, not engineers).

The fields are **this book's recommendation**.

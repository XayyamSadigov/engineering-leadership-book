# Chapter 28 solutions — Architecture Decision-Making and Governance

Worked solutions for the [chapter 28 exercises](../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Routing six decisions

| Decision | Class | Decider | Record |
|---|---|---|---|
| Rename an email template variable in notification-svc | Looks internal; is cross-team if the variable is part of what other teams' templates or code use | Owning team, after checking consumers | Commit message, or an ADR if it is a contract |
| Change the webhook signature format | Cross-team, and customer-facing | Providing team's technical lead with a mandate, consumers consulted (including customers via a versioning policy) | ADR plus a versioning rule |
| Add an index to a ledger table | Inside Billing, but hard to reverse operationally and affects replicas others read | Billing's technical lead | Short ADR or migration note; a rehearsal under the week 10 rule |
| JSON library inside erp-sync | Inside one team, reversible | The engineer | Commit message |
| Consolidate four build systems | Organization-wide | Forum with a named signer; cost to the director or CTO | Full ADR and design doc |
| Add a field to the posted-invoice export | Cross-team interface | Domain decider or providing lead; additive change may be pre-approved by the contract's rules | Contract change log; ADR only if it breaks compatibility |

The point of the exercise is that two "trivial" items are not trivial: INC-412 (a renamed email
template variable sent blank confirmations) shows that a variable can be an undeclared contract. A
good answer names the fact that would move each case (is anyone outside the team reading this? can it
be undone without another team?). The weak answer classifies by technical size rather than by reach.

## F2 — Writing ADR-0001

A strong record fits on two pages and contains: title ("How integrations read posted ledger data");
status Proposed; decider (left blank or named per the reader's A1 answer, never "the team"); context
(renewal date in week 19, 12 tables read directly by older erp-sync connectors and warehouse
pipelines, INC-424's stale replicas, the six reserved Billing engineer-weeks); the three options with
effort and risk; the recommendation; consequences; assumptions; review trigger; fitness function.

The consequences section for option B must be honest on both sides. Billing takes on a new public
interface: it must version it, keep it backward compatible, run consumers' contract tests, and answer
for breakages, without a technical lead today. The warehouse pipelines lose direct access over time
and must migrate, which costs Data and Analytics capacity in quarter 3. Positive consequences: ledger
migrations no longer silently break consumers for the new connector, and the dependency links between
the two teams shrink.

Assumptions worth writing: posting volume stays within what a daily export handles; no third consumer
appears this quarter; Billing can staff the interface. The weak answer lists only benefits, or omits
the review trigger.

## F3 — Interrogating a board's report

The report is consistent with both a healthy board and a rubber stamp, so the reader needs data that
separates them.

1. **Share of submissions already in build.** High means late review; approvals are then forced.
2. **Conditions verified.** Of the 30 conditional approvals, how many conditions were checked later?
   If none, the conditions are decoration.
3. **Distribution of wait, not only the median.** A 19-day median with a long tail tells teams to
   route around the board.
4. **Bypass rate.** Sample merged cross-team interface changes and count how many never came to the
   board.
5. **What changed in the approved designs.** Did review alter anything, or only approve?
6. **Rejected proposals.** Two rejections in 43 may be fine if submissions are pre-filtered.

Convincing evidence of a working board: most submissions before building, conditions verified, low
bypass, a visible fraction of designs changed by review, and a falling agenda as questions become
standards. The weak answer judges the board by its approval rate alone, in either direction.

## A1 — Choosing the decider for ADR-0001

One defensible answer: the director names **Li Na Zhou (staff engineer, data and integration) as decider**, because the decision is a data
contract in Li Na Zhou's written standards domain (data, migration, configuration), and Li Na Zhou
has the technical information. To meet the chapter's conditions, the director adds three things. The
mandate for the domain is written down as the first decision-rights entry. Because the decider
authored the proposal, the record must show a five-day written comment window that Billing, Payments
and Integrations, and Data and Analytics actually used, and Ines Carvalho (staff engineer, Core domain) reads it as a second
technical reviewer. And the decider owns the review trigger and the fitness function, and so carries
the consequences.

Marcus Oyelaran (Billing manager) and Elena Sokolova (Payments and Integrations manager) hold **agreement rights on capacity and dates only**: Marcus on
whether option B fits the six reserved engineer-weeks, Elena on whether the week 19 date holds. A
design objection from either goes in the comment window, not through the agreement right.

The decision date should fall in week 15, so that Billing's reserved weeks 14 to 16 are not spent
waiting. Also defensible: the director as decider because the option choice is partly a date-risk
trade-off, provided the record says so. Weak answers: "the managers agree among themselves" (no
decider), or Li Na Zhou deciding alone with no comment window.

## A2 — Handling the CTO's hallway remark

The remark is an informal overrule before a decision exists, and two engineers are already acting on
it. The aim is to bring Victor Lindqvist's (the CTO's) view into the record, not to defeat it.

**With Victor, privately, the same day.** Acknowledge the concern (week 19 is a renewal date) and that
it is legitimate input. Explain the cost of option A (a third silent consumer of ledger tables, the
replica lag seen in INC-424) and that option B is estimated to fit the reserved capacity. Ask him to
put his view in the ADR's comment window, or, if he wants to decide it himself because it is a
date-risk trade-off, to do so through the record so the team sees a decision rather than a remark.
Agree that if the evidence shows B threatens week 19 by the decision date, A with a dated exit is a
legitimate outcome.

**With the team.** Say plainly that the decision is open, who decides, and by when; that the CTO's
concern about the date is in the record; and that work on option A pauses unless it is reusable (much
of the reconciliation logic is). Do not imply Victor was wrong.

Weak answers: overruling Victor in front of the team, which repeats the hallway pattern, or letting
the remark stand as the decision.

## A3 — The request to reopen direct reads

The request is a proposal to supersede part of an accepted decision, so it is handled as a new ADR,
not as an exception granted in chat. The decider is the domain decider for ledger data (Li Na Zhou in
the A1 answer), with Billing and Data and Analytics consulted in writing.

The analysis should separate two complaints. "The contract slows every ledger change" may be a
problem with how the contract is run (too many fields exposed, no additive-change rule, slow contract
test feedback), which can be fixed without abandoning it. "Just for month-end reporting" is a request
for a second interface that bypasses the first; if granted, it should be scoped (named tables,
read-only, expiry date), monitored by the fitness function as an approved exception, and owned.

Either way the record shows the evidence (how much slower are ledger changes, measured how?), the
options, the decision, and a review trigger. A good answer also checks whether the original ADR's
review trigger has fired. Weak answers: refusing because "the ADR says so", or quietly granting a
database grant, which the fitness function would then flag as a violation nobody owns.

## X1 — The CTO's proposed review board

Estimate the load first from the 61 cross-team work items and 86 dependency links in the exercise. If
even half of those items involved a design choice another team builds on, that is about 30 designs a
quarter, about 2.3 a week (30 ÷ 13), plus team-internal hard-to-reverse
decisions if "cross-team" is read loosely. A weekly board that can review four proposals has headroom
on paper, but the CTO as chair becomes a single point of scheduling, and his presence anchors every
discussion.

**Recommendation: modify.** Support the goal (no more unrecorded interface changes) and replace the
mechanism: domain deciders with written mandates for cross-team interfaces and a ten-working-day
service level; a small forum of the three staff engineers for organization-wide decisions, with the
CTO as signer only for cost and risk trade-offs; a code review trigger requiring ADRs for interface
changes; and a monthly session in which the CTO reads a sample of records. Offer a measure to judge it
after a quarter: the share of interface changes with a linked ADR, and cross-team decision time.

Weak answers: accepting the board as proposed (a queue chaired by the person least able to attend), or
opposing it without offering a mechanism that addresses INC-418.

## X2 — Was governance worth it?

Assemble evidence that is checkable and modest:

- **Decision time** for cross-team decisions before and after (the baseline has none recorded, so use
  a reconstructed sample from chat history, and say so).
- **Interface-related incidents**: incidents whose reviews name an unrecorded or violated
  architectural decision (INC-418 and INC-424 are the baseline examples).
- **Coverage**: share of cross-team interface changes with a linked record.
- **Fitness function catches**: violations caught before production.
- **Cost**: staff engineer hours spent deciding and reviewing, estimated from calendars.

Refuse to claim that governance caused any reliability improvement on its own; the quality program,
weekly releases, and contract tests changed at the same time. Refuse to cite the number of records as
a success measure. Say that no study shows ADRs improve outcomes, and the one study of their use found
many logs abandoned early.

If the evidence is weak, stop the parts with the least return first: drop ADRs for team-internal
decisions, keep them for cross-team interfaces, and keep the fitness functions, which cost little
once built. The weak answer either claims too much or defends the process by its volume.

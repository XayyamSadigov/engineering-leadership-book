# Northstar at the start of quarter 4

!!! warning "Fictional"
    Everything on this page is invented for the book. See the note on the
    [Northstar overview](index.md).

This briefing is for readers who start at Parts X–XIII. It says where Northstar stands at week 40 of
the director's first year, what the latest results are, and which decisions are open. None of these
decisions has a recorded outcome, and the chapters leave each one open. The details are in
[quarter 4 of the director's first year](first-quarter.md#quarter-4); the people are on the
[cast](cast.md) page; the [timeline](timeline.md) shows the weeks.

## Where things stand at week 40

You are the Engineering Director. 80 engineers (3 of them staff engineers) and 6 managers report
through you to Victor Lindqvist (CTO). Your mandate, given in week 1, runs to week 52: halve Sev1 and Sev2
incidents, meet 99.9 percent availability on the order and payment paths, keep headcount flat, and
keep the two renewal commitments.

- **The renewals are delivered.** The accounting integration has been live since week 19. Bulk
  ordering was complete in week 26 and forecast to ship by the end of that week.
- **The quality changes are in place.** Ownership, severity definitions,
  weekly Core releases, and a prevention allocation (8 FTE in quarter 3) are in place. The seven QA
  engineers work in product teams.
- **The organization's shape is the next question.** Customer Experience still runs web and mobile
  under one manager, and core/permissions has no owner: its exemption lapsed in week 39.

## Latest results: quarter 3

Quarter 4 results are not recorded, so quarter 3 is the latest quarter anyone can cite.

| Measure | Baseline | Quarter 3 |
|---|---|---|
| Sev1 and Sev2 incidents | 30 | 14 (2 Sev1); the first quarter at or below the mandate's 15 |
| Availability, contractual paths | 99.62% | 99.89%, still just below 99.9% |
| Service credits | $410,000 | $60,000 |
| Unplanned work | 34% | 25% |
| Tier 1 components meeting the four operational minimums | 3 of 15 | 13 of 15 |

## The open decisions

| Decision | What is proposed | Who decides | By when |
|---|---|---|---|
| Year-2 organization | Split Customer Experience into Web (Daniel Cho) and Mobile (Mateo Arango Ríos); core/permissions to Orders; search-svc to Data and Analytics; Platform Operations becomes Developer Platform. Alternatives B, C, D are in the draft | Victor Lindqvist | Decision week 46; announcement week 51; effective week 53 |
| VP of Engineering | Whether Northstar needs a VP in year 2 or the director grows into the role. A VP takes one of the 87 seats | Victor asked for a recommendation | Week 48 |
| Quality continuation | Stage 2 "Hold" (quarters 5–6, 6 FTE, $150,000 tooling) and stage 3 "Converge" (quarters 7–8, 5 FTE); no headcount request | Management, inside the board's budget envelope; executives took positions in weeks 46–47 | Requested by week 51 |
| Workforce plan | Four options: like-for-like, shaped backfills, two requisitions held ahead, a fixed-scope vendor contract; plus the rule "no customer date without an engineering estimate and a named owner" | Draft to Victor and Rajiv Menon (CFO) in week 49; recommendation left open | With the budget pack |
| Week 34 portfolio forum | Greg Tanaka's third deal feature (purchase approval rules) against the limit of three cross-team initiatives | The portfolio forum | Held week 34; outcome not recorded |
| CI target | GitLab CI was proposed as the consolidation target in quarter 2. Stage 3 tooling depends on a choice | Open; Victor's strategy draft says the week 78 gate | Week 78 (draft) |
| ADR-0001 | How integrations read posted ledger data: read the tables, a versioned export contract (Li Na Zhou's recommendation), or ledger posting events | Nobody's decision rights are mapped; Victor's strategy draft reverses his week 14 "read the tables" remark | Week 60 (proposed) |
| Board headline | Victor's "Sev1 and Sev2 below 10 per quarter" or the director's counter (at or below 40 over year 2, rolling, with the severity audit) | Open; the draft page carries both | Board pack sent end of week 49 |
| SOC 2 | Option A (audit in year 2), B (readiness in quarters 5–6, decision at week 78; recommended), or C (evidence library only). A prospect worth about $310,000 a year requires a report | Not named; the options are in the risk register drafted for Victor's review | Not set; option B decides at week 78 |
| AI position | An interim AI-assisted engineering policy; a staggered coding-assistant trial in quarter 5; non-AI fixes first for order checking; the order assistant deferred; no backfills held open on AI | Victor, for whom the position is written; all decisions open | Trial would start week 53 |
| Security reporting line | Marta Kowalczyk (Head of IT) objects to moving security out of IT; three reporting options recorded without a recommendation | Open; none chosen | Not set |
| TR-01 funding | The Core framework migration (TR-01 on the technology risk register): 120, 190, or 243 engineer-days ($96,000 to $194,400), expensed. One open critical vulnerability waits on it | Open | Not set |

Two further items fall in quarter 4. Victor says he will either sign the auth-svc security exception
before week 50 or have auth-svc restricted further. The rules and processes inventory (weeks 50–51)
gives a draft verdict on every organization-wide rule; whether Victor uses it is open.

## Week 50: the board and the audit committee

The quarter 4 board meeting is in week 50. Helena Marsh (CEO) presents the year-2 operating plan and
budget envelope for approval. Victor's agenda item is the three-year technology strategy, for
discussion, not approval. Decisions inside the envelope stay with management: the year-2
organization, the quality continuation, and the workforce plan. The same week, the audit committee,
chaired by Margaret Lin, holds a technology risk session. Victor reviewed the director's draft risk
register in week 48. The board's response and the committee's are not recorded.

## Where to read more

The quarter 4 record covers [the CTO's job](first-quarter.md#the-ctos-job-chapter-50),
[finances](first-quarter.md#finances-chapter-52),
[risk and security](first-quarter.md#risk-security-and-compliance-chapter-53),
[data and AI](first-quarter.md#data-and-ai-chapter-54), and
[board preparation](first-quarter.md#board-preparation-chapter-55).

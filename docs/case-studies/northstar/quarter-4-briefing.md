# Northstar at the start of quarter 4

!!! warning "Fictional"
    Everything on this page is invented for the book. See the note on the
    [Northstar overview](index.md).

This briefing is for readers who start at Parts X–XIII. It says where Northstar stands at week 40 of
the director's first year, what the latest results are, and which decisions are open. None of these
decisions has a recorded outcome, and the chapters leave each one open. If you have not followed the
story, read [the year in brief](year-in-brief.md) first (about six minutes). The details are in
[quarter 4 of the year 1 record](first-quarter.md#quarter-4); the people are on the
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

## The three decisions that drive quarter 4

Three decisions shape everything else in quarter 4. Each draws on the same fixed pool of 87 people
(80 engineers, 6 managers, and the director; see [seat](../../glossary.md#seat)).

**The year-2 organization.** The director proposes splitting Customer Experience into Web, under Daniel
Cho, and Mobile, under Mateo Arango Ríos in Bogotá, whose engineering seat would not be backfilled.
core/permissions moves to Orders, search-svc to Data and Analytics, and Platform Operations becomes
Developer Platform, run as an internal product. Three alternatives are in the draft: keep Customer
Experience whole with two subteams (B), also split Orders and grow the platform team (C), or add two
managers of managers (D). Victor Lindqvist decides by week 46; the change would be announced in week 51
and take effect in week 53, the start of year 2. At stake: about 21 engineer-weeks of transition cost,
and whether the shape that carried year 1 fits year 2.

**The quality continuation.** The director's two-year proposal continues the quality program in two
named stages. Stage 2, "Hold", covers quarters 5–6 with 6 FTE of prevention work and $150,000 of
tooling. Stage 3, "Converge", covers quarters 7–8 with 5 FTE, plus $100,000 of tooling only if a CI
target is chosen. Each stage ends at a gate, a review where written exit criteria decide whether the
next stage is funded, in weeks 56, 78, and 104 (the "week 78 gate" is the end of stage 2). There is no
headcount request. Management decides inside the board's
[budget envelope](../../glossary.md#budget-envelope); the executives took positions in weeks 46–47, and
decisions are requested by week 51. At stake: whether prevention keeps its capacity, when Rajiv Menon
(CFO) wants the tooling offset inside the existing budget and Greg Tanaka (VP Sales) wants the
prevention engineers on deal features.

**The board headline.** The engineering page of the [board pack](../../glossary.md#board-pack) needs
one reliability promise. Victor proposes "Sev1 and Sev2 incidents below 10 per quarter" with flat
headcount. The director's counter is at or below 40 over year 2 as a rolling four-quarter total,
reported with the severity audit, together with 99.9 percent availability every quarter and prevention
funded as in the continuation. The draft page carries both; the pack goes to the board at the end of
week 49. At stake: the number the board will hold engineering to for a year, and whether it rewards
reclassifying incidents instead of preventing them.

## Other open items

| Item | What is at stake | Who decides | By when |
|---|---|---|---|
| VP of Engineering | Whether Northstar adds a VP in year 2 or the director grows into the role. A VP takes one of the 87 seats, so one engineer seat goes | Victor asked for a recommendation | Week 48 |
| Workforce plan | How vacancies are filled in year 2. Four options: like-for-like backfills, shaped backfills, two [requisitions](../../glossary.md#requisition) held ahead (which needs an exception to the 87-seat rule), or a fixed-scope vendor contract; plus the rule "no customer date without an engineering estimate and a named owner", which Greg opposes | Draft to Victor and Rajiv in week 49; recommendation left open | With the budget pack |
| Week 32 portfolio forum | Whether Greg's third deal feature (purchase approval rules) breaks the limit of three cross-team initiatives in progress | The portfolio forum | Held week 34; outcome not recorded |
| CI target | Which build system the other three converge on. GitLab CI was proposed in quarter 2, and stage 3's tooling depends on the choice | Open; Victor's strategy draft says the week 78 gate | Week 78 (draft) |
| [ADR-0001](../../glossary.md#adr-0001) | How integrations read posted ledger data: read the tables, a versioned export contract (Li Na Zhou's recommendation), or ledger posting events. Victor's strategy draft reverses his week 14 "read the tables" remark | Nobody's decision rights are mapped | Week 60 (proposed) |
| SOC 2 | Whether Northstar gets an independent audit report on its controls: option A (audit in year 2), B (readiness in quarters 5–6, decision at week 78; recommended), or C (evidence library only). A prospect worth about $310,000 a year requires a report | Not named; the options are in the risk register drafted for Victor's review | Not set; option B decides at week 78 |
| AI position | How engineers may use AI tools, and which AI features to build: an interim policy, a staggered coding-assistant trial in quarter 5, non-AI fixes first for order checking, the order assistant deferred, no backfills held open on AI | Victor, for whom the position is written; all decisions open | Trial would start week 53 |
| Security reporting line | Whether the two-person security function stays inside IT. Marta Kowalczyk (Head of IT) objects to moving it; three options are recorded without a recommendation | Open; none chosen | Not set |
| TR-01 funding | Whether to pay for the Core framework migration, item TR-01 on the technology risk register (see [register IDs](../../glossary.md#register-ids)): 120, 190, or 243 engineer-days ($96,000 to $194,400 at Finance's day rate of $800), expensed. One open critical vulnerability waits on it | Open | Not set |

Finance's day rate is $185,000 ÷ about 230 working days. It is higher per day than the book's planning
rate of $3,558 per engineer-week because Finance counts only working days.

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

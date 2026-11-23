# Chapter 55 solutions — Boards, Due Diligence, and Executive Decision-Making

Worked solutions for the [chapter 55 exercises](../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional, and the scenarios marked hypothetical in the exercises are not part of Northstar's record.

## The headline table: how the probabilities are computed

The chapter's table treats quarterly Sev1 and Sev2 counts as Poisson, that is, varying randomly around a
fixed true average. With a true quarterly mean of 9, the chance a quarter has 9 or fewer is about 0.587,
so "below 10" fails in a single quarter about 41 percent of the time, and holds in all four quarters with
probability 0.587⁴, about 0.119. For the annual total, the yearly mean is four times the quarterly one:
with a yearly mean of 36, the chance of 40 or fewer is about 0.777; with 40, about 0.542; with 48, about
0.138. These are the 78, 54, and 14 percent in the last column.

## F1 — From dashboard to board page

**Keep five measures**, each with definition and source beneath it:

| Measure | Board translation | Label |
|---|---|---|
| Availability 99.89% (contractual paths, synthetic checks) | About 144 minutes unavailable against about 131 allowed in a 91-day quarter: 13 minutes short of the contract | Information, stated first |
| Service credits $60,000 | About $240,000 a year at this rate, against $1.64M at baseline ($410,000 × 4) | Information |
| Sev1 and Sev2: 14 (week 3 definitions, weekly severity audit) | Mandate of at most 15 met for the first time; one quarter, not yet a trend | Information |
| Unplanned work 25% | About 20 of 80 engineers' capacity on recovery and interrupts (80 × 25%) | Information |
| The reliability commitment for year 2 | Protects about $7.0M of ARR renewing in quarters 5 to 8 (6 × $1.17M) | Discussion, inside the plan the board approves |

**Removed.** Core's change failure rate (a release-train measure from quarter 2, not the latest quarter,
on counts too small for a board to interpret); flaky tests (an input, not an exposure); the tier 1
minimums (keep them in the CTO's own review; mention only if the board has asked about operational
readiness); the CI target (a management decision with no material risk at board level).

A good answer leads with the miss in minutes, keeps every number identical to the director's dashboard,
and labels at most one item for discussion. The weak answer keeps eight measures "for completeness",
or presents 99.89 percent as success.

## F2 — Assigning diligence findings

| Finding | Assignment | Evidence that would change it |
|---|---|---|
| Database past end of support, with a migration estimate | Price (the estimate, with a contingency) and integration plan | An estimate the target cannot explain moves it to terms (a specific warranty) |
| One engineer alone understands the billing engine | Terms (a retention agreement for that engineer) and integration plan (knowledge transfer in the first quarter) | If billing is the thesis and the engineer will not stay, it can break the thesis |
| Strong copyleft library linked into the distributed product | Terms (warranty and indemnity, a closing condition to remediate) until the obligation is analyzed | A legal analysis showing the obligation is met, or the library replaced, moves it to integration |
| Attestation claimed, only a summary letter sent | Terms: closing condition that the full report is produced | If the report does not exist or covers something else, it becomes a question of honesty, which can mean walking away |
| Cloud cost per customer doubled in a year | Price, if the cause is understood; diligence continues if not | A cause found in architecture rather than usage changes the thesis's margins |

The reasoning follows the chapter's triage: estimable cost goes to price, unestimable risk to terms, known
work to the integration plan, and anything that breaks the thesis to a walk-away. Note the attestation:
the problem is not the missing letter but the gap between claim and evidence, which Larson names as a
common overlooked risk. A good answer states what evidence would move each item. The weak answer files
everything under "integration risk" with no effect on price or terms, which means diligence changed
nothing.

## F3 — Placing Northstar's open decisions

| Decision | Decider | Cheap to reverse? | What the board sees |
|---|---|---|---|
| Year-2 operating plan and envelope | Board, on Helena Marsh's proposal | No (a year's commitment) | It decides, in week 50 |
| Year-2 organization proposal | Victor Lindqvist (the CTO decides) | Partly; reorganizations are costly to reverse (about 21 engineer-weeks of transition) | Informed, as part of how the plan will be delivered |
| $150,000 of stage 2 tooling | Within the envelope: Rajiv Menon's approval, offset or not | Yes, mostly (tooling contracts aside) | Nothing separately; it sits inside the envelope |
| Workforce option C (exception to the 87-seat rule) | The executive team; if the envelope assumes 87 seats, it may need the board | No (hires are hard to reverse) | Only if it changes the envelope the board approved |
| CI consolidation target | Delegated technical decision (Chapter 32), owned under the CTO | Expensive to reverse once migrated | Not involved |
| Reliability headline on the board page | Victor Lindqvist, with Helena Marsh | Cheap to change before the pack, expensive after | It is what the board will hold engineering to |

The subtle one is option C: it is a management decision unless it breaks the envelope the board is
about to approve, in which case raising it before week 50 is honest and raising it after is asking for
forgiveness. A good answer catches that, and notices that the headline becomes costly to reverse once
published. The weak answer sends the year-2 organization to the board, which asks directors to decide
what they cannot oversee.

## A1 — The expert director

**What to give.** The quarter 3 incident list in summary form (counts by severity and trigger, each
Sev1 with a one-line cause and the corrective action's status), the availability definition, and the
quarter 2 risk register entry for the Core framework (TR-01). This is information the board is entitled
to, and David Ferrante will read it well.

**What to decline.** An architecture review before the meeting whose conclusions would carry a
director's authority. Offer instead a working session after the meeting with Kwame Mensah and Ines
Carvalho, framed as advice to management.

**What to say.** "I'd value your eyes on the payment path. Let me send the incident summary and the
availability definition this week so you have what the rest of the board has. I'd rather not have a
director review the architecture before the meeting, because whatever you conclude would read as the
board's view. After week 50 I'd like you to spend a session with Kwame and Ines as an adviser; we'll
decide what to do with your input." On the weekly train: acknowledge the point, and offer to show which
parts of the payment path ship on the Core train and which deploy as services.

**The chair.** Tell Anders Holm briefly that David asked for detail, what was sent (the same to all
directors on request), and the offer made. A good answer uses the expertise, keeps the decision line,
and keeps the board informed equally. The weak answers are refusing everything (losing an ally) or
granting a private review (creating a second line of authority).

## A2 — Readiness for a hypothetical technology review

**Weeks 1–2: inventory.** Collect what exists: the enterprise technology risk register (ER-01 to ER-09),
incident and availability history since baseline, the decision log and ADRs, the succession table,
dependency scan coverage and the vulnerability exceptions with expiry dates. Name the gaps: at the week 44
snapshot, 14 of 15 tier 1 components had an SBOM per build (all but auth-svc), none had signed provenance,
and no license inventory is recorded.

**Weeks 3–6: close cheap gaps.** Extend SBOMs to auth-svc and the non-tier-1 components, and confirm the
14 tier 1 SBOMs are current (20 components were scanned in the pipeline and 4 weekly at week 44); run a
license scan; write a
two-page architecture overview with Ines Carvalho. Budget about two engineer-weeks, taken from Platform
Operations' planned work, not from stage 2's prevention capacity.

**Weeks 7–8: rehearse.** Victor and the director answer twenty likely questions against the evidence and
compare the answers with the last four board packs.

**Who knows.** Victor, the director, Kwame Mensah, Ines Carvalho, and Rajiv Menon, under confidentiality;
the rest of engineering sees the SBOM and license work as normal hygiene, which it is.

**Presentation.** The Core framework risk as in the register: what it is, the 120 to 180 engineer-day
estimate, the owner, the patching under exception meanwhile. Any open vulnerability exceptions with
mitigation and expiry. **Refuse:** to remove items from the register before the review, to describe a
plan as done, or to divert prevention engineers. A good answer makes the data room agree with the board
packs. The weak answer treats readiness as presentation work.

## A3 — A possible exposure the day before the pack

**Order of notification.** Victor tells Helena Marsh the same day, with Joon Park's assessment and what is
unknown; Rajiv Menon, because security sits in IT under him; and, with Helena, Margaret Lin as audit
committee chair, because the audit committee oversees technology and security risk. The chair, Anders
Holm, hears from Helena. Everyone gets the same short written note: what is known, what is not, what is
being done (rotate the key now, which is cheap and reversible; investigate whether it was used), and when
the next update comes.

**The pack.** Do not hold or rewrite the engineering page to hide it, and do not put an unconfirmed
incident into a document that will circulate. Add one line under risks, agreed with Helena and Margaret
Lin: a possible key exposure under investigation, key rotated, update at the meeting.

**If asked in week 50.** State what is known by then, plainly, including whether it was used.

**The record.** A timestamped log: when Joon knew, when Victor knew, whom he told, and what was decided.

**Why.** In the Yahoo case the SEC's finding was not only about the breach but about the absence of
controls that took the security team's knowledge to the people deciding disclosure. A good answer builds
that path in hours. The weak answer waits for certainty before telling anyone, which is the failure the
case illustrates.

## X1 — Choosing the headline

**One defensible choice: the director's counter (option B).** Reasoning for the record: at a true average
of 9 a quarter, "below 10" is met in only about 59 percent of quarters and in all four only about 12
percent of the time; at a true average of 10 it is met all year about 4 percent of the time. A target
missed by chance pushes on severity ratings, which Margaret Lin will probe. The rolling total of 40 is met
about 78 percent of the time at a true average of 9 per quarter, and is still reported every quarter.

**Completed record.** Decision: option B. What we would have to believe: the board accepts an annual
commitment shown quarterly; the rolling total is read with the audit result beside it. Dissent (Victor,
if he concedes; or the director, if Victor keeps A): "A quarterly number is what the board can check; an
annual total hides a bad quarter until it is too late." Reversal trigger: two consecutive quarters above
12 reopen prevention with Victor and Amara Okafor. Review: week 78, against this record.

**Board paragraph.** "In year 2 we commit to at most 40 Sev1 and Sev2 incidents, shown every quarter as a
rolling four-quarter total with the result of the weekly severity audit run in the director's operational review, and to 99.9 percent
availability on the contractual paths every quarter. Quarter 3: 14 incidents; 99.89 percent, 13 minutes
short."

**To Margaret Lin.** "Severity is rated against written definitions and audited weekly in the operational
review; any re-rating appears in the audit result we show you." If she presses on independence, say
plainly that the audit is run by engineering today, and that having someone outside engineering sample it
(for example Joon Park or Finance) is a proposal, not current practice.

Option A is defensible if Victor records the chance of a miss and pre-commits to how a chance miss will be
explained. The weak answer picks either option without the arithmetic or without recording the dissent.

## X2 — Diligence as an acquirer at Halvard

**The thesis**, written before diligence starts: the target's product becomes a fifth group; its platform
can carry Halvard's customer base within two years; its key engineers stay; integration costs fit inside
the price.

**Design.** A team of five (a principal engineer, a security lead, an infrastructure lead, a finance
partner, the CTO), a base template (product, intellectual property, security, compliance, integration,
cost and scale, culture) plus thesis-specific questions, materials requested in week one, two meetings
with the target's engineers, hands-on use of the product, and a code read of the core. Each finding is
logged with its branch (price, terms, integration, walk away) and its cost estimate.

**The attestation finding.** It does not cover the product being bought. Tell the CEO the same day, in
writing: the claim and the evidence do not match; the security and compliance posture of the acquired
product is unknown; this cannot be priced. Recommend terms that make closing conditional on an
independent assessment, or a delay. If the target described the attestation as covering this product,
say plainly that it is also a question of candor, which the CEO and the deal team must weigh.

**One vote.** The CTO cannot veto, so the recommendation must be specific and priced: "close only with
these conditions" is a position the deal team can act on; "engineering has concerns" is not. Record the
recommendation and, if overruled, the dissent and the reversal trigger (for example, the assessment's
result). The weak answer either blocks the deal in general terms or accepts the summary to keep the
timetable.

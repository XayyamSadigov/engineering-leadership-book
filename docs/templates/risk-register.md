# Risk register

**Used in:** [Chapter 30](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md)
(the first technology risk register), [Chapter 53](../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md)
(enterprise technology risk, governance, and reporting),
[Chapter 55](../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md)
(reporting to a board).
**Owner:** the CTO for the enterprise technology register; a director or vice president for an
engineering or group register. Each line has its own owner and accepter.
**Cadence:** engineering register monthly in the quality review; enterprise register quarterly with
the CFO and head of IT; reported to the [audit committee](../glossary.md#audit-committee) twice a year,
and at the next meeting whenever a risk moves outside appetite. Every acceptance carries an expiry date
and is decided again on it.

A [risk register](../glossary.md#risk-register) is a decision record. Each line exists to force one
decision (reduce, transfer, avoid, or accept) by a person with the authority to make it, and to show
later whether the decision still holds. [Risk appetite](../glossary.md#risk-appetite) is the amount of
risk the company has agreed to carry, written as lines a risk is inside or outside. A register that
only lists worries, or is rebuilt once a year for a committee, does neither.

!!! tip "Minimum version"
    Start with five fields per risk: the statement (cause, event, consequence), owner, accepter,
    treatment with a date, and review date. Add ratings, exposure, indicators, and appetite once the
    company has a scale and appetite lines to rate against.

## How to fill it in

1. **Collect the existing lists.** Team and engineering registers, IT's risks, open security findings,
   compliance and customer demands, and the company register's technology lines.
2. **Write each risk as cause, event, consequence.** "Because X, Y may happen, which would cause Z."
   The consequence is in business terms; the technical cause is underneath.
3. **Group by consequence** at the enterprise level and list the grouped items in the sources column,
   so anyone can audit the roll-up.
4. **Name an owner and an accepter.** The owner manages the risk and its treatment. The accepter has
   authority over the residual risk: the owner inside appetite, a director outside appetite, the CTO for
   tier 1 or financial risks, with the audit committee informed of company-level risks outside appetite.
   For risks owned outside engineering, the accepter is the executive the owner reports to (for IT, the
   CFO); for commercial risks the CTO owns, the CEO.
5. **Rate for triage, then add exposure.** Use the company's scale. Add a dollar range only where
   finance or contract numbers support one; otherwise write "not quantified". Explain each score in one
   sentence.
6. **Decide the treatment** with action, cost, owner, and date. For acceptance, record the reason and
   an expiry no more than two quarters away.
7. **Choose an indicator** that moves before the risk does, with its current value.
8. **Check against appetite.** If the company has appetite lines, mark each risk inside or outside.
9. **Set the review date.** An expired acceptance escalates one level; it is not renewed by the same
   person.

## Template

| Field | Contents |
|---|---|
| ID | Stable identifier; never reused |
| Risk statement | Cause, event, consequence |
| Category | Reliability, security, financial correctness, compliance, concentration, end of life, vendor, people |
| Sources | Lower-level items this line groups |
| Owner | Manages the risk and the treatment |
| Accepter | Authority over the residual risk, at the level the rules require |
| Likelihood, impact, score | On the company's scale, with one sentence of reasoning |
| Exposure | Dollar range with its derivation, or "not quantified" |
| Trend | Rising, flat, or falling since the last review, with the evidence |
| Treatment | Reduce, transfer, avoid, or accept; action, cost, owner, date |
| Indicator | Measure that moves before the risk; current value and threshold |
| Appetite | Inside or outside; which appetite line |
| Acceptance | If accepted: reason, accepter, date signed, expiry |
| Review date | When the decision is made again |

```yaml
register:
  name: ""
  level: ""                      # team / engineering / group / enterprise
  owner: ""
  last_review: ""
  scale:
    likelihood: ""               # what each point means, in time or frequency
    impact: ""                   # what each point means, in business terms
  appetite_lines: []             # each in the units of an indicator
risks:
  - id: ""
    statement: ""                # because ..., ... may happen, which would cause ...
    category: ""
    sources: []
    owner: ""
    accepter: ""
    rating: {likelihood: 0, impact: 0, score: 0, reasoning: ""}
    exposure: {range: "", derivation: ""}   # or range: not quantified
    trend: {direction: "", evidence: ""}
    treatment:
      type: ""                   # reduce / transfer / avoid / accept
      action: ""
      cost: ""
      owner: ""
      due: ""
    indicator: {measure: "", current: "", threshold: ""}
    appetite: {inside: true, line: ""}
    acceptance: {reason: "", accepter: "", signed: "", expires: ""}
    review_date: ""
```

## Example: Northstar, enterprise technology register (draft, week 47)

!!! info "Northstar so far"
    Week 47 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Victor Lindqvist (CTO) asked for an enterprise technology risk register after Margaret Lin, who
    chairs the board's audit committee, asked for a risk session in week 50. This is the director's
    draft; whether the committee adopts its appetite lines is not recorded. See the
    [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md), the
    [cast](../case-studies/northstar/cast.md), and the
    [quarter 4 briefing](../case-studies/northstar/quarter-4-briefing.md).

The figures come from [risk, security, and compliance](../case-studies/northstar/first-quarter.md#risk-security-and-compliance-chapter-53)
and [finances](../case-studies/northstar/first-quarter.md#finances-chapter-52) in the year 1 record.
Weeks count from the director's first week ([weeks](../glossary.md#weeks-quarters-and-years)); ER-01 to
ER-09 are this register's IDs and TR-01 is an item on the lower-level technology register
([register IDs](../glossary.md#register-ids)). The ratings, reasoning, and exposure ranges are illustrative. Other people named: Marcus
Oyelaran (Billing manager), Tom Becker (Platform Operations manager), Kwame Mensah and Ines Carvalho
(staff engineers), Joon Park (IT security lead), Marta Kowalczyk (Head of IT), Rajiv Menon (CFO), and
Helena Marsh (CEO).

**Scale.** Likelihood 1 to 5, where 4 means expected within four quarters and 5 means already
happening. Impact 1 to 5, where 4 means a tier 1 path, financial correctness, or a material deal at
stake and 5 means revenue at renewal or contractual breach. ER-01 is rated likelihood 4 because six
top-40 renewals fall in quarters 5 to 8 and availability was below 99.9 percent in every quarter in
which it was measured (99.86 and 99.89 percent); a loss is judged likely, not certain.

**The numbers behind the exposure column.** Six of the 40 largest customers renew in quarters 5 to 8,
at about $1.17M a year each, with a 72 percent gross margin. TR-01 is the migration of Core (the
company's monolith) off its unsupported framework. Finance prices it at its **day rate**, $800 an
engineer-day ($185,000 ÷ about 230 working days). That is more per day than the book's planning rate of
$3,558 an engineer-week because Finance counts only working days.

| Item | Derivation | Result |
|---|---|---|
| Revenue at renewal | 6 × $1.17M | $7.02M |
| Margin per customer lost | $1.17M × 72% | about $842,000 a year |
| Service credits, annualized | $60,000 (quarter 3) or $95,000 (quarter 2) a quarter × 4 | $240,000 to $380,000 a year |
| Questionnaire load | 34 × 14 hours = 476 hours; ÷ 1,840 hours a year; × $185,000 | 0.26 FTE, about $48,100 a year |
| TR-01 migration | 120, 190, or 243 engineer-days × $800, Finance's day rate (Finance's scenarios) | $96,000, $152,000, or $194,400 |

| ID | Risk (consequence) | Owner | Accepter | Score | Exposure | Treatment | Appetite |
|---|---|---|---|---|---|---|---|
| ER-01 | A large customer leaves at renewal over reliability | Engineering Director | Victor Lindqvist | 20 | About $842,000 a year of margin per customer lost; credits $240,000 to $380,000 a year | Reduce ([the continuation](../glossary.md#the-continuation), the two-year quality proposal) | Line 1: inside (the year-2 plan targets 99.9 percent); quarter 3's 99.89 percent is reported with its cause |
| ER-02 | A financial error reaches customers | Marcus Oyelaran | Victor Lindqvist | 12 | Not quantified | Reduce (pairing; a decision on the tax service, tax-svc) | No line |
| ER-03 | A [known-exploited vulnerability](../glossary.md#known-exploited-vulnerability-kev) on internet-facing tier 1 is exploited | Tom Becker | Victor Lindqvist | 15 | Not quantified | Reduce; exception to week 52 | Line 2: outside |
| ER-04 | The build and deploy path is compromised or lost | Kwame Mensah | Victor Lindqvist | 15 | Not quantified | Reduce (CI consolidation phase 1, secrets manager) | Line 3: outside while auth-svc deploys by script |
| ER-05 | The Core platform cannot be patched | Ines Carvalho | Victor Lindqvist | 12 | Migration $96,000 to $194,400 (Finance's scenarios) | Accept with patches until the migration decision | No line |
| ER-06 | Missing assurance costs deals and renewals | Victor Lindqvist | Helena Marsh (commercial risk owned by the CTO) | 12 | At least $310,000 of annual recurring revenue (ARR); $48,100 a year of capacity | Decision open: [SOC 2](../glossary.md#soc-2) audit in year 2, readiness first, or an evidence library only | No line |
| ER-07 | Card data scope is wider than believed | Joon Park | Rajiv Menon (IT-owned; payments correctness is also Victor Lindqvist's concern) | 8 | Review about 5 days | Reduce (scope review) | No line |
| ER-08 | A corporate identity compromise reaches production | Marta Kowalczyk | Rajiv Menon (IT-owned) | 12 | Not quantified | Reduce | No line |
| ER-09 | Corporate business systems are lost | Marta Kowalczyk | Rajiv Menon | 6 | Not quantified | Reduce (restore tests) | No line |

One line in full:

```yaml
register:
  name: Northstar enterprise technology risk register (draft)
  level: enterprise
  owner: Victor Lindqvist
  last_review: week 47 (director's draft)
  scale:
    likelihood: "1 rare ... 4 expected within four quarters, 5 already happening"
    impact: "4 tier 1 path, financial correctness, or material deal; 5 revenue at renewal or contract breach"
  appetite_lines:
    - "L1: order and payment paths planned at or above 99.9 percent every quarter"
    - "L2: no known-exploited vulnerability on internet-facing tier 1 open beyond 7 days without a
       compensating control and a CTO-signed exception of at most one quarter"
    - "L3: every production change to tier 1 passes an auditable pipeline; exceptions named"
risks:
  - id: ER-03
    statement: Because auth-svc deploys by shell script and cannot take the library upgrade safely, a
      known-exploited critical stays mitigated only at the load balancer, and an attacker who bypasses
      the restriction could reach customer sessions on the order path
    category: security
    sources: [auth-svc known-exploited critical, Core critical held by TR-01, 9 highs past service level]
    owner: Tom Becker (auth-svc); Ines Carvalho (Core item)
    accepter: Victor Lindqvist
    rating: {likelihood: 3, impact: 5, score: 15, reasoning: "exploit code exists by definition of
      known-exploited; one control stands between it and a tier 1 path"}
    exposure: {range: not quantified, derivation: "Northstar has no defensible breach-cost estimate"}
    trend: {direction: falling, evidence: "open criticals 11 at baseline, 3 at day 90, 2 in week 44"}
    treatment:
      type: reduce
      action: move auth-svc to an auditable pipeline, then upgrade the library
      cost: inside CI consolidation phase 1; auth-svc first is an option
      owner: Tom Becker
      due: not yet committed
    indicator: {measure: "days the known-exploited item is open past 7", current: "far beyond one quarter", threshold: "any value above 0 without a CTO-signed exception"}
    appetite: {inside: false, line: L2}
    acceptance: {reason: "compensating control at the load balancer", accepter: "Engineering Director (quarter 1, 'until the migration'); no CTO signature", signed: "quarter 1", expires: "week 52, written in by Joon Park in week 44 with no new signature"}
    review_date: week 52
```

What to notice: four risks score 12 and have nothing in common, which is why the exposure, reasoning,
and appetite columns exist. Two risks are outside the proposed appetite on the day it is proposed; the
draft says so rather than softening the lines. ER-03's acceptance shows the commonest defect in real
registers: a temporary exception recorded at one level and never re-decided at the level its risk
requires. And the only line with a defensible dollar range, ER-01, is not a security risk at all.

## Common mistakes

- **One line for all technology risk.** "Cyber attack or IT outage", rated amber for years, governs
  nothing. Split by consequence with one owner each.
- **Owner and accepter are the same person by default.** The person who would bear the consequence, or
  someone senior enough to, accepts.
- **Acceptances without expiry.** They become permanent by neglect.
- **Scores without reasoning.** Two 12s for different reasons look identical.
- **Invented dollar figures.** Write "not quantified" rather than borrowing a breach-cost statistic that
  does not describe your company.
- **Activity indicators.** Training completion and scans run do not move before a risk does.
- **A register nobody below the CTO has seen.** Items must appear in the reviews where owners report
  progress.

## Review questions

1. Which line has been accepted without anyone signing the acceptance, and who should sign it?
2. If two lines with the same score swapped places, would any decision change? If not, what does the
   score add?
3. Which indicator would have moved first before the last serious incident?
4. Which risks are outside appetite today, and has the audit committee been told?
5. Which lower-level item is not represented in any enterprise line, and why?

## Evidence and references

The method is [Chapter 53](../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md);
this template gives the fields.

- [Quinn et al., 2025](../references/bibliography.md#nist2025ir8286r1): NIST IR 8286 Rev. 1 describes
  risk registers at system and organizational levels whose measures roll up to the enterprise
  (**standard**).
- [Cox, 2008](../references/bibliography.md#cox2008risk): the abstract reports that likelihood-impact
  matrices are poor at ranking risks and can rate smaller risks above larger ones (**research
  finding**). The template keeps a matrix because most companies' registers use one, and adds an
  exposure range and a line of reasoning beside every score.

The two-quarter limit on acceptances, the accepter rules, and the field set are **this book's
recommendation**.

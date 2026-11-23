# Chapter 52 — Technology Investment, Budgeting, and Financial Literacy

A CTO controls one of the largest budgets in a software company and is often the executive least
practiced at reading where that money shows up. This chapter assumes no finance training. It teaches
the three financial statements and the engineering budget as an annual contract with finance. It then
covers the choice between capitalizing and expensing software work, and the investment case written
with scenarios instead of one hopeful number. The running example is Victor Lindqvist,
CTO of the fictional [Northstar Technologies](../../case-studies/northstar/index.md), in quarter 4 of the
Engineering Director's first year, as Finance prepares the year-2 budget for the week 50 board.

Related chapters: [45](../10-business-leadership/45-business-models-and-engineering-economics.md) (the
economics underneath: cost of delay, payback, net present value), 48 (vacancy and workforce plans), and
49 (staged funding).

## Why This Matters

At team scale, money is invisible. Engineers are paid whatever the team works on, and a manager's first
meeting with finance is often an unexplained request to tag tickets for "capitalization".

At organization scale, the director's budget is mostly people, and the job is spending it well
(Chapters 38 and 48). Money shows only at the edges: a tooling purchase above the limit, a cloud bill that
grew, a CFO's request for an output-per-engineer figure.

At executive scale, the CTO answers for a large share of operating expense and for numbers the board
reads directly. At Northstar, engineering personnel plus cloud and tooling are $20.3M a year, about 14
percent of revenue. The board reads that spending through operating income,
[EBITDA](../../glossary.md#ebitda) (earnings before interest, tax, depreciation, and amortization), and
cash. The CFO books part of it as an asset, and investors may value the company on a multiple of a figure
that engineering's time sheets change. A CTO who cannot follow a dollar of salary through the three
statements cannot tell when an accounting presentation makes an investment look cheaper than it is. Nor
can that CTO defend a budget in the room where it is cut.

## Learning Objectives

After this chapter you will be able to:

- Read an income statement, balance sheet, and cash-flow statement and locate every place technology
  spending appears in them.
- Explain capitalized versus expensed software work, apply the current US standard's criteria to real
  work items, and predict the effect of a capitalization policy on operating income, EBITDA, and cash.
- Build an engineering budget in both views finance uses (by function and by accounting treatment),
  separate the forecast from the target, and defend it in variance reviews.
- Write an investment case with scenarios, stated assumptions, and the input that would change the
  decision, and show how it will be booked as well as what it is worth.
- Detect the common ways budgets and capitalization are gamed, including by engineering leaders.

## The Mental Model

> **Mental model:** One set of events, three lenses. The income statement asks whether the company
> earned money in a period, the balance sheet what it owns and owes at a moment, the cash-flow
> statement whether money actually arrived. Accounting choices, above all capitalization, move
> engineering spending between the lenses and across years. They change timing and presentation, not
> economics: the cash left when the engineers were paid, and the capacity was spent when they worked.

The first consequence: before arguing about any figure, ask which lens it comes from. "Engineering
personnel costs $16.1M" is a cash and budget figure. "R&D expense is $16.4M" is an income-statement figure
that includes other things and excludes the capitalized part. Both are right.

The second consequence: the decision and the booking are separate questions. Chapter 45 decides
whether an investment is worth its capacity; this chapter adds how it will look in the statements, on
which executives are measured. A good project can look expensive, and a poor one cheap.

```mermaid
flowchart TD
    PAY["Engineer paid: cash out"] --> Q{"Capitalizable work?"}
    Q -->|No| EXP["Expense this year"]
    Q -->|Yes| ASSET["Asset on balance sheet"]
    ASSET --> AMORT["Amortized over years"]
    EXP --> PL["Income statement"]
    AMORT --> PL
    EXP --> CFO["Cash flow: operating"]
    ASSET --> CFI["Cash flow: investing"]
```

| Path | Income statement | Balance sheet | Cash-flow statement |
|---|---|---|---|
| Expensed work | Full cost this year, inside R&D or cost of revenue | Nothing | Operating outflow this year |
| Capitalized work | Nothing until the software is in service, then amortization over its useful life (Northstar amortizes each year's amount over the following three years) | An asset that shrinks as it is amortized | Investing outflow this year; operating cash flow looks higher |

The cash leaves in the same week either way. What changes is which line shows it and in which year.

!!! note "Terms used in this chapter"
    - **Amortization and depreciation**: spreading the cost of an asset over the years it is used.
      Amortization is the word for intangible assets such as capitalized software; depreciation is the
      word for physical ones such as laptops and servers. Neither is a cash payment.
    - **[Fully loaded cost](../../glossary.md#fully-loaded-cost)**: the full yearly cost of one employee,
      salary plus benefits, payroll taxes, and seat costs. Northstar uses $185,000 per engineer-year.
    - **Working capital**: the money tied up in day-to-day operations, such as amounts customers owe minus
      amounts the company owes suppliers. When customers prepay more, working capital releases cash.
    - **Controller**: the finance executive who keeps the books, closes each period, and works with the
      auditors, usually reporting to the CFO.
    - **[Discount rate](../../glossary.md#discount-rate-and-hurdle-rate)**: the yearly rate that shrinks
      future money to today's value. Northstar's Finance uses 10 percent.
    - **Annuity factor**: converts a yearly amount into today's money at the discount rate. Three years at
      10 percent gives 2.487, so $1 a year for three years is worth about $2.49 today (Chapter 45).
    - **Fiscal years**: FY1 is the director's first year (weeks 1 to 52), FY0 the year before, FY−2
      the year before that, and FY2 is year 2.

## Deep Conceptual Explanation

### The three statements, read by a technology leader

The definitions here are **standard**, from the US Securities and Exchange Commission's introductory
guide ([SEC, 2014](../../references/bibliography.md#sec2014beginners)). Behind the balance sheet is one
identity: assets equal liabilities plus shareholders' equity.

**The income statement** reports revenue earned over a period and the costs of earning it. Read it
top-down:

| Line | What it is | Where technology sits |
|---|---|---|
| Revenue | Subscription and services revenue recognized in the period | Service credits usually reduce it directly |
| Cost of revenue | Costs of delivering the service | Production hosting, support, third-party fees, often amortization of capitalized software |
| Gross margin | Revenue minus cost of revenue, as a share of revenue | Hosting efficiency and incident load move it |
| Operating expenses | Research and development (R&D), sales and marketing, general and administrative (G&A) | Most engineering salaries in R&D; corporate IT in G&A |
| Operating income | Gross profit minus operating expenses | The figure "flat operating expense" protects |
| EBITDA | Earnings before interest, tax, depreciation, and amortization | Adds back amortization, so capitalization raises it |

Revenue is not [ARR](../../glossary.md#arr): annual recurring revenue is the run rate of contracts in
force at a moment (Chapter 45), revenue what was earned over a period. They diverge whenever the business grows or
shrinks.

**The balance sheet** is a snapshot. Three lines matter to a CTO of a subscription company.
**Deferred revenue** is a liability: customers paid in advance for service not yet delivered. A renewal
lost to unreliability therefore stops cash before it stops revenue. **Capitalized software** is an
asset: engineering work expected to pay off over several years. **Cash** funds next year's choices.

**The cash-flow statement** has operating, investing, and financing sections. It shows whether the
company generated cash, which differs from net income; the operating section adds back non-cash items
such as depreciation (SEC, 2014). Capitalized software is an investing outflow, so operating cash flow
alone flatters a company that capitalizes heavily. **Free cash flow** removes that effect: in this book,
operating cash flow minus capital spending, including capitalized software. Companies define it
differently, so ask which definition a deck uses.

These numbers rest on estimates and judgment, so reading them well means knowing where the judgment
sits ([Berman and Knight, 2006](../../references/bibliography.md#berman2006financial)). For a technology
leader the largest judgment is capitalization, and engineering supplies its data.

### Capitalized versus expensed software

**Expensing** puts a cost in the income statement when it occurs. **Capitalizing** records an asset and
spreads the cost over its useful life as amortization (SEC, 2014). Accounting standards decide which
software work qualifies; finance applies them and auditors check them. Engineering's job is to describe
the work accurately. This chapter is not accounting advice.

**The engineer's rule.** Under the current US standard, as amended in 2025, three questions decide most
cases (**standard**, in this book's words) ([FASB, 2025](../../references/bibliography.md#fasb2025asu202506)):

1. Has management authorized and committed funding for the project?
2. Is completion probable, with no **significant development uncertainty** left? Uncertainty remains
   while novel features are unproven in code and tests, or while major performance requirements are
   still unknown or changing.
3. Does the work add functionality the software did not have?

If all three are yes, the direct costs below are capitalized until the software is substantially
complete. Otherwise they are expensed.

| Capitalizable once the threshold is met | Expensed |
|---|---|
| Payroll and payroll-related costs of employees working directly on the project, for that time | General, administrative, and overhead costs |
| External direct costs (contractors, purchased software, related travel) | Training |
| Upgrades and enhancements that add functionality the software did not have | Maintenance, and minor upgrades not separable from it at reasonable cost |
| Software that converts old data for new systems | Other data conversion |

**Which guidance applies.** Software a software-as-a-service company uses to serve customers falls under
the US internal-use software guidance, ASC 350-40; software sold or licensed falls under ASC 985-20. A
software-as-a-service company is, in accounting terms, mostly an internal-use software company. The 2025
update (ASU 2025-06) replaced the older project stages (preliminary, application development,
post-implementation), which fit iterative development badly, with the threshold above. Most companies,
Northstar included, still apply the stage-based guidance until the update takes effect; the FASB expects
little change for most software.

**When a project stalls.** If completion stops being probable, capitalization stops and the asset is
impaired, which means written down. The standard presumes uncompleted software is worth zero, and its
warning signs include no budgeted spending, unresolved programming difficulties, and large overruns. An
abandoned capitalized project returns as a write-off.

Outside the US, IFRS (IAS 38) asks a similar engineering question: is this a new capability, with the
uncertainty resolved ([IFRS Foundation, IAS 38](../../references/bibliography.md#ifrs-ias38))? Research
on packaged-software companies under the older US standard found that, as capitalization matured,
amortization of past years roughly offset new capitalization's effect on profit
([Aboody and Lev, 1998](../../references/bibliography.md#aboody1998software)). That is an old,
correlational **research finding**, but the steady-state point holds by arithmetic.

### What capitalization does and does not change

Capitalizable work is measured by ticket, by project, or a hybrid; many finance teams and auditors
distrust fixed percentages per role. Larson's three tests for a tracking method are that it is easy to
justify to an auditor, available in time for reporting, and cheap to run. Most finance teams, he notes,
care more about compliance than about maximizing capitalization
([Larson, 2023b](../../references/bibliography.md#larson2023capitalize); **expert opinion**).

Four effects follow from the mechanics (**this book's recommendation** for reading them):

1. **Cash and capacity do not change.** A capitalized engineer-week costs the same cash and displaces
   the same alternative as an expensed one.
2. **EBITDA rises by the full capitalized amount** every year, compared with expensing.
3. **Operating income rises only while capitalization grows.** In steady state, amortization roughly
   equals new capitalization.
4. **Capitalization creates obligations**: an amortization tail later years absorb, and an impairment
   if a project is abandoned.

Effect 2 makes capitalization a board topic wherever the company is valued on EBITDA.

### The engineering budget

A budget is a quantitative plan of when and how much money will be received and spent. Its known
problems are **practitioner consensus**: padding creates slack, and managers set targets they are sure to
hit ([Franklin et al., 2019](../../references/bibliography.md#franklin2019managerial)). Larson places the
engineering budget inside an annual plan of headcount, capacity allocation, and roadmap, with allocations
changed rarely ([Larson, 2023a](../../references/bibliography.md#larson2023planning); **expert opinion**).
The engineering budget is the part a CTO is expected to own.

Finance needs the engineering budget in two views at once:

| View | Lines | Reader |
|---|---|---|
| By function and kind | Seats, contractors, production hosting, development tooling, licenses | CTO, finance planning, the board's operating plan |
| By accounting treatment | Cost of revenue or operating expense; expensed or capitalized; recurring or one-time | Controller, auditors, the board's income statement |

Four distinctions decide most budget arguments:

- **Budget, forecast, and target differ.** The budget is the approved plan, the forecast the current
  best estimate, a target what someone is rewarded for. Some argue for abandoning budgets altogether
  ([Hansen et al., 2003](../../references/bibliography.md#hansen2003budgeting);
  [Hope and Fraser, 2003](../../references/bibliography.md#hope2003budgets)), but most CTOs work inside
  one. The usable lesson (**this book's recommendation**): reward nobody for the forecast, so it can move
  honestly while the budget stays fixed.
- **Fixed versus variable.** Salaries are fixed within the year; hosting varies with load and with
  engineering decisions. Cloud cost is a shared accountability of engineering and finance
  ([FinOps Foundation](../../references/bibliography.md#finops-what-is)), and a variable cost needs an
  owner who sees it weekly.
- **Committed versus discretionary.** Last year's hiring commits most of the budget, so small
  discretionary caps matter.
- **Seats versus dollars.** Seat budgets hide vacancy, approved money unspent and capacity lost
  (Chapter 48); dollar budgets expose it and tempt finance to bank it.

**Variance**, the gap between budget and actual, has three causes: the plan was wrong, conditions
changed, or execution differed. Vacancy underspend is not efficiency, and a cloud overspend from a new
customer may be good news. Explain variances before finance finds them.

### Investment cases with scenarios

Chapter 45 covers valuation, and the
[technology investment business case template](../../templates/technology-investment-business-case.md)
gives the fields. A CTO-level case adds scenarios, the booking, and protection against the author's
bias.

Forecasts go wrong through optimism bias (judging the future more kindly than experience warrants) and
strategic misrepresentation (understating costs to win approval). Flyvbjerg's remedy, reference class
forecasting, places a project among the outcomes of comparable past projects
([Flyvbjerg, 2006](../../references/bibliography.md#flyvbjerg2006nobel)). His evidence is public
infrastructure, not software, so the transfer is **this book's recommendation**: use your own
organization's estimate history as the reference class. Kahneman, Lovallo, and Sibony propose a
checklist a decision maker runs against a team's proposal to expose its biases
([Kahneman et al., 2011](../../references/bibliography.md#kahneman2011bigdecision)).

| Scenario | Built from | Purpose |
|---|---|---|
| Base | The estimate, uplifted by the organization's typical overrun | What you expect |
| Pessimistic | Top of the range, worst observed overrun, the most likely failure | What you would have to absorb |
| Optimistic | Bottom of the range, no overrun | What the sponsor believes |

Two further lines separate a CTO case from a team request. **The booking** says whether the cost is
expensed or capitalized, recurring or one-time, inside or outside the envelope. **The decisive input**
is the assumption the decision turns on, with its break-even, tested for sensitivity
([Dahlquist and Knight, 2022](../../references/bibliography.md#dahlquist2022finance)).

```mermaid
flowchart TD
    EST["Team estimate"] --> REF["Apply own overrun history"]
    REF --> SC["Three scenarios"]
    SC --> BOOK["How it is booked"]
    SC --> VAL["Value: Chapter 45 tools"]
    BOOK --> BRK["Decisive input, break-even"]
    VAL --> BRK
    BRK --> ASK["Ask with checkpoints"]
```

The ask ends in checkpoints, where Chapter 49's staging meets the budget: each checkpoint releases or
holds funds.

## Engineering Organization Example

!!! info "Northstar so far"
    Week 47 of the director's first year. Sev1 and Sev2 incidents fell from 30 a quarter to 14 in
    quarter 3, and service credits from $410,000 to $60,000 a quarter, with headcount flat at 80
    engineers. The year-2 budget, organization, and quality continuation are drafted but not decided.
    See the [timeline](../../case-studies/northstar/timeline.md) and the
    [quarter 4 briefing](../../case-studies/northstar/quarter-4-briefing.md).

The figures are **illustrative** and fictional, taken from Northstar's
[finance record](../../case-studies/northstar/first-quarter.md#finances-chapter-52). Northstar reports
under US GAAP (the US accounting standards), and its statements are audited. In week 46, Rajiv Menon
(CFO) sends the executive team Finance's FY1 latest estimate (LE: quarters 1 to 3 actual, quarter 4
forecast) and the draft FY2 envelope for the week 50 board. You are Victor Lindqvist (CTO) in week 47,
reading it before your one-on-one with Rajiv.

**The income statement, FY1 latest estimate ($M).**

| Line | FY1 LE | Note |
|---|---|---|
| Subscription revenue, net of service credits | 140.0 | ARR roughly flat at about $140M |
| Professional services revenue | 5.0 | Implementation and onboarding |
| **Total revenue** | **145.0** | |
| Cost of revenue | 40.6 | Support and success 18.0, services staff 8.5, payment and data fees 6.0, production hosting 3.1, amortization of capitalized software 2.1, other 2.9 |
| **Gross profit** | **104.4** | 72 percent gross margin |
| Research and development | 16.4 | Engineering personnel expensed 13.7, development tooling 1.1, product management 1.6 |
| Sales and marketing | 46.0 | |
| General and administrative | 21.0 | Includes corporate IT and Joon Park's security function |
| **Operating income** | **21.0** | 14.5 percent of revenue |
| EBITDA | 23.9 | 21.0 + 2.1 amortization + 0.8 depreciation |
| Net income | 16.8 | After 1.4 interest income and 25 percent tax |

**Where the $20.3M of engineering spending is.**

| Engineering spending | $M | Where it appears |
|---|---|---|
| Personnel, expensed | 13.7 | R&D expense |
| Personnel, capitalized | 2.4 | Balance sheet asset (about 15.3 [FTE](../../glossary.md#fte)-years at $157,250) |
| Production hosting | 3.1 | Cost of revenue |
| Development tooling | 1.1 | R&D expense |
| **Total** | **20.3** | |

The capitalized rate is 85 percent of the $185,000 fully loaded cost, because office, equipment, and
recruiting overhead may not be capitalized. Earlier years' capitalized work returns as $2.1M of
amortization in cost of revenue. No line equals engineering's budget, so the two views need a
reconciliation the CTO and the controller both sign.

**What the credits did.** Service credits are netted against revenue, so every dollar of credit is a
dollar of operating income. The baseline quarter's $410,000 ran at $1.64M a year; quarter 3's $60,000
runs at $240,000. The difference, about $1.4M a year, is 6.7 percent of FY1 operating income, with no
headcount added: the year-1 quality program in the CFO's lens.

**The balance sheet ($M).**

| Line | End FY0 | End FY1 LE |
|---|---|---|
| Cash | 56.0 | 73.5 |
| Accounts receivable | 17.0 | 17.5 |
| Prepaid and other | 3.0 | 3.0 |
| Capitalized software, net | 4.4 | 4.7 |
| Property and equipment, net | 2.4 | 2.4 |
| **Total assets** | **82.8** | **101.1** |
| Payables and accrued expenses | 6.0 | 6.2 |
| Accrued compensation | 7.0 | 7.3 |
| Deferred revenue | 54.0 | 55.0 |
| **Total liabilities** | **67.0** | **68.5** |
| **Shareholders' equity** | **15.8** | **32.6** |

Deferred revenue is about 39 percent of ARR because most customers pay a year in advance: $55M of
service Northstar owes, and the reason a lost renewal reaches cash before revenue. Equity rose by 16.8,
exactly net income, since there were no distributions or new investment.

**The cash-flow statement, FY1 LE ($M).**

| Line | FY1 LE | Note |
|---|---|---|
| Net income | 16.8 | From the income statement |
| Amortization and depreciation | +2.9 | Non-cash costs added back |
| Working capital | +1.0 | Mostly the growth in deferred revenue |
| **Operating cash flow** | **20.7** | |
| Capitalized software | −2.4 | Investing |
| Equipment | −0.8 | Investing |
| Financing | 0.0 | None |
| **Change in cash** | **17.5** | Also free cash flow, since there is no financing |

**The capitalization test.** Finance has capitalized $1.8M, $2.1M, $2.4M, and $2.4M in FY−2 to FY1,
amortizing each year's amount over the next three years:

| FY1 measure | As reported | If everything were expensed | Change |
|---|---|---|---|
| Operating income | 21.0 | 20.7 | −0.3 (capitalized 2.4 minus amortization 2.1) |
| EBITDA | 23.9 | 21.5 | −2.4 |
| Operating cash flow | 20.7 | 18.3 | −2.4 (ignoring tax effects) |
| Free cash flow | 17.5 | 17.5 | none |

Northstar's capitalization is in steady state: it barely moves operating income, moves EBITDA by 10
percent, and changes no cash. Northstar's minority investor, the growth-equity firm Calder Ridge
Partners, holds two board seats. If it or a future buyer values Northstar on EBITDA, the policy is worth
real money, and the engineering time data under it is a CTO responsibility.

**What Victor takes to Rajiv.** Three things. A reconciliation of the $20.3M to the statements, so
"engineering cost" means one thing in the board pack. The credits line, as the year-1 result in
operating-income terms. And a warning: if the year-2 pack compares investments by income-statement cost,
prevention will look far more expensive than features. A prevention engineer-year shows $185,000 of
expense in the year. A fully capitalized feature engineer-year shows only the $27,750 of overhead that
cannot be capitalized; the rest arrives as amortization later. The cash is identical, so Victor asks
that the pack compare investments in cash and capacity and show the accounting effect separately.

## Decision Framework

Use the lens that fits the question, and say which one you are using.

| Question | Lens | Figure | Common mistake |
|---|---|---|---|
| Can we afford it this year? | Budget and cash | Cash cost, inside or outside the envelope | Treating capitalized cost as "not really spent" |
| Is it worth doing? | Economics (Chapter 45) | Capacity at the fully loaded rate, value, cost of delay | Letting the booking decide the economics |
| How will the board see it? | Income statement and EBITDA | Expensed cost, amortization, capitalized amount | Presenting only the most flattering line |
| What does it commit us to later? | Balance sheet and future budgets | Amortization tail, recurring run cost, impairment risk | Ignoring year-2 and year-3 effects |
| Did we execute? | Variance against budget and forecast | Explained variance by cause | Calling vacancy savings efficiency |

For classifying work, Northstar's policy capitalizes coding and testing on budget-authorized projects
that add functionality. Finance still applies the stage-based guidance, and the amended standard gives
similar answers for these items. Engineering describes the work; finance and the auditors decide.

```mermaid
flowchart TD
    A{"Funding authorized?"} -->|No| X["Expense"]
    A -->|Yes| B{"Development uncertainty resolved?"}
    B -->|No| X
    B -->|Yes| C{"Adds functionality?"}
    C -->|No| X
    C -->|Yes| D{"Coding or testing? (Northstar policy)"}
    D -->|No| X
    D -->|Yes| CAP["Capitalize, then amortize"]
```

| Northstar work item | Likely treatment (Northstar policy) | Why |
|---|---|---|
| Bulk ordering, after scope was fixed | Capitalize the coding and testing | Authorized, requirements settled, new functionality |
| Its discovery and prototyping weeks | Expense | Preliminary stage under the current guidance; unresolved requirements under the amended one |
| Prevention allocation, incident response, flaky-test repair | Expense | Maintenance; no new functionality |
| Permissions extraction inside Core | Expense, unless it delivers new capability | Restructuring that the software could already do |
| Core framework migration (TR-01) | Expense | Keeps existing function on a supported version |
| Training the quality engineers | Expense | Training is excluded |
| Internal tool for service-credit statements | Capitalize if authorized and probable | Internal-use software for Northstar's own operations |

Two guards (**this book's recommendation**): a work item's treatment is recorded when the project is
authorized, not argued after the quarter closes; and the person who benefits from a classification is
never its only author.

## Trade-offs

**Capitalizing versus expensing.** Capitalization raises EBITDA, which some investors and lenders
reward, at the cost of time tracking, audit scrutiny, an amortization tail, and impairment risk.
Expensing everything is simpler but understates investment in the product. The choice is finance's; the
CTO owes accurate data.

**Tracking precision versus its cost.** Ticket tagging is defensible but noisy and resented; project
codes are cheaper and coarser; role percentages are cheapest and least trusted by auditors (Larson,
2023b). Use the cheapest method the auditor accepts, and keep it stable.

**Annual budget versus rolling forecast.** An annual budget is a stable yardstick; a rolling forecast
adapts but needs continual updating. The common hybrid, quarterly reforecasts inside an annual budget,
works if nobody is paid on the forecast.

**Seats versus dollars.** Budget in seats to protect capacity, and report vacancy in dollars with an
agreed rule for its use.

**Cloud commitments versus flexibility.** A committed-use discount (a lower price for promising a cloud
provider a minimum spend for one to three years) turns a variable cost into a fixed one: right for a
stable baseline, wrong for load you may move or remove.

## Failure Modes

**Capitalization drift.** Maintenance relabeled as enhancement as targets tighten. Signal: the
capitalized share rises while unplanned work is flat or rising. Detect: reconcile the capitalized share
with the capacity model's categories each quarter.

**The amortization tail and impairment surprise.** A heavy capitalization year flatters itself and
burdens the next three; a stalled project becomes an unplanned write-off. Detect: a three-year
amortization schedule with every budget, and a review of capitalized projects at each stage gate.

**Sandbagging and use-it-or-lose-it.** Padding invites across-the-board cuts, so everyone pads more,
and quarter 4 purchases cluster to protect next year's baseline. Detect: publish forecast accuracy by
line, and let justified underspend carry forward by agreement.

**Vacancy counted as efficiency.** Unfilled-seat underspend reported as savings and removed from next
year's budget, which then cannot fund the seats. Detect: report vacancy separately, in weeks and dollars.

**EBITDA mistaken for cash.** A plan that "improves EBITDA" by capitalizing more spends the same cash.
Detect: free cash flow next to EBITDA in every board view.

**The single-point case.** One number, written by its sponsor, equal to the budget request. Detect:
require three scenarios built from the organization's own overrun history.

**The unowned variable cost.** Cloud spend reviewed annually by finance instead of weekly by the teams
whose decisions drive it. Detect: weekly cost per service with a named owner.

## Enterprise Application

At 50 to 150 engineers there is no finance team inside engineering. Financial literacy is a practice
shared by the engineering leader, a finance business partner, and the controller, and it rests on four
artifacts:

- **One reconciliation** from the engineering budget to the three statements, updated quarterly; every
  engineering number in the board pack comes from it.
- **A written capitalization method**: which projects are capitalizable, how time is recorded, who
  classifies a project and when. Review it annually and when the standard changes, as it does with ASU
  2025-06.
- **A quarterly variance review** inside the operating reviews of
  [Chapter 39](../08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md).
- **A case threshold**: above a set size (say a quarter of a team's capacity), the business case
  template with scenarios and the booking line.

The transition costs a quarter, and engineers' goodwill if time tracking arrives without its purpose.

## CTO Perspective

First, **the CTO negotiates the envelope, not the lines.** The board approves an operating plan and a
budget envelope; management allocates inside it. Leverage is greatest while Finance drafts and smallest
after the board meets.

Second, **the CTO answers for the integrity of engineering's numbers.** Capitalization rests on
engineering's records. If the method cannot survive an audit or due diligence
([Chapter 55](55-boards-due-diligence-and-executive-decision-making.md)), the CTO's credibility falls
with it.

Third, **the CTO translates between economics and accounting.** Presenting investments in cash and
capacity, with the accounting effect separate, prevents a quiet bias toward whatever is capitalizable.

Fourth, **technology strategy becomes a capital allocation story.** [Chapter 51](51-enterprise-technology-strategy.md)'s three-year strategy
needs this chapter's financial form: cash per horizon, the recurring share, the booking, and the effect
on margin, EBITDA, and free cash flow.

## Practical Playbook

1. **Meet the controller.** Get the audited statements, the accounts engineering touches, and the
   capitalization policy in writing.
2. **Build and agree the reconciliation** from the engineering budget to each statement.
3. **Learn three numbers**: gross margin, operating margin, and what the company is valued on.
4. **Map capacity categories to accounting treatment** before the year starts.
5. **Choose the cheapest tracking the auditor accepts**, write it down, and keep it stable.
6. **Budget in both views**, with a three-year amortization schedule.
7. **Separate budget, forecast, and target**; publish forecast accuracy by line.
8. **Report vacancy and variable cost** each quarter, with causes.
9. **Write large investments with three scenarios**, the booking line, and the decisive input's
   break-even, uplifted by your own estimate history.
10. **Lead with cash and capacity** in every executive and board document; accounting effect second.

[Project 8](../../projects/p8-cto-technology-investment-proposal.md) applies this playbook: you build a
CTO technology investment proposal for Northstar, with scenarios and an accounting note.

## Case Study

This case is **illustrative** and fictional. The extended-support price is an assumption for this case;
the other figures are Northstar's record. Nothing is decided: neither the week 50 board's decision on
the year-2 envelope nor whether TR-01 is funded is recorded.

**The situation.** You are Victor Lindqvist in week 48. TR-01 has been on the technology risk register
since quarter 2: [Core](../../glossary.md#core), Northstar's monolith, runs on an application framework a
major version past free community support, with no extended support bought (Chapter 30). The migration
is estimated at 120 to 180 engineer-days, at Northstar's planning rate of $800 per engineer-day. The
draft year-2 envelope:

| Line | Year 2 ($M) |
|---|---|
| Engineering personnel at full seats ($16.10M, plus 3 percent merit increase $0.483M, plus $0.15M reserve for promotions and market adjustments) | 16.73 |
| Less expected vacancy (Chapter 48) | −0.43 |
| **Personnel after vacancy** | **16.31** |
| Cloud and tooling | 4.2 |

Rajiv Menon wants the quality continuation's $150,000 of tooling offset inside the $4.2M. (The
[continuation](../../glossary.md#the-continuation) is the director's staged proposal to keep the quality
program funded in year 2.) You must decide whether TR-01 is a funded item in the year-2 plan, and how to
describe it to Rajiv and, if asked, the board.

**Three scenarios.** Northstar has a small reference class of its own: recent Orders features grew 15
to 35 percent between start and delivery. Using it as the uplift is a judgment, since a framework
migration is not a feature:

| Scenario | Engineer-days | Cost at $800 | Engineer-weeks displaced | Story |
|---|---|---|---|---|
| Optimistic | 120 | $96,000 | 24 | Low end, no growth |
| Base | about 190 | $152,000 | 38 | Midpoint 150 × 1.25 |
| Pessimistic | about 243 | $194,400 | about 49 | 180 × 1.35, plus a regression found late |

**The booking.** The migration adds no functionality, so it is expensed: $96,000 to $194,400 of FY2
operating expense. The personnel are already budgeted, so it reallocates capacity rather than adding
money. Bundling it with a feature to capitalize part of it would be capitalization drift.

**The alternative.** Extended commercial support, at an assumed $60,000 a year (no quote exists), is
also operating expense, but new money: it lands inside the $4.2M Rajiv wants held flat. It buys time and
patches, not the migration.

**The decisive input.** The economic case rests on the expected loss the migration avoids. A
[tier 1](../../glossary.md#tier-1) framework with no upstream fixes accumulates unpatched
vulnerabilities, while Northstar's remediation service level for critical internet-facing issues is 7
days (Chapter 26). At the base cost, the migration breaks even over three years at the 10 percent rate
if it avoids an expected loss of about $61,100 a year. That is $152,000 divided by the three-year annuity
factor of 2.487: for example, a 1-in-10 yearly chance of a $611,000 event. Nobody at Northstar can yet
defend a probability. The case states the break-even and asks Joon Park (IT security lead) and Ines
Carvalho (staff engineer, Core domain) whether they believe the risk exceeds it.

**The real price.** Money is not the constraint: 24 to 49 engineer-weeks of the few people who can
change Core safely are, displacing other Core work for one or two quarters. That opportunity cost is
the line Amara Okafor (CPO) will read first.

**Victor's draft note to Rajiv (one possible version).** "TR-01 is a reallocation inside the personnel
budget, not new money. Base cost is $152,000 of capacity (range $96,000 to $194,000), expensed, with no
cash effect beyond salaries we already pay. Extended support, at an assumed $60,000 a year, would be new
operating expense inside cloud and tooling and still leaves the migration ahead of us. I propose funding
TR-01 from Core capacity in quarters 5 and 6. A checkpoint after the first 40 engineer-days compares
progress with the scenarios; if it is tracking pessimistic, we decide then whether to buy support for a
year. The price is about 38 engineer-weeks of Core work; Amara and I will name what moves."

**What is open.** Whether Victor sends that note, and whether Rajiv accepts a capacity-funded item in an
envelope he wants flat. How the item interacts with the continuation's stage 2 and the year-2
organization, and what the week 50 board approves (see the
[quarter 4 briefing](../../case-studies/northstar/quarter-4-briefing.md)).

## Exercises

Worked solutions are in the [Chapter 52 solutions](../../solutions/ch52-solutions.md).

### Foundational

**F1.** Using Northstar's FY1 latest estimate in the Engineering Organization Example, compute gross
margin, operating margin, EBITDA margin, and free cash flow as a share of revenue. Then explain to an
engineering manager, in no more than five sentences, why operating cash flow (20.7) is higher than net
income (16.8), and why that does not mean Northstar is hiding profit.

**F2.** Classify each Northstar work item below as capitalize, expense, or "depends, ask finance".
Give the reason in one line under Northstar's policy and the amended standard.

- The new erp-sync connector: four Payments and Integrations engineers built it for the renewal
  commitment, an authorized project that sends posted invoices to a customer's accounting system with
  daily reconciliation.
- The 140 quarantined flaky tests and their fixes.
- The [contract tests](../../glossary.md#contract-test) on tier 1 boundaries, which check that services
  keep the interfaces their consumers rely on.
- The self-service test environments Platform Operations built so teams stop waiting for shared ones.
- The proposed deployment-event store: a shared record of deployments for delivery measurement, about
  six engineer-weeks taken from the prevention allocation, not a budget-authorized project.

Add two hypothetical items that are not part of Northstar's record. Suppose Orders had spent six weeks
defining bulk ordering's scope with the renewal customer before the requirements settled. Suppose also
that moving customer records into a new schema needed a one-off data conversion.

**F3.** Suppose Finance proposed that Northstar stop capitalizing entirely from the start of FY2, while
the engineering work stays the same as in FY1. Using the chapter's capitalization history, describe
the effect on FY2 operating income, EBITDA, operating cash flow, and free cash flow. Explain which of
those changes Calder Ridge Partners would care about and why.

### Applied Leadership

**A1.** Rajiv Menon wants the quality continuation's $150,000 of stage 2 tooling offset inside the
$4.2M cloud and tooling budget. Draft three offset options (one in production hosting, one in
development tooling, one using expected personnel vacancy), with the assumptions each requires, its
effect on gross margin or operating expense, and its risk. Recommend one and write the paragraph you
would send Rajiv.

**A2.** Chapter 30's tax-svc decision (how Northstar calculates sales tax) has three options:

- build out: 120 engineer-days upfront, then 0.5 FTE a year;
- buy a commercial engine: a $150,000 a year subscription, 80 engineer-days of integration, 0.15 FTE;
- hybrid: $45,000 a year of rate content, 70 engineer-days, 0.25 FTE.

For year 1 of each, show the likely effect on operating expense, EBITDA, and cash. Assume the
build-out's upfront work is capitalizable and the integrations are not. Then explain which option each of Rajiv Menon, Greg Tanaka,
and Victor Lindqvist would find most attractive on those figures, and why the figures should not
decide it.

**A3.** In week 47, Greg Tanaka argues that moving 2 of the 6 prevention engineers to his deal features
in quarters 5 and 6 "costs the company nothing and actually improves profit, because feature work gets
capitalized". Using the chapter's figures, assess each part of that claim, and write the three or four
sentences the director should put in the continuation proposal so the executive team compares the
options correctly.

### Executive Decision-Making

**X1.** You are Victor Lindqvist in week 48. Using the Case Study, decide whether to put TR-01 in the
year-2 plan, buy extended support, or do both in sequence, and set the checkpoint rule. Then write the
two-sentence version you would use if a board member asked about it in week 50, and state what evidence
would make you reverse your decision during year 2.

**X2.** Suppose, hypothetically, that you are CTO of Halvard Systems (500 engineers, payroll about
$102.9M). A debt refinancing will be priced on EBITDA. The CFO proposes raising the capitalized share of
engineering payroll from 18 to 28 percent by reclassifying platform and reliability work as
enhancements. This scenario is not part of Halvard's record. Quantify the effect on EBITDA and cash,
assess it against the standard's criteria, and write your response to the CFO, including what you
would offer instead.

## Reflection Questions

1. Could you reconcile your organization's engineering budget to the income statement today? If not,
   who in your company can, and what does that say about who controls engineering's story?
2. Which of your organization's projects would look different if prevention and features were compared
   in cash and capacity rather than income-statement cost?
3. When did you last pad an estimate, and what in your budget process rewarded it?
4. Does anyone in engineering see the cloud bill weekly? If cost were a quality attribute, who would
   own it?
5. If an auditor or an acquirer asked tomorrow how your capitalized hours were recorded, would the
   answer survive the question that follows?

## Key Takeaways

- One set of events, three lenses: income statement, balance sheet, cash flow. Say which lens a
  number comes from before arguing about it.
- Capitalization changes timing and presentation, never cash or capacity. Decide on economics; report
  the booking separately.
- In steady state, capitalization barely moves operating income but raises EBITDA by the full
  capitalized amount. Know your company's rate and its trend.
- Capitalize only authorized work, with uncertainty resolved, that adds functionality; maintenance,
  training, and overhead are expensed. Finance and auditors decide; engineering's records must be
  accurate.
- Build the budget in two views, by function and by accounting treatment, with one reconciliation
  table both the CTO and the controller sign.
- Keep budget, forecast, and target separate, and report vacancy and variable cost explicitly.
- Write investment cases with three scenarios, your organization's own overrun history, the booking
  line, and the decisive input's break-even.
- Service credits are refunded revenue: reliability improvements reach operating income dollar for
  dollar, which is often the strongest sentence a CTO can give a board.

## References and Further Reading

- [SEC, 2014](../../references/bibliography.md#sec2014beginners). The SEC's beginners' guide to the
  financial statements; clear standard definitions, free.
- [FASB, 2025](../../references/bibliography.md#fasb2025asu202506). ASU 2025-06 on internal-use
  software; its four-page summary is readable by engineers and states the new capitalization threshold
  (paragraph 350-40-25-12A on development uncertainty, 350-40-35-3 on impairment, BC13 on cloud
  arrangements). It applies to annual periods beginning after December 15, 2027, with early adoption
  allowed.
- [IFRS Foundation, IAS 38](../../references/bibliography.md#ifrs-ias38). The international standard
  for intangible assets, for companies reporting under IFRS.
- [Aboody and Lev, 1998](../../references/bibliography.md#aboody1998software). The classic study of
  software capitalization and investors; read for the steady-state effect and its limits.
- [Larson, 2023b](../../references/bibliography.md#larson2023capitalize). An engineering executive's
  practical account of capitalization tracking methods and how to choose one.
- [Larson, 2023a](../../references/bibliography.md#larson2023planning). Annual financial planning from
  the engineering executive's seat: the annual plan, portfolio allocation, and roadmap.
- [Larson, 2024](../../references/bibliography.md#larson2024primer). The engineering executive's job
  as a whole, including planning.
- [Franklin et al., 2019](../../references/bibliography.md#franklin2019managerial). An open textbook
  chapter on why and how managers budget, including slack and gaming.
- [Hansen et al., 2003](../../references/bibliography.md#hansen2003budgeting). Research perspective on
  improving versus abandoning budgets.
- [Hope and Fraser, 2003](../../references/bibliography.md#hope2003budgets). The case against
  traditional budgeting, from the Beyond Budgeting movement.
- [Berman and Knight, 2006](../../references/bibliography.md#berman2006financial). Financial
  statements for non-financial managers, with an emphasis on where judgment enters.
- [Flyvbjerg, 2006](../../references/bibliography.md#flyvbjerg2006nobel). Optimism bias, strategic
  misrepresentation, and reference class forecasting; the basis for scenario uplifts.
- [Kahneman et al., 2011](../../references/bibliography.md#kahneman2011bigdecision). Checking a team's
  recommendation for bias before a large decision.
- [Dahlquist and Knight, 2022](../../references/bibliography.md#dahlquist2022finance). Payback and NPV,
  with the advice to test sensitivity.
- [FinOps Foundation](../../references/bibliography.md#finops-what-is). The practitioner framework for
  shared financial accountability in cloud spending.

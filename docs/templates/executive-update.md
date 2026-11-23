# Executive update

**Used in:** [Chapter 39](../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md)
(reviews, decision logs, escalation, and executive reporting),
[Chapter 49](../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md)
(the CTO and the executive team).
**Owner:** the engineering director (to the CTO) or the CTO (to the CEO and executive team); managers
supply facts, the author writes the headline.
**Cadence:** monthly, at most two pages, plus an unscheduled update within a day when a customer
commitment changes color. The quarterly version is the [Quarterly engineering review](quarterly-engineering-review.md),
which is longer and ends a planning cycle; this one is for the months in between.

An executive update tells a busy reader, in the first three lines, what changed, what is at risk, and
what decision is needed from them. Everything after the headline supports it. The update is not a status report of activity. A reader should be able to act on it without a
meeting, and should never learn something important about engineering from someone else first.

!!! tip "Minimum version"
    On day one, send three things: a two-sentence headline, the same three to five measures every time
    with a one-phrase reading, and each decision you need with a deadline. Add the commitments table,
    risks, and "decided since last time" in the second month.

## How to fill it in

1. **Write the headline last, and put it first.** Two to four sentences: the main result, the main
   gap, and the number of decisions needed. Bad news belongs in the headline if it would change what
   the reader does.
2. **List customer and executive commitments with defined colors.** Green: forecast inside the date
   with known risks covered. Amber: forecast at risk, recovery plan exists and needs nothing from the
   reader. Red: will miss without a decision from the reader. A color without a forecast is not a
   status.
3. **Show the same measures every time,** including the flat and the worse ones, with a one-phrase
   reading. Small counts get "direction only". Never drop a measure because it moved the wrong way.
4. **Name what went wrong** since the last update, with the response. A run of updates with nothing
   wrong is not believed.
5. **Risks:** at most three, each with an owner and the date or trigger at which you will ask for
   help.
6. **Decisions needed:** each with options, your recommendation, the deadline, and what happens if
   it is decided late.
7. **Decided since last time:** a line per decision taken below the reader's level, so that the
   reader sees the escalation path working.
8. **Mark what you do not know.** A figure not yet measured is written as not recorded, never
   estimated silently.

## Template

```markdown
**Engineering update to <reader>, <period> (<date>)**

**Headline.** <main result>. <main gap>. <n> decisions needed from you by <date>.

| Commitment | Due | Status | Forecast and note |
|---|---|---|---|

| Measure | Last period | This period | Reading |
|---|---|---|---|

**What went wrong.** <what, effect, response>
**Risks.** (1) <risk>. Owner: <name>. I will ask for <help> if <trigger> by <date>.
**Decisions needed.** (1) <question>: options <A/B>; I recommend <A> because <reason>;
needed by <date>; if late, <consequence>.
**Decided since last update.** <decision, decider, logged as>
```

```yaml
update:
  to: ""
  from: ""
  period: ""
  sent: ""
headline: ""
commitments:
  - {item: "", owner: "", due: "", status: "", forecast: "", note: ""}   # green / amber / red / delivered
measures:
  - {name: "", previous: "", current: "", reading: ""}                   # "not recorded" where unknown
went_wrong:
  - {what: "", effect: "", response: ""}
risks:
  - {risk: "", owner: "", ask_trigger: ""}
decisions_needed:
  - {id: D1, question: "", options: [], recommendation: "", needed_by: "", if_late: ""}
decided_since_last:
  - {decision: "", decider: "", log_id: ""}
```

## Example: Northstar, end of quarter 3 (sent week 40)

!!! info "Northstar so far"
    Week 40 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Quarter 3 is the first quarter at the CTO's incident target; the renewal features shipped in quarter
    2. The director writes to Victor Lindqvist (CTO). See the
    [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Figures come from [quarter 3 results](../case-studies/northstar/first-quarter.md#quarter-3-results).
Delivery of the cross-team initiatives is not recorded, so the update says **not recorded**, which is
how a real update should show a figure not yet in hand. The wording, the risks' triggers, and the ask
are illustrative. People named: Greg Tanaka (VP Sales), Sofia Alvarez (VP Customer Success), Rajiv
Menon (CFO), Amara Okafor (CPO), Marcus Oyelaran and Priya Raman (Billing and Orders managers).
The core/permissions module is a [tier 1](../glossary.md#tier-1) part of Core, the monolith, that four
teams change; its temporary exemption from having an owner has lapsed. Weeks count from the director's
first week; the [mandate](../glossary.md#the-mandate) is the CTO's target of 15 or fewer Sev1 and Sev2
incidents a quarter. The forum is the week 34 portfolio forum on a third deal feature, purchase approval
rules, that Greg Tanaka requested in week 31.

> **Engineering update to Victor Lindqvist, end of quarter 3 (week 40)**
>
> **Headline.** The quarter ran on the first plan with an explicit unplanned-work band (22 percent
> planned, 28 percent cautious) and a limit of three cross-team initiatives. Quarter 3 came in at 14
> Sev1 and Sev2, the first quarter at or below the mandate's 15, but availability was 99.89 percent,
> still under the 99.9 percent commitment ($60,000 in credits). One thing I started failed:
> Engineering Excellence Day, which I have stopped. The core/permissions exemption lapsed at the end
> of week 39 with no owner, and I need one decision from you about it.
>
> | Commitment | Due | Status | Forecast and note |
> |---|---|---|---|
> | Multi-currency price lists (Greg Tanaka) | Forecast week 38 | not recorded | Date already given in an open deal |
> | Catalog export (Greg Tanaka) | Forecast week 34 | not recorded | |
> | Customer incident status notifications (Sofia Alvarez) | Forecast week 33 | not recorded | |
> | Automated service-credit statements (Rajiv Menon) | Start about week 33 | not recorded | Depends on the week 34 forum outcome |
>
> | Measure | Quarter 1 | Quarter 2 | Quarter 3 plan | Quarter 3 |
> |---|---|---|---|---|
> | Sev1 and Sev2 incidents | 21 | 17 | | 14 (2 Sev1) |
> | Unplanned work | 31% | 28% | 22% (cautious 28%) | 25%, inside the band |
> | Tier 1 at four operational minimums | 8 of 15 | 11 of 15 | | 13 of 15 |
> | Availability, order and payment paths | not recorded | 99.86% | 99.9% (contract) | 99.89%; credits $60,000 |
>
> **What went wrong.** I launched Engineering Excellence Day in week 27 without the managers or
> Amara Okafor. Participation fell from 64 to 41 to 23 engineers; 71 items merged, none from the
> priced debt register, and one core/scheduler change caused a Sev3. I stopped it in week 37 and
> wrote to the managers.
>
> **Risks.** (1) core/permissions has no owner and no exemption. Owner: me. (2) Ledger knowledge is
> still concentrated in three Billing engineers. Owner: Marcus Oyelaran. (3) Purchase approval rules:
> whichever option the forum takes, a dated commitment depends on Orders, which already leads
> multi-currency. Owner: Priya Raman.
>
> **Decision needed.** (1) Owner for core/permissions: renew the exemption for one quarter, or settle
> ownership in the year-2 organization proposal I will bring you in week 44. I recommend the
> proposal, with no renewal; renewing would stretch an exemption already at its two-quarter maximum,
> for a tier 1 module that four teams change. If late, the module stays unowned into year 2.
>
> **Decided since last update.** The first calibrated promotion cycle: 9 nominated, 5 promoted,
> 4 "not yet".

What to notice: the headline puts the miss on availability next to the incident result instead of
behind it, and the failure is owned in the first person. The commitments table still says not
recorded for all four initiatives; that is better than a complete-looking table assembled from
guesses. A real update would fill those cells first; if it could not, it would say when they will
arrive.

## Common mistakes

- **Activity instead of outcome.** "Held 12 design reviews" tells the reader nothing they can act on.
- **Watermelon status.** Green outside, red inside: colors without forecasts, or colors chosen to
  avoid a conversation.
- **Dropping the bad measure.** A measure that disappears the month it worsens costs more trust than
  the bad number would have.
- **Decisions buried at the end of paragraphs.** Each ask is numbered, with a date and the cost of
  lateness.
- **Surprises.** If the reader would have wanted to know within a day, the monthly update is too late.
- **Length.** A five-page update is read as one page: the first.

## Review questions

1. If the reader read only the headline, would they do the right thing?
2. Which measure would you be tempted to leave out this month, and is it in?
3. Does every decision needed say what happens if it is decided late?
4. Is there anything in this update the reader has already heard from someone else?

## Evidence and references

The method is [Chapter 39](../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md).

- [Minto, 2002](../references/bibliography.md#minto2002pyramid): the pyramid principle, known for
  stating the governing point first and grouping the support beneath it (**expert opinion**). It is
  the reason the headline comes first.

The color definitions, the fixed measure set, and the "decided since last time" line are **this
book's recommendation**.

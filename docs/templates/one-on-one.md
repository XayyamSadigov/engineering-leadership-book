# 1:1 template

**Used in:** [Chapter 5](../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md)
(one-on-ones, coaching, and mentorship), [Chapter 9](../parts/02-people-management/09-performance-management-and-underperformance.md)
(performance management, where the record replaces recollection),
[Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)
(managing managers, whose one-on-ones follow the same design).
**Owner:** the report owns the agenda; the manager owns the record and every commitment made in it.
**Cadence:** weekly or every two weeks, set per person; a five-minute record after each meeting; a
three-line summary each month; a channel check every six weeks.

A one-on-one is a recurring private meeting between a manager and one report. It is an information
channel owned by the report, and its value is the news it carries: what the manager could not have
learned from the board, the chat, or the stand-up. This template has three parts. A shared running
document puts the report's topics first and keeps status out. A record, written in five minutes
afterwards, turns the meeting into dated evidence for reviews and promotions. A six-week check counts
whether the channel still carries news, because the manager's own impression is the least reliable
judge of that.

!!! tip "Minimum version"
    On day one, use only Part 1 (the shared document: the report's topics first, then commitments both
    ways) and the "News" line of Part 2. Add the rest of the record after a month, and the six-week
    check once you have six weeks of entries.

## How to fill it in

1. **Open one running document per report,** newest entry at the top, shared with them. Head it "Your
   agenda first; status lives elsewhere." Status comes from the board and a three-line written update
   (done, next, stuck), not from the meeting.
2. **Set the cadence per person,** not per team: weekly for someone new, someone others depend on, or
   someone whose work is changing fast; every two weeks for an established engineer with clear scope.
   Record the reason. Below every two weeks the channel loses continuity; if a span forces that, the
   span is the problem (Chapter 34).
3. **Before the meeting, the report adds topics.** The manager adds theirs underneath. If the report's
   section is empty, ask what is on their mind and wait; if it stays empty, use one deeper question from
   the rotation.
4. **Open by closing the manager's commitments from last time.** The report is watching what happened
   to the last thing they raised.
5. **Shorten rather than cancel.** A meeting moved three times tells the report where they rank.
6. **Within five minutes afterwards, write the record:** topics the report raised, commitments both
   ways with dates, observations (specific behavior, its effect, date, source), growth (their stated
   goal and what moved toward it), and sponsorship actions. Mark the meeting "news: yes" only if you
   learned something no other channel showed.
7. **Keep out** speculation about motives, health details, protected characteristics, and gossip. Write
   as if the person will read it one day; HR can tell you whether they may.
8. **Once a month,** write three lines: what this person did, what they are working toward, what you owe
   them.
9. **Every six weeks,** count the decay signals from the record. Once a quarter, ask the report in
   writing what the meetings should do more of and less of, and weight specifics over ratings.

## Template

**Part 1. The shared running document (one entry per meeting)**

| Field | Meaning |
|---|---|
| Date and length | Booked and actual minutes; "moved" or "cancelled", and by whom |
| Report's topics | Added by the report before the meeting, in their words |
| Manager's topics | Added below the report's; never status |
| Last time's commitments | Each commitment from the previous entry: kept, late, or dropped, with a reason |
| New commitments | Who, what, by when; both directions |

**Part 2. The manager's record (written within five minutes)**

| Field | Meaning |
|---|---|
| News | Yes or no: did you learn something the board, chat, or stand-up did not show? One line on what |
| Topic type | Work, people, growth, the manager, personal (one or more) |
| Observations | Behavior, effect, date, source. "Led the incident review on 3 March; every action had an owner" is evidence; "strong communicator" is not |
| Growth | Their stated goal and what moved toward it |
| Mode of help used | Directing, coaching, mentoring, or sponsoring (Chapter 5), and whether the goal needed that mode |
| Sponsorship actions | Opportunities you proposed them for, and the result |

**Part 3. The six-week channel check**

| Signal | Count from the record | Healthy (illustrative) | Decayed (illustrative) |
|---|---|---|---|
| News rate | Meetings with news ÷ meetings held | A third or more | Under one in seven |
| Agenda source | Meetings where the report added topics | Most weeks | Manager's topics every time |
| Topics | Topic types seen in six weeks | Work, people, growth, the manager | Work only |
| Cancellations | Moved or cancelled, and by whom | Rare, rescheduled | Frequent; mostly the manager |
| Surprises | Things learned about this report from someone else | Few, and foreseen | Resignation, conflict, or burnout learned elsewhere |

**Deeper questions for a light agenda (rotate):** What is the most frustrating part of your week? What
kind of work do you want more of in a year? What am I doing that gets in your way? What did you decide
not to raise with me this month? Who on another team makes your work harder, and how?

```yaml
one_on_one: {report: "", manager: "", cadence: "", cadence_reason: ""}
entries:
  - date: ""
    minutes: 0
    moved_or_cancelled: ""        # blank, or "moved by manager", "cancelled by report", ...
    report_topics: []
    manager_topics: []
    commitments: []               # {owner, item, due, result: kept / late / dropped}
    record:
      news: false                 # plus one line on what
      topic_types: []             # work / people / growth / manager / personal
      observations: []            # {date, behavior, effect, source}
      growth: ""
      mode_of_help: ""            # directing / coaching / mentoring / sponsoring
      sponsorship: []
monthly_summary: []               # {month, did, working_toward, owed_by_manager}
```

## Example: Northstar, Daniel Cho and Mateo Arango Ríos (quarter 2)

!!! info "Northstar so far"
    Week 19 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Daniel Cho manages Customer Experience: 15 web and mobile engineers, 17 reports with the two quality
    engineers who joined in week 10. Mateo Arango Ríos is the team's informal mobile lead in Bogotá. See
    the [timeline](../case-studies/northstar/timeline.md) and the [cast](../case-studies/northstar/cast.md).

**The channel check, weeks 14 to 19 (Part 3).** The director recoded Daniel's records for six weeks.
The two quality engineers were left out of the sample as too recent.

| Signal | Count | Reading |
|---|---|---|
| News rate | 11 of 84 held (13 percent) | Decayed: under one in seven |
| Agenda source | 79 of 84 opened from Daniel's questions | Decayed: the manager's template every time |
| Topics | Status or blockers already on the board 64; career or growth 8 (with 6 people); team or process 7; personal 5 | Mostly work; 9 of 15 engineers had no career conversation in six weeks |
| Cancellations | 90 scheduled, 84 held, average 26 minutes | Healthy on attendance, which is the measure that misleads |
| Surprises | Mobile rated four areas red in the week 16 team health check; in week 17 Mateo told the director, not Daniel, that he had done a lead's job for over a year | Decayed: both learned through other channels |

The two informal leads' 12 meetings were all dominated by platform-wide status. Mateo described his as
"where I tell Daniel where mobile is."

**Mateo's first entry under Daniel's week 19 draft (Parts 1 and 2, before the meeting).** The layout is
illustrative, and whether Daniel adopts the draft is not recorded.

| Field | Entry |
|---|---|
| Cadence and reason | Weekly, 30 minutes: Mateo is a lead others depend on |
| Report's topics | Left empty for Mateo. Daniel does not fill it |
| Manager's topics | 1. What the mobile group asked for in the health check: "our own board, and decisions that happen where we can hear them." 2. How Mateo wants the lead work he has done to be recognized |
| Status | Moved to the three-line weekly written update; not discussed |
| Observations (with source) | Leads mobile technical direction without a title for over a year (baseline). Week 16: the mobile group's request in his words (health check, shared with the group's agreement). Week 17: raised the unrecognized lead work with the director, who passes it on with Mateo's agreement |
| Growth | Not yet asked; Mateo states it in his own words |
| Mode of help | Open. Recognition of lead work is a sponsorship question, not a coaching one |
| Sponsorship action | Open: propose him as a named tech lead (needs the director's agreement) or start with smaller opportunities |

What to notice: by attendance, Daniel's practice looked excellent (84 of 90 held). By the measure that
matters it carried news in 13 percent of meetings, and the two largest pieces of news about his own
team reached him through a health check and through his manager. The draft fixes the cause, not the
frequency: the report's section comes first, and status leaves the meeting.

## Common mistakes

- **Measuring attendance.** A held meeting that carries only status has a perfect record and a broken
  channel. Count news.
- **The manager's agenda in the report's meeting.** "What are you working on, any blockers?" is a status
  meeting; status lives on the board.
- **Commitments that disappear.** If the manager's promises are not closed at the start of the next
  meeting, the report stops raising things.
- **Cancelling instead of shortening.** Repeated moves tell the report where they rank.
- **Notes written from memory at review time.** The record exists so that February is not forgotten in
  December; five minutes after each meeting is the whole cost.
- **Writing what you would not want the person to read.** Motives, health, and gossip do not belong in
  the record.
- **One cadence for the whole team.** The person new to the team and the established specialist need
  different rhythms.

## Review questions

1. In the last six weeks, what did you learn from this person that no other channel showed you?
2. Who set the agenda in each of the last six meetings?
3. Which of your commitments to this person is overdue, and does the record say so?
4. What did you learn about this report from someone else this quarter?
5. When did this person last talk with you about their career, and what did you do about it?

## Evidence and references

The method is [Chapter 5](../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md),
which also gives the cadence table and the four modes of help.

- [Rogelberg, 2024](../references/bibliography.md#rogelberg2024unlocking): in a researcher's summary of
  his survey work, meetings were rated highest when the report created the agenda, and managers' ratings
  of their own one-on-one skill appeared inflated. That is **expert opinion** informed by survey data
  whose methods the summary does not describe.
- [Grove, 1983](../references/bibliography.md#grove1983high): *High Output Management*, the book known
  for treating the one-on-one as the subordinate's meeting (**expert opinion**).

The fields, the thresholds in Part 3 (marked illustrative), and the five-line record are **this book's
recommendation**.

# 1:1 template

!!! warning "Awaiting human review"
    This template has passed the book's automated validation and an editorial self-review, but not yet
    the human review in which each cited claim is checked against its source. Treat it as a reviewed
    draft. Corrections are welcome; see the repository's CONTRIBUTING file.

**Used in:** Chapter 5 (one-on-ones, coaching, and mentorship), Chapter 9 (performance management,
where the record replaces recollection), Chapter 41 (managing managers, whose one-on-ones follow the
same design).
**Owner:** the report owns the agenda; the manager owns the record and every commitment made in it.
**Cadence:** weekly or every two weeks, set per person with Chapter 5's cadence table; a five-minute
record after each meeting; a three-line summary each month; a channel check every six weeks.

A one-on-one is an information channel owned by the report, and its value is the news it carries:
what the manager could not have learned from the board, the chat, or the stand-up
([Chapter 5](../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md)). This template
has three parts that serve that purpose. A shared running document puts the report's topics first and
keeps status out. A record, written in five minutes afterwards, turns the meeting into dated evidence
for reviews and promotions. A six-week check counts whether the channel still carries news, because the
manager's own impression is the least reliable judge of that.

The design follows the two points the evidence and the practitioner tradition agree on. In a researcher's
summary of his survey work, meetings were rated highest when the report created the agenda, and
managers' ratings of their own one-on-one skill appeared inflated
([Rogelberg, 2024](../references/bibliography.md#rogelberg2024unlocking)); that is **expert opinion**
informed by survey data whose methods the summary does not describe. Treating the one-on-one as the
subordinate's meeting is the idea Grove's *High Output Management* is known for
([Grove, 1983](../references/bibliography.md#grove1983high)), which is **expert opinion**. The
fields, thresholds, and the five-line record are **this book's recommendation**.

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
| Mode of help used | Directing, coaching, mentoring, or sponsoring (Chapter 5's diagram), and whether the goal needed that mode |
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
one_on_one:
  report: ""
  manager: ""
  cadence: ""              # weekly / every two weeks
  cadence_reason: ""
  minutes_booked: 0
entries:
  - date: ""
    minutes_actual: 0
    moved_or_cancelled: ""  # blank, or "moved by manager", "cancelled by report", ...
    report_topics: []
    manager_topics: []
    previous_commitments:
      - {owner: "", item: "", due: "", result: ""}   # kept / late / dropped: reason
    new_commitments:
      - {owner: "", item: "", due: ""}
    record:
      news: false
      news_note: ""
      topic_types: []      # work / people / growth / manager / personal
      observations:
        - {date: "", behavior: "", effect: "", source: ""}
      growth: ""
      mode_of_help: ""     # directing / coaching / mentoring / sponsoring
      sponsorship: []
monthly_summary:
  - {month: "", did: "", working_toward: "", owed_by_manager: ""}
channel_check:
  window: {start: "", end: ""}
  held: 0
  with_news: 0
  report_added_topics: 0
  topic_types_seen: []
  moved_or_cancelled: {by_manager: 0, by_report: 0}
  surprises: []
  quarterly_written_feedback: {more_of: "", less_of: ""}
```

## Example: Northstar, Daniel Cho and Mateo Arango Ríos (quarter 2)

**Fictional.** Every fact below is canon, from the [baseline data](../case-studies/northstar/baseline-data.md),
the [first quarter](../case-studies/northstar/first-quarter.md) page, and the case studies of Chapters
5 and 14. The layout of the entry, and Daniel's choice of what to write in it, are illustrative and
written for this template; the canon leaves Daniel with a draft, and no outcome of that draft is
recorded here.

**The channel check, weeks 14 to 19 (Part 3, filled in from Chapter 5's recode).** Daniel Cho manages
15 engineers in Customer Experience (17 reports from week 10, counting the two quality engineers, who
were left out of the sample as too recent).

| Signal | Count | Reading |
|---|---|---|
| News rate | 11 of 84 held (13 percent) | Decayed: under one in seven |
| Agenda source | 79 of 84 opened from Daniel's questions | Decayed: the manager's template every time |
| Topics | Status or blockers already on the board 64; career or growth 8 (with 6 people); team or process 7; personal 5 | Mostly work; 9 of 15 engineers had no career conversation in six weeks |
| Cancellations | 90 scheduled, 84 held, average 26 minutes | Healthy on attendance, which is the measure that misleads |
| Surprises | Mobile rated four areas red in the week 16 health check; in week 17 Mateo told the director, not Daniel, that he had done a lead's job for over a year | Decayed: both learned through other channels |

The two informal leads' 12 meetings were all dominated by platform-wide status. Mateo described his as
"where I tell Daniel where mobile is."

**What the first entry of Mateo's running document would hold under Daniel's week 19 draft (Parts 1
and 2, before the meeting; illustrative, since whether Daniel adopts the draft is open).**

| Field | Entry |
|---|---|
| Cadence and reason | Weekly, 30 minutes (cadence D in Chapter 5): Mateo is a lead others depend on |
| Report's topics | Left empty for Mateo. Daniel does not fill it |
| Manager's topics | 1. What the mobile group asked for in the health check: "our own board, and decisions that happen where we can hear them." 2. How Mateo wants the lead work he has done to be recognized |
| Status | Moved to the three-line weekly written update; not discussed |
| Observations to record (with source) | Baseline: leads mobile technical direction without a title for over a year (baseline page). Week 16: the mobile group's request in his words (health check, shared once with the group's agreement). Week 17: raised the unrecognized lead work with the director, who brings it with Mateo's agreement (director) |
| Growth | Not yet asked; Mateo states it in his own words |
| Mode of help | Open. Recognition of lead work is a sponsorship question, not a coaching one |
| Sponsorship action | Open in Daniel's draft: propose him as a named tech lead (needs the director's agreement and changes how other teams work with Customer Experience) or start with smaller opportunities |

What to notice: by attendance, Daniel's practice looked excellent (84 of 90 held). By
the measure that matters it carried news in 13 percent of meetings, and the two largest pieces of news
about his own team reached him through a health check and through his manager. The draft entry addresses the
cause, not the frequency: the report's section comes first and stays empty until Mateo fills it, and
status leaves the meeting entirely. The record's observations each carry a source, so that when
Chapter 41's question "who on your team is doing a piece of your job?" is asked, Daniel can answer from
evidence rather than memory.

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

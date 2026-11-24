# Meaning check, batch 15: chapters 43 and 44

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batches 8 to 14:

1. Every doubt in `editing-ch43.md` and `editing-ch44.md` section 4 and in the translator's notes
   (`notes-t16.md`) gets a verdict.
2. Completeness: headings (43: 27; 44: 26), table lines (43: 39; 44: 55), list items (43: 27; 44: 25),
   ordered items (43: 20; 44: 25), exercises (8 each), Mermaid blocks (3 each), admonitions (43: 2;
   44: 1), paragraphs per section, and relative link targets (34 and 39, identical in order) match the
   English. Every number in table lines is identical to the English. No wrapped line begins with a
   number and a period outside a real ordered list. Table rows, exercises, reflection questions,
   takeaways, and reference lines were also checked by eye: nothing is missing. All admonitions keep
   their body indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. Evidence labels
   were checked one by one; Northstar names and numbers were checked against the English.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 12 editor doubts plus the translator's notes checked; none led to a change. Further fixes from
the full read: ch 43 ×5, ch 44 none.
Validation: `tools/validate_book.py` passed.

## Chapter 43

| # | Doubt | Verdict |
|---|---|---|
| 1 | X1, «На этом совещании Amara Okafor уже назвала Excellence Day „потерянной неделей“» | ok. The English: "for his staff meeting with the other executives, where Amara Okafor has already called it 'a lost week of roadmap'"; "where" is the meeting. |
| 2 | Launch, «Правила: никаких встреч…» | ok. The English lists the rules ("There would be no meetings, results would be posted on the Monday, and on-call engineers were exempt"); the frame word adds nothing. |
| 3 | Diagnosis, «один день раз в четыре недели» | ok. The English: "a day every four weeks". |
| 4 | Self-assessment, «проверить по хронике года 1, какие типичные провалы были в кварталах 1 и 2» | ok. The English: "look at quarters 1 and 2 against the failure patterns, using the year 1 record". |
| 5 | «Поэтому проверкой служит просмотр списка обязательств руководителем» | ok. The English joins the clauses with a semicolon ("the same person chose the evidence and the verdict; the manager's review of the commitments list is the check"); the second clause answers the first, so the causal link is in the source. Unlike batch 14 (ch 42, doubt 2), the connective states a logic the English implies. |
| 6 | Trade-offs, «признав ошибку, они ослабят свои позиции» | ok. The English: "admitting a mistake weakens them". |
| t16 | "credibility" → «репутация» in Why This Matters, «доверие» elsewhere | ok. |
| t16 | "design" of a change → «проект» | ok. |
| t16 | "1.0 each" → «по 1.0» | ok; number verbatim. |
| t16 | "Day 2 fell on Billing's period-close support" → «поддержка закрытия периода в Billing» | ok. |
| t16 | "merged" → «смёржено» (editor applied it, per the Northstar pages) | ok. |
| t16 | "escalation of commitment" → «эскалация приверженности» | ok; the chapter's own note on bare "escalation" is kept. |

Further fixes:
- Why This Matters, organization scale: "gets compliance in meetings and workarounds in the work" had
  become «на встречах директор получит согласие». Compliance is outward going-along, not agreement; the
  chapter's whole point is that agreement is missing. Now «получит видимое согласие».
- Trade-offs, carriers versus speed: "A safety or security change with a deadline" had become
  «Изменение в области надёжности или безопасности»: "safety" is not reliability. «безопасность» covers
  both safety and security, so now «Изменение в области безопасности с жёстким сроком».
- Engineering Organization Example: "leaving almost nothing for an incident or a resignation" had become
  «чьего-то увольнения» (which can read as a dismissal). Now «чьего-то ухода».
- Case, self-assessment table, decision vacuum: the reading "At risk" had become «Под угрозой»
  ("threatened"), which says something is endangered rather than that the pattern is a risk. Now
  «Есть риск».
- X1: "what you ask of Amara for the next change" had become «перед следующим изменением» (before).
  Now «для следующего изменения».

Full read: no other drift. The opening and related-chapters box, the three scales, the objectives, the
mental model and loop diagram (the editor's two-sentence note keeps both clauses), Kotter (expert
opinion; more than 100 companies; the five errors), Hughes (research finding as the abstract reports it;
five sources), Oreg et al. (79 studies; the one point taken), Kane et al., Rumelt, Lencioni, Weick and
Watkins (expert opinion), the four diagnosis questions, the carriers test, the pilot and reinforcement
sections, the engineer-communication paragraph (this book's recommendation), the eight-row failure
patterns table (this book's recommendation), Staw and the escalation diagram, Kim et al. (two
experiments; the transfer labeled as the book's inference), the four recovery parts, the example (110
engineers, 12 teams, 9 managers; 45 hours, 85 percent, 7, 5, 70, 1.5, 90 percent), the decision table
and diagram, five trade-offs, six failure modes, the enterprise section, the CTO section, the 11-step
playbook, the case (week 27; 12 to 8 FTE; weeks 28, 32, 36; Kwame Mensah, Amara Okafor; 240
engineer-days, 48 engineer-weeks, 3.7 FTE; the three-day table; 25.6; 71 = 52 + 9 + 10; the Sev3
scheduler delay, week 29; Marcus Oyelaran and Farah Haddad, 26 engineers, 54, 5, 8, 41; the pulse
52 = 11 + 29 + 12; the four errors and two commitments; the seven-row self-assessment), all exercises,
reflection questions, takeaways, and references match.

## Chapter 44

| # | Doubt | Verdict |
|---|---|---|
| 1 | «три межкомандные инициативы, которыми ограничен портфель из главы 42» | ok. The English: "the three cross-team initiatives that Chapter 42's portfolio limits": the portfolio is capped at three. |
| 2 | Trade-offs, the gloss on «контрфактическая» | ok. Explanatory, adds no claim; keep. |
| 3 | Step 3, «Третий ограничитель важен: если…» | ok. The English sentence ("A prompt that makes buyers give up would lower corrections by losing orders") explains the abandoned-cart guardrail. |
| 4 | A3, «Сделка с этим клиентом оценивается примерно в $300 000 в год» | ok. The English: "The prospect is worth about $300,000 a year"; the value is the prospective deal's. |
| 5 | Weeks 40–41, «Keiko и директор переводят список в дорожную карту результатов» | ok. The English: "run the conversion described in the Engineering Organization Example". |
| 6 | «Перенести сам метод труднее» | ok. The English: "The method transfers less well". |
| t16 | "workable for the business" → «жизнеспособна для бизнеса» | ok; see English problem 2. |
| t16 | "Related chapters:" kept as a paragraph | ok; it is a paragraph in the English. |
| t16 | "committed roadmap items delivered" → «выполненные обещанные пункты дорожной карты» | ok; nothing added. |
| t16 | A1, "push order latency to about 98.6 percent within 2 seconds" rebuilt | ok. The SLO is "99 percent within 2 seconds"; the rebuilt sentence says the share within 2 seconds falls to about 98.6 percent, which is the meaning. |
| t16 | Sofia Alvarez's title per cast.ru | ok. |
| t16 | "online controlled experiments" → «онлайн-контролируемые эксперименты» | ok in meaning; the editor's proposal «контролируемые онлайн-эксперименты» reads better and is left to the maintainer (term also in References). |

Full read: no drift found. The opening, the three scales (17, 7, 5; 212 and 27, 13 percent), the
objectives and related chapters, the mental model and discovery diagram, Cagan and Cagan and Jones
(expert opinion), the feasibility paragraph and tier 1 gloss, Perri and the outputs-over-outcomes
agreement (practitioner consensus), Bjarnason et al. (research finding, one company, interview study;
nine practitioners), the nine-clause contract table (this book's recommendation) and its two comments,
the four engineer contributions, the fifth-of-an-engineer arithmetic, Kohavi et al. (documented practice,
peer-reviewed; Bing, about 1 percent), the B2B limits (1,900 customers, 40 for a third of revenue), Ries
(expert opinion), Fagerholm et al. (research finding, two small companies), the five conversion steps
and diagram, the four-row date table, the info box (week 40; 30 to 14; week 39, 14 engineer-weeks, week
46), the example (600,000; 60 and 68 engineer-weeks; 7,800, 1.3 percent; 400 = 60 + 340; 1.1 percent,
6,630; the cause table; 6, 4, 10, 3, 5, 1; the sizing table, 59; 46 percent, 157 of 340; 0.8 percent,
weeks 52 and 46; the three guardrails), the decision table and diagram, five trade-offs (0.2 and 0.6 FTE,
three-quarters of a percent), six failure modes, the enterprise section, the CTO section, the 10-step
playbook, the case (62 and 22.6 FTE-quarters; Amara, Keiko, Helena Marsh, Sofia Alvarez, Greg Tanaka;
weeks 40–42; the four responses, 29 percent; week 46 commitment, forecast weeks 44 to 46), all
exercises (Rajiv Menon, Victor Lindqvist; 1.1 to 0.7 and 1.0; 98.6 percent; $300,000; 0.6 FTE),
reflection questions, takeaways, and references match.

Rendering left as is: "written scope" is «письменное содержание» while "flex scope" / "minimum scope" are
«объём». «Содержание» is the standard project-management word for scope, so the meaning holds; the
maintainer may unify.

## Possible problems in the English (not edited)

1. **Ch 43, F1**: "a single two-week sprint cadence for all six Northstar teams", then the methods of
   only five teams are given (Payments and Integrations, Data and Analytics, Platform Operations, Orders,
   Billing). Customer Experience (two-week sprints, per the baseline page) is missing. Also, the baseline
   page gives Platform Operations an "interrupt-driven ticket queue", while F1 says "runs an interrupt
   rotation" (the rotation may be a later change; check the timeline). The Russian mirrors the English.
2. **Ch 44, Two functions**: Cagan's fourth risk is usually "viable for the business"; the English says
   "workable" (noted by the translator). The Russian «жизнеспособна» follows Cagan's usual term, which
   fits the meaning.

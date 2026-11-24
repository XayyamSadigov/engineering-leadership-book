# Meaning check, batch 6: chapters 25 and 26

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batch 5:

1. Every doubt in `editing-ch25.md` and `editing-ch26.md` section 4 and in the translator's notes
   (`notes-t7.md`) gets a verdict.
2. Completeness: a script split both files into H1/H2/H3 sections and counted paragraphs, list items,
   table rows, admonitions, blockquotes, and code blocks per section. All anchors match (25: 29
   sections; 26: 30). The only count difference (ch 25, Engineering Organization Example, one list item)
   is a false positive. In the English the wrapped line "500. INC-422" starts with a number and a period,
   so the script read it as a list item. The collapsible note "The 19 incidents, by prevention point" has
   its body indented under the title, and so does the Russian.
3. Meaning: every paragraph of both chapters was read side by side with the English. That covered the
   mental model, the research passages, the Northstar examples and cases, all tables, exercises,
   reflection questions, takeaways, and reference lines. Evidence labels were checked one by one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 13 doubts checked, 1 changed (ch 26 no. 2). Further fixes from the full read: ch 25 ×1, ch 26 ×2.
Validation: `tools/validate_book.py` passed.

## Chapter 25

| # | Doubt | Verdict |
|---|---|---|
| 1 | Case, week 9: «Разбор вёл инженер, причастный к инциденту» contradicts the neutral-facilitator rule | ok as a translation. The English says "The engineer involved led the review." The Russian is faithful. The contradiction is in the English (see below). Not changed. |
| 2 | «Отвечают здесь за систему, а не за то, что оказались ближе всего к сбою» | ok. The English reads "accountability for the system, not for the person nearest the failure": accountability is not placed on whoever was nearest. |
| 3 | «пользуясь остальными вопросами диаграммы» | ok. The English says "using the diagram's later questions", and the next sentence explains that the first question cannot be answered from the file. |
| 4 | «три инцидента оказались пограничными» | ok. The English says "left three incidents as judgment calls". |
| 5 | «поэтому их подали как обнадёживающие» | ok. The English reads "Both rest on few events and were reported as encouraging, not conclusive." Few events are the reason for the cautious framing, so «поэтому» makes explicit what the English implies. |
| t7 | "until the director re-rated it" (singular) rendered as plural | ok. Now «пока директор не переоценил эти инциденты». |
| t7 | "Severity drift" has no "Signal:" field | ok. The Russian follows the English. |
| t7 | "contested" not bold → «и вопрос спорный» | ok. Strength unchanged. |

Further fixes:
- First minutes, step 1: "lowering it later is cheap" had become «понизить его потом ничего не стоит»
  (costs nothing), which overstates it. Now «понизить его потом дёшево».

Full read: no other drift. Stribblehill (documented practice from one organization, not outcome
evidence), Lunney and Lueder, Allspaw (the information argument, the second story, hindsight bias), Cook
(expert opinion, mainly about healthcare), Nash (industry research, from the talk's abstract), "the
evidence is contested", Sillito and Kutomi and Anandayuvaraj et al. (qualitative, no comparison), Murray
et al. ("scant and mostly theoretical"), van Marum et al., and Edmondson (association) all match. So do
the four severity properties, the two communication rules, the closure and recurrence gaming, the
prevention-point diagram and its three rules, the illustrative classification and the note, the four
observations, the decision table, the trade-offs, the six failure modes, the enterprise and CTO
sections, the playbook, the case with all its numbers, and all exercises.

## Chapter 26

| # | Doubt | Verdict |
|---|---|---|
| 1 | «результаты CSF — не чек-лист» | ok. The English reads "The document states that its outcomes are not a checklist of actions", and "the document" is CSF 2.0. |
| 2 | «Вместо этого CSF предлагает…» | fixed: → «CSF предлагает…». The English ("It proposes a Current Profile…") does not present the profiles as the alternative to a checklist. The connective added framing. |
| 3 | «вызывает раздражение» for "builds resentment" | ok. Slightly weaker than "resentment" but natural in an organizational context; the point (tickets-only central teams alienate product teams) survives. |
| 4 | «Это научные результаты, но каждый получен в одной организации» | ok. The English reads "Both are single-organization **research findings**." The label and the caveat are kept. |
| 5 | auth-svc: the director as agent of the restriction and the exception | ok. In the English the director "assigned … restricted … and recorded"; Kwame Mensah is only the technical lead. |
| t7 | References: «Core (ядро CSF)» | ok, an acceptable clarification. In the English "the Core" is the CSF Core. A reader of this book would otherwise take it for Northstar's monolith, Core. The gloss names what the English already means and adds no claim. |
| t7 | "migrate it off scripts" → «увести их со скриптов» | ok. "it" refers to webhooks. |
| t7 | A1 "The Billing team of Marcus Oyelaran (Billing manager)" → «Команде Billing, которой руководит Marcus Oyelaran» | ok |

Further fixes:
- F3: a missing comma before the parenthetical: «Build и Source скорее всего, соответствует» → «Build и
  Source, скорее всего, соответствует».
- A3: "The renewal customer's questionnaire" had become «Опросник клиента, чьё продление под вопросом».
  "Под вопросом" (in doubt) is not in the English. The case only says that the customer's renewal depends
  on the renewal commitments. Now «Опросник клиента, чьё продление зависит от обязательств (см. «Кейс»)».

Full read: no other drift. AWS Well-Architected (vendor guidance), CSF 2.0 (standard), the SSDF and its
four groups, the mapping table (this book's, not NIST's), the SLSA tracks table and the replaced 1–4
ladder, the NTIA minimum elements and the CISA draft, Decan et al. (a mechanism, not a number), the CVSS
thresholds, the four-part remediation policy (this book's starting point), CISA's KEV statement, Meli et
al. (research finding about public repositories), the Threat Modeling Manifesto (practitioner consensus),
the six-method table, OWASP on SAST, DAST, and disclosure (practitioner consensus), and the tool sequence
(this book's recommendation) all match. So do Gutfleisch et al. and Nguyen-Duc et al., the measures table
and the "no peer-reviewed outcome evidence" caveat, both Northstar tables (numbers verbatim, "1.8 FTE"
kept), the decision diagram and tables, the trade-offs, the six failure modes, the enterprise, CTO, and
playbook sections, the case and its day-90 table, and all exercises.

## Possible problems in the English (not edited)

1. **Ch 25, Case Study, week 9**: "The engineer involved led the review." The chapter's Decision
   Framework requires a "neutral facilitator" for a full Sev1 review and says "the outsider runs the
   meeting, the manager owns the document and actions". The week-9 incident was a Sev1, so the case
   breaks the chapter's own rule without comment. If the intent is that the engineer involved took part
   fully and without blame, suggest "The engineer involved helped write the review, which a staff engineer
   from another team facilitated." Otherwise add a sentence explaining the exception. The Russian follows
   the English and should be re-synced if the English changes.
2. **Ch 25, Severity definitions**: "four consecutive incidents were rated Sev3 … until the director
   re-rated it". "it" should be "them" (already in `notes-t7.md`).
3. **Ch 25, Failure Modes, Severity drift**: the only failure mode without a "Signal:" field. Its first
   sentence is in effect the signal. Suggest "Signal: Sev1 and Sev2 counts fall while…".
4. **Ch 26, References, NIST 2024**: "the statement that the Core is not a checklist". In this book "Core"
   means Northstar's monolith; suggest "the CSF Core". The prose says "its outcomes", which is consistent.
5. **Ch 26, Case Study, webhook keys**: "with time to migrate it off scripts". "it" refers to "webhooks";
   suggest "them".

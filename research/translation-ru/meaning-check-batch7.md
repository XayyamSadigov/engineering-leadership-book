# Meaning check, batch 7: chapters 27 and 28

A bilingual check of the fresh translation and its literary edit against the English source
(2026-11-24). Method as in batch 6:

1. Every doubt in `editing-ch27.md` and `editing-ch28.md` section 4 and in the translator's notes
   (`notes-t8.md`) gets a verdict.
2. Completeness: a script split both files into H1/H2/H3 sections and counted paragraphs, list items,
   table rows, admonitions, blockquotes, and code blocks per section. All anchors match (27: 28
   sections; 28: 27), and every count is identical in every section. No paragraph, list item, table
   row, exercise, or reference line is missing. Both "Northstar so far" admonitions keep their body
   indented under the title.
3. Meaning: every paragraph of both chapters was read side by side with the English. That covered the
   mental models and diagrams, the research passages, the Northstar examples and cases, all tables,
   exercises, reflection questions, takeaways, and reference lines. Evidence labels were checked one by
   one.

Fixes are minimal and keep the editor's style. Anchors, links, and numbers are untouched. English was not
edited.

Totals: 16 doubts checked, 4 changed (ch 27 no. 3 and no. 4; ch 28 no. 1 and no. 4). The lead-in «Из
модели следуют три вывода» is kept. Further fixes from the full read: ch 27 ×3, ch 28 ×3.
Validation: `tools/validate_book.py` passed.

## Chapter 27

| # | Doubt | Verdict |
|---|---|---|
| 1 | Lead-in «Из модели следуют три вывода.» before «Во-первых…» | kept. The English follows the table with "First, the dip is real… Second, the plan pays back… Third, the money is not small", three numbered readings of the model. The lead-in announces exactly that structure and adds no claim. |
| 2 | «В итоге растут пачки либо появляются тесты…» for "Batches grow, or tests run code…" | ok. The two outcomes map to the two mandates (sign-off → bigger batches; coverage target → assertion-free tests). |
| 3 | QA announcement: «…и к тому времени двое QA-инженеров уже спросили…» | ok on the causality: the English ("delayed the announcement until week 10, after two QA engineers had asked") states order, not cause. Fixed the question itself: «не автоматизируют ли заодно и их самих» added "заодно" and blurred "automated out of a job". Now «не лишатся ли они работы из-за автоматизации». |
| 4 | CTO perspective: «доступность по договору в сравнении с обязательством» | fixed: → «доступность в сравнении с договорным обязательством». The English "contractual availability against commitment" compares measured availability with the 99.9% contractual commitment; the old wording read as "contracted availability versus commitment", which is circular. |
| 5 | «Обе петли работают в любую сторону» while the diagram shows "one loop with two branches" | ok, and the English is right too. The diagram has two cycles through «Незапланированная работа»: via planned capacity, schedule pressure and shortcuts, and via less prevention. "Both loops" are these two. |
| t8 | "two afternoons" → «две вторые половины дня» | ok as now edited: «два раза по полдня». |
| t8 | ARR not introduced for "$9M in annual recurring revenue" | ok; «годовой регулярной выручки» spelled out, as the English does. |
| t8 | "(about 13 FTE by quarter 4)" → «к кварталу 4» | ok. |

Further fixes:
- Changing roles, move 4: "Keeping a shrinking part of the old work and starting automation at once
  both help the program" had become «те, кто доведёт до конца сокращающуюся часть старой работы»
  (finish it off). "Keeping" means continuing to do it. Now «те, кто сохранит за собой сокращающуюся
  часть старой работы».
- Scorecard rules: "audit the classification ones, severity above all" had become «проверяйте, начиная
  с серьёзности», which reads as an order of work. Now «проверяйте, и прежде всего серьёзность».
- CTO perspective: "an auditable pipeline" had become «пайплайн с журналом аудита», narrower than the
  English and inconsistent with the glossary, the year 1 record, the cast, and Halvard («аудируемый
  пайплайн»). Now «аудируемый пайплайн».

Full read: no other drift. Meadows, Goldratt and Cox, Humble and Farley, DORA as industry research
(unbolded, "survey-based and correlational… not a law"), Campbell ("usually credited"), Grove, the
five role-change moves (this book's recommendation), the illustrative capacity model with its
assumptions and both tables (numbers verbatim), the pessimistic case, the decision diagram and both
tables, the three Northstar program shapes, the four trade-offs, the six failure modes (the
action-item graveyard has no "Как заметить" field, as in the English), the enterprise roles and cadence
table, the CTO section, the 17-step playbook, the case (week 2, the managers' beliefs, the 25/10/15
percent split, the three things that went wrong, the day-90 table and the cautious reading), all
exercises, reflection questions, takeaways, and references all match.

## Chapter 28

| # | Doubt | Verdict |
|---|---|---|
| 1 | «как следят, чтобы они оставались в силе» for "how they are kept true" | fixed: → «как следят за их соблюдением». The paragraph is about architectural erosion (decisions left implicit), and the chapter later answers it with fitness functions; "kept true" means the system keeps conforming to the decisions, not that they stay formally valid. |
| 2 | Trade-offs: «Право согласия … — плата за это» | ok. The English says "The agreement right on capacity and dates is the price, and it must stay narrow." «Плата» renders "price" exactly; «компенсация» would add an interpretation. |
| 3 | Takeaway «заводите их по триггеру из код-ревью» | ok. The English "triggered by code review" refers to the code-review trigger of the ADR section (playbook step 5). |
| 4 | References, Nygard: «Исходная запись решения» | fixed: → «Первоначальное описание записей решений». The English "The original decision record" points to Nygard's 2011 post that introduced the format (the prose cites it for the format); «Исходная запись решения» read as one specific record. See English note 3. |
| 5 | Buchgeher: «Согласно аннотации» | ok as a translation: the English says "Their abstract reports". The access note in reader text is an English issue (note 1). Not changed. |
| 6 | Board section: «Глава 20 показывает…» plus a second link «([глава 20](…))» | ok as a translation; the doubled reference is in the English (note 2). Not changed. |
| t8 | "expert opinion (economic theory)" bold | ok. |
| t8 | Table cell "2, plus contract tests" → «2 плюс контрактные тесты» | ok; number unchanged, the comma was punctuation. |

Further fixes:
- Aghion and Tirole: "It fits a familiar pattern" had become «Но теория хорошо объясняет знакомую
  картину», which strengthens an expert-opinion claim into an explanation. Now «Но она согласуется со
  знакомой картиной».
- Case, how Northstar decided: "Decisions were made by whichever team built first, in chat threads, or
  during incidents" lists three alternatives; «Решала та команда, которая первой начинала строить, — в
  чатах или во время инцидентов» made chats and incidents the venue of the first-building team. Now
  «Решала та команда, которая первой начинала строить, либо решение складывалось в чатах или во время
  инцидентов».
- A2: "without … overruling him in a hallway yourself" had become «не отменили его решение в коридоре».
  Victor's remark is not a recorded decision, and the English overrules him, not a decision. Now «не
  переиграли его в коридоре».

Full read: no other drift. Jansen and Bosch ("argued"), adr.github.io, Larson (three sources), Aghion and
Tirole (expert opinion, economic theory, "not a study of software teams"), the position and its "no
study compares" caveat, the decision-rights table, the two corollaries (the editor's «Из этого следуют
два вывода» matches "Two corollaries"), Nygard, the Thoughtworks Radar entries (practitioner consensus,
"not evidence of effect"), Buchgeher et al. (research finding, open source only, no outcomes), Ubl and
Manshreck (documented practice from one company), the feedback-versus-gate table, the three board
failures and the loop diagram, the fitness-function pairing (this book's recommendation), Conway, the
illustrative queue example with both tables (numbers verbatim), the decision table and borderline test,
the five trade-offs, the six failure modes, the enterprise and CTO sections, the playbook and the
recovered-record subsection, the case with the ADR-0001 options table, and all exercises match.

## Possible problems in the English (not edited)

1. **Ch 28, Architecture decision records, Buchgeher**: "Their abstract reports ADR adoption low…" puts
   an access note in reader text, which CLAUDE.md section 7 forbids ("no notes on how a source was
   accessed. Fold access limits into the evidence label"). Suggest "Buchgeher and colleagues … report
   ADR adoption low…" and let the bibliography carry the access level. The Russian follows the English
   («Согласно аннотации») and should be re-synced if the English changes.
2. **Ch 28, When an architecture board becomes a queue**: "Chapter 20 shows how a council … becomes an
   unbounded queue that teams route around ([Chapter 20](…))" names Chapter 20 twice. Suggest linking
   the first mention and dropping the parenthetical.
3. **Ch 28, References, Nygard**: "The original decision record" is ambiguous (one record, or the
   format). Suggest "The original description of the decision record format" or "The post that
   introduced ADRs".
4. **Ch 27, Engineering Organization Example**: "The figures for the first quarter come from Northstar's
   baseline" while the table also has a separate Baseline row and the Q1 row is itself a projection
   (33%, 12 FTE). Probably "The baseline figures come from Northstar's baseline quarter; the four
   quarters are the director's projection". The Russian follows the English.

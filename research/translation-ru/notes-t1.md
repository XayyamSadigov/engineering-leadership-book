# Lane t1 notes: Chapters 1–6 (Russian)

Translated from the English working tree at `b84a765`.

## New terms (not in the term base; used consistently in Chapters 1–6)

| English | Русский | Where | Note |
|---|---|---|---|
| people management / delivery management / technical direction (the three jobs) | управление людьми / управление поставкой / техническое направление | Ch 1–4 | follows existing usage in `baseline-data.ru.md`, `learning-roadmaps.ru.md`; short table labels: Люди / Поставка / Техника |
| the three jobs | три работы | Ch 1, 4 | «карта трёх работ» for the three-jobs map |
| calendar audit | аудит календаря | Ch 1–4 | |
| leveraged / necessary / substitutable (audit marks) | с рычагом / необходимое / заменимое | Ch 1, 3 | |
| managerial output | результат руководителя | Ch 1–4 | |
| leverage (managerial) | рычаг; управленческий рычаг | Ch 1–4 | matches the ru nav title of Ch 3 |
| leverage band | уровень рычага | Ch 1, 3 | |
| tech lead manager (TLM) | техлид-руководитель (tech lead manager) | Ch 1, 4 | |
| staff track | staff-трек; трек staff-plus | Ch 1, 4 | |
| staff archetypes: tech lead, architect, solver, right hand | техлид, архитектор, решатель (solver), правая рука (right hand) | Ch 1, 4 | |
| level of control (delegation scale) | уровень контроля | Ch 2 | levels: Указание / Рекомендация / Намерение / Действие и информирование / Владение |
| delegate (noun) | исполнитель | Ch 2 | |
| merge request | мерж-реквест | Ch 2, 4 | glossed once per chapter where English glosses it |
| Peter Principle | принцип Питера | Ch 2, 4 | |
| single-person area | область, завязанная на одного человека | Ch 2 | |
| follow-up action | последующее действие | Ch 2 | Ch 25 may use «корректирующее действие» for corrective action; kept distinct |
| managing up | управлять вверх; работа с собственным руководителем | Ch 2 | heading rendered «Работа с собственным руководителем» |
| on-call stipend | надбавка за дежурства | Ch 3 | |
| page (on-call) | вызов | Ch 3, 4 | «вызовы без действий» for no-action pages |
| gain (of a loop) | коэффициент усиления | Ch 3 | |
| backfill | найм на замену (ушедшего) | Ch 3 | |
| seat-weeks | место-недели | Ch 3 | |
| multipliers / diminishers (Wiseman) | мультипликаторы (multipliers) / ослабители (diminishers) | Ch 3 | maintainer may prefer the published Russian edition's terms if one is adopted |
| previous-level gravity | притяжение прежнего уровня | Ch 4 | |
| title inflation | инфляция должностей | Ch 4 | |
| scope (of a role) | область ответственности | Ch 4 | |
| time horizon | горизонт времени | Ch 4 | |
| management bench / leadership bench | управленческий резерв / резерв руководителей | Ch 2, 4 | |
| engineering executive (Larson) | руководитель разработки высшего уровня (engineering executive) | Ch 4 | |
| senior manager (ladder rung) | старший руководитель | Ch 4 | |
| trial period (track switch) | пробный период | Ch 4 | |
| unit outcomes | результаты подразделения | Ch 4 | |
| report (direct report, as noun) | подчинённый | Ch 5, 6 | term base has «прямой подчинённый» for direct report |
| directing / coaching / mentoring / sponsoring | указание / коучинг / менторство / спонсорство | Ch 5 | the four modes of help |
| news rate | доля встреч с новостями | Ch 5 | |
| decay (of one-on-ones) | вырождение | Ch 5 | «петля вырождения», «сигналы вырождения» |
| running document | текущий документ | Ch 5 | |
| team health check | проверка здоровья команды | Ch 5 | |
| board (task board) / stand-up | доска задач / стендап | Ch 5 | |
| task / process / relationship / status / values conflict | конфликт задачи / процесса / отношений / статусный конфликт / конфликт ценностей | Ch 6 | |
| feedback intervention theory | теория вмешательства через обратную связь (feedback intervention theory) | Ch 6 | |
| ruinous empathy | разрушительная эмпатия | Ch 6 | |
| compliment sandwich | бутерброд из комплиментов | Ch 6 | |
| false harmony / artificial harmony | ложная гармония / искусственная гармония | Ch 6 | |
| proxy wars | войны чужими руками | Ch 6 | |
| over-correction | перегиб | Ch 6 | |
| "know where they stand" | знать, на каком ты счету | Ch 6 | |
| **contested** (used like an evidence label in Ch 6) | **вопрос спорный** | Ch 6 | not in the section 4.3 label list; maintainer may want a fixed rendering |

## Doubts and observations (English not changed)

- Ch 1, Case Study: "$140M of annual recurring revenue" rendered as «годовая регулярная выручка компании —
  $140 млн» without introducing the ARR abbreviation, since the English does not use it here.
- Ch 2, References: "cited here from its publisher's summary" is an access note in reader text
  (CLAUDE.md section 7 asks for evidence labels instead). Translated faithfully; flag for the English
  maintainer.
- Ch 4, References: "Draft chapters cited" and "mostly free at staffeng.com" are similar bookkeeping-like
  notes; translated faithfully.
- Ch 5, English line 178 ("2. Its cost is that people learn to wait...") is a wrapped prose line that
  begins with "2."; harmless in Python-Markdown (a list cannot interrupt a paragraph without a blank
  line), but worth rewrapping in the English source. The Russian text avoids line-initial numbers.
- Ch 3, Engineering Organization Example: "cause-based alerts" kept as an English gloss in parentheses
  after «алерты, которые срабатывают по причинам», since Ch 24's Russian rendering is not fixed yet.
- Chapter cross-references by title use the `ru` nav translations from `mkdocs.yml` (Ch 6, 34, 41).
- Checker false positives: table rows containing «1:1» differ from English in digit tokens; numbers are
  otherwise verbatim.

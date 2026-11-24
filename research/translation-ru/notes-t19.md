# Translation notes, lane t19 (Chapters 49–50)

Source: English working tree. Files:
`docs/parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.ru.md`,
`docs/parts/12-cto-leadership/50-what-a-cto-actually-does.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, exercise labels,
admonition types, Mermaid count and node ids, table rows and every number in tables identical. Prose
number differences are only word forms ("year 1/2/3" → «первый/второй/третий год»: ch49 nine "2", three
"1", one "3"; ch50 five "2"), «1:1» once in ch49 and the thousands separator. No wrapped line starts with
a number followed by a period. Words (wc -w; no-break spaces glue some tokens): ch49 5 736, ch50 5 925.

Failure Modes: ch49 has only "Early sign:" → «Как заметить:» (ch43 precedent). Ch50 has "Early sign:"
everywhere plus one "Detection:" (shadow architect), so inside ch50 "Early sign" → «Признак:» and
"Detection" → «Как заметить:» (ch35/ch47 precedent for a two-field entry).

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| gate (stage gate); gate review; gate rule; gate date | контрольная точка (gate); разбор на контрольной точке; правило контрольной точки; дата контрольной точки | T (term base 3.8) | ch49 |
| stage-gate (Cooper) | stage-gate (идея, модель stage-gate) | E | ch49 |
| stage names Stabilize / Hold / Converge | Стабилизация / Удержание / Консолидация | T | ch49; "Converge" = converging the four build systems |
| re-scope | пересмотр объёма | T | ch49 |
| the ask | запрос | T | ch49 |
| cost of no | цена отказа | T | ch49 |
| page one | первая страница | T | ch49 |
| an option beyond it (next stage) | вариант на следующий этап; вариант продолжения | T | ch49 |
| funders | финансирующие | T | ch49 |
| success paradox | парадокс успеха | T | ch49 |
| strategic misrepresentation / optimism bias | стратегическое искажение данных / оптимистическое искажение | B | follows notes-t3 |
| issue selling | продвижение вопросов (issue selling) | B | ch49 |
| packaging, involvement, timing | упаковка, вовлечение, выбор момента | T | ch49 |
| political skill; Political Skill Inventory | политические навыки; опросник Political Skill Inventory | T, E | ch49 |
| perceived (organizational) politics | воспринимаемая (организационная) политика | T | ch49 |
| pre-wiring | предварительное согласование (pre-wiring) | B | ch49 |
| transcript / record / interests tests | тест стенограммы / тест записи / тест интересов | T | ch49 |
| workstream | направление работ | T | ch49; kept apart from bare «направление» (= a director's area, notes-t18) |
| decision meeting | встреча, на которой принимают решение | T | ch49 |
| end state | конечное состояние | T | ch49 |
| permanent tax | постоянный налог | T | ch49; «налог» follows notes-t13 |
| offset (budget) | компенсирующая экономия | T | ch49 |
| two-year blank check / moving goalposts / engineering-only case / buried ask / back-channel trading / sponsor-dependent program / victory by attrition | карт-бланш на два года / правила меняют по ходу игры / доводы только на языке разработки / спрятанный запрос / торг в обход / программа, завязанная на спонсора / победа измором | T | ch49 failure modes; «измором» follows notes-t13 |
| contest of advocacy | состязание в красноречии | T | ch49 X2 |
| archetypes: infrastructure manager / technology visionary and operations manager / external-facing technologist / big thinker / organization builder | управляющий инфраструктурой / технологический визионер и операционный руководитель / внешний технолог / стратегический мыслитель (big thinker) / строитель организации | T, B on first use | ch50; table short form «Визионер и операционный руководитель» |
| residual (the role is a residual) | остаток | T | ch50 |
| CIO; head of IT; Corporate IT | CIO (chief information officer, директор по информационным технологиям); руководитель ИТ; корпоративное ИТ | B, T | ch50; follows cast.ru, glossary.ru |
| identity (and access) | учётные записи (и доступ) | T | ch50 |
| controls (security) | меры защиты; меры контроля | T | ch50; «меры защиты» follows notes-t7 |
| seam | шов | T | follows notes-t10/t11 |
| ruling; informal ruling; hallway ruling | вердикт; неформальный вердикт; вердикт в коридоре | T | ch50; avoids the ambiguous «решение» (editing pattern 6) |
| redirect; misrouted request | перенаправлять; запрос, пришедший не по адресу | T | ch50 |
| receiver (of delegated work) | получатель | T | ch50 |
| keep, give, stop list | список «оставить, отдать, прекратить» | T | ch50 |
| decision class | класс решений | T | ch50 |
| ratify | утверждать | T | ch50 |
| Binds the company? / Needs top trust? | Обязывает компанию? / Нужно личное доверие? | T | ch50 diagram |
| first team / second team | первая команда / вторая команда | T | ch50; «первая команда» follows notes-t18 |
| bridge (incident call) | созвон | T | ch50 |
| evidence library; engineering evidence owner | библиотека доказательств; владелец доказательств со стороны разработки | T | ch50; follows quarter-4-briefing.ru |
| remediation service levels | уровни сервиса по устранению уязвимостей | T | ch50 |
| shadow architect / absent executive / engineering advocate / archetype lag / orphaned seam | теневой архитектор / отсутствующий руководитель / адвокат разработки / отставание архетипа / бесхозный шов | T | ch50 failure modes; «бесхозный» follows notes-t9 |
| thrash (new executive) | метания | T | ch50 |

Reused: эскалация приверженности, сервисные кредиты (компенсации по SLA), доля неудачных изменений
(change failure rate), FTE-квартал, свободный бюджет на инструменты, операционные минимумы, tier 1,
аудит серьёзности, реестр владения, целевая система CI, портфельный форум, функции для сделок, скользящая
сумма за четыре квартала, условие пересмотра, покрытие преемниками, «готов сейчас / готов после
развития», руководитель разработки высшего уровня (engineering executive), рамки бюджета, операционный
план, пакет для совета директоров, путь эскалации, выделение на профилактику, квартальная перезагрузка,
операционный разбор, бизнес-обзор, «Год вкратце», действующие лица, брифинг квартала 4.

*The Effective Executive* glossed with its published Russian title «Эффективный руководитель»; *The Five
Dysfunctions of a Team* as «Пять пороков команды» (notes-t18).

## Doubts and notes on the English (English not changed)

- ch49 Decision Framework table: "funding an unexplained miss is escalation" rendered «это эскалация
  приверженности», since bare «эскалация» would read as an escalation path in this book.
- ch49 "do not trade away the floor in the room": "the floor" read as the minimum the proposal will not go
  below (ch46's quality floor); rendered «нижняя планка».
- ch49 "the CTO decides whether to sponsor the proposal or present it" read as "back it while the
  director presents, or present it in person"; rendered so.
- ch49 Case: the stage table writes "1: Stabilize (year 1)" and "Year 3 option"; kept as «год 1», «год 3»
  in the table so table numbers stay identical, word forms in prose.
- ch49 "the year-2 organization proposal" in a table cell rendered «предложение по организации на год 2»
  for the same reason.
- ch50 Example: the hours table says "one-on-one"; rendered «встреча один на один», not «1:1», so table
  digits stay identical.
- ch50 "reaches you only for customer commitments or the director's budget authority" read as "only when
  customer commitments or the limits of the director's budget authority are involved".
- ch50 Failure Modes mix "Early sign:" and one "Detection:" within the chapter; the maintainer may want one
  label set book-wide (same point as notes-t12, notes-t18).
- ch50 References: Larson 2023c "Disengagement as the worse failure" rendered «худший из двух провалов»
  (the chapter compares two failures).
- ch50 Fournier reference: "Known for following the management track…" has the book as subject;
  rendered «Известна тем, что проходит управленческий трек…» (книга).

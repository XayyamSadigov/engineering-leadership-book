# Translation notes, lane t23 (Chapters 57–58)

Source: English working tree. Files:
`docs/parts/13-advanced-problems/57-crises-executive-disagreement-and-resistance.ru.md`,
`docs/parts/13-advanced-problems/58-layoffs-reductions-and-mergers.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, citation link
texts, exercise labels, admonition types, Mermaid count and node ids, table rows and every number in
tables identical. No wrapped line starts with a number followed by a period. Prose number differences
are only the thousands separator and word forms (ch57: "year 2" four times → «второй год»; ch58: "year 2"
twice, "month 2/4/5" → «на втором/четвёртом/пятом месяце»). H1 titles follow the `ru` nav translations.

Failure Modes: ch57 has only "Early sign:" → «Как заметить:» (ch43, ch49, ch51 precedent); ch58 has
only "Detect it when/with/in…" → «Как заметить:» (ch32 precedent). Neither chapter has a Signal or
Countermeasure field, so «Признак:» and «Что делать:» do not occur.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| response track / leadership track (executive track) | трек реагирования / трек руководства | T | ch57 |
| incident bridge; bridge | бридж инцидента (живой созвон, где координируются те, кто чинит); бридж | T | ch57, ch57 X1; follows halvard.ru («подключается к бриджу»); notes-t19 has «созвон» for the same word in ch50, the maintainer may unify |
| executive (person) | высший руководитель; руководитель высшего уровня; высшее руководство (plural) | T | ch57, ch58 |
| accountable executive | ответственный руководитель | T | ch57 |
| Situational Crisis Communication Theory (SCCT) | ситуационная теория кризисной коммуникации (Situational Crisis Communication Theory, SCCT) | B | ch57 |
| instructing / adjusting information | инструктирующая информация (instructing information) / адаптирующая информация (adjusting information) | B | ch57 |
| crisis clusters victim / accidental / preventable | жертва / случайность / предотвратимый кризис; «кластеры» | T | ch57 |
| crisis history; intensifying factor | история кризисов; усиливающий фактор | T | ch57 |
| response groups deny / diminish / rebuild (denial, scapegoating; excuse, justification; compensation, apology) | отрицать / преуменьшать / восстанавливать (отрицание, поиск козла отпущения; отговорки, оправдание; компенсация, извинение); «стратегии восстановления» | T | ch57; verbs for the group names so that «отрицание» is not both group and member |
| attribution (of responsibility) | приписанная ответственность | T | ch57; «атрибуция» avoided in prose |
| competence / integrity violation | нарушение, связанное с компетентностью / с честностью; «провал компетентности», «вопрос честности» | T | ch57; follows notes-t16 |
| sensemaking (Weick) | осмысление происходящего | T | ch57 |
| status post; status page; support macro | публикация статуса; страница статуса; шаблон ответа поддержки | T | ch57; follow halvard.ru |
| first notice; cadence updates | первое уведомление; плановые обновления | T | ch57 |
| card processor | процессинговая компания | T | ch57 |
| merchants (Halvard) | продавцы | T | follows halvard.ru |
| voice (speaking up); exit; silence (forms of resistance) | высказывание (voice); уход; молчание | B for voice | ch57; voice follows notes-t2 |
| silent compliance | молчаливое подчинение | T | ch57 |
| slow-walk | тянуть с работой | T | ch57 |
| commit (to a decision); commit-or-escalate test | поддержать решение; тест «поддержать или эскалировать» | T | ch57, ch58; «обязательство» avoided (taken by commitment in the forecast triad) |
| sandbagging (a decision you opposed) | саботировать | T | ch57 objective; notes-t3's «занижение обязательств (sandbagging)» is the forecasting sense, not this one |
| revisit trigger | условие пересмотра | T | follows notes-t17 |
| written floor; floor | записанная планка; планка | T | follows ch46.ru |
| board headline | главный показатель для совета директоров | T | follows quarter-4-briefing.ru |
| joint escalation; escalate to oversight | совместная эскалация; эскалация к надзору (тем, кто надзирает) | T | ch57 |
| change agent; recipients (of a change) | инициатор изменения; те, кого касается изменение | T | ch57 |
| reading (of resistance): content / process / interest / history / capacity / person | трактовка: содержание / процесс / интересы / история / ресурс / человек | T | ch57; «трактовка» chosen over «прочтение» as more natural Russian |
| ambivalence | двойственное отношение | T | ch57 |
| paper compliance | соблюдение на бумаге | T | ch57 |
| voice climate | климат для высказываний | T | ch57 |
| crisis role card | карточка кризисных ролей | T | ch57 |
| out-of-band channel | резервный канал (связи с клиентами), размещённый вне продукта | T | ch57; «внеполосный» avoided as jargon |
| general counsel | главный юрисконсульт (general counsel) | B | ch57 X2 |
| head of communications | руководитель коммуникаций | T | follows halvard.ru |
| failure modes: the executive on the bridge / the approved-to-death first notice / the speculative cause / mixed strategies / naming the engineer / the silent commit / escalation as threat / resistance as pathology / the listening tour that changes nothing | руководитель на бридже / первое уведомление, утонувшее в согласованиях / догадка вместо причины / смешанные стратегии / имя инженера / мнимая поддержка / эскалация как угроза / сопротивление как патология / сбор мнений, который ничего не меняет | T | ch57; «эскалация как угроза» follows notes-t14 |
| this book's inference | вывод книги | T | ch57, ch58; not in glossary 4.3, formed like «синтез книги»; not bold in the English either |
| reduction (in force); layoff | сокращение (штата); увольнение | T | term base |
| survivors | оставшиеся (сотрудники); glossed once «в исследованиях их называют survivors» | T | ch58 |
| severance; severance waiver | выходное пособие; отказ от претензий в обмен на выходное пособие (severance waiver) | B | ch58 |
| selection criteria; criterion family | критерии отбора; семейство критериев | T | ch58 |
| disparate effects (on protected groups) | несоразмерное влияние на защищённые группы (disparate effects) | B | ch58 |
| ownership check; continuity of ownership | проверка владения; непрерывность владения | T | follows notes-t10 |
| notification day; the survivors' note | день уведомления; записка для оставшихся | T | ch58 |
| sustaining team / roles | команда поддержки; роли в команде поддержки | T | follows halvard.ru |
| transition contract | контракт на передачу дел | T | follows halvard.ru |
| employment counsel | юрист по трудовому праву; юристы | T | ch58 |
| bumping | вытеснение других (bumping) | B | ch58 |
| spread cut / across-the-board / spreadsheet cut | равномерное сокращение / «под одну гребёнку» / сокращение по таблице | T | ch58 |
| WARN Act | Федеральный закон США WARN Act (о заблаговременном уведомлении работников о массовых увольнениях) | E + gloss | ch58; official name kept English, gloss in the table cell at first use |
| EU collective redundancies directive | директива ЕС о массовых увольнениях (collective redundancies directive) | B | ch58 |
| EEOC; US DOL | EEOC (Equal Employment Opportunity Commission, Комиссия по равным возможностям при трудоустройстве); Министерство труда США (Department of Labor) | B | ch58 |
| integration dimensions people / product / platform / policy | люди / продукт / платформа / политики | T | ch58 |
| preserve / hold / integrate in stages / absorb | сохранить / отложить / интегрировать поэтапно / поглотить | T | ch58 |
| close (of a deal); deal thesis; deal model | закрытие сделки; тезис сделки; модель сделки | T | ch58 |
| merger of peers | слияние равных | T | ch58 |
| retention bonus | бонус за удержание | T | ch58 |
| leveling (of acquired staff) | определение уровней | T | ch58 |
| HR business partner | HR бизнес-партнёр | T | follows halvard.ru |
| failure modes: the spreadsheet cut / the performance cleanup / the silent expert / access before conversation / the rolling layoff / the vanished leader / day-one absorption / leveling as demotion | сокращение по таблице / чистка по результативности / молчаливый эксперт / доступ раньше разговора / сокращение в рассрочку / исчезнувший руководитель / поглощение в первый день / уровень как понижение | T | ch58 |

Reused: координатор инцидента (incident commander, IC), безобвинительный разбор, «не согласен, но
действую» (disagree and commit), носители (изменения), пульс-опрос, исключение, аудит серьёзности,
скользящая сумма за четыре квартала, продолжение программы качества, рабочий договор, исправленные
заказы, функции для сделок, «отличные» возможности, Engineering Excellence Day, закрытие периода,
текучесть, заявка на найм, вестинг, место, интервью об удержании (stay interview), встреча через уровень
(skip-level), полная стоимость сотрудника, операционные минимумы tier 1, truck factor (он же bus factor),
ранбук (runbook), инженеро-квартал, руководитель разработки высшего уровня, «Год вкратце», действующие
лица, брифинг квартала 4, хроника года 1.

## Doubts and notes on the English (English not changed)

- ch57 Decision Framework: "Use the three tables together" but the third tool (reading resistance) is a
  paragraph, and the second is a diagram; translated as written («три таблицы»).
- ch57 Example: "8,600 merchants take card payments", "64 percent", "1,500 a minute" match halvard.md.
  The impact table "About 168,000" rounds halvard.md's 168,480; fine.
- ch57 line 85 and ch58 lines 275, 293, 461 are overlong source lines; cosmetic.
- ch57 Mental model sentence "the leader who controls the message instead of the information loses both"
  rendered literally («теряет и то и другое»).
- ch57 X2: "general counsel" glossed «главный юрисконсульт (general counsel)».
- ch58 Not-legal-advice box: translated with the same strength («Она не говорит, что применимо к вам»;
  «нужен юрист по трудовому праву в каждой затронутой юрисдикции, и привлечь его нужно до того, как план
  зафиксирован»).
- ch58 Selection criteria: "Four families of criteria are common" followed by an EEOC list of three;
  translated as written.
- ch58 Failure mode "The rolling layoff": "each below a notice threshold, which they can be aggregated to
  cross anyway" is ungrammatical; rendered by sense («хотя при суммировании они всё равно могут его
  превысить»). The English may want "though they can be aggregated to cross it anyway".
- ch58 Integration tree: the diagram labels "Value needs interdependence?" / "Capability needs autonomy?"
  kept in full in Russian («Ценности нужна взаимозависимость?» / «Возможностям нужна автономия?»).
- ch58 Step 5: "three at a site in an EU member state, where four roles are affected" (3 separated, 4
  roles affected) is consistent with halvard.md; kept.
- ch58 Case: "Corvane had flat titles" rendered «должности были без уровней».
- ch58 CTO is glossed «технический директор» at the CTO Perspective section; the earlier mentions are in a
  table and in the case's "chief technology officer".
- Word counts (wc -w; no-break spaces glue some tokens): ch57 6 707, ch58 6 938.

# Translation notes, lane t22 (Chapters 55–56)

Source: English working tree. Files:
`docs/parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.ru.md`,
`docs/parts/13-advanced-problems/56-recovering-a-failing-engineering-organization.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order (identical to the slugified English headings), link targets, citation link
texts, exercise labels, admonition types, Mermaid count and node ids, table rows and every number in
tables identical. No wrapped line starts with a number followed by a period. Words (wc -w; no-break
spaces glue some tokens): ch55 about 6 980, ch56 about 6 700.

Failure Modes: both chapters have only "Early sign(s):" → «Как заметить:» (precedent: ch43, ch49, ch51;
accepted in meaning-check batch 18).

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| exposure (risk in money, board sense) | подверженность риску (exposure); in prose also «язык риска», «чем рискует компания» | B | ch55; ch53's «диапазон возможного ущерба» is the dollar range, ch26's «уязвимость системы» the security sense |
| translator of exposure | CTO переводит инженерные факты на язык риска | T | ch55 mental model |
| board member / director (of a board) | член совета (директоров); «независимый директор» only in tables, following cast.ru | T | ch55, ch56; avoids a clash with the engineering director |
| expert director | член совета — эксперт | T | ch55 |
| pre-meeting decision | решение до заседания | T | ch55 |
| chair (of the board) | председатель (совета) | T | ch55 |
| for decision / for discussion / for information | для решения / для обсуждения / для информации | T | ch55 |
| headline (board page); reliability headline; headline target | главный показатель; главный показатель надёжности; главная цель | T | ch55, ch56; follows quarter-4-briefing.ru «главный показатель для совета директоров» (ch46.ru «главная формулировка» is the board-page wording) |
| the ask | запрос | T | follows notes-t19 |
| acquisition thesis; re-thesis | тезис сделки (acquisition thesis); новый тезис | B | ch55 |
| target (company) | компания-цель | T | ch55 |
| deal team | команда сделки | T | ch55 |
| data room | data room (комната данных) | B/E | ch55 |
| warranty / indemnity / escrow | гарантия (warranty) / возмещение убытков (indemnity) / эскроу (escrow) | B | ch55; per the lane brief; glossary.ru entry says «возмещение» |
| closing condition; material adverse effect | условие закрытия сделки; существенное неблагоприятное изменение (material adverse effect) | T, B | ch55 |
| copyleft license; strongly copyleft | копилефт-лицензия; «сильный копилефт» | T | ch55 |
| license scan; license inventory | сканирование лицензий; перечень лицензий | T | ch55 |
| contributor agreements | соглашения с контрибьюторами | T | ch55 |
| outcome (of a decision); outcome bias | исход; ошибка оценки по исходу (outcome bias) | T, B | ch55; «исход» keeps it apart from «результат (outcome)» in the product sense |
| task conflict | разногласия по существу задачи | T | ch55; notes-t1 «конфликт задачи» is the ch6 typology label |
| top management teams | команды высшего руководства | T | ch55 |
| consensus by fatigue | консенсус от усталости | T | ch55, also a failure-mode name |
| disagree and commit | «не согласен, но действую» (disagree and commit) | B | follows notes-t3 |
| dissent (recorded) | особое мнение; несогласие | T | ch55 |
| What we would have to believe | Во что нам пришлось бы поверить | T | ch55 record field |
| reversal triggers / review date | триггеры пересмотра / дата разбора | T | ch55; «дата пересмотра» (ch20) is a standard's review date |
| counsel (company's) | юристы компании | T | ch55 |
| the engineering pack / the moving definition / asking the board for cover / the diligence surprise / the deal-team yes / outcome-based review / consensus by fatigue | инженерный пакет / плавающее определение / прикрытие у совета / сюрприз на due diligence / «да» команды сделки / разбор по исходу / консенсус от усталости | T | ch55 failure modes |
| failing / declining / underperforming (organization) | проваливается / деградация / работа ниже возможностей | T | ch56; «проваливающаяся» follows the ru nav title |
| turnaround / realignment | вывод из кризиса (turnaround) / перенастройка (realignment) | B | ch56; zone forms «зона вывода из кризиса», «зона перенастройки». The published Russian edition of Watkins may use other words; the maintainer may align |
| triage (organizational) | сортировка (triage) | B | ch56; ch53 already uses «сортировка» |
| stop the bleeding | остановить кровотечение | T | ch56 |
| threat rigidity | ригидность под угрозой (threat rigidity) | B | ch56 |
| capability / trust / people loop | петля возможностей / доверия / людей | T | ch56; «ловушка возможностей» per term base |
| ability / benevolence / integrity (Mayer) | способности / доброжелательность / честность | T | ch56 |
| keep / coach / move / replace | оставить / коучинг / перевести (перевод) / заменить (замена) | T | ch56; heading «Оставить, коучинг, перевод или замена»; in prose «работать через коучинг» |
| two tracks, two clocks | два трека, двое часов | T | ch56 |
| promise ledger | журнал обещаний | T | ch56 |
| incident bridge | созвон по инцидентам | T | follows notes-t19; halvard.ru says «бриджи» |
| commander rotation | график координаторов | T | follows notes-t7 |
| directorates (Halvard) | направления | T | follows notes-t18 |
| the hero arrival / the purge / diagnosis paralysis / the promise binge / one track only / quiet coaching / declaring victory on small counts | явление героя / чистка / паралич диагностики / раздача обещаний / только один трек / коучинг втихую / победа, объявленная по малым числам | T | ch56 failure modes |

Reused: пакет для совета директоров, рамки бюджета, операционный план, комитет по аудиту, due diligence
(комплексная проверка), сервисные кредиты (компенсации по SLA), операционные минимумы, tier 1,
продолжение, выделение на профилактику, аудит серьёзности, переоценка серьёзности, покрытие преемниками,
критические роли, технологический ландшафт, сведения о происхождении, скользящая сумма за четыре
квартала, риск-аппетит, премортем, руководитель разработки высшего уровня, координатор инцидента
(incident commander), интервью об удержании (stay interview), метрики механизмов, журнал
почти-инцидентов, корпоративная политика, вызовы в нерабочее время, «пока нет», хроника года 1,
«Год вкратце», действующие лица, брифинг квартала 4.

## Doubts and notes on the English (English not changed)

- ch55: "Two **standards** make parts of this checkable" — the label is plural; rendered «по двум
  **стандартам**».
- ch55 Yahoo bullet: "Yahoo had failed to maintain controls ensuring its security team's reports were
  assessed for disclosure" rendered «У Yahoo не было работающих механизмов контроля…» (sense of "failed
  to maintain"); «механизм контроля» follows notes-t21.
- ch55 "documented practice, from a regulator's settled findings and the company's filing" is a source
  note inside the label, rendered «по выводам регулятора, зафиксированным при урегулировании дела».
- ch55 Example table: "Six top-40 renewals" kept as a word («Шесть продлений из топ-40»), as in English.
- ch55 Diligence table: ADR-0001 treated as feminine («остаётся открытой»), per notes-t8; the apposition
  moved into parentheses so the agreement reads cleanly.
- ch55 F3 "Place each … in the decision framework" rendered as «к строке таблицы из раздела „Как
  принимать решение“», since the framework is that section's table.
- ch55 Practical Playbook item 10 and Key Takeaway 4 are overlong lines in the source (cosmetic).
- ch56 Example: "a split of 15 or fewer happens by chance about one time in eight" rendered as «15 или
  меньше во втором квартале случайно выпадает примерно в одном случае из восьми» (the second quarter is
  meant).
- ch56 Watkins quotation translated in quotes («располагает к подходу, ориентированному на действие и
  зачастую более директивному»); the English quotes the article.
- ch56 Case: "the one promise" rendered «это и было одно обещание».
- ch56 Several overlong source lines (lines 88, 189, 258, 291, 532, 569, 573, 580); cosmetic.
- ch56 Decision table "Move … often a return to a senior individual-contributor track" rendered «возврат
  на старший уровень трека индивидуального исполнителя».

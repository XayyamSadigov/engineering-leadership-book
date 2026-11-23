# Literary editing notes: chapter 7

File: `docs/parts/02-people-management/07-hiring-and-structured-interviews.ru.md`. Edited from the Russian
text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `git show HEAD:<file>`
(NBSP normalised); link targets, citation link texts, `{ #anchors }`, exercise labels, admonition types,
Mermaid node ids and every number inside tables are identical (diffed). Table text touched in two cells
only («как написано» → «как есть»; «названный бадди, выбрана…» → «назначенный бадди, выбранная…»; «это
вход для проверки» → «это исходные данные для проверки»). One list label renamed to remove a clash:
«**Рекомендации.**» (references) → «**Отзывы рекомендателей.**», because the bullet above uses
«рекомендации» for referrals. A stray mid-paragraph line break in the opening paragraph was removed.
«merge request» → «мерж-реквест» (notes-t1).

Overall: the cleanest of the chapters seen so far in vocabulary; the work was syntax. Research
paragraphs were the heaviest: long sentences with the study as subject, participle chains, and findings
packed into one clause.

## 1. Patterns new beyond glossary section 2a

### 1.1 Study design and finding packed into one participial sentence

English "Students who predicted other students' grades formed confident impressions…" became a
participle («студенты, предсказывавшие…») followed by the finding. Split: design first, finding second.

- «В трёх исследованиях студенты, предсказывавшие оценки других студентов, составляли уверенное
  впечатление даже по интервью, в которых ответы собеседника втайне были случайными.» → «В трёх
  исследованиях студенты предсказывали оценки других студентов. Уверенное впечатление они составляли даже
  по интервью, в которых собеседник втайне отвечал случайным образом.»
- «когда люди, отвечавшие на вопросы с численной оценкой фактов, видели оценки других, их ответы
  сходились» → «Люди численно оценивали факты, и когда они видели оценки других, их ответы сходились»
- «Behroozi с коллегами провели рандомизированный эксперимент с 48 студентами…: когда за решением…» →
  two sentences, design then result.

### 1.2 Nominalised condition: «Добавление X к Y ухудшало…»

- «Добавление неструктурированного интервью к анкетным данным ухудшало прогнозы по сравнению с одними
  анкетными данными.» → «Если к анкетным данным добавляли неструктурированное интервью, прогнозы
  становились хуже, чем по одним анкетным данным.»
- «Перенос этого на итоговые обсуждения — экстраполяция» → «Переносить это на итоговые обсуждения —
  экстраполяция»

### 1.3 Method or document as the agent of a human action

English lets a work sample "ask" and a guide "begin with". Russian wants the person or a passive-free
frame.

- «Рабочее задание (work sample) просит кандидата под наблюдением выполнить часть настоящей работы» →
  «В рабочем задании (work sample) кандидат под наблюдением выполняет часть настоящей работы»
- «Руководство начинает с определения качеств… и использует вопросы двух видов» → «Начинается всё с
  определения качеств, нужных для успеха. Вопросы бывают двух видов…»
- «Долгое молчание теряет тех кандидатов, которых вы хотели.» → «Из-за долгого молчания вы теряете как
  раз тех, кого хотели нанять.»

### 1.4 Pronoun that can point at two people: «тот», «его»

- «Ведущий — не нанимающий руководитель; тот говорит последним.» → «Ведущий — не нанимающий
  руководитель; нанимающий руководитель говорит последним.»
- «ложное обвинение стоит вам хорошего кандидата, и защитить его трудно» («его» = candidate or
  accusation?) → «ложное обвинение лишит вас хорошего кандидата, а отстоять такое обвинение трудно»

### 1.5 Self-contradicting calque in a list label

- «**Адаптация условий по запросу**, предложенная в приглашении, а не только когда кто-то попросит.»
  ("on request… not only when asked") → «**Адаптация условий по запросу**: предложите её уже в
  приглашении, а не ждите, пока кто-то попросит.»

### 1.6 "Counter / Противодействие:" as a repeated field label

Five failure modes each ended «Противодействие: …», a military-bureaucratic word. → «Что делать: …».
«Сигнал:» kept (short, neutral).

### 1.7 Bureaucratic "таковыми не являются" and "в точности"

- «кажутся информативными, хотя таковыми не являются» → «…хотя на деле это не так»
- «Замена вышла через 15 недель, в точности по медиане» → «…точно по медиане»

## 2. Patterns from section 2a, as they appeared here

- Scale openers (2a.2): the three «На уровне…» paragraphs → «Для команды / Для организации / Для высшего
  руководства».
- Connectives (2a.5): «Большинство организаций проходят только середину этого цикла. Без первого блока…»
  → «…Но без первого блока…»; «Это не доказывает… Пример показывает, что затраты…» → «…Пример показывает
  другое: затраты…»
- «решение» (2a.6): «Решения — в решениях к главе 7» → «Разборы упражнений — в решениях к главе 7».
  «Решение во втором квартале» kept: there it is a decision.
- Unclear subject in A1-type tasks: «в ledger команды Billing» (two genitives, "into the ledger of team
  Billing") → «найм на замену — инженера по ledger в команду Billing».

## 3. Three showcase paragraphs

### 3.1 Dana, Dawes and Peterson

**Before.** Если структура лучше, почему большинство инженерных интервью по-прежнему заканчиваются
вопросом «хотел бы я работать с этим человеком»? Dana, Dawes и Peterson предлагают объяснение. В трёх
исследованиях студенты, предсказывавшие оценки других студентов, составляли уверенное впечатление даже
по интервью, в которых ответы собеседника втайне были случайными. Добавление неструктурированного
интервью к анкетным данным ухудшало прогнозы по сравнению с одними анкетными данными. И всё же
большинство участников предпочитали случайное интервью никакому (…). Интервьюер может найти смысл почти
в чём угодно, что говорит кандидат, и это ощущение смысла кажется проницательностью.

**After.** Если структура лучше, почему большинство инженерных интервью по-прежнему заканчиваются
вопросом «хотел бы я работать с этим человеком»? Объяснение предлагают Dana, Dawes и Peterson. В трёх
исследованиях студенты предсказывали оценки других студентов. Уверенное впечатление они составляли даже
по интервью, в которых собеседник втайне отвечал случайным образом. Если к анкетным данным добавляли
неструктурированное интервью, прогнозы становились хуже, чем по одним анкетным данным. И всё же
большинство участников предпочитали случайное интервью отсутствию интервью (…). Интервьюер способен
увидеть смысл почти в любых словах кандидата, и это ощущение смысла кажется ему проницательностью.

### 3.2 Debrief protocol, four details

**Before.** Работает он благодаря четырём деталям. Оценки и заметки подаются до того, как кто-либо
увидит чужие. Ведущий — не нанимающий руководитель; тот говорит последним. Обсуждение идёт по
компетенциям, и каждое утверждение опирается на то, что кандидат сказал или сделал. После обсуждения
оценки можно менять, но исходная сохраняется, чтобы потом увидеть, улучшила ли их дискуссия.

**After.** Работает протокол благодаря четырём деталям. Каждый сдаёт оценки и заметки до того, как
увидит чужие. Ведущий — не нанимающий руководитель; нанимающий руководитель говорит последним.
Обсуждение идёт по компетенциям, и каждое утверждение опирается на то, что кандидат сказал или сделал.
После обсуждения оценки можно менять, но исходные сохраняются, чтобы потом проверить, улучшила ли их
дискуссия.

### 3.3 Case: why Tamsin was not on call

**Before.** К концу базового квартала, примерно через 24 недели после её первого рабочего дня, Tamsin
не была в графике дежурств, и три оставшихся инженера ledger разбирали большую часть вызовов Billing.
Причин было две. Одну рассказывает глава 3: … Другую — эта глава: … Пробел был невидим до оффера, а план
его закрыть был репликой на итоговом обсуждении, а не планом выхода на продуктивность с выделенным
временем. Tamsin — способный инженер; её наняли по неверной мерке, и если считать проблемой её,
организация ничему не научится.

**After.** К концу базового квартала, примерно через 24 недели после первого рабочего дня, Tamsin так и
не вошла в график дежурств, и большую часть вызовов Billing разбирали три оставшихся инженера по ledger.
Причин две. Об одной рассказывает глава 3: … О другой — эта глава: … До оффера пробела никто не видел, а
план его закрыть свёлся к реплике на итоговом обсуждении вместо плана выхода на продуктивность с
выделенным временем. Tamsin — способный инженер, просто её наняли по неверной мерке. Если считать
проблемой её саму, организация ничему не научится.

## 4. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| инженеры ledger / эксперты по ledger | «инженеры по ledger» everywhere | ch 6 uses «инженеры по ledger»; «инженер ledger» reads as a genitive of possession. Applied here |
| рекомендации (referrals) vs рекомендации (references) | referrals: «рекомендации»; references: «отзывы рекомендателей» | the two senses sat in adjacent bullets |
| различение содержания и оценки | «различие между содержанием и оценкой» | «различение» is the act; the chapter means the distinction. Applied in prose and F1 |
| Противодействие (failure-mode "Counter:") | «Что делать:» | register; propose for all chapters with this field |
| панель (interview panel) | keep | understood in HR Russian; «состав интервьюеров» as fallback |
| итоговое обсуждение (debrief) | keep | works; long but clear |
| выход на полную продуктивность (ramp) | keep | notes-t2 |

## 5. Meaning doubts (not changed in meaning; please check against the English)

1. **«в нижней и средней части диапазона 0,60–0,69»** (notes-t2: "low-to-mid .60s"). Kept. Readers may
   take «диапазон» for a statistical range; «около 0,61–0,65» would be friendlier, but it would change a
   number, so not touched.
2. **Sackett 2022.** «большинство процедур, которые раньше были в верхней части списка, там и остались,
   но средние оценки снизились» — unclear whether "mean estimates dropped" for those top procedures or
   for procedures in general. Kept general.
3. **Behroozi.** «результат падал больше чем вдвое» — check the English says performance more than
   halved (not "the failure rate more than doubled").
4. **Tom Becker's objection.** «его инженеров инфраструктуры будут отвлекать в панели интервью»
   rendered «начнут отрывать от работы ради панелей интервью». If the English means his engineers will be
   *drafted onto* panels (not just distracted), both versions fit; if it means panels will interrupt
   on-call infrastructure work, this is fine.
5. **Reflection 2.** «когда-то он сработал на вас» ("it once worked on you") kept literally; the Russian
   is slightly opaque. If the English means "because it once impressed you as a candidate", say so.
6. **References: Google re:Work** «Задокументированное руководство» echoes the evidence label
   "documented practice"; if the English line is just "the published guide", «Опубликованное
   руководство» reads better.

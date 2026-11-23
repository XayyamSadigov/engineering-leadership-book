# Literary editing notes: chapter 14

File: `docs/parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.ru.md`. Edited
from the Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the digit sequence (sorted) is identical to `git show HEAD:<file>`, and
the sorted number tokens differ only in trailing punctuation; link targets, citation link texts,
`{ #anchors }`, exercise labels, admonition types, Mermaid ids and edges, table shapes and every number in
tables are identical (scripted diff). No heading or Mermaid label changed. Two link texts reworded,
targets kept («действующих лиц» → «„Действующие лица“», «операционные расходы» → «операционным
расходам»). Ten non-breaking spaces that were glued to the word *after* a label number («главы 18,⍽который»,
«квартала 2,⍽а», «неделе 16⍽директор», «вместо 4,⍽у», «tier 2⍽и») moved to the label side (2a.8).

Failure modes: the italic label «*Как обнаружить:*» became «*Как заметить:*». This chapter's failure
modes have no countermeasure field, so no «Что делать:» was added (adding one would add content).

## 1. Patterns new beyond glossary section 2a

### 1.1 Idioms of the English source carried over literally

- «**Где расстояние кусается.** … Кусается место.» ("where distance bites") → «**Где расстояние даёт о
  себе знать.** … Дело в месте.»
- «mobile-bff развернули против старой версии контракта» ("deployed against") → «развернули в расчёте на
  старую версию контракта»
- «Требование, обоснованное данными пропусков» ("badge data") → «данными турникетов»
- «Коучинг структурной проблемы тратит кварталы впустую» / «Не коучьте структурную проблему» → «Если
  лечить структурную проблему коучингом…» / «Не лечите структурную проблему коучингом» (kept as the
  failure-mode title, where it is a name)

### 1.2 "Manage the score" → «управлять оценкой»

Russian «управлять оценкой» does not say "game it". Where the sense is gaming, use the term base's
«подгонять» («оценку, которую люди научатся подгонять»); where the chapter's concept is meant, use the
heading's own phrase «оценка, которой управляют».

### 1.3 A list hung on a colon that belongs to another sentence → give the list its own frame

- «Дисфункциональная команда — та, которой… Диагностика начинается с наблюдаемых признаков, потому что…
  ничего не сделать: действия… повторяются…; промахи, о которых…; просьбы о переводе.» (the list mixed
  clauses and bare nouns after a colon that belonged to a different sentence) → «…работать нельзя.
  Признаки такие: …; случаются промахи, о которых…; люди просят о переводе.»
- «Правила, которые сохраняют петлю честной (…):» → «Чтобы петля оставалась честной, нужны правила (…):»

### 1.4 "X is not Y, which…" contrast → «Не путайте X с Y»

- «Проверка здоровья — это не опрос об опыте разработчиков из главы 18, который анонимно измеряет…» →
  «Не путайте проверку здоровья с опросом об опыте разработчиков из главы⍽18. Опрос анонимно измеряет…»

### 1.5 Long consequence lists after "Signals to every other manager" → two conditional sentences

- «Замена руководителя сообщает всем остальным руководителям, что организация терпит: слишком поздно —
  значит, результативность не важна; без предварительных ожиданий — значит, следующим может стать любой.»
  → «Замена руководителя показывает всем остальным руководителям, что организация готова терпеть. Если
  замена запоздала, они поймут, что результативность не важна; если ожиданий заранее не задали — что
  следующим может оказаться любой.»

## 2. Two showcase paragraphs

### 2.1 Evidence synthesis after the research table

**Before.** Это **научные результаты**, каждый — по одной организации; исследования пандемийного
периода измеряют вынужденное и внезапное изменение. Вместе они согласуются лучше, чем публичный спор.
Гибридный формат с несколькими днями дома в единственном рандомизированном исследовании не стоил ничего
измеримого и помог удержанию. Полная удалёнка в масштабе ослабляет связи между группами и повышает
стоимость координации. Близость передаёт обратную связь от опытных инженеров новичкам.

**After.** Это **научные результаты**, но каждый получен в одной организации, а исследования
пандемийного периода измеряют вынужденную и внезапную перемену. Вместе они согласуются лучше, чем можно
подумать по публичному спору. В единственном рандомизированном исследовании гибридный формат с
несколькими днями дома не обошёлся ни во что измеримое и помог удержанию. Полная удалёнка в масштабе
компании ослабляет связи между группами и удорожает координацию. Через близость обратная связь доходит
от опытных инженеров до новичков.

### 2.2 Case, health check

**Before.** Обычно за пределы комнаты выходят только закономерности и запросы. Поскольку от них зависело
структурное решение, обе группы согласились в этот раз показать свои оценки Daniel и директору.

**After.** Обычно за пределы комнаты выходят только закономерности и запросы. Но на этот раз от оценок
зависело структурное решение, и обе группы согласились показать их Daniel и директору.

(«от них» in the original grammatically pointed to «закономерности и запросы», not to the scores.)

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| фасилитировать / провести фасилитацию | «вести (сессию)», «ведущий» in prose; keep «фасилитируемые ретроспективы / воркшопы» as category names | notes-t2 already uses «ведущий» for facilitator (ch7); «провести фасилитацию» is jargon |
| малорисковый вариант по умолчанию | «вариант по умолчанию с низким риском» | «малорисковый» reads as finance jargon; changed in both places (book position, takeaways) |
| опорные (офисные) дни | keep | consistent with notes-t3 |
| удалёнка | keep in this chapter | colloquial but the established word; the chapter uses it consistently and it reads naturally with «полная удалёнка» |
| Как обнаружить → Как заметить | adopted | per the maintainer's label decision for Failure Modes |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Reflection question 1.** «Если бы самое важное решение… принималось, когда все работали удалённо, кто
   узнал бы о нём позже, чем узнал на самом деле?» Logically odd: if everyone were remote, the people
   who heard late in reality (Bogotá) would hear *sooner*. If the English asks "who would have heard
   about it sooner", the Russian is inverted. Kept unchanged.
2. **Bogotá office.** «не более чем в часе от Миннеаполиса» rendered «разница во времени с Миннеаполисом не
   больше часа», following «Площадки Northstar разделяет час» in the async section. If the English means
   flight time, revert.
3. **Why this matters, organization paragraph.** The opener «На уровне организации большинство
   организаций…» was dropped to avoid the repetition; the scale is still clear from «организаций из
   50–150 инженеров».
4. **Leadership diagnosis.** «Сопутствующий фактор; ожиданий… ему никто никогда не задавал» rendered as two
   sentences joined by «При этом». If the English presents the missing expectations as the reason the
   leadership factor is only contributing, «потому что» would be more exact.
5. **Trade-off «Работа в одном месте против пула найма».** «Один офис покупает случайные контакты и
   менторство и теряет кандидатов; в … исследовании дни дома снизили число увольнений» rendered with «к
   тому же» before the RCT clause: it reads as a second cost of a single office (losing the retention
   benefit). Check that this is the English logic.

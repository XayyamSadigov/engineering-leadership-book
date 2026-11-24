# Literary editing notes: chapter 29

File: `docs/parts/06-technical-leadership/29-staff-and-principal-engineers.ru.md`. Edited from the Russian text
only; the English chapter was not opened. The file was not yet committed, so the pre-edit copy was kept in the
session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (189 tokens,
NBSP normalised); link targets, `{ #anchors }`, heading order, exercise labels, admonition lines, every table
line, citations and Mermaid blocks are identical. About 65 sentence-level edits. Failure modes in this chapter
are prose (no «Как заметить:» fields in the source), and stay prose. Two NBSPs moved to the label side
(«неделях 12⍽и 13⍽директор» → «неделях⍽12 и⍽13 директор»); «глава⍽N» kept with the label.

The section 2a patterns appeared as expected (missing connectives, counts announced and then given as bare
sentences, «Кроме того» for the second of two). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «Это видно, когда…» as the opener of a detection sentence

English "Detect it when…" became a repeated «Это видно, когда…», which has no clear antecedent for «Это».
Use the noun «Признак:» or a direct imperative.

- «Это видно, когда инженеры называют staff-инженера тем, кто решает, чем они займутся на неделе.» →
  «Признак: инженеры говорят, что решать, чем им заниматься на неделе, — дело staff-инженера.»
- «Проверить можно, спросив, чем staff-инженер будет владеть…» → «Проверка простая: спросите, чем
  staff-инженер будет владеть…»

### 1.2 Mixed parallel series of cross-references

English lists "X is in Chapter 4; Chapter 8 covers Y; Z — Chapter 28" with three syntaxes in one sentence.
Pick one frame and keep it.

- «…— в главе 4 (…); карьерные лестницы и повышения разбирает глава 8; распределение архитектурных прав на
  решения и записи решений — глава 28 (…)» → «…— в главе⍽4 (…), карьерные лестницы и повышения — в
  главе⍽8, архитектурные права на решения и записи решений — в главе⍽28 (…)»

### 1.3 A chapter or document as the actor of a story event

Extends chapter 25 pattern 1.5 to cross-chapter narration: «Глава 10 планирует разговор, в котором
директор…» makes the chapter a character.

- «Глава 10 планирует разговор, в котором директор поднимает с Ines вопрос…» → «В главе⍽10 директор
  готовит разговор с Ines о её поведении на ревью.»
- «Этот пример — диагностика Northstar… с помощью инструментов этой главы» → «В этом примере инструменты
  главы применены к Northstar… для диагностики.»
- «Считать паттерн критика структурной проблемой — рекомендация этой главы, но она не гарантирует, что
  Ines её примет» (two pronouns, two referents) → «Глава рекомендует считать паттерн критика структурной
  проблемой, но эта рекомендация не гарантирует, что Ines примет такой взгляд…»

### 1.4 Zeugma: one verb with a spatial and a temporal object

- «когда домен охватывает несколько областей ответственности staff-уровня и несколько лет» → «когда
  находится домен шире нескольких областей ответственности staff-уровня, с горизонтом в несколько лет»

### 1.5 Tautology with the term «запись решения»

- «записывает обоснование границ в запись решения» → «фиксирует обоснование границ в записи решения»

### 1.6 Verbless fragments used as failure-mode signatures

English noun fragments ("Every incident, every question, and no finished durable work") read as broken
Russian. Give them a head noun.

- «Каждый инцидент, каждый вопрос и ни одной законченной долговечной работы.» → «Участие в каждом
  инциденте, ответ на каждый вопрос — и ни одной законченной долговечной работы.»

## 2. Two showcase paragraphs

### 2.1 Principal levels: two caveats

**Before.** Здесь два предостережения. Роль principal оправдывает проблема соответствующего масштаба, а не
стаж. В компании с одним продуктом и восемьюдесятью инженерами редко найдётся домен, который не удержит
staff-инженер с хорошим спонсором. Кроме того, чем выше уровень, тем сильнее тянет к архитектуре указами.
Principal-инженеры сохраняют доверие, участвуя в ревью дизайна и разборах инцидентов на реальной работе и
продолжая немного писать код.

**After.** Здесь два предостережения. Первое: роль principal оправдывает проблема соответствующего масштаба,
а не стаж. В компании с одним продуктом и восемьюдесятью инженерами редко найдётся домен, который не по силам
staff-инженеру с хорошим спонсором. Второе: чем выше уровень, тем сильнее тянет управлять архитектурой с
помощью указов. Доверие principal-инженеры сохраняют, когда участвуют в ревью дизайна и разборах инцидентов
на реальной работе и продолжают понемногу писать код.

### 2.2 CTO as sponsor of last resort

**Before.** А поскольку полномочия staff-инженера взяты взаймы через спонсора, CTO — спонсор последней
инстанции. Отмена решения principal-инженера в коридоре урезает полномочия каждого staff-инженера.
Дисциплина руководителя высшего уровня в том, чтобы спорить тем же письменным путём, которым пользуются
руководители.

**After.** А поскольку полномочия staff-инженера взяты взаймы через спонсора, CTO — спонсор последней
инстанции. Если CTO отменяет решение principal-инженера в коридорном разговоре, он урезает полномочия
каждого staff-инженера. Поэтому от руководителя высшего уровня требуется дисциплина: спорить тем же
письменным путём, которым пользуются остальные руководители.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| долговечная работа (durable work) | keep for consistency; consider «работа с долгим эффектом» | «долговечная» fits things, not work; used five times, so left as is |
| паттерн критика | keep | reads as a term after the first use |
| «даёт информацию» (provides input) | «с ним только советуются» | aligned the mental-model blockquote with the scope list, which already uses this phrasing |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **Roaming critic, "What it looks like".** «Замечания на ревью отклоняют без объяснения причин» read as
   "his review comments get rejected". From the failure-modes section («Отказы без причин») the critic is the
   one rejecting. Rendered «На ревью человек отказывает без объяснения причин». Confirm.
2. **Example, info box: «После изменений во владении, серьёзности и перехода…».** «изменений в серьёзности»
   is unclear (severity definitions? re-rating?). Not changed; the same box sits in chapter 30.
3. **«делятся с командами»** (domain outcomes) rendered «заслугу за них staff-инженер делит с командами».
   Assumes "shared with teams" means attribution.
4. **Example, Ines's eight hours.** «Восемь часов… остались на уровне базового квартала» rendered «по-прежнему
   отнимают восемь часов, как и в базовом квартале», hours per week implied by the table. Confirm the
   baseline figure is also eight per week.
5. **«Решатель… глубоко погружается в трудные задачи, одну за другой»** reordered to «берётся за трудные задачи
   одну за другой… и глубоко в них погружается». Same claim.

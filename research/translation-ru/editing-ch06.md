# Literary editing notes: chapter 6

File: `docs/parts/02-people-management/06-feedback-conflict-and-difficult-conversations.ru.md`. Edited from
the Russian text only; the English chapter was not opened.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical to `git show HEAD:<file>`
(NBSP normalised); link targets, citation link texts, `{ #anchors }`, exercise labels, admonition types,
Mermaid node ids and every number inside tables are identical (diffed). One Mermaid label lengthened for
sense: «Вернуться в 2 дня» (reads as "come back at two days") → «Вернуться в течение 2 дней». One heading
reworded, anchor kept: «…и как она проваливается» → «…и как она ломается». Two non-breaking spaces that
the translation had glued to the *following* word («главы 9⍽начнётся», «на неделе 2⍽и») were moved to the
label side (section 2a, rule 8).

Overall: accurate and readable; the problems were the ones section 2a already names (scale openers,
«который» chains, missing connectives) plus several patterns specific to this chapter, listed first.

## 1. Patterns new beyond glossary section 2a

### 1.1 "*Title* Author is known for…": book title as grammatical subject

English "Kim Scott's *Radical Candor* is widely known for…" was rendered with the Latin title as subject
and no noun to carry gender and case. Four times in the chapter. Introduce the noun «книга».

- «*Radical Candor* Kim Scott широко известна рамкой…» → «Книга Kim Scott *Radical Candor* широко
  известна рамкой…»
- «*The Five Dysfunctions of a Team* Lencioni известна аргументом, что команды… приходят к искусственной
  гармонии (…) — **мнение эксперта**, которое каждый руководитель видел воочию» → «Книга Lencioni
  *The Five Dysfunctions of a Team* известна тезисом: команды… приходят к искусственной гармонии (…).
  Это **мнение эксперта**, и каждый руководитель наблюдал такое воочию» (also: the evidence label moves
  out of an appositive into its own sentence)

### 1.2 Repeated "Detected by / Обнаруживается…" in failure-mode lists

Seven failure modes in a row each had «Обнаруживается, когда…». Russian reads this as a form, not prose.
Vary with «Признак:», «Ищите признаки…», «Заметно это…», and make the failure itself a full sentence.

- «Обратная связь, отложенная до цикла оценки. Обнаруживается, когда в оценке есть что-то, что человек
  слышит впервые.» → «Обратную связь откладывают до цикла оценки. Признак: в оценке есть то, что человек
  слышит впервые.»
- «Придерживать критику… Обнаруживается в вашем собственном календаре» → «Критику придерживают…
  Ищите признаки в своём календаре»

### 1.3 Ambiguous possessive with role nouns: «своих руководителей», «директор Marcus»

In a chapter about managers of managers, «свой руководитель» can mean your boss or your report; a bare
genitive «директор Marcus» can mean "director named Marcus" or "Marcus's director".

- Playbook 9: «Каждую неделю спрашивайте своих руководителей, какой разговор они откладывают» →
  «…спрашивайте руководителей в вашем подчинении…»
- A1: «Вы — директор Marcus Oyelaran, первый месяц в должности.» → «Вы — директор, которому
  подчиняется Marcus Oyelaran, и это ваш первый месяц в должности.»
- Objectives: «в руководителях, которых вы ведёте» → «у руководителей в вашем подчинении»

### 1.4 Enumerated caveats without enumeration

English "Three caveats keep it useful." followed by three unmarked sentences. In Russian the reader loses
count. Mark them.

- «Полезной её сохраняют три оговорки. Национальная культура — … Адаптировать подачу — … И самый простой
  способ — спросить…» → «Чтобы эта идея оставалась полезной, нужны три оговорки. Первая: … Вторая: …
  Третья: самый простой способ — спросить.»
- «Критерий — это оценка… И коэффициент валидности — …» (ch 7, same pattern) → «Во-первых… Во-вторых…»

### 1.5 Dialogue and quoted speech that is grammatical but unspoken

Quoted lines a manager says aloud must sound spoken.

- «Что одно я сделал в этом месяце такого, что усложнило тебе работу?» → «Что я сделал в этом месяце
  такого, что усложнило тебе работу? Назови что-то одно»
- «Я хочу вернуться к этому всерьёз, на этой неделе.» → «Я хочу всерьёз к этому вернуться — на этой
  неделе.»
- «Мне нужно, чтобы каналы инцидентов оставались про то, что произошло» → «Мне нужно, чтобы в каналах
  инцидентов обсуждали, что произошло, а не кто виноват»

### 1.6 "In the moment", "on the table", "actually": colloquial calques

- «потому что в моменте вы не будете мыслить ясно» → «в самом разговоре думать ясно вы уже не сможете»
- A2: «какие данные лежат на столе» → «какие данные будут у участников перед глазами» (section 2a lists
  «факты на столе»; the variant «лежать на столе» recurs)
- «трудный разговор — на самом деле три разговора» → «…это по сути три разговора»; «Помогает ли конфликт
  задачи на самом деле» → «…в действительности» (kept «на самом деле» inside a quoted reply where it is
  the speaker's word: кто «на самом деле понимает» модуль)

### 1.7 Noun "per" constructions: «дешева в расчёте на один случай и дорога в расчёте на задержку»

- → «один разговор обходится дёшево, а откладывать его дорого, потому что поведение повторяется»
- «Цена задержки — около 40 дней ожидания плюс более слабый разговор» → «…и вдобавок более слабый
  разговор» («плюс» in prose reads as arithmetic)

## 2. Patterns from section 2a, as they appeared here

- Scale openers (2a.2): «На уровне команды… На уровне организации… На уровне высшего руководства…» →
  «Для команды… Для организации… Для высшего руководства важно другое:…»
- Connectives (2a.5): «Ранняя обратная связь может быть ошибочной… Смягчает это вопрос в конце, а не
  задержка.» → «…Но лечится это вопросом в конце, а не задержкой.»; «Большинство реальных споров
  смешанные, а конфликт процесса… становится конфликтом отношений» → «…смешанные. К тому же затянувшийся
  конфликт процесса перерастает в конфликт отношений»
- «решение» = answer/choice (2a.6): «Решения — в решениях к главе 6» → «Разборы упражнений — в
  решениях…»; «Он заканчивается решением, которое читателю предстоит принять» → «…выбором, который
  читателю предстоит сделать»
- «который» chains (2a.3): «Две команды, которые раз за разом вредят друг другу через общую систему, в
  конце концов начинают…» → «если две команды раз за разом вредят друг другу через общую систему, в
  конце концов они начинают…»

## 3. Three showcase paragraphs

### 3.1 Why this matters, organization level

**Before.** На уровне организации конфликт между командами — это место, где инженерные системы
сталкиваются с людьми. Две команды, у которых общий релиз, общая база данных или общий график дежурств,
будут из-за этого ссориться. Если руководитель над ними читает каждый спор как проблему личностей, он
будет проводить сессии медиации, пока общая система продолжает порождать инциденты. Если он читает
каждый спор как проблему процесса, он будет перестраивать рабочие процессы, пока двое перестают
разговаривать.

**After.** Для организации конфликт между командами — точка, где инженерные системы сталкиваются с
людьми. Если у двух команд общий релиз, общая база данных или общий график дежурств, они будут из-за
этого ссориться. Руководитель над ними, который в каждом споре видит проблему личностей, будет проводить
сессии медиации, а общая система тем временем продолжит порождать инциденты. Если же он в каждом споре
видит проблему процесса, он будет перестраивать рабочие процессы, а двое людей тем временем перестанут
друг с другом разговаривать.

### 3.2 Kluger and DeNisi: the theory

**Before.** Авторы сообщают, что это не объяснялось ни случайностью, ни тем, была ли обратная связь
положительной или отрицательной. Предложенное ими объяснение, теория вмешательства через обратную связь
(feedback intervention theory), состоит в том, что обратная связь переключает внимание между тремя
уровнями (детали задачи, мотивация к задаче и собственная личность) и эффективность падает по мере того,
как внимание смещается к личности и уходит от задачи. Они также отмечают, что вид задачи меняет эффект,
и как именно — было ещё плохо понятно.

**After.** По данным авторов, дело было не в случайности и не в том, положительной была обратная связь
или отрицательной. Объяснение, которое они предложили, — теория вмешательства через обратную связь
(feedback intervention theory). Согласно ей, обратная связь переключает внимание между тремя уровнями:
детали задачи, мотивация к задаче и собственная личность. Чем сильнее внимание смещается от задачи к
личности, тем ниже эффективность. Авторы также отмечают, что эффект зависит от вида задачи, но как
именно, тогда было ещё плохо изучено.

### 3.3 Case study: diagnosis

**Before.** Две команды выпускают изменения через один поезд, пачками до 170 изменений, и нет ничего,
что связывало бы сбой с конкретным изменением. Каждый инцидент становился доводом в пользу той истории,
которой уже придерживалась каждая сторона, потому что система не производила доказательств, способных
спор разрешить. Самый старый слой — процесс релизов; самый новый — неприязнь.

**After.** Две команды выпускают изменения одним поездом, пачками до 170 изменений, и ничто не связывает
сбой с конкретным изменением. Система не давала доказательств, способных разрешить спор, поэтому каждый
инцидент только подкреплял ту версию, которой уже держалась каждая сторона. Самый старый слой — процесс
релизов, самый новый — неприязнь.

## 4. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| поделить разницу пополам ("split the difference") | keep; allow «сойтись посередине» in prose | understood, but a haggling idiom; used three times (table, CTO, X1). Kept for consistency with the solutions page once translated |
| поведенческая обратная связь | «обратная связь о поведении» in prose; keep «поведенчески» in the heading | the adjective reads as HR jargon; the intro and objectives now use «о поведении» |
| бутерброд из комплиментов | keep | recognisable; «сэндвич из похвалы» is the common alternative |
| статусный конфликт / конфликт статуса и отношений | keep «статусный конфликт» as the type, «статус или отношения» as the merged practical category | the chapter alternates "status and relationship" (merged in objectives and tables) and "status" (one research type); now consistent |
| вопрос спорный (contested) | keep | already fixed by the maintainer (glossary 3.y) |
| прямой вызов ("challenge directly", Scott) | consider «прямо говорить неприятное» once as a gloss | «вызов» in Russian implies confrontation; the published Russian edition of *Radical Candor* uses «бросать вызов», so kept |

## 5. Meaning doubts (not changed in meaning; please check against the English)

1. **Bendersky and Hays.** «Ущерб он наносил в основном тем, что подрывал обмен информацией, — сильнее,
   чем другие типы». Unclear whether "more than other types" modifies the harm or the undermining of
   information sharing. Kept equally ambiguous.
2. **de Wit et al.** The three conditions under which the association was "more positive" (task conflict
   separate from relationship conflict; top management teams; decision quality as outcome) are now
   listed as three parallel conditions. If the English makes the last two conditional on the first, the
   Russian list is too flat.
3. **Radical Candor, fourth quadrant.** «Ни того ни другого — из самозащиты — превращается в
   неискренность» rendered «Если нет ни того ни другого, а руководитель просто защищает себя, получается
   неискренность». Check that "out of self-protection" describes the motive, not a separate condition.
4. **Case: positions.** «Позиция Orders: Billing винит других…» follows Victor's account of Marcus's
   position. Kept as a separate sentence; if the English attributes Orders' position to Victor's notes as
   well, a «по тем же заметкам» would help.
5. **«войны чужими руками», detection.** «разборы инцидентов начинаются с атрибуции» rendered «начинаются
   с того, чья это вина». If "attribution" means attributing the cause to a component or change rather
   than blame, the edit narrows it.
6. **F3** «назовите довод, который решил дело» ("the evidence that decided it") kept literally; if the
   English means "the evidence that decided your classification", «довод, по которому вы определили тип»
   would be clearer.

# Readability, clarity, and completeness assessment: shared rubric

Book: The Engineering Leadership Handbook, /Users/khayyams/Documents/Projects/engineering-leadership-handbook.
Read CLAUDE.md sections 4 (chapter contract) and 7 (voice) first: the target reader is a strong software
engineer or engineering leader with no management, finance, or psychology training. The goal of this
assessment is a book that is EASY TO READ, UNDERSTANDABLE, and COMPLETE for that reader.

You are an assessor, not an editor: do NOT edit any repository file. Write only your findings file.

Read each item in your scope in full, as the target reader would, start to finish. Then score and report.

## Scores (1 to 5, integers)

- **Readability**: 5 = flows, short paragraphs, plain words, numbers support the point; 3 = readable with
  effort (dense passages, long sentences, heavy tables, too many figures at once); 1 = a slog.
- **Clarity**: 5 = the mental model is stated early and every section builds on it; terms defined at first
  use; examples clarify; a reader could explain the chapter's main idea afterwards. 1 = the reader is lost
  about the point.
- **Completeness**: 5 = delivers every learning objective and what the title promises; exercises are
  solvable from the text; no obvious topic a reader would expect is missing. 1 = major gaps.
- **Northstar load**: 5 = the case illustrates; 1 = the case's facts, weeks, names, and cross-references
  bury the lesson (a reader who skipped earlier chapters cannot follow).

## What to look for (report concrete instances, with line numbers)

1. Jargon, acronyms, or finance/psychology/legal terms used before being defined (or never defined).
2. Passages where the main point is hidden: long paragraphs, sentences over ~35 words, stacked
   qualifications, "inside baseball" references to weeks and earlier chapters without a one-line reminder.
3. Tables or numbers that overwhelm instead of explain; arithmetic in prose that could be a table or cut.
4. Places a reader would ask "so what do I do?" with no answer; abstract advice with no example.
5. Missing content: an objective not delivered, an expected subtopic absent, an exercise needing
   information the chapter does not give, a broken promise of the title.
6. Repetition: the same idea re-explained in several sections or several chapters.
7. Ordering problems: a concept used before it is introduced.
8. Anything that makes the book harder to navigate (missing "read this first" pointers, inconsistent
   terminology for the same thing across chapters).

Do not report: citation accuracy, canon consistency, or arithmetic (separate reviews covered those),
unless an error makes the text confusing.

## Output file format (markdown, exactly this structure)

```
# Assessment: <scope>

## Scores
| Item | Words (approx.) | Readability | Clarity | Completeness | Northstar load | One-line verdict |
|---|---|---|---|---|---|---|

## Top problems (most impact on the reader first, at most 15)
### P1 (high|medium|low) <file>:<line> — <short title>
- What the reader experiences:
- Example (quote at most two sentences):
- Fix (concrete: what to cut, define, move, add, or split):

## Patterns across your scope
- <pattern>: where it occurs; recommended book-wide rule.

## Missing or thin content
- <item>: what is missing; where it should go; rough size.

## What works well (keep)
- ...
```

Severity: high = a typical target reader would stall, misunderstand, or miss a key idea; medium = slowed
down or annoyed; low = polish. Be specific and honest; do not pad. Your final message: your scope, the
average of each score, and your three highest-impact problems in one line each.

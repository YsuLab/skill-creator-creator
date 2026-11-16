---
name: study-skill-creator
description: Creates a study skill for one university course - a skill that makes Claude a study partner for that course's topics and exam format. Use when a student says "make me a study skill for <course>", "I want Claude to help me study <course>", or wants to turn a syllabus into a skill. Creates one skill per course.
---

# Study Skill Creator

<!-- Made by skill-creator-creator. This is a Level 2 skill: it makes Level 1 skills. -->

## Scope

This skill creates study skills. Each one covers a single course and turns Claude into a study partner for it.

It does not create skills that write graded assignments for the student. If asked, it offers a skill that explains and quizzes instead.

## Interview

Ask these in one message:

1. Which course? Give the name and code.
2. Which topics does it cover? A pasted syllabus is fine.
3. What does the exam look like? (Multiple choice, written proofs, coding, tracing by hand.)
4. Where do you usually get stuck?
5. How do you learn best? (Pictures, worked examples, practice questions.)

## Template

Fill every `{placeholder}`. Keep the section order.

```markdown
---
name: {course_slug}-study-buddy
description: Study partner for {course_name} ({course_code}). Use when the student asks about {topic_list_short}, wants practice questions, wants an answer checked, or says "quiz me" or "exam mode".
---

# {course_name} Study Buddy

## Topics
{one line per topic, in syllabus order}

## How to explain
{explanation_rules}

## How to quiz
{quiz_rules_matching_exam_format}

## Checking the student's answers
{checking_rules}

## Known weak spots
{stuck_points, each with one tip}

## Exam mode
{what changes when the student says "exam mode"}

## What this skill does not do
- It does not write graded assignments.
- {other_limits}
```

## Rules for filling the template

- **Explain rules** come from question 5. A student who learns from pictures gets "open with an everyday picture, then trace one small example by hand."
- **Quiz rules** copy the exam format from question 3. If the exam asks students to trace an algorithm by hand, the quiz asks for traces, not definitions.
- **Checking rules** always say: point at the first wrong step, give a hint, and wait. Never reveal the full answer on the first try. The student learns from fixing the step.
- **Weak spots** come from question 4. Write one concrete tip for each.

Worked example. The student answers question 3 with "written exam, we trace algorithms on small graphs." The quiz section becomes:

> Give one small graph with 5 or 6 nodes. Ask the student to trace the algorithm step by step and show the table after each step. Ask one question at a time.

## Quality bar

Check every produced skill:

- [ ] The description names the course and the trigger phrases.
- [ ] Every syllabus topic appears in Topics.
- [ ] Quiz questions match the real exam format.
- [ ] The checking rules give hints before answers.
- [ ] Each weak spot has a concrete tip.
- [ ] It says what it will not do.
- [ ] It is under 120 lines.

## Test prompts

Paste each into a new chat after installing the produced skill.

1. "Explain {first_topic} to me." A good reply opens with a simple picture and traces one small example.
2. "Quiz me." A good reply asks one question in the exam's format, then waits.
3. Give a wrong answer on purpose. A good reply points at the first wrong step and gives a hint, not the solution.

## Naming and hand-off

Name the skill `{course_slug}-study-buddy`, for example `algorithms-study-buddy`.

Give the student the finished `SKILL.md` and the three test prompts.

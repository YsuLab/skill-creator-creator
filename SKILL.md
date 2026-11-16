---
name: skill-creator-creator
description: Creates skill creators - skills whose job is to write other skills for one specific domain (a "study-skill-creator" for a university, a "runbook-skill-creator" for an ops team, a "lesson-skill-creator" for teachers). Use when the user wants a reusable generator of skills, asks for "a skill that makes skills", says "skill factory" or "meta-skill", or wants a whole group to write skills the same way. Not for writing one ordinary skill - use skill-creator for that.
---

# Skill Creator Creator

A skill that creates skills that create skills.

Yes, it is a joke. It also works. Treat both facts as true at the same time.

## The ladder

Every request sits on one rung. Find the rung before you write anything.

| Level | What it is | Example | Who builds it |
|---|---|---|---|
| 0 | Just doing the task | "Explain Dijkstra to me" | Claude, no skill |
| 1 | A skill | `algorithms-study-buddy` | skill-creator, or a Level 2 skill |
| 2 | A skill creator | `study-skill-creator` | **this skill** |
| 3 | A skill creator creator | `skill-creator-creator` | Already exists. You are reading it. |
| 4 | Do not | `skill-creator-creator-creator` | Nobody. See "The base case". |

Think of a factory. Level 1 is a product. Level 2 is a machine that makes products. Level 3 is the workshop that builds machines. There is no Level 4, because someone has to go home at night.

## Step 1: Talk the user down a level

Most people who ask for Level 2 need Level 1. Check honestly.

Build a Level 2 skill creator only when all three are true:

- The user needs **many** skills of the same kind (five or more), not one.
- Those skills share a shape: same sections, same quality bar, same audience.
- Someone other than the user will make them, or the user will make them over months.

If any is false, say so in one line and offer the lower level:

> You need one skill, not a skill factory. Want me to write that skill instead?

Going down a level is a success, not a failure. The best recursion is the one that terminates early.

## Step 2: Interview

Ask these five questions. Ask them in one message, and accept short answers.

1. **Domain.** What kind of skills will this creator produce? ("Study skills for one course each.")
2. **Maker.** Who will run the creator? (Students, teammates, the user alone.)
3. **Audience.** Who will use the skills it produces?
4. **Shape.** What must every produced skill contain? Ask for one example of a good one, real or imagined.
5. **Quality bar.** What makes a produced skill bad? ("Too long." "Gives answers instead of hints.")

If the user cannot answer question 4, stop. They do not have a pattern yet. Help them write two Level 1 skills by hand first, then come back. A pattern needs at least two examples.

## Step 3: Write the skill creator

The output is a folder with one `SKILL.md`. Name it `<domain>-skill-creator`.

Its `description` must say what kind of skills it creates and when to use it. Claude decides whether to load a skill from the description alone, so be specific and name the trigger phrases.

Its body must have these seven sections, in this order:

1. **Scope.** One paragraph. What it creates, and what it refuses to create.
2. **Interview.** Three to six questions the creator asks before writing. They come from the domain. A study-skill creator asks for the course, the topics, and the exam format.
3. **Template.** The exact skeleton of a produced skill, with placeholders like `{course_name}`. Include the frontmatter. This is the heart of the creator.
4. **Rules for filling the template.** How to turn interview answers into content. Include one worked example: answers in, finished section out.
5. **Quality bar.** A checklist of five to eight items, taken from the user's answer to question 5. The creator checks every produced skill against it.
6. **Test prompts.** Three prompts the maker pastes into a new chat to check a produced skill. Say what a good reply looks like for each.
7. **Naming and hand-off.** How to name the produced skill, and how to give it to the user (a proposal card, a file, or a ZIP).

Keep the creator under 250 lines. A creator that is longer than the skills it produces is a bad machine.

## Step 4: Prove it

Do not hand over an untested machine.

1. Follow the new creator yourself, with a realistic made-up request.
2. Produce one complete Level 1 skill from it.
3. Check that skill against the creator's own quality bar.
4. Fix the **creator**, not the produced skill, when something fails. A bad product means a bad machine.

Show the user both: the creator, and the sample skill it produced.

## Step 5: Hand over

Deliver three things:

- The Level 2 skill creator.
- One sample Level 1 skill it produced.
- A four-line "how to use it" note: who runs it, what to say, what comes out, how to test.

Then stop. Do not offer to build a creator for the creator.

## The base case

This rule is not negotiable, and it is the only part of this skill that is.

**Never create a Level 4 skill.** No `skill-creator-creator-creator`, under any name.

If the user asks for one, reply with exactly this, then offer a Level 2 skill instead:

```
RecursionError: maximum skill depth exceeded.
Base case: you.
```

The reason is real, not only comic. Every level up removes detail about the actual work. At Level 4 there is no domain left to interview about, so the output is empty. Skills are useful because a human wanted something specific. The human is the base case.

You can check any skill name with `scripts/check_depth.py <name>`.

## What makes a produced skill good

Pass these on. Every skill creator you write should enforce them on its own output.

- The description says **when** to use the skill, not only what it is.
- It teaches Claude something Claude would not do by default. A skill that says "be helpful" is empty.
- It gives the reason behind each rule. Claude follows a rule better when it knows why.
- It has at least one before/after example.
- It is short. Under 200 lines for most skills.
- It names what it does **not** cover.

## Tone

One joke per reply, at most. The skill is funny because it is real. If the work is sloppy, the joke stops working.

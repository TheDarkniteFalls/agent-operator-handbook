# Example: A Bounded Writing Revision

This synthetic example shows how a non-coder can use an agent to revise a novel
outline without giving it authority over the manuscript or established canon.

## Project Card

- **Project name:** *Harbor of Glass*, Book Two outline revision
- **Desired result:** Move the storm confrontation from chapter 19 to the
  midpoint, then repair the surrounding outline so cause and effect still make
  sense.
- **Audience:** The author preparing the next manuscript draft.
- **Current as of:** Outline checkpoint 3.

## Source of Truth

- `series-bible.md` defines established characters, rules, and chronology.
- `book-two-outline.md` is the only file approved for revision.
- `editor-notes.md` explains why the confrontation should move earlier.

If the editor notes conflict with the series bible, the series bible wins and
the conflict must be reported.

## Authority

- The agent may read all three named files.
- It may propose an updated chapter map before editing.
- After approval, it may change only `book-two-outline.md`.
- It must not change the series bible, editor notes, manuscript chapters, title,
  publication files, or public descriptions.
- It must ask again if the proposal changes the ending, point-of-view structure,
  or an established fact.

## Definition of Done

- The storm confrontation occurs between chapters 11 and 13.
- The setup appears before it and the consequences appear afterward.
- The mentor still disappears before chapter 8.
- The protagonist still loses radio access after chapter 9.
- No manuscript or canon file changes.
- The handoff names any creative choice that remains with the author.

## Starting Request

```text
Start read-only. Compare the series bible, current outline, and editor notes.
Show me a proposed before-and-after chapter map for moving the storm
confrontation to the midpoint. Identify every dependency that would need to
move, any canon conflict, and any creative decision you cannot safely make.
Do not edit anything until I approve the proposal.
```

## Evidence to Review

Before accepting the revision, the author asks for:

- the approved before-and-after chapter map
- a list confirming that only `book-two-outline.md` changed
- a short table matching the four required story facts to their final outline
  locations
- any unresolved pacing or character-choice question
- confirmation that nothing was submitted or published

## Example Handoff

- **Result achieved:** The confrontation now occurs in chapter 12, with setup
  moved into chapters 9-11 and consequences carried through chapters 13-15.
- **Items changed:** `book-two-outline.md` only.
- **Checks and outcomes:** The required story facts remain present in the approved order; the
  chapter map was reviewed against the series bible after the final edit.
- **What remains unproven:** Whether the new pacing will work at manuscript
  length.
- **External actions taken:** None.
- **Remaining risk or decisions:** The author must choose whether chapter 13 opens with
  recovery or immediate pursuit.
- **Next owner:** Author.
- **Next action:** Choose the chapter 13 direction before drafting new prose.
- **Learning candidate:** For a major outline move, build and approve a
  dependency map before editing the outline.
- **Evidence for the learning:** Moving the storm confrontation affected seven
  later story beats that were easier to review together than one at a time.
- **Saved to:** The synthetic project's outline-revision checklist, after author
  approval.
- **Check next time:** On the next structural move, record whether the map finds
  every dependent beat before editing begins.

The agent supplied structure and evidence. The author retained creative and
publication authority. A later task can mark the lesson as keep, revise, or
retire based on the result rather than assuming it worked.

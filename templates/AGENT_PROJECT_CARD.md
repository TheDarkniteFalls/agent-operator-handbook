# Agent Project Card

Give this card to the agent before substantial work. Ask it to draft what it
can from the current project, then bring you only the missing information and
decisions that require human judgment. Keep the completed card short enough to
check during the task.

## Project

- **Project name:** [Name]
- **Exact target:** [Folder, repository, branch, document, service, or shared record]
- **Starting checkpoint:** [Commit, version, timestamp, or other exact current state]
- **Desired result:** [What should be true when the work is finished?]
- **Audience or user:** [Who is the result for?]

## Source of Truth

- **Authoritative sources:** [Files, records, pages, or systems that define the current state]
- **Supporting sources:** [Useful context that is not authoritative]
- **Facts that must be confirmed:** [Anything likely to be stale, missing, or disputed]

If sources conflict, stop and report the conflict. Do not silently choose one.

## Authority

- **May read:** [Named sources or areas]
- **May propose:** [Plans, drafts, classifications, or changes]
- **May run:** [Named commands, tools, model or service calls, and network reads]
- **Expected side effects:** [Local files, temporary files, network access, connected services, or none]
- **May change after approval:** [Exact items or boundaries]
- **Must not change:** [Protected content, settings, records, or areas]
- **Fresh approval required before:** [Staging, committing, pushing, sending, publishing, purchasing, deleting, deploying, or changing shared state]

Approval applies only to the agreed target, scope, and content. Ask again if any
of those change. Each fresh approval gate is separate: permission to edit does
not approve a commit, and permission to commit does not approve a push or any
other external action.

## Definition of Done

- **User-visible result:** [What should a person be able to see or do?]
- **Required checks:** [The smallest checks that matter]
- **Evidence expected:** [Final checkpoint, scope comparison, structural check, visible or live result, human review, or other proof]
- **Out of scope:** [Useful work that is deliberately deferred]

## Starting State

- **Existing work or unrelated changes:** [What was already in progress?]
- **Protected starting state:** [Items that must remain byte-identical, unchanged, private, unpublished, or otherwise preserved]
- **Local, shared, or published state:** [Which copy is authoritative and whether another copy differs]
- **Known risks or open questions:** [What may affect the result?]
- **Recovery point:** [What can be restored if the work goes wrong?]

## Stop Conditions

Stop and report before continuing if:

- the exact target or starting checkpoint differs from this card;
- a protected or unrelated item changes;
- a tool, command, model or service call, network request, or external action
  appears that was not expected;
- a required source conflicts or required evidence is unavailable;
- a required check cannot run or still fails after the authorized work; or
- resolving a failure or completing the task would require broader scope or
  authority, or would risk protected state.

Do not silently retry with more authority, repair an unrelated problem, or
move to the next approval gate. Preserve the safest available state and ask for
a new decision.

## Prior Learning To Try

- **Lesson:** [A previously accepted lesson relevant to this task, or none]
- **Recorded in:** [The instruction, checklist, template, or project note that owns it]
- **How we will know it helped:** [One observable result]

## Working Agreement

- Start by reporting the current state without making changes.
- Prefer the smallest useful change that meets the definition of done.
- Separate facts, inferences, recommendations, and actions.
- Flag missing evidence rather than guessing.
- Recheck the result after the final change.
- Do not take an external action without a fresh human decision.
- Treat `passed`, `failed`, `not run`, `blocked`, and `missing evidence` as
  different outcomes.

## Required Handoff

- **Result achieved:**
- **Exact final checkpoint:** [Commit, version, timestamp, or live as-of time]
- **Items changed:**
- **Expected and unexpected side effects:**
- **Checks and outcomes:**
- **What remains unproven:**
- **External actions taken:** [None, or exact action]
- **Canonical external record:** [URL or record ID, live-confirmed state and time, or explicitly unverified]
- **Remaining risk or decisions:**
- **Next owner:**
- **Next action:**
- **Due or follow-up date:**
- **Learning candidate:** [One reusable lesson, or none]
- **Evidence for the learning:** [What happened that supports it]
- **Saved to:** [Authoritative project location, pending approval, or not saved]
- **Check next time:** [How a later task can test whether it helped]

## Learning Review

Complete this when a later task reuses a prior lesson:

- **Prior lesson applied:** [Yes, no, or not relevant]
- **Observed outcome:** [Helped, no clear difference, caused a problem, or unknown]
- **Decision:** [Keep, revise, or retire]

The agent may propose and complete these fields. A human approves any learning
that changes authority, privacy boundaries, or project direction.

## Human Decision

Choose one:

- [ ] Ready for a read-only inspection
- [ ] Approved for the named local changes
- [ ] Fresh approval granted for this exact external action: [Exact action]
- [ ] Needs more evidence or clarification
- [ ] Accepted as complete
- [ ] Held or rejected

# Verify Agent Work Without Reading Code

You do not need to understand every internal detail to review agent work. You
do need evidence connected to the result you requested.

Give this guide to the agent after it finishes the task and ask it to assemble
the review packet. Your job is to inspect the result, question weak evidence,
and choose the final review state.

## 1. Confirm the Starting Point

Ask the agent to identify:

- the current source of truth
- the state before its work
- existing or unrelated changes
- missing, stale, or conflicting information

If the starting point is wrong, later evidence may describe the wrong project.

## 2. Confirm the Scope

Ask for the exact files, records, pages, or settings touched. Compare that list
with the authority you granted.

Unexpected changes are not automatically bad, but they require explanation and
usually a new decision.

## 3. Ask for a Named Check

A useful check has a clear question, such as:

- Does the revised document still preserve the approved facts?
- Does the important user journey still work?
- Did the cleanup leave every protected category untouched?
- Does the final file open and show the expected result?

Ask when the check ran. Evidence recorded before the final change may be stale.

## 4. Inspect the Result That Matters

Where possible, review the real output:

- open the finished document
- view the relevant page or screen
- compare before and after
- inspect a small sample of changed and protected items
- ask the agent to point to the evidence for each acceptance criterion

A technical check can support this review, but it should not replace the
user-visible result.

## 5. Ask What the Evidence Does Not Prove

Every check has limits. Ask the agent to state them plainly.

| Agent claim | Evidence to request | What may still be unproven |
| --- | --- | --- |
| "The work is complete" | Acceptance criteria matched to evidence | Whether the criteria were sufficient |
| "The checks passed" | Exact check, timing, and result | Whether the check covered the right risks |
| "Nothing else changed" | Complete changed-item list or comparison | Changes outside the inspected boundary |
| "The information is current" | Source and as-of date | Later changes or missing sources |
| "It is safe to publish" | Privacy review, final content review, and human approval | Unknown sensitive context or legal obligations |

## A Copyable Review Request

```text
Before I accept this work, give me a plain-language review packet:

1. Restate the result you were authorized to produce.
2. Name the source of truth and the state you started from.
3. List every item changed and any unexpected item encountered.
4. Map each definition-of-done item to current evidence.
5. State which checks ran after the final change and show their outcomes.
6. Explain what those checks do not prove.
7. List skipped checks, remaining risks, and unresolved decisions.
8. Confirm whether anything was sent, published, deleted, purchased, or changed outside the approved local scope.
9. Name the next owner and one concrete next action.
10. If the evidence supports a reusable lesson, propose one, say where it should be saved, and explain how we can test it next time. Do not change project instructions without approval.
```

## Choose the Review Result

Finish with one of these states:

- **Verified enough:** the evidence supports the intended use and the remaining risk is accepted.
- **Needs review:** the work may be useful, but an important question or check remains.
- **Not verified:** the evidence is missing, stale, contradictory, or outside the approved scope.

"Not verified" is a useful result. It prevents uncertainty from being hidden
behind a confident summary.

Only propose a learning after the work has been verified. A learning candidate
is an idea to test in future work, not proof that the project has improved.

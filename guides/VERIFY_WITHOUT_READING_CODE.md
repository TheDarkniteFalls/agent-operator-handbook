# Verify Agent Work Without Reading Code

You do not need to understand every internal detail to review agent work. You
do need evidence connected to the result you requested.

Give this guide to the agent after it finishes the task and ask it to assemble
the review packet. Your job is to inspect the result, question weak evidence,
and choose the final review state.

## 1. Confirm the Starting Point

Ask the agent to identify:

- the current source of truth
- the exact folder, repository, branch, version, record, or as-of time
- the state before its work and the final checkpoint being reviewed
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

## 4. Use The Proof Ladder

Different evidence answers different questions. Check only the layers that
matter to the task, but do not let proof at one layer stand in for another.

| Layer | Question | Useful evidence |
| --- | --- | --- |
| Exact version | Which exact final version is under review? | Commit, version, file digest, record ID, or as-of time |
| Change boundary | Did only the authorized items change? | Complete comparison plus protected and unrelated items checked |
| Structural checks | Does the result have the required shape or pass its named checks? | Format check, test, build, schema validation, or clean extraction |
| Real-world result | Does the real document, app, browser journey, or remote record work now? | Opened document, exercised controls, rendered screen, or live-read canonical record |
| Human usefulness | Is the result suitable for its intended person and purpose? | Human use, acceptance, edit, rejection, or recorded judgement |

A structural pass does not prove that the real-world result works. A working
result does not prove that a person found it useful. After any material change,
identify which earlier evidence became stale and rerun the relevant checks.

Record each check as `passed`, `failed`, `not run`, `blocked`, or `missing
evidence`. Do not turn a blocked or missing result into a pass.

## 5. Inspect the Result That Matters

Where possible, review the real output:

- open the finished document
- view the relevant page or screen
- compare before and after
- inspect a small sample of changed and protected items
- ask the agent to point to the evidence for each acceptance criterion

A technical check can support this review, but it should not replace the
user-visible result.

For an external action, inspect the canonical URL or record after the action.
Record its live state, when it was confirmed, who owns the next move, and any
due or follow-up date. A successful tool or connector response is not proof
that the intended external state now exists.

## 6. Ask What the Evidence Does Not Prove

Every check has limits. Ask the agent to state them plainly.

| Agent claim | Evidence to request | What may still be unproven |
| --- | --- | --- |
| "The work is complete" | Acceptance criteria matched to evidence | Whether the criteria were sufficient |
| "The checks passed" | Exact check, timing, and result | Whether the check covered the right risks |
| "Nothing else changed" | Complete changed-item list or comparison | Changes outside the inspected boundary |
| "The information is current" | Source and as-of date | Later changes or missing sources |
| "The external action completed" | Canonical record, live state, and confirmation time | Later changes or obligations still awaiting follow-up |
| "It is safe to publish" | Privacy review, final content review, and human approval | Unknown sensitive context or legal obligations |

## A Copyable Review Request

```text
Before I accept this work, give me a plain-language review packet:

1. Restate the authorized result and name the source of truth, starting checkpoint, and final checkpoint.
2. List every changed item, every protected item checked, and any unexpected side effect.
3. Map each definition-of-done item to the relevant proof layers: Exact version, Change boundary, Structural checks, Real-world result, and Human usefulness.
4. Give the final check outcomes, mark each one passed, failed, not run, blocked, or missing evidence, and explain its limits or stale evidence.
5. List remaining risks and unresolved decisions.
6. For any external action, give the canonical record, live-confirmed state and confirmation time or explicitly unverified status, and follow-up date.
7. Name the next owner, one concrete next action, and its date.
8. Optionally propose one reusable lesson, where it should be saved, and how to test it next time. Do not change project instructions without approval.
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

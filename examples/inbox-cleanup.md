# Example: Preserve-First Inbox Cleanup

This synthetic example shows how to use an agent for a bulk operation without
turning a broad instruction into accidental deletion or lost correspondence.

## Project Card

- **Project name:** Community group inbox cleanup
- **Desired result:** Archive routine event notices older than 90 days while
  preserving personal replies, receipts, unresolved requests, and flagged mail.
- **Audience:** The volunteer who manages the inbox.
- **Current as of:** 30 June 2026.

## Source of Truth

- The live inbox is authoritative for message state.
- The written exception list defines protected categories.
- A search result is a temporary working set, not a new source of truth.

## Authority

- The agent may search and inspect a small sample.
- It may propose a search rule and report the expected count.
- It may archive the approved result set only after human confirmation.
- It must not delete, reply, forward, unsubscribe, alter contacts, remove flags,
  or change labels outside the approved archive action.
- Any changed search rule or materially different message count requires new
  approval.

## Preserve-First Loop

1. **Search narrowly.** Start with routine event notices older than 90 days.
2. **Inspect a sample.** Review examples from the start, middle, and end of the
   result set.
3. **Find exceptions.** Exclude personal replies, receipts, unresolved requests,
   and flagged messages.
4. **Preview the action.** Show the final rule, count, and several included and
   excluded examples.
5. **Approve once.** Approval applies only to that exact rule and result shape.
6. **Archive.** Perform no other mailbox action.
7. **Verify.** Confirm the approved search is clear and protected examples are
   still present.

## Synthetic Walkthrough

The first search finds 36 messages. An eight-message sample reveals one receipt
and one unresolved personal reply, so the agent stops instead of archiving.

The revised search excludes those categories and returns 29 messages. The agent
shows the revised rule, count, three included examples, and the protected
exceptions. The human approves that exact preview.

After archiving, the agent reports:

- 29 messages archived
- 0 messages remaining under the approved search
- the sampled receipt, personal reply, flagged message, and unresolved request
  still present
- no messages deleted, sent, forwarded, or relabeled

## Evidence to Review

The operator checks:

- the final search rule matches the approved preview
- the before and after counts reconcile
- included and protected samples are correctly classified
- the approved search is empty after the action
- the protected searches still return their expected examples
- the handoff names any uncertain message left for manual review

## Example Handoff

- **Result achieved:** The approved set of 29 routine notices was archived.
- **Items changed:** Archive state for those 29 messages only.
- **Checks and outcomes:** The approved search is clear; four protected sample messages remain
  unchanged.
- **What remains unproven:** Whether other senders use unusual subject lines that
  should be included in a future cleanup.
- **External actions taken:** No replies, forwards, deletions, or unsubscribes.
- **Remaining risk or decisions:** Three ambiguous notices were deliberately left untouched.
- **Next owner:** Inbox operator.
- **Next action:** Review the three ambiguous notices individually.
- **Learning candidate:** Every bulk archive rule should explicitly exclude
  receipts and unresolved personal replies before approval.
- **Evidence for the learning:** The first eight-message sample found one of
  each, preventing them from being archived with routine notices.
- **Saved to:** The synthetic inbox-cleanup checklist, after operator approval.
- **Check next time:** Confirm the protected-category sample is clean before a
  later bulk action, then record whether the rule prevented rework.

The safe result is not the largest possible cleanup. It is the largest cleanup
supported by the inspected evidence and the approved boundary. The next cleanup
will decide whether to keep, revise, or retire the new exclusion rule.

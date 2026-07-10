# Minimum Recurring-Work Workspace

This is a small, file-based starting point for one recurring workflow. Copy the
whole `recurring-workspace` folder into a new workspace, then personalize it
with Codex.

The files have different jobs:

- `WORKING_AGREEMENT.md` defines purpose, sources, authority, output rules, and
  completion proof.
- `TODAY.md` holds the current focus, next moves, blockers, waiting items, and
  outputs needing review.
- `SOURCE_SHELF.md` records what each source is authoritative for, its date,
  limitations, and review timing.
- `REVIEW_LOG.md` records what happened to material outputs and what was
  learned.
- `context/` holds small source-backed notes with visible confidence states.
- `outputs/` holds reusable results outside chat.

Do not fill these files with every fact, task, or conversation. Their purpose
is to preserve the minimum state that helps a later session do better work.

## Setup Prompt

Open Codex in the copied workspace and paste:

```text
Help me personalize this minimum assistant workspace.

Do not add an app, database, automation, broad connector access, or new daily
interface. Ask me no more than three questions:
1. What recurring job should this workspace improve first?
2. Which sources should it trust for that job?
3. What must it never do without asking me?

Then update only WORKING_AGREEMENT.md, TODAY.md, and SOURCE_SHELF.md. Keep the
files short. Explain the first workflow, its visible proof, what remains
unconfigured, and one exact prompt I can use to run it. Do not take any
external action.
```

## First-Use Test

Before adding more machinery:

1. Copy the starter into an otherwise empty folder.
2. Use a fresh Codex session that can see only the included files and the
   synthetic or private sources you deliberately add.
3. Run one bounded workflow through to a saved output.
4. Confirm the result names its sources, uncertainty, validation, and next
   action.
5. Record whether the result was used, edited, rejected, or superseded.
6. Write down any missing file, hidden assumption, confusing term, or required
   capability.

The starter passes when a fresh session can complete the first workflow from
these files alone. A polished folder structure is not proof.

## Public-Safe Use

Keep private messages, credentials, personal records, connector exports, raw
agent logs, unpublished work, and internal URLs out of public copies. Replace
real examples with synthetic ones before sharing.

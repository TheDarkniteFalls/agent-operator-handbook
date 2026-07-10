# Example: A Weekly Community Brief

This entirely synthetic example shows how the minimum assistant workspace can
support one recurring job without an app, database, automation, or broad
connector access.

## The Job

A volunteer coordinator prepares a Friday brief from three local files:

- `sources/events.md`: confirmed upcoming events;
- `sources/announcements.md`: approved notices;
- `sources/open-questions.md`: unresolved items that may need a person.

The desired result is a short internal brief saved to `outputs/`. Codex may
draft and save the brief. It may not email, publish, or edit the source files.

## Working Agreement Extract

- **Recurring job:** Prepare the Friday community brief.
- **Desired result:** A source-backed summary of the next seven days, followed
  by decisions and missing information.
- **Source order:** `events.md`, then `announcements.md`, then
  `open-questions.md` for unresolved context only.
- **Must ask before:** Sending or publishing the brief, changing a source file,
  or treating an unresolved item as confirmed.
- **Done:** The brief is saved, every event has a source, missing evidence is
  visible, and the final file is checked against all three named sources.

## Source Shelf Extract

| Source | Authoritative For | Limitation |
| --- | --- | --- |
| `sources/events.md` | Date, time, location, and confirmed organiser for approved events | Does not establish whether a draft announcement was sent |
| `sources/announcements.md` | Wording approved for internal circulation | May contain notices for later weeks |
| `sources/open-questions.md` | Questions that still need an owner or decision | A question is not evidence that its proposed answer is true |

## First Run

The coordinator asks:

```text
Prepare this Friday's community brief from the three sources named in the
working agreement. Save it in outputs/. Do not send or publish it. Treat missing
or conflicting information as a review item, not as a fact.
```

The sources contain two confirmed events, one announcement for the following
month, and a question asking whether the library room has been booked.

## Saved Output

```markdown
# Community Brief — 2026-08-07

Output ID: community-brief-2026-08-07
Intended use: Internal coordinator review before any circulation

## Confirmed This Week

- Tuesday, 18:00 — Garden planning session, Hall A.
  Source: sources/events.md, checked 2026-08-07.
- Thursday, 19:30 — Volunteer welcome evening, Room 2.
  Source: sources/events.md, checked 2026-08-07.

## Decisions or Missing Evidence

- Library workshop room booking: unknown due to missing confirmation. The
  question in sources/open-questions.md is a retrieval hint, not booking proof.

## Deliberately Omitted

- Next month's recycling notice is outside this brief's seven-day window.

## Validation

- Checked all three declared sources after drafting.
- Confirmed both included dates fall inside the seven-day window.
- No message was sent and no source file was changed.

## Next Action

Coordinator: confirm the library booking with the venue owner, then decide
whether the workshop belongs in the brief.
```

This output is useful even though it is not complete enough to circulate. Its
operational state is `needs_review`; that is different from a failed workflow.

## Feedback and Closure

The coordinator uses the two-event brief but edits the headings to sound less
formal. The matching review entry becomes:

| Date | Output ID | Outcome | What Changed | Lesson | Check Next Time |
| --- | --- | --- | --- | --- | --- |
| 2026-08-07 | `community-brief-2026-08-07` | edited and used | Replaced “Decisions or Missing Evidence” with “Needs a Check” | Use plain headings for volunteer briefs; retain explicit evidence status in the item text | Compare headings and evidence status in the next two briefs |

The feedback closes the output and creates one bounded lesson. It does not
store the whole conversation, rewrite every writing rule, or create another
pending review card.

## What This Example Proves

- The workflow can produce a useful saved result from a narrow source set.
- A missing confirmation remains unknown rather than becoming a false claim.
- The assistant can distinguish useful output from circulation readiness.
- Human feedback updates both the matching output state and a testable writing
  lesson.
- External action remains separately approval-gated.

It does not prove that this workflow needs connectors, automation, a custom
interface, or a database. Those should be considered only after repeated use
reveals a specific burden worth replacing.

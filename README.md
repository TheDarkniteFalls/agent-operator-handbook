# Build with Codex: A Plain-English Handbook

<!-- toolkit-trust-card:start -->
> **Public contract:** Stable guide · about 5 min · No code; Python optional · no model · no network
>
> **Operation:** Guidance only
>
> **A pass establishes:** The starter bundle contains the declared source, authority, review, and handoff files and passes its structural checks.
>
> **It does not establish:** Guidance and templates do not enforce permissions or verify a live project.
>
> **First check:** `python3 scripts/check_starter_bundle.py`
<!-- toolkit-trust-card:end -->

Codex can help turn project material and ordinary-language instructions into
finished work even if you do not code. The harder part is telling it which
material to trust, what result you want, what it may change, and what evidence
must come back before you accept the work.

This handbook is for writers, creators, researchers, small-business owners, and
anyone else with an idea who wants to complete one bounded task with Codex
without first becoming a software engineer. The same method also works with
Claude and similar file-and-tool agents.

Use it to turn an idea into a clear project, let the agent do the approved work,
and review the finished result in plain language. You remain responsible for
the destination and important decisions; the agent is responsible for working
inside those boundaries and showing what it did.

To follow the runnable steps, you need Codex or a similar file-and-tool agent
and a local project folder it may read. If you only want to learn the method,
continue without running the prompts.

## Start in 60 Seconds

Open Codex in the folder that contains your project material and paste:

```text
I do not code, but I have a project idea. Read the material in this project and
explain what already exists in plain language. Name the exact folder,
repository, branch, version, or shared record you inspected, plus any work
already in progress. Then draft an Agent Project Card covering the finished
result, reliable source material, what must stay protected, expected side
effects, actions that require my approval, stop conditions, and any decisions
or missing information you need from me. Do not change anything yet.
```

Codex should return a short current-state explanation, a draft Project Card,
and only the questions that genuinely require your judgment. Review those
decisions before authorizing any changes.

This first request is deliberately read-only. It lets you check the agent's
understanding and the proposed boundary before deciding whether any change
should happen.

## The Basic Routine

Most agent guides explain how to ask for work. This guide explains how to let
an agent do most of that work without losing control of the project.

Think of the agent as a capable worker. You do not need to manage every step or
choose every technical check. You give it a destination, show it where the
reliable information lives, and mark the few decisions that still belong to
you.

The basic routine is:

1. **Show it the right material.** Name the exact folder, repository, version,
   page, message, or record that describes the project now. Ask the agent to
   flag anything missing, stale, contradictory, or already in progress.
2. **Describe the finished result.** Explain in ordinary language what you want
   to be true when the work is done. The agent can work out the detailed steps.
3. **Set a few stop signs.** Say which files, tools, online services, or shared
   information it expects to use or change; what must stay protected; and when
   it must stop and ask you first. Sending, publishing, deleting, purchasing,
   and changing shared information always need a fresh decision.
4. **Let it do the work.** Give it room to investigate, make the approved local
   changes, and choose sensible checks. Ask it to explain important decisions
   in plain language.
5. **Make it show its work at the end.** The agent should identify the exact
   final state, show the result, list what changed, explain what each check
   proves, and say what remains uncertain and what should happen next.

## Start with a Project Card

1. Give the agent the [Agent Project Card](templates/AGENT_PROJECT_CARD.md) and
   ask it to draft the card from the project information it can find.
2. Review the draft and answer only the questions that require your judgment:
   the result you want, what must stay protected, and what needs your approval.
3. Ask the agent to complete the work inside that agreed boundary.
4. At the end, have it follow [Verify Without Reading
   Code](guides/VERIFY_WITHOUT_READING_CODE.md) and give you the result in plain
   language.
5. Save its final handoff with the project so a future session can continue
   from the real current state.

The Project Card is not homework you must complete alone. Let the agent fill in
what it can, then bring you the gaps and decisions that genuinely need a human.

See the filled examples for a [writing revision](examples/writing-revision.md)
and a [preserve-first inbox cleanup](examples/inbox-cleanup.md).

## How Much Can the Agent Do?

Give the agent more freedom one step at a time. Treat each step as a separate
decision:

| Step | What you allow | Typical instruction |
| --- | --- | --- |
| Read | Inspect named sources and report current state | "Read these items. Do not change anything." |
| Propose | Recommend a plan or draft | "Show me the proposed result first." |
| Preview | Show the exact intended action and likely impact | "List what would change and what would stay untouched." |
| Change | Modify only the approved local items | "Apply this approved version to these named items." |
| External action | Send, publish, purchase, delete, deploy, or change shared records | "Stop and ask for a fresh decision before acting." |

Approval at one step does not automatically approve the next. If the target,
scope, or proposed content changes, the agent should ask again.

Before approving a change, ask the agent to list the side effects it expects:
local files, commands, additional model or service calls, network access,
connected accounts, and changes outside the local project. Treat each fresh
gate as a separate choice. Approval to edit does not approve staging or
committing; a commit does not approve pushing; and a push does not approve a
pull request, publication, message, or deployment.

If the starting state differs, a protected item changes, an unexpected side
effect appears, or required evidence is unavailable, the agent should stop and
report the difference. It should not solve the problem by silently expanding
scope, retrying with more authority, or taking the next external step.

## What Good Evidence Looks Like

Useful evidence is tied to the promised result:

- the exact final version, revision, or as-of time
- a before-and-after comparison and the exact items changed
- proof that protected and unrelated items stayed untouched
- a named structural or automated check run after the final change
- the visible result in the document, app, browser, or live service that matters
- human review of whether the result is actually useful, when that claim matters
- skipped checks and remaining uncertainty
- a statement of what each check does not prove

"Done," "looks good," and "tests passed" are claims. Evidence lets a person
decide whether to trust those claims. A structural check does not prove a live
journey worked, and a working journey does not prove that a person found the
result useful. See [Verify Without Reading
Code](guides/VERIFY_WITHOUT_READING_CODE.md) for the full proof ladder.

## The Required Handoff

End substantial work with:

- the result achieved
- the exact final version, revision, or as-of time
- the items changed
- expected and unexpected side effects
- the checks performed and their outcomes
- anything failed, skipped, or not independently verified
- remaining risk or unresolved decisions
- whether any external action occurred and, if so, its canonical link or record,
  live-confirmed state and confirmation time, or an explicit note that it
  remains unverified
- the next owner, one concrete next action, and any due or follow-up date

Chat history can be useful background, but it is not a reliable project record.
Save important state in the project's chosen source of truth.

## Go Further

Complete one bounded task before expanding the system. The sections below are
for recurring work, evidence-backed learning, and optional public-safe
first-use feedback after the basic routine is clear.

### Build a Recurring-Work Assistant

Once one project is working well, you may want Codex to help with a recurring
body of work: weekly research, programme coordination, content planning, or
another job that needs continuity across sessions.

Start with [Build a Working Assistant with Codex](guides/BUILD_A_RECURRING_WORK_SYSTEM.md).
It distils 27 lessons from a long-running private Chief-of-Staff build into a
small operating pattern: trusted sources, durable state outside chat, bounded
authority, useful feedback, low-noise attention, and evidence of completion.

Use the [copyable recurring-work workspace](templates/recurring-workspace/README.md)
to prove one workflow before adding databases, broad connector access,
background automation, or a custom application. The
[weekly community brief](examples/weekly-community-brief.md) shows the pattern
with entirely synthetic information.

#### Download The Starter

[Create a private Reliable AI Work Starter](https://github.com/new?template_owner=TheDarkniteFalls&template_name=reliable-ai-work-starter&visibility=private),
open the new repository in Codex, and paste the setup prompt from its
`README.md`. The copy is private by default and includes the working agreement,
source shelf, current-state handoff, review log, output boundary, and a small
structural check.

If you prefer an offline folder, [download the minimum recurring-work
workspace](downloads/minimum-recurring-workspace.zip?raw=1) instead. Its
published [SHA-256 checksum](downloads/minimum-recurring-workspace.sha256) and
automated clean-folder check are rebuilt from the same source templates.

The check proves that the committed download matches those templates, extracts
cleanly into one folder, contains the required agreement and handoff surfaces,
and avoids the repository's known private-data markers. It does **not** run
Codex, inspect your sources, enforce authority, or prove that the starter will
improve every workflow. The real first-use proof is one bounded task completed
in a fresh session.

### Let the Project Learn

After meaningful work, let the agent suggest one lesson that could make a
future task easier or safer. The user does not need to study the logs or design
a learning system.

Use this small loop:

1. **Notice.** The agent identifies a point of confusion, rework, failure, or
   unexpected success from the completed task.
2. **Support it.** The agent points to the result, check, or other evidence
   behind the proposed lesson.
3. **Choose.** A human accepts, changes, defers, or rejects the lesson. Anything
   affecting authority, privacy, or project direction needs a human decision.
4. **Save it.** Put an accepted lesson in the project's real instructions,
   checklist, template, or other source of truth. Do not leave it only in chat.
5. **Test it next time.** On the next relevant task, the agent records whether
   the lesson was used and whether it helped. Then keep, revise, or retire it.

Good lessons are specific, supported by what happened, likely to matter again,
and safe to store. Do not turn speculation or a temporary workaround into a
permanent rule. Do not save raw private conversations merely because they may
contain something useful.

This loop needs a short handoff, not a larger tracking system or more raw logs.
The agent records the lesson, its evidence, where it was saved, and how to
check it next time. The project improves only when a later result shows that
the lesson was useful.

### Help Test The First Use

If you choose to try the starter, follow the optional
[30-to-60-minute first-use trial](docs/FIRST_USE_TRIAL.md). You may then submit
a [public-safe first-use report](https://github.com/TheDarkniteFalls/reliable-ai-work-starter/issues/new?template=first-use-report.yml).
Voluntary reports are summarized in the starter's
[usage-evidence ledger](https://github.com/TheDarkniteFalls/reliable-ai-work-starter/blob/main/USAGE_EVIDENCE.md).

There is no participation target. A report may support only the smallest
correction it directly justifies; other changes should be labelled as
maintainer judgement rather than user evidence. Reports do not establish broad
adoption or effectiveness.

Never put private sources, identifying details, credentials, internal links,
connector exports, raw model logs, customer data, or unpublished material in a
public issue.

## Trust and Limits

The automated checks cover the published starter bundle, not the quality or
safety of a live project:

[![checks](https://github.com/TheDarkniteFalls/agent-operator-handbook/actions/workflows/checks.yml/badge.svg)](https://github.com/TheDarkniteFalls/agent-operator-handbook/actions/workflows/checks.yml)

Outside-use evidence is recorded separately in the starter's
[usage-evidence ledger](https://github.com/TheDarkniteFalls/reliable-ai-work-starter/blob/main/USAGE_EVIDENCE.md).
Passing structural checks is not evidence that the method works for every
workflow.

## Repository Checks

```sh
python3 scripts/build_starter_bundle.py --check
python3 scripts/check_starter_bundle.py
python3 -m py_compile scripts/build_starter_bundle.py scripts/check_starter_bundle.py
```

Expected result:

```text
PASS deterministic_starter_bundle
PASS starter_source
PASS starter_archive
PASS clean_folder_shape
PASS public_safe_starter
```

## Scope

This repository contains guidance and synthetic examples only. It does not call
an AI model, inspect a project, enforce permissions, verify evidence, or approve
work on anyone's behalf.

The goal is not to remove human judgment. It is to make that judgment easier by
keeping authority, evidence, uncertainty, and ownership visible.

## License

This project is available under the [MIT License](LICENSE).

## Public-Safe Use

Do not copy private messages, credentials, personal records, unpublished work,
customer data, connector exports, or raw agent logs into a public repository.
Replace sensitive details with synthetic examples before sharing a project card
or handoff. See [SECURITY.md](SECURITY.md) for reporting guidance.

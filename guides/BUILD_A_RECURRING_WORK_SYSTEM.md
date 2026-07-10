# Build a Working Assistant with Codex

A prompt starts a conversation. A useful assistant has a clear job, trusted
sources, durable state, bounded authority, repeatable workflows, and proof that
the work was completed properly.

This guide distils hard-won lessons from building a private Chief-of-Staff
workspace. It preserves the operating lessons without copying its private
context, data, codebase, internal sources, or full machinery. The pattern is
useful for research, programme coordination, content work, learning, sales, or
almost any other recurring body of knowledge work.

You do not need to be a developer. You do need to describe the outcome you
want, identify the sources that deserve trust, set boundaries, judge the
result, and insist on evidence before calling work complete.

## Start Here

Build one workflow before you build an assistant.

1. Choose one recurring job that matters.
2. Name the sources that define the current truth.
3. State what Codex may do and what still needs your approval.
4. Save the useful result outside chat.
5. Record whether you used, edited, rejected, or replaced it.
6. Run the workflow several times before adding machinery.

The minimum loop is:

```text
one useful job
  -> narrow trusted sources
  -> bounded work
  -> saved output
  -> human outcome
  -> evidence-backed improvement
```

Use the [copyable recurring-work workspace](../templates/recurring-workspace/README.md)
for the minimum files. See the
[weekly community brief](../examples/weekly-community-brief.md) for a complete
synthetic example.

## The Operating Pattern

A dependable assistant usually needs seven things:

1. **One clear front door.** The user asks for help in one place instead of
   learning several internal tools.
2. **A written agreement.** Purpose, sources, boundaries, output rules, and the
   definition of done are visible.
3. **Small durable state.** Priorities, confirmed context, reusable outputs,
   and review outcomes live in ordinary files rather than only in chat.
4. **Repeatable workflows.** Important jobs have a bounded method and a
   visible success condition.
5. **Approval before external action.** Drafting and analysis can be generous;
   sending, publishing, deleting, purchasing, or changing shared state needs a
   fresh decision.
6. **Proof before completion.** The assistant shows what changed, what was
   checked, and what remains uncertain.
7. **Learning from real use.** Accepted, edited, rejected, superseded, and
   stale outputs all improve the next run.

Do not copy a mature assistant feature for feature. Its design reflects one
person's work, sources, preferences, risks, and history. Replicate the pattern,
then let your own workflows earn additional complexity.

## The 27 Hard-Won Lessons

Each lesson below keeps three parts visible: the failure, the replacement rule,
and the smallest useful proof. This is important. Advice without its failure
mode is easy to apply in the wrong situation; a rule without proof is only a
preference.

### Memory and Context

#### 1. Memory must discriminate, not merely accumulate

- **Failure:** Remembering almost nothing loses continuity. Capturing
  everything creates duplicates, stale claims, weak candidates, and review
  noise.
- **Replacement rule:** Route durable context into `confirmed`, `provisional`,
  or `needs_judgement`. Record the source, source date, confidence, and review
  date.
- **Proof:** A later task can retrieve a useful confirmed item while an
  ambiguous or conflicting item remains visibly provisional.

Here, *discriminating* means selective and evidence-aware. It does not refer to
judgements about people.

#### 2. Missing evidence must mean unknown, not false

- **Failure:** A missing message, absent field, stale source, or failed read is
  treated as proof that something did not happen.
- **Replacement rule:** Make `unknown_due_to_missing_source` a valid result.
  Distinguish source-backed, provisional, conflicting, partial, and unavailable
  evidence.
- **Proof:** Tests include missing, stale, conflicting, and partial sources and
  produce calibrated uncertainty rather than confident negative claims.

#### 3. Retrieval hints are not relationship or ownership proof

- **Failure:** Co-occurrence in a meeting, document, or thread becomes an
  inferred reporting line, commitment, preference, or owner.
- **Replacement rule:** Store `related_for_search` separately from
  `relationship_proven`. Consequential relationships require an authoritative
  source, a defined relationship type, freshness, confidence, and no unresolved
  conflict.
- **Proof:** Repeated mentions improve discovery without silently creating a
  typed relationship.

#### 4. Entity hygiene starts at extraction

- **Failure:** Names with initials, punctuation, nicknames, or variants create
  duplicate records. Generic words become people or projects. Two records can
  overwrite the same readable profile.
- **Replacement rule:** Check aliases and canonical names before accepting a
  new entity. Reject obvious noise deterministically and leave uncertain
  remaps provisional.
- **Proof:** Cases covering initials, punctuation, aliases, generic nouns, and
  duplicate readable names cannot create silent collisions.

#### 5. Stored is not the same as retrievable

- **Failure:** A document appears registered even though extraction failed,
  stored chunks are unusable, or retrieval reaches only a derived summary.
- **Replacement rule:** Give every ingested source a receipt covering file
  identity, extraction status, chunk count, source metadata, and a
  source-specific retrieval example.
- **Proof:** Every supplied file independently answers a smoke query that
  reaches the expected source.

### Feedback, Writing, and Learning

#### 6. The version actually used is stronger evidence than the draft

- **Failure:** Writing guidance learns from what the assistant proposed rather
  than what the user edited, discarded, or sent.
- **Replacement rule:** Compare the proposed and used versions. Record what was
  cut, added, softened, clarified, or made more human, and apply the lesson to
  the matching writing mode.
- **Proof:** A later draft reproduces the accepted pattern without copying raw
  private messages into long-term context.

#### 7. Feedback must close the matching work item

- **Failure:** The system learns from “I used that” but continues asking the
  user to review the same draft.
- **Replacement rule:** Give reusable outputs stable IDs. Resolve feedback by
  exact ID, exact active title, or a uniquely focused recent item; ask when the
  reference is ambiguous. Apply the outcome and learning record together.
- **Proof:** A used, rejected, superseded, or archived output leaves no stale
  pending review behind.

#### 8. Follow-through is not recommendation quality

- **Failure:** A used recommendation is automatically counted as good, while
  an unused recommendation is treated as bad.
- **Replacement rule:** Track `what_happened` separately from
  `recommendation_quality`. Quality still needs human judgement, source
  quality, and outcome evidence.
- **Proof:** The system can record “used but weak” and “good but not acted on”
  without contradiction.

#### 9. Skills should encode proven workflows, not accumulated advice

- **Failure:** Generic skills and long instruction files grow faster than
  reliable behaviour.
- **Replacement rule:** Create a skill only after a workflow or failure recurs.
  Give it a precise trigger, required steps, a known failure pattern, and a
  realistic validation prompt. Retire it if it does not improve real work.
- **Proof:** The same relevant prompt produces the intended workflow in a fresh
  session without loading unrelated guidance.

### Attention and Review Noise

#### 10. Review items should represent judgement, not activity

- **Failure:** Review queues fill with routine meetings, status messages,
  empty runs, receipts, and other items that require no decision.
- **Replacement rule:** Before surfacing an item, answer: `Who must decide
  what?` Keep routine evidence quiet. Surface user-facing work, approvals,
  ambiguity, material risks, and genuine exceptions.
- **Proof:** Every visible review item names a decision, approval, ambiguity,
  risk, or useful review action.

#### 11. Registration needs stable identity and terminal outcomes

- **Failure:** Re-running a report creates duplicates, while replaced or
  completed drafts remain pending indefinitely.
- **Replacement rule:** Register outputs by stable purpose and artifact
  identity. Support terminal states such as `used`, `acknowledged`, `archived`,
  and `superseded`.
- **Proof:** Re-running the same workflow updates the right record unless the
  content or routing identity genuinely changed.

#### 12. Wrong surface is useful feedback

- **Failure:** A useful item appears in the wrong place, but the only choices
  are to use it or archive it.
- **Replacement rule:** Treat `wrong_surface` as different from
  `wrong_content`. Record where the item belonged and aggregate repeated
  corrections before changing policy.
- **Proof:** A routing correction improves later placement without one click
  silently rewriting system-wide rules.

#### 13. Interfaces should remove monitoring burden

- **Failure:** Tabs, dashboards, queues, diagnostic pages, and compatibility
  views create more places the user feels obliged to check.
- **Replacement rule:** Keep one conversational front door, one compact daily
  companion if needed, and explicit drill-down or diagnostic surfaces. A new
  daily surface should replace an old burden.
- **Proof:** The user can operate the workflow without learning the internal
  machinery or monitoring several locations.

#### 14. Silence and nothing due can be healthy

- **Failure:** A quiet scheduled run looks broken, or a health threshold is
  shorter than the real schedule and creates false alarms.
- **Replacement rule:** Define the expected silent state and align freshness
  thresholds with the actual cadence. Alert on evidence of missed work or
  broken state, not on the absence of chatter.
- **Proof:** Tests cover both `something_due` and `nothing_due`, and a healthy
  quiet run leaves a fresh status record.

### Token and Context Efficiency

#### 15. Diagnose token waste before compressing quality

- **Failure:** “Use fewer tokens” produces shorter answers, weaker reasoning,
  or skipped validation while repeated context and raw output remain.
- **Replacement rule:** Measure cost by workflow, output shape, and terminal
  outcome. Find replay, broad status dumps, raw payloads, and abandoned long
  sessions before lowering reasoning quality.
- **Proof:** A change removes a named source of waste while the same acceptance
  evidence still passes.

#### 16. Keep the always-on kernel small

- **Failure:** Detailed recipes, preferences, and examples are loaded into
  every task, even when irrelevant.
- **Replacement rule:** Keep only universal safety, authority, working style,
  and completion rules always on. Load task recipes and examples on demand.
- **Proof:** A smaller instruction kernel preserves boundary and validation
  behaviour across representative tasks.

#### 17. Keep raw payloads out of the working chat

- **Failure:** Full connector results, spreadsheets, transcripts, JSON, or
  binary content flood the conversation and cannot be reliably removed later.
- **Replacement rule:** Save raw evidence to declared files. Return compact
  source cards, IDs, audit paths, and decision-relevant summaries to chat.
- **Proof:** A fresh session can continue from a short handoff and source
  handles without replaying the raw material.

#### 18. Use different context depths

- **Failure:** Routine tasks receive either too little context or the same deep
  bundle used for audits and meeting preparation.
- **Replacement rule:** Define `fast`, `normal`, and `deep` modes with explicit
  source-card limits and a discoverable location for omitted evidence.
- **Proof:** A routine question uses a small packet; a complex task expands
  deliberately and can still trace every important claim.

#### 19. Better reasoning often comes from a harness, not a bigger model

- **Failure:** Expensive reasoning compensates for implicit sources,
  boundaries, validation, and stop rules, while consequential work may still
  be under-framed.
- **Replacement rule:** For material tasks, state the task family, source
  posture, authority boundary, output target, risks, smallest plan, validation,
  and stop condition. Escalate when the frame is uncertain, evidence conflicts,
  or action is hard to reverse.
- **Proof:** The workflow produces consistent, reviewable decisions across
  model or reasoning settings without letting efficiency override safety.

### Connectors, Provenance, and Source Truth

#### 20. A connector call is not completion proof

- **Failure:** Useful messages appear in chat even though paging, query
  coverage, or finalization is incomplete.
- **Replacement rule:** Declare the expected query set before reading. Track
  `useful`, `partial`, and `clean` separately, and advance the last-successful
  checkpoint only after clean finalization.
- **Proof:** A coverage gap produces a partial artifact and blocks a false
  clean checkpoint.

#### 21. File existence is not provenance

- **Failure:** A plausible filename in a cache is treated as a confirmed
  attachment or trusted source.
- **Replacement rule:** Record source system, parent record ID, attachment ID,
  original filename, retrieval time, and confidence. Skip ingestion when that
  chain cannot be established.
- **Proof:** Every imported file can be traced to the source record that
  supplied it.

#### 22. Returned data still needs a discoverable handshake

- **Failure:** An external read returns data in the conversation, but the local
  workflow cannot find or ingest the matching result. Repeating a broad search
  spends more without repairing the handoff.
- **Replacement rule:** Give each external read a run ID, declared result path,
  and ingest acknowledgement. Diagnose missing links before repeating the
  source query.
- **Proof:** The source request, returned result, stored artifact, and ingest
  receipt can be connected for the same run.

### Delivery, Validation, and Stewardship

#### 23. Planning risk and carrying out the plan are different jobs

- **Failure:** A good plan fails during execution, or a useful first slice is
  described as if the entire plan were complete. Trivial edits can also attract
  unnecessary ceremony.
- **Replacement rule:** Use plans for broad, risky, multi-step, or
  hard-to-verify work. Review privacy, noise, false confidence, user burden,
  failure modes, validation, and simpler paths before implementation. Reconcile
  each meaningful slice during execution.
- **Proof:** The closeout maps every planned item to complete, changed,
  blocked, deferred, or unsafe.

#### 24. Done needs proof and checkpoint honesty

- **Failure:** A polished patch or document is called complete without tests,
  visual inspection, source checks, diff review, or a real saved checkpoint.
- **Replacement rule:** Define proportional validation for each workflow.
  State what passed, what was not run, what remains uncertain, and whether a
  commit, publication, or other checkpoint actually happened.
- **Proof:** Evidence was produced after the final change and maps to the
  promised result rather than merely to implementation activity.

#### 25. Readiness, trust, acceptance, and utility are different projections

- **Failure:** A green harness or scorecard becomes “the system is ready” even
  when sources, review pressure, or live operating state remain unhealthy.
- **Replacement rule:** Keep separate answers for `does_it_work`,
  `is_it_safe_and_ready`, `is_it_useful`, and `is_current_evidence_healthy`.
  Refresh live-state claims rather than reusing old snapshots.
- **Proof:** The system can be technically passing, useful, and operationally
  unready at the same time without hiding the reason.

#### 26. Stabilize before adding features

- **Failure:** New dashboards, memory layers, automation, exports, and metrics
  are more attractive than backlog reduction, source repair, review cleanup,
  and proof.
- **Replacement rule:** Sequence work as live state, stabilization, backlog
  reduction, then feature growth. Keep a feature only if it changes a decision,
  reduces work, improves trust, or provides dependable proof.
- **Proof:** A review after real use can produce `keep`, `tighten`, `retire`, or
  `defer`, and sunk effort does not prevent retirement.

#### 27. Shareability requires a clean first-use test

- **Failure:** A package works only in its original workspace because it
  assumes hidden state, old filenames, a live interface, or unavailable tools.
- **Replacement rule:** Install the package into an empty folder and ask a
  fresh Codex session to follow only the included instructions. Record every
  missing file, hidden dependency, confusing term, and assumed capability.
- **Proof:** A new user can complete the first workflow from the public files
  alone and produce a reviewable result.

## Six Copy-Paste Prompts

### 1. Set up the workspace

```text
Help me build a small, file-based assistant for this workspace.

Do not start with an app, database, automation, or broad connector access.
Ask me no more than three questions:
1. What recurring work should this assistant improve first?
2. Which sources should it trust?
3. What must it never do without asking me?

Use the recurring-workspace starter to personalize the first version. Explain
what I can use immediately, what can wait, and give me one exact prompt for the
first workflow.
```

### 2. Run a material task

```text
Work this task through to a verified, saved result.

Before changing anything, state briefly:
- the intended outcome;
- the sources you will use;
- what you may change;
- what you must not infer or do;
- the smallest useful plan;
- how you will validate the result;
- where the final output will be saved.

Continue until the plan is complete, blocked, or unsafe. Do not treat a useful
first draft as completion. If evidence changes the plan, revise it. At the end,
state what was verified and what remains uncertain.
```

### 3. Review source quality

```text
Before answering, inspect the named sources.

Tell me whether the evidence is sufficient, useful but incomplete, stale and
in need of a targeted refresh, conflicting, or insufficient to answer safely.
Use the narrowest source set likely to answer the question. Separate evidence,
interpretation, recommendation, and action. Do not imply current evidence
unless you checked a current source.
```

### 4. Close out the work

```text
Close this work out properly.

- Save the reusable result outside chat.
- Check it against the original request and sources.
- Run the smallest meaningful validation.
- Inspect what changed and avoid unrelated edits.
- Record whether the result is ready to use, needs review, or is provisional.
- State the next action and when the output should be reviewed, replaced, or
  retired.
```

### 5. Turn a failure into a reusable lesson

```text
Review this failure without defending the previous output.

Identify the trigger, what failed, the likely cause, the smallest correction,
when that correction should and should not apply, and one realistic test that
would prove it works. Recommend whether the lesson belongs in the working
agreement, source guidance, a reusable workflow, a test case, or nowhere
durable.
```

### 6. Audit the system

```text
Audit this workspace as an operating system, not merely a collection of files
or features.

Look for noisy memory, missing sources treated as facts, feedback that does not
close work, review items without decisions, duplicate or stale outputs, context
waste, incomplete connector coverage, weak provenance, unproved ingestion,
machinery that adds more work than value, and completion claims without proof.

For each finding, provide the evidence, user consequence, smallest correction,
proof that it worked, and a keep, tighten, retire, or defer recommendation. Do
not change anything during the audit. Rank the five highest-value corrections.
```

## A Four-Week Adoption Plan

### Week 1: Prove one workflow

- Create the minimum workspace.
- Run one recurring job three times on real material.
- Save each material output.
- Record what was used, edited, rejected, or replaced.

Success means the workflow saves effort or improves a real decision. It does
not mean the workspace looks sophisticated.

### Week 2: Improve sources and boundaries

- Identify the smallest trusted source set.
- Record source authority, date, limitations, and review timing.
- Tighten approval boundaries and negative controls.
- Test a stale, missing, or conflicting source case.

Success means Codex is clearer about what it knows, what it does not know, and
what it may do.

### Week 3: Make the workflow repeatable

- Turn the successful process into a short command, checklist, or skill.
- Add realistic pass, fail, and ambiguous examples.
- Remove vague or duplicated instructions.
- Create a short handoff for continuing in a fresh session.

Success means a new session can reproduce the useful behaviour without
replaying the entire history.

### Week 4: Decide what has earned more machinery

- Review outputs and corrections.
- Keep, tighten, retire, or defer each workflow.
- Add retrieval, a script, or a small interface only where repeated use shows
  clear friction.
- Do not automate an unstable workflow.

Success means the system is simpler to operate at the end of the month, not
merely larger.

## What You Do Not Need at the Start

You do not need:

- a custom application;
- a database or vector store;
- multiple agents;
- broad inbox, calendar, chat, or drive access;
- background automation;
- a large skill library;
- a perfect architecture;
- the ability to write code yourself.

Your contribution is to define the job, choose trusted sources, set boundaries,
judge outputs, and decide what has earned the right to become repeatable.

## A Small Monthly Scorecard

- **Usefulness:** How many material outputs were actually used?
- **Edit burden:** Did outputs require fewer corrections over time?
- **Source quality:** Were important claims traceable and current enough?
- **Safety:** Were approval boundaries respected?
- **Reliability:** Did repeated workflows behave consistently?
- **Clutter:** Did the system add or remove places to monitor?
- **Continuity:** Could a fresh session continue from files and a short handoff?
- **Maintenance:** Are instructions, sources, and workflows still current?

The desired direction is more accepted work, less correction, clearer evidence,
and less operator burden. More files, prompts, tokens, dashboards, and
automations are not success measures by themselves.

## Evidence and Limits

These are experience-backed operating lessons, not proof that every assistant
needs the same architecture. Different roles and organisations require
different sources, terminology, risk boundaries, and levels of automation.

- **Evidence type:** Repeated failures, corrections, validation work, and
  feature retirement from a private long-running build.
- **External proof still required:** A new user should trial the starter on one
  real workflow and record use, edits, failures, and improvement over several
  runs.
- **Do not infer:** No permission to import private context; no claim that
  automation, connectors, or later technical machinery are required.
- **Review after:** The first outside trial or a material change in Codex's
  project workflow.
- **Retire or revise if:** The guide creates more setup and review work than the
  first workflow returns in value.

## Final Principle

Build the smallest system that can do one important piece of work well, prove
it, save it, and improve from the result. Everything else should be earned.

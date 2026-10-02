# Build a Working Assistant with Codex

Start with a job you repeat: a weekly research brief, a content plan, or a
review of outstanding work. Give Codex a few reliable sources, a place to save
the result, and clear limits on what it may change.

I drew these lessons from building a private assistant workspace. This guide
shares the working practices, without its private data, internal sources or
code. Try the small workspace below on one job before deciding whether the
practices fit your work.

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

Use these seven questions to review your first workflow:

1. **One clear front door.** The user asks for help in one place instead of
   learning several internal tools.
2. **A written agreement.** Purpose, sources, boundaries, output rules, and the
   definition of done are visible.
3. **A short saved record.** Priorities, confirmed context, reusable outputs,
   and review outcomes live in ordinary files rather than only in chat.
4. **A way to repeat the job.** Important jobs have a bounded method and a
   visible success condition.
5. **Approval before external action.** Drafting and analysis can be generous;
   sending, publishing, deleting, purchasing, or changing shared state needs a
   fresh decision.
6. **Proof before completion.** The assistant shows what changed, what was
   checked, and what remains uncertain.
7. **Learning from real use.** Record whether outputs were accepted, edited,
   rejected, replaced, or stale, then check whether a change helps the next run.

Do not copy a mature assistant feature for feature. Its design reflects one
person's work, sources, preferences, risks, and history. Replicate the pattern,
then let your own workflows earn additional complexity.

## 27 Lessons to Try

Each lesson describes a problem, a change to try, and a way to check it.
Choose the ones that match a problem you have encountered; you do not need to
turn all 27 into instructions.

### Memory and Context

#### 1. Keep useful context and mark what is uncertain

- **What went wrong:** Remembering almost nothing loses continuity. Capturing
  everything creates duplicates, stale claims, weak candidates, and review
  noise.
- **Try this:** Route durable context into `confirmed`, `provisional`,
  or `needs_judgement`. Record the source, source date, confidence, and review
  date.
- **How to check:** A later task can retrieve a useful confirmed item while an
  ambiguous or conflicting item remains visibly provisional.

Review stored notes for relevance and evidence before treating them as settled facts.

#### 2. Missing evidence must mean unknown, not false

- **What went wrong:** A missing message, absent field, stale source, or failed read is
  treated as proof that something did not happen.
- **Try this:** Make `unknown_due_to_missing_source` a valid result.
  Distinguish source-backed, provisional, conflicting, partial, and unavailable
  evidence.
- **How to check:** Tests include missing, stale, conflicting, and partial sources and
  produce calibrated uncertainty rather than confident negative claims.

#### 3. Retrieval hints are not relationship or ownership proof

- **What went wrong:** Co-occurrence in a meeting, document, or thread becomes an
  inferred reporting line, commitment, preference, or owner.
- **Try this:** Store `related_for_search` separately from
  `relationship_proven`. Consequential relationships require an authoritative
  source, a defined relationship type, freshness, confidence, and no unresolved
  conflict.
- **How to check:** Repeated mentions improve discovery without silently creating a
  typed relationship.

#### 4. Check names before creating new records

- **What went wrong:** Names with initials, punctuation, nicknames, or variants create
  duplicate records. Generic words become people or projects. Two records can
  overwrite the same readable profile.
- **Try this:** Check aliases and canonical names before accepting a
  new entity. Reject obvious noise deterministically and leave uncertain
  remaps provisional.
- **How to check:** Cases covering initials, punctuation, aliases, generic nouns, and
  duplicate readable names cannot create silent collisions.

#### 5. Try finding each source after you save it

- **What went wrong:** A document appears registered even though extraction failed,
  stored chunks are unusable, or retrieval reaches only a derived summary.
- **Try this:** Give every ingested source a receipt covering file
  identity, extraction status, chunk count, source metadata, and a
  source-specific retrieval example.
- **How to check:** Every supplied file independently answers a smoke query that
  reaches the expected source.

### Feedback, Writing, and Learning

#### 6. The version actually used is stronger evidence than the draft

- **What went wrong:** Writing guidance learns from what the assistant proposed rather
  than what the user edited, discarded, or sent.
- **Try this:** Compare the proposed and used versions. Record what was
  cut, added, softened, clarified, or made more human, and apply the lesson to
  the matching writing mode.
- **How to check:** A later draft reproduces the accepted pattern without copying raw
  private messages into long-term context.

#### 7. Feedback must close the matching work item

- **What went wrong:** The system learns from “I used that” but continues asking the
  user to review the same draft.
- **Try this:** Give reusable outputs stable IDs. Resolve feedback by
  exact ID, exact active title, or a uniquely focused recent item; ask when the
  reference is ambiguous. Apply the outcome and learning record together.
- **How to check:** A used, rejected, superseded, or archived output leaves no stale
  pending review behind.

#### 8. Follow-through is not recommendation quality

- **What went wrong:** A used recommendation is automatically counted as good, while
  an unused recommendation is treated as bad.
- **Try this:** Track `what_happened` separately from
  `recommendation_quality`. Quality still needs human judgement, source
  quality, and outcome evidence.
- **How to check:** The system can record “used but weak” and “good but not acted on”
  without contradiction.

#### 9. Skills should encode proven workflows, not accumulated advice

- **What went wrong:** Generic skills and long instruction files grow faster than
  reliable behaviour.
- **Try this:** Create a skill only after a workflow or failure recurs.
  Give it a precise trigger, required steps, a known failure pattern, and a
  realistic validation prompt. Retire it if it does not improve real work.
- **How to check:** The same relevant prompt produces the intended workflow in a fresh
  session without loading unrelated guidance.

### Attention and Review Noise

#### 10. Ask for review when there is a decision to make

- **What went wrong:** Review queues fill with routine meetings, status messages,
  empty runs, receipts, and other items that require no decision.
- **Try this:** Before surfacing an item, answer: `Who must decide
  what?` Keep routine evidence quiet. Surface user-facing work, approvals,
  ambiguity, material risks, and genuine exceptions.
- **How to check:** Every visible review item names a decision, approval, ambiguity,
  risk, or useful review action.

#### 11. Give each output a lasting ID and a clear status

- **What went wrong:** Re-running a report creates duplicates, while replaced or
  completed drafts remain pending indefinitely.
- **Try this:** Register outputs by stable purpose and artifact
  identity. Support terminal states such as `used`, `acknowledged`, `archived`,
  and `superseded`.
- **How to check:** Re-running the same workflow updates the right record unless the
  content or routing identity genuinely changed.

#### 12. Wrong surface is useful feedback

- **What went wrong:** A useful item appears in the wrong place, but the only choices
  are to use it or archive it.
- **Try this:** Treat `wrong_surface` as different from
  `wrong_content`. Record where the item belonged and aggregate repeated
  corrections before changing policy.
- **How to check:** A routing correction improves later placement without one click
  silently rewriting system-wide rules.

#### 13. Interfaces should remove monitoring burden

- **What went wrong:** Tabs, dashboards, queues, diagnostic pages, and compatibility
  views create more places the user feels obliged to check.
- **Try this:** Keep one conversational front door, one compact daily
  companion if needed, and explicit drill-down or diagnostic surfaces. A new
  daily surface should replace an old burden.
- **How to check:** The user can operate the workflow without learning the internal
  machinery or monitoring several locations.

#### 14. Silence and nothing due can be healthy

- **What went wrong:** A quiet scheduled run looks broken, or a health threshold is
  shorter than the real schedule and creates false alarms.
- **Try this:** Define the expected silent state and align freshness
  thresholds with the actual cadence. Alert on evidence of missed work or
  broken state, not on the absence of chatter.
- **How to check:** Tests cover both `something_due` and `nothing_due`, and a healthy
  quiet run leaves a fresh status record.

### Token and Context Efficiency

#### 15. Diagnose token waste before compressing quality

- **What went wrong:** “Use fewer tokens” produces shorter answers, weaker reasoning,
  or skipped validation while repeated context and raw output remain.
- **Try this:** Measure cost by workflow, output shape, and terminal
  outcome. Find replay, broad status dumps, raw payloads, and abandoned long
  sessions before lowering reasoning quality.
- **How to check:** A change removes a named source of waste while the same acceptance
  evidence still passes.

#### 16. Keep the instructions loaded for every task short

- **What went wrong:** Detailed recipes, preferences, and examples are loaded into
  every task, even when irrelevant.
- **Try this:** Keep only universal safety, authority, working style,
  and completion rules always on. Load task recipes and examples on demand.
- **How to check:** A smaller instruction kernel preserves boundary and validation
  behaviour across representative tasks.

#### 17. Keep raw payloads out of the working chat

- **What went wrong:** Full connector results, spreadsheets, transcripts, JSON, or
  binary content flood the conversation and cannot be reliably removed later.
- **Try this:** Save raw evidence to declared files. Return compact
  source cards, IDs, audit paths, and decision-relevant summaries to chat.
- **How to check:** A fresh session can continue from a short handoff and source
  handles without replaying the raw material.

#### 18. Use different context depths

- **What went wrong:** Routine tasks receive either too little context or the same deep
  bundle used for audits and meeting preparation.
- **Try this:** Define `fast`, `normal`, and `deep` modes with explicit
  source-card limits and a discoverable location for omitted evidence.
- **How to check:** A routine question uses a small packet; a complex task expands
  deliberately and can still trace every important claim.

#### 19. Make the task and checks clear before changing models

- **What went wrong:** Expensive reasoning compensates for implicit sources,
  boundaries, validation, and stop rules, while consequential work may still
  be under-framed.
- **Try this:** For material tasks, state the task family, source
  posture, authority boundary, output target, risks, smallest plan, validation,
  and stop condition. Escalate when the frame is uncertain, evidence conflicts,
  or action is hard to reverse.
- **How to check:** The workflow produces consistent, reviewable decisions across
  model or reasoning settings without letting efficiency override safety.

### Connectors, Provenance, and Source Truth

#### 20. A connector call is not completion proof

- **What went wrong:** Useful messages appear in chat even though paging, query
  coverage, or finalization is incomplete.
- **Try this:** Declare the expected query set before reading. Track
  `useful`, `partial`, and `clean` separately, and advance the last-successful
  checkpoint only after clean finalization.
- **How to check:** A coverage gap produces a partial artifact and blocks a false
  clean checkpoint.

#### 21. File existence is not provenance

- **What went wrong:** A plausible filename in a cache is treated as a confirmed
  attachment or trusted source.
- **Try this:** Record source system, parent record ID, attachment ID,
  original filename, retrieval time, and confidence. Skip ingestion when that
  chain cannot be established.
- **How to check:** Every imported file can be traced to the source record that
  supplied it.

#### 22. Check that returned data reaches the right file

- **What went wrong:** An external read returns data in the conversation, but the local
  workflow cannot find or ingest the matching result. Repeating a broad search
  spends more without repairing the handoff.
- **Try this:** Give each external read a run ID, declared result path,
  and ingest acknowledgement. Diagnose missing links before repeating the
  source query.
- **How to check:** The source request, returned result, stored artifact, and ingest
  receipt can be connected for the same run.

### Delivery, Validation, and Stewardship

#### 23. Planning risk and carrying out the plan are different jobs

- **What went wrong:** A good plan fails during execution, or a useful first slice is
  described as if the entire plan were complete. Trivial edits can also attract
  unnecessary ceremony.
- **Try this:** Use plans for broad, risky, multi-step, or
  hard-to-verify work. Review privacy, noise, false confidence, user burden,
  failure modes, validation, and simpler paths before implementation. Reconcile
  each meaningful slice during execution.
- **How to check:** The closeout maps every planned item to complete, changed,
  blocked, deferred, or unsafe.

#### 24. Done needs proof and checkpoint honesty

- **What went wrong:** A polished patch or document is called complete without tests,
  visual inspection, source checks, diff review, or a real saved checkpoint.
- **Try this:** Define proportional validation for each workflow.
  State what passed, what was not run, what remains uncertain, and whether a
  commit, publication, or other checkpoint actually happened.
- **How to check:** Evidence was produced after the final change and maps to the
  promised result rather than merely to implementation activity.

#### 25. Check whether it works, whether it is ready, and whether it helps

- **What went wrong:** A green harness or scorecard becomes “the system is ready” even
  when sources, review pressure, or live operating state remain unhealthy.
- **Try this:** Keep separate answers for `does_it_work`,
  `is_it_safe_and_ready`, `is_it_useful`, and `is_current_evidence_healthy`.
  Refresh live-state claims rather than reusing old snapshots.
- **How to check:** The system can be technically passing, useful, and operationally
  unready at the same time without hiding the reason.

#### 26. Stabilize before adding features

- **What went wrong:** New dashboards, memory layers, automation, exports, and metrics
  are more attractive than backlog reduction, source repair, review cleanup,
  and proof.
- **Try this:** Sequence work as live state, stabilization, backlog
  reduction, then feature growth. Keep a feature only if it changes a decision,
  reduces work, improves trust, or provides dependable proof.
- **How to check:** A review after real use can produce `keep`, `tighten`, `retire`, or
  `defer`, and sunk effort does not prevent retirement.

#### 27. Shareability requires a clean first-use test

- **What went wrong:** A package works only in its original workspace because it
  assumes hidden state, old filenames, a live interface, or unavailable tools.
- **Try this:** Install the package into an empty folder and ask a
  fresh Codex session to follow only the included instructions. Record every
  missing file, hidden dependency, confusing term, and assumed capability.
- **How to check:** A new user can complete the first workflow from the public files
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

## What These Lessons Show

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

## Keep the First Job in View

Build the smallest system that can do one important piece of work well, prove
it, save it, and improve from the result. Everything else should be earned.

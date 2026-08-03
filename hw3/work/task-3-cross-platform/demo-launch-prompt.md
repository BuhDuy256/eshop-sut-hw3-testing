You are running a prepared Agent Skills demo. First read the demo
implementation plan, demo workspace state, both SKILL.md files, and the
current validation record. Do not ask the user for setup details that are
already available in the repository.

Read these files, in this order, before doing anything else or saying
anything to the user:

1. `hw3/work/task-3-cross-platform/demo-skill-implementation-plan.md` — the
   full demo plan (goal, scope, flow, checkpoint strategy, failure/recovery
   strategy, video structure, required output).
2. `hw3/work/task-3-cross-platform/demo-workspace/README.md`,
   `demo-state.md`, `demo-run-log.md`, `demo-output-summary.md`,
   `dry-run-result.md` — current workspace state and the dry-run result from
   the preparation session (already passed; no discrepancy is expected, but
   re-verify live rather than trusting the cached numbers).
3. `.claude/skills/compat-run-planner/SKILL.md` and
   `.claude/skills/compat-evidence-report/SKILL.md` — the two skills you
   will invoke.
4. `hw3/work/task-3-cross-platform/skill-validation.md` — prior validation
   baseline for both skills.

## Project context (do not ask the user to re-explain this)

Repository root: `C:\Users\Duy\Desktop\eshop-sut-hw3-testing`. This is HW03
(GUI & Usability Testing) for the EMS system. Task 3 (cross-browser /
cross-platform compatibility testing) is done; two Agent Skills were built
from that real workflow:

- `compat-run-planner` — reads the working compatibility manifest, evidence
  folders, and run logs, and reports true coverage without changing any
  verdict.
- `compat-evidence-report` — reads reviewed evidence and run logs and
  drafts/refreshes a report into `hw3/work/task-3-cross-platform/report-draft.md`,
  never into `hw3/out/`.

**Source-of-truth numbers — use these throughout, do not recompute from
memory, always re-verify live against the real files:**

```text
Manifest rows: 28
Executed cells: 20
- Pass: 19
- Fail: 1 — C1 / Run F / iOS / Safari / Phone, Finding F-022, severity 2
Blocked cells: 8
- Run D / macOS Safari Desktop × C1–C4
- Run E / iOS Tablet × C1–C4
- No Pass/Fail on Blocked rows
Supplementary validation:
- C3 Full Confirm Final Validation, Run A / Chrome / Windows
- NOT a new cell — only upgrades C3/Run A's Interaction Coverage field to
  "Full confirm flow"
Coverage (Executed rows): OS 2/3 (Windows, iOS), Browser 5/5, Device 2/3
  (Desktop, Phone)
Missing artifacts: 0. File-name mismatch: 0.
```

Never use 24 as the Executed target, never call a Blocked row a Fail, never
count the C3 Full Confirm step as cell #21 or manifest row #29.

## What this session is for

Record one demo video (single take, ~3–5 minutes) proving both skills run
for real against the actual Task 3 artifacts:

- Part 1: invoke `compat-run-planner`, show its output, confirm it matches
  the source-of-truth numbers above.
- Part 2: invoke `compat-evidence-report`, show it refresh
  `hw3/work/task-3-cross-platform/report-draft.md`, confirm the output stays
  entirely inside `hw3/work/` and covers all 12 required sections (Scope and
  methodology; Executed coverage; Pass/Fail matrix; Blocked coverage;
  Requirement gap; F-022 finding; C3 Interaction Coverage; Actual Execution
  Mode summary; Evidence index; Limitations and residual risks; Human-review
  statement; AI-use summary).

This session does **not**:
- Re-run any UI test against EMS.
- Change any verdict.
- Fabricate any evidence or number.
- Promote anything to `hw3/out/` (no final matrix, no final report, no
  copying either SKILL.md to `hw3/out/agent-skills/`).
- Touch Main Report, Findings Log promotion, or ZIP submission — out of
  scope entirely.

## Approval behavior — follow this exactly

You run autonomously between checkpoints. Do **not** ask open-ended
questions like "what would you like to do next?" You decide on your own
when a stop is actually required, using this rule:

**Run without asking, no confirmation needed, for:**
- Reading any file, listing any directory.
- Invoking either skill.
- Generating or refreshing `report-draft.md`.
- Any other read-only or working-draft-only action.

**Stop and wait for approval only at these points:**
1. Before you start recording (first checkpoint of the session).
2. After Skill 1 produces its output, before treating it as validated.
3. Before applying any correction, if Skill 1 or Skill 2 output disagrees
   with the source-of-truth numbers above.
4. After Skill 2 produces its output, before treating it as validated.
5. At the end of the demo, before telling the user to stop recording (and
   before any final promotion — though none is planned in this session).

At every one of these points:
- Present exactly one concrete, already-prepared action proposal — never a
  list of options, never an open question.
- If the platform supports an action-card / approval UI control, use that
  form instead of asking the user to type a word.
- Otherwise, end your message with a single clear call to action the user
  can satisfy by typing "Approve" — nothing else required from them.
- After the user approves, continue immediately. Do not re-ask about the
  same thing, do not ask for confirmation of something already approved,
  and do not ask the user to type any command, path, or file content
  themselves — you already have everything you need from the repository.

If something breaks that you cannot resolve on your own (a file genuinely
missing, a skill erroring in a way this prompt doesn't anticipate), then and
only then present the discrepancy plainly (expected vs. actual) with one
recommended fix, and wait for approval before applying it.

## Failure / recovery behavior

If either skill's output disagrees with the source-of-truth numbers above:

1. Stop immediately — do not continue the demo with the wrong numbers on
   screen.
2. Show expected vs. actual in a short table.
3. Propose exactly one concrete correction.
4. Wait for approval.
5. After approval, apply the fix only inside `hw3/work/` — never touch
   `hw3/out/` during this session.
6. Re-run only the affected part (not the whole demo from the start).
7. Resume the demo from where it stopped.

## Session flow

1. **Pre-demo setup** (silent, no approval needed): read all files listed
   above, re-verify the source-of-truth numbers live against the real
   manifest/evidence/run-log files (don't just trust `dry-run-result.md`),
   confirm both skills load.
2. **Start checkpoint:** once setup is confirmed clean, present the
   prepared proposal "Ready to start recording Part 1 (`compat-run-planner`)
   — say Approve to begin." Wait.
3. **Demo Skill 1:** invoke `compat-run-planner` for real, present its full
   output.
4. **Validation checkpoint 1:** compare the output to the source-of-truth
   numbers; if it matches, propose "Skill 1 output confirmed correct —
   Approve to continue to Part 2 (`compat-evidence-report`)." If it doesn't
   match, follow Failure/recovery behavior above instead.
5. **Demo Skill 2:** invoke `compat-evidence-report` for real, refresh
   `hw3/work/task-3-cross-platform/report-draft.md`, present its output
   (confirm all 12 sections and confirm the write path is inside
   `hw3/work/`).
6. **Validation checkpoint 2:** compare against requirements; if correct,
   propose "Skill 2 output confirmed correct — Approve to move to final
   summary."
7. **Final summary:** state on screen: both skills ran on real artifacts,
   final numbers (20 Executed / 19 Pass / 1 Fail / 8 Blocked), confirm no
   promotion happened during this session.
8. **End checkpoint:** propose "Demo complete — Approve to stop recording."
   Wait.
9. **Post-demo artifact update** (silent, no approval needed): update
   `hw3/work/task-3-cross-platform/demo-workspace/demo-state.md`,
   `demo-run-log.md`, and `demo-output-summary.md` with what actually
   happened during this video session (the "Video thật" rows/sections in
   each file are reserved for this). Do not touch `hw3/out/`.

After Step 9, tell the user recording is safe to upload, and that you're
ready to record the video URL once they provide it (do not invent a
placeholder URL — leave it unset until the user gives a real one, and when
they do, write it only into
`hw3/work/task-3-cross-platform/demo-video-links-draft.md`, never directly
into `hw3/out/`).

## Constraints that apply throughout

- No password, cookie, token, or personal email other than the student
  email already present in existing evidence
  (`23127179@student.hcmus.edu.vn`) may ever appear on screen.
- Do not open all 28 manifest rows or every individual screenshot on
  screen — only show each skill's own summarized output.
- Do not promote anything to `hw3/out/` under any circumstance in this
  session.

Begin now: read the files listed at the top of this prompt, re-verify the
source-of-truth numbers live, and then present the Start checkpoint.

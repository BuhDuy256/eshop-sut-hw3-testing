# Demo Video Links — Draft (Agent Skills, Task 3)

Working draft. Promoted (verbatim) to
`hw3/out/reports/task-3-cross-platform/demo-video-links.md` once reviewed.

## Video

| Field | Value |
|---|---|
| **URL** | https://youtu.be/GbhAEK7x8Vk |
| **Provided by** | Student (Nguyễn Bảo Duy, 23127179), given directly in chat |
| **Link status** | Provided by student; upload completed |
| **Independently opened/verified by AI?** | **No.** This URL has not been fetched or played back by the assistant in this session — it is recorded as given, not independently verified. |
| **Recording date** | 2026-08-03 (per `demo-workspace/demo-state.md` and `demo-run-log.md`, "Video thật" section) |
| **Skills demonstrated** | `compat-run-planner`, `compat-evidence-report` |

## Structure (as planned in `demo-skill-implementation-plan.md` Mục 6)

| Segment | Content | Timestamp |
|---|---|---|
| Intro | Demo goal, the two skills to be run | Timestamp not independently recorded during the session |
| Part 1 | `compat-run-planner` invoked live; output shown (20 Executed / 19 Pass / 1 Fail / 8 Blocked, coverage, missing/mismatch = 0); validation checkpoint | Timestamp not independently recorded during the session |
| Part 2 | `compat-evidence-report` invoked live; `report-draft.md` refreshed in `hw3/work/`; 12-section output shown; validation checkpoint | Timestamp not independently recorded during the session |
| Final summary | Confirmed numbers match source of truth; confirmed no promotion to `hw3/out/` occurred during the session | Timestamp not independently recorded during the session |

No relative timestamps were logged during the session in
`demo-run-log.md` beyond the ordered step list, so exact mm:ss markers
cannot be stated without guessing. The ordered steps above are read directly
from `demo-run-log.md`'s "Video thật" section (a real record from the video
session, not reconstructed here).

## What the recorded session actually confirms (from `demo-workspace/` records)

- Both skills were invoked for real against the actual Task 3 artifacts
  (not a rehearsal restated as if new) — evidenced by
  `demo-workspace/report-draft.backup-pre-video.md`, a backup created
  specifically during the video session before `report-draft.md` was
  overwritten again.
- Skill 1 output: 20 Executed / 19 Pass / 1 Fail (C1/Run F/iOS/Safari/Phone,
  F-022, severity 2) / 8 Blocked, OS 2/3, Browser 5/5, Device 2/3, missing
  artifacts = 0, file-name mismatch = 0.
- Skill 2 output: `report-draft.md` refreshed with all 12 required sections,
  no use of the numbers 24/23, Blocked never called Fail, output confirmed
  to remain only inside `hw3/work/`.
- No discrepancy was triggered during the recorded session (per
  `demo-output-summary.md`'s "Video thật" row) — the Failure/recovery branch
  of the plan was not exercised in this recording.
- No file inside `hw3/out/reports/task-3-cross-platform/` (other than the
  pre-existing `evidence/` folder) was created or modified during the demo
  session.

## Note on video-content verification

This draft records what the session logs say happened, cross-checked
against real file artifacts (the backup file, the updated workspace state
files). It does **not** constitute independent verification of the video's
actual visual/audio content — no one has watched the video back in this
session. If the student wants the assistant to review the actual footage
before final submission, that requires explicitly fetching/opening the URL,
which has not been done here.

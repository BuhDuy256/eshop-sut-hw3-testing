---
name: compat_evidence_report
description: >
  Reads a reviewed compatibility manifest together with raw evidence,
  annotated candidates, the final verdicts recorded in run logs, blocker
  evidence, and any findings tied to a Fail cell, and drafts a cross-platform
  compatibility report. Checks that every piece of evidence actually shows
  what it claims to show — the overlay's email, screen ID, OS, browser,
  device, and timestamp, the EMS URL, the correct browser window, and a clear
  trail back through candidate to raw — and keeps Pass, Fail, and Blocked /
  Not Executed as three distinct states throughout. Writes only to a draft
  file inside the working directory; it never writes into the frozen output
  folder.
---

# Compat Evidence Report

Turns reviewed Task 3 evidence and run logs into a report draft; the stage
order matters because evidence must be checked before it is cited, and every
section must be written from what Stage 1–2 actually confirmed — never from
what the report "should" say to look complete.

---

## Skill Metadata

**Task Type:** Compatibility Test Report Drafting
**Methodology:** Evidence-first drafting — verify each cell's evidence →
verify blocker evidence → write each of the twelve required sections strictly
from verified inputs → write only to the working draft path.

---

## Authoritative Inputs

Only treat each input as authoritative for what it actually contains.

| Input | Authoritative for | NOT authoritative for |
|---|---|---|
| Reviewed working manifest | Which rows are Executed, Blocked, or Supplementary, and each row's stated verdict / Interaction Coverage / Execution Mode | Whether the underlying evidence file actually matches what the row claims — check the file itself |
| `raw-evidence/` | The unannotated capture behind a promoted file | Whether it was ever reviewed — review status comes from the candidate/promotion stage |
| `annotated-candidates/` | What the overlay actually shows (email, screen, OS, browser, device, timestamp) once opened and read | Whether it was promoted to final evidence — check the final evidence folder |
| Run logs' final verdicts | The Pass/Fail/Dialog-only/Full-confirm-flow text for each screen, and any incident notes | Anything the log doesn't say — never pad a thin log entry with an assumed detail |
| Blocker evidence (banner screenshot + pilot note) | Why Blocked rows have no verdict | Whether a Blocked row could have passed — that was never tested and must not be implied |
| F-022 draft + working findings log | The Fail cell's finding content, severity, and submission status exactly as recorded | A submission date/timestamp beyond what's actually recorded — cite the same hedged wording the findings log uses |

---

## Guardrails (non-negotiable — apply in every stage)

1. Never write to anything outside `hw3/work/task-3-cross-platform/report-draft.md`. No output goes into `hw3/out/`.
2. Never call a Blocked row a Fail. Blocked means "not executed, no verdict" — a different state from a Fail, which means "executed and did not pass."
3. Never describe the 28 manifest rows as "28 cells tested." Only the 20 Executed rows were tested; the other 8 are Blocked / Not Executed.
4. Never fold the C3 Full Confirm Final Validation into the Executed count as a new row — it is a field upgrade on the existing C3/Run A row.
5. Never state a date, timestamp, or submission fact more confidently than the source artifact does. If a source uses hedged wording (e.g. "recorded — not independently verified this session"), carry that same hedge into the report.
6. Never invent an EMS URL, timestamp, or overlay detail that isn't visible in the actual evidence file — open and read the file before citing what it shows.

---

## Stage 1: Load reviewed inputs

**Objective:** Gather everything the report will cite before drafting any
section.

- **Step 1.1 — Load the reviewed working manifest** (Executed, Blocked, and
  Supplementary Validation sections, kept separate).
- **Step 1.2 — Load run logs' final verdicts** for every Executed cell.
- **Step 1.3 — Load blocker evidence** (banner screenshot path + pilot
  note/log describing what was tried and why it failed).
- **Step 1.4 — Load the Fail cell's finding** (F-022 draft and its row in the
  working findings log) exactly as currently worded.

---

## Stage 2: Verify evidence before citing it

**Objective:** Confirm each piece of evidence shows what the report is about
to claim it shows.

- **Step 2.1 — Open and check each final evidence file:**
  - **Input:** A final (promoted) evidence file for one Executed cell.
  - **Reasoning:**
    → Does the overlay show the correct student email, Screen ID, OS,
      Browser, Device, and a timestamp — all matching what this cell claims
      to be?
    → Is the EMS URL visible (address bar or an equivalent), and does it
      match the screen this cell is supposed to show?
    → Does the visible window/browser chrome match the browser this cell
      claims to test (not some other tab or application)?
    → If a URL or address bar is missing for a legitimate, previously
      disclosed reason (e.g. a mobile download panel covering it), is that
      exception already documented in the run log? Cite the exception, don't
      silently ignore the gap or silently invent a URL.
  - **Output:** A confirmed/flagged status for this file's evidence
    correctness.
- **Step 2.2 — Check raw → candidate → final traceability** for the same
  cell, and confirm which files are primary versus supplementary for that
  cell.
- **Step 2.3 — Check blocker evidence** shows the actual banner/limit
  encountered, matching the pilot note's description.

---

## Stage 3: Draft the report sections

**Objective:** Write each required section strictly from what Stage 1–2
confirmed — no section may assert something beyond its verified source.

- **Step 3.1 — Scope and methodology.** Plain action: state the Coverage
  Fallback Strategy, the No-DOM Policy, and the actor model, as already
  documented in the plan — do not re-justify or alter them here.
- **Step 3.2 — Executed coverage.** Plain action: the 20-row table from
  Stage 1/2, each row's OS/Browser/Device/verdict/evidence refs.
- **Step 3.3 — Pass/Fail matrix:**
  - **Input:** The 20 Executed rows and their verdicts.
  - **Reasoning:**
    → Does every Fail row cite its finding ID and severity? Does every Pass
      row cite the evidence that supports it, not just assert "Pass"?
  - **Output:** A matrix with 19 Pass, 1 Fail (C1/Run F/iOS/Safari/Phone,
    F-022, severity 2), each cited to evidence.
- **Step 3.4 — Blocked coverage.** Plain action: the 8-row table, each row's
  reason and blocker evidence path, explicitly labeled "Blocked / Not
  Executed" — never "Fail."
- **Step 3.5 — Requirement gap.** Plain action: state the assignment's ideal
  3 OS × 5 browser × 3 device-class target against what Executed rows
  actually cover, and name the residual risk (unknown behavior on macOS
  Safari and on a real tablet).
- **Step 3.6 — F-022 finding.** Plain action: reproduce the finding content
  from the draft/working log verbatim — description, steps, severity,
  evidence, and the exact hedged submission-status wording already in the
  findings log (never a more confident restatement).
- **Step 3.7 — C3 Interaction Coverage.** Plain action: state Dialog-only for
  Runs B/C/G/F and Full confirm flow for Run A, and that the Full Confirm
  step is a field upgrade, not a new cell.
- **Step 3.8 — Actual Execution Mode summary.** Plain action: tri-state count
  (AI-executed / AI-executed with human checkpoints / Human-executed with AI
  guidance) exactly as each run log states it — never inferred for a cell the
  log doesn't cover.
- **Step 3.9 — Evidence index.** Plain action: list every promoted evidence
  file with its cell, and mark primary vs. supplementary.
- **Step 3.10 — Limitations and residual risks.** Plain action: BrowserStack
  trial limitation, the untested macOS/Tablet gap, and any evidence exception
  already disclosed (e.g. the C4/Run F missing URL).
- **Step 3.11 — Human-review statement.** Plain action: a placeholder marking
  where the student's own review statement belongs — this skill does not
  write it on the student's behalf.
- **Step 3.12 — AI-use summary.** Plain action: which stages were
  AI-executed, human-guided, or human-executed, at a section level — cross-
  reference the AI Audit rather than duplicating it in full.

---

## Stage 4: Write the draft, nowhere else

**Objective:** Guarantee the output lands only in the working draft path.

- **Step 4.1 — Write to `hw3/work/task-3-cross-platform/report-draft.md`.**
  Overwrite only this path. Do not touch `hw3/out/` in this stage under any
  condition.

---

## Output Format

A single Markdown file, `report-draft.md`, containing exactly the twelve
sections from Stage 3 in that order, each one sourced only from what Stage 1–2
verified. No section may introduce a fact that wasn't already confirmed
against a real file or log entry earlier in the run.

# Manual Pilot Strategy for HW3

**Requirement source:** `hw3/docs/hw3-reqs/2026.HW03.GUI Usability EMS_En.md`
**Frozen input:** `hw3/docs/gui-checklist/Shared_GUI_Checklist.md` — v1.9, 60 items
**Scope:** Scenario **C**, screens **C1–C4**
**Last updated:** 2026-08-02

This document defines pilot strategies for each pipeline that needs one before scaling up execution. A pilot proves the *method* on a small slice; nothing here designs test content.

> **What is no longer a pilot.** Checklist *design* was Task 1A and is finished. There is no mini-checklist to draft and no item-granularity question left open — those were settled across five documented review rounds. Pilot 1 below is a pilot of **execution**, not of design.

## Pilot 1: Checklist Execution Pilot (one screen)

**Why pilot this first:**
Execution is the highest-volume work in the assignment — 60 items × 4 screens. Any friction in the verdict format, the evidence workflow or the per-item time cost multiplies by 240. Prove it once on one screen before paying it four times.

**What to pilot:**
- Pick **C1 (Users list)** — the widest surface in scenario C (table, filters, search, pagination, sidebar, toolbar, empty/loading states), so it exercises the largest share of applicable items.
- Execute **every** checklist item against C1 on the live EMS, marking **Pass / Fail / N/A**.
- Write a one-line reason for every **N/A** and for every **Fail**.
- Capture evidence for **Failed items only**, using the naming convention in `execution-workflow.md` §3b.
- Write 1–2 bug reports from Failed items.
- Submit **1** finding to the Google Form to prove the submission workflow end to end, and log it with its timestamp.

**Artifacts to produce during pilot:**
- `hw3/out/reports/checklist-execution/C1.md` — the full execution table for one screen.
- Evidence files for the failures, named per convention.
- 1–2 bug reports in the agreed structure (ID, screen, steps, expected, actual, severity, screenshot ref).
- 1 Google Form submission + its matching Findings Log entry.

**What to learn:**
- **Time per item**, and therefore the real cost of the remaining three screens. This is the number the pilot exists to produce.
- Which items turn out **N/A on the user-admin surface** versus the 14 the checklist predicted — a prediction is not a result.
- Whether the verdict table stays readable at 60 rows, or needs grouping by IA.
- Whether evidence naming survives contact with a real screenshot folder.
- Whether the Google Form's fields accept everything my bug-report structure carries.
- Where AI help is genuinely useful (formatting a bug report from notes) versus where it cannot go (deciding whether a heuristic item passes on a real screen).

**Exit criteria:**
- All 60 items executed on C1 with real evidence, every N/A justified.
- ≥ 1 real bug documented with a screenshot.
- 1 Google Form submission confirmed and logged.
- A measured time estimate for scaling to C2, C3 and C4.

**What NOT to do in the pilot:**
- **Do not edit, extend or reword the checklist** — §18 requires it identical across the group.
- Don't cover the other screens yet.
- Don't extract a skill yet — the methodology is not proven until this pilot closes.
- Don't read or reason about EMS source code; there is none available and none is permitted as justification.

## Pilot 2: Cross-Browser/Cross-Platform Pilot

**Why pilot this:**
BrowserStack workflow is entirely new — need to prove it works before building the full matrix.

**What to pilot:**
- Open BrowserStack/LambdaTest account.
- Test **C1** on 3 different configurations (1 desktop Chrome, 1 tablet Safari, 1 mobile Android).
- Capture screenshots with the `MSSV@....edu.vn` overlay, the EMS URL and the browser/OS/device identity all visible in the same frame.
- Verify screenshots show browser/OS/device identity alongside EMS URL.
- Document 1 rendering issue if found.

**Artifacts to produce:**
- 3 screenshots with proper overlay.
- Mini compatibility matrix (1 screen × 3 configs).
- 1 compatibility defect report if applicable.

**What to learn:**
- How to efficiently capture screenshots with overlays in BrowserStack.
- How to organize screenshot files.
- What rendering issues look like across platforms.
- How long each configuration takes (time estimation for full matrix).

**Exit criteria:**
- BrowserStack account working.
- 3 valid screenshots with overlay captured.
- Screenshot naming convention established.
- Time estimate for full matrix calculated.

## Pilot 3: User Testing Pilot

**Why pilot this:**
Requirement explicitly says 'run a pilot with one extra person' (§6 Task 2 Phase 1). This is REQUIRED, not optional.

**Open question this pilot must settle first — who is a realistic user of scenario C?**
§6 says participants must match *"the target user profile (students, lecturers, or event-goers as fits your scenario)"*. Scenario C is **admin-side user administration**, so its real-world user is faculty staff, not a student attendee. Two workable readings, to be decided in Step 6 and stated explicitly in the Usability Report:
1. Recruit people who plausibly do administrative work (staff, club/organisation committee members) and give them the admin account.
2. Recruit ordinary participants and frame the task as *"you have just been given the admin account — do X"*, treating first-use learnability as the thing being measured.
Either is defensible; leaving it unstated is not, because it changes how the SUS score should be read. The pilot participant is the right place to find out which framing actually works.

**What to pilot:**
- Write draft task scenario — goal-oriented, on C1–C4 (e.g. *"a lecturer says they cannot sign in — find their account, check its state, and restore their access"*), **not** step-by-step clicks.
- Define metrics (task success, time on task, error/hesitation count, SUS or UEQ-S) and probe questions on clarity, error recovery, speed and trust.
- Run pilot with 1 extra person (**NOT** one of the 5 real participants).
- Observe friction, unclear instructions, broken flows.
- Refine scenario based on pilot findings.

**Artifacts to produce:**
- Draft task scenario (v1).
- Metrics definition.
- Pilot session notes (what went wrong, what was unclear).
- Refined task scenario (v2).
- SUS/UEQ-S form/template.

**What to learn:**
- Is the task scenario clear enough?
- Does the EMS flow actually work end-to-end for this scenario?
- Are the screens accessible and functional?
- How long does a session take?
- Is the SUS/UEQ-S format appropriate?

**Exit criteria:**
- Pilot completed with 1 real person.
- Scenario refined based on feedback.
- Session duration estimated.
- All 5 participant sessions can proceed with confidence.

**CRITICAL: Cannot be simulated or fabricated**
- The pilot participant must be a real person.
- The session must happen on the real EMS.
- Notes must reflect what actually happened.

## Pilot sequencing:
1. **First:** Pilot 1 (Checklist) — establishes screen familiarity and basic workflow.
2. **Second:** Pilot 2 (Cross-Platform) — can run in parallel with Pilot 1 once BrowserStack is set up.
3. **Third:** Pilot 3 (User Testing) — requires the most preparation and a real person.

## Conditions for concluding methodology is stable:
- All 3 pilots completed successfully.
- Artifact formats validated on real data.
- Evidence capture workflow proven.
- Time estimates calculated for full-scale execution.
- No fundamental blockers remaining.
- Ready to scale and (where appropriate) extract skills.

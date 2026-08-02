# HW3 Implementation Plan: GUI & Usability Testing on EMS

**Owner:** Nguyễn Bảo Duy — 23127179 — Group 09 · **Scenario C** · Screens **C1–C4**
**Last updated:** 2026-08-02

## GLOBAL RULES
- **Manual GUI testing of an external SUT**: EMS is a live web app tested through its UI. **No source code is available, read, analysed or modified. There is no implementation work in this project.**
- **No fabricated evidence**: AI cannot and will not generate fake screenshots, user data, or test results.
- **Real screenshots from the real EMS**: `https://prod-dev.ems-fitus.cloud/`. Its data may reset — capture as you go.
- **The shared checklist is a frozen input**: Task 1A is complete (v1.9, 60 items). **Never regenerate or reword it**; §18 requires it identical across the group.
- **Real user testing participants**: The 5 participants for Task 2 must be real people outside the class.
- **Audit as you go**: Maintain the AI Audit Report incrementally as AI is used for various tasks.
- **One commit per step**: Adhere strictly to the git commit boundaries defined in this plan.
- **Findings Log must match Google Form**: Every entry in the Findings Log must have a corresponding Google Form submission.

---

## Step 0 — Resolve External Blockers · 🟡 **PARTLY DONE**
**Objective:** Get answers that only a human can provide.
**Input:** N/A (Start of project)
**Actions:**
- ✅ 0.1 Confirm group members and who takes which scenario — **Group 09, four members, scenarios A/B/C/D**
- ✅ 0.2 Decide which scenario THIS student takes — **Scenario C, Admin manages users**
- ⬜ 0.3 Access the EMS SUT — verify `https://prod-dev.ems-fitus.cloud/` loads and `admin@gmail.com` / `Admin@123` signs in. *(No personal student account needed: scenario C is admin-side only.)*
- ⬜ 0.4 Verify BrowserStack/LambdaTest trial access
- ⬜ 0.5 Identify and recruit pilot participant (1 person for the user-testing pilot, not one of the 5)
- ⬜ 0.6 Begin identifying 5 real participants for user testing
- ⬜ 0.7 Obtain the group's companion artefacts missing from this repo — reference sources + AI prompts, AI audit, live survey, the 14 screenshots (**B-11**)
- ✅ 0.8 Record all resolutions in `hw3/docs/blockers.md`
**Output artifacts:** `hw3/docs/blockers.md`
**Human review gate:** All blockers answered.
**Exit criteria:** SUT accessible, BrowserStack working, pilot participant identified, group artefacts obtained.
**Git commit boundary:** `Step 0: resolve external blockers`
**Dependencies:** None
**NOT YET:** Don't create any test artifacts.

## Step 1 — Explore the SUT and Select Screens · ✅ **DONE**
**Objective:** Familiarize with EMS and choose ≥3 screens for the selected scenario.
**Outcome:** **four** screens selected — **C1** Users list · **C2** Assign Role / Edit user · **C3** Block-Unblock & Reset-Password dialogs · **C4** Export to Excel. Four rather than three because the user-admin surface is small and three would push too much of a 60-item checklist into N/A.
**Remaining action:** on first live access, resolve **B-12** — whether Assign Role, Block/Unblock and Reset Password all live inside one Edit User dialog. If so, C2 and C3 are one screen (package becomes C1 · C2+C3 · C4 = three, still §5-compliant) and the execution report must say so instead of double-counting.
**Output artifacts:** `hw3/docs/screen-selection.md`
**Human review gate:** Screen selection approved — enough variety across IA-01..04?
**Git commit boundary:** `Step 1: select screens for scenario C`
**Dependencies:** Step 0

## Step 2 — Shared GUI Checklist (Group, Task 1A) · ✅ **DONE — FROZEN**
**Objective:** *(complete)* the > 40-item checklist covering all 4 IAs.
**Delivered:** `hw3/docs/gui-checklist/Shared_GUI_Checklist.md` — **v1.9, 60 items** (IA-01: 13 · IA-02: 15 · IA-03: 15 · IA-04: 17). All 10 Nielsen heuristics, 6 Norman principles, 8 Shneiderman rules and 6 WCAG 2.1 criteria cited; five review rounds documented in its changelog, including which items the AI missed and why (§6's explicit requirement).
**⚠ This step produces nothing further. Do not generate a checklist.** My Task 1 begins at Part B / Step 3.
**Companion group artefacts still to be obtained (not rebuilt):** reference-sources + AI-prompts log, group AI audit, live-survey record, the 14 source screenshots — **B-11**.
**Optional group-side follow-up:** v1.7–v1.9 sign-off; the pillar-4 "team experience" gap (4 of 60 items) targeted at v2.0 — 1–2 items per member from personal frustration using EMS. Does **not** block anything below.
**Git commit boundary:** `Step 2: shared GUI checklist (frozen, v1.9)` — commit the file unchanged before Step 3 so the freeze-before-execute order is provable.
**Dependencies:** —

## Step 3 — Pilot: Checklist Execution on C1
**Objective:** Validate the *execution* methodology on one real screen before scaling to the other three.
**Input:** Step 2 (checklist frozen) + Step 0.3 (SUT reachable)
**Actions:**
- 3.1 Use **C1 (Users list)** — the widest surface in scenario C
- 3.2 Execute **every** checklist item against C1 on the live EMS
- 3.3 Mark **Pass / Fail / N/A**; write Notes for every Fail **and** every N/A (one line naming the absent widget)
- 3.4 Capture screenshots for **Failed items only**, named per `execution-workflow.md` §3b
- 3.5 Write bug reports for discovered bugs
- 3.6 Submit 1 finding to the Google Form (proves the submission workflow)
- 3.7 Add 1 entry to the Findings Log with its form timestamp
- 3.8 Measure time per item; review whether the process scales to 3 more screens
**Output artifacts:**
- `hw3/out/reports/checklist-execution/C1.md`
- `hw3/out/reports/checklist-execution/evidence/` (failure screenshots)
- `hw3/out/reports/checklist-execution/bug-reports.md` (initial)
- `hw3/work/findings-log.md` (initial, 1 entry)
**Human review gate:** Is the execution format clear? Are bugs well-documented? Is every N/A justified? Is the pace sustainable?
**Exit criteria:** All 60 items executed on C1, ≥1 bug documented with evidence, Google Form submission confirmed, time estimate produced.
**Git commit boundary:** `Step 3: pilot checklist execution on C1`
**Dependencies:** Step 2
**NOT YET:** Don't scale to other screens yet. Don't extract skills yet. Don't edit the checklist.

## Step 4 — Pilot: Cross-Platform on 1 Screen
**Objective:** Validate the cross-platform testing workflow.
**Input:** Step 0 (BrowserStack available), Step 1 (screen selected)
**Actions:**
- 4.1 Open BrowserStack/LambdaTest
- 4.2 Test **C1** on 3 configurations (1 desktop, 1 tablet, 1 phone)
- 4.3 Capture screenshots with the `MSSV@....edu.vn` overlay, EMS URL and browser/OS/device identity in frame
- 4.4 Verify screenshots show browser/OS/device identity
- 4.5 Document any rendering issues
- 4.6 Measure time per configuration
**Output artifacts:**
- `hw3/out/reports/cross-platform/C1/` (screenshots)
- `hw3/work/scenario-c/compatibility/pilot-matrix.md`
**Human review gate:** Are screenshots capturing correctly? Is the process efficient?
**Exit criteria:** 3 screenshots with proper overlay, time estimate calculated.
**Git commit boundary:** `Step 4: pilot cross-platform on [screen-1]`
**Dependencies:** Step 0, Step 1 (can run in parallel with Step 3)
**NOT YET:** Don't build the full matrix. Don't try all browsers.

## Step 5 — Scale: Checklist Execution on C2, C3, C4
**Objective:** Execute the checklist on the remaining screens.
**Input:** Step 3 complete (methodology validated)
**Actions:**
- 5.1 For each of **C2, C3, C4**:
  - Execute all 60 checklist items
  - Mark Pass / Fail / N/A, with Notes for every Fail and every N/A
  - Capture screenshots for Failed items
  - Write bug reports
  - Add entries to Findings Log
- 5.2 Submit all findings to the Google Form
- 5.3 Review consistency across screens — an item that failed on C1 and passed on C2 needs an explanation, not a shrug
- 5.4 If **B-12** resolved C2 and C3 into one dialog, record the merge explicitly rather than filing two near-identical reports
**Output artifacts:**
- `hw3/out/reports/checklist-execution/C2.md`, `C3.md`, `C4.md`
- `hw3/out/reports/checklist-execution/evidence/` (per-screen failure screenshots)
- Updated `hw3/out/reports/checklist-execution/bug-reports.md`
- Updated `hw3/work/findings-log.md`
**Human review gate:** Are all screens covered? Are bugs properly documented? Is every N/A justified?
**Exit criteria:** All selected screens have complete execution results, all bugs documented.
**Git commit boundary:** `Step 5.N: checklist execution on C<N>` (one per screen)
**Dependencies:** Step 3

## Step 6 — Design User Testing Scenario (Task 2, Phase 1)
**Objective:** Create the goal-based task scenario and prepare for user testing.
**Input:** Step 1 (screens selected), familiarity from Steps 3+5
**Actions:**
- 6.0 **Decide and state the participant profile.** §6 asks for participants matching the target user profile, but scenario C's real user is admin/staff, not a student attendee. Choose: recruit people who plausibly do admin work, **or** recruit ordinary participants and frame it as first-use of an admin account measuring learnability. Either is defensible; the choice must be written into the Usability Report because it changes how the SUS score reads.
- 6.1 Write goal-based task scenario on C1–C4 (NOT step-by-step clicks) — e.g. *"a lecturer says they cannot sign in: find their account, work out why, and restore their access"*
- 6.2 Define metrics: task success, time on task, error/hesitation count, SUS/UEQ-S
- 6.3 Prepare SUS/UEQ-S form/template
- 6.4 Prepare probe questions (clarity, error recovery, speed, trust)
- 6.5 Prepare observation note template
**Output artifacts:**
- `hw3/work/user-testing/task-scenario.md`
- `hw3/work/user-testing/metrics-definition.md`
- `hw3/work/user-testing/sus-template.md` (or UEQ-S)
- `hw3/work/user-testing/probe-questions.md`
- `hw3/work/user-testing/observation-template.md`
**Human review gate:** Is the scenario clear and goal-oriented? Are metrics appropriate?
**Exit criteria:** Scenario written, all templates prepared, ready for pilot.
**Git commit boundary:** `Step 6: user testing scenario design`
**Dependencies:** Step 1 (can run in parallel with Steps 3-5)
**NOT YET:** Don't run sessions yet. Pilot first.

## Step 7 — Pilot: User Testing with 1 Person
**Objective:** Validate the testing scenario and session procedure. REQUIRED by §6.
**Input:** Step 6 complete, pilot participant available
**Actions:**
- 7.1 Run a moderated session with 1 pilot participant on real EMS
- 7.2 Observe friction, unclear instructions, broken flows
- 7.3 Have pilot participant complete SUS/UEQ-S
- 7.4 Note what worked and what didn't in the procedure
- 7.5 Refine the task scenario based on findings
**Output artifacts:**
- `hw3/work/user-testing/pilot-session-notes.md`
- Updated `hw3/work/user-testing/task-scenario.md` (v2, refined)
**Human review gate:** Is the scenario ready for the 5 real sessions?
**Exit criteria:** Pilot completed with real person, scenario refined, procedure validated.
**Git commit boundary:** `Step 7: user testing pilot session`
**Dependencies:** Step 6
**NOT YET:** Don't run the 5 real sessions yet.
**CRITICAL:** This MUST be a real person on the real EMS. Cannot be simulated.

## Step 8 — Run 5 User Testing Sessions (Task 2, Phase 2)
**Objective:** Conduct the 5 real moderated user testing sessions.
**Input:** Step 7 complete (scenario validated), 5 participants recruited
**Actions:**
- 8.1 For each participant (1-5):
  - Set the stage (testing the product, not them; think-aloud)
  - Observe neutrally, record screen if possible
  - Take structured notes on friction, errors, hesitations
  - Have participant complete SUS/UEQ-S
  - Ask probe questions
  - Record session details
**Output artifacts:**
- `hw3/work/user-testing/sessions/participant-N.md` (one per participant, with masked contact)
- `hw3/work/user-testing/sessions/sus-responses.md` (raw SUS/UEQ-S data)
- Screen recordings (if captured)
**Human review gate:** Each session must be a real person. Notes must reflect actual observations.
**Exit criteria:** 5 sessions completed, all have task success/time/errors/SUS scores.
**Git commit boundary:** `Step 8.N: user testing session [N]` (one per session)
**Dependencies:** Step 7
**NOT YET:** Don't analyse yet. Collect all data first.
**CRITICAL:** ALL 5 participants must be real people outside the class. TA may call 2.

## Step 9 — Analyse User Testing and Write Usability Report (Task 2, Phase 3)
**Objective:** Score metrics, analyse findings, produce Usability Report.
**Input:** Step 8 complete (all 5 sessions)
**Actions:**
- 9.1 Score SUS/UEQ-S across 5 participants
- 9.2 Calculate task metrics (success rate, mean time, mean errors)
- 9.3 Group similar pain points
- 9.4 Separate isolated bugs from systemic design issues
- 9.5 Rank findings by severity (0-4)
- 9.6 Write recommendations
- 9.7 Compile Usability Report
- 9.8 Add usability findings to Findings Log
- 9.9 Submit usability findings to Google Form
**Output artifacts:**
- `hw3/out/reports/usability-report.md`
- `hw3/work/user-testing/metrics-table.md`
- Updated `hw3/work/findings-log.md`
**Human review gate:** Are findings properly ranked? Are recommendations actionable?
**Exit criteria:** Usability Report complete with all required sections.
**Git commit boundary:** `Step 9: usability report`
**Dependencies:** Step 8

## Step 10 — Scale: Full Cross-Platform Matrix (Task 3)
**Objective:** Build and execute the full compatibility matrix for all screens.
**Input:** Step 4 (pilot validated), Steps 3+5 (all screens executed)
**Actions:**
- 10.1 Design the full matrix: 3 OS × 5 browsers × 3 device classes per screen
- 10.2 Select specific combinations ensuring coverage requirements
- 10.3 Execute each cell on BrowserStack/LambdaTest
- 10.4 Capture screenshots with MSSV overlay
- 10.5 Mark Pass/Fail per cell
- 10.6 Document rendering defects
- 10.7 Add compatibility defects to Findings Log
- 10.8 Submit compatibility findings to Google Form
**Output artifacts:**
- `hw3/out/reports/cross-platform/` (matrix + screenshots per screen)
- Updated `hw3/work/findings-log.md`
**Human review gate:** Does the matrix cover all required dimensions?
**Exit criteria:** Every OS ≥1, every browser ≥1, every device class ≥1 per screen; all screenshots captured.
**Git commit boundary:** `Step 10.N: cross-platform [screen-N]` (one per screen)
**Dependencies:** Step 4 + Steps 3/5 (all screens known)

## Step 11 — Extract Agent Skills (Task 5)
**Objective:** Extract reusable skills from validated methodologies.
**Input:** Steps 3-10 complete (manual methodology proven)
**Actions:**
- 11.1 Review which pipelines have stable enough methodology for skill extraction
- 11.2 Write methodology notes from what worked in practice
- 11.3 Author the skill(s) with the `generate-skill` skill (SUT-agnostic; the other skills already in `.claude/skills/` are HW2 domain/BVA artefacts and are **not** templates for this)
- 11.4 Validate each skill on a different screen than the pilot (C2 or C4)
- 11.5 Run the coupling smell-test from `skill-extraction-plan.md`
- 11.6 Record demo video showing end-to-end use on a complete screen or flow (§8)
**Output artifacts:**
- `.claude/skills/[skill-name]/SKILL.md` (one per skill)
- Demo video (YouTube link)
**Human review gate:** Does the skill reproduce equivalent results? Does it pass the coupling test?
**Exit criteria:** ≥1 skill validated, smell-test passes, demo recorded.
**Git commit boundary:** `Step 11: extract [skill-name] skill`
**Dependencies:** Steps 3-10 (enough manual artifacts to extract from)

## Step 12 — Consolidate Findings Log (Task 4)
**Objective:** Finalize the aggregated Findings Log and ensure Google Form consistency.
**Input:** All testing complete (Steps 5, 9, 10)
**Actions:**
- 12.1 Compile all bugs, usability findings, and compatibility defects into one file
- 12.2 Assign consistent IDs
- 12.3 Verify every entry has a matching Google Form submission
- 12.4 Cross-check counts
**Output artifacts:**
- `hw3/out/findings-log.md` (final, canonical)
**Human review gate:** Do form submissions match the log? Are counts consistent?
**Exit criteria:** Log and Form are consistent, all findings accounted for.
**Git commit boundary:** `Step 12: finalize findings log`
**Dependencies:** Steps 5, 9, 10

## Step 13 — AI Audit, AI Critique, and Final Report
**Objective:** Complete all remaining deliverables.
**Input:** All prior steps
**Actions:**
- 13.1 Finalize AI Audit Report — promote `hw3/work/ai-audit.md` → `hw3/out/ai-audit.md`. Uses the faculty form `[AI-02] - FIT@HCMUS - AI Audit Report_En.docx.md` (6 sections). It must have been appended to throughout; §12 verifies that it was not reconstructed at the end.
- 13.2 Write AI Critique (**200–300 words**, §11) — promote `hw3/work/ai-critique.md` → `hw3/out/ai-critique.md`. Three paragraphs: one concrete AI mistake + how it was noticed · the workflow change · the transferable principle. The mistake must match an `INVALID`/`INCOMPLETE` row in the audit table. Note the HW2 critique runs ~340 words — over the HW3 limit.
- 13.3 Compile main report (Markdown + PDF)
- 13.4 Write README.md with self-assessment table and test summary
- 13.5 Generate git commit log: `git log --oneline > hw3/out/git_commit_log.txt`
- 13.6 Assemble submission .zip
**Output artifacts:**
- `hw3/out/ai-audit.md`
- `hw3/out/ai-critique.md`
- `hw3/out/main-report.md` (+ PDF)
- `hw3/out/README.md`
- `hw3/out/git_commit_log.txt`
**Human review gate:** Self-assessment accurate? All required files present?
**Exit criteria:** All files present per §15, zip named correctly.
**Git commit boundary:** `Step 13: final deliverables`
**Dependencies:** All prior steps

---

## STATUS

| Step | Objective | Status |
| :--- | :--- | :--- |
| 0 | Resolve External Blockers | 🟡 Partly done — scenario/screens/group settled; SUT access, BrowserStack, participants, group artefacts open |
| 1 | Explore the SUT and Select Screens | ✅ Done — Scenario C, screens C1–C4 (verify B-12 on first live access) |
| 2 | Shared GUI Checklist (Task 1A) | ✅ **Done — v1.9, 60 items, frozen. Do not regenerate.** |
| 3 | Pilot: Checklist Execution on C1 | [ ] Pending |
| 4 | Pilot: Cross-Platform on C1 | [ ] Pending |
| 5 | Scale: Checklist Execution on C2, C3, C4 | [ ] Pending |
| 6 | Design User Testing Scenario | [ ] Pending |
| 7 | Pilot: User Testing with 1 Person | [ ] Pending |
| 8 | Run 5 User Testing Sessions | [ ] Pending |
| 9 | Analyse User Testing and Write Usability Report | [ ] Pending |
| 10 | Scale: Full Cross-Platform Matrix | [ ] Pending |
| 11 | Extract Agent Skills | [ ] Pending |
| 12 | Consolidate Findings Log | [ ] Pending |
| 13 | AI Audit, AI Critique, and Final Report | [ ] Pending |

---

## NEXT ACTION
**Close the remaining Step 0 blockers, in this order:**
1. **0.3** — sign in to `https://prod-dev.ems-fitus.cloud/` with `admin@gmail.com` / `Admin@123`, and while there resolve **B-12** (are Assign Role / Block / Reset Password all inside one Edit User dialog?).
2. **0.7** — get the group's companion artefacts (**B-11**) into this repo; §15 requires them and they cannot be rebuilt honestly.
3. **0.4** — BrowserStack/LambdaTest trial.
4. **0.5 / 0.6** — pilot participant, then the 5 real participants (longest lead time — start now even though Step 8 is far off).

Then commit the frozen checklist (Step 2 boundary) and begin **Step 3 — execution on C1**.

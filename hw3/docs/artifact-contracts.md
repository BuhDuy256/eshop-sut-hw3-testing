# Artifact Contracts (HW3: GUI & Usability Testing)

This document defines the exact schema, lifecycle, and strict traceability rules for every artifact produced during HW3 (EMS GUI & Usability Testing). It serves as the authoritative guide for both AI and human collaborators to ensure consistent, compliant, and structurally sound deliverables.

**Reference:**
- SUT: EMS (Event Management System) — external live web app, `https://prod-dev.ems-fitus.cloud/`. **Black-box: tested through the UI only; no source code is read or modified.**
- Scenario: **C — Admin manages users** · Screens **C1** Users list · **C2** Assign Role / Edit user · **C3** Block-Unblock & Reset-Password dialogs · **C4** Export to Excel.
- Required Bloom-AI Level: G9.3 (Analyse), G9.4 (Collaborate)
- Core philosophy: AI-First but disciplined, Human-in-the-loop at decision gates, Freeze before execute, Example-first development, real evidence.

**Path root.** All paths below are relative to the repository root; deliverables live under `hw3/out/`, working material under `hw3/work/`, planning under `hw3/docs/`.

---

## 1. Artifact Definitions

### 1.1 Task 1: GUI Checklist Design & Execution

#### 1. Shared GUI Checklist (Group) — ✅ **DELIVERED · FROZEN INPUT**
* **Purpose:** A comprehensive, group-shared checklist based on recognized UI heuristics covering 4 interface aspects (IA-01 to IA-04).
* **Source of truth:** `hw3/docs/gui-checklist/Shared_GUI_Checklist.md` — **v1.9, 60 items** (§6 requires > 40).
* **Actual row schema (as built):** `Item ID · Aspect · Reference Source · Verification Rule · Expected Behavior`. Provenance (AI-drafted vs team-added, and *why the AI missed it*) is carried in the file's own §"Items added beyond the AI output" and §"Coverage summary" tables, not as per-row columns.
* **Produced by:** Group 09 + AI, across five documented review rounds (see its changelog).
* **Consumed by:** Per-Screen Checklist Execution (individual).
* **No-duplicate rule:** One checklist for the entire group; §18 requires it identical across members.
* **Lifecycle state: `frozen`.** **This artefact is not to be produced, regenerated or reworded by any individual.** A suspected defect in an item is raised with the group; it never becomes a personal edit.
* **Outstanding group-side only (does not block execution):** v1.7–v1.9 sign-off; the pillar-4 "team experience" gap (4/60) targeted at v2.0.

#### 2. Checklist Reference Sources + AI Prompts Log (Group) — ⚠ **MISSING FROM THIS REPO**
* **Purpose:** Documents the foundations of the checklist and the AI interactions that produced it. §6 Task 1A and §15 require **both** as group artefacts.
* **Source of truth:** the group's `Reference_Sources_and_Prompts.md` — cited repeatedly by the checklist but **not present in this repository**. Also absent: `AI_Audit_Report.md`, `EMS_Live_Survey_2026-07-26.md`, and the 14 source screenshots in `screenshots/`.
* **Action:** obtain the group's copies (blocker **B-11**). **Do not reconstruct them** — a rebuilt prompt log or survey record fabricates provenance for work already done, which §12 treats as the thing being verified.
* **Consumed by:** AI Audit Report; the §15 submission bundle.

#### 3. *(merged into #2 — the group keeps sources and prompts in one file)*

#### 4. Per-Screen Checklist Execution
* **Purpose:** Applies the frozen Shared GUI Checklist to my screens (C1–C4).
* **Source of truth:** `hw3/out/reports/checklist-execution/<SCREEN>.md`, one file per screen.
* **Required fields:** Checklist Item ID, Screen ID, **Verdict (Pass / Fail / N/A)**, Notes, Screenshot Ref.
* **Verdict rules:**
  * **Fail** → Notes state the reason; Screenshot Ref is **mandatory**.
  * **N/A** → Notes state, in one line, which widget is absent from this screen. **Mandatory.**
  * **N/A is never counted as a pass.** Report *designed (60) / applicable / executed / passed / failed*.
* **Produced by:** Individual member (Execution phase), by hand against the live UI.
* **Consumed by:** GUI Bug Report.
* **No-duplicate rule:** One execution record per screen; no overlap with other members' screens (§5, §18).
* **Evidence linkage:** References the Shared GUI Checklist by item ID. Screenshots for failures only.
* **Lifecycle states:** executed → reviewed

#### 5. GUI Bug Report
* **Purpose:** Formal documentation of defects found during checklist execution.
* **Source of truth:** `hw3/out/reports/checklist-execution/bug-reports.md`.
* **Required fields:** Bug ID, Screen, Steps to Reproduce, Expected, Actual, Severity, Screenshot Ref, Findings-Log-ID.
* **Produced by:** Individual member (Reporting phase).
* **Consumed by:** Bug & Usability Findings Log, Google Form.
* **No-duplicate rule:** Must be reported BOTH in the report AND via the Google Form.
* **Evidence linkage:** Screenshot showing the defect on the real EMS interface.
* **Lifecycle states:** discovered → documented → submitted-to-form

---

### 1.2 Task 2: User Testing & Usability Report

#### 6. User-Testing Task Scenario
* **Purpose:** Goal-oriented task description for user testing participants (not step-by-step clicks).
* **Source of truth:** Usability Report section.
* **Required fields:** Scenario ID, Goal Description, Target Screens, Target User Profile, Metrics Defined.
* **Produced by:** Individual member (Design phase).
* **Consumed by:** Participant testing sessions.
* **Lifecycle states:** drafted → piloted → refined → frozen

#### 7. Pilot Session Notes
* **Purpose:** Validate scenario clarity and flow before real testing.
* **Source of truth:** Pilot run documentation.
* **Required fields:** Participant (pilot), Issues Found, Refinements Made.
* **Produced by:** Individual member (after 1 pilot run).
* **Consumed by:** User-Testing Task Scenario (refinement).

#### 8. Participant Session Record
* **Purpose:** Raw, structured observation notes for each real testing session.
* **Source of truth:** Individual session records directory (5 total).
* **Required fields:** Participant ID, Name (for verification), Contact (masked - middle 4 digits), Session Date/Time, Task Success (completed/partial/failed), Time on Task, Error Count, Hesitation Count, Think-Aloud Notes, Friction Points, Screen Recording Ref.
* **Produced by:** Individual member (during live sessions).
* **Consumed by:** Usability Metrics Table, Usability Finding.
* **No-duplicate rule:** Must be real, verifiable data (TA verification applies).

#### 9. SUS/UEQ-S Raw Responses
* **Purpose:** Post-task standardized questionnaire results.
* **Source of truth:** Individual raw response logs (5 total).
* **Required fields:** Participant ID, Question responses (SUS: 10 items, scale 1-5), Probe Question Responses.
* **Produced by:** Individual member (post-session collection).
* **Consumed by:** Usability Metrics Table.

#### 10. Usability Metrics Table
* **Purpose:** Aggregated quantitative data from all 5 sessions.
* **Source of truth:** Usability Report section.
* **Required fields:** Metric Name, Per-Participant Values, Mean, Notes.
* **Produced by:** Individual member (Analysis phase).
* **Consumed by:** Usability Report.

#### 11. Usability Finding
* **Purpose:** Analyzed usability issues derived from session records.
* **Source of truth:** Usability findings section/log.
* **Required fields:** Finding ID, Category (isolated-bug vs systemic-design-issue), Severity (0-4), Description, Affected Screens, Evidence (participant sessions that surfaced it), Screenshot Ref, Recommendation.
* **Produced by:** Individual member (Analysis phase).
* **Consumed by:** Usability Report, Bug & Usability Findings Log.
* **Lifecycle states:** identified → grouped → severity-ranked

#### 12. Usability Report
* **Purpose:** The final deliverable for Task 2, synthesizing findings and metrics.
* **Source of truth:** `hw3/out/reports/usability-report.md`
* **Required fields:** Scenario, Participant Table, Metrics Table, Ranked Findings, Recommendations.
* **Produced by:** Individual member (Reporting phase).
* **Consumed by:** Final grading submission.
* **Lifecycle states:** drafted → reviewed → finalized

---

### 1.3 Task 3: Cross-Browser / Cross-Platform

#### 13. Compatibility Matrix
* **Purpose:** Planning grid for cross-platform coverage across ≥3 screens.
* **Source of truth:** Cross-platform report section.
* **Required fields:** Grid (rows = OS×Device, columns = Browser), Pass/Fail per cell, Screenshot Ref per cell. Coverage check (every OS ≥1, every browser ≥1, every device class ≥1 per screen).
* **Produced by:** Individual member (Planning/Execution phase).
* **Consumed by:** Execution tracking.

#### 14. Compatibility Execution Result
* **Purpose:** Detailed result of testing a specific OS/Browser/Device combination.
* **Source of truth:** Matrix cell entries.
* **Required fields:** Screen ID, OS, Browser, Device Class, Tool Used (BrowserStack/LambdaTest/physical), Pass/Fail, Screenshot Path, Defect Note (if Fail).
* **Produced by:** Individual member (Execution phase).
* **Consumed by:** Compatibility Defect.
* **Evidence linkage:** Screenshots MUST have MSSV email overlay showing the EMS URL.

#### 15. Compatibility Defect
* **Purpose:** Documentation of rendering/layout issues found.
* **Source of truth:** Cross-platform defect list.
* **Required fields:** Defect ID, Screen, OS, Browser, Device, Description (overflow/overlap/broken layout/etc.), Screenshot Ref, Findings-Log-ID.
* **Produced by:** Individual member (Reporting phase).
* **Consumed by:** Bug & Usability Findings Log, Google Form.

---

### 1.4 Global Management & Audit

#### 16. Bug & Usability Findings Log
* **Purpose:** THE aggregated source of truth for all findings across Tasks 1-3.
* **Source of truth:** `hw3/out/findings-log.md` (built incrementally at `hw3/work/findings-log.md`, promoted at Step 12).
* **Required fields:** ID, Scenario/Screen, Type (Bug|Usability), Description, Steps/Heuristic, Severity, Suggested Fix, Screenshot Ref, Form-Submission Timestamp.
* **Produced by:** Individual member (Final aggregation phase).
* **Consumed by:** Final grading submission, Google Form.
* **No-duplicate rule:** Single file, no duplicates. Must match Google Form submissions exactly.

#### 17. AI Audit Entry
* **Purpose:** Logs every AI interaction for accountability.
* **Source of truth:** `hw3/out/ai-audit.md` — append-only. Working copy: `hw3/work/ai-audit.md`.
* **Template — mandatory:** the faculty form `[AI-02] - FIT@HCMUS - AI Audit Report_En.docx.md` (6 sections: Student Information · Instructions · Audit Table · Summary of AI Accuracy · Conclusion · Mandatory Disclosure + Signature). §10 says to use the given AI Templates; the form is course-wide, not HW2-specific.
* **Required fields (Section 3, one row per artifact):** (1) Prompt + Tool + timestamp, (2) AI Output verbatim, (3) Verdict `VALID | INVALID | INCOMPLETE`, (4) Reasoning citing an authority, (5) Student Fix.
* **HW3-specific:** column (4) cites the assignment §, slide S13 page, Nielsen/Norman/Shneiderman principle, or WCAG SC — **not** EMS source code, which does not exist here. Section 4 is additionally broken down per task (1/2/3/Skills), since the three tasks differ in kind and one aggregate hides where AI was weak.
* **Produced by:** Individual member/Agent (during work).
* **No-duplicate rule:** Appended at creation time, never reconstructed retroactively.

#### 18. AI Critique
* **Purpose:** Reflective analysis on AI performance and collaboration principles.
* **Source of truth:** `hw3/out/ai-critique.md`. Working copy with structure + candidate material: `hw3/work/ai-critique.md`.
* **Required fields:** **200–300 words** (§11) covering where AI was wrong/biased/incomplete, why it failed, principles learned.
* **Shape:** three paragraphs, following the HW2 critique that scored well — (1) one concrete AI mistake *and how it was noticed*, (2) the workflow change that followed, (3) the transferable principle. One mistake told deeply beats five listed shallowly.
* **Consistency rule:** the mistake described here must correspond to a row marked `INVALID` or `INCOMPLETE` in AI Audit Report §3. Two documents that agree are both more credible.
* **Watch the limit:** the HW2 critique runs ~340 words; HW3 caps at 300.
* **Produced by:** Individual member (End of project) — but the raw observation is recorded *when it happens*, not reconstructed at the end.

#### 19. Git Commit Log
* **Purpose:** Proof of iterative work process.
* **Source of truth:** `hw3/out/git_commit_log.txt`
* **Required fields:** One commit per major step (checklist design, per-screen execution, bug logging, evaluation, cross-platform).
* **Produced by:** Individual member (Continuous).

#### 20. Skill Input/Output (Agent Skills)
* **Purpose:** Defines the capability-based skills developed for reuse.
* **Source of truth:** `.claude/skills/<skill-name>/SKILL.md`
* **Required fields:** Defined inputs, expected outputs, judgment points requiring human decision.
* **Lifecycle states:** Skills are NOT created until a manual pilot validates the methodology.
* **Note:** the skills already present in `.claude/skills/` (`bug-reporting`, `domain-test-design`, `generate-skill`) are **HW2 artefacts**. `generate-skill` is a reusable generator and may be used; the other two are domain/BVA-specific and are **not** HW3 deliverables and not templates for GUI work.
* **§8 also requires:** a demonstration video (YouTube link) per skill, showing end-to-end use on a complete screen or flow.

---

## 2. Traceability Chain

To ensure rigorous linkage between design, execution, and reporting, all artifacts must maintain strict references:

1. **Task 1 Traceability:**
   Checklist Item → Per-Screen Execution → GUI Bug Report → Findings Log → Google Form

2. **Task 2 Traceability:**
   User Testing Scenario → Session Records → Metrics → Usability Findings → Usability Report → Findings Log → Google Form

3. **Task 3 Traceability:**
   Compatibility Matrix → Execution Results → Compatibility Defects → Findings Log → Google Form

---

## 3. Strict No-Fabrication Rules

The core tenet of HW3 is executing against a live environment with real constraints. **Fabrication is strictly prohibited and structurally prevented:**

* **Screenshots:** Must be captures of the REAL, live EMS SUT interface (no generated mockups).
* **User Testing:** Participants MUST be real people (outside the class). Contacts are recorded (masked) and subject to TA verification. Impersonation voids Task 2.
* **Cross-Platform Evidence:** Screenshots MUST show a real browser/OS/device context alongside the EMS URL, WITH the student's email overlay (MSSV@....edu.vn).
* **Recordings:** Session recordings and evidence captures must reflect real execution.
* **State transience (§4):** the EMS instance is tunnelled and its data may be reset periodically. Capture evidence as you go; never assume a state you created earlier still exists next session. Counts recorded during the group's survey have already drifted once — read live numbers, never quoted ones.
* **Black-box boundary:** no finding may be justified by application source code, because none is available. Every expected result traces to the checklist item's stated Expected Behavior, a cited heuristic (Nielsen / Norman / Shneiderman / WCAG / course slides), or an observed cross-screen inconsistency — never to an inspection of how EMS is implemented.
* **Frozen input, not output:** the shared checklist is consumed, never authored, by this individual work.

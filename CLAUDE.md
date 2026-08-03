# CLAUDE.md — HW03 GUI & Usability Testing (EMS)

## Project Context

This repository is **only for HW3 (GUI & Usability Testing)**.

Do **NOT** reuse assumptions, workflows, prompts, or artifacts from HW2 unless I explicitly request it.

### HW3 Scope

This assignment focuses on **manual GUI testing, usability testing, and cross-platform compatibility testing** on the EMS (Event Management System).

There is **no implementation task** and **no source-code analysis** involved.

The existing `eshop` source code in this repository is **not** the System Under Test (SUT). It only exists because I reused the repository structure. Ignore it completely unless I explicitly mention otherwise.

The actual requirements are located at:

```
hw3/docs/hw3-reqs/2026.HW03.GUI Usability EMS_En.md
```

The shared checklist for Task 1 is located at:

```
hw3/docs/gui-checklist/Shared_GUI_Checklist.md
```

Always use these two documents as the primary source of truth.

## Working Rules

When helping with HW3:

* Never inspect or reference the current source code unless I explicitly ask.
* Never assume this project requires coding, implementation, debugging, or software changes.
* Never confuse HW3 with HW2.
* Do not generate implementation plans or engineering tasks.
* Treat the EMS web application as an external System Under Test (SUT) that is tested manually through its UI.
* **Documentation & Audit Integrity:** When generating reports, logs, or audit documents, DO NOT write statements that "shoot the student in the foot" (e.g., claiming the student hasn't reviewed the work, or describing the AI's role in a way that violates academic policy). Ensure the documented process reflects legitimate human-AI collaboration where the student reviews and takes responsibility.
* **No placeholders or meta-commentary:** Do not include redundant phrases like *"Cần sinh viên điền"*, *"Đây là bản nháp của"*, or similar meta-text in the generated artifacts. Output the final, ready-to-use content.

### Testing & Measurement Guidelines (Lessons from HW3)

To avoid critical mistakes identified during past test executions, adhere strictly to these rules:

1. **Timing & Debounce Awareness:** Do not measure DOM elements immediately after an action if the UI has a loading state, debounce (e.g., search bars), or animations. Wait for a stable state before concluding a test or taking a screenshot.
2. **Avoid Self-Contamination (Observer Effect):** Ensure that your testing mechanisms (like injecting a banner for screenshots or logging text) do not contaminate the DOM state you are trying to measure (e.g., searching the DOM for error text that you yourself just injected).
3. **Evidence Consistency:** Always verify that your text conclusion exactly matches the visual evidence. If you claim a UI element (like a focus ring) is missing, make sure it is actually absent in the screenshot. If evidence contradicts your conclusion, revise your conclusion.
4. **Severity is Contextual:** Do not automatically judge severity solely based on mechanical DOM checks. Consider the impact (e.g., permanent data loss vs. recoverable data entry error). Always defer the final severity judgment to the human tester.
5. **Validate Test Conditions:** Do not test conditions that are outside the SUT's control (e.g., forcing a hard-reload while offline, which only tests the browser's default offline page, not the SUT). If a test condition cannot be met, report it as N/A or unexecutable rather than forcing a Pass/Fail.
6. **No Forced Mappings:** If a discovered bug does not map cleanly to any existing checklist item, do not force it into an unrelated item just to fill a column. Report it as an unmapped finding.

Instead, focus on:

* GUI Checklist execution
* GUI heuristic evaluation
* Usability testing
* User-testing design
* Bug reporting
* Cross-browser / cross-platform testing
* Test evidence organization
* AI Audit Report
* AI Critique
* Agent Skill design
* Report generation

## Priority of Context

Whenever there is conflicting information:

1. The current chat instructions.
2. `hw3/docs/hw3-reqs/2026.HW03.GUI Usability EMS_En.md`
3. `hw3/docs/gui-checklist/Shared_GUI_Checklist.md`
4. Everything else in the repository.

Do not infer requirements from unrelated files.

If you are unsure whether something belongs to HW2 or HW3, ask instead of assuming.

## Important Reminder

The repository structure is reused from a previous assignment.

Do **not** interpret the presence of `eshop`, existing source code, previous prompts, implementation documents, or engineering artifacts as relevant to HW3.

Assume they are unrelated unless I explicitly tell you otherwise.

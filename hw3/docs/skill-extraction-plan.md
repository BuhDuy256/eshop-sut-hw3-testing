# Skill Extraction Plan for HW3

**IMPORTANT NOTE:** None of these candidate skills should be created until the manual pilots are complete and their methodology is proven stable. §8 asks for skills that *"apply the GUI-checklist execution, the heuristic usability evaluation, and the compatibility-matrix runs, so they can be reused on additional EMS screens and flows"* — reusability is the point, so a skill that only works on scenario C is not a deliverable.

**Not a candidate: a checklist-*design* skill.** Task 1A is complete; the 60-item checklist exists and is frozen. A skill that generates checklist items would duplicate finished work and, under §18, must not be used to produce a second variant.

**Existing `.claude/skills/` contents are HW2 artefacts.** `bug-reporting` and `domain-test-design` are domain/BVA skills for a different SUT — not HW3 deliverables, not templates for GUI work. `generate-skill` is SUT-agnostic and may be used to author the skills below.

**Every skill submitted needs a demonstration video** (YouTube link) showing end-to-end use on a complete screen or flow (§8, §15).

## Candidate Skills

### Skill 1: `gui-checklist-execution`
- **Capability:** Systematically execute a GUI checklist against a given screen, producing Pass / Fail / **N/A** verdicts with evidence.
- **Input:** A frozen GUI checklist + a screen identifier + observations/screenshot of the screen.
- **Output:** Execution table (item × verdict × notes × screenshot ref) + the list of failed items needing bug reports.
- **Verdict discipline the skill must enforce:** every **Fail** carries a reason and a screenshot ref; every **N/A** carries a one-line reason naming the absent widget; **N/A is never counted as a pass** in any summary the skill produces.
- **Judgment points (human required):**
  - Whether a subjective heuristic item passes or fails on a specific screen.
  - Whether a visual issue is a real defect or acceptable design.
  - Whether an item is genuinely N/A or merely hard to check.
  - Whether the evidence screenshot correctly captures the failure.
- **Reference artifact for extraction:** Pilot 1 execution results (C1).
- **Validation:** Run the skill on a DIFFERENT screen than the pilot (C2 or C4); compare human vs skill verdicts.
- **Coupling smell-test:** see the unified grep list below.
- **What CANNOT be a skill:** the actual screenshot capture and the live navigation (require real browser interaction), and the final verdict on a subjective item.

### Skill 2: `gui-bug-reporting`
- **Capability:** Take a failed checklist item + evidence and produce a structured bug report.
- **Input:** Failed checklist item + screenshot + screen context.
- **Output:** Bug report (ID, screen, steps, expected/actual, severity, screenshot ref).
- **Judgment points:** Severity classification, whether steps are reproducible, whether expected behavior is correctly stated.
- **Reference artifact:** Pilot 1 bug reports.
- **Coupling smell-test:** Grep for project-specific terms (see unified list below).

### Skill 3: `usability-analysis`
- **Capability:** Analyse raw user testing data (session notes, SUS scores, metrics) into ranked usability findings.
- **Input:** 5 session records + SUS/UEQ-S raw data + metrics table.
- **Output:** Ranked usability findings + recommendations + Usability Report structure.
- **Judgment points:**
  - Grouping: which pain points are the same underlying issue vs separate issues.
  - Severity rating (0-4).
  - Whether a finding is an isolated bug vs systemic design issue.
  - Recommendation quality.
- **Reference artifact:** Pilot 3 analysis (after all 5 sessions are complete).
- **CRITICAL LIMITATION:** This skill can only analyse REAL data. Session notes, participant responses, and metrics must be real. The skill analyses; it does not generate data.
- **Coupling smell-test:** Grep for project-specific terms.

### Skill 4: `compatibility-matrix-analysis`
- **Capability:** Analyse cross-platform screenshots and produce compatibility defect reports.
- **Input:** Matrix of screenshots + expected rendering baseline.
- **Output:** Pass/Fail per cell + defect reports for failures.
- **Judgment points:**
  - Whether a rendering difference is a defect or acceptable variation.
  - Severity of layout issues.
- **Reference artifact:** Pilot 2 mini-matrix.
- **CRITICAL LIMITATION:** Screenshots must be pre-captured by human using BrowserStack. Skill only analyses, never captures.
- **Coupling smell-test:** Grep for project-specific terms.

### Skill 5: `findings-log-compiler`
- **Capability:** Compile all bugs and usability findings from all pipelines into the consolidated Findings Log.
- **Input:** GUI bug reports + usability findings + compatibility defects.
- **Output:** Bug & Usability Findings Log (with all required columns).
- **Judgment points:** Deduplication, consistent severity across sources.
- **Reference artifact:** Manual findings log from pilot.
- **Coupling smell-test:** Grep for project-specific terms.

## Skills NOT to create:
- Screenshot capture (requires real browser interaction).
- User testing session facilitation (requires real human interaction).
- BrowserStack/LambdaTest operation (requires real tool interaction).
- Google Form submission (requires real form interaction).
- Participant recruitment (requires real people).

## Extraction timeline:
- **After Pilot 1:** Extract `gui-checklist-execution` + `gui-bug-reporting` candidates.
- **After Pilot 2:** Extract `compatibility-matrix-analysis` candidate.
- **After all 5 user sessions:** Extract `usability-analysis` candidate.
- **After first full findings compile:** Extract `findings-log-compiler` candidate.

## Coupling Smell-Test Grep List
For EACH skill extracted, run a check to ensure it is decoupled from this project's specific data. Grep the extracted skill for:
- `EMS` / `ems` / `ems-fitus` / `prod-dev`
- `Event Management`
- `admin@gmail.com` / `Admin@123`
- `ngrok`
- Scenario letters `A/B/C/D` and screen IDs `C1`…`C4`
- Specific screen names (Users list, Events list, Support requests, etc.)
- Specific item IDs (`IA01-`, `IA02-`, `IA03-`, `IA04-`)
- `23127179`, `Group 09`, member names
- Specific participant names or contacts

A hit is not automatically a failure — it is a prompt to ask whether the skill would still work on a different system. Names inside an *example* are fine; names inside a *rule* are the coupling to remove.

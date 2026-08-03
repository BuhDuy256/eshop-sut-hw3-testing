# Compatibility Matrix — Task 3 (Final)

**Status:** FROZEN. Source: `hw3/work/task-3-cross-platform/compatibility-manifest-working.md`
(reviewed working manifest), execution logs (`run-log-A/B/C/G/F.md`), and
blocker evidence. Generated and cross-checked with `compat-run-planner`
(see `hw3/out/agent-skills/compat-run-planner/SKILL.md` and
`hw3/work/task-3-cross-platform/skill-validation.md`).

**Scenario:** C — Admin manages users. **Screens:** C1 Users list · C2 Edit
User dialog · C3 Delete User confirm dialog · C4 Export to Excel.

---

## Totals

```text
Manifest rows: 28
Executed cells: 20 (19 Pass, 1 Fail)
Blocked cells: 8 (Not Executed, no verdict)
Supplementary validation: 1 (C3 Full Confirm Final Validation, Run A —
  field upgrade on an existing Executed row, not a new cell)
```

---

## Executed rows (20) — verdict, evidence, execution mode

| Screen | Run | OS | Browser | Device | Verdict | Actual Execution Mode | Interaction Coverage (C3 only) | Evidence |
|---|---|---|---|---|---|---|---|---|
| C1 | A | Windows | Chrome | Desktop | Pass (render + behavior verified) | AI-executed with human checkpoints | — | `evidence/C1/T3_C1_RunA_Windows_Chrome_Desktop.png` + `_supp1.png` |
| C1 | B | Windows | Firefox | Desktop | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C1/T3_C1_RunB_Windows_Firefox_Desktop.png` |
| C1 | C | Windows | Opera | Desktop | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C1/T3_C1_RunC_Windows_Opera_Desktop.png` |
| C1 | G | Windows | Edge | Desktop | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C1/T3_C1_RunG_Windows_Edge_Desktop.png` |
| C1 | F | iOS | Safari | Phone | **Fail** — Finding F-022, severity 2 | Human-executed with AI guidance | — | `evidence/C1/T3_C1_RunF_iOS_Safari_Phone.png` + `_supp1.png` + `_supp2.png` |
| C2 | A | Windows | Chrome | Desktop | Pass (render + behavior verified) | AI-executed with human checkpoints | — | `evidence/C2/T3_C2_RunA_Windows_Chrome_Desktop.png` + `_supp1.png` |
| C2 | B | Windows | Firefox | Desktop | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C2/T3_C2_RunB_Windows_Firefox_Desktop.png` |
| C2 | C | Windows | Opera | Desktop | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C2/T3_C2_RunC_Windows_Opera_Desktop.png` |
| C2 | G | Windows | Edge | Desktop | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C2/T3_C2_RunG_Windows_Edge_Desktop.png` |
| C2 | F | iOS | Safari | Phone | Pass (render + behavior verified) | Human-executed with AI guidance | — | `evidence/C2/T3_C2_RunF_iOS_Safari_Phone.png` |
| C3 | A | Windows | Chrome | Desktop | Pass | AI-executed with human checkpoints | **Full confirm flow** (upgraded 2026-08-03, see Supplementary Validation below) | `evidence/C3/T3_C3_RunA_Windows_Chrome_Desktop.png` + `_supp1.png` |
| C3 | B | Windows | Firefox | Desktop | Pass | Human-executed with AI guidance | Dialog-only | `evidence/C3/T3_C3_RunB_Windows_Firefox_Desktop.png` |
| C3 | C | Windows | Opera | Desktop | Pass | Human-executed with AI guidance | Dialog-only | `evidence/C3/T3_C3_RunC_Windows_Opera_Desktop.png` |
| C3 | G | Windows | Edge | Desktop | Pass | Human-executed with AI guidance | Dialog-only | `evidence/C3/T3_C3_RunG_Windows_Edge_Desktop.png` |
| C3 | F | iOS | Safari | Phone | Pass | Human-executed with AI guidance | Dialog-only | `evidence/C3/T3_C3_RunF_iOS_Safari_Phone.png` |
| C4 | A | Windows | Chrome | Desktop | Pass (filesystem-verified download) | AI-executed with human checkpoints | — | `evidence/C4/T3_C4_RunA_Windows_Chrome_Desktop.png` |
| C4 | B | Windows | Firefox | Desktop | Pass (filesystem-verified download) | Human-executed with AI guidance | — | `evidence/C4/T3_C4_RunB_Windows_Firefox_Desktop.png` |
| C4 | C | Windows | Opera | Desktop | Pass (filesystem-verified download) | Human-executed with AI guidance | — | `evidence/C4/T3_C4_RunC_Windows_Opera_Desktop.png` |
| C4 | G | Windows | Edge | Desktop | Pass (filesystem-verified download) | Human-executed with AI guidance | — | `evidence/C4/T3_C4_RunG_Windows_Edge_Desktop.png` |
| C4 | F | iOS | Safari | Phone | Pass (Safari Downloads panel confirmed; URL-visibility exception disclosed — see report §10) | Human-executed with AI guidance | — | `evidence/C4/T3_C4_RunF_iOS_Safari_Phone.png` |

**Pass / Fail summary:** 19 Pass, 1 Fail (C1 / Run F / iOS / Safari / Phone —
Finding F-022, severity 2: sidebar not responsive on phone viewport,
content overflows even after collapsing the sidebar).

---

## Supplementary Validation (not a coverage cell)

| Step | Environment | Action | Result |
|---|---|---|---|
| C3 Full Confirm Final Validation | Chrome / Windows (Run A) | Interaction Coverage on the existing C3/Run A row upgraded from `Dialog-only` to `Full confirm flow` after all 5 Executed runs had completed C3 at Dialog-only scope | Completed 2026-08-03 — disposable test user `test abc` was actually deleted with explicit human approval; a follow-up search confirmed 0 results. Evidence: `evidence/C3/T3_C3_RunA_Windows_Chrome_Desktop_supp1.png` |

This step does **not** add a 21st Executed row or a 29th manifest row — it
only updates one field on a row already counted in the 20 Executed total.

---

## Blocked rows (8) — Not Executed, no verdict

| Screen | Run | OS | Browser | Device | Status | Reason | Evidence |
|---|---|---|---|---|---|---|---|
| C1 | D | macOS | Safari | Desktop | Blocked / Not Executed | BrowserStack Free Trial enforces a hard 1-minute session limit — confirmed via a live pilot (2026-08-03), not enough time to log in, navigate, and capture evidence | `evidence/blocked/browserstack-1min-trial-limit-banner.jpg` |
| C2 | D | macOS | Safari | Desktop | Blocked / Not Executed | same root cause | same |
| C3 | D | macOS | Safari | Desktop | Blocked / Not Executed | same root cause | same |
| C4 | D | macOS | Safari | Desktop | Blocked / Not Executed | same root cause | same |
| C1 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | Same root cause as Run D (cloud-dependent, same provider limitation) — not independently piloted to avoid consuming another trial session on an already-established result | same |
| C2 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same | same |
| C3 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same | same |
| C4 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same | same |

**Blocked means "not executed, no verdict."** It is not a Fail, and it does
not imply these screens would have failed on macOS or a tablet — no
behavior on those platforms was observed, so none is claimed.

---

## Requirement-gap summary

| Axis | Covered (Executed rows) | Assignment target | Gap |
|---|---|---|---|
| OS | Windows, iOS (2) | Windows, macOS, iOS (3) | **macOS not executed** |
| Browser | Chrome, Firefox, Opera, Edge, Safari (5) | same 5 | none |
| Device class | Desktop, Phone (2) | Desktop, Tablet, Phone (3) | **Tablet not executed** |

**Residual risk:** EMS's rendering behavior on macOS Safari desktop and on a
real tablet viewport is untested and unknown. Given that the one confirmed
Fail (F-022) is a phone-viewport layout defect, a tablet viewport (an
intermediate width) could plausibly surface a related — or a different —
layout issue; this cannot be confirmed or ruled out from the Executed data
alone.

---

## Cross-references

- Full narrative report: `report.md` (this folder).
- Finding detail: F-022, `hw3/work/findings-log.md`.
- Skill used to reconcile this matrix: `hw3/out/agent-skills/compat-run-planner/SKILL.md`.
- Demo video: `demo-video-links.md` (this folder).

# Step 1 — Scenario & Screen Selection

**Owner:** Nguyễn Bảo Duy — 23127179 — Group 09
**Sources:** requirement §5 · `Shared_GUI_Checklist.md` (scenario-assignment table + EMS live survey, 2026-07-26)
**Status:** selected; two items to verify on the live system before Step 3 (see §5)

---

## 1. Chosen scenario

**Scenario C — Admin manages users.** Function group: user administration.

Assigned in the group's scenario table; A, B and D are owned by the other three members, so §5's no-duplication rule is satisfied by scenario alone — no screen appears twice in Group 09.

**Account:** `admin@gmail.com` / `Admin@123`. Scenario C lives entirely on the admin side, so no personal participant account is needed for Task 1B.

## 2. Selected screens — four, not three

§5 requires **at least three**. I take **four**, for the reason the checklist records: *"the user-administration surface is small (a 7-column table, two filters, Edit/Delete row actions). Taking all four C screens keeps the applicable-item count respectable."* At three screens, too much of a 60-item checklist collapses into N/A and criterion 1b has little to grade.

| ID | Screen | What it contributes to checklist coverage |
| --- | --- | --- |
| **C1** | **Users list** (`/dashboard/admin/users`) — 7 columns (USER · Role · MEMBER CODE · Status · CREATED · UPDATED · ACTIONS), 2 header filters, search, pagination, toolbar **Export** + **Add User** | The only IA-03 surface in the scenario: pagination (IA03-06), filter-vs-sort classification (IA03-08), sidebar/active-state (IA03-01), browser-back state (IA03-13). Also the empty/loading states (IA01-06, IA01-07) |
| **C2** | **Assign Role / Edit user** dialog — reached from a row's Edit action | The scenario's only form. Carries IA-02: label persistence (IA02-02), required-field marking (IA02-01 — the checklist names this dialog explicitly as its *third* form), inline errors (IA02-08), selection controls (IA02-12), unsaved-changes exit (IA02-13) |
| **C3** | **Block / Unblock** and **Reset Password** confirmation dialogs | IA-04 destructive-action feedback: confirmation naming the record and its consequence (IA04-03), modality and dimmed background (IA04-02), success toast (IA04-04), ESC-to-close and focus return (IA03-10), status-colour semantics on the resulting Blocked pill (IA04-01, IA01-05) |
| **C4** | **Export to Excel** — toolbar **Export** on Users Management | §5 C4 names it by name: *"column completeness and download feedback."* Sole referent for IA04-13, and the only place where filter-vs-dataset scope can be tested |

## 3. Why these four and not others

§5's suggested list for scenario C is exactly C1–C4; I take all of it, so no "chose others in the same group" justification is owed. The four were kept together rather than trimmed to three because each is the **only** carrier of one IA family in this scenario — dropping C2 loses IA-02 almost entirely, dropping C3 loses the destructive-action half of IA-04, dropping C4 loses IA04-13 and with it §5 C4's own named requirement.

## 4. Predicted N/A profile — plan with it, do not pre-record it

The checklist predicts these N/A for scenario C: **IA01-10, IA01-11, IA02-03…07, IA02-11, IA02-14, IA03-12, IA04-05, IA04-06, IA04-09, IA04-10** — 14 of 60, leaving roughly **46 applicable** items per screen. Cause: the user-admin surface has no upload, no rich-text editor, no date control, no toggle, no capacity figure and no real-time counter.

Two standing rules from the checklist apply:

- These are **predictions to plan with, not results.** Confirm each on my own screens; every N/A carries a **mandatory one-line reason**. Never count N/A as a pass.
- **IA04-13 is not N/A for C** — Export is C4's whole point.

C is the thinnest of the four scenarios. A higher N/A count is expected and acceptable *provided every one is justified in Notes*.

## 5. Open verification before Step 3

1. **C2 vs C3 may be one surface.** The live survey found no row-level Assign-Role / Block / Reset-Password buttons — *"those live inside the Edit dialog."* If all three sit inside a single Edit User dialog, C2 and C3 collapse into one screen and the package is C1 · C2+C3 · C4 = three screens. Still compliant with §5, but the execution report must present it honestly instead of reporting four independent screens. Decide this by opening the dialog, not by assumption. → tracked as **B-12**.
2. **Confirm the Export destination.** IA04-13 covers four Export buttons across EMS; only the **Users Management** one is mine. Do not execute the `/profile`, Support-requests or Registrants exports — they belong to other members' scenarios.

## 6. Screen IDs used in evidence

Evidence filenames and execution tables use these IDs verbatim: `C1`, `C2`, `C3`, `C4`. If C2/C3 collapse per §5.1, the merged screen is recorded as `C2` with a note, and `C3` is retired rather than silently reused.

# Task 3 — Cross-Browser / Cross-Platform Compatibility Report

**Status:** FINAL — promoted from `hw3/work/task-3-cross-platform/report-draft.md`
after human review. Numbers cross-checked against
`hw3/out/reports/task-3-cross-platform/compatibility-matrix.md` and
`hw3/work/task-3-cross-platform/skill-validation.md`.
**Source:** Tự tổng hợp từ `hw3/work/task-3-cross-platform/`. Nội dung được sinh viên kiểm tra trực tiếp.
**Scope note:** this document covers Task 3 (Cross-Browser / Cross-Platform
Compatibility) only. It is not the assignment's consolidated Main Report —
that aggregate document also requires Task 2 (User Testing), which is not
yet complete (see Section 10).

---

## 1. Scope and methodology

Scope: Scenario C (Admin manages users) on the EMS SUT
(`https://prod-dev.ems-fitus.cloud`), screens C1 (Users list), C2 (Edit User
dialog), C3 (Delete User confirm dialog), C4 (Export to Excel).

**Coverage Fallback Strategy.** The assignment's ideal target is 3 OS
(Windows, macOS, iOS) × 5 browsers (Chrome, Firefox, Opera, Safari, Edge) × 3
device classes (desktop, tablet, phone), per screen. A pilot run on
BrowserStack (Run D, 2026-08-03) confirmed the Free Trial plan enforces a
hard 1-minute session limit — not enough to log in, navigate, and capture
evidence. This is a third-party infrastructure limit, not an avoidance
choice. The plan shifted to a Coverage Fallback Strategy: run the 5
configurations that are actually feasible without cloud infrastructure (4
browsers on local Windows + Safari on a physical iPhone) as **Executed**
cells, and mark the 2 cloud-dependent configurations (macOS Desktop, iOS
Tablet) as **Blocked / Not Executed** with evidence, rather than simulating
them.

**No-DOM Policy.** All interaction with EMS itself is through the visible UI
only (click, type, scroll, screenshot) — no DOM inspection, no script
injection, no selector-based actions against EMS. DOM-based tooling was used
only against BrowserStack's own control panel during the pilot, never
against EMS, and only before the cloud path was abandoned.

**Actor model.** Each cell records a Planned and an Actual Execution Mode,
one of: `AI-executed`, `AI-executed with human checkpoints`, or
`Human-executed with AI guidance`. Section 8 summarizes the actual
distribution.

**Test data.** A single disposable test user (`test abc` /
`abcdefabc@gmail.com`, Guest, Inactive, Member Code `91984123`) was reused
across all 5 Executed runs for C2/C3. C3 was run at "Dialog-only" scope
(Cancel, not Confirm) on every run except a final, separate step on Run A
that performed the actual deletion once all runs had finished with the
dialog — see Section 7.

---

## 2. Executed coverage (20 cells)

| Screen | Run | OS | Browser | Device | Actual Execution Mode | Verdict |
|---|---|---|---|---|---|---|
| C1 | A | Windows | Chrome | Desktop | AI-executed with human checkpoints | Pass (render + behavior verified) |
| C1 | B | Windows | Firefox | Desktop | Human-executed with AI guidance | Pass (render + behavior verified) |
| C1 | C | Windows | Opera | Desktop | Human-executed with AI guidance | Pass (render + behavior verified) |
| C1 | G | Windows | Edge | Desktop | Human-executed with AI guidance | Pass (render + behavior verified) |
| C1 | F | iOS | Safari | Phone | Human-executed with AI guidance | **Fail** — F-022, severity 2 |
| C2 | A | Windows | Chrome | Desktop | AI-executed with human checkpoints | Pass (render + behavior verified) |
| C2 | B | Windows | Firefox | Desktop | Human-executed with AI guidance | Pass (render + behavior verified) |
| C2 | C | Windows | Opera | Desktop | Human-executed with AI guidance | Pass (render + behavior verified) |
| C2 | G | Windows | Edge | Desktop | Human-executed with AI guidance | Pass (render + behavior verified) |
| C2 | F | iOS | Safari | Phone | Human-executed with AI guidance | Pass (render + behavior verified) |
| C3 | A | Windows | Chrome | Desktop | AI-executed with human checkpoints | Pass — **Full confirm flow** (see Section 7) |
| C3 | B | Windows | Firefox | Desktop | Human-executed with AI guidance | Pass — Dialog-only, Confirm not pressed |
| C3 | C | Windows | Opera | Desktop | Human-executed with AI guidance | Pass — Dialog-only, Confirm not pressed |
| C3 | G | Windows | Edge | Desktop | Human-executed with AI guidance | Pass — Dialog-only, Confirm not pressed |
| C3 | F | iOS | Safari | Phone | Human-executed with AI guidance | Pass — Dialog-only, Confirm not pressed |
| C4 | A | Windows | Chrome | Desktop | AI-executed with human checkpoints | Pass (filesystem-verified download) |
| C4 | B | Windows | Firefox | Desktop | Human-executed with AI guidance | Pass (filesystem-verified download) |
| C4 | C | Windows | Opera | Desktop | Human-executed with AI guidance | Pass (filesystem-verified download) |
| C4 | G | Windows | Edge | Desktop | Human-executed with AI guidance | Pass (filesystem-verified download) |
| C4 | F | iOS | Safari | Phone | Human-executed with AI guidance | Pass (Safari Downloads panel confirmed — see Section 10 for an evidence exception on this cell) |

Evidence for every row above is a promoted file under
`hw3/out/reports/task-3-cross-platform/evidence/<screen>/`, each traceable
back to a raw capture and a reviewed annotated candidate in
`hw3/work/task-3-cross-platform/` (see Section 9).

---

## 3. Pass / Fail matrix

| Verdict | Count | Cells |
|---|---|---|
| Pass | **19** | All Executed cells except C1/Run F |
| Fail | **1** | C1 / Run F / iOS / Safari / Phone — **Finding F-022**, severity 2 (see Section 6) |

No other Executed cell produced a Fail. C2/Run F (same device, different
screen) passed cleanly, which is itself evidence that the C1 Fail is a
layout-specific defect in the Users-list screen, not a blanket
mobile-Safari incompatibility (see Section 6).

---

## 4. Blocked coverage (8 cells — Not Executed, no verdict)

| Screen | Run | OS | Browser | Device | Status | Evidence |
|---|---|---|---|---|---|---|
| C1 | D | macOS | Safari | Desktop | Blocked / Not Executed | `setup-evidence/browserstack-1min-trial-limit-banner.jpg` + pilot note (2026-08-03) |
| C2 | D | macOS | Safari | Desktop | Blocked / Not Executed | same (shared root cause, not re-tested per cell) |
| C3 | D | macOS | Safari | Desktop | Blocked / Not Executed | same |
| C4 | D | macOS | Safari | Desktop | Blocked / Not Executed | same |
| C1 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same root cause as Run D — not independently piloted, to avoid burning another trial session for a result already known |
| C2 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same |
| C3 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same |
| C4 | E | iOS | (not selected) | Tablet | Blocked / Not Executed | same |

**Reason (all 8 rows):** BrowserStack's Free Trial plan enforces a hard
1-minute session limit, confirmed directly during the Run D pilot
(2026-08-03) — not enough time to log in, navigate to the target screen, and
capture evidence before the session force-closes. **Blocked means "not
executed, no verdict" — it is not a Fail and does not imply the screen would
have failed on macOS/tablet.** No behavior on these platforms was observed,
so none is claimed.

---

## 5. Requirement gap

The assignment's ideal target (3 OS × 5 browsers × 3 device classes, per
screen) is **not fully met** by the Executed set:

| Axis | Covered (Executed) | Target | Gap |
|---|---|---|---|
| OS | Windows, iOS (2) | Windows, macOS, iOS (3) | **macOS missing** |
| Browser | Chrome, Firefox, Opera, Edge, Safari (5) | same 5 | none |
| Device class | Desktop, Phone (2) | Desktop, Tablet, Phone (3) | **Tablet missing** |

**Residual risk:** EMS's actual rendering behavior on macOS Safari desktop
and on a real tablet viewport is unknown and untested. Given that C1's
sidebar/layout defect (F-022) was found specifically on a phone viewport,
there is a non-trivial chance a tablet viewport (intermediate width) could
surface a related or different layout issue — this cannot be confirmed or
ruled out from the Executed data alone.

---

## 6. F-022 finding

| Field | Content |
|---|---|
| ID | F-022 |
| Screen / Scenario | C1 — Users Management (cross-platform, Safari/iOS/iPhone thật) |
| Type | Bug |
| Severity | 2 (Minor — confirmed by the student) |
| Description | On a phone viewport (828×1792, Safari/iOS), Users Management loads with the sidebar fully expanded by default, covering nearly all main content (title, search box, Export/Add User buttons, table, ACTIONS column) — only a narrow strip is visible. Collapsing the sidebar to icon-only (the reasonable next step a real user would try) does **not** fix it: main content still overflows the viewport (title, Export button cut off at the right edge), still requires horizontal scrolling. |
| Steps to reproduce | 1. Open `https://prod-dev.ems-fitus.cloud/dashboard/admin/users` on Safari, physical iPhone. 2. Observe default state — sidebar open, content obscured. 3. Tap the sidebar-collapse (hamburger) control. 4. Observe: main content still overflows past the right edge. |
| Expected | On a phone viewport, the sidebar should collapse or hide as an overlay/drawer by default, and main content should reflow to fit the screen width without horizontal scrolling. |
| Actual | Sidebar open by default, obscuring content; even after collapsing, main content still overflows the 828px viewport. |
| Suggested fix | Add a responsive breakpoint for viewports ≲430–768px: (a) sidebar collapsed/hidden as a drawer by default on phone; (b) main content uses a fluid layout (flex/grid with a viewport-relative max-width) instead of a fixed desktop width. |
| Evidence | Primary: `T3_C1_RunF_iOS_Safari_Phone.png` (default state). Supplementary: `_supp1.png` (after horizontal scroll), `_supp2.png` (after sidebar collapse, still overflowing). |
| Google Form submission | Submitted 2026-08-03, confirmed via the "Your response has been recorded" screenshot — **exact timestamp not recorded** (Form does not return a per-response timestamp). This is a directly verified submission, not merely a recorded claim (contrast with Section 12 / AI Audit note on the Task 1 findings). |

**Contrast with C2/Run F:** on the same physical device and browser, the C2
Edit User dialog rendered correctly with no overflow — the defect is
specific to the C1 list+sidebar layout, not a blanket iOS/Safari
incompatibility.

---

## 7. C3 Interaction Coverage

| Run | Interaction Coverage | Note |
|---|---|---|
| A (Chrome/Windows) | **Full confirm flow** | Upgraded 2026-08-03, after Runs B/C/G/F had all completed C3 at Dialog-only scope, to avoid needing to recreate the disposable test user mid-sequence. The user explicitly confirmed ("Confirm") before the actual delete was performed. `test abc` was deleted for real; a follow-up search for `abcdefabc` returned 0 results, confirming the delete succeeded. |
| B, C, G, F | Dialog-only | Dialog opened, warning read, closed via Cancel — Confirm never pressed, to preserve the disposable user for the remaining runs. |

**This upgrade is a Supplementary Validation step, not a 21st Executed
cell.** It only changes the Interaction Coverage field already tracked on
the existing C3/Run A row (row #11 of the manifest's Executed section). The
Executed total remains 20.

---

## 8. Actual Execution Mode summary

| Mode | Count (of 20 Executed cells) | Runs |
|---|---|---|
| AI-executed with human checkpoints | 4 | Run A (all 4 screens) |
| Human-executed with AI guidance | 16 | Runs B, C, G, F (4 screens each) |
| AI-executed (no human checkpoint) | 0 | — |

Every count above is read directly from each run log's own stated mode —
none is inferred for a cell the log doesn't explicitly cover.

---

## 9. Evidence index

All paths relative to `hw3/out/reports/task-3-cross-platform/evidence/`
unless noted. **P** = primary, **S** = supplementary.

| Screen | Run | Files |
|---|---|---|
| C1 | A | `T3_C1_RunA_Windows_Chrome_Desktop.png` (P) · `..._supp1.png` (S — filtered-list state) |
| C1 | B | `T3_C1_RunB_Windows_Firefox_Desktop.png` (P) |
| C1 | C | `T3_C1_RunC_Windows_Opera_Desktop.png` (P) |
| C1 | G | `T3_C1_RunG_Windows_Edge_Desktop.png` (P) |
| C1 | F | `T3_C1_RunF_iOS_Safari_Phone.png` (P) · `..._supp1.png`, `..._supp2.png` (S) |
| C2 | A | `T3_C2_RunA_Windows_Chrome_Desktop.png` (P) · `..._supp1.png` (S — dropdown/checkbox state) |
| C2 | B/C/G/F | one primary file each |
| C3 | A | `T3_C3_RunA_Windows_Chrome_Desktop.png` (P) · `..._supp1.png` (S — post-delete state) |
| C3 | B/C/G/F | one primary file each |
| C4 | A/B/C/G/F | one primary file each |
| Blocker (Run D/E, all screens) | — | `setup-evidence/browserstack-1min-trial-limit-banner.jpg` (shared) |

Every file above traces back to a raw capture and a reviewed annotated
candidate under `hw3/work/task-3-cross-platform/` — verified 1:1 during this
drafting pass (25 files: 20 primary + 5 supplementary, matching across raw /
candidate / final at every screen).

---

## 10. Limitations and residual risks

- **BrowserStack Free Trial limitation** — the single cause behind all 8
  Blocked cells (Section 4/5). Not retried beyond one pilot per
  root-cause-sharing group, to avoid burning further trial sessions for a
  result already established.
- **Untested macOS/Tablet behavior** — genuinely unknown, not assumed safe
  or assumed broken (Section 5).
- **C4/Run F evidence exception (disclosed):** the primary screenshot for
  C4/Run F does not show the browser address bar — it is covered by
  Safari's native Downloads panel, which was the very thing the screenshot
  needed to capture. Per explicit instruction from the student, this was
  accepted without a companion URL-visible shot; the URL is corroborated
  indirectly through the C1/C2 screenshots from the same session (same
  search term `abcdefabc`, same date 2026-08-03).
- **No DevTools-simulated tablet/mobile evidence was substituted** for the
  Blocked cells — doing so was explicitly ruled out as a §12-violating
  workaround throughout planning.

---

## 11. Human-review statement

Tôi (sinh viên) xác nhận đã trực tiếp chạy pilot, thiết kế cấu trúc test, và review lại toàn bộ các verdict cũng như screenshot do Agent Skill phụ trợ xuất ra. Các quyết định về severity (như F-022) và giới hạn coverage (thiếu macOS/Tablet do BrowserStack) là quyết định có chủ đích và do chính tôi chịu trách nhiệm. Mọi artifact trong báo cáo này đều phản ánh đúng sự thật của quá trình test EMS.

---

## 12. AI-use summary

Tóm tắt mức độ sử dụng AI (chi tiết nằm trong AI Audit Report của nhóm):

- **Planning & pilot:** Sử dụng AI để lập kế hoạch; quyết định Coverage Fallback được đưa ra dựa trên kết quả pilot BrowserStack thực tế.
- **Run A:** AI-executed with human checkpoints (Sinh viên kiểm soát và duyệt qua từng checkpoint để AI thao tác an toàn trên trình duyệt).
- **Runs B, C, G, F:** Human-executed with AI guidance (Sinh viên tự thao tác 100% trên thiết bị thật, AI hỗ trợ chú thích ảnh và log data).
- **Evidence annotation & drafting:** AI tạo bản nháp dựa trên log của sinh viên, sinh viên trực tiếp rà soát và duyệt từng ghi chú, đặc biệt là lỗi F-022.
- **Report này:** Do sinh viên tổng hợp, có dùng AI hỗ trợ format markdown cho chuẩn và đối chiếu số liệu. Mọi thay đổi đều được sinh viên xác nhận.

**Note on Task 1 submissions:** Các Google Form submissions của Task 1B đã được ghi nhận trong `README.md`, `bug-reports.md`, và `findings-log.md` theo quy trình đối soát ở Task 1.

---

## 13. Demo-video reference

Both Agent Skills used to reconcile and draft this report — `compat-run-planner`
and `compat-evidence-report` — are demonstrated end-to-end on these real
Task 3 artifacts in a recorded video:

- **URL:** https://youtu.be/GbhAEK7x8Vk
- **Full record:** `demo-video-links.md` (this folder) — recording date,
  segment structure, and what the session logs confirm actually happened
  (both skills invoked live, numbers matched source of truth, no
  promotion occurred during the recording).
- **Skill sources:** `hw3/out/agent-skills/compat-run-planner/SKILL.md`,
  `hw3/out/agent-skills/compat-evidence-report/SKILL.md`.
- **Note:** Video được quay từ phía sinh viên thao tác thật, chứng minh các công cụ AI được gọi một cách tường minh và an toàn, kết quả khớp với số liệu trong báo cáo.

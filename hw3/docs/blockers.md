# Step 0 — Blockers

**Owner:** Nguyễn Bảo Duy — 23127179 — Group 09
**Sources of truth:** `hw3/docs/hw3-reqs/2026.HW03.GUI Usability EMS_En.md` (§) · `hw3/docs/gui-checklist/Shared_GUI_Checklist.md`
**Last updated:** 2026-08-02

---

## Resolved

| ID | Question | Resolution | Evidence |
| --- | --- | --- | --- |
| **B-01** | Which scenario? | **Scenario C — Admin manages users** | Scenario-assignment table, `Shared_GUI_Checklist.md` §Scenario assignment |
| **B-02** | Which screens? | **C1** Users list · **C2** Assign Role / Edit user · **C3** Block-Unblock & Reset-Password dialogs · **C4** Export to Excel — four, not the §5 minimum of three | Same table; rationale in `screen-selection.md` |
| **B-03** | Who is in the group? | **Group 09**, four members, four distinct scenarios (A/B/C/D) — §5 no-duplication satisfied by scenario alone | `Shared_GUI_Checklist.md` §Group Information |
| **B-04** | Task 1A — does the shared checklist exist? | **Yes. Task 1A is complete.** `Shared_GUI_Checklist.md` v1.9, **60 items** across IA-01…IA-04 (§6 requires > 40). **Do not generate a new checklist.** | The file itself |
| **B-05** | Which account is needed? | `admin@gmail.com` / `Admin@123` (§4). Scenario C is admin-side only — **no personal student account is required** for C1–C4 (that constraint applies to scenarios B and the user half of D) | §4 of the requirement |

---

## Open — human action required

| ID | Blocker | Why it blocks | Needed before |
| --- | --- | --- | --- |
| **B-06** ✅ **RESOLVED 2026-08-02** | **EMS reachable?** Confirm login at `https://prod-dev.ems-fitus.cloud/login?callbackUrl=%2F` with the admin account. §4 warns the instance is tunnelled and its data may be reset periodically — capture evidence as you go. | Nothing can be executed against a dead SUT | Step 3 |
| **B-07** | **BrowserStack / LambdaTest trial** registered and working (§6 Task 3 — "you are responsible for obtaining your own trial access"). | Task 3 (25 pts) cannot start | Step 4 |
| **B-08** | **1 pilot participant** recruited (§6 Task 2 Phase 1 — the pilot is *required*, not optional). Must **not** be one of the 5. | Step 7 | Step 7 |
| **B-09** | **5 real participants**, outside this class, with verifiable contacts (Zalo / email / phone, middle four digits masked). TA may call two; impersonation voids Task 2. | Task 2 (25 pts) | Step 8 |
| **B-10** | **Student-ID email** (`MSSV@....edu.vn`) available and usable. §6 Task 3 requires it as an overlay on every cross-platform screenshot; §7 requires it as the Google-Form identity. | Every Task 3 capture and every form submission | Step 3 (first form submission) |
| **B-11** | **Group companion artefacts are not in this repository.** `Shared_GUI_Checklist.md` cites four group files that are absent here: `Reference_Sources_and_Prompts.md`, `AI_Audit_Report.md`, `EMS_Live_Survey_2026-07-26.md`, and `../screenshots/` (14 PNGs). §15 requires the reference-sources list and the checklist AI prompts as group artefacts in the submission. Obtain copies from the group — **do not reconstruct them**; they document work already done and reconstructing them would fabricate provenance. | §15 submission completeness; criterion 1a | Step 13 (but fetch early) |
| **B-12** ✅ **RESOLVED 2026-08-02** | **C2 and C3 may be the same surface.** The live survey records: *"No Assign-Role / Block / Reset-Password button at row level — those live inside the Edit dialog."* If Assign Role, Block/Unblock and Reset Password are all controls **inside one Edit User dialog**, then C2 and C3 are one screen, leaving C at three (C1, C2+C3, C4) — still ≥ 3, but the execution report must say so rather than double-count. Verify on the live system in Step 1/3. | Screen count integrity (§5); execution-report honesty | Step 3 |
| **B-13** | **Checklist group sign-off.** v1.7, v1.8 and v1.9 are logged as *"pending group review / group sign-off"*. Also outstanding: the **pillar-4 gap** — 1–2 items per member drawn from personal frustration using EMS, retargeted to v2.0. This is optional for my individual tasks but is the cheapest remaining gain on criterion 1a (group). | Criterion 1a only — **does not block Task 1B execution** | Optional |

---

## Rules that follow from these answers

1. **Task 1 starts at Part B.** My first Task-1 action is executing the existing 60-item checklist against C1–C4 — not designing items.
2. **The checklist is frozen input.** §Task 1A: *"Do not edit item wording per-member — the checklist must stay identical across the group."* Any defect I find in an item goes to the group, not into my copy.
3. **EMS is an external, black-box web SUT.** All evidence comes from the browser. No source code is available or examined.


---

## Cập nhật sau phiên execution Task 1B — 2026-08-02

### B-06 ✅ RESOLVED
EMS truy cập được. Đăng nhập `admin@gmail.com` thành công, mở được `/dashboard/admin/users`.
**Cảnh báo §4 là thật:** dữ liệu đổi **ngay trong phiên** — tổng số user đi từ **105 → 106 → 107**, badge Support requests từ **7 → 6**. Mọi số đo trong báo cáo đều ghi kèm thời điểm đo.

### B-12 ✅ RESOLVED — và kết quả làm hẹp phạm vi C3

Mở dialog Edit User và khảo sát trực tiếp DOM:

| Chức năng | Kết quả |
| --- | --- |
| **Assign Role** | ✅ Có — dropdown `Role` (Admin/Guest/Lecturer/Student) **bên trong dialog Edit User** |
| **Block / Unblock** | ✅ Có, nhưng **không phải dialog riêng** — là checkbox `Active` **bên trong chính dialog Edit User**. Không có nút Block ở cấp dòng |
| **Reset Password** | ❌ **KHÔNG TỒN TẠI trong EMS.** Không ở cấp dòng, không trong dialog Edit, không trên toolbar. Field `Password` chỉ có ở dialog **Create New User** |

**Quyết định:** C3 được định nghĩa lại thành **dialog xác nhận Delete User** — bề mặt duy nhất trên scenario C thật sự là một dialog riêng và thật sự thuộc nhóm hành động phá huỷ. Bộ màn hình vẫn là 4 bề mặt phân biệt, **nhưng README ghi rõ rằng một nửa nội dung C3 gốc không tồn tại**, không đếm gộp cho đủ 4. Chi tiết: `hw3/work/notes/C2-exploration.md` §5 và `hw3/out/reports/checklist-execution/README.md` §*Số màn hình thực tế*.

### B-10 ⬜ VẪN CHẶN — cần email sinh viên
20 finding đã sẵn sàng trong `hw3/out/reports/checklist-execution/bug-reports.md` nhưng **chưa submit** lên Google Form, vì Form cần đăng nhập bằng `MSSV@....edu.vn`. Cột *Form timestamp* trong `work/findings-log.md` để trống toàn bộ (0/20).

### B-11 ⬜ VẪN CHẶN — cần xin từ nhóm
4 artefact của nhóm vẫn chưa có trong repo. **Không dựng lại.**

### Blocker mới phát sinh trong phiên — B-13 🟡 GIẢI QUYẾT MỘT NỬA (2026-08-03)
**2 item cần DevTools throttling không chạy được bằng công cụ tự động hoá:** `IA01-07` (Slow 3G) và `IA04-11` (Offline).

**Cập nhật 2026-08-03 — sinh viên chạy tay:**
- ✅ **IA01-07 — XONG, verdict `Pass`.** DevTools → Network → Slow 3G → hard-reload Users Management: **có skeleton** trong lúc bảng tải. Ghi vào `C1.md`.
- 🟡 **IA04-11 — XONG MỘT NỬA.** Lần báo đầu tiên (logout khỏi user account → sang admin → set Inactive → *"không báo lỗi gì cả"*) **không dùng được** để chấm, vì thao tác đó **thành công**, không phải kịch bản offline; quan sát ấy được chuyển vào **F-014**. Lần thứ hai, sinh viên chạy **đúng** kịch bản: DevTools → Network → Offline → Edit User → bỏ tick `Active` → Save Changes.
  - **Vế *"submit a form"* → XONG, verdict `Fail` trên C2**, thành **F-021**. Kết quả đáng chú ý: EMS **có** báo lỗi inline trong dialog và **không** có toast success giả — tức tránh được đúng cái tệ nhất mà item cảnh báo. Cái hỏng là **nội dung** thông báo: chuỗi thô `Failed to fetch` của Fetch API, không nói cái gì hỏng, không có retry. Bằng chứng: `evidence/C2/C2_IA04-11_offline-save-failed-to-fetch.png` (97 request `(failed)`, 121 console error).
  - ⬜ **Vế *"load a list screen"* → VẪN CHƯA CHẠY.** Lần đo đó không reload danh sách trong lúc offline; bảng phía sau dialog là dữ liệu cũ đã tải trước khi ngắt mạng. Cần: bật Offline → **hard-reload** `/dashboard/admin/users`. Ô verdict `IA04-11` trên **C1** vẫn để trống.

**Bài học ghi lại:** dự đoán trong báo cáo bản đầu (*"nếu lưu hỏng mà im lặng thì đó là severity cao nhất"*) đã **bị dữ liệu thật bác bỏ**. Giữ nó lại trong F-014 có đánh dấu, thay vì xoá — để thấy phỏng đoán đã được kiểm chứng chứ không âm thầm biến mất. Extension trình duyệt không bật được Network throttling. Hai ô verdict để trống có ghi rõ lý do, **không đoán**. IA04-11 là item đáng tiếc nhất: đã biết chắc EMS không phát toast khi Save **thành công**, nên câu còn bỏ ngỏ là khi Save **thất bại** giao diện có nói gì không — nếu cũng im lặng thì một lần lưu hỏng trông y hệt một lần lưu thành công.

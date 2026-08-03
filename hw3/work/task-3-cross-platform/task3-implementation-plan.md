# Task 3 — Cross-Browser / Cross-Platform Testing: Implementation Plan

**Scenario:** C — Admin manages users (kế thừa nguyên vẹn từ Task 1/Task 2)
**Screens/functions (4, đã đóng băng từ Task 1):**

| ID | Screen | Vì sao vẫn dùng đúng bộ này cho Task 3 |
| --- | --- | --- |
| C1 | Users list (`/dashboard/admin/users`) | §6 đề bài: *"Tasks 1B, 2, and 3 all operate on the same three (or more) screens."* Ràng buộc cứng — Task 1 đã đóng băng 4 bề mặt C1–C4 |
| C2 | Edit User dialog (Assign Role + Block/Unblock) | nt |
| C3 | Delete User confirm dialog | nt — đã xác minh với `C3.md` gốc |
| C4 | Export to Excel | nt |

**Trạng thái tài liệu:** Kế hoạch, bản **v7** — chuyển sang **Coverage Fallback Strategy** sau khi pilot thật phát hiện blocker (BrowserStack Free Trial giới hạn cứng 1 phút/phiên). **Manifest đã tạo (`compatibility-manifest-working.md`), Bước 1 đã hoàn thành phần lớn, chưa chạy cell thật nào (chưa có raw evidence), chưa gọi `generate_skill`.**

**Thay đổi cốt lõi ở v7:**
1. **Pilot Run D phát hiện blocker thật:** BrowserStack Free Trial = 1 phút/phiên, tự động đóng — không đủ để login + điều hướng + chụp evidence. Evidence blocker: `setup-evidence/browserstack-1min-trial-limit-banner.jpg`.
2. **Chuyển từ "24/24 bắt buộc" sang Coverage Fallback Strategy:** chạy đầy đủ 5 cấu hình thật sự có (4 browser Windows local + Safari iPhone thật) = 20 cell; 2 run phụ thuộc cloud (macOS Desktop, iOS Tablet) đánh dấu **Blocked / Not Executed** kèm evidence, không Pass/Fail, không giả lập.
3. **Thêm Run G — Edge/Windows/Desktop (mới)** vào bộ chạy được, để vẫn giữ đủ 5 browser phân biệt trong phần Executed.
4. **Phát hiện thêm 1 ràng buộc quan trọng:** Claude không được tự nhập password vào EMS ở **bất kỳ môi trường nào** (kể cả Chrome local) — người dùng phải tự đăng nhập 1 lần/browser/thiết bị, sau đó session giữ đăng nhập qua cookie để Claude điều hướng tiếp các screen còn lại.
5. Report giờ tách rõ 3 phần: **Executed coverage / Blocked coverage / Requirement gap** — nói thẳng Task 3 không đạt đủ 3 OS × 3 device class theo đúng nghĩa đen, nhưng không fabricate.

### Xác minh scope C3 (không đổi qua các vòng review)

Đã đọc `hw3/out/reports/task-1-checklist-execution/C3.md` (dòng 1–29): "Block-Unblock and Reset-Password dialogs" theo phân công gốc không tồn tại trong EMS. C3 được định nghĩa lại có chủ đích thành "dialog xác nhận Delete User" — deviation được đề bài cho phép tường minh (§5). Giữ nguyên.

### Phân tách Working vs Final (không đổi nguyên tắc)

`hw3/work/task-3-cross-platform/` chứa mọi thứ đang thay đổi. `hw3/out/` chỉ chứa kết quả cuối đã human-approved. 12 quy tắc promotion giữ nguyên từ v6 (screenshot raw → annotated-candidates → out/evidence; manifest working → compatibility-matrix.md; report-draft.md → report.md; skill → agent-skills; findings-log working → out/findings-log.md thuộc Final Submission Integration; report.md → Main Report thuộc Final Submission Integration). Promotion cần **explicit human approval**, không nhất thiết là thao tác tay theo nghĩa đen.

---

## A. Requirement interpretation (Requirement-derived)

1. **Coverage bắt buộc theo đề (lý tưởng, không đổi):** 3 OS (Windows, macOS, iOS) · 5 browser (Chrome, Firefox, Opera, Safari, Edge) · 3 device class (desktop, tablet, phone) — mỗi screen.
2. **Thực tế đã xác minh qua pilot (mới ở v7):** macOS và Tablet phụ thuộc hoàn toàn vào BrowserStack cloud, và cloud bị giới hạn 1 phút/phiên trên Free Trial — không đủ thời gian login + điều hướng + chụp evidence hợp lệ. Đây là **giới hạn hạ tầng bên thứ ba**, không phải lựa chọn né tránh.
3. **Coverage Fallback Strategy (mới ở v7, xem Section D):** chạy đủ 5 cấu hình thật sự khả thi (4 browser Windows local + Safari trên iPhone thật) cho cả 4 screen = 20 cell **Executed**. 2 cấu hình phụ thuộc cloud (macOS Desktop, iOS Tablet) đánh dấu **Blocked / Not Executed** cho cả 4 screen = 8 dòng blocked, kèm evidence blocker, không gán Pass/Fail, không dùng DevTools giả lập tablet để lấp chỗ trống.
4. **Công cụ:** BrowserStack (đã xác nhận có tài khoản), dự phòng LambdaTest — **nhưng bản chất giới hạn thời gian trial nhiều khả năng tương tự ở bất kỳ provider miễn phí nào**; không giả định đổi provider sẽ tự động giải quyết được vấn đề.
5. **Evidence bắt buộc cho MỌI cell Executed:** 1 screenshot final/cell, đủ browser/OS/device + EMS URL + overlay email, truy ngược được về raw.
6. **Cell Fail** cần ghi chú mô tả lỗi cụ thể.
7. **Pass/Fail phải dựa trên run thật**, không suy đoán (§12). Cell Blocked **không có verdict** (không Pass, không Fail) — khác biệt rõ với Fail.
8. **C3 có 2 phạm vi verdict riêng biệt:** Dialog-only vs Full confirm flow — xem Section D. Chỉ áp dụng cho cell Executed.
9. **Xử lý đăng nhập EMS (mới ở v7):** Claude không tự nhập password ở bất kỳ môi trường nào. Người dùng đăng nhập 1 lần/browser/thiết bị; session giữ qua cookie cho các thao tác điều hướng tiếp theo trong cùng browser đó. Xem Section B.
10. **Liên hệ phần khác của bài** — tách theo 2 nhóm:
    - **Thuộc Task 3 Execution Done:** matrix 20 cell Executed + 8 cell Blocked có evidence, report module Task 3 (tách Executed/Blocked/Requirement gap), findings từ cell Executed đã submit Form + merge vào working log, 2 skill + demo video, AI Audit entries của Task 3 (gồm cả phiên pilot dẫn tới quyết định Blocked).
    - **Thuộc Final Submission Integration Done (phụ thuộc Task 1/2, làm sau):** Findings Log final toàn bài, Main Report MD/PDF hợp nhất, README cuối kỳ, git commit log cuối kỳ, AI Critique cuối cùng, ZIP nộp.

**Giả định/Đã xác nhận:**
- BrowserStack: đã đăng nhập (`nguyenbaoduy29@gmail.com`, Google, Owner) — **nhưng Free Trial 1 phút/phiên là blocker thật, không phải giả định.**
- Overlay email: `23127179@student.hcmus.edu.vn`.
- Disposable test user `test abc` / `abcdefabc@gmail.com` (Guest, Inactive, Member Code `91984123`): còn tồn tại — xác nhận qua Bước 1.

**Thiết bị xác nhận thật:** Windows desktop (Firefox ✅ cài sẵn v153.0.1, Opera ⏳ người dùng tự cài), một iPhone thật. Không iPad, không Mac, không Android.

---

## B. Feasibility assessment — Actor Model, No-DOM Policy, Coverage Fallback

### Tư duy HW2 tái sử dụng được đến đâu (không đổi)

| Tư duy HW2 | Áp dụng cho Task 3? | Vì sao |
| --- | --- | --- |
| 1. Chạy tay 1 flow đầu để hiểu thực tế | ✅ | Pilot đã đúng vai trò: phát hiện blocker thật trước khi cam kết chạy đại trà |
| 2. Ghi nhận kết quả + evidence | ✅, kể cả evidence của **blocker**, không chỉ evidence Pass/Fail |
| 3. Human review trước khi đóng băng | ✅ |
| 4. Chuẩn hoá thành Agent Skill | ✅ |
| 5. Dùng skill áp dụng nhanh cho phần còn lại | ⚠️ Không giải quyết được giới hạn hạ tầng của provider — skill chỉ quản lý dữ liệu |
| 6. Human-in-the-loop | ✅ |
| 7. Sinh report/audit từ dữ liệu đã review | ✅, **cộng thêm phần Blocked/Requirement gap** phải do người viết, không chỉ AI tổng hợp số |

### No-DOM Policy (không đổi từ v6)

> EMS DOM, console và network không được dùng trong test execution hoặc để xác định Pass/Fail. Sau khi một Fail đã được xác nhận qua visible UI, có thể dùng diagnostic tools để điều tra nguyên nhân — ghi trong run log, không đổi verdict.

> Không được sử dụng hidden DOM state, invisible controls, internal attributes, hoặc selector-based actions để bypass visible UI.

BrowserStack's own control panel vẫn không bị cấm DOM-based tool (không phải EMS).

### Xử lý đăng nhập EMS — mới ở v7 (không nhập password ở bất kỳ đâu)

Phát hiện qua pilot Run D: khi Claude điều hướng EMS mà chưa đăng nhập, EMS redirect về `/login`. Theo chính sách đang áp dụng, **Claude không nhập password vào bất kỳ form nào, kể cả account test của bài tập, kể cả trên Chrome local.**

**Quy trình chuẩn (áp dụng cho mọi run Executed):**
1. Người dùng **tự đăng nhập EMS admin** (`admin@gmail.com`/`Admin@123`) đúng 1 lần trong mỗi browser/thiết bị sẽ dùng: Chrome (đúng cửa sổ Claude in Chrome đang kết nối), Firefox, Opera, Edge, Safari trên iPhone.
2. Session giữ đăng nhập qua cookie của trình duyệt đó. Claude (với Chrome) hoặc người dùng (với Firefox/Opera/Edge/iPhone) điều hướng tiếp qua C1–C4 mà không cần đăng nhập lại, **miễn phiên chưa hết hạn/bị đăng xuất.**
3. Nếu phiên hết hạn giữa chừng (đăng xuất bất ngờ), dừng, báo người dùng đăng nhập lại — không tự thử nhập password để "tiếp tục cho nhanh."
4. **BrowserStack cloud không áp dụng được quy trình này** — mỗi phiên là máy/thiết bị mới, không có cookie cũ, và 1 phút không đủ để cả đăng nhập lẫn thao tác. Đây là lý do chính khiến cloud cell bị Blocked, không chỉ vì giới hạn thời gian đơn thuần.

### Coverage Fallback Strategy — mới ở v7

Thay cho mục tiêu cứng "24/24 cell", plan giờ theo khung:

```
Target (lý tưởng theo đề):     24 cells (3 OS × 5 browser × 3 device, covering set 6/screen)
Guaranteed execution:          20 cells (5 cấu hình thật × 4 screen — Executed)
Cloud-dependent cells:         8 cells (2 cấu hình cloud × 4 screen — Blocked, có evidence)
Fabrication:                   0 — không có cell nào Pass/Fail mà chưa chạy thật, không dùng DevTools giả lập thiết bị
```

**Nguyên tắc xử lý Blocked cell:**
- Ghi trạng thái `Blocked / Not Executed` — không phải `Fail`, không phải để trống.
- Đính kèm evidence: screenshot banner giới hạn trial (`setup-evidence/browserstack-1min-trial-limit-banner.jpg`) + ghi chú mô tả đã thử gì, thất bại ở đâu.
- Ghi rõ: đã thử BrowserStack (Sonoma/Safari, Run D pilot 2026-08-03); nếu có thời gian, có thể thử thêm 1 provider khác (LambdaTest) trước khi chấp nhận Blocked hẳn — xem "Workaround cuối" dưới.
- Không Pass/Fail cho cell Blocked.
- Không dùng DevTools responsive mode rồi ghi nhãn "tablet thật" để lấp chỗ trống — vi phạm §12 trực tiếp, đã cấm từ các bản trước, không đổi.

**Workaround cuối trước khi chấp nhận Blocked hẳn (tuỳ chọn, không bắt buộc):** thử lại 1 lần với điều kiện: người dùng tự đăng nhập ngay khi phiên cloud mở ra, Claude chỉ làm 1 thao tác ngắn trên C1, chụp evidence ngay. **Đánh giá tính khả thi thực tế:** do độ trễ giữa các lượt tương tác trong hội thoại (Claude gửi lệnh → người đọc/gõ → phản hồi), khả năng cao tổng thời gian vượt quá 60 giây chỉ vì độ trễ trao đổi, chưa tính thời gian gõ password thật. Nếu muốn thử, cần người dùng đã sẵn sàng gõ ngay khi phiên vừa mở, không chờ Claude nhắc lại — nếu vẫn không kịp, dừng và ghi Blocked, không lặp lại nhiều lần (tránh tốn thêm phiên trial vô ích).

### Actor model: Planned vs Actual Execution Mode (không đổi khái niệm, cập nhật danh sách run)

3 giá trị: `AI-executed` · `AI-executed with human checkpoints` · `Human-executed with AI guidance`. Ghi ở cấp cell, Planned trước khi chạy, Actual sau khi chạy thật.

**Planned Execution Mode — cập nhật ở v7 (thêm Run G, đánh dấu D/E là Blocked không phải Planned-to-execute):**

| Run | Môi trường | Trạng thái | Planned Execution Mode | Vì sao |
| --- | --- | --- | --- | --- |
| A | Chrome / Windows local | **Executed** | AI-executed with human checkpoints | Cần người login 1 lần trước; sau đó Claude điều hướng qua No-DOM Policy |
| B | Firefox / Windows local | **Executed** | Human-executed with AI guidance | Claude in Chrome không điều khiển được Firefox |
| C | Opera / Windows local | **Executed** | Human-executed with AI guidance | nt, Opera |
| G | **Edge / Windows local (mới ở v7)** | **Executed** | Human-executed with AI guidance | Thay thế vai trò của Edge từ cell cloud (Run E) đã Blocked — đảm bảo vẫn đủ 5 browser phân biệt trong phần Executed |
| F | Safari / iPhone thật (vật lý) | **Executed** | Human-executed with AI guidance | Thiết bị vật lý, không có giao diện phần mềm để Claude thao tác |
| D | Safari / macOS, BrowserStack cloud desktop | **Blocked** | ~~AI-executed with human checkpoints~~ | Pilot 2026-08-03: Free Trial 1 phút/phiên, không đủ để login+điều hướng+capture. Evidence: `browserstack-1min-trial-limit-banner.jpg` |
| E | */ iOS Tablet, BrowserStack real device | **Blocked** | ~~AI-executed with human checkpoints~~ | Cùng root cause với Run D (giới hạn provider), không cần lặp lại thử nghiệm riêng để chứng minh lại — dùng chung evidence, ghi rõ lý do suy luận từ cùng 1 root cause |

**Quy tắc:** Report chỉ thống kê Actual của cell **Executed**. Cell Blocked không có Actual Execution Mode (vì chưa chạy) — chỉ ghi "Blocked, lý do X, evidence Y".

### Khi nào bắt buộc cần BrowserStack/cloud tool hoặc thiết bị thật (cập nhật ở v7)

- OS = macOS → **hiện Blocked**, không có máy Mac vật lý và cloud không khả thi trong khung thời gian Free Trial.
- Safari trên Windows không hợp lệ.
- Mọi cell Tablet → **hiện Blocked**, cùng lý do.
- Cell Phone/iOS → iPhone thật, **vẫn Executed bình thường** — không phụ thuộc cloud.

### Rủi ro khiến evidence không hợp lệ (không đổi từ v6, cộng thêm rủi ro mới)

- DevTools responsive mode ghi nhầm "tablet/phone thật".
- Khung BrowserStack chỉ chứng minh OS/browser/device, không chứng minh URL — **không còn áp dụng cho phần Executed** (cloud đã Blocked), giữ lại làm ghi chú lịch sử.
- Overlay bị che nội dung trang.
- **(Mới)** Blocked cell bị âm thầm bỏ qua, không ghi vào report/manifest → bắt buộc xuất hiện trong DoD (Section K).
- **(Mới)** Cố lặp lại nhiều lần thử cloud, tốn thời gian/phiên trial vô ích thay vì chấp nhận Blocked → giới hạn "workaround cuối" thử tối đa 1 lần thêm, không lặp vô hạn.

---

## C. Proposed execution architecture (cập nhật layer 3/4 để phản ánh bước đăng nhập)

| Lớp | Input | Output | Trách nhiệm AI | Trách nhiệm người |
| --- | --- | --- | --- | --- |
| 0. Login setup (mới ở v7) | Chưa đăng nhập | Session đã đăng nhập, giữ qua cookie | Không nhập password ở bất kỳ đâu; chờ người xác nhận đã đăng nhập | Tự đăng nhập 1 lần/browser/thiết bị (Chrome, Firefox, Opera, Edge, iPhone Safari) |
| 1. Requirement layer | §6 Task 3 | Diễn giải đã đóng băng (Section A) | Trích dẫn đúng | Xác nhận đúng ý đề |
| 2. Test manifest | Section A + D | Manifest 28 dòng (20 Executed target + 8 Blocked) | Soạn draft, đã tạo `compatibility-manifest-working.md` | Duyệt/sửa |
| 3. Manual/AI execution | Manifest (Planned Mode/cell, chỉ áp dụng cell Executed) | Trạng thái UI quan sát + Actual Mode | Theo Planned mode, thao tác qua visible UI; dừng khi gặp trở ngại | Sẵn sàng tiếp quản; tự thao tác cell Human-executed |
| 4. Evidence capture | Trạng thái UI ổn định | Raw → `annotated-candidates/` | Chụp raw (nếu là actor); quan sát ảnh để tự đánh giá ổn định | Luôn thực hiện annotation trên copy |
| 5. Human review + approval | Ảnh + quan sát thực tế | Pass/Fail (cell Executed) hoặc Blocked-note (cell cloud) | Đề xuất verdict/severity kèm bằng chứng | Quyết định cuối; approve promotion |
| 6–9 | (không đổi từ v6) | | | |
| 10. Task 3 completeness validation | Manifest + evidence + **Blocked evidence** + report | Báo cáo đủ/thiếu theo Task 3 Execution Done (Section K) | Chạy checklist, gồm kiểm tra Blocked có đủ evidence | Xác nhận Task 3 hoàn chỉnh dưới Coverage Fallback Strategy |

---

## D. Compatibility matrix strategy — Coverage Fallback Strategy áp dụng

**Bộ giá trị cố định (lý tưởng theo đề, không đổi):** OS: Windows, macOS, iOS · Browser: Chrome, Firefox, Opera, Safari, Edge · Device: Desktop, Tablet, Phone.

### Bảng 7 dòng/screen — 5 Executed + 2 Blocked (tổng 28 dòng, 20 Executed + 8 Blocked)

| Run | Screen | OS | Browser | Device | Tool / môi trường | Trạng thái | Pass/Fail criteria |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | C_x | Windows | Chrome | Desktop | Máy Windows hiện tại | **Executed** | Mini-checklist theo screen × device |
| B | C_x | Windows | Firefox | Desktop | Máy Windows hiện tại | **Executed** | nt |
| C | C_x | Windows | Opera | Desktop | Máy Windows hiện tại | **Executed** | nt |
| G | C_x | Windows | Edge | Desktop | Máy Windows hiện tại | **Executed** | nt |
| F | C_x | iOS | Safari | Phone | iPhone thật (sở hữu) | **Executed** | nt |
| D | C_x | macOS | Safari | Desktop | BrowserStack Live | **Blocked** | Không áp dụng — evidence blocker thay cho verdict |
| E | C_x | iOS | (chưa chốt) | Tablet | BrowserStack Real Device Cloud | **Blocked** | nt |

**Coverage của phần Executed (5 run × 4 screen = 20 cell):** OS {Windows: A/B/C/G, iOS: F} = 2/3 ✓~ (thiếu macOS) · Browser {Chrome, Firefox, Opera, Edge, Safari} = 5/5 phân biệt ✓ (đủ) · Device {Desktop: A/B/C/G, Phone: F} = 2/3 ✓~ (thiếu Tablet).

**Requirement gap tường minh (không né tránh):** phần Executed đạt đủ **5/5 browser**, nhưng chỉ **2/3 OS** (thiếu macOS) và **2/3 device class** (thiếu Tablet) — đúng theo đề bài §6 vẫn cần 3/3/3 cho từng screen. Đây là gap thật, ghi rõ trong report (Section I), không che giấu.

### Ràng buộc 5 browser trong phần Executed — vẫn giữ nguyên tắc không hạ thấp

Phần Executed đã tự nhiên đủ 5 browser phân biệt (Chrome/Firefox/Opera/Edge/Safari) nhờ thêm Run G — không cần phương án dự phòng nào ở đây. Ràng buộc "không chấp nhận 4 browser" (từ các bản trước) không áp dụng cho phần Executed vì đã đủ 5; nó chỉ còn ý nghĩa lịch sử cho lý do vì sao thêm Run G.

### Quy ước tên file (không đổi, Run G dùng cùng convention)

```
T3_<screen>_Run<run-id>_<OS>_<browser>_<device>_raw.png
T3_<screen>_Run<run-id>_<OS>_<browser>_<device>.png
```

Run D/E (Blocked) không có screenshot cell theo tên này — evidence của chúng là evidence blocker dùng chung (`browserstack-1min-trial-limit-banner.jpg`), không phải 1 ảnh/cell.

### Test Data Strategy (cập nhật ở v8 — trình tự "Dialog-only trước, Full confirm flow sau cùng")

1. Disposable test user `test abc` — **đã xác nhận còn tồn tại** qua Bước 1.
2. C3 luôn chạy cuối cùng trong mỗi run Executed.
3. **Trình tự Interaction Coverage của C3 (sửa ở v8, quyết định 2026-08-03 khi chạy thật Run A):**
   - **Tất cả 5 run (A, B, C, G, F) chạy C3 ở phạm vi `Dialog-only` trước** — mở dialog, kiểm render/text/button/close behavior, đóng bằng Cancel, **không bấm Confirm**. Điều này giữ nguyên `test abc` để mọi browser dùng chung, tránh phải tạo lại disposable user giữa chừng.
   - **Chỉ sau khi cả 5 run đã hoàn tất C3 Dialog-only**, mới quay lại Chrome/Windows (Run A) làm bước riêng **"C3 Full Confirm Final Validation"**: xin xác nhận người dùng → bấm Confirm thật → chụp supplementary evidence trạng thái sau xoá → cập nhật Interaction Coverage của Run A/C3 từ `Dialog-only` thành `Full confirm flow`.
   - Lý do đổi từ bản trước (Full confirm flow làm ngay trong Run A): nếu xoá `test abc` sớm, các browser B/C/G/F chạy sau sẽ không còn user disposable để mở dialog C3 — phải tạo lại, tốn công và có thể gặp lại blocker "EMS bắt buộc field Password khi tạo user mới" đã ghi nhận ở Task 1.
4. Downgrade chain (nếu disposable user biến mất giữa chừng trước khi tới bước Final Validation) không đổi từ v6: thử tạo mới → thử user hiện có → ghi blocker → lưu evidence → downgrade toàn bộ C3 về Dialog-only vĩnh viễn nếu không cứu được.
5. **Không xoá disposable user trước khi toàn bộ Run B/C/G/F đã dùng nó xong cho C3 Dialog-only.**

### Quy trình evidence thống nhất (cập nhật ở v8 — thêm kỹ thuật capture đã xác minh thực tế)

raw → `annotated-candidates/` → annotation → Skill 2 check → human review → promote `out/evidence/`.

**Kỹ thuật capture cho local run (A/B/C/G) — đã xác minh khi chạy Run A thật, 2026-08-03:**
1. Mỗi browser giữ EMS trong **cửa sổ riêng, chỉ 1 tab** (không chung cửa sổ với các tab khác) — bắt buộc, vì phát hiện sự cố thật: cùng 1 cửa sổ nhiều tab, tab active có thể đổi bất cứ lúc nào ngoài tầm kiểm soát, khiến ảnh chụp sai hoàn toàn (đã xảy ra ở C2, Run A — chụp trúng cửa sổ ChatGPT).
2. Trước mỗi lần chụp OS-level screenshot: foreground cửa sổ mục tiêu, sau đó **verify `GetForegroundWindow()` title thực sự chứa `Admin Management | HCMUS EMS`** trước khi capture. Nếu không khớp: **không chụp, không ghi đè raw cũ**, coi là lỗi cần xử lý lại (không phải Fail của EMS).
3. Annotation qua overlay được thực hiện bằng script (PowerShell + System.Drawing) thay vì bắt người dùng tự mở photo editor cho từng ảnh — người vẫn review/duyệt ảnh annotated trước khi promote, giữ đúng nguyên tắc "human approval trước promotion" (không đổi tinh thần, chỉ đổi công cụ thực hiện việc vẽ overlay).
4. Toạ độ click qua Claude in Chrome (`computer` tool) dùng hệ toạ độ viewport của tab, **khác** với hệ toạ độ ảnh OS-level full-screen — không được trộn lẫn 2 hệ toạ độ (đã gây lỗi click nhầm 1 lần ở Run A).

### Mini Pass/Fail checklist theo từng screen × device class (không đổi từ v6, chỉ áp dụng Desktop/Phone vì Tablet Blocked)

| Screen | Desktop | Phone |
| --- | --- | --- |
| **C1 — Users list** | Bảng không mất cột; horizontal scroll nếu tràn; search/filter dùng được; sidebar không đè nội dung | Bảng dùng được ở dạng list/card nếu responsive; tap target đủ lớn |
| **C2 — Edit User dialog** | Dialog trọn viewport; dropdown Role click được; Save/Cancel bấm được; đóng bằng ESC | Dialog không tràn màn hình; keyboard không che field; đóng bằng Cancel hoặc Back gesture |
| **C3 — Delete User confirm dialog** | Dialog-only mọi cell: overflow, cảnh báo đọc được, Cancel/Confirm bấm được, ESC. Full confirm flow (Run A): xoá thành công | Dialog-only: đọc được trên màn hình nhỏ, đóng bằng Cancel/Back gesture |
| **C4 — Export to Excel** | Nút Export bấm được; phản hồi rõ; file ở download bar/Downloads | Nếu mobile OS chặn download, ghi nhận là hành vi hệ điều hành |

Cột Tablet bỏ khỏi bảng này vì Blocked — không có mini-checklist áp dụng cho cell chưa chạy.

---

## E. Pilot strategy — đã kết luận (mới ở v7)

**Pilot Run D (Safari/macOS/BrowserStack, cell C1) đã thực hiện 2026-08-03.** Kết quả:
- ✅ Xác nhận tích cực: remote session hiển thị browser chrome thật đầy đủ (address bar, tab bar) — nếu không bị giới hạn thời gian, phương án evidence 1-ảnh sẽ khả thi.
- ✅ Xác nhận: EMS load đúng, redirect `/login` đúng hành vi khi chưa auth.
- ❌ **Blocker xác nhận:** Free Trial giới hạn cứng 1 phút/phiên, tự động đóng session — không đủ để hoàn thành login + điều hướng + capture. Evidence: `setup-evidence/browserstack-1min-trial-limit-banner.jpg`.
- ❌ Không thể tiếp tục theo actor model gốc vì Claude không được nhập password, và trong 60 giây việc bàn giao người dùng gõ password gần như không kịp do độ trễ trao đổi qua lại giữa các lượt hội thoại.

**Quyết định:** không tiếp tục pilot Run E (tablet cloud) riêng — root cause giống Run D (giới hạn provider), tiếp tục thử sẽ tốn thêm phiên trial mà không mang lại thông tin mới. Run D và Run E chuyển thẳng sang trạng thái **Blocked**, dùng chung 1 evidence blocker, theo đúng Coverage Fallback Strategy (Section D/B).

**Pilot Run F (iPhone thật)** không cần vì đã xác nhận tính khả thi từ nguyên tắc (thiết bị vật lý, không phụ thuộc hạ tầng thứ ba) — sẽ chạy trực tiếp ở Bước 5 như 1 run bình thường, cùng Run A/B/C/G.

**Điều kiện chuyển sang build skill (đã đạt):** đã biết rõ 5 run Executed + 2 run Blocked; manifest đã phản ánh đúng; không cần pilot thêm.

---

## F. Agent Skill strategy (2 skill, không đổi từ v6, chỉ cập nhật phạm vi dữ liệu)

Skill 1 (`compat-run-planner`) và Skill 2 (`compat-evidence-report`) quản lý **28 dòng** manifest (20 Executed + 8 Blocked), không chỉ 24. Với dòng Blocked, Skill 1 không đánh dấu "done" theo nghĩa raw/candidate/promoted — mà đánh dấu "Blocked, có evidence" hoặc "Blocked, thiếu evidence" (cảnh báo nếu thiếu). Skill 2 khi dựng report phải tách rõ 3 nhóm số liệu: Executed (Pass/Fail), Blocked (không verdict), Requirement gap (OS/device còn thiếu so với đề). Các quy tắc khác (không ghi vào `out/` trực tiếp, không tự chốt verdict, không tự severity mà không có bằng chứng) giữ nguyên.

---

## G. Step-by-step execution plan (cập nhật thứ tự — ưu tiên Executed, Blocked đã kết luận)

### Bước 1 — Chuẩn bị (đã hoàn thành phần lớn 2026-08-03)

- ✅ BrowserStack: đăng nhập, nhưng xác nhận Free Trial giới hạn 1 phút — **dẫn tới quyết định Blocked cho D/E, không phải blocker cần giải quyết tiếp trước khi làm Bước 2+.**
- ✅ Firefox cài sẵn. ⏳ Opera đang tự cài (người dùng).
- ✅ Disposable user `test abc` còn tồn tại.
- ✅ Overlay email chốt: `23127179@student.hcmus.edu.vn`.
- **Mới, cần làm tiếp:** người dùng tự đăng nhập EMS admin **1 lần trong mỗi browser sẽ dùng cho phần Executed** — Chrome (cửa sổ đang kết nối Claude in Chrome), Firefox, Opera, Edge, và Safari trên iPhone. Đây là điều kiện tiên quyết trước khi chạy bất kỳ run Executed nào (kể cả Run A).
- **Git commit gợi ý:** `Step 1 (Task 3): confirm accounts/tools; discover BrowserStack 1-minute trial blocker`.

### Bước 1b — Kết luận Coverage Fallback (mới, đã thực hiện qua pilot Run D)

- **Hành động:** ghi nhận blocker, chuyển D/E sang Blocked, cập nhật manifest (28 dòng), cập nhật plan (văn bản này).
- **Evidence:** `setup-evidence/browserstack-1min-trial-limit-banner.jpg` + `setup-evidence/step1-checks.md`.
- **Git commit gợi ý:** `Step 1b (Task 3): pilot run D confirms cloud trial blocker; adopt coverage fallback strategy (20 executed / 8 blocked)`.

### Bước 2 — Manifest (đã tạo, 2026-08-03)

- `compatibility-manifest-working.md` — cần cập nhật lại theo cấu trúc 28 dòng (5 Executed run × 4 screen + 2 Blocked run × 4 screen), thay cho bản 24-dòng cũ.
- **Git commit gợi ý:** `Step 2 (Task 3): update working manifest to 28-row coverage-fallback structure`.

### Bước 3 — ~~Pilot~~ đã kết luận (xem Section E) — không còn bước riêng

### Bước 4 — Build 2 skill (không đổi thời điểm — sau khi cấu trúc manifest ổn định, tức là bây giờ)

### Bước 4b — Demo video (không đổi)

### Bước 5 — Chạy 5 run Executed (A, B, C, G, F) × 4 screen = 20 cell

- **Điều kiện tiên quyết:** người dùng đã đăng nhập từng browser/thiết bị (Bước 1).
- **Hành động:** mỗi run chạy trọn C1→C2→C4→C3 (C3 cuối cùng, Test Data Strategy); raw → annotated-candidates → review → promote.
- **Git commit gợi ý (1 commit/run hoàn tất):**
  - `Step 5.1 (Task 3): run A (Chrome/Windows) — C1–C4 done + promoted`
  - `Step 5.2 (Task 3): run B (Firefox/Windows) — C1–C4 done + promoted`
  - `Step 5.3 (Task 3): run C (Opera/Windows) — C1–C4 done + promoted`
  - `Step 5.4 (Task 3): run G (Edge/Windows) — C1–C4 done + promoted`
  - `Step 5.5 (Task 3): run F (Safari/iPhone) — C1–C4 done + promoted`

### Bước 6 — Đồng bộ findings (không đổi, chỉ từ cell Executed)

### Bước 7 — Đóng băng matrix + promote report + promote skills

- **Report phải tách 3 phần:** Executed coverage (20 cell, Pass/Fail thật) / Blocked coverage (8 cell, evidence + lý do) / Requirement gap (OS macOS thiếu, device Tablet thiếu — nêu rõ residual risk).

### Bước 7b, Bước 8 — không đổi (Final Submission Integration / AI Audit+Critique)

---

## H. Artifact plan (không đổi cấu trúc thư mục, chỉ đổi nội dung manifest/report bên trong)

Giữ nguyên cây thư mục từ v6 (`hw3/work/task-3-cross-platform/{...}`, `hw3/out/reports/task-3-cross-platform/{...}`, `hw3/out/agent-skills/`). Thêm 1 file mới: `setup-evidence/browserstack-1min-trial-limit-banner.jpg` (đã lưu) và `setup-evidence/step1-checks.md` (đã lưu).

---

## I. Report automation strategy (cập nhật cấu trúc report — Executed/Blocked/Requirement gap)

Report Task 3 (`report.md`) bắt buộc có 3 phần tách biệt:

1. **Executed coverage:** bảng 20 cell, Pass/Fail thật, mini-checklist theo device, Interaction Coverage của C3.
2. **Blocked coverage:** bảng 8 cell (Run D, E × 4 screen), lý do (BrowserStack Free Trial 1 phút/phiên), evidence đính kèm, ngày thử, kết luận không tiếp tục thử thêm (hoặc có thử LambdaTest nếu làm).
3. **Requirement gap:** nêu thẳng đề bài yêu cầu 3 OS/3 device class mỗi screen, phần Executed chỉ đạt 2/3 mỗi loại (thiếu macOS, thiếu Tablet), rủi ro còn lại (residual risk) là gì (ví dụ: chưa biết EMS render thế nào trên macOS Safari thật hay trên tablet thật).

Câu kết luận mẫu (người viết lại theo giọng riêng, không copy nguyên AI draft):
> "I did not claim unexecuted environments as Pass or Fail. I tested every environment physically available to me, documented the cloud-trial limitation with evidence, and reported the remaining compatibility risk transparently."

**Bắt buộc người tự quyết định cuối:** severity, ý nghĩa defect, nội dung phần Requirement gap (đây là nhận định rủi ro, không phải số liệu tự động), lời văn Critique, kết luận report.

---

## J. Risk and anti-cheat controls (cập nhật — thêm risk Coverage Fallback)

| Rủi ro | Biện pháp kiểm soát |
| --- | --- |
| (các rủi ro từ v6 về overlay, DOM, Run ID, Test Data Strategy... không đổi) | (không đổi) |
| **Cell Blocked bị âm thầm bỏ qua, không xuất hiện trong report/manifest** | Bắt buộc trong DoD (Section K); Skill 1/2 phải liệt kê rõ 8 dòng Blocked, không được xoá khỏi manifest |
| **Coverage Fallback bị hiểu nhầm là "đã đủ 24/24"** | Report Section I bắt buộc nêu Requirement gap tường minh, không che giấu thiếu OS/device |
| **Lặp lại thử cloud nhiều lần, tốn phiên trial vô ích** | Section E giới hạn: đã kết luận Blocked sau 1 lần pilot thật + đánh giá root cause, không lặp vô hạn; "workaround cuối" (nếu làm) giới hạn 1 lần |
| **Claude tự nhập password để "tiện" bỏ qua bước người đăng nhập** | Cấm tuyệt đối ở mọi môi trường (Section B) — kể cả khi có password trong tài liệu công khai của đề bài |
| **Dùng DevTools giả lập tablet để lấp Blocked** | Cấm tuyệt đối, không đổi từ các bản trước |

---

## K. Definition of Done — cập nhật theo Coverage Fallback Strategy

### K1. Task 3 Execution Done (độc lập, không phụ thuộc Task 2)

- [ ] `compatibility-manifest-working.md` đủ 28 dòng (20 Executed target + 8 Blocked), Run ID, Planned/Actual Mode (chỉ cell Executed).
- [ ] **20 cell Executed** có đủ raw → annotated-candidate → final, truy ngược 1-1.
- [ ] **8 cell Blocked** có evidence blocker (screenshot + ghi chú), không có Pass/Fail, không giả lập.
- [ ] Phần Executed đủ 5/5 browser phân biệt cho mỗi screen.
- [ ] Không có cell nào dùng DevTools responsive mode/emulator nhưng ghi "real device".
- [ ] Không có DOM/JS/console/network tool nào dùng để thực thi test hoặc quyết định verdict; không có password nào được Claude tự nhập ở bất kỳ môi trường nào.
- [ ] Test Data Strategy tuân thủ cho C3 trong phần Executed; Interaction Coverage (Dialog-only/Full confirm flow) ghi rõ.
- [ ] `annotated-candidates/` dùng làm staging; Skill 2 không đọc `out/evidence/` làm nguồn.
- [ ] Mini-checklist áp dụng theo device (Desktop/Phone — Tablet không áp dụng vì Blocked).
- [ ] Mọi Pass/Fail (cell Executed) đã người xác nhận trực tiếp.
- [ ] Mọi cell Fail có defect note.
- [ ] Toàn bộ finding thật (từ cell Executed) đã submit Google Form và merge vào `hw3/work/findings-log.md`.
- [ ] `compatibility-matrix.md` (out) sinh từ manifest 28 dòng đã ổn định + human approval, **có ghi rõ 20 Executed / 8 Blocked, không trình bày như 28 cell ngang hàng.**
- [ ] `report.md` (out) có đủ 3 phần: Executed coverage / Blocked coverage / Requirement gap.
- [ ] Hai Agent Skills có bản final trong `hw3/out/agent-skills/`.
- [ ] Demo video đã quay, upload, có URL.
- [ ] AI Audit có entry cho phiên pilot dẫn tới quyết định Blocked (không chỉ artifact có file).
- [ ] Không có working artifact/draft nào nằm trong `hw3/out/reports/task-3-cross-platform/`, trừ khi report trích dẫn phần cần thiết.

### K2. Final Submission Integration Done (không đổi từ v6 — phụ thuộc Task 1/2)

(giữ nguyên nội dung v6: Main Report MD/PDF, Findings Log final, README, git commit log, AI Critique cuối, ZIP nộp)

**Lưu ý quan trọng cho oral defense:** Task 3 dưới Coverage Fallback Strategy **không đạt đủ nghĩa đen của §6** (3 OS × 3 device class/screen) — điều này đã nói rõ trong report, không che giấu. K1 đạt đủ nghĩa là "đã làm hết khả năng thật có, có evidence, không fabricate" — không đồng nghĩa "đạt 100% yêu cầu coverage của đề."

---

## Điểm cần người dùng xác nhận / hành động tiếp theo

1. **Opera:** đang tự cài — báo khi xong để chạy Run C.
2. **Đăng nhập EMS admin 1 lần/browser:** cần làm trước khi chạy bất kỳ run Executed nào — Chrome, Firefox, Opera, Edge (khi cài xong), Safari trên iPhone.
3. **Cell nào chạy Full confirm flow cho C3:** đề xuất Run A.
4. **Có muốn thử LambdaTest** như 1 phương án cloud khác trước khi chấp nhận Blocked hẳn, hay chấp nhận luôn Coverage Fallback Strategy và tập trung chạy 20 cell Executed?
5. **Path Main Report MD/PDF:** thuộc Final Submission Integration, xác nhận sau khi Task 2 xong.

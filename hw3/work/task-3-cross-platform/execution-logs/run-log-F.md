# Run Log — Run F (Safari / iOS / Phone — iPhone thật)

**Ngày:** 2026-08-03
**Actor:** Người dùng thao tác trực tiếp trên iPhone thật (Human-executed with AI guidance). Kết nối qua Claude remote-control (không phải màn hình mirror trên PC) — người dùng chụp ảnh trên điện thoại và gửi trực tiếp cho Claude xử lý overlay.
**Điều kiện tiên quyết:** Safari trên iPhone đã đăng nhập admin từ trước, đang ở đúng URL EMS.

| Screen | Actual Execution Mode | Verdict | Hành động thật đã kiểm | Ghi chú |
|--------|------------------------|---------|-------------------------|---------|
| C1 — Users Management | Human-executed with AI guidance | **FAIL** | Quan sát trạng thái mặc định (sidebar mở, che nội dung) → thử cuộn ngang (workaround) → thử thu gọn sidebar về icon-only (vẫn tràn) | **Finding F-022 (draft)**, severity 2 — người dùng đã xác nhận. Xem `findings-drafts/F-022-draft.md`. 3 ảnh evidence: primary (mặc định) + supp1 (sau cuộn ngang) + supp2 (sau thu gọn sidebar, vẫn Fail) |
| C2 — Edit User dialog | Human-executed with AI guidance | **Pass (render + behavior verified)** | Native Role picker (iOS select UI) Guest→Lecturer→Guest; checkbox Active tick/bỏ tick; Cancel không lưu | **Đối lập rõ với C1:** dialog modal render đúng, không tràn, khác hẳn vấn đề layout của trang list C1 — cho thấy vấn đề C1 là riêng của layout list+sidebar, không phải lỗi toàn hệ thống trên mobile |
| C4 — Export to Excel | Human-executed with AI guidance | **Pass (download xác nhận qua Safari Downloads panel)** | Bấm Export → Safari tự mở panel Downloads native hiện file `users-export-178576249....xlsx` (16 KB) | **Ngoại lệ evidence đã ghi nhận minh bạch:** ảnh chính không thấy thanh địa chỉ (bị panel Downloads che) — theo yêu cầu người dùng, chấp nhận không cần ảnh companion có URL; URL củng cố gián tiếp qua ảnh C1/C2 cùng phiên (cùng search "abcdefabc", cùng ngày 2026-08-03) |
| C3 — Delete User confirm dialog | Human-executed with AI guidance | **Dialog-only: Pass** | Mở dialog, đọc cảnh báo, đóng bằng Cancel — không bấm Confirm | Render đúng, URL rõ, kèm icon download xanh trên thanh địa chỉ (dấu vết từ C4 vừa chạy trước đó — củng cố thêm tính liên tục của phiên) |

## Chi tiết phát hiện Fail

Trên viewport phone (828×1792, Safari/iOS), trang C1 mặc định load với sidebar mở toàn bộ, che gần hết nội dung chính. Ngay cả sau khi thu gọn sidebar về dạng icon-only (cách hợp lý nhất người dùng thật sẽ làm), nội dung chính (tiêu đề, nút Export, bảng, cột ACTIONS) vẫn tràn khỏi mép phải viewport, buộc phải cuộn ngang. Đây là lỗi responsive layout thật, không phải do thao tác sai — đã xác minh qua đúng quy trình Fail protocol: dừng lại, thu thập đủ raw + supplementary evidence, phân tích, đề xuất severity, chờ người dùng xác nhận trước khi ghi nhận chính thức.

**Do phát hiện Fail, thứ tự Run F tạm dừng ở C1** để xử lý finding trước khi tiếp tục C2/C4/C3, theo đúng rule "phát hiện Fail → dừng đúng tại cell đó, không promote (cho tới khi xác nhận), chờ quyết định."

## Kết quả cuối Run F

- **4/4 screen đã chạy:** C1 = FAIL (F-022, severity 2), C2 = Pass, C4 = Pass (ngoại lệ evidence đã ghi nhận), C3 = Dialog-only Pass.
- **`test abc` xác nhận còn nguyên vẹn** sau toàn bộ Run F — sẵn sàng cho bước "C3 Full Confirm Final Validation" (Chrome/Run A) vì tất cả 5 run (A, B, C, G, F) đã hoàn tất C3 Dialog-only.

## Việc còn lại

- Người dùng submit F-022 lên Google Form + merge vào `hw3/work/findings-log.md`.
- Tiến hành **C3 Full Confirm Final Validation** trên Chrome (Run A) khi người dùng sẵn sàng.

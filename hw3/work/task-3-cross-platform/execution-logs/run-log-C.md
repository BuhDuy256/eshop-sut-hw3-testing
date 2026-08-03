# Run Log — Run C (Opera / Windows / Desktop)

**Ngày:** 2026-08-03
**Actor:** Người dùng thao tác trực tiếp trong Opera (Human-executed with AI guidance).
**Điều kiện tiên quyết:** cửa sổ Opera riêng, 1 tab EMS, handle `265052`, title `Admin Management | HCMUS EMS - Opera`, đã đăng nhập admin từ trước. Xác nhận qua PowerShell atomic verify trước khi bắt đầu.

| Screen | Actual Execution Mode | Verdict | Hành động thật đã kiểm | Ghi chú |
|--------|------------------------|---------|-------------------------|---------|
| C1 — Users Management | Human-executed with AI guidance | **Pass (render + behavior verified)** | Gõ `abcdefabc` → lọc còn 1 kết quả → xoá → phục hồi danh sách | Ảnh chính chụp ở trạng thái đang filter (test abc), thể hiện luôn search hoạt động |
| C2 — Edit User dialog | Human-executed with AI guidance | **Pass (render + behavior verified)** | Dropdown Role Guest→Lecturer→Guest; checkbox Active tick/bỏ tick; đóng bằng Cancel | Ảnh chính chụp lúc Active đã tick — bằng chứng thao tác thật |
| C4 — Export to Excel | Human-executed with AI guidance | **Pass (download độc lập xác nhận)** | Bấm Export → download panel hiện rồi tự ẩn khi click chỗ khác (hành vi giống Chrome/Firefox) → **xác minh filesystem:** `users-export-1785756215884.xlsx` (16272 bytes) tồn tại thật, mtime khớp | Người dùng mô tả đúng: panel tự hide khi click nơi khác — không coi đây là bug, hành vi UX chuẩn của browser |
| C3 — Delete User confirm dialog | Human-executed with AI guidance | **Dialog-only: Pass** | Mở dialog, đọc cảnh báo, đóng bằng Cancel — không bấm Confirm | Giữ `test abc` cho Run G/F |

## Sự cố kỹ thuật

**Lần thử capture C2 đầu tiên bị chặn đúng:** verify title trước khi chụp phát hiện foreground đang là cửa sổ terminal (không phải Opera) — hàm đã **từ chối chụp, không ghi đè raw**, đúng thiết kế. Thử lại (thêm thời gian settle + retry loop 3 lần) thành công ở lần thử thứ 2. Không có ảnh sai nào được tạo ra hay promote — an toàn.

## Kết quả

- **4/4 screen Pass** (C1, C2, C4 đầy đủ render+behavior; C3 Dialog-only Pass).
- **Không có Fail nào ở Run C.**
- **Không phát hiện khác biệt so với Chrome/Firefox** — Opera render và hành xử tương đương.
- **`test abc` xác nhận còn nguyên vẹn** — sẵn sàng cho Run G (Edge).

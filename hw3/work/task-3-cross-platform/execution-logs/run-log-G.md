# Run Log — Run G (Edge / Windows / Desktop)

**Ngày:** 2026-08-03
**Actor:** Người dùng thao tác trực tiếp trong Edge (Human-executed with AI guidance).
**Điều kiện tiên quyết:** cửa sổ Edge riêng, 1 tab EMS, handle `2951668`, title chứa `Admin Management | HCMUS EMS`, đã đăng nhập admin từ trước.

| Screen | Actual Execution Mode | Verdict | Hành động thật đã kiểm | Ghi chú |
|--------|------------------------|---------|-------------------------|---------|
| C1 — Users Management | Human-executed with AI guidance | **Pass (render + behavior verified)** | Search `abcdefabc` → lọc 1 kết quả → xoá → phục hồi danh sách | |
| C2 — Edit User dialog | Human-executed with AI guidance | **Pass (render + behavior verified)** | Dropdown Role Guest→Lecturer→Guest; checkbox Active tick/bỏ tick; đóng bằng Cancel | |
| C4 — Export to Excel | Human-executed with AI guidance | **Pass (download độc lập xác nhận)** | Bấm Export, hiệu ứng tương tự browser khác → **xác minh filesystem:** `users-export-1785757456182.xlsx` (16422 bytes) tồn tại thật, mtime khớp | |
| C3 — Delete User confirm dialog | Human-executed with AI guidance | **Dialog-only: Pass** | Mở dialog, đọc cảnh báo, đóng bằng Cancel — không bấm Confirm | |

## Sự cố kỹ thuật

- **Capture timing:** một số lần chụp cần thời gian settle dài hơn (1.5s + 0.7s thay vì 0.7s+0.3s) vì foreground window đôi khi bị terminal giành lại — hàm verify-trước/sau đã chặn đúng các lần không khớp, không có ảnh sai nào lọt qua.
- **Lệnh copy C3 bị timeout hiển thị (>120s)** nhưng thực thi thành công ở background (xác nhận qua kiểm tra file đích tồn tại đúng kích thước). Không phải lỗi dữ liệu, chỉ là độ trễ hiển thị của tool.

## Kết quả

- **4/4 screen Pass** (C1, C2, C4 đầy đủ render+behavior; C3 Dialog-only Pass).
- **Không có Fail nào ở Run G.**
- **Không phát hiện khác biệt so với Chrome/Firefox/Opera.**
- **`test abc` cần xác nhận lại còn nguyên vẹn** trước khi chuyển sang Run F (iPhone).

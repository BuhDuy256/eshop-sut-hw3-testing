# Run Log — Run B (Firefox / Windows / Desktop)

**Ngày:** 2026-08-03
**Actor:** Người dùng thao tác trực tiếp trong Firefox (Human-executed with AI guidance) — Claude không điều khiển được Firefox, chỉ dẫn từng bước nhỏ, tự lo phần capture (PowerShell, verify-before/after title) + overlay + completeness check + promotion.
**Điều kiện tiên quyết:** cửa sổ Firefox riêng, chỉ 1 tab EMS, handle `723490`, title `Admin Management | HCMUS EMS — Mozilla Firefox`, đã đăng nhập admin từ trước. Xác nhận qua PowerShell trước khi bắt đầu (đủ 5 điều kiện: tồn tại, đúng title, 1 tab, đã login, foreground/maximize ổn định).

| Screen | Actual Execution Mode | Verdict | Hành động thật đã kiểm | Ghi chú |
|--------|------------------------|---------|-------------------------|---------|
| C1 — Users Management | Human-executed with AI guidance | **Pass (render + behavior verified)** | Gõ `abcdefabc` → lọc còn 1 kết quả (`test abc`) → xoá search → danh sách phục hồi 132 kết quả/27 trang | Tổng số user tăng 131→132 (user mới `Lê văn Hùng` xuất hiện) — biến động dữ liệu EMS trong phiên, đúng cảnh báo §4 đề bài, không phải bug |
| C2 — Edit User dialog | Human-executed with AI guidance | **Pass (render + behavior verified)** | Dropdown Role đổi `Guest → Lecturer` rồi trả về `Guest`; checkbox Active tick rồi bỏ tick; đóng bằng Cancel | Ảnh chính chụp ở trạng thái Active đã tick (bằng chứng thao tác thật), Role đã trả về Guest trước khi chụp. Dữ liệu `test abc` không đổi sau Cancel |
| C4 — Export to Excel | Human-executed with AI guidance | **Pass (download độc lập xác nhận)** | Bấm Export → icon download sáng → **xác minh qua filesystem:** `users-export-1785755194928.xlsx` (16192 bytes) thực sự có trong Downloads, mtime khớp thời điểm bấm | Không chỉ dựa vào icon — đã kiểm tra file thật, đúng nguyên tắc rút ra từ rà soát Run A |
| C3 — Delete User confirm dialog | Human-executed with AI guidance | **Dialog-only: Pass** | Mở dialog, đọc cảnh báo, đóng bằng Cancel — **không bấm Confirm** | Giữ `test abc` nguyên vẹn cho Run C/G/F dùng tiếp |

## Sự cố kỹ thuật

**Sự cố — precheck Firefox lần đầu bị sai window:** khi kiểm tra điều kiện trước khi bắt đầu, tách foreground+verify và bước chụp screenshot thành 2 lệnh PowerShell riêng biệt → giữa 2 lệnh, foreground đổi lại thành Chrome, ảnh chụp sai (chụp trúng Chrome thay vì Firefox). **Xử lý:** phát hiện ngay qua việc tự đọc lại ảnh trước khi dùng làm evidence; sửa hàm capture thành atomic — verify title NGAY TRƯỚC và NGAY SAU khi chụp trong cùng 1 lệnh PowerShell duy nhất, không tách rời. Áp dụng lại cho toàn bộ Run B, không tái diễn.

## Kết quả

- **4/4 screen Pass** (C1, C2, C4 đầy đủ render+behavior; C3 Dialog-only Pass).
- **Không có Fail nào ở Run B.**
- **Không phát hiện khác biệt so với Chrome (Run A)** — Firefox render và hành xử tương đương Chrome trên cả 4 screen.
- **`test abc` xác nhận còn nguyên vẹn** (Guest, Inactive, Member Code 91984123) sau khi kiểm tra lại — sẵn sàng cho Run C.

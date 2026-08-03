# Run Log — Run A (Chrome / Windows / Desktop)

**Ngày:** 2026-08-03
**Điều kiện tiên quyết:** người dùng đã đăng nhập admin (`admin@gmail.com`) trong cửa sổ Chrome riêng (1 tab, chỉ EMS), window handle `8849738`, title `Admin Management | HCMUS EMS - Google Chrome`.
**Kỹ thuật capture:** verify foreground window title chứa `Admin Management | HCMUS EMS` trước mỗi lần chụp OS-level screenshot; nếu không khớp, không chụp, không ghi đè raw cũ (phát hiện lỗi này ở lần thử đầu của C2 — xem mục "Sự cố" dưới).

| Screen | Actor | Actual Execution Mode | Verdict | Ghi chú |
|--------|-------|------------------------|---------|---------|
| C1 — Users Management | Claude (Claude in Chrome, visible UI only) | AI-executed with human checkpoints | **Pass (render + behavior verified)** | Đủ 6 cột, sidebar không đè nội dung, dữ liệu load ổn định (131 results). **Behavior đã thao tác thật (bổ sung 2026-08-03):** gõ `abcdefabc` vào Search → lọc đúng còn 1 kết quả (`test abc`) → xoá search → danh sách phục hồi đủ 131 kết quả/27 trang. Evidence: `T3_C1_RunA_Windows_Chrome_Desktop.png` (primary, trạng thái mặc định — annotated candidate đã có sẵn từ 2026-08-03 nhưng bị bỏ sót khỏi lần promote đầu tiên, bổ sung khi rà completeness cho K1) + `T3_C1_RunA_Windows_Chrome_Desktop_supp1.png` (supplementary, trạng thái đã filter). |
| C2 — Edit User dialog | Claude | AI-executed with human checkpoints | **Pass (render + behavior verified)** | Dialog trọn viewport, đủ field. **Behavior đã thao tác thật (bổ sung 2026-08-03):** dropdown Role đổi giá trị thật `Guest → Lecturer` (phím Down, không dùng DOM) rồi trả về `Guest` (phím Up); checkbox Active bấm thật (unchecked → checked), sau đó đóng bằng **Cancel** (không Save) — xác nhận lại `test abc` vẫn Guest/Inactive, không đổi. Evidence: `T3_C2_RunA_Windows_Chrome_Desktop_supp1.png` (supplementary, trạng thái dropdown=Lecturer + checkbox=checked). |
| C4 — Export to Excel | Claude | AI-executed with human checkpoints | **Pass (download độc lập xác nhận)** | Bấm Export, download icon sáng trên toolbar Chrome. **Xác minh bổ sung (2026-08-03):** kiểm tra trực tiếp thư mục Downloads bằng lệnh hệ thống — file `users-export-1785752398563.xlsx` (16028 bytes, mtime 2026-08-03 17:19) thực sự tồn tại, khớp đúng thời điểm bấm Export. Không chỉ dựa vào icon — file completion đã verify độc lập qua filesystem. EMS không hiện toast/loading riêng — nhất quán với hành vi đã ghi nhận ở Task 1, không phải bug mới. |
| C3 — Delete User confirm dialog | Claude | AI-executed with human checkpoints | **Dialog-only: Pass** (Full confirm flow: chưa thực hiện) | Dialog render đúng (cảnh báo rõ, nút Cancel/Confirm đủ lớn, style destructive đúng — nút Confirm đỏ). Đóng bằng **Cancel**, không bấm Confirm — theo quyết định 2026-08-03 hạ tạm xuống Dialog-only để giữ `test abc` cho các browser khác dùng. Full confirm flow dời sang bước "C3 Full Confirm Final Validation" riêng sau khi B/C/G/F xong. |

## Rà soát bổ sung (2026-08-03, theo yêu cầu review trước khi sang Run B)

- **C1:** ban đầu chỉ quan sát render (search box trống, không thao tác). Đã bổ sung thao tác thật: gõ/xoá search, xác nhận filter + restore hoạt động đúng. Nâng từ "Render Pass" lên "Pass (render + behavior verified)".
- **C2:** ban đầu chỉ quan sát dropdown/checkbox hiển thị, không thao tác. Đã bổ sung: đổi giá trị dropdown thật qua phím mũi tên (không dùng DOM/selector — vẫn qua visible UI, đúng No-DOM Policy), toggle checkbox thật, sau đó Cancel để không lưu thay đổi. Nâng lên "Pass (render + behavior verified)".
- **C4:** ban đầu chỉ quan sát download icon sáng lên trên toolbar, chưa xác minh file. Đã bổ sung: kiểm tra trực tiếp Downloads folder, xác nhận file `.xlsx` tồn tại thật với kích thước và mtime hợp lý. Nâng từ "Export trigger observed" lên "Pass (download độc lập xác nhận)".

## Sự cố trong quá trình chạy

**Sự cố 1 — Sai window khi chụp C2 (lần đầu):** dùng window handle cũ (132894) để foreground+capture, nhưng tab active trong cửa sổ đó đã đổi sang ChatGPT (do người dùng có nhiều tab trong cùng 1 cửa sổ Chrome). Ảnh chụp sai hoàn toàn (chụp trúng ChatGPT). **Xử lý:** phát hiện qua bước tự kiểm tra ảnh trước khi promote (không promote ảnh sai); dừng theo đúng rule "workflow cần thay đổi"; đề xuất và người dùng đồng ý tách EMS ra cửa sổ riêng (1 tab/cửa sổ) cho từng browser. Từ đó thêm bước verify title trước mỗi lần chụp.

**Sự cố 2 — Toạ độ click sai hệ quy chiếu:** khi bấm nút Cancel bằng toạ độ lấy từ ảnh OS-level (1920×1080) nhưng gọi `computer.left_click` (dùng hệ toạ độ viewport 1568×704 của tab), click bị lệch, không trúng gì. **Xử lý:** luôn lấy toạ độ click từ ảnh chụp bằng chính `computer` tool (viewport), không dùng toạ độ từ ảnh OS-level full-screen để click qua Claude in Chrome.

## Kết quả (lượt chạy đầu)

- **4/4 screen Pass** (C1, C2, C4 đầy đủ; C3 Dialog-only Pass, Full confirm flow hoãn).
- **Không có Fail nào ở Run A** (Fail duy nhất của Task 3 là C1/Run F trên iPhone — xem `run-log-F.md`).
- **Không có finding mới** phát sinh từ Run A (hành vi quan sát được khớp với các finding đã biết từ Task 1, không phát hiện lỗi compatibility riêng của Chrome/Windows).
- Disposable user `test abc` **còn nguyên vẹn** (Guest, Inactive, Member Code 91984123) — đã dùng tiếp cho Run B/C/G/F.

## C3 Full Confirm Final Validation (bổ sung 2026-08-03, sau khi Run B/C/G/F hoàn tất Dialog-only)

- Sau khi cả 5 run (A, B, C, G, F) đã xác nhận C3 Dialog-only Pass, người dùng xác nhận rõ ràng ("Confirm") để tiến hành bấm Confirm thật trên `test abc` tại Chrome (Run A).
- **Sự cố kỹ thuật giữa chừng:** tab group EMS Chrome cũ bị mất liên kết (window quan sát được đổi tiêu đề thành "Facebook", có thể do tab bị đóng hoặc window bị dùng cho việc khác). Xử lý: tạo tab mới, điều hướng lại EMS — **session vẫn đăng nhập nhờ cookie**, không cần đăng nhập lại. Nhờ người dùng tự xác nhận đúng tab đang hiển thị EMS trên màn hình của họ trước khi tiếp tục — bước thận trọng hợp lý cho 1 hành động không thể hoàn tác.
- Search `abcdefabc` → xác nhận `test abc` còn tồn tại → mở Delete dialog → **bấm Confirm thật**.
- Kết quả: `test abc` bị xoá thành công — search `abcdefabc` sau đó trả về "No users found matching your filters" (0 kết quả).
- Evidence: `T3_C3_RunA_Windows_Chrome_Desktop_supp1.png` (trạng thái sau xoá, đã promote).
- **Interaction Coverage của Run A/C3 nâng từ Dialog-only lên Full confirm flow — HOÀN TẤT.**
- Toàn bộ **20 cell Executed** của Task 3 (5 run × 4 screen) nay đã có verdict: **19 Pass** (gồm Dialog-only Pass và Full confirm flow Pass) **+ 1 Fail** (C1/Run F). Cộng thêm **8 cell Blocked** (Run D + Run E, không đổi từ đầu) = 28 dòng manifest, không phải 24. C3 Full Confirm Final Validation **không phải 1 cell riêng** — chỉ là nâng cấp Interaction Coverage của cell C3/Run A đã có sẵn (Dialog-only → Full confirm flow), không cộng thêm vào tổng số cell.

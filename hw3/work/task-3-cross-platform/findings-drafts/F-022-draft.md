# F-022 (draft) — Sidebar không responsive trên phone, nội dung tràn viewport kể cả sau khi thu gọn

**Trạng thái:** Draft — chờ người dùng xác nhận severity (đã xác nhận: 2) và tự submit Google Form.

| Trường | Nội dung |
| --- | --- |
| ID | F-022 (tiếp nối sau F-021, ID cao nhất đã dùng trong log) |
| Scenario/Screen | C — Admin manages users / C1 (Users Management) |
| Type | Bug |
| Severity | 2 (Trung bình — người dùng xác nhận) |
| Môi trường phát hiện | iOS Safari, iPhone thật, Task 3 Run F |
| Mô tả | Trên viewport điện thoại (828×1792, Safari/iOS), trang Users Management **mặc định load với sidebar mở toàn bộ**, che gần hết nội dung chính (tiêu đề, search box, nút Export/Add User, bảng, cột ACTIONS) — chỉ còn 1 dải hẹp bên phải hiển thị được. Sau khi cuộn ngang thủ công thấy được nội dung, nhưng đây không phải hành vi responsive chuẩn. Thử thu gọn sidebar về dạng icon-only (cách 1 người dùng hợp lý sẽ làm) — **vẫn không giải quyết được**: nội dung chính vẫn tràn khỏi viewport, tiêu đề "Users Management" và nút Export vẫn bị cắt ở mép phải, vẫn cần cuộn ngang. |
| Steps to reproduce | 1. Mở `https://prod-dev.ems-fitus.cloud/dashboard/admin/users` trên Safari, iPhone thật.<br>2. Quan sát trạng thái mặc định — sidebar mở, nội dung bị che.<br>3. Tìm và bấm nút thu gọn sidebar (hamburger).<br>4. Quan sát: nội dung chính (tiêu đề, Export, bảng) vẫn tràn khỏi mép phải màn hình. |
| Expected | Trên viewport phone, sidebar nên tự thu gọn mặc định (hoặc ẩn dưới dạng overlay/drawer), và nội dung chính phải tự co giãn để vừa khít chiều rộng màn hình mà không cần cuộn ngang — đúng heuristic "General UI standards / responsive layout" đã dùng ở Task 1 (Nielsen/Shneiderman). |
| Actual | Sidebar mặc định mở, che gần hết nội dung. Kể cả sau khi thu gọn, nội dung chính vẫn tràn khỏi viewport 828px, phải cuộn ngang mới xem hết. |
| Severity | 2 — chức năng vẫn dùng được (không mất dữ liệu, không crash), nhưng usability bị ảnh hưởng đáng kể trên mọi trang admin có sidebar khi dùng trên phone. |
| Suggested fix | Thêm breakpoint responsive cho viewport ≤ ~430–768px: (a) sidebar mặc định thu gọn/ẩn (drawer) trên phone; (b) nội dung chính dùng layout co giãn (flex/grid với max-width theo viewport) thay vì giữ nguyên độ rộng thiết kế cho desktop. |
| Screenshot ref | `hw3/out/reports/task-3-cross-platform/evidence/C1/T3_C1_RunF_iOS_Safari_Phone.png` (primary — trạng thái mặc định), `..._supp1.png` (sau cuộn ngang), `..._supp2.png` (sau thu gọn sidebar, vẫn tràn) |
| Form-submission timestamp | *(người dùng điền sau khi tự submit Google Form)* |

**Việc còn lại (người dùng thực hiện):**
1. Nội dung copy-paste sẵn sàng ở `hw3/work/form-copy-paste.txt` — "LẦN SUBMIT 19 (Task 3)". Submit lên Google Form (`https://forms.gle/CJQFQCAXcsDbXDMM9`) bằng email `23127179@student.hcmus.edu.vn`.
2. Merge dòng tương ứng vào `hw3/work/findings-log.md` (bảng chung), điền cột Form-submission timestamp.

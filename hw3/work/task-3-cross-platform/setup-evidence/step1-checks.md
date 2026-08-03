# Bước 1 — Kết quả kiểm tra tài khoản/công cụ (2026-08-03)

**Lưu ý:** đây là evidence nội bộ cho Bước 1, không phải evidence chính thức của 24 cell (không copy sang `hw3/out/`).

| Mục | Kết quả | Ghi chú |
| --- | --- | --- |
| BrowserStack account | ✅ Sẵn sàng | Đăng nhập qua Google Sign-In, email `nguyenbaoduy29@gmail.com`, IAM Role: Owner. Xác nhận qua ảnh chụp trang Account & Profile do người dùng cung cấp trực tiếp trong hội thoại. |
| Overlay email (khác với BrowserStack login) | ✅ Chốt | `23127179@student.hcmus.edu.vn` — đúng định dạng MSSV@....edu.vn theo §12 đề bài. |
| Firefox (Windows local) | ✅ Có sẵn | v153.0.1, `C:\Program Files\Mozilla Firefox\firefox.exe` — xác nhận qua registry uninstall scan. |
| Opera (Windows local) | ⏳ Chưa cài | Không tìm thấy qua path check/registry scan. Người dùng tự cài, không chặn pilot (Opera chỉ cần cho Run C ở Bước 5, không cần cho pilot Run D/E/F). |
| iPhone Safari | Mặc định sẵn sàng | Thiết bị vật lý, không cần kiểm tra thêm. |
| Disposable test user `test abc` | ✅ Còn tồn tại | Kiểm tra qua Claude in Chrome, đăng nhập bởi người dùng (không tự nhập password), điều hướng `https://prod-dev.ems-fitus.cloud/dashboard/admin/users`. Search bằng đúng cụm "test abc" trả về **0 kết quả** — đúng bug F-008 đã ghi nhận ở Task 1 (search không khớp full displayed name). Search lại bằng "abcdefabc" (email) ra đúng 1 kết quả: `test abc` / `abcdefabc@gmail.com`, Role: Guest, Member Code: `91984123`, Status: **Inactive**, Created 31/07/2026 21:22, Updated 02/08/2026 17:44. |

**Kết luận:** Test Data Strategy cho C3 khả thi ngay, không cần chuỗi fallback downgrade. Có thể tiến hành Bước 2 (soạn manifest) và Bước 3 (pilot Run D) mà không cần chờ Opera.

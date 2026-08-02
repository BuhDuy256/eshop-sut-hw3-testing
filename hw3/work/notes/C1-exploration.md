# Exploration Notes — C1 (Users list)

**Mục đích:** đi một vòng màn hình **trước khi** execute checklist, để biết trên đó có widget gì. Không chấm Pass/Fail ở bước này.
**Ngày:** 2026-08-02
**URL thật:** `https://prod-dev.ems-fitus.cloud/dashboard/admin/users`
**Người khảo sát:** agent Claude (Claude Code + claude-in-chrome), điều phối bởi Nguyễn Bảo Duy — 23127179

---

## 1. Đường đi tới màn hình

1. Mở `https://prod-dev.ems-fitus.cloud/dashboard/admin/users` → EMS redirect sang `/login?callbackUrl=%2Fdashboard%2Fadmin%2Fusers`
2. Chrome đã autofill sẵn `admin@gmail.com` → bấm **Login**
3. Vào thẳng **Users Management**. Sidebar bên trái, mục "Users Management" được highlight.

> Ghi chú: URL không đổi khi phân trang / lọc / đổi rows-per-page. Luôn là `/dashboard/admin/users`, không có query string.

## 2. Widget inventory — trên màn hình này có gì?

Kiểm bằng **cả mắt lẫn DOM** (`document.querySelectorAll` qua console).

| Widget | Có? | Ghi chú (số lượng, vị trí, tên hiển thị) |
| --- | --- | --- |
| Bảng dữ liệu (số cột) | ✅ | **7 cột**: USER · Role · MEMBER CODE · Status · CREATED · UPDATED · ACTIONS. `<table aria-label="Users table">` |
| Phân trang | ✅ | Bar dưới cùng: `Rows per page` (select **5/10/20/50/100**, mặc định 5) · label `1-5 of 105 results` · `Go to page` (input number) · nút số trang · mũi tên prev/next |
| Control **sort** trên header | ❌ | **`aria-sort` = 0 phần tử** trên toàn trang. Không có control sort nào |
| Control **filter** trên header | ✅ | **2 cái**: icon phễu ở `Role` và `Status`. Menu Status = All Status / Active / Inactive. Khi active hiện thêm nút `x` màu xanh để clear |
| Ô search | ✅ | 1 ô, `aria-label="Search users"`, placeholder `Search users...`, lọc theo kiểu debounce khi gõ (không cần Enter) |
| Nút toolbar (Export, Add…) | ✅ | **Export** (xanh lá) · **Add User** (xanh cyan) |
| Row actions (Edit, Delete…) | ✅ | 2 nút icon-only mỗi dòng: `aria-label="Edit user"` · `aria-label="Delete user"`. **Không có** Assign Role / Block / Reset Password ở cấp dòng |
| Form / input text | ✅ | Chỉ ô search. Form thật nằm trong dialog (C2) |
| Dropdown / select | ✅ | 1 `<select>` = rows-per-page |
| Checkbox | ❌ | 0 `input[type=checkbox]` trên C1 (có trong dialog) |
| Toggle switch (`role="switch"`) | ❌ | 0 |
| Date input | ❌ | 0 |
| Upload file | ❌ | 0 |
| Rich-text editor | ❌ | 0 |
| Modal / dialog | ✅ | Mở từ C1: **Edit User** (C2), **Create New User**, **Delete User** confirm (C3). Đều `role="dialog" aria-modal="true"` |
| Tab | ❌ | 0 `role="tab"` |
| Breadcrumb | ❌ | 0. Không có `aria-label` chứa "breadcrumb", không có class `breadcrumb` |
| Back control | ❌ | Không có. C1 là trang cấp 1 dưới dashboard, không phải trang detail |
| Badge / status pill | ✅ | Status: `Active` (xanh lá) · `Inactive` (đỏ). Role: `Student` (xanh lá) · `Guest` (xám) · `Admin` (xanh dương) · `Lecturer` (tím nhạt) |
| Toast | ❌ | **Không tồn tại.** Quan sát bằng MutationObserver không lọc trong suốt một thao tác Save: chỉ có 4 mutation (mở dialog, đóng dialog, re-render bảng). Không node toast nào được chèn |
| Progress bar / bar meter | ❌ | 0 `progress`/`[role=progressbar]` |
| Empty state | ✅ | `No users found matching your filters.` — căn giữa, giữ nguyên header bảng |
| Ảnh (avatar, thumbnail) | ⚠ | Chỉ **1** `<img>` trên trang = logo `alt="FIT"`. Avatar người dùng là `<div>` chữ cái đầu (SBQ, TLQ…), một số dòng có ảnh thật |
| Sidebar | ✅ | 7 `<a>` + 2 `<button>` (Analytics, Settings) + nút **Collapse** = 9 đích + collapse |
| `aria-live` / `role="status"` | ❌ | **0 phần tử** trên toàn trang, ở mọi thời điểm |

## 3. Các hành động có thể làm trên màn hình này

- Search theo tên/email/member code (debounce, không cần Enter)
- Lọc theo Role và theo Status
- Đổi rows-per-page; nhảy trang bằng nút số hoặc "Go to page"
- **Export** → tải file `.xlsx` về Downloads
- **Add User** → mở dialog Create New User (có field Password → agent không thực hiện, xem §5)
- **Edit user** → mở dialog Edit User (C2) — chứa cả Role và checkbox Active (block/unblock)
- **Delete user** → mở dialog xác nhận (C3)

## 4. Dữ liệu cần chuẩn bị trước khi execute

- **User Active + user Inactive để so màu badge:** ✅ có sẵn. Lọc Status = Inactive cho **5 user**, trong đó có sẵn các tài khoản test cũ: `test abc`, `TIẾN ĐỖ ĐĂNG NHẬT`, `ĐẠT PHẠM THÀNH`, `Quốc Nguyễn Hồ Anh`, `Ban hoạt động SAB`
- **Đủ 2 trang:** ✅ 105–106 user, ở rows-per-page = 5 là 21–22 trang
- **Từ khoá search không ra kết quả:** ✅ `zzzqqq`
- **User test để block/unblock:** ✅ dùng **`test abc` / `abcdefabc@gmail.com` / Guest / Inactive** — đây là tài khoản test **có sẵn từ trước**, không phải của 3 thành viên nhóm, không phải `admin@gmail.com`. Đã block/unblock round-trip và **trả về đúng trạng thái ban đầu (Inactive)**

> **Không tạo user test mới.** Form Create New User bắt buộc field **Password** (`required=true`). Agent không nhập mật khẩu vào bất kỳ field nào — xem §5. Tài khoản `test abc` có sẵn đã phủ trọn nhu cầu (IA04-03, IA04-04, IA02-13, IA04-02), nên không mất coverage.

## 5. Câu hỏi còn mở

1. **B-12 — ĐÃ TRẢ LỜI.** Xem `C2-exploration.md` §5. Tóm tắt: Assign Role và Block/Unblock **nằm trong dialog Edit User**; **Reset Password KHÔNG tồn tại** ở bất kỳ đâu trên bề mặt user-admin.
2. **Tạo user test:** không thực hiện được bằng agent (field Password bắt buộc). Đã thay bằng tài khoản test có sẵn `test abc`. Không chặn item nào.
3. **Dữ liệu biến động trong lúc chạy:** tổng số user đổi từ **105 → 106** và badge Support requests đổi **7 → 6** ngay trong phiên. Đúng như cảnh báo §4 của đề. Mọi số đo trong báo cáo đều ghi kèm thời điểm đo.
4. **Deep link tới một user:** không có route riêng cho từng user (Edit là dialog, URL không đổi) → ảnh hưởng IA03-07 và IA04-17.

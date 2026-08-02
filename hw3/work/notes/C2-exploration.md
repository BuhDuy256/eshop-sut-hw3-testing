# Exploration Notes — C2 (Edit User dialog / Assign Role)

**Ngày:** 2026-08-02
**URL thật:** `https://prod-dev.ems-fitus.cloud/dashboard/admin/users` — **dialog, URL không đổi khi mở**
**Đường đi:** C1 → cột ACTIONS → nút icon `aria-label="Edit user"` của một dòng

---

## 2. Widget inventory

| Widget | Có? | Ghi chú |
| --- | --- | --- |
| Dialog | ✅ | `role="dialog"`, `aria-modal="true"`. **Không có** `aria-label`/`aria-labelledby` → dialog không có accessible name |
| Overlay / dim | ✅ | `<div class="absolute inset-0 bg-gray-900/40 backdrop-blur-sm">` — nền tối 40% + blur. `document.elementFromPoint` ở vùng nền trả về overlay, **không** trả về control bên dưới → không click xuyên được |
| Nút X đóng | ✅ | icon-only, có `aria-label="Close"` |
| Text input | ✅ | First Name · Last Name · Email (`type=email`) · Phone Number · Member Code |
| Dropdown / select | ✅ | 1 — **Role**: `Select a Role` / Admin / Guest / Lecturer / Student. Giá trị hiện tại của user **được preselect đúng** |
| Checkbox | ✅ | 1 — **`Active`** → **đây chính là cơ chế Block/Unblock** |
| Password field | ❌ | **Không có trong Edit User** (chỉ có trong Create New User) |
| Nút submit | ✅ | `Cancel` · `Save Changes` |
| Date / upload / rich-text / toggle switch | ❌ | 0 |
| Label `<label for=…>` | ⚠ | 7 `<label>` nhưng **`for=null` toàn bộ**, và `input.labels` rỗng với mọi field trừ checkbox Active → **label không liên kết programmatically với input** |
| Dấu `*` bắt buộc | ❌ | `dialog.textContent.includes('*')` = **false**; `getComputedStyle(label,'::before'/'::after').content` = **`none`** trên cả 8 label → không có marker vẽ bằng CSS |
| `required` trong DOM | ✅ | First Name, Last Name, Email = `required=true` (Create User thêm Password). **`aria-required` = null trên tất cả** |
| `aria-live` / `role="status"` | ❌ | 0 |

## 3. Các hành động có thể làm

- Sửa First/Last name, Email, Phone, Member Code
- **Assign Role** qua dropdown Role
- **Block / Unblock** qua checkbox `Active`
- Save Changes → ghi thật xuống DB (đã xác minh: cột UPDATED đổi, badge Status đổi)
- Cancel / X / ESC → đóng dialog

## 4. Dữ liệu cần chuẩn bị

- Đã dùng `test abc` (Guest, Inactive) cho toàn bộ thao tác ghi. Round-trip Inactive → Active → Inactive, **trạng thái cuối = trạng thái đầu**.

## 5. B-12 — TRẢ LỜI DỨT ĐIỂM

**Câu hỏi:** Assign Role, Block/Unblock, Reset Password có nằm chung trong dialog Edit không?

**Trả lời (quan sát trực tiếp, 2026-08-02):**

| Chức năng C3 theo phân công | Thực tế trong EMS |
| --- | --- |
| **Assign Role** | ✅ Có — dropdown `Role` **bên trong dialog Edit User**. Tức là **C2 và "assign role" là một** |
| **Block / Unblock** | ✅ Có, nhưng **không phải dialog riêng** — là checkbox `Active` **bên trong chính dialog Edit User**. Không có nút Block ở cấp dòng, không có dialog Block riêng |
| **Reset Password** | ❌ **KHÔNG TỒN TẠI.** Không có nút/menu Reset Password ở cấp dòng, không có trong dialog Edit, không có trong toolbar. Field `Password` chỉ xuất hiện ở dialog **Create New User** (lúc tạo mới); không có đường nào để admin đặt lại mật khẩu cho user đã tồn tại |

**Hệ quả cho việc đóng gói màn hình** — xem `../../out/reports/checklist-execution/README.md`:

- "C3 — Block-Unblock & Reset-Password **dialogs**" như phân công ban đầu **không tồn tại dưới dạng đó**.
- Nửa **Block/Unblock** → chấm trên **C2** (nó là một control của C2).
- Nửa **Reset Password** → **không có chức năng để test**, ghi rõ là giới hạn phạm vi, **không** tính là coverage.
- Cái **thật sự** là một dialog riêng và thật sự thuộc nhóm "hành động phá huỷ" là **Delete User confirm** → đó là nội dung của `C3.md`.

**Không đếm gộp để giữ con số 4.** Cách đếm trung thực: **C1 · C2 (Edit, gồm role + block) · C3 (Delete confirm) · C4 (Export)** = 4 bề mặt, nhưng **một nửa nội dung C3 theo phân công gốc đã bốc hơi vì EMS không có chức năng đó**, và điều này được nói thẳng trong README.

## 6. Câu hỏi còn mở

1. Focus **không** được chuyển vào dialog khi mở (`document.activeElement` vẫn là nút "Edit user" đã bấm) → không có focus trap. Ảnh hưởng IA03-10, IA01-12.
2. Label "First Name" / "Last Name" **bị hoán đổi so với field thật** — xác nhận bằng 2 nguồn độc lập, xem `C2.md` IA02-02.

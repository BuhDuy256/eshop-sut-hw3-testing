# Exploration Notes — C3 (Delete User confirmation dialog)

**Ngày:** 2026-08-02
**URL thật:** `https://prod-dev.ems-fitus.cloud/dashboard/admin/users` — dialog, URL không đổi
**Đường đi:** C1 → cột ACTIONS → nút icon `aria-label="Delete user"` của một dòng

> **Phạm vi C3 đã được điều chỉnh theo kết quả B-12.** Phân công gốc ghi "Block-Unblock & Reset-Password dialogs". Khảo sát cho thấy: Block/Unblock là **checkbox `Active` trong dialog Edit (C2)**, không phải dialog riêng; **Reset Password không tồn tại trong EMS**. Bề mặt duy nhất thật sự là một dialog riêng thuộc nhóm hành động phá huỷ trên scenario C là **Delete User confirm** → C3 = dialog này. Chi tiết ở `C2-exploration.md` §5.

---

## 2. Widget inventory

| Widget | Có? | Ghi chú |
| --- | --- | --- |
| Dialog xác nhận | ✅ | Tiêu đề **`Delete User`** kèm icon thùng rác đỏ |
| Nội dung cảnh báo | ✅ | `Are you sure you want to delete user **SƠN BÙI QUANG**? This action cannot be undone.` — **nêu đúng tên record** (in đậm) **và** nêu hậu quả |
| Nút hành động | ✅ | `Cancel` (viền, trung tính) · `Confirm` (nền **đỏ** — màu cảnh báo đúng ngữ nghĩa) |
| Nút X đóng | ✅ | icon-only góc phải |
| Overlay / dim | ✅ | nền tối + blur như C2 |
| `aria-live` / `role="status"` | ❌ | 0 |
| Toast sau khi thao tác | ❌ | không có (xem C1/C2 IA04-04) |
| Input / select / checkbox | ❌ | 0 — dialog chỉ có text + 3 nút |

## 3. Các hành động có thể làm

- `Cancel` → đóng, **record không bị đụng** (đã xác minh: bấm Delete trên dòng `SƠN BÙI QUANG` rồi Cancel, dòng vẫn còn nguyên)
- `Confirm` → xoá thật. **KHÔNG thực hiện** trong phiên này (không có user nào được phép xoá vĩnh viễn; §7 handoff cấm xoá hẳn)
- `X` / ESC → đóng

## 4. Dữ liệu cần chuẩn bị

- Không cần tạo gì. Test bằng cách mở confirm rồi **Cancel** — phủ trọn IA04-03 mà không mất dữ liệu.

## 5. Câu hỏi còn mở

1. Nhánh `Confirm` (xoá thật) **không được chạy** — có chủ ý, để không phá dữ liệu thật. Ghi rõ trong `C3.md` là giới hạn phạm vi tự đặt, không phải Pass cũng không phải Fail.
2. Không có toast sau bất kỳ hành động nào → cùng gốc với finding IA04-04 trên C1/C2.

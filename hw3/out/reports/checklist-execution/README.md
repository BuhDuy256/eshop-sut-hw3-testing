# Task 1 — GUI Checklist: Design & Execution

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Scenario:** **C — Admin manages users**
**SUT:** EMS — https://prod-dev.ems-fitus.cloud/ (external web app, test thủ công qua UI, không đọc source code)
**Ngày hoàn thành:** _(yyyy-mm-dd)_

> Đây là bản tổng hợp Task 1 để nộp. Chi tiết từng item nằm trong `C1.md` … `C4.md`; bug nằm trong `bug-reports.md`; ảnh nằm trong `evidence/`.

---

## Part A — Shared GUI Checklist (group deliverable) ✅

| Mục | Nội dung |
| --- | --- |
| File | `hw3/docs/gui-checklist/Shared_GUI_Checklist.md` |
| Version | v1.9 |
| Số item | **60** (yêu cầu §6: > 40) |
| Phân bố | IA-01: 13 · IA-02: 15 · IA-03: 15 · IA-04: 17 |
| Nền tảng | WCAG 2.1 (6 SC) · Nielsen 10/10 · Norman 6/6 · Shneiderman 8/8 · slide S13 · khảo sát 14 trang EMS thật |
| Vai trò của tôi | _(điền: đã đóng góp item nào / review vòng nào)_ |
| Reference sources + AI prompts | `hw3/out/group/` — _(điền tên file sau khi lấy từ group)_ |

Checklist là **group deliverable đã đóng băng**. Trong Task 1B tôi **thực thi** nó, không sửa lời văn item nào (§18 yêu cầu checklist giống hệt nhau giữa các thành viên).

## Part B — Execution trên các màn hình của tôi

### Màn hình đã test và lý do chọn

| ID | Màn hình | Vì sao chọn |
| --- | --- | --- |
| **C1** | Users list | Bề mặt IA-03 duy nhất của scenario: bảng 7 cột, filter, search, phân trang, sidebar, toolbar |
| **C2** | Assign Role / Edit user (dialog) | Form duy nhất của scenario — chở gần như toàn bộ IA-02 |
| **C3** | Block-Unblock & Reset-Password (dialog xác nhận) | Nửa "hành động phá huỷ" của IA-04: confirm, modality, toast, ESC |
| **C4** | Export to Excel | §5 C4 gọi tên trực tiếp — "column completeness and download feedback"; là referent duy nhất của IA04-13 |

§5 yêu cầu tối thiểu **3** màn hình; tôi lấy **4** vì bề mặt user-admin nhỏ, dừng ở 3 sẽ đẩy quá nhiều item thành N/A.

_(Nếu C2 và C3 hoá ra là **một** dialog — xem blocker B-12 — ghi rõ ở đây và trình bày package là C1 · C2+C3 · C4 = 3 màn hình, không đếm gộp thành 4.)_

### Kết quả tổng hợp

| Màn hình | Applicable | Executed | Passed | Failed | N/A | Bug |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | | | | | | |
| C2 | | | | | | |
| C3 | | | | | | |
| C4 | | | | | | |
| **Tổng** | | | | | | |

> **N/A không được tính là Passed.** Tỉ lệ pass = Passed / Applicable.

### Phân bố Failed theo Interface Aspect

| Aspect | Số item Failed | Nhận xét |
| --- | --- | --- |
| IA-01 General UI | | |
| IA-02 Forms | | |
| IA-03 Navigation | | |
| IA-04 Feedback / State | | |

### Vì sao có nhiều N/A ở scenario C

_(Điền sau khi execute. Nội dung dự kiến: bề mặt user-admin không có upload, rich-text, date control, toggle, capacity figure hay real-time counter; ngoài ra 6 item v1.8/v1.9 được viết riêng cho scenario B và D. Mỗi N/A đã có lý do một dòng trong file execution tương ứng.)_

## Bug & Usability findings từ Task 1

| Findings-Log-ID | Bug ID | Screen | Type | Severity | Tiêu đề |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Chi tiết: `bug-reports.md`. Tất cả đã submit lên Google Form (§7) và có mặt trong `hw3/out/findings-log.md`.

## Ghi chú về quy trình

**Thứ tự thực hiện:** C1 (pilot, chạy đủ 60 item để đo thời gian) → review → C2 → C3 → C4.

**Thời gian thực tế:** _(điền)_

**Điều chỉnh giữa chừng:** _(điền: sau pilot đã đổi gì trong cách ghi chép/chụp ảnh)_

**Giới hạn đã biết:** _(vd: item cần môi trường đặc biệt — Slow 3G, Offline — chạy trên máy cá nhân, không phải môi trường lab; dữ liệu EMS có thể đã reset giữa các phiên)_

## Đối chiếu với yêu cầu §6 Task 1

| Yêu cầu | Đáp ứng |
| --- | --- |
| Checklist > 40 item, phủ IA-01…IA-04 | ✅ 60 item |
| Reference sources + AI prompts (group) | _(điền)_ |
| Giải thích item nào AI bỏ sót và vì sao | ✅ §"Items added beyond the AI output" trong checklist |
| Execute checklist trên ≥ 3 màn hình | _(điền)_ |
| Đánh dấu Passed/Failed từng item từng màn hình | _(điền)_ |
| Cột Notes ghi lý do cho mỗi Failed | _(điền)_ |
| Screenshot cho item Failed | _(điền)_ |
| Bug có: screen, steps, expected vs actual, severity, screenshot | _(điền)_ |
| Bug đã report qua kênh §7 | _(điền)_ |

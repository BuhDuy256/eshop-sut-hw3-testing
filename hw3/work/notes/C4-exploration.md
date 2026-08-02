# Exploration Notes — C4 (Export to Excel)

**Ngày:** 2026-08-02
**URL thật:** `https://prod-dev.ems-fitus.cloud/dashboard/admin/users` — Export là nút trên toolbar C1, không có route riêng
**Đường đi:** C1 → toolbar → nút **Export** (nền xanh lá, icon download)

---

## 2. Widget inventory

| Widget | Có? | Ghi chú |
| --- | --- | --- |
| Nút Export | ✅ | 1, text `Export`, nền xanh lá. Trên Support requests nút tương đương tên là `Export Excel` (khác chữ) |
| Busy state / spinner khi bấm | ❌ | Đo bằng polling 150 ms trong 6 s: `disabled` luôn `false`, text luôn `Export`, không có `.animate-spin` |
| Toast / thông báo hoàn tất | ❌ | không có |
| Dialog chọn phạm vi / cột | ❌ | không có — bấm là tải luôn |
| Progress bar | ❌ | 0 |
| File tải về | ✅ | `users-export-1785667505695.xlsx`, 14 339 bytes, vào thư mục Downloads của Windows |

## 3. Các hành động có thể làm

- Bấm Export khi **không** lọc → file toàn bộ dataset
- Bấm Export khi **đang** lọc/search → (đã đo) vẫn ra toàn bộ dataset

## 4. Dữ liệu cần chuẩn bị

- Cần một filter đang bật để kiểm phạm vi export. Đã dùng search `abc` → màn hình còn **1 dòng**.

## 5. Nội dung file đã mở và đối chiếu

Đọc bằng Python (`zipfile` + parse `sheet1.xml` / `sharedStrings.xml`), không qua Excel.

**Cấu trúc file:** 108 row = 1 dòng tiêu đề `USER REPORT` + 1 dòng metadata `Export date: 8/2/2026 | Exporter: Admin Tôi là` + 1 dòng header + **105 dòng dữ liệu**.

**Header trong file:** `Last Name · First Name · Email · Phone · Card Code · Role · Status · Created At`

**So với bảng trên màn hình:** `USER · Role · MEMBER CODE · Status · CREATED · UPDATED · ACTIONS`

| Cột trên màn hình | Trong file | Nhận xét |
| --- | --- | --- |
| USER (tên + email) | `Last Name` + `First Name` + `Email` | tách ra, đủ |
| Role | `Role` | ✅ |
| MEMBER CODE | `Card Code` | ⚠ **đổi tên**, không khớp thuật ngữ trên UI |
| Status | `Status` | ⚠ giá trị là **`Hoạt động`** (tiếng Việt) trong khi UI hiển thị `Active` (tiếng Anh) |
| CREATED | `Created At` | ✅ (numFmt 164 = `DD/MM/YYYY HH:MM`, render đúng là ngày) |
| UPDATED | — | ❌ **THIẾU HẲN** |
| — | `Phone` | thêm, không có trên màn hình (không phải lỗi) |

**Phạm vi:** màn hình đang lọc còn **1 dòng**, file chứa **105 dòng** — user đang lọc nằm ở dòng thứ 38 trong file. Export **bỏ qua filter** và UI không hề nói điều đó.

## 6. Câu hỏi còn mở

1. Không kiểm được export ở 3 chỗ còn lại (`/profile` My Activities, Registrants tab, Support requests) — ngoài phạm vi 4 màn hình của scenario C. Ghi rõ trong `C4.md` là chỉ chấm 1/4 export.
2. Ngày trong file **đúng định dạng** (đã kiểm `styles.xml`, có numFmt) — **không** báo đây là lỗi, dù giá trị thô là số serial Excel.

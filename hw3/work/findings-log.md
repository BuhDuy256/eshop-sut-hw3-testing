# Bug & Usability Findings Log (working copy)

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Google Form:** https://forms.gle/CJQFQCAXcsDbXDMM9 — submit bằng email `MSSV@....edu.vn`
**Trạng thái:** file **đang chạy**. Ở Step 12 sẽ chốt và copy sang `hw3/out/findings-log.md`.

> **Đây là single source of truth.** Mọi finding vào file này **trước**, rồi mới submit Form. §7 nói TA có thể đối chiếu số lượng giữa file này và Form — hai bên phải khớp tuyệt đối.

## Quy tắc

1. **Log trước, submit sau.** Ghi dòng vào bảng → submit Form → quay lại điền cột *Form timestamp*. Dòng nào thiếu timestamp = chưa submit.
2. **ID không tái sử dụng.** F-001, F-002… tăng dần, kể cả khi một finding bị bỏ.
3. **Không trùng.** Nhiều item Fail cùng nguyên nhân gốc = **1 dòng**, cột *Steps/Heuristic* liệt kê hết item ID.
4. **Type** chỉ có 2 giá trị: `Bug` hoặc `Usability`.
5. **Severity** dùng thang Nielsen 0–4 (bảng trong `out/reports/checklist-execution/bug-reports.md`).
6. **Source** cho biết finding đến từ đâu — Task 1B / Task 2 / Task 3.

> ### ⚠ Cột *Form timestamp* đang trống toàn bộ — chờ sinh viên trực tiếp submit
>
> Cả 21 dòng dưới đây **chưa được submit lên Google Form**. *(Ghi chú audit: Sinh viên đã rà soát lại toàn bộ nội dung của 21 lỗi này và chốt severity thủ công, nhưng việc submit phải được thực hiện bằng chính tài khoản email thật `MSSV@....edu.vn` của sinh viên theo §7).* Nội dung sẵn sàng để dán đã được chuẩn bị trong `out/reports/task-1-checklist-execution/bug-reports.md` — mỗi finding là một khối đầy đủ trường.
>
> **Sau khi sinh viên tự tay submit từng dòng, sinh viên sẽ điền timestamp vào cột cuối rồi cập nhật bảng Đối soát ở cuối file.** Đừng sửa số cho khớp — nếu lệch thì tìm dòng chưa submit và submit nốt.

## Bảng findings

| ID | Source | Scenario/Screen | Type | Description | Steps / Heuristic | Severity | Suggested fix | Screenshot ref | Form timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | Task 1B | C — C1 Users list (header, toàn khu admin) | Bug | Nút chuyển ngôn ngữ EN/VI ở header không có tác dụng gì: bấm 3 lần, `lang` vẫn `"en"`, `<title>` không đổi, mọi label vẫn tiếng Anh, không có dropdown, không ghi key locale nào vào cookie/localStorage | IA01-08 · IA01-09 · Slides S13 p.26 — Localization / Nielsen H4 | 3 | Nối nút vào provider i18n thật, hoặc ẩn nút nếu bản dịch chưa sẵn sàng | `evidence/C1/C1_IA01-08_language-toggle-no-effect.png` | |
| F-002 | Task 1B | C — C1 Users list (so với Support requests) | Usability | Ngày giờ hiển thị 3 quy ước khác nhau trong cùng một locale: `02/08/2026 17:11` (Users) · `Aug 2, 2026, 12:56 AM` (Support) · placeholder `mm/dd/yyyy` (date filter) | IA01-09 · Slides S13 p.26 / Nielsen H4 | 2 | Dùng một hàm format ngày chung, gắn với locale; ưu tiên `dd/MM/yyyy` | `evidence/C1/C1_IA01-09_two-date-formats-1-users.png` · `…-2-support.png` | |
| F-003 | Task 1B | C — C1 Users list (so với Events, Support) | Usability | Tiêu đề trang không nhất quán: Users/Events dùng `font-weight 700` + gạch chân cyan, không subtitle; Support dùng `800`, không gạch chân, có subtitle | IA01-01 · Nielsen H4 / Slides S13 p.16 | 1 | Tách tiêu đề trang thành component dùng chung có prop subtitle | `evidence/C1/C1_IA01-01_page-title-inconsistent-1-users.png` · `…-2-support.png` | |
| F-004 | Task 1B | C — C1 + C2 + C3 | Bug | Ô `Go to page` nhận focus bàn phím với `outline` trong suốt (`rgba(0,0,0,0)`), border 0, không box-shadow → không thấy focus. Và khi mở dialog Edit/Delete, `document.activeElement` vẫn ở ngoài dialog (`dialog.contains()` = false), không có focus trap | IA01-12 · WCAG 2.1 SC 2.4.7 — Focus Visible | 2 | Cấp style focus cho `Go to page`; đặt focus vào dialog khi mở (dialog xoá → lên `Cancel`), thêm focus trap và `aria-labelledby` | `evidence/C1/C1_IA01-12_go-to-page-focus-invisible.png` · `evidence/C2/C2_IA01-12_focus-stays-outside-dialog.png` · `evidence/C3/C3_IA01-12_focus-not-moved-into-delete-dialog.png` | |
| F-005 | Task 1B | C — C1 Users list (sidebar) | Bug | Sidebar thu gọn không có tooltip: 0/11 mục có `title`, 0/11 có `aria-label`, hover 3 s không ra node tooltip nào; 10/11 mục mất luôn `textContent` nên không còn tên cho screen reader | IA03-01 · Nielsen H1/H7 · Shneiderman R2 · Slides S13 p.17 | 2 | Thêm `title` + `aria-label` cho mọi mục sidebar, hoặc giữ nhãn trong DOM bằng visually-hidden | `evidence/C1/C1_IA03-01_collapsed-sidebar-no-tooltip.png` | |
| F-006 | Task 1B | C — C1 Users list | Usability | Bảng 7 cột không sort được cột nào: `[aria-sort]` = 0 phần tử, chỉ 2/7 header có control và cả hai là filter. 107 user / 22 trang mà không sắp xếp được theo tên hay ngày tạo | IA03-08 · Norman P1 · Slides S13 p.12, p.14 | 2 | Thêm sort cho `CREATED`, `UPDATED`, `USER`; phơi `aria-sort`; dùng icon mũi tên khác icon phễu | `evidence/C1/C1_IA03-08_seven-columns-zero-sort.png` | |
| F-007 | Task 1B | C — C1 Users list | Bug | `<select>` rows-per-page có option rỗng làm option đầu (`["","5","10","20","50","100"]`); khi option đó được chọn, nhãn phân trang render `NaN-NaN of 107 results` trong khi bảng vẫn hiện 5 dòng | IA03-06 (vế a) · Nielsen H4 | 2 | Bỏ option rỗng khỏi `<select>`; thêm giá trị mặc định phòng hờ để nhãn không bao giờ ra `NaN` | `evidence/C1/C1_IA03-06_label-shows-NaN-NaN.png` | |
| F-008 | Task 1B | C — C1 Users list (so với Events, Support) | Usability | Thang rows-per-page không khớp giữa các list: Users/Events = 5/10/20/50/100 mặc định 5; Support = 10/20/50/100 (thiếu 5) mặc định 20 | IA03-06 (vế b) · Nielsen H4 | 1 | Đưa thang và giá trị mặc định vào một hằng số dùng chung | `evidence/C1/C1_IA03-06_pagination-scale-differs.png` | |
| F-009 | Task 1B | C — C1 Users list | Bug | Bấm Back của trình duyệt làm mất trạng thái danh sách: đang ở trang 2 với rows=10 (`11-20 of 106`), sau Back thành `1-5 of 106` và rows tự về 5. URL không bao giờ đổi nên không có state để khôi phục | IA03-13 · Nielsen H3 · Slides S13 p.18 | 2 | Đưa page/rows/filter/search vào query string và đọc lại khi mount | `evidence/C1/C1_IA03-13_before-page2-rows10.png` · `…_after-back-reset-page1-rows5.png` | |
| F-010 | Task 1B | C — C1 Users list | Bug | Không tìm được user bằng tên đầy đủ đang hiển thị: query `test abc` → 0 kết quả ("No users found matching your filters") dù bảng đang hiển thị đúng chữ `test abc`; query `test` → 6 dòng, query `abc` → 1 dòng đúng user đó | **Không thuộc item nào** (checklist v1.9 thiếu item về ô search bảng dữ liệu) · Nielsen H6 | 3 | Cho search khớp trên tên đã ghép cả hai chiều, hoặc tách token và yêu cầu mọi token khớp ở bất kỳ trường nào | `evidence/C1/C1_F010_search-exact-displayed-name-0-results-1.png` · `…-2.png` | |
| F-011 | Task 1B | C — C1 Users list | Bug | Trong ~1 s sau khi gõ, bảng hiển thị kết quả của truy vấn cũ kèm nhãn khẳng định: tại 3 780 ms ô search đã hiện `test` nhưng bảng render 94 dòng và nhãn ghi `1-94 of 94 results`; tới 3 998 ms mới thành `1-6 of 6`. Không có spinner/skeleton | **Không thuộc item nào** (gần nhất IA01-07 nhưng item đó yêu cầu Slow 3G) · Nielsen H1 | 2 | Huỷ/bỏ qua response của request search cũ; hiển thị trạng thái đang tải | *(không có ảnh — trạng thái chỉ tồn tại ~0,2 s; bằng chứng là log lấy mẫu trong bug-reports.md)* | |
| F-012 | Task 1B | C — C2 Edit/Create User dialog | Bug | Nhãn `First Name` và `Last Name` bị gán ngược so với ô nhập. 3 nguồn độc lập cùng xác nhận: placeholder đảo; lỗi validation báo "Last name is required" dưới nhãn First Name; file export ghi `Last Name="BÙI QUANG"` trong khi dialog để giá trị đó dưới nhãn `First Name` | IA02-02 · Nielsen H6 · Slides S13 p.16 — Labels | 3 | Hoán lại 2 nhãn theo chuẩn của thông báo lỗi + header export; rà lại dữ liệu đã nhập trước khi sửa | `evidence/C2/C2_IA02-02_validation-messages-prove-labels-swapped.png` · `evidence/C2/C2_IA02-01_no-required-marker-and-swapped-labels.png` | |
| F-013 | Task 1B | C — C2 Edit/Create User dialog | Bug | 4 trường bắt buộc không có dấu hiệu nào: không `*` trong text, `::before`/`::after` = `none` trên cả 8 nhãn, `aria-required` = null toàn bộ, và cả 7 `<label>` đều `for=null` nên không liên kết với input. Chỉ trường **không** bắt buộc được đánh dấu (`Member Code (Optional)`) | IA02-01 · Norman P3/P6 · Slides S13 p.11 | 2 | Thêm marker bắt buộc nhìn thấy được + `aria-required="true"` + nối `<label for>` với `id` input | `evidence/C2/C2_IA02-01_no-required-marker-and-swapped-labels.png` | |
| F-014 | Task 1B | C — C2 Edit User dialog + C4 Export (+ xác nhận độc lập trên luồng block/unblock, sinh viên chạy tay 2026-08-03) | Bug | Không có toast/xác nhận nào sau hành động thành công. Một lần Save thật (Inactive→Active, UPDATED đổi) chỉ sinh 4 mutation ở body (mở dialog, đóng dialog, re-render bảng), không node toast nào. `[aria-live],[role=status],[role=alert]` = **0** phần tử ở mọi thời điểm. Export cũng vậy | IA04-04 · IA04-12 · Nielsen H1 · Shneiderman R3 · WCAG 2.1 SC 4.1.3 | 3 | Thêm hệ thống toast dùng chung trong container `role="status" aria-live="polite"`, ≥ 5 s, cho cả trường hợp thất bại | `evidence/C2/C2_IA04-04_no-toast-after-successful-save.png` · `evidence/C4/C4_IA04-13_export-no-feedback-and-ignores-filter.png` | |
| F-015 | Task 1B | C — C2 Edit User dialog | Usability | Gõ `UNSAVED-EDIT-999` vào ô Phone Number rồi bấm ESC: dialog đóng ngay, không cảnh báo (không có chuỗi `unsaved\|discard\|are you sure\|lost` nào trên trang), thay đổi mất hẳn, không khôi phục được | IA02-13 · Nielsen H5 · Shneiderman R6 | 2 | Theo dõi trạng thái dirty; ESC/Cancel/X phải hỏi "Bỏ thay đổi?" kèm lựa chọn ở lại | `evidence/C2/C2_IA02-13_esc-discards-edit-silently-1-before.png` · `…-2-after.png` | |
| F-016 | Task 1B | C — C2 Create/Edit User dialog | Usability | Bấm Enter ở ô cuối form không kích hoạt hành động chính: dialog vẫn mở, 0 lỗi inline, không tạo user, không reload. Nguyên nhân: dialog không có phần tử `<form>` nên không có implicit submit | IA02-10 (ca b) · Norman P4 · Slides S13 p.18 | 2 | Bọc field trong `<form onSubmit>` và để nút chính `type="submit"` | `evidence/C2/C2_IA02-10_enter-does-nothing-on-form.png` | |
| F-017 | Task 1B | C — C4 Export to Excel | Bug | Export bỏ qua filter đang bật: màn hình đang lọc còn **1 dòng** (`1-1 of 1 results`) nhưng file chứa **105 dòng** — toàn bộ dataset; user đang lọc nằm ở dòng 38. Giao diện không nói phạm vi export là gì | IA04-13 · Assignment §5 C4 · Nielsen H1 | 3 | Cho export theo đúng filter đang bật; và nói rõ phạm vi ngay tại nút hoặc trong hộp xác nhận | `evidence/C4/C4_IA04-13_export-no-feedback-and-ignores-filter.png` · `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | |
| F-018 | Task 1B | C — C4 Export to Excel | Bug | File export thiếu cột `UPDATED` (có trên màn hình, không có trong file) và đổi tên `MEMBER CODE` thành `Card Code`, không khớp thuật ngữ giao diện | IA04-13 · Assignment §5 C4 — "column completeness" | 2 | Thêm cột `Updated At`; đổi `Card Code` → `Member Code` | `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | |
| F-019 | Task 1B | C — C4 Export to Excel | Bug | Giá trị cột Status trong file ghi bằng tiếng Việt (`Hoạt động`) trong khi giao diện hoàn toàn tiếng Anh (`Active`) và không đổi ngôn ngữ được; header file lại bằng tiếng Anh → một bảng trộn 2 ngôn ngữ | IA04-13 · Nielsen H4 | 1 | Cho phần sinh file dùng chung bộ chuỗi i18n với giao diện | `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | |
| F-020 | Task 1B | C — C4 Export to Excel | Usability | Tên file export là `users-export-1785667505695.xlsx` — dùng epoch mili-giây thay vì ngày đọc được | IA04-13 · Nielsen H1 · Shneiderman R3 | 1 | Đặt tên dạng `users-export-2026-08-02_1745.xlsx`; ghi luôn phạm vi filter nếu có | `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | |
| F-021 | Task 1B | C — C2 Edit User dialog | Bug | Khi Save thất bại (offline), EMS **có** báo lỗi inline trong dialog và **không** có toast success giả — nhưng nội dung là chuỗi thô của Fetch API: **`Failed to fetch`**, không nói cái gì hỏng, không nói vì sao, không có nút retry | IA04-11 · Slides S13 p.11 · Nielsen H9 · Shneiderman R5 | 2 | Bắt lỗi mạng ở tầng gọi API, thay bằng thông báo theo ngữ cảnh + nút **Thử lại**; không để chuỗi lỗi JS thô lọt ra UI | `evidence/C2/C2_IA04-11_offline-save-failed-to-fetch.png` | |

**Đường dẫn ảnh** tính tương đối từ `hw3/out/reports/checklist-execution/`.

## Thống kê nhanh

| Chỉ số | Giá trị |
| --- | --- |
| Tổng finding | **21** |
| Type = Bug | **15** |
| Type = Usability | **6** |
| Severity 4 (Catastrophe) | 0 |
| Severity 3 (Major) | **5** — F-001, F-010, F-012, F-014, F-017 |
| Severity 2 (Minor) | **12** |
| Severity 1 (Cosmetic) | **4** — F-003, F-008, F-019, F-020 |
| Truy được về một item checklist | **19** |
| **Không** thuộc item nào | **2** — F-010, F-011 |

## Đối soát (điền ở Step 12)

| Kiểm tra | Kết quả |
| --- | --- |
| Số dòng trong bảng này | **21** |
| Số lần submit Form (đếm từ email xác nhận / bản ghi riêng) | 0 *(Đang chờ nộp chính thức bằng email `MSSV@...`)* |
| Hai số trên khớp? | *(Đang chờ đối chiếu sau khi sinh viên nộp xong)* |
| Mọi dòng đều có Screenshot ref? | **20/21.** F-011 cố ý không có ảnh: trạng thái lỗi chỉ tồn tại ~0,2 s nên không chụp kịp; bằng chứng thay thế là log lấy mẫu theo mốc thời gian, ghi trong `bug-reports.md` và tái hiện được bằng các bước đã mô tả |
| Mọi dòng đều có Form timestamp? | **0/21** — xem cảnh báo ở đầu file |

## Các trường của Google Form

_(Ghi chú: Sinh viên sẽ mở Form bằng email trường để chép lại danh sách câu hỏi vào đây, chuẩn bị thông tin trước khi dán các finding.)_

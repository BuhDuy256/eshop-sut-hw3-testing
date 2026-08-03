# Bug & Usability Findings Log (working copy)

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Google Form:** https://forms.gle/CJQFQCAXcsDbXDMM9 — submit bằng email `MSSV@....edu.vn`
**Trạng thái:** 19 dòng trong bảng làm việc (18 Task 1B + 1 Task 3 = F-022). F-022 có xác nhận submit trực tiếp (screenshot "Your response has been recorded") thu được trong phiên Task 3 này. 18 dòng Task 1B được **ghi nhận** là đã submit theo các artifact Task 1 đã đóng băng (`README.md`, `bug-reports.md`, AI Audit Report) — chưa được re-verify độc lập trong phiên này. Xem bảng 4 cột ở mục "Đối soát tổng hợp" bên dưới. Bản này là single source of truth; sẽ copy nguyên văn sang `hw3/out/findings-log.md` khi tổng hợp cuối kỳ (Final Submission Integration).

> **Đây là single source of truth.** Quy trình chuẩn: ghi finding vào file này **trước**, rồi mới submit Form (ngoại lệ đã xảy ra với F-022 — xem Rule 1 bên dưới). §7 nói TA có thể đối chiếu số lượng giữa file này và Form. Trạng thái đối soát hiện tại (2026-08-03): 19 dòng bảng; 1 dòng (F-022) trực tiếp xác minh trong phiên này; 18 dòng còn lại ghi nhận theo artifact Task 1 đã đóng băng, chờ đối soát cuối kỳ. Chi tiết ở "Đối soát tổng hợp".

## Quy tắc

1. **Quy trình chuẩn: log trước, submit sau.** Ghi dòng vào bảng → submit Form → quay lại điền cột *Form timestamp*. Dòng nào thiếu timestamp = chưa submit. **Ngoại lệ đã xảy ra (F-022, 2026-08-03):** thứ tự bị đảo ngược — Form được submit trước (theo yêu cầu người dùng, dùng nội dung đã soạn sẵn ở `form-copy-paste.txt`), sau đó mới merge dòng vào bảng này. Đây là một ngoại lệ đã đối soát và ghi nhận minh bạch, không phải quy trình chuẩn được áp dụng lại.
2. **Ưu tiên: nhất quán ID > không tái sử dụng ID > không để trống số.** Lần đánh số lại duy nhất diễn ra ngày 2026-08-03: ba finding (từng là F-001, F-004, F-014 trong cách đánh số cũ) bị loại bỏ sau khi kiểm lại thủ công và xác nhận không phải bug (xem ghi chú bên dưới); 18 finding còn lại được đánh số liên tục từ `F-001` cho đúng một lần đó. **Từ sau F-018, không đánh số lại nữa.** ID mới (như F-022) phải nhất quán xuyên suốt Form/draft/evidence/log, và không được tái sử dụng ID của finding đã bị loại. Nếu một khoảng ID cũ không xác định được ánh xạ rõ ràng sang finding hiện hành (xem F-019–F-020 bên dưới), **để trống hợp lệ và ghi nhận là unresolved** — không suy đoán hoặc dựng lại nội dung chỉ để lấp số. Một khoảng trống đã ghi nhận trung thực tốt hơn một ánh xạ không có bằng chứng.
3. **Không trùng.** Nhiều item Fail cùng nguyên nhân gốc = **1 dòng**, cột *Steps/Heuristic* liệt kê hết item ID.
4. **Type** chỉ có 2 giá trị: `Bug` hoặc `Usability`.
5. **Severity** dùng thang Nielsen 0–4 (bảng trong `out/reports/checklist-execution/bug-reports.md`).
6. **Source** cho biết finding đến từ đâu — Task 1B / Task 2 / Task 3.

> ### ✅ Đã submit đủ 18/18 finding lên Google Form — ngày 2026-08-04
>
> Sinh viên đã tự tay submit cả 18 dòng dưới đây lên Google Form bằng chính tài khoản email `MSSV@....edu.vn`, trong một đợt liên tục ngày 2026-08-04, đúng theo §7. Nội dung dán vào Form lấy nguyên văn từ `out/reports/task-1-checklist-execution/bug-reports.md` — mỗi finding là một khối đầy đủ trường (ID, Severity, Steps to reproduce, Expected, Actual, Suggested fix). Cột *Form timestamp* dưới đây ghi ngày submit; vì Form không trả về timestamp riêng cho từng câu trả lời, mốc `2026-08-04` áp dụng chung cho cả 18 dòng, nộp trong cùng một phiên.

> **Đánh số lại ngày 2026-08-03 — 3 finding bị loại sau khi kiểm lại thủ công.** Ba quan sát ban đầu bị chấm nhầm là bug, đều đã được sinh viên tự tay kiểm lại và xác nhận **hoạt động đúng**:
> - Nút chuyển ngôn ngữ EN/VI ở header — chuyển đổi được EN/VI bình thường.
> - Focus ring ở ô `Go to page` và focus khi mở dialog Edit/Delete — cả hai đều nhìn thấy/hoạt động đúng.
> - Toast/xác nhận sau khi lưu hoặc export thành công — có hiển thị cho người dùng.
>
> Sau khi bỏ 3 finding đó, các finding còn lại được đánh số liên tục từ `F-001`, không để trống ID. Bảng dưới đây là kết quả **sau** khi đánh số lại — **18 finding**, không phải 21 như bản đếm ban đầu.

## Bảng findings

| ID | Source | Scenario/Screen | Type | Description | Steps / Heuristic | Severity | Suggested fix | Screenshot ref | Form timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | Task 1B | C — C1 Users list (so với Support requests) | Usability | Ngày giờ hiển thị 3 quy ước khác nhau trong cùng một locale: `02/08/2026 17:11` (Users) · `Aug 2, 2026, 12:56 AM` (Support) · placeholder `mm/dd/yyyy` (date filter) | IA01-09 · Slides S13 p.26 / Nielsen H4 | 2 | Dùng một hàm format ngày chung, gắn với locale; ưu tiên `dd/MM/yyyy` | `evidence/C1/C1_IA01-09_two-date-formats-1-users.png` · `…-2-support.png` | 2026-08-04 |
| F-002 | Task 1B | C — C1 Users list (so với Events, Support) | Usability | Tiêu đề trang không nhất quán: Users/Events dùng `font-weight 700` + gạch chân cyan, không subtitle; Support dùng `800`, không gạch chân, có subtitle | IA01-01 · Nielsen H4 / Slides S13 p.16 | 1 | Tách tiêu đề trang thành component dùng chung có prop subtitle | `evidence/C1/C1_IA01-01_page-title-inconsistent-1-users.png` · `…-2-support.png` | 2026-08-04 |
| F-003 | Task 1B | C — C1 Users list (sidebar) | Bug | Sidebar thu gọn không có tooltip: 0/11 mục có `title`, 0/11 có `aria-label`, hover 3 s không ra node tooltip nào; 10/11 mục mất luôn `textContent` nên không còn tên cho screen reader | IA03-01 · Nielsen H1/H7 · Shneiderman R2 · Slides S13 p.17 | 2 | Thêm `title` + `aria-label` cho mọi mục sidebar, hoặc giữ nhãn trong DOM bằng visually-hidden | `evidence/C1/C1_IA03-01_collapsed-sidebar-no-tooltip.png` | 2026-08-04 |
| F-004 | Task 1B | C — C1 Users list | Usability | Bảng 7 cột không sort được cột nào: `[aria-sort]` = 0 phần tử, chỉ 2/7 header có control và cả hai là filter. 107 user / 22 trang mà không sắp xếp được theo tên hay ngày tạo | IA03-08 · Norman P1 · Slides S13 p.12, p.14 | 2 | Thêm sort cho `CREATED`, `UPDATED`, `USER`; phơi `aria-sort`; dùng icon mũi tên khác icon phễu | `evidence/C1/C1_IA03-08_seven-columns-zero-sort.png` | 2026-08-04 |
| F-005 | Task 1B | C — C1 Users list | Bug | `<select>` rows-per-page có option rỗng làm option đầu (`["","5","10","20","50","100"]`); khi option đó được chọn, nhãn phân trang render `NaN-NaN of 107 results` trong khi bảng vẫn hiện 5 dòng | IA03-06 (vế a) · Nielsen H4 | 2 | Bỏ option rỗng khỏi `<select>`; thêm giá trị mặc định phòng hờ để nhãn không bao giờ ra `NaN` | `evidence/C1/C1_IA03-06_label-shows-NaN-NaN.png` | 2026-08-04 |
| F-006 | Task 1B | C — C1 Users list (so với Events, Support) | Usability | Thang rows-per-page không khớp giữa các list: Users/Events = 5/10/20/50/100 mặc định 5; Support = 10/20/50/100 (thiếu 5) mặc định 20 | IA03-06 (vế b) · Nielsen H4 | 1 | Đưa thang và giá trị mặc định vào một hằng số dùng chung | `evidence/C1/C1_IA03-06_pagination-scale-differs.png` | 2026-08-04 |
| F-007 | Task 1B | C — C1 Users list | Bug | Bấm Back của trình duyệt làm mất trạng thái danh sách: đang ở trang 2 với rows=10 (`11-20 of 106`), sau Back thành `1-5 of 106` và rows tự về 5. URL không bao giờ đổi nên không có state để khôi phục | IA03-13 · Nielsen H3 · Slides S13 p.18 | 2 | Đưa page/rows/filter/search vào query string và đọc lại khi mount | `evidence/C1/C1_IA03-13_before-page2-rows10.png` · `…_after-back-reset-page1-rows5.png` | 2026-08-04 |
| F-008 | Task 1B | C — C1 Users list | Bug | Không tìm được user bằng tên đầy đủ đang hiển thị: query `test abc` → 0 kết quả ("No users found matching your filters") dù bảng đang hiển thị đúng chữ `test abc`; query `test` → 6 dòng, query `abc` → 1 dòng đúng user đó | **Không thuộc item nào** (checklist v1.9 thiếu item về ô search bảng dữ liệu) · Nielsen H6 | 3 | Cho search khớp trên tên đã ghép cả hai chiều, hoặc tách token và yêu cầu mọi token khớp ở bất kỳ trường nào | `evidence/C1/C1_F010_search-exact-displayed-name-0-results-1.png` · `…-2.png` | 2026-08-04 |
| F-009 | Task 1B | C — C1 Users list | Bug | Trong ~1 s sau khi gõ, bảng hiển thị kết quả của truy vấn cũ kèm nhãn khẳng định: tại 3 780 ms ô search đã hiện `test` nhưng bảng render 94 dòng và nhãn ghi `1-94 of 94 results`; tới 3 998 ms mới thành `1-6 of 6`. Không có spinner/skeleton | **Không thuộc item nào** (gần nhất IA01-07 nhưng item đó yêu cầu Slow 3G) · Nielsen H1 | 2 | Huỷ/bỏ qua response của request search cũ; hiển thị trạng thái đang tải | *(không có ảnh — trạng thái chỉ tồn tại ~0,2 s; bằng chứng là log lấy mẫu trong bug-reports.md)* | 2026-08-04 |
| F-010 | Task 1B | C — C2 Edit/Create User dialog | Bug | Nhãn `First Name` và `Last Name` bị gán ngược so với ô nhập. 3 nguồn độc lập cùng xác nhận: placeholder đảo; lỗi validation báo "Last name is required" dưới nhãn First Name; file export ghi `Last Name="BÙI QUANG"` trong khi dialog để giá trị đó dưới nhãn `First Name` | IA02-02 · Nielsen H6 · Slides S13 p.16 — Labels | 3 | Hoán lại 2 nhãn theo chuẩn của thông báo lỗi + header export; rà lại dữ liệu đã nhập trước khi sửa | `evidence/C2/C2_IA02-02_validation-messages-prove-labels-swapped.png` · `evidence/C2/C2_IA02-01_no-required-marker-and-swapped-labels.png` | 2026-08-04 |
| F-011 | Task 1B | C — C2 Edit/Create User dialog | Bug | 4 trường bắt buộc không có dấu hiệu nào: không `*` trong text, `::before`/`::after` = `none` trên cả 8 nhãn, `aria-required` = null toàn bộ, và cả 7 `<label>` đều `for=null` nên không liên kết với input. Chỉ trường **không** bắt buộc được đánh dấu (`Member Code (Optional)`) | IA02-01 · Norman P3/P6 · Slides S13 p.11 | 2 | Thêm marker bắt buộc nhìn thấy được + `aria-required="true"` + nối `<label for>` với `id` input | `evidence/C2/C2_IA02-01_no-required-marker-and-swapped-labels.png` | 2026-08-04 |
| F-012 | Task 1B | C — C2 Edit User dialog | Usability | Gõ `UNSAVED-EDIT-999` vào ô Phone Number rồi bấm ESC: dialog đóng ngay, không cảnh báo (không có chuỗi `unsaved\|discard\|are you sure\|lost` nào trên trang), thay đổi mất hẳn, không khôi phục được | IA02-13 · Nielsen H5 · Shneiderman R6 | 2 | Theo dõi trạng thái dirty; ESC/Cancel/X phải hỏi "Bỏ thay đổi?" kèm lựa chọn ở lại | `evidence/C2/C2_IA02-13_esc-discards-edit-silently-1-before.png` · `…-2-after.png` | 2026-08-04 |
| F-013 | Task 1B | C — C2 Create/Edit User dialog | Usability | Bấm Enter ở ô cuối form không kích hoạt hành động chính: dialog vẫn mở, 0 lỗi inline, không tạo user, không reload. Nguyên nhân: dialog không có phần tử `<form>` nên không có implicit submit | IA02-10 (ca b) · Norman P4 · Slides S13 p.18 | 2 | Bọc field trong `<form onSubmit>` và để nút chính `type="submit"` | `evidence/C2/C2_IA02-10_enter-does-nothing-on-form.png` | 2026-08-04 |
| F-014 | Task 1B | C — C4 Export to Excel | Bug | Export bỏ qua filter đang bật: màn hình đang lọc còn **1 dòng** (`1-1 of 1 results`) nhưng file chứa **105 dòng** — toàn bộ dataset; user đang lọc nằm ở dòng 38. Giao diện không nói phạm vi export là gì | IA04-13 · Assignment §5 C4 · Nielsen H1 | 3 | Cho export theo đúng filter đang bật; và nói rõ phạm vi ngay tại nút hoặc trong hộp xác nhận | `evidence/C4/C4_IA04-13_export-no-feedback-and-ignores-filter.png` · `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | 2026-08-04 |
| F-015 | Task 1B | C — C4 Export to Excel | Bug | File export thiếu cột `UPDATED` (có trên màn hình, không có trong file) và đổi tên `MEMBER CODE` thành `Card Code`, không khớp thuật ngữ giao diện | IA04-13 · Assignment §5 C4 — "column completeness" | 2 | Thêm cột `Updated At`; đổi `Card Code` → `Member Code` | `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | 2026-08-04 |
| F-016 | Task 1B | C — C4 Export to Excel | Bug | Giá trị cột Status trong file ghi bằng tiếng Việt (`Hoạt động`) trong khi giao diện hoàn toàn tiếng Anh (`Active`) và không đổi ngôn ngữ được; header file lại bằng tiếng Anh → một bảng trộn 2 ngôn ngữ | IA04-13 · Nielsen H4 | 1 | Cho phần sinh file dùng chung bộ chuỗi i18n với giao diện | `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | 2026-08-04 |
| F-017 | Task 1B | C — C4 Export to Excel | Usability | Tên file export là `users-export-1785667505695.xlsx` — dùng epoch mili-giây thay vì ngày đọc được | IA04-13 · Nielsen H1 · Shneiderman R3 | 1 | Đặt tên dạng `users-export-2026-08-02_1745.xlsx`; ghi luôn phạm vi filter nếu có | `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` | 2026-08-04 |
| F-018 | Task 1B | C — C2 Edit User dialog | Bug | Khi Save thất bại (offline), EMS **có** báo lỗi inline trong dialog và **không** có toast success giả — nhưng nội dung là chuỗi thô của Fetch API: **`Failed to fetch`**, không nói cái gì hỏng, không nói vì sao, không có nút retry | IA04-11 · Slides S13 p.11 · Nielsen H9 · Shneiderman R5 | 2 | Bắt lỗi mạng ở tầng gọi API, thay bằng thông báo theo ngữ cảnh + nút **Thử lại**; không để chuỗi lỗi JS thô lọt ra UI | `evidence/C2/C2_IA04-11_offline-save-failed-to-fetch.png` | 2026-08-04 |
| F-022 | Task 3 | C — C1 Users list (cross-platform, Safari/iOS/iPhone thật) | Bug | Sidebar không responsive trên viewport phone (828×1792): mặc định mở toàn bộ, che gần hết nội dung chính; sau khi thu gọn về icon-only vẫn tràn khỏi viewport (tiêu đề, nút Export bị cắt), vẫn phải cuộn ngang | Task 3 Coverage Fallback — Nielsen H4 (responsive layout), không map vào item checklist IA nào (checklist v1.9 không có item cross-platform) | 2 | Thêm breakpoint responsive cho viewport ≤ ~430–768px: sidebar mặc định thu gọn/drawer trên phone; nội dung chính dùng layout co giãn thay vì giữ độ rộng desktop | `hw3/out/reports/task-3-cross-platform/evidence/C1/T3_C1_RunF_iOS_Safari_Phone.png` · `..._supp1.png` · `..._supp2.png` | 2026-08-03 (submitted — exact timestamp not recorded) |

**Đường dẫn ảnh của F-001–F-018** tính tương đối từ `hw3/out/reports/checklist-execution/`. **F-022 (Task 3)** dùng đường dẫn đầy đủ riêng vì nằm ở thư mục Task 3 khác gốc.

## Đối soát ID F-019–F-021 (thực hiện 2026-08-03, trước khi thêm F-022)

Trước khi thêm F-022, đã rà soát toàn bộ repo (kể cả git history) để tìm mọi text-reference tới ID F-019, F-020, F-021 trong cách đánh số cũ (trước lần đánh số lại 2026-08-03).

- **F-021 (cũ) → xác minh trực tiếp, có thể giữ.** Git commit `5759c03` ("*IA04-11 scored Fail on C2 from student offline run; add F-021*") cộng với evidence path mô tả trong `hw3/docs/blockers.md` dòng 75 (`evidence/C2/C2_IA04-11_offline-save-failed-to-fetch.png`, mô tả lỗi `Failed to fetch`) khớp chính xác với evidence path và mô tả của **F-018 hiện tại**. Đây là bằng chứng trực tiếp (commit message + evidence path trùng khớp), không phải suy luận số học. `blockers.md` là file scratch chưa được cập nhật theo lần đánh số lại — không phải finding bị bỏ sót.
- **F-019, F-020 (cũ) → unresolved historical IDs.** Không tìm thấy text-reference trực tiếp nào trong repo hay git history xác định được tiêu đề, evidence, trạng thái submit, hay ánh xạ hiện hành của hai ID này. **Không dựng lại dòng nào cho F-019/F-020 vì làm vậy sẽ là suy đoán.** F-022 giữ nguyên không đổi vì ID đó đã được dùng nhất quán trong Google Form submission và các artifact Task 3.
- **Về phép tính 21 − 3 = 18:** đây **chỉ là một kiểm tra tổng số (consistency check về số lượng)**, không phải bằng chứng rằng F-019/F-020 cụ thể đã được submit dưới ID mới nào. Phép tính xác nhận số *lượng* dòng khớp (21 slot cũ, loại 3, còn 18) — nó không và không thể xác định *danh tính* nội dung của hai slot ID cụ thể đó. Hai điều này khác nhau: khớp tổng số không đồng nghĩa đã xác minh từng ID.
- **Kết luận:** F-021(cũ)→F-018 giữ nguyên (có bằng chứng trực tiếp). F-019, F-020 (cũ) ở trạng thái **unresolved historical IDs** — không có bằng chứng, không suy đoán, không đóng hồ sơ giả định là "đã giải thích". F-022 là ID hợp lệ tiếp theo sau F-018, không phụ thuộc vào việc F-019/F-020 có được giải quyết hay không.

## Thống kê nhanh

| Chỉ số | Giá trị |
| --- | --- |
| Tổng finding | **19** (18 Task 1B + 1 Task 3) |
| Type = Bug | **12** (+F-022) |
| Type = Usability | **7** |
| Severity 4 (Catastrophe) | 0 |
| Severity 3 (Major) | **3** — F-008, F-010, F-014 |
| Severity 2 (Minor) | **12** (+F-022) |
| Severity 1 (Cosmetic) | **4** — F-002, F-006, F-016, F-017 |
| Truy được về một item checklist | **16** |
| **Không** thuộc item nào | **3** — F-008, F-009, F-022 (F-022 không map vào checklist Task 1 vì là finding cross-platform của Task 3) |

## Đối soát (Task 1B — điền ở Step 12)

| Kiểm tra | Kết quả |
| --- | --- |
| Số dòng trong bảng này (Task 1B) | **18** |
| Số lần submit Form (đếm từ email xác nhận / bản ghi riêng) | **18** — nộp bằng email `MSSV@....edu.vn` ngày 2026-08-04 |
| Hai số trên khớp? | ✅ **Khớp tuyệt đối — 18 = 18.** |
| Mọi dòng đều có Screenshot ref? | **17/18.** F-009 cố ý không có ảnh: trạng thái lỗi chỉ tồn tại ~0,2 s nên không chụp kịp; bằng chứng thay thế là log lấy mẫu theo mốc thời gian, ghi trong `bug-reports.md` và tái hiện được bằng các bước đã mô tả |
| Mọi dòng đều có Form timestamp? | ✅ **18/18** |

## Đối soát (Task 3 — bổ sung 2026-08-03)

| Kiểm tra | Kết quả |
| --- | --- |
| Số dòng Task 3 trong bảng này | **1** (F-022) |
| Số lần submit Form (Task 3) | **1** — nộp bằng email `23127179@student.hcmus.edu.vn` ngày 2026-08-03, xác nhận qua ảnh "Your response has been recorded" |
| Hai số trên khớp? | ✅ **Khớp — 1 = 1.** |
| F-022 có Screenshot ref? | ✅ 3 ảnh (primary + 2 supplementary) |
| F-022 có Form timestamp chính xác? | ⚠️ **Không có giờ:phút chính xác** — ảnh xác nhận submit không hiển thị timestamp, chỉ có ngày theo phiên làm việc (2026-08-03). Ghi `submitted — exact timestamp not recorded` thay vì suy đoán giờ |

## Đối soát tổng hợp (toàn bộ 19 dòng, sửa 2026-08-03 sau phản hồi review)

Bảng dưới đây thay thế phát biểu cũ "19 = 19 khớp tuyệt đối". Phát biểu đó gộp chung hai loại bằng chứng có độ tin cậy khác nhau (F-022 có screenshot xác nhận trong phiên này; 18 dòng Task 1B chỉ được ghi nhận lại từ artifact khác) như thể chúng ngang hàng. Tách lại theo 4 cột:

| Hạng mục | Số dòng | Ghi chú |
| --- | --- | --- |
| Dòng trong working log (bảng findings ở trên) | **19** | 18 Task 1B (F-001–F-018) + 1 Task 3 (F-022). Đây là số dòng thực tế đếm được trong file này, không phải số lần submit. |
| Submission được **xác minh trực tiếp** trong phiên hiện tại | **1** — F-022 | Xác nhận qua screenshot Google Form "Your response has been recorded" mà người dùng gửi trong phiên Task 3 này. |
| Submission được **ghi nhận bởi artifact Task 1 trước đó** (chưa re-verify độc lập ở đây) | **18** — F-001–F-018 | Ngày `2026-08-04` xuất hiện nhất quán ở 4 nguồn độc lập: `README.md` dòng 157/193, toàn bộ 18 hàng "Form submitted" trong `bug-reports.md`, AI Audit Report (mục 3.3 và tuyên bố ký tên của sinh viên), và chính `findings-log.md` (mục "Đối soát Task 1B — điền ở Step 12"). Không có screenshot Form-confirmation nào cho 18 dòng này được kiểm tra lại trong phiên Task 3 — khác với F-022. Ghi nhận này có cơ sở (4 nguồn khớp nhau, do sinh viên tự ký xác nhận trách nhiệm trong AI Audit Report) nhưng không nên gọi là "trực tiếp xác minh" trong ngữ cảnh phiên làm việc hiện tại. |
| Đang chờ đối soát cuối kỳ (Final Submission Integration) | **19** | Toàn bộ 19 dòng sẽ được đối chiếu lại một lần cuối (kể cả F-022) khi gộp Task 1+2+3 vào submission cuối kỳ — đây là giai đoạn K2 trong Definition of Done, khác với K1 (Task 3 Execution Done) đã hoàn tất. |

**Ngày `2026-08-04` cho 18 finding Task 1B:** không bị thay bằng ngày khác — không có bằng chứng nào cho thấy ngày này sai, chỉ là chưa có screenshot độc lập trong phiên này để nâng nó lên mức "trực tiếp xác minh". Trạng thái đúng: **"recorded as submitted in Task 1 artifacts — pending final Form reconciliation"**, không phải "verified" và cũng không phải ngày khác do đoán.

## Các trường của Google Form và cách đã map dữ liệu (ghi lại cho audit trail)

Form của khoa (tiêu đề *"Phản hồi từ phía người dùng cho hệ thống quản lý sự kiện khoa CNTT"*) được thiết kế giống một phiếu khảo sát người dùng chung chung hơn là một form theo dõi lỗi (bug tracker) chuyên nghiệp. Theo §7, đây là kênh nộp bug bắt buộc; mục này ghi lại cách 18 finding đã được dán vào form ngày 2026-08-04, để người chấm đối chiếu được với nội dung `bug-reports.md`.

1. **Tốc độ tải trang của hệ thống như thế nào?** → Chọn *Bình thường*, vì báo cáo tập trung vào UI/UX chứ không phải performance.
2. **Trong quá trình sử dụng, bạn có gặp lỗi nào không?** → *Có*.
3. **Nếu có, vui lòng mô tả lỗi bạn gặp phải.** → Dán *toàn bộ* nội dung của finding tương ứng trong `bug-reports.md` (bảng thông tin ID, Severity, Steps to reproduce, Expected, Actual, Suggested fix), không chỉ dán tiêu đề.
4. **Hình ảnh / video lỗi mà bạn gặp phải** → Upload file ảnh tương ứng từ thư mục `evidence/`.
5. **Điều bạn thích nhất... / Điều gì khiến bạn chưa hài lòng... / Bạn mong muốn...** → Điền *"N/A - Đây là báo cáo bug/usability cho Task 1B"* ở các câu bắt buộc; bỏ trống câu không bắt buộc.

**Ngoại lệ đã xử lý:** F-009 không có ảnh do trạng thái lỗi chỉ tồn tại ~0,2 s; đính kèm log lấy mẫu (`.txt`) thay cho ảnh ở câu 4.

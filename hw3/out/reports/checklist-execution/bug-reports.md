# Bug Reports — Task 1B (Scenario C)

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Nguồn:** các item bị **Fail** trong `C1.md` … `C4.md`
**Nguyên tắc:** mỗi bug ở đây phải (1) xuất phát từ một item Fail có thật, (2) có screenshot, (3) có 1 dòng tương ứng trong `hw3/work/findings-log.md`, (4) đã submit lên Google Form.

---

## Quy tắc chuyển Fail → Bug

Không phải mọi `Fail` đều thành **một** bug report.

| Tình huống | Xử lý |
| --- | --- |
| 3 item Fail vì **cùng một nguyên nhân gốc** trên **cùng một màn hình** | Gộp thành **1 bug**, liệt kê cả 3 item ID trong trường *Checklist items* |
| Cùng một lỗi xuất hiện trên **nhiều màn hình** | **1 bug**, phần *Screen* ghi tất cả màn hình bị ảnh hưởng |
| Item Fail nhưng không phải "sai", mà là "thiết kế gây khó" (vd: không có sort trên bảng 7 cột) | Vẫn log, nhưng **Type = Usability**, không phải Bug |
| Item Fail vì môi trường (mạng rớt, dữ liệu vừa bị reset) | **Không** phải bug. Chạy lại item. |

## Thang Severity (dùng chung cho cả Bug và Usability)

Dùng thang **Nielsen 0–4** cho mọi finding, vì §6 Task 2 bắt buộc thang 0–4 và findings log là **một** file trộn cả Bug lẫn Usability — hai thang khác nhau trong một cột sẽ không so sánh được.

| Mức | Tên | Nghĩa | Ví dụ trên scenario C |
| --- | --- | --- | --- |
| **4** | Catastrophe | Mất/lộ dữ liệu, hành động sai đối tượng, hoặc chặn hoàn toàn công việc | Nút Block khoá nhầm user khác; export lộ dữ liệu không được phép |
| **3** | Major | Cản trở nghiêm trọng, có workaround nhưng khó tìm | Toast báo "thành công" nhưng thay đổi không được lưu |
| **2** | Minor | Gây bực bội, làm chậm, nhưng vẫn hoàn thành được việc | Phân trang ghi "1–20 of 45" trong khi chỉ render 18 dòng |
| **1** | Cosmetic | Lệch thẩm mỹ/nhất quán, không ảnh hưởng thao tác | Icon sidebar khác stroke width |
| **0** | Not a problem | Không phải vấn đề | — |

**Cách quyết định nhanh — hỏi 3 câu theo thứ tự:**
1. Có làm sai/mất dữ liệu, hoặc tác động nhầm record không? → **4**
2. Có làm người dùng **không hoàn thành được** việc, hoặc tin vào một kết quả sai không? → **3**
3. Có làm chậm/khó chịu nhưng vẫn xong việc không? → **2**, ngược lại → **1**

Nếu phân vân giữa hai mức: chọn mức **thấp hơn** và ghi lý do vào Notes. Thổi phồng severity là thứ TA phát hiện được, và nó làm giảm độ tin của cả log.

---

## Mẫu bug report — copy khối dưới cho mỗi bug

```markdown
### BUG-C-00N — <tiêu đề ngắn, mô tả triệu chứng, không mô tả nguyên nhân>

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | IA03-06 |
| **Type** | Bug (hoặc Usability) |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome 1xx / Windows 11 |
| **Ngày phát hiện** | yyyy-mm-dd |
| **Findings-Log-ID** | F-00N |
| **Form submitted** | yyyy-mm-dd hh:mm |

**Steps to reproduce**
1. Đăng nhập bằng `admin@gmail.com`
2. Mở Users Management
3. …

**Expected**
<Hành vi mong đợi. Trích từ cột *Expected Behavior* của item checklist, hoặc từ heuristic được cite — KHÔNG suy từ code.>

**Actual**
<Cái thực sự thấy, kèm số đo cụ thể.>

**Evidence**
`evidence/C1/C1_IA03-06_pagination-sai.png`

**Suggested fix**
<1–2 câu. Đề xuất hướng, không viết code.>
```

---

## Danh sách bug

**20 finding**, đánh số `F-001`…`F-020` — dùng chung ID với `hw3/work/findings-log.md` để một finding chỉ có **một** mã duy nhất xuyên suốt bug report → findings log → Google Form.

| Nguồn | Số finding |
| --- | --- |
| Từ item Fail có trong checklist | **18** |
| **Không** thuộc item nào trong 60 item (phát hiện trong lúc chạy) | **2** — F-010, F-011 |

> **Hai finding không map được vào item nào.** F-010 và F-011 đều là lỗi thật, tái hiện được, nhưng checklist v1.9 **không có item nào nói về ô search của bảng dữ liệu**. Chúng vẫn được báo cáo và vẫn nên submit lên Google Form (§7 nhận bug bất kể có thuộc checklist hay không), và khoảng trống này được ghi lại như một đề xuất cho **v2.0** trong `README.md`. Gán chúng vào một item không liên quan chỉ để "có mã item" sẽ là gán sai bằng chứng.

**Phân bố severity:** `4` → 0 · `3` → 5 · `2` → 11 · `1` → 4 · `0` → 0.
**Không có finding nào ở mức 4.** Trong phiên này không quan sát được trường hợp nào mất dữ liệu, tác động nhầm record, hay chặn hoàn toàn công việc. Mức cao nhất là 3.

---

### F-001 — Nút chuyển ngôn ngữ EN/VI trên header không có tác dụng gì

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list (control ở header, ảnh hưởng toàn bộ khu admin) |
| **Checklist items** | IA01-08 · IA01-09 (vế "không đổi được locale") |
| **Type** | Bug |
| **Severity** | 3 — Major |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-001 |
| **Form submitted** | _(chưa submit — xem findings-log.md)_ |

**Steps to reproduce**
1. Đăng nhập `admin@gmail.com` tại https://prod-dev.ems-fitus.cloud/login
2. Mở **Users Management**
3. Bấm nút cờ (`aria-label="Switch language"`) ở góc trên bên phải header
4. Chờ 6 giây, quan sát sidebar, header bảng, ô search và tiêu đề tab trình duyệt
5. Lặp lại bước 3–4 thêm 2 lần nữa

**Expected**
Theo IA01-08 (Slides S13 p.26 — Localization / Nielsen H4): *"The toggle sits in the same header position everywhere and switches **all** static labels, leaving no untranslated string or raw translation key — the `<title>` included."*

**Actual**
Không có gì thay đổi sau cả 3 lần bấm. Đo sau lần bấm thứ 3:
- `document.documentElement.lang` = `"en"` (không đổi)
- `document.title` = `"Admin Management | HCMUS EMS"` (không đổi)
- 7 label sidebar, 7 header bảng, placeholder `Search users...` — vẫn tiếng Anh
- icon cờ vẫn là cờ Mỹ; **không** có dropdown chọn ngôn ngữ nào mở ra
- `localStorage` và `document.cookie`: **không** có key nào khớp `lang|locale|NEXT_LOCALE`

Nghĩa là toàn bộ khu admin của EMS **không dùng được bằng tiếng Việt**, dù giao diện có một nút hứa hẹn điều đó.

**Evidence**
`evidence/C1/C1_IA01-08_language-toggle-no-effect.png`

**Suggested fix**
Nối nút này vào provider i18n thật (đặt locale + ghi cookie/localStorage + re-render); hoặc nếu bản dịch tiếng Việt chưa sẵn sàng thì **ẩn nút đi**. Một control hứa chức năng không tồn tại còn tệ hơn là không có control.

---

### F-002 — Ngày giờ hiển thị theo hai định dạng khác nhau giữa các màn hình admin

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list (so với Support request management) |
| **Checklist items** | IA01-09 |
| **Type** | Usability |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users · …/dashboard/admin/complaints |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-002 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, đọc cột `CREATED` / `UPDATED`
2. Mở **Support requests**, đọc cột `TIME`
3. Trong panel **Filters** của Support requests, xem placeholder của 2 ô `From date` / `To date`

**Expected**
Theo IA01-09 (Slides S13 p.26 / Nielsen H4): ngày giờ và số phải render theo **một** quy ước của locale đang chọn, không phải mỗi màn hình một kiểu.

**Actual**
Ba quy ước cùng tồn tại trong cùng một phiên, cùng một locale:
- Users Management: `02/08/2026 17:11` — `dd/MM/yyyy`, 24 giờ
- Support request management: `Aug 2, 2026, 12:56 AM` — kiểu Mỹ, 12 giờ AM/PM
- Ô date filter native của Support requests: placeholder `mm/dd/yyyy` — thứ tự tháng/ngày kiểu Mỹ

Với một ngày như `02/08` thì hai cách đọc lệch nhau **6 tháng** (2 tháng 8 so với 8 tháng 2), và không có gì trên màn hình nói cho người dùng biết đang dùng quy ước nào.

Ghi lại vế **đạt** để không thổi phồng: **không** thấy raw ISO timestamp nào lọt ra giao diện.

**Evidence**
`evidence/C1/C1_IA01-09_two-date-formats-1-users.png` · `evidence/C1/C1_IA01-09_two-date-formats-2-support.png`

**Suggested fix**
Chuẩn hoá về một hàm format ngày dùng chung cho toàn app, gắn với locale đang chọn. Ưu tiên `dd/MM/yyyy` vì đây là hệ thống của một trường đại học Việt Nam.

---

### F-003 — Kiểu tiêu đề trang không nhất quán giữa các màn hình admin

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list (so với Events Management và Support request management) |
| **Checklist items** | IA01-01 |
| **Type** | Usability |
| **Severity** | 1 — Cosmetic |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-003 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở lần lượt **Users Management** → **Events Management** → **Support requests**
2. Mỗi lần, quan sát tiêu đề trang: độ đậm chữ, có gạch chân accent hay không, có dòng mô tả phụ hay không

**Expected**
Theo IA01-01 (Nielsen H4 — Consistency and Standards / Slides S13 p.16): *"one page-title style system-wide"*.

**Actual**
Ba màn hình, hai kiểu:

| Màn hình | font-weight | Gạch chân accent | Subtitle |
| --- | --- | --- | --- |
| Users Management | 700 | có (cyan) | không |
| Events | 700 | có (cyan) | không |
| Support request management | **800** | **không** | **có** — "Review and respond to support requests." |

**Evidence**
`evidence/C1/C1_IA01-01_page-title-inconsistent-1-users.png` · `evidence/C1/C1_IA01-01_page-title-inconsistent-2-support.png`

**Suggested fix**
Tách tiêu đề trang thành một component dùng chung, có prop tuỳ chọn cho subtitle, để cả 3 màn hình render qua cùng một đường.

---

### F-004 — Focus bàn phím không vào dialog khi dialog mở; ô "Go to page" không có dấu hiệu focus nào

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list · C2 Edit User dialog · C3 Delete User confirm dialog |
| **Checklist items** | IA01-12 (trên cả C1, C2 và C3) |
| **Type** | Bug (accessibility) |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-004 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
*Phần A — ô "Go to page":*
1. Mở **Users Management**
2. Bấm `Tab` liên tục từ đầu trang, không dùng chuột
3. Khi focus tới ô `Go to page` ở thanh phân trang, nhìn xem có viền/ring nào hiện ra không

*Phần B — dialog:*
4. Bấm nút **Edit user** (rồi làm lại với **Delete user**) trên một dòng
5. Khi dialog đã mở, kiểm `document.activeElement`

**Expected**
Theo IA01-12 (WCAG 2.1 SC 2.4.7 — Focus Visible): *"Every focused element shows a clearly visible focus ring… focus order follows a logical reading order."* Với dialog, focus phải được chuyển vào trong dialog để người dùng bàn phím thao tác được ngay.

**Actual**
*Phần A.* Ô `Go to page` nhận focus bàn phím nhưng **không vẽ gì cả**:
`outline: 0.872727px solid rgba(0, 0, 0, 0)` (alpha = 0, trong suốt hoàn toàn) · `border-width: 0px` · `box-shadow: none` · nền không đổi.
Để đối chiếu, cùng lần Tab đó ghi nhận các phần tử khác **có** ring nhìn rõ: nút phân trang `2` → `outline auto rgb(54,65,83)`; link sidebar `Categories` → `outline 2.6px auto rgb(153,161,175)`.
Ngoài ra `<table>` và **từng `<tr>`** cũng nhận focus dù không phải control tương tác — thêm các điểm dừng vô nghĩa vào thứ tự Tab.

*Phần B.* Mở dialog Edit User: `document.activeElement` = `BUTTON[aria-label="Edit user"]`, `dialog.contains(document.activeElement)` = **`false`**. Mở dialog Delete User: `document.activeElement` = `BUTTON[aria-label="Delete user"]`, cũng **`false`**. Focus **không bao giờ** vào trong dialog và không có focus trap. Cả hai dialog cũng không có accessible name (`aria-label` = `null`, `aria-labelledby` = `null`) dù đã khai `role="dialog" aria-modal="true"`.

Trường hợp đáng lo nhất là **dialog xoá**: người dùng bàn phím không được đặt sẵn lên `Cancel` (mặc định an toàn) mà bị bỏ lại ở đúng nút vừa bấm, phía sau lớp overlay.

**Evidence**
`evidence/C1/C1_IA01-12_go-to-page-focus-invisible.png` · `evidence/C2/C2_IA01-12_focus-stays-outside-dialog.png` · `evidence/C3/C3_IA01-12_focus-not-moved-into-delete-dialog.png`

**Suggested fix**
(1) Cho ô `Go to page` dùng cùng style focus với các input khác. (2) Khi dialog mở, đặt focus vào phần tử đầu tiên trong dialog — với dialog xoá thì đặt lên `Cancel` — giữ focus trong dialog (focus trap), và trả focus về nút đã mở khi đóng. (3) Bỏ `tabindex` khỏi `<table>`/`<tr>`. (4) Thêm `aria-labelledby` trỏ tới tiêu đề dialog.

---

### F-005 — Sidebar thu gọn không có tooltip; các mục mất hẳn tên

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list (sidebar dùng chung toàn khu admin) |
| **Checklist items** | IA03-01 |
| **Type** | Bug (accessibility / usability) |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-005 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**
2. Bấm **Collapse** ở đáy sidebar
3. Rê chuột lên từng icon và giữ yên 3 giây

**Expected**
Theo IA03-01 (Nielsen H1 / H7 / Shneiderman R2 / Slides S13 p.17): *"Collapsed, the sidebar becomes icon-only yet stays fully navigable (icons clickable, **tooltips present**) and expands again — all nine destinations remain reachable in one click in both states."*

**Actual**
Sidebar thu gọn đúng và 9 đích vẫn click được, **nhưng không có tooltip nào**:
- **0/11** mục có thuộc tính `title`
- **0/11** mục có `aria-label`
- Rê chuột lên icon `Categories` giữ 3 giây → **0** node `[role=tooltip]`, `.tooltip` hay `[data-tooltip]`; chuỗi "Categories" xuất hiện **0 lần** trong text nhìn thấy được
- Ở trạng thái thu gọn đã ổn định, **10/11** mục có `textContent` **rỗng** — tức các mục (gồm `Analytics` và `Settings`) không còn tên gọi nào, kể cả cho screen reader

Sau khi thu gọn, người dùng phải nhớ 9 icon nghĩa là gì, và người dùng screen reader mất khả năng điều hướng sidebar.

**Evidence**
`evidence/C1/C1_IA03-01_collapsed-sidebar-no-tooltip.png`

**Suggested fix**
Thêm `title` **và** `aria-label` cho mỗi mục sidebar (luôn có, không chỉ khi thu gọn), hoặc giữ nhãn text trong DOM và ẩn bằng kỹ thuật visually-hidden thay vì xoá khỏi cây.

---

### F-006 — Bảng Users 7 cột không sắp xếp được theo cột nào

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | IA03-08 |
| **Type** | Usability |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-006 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**
2. Bấm thử vào từng tiêu đề cột: `USER`, `MEMBER CODE`, `CREATED`, `UPDATED`
3. Kiểm trong DevTools: `document.querySelectorAll('[aria-sort]')`

**Expected**
Theo IA03-08 (Norman P1 / Slides S13 p.12, p.14): *"For a table this wide, a **complete absence of sorting** is a usability finding, not a pass."*

**Actual**
`document.querySelectorAll('[aria-sort]').length` = **0** trên toàn trang. Chỉ **2/7** tiêu đề có control (icon phễu ở `Role` và `Status`) và cả hai đều là **filter**. Năm cột còn lại — `USER`, `MEMBER CODE`, `CREATED`, `UPDATED`, `ACTIONS` — không có control nào; bấm vào tiêu đề không có phản ứng.

Với 107 user trải trên 22 trang (rows-per-page = 5), không có cách nào sắp xếp theo ngày tạo hay theo tên; admin muốn tìm user mới nhất phải lật từng trang.

Ghi lại hai vế **đạt** của cùng item để không thổi phồng: icon phễu **có** đổi hình khi filter đang bật, và filter **sống qua phân trang**.

**Evidence**
`evidence/C1/C1_IA03-08_seven-columns-zero-sort.png`

**Suggested fix**
Thêm sort cho ít nhất `CREATED`, `UPDATED` và `USER`; dùng `aria-sort` để phơi trạng thái sắp xếp; dùng icon mũi tên (khác hẳn icon phễu) để phân biệt sort với filter.

---

### F-007 — Nhãn phân trang hiện "NaN-NaN of 107 results" khi option rỗng của rows-per-page được chọn

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | IA03-06 (vế a — nhãn phải đúng số học) |
| **Type** | Bug |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-007 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**
2. Bấm vào dropdown **Rows per page** ở thanh phân trang để mở nó
3. Bấm `Esc` để đóng dropdown, rồi bấm `Tab`
   *(Cách trực tiếp hơn: chọn option **đầu tiên** — option rỗng — của `<select>` đó.)*
4. Đọc nhãn ở giữa thanh phân trang

**Expected**
Theo IA03-06 (Nielsen H4): *"each label is arithmetically true — it states a range matching the rows displayed and the real total"*. Nhãn phân trang phải luôn là một khoảng số hợp lệ.

**Actual**
Nhãn hiện **`NaN-NaN of 107 results`** — giá trị `NaN` thô của JavaScript lọt thẳng ra giao diện. Cùng lúc, ô `Rows per page` hiển thị **trống**, còn bảng vẫn render **5 dòng**.

Nguyên nhân quan sát được ở DOM: `<select>` rows-per-page **xuất xưởng kèm một option rỗng làm option đầu tiên** — `[...select.options].map(o => o.value)` trả về `["", "5", "10", "20", "50", "100"]`. Khi option `""` được chọn, phép tính khoảng trang chạy trên một giá trị không phải số.

Với các giá trị bình thường thì nhãn hoàn toàn đúng — đã đếm tay và khớp ở 3 mốc: `1-5 of 105` với 5 dòng, `1-100 of 105` với đúng 100 dòng, `101-105 of 105` với đúng 5 dòng.

**Evidence**
`evidence/C1/C1_IA03-06_label-shows-NaN-NaN.png`

**Suggested fix**
Bỏ option rỗng khỏi `<select>` rows-per-page (nó không có công dụng gì) và thêm giá trị mặc định phòng hờ khi state rows-per-page không phải số, để nhãn không bao giờ render `NaN`.

---

### F-008 — Thang "rows per page" và giá trị mặc định khác nhau giữa các danh sách

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list (so với Events Management và Support request management) |
| **Checklist items** | IA03-06 (vế b — các list phải nhất quán) |
| **Type** | Usability |
| **Severity** | 1 — Cosmetic |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-008 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, mở dropdown `Rows per page`, ghi lại các lựa chọn và giá trị đang chọn
2. Làm lại với **Events Management**
3. Làm lại với **Support requests**

**Expected**
Theo IA03-06 vế (b) (Nielsen H4): *"the five lists agree — same rows-per-page scale, same label wording, same control set, same position."*

**Actual**

| Danh sách | Thang rows-per-page | Mặc định |
| --- | --- | --- |
| Users Management | 5 / 10 / 20 / 50 / 100 | **5** |
| Events Management | 5 / 10 / 20 / 50 / 100 | **5** |
| Support request management | **10** / 20 / 50 / 100 — *thiếu lựa chọn 5* | **20** |

Cách viết nhãn (`1-6 of 6 results`), bộ control (`Go to page` + nút số trang) và vị trí (thanh dưới cùng) thì giống nhau — chỉ thang và mặc định là lệch.

**Evidence**
`evidence/C1/C1_IA03-06_pagination-scale-differs.png`

**Suggested fix**
Đưa thang rows-per-page và giá trị mặc định vào một hằng số dùng chung cho mọi bảng.

---

### F-009 — Nút Back của trình duyệt làm mất vị trí trang và thiết lập rows-per-page

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | IA03-13 |
| **Type** | Bug |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-009 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**
2. Đặt `Rows per page` = **10**
3. Sang **trang 2** — nhãn lúc này đọc `11-20 of 106 results`
4. Bấm **Categories** trên sidebar (hoặc mở màn hình admin bất kỳ khác)
5. Bấm nút **Back** của trình duyệt
6. Đọc lại nhãn phân trang và ô `Rows per page`

**Expected**
Theo IA03-13 (Nielsen H3 / Slides S13 p.18): *"Back returns to the list with filter and page still applied — not to an unfiltered page 1."*

**Actual**
Sau khi Back:
- nhãn thành **`1-5 of 106 results`** (đáng lẽ `11-20 of 106 results`)
- bảng render **5 dòng** (đáng lẽ 10)
- ô `Rows per page` **tự về 5** (đáng lẽ giữ 10)

Mất cả vị trí trang lẫn thiết lập rows-per-page. Nguyên nhân quan sát được: **URL không bao giờ đổi** — suốt quá trình luôn là `/dashboard/admin/users`, không có query string mang page/filter/rows, nên Back không có gì để khôi phục.

Hệ quả thực tế: admin đang duyệt trang 15/22 mà lỡ mở nhầm một màn hình khác thì phải bấm lại từ đầu.

**Evidence**
`evidence/C1/C1_IA03-13_before-page2-rows10.png` · `evidence/C1/C1_IA03-13_after-back-reset-page1-rows5.png`

**Suggested fix**
Đưa page / rows-per-page / filter / search vào query string của URL và đọc lại từ đó khi mount. Việc này đồng thời làm danh sách chia sẻ được bằng link — hiện giờ không chia sẻ được.

---

### F-010 — Không tìm được user bằng chính tên đầy đủ đang hiển thị của họ

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | **Không thuộc item nào** — checklist v1.9 không có item về ô search của bảng dữ liệu |
| **Type** | Bug |
| **Severity** | 3 — Major |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-010 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**
2. Tìm trong bảng một user có tên hiển thị gồm 2 từ — ví dụ dòng hiển thị đúng chữ **`test abc`**
3. Gõ **`test abc`** (nguyên văn tên đang hiển thị) vào ô `Search users...`
4. Chờ ~8 giây cho kết quả ổn định
5. Để đối chiếu, xoá đi rồi gõ lần lượt `test`, rồi `abc`

**Expected**
Gõ đúng tên đang hiển thị của một record thì phải tìm ra record đó. Đây là kỳ vọng cơ bản nhất của một ô search (Nielsen H6 — Recognition Rather Than Recall: người dùng nhận ra cái tên trên màn hình và gõ lại nó, chứ không phải nhớ xem tên đó được lưu tách thành mấy trường).

**Actual**
- `test abc` → **`No users found matching your filters.`**, **0 dòng** — trong khi dòng đó đang hiển thị đúng chữ `test abc` ngay trước đó
- `test` → **6 dòng**, có chứa user đó ✓
- `abc` → **1 dòng**, đúng user đó ✓

Search khớp được từng token riêng lẻ nhưng **không khớp được chuỗi "họ + tên" mà chính giao diện đang hiển thị** — nhiều khả năng vì tên được lưu tách thành `firstName`/`lastName` và truy vấn so chuỗi tìm kiếm với từng trường riêng, không so với tên đã ghép.

Với bảng 107 user và không có sort (F-006), search là công cụ tìm chính; gõ đúng tên nhìn thấy mà báo "không có" khiến admin tin rằng user đó không tồn tại.

**Evidence**
`evidence/C1/C1_F010_search-exact-displayed-name-0-results-1.png` (query `test abc` → 0 kết quả) · `evidence/C1/C1_F010_search-exact-displayed-name-0-results-2.png` (query `abc` → tìm ra đúng user đó)

**Suggested fix**
Cho search so khớp trên tên đã ghép (`firstName + ' ' + lastName` **và** `lastName + ' ' + firstName`), hoặc tách chuỗi tìm kiếm theo khoảng trắng rồi yêu cầu mọi token đều khớp ở bất kỳ trường nào.

---

### F-011 — Bảng hiển thị kết quả cũ kèm số đếm khẳng định, không có chỉ báo đang tải

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | **Không thuộc item nào** — gần nhất là IA01-07, nhưng item đó yêu cầu kịch bản Slow 3G, còn lỗi này quan sát được trên mạng bình thường |
| **Type** | Bug |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-011 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, để ô search trống (107 kết quả)
2. Gõ **`test`** vào ô search với tốc độ gõ bình thường
3. Quan sát nhãn phân trang và số dòng trong khoảng **3–4 giây** ngay sau khi gõ xong

**Expected**
Theo Nielsen H1 — Visibility of System Status: trong lúc dữ liệu đang tải, giao diện phải cho biết là **đang tải**; không được hiển thị dữ liệu của một truy vấn khác như thể đó là kết quả cuối cùng.

**Actual**
Đo bằng cách gắn interval lấy mẫu mỗi 200 ms trong lúc gõ:

```
3780 ms  q='test'  label='1-94of94results'  rows=94
3998 ms  q='test'  label='1-6of6results'    rows=6
```

Tại mốc 3,78 giây — khi ô search **đã hiện đủ chữ `test`** — bảng render **94 dòng** và nhãn ghi **`1-94 of 94 results`**. Đó là kết quả của một tiền tố ngắn hơn còn sót lại. Nhãn này **tự nó nhất quán về số học** (94 dòng, ghi 94) nên không có gì gợi ý rằng nó sai; không có spinner, không có skeleton, không làm mờ bảng. Đến 4,0 giây nó mới đổi thành kết quả đúng `1-6 of 6 results`.

Trong gần một giây, giao diện khẳng định chắc chắn một con số sai cho truy vấn đang hiển thị.

**Evidence**
Không có ảnh — trạng thái chỉ tồn tại ~0,2 s nên chụp bằng tay không kịp. Bằng chứng là log lấy mẫu ở trên, tái hiện được bằng đúng các bước trong *Steps to reproduce*. *(Ghi rõ điều này thay vì gán một ảnh không thể hiện đúng khoảnh khắc đó.)*

**Suggested fix**
Huỷ hoặc bỏ qua response của các request search cũ (đánh số request, chỉ nhận response mới nhất), và hiển thị trạng thái đang tải (làm mờ bảng hoặc skeleton) từ lúc gõ tới lúc có kết quả.

---

### F-012 — Nhãn "First Name" và "Last Name" bị gán ngược so với ô nhập tương ứng

| Trường | Nội dung |
| --- | --- |
| **Screen** | C2 Edit User dialog · dialog Create New User |
| **Checklist items** | IA02-02 |
| **Type** | Bug |
| **Severity** | 3 — Major |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-012 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, bấm **+ Add User**
2. Nhìn ô nằm dưới nhãn **`First Name`** → placeholder của nó ghi **`Last Name`**; ô dưới nhãn `Last Name` có placeholder `First Name`
3. Bấm **Create User** khi form còn trống → đọc thông báo lỗi dưới từng ô
4. Đối chiếu độc lập: bấm **Export**, mở file `.xlsx`, so cột `First Name` / `Last Name` của một user với dialog **Edit user** của chính user đó

**Expected**
Theo IA02-02 (Nielsen H6 — Recognition Rather Than Recall / Slides S13 p.16 — Labels): nhãn của một ô phải gọi đúng dữ liệu mà ô đó chứa. Đây là chức năng tối thiểu của một nhãn.

**Actual**
**Ba nguồn độc lập đều nói nhãn sai:**

1. **Placeholder** — ô dưới nhãn `First Name` có placeholder `Last Name`, và ngược lại.
2. **Thông báo lỗi validation** — submit form rỗng: ô dưới nhãn `First Name` báo **`Last name is required`**; ô dưới nhãn `Last Name` báo **`First name is required`**.
3. **File Excel do chính EMS xuất ra** — user hiển thị trong bảng là `SƠN BÙI QUANG`; file ghi `Last Name = "BÙI QUANG"`, `First Name = "SƠN"`; dialog Edit của đúng user đó hiển thị ô `First Name` = `BÙI QUANG`, ô `Last Name` = `SƠN`.

Cả ba nguồn đều xác định ô bên trái là **họ**; chỉ riêng cái nhãn nói nó là tên.

**Hệ quả:** admin làm theo nhãn sẽ gõ tên vào ô họ và họ vào ô tên. Dữ liệu vào sai cột, **không có cảnh báo nào**, và chỉ lộ ra khi xuất file hoặc khi tên hiển thị sai thứ tự ở nơi khác. Xếp mức 3 chứ không phải 4 vì dữ liệu vẫn được lưu và vẫn sửa lại được — nhưng đây là finding đáng sửa trước nhất trong toàn bộ báo cáo này.

**Evidence**
`evidence/C2/C2_IA02-02_validation-messages-prove-labels-swapped.png` · `evidence/C2/C2_IA02-01_no-required-marker-and-swapped-labels.png` · `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt`

**Suggested fix**
Hoán lại hai nhãn cho khớp với ô mà chúng mô tả (lấy thông báo lỗi và header file export làm chuẩn, vì hai chỗ đó đang đúng). Sau đó rà lại dữ liệu đã nhập qua form này, vì các bản ghi tạo trước khi sửa có thể đã bị đảo họ/tên.

---

### F-013 — Trường bắt buộc không có dấu hiệu nào cho biết là bắt buộc; nhãn không liên kết với ô nhập

| Trường | Nội dung |
| --- | --- |
| **Screen** | C2 Edit User dialog · dialog Create New User |
| **Checklist items** | IA02-01 |
| **Type** | Bug (accessibility) |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-013 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management** → **+ Add User**
2. Nhìn 8 nhãn: có dấu `*` hay chữ "required" ở đâu không?
3. Trong DevTools, kiểm `required`, `aria-required`, và thuộc tính `for` của các `<label>`
4. Bấm **Create User** khi form trống để xem hệ thống thực sự bắt buộc những trường nào

**Expected**
Theo IA02-01 (Norman P3 / P6 / Slides S13 p.11): *"no required field unmarked… and the requirement exposed programmatically as well as visually."*

**Actual**
Ba vế lệch nhau:
- **(a) Nhìn thấy — không có gì.** `dialog.textContent.includes('*')` = `false`. Kiểm cả marker vẽ bằng CSS: `getComputedStyle(label, '::before').content` và `'::after'` đều trả `none` trên **cả 8** nhãn. Không dấu sao, không chữ "required", không đổi màu. Trớ trêu là **chỉ trường không bắt buộc mới được đánh dấu** — placeholder ghi `Member Code (Optional)`.
- **(b) Programmatic — nửa vời.** `required=true` có trên First Name / Last Name / Email / Password, nhưng `aria-required` = `null` trên **toàn bộ** input. Nặng hơn: **`<label>` không liên kết với input** — cả 7 `<label>` đều `for=null`, và `input.labels` rỗng với mọi trường trừ checkbox `Active`.
- **(c) Thực sự chặn — có.** Submit rỗng bị chặn với 4 lỗi.

Kết quả: hệ thống bắt buộc 4 trường, không nói cho người nhìn biết trường nào bắt buộc, và không phơi thông tin đó cho screen reader. Người dùng chỉ biết bằng cách submit hỏng.

**Evidence**
`evidence/C2/C2_IA02-01_no-required-marker-and-swapped-labels.png`

**Suggested fix**
Thêm dấu hiệu bắt buộc nhìn thấy được (dấu `*` kèm chú thích, hoặc chữ "required") cho 4 trường đó; thêm `aria-required="true"`; và nối `<label for>` với `id` của input để nhãn được đọc lên cùng ô.

---

### F-014 — Không có toast hay xác nhận nào sau khi lưu thành công; toàn app không có vùng aria-live

| Trường | Nội dung |
| --- | --- |
| **Screen** | C2 Edit User dialog · C4 Export |
| **Checklist items** | IA04-04 (C2, C4) · IA04-12 (C2, C4) |
| **Type** | Bug |
| **Severity** | 3 — Major |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-014 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, tìm `abc`, bấm **Edit user** trên dòng `test abc`
2. Tick checkbox **Active**, bấm **Save Changes**
3. Quan sát toàn màn hình trong 5 giây: có toast không, có dòng xác nhận nào không
4. Kiểm trong DevTools: `document.querySelectorAll('[aria-live],[role=status],[role=alert]')`
5. Làm tương tự với nút **Export**

**Expected**
Theo IA04-04 (Nielsen H1 / Shneiderman R3): *"A toast or inline confirmation names what happened… the UI never just silently redirects."*
Theo IA04-12 (WCAG 2.1 SC 4.1.3 — Status Messages): thông báo trạng thái phải nằm trong vùng `role="status"` / `aria-live="polite"` để được đọc lên mà không cướp focus.

**Actual**
Thao tác lưu **thành công thật** — cột `STATUS` đổi từ `Inactive` sang `Active`, cột `UPDATED` đổi thành `02/08/2026 17:43`, tức đã ghi xuống DB. Nhưng:
- Một `MutationObserver` **không lọc** đặt trên `document.body` với `subtree:true` ghi nhận **đúng 4 mutation** cho cả thao tác: dialog mở, dialog đóng, bảng re-render. **Không một node toast nào được chèn vào.**
- Không có xác nhận inline nào trong dialog trước khi nó đóng.
- `document.querySelectorAll('[aria-live],[role=status],[role=alert]').length` = **0**, đo ở mọi thời điểm: trước khi mở dialog, khi dialog đang mở, ngay sau khi Save, sau khi bảng re-render.

Luồng **Export** cũng vậy: bấm Export → file về thật (14 339 bytes) nhưng không có busy state, không spinner, không toast (lấy mẫu mỗi 150 ms trong 6 giây).

Hệ quả: người dùng sáng mắt phải tự soi lại dòng trong bảng mới biết đã lưu được chưa; người dùng screen reader **không có cách nào biết** hành động đã hoàn tất. Với Export thì phản hồi duy nhất nằm hoàn toàn ngoài trang (trong thư mục Downloads).

Xếp mức 3 vì người dùng phải tin vào một kết quả mà giao diện không hề xác nhận — và nếu thao tác lưu **thất bại**, nhiều khả năng nó cũng im lặng y hệt (chưa kiểm được; cần ca offline của IA04-11).

**Evidence**
`evidence/C2/C2_IA04-04_no-toast-after-successful-save.png` · `evidence/C4/C4_IA04-13_export-no-feedback-and-ignores-filter.png`

**Suggested fix**
Thêm một hệ thống toast dùng chung, đặt trong container có `role="status"` `aria-live="polite"`, hiển thị ≥ 5 giây, phát cho mọi hành động ghi (save, block/unblock, delete, export) và cho cả trường hợp **thất bại**.

---

### F-015 — Thoát dialog đang sửa dở làm mất thay đổi, không hỏi gì

| Trường | Nội dung |
| --- | --- |
| **Screen** | C2 Edit User dialog |
| **Checklist items** | IA02-13 |
| **Type** | Usability |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-015 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, bấm **Edit user** trên một dòng bất kỳ
2. Sửa nội dung một ô — ví dụ gõ `UNSAVED-EDIT-999` đè lên ô `Phone Number`
3. **Không** bấm Save. Bấm phím `Esc`
4. Mở lại dialog của đúng user đó

**Expected**
Theo IA02-13 (Nielsen H5 — Error Prevention / Shneiderman R6 — Permit Easy Reversal): *"Every exit path warns that unsaved changes will be lost and offers a way to stay; entered data is never discarded silently."*

**Actual**
Dialog đóng **ngay lập tức**, không hỏi gì. Kiểm sau khi đóng (đã loại phần chú thích của người test ra khỏi phép tìm): không có chuỗi nào khớp `unsaved|discard|are you sure|lost` xuất hiện trên trang. Nội dung vừa gõ biến mất hoàn toàn; mở lại dialog thì ô `Phone Number` trở về giá trị cũ. Không có cảnh báo, không có lựa chọn "ở lại", không có cách khôi phục.

Phạm vi đã chạy: đường thoát bằng `Esc`. Hai đường còn lại của dialog (`Cancel`, `X`) chưa thao tác riêng, nhưng vì **không tồn tại cơ chế cảnh báo nào** nên nhiều khả năng cũng vậy.

**Evidence**
`evidence/C2/C2_IA02-13_esc-discards-edit-silently-1-before.png` · `evidence/C2/C2_IA02-13_esc-discards-edit-silently-2-after.png`

**Suggested fix**
Theo dõi trạng thái "form đã bị sửa"; nếu có thay đổi chưa lưu thì `Esc`/`Cancel`/`X` phải hiện hộp xác nhận "Bỏ thay đổi?" với lựa chọn ở lại.

---

### F-016 — Bấm Enter ở ô cuối của form không kích hoạt hành động chính

| Trường | Nội dung |
| --- | --- |
| **Screen** | C2 dialog Create New User / Edit User |
| **Checklist items** | IA02-10 (ca b) |
| **Type** | Usability |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-016 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management** → **+ Add User**
2. Điền vài trường
3. Đặt con trỏ vào ô `Member Code` và bấm **Enter**

**Expected**
Theo IA02-10 (Norman P4 — Mapping / Slides S13 p.18): *"Enter triggers the primary submit/search action — and never a different button (Delete, Cancel) nor a page reload that loses input."*

**Actual**
**Không có gì xảy ra.** Dialog vẫn mở, **0** thông báo lỗi inline xuất hiện, không có user nào được tạo, `performance.getEntriesByType('navigation')[0].type` vẫn là `navigate` (không reload), nội dung đã gõ vẫn còn. Enter **không** kích hoạt `Create User`.

Nguyên nhân quan sát được: dialog **không có phần tử `<form>`** — `dialog.querySelector('form')` trả về `null` — nên trình duyệt không có gì để implicit-submit.

Ghi lại vế **đạt** để không thổi phồng: Enter cũng **không** kích hoạt nhầm `Cancel`/`X` và **không** làm mất dữ liệu đã gõ. Ở ô search một trường của C1, Enter hành xử đúng (đã chấm Pass).

**Evidence**
`evidence/C2/C2_IA02-10_enter-does-nothing-on-form.png`

**Suggested fix**
Bọc các trường trong `<form onSubmit={…}>` và để nút chính là `type="submit"`, để Enter hoạt động theo quy ước bàn phím.

---

### F-017 — Export bỏ qua filter/search đang bật và xuất toàn bộ dataset mà không báo

| Trường | Nội dung |
| --- | --- |
| **Screen** | C4 Export to Excel |
| **Checklist items** | IA04-13 |
| **Type** | Bug |
| **Severity** | 3 — Major |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-017 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**
2. Gõ `abc` vào ô search → màn hình còn đúng **1 dòng**, nhãn ghi `1-1 of 1 results`
3. Bấm **Export**
4. Mở file `.xlsx` vừa tải về và đếm số dòng dữ liệu

**Expected**
Theo IA04-13 (Assignment §5 C4 / Nielsen H1): *"the UI makes unambiguous **whether the export covers the current filter/page or the whole dataset** — silently exporting something other than what the user is looking at is a Fail."*

**Actual**
Màn hình hiển thị **1 dòng**; file tải về chứa **105 dòng dữ liệu** — toàn bộ dataset. User đang được lọc nằm ở **dòng thứ 38** trong file.

Giao diện **không hề** nói export lấy toàn bộ hay lấy phần đang lọc: không có hộp thoại chọn phạm vi, không có chú thích cạnh nút, không có thông báo sau khi tải.

Hệ quả: admin lọc ra một nhóm rồi bấm Export với ý định lấy đúng nhóm đó sẽ nhận về toàn bộ danh sách — và nếu không mở file ra đếm thì không biết. Ở chiều ngược lại, đây cũng là rủi ro đưa dữ liệu ngoài ý muốn ra ngoài khi file được gửi đi.

**Evidence**
`evidence/C4/C4_IA04-13_export-no-feedback-and-ignores-filter.png` · `evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` · `evidence/C4/users-export-1785667505695.xlsx`

**Suggested fix**
Cho export áp dụng đúng filter/search đang bật; và dù chọn hướng nào cũng phải nói rõ ngay tại nút hoặc trong một hộp thoại xác nhận ("Xuất 1 dòng đang lọc" so với "Xuất toàn bộ 105 dòng").

---

### F-018 — File export thiếu cột UPDATED và đổi tên cột MEMBER CODE

| Trường | Nội dung |
| --- | --- |
| **Screen** | C4 Export to Excel |
| **Checklist items** | IA04-13 |
| **Type** | Bug |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-018 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, ghi lại 7 tiêu đề cột trên màn hình
2. Bấm **Export**, mở file `.xlsx`, đọc dòng header
3. So hai danh sách

**Expected**
Theo IA04-13: *"Its columns are complete relative to the on-screen table (Users: USER · Role · MEMBER CODE · Status · CREATED · UPDATED)."*

**Actual**
- Header trong file: `Last Name · First Name · Email · Phone · Card Code · Role · Status · Created At`
- Trên màn hình: `USER · Role · MEMBER CODE · Status · CREATED · UPDATED · ACTIONS`

→ Cột **`UPDATED` thiếu hẳn** khỏi file, dù đây là cột dùng để biết bản ghi nào vừa bị sửa.
→ `MEMBER CODE` bị đổi tên thành **`Card Code`** trong file, không khớp thuật ngữ trên giao diện.
→ (`Phone` có trong file mà không có trên màn hình — thừa thì không phải lỗi, chỉ ghi nhận.)

**Evidence**
`evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` · `evidence/C4/users-export-1785667505695.xlsx`

**Suggested fix**
Thêm cột `Updated At` vào file export và đổi `Card Code` thành `Member Code` cho khớp với giao diện.

---

### F-019 — Giá trị Status trong file export là tiếng Việt trong khi giao diện hoàn toàn tiếng Anh

| Trường | Nội dung |
| --- | --- |
| **Screen** | C4 Export to Excel |
| **Checklist items** | IA04-13 |
| **Type** | Bug |
| **Severity** | 1 — Cosmetic |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-019 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management** (giao diện đang là tiếng Anh, và không đổi được — xem F-001)
2. Bấm **Export**, mở file `.xlsx`, đọc cột `Status`

**Expected**
Nội dung file xuất ra phải dùng cùng ngôn ngữ với giao diện đã tạo ra nó (Nielsen H4 — Consistency and Standards).

**Actual**
Giao diện hiển thị `Active` / `Inactive`; file ghi **`Hoạt động`**. Header của file thì lại bằng tiếng Anh (`Last Name`, `Status`, `Created At`) — nên bản thân file đã trộn hai ngôn ngữ trong cùng một bảng.

**Evidence**
`evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` · `evidence/C4/users-export-1785667505695.xlsx`

**Suggested fix**
Cho phần sinh file dùng chung bộ chuỗi i18n với giao diện, và xuất theo locale đang chọn.

---

### F-020 — Tên file export dùng epoch mili-giây thay vì ngày đọc được

| Trường | Nội dung |
| --- | --- |
| **Screen** | C4 Export to Excel |
| **Checklist items** | IA04-13 |
| **Type** | Usability |
| **Severity** | 1 — Cosmetic |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome / Windows 11 |
| **Ngày phát hiện** | 2026-08-02 |
| **Findings-Log-ID** | F-020 |
| **Form submitted** | _(chưa submit)_ |

**Steps to reproduce**
1. Mở **Users Management**, bấm **Export**
2. Nhìn tên file trong thư mục Downloads

**Expected**
Theo IA04-13: *"The file arrives with a meaningful, dated filename."*

**Actual**
Tên file là `users-export-1785667505695.xlsx`. Phần `1785667505695` là **epoch tính bằng mili-giây** — đúng về kỹ thuật nhưng không ai đọc ra được đó là ngày nào. Xuất vài lần trong ngày sẽ được một loạt file không phân biệt nổi nếu không mở ra.

**Evidence**
`evidence/C4/C4_IA04-13_file-contents-vs-screen.txt` (dòng `Downloaded file:`)

**Suggested fix**
Đặt tên theo dạng đọc được, ví dụ `users-export-2026-08-02_1745.xlsx`; nếu export có áp filter thì ghi luôn phạm vi vào tên file.

---

## Đối chiếu Fail → finding (kiểm tra không sót, không trùng)

| Màn hình | Item Fail | Finding tương ứng |
| --- | --- | --- |
| C1 | IA01-01 | F-003 |
| C1 | IA01-08 | F-001 |
| C1 | IA01-09 | F-001 (vế không đổi được locale) + F-002 (vế 2 định dạng) |
| C1 | IA01-12 | F-004 |
| C1 | IA03-01 | F-005 |
| C1 | IA03-06 | F-007 (vế a) + F-008 (vế b) — item ghi rõ phải tách 2 finding |
| C1 | IA03-08 | F-006 |
| C1 | IA03-13 | F-009 |
| C1 | *(ngoài checklist)* | F-010, F-011 |
| C2 | IA01-12 | F-004 (gộp — cùng nguyên nhân gốc) |
| C2 | IA02-01 | F-013 |
| C2 | IA02-02 | F-012 |
| C2 | IA02-10 | F-016 |
| C2 | IA02-13 | F-015 |
| C2 | IA04-04 | F-014 |
| C2 | IA04-12 | F-014 (gộp — cùng nguyên nhân gốc: không có hệ thống toast) |
| C3 | IA01-12 | F-004 (gộp) |
| C4 | IA04-04 | F-014 (gộp) |
| C4 | IA04-12 | F-014 (gộp) |
| C4 | IA04-13 | F-017 + F-018 + F-019 + F-020 (4 nguyên nhân gốc khác nhau) |

**Tổng:** 18 lượt item Fail trên 4 màn hình → **18 finding có item** + **2 finding ngoài checklist** = **20 finding**.
Mọi item Fail đều đã được xử lý; không finding nào không truy được về một quan sát cụ thể có số đo.

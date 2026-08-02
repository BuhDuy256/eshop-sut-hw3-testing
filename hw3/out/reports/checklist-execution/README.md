# Task 1 — GUI Checklist: Design & Execution

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Scenario:** **C — Admin manages users**
**SUT:** EMS — https://prod-dev.ems-fitus.cloud/ (external web app, test thủ công qua UI, không đọc source code)
**Ngày hoàn thành:** 2026-08-02

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
| Vai trò của tôi | _(CẦN SINH VIÊN ĐIỀN: đã đóng góp item nào / review vòng nào — đây là thông tin chỉ sinh viên biết, không dựng lại được từ repo)_ |
| Reference sources + AI prompts | `hw3/out/group/` — **còn thiếu**, xem blocker B-11 ở mục *Việc còn nợ* |

Checklist là **group deliverable đã đóng băng**. Trong Task 1B tôi **thực thi** nó, không sửa lời văn item nào (§18 yêu cầu checklist giống hệt nhau giữa các thành viên). Commit `Step 2: shared GUI checklist (frozen, v1.9)` được tạo **trước** mọi commit execution, để chứng minh thứ tự này.

## Part B — Execution trên các màn hình của tôi

### Số màn hình thực tế — đọc mục này trước khi đọc số liệu

Phân công ban đầu ghi 4 màn hình, trong đó **C3 = "Block-Unblock & Reset-Password dialogs"**. Khảo sát trực tiếp (blocker **B-12**) cho thấy mô tả đó **không khớp với EMS thật**:

| Chức năng theo phân công | Thực tế trong EMS | Hệ quả |
| --- | --- | --- |
| **Assign Role** | Dropdown `Role` **bên trong dialog Edit User** | Không phải màn hình riêng → thuộc **C2** |
| **Block / Unblock** | Checkbox `Active` **bên trong dialog Edit User**. Không có nút Block ở cấp dòng, không có dialog Block riêng | Không phải màn hình riêng → chấm ở **C2** |
| **Reset Password** | **KHÔNG TỒN TẠI.** Không có ở cấp dòng, không có trong dialog Edit, không có trên toolbar. Field `Password` chỉ xuất hiện khi **tạo** user mới; admin không có đường nào đặt lại mật khẩu cho user đã tồn tại | **Không có chức năng để test** |

**Cách xử lý — nói thẳng thay vì đếm gộp cho đủ 4:**

- **C3 được định nghĩa lại** thành bề mặt duy nhất trên scenario C thật sự là một dialog riêng và thật sự thuộc nhóm hành động phá huỷ: **dialog xác nhận Delete User**.
- Bộ màn hình cuối cùng vẫn là **4 bề mặt phân biệt** — C1 (trang), C2 (dialog Edit), C3 (dialog Delete confirm), C4 (chức năng Export) — thoả §5 (tối thiểu 3).
- **Nhưng coverage bị hẹp lại thật:** một nửa nội dung C3 theo phân công gốc biến mất vì EMS không có chức năng đó. Báo cáo này ghi nhận điều đó thay vì giấu đi.
- Bản thân việc **"Reset Password không tồn tại"** là một quan sát đáng chú ý về sản phẩm, nhưng **không được tính là một item Fail**, vì không item nào trong 60 item nói về chức năng này.

### Màn hình đã test và lý do chọn

| ID | Màn hình | URL / đường đi | Vì sao chọn |
| --- | --- | --- | --- |
| **C1** | Users list | `/dashboard/admin/users` | Bề mặt IA-03 duy nhất của scenario: bảng 7 cột, 2 filter, search, phân trang, sidebar, toolbar |
| **C2** | Edit User dialog (gồm Assign Role + Block/Unblock) | C1 → nút `Edit user` trên dòng | Form **duy nhất** của scenario — chở gần như toàn bộ IA-02 |
| **C3** | Delete User confirm dialog | C1 → nút `Delete user` trên dòng | Bề mặt "hành động phá huỷ" của IA-04: confirm, modality, ESC |
| **C4** | Export to Excel | C1 → nút `Export` trên toolbar | §5 C4 gọi tên trực tiếp — *"column completeness and download feedback"*; là referent duy nhất của IA04-13 |

§5 yêu cầu tối thiểu **3** màn hình; lấy **4** vì bề mặt user-admin nhỏ, dừng ở 3 sẽ đẩy quá nhiều item thành N/A.

### Kết quả tổng hợp

| Màn hình | Applicable | Executed | Passed | Failed | N/A | Chưa execute | Tỉ lệ pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 Users list | 21 | 19 | 11 | 8 | 39 | 2 | 52,4 % |
| C2 Edit User dialog | 14 | 13 | 6 | 7 | 46 | 1 | 42,9 % |
| C3 Delete confirm | 6 | 5 | 4 | 1 | 54 | 1 | 66,7 % |
| C4 Export | 3 | 3 | 0 | 3 | 57 | 0 | 0 % |
| **Tổng (cộng theo lượt màn hình)** | **44** | **40** | **21** | **19** | **196** | **4** | **47,7 %** |

**Kiểm tra số học:** với **từng** màn hình, `Passed + Failed + N/A + chưa execute = 60` ✓ (C1: 11+8+39+2 · C2: 6+7+46+1 · C3: 4+1+54+1 · C4: 0+3+57+0).

> **N/A không được tính là Passed.** Tỉ lệ pass = `Passed / Applicable` = `21 / 44` = **47,7 %**. Nếu tính sai thành `21 / 240` thì ra 8,8 % — con số vô nghĩa.

**4 item chưa execute** (để trống Verdict có chủ ý, **không** đoán):

| Item | Màn hình | Vì sao |
| --- | --- | --- |
| IA01-07 | C1 | Cần DevTools → Network → **Slow 3G**. Công cụ tự động hoá không bật được throttling |
| IA04-11 | C1, C2 | Cần DevTools → Network → **Offline**. Như trên |
| IA04-04 | C3 | Muốn chấm phải bấm `Confirm` và **xoá thật** một user — không đảo ngược được, bị cấm bởi quy tắc dữ liệu tự đặt |

### Phân bố Failed theo Interface Aspect

| Aspect | Số lượt item Failed | Nhận xét |
| --- | --- | --- |
| **IA-01 General UI** | **6** (IA01-01, IA01-08, IA01-09, IA01-12 ×3) | Hỏng chủ yếu ở **i18n** và **accessibility**. Nút chuyển ngôn ngữ hoàn toàn không hoạt động, nên toàn bộ khu admin chỉ dùng được bằng tiếng Anh — với một hệ thống của trường đại học Việt Nam thì đây là khiếm khuyết đáng kể. IA01-12 fail trên cả 3 màn hình có tương tác, tức là vấn đề nằm ở component dùng chung chứ không phải một chỗ lẻ |
| **IA-02 Forms** | **4** (IA02-01, IA02-02, IA02-10, IA02-13) | **Nhóm yếu nhất theo tỉ lệ**: trên C2 có 7 item IA-02 áp dụng được thì 4 hỏng (57 %). Và finding nghiêm trọng nhất của cả Task 1 nằm ở đây — nhãn `First Name`/`Last Name` bị gán ngược (F-012), tức là form **ghi dữ liệu vào sai cột** với người dùng làm đúng theo nhãn |
| **IA-03 Navigation** | **4** (IA03-01, IA03-06, IA03-08, IA03-13) | Có một chủ đề chung rõ rệt: **trạng thái danh sách không được lưu ở đâu cả**. URL không bao giờ đổi (`/dashboard/admin/users` suốt), nên Back mất trang + rows-per-page, danh sách không chia sẻ được bằng link, và không có sort để bù |
| **IA-04 Feedback / State** | **5** (IA04-04 ×2, IA04-12 ×2, IA04-13) | **Nhóm hỏng triệt để nhất về bản chất:** EMS **không có hệ thống toast nào cả** và **không có một vùng `aria-live`/`role="status"` nào** trên toàn bộ luồng đã kiểm. Mọi hành động ghi (save, block/unblock, export) đều hoàn tất trong im lặng. Với người dùng screen reader, kết quả của thao tác là **không thể biết được** |

**Nhận định tổng thể:** hai điểm yếu xuyên suốt, cùng lặp lại trên nhiều màn hình nên gần như chắc chắn là vấn đề ở tầng component/kiến trúc chứ không phải lỗi lẻ:
1. **Không có kênh phản hồi trạng thái** (IA-04) — không toast, không live region, ở mọi luồng.
2. **Accessibility bàn phím và nhãn** (IA-01 + IA-02) — focus không vào dialog, focus ring trong suốt, `<label>` không nối với input, `aria-required` vắng mặt.

Điểm sáng: **C3 (dialog xác nhận xoá) làm đúng gần hết** — gọi đúng tên record, nêu rõ hậu quả không hoàn tác được, tô đỏ nút phá huỷ, chặn click xuyên nền, ESC hành xử như Cancel. Đây là bằng chứng rằng đội phát triển **biết** cách làm đúng ở chỗ họ có chú ý tới.

### Vì sao có nhiều N/A ở scenario C

Con số N/A rất cao (196/240 lượt) và **lệch xa dự đoán**. Nói rõ cả hai lý do:

**1. Dự đoán trước khi chạy đã sai về bản chất — và đây là phát hiện đáng ghi nhất về chính checklist.**
Bảng *"Predicted N/A by scenario"* trong checklist dự đoán ~14 (v1.6), điều chỉnh lên ~21 sau khi cộng các item v1.8/v1.9 viết riêng cho scenario B và D. Thực tế C1 một mình đã có **39 N/A**.

Nguyên nhân: bảng dự đoán được viết cho **scenario**, nhưng verdict phải chấm cho **từng màn hình**. Một item áp dụng được với scenario C (ví dụ IA02-01 — đánh dấu required) chỉ có widget để bám vào trên **một** trong bốn màn hình. Ba màn hình còn lại buộc phải ghi N/A. Với 4 màn hình, một item "applicable với scenario" vẫn sinh ra 3 dòng N/A.

→ **Đề xuất cho v2.0:** bảng dự đoán N/A nên dự đoán theo **cặp (item × màn hình)**, không phải theo scenario; hoặc checklist nên nói rõ rằng tỉ lệ N/A cao là hệ quả thiết kế đã biết khi một người chạy cùng bộ item trên nhiều màn hình.

**2. Bề mặt user-admin vốn mỏng.** Không có upload, không rich-text editor, không date control, không toggle switch, không capacity figure, không real-time counter, không tab, không breadcrumb, không drag-and-drop, không QR, không spotlight hero. Cộng thêm **7 item** (IA02-15, IA03-14, IA03-15, IA04-07, IA04-14, IA04-15, IA04-16) viết riêng cho scenario B và D.

**Mọi N/A đều có lý do một dòng** trong file execution tương ứng, nêu đích danh widget nào vắng mặt — không có dòng nào bỏ trống hay ghi "không áp dụng" suông.

### Một khoảng trống của checklist phát hiện được khi chạy

**2 trong 20 finding không map được vào bất kỳ item nào trong 60 item** — cả hai đều là lỗi của **ô search trên bảng dữ liệu**:

- **F-010** — không tìm được user bằng chính tên đầy đủ đang hiển thị của họ (`test abc` → 0 kết quả, dù `test` và `abc` riêng lẻ đều tìm ra đúng user đó). Severity 3.
- **F-011** — bảng hiển thị kết quả của truy vấn cũ kèm nhãn đếm khẳng định, không có chỉ báo đang tải. Severity 2.

Checklist v1.9 có item cho phân trang (IA03-06), cho sort/filter trên header (IA03-08), cho filter của scenario D (IA03-14) và search của scenario B (IA03-15) — **nhưng không có item nào cho ô search của một bảng admin**, dù cả 5 danh sách trong EMS đều có ô search.

→ **Đề xuất cho v2.0: thêm một item về tính đúng đắn của search trên bảng dữ liệu** — khớp được tên hiển thị đầy đủ, không trả kết quả cũ, và trạng thái rỗng phân biệt được "không có kết quả" với "đang tải".

Hai finding này **vẫn được báo cáo đầy đủ** và vẫn nên submit lên Google Form: §7 nhận bug bất kể nó có thuộc checklist hay không. Chúng **không** bị gán bừa vào một item gần đúng chỉ để có mã item — làm vậy là gán sai bằng chứng.

## Bug & Usability findings từ Task 1

**20 finding.** Bug: 14 · Usability: 6. Severity: `4` → 0 · `3` → 5 · `2` → 11 · `1` → 4.

| Findings-Log-ID | Screen | Type | Sev | Tiêu đề |
| --- | --- | --- | --- | --- |
| F-001 | C1 | Bug | 3 | Nút chuyển ngôn ngữ EN/VI trên header không có tác dụng gì |
| F-010 | C1 | Bug | 3 | Không tìm được user bằng chính tên đầy đủ đang hiển thị của họ |
| F-012 | C2 | Bug | 3 | Nhãn "First Name" và "Last Name" bị gán ngược so với ô nhập tương ứng |
| F-014 | C2, C4 | Bug | 3 | Không có toast hay xác nhận nào sau khi lưu thành công; toàn app không có vùng aria-live |
| F-017 | C4 | Bug | 3 | Export bỏ qua filter đang bật và xuất toàn bộ dataset mà không báo |
| F-002 | C1 | Usability | 2 | Ngày giờ hiển thị theo hai định dạng khác nhau giữa các màn hình admin |
| F-004 | C1, C2, C3 | Bug | 2 | Focus không vào dialog khi mở; ô "Go to page" không có dấu hiệu focus |
| F-005 | C1 | Bug | 2 | Sidebar thu gọn không có tooltip; các mục mất hẳn tên |
| F-006 | C1 | Usability | 2 | Bảng Users 7 cột không sắp xếp được theo cột nào |
| F-007 | C1 | Bug | 2 | Nhãn phân trang hiện "NaN-NaN of 107 results" khi option rỗng được chọn |
| F-009 | C1 | Bug | 2 | Nút Back làm mất vị trí trang và thiết lập rows-per-page |
| F-011 | C1 | Bug | 2 | Bảng hiển thị kết quả cũ kèm số đếm khẳng định, không có chỉ báo tải |
| F-013 | C2 | Bug | 2 | Trường bắt buộc không có dấu hiệu nào; nhãn không liên kết với ô nhập |
| F-015 | C2 | Usability | 2 | Thoát dialog đang sửa dở làm mất thay đổi, không hỏi gì |
| F-016 | C2 | Usability | 2 | Bấm Enter ở ô cuối của form không kích hoạt hành động chính |
| F-018 | C4 | Bug | 2 | File export thiếu cột UPDATED và đổi tên cột MEMBER CODE |
| F-003 | C1 | Usability | 1 | Kiểu tiêu đề trang không nhất quán giữa các màn hình admin |
| F-008 | C1 | Usability | 1 | Thang "rows per page" và giá trị mặc định khác nhau giữa các danh sách |
| F-019 | C4 | Bug | 1 | Giá trị Status trong file export là tiếng Việt trong khi giao diện tiếng Anh |
| F-020 | C4 | Usability | 1 | Tên file export dùng epoch mili-giây thay vì ngày đọc được |

Chi tiết: `bug-reports.md`. Log: `hw3/work/findings-log.md`.

> ⚠ **Chưa submit lên Google Form.** Form yêu cầu đăng nhập bằng email sinh viên `MSSV@....edu.vn` (§7), không có trong phiên chạy này. Cả 20 finding đã ở dạng sẵn sàng dán, cột *Form timestamp* trong findings log để trống chờ điền sau khi submit.

## Ghi chú về quy trình

**Thứ tự thực hiện:** khảo sát 4 màn hình (chưa chấm điểm) → C1 (pilot, chạy đủ 60 item) → review quy trình → C2 → C3 → C4 → gộp bug → tổng hợp.

**Thời gian thực tế:** ~2 giờ 40 phút cho toàn bộ Task 1B (C1 ~43 phút · C2 ~25 phút · C3 ~12 phút · C4 ~15 phút · khảo sát, gộp bug và viết báo cáo chiếm phần còn lại).

**Điều chỉnh giữa chừng — pilot có tác dụng thật:**

1. **Ảnh chụp không có thanh địa chỉ.** Ảnh chụp qua công cụ tự động chỉ lấy vùng nội dung trang, không có URL bar, nên không tự chứng minh được là chụp từ hệ thống thật (§12 kiểm đúng chỗ này). **Sửa ngay trong C1:** chèn một dải chú thích ở đầu trang ghi `location.href` thật + giờ hệ thống + mô tả phép đo, và ghi rõ trên dải đó rằng nó **do người test thêm vào, không phải giao diện EMS**.
2. **Cách đo contrast phải làm lại.** EMS dùng Tailwind v4 nên `getComputedStyle` trả màu ở dạng `lab()`, không phải `rgb()`. Hàm tính đầu tiên trả về rỗng. Sửa bằng cách chuyển `lab()` sang sRGB qua canvas trước khi áp công thức WCAG.
3. **Phải chờ dữ liệu ổn định trước khi đọc số.** Search của EMS có debounce; đo quá sớm sẽ đọc trúng kết quả của truy vấn cũ. Sau khi phát hiện, mọi phép đo liên quan tới search đều chờ 7–9 giây rồi mới đọc — và bản thân hành vi đó về sau trở thành finding **F-011**.

**Giới hạn đã biết — nói rõ để không ai đọc quá kết quả:**

- **2 item cần DevTools throttling chưa chạy** (IA01-07 Slow 3G, IA04-11 Offline). IA04-11 là item đáng tiếc nhất: đã biết chắc EMS không phát toast khi Save **thành công**, nên câu hỏi còn bỏ ngỏ là khi Save **thất bại** giao diện có nói gì không. Nếu cũng im lặng thì một lần lưu hỏng trông y hệt một lần lưu thành công.
- **Nhánh xoá thật (`Confirm`) không chạy** trên C3, có chủ ý, để không phá dữ liệu. Nên IA04-04 trên C3 không có kết quả.
- **Không tạo user test mới.** Form Create New User bắt buộc field `Password`; phiên chạy này không nhập mật khẩu vào bất kỳ ô nào. Thay bằng tài khoản test **có sẵn** `test abc` (Guest, Inactive) — đã Block→Unblock→Block round-trip và **trả về đúng trạng thái ban đầu**. Không mất coverage item nào.
- **Chỉ chấm 1 trong 4 export của EMS.** IA04-13 nói EMS có 4 chỗ export; bộ màn hình scenario C chỉ chứa Export của Users Management.
- **IA02-01 chỉ chấm được 1 trong 3 form** mà item yêu cầu (Edit User dialog). Hai form kia (Add/Edit Event, Create Support Request) thuộc màn hình của thành viên khác; kết luận về "ba form ba quy ước" có dùng số liệu khảo sát của nhóm, và điều đó được ghi rõ trong Notes của item.
- **Kiểm accessibility bằng DOM, không bằng screen reader.** IA04-12 và các nhận định về `aria-*` đều đọc từ DOM; không chạy NVDA.
- **Dữ liệu EMS thay đổi ngay trong phiên** — tổng số user đi từ **105 → 107**, badge Support requests từ **7 → 6**. Đúng như cảnh báo §4 của đề. Mọi số đo trong báo cáo đều kèm thời điểm đo, nên các con số tổng có thể không khớp nếu chạy lại sau này.

## Đối chiếu với yêu cầu §6 Task 1

| Yêu cầu | Đáp ứng |
| --- | --- |
| Checklist > 40 item, phủ IA-01…IA-04 | ✅ 60 item (13/15/15/17) |
| Reference sources + AI prompts (group) | ❌ **Chưa có** — blocker B-11, phải xin từ nhóm, không dựng lại |
| Giải thích item nào AI bỏ sót và vì sao | ✅ Mục *"The four grounding pillars"* + *"Known weakness"* trong checklist |
| Execute checklist trên ≥ 3 màn hình | ✅ 4 bề mặt (C1, C2, C3, C4) — kèm ghi chú trung thực rằng phạm vi C3 đã hẹp lại vì Reset Password không tồn tại |
| Đánh dấu Passed/Failed từng item từng màn hình | ✅ 240 ô verdict; 236 đã điền, **4 để trống có ghi rõ lý do** (không đoán) |
| Cột Notes ghi lý do cho mỗi Failed | ✅ Mọi Fail đều có số đo cụ thể hoặc chuỗi ký tự nguyên văn, không có dòng nào ghi chung chung |
| Screenshot cho item Failed | ✅ 19 ảnh + 1 file `.txt` phân tích nội dung xlsx + chính file `.xlsx` gốc. **1 finding (F-011) cố ý không có ảnh** vì trạng thái chỉ tồn tại ~0,2 s — ghi rõ lý do và thay bằng log lấy mẫu theo mốc thời gian |
| Bug có: screen, steps, expected vs actual, severity, screenshot | ✅ Cả 20 finding đủ trường; mọi *Expected* đều trích từ cột *Expected Behavior* của item hoặc từ heuristic/WCAG được cite, không suy từ code |
| Bug đã report qua kênh §7 | ❌ **Chưa** — cần email sinh viên để đăng nhập Google Form. Nội dung đã sẵn sàng dán |

## Việc còn nợ

| # | Việc | Ai làm | Chặn cái gì |
| --- | --- | --- | --- |
| 1 | **Submit 20 finding lên Google Form** bằng email `MSSV@....edu.vn`, rồi điền cột *Form timestamp* trong findings log | Sinh viên | Tiêu chí 4 (§7) |
| 2 | **Chạy IA01-07 (Slow 3G) và IA04-11 (Offline)** bằng DevTools | Sinh viên | 2 ô verdict còn trống |
| 3 | **B-11 — lấy group artefacts** về `hw3/out/group/`: `Reference_Sources_and_Prompts.md`, `AI_Audit_Report.md`, `EMS_Live_Survey_2026-07-26.md`, 14 screenshot gốc | Sinh viên xin từ nhóm | §15 bắt buộc; **không dựng lại** — dựng lại là bịa provenance |
| 4 | **Điền vai trò cá nhân trong Part A** (đóng góp item nào, review vòng nào) | Sinh viên | Part A |

# Task 1 — Runbook cầm tay chỉ việc

**Cho:** Nguyễn Bảo Duy — 23127179 — Group 09
**Giả định:** bạn chưa từng làm GUI Testing. Runbook này không bỏ qua bước nào.
**Phạm vi:** chỉ Task 1 (GUI Checklist). Task 2 (User Testing) và Task 3 (Cross-Platform) có runbook riêng.
**Thời gian ước tính:** 5–7 giờ, chia được thành 3–4 buổi.

---

## Đọc 2 phút này trước khi làm bất cứ thứ gì

**Task 1 có hai phần:**

| Phần | Nội dung | Trạng thái |
| --- | --- | --- |
| **Part A** | Cả nhóm thiết kế **một** checklist GUI > 40 item | ✅ **XONG RỒI** — 60 item, v1.9 |
| **Part B** | *Bạn* chạy checklist đó trên ≥ 3 màn hình của mình | ⬜ **Đây là việc của bạn** |

**Việc của bạn bắt đầu ở Part B.** Không thiết kế checklist mới. Không sửa chữ trong checklist. Nếu bạn thấy một item viết sai → báo nhóm, không tự sửa bản của mình (§18: checklist phải giống hệt nhau giữa 4 thành viên; sửa riêng là tự phá điều kiện đó).

**Ba luật nền, vi phạm là hỏng bài:**

1. **EMS là hệ thống bên ngoài, test thủ công qua giao diện.** Không có source code, không đọc code, không sửa code. Mọi kết luận đến từ những gì bạn nhìn thấy trên trình duyệt.
2. **Bằng chứng phải thật.** Screenshot phải chụp EMS thật đang chạy. §12 nói TA kiểm tra chính chỗ này.
3. **N/A không bao giờ là Pass.** Item nào không áp dụng được thì ghi N/A kèm lý do, và không đếm vào số Passed.

**Ba nơi phải luôn khớp nhau** — nhớ kỹ, đây là chỗ dễ mất điểm nhất:

```
Execution file (C1.md…)  →  Bug report  →  Findings log  →  Google Form
     Fail + ảnh              BUG-C-00N         F-00N          timestamp
```

Mỗi lần thêm dữ liệu, đi hết cả 4 chặng rồi mới làm việc khác. Đừng để dồn.

---

# PHẦN 0 — CHUẨN BỊ

## Step 0.1 — Đọc tài liệu, đúng thứ tự

### Mục tiêu
Biết đề bài yêu cầu gì trước khi mở EMS. Đọc sai thứ tự sẽ dẫn tới làm thừa hoặc làm thiếu.

### Bạn cần làm

Đọc đúng 4 tài liệu này, theo thứ tự, không đọc gì khác:

| # | File | Đọc phần nào | Cần rút ra được gì |
| --- | --- | --- | --- |
| 1 | `hw3/docs/hw3-reqs/2026.HW03.GUI Usability EMS_En.md` | §4 (SUT), §5 (Scope), **§6 Task 1** (kỹ), §7 (kênh nộp bug), §15 (nộp bài), §16 (thang điểm) | Task 1B đáng **15 điểm**; cần ≥ 3 màn hình; mỗi Failed phải có Notes + screenshot; mọi bug phải submit Google Form |
| 2 | `hw3/docs/gui-checklist/Shared_GUI_Checklist.md` | §How to use · §Predicted N/A · §Scenario assignment · rồi **đọc lướt hết 60 item** | Cấu trúc 5 cột của một item; luật Pass/Fail/N/A; scenario của bạn là **C** |
| 3 | `hw3/docs/screen-selection.md` | Toàn bộ (ngắn) | 4 màn hình C1–C4 và vì sao chọn chúng |
| 4 | `hw3/docs/blockers.md` | Toàn bộ (ngắn) | Cái gì đã chốt, cái gì bạn còn phải tự đi giải quyết |

**Không đọc:** bất cứ thứ gì trong `backend/`, `frontend-*/`, `hw2/`, `README.md` ở gốc repo. Đó là tàn dư của bài tập cũ, không liên quan.

**Mẹo đọc 60 item lần đầu:** đừng cố nhớ. Chỉ cần trả lời được: "item này nói về **widget** nào?" Vì đó chính là câu hỏi quyết định Applicable hay N/A ở Step 2.2.

### Kết quả cần có
Bạn nói được thành lời: *"Tôi phải chạy 60 item lên 4 màn hình admin quản lý user, mỗi item chấm Pass/Fail/N/A, cái nào Fail thì chụp ảnh + viết bug + submit form."*

### Checklist trước khi sang bước tiếp theo
- [X] Đã đọc §6 Task 1 của đề, không phải đọc lướt
- [X] Đã lướt hết 60 item một lượt
- [X] Biết scenario của mình là C và 4 màn hình là gì

---

## Step 0.2 — Chuẩn bị công cụ

### Mục tiêu
Cài đủ đồ trước, để lúc execute không phải dừng giữa chừng.

### Bạn cần làm

**Bắt buộc:**

| Công cụ | Dùng cho item nào | Cách mở |
| --- | --- | --- |
| **Google Chrome** (hoặc Edge) | Toàn bộ | — |
| **DevTools** | IA01-05, IA01-13, IA02-01, IA03-04, IA03-08, IA04-12 | `F12` |
| → tab **Elements** | Xem `alt`, `required`, `aria-label`, `aria-live` | F12 → Elements |
| → tab **Network** → **Throttling** | IA01-07 (Slow 3G), IA04-11 (Offline) | F12 → Network → dropdown "No throttling" |
| → **Accessibility pane** | Kiểm accessible name của nút icon-only | F12 → Elements → tab Accessibility (bên phải) |
| → **contrast inspector** | IA01-05 đo tỉ lệ tương phản | Elements → chọn element → trong Styles, click ô màu → xem "Contrast ratio" |
| **Công cụ chụp màn hình** | Mọi item Fail | Windows: `Win + Shift + S` |

**Nên có (không bắt buộc):**
- **WebAIM Contrast Checker** (web) — để kiểm tra chéo số DevTools đưa ra.
- **NVDA** (screen reader miễn phí cho Windows) — cho IA04-12. Nếu không cài, vẫn làm được bằng cách đọc DOM trong DevTools; ghi rõ vào Notes là đã kiểm bằng DOM chứ không bằng screen reader.

**Tạo sẵn thư mục ảnh tạm** trên Desktop, đặt tên `hw3-shots`, để ảnh chụp rơi vào đó rồi mới đổi tên và chuyển vào repo. Chụp thẳng vào repo sẽ làm bạn đặt tên vội và sai.

### Kết quả cần có
Mở được DevTools, đổi được throttling sang Slow 3G và Offline, đo được contrast ratio của một chữ bất kỳ.

### Checklist trước khi sang bước tiếp theo
- [ ] Mở được DevTools và tìm thấy Network → Throttling
- [ ] Đo thử được contrast ratio của một element bất kỳ trên một trang bất kỳ
- [ ] Có phím tắt chụp màn hình hoạt động
- [ ] Có thư mục ảnh tạm

---

## Step 0.3 — Đăng nhập EMS và xác nhận SUT sống

### Mục tiêu
Chứng minh hệ thống truy cập được **trước** khi lên kế hoạch chi tiết. Nếu SUT chết thì mọi bước sau vô nghĩa.

### Bạn cần làm

1. Mở: **https://prod-dev.ems-fitus.cloud/login?callbackUrl=%2F**
2. Đăng nhập: `admin@gmail.com` / `Admin@123`
3. Xác nhận vào được **Dashboard admin** và thấy sidebar bên trái.
4. Bấm **Users Management** trên sidebar → đây chính là **C1**. Copy URL thật ở address bar (dự kiến `…/dashboard/admin/users`) và dán vào `hw3/out/reports/checklist-execution/C1.md`, dòng *URL màn hình*.

**Về account — đọc kỹ đoạn này:**

| Câu hỏi | Trả lời cho scenario C |
| --- | --- |
| Cần tạo account mới không? | **Không.** Scenario C nằm hoàn toàn phía admin. Account `admin@gmail.com` là đủ cho C1–C4. |
| Khi nào mới phải tạo account riêng? | Chỉ scenario **B** và nửa user của scenario **D** mới cần account sinh viên riêng (§4). Đó là việc của bạn cùng nhóm, không phải của bạn. |
| Có được đăng ký tài khoản test để thử Block không? | Có, và **nên** — xem Step 1.3. Nhưng đó là dữ liệu test, không phải account thi hành của bạn. |

> **Cảnh báo §4:** dữ liệu EMS có thể bị reset định kỳ. Đừng tạo dữ liệu hôm nay rồi định chụp ảnh vào tuần sau. Chụp ngay lúc thấy.

### Kết quả cần có
Vào được EMS bằng account admin, mở được Users Management, đã ghi URL thật vào `C1.md`.

### Checklist trước khi sang bước tiếp theo
- [ ] Đăng nhập thành công
- [ ] Mở được Users Management
- [ ] Đã ghi URL thật vào C1.md
- [ ] Đánh dấu **B-06 = resolved** trong `hw3/docs/blockers.md`

---

## Step 0.4 — Chuẩn bị kênh nộp bug (Google Form)

### Mục tiêu
Biết trước Form hỏi những trường gì, để lúc viết bug report bạn ghi sẵn đúng thông tin, không phải quay lại đào.

### Bạn cần làm

1. Mở **https://forms.gle/CJQFQCAXcsDbXDMM9**
2. **Chưa submit gì cả.** Chỉ đọc và chép lại danh sách câu hỏi của Form vào cuối file `hw3/work/findings-log.md`, dưới tiêu đề `## Các trường của Google Form`.
3. Xác nhận bạn đăng nhập Google bằng **email sinh viên** (`MSSV@....edu.vn`). §7 yêu cầu submit bằng địa chỉ này để quy trách nhiệm được.
4. Nếu Form có trường "email" tự động lấy từ tài khoản Google — kiểm tra nó lấy đúng email sinh viên chứ không phải Gmail cá nhân.

### Kết quả cần có
Danh sách trường của Form được chép vào findings log; xác nhận đang đăng nhập đúng email sinh viên.

### Checklist trước khi sang bước tiếp theo
- [ ] Đã mở được Form
- [ ] Đã chép danh sách trường vào `findings-log.md`
- [ ] Đang đăng nhập Google bằng email `MSSV@....edu.vn` (**B-10**)

---

# PHẦN 1 — SCENARIO VÀ SCREEN

## Step 1.1 — Hiểu vì sao chọn Scenario C (và cách chọn nói chung)

### Mục tiêu
Bạn cần **giải thích được** lựa chọn này trong báo cáo và ở buổi vấn đáp (§14 — 30% sinh viên bị gọi). Không phải chọn lại.

### Bạn cần làm

**Kết quả đã chốt: Scenario C — Admin manages users.** Ghi trong bảng phân công của nhóm ở đầu file checklist.

**Phương pháp chọn scenario, nếu sau này phải làm lại từ đầu — 3 câu hỏi theo thứ tự:**

1. **§5 no-duplication:** trong nhóm, hai người không được trùng cả scenario lẫn bộ màn hình. Nhóm 09 có 4 người và có đúng 4 scenario → mỗi người một cái, hết chuyện. Đây là ràng buộc **cứng**, quyết định trước mọi thứ khác.
2. **Account có sẵn không?** Scenario A và C chỉ cần admin. Scenario B và D cần thêm account sinh viên tự đăng ký. Ít phụ thuộc hơn = ít rủi ro hơn.
3. **Bề mặt UI có đủ dày để 60 item bám vào không?** A dày nhất (form Add/Edit Event một mình đã phủ gần hết IA-02). C mỏng nhất. Đây là lý do C phải lấy đủ 4 màn hình.

**Điểm yếu của C và cách bù** — nói thẳng ra trong báo cáo thì tốt hơn là giấu:

> Bề mặt user-admin không có upload, không rich-text, không date control, không toggle, không counter real-time. Nên số N/A sẽ cao. Bù lại bằng cách (a) lấy đủ 4 màn hình thay vì 3, và (b) mỗi N/A đều có lý do một dòng, để người chấm thấy đó là kết luận có kiểm chứng chứ không phải bỏ trống.

### Kết quả cần có
Bạn viết được 3–4 câu giải thích vì sao chọn C, dùng được luôn cho phần "Screen selection justification" của báo cáo.

### Checklist trước khi sang bước tiếp theo
- [ ] Hiểu và giải thích được lựa chọn Scenario C
- [ ] Hiểu vì sao C là scenario mỏng nhất

---

## Step 1.2 — Hiểu vì sao chọn 4 màn hình C1–C4

### Mục tiêu
Biết mỗi màn hình gánh phần nào của checklist — đây chính là thứ giúp bạn quyết định N/A nhanh ở Step 3.

### Bạn cần làm

**Kết quả đã chốt:**

| ID | Màn hình | Đi tới bằng cách nào | Gánh nhóm item nào |
| --- | --- | --- | --- |
| **C1** | Users list | Sidebar → **Users Management** | IA-03 gần như toàn bộ (bảng, filter, search, phân trang, sidebar) + empty/loading state |
| **C2** | Assign Role / Edit user | C1 → click **Edit** ở một dòng | IA-02 gần như toàn bộ (đây là form duy nhất của scenario) |
| **C3** | Block-Unblock & Reset-Password | Trong dialog Edit (hoặc row action) → **Block** / **Reset Password** | IA-04 nửa "hành động phá huỷ": confirm, modality, toast, ESC |
| **C4** | Export to Excel | C1 → nút **Export** trên toolbar | IA04-13 — §5 C4 gọi tên trực tiếp |

**Phương pháp chọn màn hình, nói chung — 4 tiêu chí:**

1. **Có trong danh sách gợi ý §5 không?** Nếu có → không cần giải trình. Nếu chọn màn hình khác → §5 bắt phải giải thích lý do.
2. **Đủ số lượng chưa?** Tối thiểu 3. Lấy thêm nếu bề mặt mỏng.
3. **Có phủ đủ 4 IA không?** Nếu cả 3 màn hình đều là bảng dữ liệu thì toàn bộ IA-02 thành N/A và bạn mất 1/4 checklist. Chọn sao cho có ít nhất một form và một luồng có feedback.
4. **Không trùng với người khác trong nhóm.**

### ⚠ Một việc phải xác minh — blocker B-12

Khảo sát của nhóm ghi: *"Không có nút Assign-Role / Block / Reset-Password ở cấp dòng — chúng nằm bên trong dialog Edit."*

Nghĩa là **C2 và C3 có thể là cùng một dialog**. Nếu đúng vậy:
- Bộ của bạn là **C1 · C2+C3 · C4 = 3 màn hình** — vẫn hợp lệ theo §5.
- Nhưng báo cáo phải nói thẳng điều đó, **không được đếm thành 4**. Đếm gộp là thổi phồng coverage, và mở dialog ra là thấy ngay.

Xác minh ở Step 1.3, không đoán.

### Kết quả cần có
Biết đường đi tới từng màn hình và biết màn hình nào gánh IA nào.

### Checklist trước khi sang bước tiếp theo
- [ ] Mở được cả 4 màn hình bằng tay
- [ ] Hiểu B-12 là gì và sẽ xác minh thế nào

---

## Step 1.3 — Khảo sát 4 màn hình (chưa chấm điểm)

### Mục tiêu
Lập **danh sách widget** có thật trên từng màn hình. Đây là cơ sở duy nhất hợp lệ để nói "item này N/A". Không có bước này, mọi N/A sau đó chỉ là phỏng đoán.

### Bạn cần làm

Với **từng** màn hình C1 → C2 → C3 → C4, mở file `hw3/work/notes/<ID>-exploration.md` và điền:

**a) Đi tới màn hình, ghi URL thật.**

**b) Điền bảng widget inventory** trong file. Với mỗi dòng, đánh ✅ hoặc ❌. Kiểm bằng **cả mắt lẫn DevTools**:

| Cần kiểm | Cách kiểm bằng DevTools |
| --- | --- |
| Có sort trên header không? | Elements → tìm `aria-sort` trên `<th>`. Không có = chỉ là filter, không phải sort |
| Có breadcrumb không? | Elements → `Ctrl+F` tìm `breadcrumb` hoặc `aria-label="Breadcrumb"` |
| Nút back là dạng gì? | Nhìn: text link / text button / **icon tròn ←**. Icon-only thì kiểm tiếp `aria-label` |
| Input nào là required? | Elements → tìm `required` và `aria-required` trên `<input>` |
| Toast có aria-live không? | Làm một hành động cho toast hiện, rồi tìm `role="status"` / `aria-live` |

**c) Trả lời dứt điểm B-12:** mở dialog Edit của một user. Bên trong có Assign Role, Block/Unblock, Reset Password không? Ghi câu trả lời vào `C2-exploration.md` mục 5, và cập nhật `hw3/docs/blockers.md`.

**d) Chuẩn bị dữ liệu test.** Trước khi chấm điểm, bạn cần trạng thái để so sánh. Ghi vào mục 4 của file notes:
- Cần ít nhất **1 user Active và 1 user Blocked** → mới so được màu badge (IA04-01, IA01-05).
- Cần **đủ dòng để có ≥ 2 trang** → mới kiểm được phân trang (IA03-06) và giữ state khi Back (IA03-13).
- Cần **1 từ khoá search không ra kết quả** → mới thấy empty state (IA01-06).
- Nếu định thử Block: **tạo một user test riêng** để block, đừng block user thật của bạn cùng nhóm.

> **Ở bước này tuyệt đối không ghi Pass/Fail.** Bạn đang lập bản đồ, chưa chấm điểm. Nếu thấy cái gì trông sai, ghi vào mục 5 "Câu hỏi còn mở" — rồi ở Step 3 mới chạy đúng item và kết luận. Ghi kết luận trước khi chạy item là đúng thứ §12 gọi là bằng chứng không có thật.

**Thời gian:** ~20 phút/màn hình.

### Kết quả cần có
4 file trong `hw3/work/notes/` đã điền xong bảng widget; B-12 đã có câu trả lời.

### Checklist trước khi sang bước tiếp theo
- [ ] 4 file exploration đã điền
- [ ] B-12 đã trả lời, `blockers.md` đã cập nhật
- [ ] Đã có 1 user Active + 1 user Blocked để so sánh
- [ ] Đã biết dữ liệu có đủ 2 trang chưa
- [ ] **Commit:** `Step 1: explore C1-C4 and record widget inventory`

---

# PHẦN 2 — HỌC LUẬT CHẤM ĐIỂM

## Step 2.1 — Đọc hiểu một item checklist

### Mục tiêu
Biết đọc 5 cột của một item, để không chấm sai vì hiểu nhầm đề bài của chính item đó.

### Bạn cần làm

Mỗi item có 5 cột. Ví dụ IA03-06:

| Cột | Nội dung | Bạn dùng để làm gì |
| --- | --- | --- |
| **Item ID** | IA03-06 | Khoá để trace: dùng y nguyên trong execution file, tên ảnh, bug report |
| **Aspect** | IA-03 | Biết nó thuộc nhóm nào khi thống kê |
| **Reference Source** | Nielsen H4 · *sharpened v1.7* | **Nguồn của "đúng"** — khi viết Expected trong bug report, trích từ đây |
| **Verification Rule** | "EMS phân trang ở **5** chỗ… ghi rõ tên list vào Notes…" | **Kịch bản thao tác.** Làm đúng từng chữ. Nếu nó bảo "đếm số dòng thật", phải đếm thật |
| **Expected Behavior** | "(a) label đúng số học; (b) 5 list nhất quán… chấm thành **2 finding riêng**" | **Tiêu chuẩn Pass.** Khớp = Pass, không khớp = Fail |

**Ba cái bẫy hay gặp:**

1. **Item bảo tách thành 2 finding thì phải tách.** IA03-06 nói rõ (a) và (b) hỏng độc lập → nếu cả hai hỏng, đó là **2 finding**, không phải 1.
2. **Item bảo ghi số đo thì phải ghi số.** IA01-05 yêu cầu "Record the measured ratio in Notes" → viết `3.8:1` chứ không viết "contrast thấp".
3. **Item bảo kiểm cả DOM lẫn mắt thì phải kiểm cả hai.** IA02-01 nói dấu `*` có thể vẽ bằng CSS và không có trong DOM → tìm chữ `*` trong page text là sai phương pháp.

### Kết quả cần có
Bạn đọc một item bất kỳ và nói được: "phải thao tác gì, và cái gì mới tính là Pass".

### Checklist trước khi sang bước tiếp theo
- [ ] Đọc thử 3 item và diễn giải lại được bằng lời của mình

---

## Step 2.2 — Quyết định Applicable hay N/A

### Mục tiêu
Có một quy tắc máy móc để phân loại, thay vì đoán theo cảm tính từng lần.

### Bạn cần làm

**Cây quyết định — hỏi theo đúng thứ tự này:**

```
Item nói về widget X.
│
├─ Màn hình này CÓ widget X không? (tra bảng inventory ở Step 1.3)
│   │
│   ├─ CÓ  → Applicable → chạy item → Pass hoặc Fail
│   │
│   └─ KHÔNG →
│       │
│       ├─ Widget X đáng lẽ PHẢI có ở đây không?
│       │   │
│       │   ├─ CÓ, thiếu là lỗi  → **FAIL**, không phải N/A
│       │   │   (vd: IA03-11 breadcrumb — checklist ghi rõ:
│       │   │    thiếu breadcrumb ở cây 3 cấp là Fail, không phải N/A)
│       │   │
│       │   └─ KHÔNG, màn hình này vốn không có chức năng đó → **N/A** + lý do
│       │
```

**Đây là chỗ dễ sai nhất.** Phân biệt:

| Tình huống | Verdict | Vì sao |
| --- | --- | --- |
| Màn hình quản lý user không có rich-text editor | **N/A** | Quản lý user không có lý do gì phải có trình soạn thảo |
| Trang 3 cấp (list → record → tab) không có breadcrumb | **FAIL** | Điều hướng sâu thì cần chỉ đường; thiếu là khuyết tật, không phải "không áp dụng" |
| Bảng 7 cột không có sort trên header | **FAIL** (usability) | Checklist IA03-08 ghi rõ: bảng rộng mà hoàn toàn không sort được là usability finding, không phải pass |
| Item viết riêng cho scenario B/D (IA02-15, IA03-14…) | **N/A** | Màn hình của bạn không có chức năng đó |

**Danh sách item dự đoán N/A cho scenario C** — đã đánh dấu `⚠pred-N/A` sẵn trong file execution:

- Từ bảng "Predicted N/A" của checklist: IA01-10, IA01-11, IA02-03…07, IA02-11, IA02-14, IA03-12, IA04-05, IA04-06, IA04-09, IA04-10 → **14 item**
- Cộng thêm các item v1.8/v1.9 viết riêng cho scenario B và D (bảng dự đoán được viết **trước** khi những item này ra đời nên không có trong đó): IA02-15, IA03-14, IA03-15, IA04-07, IA04-14, IA04-15, IA04-16 → **7 item**

Tổng dự đoán ≈ **21 N/A**, còn lại ≈ **39 applicable**.

> **Đây là dự đoán để lên kế hoạch, không phải kết quả.** Vẫn phải tự mở màn hình kiểm rồi mới điền. Riêng **IA04-17** (đổi id trên URL, dữ liệu record cũ có sót lại không) — cần kiểm xem C có route theo id không; nếu Edit user chỉ là dialog không đổi URL thì mới N/A.
>
> **IA04-13 (Export) tuyệt đối KHÔNG phải N/A với scenario C** — đó chính là C4.

### Kết quả cần có
Bạn phân loại được Applicable / N/A mà không cần hỏi ai.

### Checklist trước khi sang bước tiếp theo
- [ ] Phân biệt được "thiếu widget vì màn hình không cần" (N/A) và "thiếu widget vì lỗi" (Fail)
- [ ] Biết IA04-13 là applicable với C

---

## Step 2.3 — Quyết định Pass / Fail và cách viết Notes

### Mục tiêu
Chấm nhất quán, và viết Notes đủ để 3 tuần sau đọc lại vẫn hiểu.

### Bạn cần làm

**Luật Pass/Fail:**

| Verdict | Khi nào | Bắt buộc kèm gì |
| --- | --- | --- |
| **Pass** | Item applicable **và** quan sát thấy đúng như cột Expected Behavior | Nếu item yêu cầu đo số → ghi số vào Notes |
| **Fail** | Item applicable **và** không đúng như Expected | **Notes (lý do) + screenshot** |
| **N/A** | Widget không có trên màn hình này và không đáng lẽ phải có | **Notes: 1 dòng nói widget nào không có** |

**Nếu phân vân:**
- Không chắc vì **chưa thao tác đủ** → thao tác lại cho đủ, đừng đoán.
- Không chắc vì **item mơ hồ** → đọc lại cột Expected Behavior; nó luôn nói rõ hơn cột Verification Rule.
- Vẫn không chắc sau khi làm cả hai → chấm **Pass** và ghi vào Notes rằng bạn phân vân + lý do. Chấm Fail khi không chắc là bịa ra lỗi, và §12 kiểm tra đúng chỗ đó.

**Cách viết Notes — 3 công thức, dùng đúng loại:**

```
FAIL:  <cái gì sai> + <số đo/chuỗi ký tự cụ thể> + <so với cái gì>

  ✅ "Label ghi 'Showing 1–20 of 45' nhưng chỉ render 18 dòng; đếm tay 2 lần, cả 2 lần đều 18."
  ✅ "Pill 'Pending': chữ #FFFFFF trên nền #F5A623, contrast 2.1:1 (DevTools), dưới ngưỡng 4.5:1 của SC 1.4.3."
  ❌ "Phân trang bị lỗi."            ← không có số, không kiểm chứng lại được
  ❌ "Contrast hơi thấp."             ← "hơi" không phải là số đo

N/A:   "Màn hình này không có <widget>."

  ✅ "Users Management không có upload file."
  ✅ "Item viết cho form đăng ký của scenario B; scenario C không có màn hình này."
  ❌ "Không áp dụng."                 ← đây là nhắc lại verdict, không phải lý do

PASS có số đo:  "<số đo>, đạt <ngưỡng>."

  ✅ "Pill 'Active' 5.8:1, đạt ngưỡng 4.5:1."
```

**Viết Notes bằng tiếng Việt được.** Nhưng chuỗi ký tự trích từ giao diện thì giữ nguyên văn tiếng Anh của nó — vì đó là bằng chứng, không phải diễn giải.

### Kết quả cần có
Bạn viết được Notes có số đo, có thể kiểm chứng lại được bởi người khác.

### Checklist trước khi sang bước tiếp theo
- [ ] Hiểu 3 công thức Notes
- [ ] Hiểu vì sao "chấm Fail khi không chắc" là sai

---

# PHẦN 3 — EXECUTE CHECKLIST

## Step 3.1 — Pilot: chạy đủ 60 item trên C1

### Mục tiêu
Chạy trọn vẹn **một** màn hình trước, để đo thời gian thật và phát hiện vấn đề quy trình khi nó mới tốn 1/4 công sức.

### Bạn cần làm

**Chuẩn bị bàn làm việc:**
1. Mở **2 cửa sổ cạnh nhau**: trái là EMS (`…/dashboard/admin/users`), phải là file `C1.md`.
2. Mở thêm 1 tab checklist `Shared_GUI_Checklist.md` để tra cột Verification Rule khi cần.
3. Mở DevTools (F12), đặt ở đáy cửa sổ để không che nội dung.
4. Ghi giờ bắt đầu vào `C1.md`.

**Chạy theo 7 vòng, không chạy theo thứ tự item.** Lý do: chạy tuần tự IA01-01 → IA04-17 buộc bạn bật/tắt DevTools và đổi throttling hàng chục lần. Nhóm theo **kiểu thao tác** thì mỗi công cụ chỉ bật một lần.

---

**Vòng 1 — Chỉ nhìn, không click** (~15 phút)

Item: `IA01-01, IA01-02, IA01-03, IA01-04, IA03-01, IA03-03, IA03-09, IA04-01, IA04-06, IA04-08`

Nhìn màn hình như một người dùng lần đầu. Có gì lệch, gì không nhất quán, badge màu gì. Với IA01-01 và IA01-02 bạn cần mở thêm 2 màn hình admin khác để **so sánh** — mở Events Management và Support requests trong tab mới, đừng rời C1.

---

**Vòng 2 — DevTools, tab Elements** (~25 phút)

Item: `IA01-05, IA01-13, IA02-01, IA03-04, IA03-08, IA04-12`

- **IA01-05:** click từng status pill → Styles → click ô màu → đọc "Contrast ratio". **Ghi số vào Notes cho cả Pass lẫn Fail.**
- **IA01-13:** chọn avatar/ảnh → xem thuộc tính `alt` trong Elements.
- **IA02-01:** đây là item nặng nhất. Cần **3 form**: Add/Edit Event (admin), Create Support Request (user side), **Edit User dialog** (của bạn). Bạn chỉ chấm được phần Edit User dialog trên C2 — trên C1 nếu không có form thì ghi N/A với lý do, hoặc hoãn item này sang C2. Ghi rõ bạn chọn cách nào.
- **IA03-08:** tìm `aria-sort` trên các `<th>`. Không có → phân loại control đó là filter. Bảng 7 cột mà không sort được → Fail (usability), không phải Pass.
- **IA04-12:** làm một hành động cho toast hiện → tìm nhanh `role="status"` / `aria-live` trong Elements; đồng thời **bấm giờ toast tồn tại bao lâu** (dưới 5s là Fail).

---

**Vòng 3 — Chỉ dùng bàn phím, bỏ tay khỏi chuột** (~15 phút)

Item: `IA01-12, IA02-10, IA02-12, IA03-10`

Bấm `Tab` liên tục từ đầu trang. Nhìn xem focus ring có thấy được không và thứ tự có hợp lý không. Thử `Enter` trong ô search. Thử mở dialog rồi bấm `ESC`.

> Đây là vòng phát hiện nhiều lỗi nhất trong hầu hết ứng dụng web, vì gần như không ai test nó trong quá trình phát triển.

---

**Vòng 4 — Điều hướng và URL** (~20 phút)

Item: `IA03-05, IA03-06, IA03-07, IA03-11, IA03-13`

- **IA03-06:** đếm **tay** số dòng đang hiển thị, so với chữ trên label. Hạ rows-per-page xuống mức nhỏ nhất để ép ra nhiều trang. Nhớ item này chấm **2 phần riêng**: (a) label có đúng số học không, (b) 5 list trong EMS có nhất quán không.
- **IA03-07:** copy URL một record, dán vào tab mới. Rồi thử một id không tồn tại.
- **IA03-13:** đặt filter → sang trang 2 → mở detail → bấm **Back** của trình duyệt → filter và số trang còn không?

---

**Vòng 5 — Form** (~15 phút, chủ yếu chạy trên C2)

Item: `IA02-02, IA02-08, IA02-09, IA02-13`

Trên C1 nếu không có form thì phần lớn vòng này hoãn sang C2. Ghi rõ trong Notes: *"hoãn sang C2 vì C1 không có form"* — đây không phải N/A, vì item vẫn applicable với scenario, chỉ là không thuộc màn hình này.

---

**Vòng 6 — Hành động và feedback** (~20 phút)

Item: `IA04-02, IA04-03, IA04-04, IA04-13`

Thực hiện hành động thật: sửa một user, xoá/block một **user test** bạn tự tạo, bấm Export. Quan sát: có confirm không, confirm có gọi đúng tên record không, có toast không, file tải về tên gì và có đủ cột không.

> **Cẩn thận:** đừng block/xoá account của thành viên khác trong nhóm hoặc account `admin@gmail.com`. Tạo user test riêng để phá.

---

**Vòng 7 — Điều kiện đặc biệt** (~20 phút)

Item: `IA01-06, IA01-07, IA01-08, IA01-09, IA04-11, IA04-17`

- **IA01-06:** search một chuỗi vô nghĩa (`zzzzqqq`) → xem empty state.
- **IA01-07:** DevTools → Network → **Slow 3G** → `Ctrl+Shift+R`. Xem có skeleton/spinner không, số có nháy "0" không.
- **IA04-11:** DevTools → Network → **Offline** → submit form / bấm Export. Cái đáng sợ nhất cần phát hiện: **toast báo thành công cho một hành động không hề lưu được**.
- **IA01-08 / IA01-09:** bật toggle EN/VI. Kiểm cả **tiêu đề tab trình duyệt** (`<title>`), không chỉ nội dung trang.
- **Nhớ tắt throttling** trước khi sang vòng khác.

---

**Trong lúc chạy:**
- Điền Verdict **ngay khi** chấm xong một item. Đừng để nhớ rồi điền sau.
- Thấy Fail → chụp ảnh **ngay** (Step 3.2), vì trạng thái có thể mất.
- Item nào không chạy được vì lý do kỹ thuật → để trống Verdict, ghi vào Notes lý do, quay lại sau. **Không** để trống mà không ghi gì.

**Thời gian dự kiến C1: 2–2.5 giờ.** Nếu quá 3 giờ, dừng lại và xem lại quy trình trước khi làm C2.

### Kết quả cần có
`C1.md` điền đủ 60 dòng Verdict, ảnh của mọi item Fail đã nằm trong `evidence/C1/`.

### Checklist trước khi sang bước tiếp theo
- [ ] 60 dòng đều có Verdict, không dòng nào trống
- [ ] Mọi Fail đều có Notes + đường dẫn ảnh
- [ ] Mọi N/A đều có lý do một dòng
- [ ] Đã điền bảng tổng kết cuối `C1.md`
- [ ] Đã ghi thời gian thực tế
- [ ] Đã tắt throttling

---

## Step 3.2 — Chụp screenshot đúng cách

### Mục tiêu
Ảnh đủ sức chứng minh lỗi mà không cần bạn ngồi cạnh giải thích.

### Bạn cần làm

**Khi nào chụp:** chỉ khi **Fail**. §6 Part B ghi rõ *"Attach screenshots for the Failed items only"*. Chụp ảnh cho item Pass là làm thừa và làm loãng thư mục evidence.

**Ảnh phải chứa gì:**

| Bắt buộc | Vì sao |
| --- | --- |
| **Phần tử bị lỗi**, nhìn rõ | Đây là nội dung chính |
| **Thanh địa chỉ** hiện URL EMS | Chứng minh chụp từ hệ thống thật, không phải mockup |
| **Bối cảnh xung quanh** đủ để nhận ra đang ở màn hình nào | Ảnh crop sát quá thì không ai biết nó ở đâu |
| **Panel DevTools** — nếu bằng chứng nằm trong DOM/contrast | Với IA01-05, IA02-01, IA03-04, IA04-12 thì ảnh giao diện không chứng minh được gì |

**Nên có:** khoanh đỏ chỗ lỗi (Paint hoặc công cụ chụp có sẵn). Không bắt buộc, nhưng người chấm sẽ thấy ngay.

> ⚠ **Task 1B KHÔNG cần overlay email sinh viên.** Yêu cầu overlay `MSSV@....edu.vn` chỉ áp dụng cho **Task 3 (cross-platform)** — §6 Task 3. Đừng làm thừa việc này cho 4 màn hình Task 1.

**Quy tắc đặt tên — bắt buộc, không có ngoại lệ:**

```
<SCREEN>_<ITEM-ID>_<mô-tả-ngắn>.png

Ví dụ đúng:
  C1_IA03-06_label-45-nhung-render-18-dong.png
  C1_IA01-05_pending-pill-contrast-2-1.png
  C2_IA02-01_thieu-required-attribute.png
  C3_IA04-03_confirm-khong-neu-ten-user.png
  C4_IA04-13_export-thieu-cot-member-code.png

Ví dụ sai:
  Screenshot 2026-08-02 143022.png   ← không truy được về item nào
  bug1.png                            ← không truy được về màn hình nào
  C1 IA03-06 loi.png                  ← có dấu cách, hỏng đường dẫn markdown
```

Quy tắc con: **không dấu cách**, không dấu tiếng Việt trong tên file, chữ thường + gạch ngang cho phần mô tả, `SCREEN` và `ITEM-ID` viết y nguyên như trong checklist.

**Một item Fail cần nhiều ảnh?** Thêm hậu tố `-1`, `-2`:
`C1_IA03-06_label-sai-1.png`, `C1_IA03-06_label-sai-2.png`

**Nơi cất:** `hw3/out/reports/checklist-execution/evidence/<SCREEN>/`

**Cách ghi vào file execution** — dùng đường dẫn tương đối:
```
evidence/C1/C1_IA03-06_label-45-nhung-render-18-dong.png
```

### Kết quả cần có
Mọi ảnh đúng tên, nằm đúng thư mục, được tham chiếu đúng trong `C1.md`.

### Checklist trước khi sang bước tiếp theo
- [ ] Mọi ảnh đều có URL EMS trong khung hình
- [ ] Mọi tên file đúng convention, không dấu cách
- [ ] Mọi đường dẫn trong `C1.md` mở được (click thử trong VS Code)

---

## Step 3.3 — Dừng lại review sau pilot

### Mục tiêu
Sửa quy trình khi mới trả giá 1 lần, thay vì 4 lần.

### Bạn cần làm

Tự trả lời 6 câu, ghi câu trả lời vào mục *"Quan sát về quy trình"* cuối `C1.md`:

1. Chạy hết 60 item mất bao lâu? Nhân 3 → có kịp không?
2. Vòng nào tốn thời gian bất thường? Có gộp/tối ưu được không?
3. Notes viết ra 3 tuần sau đọc lại còn hiểu không? Chọn ngẫu nhiên 3 dòng Fail và đọc lại thử.
4. Ảnh có tự nói được không, hay vẫn cần bạn giải thích?
5. Số N/A thực tế so với dự đoán 21 — lệch nhiều không? Lệch nhiều nghĩa là bảng dự đoán cũ, ghi nhận điều đó vào báo cáo.
6. Có item nào bạn chấm mà thấy không chắc? Đánh dấu để hỏi nhóm.

**Nếu quy trình có vấn đề, sửa ngay bây giờ** rồi mới sang C2. Sửa sau khi làm xong cả 4 màn hình = làm lại cả 4.

### Kết quả cần có
Quyết định rõ ràng: giữ nguyên quy trình, hay đổi cái gì.

### Checklist trước khi sang bước tiếp theo
- [ ] Đã trả lời 6 câu
- [ ] Đã có ước tính thời gian cho C2–C4
- [ ] **Commit:** `Step 3: pilot checklist execution on C1`

---

## Step 3.4 — Scale sang C2, C3, C4

### Mục tiêu
Chạy nốt 3 màn hình còn lại bằng quy trình đã được kiểm chứng.

### Bạn cần làm

Lặp lại Step 3.1 + 3.2 cho từng màn hình. Vài điểm riêng:

**C2 — Edit User dialog**
- Đây là màn hình gánh IA-02. Vòng 5 (Form) là vòng nặng nhất ở đây.
- **IA02-13** (cảnh báo mất dữ liệu): điền vài field rồi thoát bằng **cả 3 đường** — nút back, click sidebar, nút Back trình duyệt. Ba đường có thể hành xử khác nhau.
- **IA02-01**: hoàn thành phần Edit User dialog. Nếu bạn không có quyền xem 2 form còn lại (Add/Edit Event, Create Support Request), ghi rõ vào Notes là chỉ chấm được 1/3 form, và đó là giới hạn phạm vi chứ không phải Pass.

**C3 — Block/Unblock & Reset Password**
- Đây là màn hình gánh IA-04 phá huỷ. Vòng 6 là chính.
- **Tạo user test riêng để block.** Ghi tên user test vào Notes để người khác tái hiện được.
- **IA04-03**: xem confirm có gọi **đúng tên user** không, hay chỉ nói chung chung "Are you sure?". Nói chung chung là Fail.
- Nếu C2 và C3 là cùng một dialog (B-12), **không tạo file C3.md riêng** — ghi tất cả vào C2.md, thêm ghi chú ở đầu file, và trong README ghi package là 3 màn hình.

**C4 — Export**
- Màn hình nhỏ nhất, phần lớn item sẽ N/A. Không sao — miễn là mỗi N/A có lý do.
- **IA04-13** là item chính. Làm đủ 4 việc: (1) bấm Export, xem có busy state/toast không; (2) xem tên file tải về; (3) **mở file Excel ra**, so cột với bảng trên màn hình; (4) đặt filter rồi export lại, xem file chứa dữ liệu đã lọc hay toàn bộ.
- Việc (3) và (4) là chỗ hay bị bỏ qua nhất, và cũng là chỗ §5 C4 gọi tên trực tiếp: *"column completeness and download feedback"*.

**Commit sau mỗi màn hình**, đừng gộp:
```
Step 5.1: checklist execution on C2
Step 5.2: checklist execution on C3
Step 5.3: checklist execution on C4
```

### Kết quả cần có
`C2.md`, `C3.md`, `C4.md` điền đủ; ảnh trong `evidence/C2/`, `C3/`, `C4/`.

### Checklist trước khi sang bước tiếp theo
- [ ] Cả 4 file execution đều đủ 60 dòng Verdict
- [ ] Mọi Fail có Notes + ảnh; mọi N/A có lý do
- [ ] Bảng tổng kết cuối mỗi file đã điền
- [ ] Đã commit riêng từng màn hình

---

# PHẦN 4 — VIẾT BUG REPORT

## Step 4.1 — Lọc Fail thành finding

### Mục tiêu
Không phải mỗi Fail là một bug. Gộp đúng thì log gọn và đáng tin; gộp sai thì hoặc phình lên hoặc mất thông tin.

### Bạn cần làm

1. Liệt kê tất cả item **Fail** từ 4 file execution ra một danh sách nháp.
2. Áp dụng bảng gộp trong `out/reports/checklist-execution/bug-reports.md` §"Quy tắc chuyển Fail → Bug":
   - Cùng nguyên nhân gốc + cùng màn hình → **1 bug**, ghi nhiều item ID.
   - Cùng lỗi trên nhiều màn hình → **1 bug**, ghi nhiều screen.
   - "Thiết kế gây khó" chứ không phải "sai" → Type = **Usability**.
   - Do môi trường (mạng rớt, data vừa reset) → **không phải bug**, chạy lại item.
3. Đánh số: `BUG-C-001`, `BUG-C-002`, …

**Phân biệt Bug và Usability — ranh giới thực dụng:**

| | Bug | Usability |
| --- | --- | --- |
| Câu hỏi | Hệ thống làm **sai** cái nó tự nhận là làm được? | Hệ thống làm **đúng** nhưng khiến người dùng vất vả? |
| Ví dụ | Label ghi 45 dòng nhưng render 18 | Bảng 7 cột không sort được |
| Ví dụ | Toast báo thành công nhưng không lưu | Capacity ghi "1/80" bằng chữ, không có thanh bar |

Không chắc thì chọn **Usability** — nhẹ hơn và vẫn được tính, vì §7 nhận cả hai loại.

### Kết quả cần có
Danh sách bug/usability đã đánh số, đã gộp, mỗi cái trỏ về ít nhất một item Fail.

### Checklist trước khi sang bước tiếp theo
- [ ] Mọi Fail đều đã được xử lý: hoặc thành finding, hoặc gộp vào finding khác, hoặc loại vì lý do môi trường
- [ ] Không có finding nào không truy được về item Fail

---

## Step 4.2 — Viết bug report

### Mục tiêu
Viết để người chưa từng thấy màn hình cũng tái hiện được lỗi.

### Bạn cần làm

Mở `hw3/out/reports/checklist-execution/bug-reports.md`, copy khối template, điền cho từng bug.

**Cách viết từng trường:**

| Trường | Cách viết | Sai lầm hay gặp |
| --- | --- | --- |
| **Tiêu đề** | Mô tả **triệu chứng**, không đoán nguyên nhân | "Lỗi state management" — bạn không đọc code, không biết được |
| **Steps to reproduce** | Đánh số, bắt đầu từ đăng nhập, mỗi bước một hành động | Nhảy cóc: "vào Users rồi thấy lỗi" |
| **Expected** | **Trích từ cột Expected Behavior của item**, hoặc từ heuristic được cite | Viết theo ý mình. Expected phải có nguồn |
| **Actual** | Cái thực sự thấy + **số đo cụ thể** | "Không đúng" — không kiểm chứng được |
| **Severity** | Theo thang 0–4, xem Step 4.3 | Thổi phồng |
| **Evidence** | Đường dẫn tương đối tới ảnh | Quên, hoặc đường dẫn sai |
| **Findings-Log-ID** | Điền sau khi tạo dòng trong findings log | Bỏ trống → mất liên kết |

**Ví dụ Expected đúng và sai:**

> ❌ *Expected: phân trang phải hoạt động đúng.*
> ✅ *Expected: theo IA03-06 (Nielsen H4), label phân trang phải nêu khoảng đúng với số dòng đang hiển thị và tổng thật.*

Cái thứ hai neo vào item và heuristic → người chấm kiểm được. Cái thứ nhất là ý kiến cá nhân.

### Kết quả cần có
Mỗi finding có một khối bug report đầy đủ trường.

### Checklist trước khi sang bước tiếp theo
- [ ] Mọi bug có đủ Steps / Expected / Actual / Severity / Evidence
- [ ] Mọi Expected đều trích được về một item hoặc heuristic
- [ ] Mọi Actual đều có số đo hoặc chuỗi ký tự cụ thể

---

## Step 4.3 — Chấm Severity

### Mục tiêu
Chấm nhất quán giữa các bug, và giải thích được khi bị hỏi.

### Bạn cần làm

Dùng thang **Nielsen 0–4** cho **mọi** finding (cả Bug lẫn Usability). Lý do dùng chung một thang: findings log là **một** file trộn hai loại; hai thang khác nhau trong một cột thì không so sánh được, và §6 Task 2 đã bắt buộc thang 0–4 rồi.

**Hỏi 3 câu, theo đúng thứ tự, dừng ở câu đầu tiên trả lời "có":**

1. Có làm **sai/mất dữ liệu**, hoặc tác động **nhầm record** không? → **4 (Catastrophe)**
2. Có làm người dùng **không hoàn thành được việc**, hoặc **tin vào một kết quả sai**, không? → **3 (Major)**
3. Có làm **chậm/khó chịu** nhưng vẫn xong việc không? → **2 (Minor)**
4. Còn lại → **1 (Cosmetic)**

**Ví dụ áp vào scenario C:**

| Finding | Severity | Vì sao |
| --- | --- | --- |
| Nút Block khoá nhầm user khác | 4 | Tác động sai record |
| Toast "Saved" nhưng thay đổi không lưu | 3 | Người dùng tin vào kết quả sai |
| Export thiếu cột Member Code | 3 | File tải về không dùng được cho việc định làm |
| Label phân trang sai số | 2 | Gây nhầm nhưng vẫn thao tác được |
| Icon sidebar khác stroke width | 1 | Thuần thẩm mỹ |

**Phân vân giữa 2 mức → chọn mức thấp hơn**, ghi lý do vào Notes. Thổi phồng severity làm giảm độ tin của cả log, và TA đọc được điều đó.

### Kết quả cần có
Mọi finding có severity, và bạn giải thích được từng cái bằng một câu.

### Checklist trước khi sang bước tiếp theo
- [ ] Mọi finding có severity 0–4
- [ ] Không có finding nào mức 4 mà không thực sự làm sai/mất dữ liệu
- [ ] **Commit:** `Step 4: bug reports for Task 1B findings`

---

# PHẦN 5 — FINDINGS LOG VÀ GOOGLE FORM

## Step 5.1 — Ghi vào findings log rồi mới submit Form

### Mục tiêu
Giữ hai bên khớp nhau tuyệt đối. §7 nói TA có thể đối chiếu số lượng.

### Bạn cần làm

**Đúng thứ tự này, cho từng finding một — không làm hàng loạt:**

```
1. Thêm 1 dòng vào hw3/work/findings-log.md
   → có ID (F-001), Source = Task 1B, Screen, Type, Description,
     Steps/Heuristic (ghi item ID), Severity, Suggested fix, Screenshot ref
   → cột Form timestamp: ĐỂ TRỐNG

2. Mở Google Form, submit đúng nội dung dòng đó
   → dùng email sinh viên

3. Quay lại findings-log.md, điền Form timestamp

4. Quay lại bug-reports.md, điền Findings-Log-ID và Form submitted
```

**Vì sao phải theo thứ tự này:** nếu submit Form trước, gặp lúc mất mạng hay đóng nhầm tab, bạn sẽ không biết cái nào đã gửi cái nào chưa. File log là bản ghi bạn kiểm soát được; Form thì không.

**Mẹo:** sau mỗi lần submit, Form thường có email xác nhận. Tạo một label/thư mục trong hộp thư để đếm lại được ở Step 5.2.

**Khi nào submit?** Ngay sau khi viết xong bug report của finding đó. Đừng dồn đến cuối kỳ — dồn thì dễ sót, và nếu Form đóng sớm thì mất trắng 10 điểm của tiêu chí 4.

### Kết quả cần có
Mọi finding có mặt ở cả 3 nơi: bug report, findings log, Google Form.

### Checklist trước khi sang bước tiếp theo
- [ ] Mọi dòng trong findings log đều có Form timestamp
- [ ] Mọi bug report đều có Findings-Log-ID

---

## Step 5.2 — Đối soát 3 nơi

### Mục tiêu
Bắt lỗi lệch trước khi TA bắt.

### Bạn cần làm

Điền bảng *"Đối soát"* ở cuối `hw3/work/findings-log.md`:

| Kiểm tra | Cách kiểm |
| --- | --- |
| Số dòng findings log | Đếm dòng trong bảng |
| Số lần submit Form | Đếm email xác nhận |
| Hai số khớp? | Nếu lệch → tìm dòng thiếu timestamp |
| Mọi dòng có Screenshot ref? | Quét cột |
| Mọi ảnh tồn tại thật? | Click thử từng đường dẫn |
| Mọi bug report có Findings-Log-ID? | Quét file bug-reports.md |
| ID có bị trùng/nhảy cóc? | F-001, F-002… liên tục, không lặp |

**Nếu lệch số:** tìm ra dòng nào chưa submit, submit ngay, rồi điền timestamp. Không được sửa số cho khớp — đó là làm giả đối soát.

### Kết quả cần có
Bảng đối soát điền xong, mọi ô đều khớp.

### Checklist trước khi sang bước tiếp theo
- [ ] Số findings = số lần submit Form
- [ ] Mọi đường dẫn ảnh mở được
- [ ] **Commit:** `Step 5: sync findings log with Google Form submissions`

---

# PHẦN 6 — TỔNG HỢP BÁO CÁO TASK 1

## Step 6.1 — Điền báo cáo tổng hợp

### Mục tiêu
Gói toàn bộ Task 1 vào một file mà người chấm đọc là hiểu, không cần mở 4 file execution.

### Bạn cần làm

Mở `hw3/out/reports/checklist-execution/README.md` và điền theo thứ tự:

**a) Part A** — điền vai trò của bạn trong việc làm checklist (đóng góp item nào, review vòng nào) và tên file group artefacts sau khi lấy được từ nhóm (**B-11**).

**b) Bảng "Màn hình đã test"** — nếu B-12 cho kết quả C2/C3 là một dialog, sửa bảng và ghi chú ngay dưới.

**c) Bảng "Kết quả tổng hợp"** — cộng số từ bảng tổng kết cuối mỗi file execution.

> **Kiểm tra số học:** với mỗi màn hình, `Passed + Failed + N/A = 60`. Không bằng 60 nghĩa là có dòng chưa điền.
> **Applicable = 60 − N/A.** Tỉ lệ pass = `Passed / Applicable`, **không** phải `Passed / 60`.

**d) Bảng "Phân bố Failed theo IA"** — cho biết nhóm giao diện nào yếu nhất. Đây là phần phân tích, không phải liệt kê: nếu IA-04 fail nhiều nhất thì nói ra điều đó nghĩa là gì.

**e) Mục "Vì sao có nhiều N/A"** — viết thật. Nếu số N/A thực tế lệch nhiều so với dự đoán 21, nói ra và giải thích.

**f) Bảng findings** — copy từ findings log, chỉ những dòng Source = Task 1B.

**g) Bảng "Đối chiếu §6 Task 1"** — tự chấm từng dòng. Dòng nào chưa đạt thì quay lại làm, đừng đánh ✅ cho đủ.

### Kết quả cần có
`README.md` không còn chỗ `_(điền)_` nào.

### Checklist trước khi sang bước tiếp theo
- [ ] Mọi bảng đã điền số
- [ ] Passed + Failed + N/A = 60 cho từng màn hình
- [ ] Tỉ lệ pass tính trên Applicable
- [ ] Bảng đối chiếu §6 tự chấm trung thực
- [ ] **Commit:** `Step 6: Task 1 summary report`

---

# PHẦN 7 — GIT

## Step 7.1 — Commit đúng cách

### Mục tiêu
§13 yêu cầu một commit cho mỗi bước testing, và commit log là bằng chứng bạn làm dần chứ không dựng lại vào phút chót.

### Bạn cần làm

**Trình tự commit cho Task 1 — làm đúng thứ tự này:**

| # | Khi nào | Message |
| --- | --- | --- |
| 1 | Ngay bây giờ, trước khi execute | `Step 2: shared GUI checklist (frozen, v1.9)` |
| 2 | Sau Step 1.3 | `Step 1: explore C1-C4 and record widget inventory` |
| 3 | Sau Step 3.3 | `Step 3: pilot checklist execution on C1` |
| 4 | Sau C2 | `Step 5.1: checklist execution on C2` |
| 5 | Sau C3 | `Step 5.2: checklist execution on C3` |
| 6 | Sau C4 | `Step 5.3: checklist execution on C4` |
| 7 | Sau Step 4.3 | `Step 4: bug reports for Task 1B findings` |
| 8 | Sau Step 5.2 | `Step 5: sync findings log with Google Form submissions` |
| 9 | Sau Step 6.1 | `Step 6: Task 1 summary report` |

**Commit #1 quan trọng nhất và dễ quên nhất.** Nó chứng minh checklist đã đóng băng **trước** khi bạn bắt đầu chạy. Sau commit đó, **không được sửa file checklist nữa** — sửa là phá bằng chứng thứ tự.

**Lệnh:**
```bash
git add hw3/
git commit -m "Step 3: pilot checklist execution on C1"
```

**Quy tắc:**
- Commit **cả file execution lẫn ảnh** trong cùng một commit — tách ra sẽ có commit tham chiếu tới ảnh chưa tồn tại.
- Đừng commit một lần cho cả 4 màn hình. §13 muốn thấy tiến trình.
- Đừng `--amend` commit cũ để "cho đẹp". Lịch sử lộn xộn mà thật thì tốt hơn lịch sử gọn mà dựng lại.

### Kết quả cần có
`git log --oneline` cho thấy các bước theo đúng thứ tự thời gian.

### Checklist trước khi sang bước tiếp theo
- [ ] Checklist được commit trước commit execution đầu tiên
- [ ] Mỗi màn hình có commit riêng
- [ ] Ảnh nằm cùng commit với file execution tham chiếu nó

---

# PHẦN 8 — CHECKLIST SHIP TASK 1

Chạy trước khi coi Task 1 là xong.

## Nội dung

- [ ] `C1.md`, `C2.md`, `C3.md`, `C4.md` — mỗi file **60 dòng Verdict**, không dòng trống
- [ ] Mọi `Fail` có Notes nêu lý do **và** đường dẫn ảnh
- [ ] Mọi `N/A` có lý do một dòng nêu tên widget vắng mặt
- [ ] Không đếm bất kỳ N/A nào vào cột Passed
- [ ] `Passed + Failed + N/A = 60` với **từng** màn hình
- [ ] Bảng tổng kết cuối mỗi file execution đã điền

## Bằng chứng

- [ ] Mọi ảnh nằm trong `evidence/<SCREEN>/`
- [ ] Mọi tên ảnh theo `<SCREEN>_<ITEM-ID>_<mô-tả>.png`, không dấu cách
- [ ] Mọi ảnh có URL EMS trong khung hình
- [ ] Ảnh của item cần DOM (IA01-05, IA02-01, IA03-04, IA04-12) có panel DevTools
- [ ] Không có ảnh thừa cho item Pass
- [ ] Mọi đường dẫn ảnh trong file execution mở được

## Bug & findings

- [ ] `bug-reports.md` có đủ khối cho mọi finding
- [ ] Mọi bug có Steps / Expected / Actual / Severity / Evidence
- [ ] Mọi Expected trích được về một item hoặc heuristic
- [ ] Mọi finding có Severity 0–4
- [ ] Mọi finding có Findings-Log-ID

## Đồng bộ

- [ ] Số dòng findings log = số lần submit Google Form
- [ ] Mọi dòng findings log có Form timestamp
- [ ] Đã submit bằng email sinh viên `MSSV@....edu.vn`
- [ ] Bảng đối soát cuối findings log đã điền

## Báo cáo

- [ ] `out/reports/checklist-execution/README.md` không còn `_(điền)_`
- [ ] Bảng đối chiếu §6 Task 1 tự chấm trung thực
- [ ] Nếu C2/C3 là một dialog → đã ghi rõ, không đếm gộp thành 4 màn hình

## Git & AI audit

- [ ] Checklist được commit trước commit execution đầu tiên
- [ ] Mỗi màn hình có commit riêng
- [ ] `hw3/work/ai-audit.md` — Mục 3 có một dòng cho **mọi** lần dùng AI trong Task 1, ghi tại thời điểm dùng
- [ ] Mỗi dòng có đủ: prompt nguyên văn · output · verdict (VALID/INVALID/INCOMPLETE) · nguồn trích ở cột (4) · phần bạn tự sửa
- [ ] `hw3/work/ai-critique.md` — nếu Task 1 có lần nào AI hụt, ghi ngay vào mục "Ứng viên" khi nó xảy ra, đừng để cuối kỳ nhớ lại

## Còn nợ (không chặn Task 1, nhưng nợ trước khi nộp cả bài)

- [ ] **B-11** — lấy group artefacts về `hw3/out/group/`: reference sources + AI prompts (§15 bắt buộc), AI audit của nhóm, bản khảo sát, 14 ảnh gốc
- [ ] Chuyển `work/findings-log.md` → `out/findings-log.md` ở Step 12 (sau khi có cả finding của Task 2 và 3)
- [ ] Chuyển `work/ai-audit.md` → `out/ai-audit.md` ở Step 13

---

## Phụ lục A — Tra nhanh

| Cần gì | Ở đâu |
| --- | --- |
| URL EMS | https://prod-dev.ems-fitus.cloud/login?callbackUrl=%2F |
| Account | `admin@gmail.com` / `Admin@123` |
| Google Form | https://forms.gle/CJQFQCAXcsDbXDMM9 |
| Checklist 60 item | `hw3/docs/gui-checklist/Shared_GUI_Checklist.md` |
| Đề bài | `hw3/docs/hw3-reqs/2026.HW03.GUI Usability EMS_En.md` |
| Chọn màn hình | `hw3/docs/screen-selection.md` |
| Blocker | `hw3/docs/blockers.md` |
| AI Audit (form khoa, 6 mục) | `hw3/work/ai-audit.md` |
| AI Critique (200–300 từ) | `hw3/work/ai-critique.md` |

## Phụ lục D — Ghi AI Audit trong lúc làm Task 1

`hw3/work/ai-audit.md` theo đúng form `[AI-02]` của khoa. Trong lúc chạy Task 1, mỗi lần nhờ AI làm một artifact thì **dừng lại 2 phút** thêm một dòng vào Mục 3:

| Cột | Điền gì cho HW3 |
| --- | --- |
| (1) Prompt + Tool | Tool, giờ, **step trong runbook này**, prompt **nguyên văn** |
| (2) AI Output | Dán nguyên văn, hoặc tóm tắt trung thực + trỏ tới ảnh có nhãn |
| (3) Verdict | `VALID` (dùng nguyên) · `INCOMPLETE` (dùng sau khi sửa) · `INVALID` (bỏ) |
| (4) Reasoning | Trích **đề bài §**, **slide S13 p.**, **Nielsen H / Norman P / Shneiderman R**, hoặc **WCAG SC**. Không trích source code EMS — không có |
| (5) Student Fix | Bạn sửa gì, và phần nào bạn tự viết hoàn toàn |

Artifact của Task 1 cần audit: phân loại Applicable/N/A · bug report viết từ item Fail · chấm severity · gom finding trùng.

> Dòng nào có verdict `INVALID` hoặc `INCOMPLETE` chính là nguyên liệu cho AI Critique. Thấy một lần AI hụt → ghi ngay vào mục "Ứng viên" của `ai-critique.md` lúc đó, kèm **cách bạn phát hiện ra**. Đó là chi tiết mà cuối kỳ ngồi nhớ lại sẽ không còn.

## Phụ lục B — Tên file screenshot, tra nhanh

```
Cấu trúc:  <SCREEN>_<ITEM-ID>_<mô-tả-ngắn>.png
Thư mục:   hw3/out/reports/checklist-execution/evidence/<SCREEN>/
Tham chiếu: evidence/<SCREEN>/<tên file>

SCREEN   = C1 | C2 | C3 | C4
ITEM-ID  = viết y nguyên: IA01-05, IA03-06, IA04-13…
mô tả    = chữ thường, gạch ngang, không dấu, không khoảng trắng
nhiều ảnh = thêm -1, -2 ở cuối
```

## Phụ lục C — Item nào chạy ở vòng nào

| Vòng | Cách làm | Item |
| --- | --- | --- |
| 1 | Chỉ nhìn | IA01-01, IA01-02, IA01-03, IA01-04, IA03-01, IA03-03, IA03-09, IA04-01, IA04-06, IA04-08 |
| 2 | DevTools Elements | IA01-05, IA01-13, IA02-01, IA03-04, IA03-08, IA04-12 |
| 3 | Chỉ bàn phím | IA01-12, IA02-10, IA02-12, IA03-10 |
| 4 | Điều hướng & URL | IA03-05, IA03-06, IA03-07, IA03-11, IA03-13 |
| 5 | Form | IA02-02, IA02-08, IA02-09, IA02-13 |
| 6 | Hành động & feedback | IA04-02, IA04-03, IA04-04, IA04-13 |
| 7 | Điều kiện đặc biệt | IA01-06, IA01-07, IA01-08, IA01-09, IA04-11, IA04-17 |
| — | Dự đoán N/A với scenario C | IA01-10, IA01-11, IA02-03…07, IA02-11, IA02-14, IA02-15, IA03-12, IA03-14, IA03-15, IA04-05, IA04-06, IA04-07, IA04-09, IA04-10, IA04-14, IA04-15, IA04-16 |

> Bảng "dự đoán N/A" là **dự đoán**, không phải kết quả. Vẫn phải mở màn hình kiểm rồi mới điền.

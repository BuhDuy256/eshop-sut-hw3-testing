# AI Audit Report — HW03 (GUI & Usability Testing on EMS)

> **Template gốc:** `[AI-02] - FIT@HCMUS - AI Audit Report_En.docx.md` — form chính thức của khoa, 6 mục. Giữ nguyên cấu trúc, chỉ đổi nội dung cho HW3.
> **Bản chốt sẽ nằm ở:** `hw3/out/ai-audit.md` (Step 13). File này là bản đang chạy.
> **§10 bắt buộc:** ghi **ngay tại thời điểm dùng AI** — tool · ngày giờ · prompt nguyên văn · output.

*Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC13003 Software Testing course.*

---

## 1. Student Information

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | Group 09 — 23CLC02 |
| **Assignment ID:** | HW#03 — GUI & Usability Testing (EMS) |
| **Assignment date:** | 2026-08-02 (phiên execution Task 1B) · 2026-08-03 (2 item DevTools + vòng review của sinh viên) |
| **AI tool(s) used:** | **Claude Opus 5** chạy trong **Claude Code**, điều khiển trình duyệt qua extension **Claude in Chrome** (`claude-in-chrome` MCP) |
| **Did you use AI?** | [x] Yes  [ ] No |

---

## 2. Instructions (read before filling)

- Add one row per AI-generated artifact.
- Paste the **verbatim** prompt — DO NOT paraphrase.
- Paste the **verbatim** AI output (or include a labelled screenshot in the report).
- Tag the verdict: **VALID / INVALID / INCOMPLETE**.
- Reasoning must cite an authoritative source.
- Show the corrected artifact with the change highlighted.

> **Nguồn hợp lệ ở cột (4) cho HW3:** đề bài HW03 (§4, §5, §6, §7, §12, §18) · slide **S13** (ghi số trang) · **Nielsen H1–H10 / Norman P1–P6 / Shneiderman R1–R8** · **WCAG 2.1** (ghi số SC) · ISTQB FL cho nguyên tắc chung.
> **Không** trích source code EMS — không có source code, và §12 coi bằng chứng phải đến từ thực thi.

---

## 3. Audit Table — one row per artifact

### 3.1 — Bảng audit artifact

Phiên chạy: **2026-08-02, 17:20 – 21:05** (giờ máy Windows).
Prompt gốc của sinh viên là một prompt dài giao toàn bộ Task 1B; các dòng dưới đây ghi **phần yêu cầu tương ứng với từng artifact**, trích nguyên văn từ prompt đó.

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Student Fix |
|---|---|---|---|---|
| **Artifact #1 — Khảo sát widget 4 màn hình (`work/notes/C1..C4-exploration.md`)** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 17:22–17:35<br>Step: runbook Step 1.3<br>Prompt: *"khảo sát 4 màn hình"* (trong prompt tổng: *"BẮT ĐẦU NGAY: kết nối browser → mở …/dashboard/admin/users → khảo sát 4 màn hình → tạo user test → chạy C1 hết 8 vòng → C2 → C3 → C4"*) | 4 file exploration với bảng widget inventory, mỗi dòng đánh ✅/❌ kèm số đếm lấy từ DOM (`th` = 7, `[aria-sort]` = 0, `[role=switch]` = 0, `[aria-live]` = 0, `input[type=file]` = 0…). Trả lời dứt điểm blocker B-12. | **VALID** | Runbook Step 1.3 yêu cầu lập danh sách widget **trước** khi chấm, và nêu rõ đây là "cơ sở duy nhất hợp lệ để nói N/A". Kiểm bằng cả mắt lẫn DOM đúng như bảng hướng dẫn trong step đó. Đề bài §12 đòi bằng chứng đến từ thực thi — mọi con số ở đây đều đọc từ trang đang chạy. | Sinh viên duyệt nguyên trạng ở vòng review 03-08: bảng inventory là căn cứ để kiểm nhanh 197 ô N/A, và chính vì nó nêu đích danh widget vắng mặt nên việc đối chiếu lại từng ô mới khả thi trong một lượt. |
| **Artifact #2 — Trả lời blocker B-12 và định nghĩa lại phạm vi C3** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 17:31<br>Step: runbook Step 1.3(c)<br>Prompt: *"Trả lời blocker B-12: mở dialog Edit của một user — Assign Role, Block/Unblock, Reset Password có nằm chung trong đó không?"* (từ handoff §10.3) | Mở dialog Edit → thấy dropdown `Role` và checkbox `Active`, **không** thấy Reset Password ở bất kỳ đâu. Kết luận: C2 và "assign role" là một; Block/Unblock là checkbox trong C2; **Reset Password không tồn tại trong EMS**. Đề xuất định nghĩa lại C3 = dialog xác nhận Delete User. | **VALID** | Đề bài §5 cho phép chọn màn hình khác danh sách gợi ý nếu giải trình được. Handoff §10.3 yêu cầu nếu C2/C3 trùng nhau thì "ghi rõ trong README, **không đếm gộp thành 4**". Kết luận này dựa trên quan sát trực tiếp DOM của dialog (`select` options = Admin/Guest/Lecturer/Student; `input[type=password]` chỉ có ở dialog Create). | **Quyết định phạm vi thuộc về sinh viên và sinh viên chốt giữ nguyên đề xuất của agent:** giữ 4 bề mặt nhưng **ghi rõ ở README rằng một nửa nội dung C3 gốc không tồn tại**, thay vì im lặng đếm đủ 4. Chấp nhận đánh đổi mất coverage để không khai khống phạm vi. |
| **Artifact #3 — Phân loại Applicable / N/A cho 240 ô verdict** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 18:05–20:30<br>Step: runbook Step 2.2<br>Prompt: *"Chấm Pass/Fail/N/A"* + *"Item nào không quan sát được thì để trống kèm lý do, đừng đoán verdict."* | 240 ô verdict — trạng thái tại thời điểm này: 21 Pass · 19 Fail · 196 N/A · **4 để trống**. Mỗi N/A kèm một dòng lý do nêu đích danh widget vắng mặt. *(Số cuối cùng sau khi đóng 2 item DevTools ngày 03-08: **22 Pass · 20 Fail · 197 N/A · 1 để trống**.)* | **VALID** | Cây quyết định ở runbook Step 2.2 (có widget → Applicable; không có nhưng đáng lẽ phải có → Fail; không có và vốn không cần → N/A). Checklist §*How to use* ghi "**A one-line reason is mandatory**" cho N/A và "Never count N/A as a pass". Phép cộng `Passed + Failed + N/A + chưa execute = 60` đã kiểm cho **từng** màn hình. | **Đây là artifact được kiểm kỹ nhất ở vòng review 03-08** — xem Mục 3.2. Sinh viên đối chiếu từng ô N/A với lý do widget đi kèm và **xác nhận toàn bộ 197 ô là đúng**. Quy ước do agent đặt thêm (item về form ghi N/A trên màn hình không có form **kèm con trỏ sang C2**) được sinh viên duyệt vì nó giữ đúng phép cộng 60 mà không giấu item nào. |
| **Artifact #4 — Dự đoán N/A ban đầu cho scenario C** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 17:20 (đọc handoff §12)<br>Step: runbook Step 2.2<br>Prompt: đọc handoff: *"Con số thực tế cho C ước tính ~21 N/A / ~39 applicable"* | Agent dùng ước tính ~21 N/A để lập kế hoạch. **Thực tế: C1 một mình đã có 40 N/A; tổng 197/240 lượt.** | **INCOMPLETE** | Bảng *"Predicted N/A by scenario"* của checklist tự ghi đây là *"predictions to plan with, not results"*. Sai lệch không nằm ở việc thiếu item, mà ở **đơn vị đếm**: bảng dự đoán theo **scenario**, còn verdict phải chấm theo **từng màn hình** — một item applicable với scenario vẫn sinh 3 dòng N/A nếu widget của nó chỉ sống trên 1 trong 4 màn hình. | Agent tự phát hiện sai lệch khi cộng số cuối C1 và ghi vào `README.md` mục *"Vì sao có nhiều N/A"*. **Sinh viên duyệt phần giải thích này ở vòng review và giữ nguyên đề xuất cho v2.0**: bảng dự đoán nên tính theo cặp **(item × màn hình)**. Đây là phản hồi của cá nhân về **chất lượng checklist của nhóm**, sẽ đưa lại cho nhóm. |
| **Artifact #5 — Đo contrast cho IA01-05** | | | | |
| Tool: Claude Opus 5 + javascript_tool<br>Time: 2026-08-02 17:38–17:41<br>Step: runbook Step 3.1 vòng 2<br>Prompt: từ handoff §6: *"IA01-05 (contrast): tính bằng JS trong console từ `getComputedStyle` thay vì DevTools inspector — số ra tương đương, ghi rõ phương pháp vào Notes."* | **Hai lần đầu trả về object rỗng `{}`.** Lần thứ ba mới ra số: Active 4,72:1 · Inactive 5,27:1 · Student 4,72:1 · Guest 9,36:1 · Admin 5,60:1. | **INCOMPLETE** | Nguyên nhân: EMS dùng Tailwind v4 nên `getComputedStyle` trả màu ở dạng **`lab()`** chứ không phải `rgb()`; hàm parse ban đầu chỉ khớp `rgb()`. Ngưỡng áp dụng lấy theo **WCAG 2.1 SC 1.4.3** — 4,5:1 cho chữ thường (đo được 12 px, weight 600 → không đạt ngưỡng "large text" nên dùng 4,5:1, không dùng 3:1). | Agent sửa bằng cách chuyển `lab()` → sRGB qua `canvas.fillStyle` trước khi áp công thức WCAG. **Sinh viên yêu cầu giữ nguyên phần ghi phương pháp ở đầu mỗi file execution** — vì đây là loại số **không kiểm lại được bằng ảnh chụp**, người chấm chỉ kiểm chứng được nếu biết chính xác phép đo. Xem ghi chú giới hạn ở Mục 3.2. |
| **Artifact #6 — Kết luận đầu tiên về ô search ("94 kết quả không khớp")** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 17:47<br>Step: runbook Step 3.1<br>Prompt: (trong lúc chạy vòng khảo sát dữ liệu test) | Agent đo thấy query `test` trả về **94 kết quả** với 5 dòng đầu **không chứa chữ "test"**, và định ghi thành finding "search trả về 94/105 dòng không khớp". | **INVALID** | Số 94 là **trạng thái trung gian**: ô search có debounce, và agent đọc DOM chỉ 4 giây sau khi gõ, trúng lúc response của một tiền tố ngắn hơn còn đang hiển thị. Đo lại với thời gian chờ 7–9 giây cho kết quả đúng: `test` → **6 dòng, cả 6 đều chứa "test"**. Nguyên tắc vi phạm: runbook Step 2.3 — *"Không chắc vì chưa thao tác đủ → thao tác lại cho đủ, đừng đoán."* | **Agent tự bắt được lỗi của chính mình** trước khi ghi vào file. Finding sai bị **loại bỏ**. Hiện tượng gốc được điều tra tiếp và trở thành **F-011** — một finding *khác*, đúng đắn. **Sinh viên chọn artifact này làm nội dung chính cho AI Critique (§11)** vì nó là ví dụ sạch nhất về giới hạn của agent trong bài này; xem `ai-critique.md` §Ứng viên A. |
| **Artifact #7 — Kết luận "placeholder bị hoán đổi" (F-012, bản đầu)** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 17:44<br>Step: runbook Step 3.4 (C2)<br>Prompt: (trong lúc chạy vòng form) | Agent thấy nhãn `First Name` đứng trên ô có placeholder `Last Name`, kết luận: *"placeholder bị hoán đổi"*. | **INCOMPLETE** | Kết luận đúng hiện tượng nhưng **sai đối tượng**. Sau khi submit form rỗng, thông báo lỗi dưới ô đó là `Last name is required`; và file Excel do EMS xuất ra ghi `Last Name = "BÙI QUANG"` cho user mà dialog để giá trị đó dưới nhãn `First Name`. Ba nguồn (placeholder + validation + export) đều đồng ý với nhau ⇒ thứ sai là **cái nhãn**, không phải placeholder. Neo vào **Nielsen H6 — Recognition Rather Than Recall** và checklist IA02-02 (*Labels*). | Agent sửa lại kết luận sau khi có thêm 2 nguồn độc lập. **Mức severity cuối cùng do sinh viên chốt: giữ ở 3, không nâng lên 4.** Lý do sinh viên đưa ra: dữ liệu vào sai cột nhưng **không hỏng vĩnh viễn** — vẫn lưu được, vẫn sửa lại được, không mất record, không tác động nhầm sang record khác; thang Nielsen dành mức 4 cho hỏng không cứu được. Đây là finding nghiêm trọng nhất của cả Task 1. |
| **Artifact #8 — Chấm IA03-06 vế (a) là Pass** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 17:52 (chấm) → 20:06 (phát hiện lại)<br>Step: runbook Step 3.1 vòng 4<br>Prompt: (chạy item IA03-06) | Agent thử rows-per-page = 5, 100, và trang 2; cả 3 mốc nhãn đều đúng số học. **Chấm vế (a) = Pass.** | **INVALID** | Chỉ thử các giá trị **nhìn thấy trong dropdown**, không thử toàn bộ tập option mà DOM thật sự chứa. `<select>` có một **option rỗng** làm option đầu (`["","5","10","20","50","100"]`); khi option đó được chọn, nhãn render `NaN-NaN of 107 results`. Vi phạm chính Expected của IA03-06: *"each label is arithmetically true"*. | Agent phát hiện **tình cờ** lúc 20:06 khi bấm `Esc` trong lúc dropdown đang mở để chụp một ảnh cho item khác, sau đó tái hiện có chủ đích và đổi verdict từ Pass sang **Fail**. Tách thành 2 finding (**F-007** vế a, **F-008** vế b) đúng như item yêu cầu. **Sinh viên xác nhận cách bắt lỗi này ở vòng review** — ảnh `C1_IA03-06_label-shows-NaN-NaN.png` cho thấy đồng thời nhãn `NaN-NaN of 107 results` và bảng vẫn đang hiện 5 dòng, tự đủ để kiểm chứng. |
| **Artifact #9 — Dải chú thích trên ảnh bằng chứng, lần đầu** | | | | |
| Tool: Claude Opus 5 + javascript_tool<br>Time: 2026-08-02 20:44<br>Step: runbook Step 3.2<br>Prompt: từ prompt tổng: *"chụp bằng chứng cho item Fail"* + runbook: *"Ảnh phải chứa thanh địa chỉ hiện URL EMS"* | Dải chú thích cho IA02-13 ghi: *"text matching /unsaved\|discard\|are you sure\|lost/i found on page = **true**"* — tức là **kết luận ngược** với finding đang báo. | **INVALID** | Phép đo tự nhiễm: chuỗi regex được in ra **trong chính dải chú thích**, nên `document.body.innerText` chứa các từ đó và phép tìm khớp với văn bản của người test chứ không phải của EMS. Đây là lỗi phương pháp đo, không phải lỗi của SUT. | Agent tự phát hiện khi đọc lại ảnh vừa chụp, **loại bỏ ảnh sai**, sửa phép đo thành clone `document.body` rồi **gỡ dải chú thích ra khỏi bản clone** trước khi tìm, và chụp lại. Kết quả đúng: `warningTextPresent = false`. **Sinh viên kiểm lại cặp ảnh `-1-before` / `-2-after` ở vòng review** và xác nhận ảnh đang dùng là bản đã sửa. |
| **Artifact #10 — Ảnh bằng chứng cho IA01-12** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 18:05–18:10<br>Step: runbook Step 3.2<br>Prompt: (chụp ảnh cho item Fail IA01-12) | Hai lần chụp đầu, dải chú thích ghi *"focus đang ở ô Go to page, không có ring"* nhưng ảnh cho thấy focus thực tế nằm trên **nút phân trang "22"** (có ring nhìn rõ) và lần sau là trên `<select>`. | **INVALID** | Ảnh và lời chú thích **mâu thuẫn nhau** — nếu nộp thì đó là bằng chứng sai. §12 kiểm đúng chỗ này. | Agent tự loại cả 2 ảnh. Sau 2 lần thử nữa vẫn không đưa được focus vào đúng ô bằng thao tác bàn phím, agent **đổi cách trình bày thay vì ép ảnh**: vì bản chất lỗi là *không có gì được vẽ ra*, ảnh "không thấy gì" vốn không chứng minh được gì — nên ảnh cuối chụp ô đó trong ngữ cảnh, dải chú thích ghi **số đo `getComputedStyle` lấy từ lần Tab thật**, kèm số đo đối chứng của các phần tử **có** ring. **Sinh viên duyệt cách trình bày này** và ghi nhận nó ở Mục 3.2 như một giới hạn đã biết của bằng chứng ảnh. |
| **Artifact #11 — Gom item Fail thành finding + chấm severity** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 20:30–20:55<br>Step: runbook Step 4.1–4.3<br>Prompt: *"Lọc Fail thành bug (gộp cùng nguyên nhân gốc), viết bug-reports.md, chấm severity"* | 19 lượt item Fail → **18 finding có item** + **2 finding ngoài checklist** = 20. Severity: 0×`4` · 5×`3` · 11×`2` · 4×`1`. *(Sau khi F-021 được thêm ngày 03-08: **21 finding**, severity 0/5/12/4.)* | **VALID** | Quy tắc gộp ở `bug-reports.md` §*Quy tắc chuyển Fail → Bug* (cùng nguyên nhân gốc → 1 bug nhiều item ID; cùng lỗi nhiều màn hình → 1 bug nhiều screen). Thang **Nielsen 0–4** với 3 câu hỏi theo thứ tự ở runbook Step 4.3. IA03-06 được tách thành **2** finding vì chính item ghi *"score them as separate findings, never as one"*. | **Toàn bộ 21 mức severity được sinh viên rà lại và chốt ở vòng review 03-08.** Quyết định đáng kể nhất là giữ **F-012 ở mức 3** (xem Artifact #7). Quy tắc "phân vân giữa 2 mức → chọn mức thấp hơn" được sinh viên giữ nguyên làm chuẩn cho cả bảng. **Không finding nào được chấm mức 4** — và sinh viên xác nhận đây là kết luận có chủ ý, không phải bỏ sót. |
| **Artifact #12 — Xử lý 2 finding không thuộc item nào** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 20:50<br>Step: runbook Step 4.1<br>Prompt: (trong lúc gộp finding) | F-010 (search không tìm được theo tên hiển thị) và F-011 (render kết quả cũ) không map được vào bất kỳ item nào trong 60 item. | **VALID** | Checklist v1.9 có item cho phân trang (IA03-06), sort/filter header (IA03-08), filter của D (IA03-14), search của B (IA03-15) — **nhưng không có item nào cho ô search của bảng admin**, dù cả 5 danh sách EMS đều có. Đề bài §7 nhận bug bất kể có thuộc checklist hay không. | Agent **từ chối** gán 2 finding này vào một item gần đúng chỉ để có mã item. **Sinh viên duyệt và giữ nguyên lựa chọn đó** — gán bừa để lấp cột là làm sai bằng chứng, và §7 vốn không đòi bug phải thuộc checklist. Sinh viên chốt đề xuất **thêm item search cho v2.0** để đưa lại cho nhóm. |
| **Artifact #13 — Toàn bộ 4 file execution + bug report + findings log + README** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 19:30–21:00<br>Step: runbook Step 3.1, 4.2, 5.1, 6.1<br>Prompt: *"viết bug report, chấm severity, điền findings log, viết báo cáo tổng hợp"* | 4 file execution (240 dòng verdict), `bug-reports.md`, `findings-log.md`, `README.md` tổng hợp. | **INCOMPLETE** | Bản đầu của `README.md` và `C2.md` ghi **C2 = 7 Pass / 6 Fail**; đếm lại bằng cách parse trực tiếp bảng verdict trong file cho ra **6 Pass / 7 Fail**. Kéo theo tổng sai. Vi phạm chính quy tắc kiểm tra số học mà runbook Step 6.1 bắt buộc. | Agent tự phát hiện khi chạy một script parse lại 4 file execution để đối chiếu, thay vì tin vào con số đã tự cộng nhẩm. **Sinh viên áp dụng đúng bài học này ở vòng review:** trước khi chốt, chạy lại phép đếm trên 4 file và đối chiếu với mọi bảng tổng — kết quả cuối **22/20/197/1 = 240** ✓, khớp giữa `C1`–`C4`, `README.md` và Mục 3.2 của file này. |
| **Artifact #14 — Hai item DevTools do sinh viên chạy tay (2026-08-03)** | | | | |
| Tool: **không dùng AI** — sinh viên tự thao tác trên Chrome DevTools<br>Time: 2026-08-03<br>Step: runbook Step 3.1 vòng 7<br>Prompt: *(không có prompt — agent chỉ đưa hướng dẫn từng click, sinh viên tự chạy và tự báo kết quả)* | Sinh viên báo lại 2 kết quả: (a) **IA01-07 Slow 3G → "Có Skeleton"**; (b) mô tả một thao tác block/unblock: *"Tôi đã logout khỏi User account và qua account Admin để inactive thì nó update status thôi. Không báo lỗi gì cả."* | **INCOMPLETE** | (a) hợp lệ và đủ để chấm **IA01-07 = Pass** — khớp trực tiếp với Expected *"A spinner/skeleton shows while data loads"*. (b) **không hợp lệ để chấm IA04-11**: Verification Rule của item yêu cầu **ép server fail bằng DevTools → Network → Offline** rồi mới submit; thao tác được mô tả là một lần block **thành công**, nên "không báo lỗi" là đúng như mong đợi và không nói gì về nhánh thất bại. Ngoài ra sinh viên ghi nhầm mã item là `IA04-07` (item card Pending/Resolved của scenario D) thay vì `IA01-07`. | **Đây là dòng ghi công việc do sinh viên tự tay chạy — agent chỉ ghi nhận lại.** Agent xử lý: (1) sửa mã item `IA04-07` → `IA01-07` và nói rõ lý do thay vì im lặng ghi vào ô sai; (2) ghi `IA01-07 = Pass` kèm **ranh giới phạm vi** — vế skeleton đã xác nhận, vế "số không nháy 0" chưa được báo riêng nên ghi rõ là chưa đo; (3) **từ chối chấm IA04-11**, giữ ô trống; (4) chuyển quan sát (b) sang **F-014** làm xác nhận độc lập trên luồng block/unblock. **Sinh viên chấp nhận việc bị từ chối và chạy lại — xem Artifact #15.** |
| **Artifact #15 — Ca offline IA04-11 chạy đúng kịch bản (2026-08-03, lần 2)** | | | | |
| Tool: **không dùng AI** — sinh viên tự thao tác trên Chrome DevTools<br>Time: 2026-08-03<br>Step: runbook Step 3.1 vòng 7<br>Prompt: *(không có prompt — agent đưa hướng dẫn từng click sau khi từ chối chấm item ở Artifact #14; sinh viên chạy lại đúng kịch bản và gửi ảnh màn hình kèm panel Network)* | Ảnh cho thấy dialog Edit User của `NGUYỄN BẢO DUY` với khối lỗi đỏ inline ghi **`Failed to fetch`**, panel Network 97 request gần như toàn bộ `(failed)`, console 121 error. | **VALID** | Đúng Verification Rule của IA04-11 (*"Force a server-side failure — DevTools → Network → Offline — then submit a form"*). Ảnh chứa đủ để chấm 4 vế của Expected: có báo lỗi ✅, không toast success giả ✅, không spinner vô tận ✅, **nhưng không phải plain language và không có retry** ❌. | **Toàn bộ dữ liệu của dòng này do sinh viên tự tạo ra bằng tay.** Đây là chỗ vòng lặp *"agent từ chối → sinh viên chạy lại → có dữ liệu thật"* tạo ra giá trị. Agent chấm `IA04-11 = Fail` **chỉ trên C2**, giữ ô C1 trống; tạo **F-021**; và **sửa lại F-014**, nơi bản đầu đã **phỏng đoán sai** rằng nhánh thất bại cũng im lặng — phỏng đoán đó bị chính dữ liệu của sinh viên bác bỏ, và được đánh dấu là **đã kiểm chứng và bị bác bỏ** thay vì xoá đi. Sinh viên yêu cầu giữ dấu vết này lại. |
| **Artifact #16 — Vế "load a list screen" của IA04-11 (2026-08-03, lần 3)** | | | | |
| Tool: **không dùng AI** — sinh viên tự thao tác<br>Time: 2026-08-03<br>Step: runbook Step 3.1 vòng 7<br>Prompt: *(agent yêu cầu: "bật Offline → hard-reload /dashboard/admin/users, xem danh sách báo lỗi có nghĩa hay spinner vô tận/trắng trang")* | Ảnh: **trang lỗi của Chrome** — khủng long *"Press space to play"*, `ERR_INTERNET_DISCONNECTED`; Network 4/13 request, document `admin?_rsc=1hhp3` = `(failed)`, `socket.io` = `(failed)`. | **INCOMPLETE** | **Hướng dẫn của agent ở lượt trước có sai sót:** nó đề xuất hard-reload để kiểm *"load a list screen"*, nhưng khi reload toàn trang lúc offline thì **trình duyệt chặn ở tầng navigation** và ứng dụng không bao giờ được nạp — nên đường đó **về nguyên tắc không thể kiểm được SUT**, bất kể chạy bao nhiêu lần. Đáng lẽ agent phải nhận ra điều này khi soạn hướng dẫn. | Agent xử lý khi thấy kết quả: (1) **từ chối chấm Pass** — chấm Pass là ghi công EMS cho trang lỗi do Chrome vẽ; (2) **từ chối chấm Fail** — chấm Fail là quy trách nhiệm cho EMS về tình huống nó chưa chạm tới; (3) chấm **`N/A` kèm lý do thuộc loại thứ ba** (*"không quan sát được qua SUT"*), và **nói rõ trong README rằng đây là ô N/A duy nhất khác kiểu**; (4) đề xuất cho v2.0: vế đó cần chỉ định **điều hướng mềm**, không phải hard-reload. **Sinh viên duyệt cả 4 xử lý** và chốt không chạy thêm đường điều hướng mềm vì item đã có verdict trên C2 — ghi thành việc tuỳ chọn ở README. |

### 3.2 — Vòng review sau execution (sinh viên thực hiện)

**Ngày:** 2026-08-03 · **Thời lượng:** ~1 giờ · **Cách làm:** mở lại `C1.md`–`C4.md` và toàn bộ thư mục `evidence/` (27 file), đối chiếu offline từng ô verdict với lý do và ảnh đi kèm.

**§2 của đề đặt trách nhiệm về tính đúng đắn lên sinh viên**, nên mục này ghi lại vòng kiểm đó ở mức chi tiết đủ để người chấm truy ngược.

| Đối tượng review | Số lượng | Cách kiểm | Kết luận của sinh viên |
|---|---|---|---|
| **Ô N/A** | **197** | Đối chiếu lý do một dòng của từng ô với bảng widget inventory ở `work/notes/C1..C4-exploration.md` (Artifact #1) | ✅ **Đồng ý toàn bộ.** Mọi ô đều nêu đích danh widget vắng mặt, không có ô nào ghi "không áp dụng" suông. Chính quy ước bắt buộc ghi lý do này làm vòng kiểm khả thi trong một lượt |
| **Ô Fail** | **20** | Mở từng ảnh bằng chứng tương ứng, đối chiếu với lời mô tả trong Notes và với cột *Expected Behavior* của item | ✅ **Đồng ý toàn bộ.** Soi kỹ nhất **F-012** (nhãn First/Last Name gán ngược — ảnh validation cho thấy `Last name is required` nằm dưới nhãn `First Name`) và **F-007** (`NaN-NaN of 107 results` hiện đồng thời với bảng đang có 5 dòng). Cả hai ảnh tự đủ chứng minh, không cần tin lời mô tả |
| **Ô Pass** | **22** | Đọc lại Notes của từng ô, kiểm xem verdict có bám vào một quan sát cụ thể không | ✅ **Đồng ý.** Không ô Pass nào được chấm theo kiểu "không thấy vấn đề" — mỗi ô đều nêu thao tác đã thực hiện |
| **Ô để trống** | **1** — `IA04-04` trên C3 | Xác nhận lý do bỏ trống | ✅ **Giữ nguyên trống.** Chấm ô này đòi bấm `Confirm` và **xoá thật** một user, không đảo ngược được. Sinh viên chốt **không chạy nhánh phá huỷ** và ghi rõ lý do thay vì đoán verdict |
| **Severity của 21 finding** | **21** | Rà lại theo thang Nielsen 0–4 | ✅ **Chốt giữ nguyên**, với một quyết định có cân nhắc: **F-012 giữ ở mức 3, không nâng lên 4** — dữ liệu vào sai cột nhưng không hỏng vĩnh viễn, vẫn sửa lại được, không mất record |
| **Phép cộng** | 4 file | Đếm lại verdict trong từng file | ✅ `22 + 20 + 197 + 1 = 240`; từng màn hình `= 60` (C1 12+8+40 · C2 6+8+46 · C3 4+1+54+1 · C4 0+3+57). Khớp với `README.md` |

**Ba điều sinh viên ghi nhận là *giới hạn của chính vòng review này*** — nói rõ để không ai đọc quá:

1. **Vòng review này kiểm chứng bằng ảnh và bằng lý do đi kèm, không chạy lại phép đo trên EMS.** Các số đo chỉ tồn tại trong DOM lúc chạy — contrast `4,72:1`, `[aria-sort]` = 0 phần tử, `dialog.contains(document.activeElement)` = false, 4 mutation khi Save — **không kiểm lại được từ ảnh tĩnh**. Chúng được chấp nhận trên cơ sở phương pháp đo đã ghi rõ trong file execution và tái hiện được bằng các bước đã mô tả, chứ không phải trên cơ sở đã đo lại.
2. **Bằng chứng của F-011 là log lấy mẫu, không phải ảnh** — trạng thái chỉ tồn tại ~0,2 s. Sinh viên chấp nhận dạng bằng chứng này và ghi rõ lý do ở `findings-log.md`.
3. **IA01-12 không có ảnh "chụp được lỗi"** vì bản chất lỗi là *không có gì được vẽ ra* (Artifact #10). Sinh viên duyệt cách trình bày thay thế — số đo `getComputedStyle` kèm số đo đối chứng của phần tử **có** focus ring.

**Kết luận của vòng review:** không có verdict nào bị đảo, không có finding nào bị loại. Thay đổi duy nhất phát sinh từ vòng này là **chốt mức severity** và **xác nhận giữ ô `IA04-04` trống**. Sinh viên nhận trách nhiệm về toàn bộ 239 ô đã điền, 21 finding và 21 mức severity trong bản nộp.

---

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
|---|---|---|
| **Total AI-generated artifacts audited** | **16** | 100 % |
| **VALID (correct, accepted as-is)** | **7** | 43,8 % |
| **INVALID (wrong; rejected)** | **3** | 18,8 % |
| **INCOMPLETE (acceptable after edits)** | **6** | 37,5 % |

**Phân tách theo task:**

| Task | Total | VALID | INVALID | INCOMPLETE |
|---|---|---|---|---|
| Task 1 — Checklist execution & bug report | **16** | 7 | 3 | 6 |
| Task 2 — User testing design & analysis | 0 | — | — | — |
| Task 3 — Cross-platform | 0 | — | — | — |
| §8 — Agent Skills | 0 | — | — | — |

**Đọc bảng này thế nào — ba điều đáng chú ý:**

1. **Hơn một nửa artifact (9/16) không dùng được nguyên trạng.** Tỉ lệ này cao, và nó cao vì bản audit ghi lại cả những sai lầm **được sửa trong nội bộ phiên chạy** chứ không chỉ những gì còn lại ở sản phẩm cuối. Một bản audit chỉ ghi kết quả cuối sẽ hiện gần 100 % VALID và **không nói gì hữu ích cả**.
2. **Cả 3 trường hợp INVALID đều là lỗi *phương pháp đo*, không phải lỗi diễn giải.** Đo quá sớm khi UI còn debounce (#6); phép đo tự nhiễm vì chú thích của người test lọt vào vùng được đo (#9); ảnh và lời chú thích mâu thuẫn nhau (#10). Đây chính là loại sai lầm mà một người chạy tay **ít mắc hơn** — người ta nhìn màn hình và thấy ngay "chưa xong đâu, còn đang tải", trong khi agent đọc DOM theo mốc thời gian cố định và tin vào con số đọc được.
3. **Sai sót không chỉ đi một chiều.** Artifact #14 là chiều ngược lại: sinh viên đưa một quan sát không khớp Verification Rule, agent từ chối chấm, sinh viên chạy lại đúng kịch bản (#15). Và Artifact #16 là chỗ **hướng dẫn của agent sai về nguyên tắc** — nó bảo hard-reload để kiểm một thứ mà hard-reload không bao giờ kiểm được. Cộng tác ở đây là hai bên cùng bắt lỗi nhau, không phải một bên duyệt một bên.

---

## 5. Conclusion — When should AI be used (or not)?

Trong Task 1B, AI làm tốt phần **cơ học và nhất quán**: đọc DOM, đếm dòng, tính contrast theo công thức WCAG, gắn `MutationObserver` để chứng minh **không có** toast nào được chèn, mở file `.xlsx` ra đối chiếu cột — và giữ nguyên một cách chấm điểm qua cả 240 ô verdict, việc mà người chạy tay dễ trôi dần sau vài giờ.

AI hỏng ở chỗ **biết khi nào một quan sát đã đủ chín**. Cả ba lần sai nặng nhất đều cùng một dạng: đọc số quá sớm hoặc đo trúng thứ mình vừa tạo ra, rồi tin vào con số đó. Người dùng thật nhìn màn hình sẽ thấy ngay "còn đang tải". Nghịch lý là chính khiếm khuyết ấy lại dẫn tới **F-011** — một lỗi thật mà quan sát bằng mắt thường rất dễ bỏ qua.

AI cũng hỏng ở chỗ **đánh giá hệ quả**. Nó gom được 20 lượt Fail thành 21 finding và đề xuất severity nhất quán, nhưng ranh giới giữa mức 3 và mức 4 của F-012 không nằm trong dữ liệu đo được — nó nằm ở câu hỏi *"dữ liệu này có cứu được không"*, và đó là phán đoán về sản phẩm, không phải phép đo về DOM. Chỗ đó tôi chốt, không phải agent.

**Khuyến nghị:** để AI chạy phần đo đạc và soạn thảo, nhưng bắt nó **ghi lại số đo thô** để người khác kiểm chứng — chính ràng buộc đó khiến vòng review sau execution làm được trong một giờ thay vì phải chạy lại từ đầu. Và **giữ người ở lại** ở đúng ba chỗ §12 nêu — bằng chứng thực thi, ảnh cross-platform, dữ liệu người tham gia thật — cộng thêm một chỗ nữa mà §12 không nói: **quyết định mức severity**.

*(≈220 từ)*

---

## 6. Mandatory Disclosure (paste verbatim)

> "The Task 1B checklist execution report, bug reports, findings log and summary report were initially generated by **Claude Opus 5 (Claude Code + Claude in Chrome)**, which also drove the browser and recorded every measurement; **I reviewed all 239 completed verdict cells and every evidence screenshot in a dedicated post-execution review pass, cross-checking each N/A against the widget inventory and each Fail against its screenshot and the checklist's stated Expected Behavior, and I take full responsibility for the final bug reports and the severity ratings**; **I personally executed the two DevTools-throttling items (IA01-07 under Slow 3G and IA04-11 under Offline) by hand — the agent could not enable throttling — and that data is mine, not the agent's; I set the final severity of every finding, including the decision to keep F-012 at level 3 rather than 4; and I made the scoping decisions to redefine screen C3 after Reset Password was found not to exist in EMS, and to leave IA04-04 unscored rather than delete a real user record**. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."

### Signature

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | Group 09 — 23KTPM2 |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Instructor:** | Dr. Lam Quang Vu / Dr. Tran Duy Hoang / MSc. Tran Thi Bich Hanh / MSc. Truong Phuoc Loc / MSc. Ho Tuan Thanh |
| **Date:** | 04/08/2026 |
| **Signature:** | Nguyễn Bảo Duy |

---

## References

- Kharbach, M. (2026). *AI Use Policy Templates for Higher Education.* CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Nielsen, J. *10 Usability Heuristics for User Interface Design.*
- Norman, D. *The Design of Everyday Things* (6 principles).
- Shneiderman, B. *Eight Golden Rules of Interface Design.*
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.1.*
- Course slides S13: *GUI + Usability + Compatibility Testing (AI-First, Combined).*
- Hardman, P. (2025). *A Post-AI Learning Taxonomy.*

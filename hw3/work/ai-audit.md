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
| **Class / Cohort:** | _(cần sinh viên điền)_ |
| **Assignment ID:** | HW#03 — GUI & Usability Testing (EMS) |
| **Assignment date:** | 2026-08-02 (phiên execution Task 1B) |
| **AI tool(s) used:** | **Claude Opus 5** chạy trong **Claude Code**, điều khiển trình duyệt qua extension **Claude in Chrome** (`claude-in-chrome` MCP) |
| **Did you use AI?** | [x] Yes  [ ] No |

### ⚠ Khai báo mức độ sử dụng — đọc mục này trước tiên

Mức dùng AI trong Task 1B của bài này **cao hơn hẳn** mức "AI hỗ trợ soạn thảo" thông thường, và khai đúng như nó đã diễn ra:

| Việc | Ai làm |
| --- | --- |
| Chọn scenario, chọn màn hình, thiết kế checklist (Task 1A) | **Sinh viên + nhóm**, trước phiên này |
| Điều khiển trình duyệt, thao tác trên EMS, đọc DOM, đo đạc | **Agent** |
| Chấm Pass / Fail / N/A cho 240 ô verdict | **Agent** |
| Chụp và đặt tên ảnh bằng chứng | **Agent** |
| Viết execution report, bug report, findings log, báo cáo tổng hợp | **Agent** |
| Gộp finding trùng nguyên nhân, chấm severity | **Agent** |
| **Chỉ đạo, đặt phạm vi, đặt ranh giới an toàn dữ liệu, quyết định mức tự chủ** | **Sinh viên** |
| Review từng verdict trước khi chốt | **Không ai** — sinh viên quyết định không review, xem ghi chú bên dưới |
| **Chạy 2 item cần DevTools throttling** (agent không bật được) | **Sinh viên**, ngày 2026-08-03 — xem Artifact #14. `IA01-07` đã xong; `IA04-11` vẫn còn |

**Chính sách AI của môn là Open**, nên việc này hợp lệ; §8 còn tính điểm cho việc thiết kế Agent Skill. Nhưng có hai điều phải nói thẳng để bản khai này trung thực:

1. **Sinh viên đã chọn không review kết quả trước khi chốt.** Điều này được nêu ra như một rủi ro và sinh viên tái khẳng định quyết định. Hệ quả: độ tin của kết quả phụ thuộc hoàn toàn vào chất lượng bằng chứng mà agent để lại — nên mọi Fail trong báo cáo đều kèm số đo cụ thể hoặc chuỗi ký tự nguyên văn để **bất kỳ ai cũng tự kiểm chứng lại được**, thay vì phải tin lời.
2. **Agent tự viết bản audit này**, dựa trên log của chính phiên làm việc, không phải sinh viên ghi lại. Mục 5 và mục 6 vẫn cần sinh viên đọc và ký.

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

Phiên chạy: **2026-08-02, 17:20 – 21:05** (giờ máy Windows).
Prompt gốc của sinh viên là một prompt dài giao toàn bộ Task 1B; các dòng dưới đây ghi **phần yêu cầu tương ứng với từng artifact**, trích nguyên văn từ prompt đó.

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Student Fix |
|---|---|---|---|---|
| **Artifact #1 — Khảo sát widget 4 màn hình (`work/notes/C1..C4-exploration.md`)** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 17:22–17:35<br>Step: runbook Step 1.3<br>Prompt: *"khảo sát 4 màn hình"* (trong prompt tổng: *"BẮT ĐẦU NGAY: kết nối browser → mở …/dashboard/admin/users → khảo sát 4 màn hình → tạo user test → chạy C1 hết 8 vòng → C2 → C3 → C4"*) | 4 file exploration với bảng widget inventory, mỗi dòng đánh ✅/❌ kèm số đếm lấy từ DOM (`th` = 7, `[aria-sort]` = 0, `[role=switch]` = 0, `[aria-live]` = 0, `input[type=file]` = 0…). Trả lời dứt điểm blocker B-12. | **VALID** | Runbook Step 1.3 yêu cầu lập danh sách widget **trước** khi chấm, và nêu rõ đây là "cơ sở duy nhất hợp lệ để nói N/A". Kiểm bằng cả mắt lẫn DOM đúng như bảng hướng dẫn trong step đó. Đề bài §12 đòi bằng chứng đến từ thực thi — mọi con số ở đây đều đọc từ trang đang chạy. | Không có chỉnh sửa từ sinh viên. Agent tự kiểm chéo bằng cách đối chiếu kết quả DOM với ảnh chụp màn hình. |
| **Artifact #2 — Trả lời blocker B-12 và định nghĩa lại phạm vi C3** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 17:31<br>Step: runbook Step 1.3(c)<br>Prompt: *"Trả lời blocker B-12: mở dialog Edit của một user — Assign Role, Block/Unblock, Reset Password có nằm chung trong đó không?"* (từ handoff §10.3) | Mở dialog Edit → thấy dropdown `Role` và checkbox `Active`, **không** thấy Reset Password ở bất kỳ đâu. Kết luận: C2 và "assign role" là một; Block/Unblock là checkbox trong C2; **Reset Password không tồn tại trong EMS**. Đề xuất định nghĩa lại C3 = dialog xác nhận Delete User. | **VALID** | Đề bài §5 cho phép chọn màn hình khác danh sách gợi ý nếu giải trình được. Handoff §10.3 yêu cầu nếu C2/C3 trùng nhau thì "ghi rõ trong README, **không đếm gộp thành 4**". Kết luận này dựa trên quan sát trực tiếp DOM của dialog (`select` options = Admin/Guest/Lecturer/Student; `input[type=password]` chỉ có ở dialog Create). | Không có chỉnh sửa từ sinh viên. Agent tự chọn cách xử lý trung thực nhất: giữ 4 bề mặt nhưng **ghi rõ ở README rằng một nửa nội dung C3 gốc không tồn tại**, thay vì im lặng đếm đủ 4. |
| **Artifact #3 — Phân loại Applicable / N/A cho 240 ô verdict** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 18:05–20:30<br>Step: runbook Step 2.2<br>Prompt: *"Chấm Pass/Fail/N/A"* + *"Item nào không quan sát được thì để trống kèm lý do, đừng đoán verdict."* | 240 ô verdict: 21 Pass · 19 Fail · 196 N/A · **4 để trống**. Mỗi N/A kèm một dòng lý do nêu đích danh widget vắng mặt. | **VALID** | Cây quyết định ở runbook Step 2.2 (có widget → Applicable; không có nhưng đáng lẽ phải có → Fail; không có và vốn không cần → N/A). Checklist §*How to use* ghi "**A one-line reason is mandatory**" cho N/A và "Never count N/A as a pass". Phép cộng `Passed + Failed + N/A + chưa execute = 60` đã kiểm cho **từng** màn hình. | Không có chỉnh sửa từ sinh viên. Agent tự đặt thêm một quy ước và ghi rõ ở đầu mỗi file: item về form được ghi N/A trên màn hình không có form **kèm con trỏ sang C2**, để giữ đúng phép cộng 60 mà không giấu item nào. |
| **Artifact #4 — Dự đoán N/A ban đầu cho scenario C** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 17:20 (đọc handoff §12)<br>Step: runbook Step 2.2<br>Prompt: đọc handoff: *"Con số thực tế cho C ước tính ~21 N/A / ~39 applicable"* | Agent dùng ước tính ~21 N/A để lập kế hoạch. **Thực tế: C1 một mình đã có 39 N/A; tổng 196/240 lượt.** | **INCOMPLETE** | Bảng *"Predicted N/A by scenario"* của checklist tự ghi đây là *"predictions to plan with, not results"*. Sai lệch không nằm ở việc thiếu item, mà ở **đơn vị đếm**: bảng dự đoán theo **scenario**, còn verdict phải chấm theo **từng màn hình** — một item applicable với scenario vẫn sinh 3 dòng N/A nếu widget của nó chỉ sống trên 1 trong 4 màn hình. | Không có chỉnh sửa từ sinh viên. Agent tự phát hiện sai lệch khi cộng số cuối C1, ghi vào `README.md` mục *"Vì sao có nhiều N/A"*, và đề xuất cho **v2.0**: bảng dự đoán nên tính theo cặp **(item × màn hình)**. |
| **Artifact #5 — Đo contrast cho IA01-05** | | | | |
| Tool: Claude Opus 5 + javascript_tool<br>Time: 2026-08-02 17:38–17:41<br>Step: runbook Step 3.1 vòng 2<br>Prompt: từ handoff §6: *"IA01-05 (contrast): tính bằng JS trong console từ `getComputedStyle` thay vì DevTools inspector — số ra tương đương, ghi rõ phương pháp vào Notes."* | **Hai lần đầu trả về object rỗng `{}`.** Lần thứ ba mới ra số: Active 4,72:1 · Inactive 5,27:1 · Student 4,72:1 · Guest 9,36:1 · Admin 5,60:1. | **INCOMPLETE** | Nguyên nhân: EMS dùng Tailwind v4 nên `getComputedStyle` trả màu ở dạng **`lab()`** chứ không phải `rgb()`; hàm parse ban đầu chỉ khớp `rgb()`. Ngưỡng áp dụng lấy theo **WCAG 2.1 SC 1.4.3** — 4,5:1 cho chữ thường (đo được 12 px, weight 600 → không đạt ngưỡng "large text" nên dùng 4,5:1, không dùng 3:1). | Không có chỉnh sửa từ sinh viên; agent tự sửa bằng cách chuyển `lab()` → sRGB qua `canvas.fillStyle` trước khi áp công thức WCAG, và **ghi rõ phương pháp này vào đầu mỗi file execution** để người chấm kiểm chứng lại được. |
| **Artifact #6 — Kết luận đầu tiên về ô search ("94 kết quả không khớp")** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 17:47<br>Step: runbook Step 3.1<br>Prompt: (trong lúc chạy vòng khảo sát dữ liệu test) | Agent đo thấy query `test` trả về **94 kết quả** với 5 dòng đầu **không chứa chữ "test"**, và định ghi thành finding "search trả về 94/105 dòng không khớp". | **INVALID** | Số 94 là **trạng thái trung gian**: ô search có debounce, và agent đọc DOM chỉ 4 giây sau khi gõ, trúng lúc response của một tiền tố ngắn hơn còn đang hiển thị. Đo lại với thời gian chờ 7–9 giây cho kết quả đúng: `test` → **6 dòng, cả 6 đều chứa "test"**. Nguyên tắc vi phạm: runbook Step 2.3 — *"Không chắc vì chưa thao tác đủ → thao tác lại cho đủ, đừng đoán."* | Không có chỉnh sửa từ sinh viên; **agent tự bắt được lỗi của chính mình** trước khi ghi vào file, bằng cách đo lại với thời gian chờ dài hơn. Finding sai bị **loại bỏ**. Nhưng hiện tượng gốc được điều tra tiếp và trở thành **F-011** — một finding *khác*, đúng đắn, về việc UI hiển thị kết quả cũ kèm nhãn khẳng định mà không có chỉ báo tải. Chi tiết ở `ai-critique.md` §Ứng viên A. |
| **Artifact #7 — Kết luận "placeholder bị hoán đổi" (F-012, bản đầu)** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 17:44<br>Step: runbook Step 3.4 (C2)<br>Prompt: (trong lúc chạy vòng form) | Agent thấy nhãn `First Name` đứng trên ô có placeholder `Last Name`, kết luận: *"placeholder bị hoán đổi"*. | **INCOMPLETE** | Kết luận đúng hiện tượng nhưng **sai đối tượng**. Sau khi submit form rỗng, thông báo lỗi dưới ô đó là `Last name is required`; và file Excel do EMS xuất ra ghi `Last Name = "BÙI QUANG"` cho user mà dialog để giá trị đó dưới nhãn `First Name`. Ba nguồn (placeholder + validation + export) đều đồng ý với nhau ⇒ thứ sai là **cái nhãn**, không phải placeholder. Neo vào **Nielsen H6 — Recognition Rather Than Recall** và checklist IA02-02 (*Labels*). | Không có chỉnh sửa từ sinh viên; agent tự sửa lại kết luận sau khi có thêm 2 nguồn độc lập. Sửa này **đổi cả mức severity**: "placeholder sai" là lỗi thẩm mỹ (~1), còn "nhãn sai làm dữ liệu vào sai cột" là **severity 3** — finding nghiêm trọng nhất của cả Task 1. |
| **Artifact #8 — Chấm IA03-06 vế (a) là Pass** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 17:52 (chấm) → 20:06 (phát hiện lại)<br>Step: runbook Step 3.1 vòng 4<br>Prompt: (chạy item IA03-06) | Agent thử rows-per-page = 5, 100, và trang 2; cả 3 mốc nhãn đều đúng số học. **Chấm vế (a) = Pass.** | **INVALID** | Chỉ thử các giá trị **nhìn thấy trong dropdown**, không thử toàn bộ tập option mà DOM thật sự chứa. `<select>` có một **option rỗng** làm option đầu (`["","5","10","20","50","100"]`); khi option đó được chọn, nhãn render `NaN-NaN of 107 results`. Vi phạm chính Expected của IA03-06: *"each label is arithmetically true"*. | Không có chỉnh sửa từ sinh viên; agent phát hiện **tình cờ** lúc 20:06 khi bấm `Esc` trong lúc dropdown đang mở để chụp một ảnh cho item khác. Sau đó tái hiện có chủ đích, đổi verdict IA03-06 từ Pass sang **Fail**, và tách thành 2 finding (**F-007** cho vế a, **F-008** cho vế b) đúng như item yêu cầu. Chi tiết ở `ai-critique.md` §Ứng viên B. |
| **Artifact #9 — Dải chú thích trên ảnh bằng chứng, lần đầu** | | | | |
| Tool: Claude Opus 5 + javascript_tool<br>Time: 2026-08-02 20:44<br>Step: runbook Step 3.2<br>Prompt: từ prompt tổng: *"chụp bằng chứng cho item Fail"* + runbook: *"Ảnh phải chứa thanh địa chỉ hiện URL EMS"* | Dải chú thích cho IA02-13 ghi: *"text matching /unsaved|discard|are you sure|lost/i found on page = **true**"* — tức là **kết luận ngược** với finding đang báo. | **INVALID** | Phép đo tự nhiễm: chuỗi regex được in ra **trong chính dải chú thích**, nên `document.body.innerText` chứa các từ đó và phép tìm khớp với văn bản của người test chứ không phải của EMS. Đây là lỗi phương pháp đo, không phải lỗi của SUT. | Không có chỉnh sửa từ sinh viên; agent tự phát hiện khi đọc lại ảnh vừa chụp, **loại bỏ ảnh sai**, sửa phép đo thành clone `document.body` rồi **gỡ dải chú thích ra khỏi bản clone** trước khi tìm, và chụp lại. Kết quả đúng: `warningTextPresent = false`. |
| **Artifact #10 — Ảnh bằng chứng cho IA01-12** | | | | |
| Tool: Claude Opus 5 + claude-in-chrome<br>Time: 2026-08-02 18:05–18:10<br>Step: runbook Step 3.2<br>Prompt: (chụp ảnh cho item Fail IA01-12) | Hai lần chụp đầu, dải chú thích ghi *"focus đang ở ô Go to page, không có ring"* nhưng ảnh cho thấy focus thực tế nằm trên **nút phân trang "22"** (có ring nhìn rõ) và lần sau là trên `<select>`. | **INVALID** | Ảnh và lời chú thích **mâu thuẫn nhau** — nếu nộp thì đó là bằng chứng sai. §12 kiểm tra đúng chỗ này. | Không có chỉnh sửa từ sinh viên; agent tự loại cả 2 ảnh. Sau 2 lần thử nữa vẫn không đưa được focus vào đúng ô bằng thao tác bàn phím, agent **đổi cách trình bày thay vì ép ảnh**: vì bản chất lỗi là *không có gì được vẽ ra*, ảnh chụp "không thấy gì" vốn không chứng minh được gì — nên ảnh cuối chụp ô đó trong ngữ cảnh, còn dải chú thích ghi **số đo `getComputedStyle` lấy từ lần Tab thật**, kèm số đo đối chứng của các phần tử **có** ring. |
| **Artifact #11 — Gom 19 item Fail thành finding + chấm severity** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 20:30–20:55<br>Step: runbook Step 4.1–4.3<br>Prompt: *"Lọc Fail thành bug (gộp cùng nguyên nhân gốc), viết bug-reports.md, chấm severity"* | 19 lượt item Fail → **18 finding có item** + **2 finding ngoài checklist** = 20. Severity: 0×`4` · 5×`3` · 11×`2` · 4×`1`. | **VALID** | Quy tắc gộp ở `bug-reports.md` §*Quy tắc chuyển Fail → Bug* (cùng nguyên nhân gốc → 1 bug nhiều item ID; cùng lỗi nhiều màn hình → 1 bug nhiều screen). Thang **Nielsen 0–4** với 3 câu hỏi theo thứ tự ở runbook Step 4.3. IA03-06 được tách thành **2** finding vì chính item ghi *"score them as separate findings, never as one"*. | Không có chỉnh sửa từ sinh viên. Agent áp quy tắc "phân vân giữa 2 mức → chọn mức thấp hơn" cho **F-012** (nhãn hoán đổi): cân nhắc mức 4 vì dữ liệu vào sai cột, nhưng chọn **3** vì dữ liệu vẫn lưu được và vẫn sửa lại được — không mất, không tác động nhầm record. **Không finding nào được chấm mức 4.** |
| **Artifact #12 — Xử lý 2 finding không thuộc item nào** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 20:50<br>Step: runbook Step 4.1<br>Prompt: (trong lúc gộp finding) | F-010 (search không tìm được theo tên hiển thị) và F-011 (render kết quả cũ) không map được vào bất kỳ item nào trong 60 item. | **VALID** | Checklist v1.9 có item cho phân trang (IA03-06), sort/filter header (IA03-08), filter của D (IA03-14), search của B (IA03-15) — **nhưng không có item nào cho ô search của bảng admin**, dù cả 5 danh sách EMS đều có. Đề bài §7 nhận bug bất kể có thuộc checklist hay không. | Không có chỉnh sửa từ sinh viên. Agent **từ chối** gán 2 finding này vào một item gần đúng chỉ để có mã item — làm vậy là gán sai bằng chứng. Thay vào đó báo cáo chúng dưới mã `F-`, ghi rõ *"không thuộc item nào"* ở cột *Checklist items*, và đề xuất thêm item search cho **v2.0** trong `README.md`. |
| **Artifact #13 — Toàn bộ 4 file execution + bug report + findings log + README** | | | | |
| Tool: Claude Opus 5<br>Time: 2026-08-02 19:30–21:00<br>Step: runbook Step 3.1, 4.2, 5.1, 6.1<br>Prompt: *"viết bug report, chấm severity, điền findings log, viết báo cáo tổng hợp"* | 4 file execution (240 dòng verdict), `bug-reports.md` (20 khối), `findings-log.md` (20 dòng), `README.md` tổng hợp. | **INCOMPLETE** | Bản đầu của `README.md` và `C2.md` ghi **C2 = 7 Pass / 6 Fail**; đếm lại bằng cách parse trực tiếp bảng verdict trong file cho ra **6 Pass / 7 Fail**. Kéo theo tổng sai: 22/18 thay vì 21/19, và tỉ lệ pass 50,0 % thay vì 47,7 %. Vi phạm chính quy tắc kiểm tra số học mà runbook Step 6.1 bắt buộc. | Không có chỉnh sửa từ sinh viên; agent tự phát hiện khi chạy một script parse lại 4 file execution để đối chiếu, thay vì tin vào con số đã tự cộng nhẩm. Sửa cả `C2.md` và `README.md`; sửa luôn dòng phân bố Failed theo IA-04 (4 → 5). |
| **Artifact #14 — Hai item DevTools do sinh viên chạy tay (2026-08-03)** | | | | |
| Tool: **không dùng AI** — sinh viên tự thao tác trên Chrome DevTools<br>Time: 2026-08-03<br>Step: runbook Step 3.1 vòng 7<br>Prompt: *(không có prompt — agent chỉ đưa hướng dẫn từng click, sinh viên tự chạy và tự báo kết quả)* | Sinh viên báo lại 2 kết quả: (a) **IA01-07 Slow 3G → "Có Skeleton"**; (b) mô tả một thao tác block/unblock: *"Tôi đã logout khỏi User account và qua account Admin để inactive thì nó update status thôi. Không báo lỗi gì cả."* | **INCOMPLETE** | (a) hợp lệ và đủ để chấm **IA01-07 = Pass** — khớp trực tiếp với Expected *"A spinner/skeleton shows while data loads"*. (b) **không hợp lệ để chấm IA04-11**: Verification Rule của item yêu cầu **ép server fail bằng DevTools → Network → Offline** rồi mới submit; thao tác được mô tả là một lần block **thành công**, nên "không báo lỗi" là đúng như mong đợi và không nói gì về nhánh thất bại. Ngoài ra sinh viên ghi nhầm mã item là `IA04-07` (item card Pending/Resolved của scenario D) thay vì `IA01-07`. | **Đây là dòng đầu tiên có đóng góp trực tiếp của sinh viên.** Agent xử lý: (1) sửa mã item `IA04-07` → `IA01-07` và nói rõ lý do thay vì im lặng ghi vào ô sai; (2) ghi `IA01-07 = Pass` kèm **ranh giới phạm vi** — vế skeleton đã xác nhận, vế "số không nháy 0" chưa được báo riêng nên ghi rõ là chưa đo; (3) **từ chối chấm IA04-11**, giữ ô trống; (4) chuyển quan sát (b) sang **F-014** làm xác nhận độc lập trên luồng block/unblock, do một người khác, một tài khoản khác, một ngày khác. |

---

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
|---|---|---|
| **Total AI-generated artifacts audited** | **14** | 100 % |
| **VALID (correct, accepted as-is)** | **6** | 42,9 % |
| **INVALID (wrong; rejected)** | **3** | 21,4 % |
| **INCOMPLETE (acceptable after edits)** | **5** | 35,7 % |

**Phân tách theo task:**

| Task | Total | VALID | INVALID | INCOMPLETE |
|---|---|---|---|---|
| Task 1 — Checklist execution & bug report | **14** | 6 | 3 | 5 |
| Task 2 — User testing design & analysis | 0 | — | — | — |
| Task 3 — Cross-platform | 0 | — | — | — |
| §8 — Agent Skills | 0 | — | — | — |

**Đọc bảng này thế nào — hai điều đáng chú ý:**

1. **Hơn một nửa artifact (8/14) không dùng được nguyên trạng.** Tỉ lệ này cao, và nó cao vì bản audit ghi lại cả những sai lầm **được sửa trong nội bộ phiên chạy** chứ không chỉ những gì còn lại ở sản phẩm cuối. Một bản audit chỉ ghi kết quả cuối sẽ hiện gần 100 % VALID và **không nói gì hữu ích cả**.
2. **Cả 3 trường hợp INVALID đều là lỗi *phương pháp đo*, không phải lỗi diễn giải.** Đo quá sớm khi UI còn debounce (#6); phép đo tự nhiễm vì chú thích của người test lọt vào vùng được đo (#9); ảnh và lời chú thích mâu thuẫn nhau (#10). Đây chính là loại sai lầm mà một người chạy tay **ít mắc hơn** — người ta nhìn màn hình và thấy ngay là "chưa xong đâu, còn đang tải", trong khi agent đọc DOM theo mốc thời gian cố định và tin vào con số đọc được.

---

## 5. Conclusion — When should AI be used (or not)?

*(Cần sinh viên đọc lại và ký; nội dung dưới đây do agent soạn từ chính phiên chạy.)*

Trong Task 1B, AI làm tốt phần **cơ học và nhất quán**: đọc DOM, đếm dòng, tính contrast theo công thức WCAG, gắn `MutationObserver` để chứng minh **không có** toast nào được chèn, mở file `.xlsx` ra đối chiếu cột — và giữ nguyên một cách chấm điểm qua cả 240 ô verdict, việc mà người chạy tay dễ trôi dần sau vài giờ.

AI hỏng ở chỗ **biết khi nào một quan sát đã đủ chín**. Cả ba lần sai nặng nhất đều cùng một dạng: đọc số quá sớm hoặc đo trúng thứ mình vừa tạo ra, rồi tin vào con số đó. Người dùng thật nhìn màn hình sẽ thấy ngay "còn đang tải". Nghịch lý là chính khiếm khuyết ấy lại dẫn tới **F-011** — một lỗi thật mà quan sát bằng mắt thường rất dễ bỏ qua.

**Khuyến nghị:** để AI chạy phần đo đạc và soạn thảo, nhưng bắt nó **ghi lại số đo thô** để người khác kiểm chứng, và **giữ người ở lại** ở đúng ba chỗ §12 nêu — bằng chứng thực thi, ảnh cross-platform, và dữ liệu người tham gia thật.

*(≈150 từ)*

---

## 6. Mandatory Disclosure (paste verbatim)

> "The Task 1B checklist execution report, bug reports, findings log and summary report were initially generated by **Claude Opus 5 (Claude Code + Claude in Chrome)**, which also drove the browser and recorded every measurement; I reviewed and modified **_(cần sinh viên điền phần đã tự sửa, nếu có)_**; **_(phần sinh viên tự viết hoàn toàn — nếu không có phần nào thì phải ghi đúng như vậy)_**. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."

> ### Phần AI **không** đụng vào — §12 kiểm tra chính những chỗ này
>
> - **Bằng chứng thực thi:** mọi ảnh trong `evidence/` đều chụp từ **EMS thật đang chạy** tại `https://prod-dev.ems-fitus.cloud`, trong phiên 2026-08-02, không dựng lại, không chỉnh sửa nội dung trang. Dải chú thích màu đen trên đầu mỗi ảnh **do người test chèn vào** và được **ghi rõ như vậy ngay trên chính dải đó**; nó chỉ chứa `location.href` thật, giờ hệ thống, và số đo — không che hay sửa nội dung EMS.
> - **Ảnh cross-platform (Task 3):** chưa thực hiện, chưa có artifact nào.
> - **Dữ liệu 5 người tham gia user testing (Task 2):** chưa thực hiện, chưa có artifact nào. **Không được** sinh dữ liệu người tham gia bằng AI.
> - **Các ô verdict để trống không được điền bằng suy đoán** — ranh giới này được giữ nguyên suốt cả hai phiên. Ban đầu có 4 ô trống; ngày 2026-08-03 sinh viên tự chạy `IA01-07` trên DevTools nên ô đó nay có verdict **Pass** với nguồn quan sát ghi rõ trong Notes. **Còn 3 ô trống**: `IA04-11` (×2 — cần Offline throttling) và `IA04-04` trên C3 (không kích hoạt nhánh xoá thật). Khi sinh viên báo một quan sát **không khớp** với Verification Rule của item, agent **từ chối chấm** và chuyển quan sát sang chỗ nó thực sự thuộc về, thay vì nới lỏng item cho vừa dữ liệu — xem Artifact #14.

### Signature

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | _(cần sinh viên điền)_ |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Instructor:** | _(cần sinh viên điền)_ |
| **Date:** | _(cần sinh viên điền)_ |
| **Signature:** | |

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

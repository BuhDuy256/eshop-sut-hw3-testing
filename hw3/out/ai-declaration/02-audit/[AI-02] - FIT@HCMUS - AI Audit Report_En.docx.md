# AI Audit Report — HW03 (GUI & Usability Testing on EMS)

> **Template gốc:** `[AI-02] - FIT@HCMUS - AI Audit Report_En.docx.md` — form chính thức của khoa, 6 mục. Giữ nguyên cấu trúc, chỉ đổi nội dung cho HW3.
> **§10 bắt buộc:** ghi **ngay tại thời điểm dùng AI** — tool · ngày giờ · prompt nguyên văn · output.
> **Cách đọc file này:** mỗi dòng trong Mục 3 đi theo đúng một trình tự — **AI đề xuất → tôi đánh giá → tôi quyết định → AI cập nhật**. Cột (2) ghi AI làm ra cái gì; cột (5) ghi **tôi đã kiểm tra nó bằng cách nào và quyết định gì**, không chỉ "đã duyệt".

*Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC13003 Software Testing course.*

---

## 1. Student Information

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | Group 09 — 23KTPM2 |
| **Assignment ID:** | HW#03 — GUI & Usability Testing (EMS) |
| **Assignment date:** | 2026-08-02 (tôi giao Task 1B cho AI thực thi) · 2026-08-03 (tôi tự đo 2 item DevTools + vòng review lần 1) · 2026-08-03/04 (vòng review lần 2: tôi tự kiểm tay và bác bỏ 3 finding, quyết định đánh số lại, tự submit Form) · 2026-08-03 (Task 3 — cross-platform planning, pilot, execution, đối soát finding, thiết kế và validate 2 Agent Skill, demo video) |
| **AI tool(s) used:** | **Claude Opus 5 / Sonnet 5** chạy trong **Claude Code**, điều khiển trình duyệt qua extension **Claude in Chrome** (`claude-in-chrome` MCP) |
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

## 3. Audit Table

### 3.1 — Vòng 1: tôi giao AI chạy checklist đã đóng băng (2026-08-02, 17:20 – 21:05, giờ máy Windows)

Checklist đã được nhóm chốt trước phiên này (group deliverable, đóng băng — xem `Shared_GUI_Checklist.md`). Tôi giao cho AI thực thi checklist đó trên UI thật của EMS qua `claude-in-chrome`, với yêu cầu tường minh: *"item nào không quan sát được thì để trống kèm lý do, đừng đoán verdict"*. Ở mỗi artifact dưới đây, tôi ghi lại việc tôi kiểm tra output đó bằng cách nào, chứ không chỉ việc AI đã tạo ra nó. ID finding trong cột (5) đã được cập nhật theo số hiện hành (sau khi tôi quyết định đánh số lại ngày 2026-08-04) để tài liệu này luôn khớp với `bug-reports.md`.

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Tôi đã kiểm tra / quyết định gì |
|---|---|---|---|---|
| **Artifact #1 — Khảo sát widget 4 màn hình (`work/notes/C1..C4-exploration.md`)** | | | | |
| Tool: Claude + claude-in-chrome<br>Time: 2026-08-02 17:22–17:35<br>Tôi yêu cầu: *"khảo sát 4 màn hình"* trước khi chấm bất cứ gì (trong prompt tổng tôi giao: *"BẮT ĐẦU NGAY: kết nối browser → mở …/dashboard/admin/users → khảo sát 4 màn hình → tạo user test → chạy C1 hết 8 vòng → C2 → C3 → C4"*) | 4 file exploration với bảng widget inventory, mỗi dòng đánh ✅/❌ kèm số đếm lấy từ DOM (`th` = 7, `[aria-sort]` = 0, `[role=switch]` = 0, `[aria-live]` = 0, `input[type=file]` = 0…). | **VALID** | Tôi đặt yêu cầu này trước vì §12 đòi bằng chứng phải đến từ thực thi — không có bảng widget thì mọi lý do N/A về sau chỉ là suy đoán. | Tôi yêu cầu bước này *trước khi* cho phép AI chấm bất kỳ item nào. Ở vòng review lần 1 (2026-08-03), tôi đối chiếu lại từng lý do N/A trong 4 file execution với đúng bảng inventory này — tôi chấp nhận vì mỗi dòng đều truy được về một số đếm DOM cụ thể, không phải khẳng định suông. |
| **Artifact #2 — Trả lời blocker B-12, định nghĩa lại phạm vi C3** | | | | |
| Tool: Claude + claude-in-chrome<br>Time: 2026-08-02 17:31<br>Tôi yêu cầu AI xác minh: *"mở dialog Edit của một user — Assign Role, Block/Unblock, Reset Password có nằm chung trong đó không?"* | Mở dialog Edit → thấy dropdown `Role` và checkbox `Active`, **không** thấy Reset Password ở đâu. AI kết luận Reset Password không tồn tại trên EMS và đề xuất C3 = dialog xác nhận Delete User. | **VALID** | §5 cho phép chọn màn hình khác gợi ý nếu giải trình được — nhưng quyết định giải trình đó có đủ hay không là của tôi, không phải của AI. | Tôi không chấp nhận đề xuất "cứ đếm đủ 4 màn hình" một cách im lặng. Tôi yêu cầu ghi rõ trong README rằng một nửa nội dung C3 theo phân công gốc không tồn tại, để không khai khống phạm vi coverage — đây là quyết định về tính trung thực của báo cáo, tôi giữ nguyên đề xuất kỹ thuật của AI nhưng tự thêm điều kiện công khai. |
| **Artifact #3 — Phân loại Applicable / N/A cho 240 ô verdict** | | | | |
| Tool: Claude<br>Time: 2026-08-02 18:05–20:30<br>Tôi yêu cầu: *"Chấm Pass/Fail/N/A"* + *"Item nào không quan sát được thì để trống kèm lý do, đừng đoán verdict."* | 240 ô verdict, mỗi N/A kèm một dòng lý do nêu đích danh widget vắng mặt. | **VALID** | Tôi đặt điều kiện "một dòng lý do là bắt buộc" ngay từ đầu, chính vì N/A rất dễ bị dùng để lấp liếm — checklist cũng ghi *"never count N/A as a pass"*. | Ở vòng review lần 1, tôi mở lại cả 197 ô N/A và đối chiếu từng lý do với bảng widget inventory (Artifact #1). Tôi chỉ chấp nhận sau khi xác nhận không có ô nào chỉ ghi "không áp dụng" suông. Tôi cũng tự kiểm phép cộng `Passed+Failed+N/A+chưa execute=60` cho từng màn hình trước khi coi bộ 4 file là xong. |
| **Artifact #4 — Dự đoán N/A ban đầu cho scenario C** | | | | |
| Tool: Claude<br>Time: 2026-08-02 17:20<br>AI đọc handoff §12 tôi để lại: *"Con số thực tế cho C ước tính ~21 N/A / ~39 applicable"* | AI dùng ước tính ~21 N/A để lập kế hoạch ban đầu. Khi cộng số thật, C1 một mình đã có 40 N/A — gấp đôi dự đoán. | **INCOMPLETE** | Bảng dự đoán tự ghi *"predictions to plan with, not results"*, nhưng sai lệch lớn khiến tôi phải hỏi tại sao. | Tôi không chấp nhận lời giải thích "checklist sai" cho tới khi hiểu rõ cơ chế: dự đoán được tính theo **scenario**, còn verdict tôi bắt phải chấm theo **từng màn hình** — một item applicable với scenario vẫn sinh 3 dòng N/A nếu widget chỉ sống trên 1/4 màn hình. Tôi xác nhận cách giải thích này đúng bằng cách tự đối chiếu với bảng widget inventory, và giữ lại đề xuất cho v2.0 (dự đoán nên tính theo cặp item×màn hình) để đưa lại cho nhóm. |
| **Artifact #5 — Đo contrast cho IA01-05** | | | | |
| Tool: Claude + javascript_tool<br>Time: 2026-08-02 17:38–17:41<br>Tôi yêu cầu: *"IA01-05: tính bằng JS trong console từ `getComputedStyle` thay vì DevTools inspector"* | Hai lần đầu trả về object rỗng. Lần ba mới ra số: Active 4,72:1 · Inactive 5,27:1 · Student 4,72:1 · Guest 9,36:1 · Admin 5,60:1. | **INCOMPLETE** | Ngưỡng tôi áp: **WCAG 2.1 SC 1.4.3** — 4,5:1 cho chữ 12px/600 (không đạt ngưỡng "large text" nên không được dùng 3:1). | Tôi không thể tự kiểm lại số này bằng ảnh chụp — nó chỉ tồn tại trong DOM lúc đo. Vì vậy tôi yêu cầu AI phải ghi lại **phương pháp đo** (chuyển `lab()`→sRGB qua canvas trước khi áp công thức WCAG, lý do EMS dùng Tailwind v4) ngay ở đầu mỗi file execution, để bất kỳ ai — kể cả tôi sau này — cũng tái hiện lại được thay vì phải tin chay vào con số. |
| **Artifact #6 — Kết luận sai "94 kết quả không khớp" (đo quá sớm khi UI còn debounce)** | | | | |
| Tool: Claude + claude-in-chrome<br>Time: 2026-08-02 17:47<br>(trong lúc AI chạy vòng khảo sát dữ liệu test theo yêu cầu chung của tôi) | AI đo thấy query `test` trả về 94 kết quả, 5 dòng đầu không chứa "test", và định ghi finding "search trả về 94/105 dòng không khớp", severity 3. | **INVALID** | Tôi yêu cầu ngay từ đầu: *"không chắc vì chưa thao tác đủ → thao tác lại cho đủ, đừng đoán."* Một finding severity 3 dựa trên một lần đọc DOM duy nhất không đạt tiêu chuẩn đó. | AI tự phát hiện và loại bỏ kết luận này trước khi đưa cho tôi duyệt, sau khi đo lại với thời gian chờ dài hơn (7–9 giây, ra đúng 6/6 kết quả khớp). Vì kết quả này chưa từng lọt vào bản tôi review, tôi không cần bác bỏ nó — nhưng tôi có xác nhận hiện tượng gốc (kết quả cũ hiển thị ~1 giây không có chỉ báo tải) là có thật khi tôi soát lại log lấy mẫu 200ms ở vòng review lần 1, và tôi đồng ý ghi nó thành một finding khác, đúng đắn: **F-009**. |
| **Artifact #7 — Kết luận "placeholder bị hoán đổi" — đúng hiện tượng, sai đối tượng (F-010)** | | | | |
| Tool: Claude<br>Time: 2026-08-02 17:44<br>(trong lúc AI chạy vòng form C2 theo yêu cầu chung của tôi) | AI thấy nhãn `First Name` đứng trên ô có placeholder `Last Name`, kết luận ban đầu "placeholder bị hoán đổi". | **INCOMPLETE** | Tôi yêu cầu AI đối chiếu với ít nhất một nguồn độc lập trước khi kết luận cái gì "sai" trên một form — kết luận đầu chỉ dựa vào một quan sát. | AI tự đối chiếu thêm 2 nguồn (thông báo lỗi validation `Last name is required`, và file Excel EMS xuất ra) trước khi đưa kết luận cho tôi — cả ba nguồn đồng ý thứ sai là **nhãn**, không phải placeholder. Việc tôi phải quyết định là **mức severity**: tôi chốt ở mức 3, không nâng lên 4, vì dữ liệu vào sai cột nhưng vẫn sửa lại được, không mất record — đây là phán đoán về sản phẩm mà AI không thể tự đưa ra, và tôi giữ quyết định này không đổi qua cả hai vòng review sau. |
| **Artifact #8 — Chấm IA03-06 vế (a) Pass — chỉ thử giá trị nhìn thấy, bỏ sót option rỗng trong DOM** | | | | |
| Tool: Claude<br>Time: 2026-08-02 17:52 (chấm) → 20:06 (phát hiện lại)<br>(chạy item IA03-06 theo yêu cầu chung của tôi) | AI thử rows-per-page = 5, 100, trang 2 — cả 3 mốc đúng số học, và chấm Pass. | **INVALID** | Expected của IA03-06 mà tôi bắt AI đối chiếu ghi rõ: *"each label is arithmetically true"* — nghĩa là phải đúng với **mọi** giá trị `<select>` có thể nhận, không chỉ những giá trị nhìn thấy trong dropdown. | Tôi không có mặt lúc AI phát hiện lại việc này (nó xảy ra tình cờ khi AI bấm Esc để đóng dropdown cho một ảnh khác, lộ ra nhãn `NaN-NaN of 107 results`), nhưng ở vòng review lần 1 tôi đã soi kỹ nhất chính ảnh bằng chứng của item này — đối chiếu `NaN-NaN` với việc bảng vẫn hiện 5 dòng cùng lúc — và chỉ chấp nhận đảo verdict Pass→Fail sau khi tự thấy hai dữ kiện đó tự đủ mâu thuẫn nhau trên cùng một ảnh, không cần tin lời mô tả. Tôi cũng yêu cầu tách thành 2 finding (**F-005** vế a, **F-006** vế b) đúng theo cách item yêu cầu. |
| **Artifact #9 — Ảnh bằng chứng tự nhiễm (dải chú thích lọt vào chính vùng đo)** | | | | |
| Tool: Claude + javascript_tool<br>Time: 2026-08-02 20:44<br>Tôi yêu cầu: *"chụp bằng chứng cho item Fail"* + *"ảnh phải chứa thanh địa chỉ hiện URL EMS"* | Dải chú thích cho IA02-13 in ra chuỗi regex `/unsaved\|discard\|are you sure\|lost/i found = true` — kết luận ngược với finding đang báo. | **INVALID** | Yêu cầu "ảnh phải tự đủ để kiểm chứng" mà tôi đặt ra ngay từ đầu vô tình lộ ra chính lỗi này: dải chú thích tôi yêu cầu chèn vào ảnh lại bị chính phép đo quét trúng. | AI tự phát hiện và sửa trước khi đưa ảnh này cho tôi — clone `document.body`, gỡ dải chú thích khỏi bản clone rồi mới tìm regex, ra kết quả đúng `false`. Ảnh sai không lọt vào bộ tôi duyệt; tôi chỉ xác nhận lại nguyên nhân (tự nhiễm, không phải lỗi SUT) có hợp lý không khi đọc report, và đồng ý đó là lỗi phương pháp đo chứ không phải điều gì cần điều tra thêm. |
| **Artifact #10 — Ảnh và lời chú thích mâu thuẫn nhau cho IA01-12 (focus)** | | | | |
| Tool: Claude + claude-in-chrome<br>Time: 2026-08-02 18:05–18:10<br>(chụp ảnh cho item Fail IA01-12 theo yêu cầu chung của tôi) | Hai lần chụp đầu, dải chú thích ghi "focus đang ở Go to page, không có ring" nhưng ảnh cho thấy focus thật nằm trên nút phân trang "22" (có ring rõ). | **INVALID** | Một ảnh mâu thuẫn với chính lời chú thích của nó là bằng chứng không dùng được — nếu tôi nộp nguyên trạng, đó là bằng chứng sai, đúng thứ §12 muốn ngăn. | Cả hai ảnh sai bị loại trước khi tới tay tôi. Tôi chấp nhận cách trình bày thay thế mà AI đề xuất (số đo `getComputedStyle` kèm số đo đối chứng của phần tử có ring, thay vì cố chụp "chỗ không có gì để chụp"), vì bản chất lỗi đúng là không có gì được vẽ ra. *(Ở vòng review lần 2, tôi tự tay đo lại đúng item này và xác nhận nó đã hoạt động đúng — xem Artifact #18.)* |
| **Artifact #11 — Gom item Fail thành finding + chấm severity** | | | | |
| Tool: Claude<br>Time: 2026-08-02 20:30–20:55<br>Tôi yêu cầu: *"Lọc Fail thành bug (gộp cùng nguyên nhân gốc), viết bug-reports.md, chấm severity"* | AI gom các item Fail thành finding theo quy tắc "cùng nguyên nhân gốc → 1 bug", đề xuất severity theo thang Nielsen 0–4. | **VALID** | IA03-06 tách thành 2 finding vì item ghi rõ *"score them as separate findings, never as one"* — tôi kiểm quy tắc gộp có tuân đúng câu đó không trước khi chấp nhận. | Tôi rà lại toàn bộ mức severity ở vòng review lần 1, rồi chốt lại lần nữa ở vòng review lần 2 sau khi tôi quyết định loại 3 finding (xem 3.2 và 3.3). Quyết định của tôi không đổi qua cả hai lần rà: giữ **F-010 ở mức 3**, không nâng lên 4. |
| **Artifact #12 — Xử lý 2 finding không thuộc item nào** | | | | |
| Tool: Claude<br>Time: 2026-08-02 20:50<br>(trong lúc gộp finding theo yêu cầu chung của tôi) | AI báo: **F-008** (search không tìm được theo tên hiển thị) và **F-009** (render kết quả cũ) không map được vào bất kỳ item nào trong 60 item, và **từ chối** gán bừa vào một item gần đúng. | **VALID** | §7 nhận bug bất kể có thuộc checklist hay không — tôi kiểm lại checklist v1.9 để xác nhận đúng là không có item nào cho ô search của bảng admin, dù cả 5 danh sách EMS đều có. | Tôi đồng ý với việc AI từ chối gán bừa — gán vào một item không liên quan chỉ để "có mã item" sẽ là gán sai bằng chứng. Tôi quyết định giữ 2 finding này ở dạng "ngoài checklist", và tự thêm một đề xuất cho v2.0 (thêm item về search trên bảng dữ liệu) để đưa lại cho nhóm. |
| **Artifact #13 — Toàn bộ 4 file execution + bug report + findings log + README, và một lỗi cộng nhẩm** | | | | |
| Tool: Claude<br>Time: 2026-08-02 19:30–21:00<br>Tôi yêu cầu: *"viết bug report, chấm severity, điền findings log, viết báo cáo tổng hợp"* | 4 file execution (240 dòng verdict), `bug-reports.md`, `findings-log.md`, `README.md` tổng hợp. Bản đầu của `README.md`/`C2.md` ghi C2 = 7 Pass/6 Fail. | **INCOMPLETE** | Runbook tôi đặt ra bắt buộc kiểm `Passed+Failed+N/A+chưa execute=60` cho từng màn hình trước khi coi là xong — con số 7/6 chưa qua phép kiểm đó. | AI tự chạy lại một script parse trực tiếp bảng verdict để đối chiếu, thay vì tin số đã cộng nhẩm, và ra đúng 6 Pass/7 Fail. Tôi áp dụng lại đúng nguyên tắc này ở cả hai vòng review sau — **không tin số tự cộng, luôn đếm lại trực tiếp từ bảng** — và chính thói quen tôi giữ đó về sau tự tôi bắt được thêm 1 lỗi đếm khác (xem Artifact #22). |

### 3.2 — Hai item DevTools tôi tự tay đo + vòng tôi review lại toàn bộ (2026-08-03)

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Tôi đã kiểm tra / quyết định gì |
|---|---|---|---|---|
| **Artifact #14 — Hai item DevTools tôi tự tay đo (AI không bật được throttling)** | | | | |
| Tool: **không dùng AI** — tôi tự thao tác Chrome DevTools<br>Time: 2026-08-03<br>AI chỉ đưa hướng dẫn từng click; tôi tự chạy và tự báo kết quả | Tôi báo lại 2 kết quả: (a) IA01-07 Slow 3G → "Có Skeleton"; (b) một thao tác block/unblock: *"qua account Admin để inactive thì nó update status thôi. Không báo lỗi gì cả."* | **INCOMPLETE** | Verification Rule của IA04-11 đòi ép server fail bằng Offline **rồi mới** submit — thao tác (b) tôi mô tả là một lần **thành công**, không phải một lần lỗi. | AI đối chiếu kết quả tôi báo với đúng Verification Rule của từng item, và chỉ chấp nhận (a) làm bằng chứng cho IA01-07 = Pass; từ chối dùng (b) để chấm IA04-11, kể cả khi tôi đã báo cáo xong. AI còn phát hiện tôi ghi nhầm mã item (`IA04-07` thay vì `IA01-07`) — tôi xác nhận đúng là mình nhầm và để AI sửa lại. Việc từ chối đó buộc tôi phải chạy lại đúng kịch bản ở Artifact #15. Quan sát (b) tôi tự làm được dùng làm tham khảo cho câu hỏi "EMS có báo toast khi Save thành công không" tại thời điểm đó — câu hỏi này sau đó tôi tự kiểm lại toàn diện ở vòng review lần 2 (Artifact #18) và kết luận **không phải bug**. |
| **Artifact #15 — Ca offline IA04-11 tôi chạy lại đúng kịch bản, dữ liệu thật (F-018)** | | | | |
| Tool: **không dùng AI** — tôi tự thao tác<br>Time: 2026-08-03<br>AI đưa lại hướng dẫn sau khi từ chối chấm ở Artifact #14; tôi chạy lại | Tôi chụp lại dialog Edit User với khối lỗi đỏ inline ghi `Failed to fetch`, panel Network 97 request gần như toàn bộ `(failed)`. | **VALID** | Tôi đối chiếu ảnh mình chụp với 4 vế Expected của IA04-11: có báo lỗi ✅, không toast success giả ✅, không spinner vô tận ✅, nhưng không plain-language và không có retry ❌. | Toàn bộ dữ liệu dòng này do tôi tự tạo bằng tay, không qua AI. Tôi chấp nhận cho AI chấm IA04-11 = Fail chỉ trên C2 (không suy ra cho C1), và đồng ý ghi thành **F-018**. |
| **Artifact #16 — Vế "load a list screen" của IA04-11 — hướng dẫn AI đưa cho tôi bị sai nguyên tắc** | | | | |
| Tool: **không dùng AI** — tôi tự thao tác<br>Time: 2026-08-03<br>AI yêu cầu tôi: *"bật Offline → hard-reload /dashboard/admin/users"* | Tôi chụp lại: trang lỗi của chính Chrome (`ERR_INTERNET_DISCONNECTED`); document request `(failed)` trước khi EMS được nạp. | **INVALID** | Khi nhìn kết quả mình vừa chụp, tôi nhận ra hướng dẫn hard-reload lúc offline **không thể** kiểm được SUT theo cách này — trình duyệt chặn ở tầng navigation trước khi EMS kịp chạy, bất kể tôi làm lại bao nhiêu lần. | Tôi từ chối để AI chấm cả Pass lẫn Fail cho vế này — chấm Pass là ghi công sai cho EMS, chấm Fail là quy trách nhiệm sai cho một thứ EMS chưa từng chạm tới. Tôi yêu cầu chấm **N/A kèm lý do "không quan sát được qua SUT"**, khác hẳn loại N/A "widget vắng mặt" đang dùng ở 196 ô còn lại, và không đồng ý làm thêm đường điều hướng mềm để bù — ghi lại thành đề xuất v2.0 thay vì cố kiểm bằng được. |

**Vòng tôi review lại toàn bộ (2026-08-03, ~1 giờ):** tôi tự mở lại 4 file execution và toàn bộ 27 ảnh evidence, đối chiếu offline từng ô verdict với lý do và ảnh đi kèm — không tin vào kết luận AI đã ghi, mà tự xem lại bằng chứng gốc. Tôi soi kỹ nhất ảnh của **F-010** (nhãn First/Last Name gán ngược) và **F-005** (`NaN-NaN of 107 results`) vì đây là hai finding có sức nặng nhất. Tôi đồng ý toàn bộ 197 ô N/A sau khi xác nhận mỗi ô đều nêu đích danh widget vắng mặt, đồng ý toàn bộ ô Fail sau khi tự đọc lại ảnh, và tự quyết định giữ nguyên 1 ô trống (`IA04-04` trên C3) vì kiểm nó đòi xoá thật một user — tôi không cho phép thao tác đó. Tôi chốt lại mức severity theo thang Nielsen. **Tôi không đảo verdict nào ở vòng này** — thay đổi duy nhất là tôi tự chốt severity và tự xác nhận giữ ô trống.

### 3.3 — Vòng tôi tự kiểm tay và bác bỏ 3 finding, quyết định đánh số lại, yêu cầu dọn ngôn ngữ audit (2026-08-03 – 2026-08-04)

Đây là vòng quan trọng nhất: tôi trực tiếp thao tác lại trên EMS thật những hành vi UI mà AI đã chấm Fail ở vòng 1, thấy chúng hoạt động khác với những gì đã ghi, nên tôi yêu cầu AI sửa lại toàn bộ artifact phụ thuộc, rồi tự kiểm lại lần cuối trước khi chốt. Tôi ghi lại theo đúng trình tự đã xảy ra: **AI đưa ra kết luận X → tôi thấy nghi ngờ vì lý do Y → tôi tự tay kiểm chứng trên SUT → kết quả trái ngược với kết luận của AI → tôi bác bỏ kết luận đó → tôi yêu cầu AI cập nhật mọi artifact phụ thuộc.**

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Tôi đã kiểm tra / quyết định gì |
|---|---|---|---|---|
| **Artifact #17 — Tôi tự kiểm tay nút chuyển ngôn ngữ EN/VI, bác bỏ kết luận Fail của AI** | | | | |
| Tool: tôi tự bấm nút trên UI thật (**không dùng AI**); AI chỉ cập nhật artifact sau khi tôi báo lại<br>Time: 2026-08-03<br>Tôi yêu cầu AI (nguyên văn): *"Hiện tại thì tôi đang chạy các bug trong findings-log.md trên EMS. Thì có một cái là chuyển ngôn ngữ... tôi có test lại là cái nút chuyển ngôn ngữ anh việt work normally chứ ko phải ko có và cx ko có bug như chuyển language ko được. Hãy review lại và chỉnh sửa cho tôi."* | AI đổi verdict `IA01-08` trên C1 từ Fail → Pass, xoá finding "nút chuyển ngôn ngữ không hoạt động" khỏi `findings-log.md` và `bug-reports.md`, sửa lại phần Actual của `IA01-09` (bỏ giả định "không đổi được locale"), cập nhật số Pass/Fail/N/A trên C1 và README. | **VALID** | §2 đặt trách nhiệm về tính đúng đắn cuối cùng lên tôi. Quan sát trực tiếp của tôi trên SUT thật là nguồn xác thực cho hành vi UI — không phải phép đo DOM một lượt trước đó của AI. | Tôi tự bấm nút chuyển ngôn ngữ trên UI thật, thấy nó chuyển đổi bình thường giữa Anh và Việt — trái ngược hẳn với verdict Fail mà AI đã ghi ở vòng 1. Tôi bác bỏ kết luận cũ và yêu cầu AI sửa. Sau khi AI cập nhật, tôi kiểm lại rằng không sót file nào trong chuỗi `C1.md → bug-reports.md → findings-log.md → README.md` trước khi chấp nhận là xong. |
| **Artifact #18 — Tôi tự kiểm tay focus (Go to page + dialog Edit/Delete), bác bỏ kết luận Fail của AI trên cả 3 màn hình** | | | | |
| Tool: tôi tự thao tác trên UI thật (**không dùng AI**); AI chỉ cập nhật artifact sau khi tôi báo lại<br>Time: 2026-08-03<br>Tôi yêu cầu AI (nguyên văn): *"F-004 work nhé => Update các cái liên quan đi"* | Trước khi sửa, AI hỏi lại tôi để làm rõ phạm vi — vì F-004 gộp 2 phần độc lập (focus ring ở "Go to page" và focus-trap khi mở dialog) và câu "work" của tôi chưa nói rõ tôi đang xác nhận phần nào. Sau khi tôi xác nhận **cả hai** phần đều đúng, AI đổi `IA01-12` từ Fail → Pass trên cả C1, C2, C3, xoá finding, cập nhật số liệu 3 file execution + README + bug-reports. | **VALID** | Tôi đánh giá cao việc AI hỏi lại thay vì tự đoán phạm vi — đây đúng là điều §2 muốn ("AI là trợ lý kỷ luật, không phải hộp đen"): không tự suy diễn khi lệnh của tôi còn mơ hồ. | Tôi tự tay Tab tới ô "Go to page" và tự mở dialog Edit/Delete để kiểm cả hai phần trước khi trả lời câu hỏi làm rõ của AI — tôi xác nhận **cả hai** đều hoạt động đúng, khác với verdict Fail mà AI đã ghi ở Artifact #10. Nhờ tôi trả lời rõ phạm vi ngay từ đầu, AI sửa đúng cả 3 màn hình trong một lượt, không phải quay lại lần hai. |
| **Artifact #19 — Tôi yêu cầu xoá finding toast và đánh số lại toàn bộ ID — AI hỏi rõ hệ quả trước khi tôi cho phép sửa** | | | | |
| Tool: tôi tự kiểm tay trước (**không dùng AI**); AI cập nhật artifact sau khi tôi ra quyết định<br>Time: 2026-08-03/04<br>Tôi yêu cầu AI (nguyên văn): *"Xóa bug F-014 đi, sau đó reset lại các id khác => Mấy cái bug ghi là 'do sinh viên chạy tay' => Xóa hộ mấy cái text kiểu z giúp, tự bắn vào chân à?"* | Trước khi xoá, AI chỉ ra rằng finding toast cũ đang được 2 item checklist (`IA04-04`, `IA04-12`) trace tới, cả hai đang Fail trên C2 và C4 — và hỏi lại tôi: nếu chỉ xoá finding mà giữ nguyên verdict Fail thì sẽ vi phạm chính quy tắc đối chiếu Fail→finding mà tôi đã yêu cầu ở Artifact #11. | **VALID** (tôi coi việc AI hỏi lại là đúng, thay vì tự suy diễn) | Tôi yêu cầu ngay từ đầu (Artifact #6): không tự đoán khi có ambiguity, phải hỏi. AI áp đúng nguyên tắc đó ở đây thay vì tự chọn một cách xử lý. | Tôi trả lời: đổi `IA04-04`/`IA04-12` thành Pass, vì tôi đã tự kiểm lại và xác nhận EMS có hiện xác nhận sau khi Save/Export thành công. Tôi cũng quyết định việc đánh số lại toàn bộ 18 finding còn lại thành `F-001…F-018` liên tục, thay vì giữ khoảng trống ID như quy tắc cũ — đây là quyết định của tôi về cách trình bày bản nộp, không phải đề xuất của AI. AI thực thi bằng một script đổi ID an toàn (map cũ→mới qua token tạm để tránh trùng số) và chạy lại `generate-paste.py` để đồng bộ `form-copy-paste.txt`. |
| **Artifact #20 — Sau khi tôi yêu cầu đánh số lại, tôi bắt AI tự đối chiếu chéo và nó tìm ra một mâu thuẫn do chính nó gây ra** | | | | |
| Tool: Claude, theo yêu cầu đối chiếu chéo tôi luôn đặt ra sau mỗi đợt sửa lớn | Sau khi chạy script renumber, khi tự đối chiếu lại toàn bộ file liên quan, AI nhận ra các ghi chú "ID X đã bị loại, không tái sử dụng" (viết theo mô hình cũ — giữ khoảng trống ID) giờ mâu thuẫn trực tiếp với chính việc đánh số lại vừa làm, vì các ID đó **đã bị finding khác chiếm lại**. | **INVALID** (bị chặn lại trước khi tới tay tôi) | Đây là hệ quả trực tiếp của quyết định đánh số lại mà tôi đưa ra ở Artifact #19 — sửa một chỗ (đánh số) nhưng chưa kiểm hết chỗ khác đang giả định trạng thái cũ (khoảng trống ID vĩnh viễn). | Tôi không yêu cầu riêng cho lần này, nhưng tôi luôn đòi một vòng tự-đối-chiếu sau mỗi thay đổi lớn (đây là cách làm việc tôi đã thiết lập từ Artifact #13, và lặp lại tường minh ở yêu cầu "Final Verification" tôi đưa ra sau đó). Khi áp dụng đúng yêu cầu đó cho lần renumber này, AI tự bắt được mâu thuẫn trước khi đưa cho tôi, xoá các ghi chú sai và viết lại Quy tắc 2 (đánh số lại một lần duy nhất ngày 2026-08-03; không tái sử dụng ID áp dụng từ nay trở đi). Tôi không phải can thiệp thêm ở artifact này, nhưng tôi ghi nó vào đây để minh bạch: lỗi này có tồn tại trong vài phút của phiên làm việc, dù không lọt ra bản tôi nộp. |
| **Artifact #21 — Tôi yêu cầu loại bỏ ngôn ngữ "chạy tay"/"AI không làm được" khỏi mọi artifact** | | | | |
| Tool: Claude<br>Time: 2026-08-04<br>Tôi yêu cầu (nguyên văn, xem Artifact #19): *"Xóa hộ mấy cái text kiểu z giúp, tự bắn vào chân à?"* | AI quét toàn bộ `C1.md`…`C4.md`, `bug-reports.md`, `findings-log.md` tìm các câu kiểu "do sinh viên chạy tay vì AI không bật được X" và "kết quả này thay thế lần đo tự động trước đó, từng ghi Fail" — cả hai đều là khung tường thuật "AI sai, người sửa" không cần thiết cho một verdict Pass hợp lệ. | **VALID** | Tôi chỉ ra rằng loại tường thuật này khiến bản nộp "tự bắn vào chân" — mô tả vai trò AI theo cách có thể bị đọc thành vi phạm chính sách học thuật, dù nội dung kỹ thuật không sai. | Tôi là người đặt ra yêu cầu này sau khi tự đọc lại các file và nhận ra vấn đề — không phải AI tự phát hiện. Tôi yêu cầu giữ lại **sự kiện** (ngày đo, verdict, bằng chứng) nhưng bỏ khung "ai đúng ai sai", vì khung đó không phục vụ mục đích chấm điểm. Tôi kiểm lại sau khi AI sửa, xác nhận áp dụng nhất quán trên toàn bộ 4 file execution + `bug-reports.md`. |
| **Artifact #22 — Tôi tự review toàn diện repo theo checklist TA-style; tôi bắt AI đối chiếu số liệu và lộ ra một lỗi đếm kế thừa từ bản gốc** | | | | |
| Tool: Claude<br>Time: 2026-08-04<br>Tôi tự soạn và giao một bản đối chiếu Requirement → Artifact → Evidence → Risk theo 6 mục (Coverage, Deliverables, Quality, AI Compliance, Risk, Readiness) | Khi tôi yêu cầu AI đối chiếu toàn bộ `hw3/out/` với đề bài và `artifact-contracts.md`, và verify lại số `Type = Bug/Usability` ở `findings-log.md` (khi đó đang ghi 12/6), AI đếm lại trực tiếp từng dòng trong bảng 18 finding và ra 11/7 — lệch 1 so với số đang ghi. | **INCOMPLETE** (lỗi kế thừa, không tự phát sinh ở lần sửa gần nhất) | Tôi yêu cầu bất kỳ con số nào trong bản nộp cũng phải verify được bằng cách đếm trực tiếp, không chấp nhận số suy ra bằng cộng/trừ nhẩm — cùng nguyên tắc tôi đã đặt ra và AI từng áp dụng ở Artifact #13. | Tôi yêu cầu AI kiểm lại nguồn gốc con số 12/6 thay vì chỉ sửa cho khớp — hoá ra nó được tính bằng cách trừ dần từ con số gốc 15/6 của bản 21-finding đầu tiên, và bản gốc đó **chưa từng được ai verify độc lập** (đếm trực tiếp ra 14/7, tức đã sai từ trước cả phiên làm việc này). Tôi chấp nhận sửa lại 11/7 sau khi thấy AI đếm bằng công cụ (`awk`) chứ không phải cộng nhẩm, ở cả `findings-log.md` và `README.md`. |
| **Artifact #23 — Tôi tự submit Google Form** | | | | |
| Tool: **không dùng AI** — tôi tự đăng nhập bằng email MSSV và submit<br>Time: 2026-08-04 | Tôi dán 18/18 finding vào Form, mỗi finding một lần submit, nội dung lấy nguyên văn từ khối tương ứng trong `bug-reports.md` mà AI đã chuẩn bị sẵn. | **VALID** | §7 yêu cầu nộp bằng chính tài khoản `MSSV@....edu.vn` của tôi — đây là hành động AI không thể và không được làm thay. | Tôi tự thực hiện toàn bộ 18 lần submit, sau đó báo lại kết quả cho AI để cập nhật cột *Form timestamp* (18/18, `2026-08-04`) trong `findings-log.md`, trường `Form submitted` trong `bug-reports.md`, và tôi yêu cầu quét xoá mọi câu "chưa submit"/"0/18" còn sót trong `README.md`. |

### 3.4 — Task 3 (Cross-Platform) và §8 Agent Skills (2026-08-03)

Vòng này khác Task 1B ở một điểm: tôi trực tiếp điều phối phần lớn quyết định
kỹ thuật trong hội thoại (không chỉ review lại sau), nên bảng dưới đây giữ
lại đúng các tương tác thể hiện tôi phản biện hoặc sửa AI, không liệt kê các
bước vận hành thuần túy (mở file, click, "continue", "approve", chỉnh toạ độ
click, foreground cửa sổ...) — những bước đó là thao tác kỹ thuật cần thiết
nhưng không phản ánh năng lực đánh giá, nên không đưa vào đây theo đúng mục
đích của Mục 3.

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Tôi đã kiểm tra / quyết định gì |
|---|---|---|---|---|
| **Artifact #24 — Kế hoạch v1 giả định cloud/thiết bị sẵn có; pilot thật lộ ra blocker, phải đổi chiến lược** | | | | |
| Tool: Claude<br>Time: 2026-08-03<br>Tôi yêu cầu lập kế hoạch coverage cho 3 OS × 5 browser × 3 device class theo đúng §6 | Bản kế hoạch đầu (v1, 24 dòng/6 run) coi cả 6 cấu hình — kể cả macOS desktop và iOS tablet qua BrowserStack cloud — là chạy được như nhau, không phân biệt cấu hình nào phụ thuộc hạ tầng bên thứ ba chưa được kiểm chứng. | **INCOMPLETE** | §12 chỉ chấp nhận bằng chứng đến từ thực thi thật — một kế hoạch coi cloud session là "chắc chạy được" mà chưa thử là một giả định chưa kiểm chứng, không phải bằng chứng. | Tôi yêu cầu chạy pilot thật (Run D) trước khi tin bất kỳ ô cloud nào là khả thi. Pilot lộ ra BrowserStack Free Trial giới hạn cứng 1 phút/phiên — không đủ login + điều hướng + capture. Tôi từ chối phương án giả lập (DevTools responsive mode gắn nhãn "tablet thật") và yêu cầu đổi sang Coverage Fallback Strategy: 20 cell Executed thật + 8 cell Blocked có bằng chứng, thay vì một ma trận 24 ô trông "đủ" nhưng có phần chưa từng chạy thật. |
| **Artifact #25 — No-DOM Policy, thứ tự xoá disposable user, và cổng phê duyệt trước hành động không thể hoàn tác** | | | | |
| Tool: Claude + claude-in-chrome<br>Time: 2026-08-03<br>Tôi yêu cầu mọi thao tác trên EMS chỉ qua UI nhìn thấy được, và yêu cầu giữ nguyên user dùng chung `test abc` cho tới khi tất cả 5 run dùng xong | AI thực thi đúng: không dùng DOM/selector để bypass UI khi thao tác EMS (chỉ dùng DOM-based tool trên panel BrowserStack, không phải trên EMS); hoãn "Full Confirm" (xoá thật) của C3 sang một bước riêng sau cùng; và dừng lại xin xác nhận rõ ràng ("Confirm") trước khi thực sự bấm nút xoá. | **VALID** | Xoá user là hành động không thể hoàn tác; §12 và nguyên tắc an toàn chung của tôi đòi con người phải là người quyết định thời điểm và có xác nhận rõ ràng, không phải AI tự quyết. | Tôi xác nhận rõ ràng bằng từ "Confirm" đúng thời điểm AI hỏi, sau khi cả 5 run đã dùng xong `test abc` ở phạm vi Dialog-only. Tôi kiểm lại rằng AI không tự ý bấm Confirm sớm hơn ở bất kỳ run nào trước đó. |
| **Artifact #26 — Tách `hw3/work/` và `hw3/out/`; pipeline raw → candidate → final bị bỏ sót một promotion, Agent Skill tự phát hiện** | | | | |
| Tool: Claude<br>Time: 2026-08-03<br>Tôi yêu cầu mọi evidence phải qua đúng pipeline raw → annotated candidate → human review → final, và `hw3/out/` chỉ chứa bản đã duyệt | Khi chạy `compat-run-planner` lần đầu để đối soát coverage, skill phát hiện ảnh evidence chính (primary) của C1/Run A đã có bản candidate được duyệt từ trước nhưng **chưa từng được promote** sang `hw3/out/` — chỉ có bản supplementary được promote. | **INCOMPLETE** | Một cell Executed thiếu ảnh primary trong thư mục final là một khoảng trống thật trong bằng chứng, dù verdict Pass của cell đó không sai. | Tôi yêu cầu không chụp ảnh mới để lấp chỗ trống (sẽ là dữ liệu không đồng nhất về thời điểm) mà phải promote đúng bản candidate đã được duyệt trước đó. Sau khi sửa, tôi yêu cầu chạy lại skill để xác nhận đủ 20/20 ảnh primary, và ghi lại sự cố này minh bạch trong `skill-validation.md` thay vì âm thầm sửa rồi báo "không có vấn đề gì". |
| **Artifact #27 — Actor model 3 trạng thái, ghi đúng theo run log, không suy diễn** | | | | |
| Tool: Claude<br>Time: 2026-08-03<br>Tôi yêu cầu mỗi cell phải ghi rõ Planned và Actual Execution Mode (`AI-executed` / `AI-executed with human checkpoints` / `Human-executed with AI guidance`) | AI ghi đúng: Run A = AI-executed with human checkpoints (Claude trực tiếp điều khiển Chrome); Run B/C/G/F = Human-executed with AI guidance (tôi tự thao tác, AI hướng dẫn từng bước). Không cell nào bị gán mode mà run log không nêu rõ. | **VALID** | Actor model chỉ có giá trị nếu phản ánh đúng ai thực sự bấm chuột — gán sai (ví dụ ghi "AI-executed" cho một run tôi tự tay làm) sẽ khai khống mức độ tự động hoá. | Tôi đối chiếu cả 2 Agent Skill: cả hai đều từ chối tự điền Actual Execution Mode cho bất kỳ cell nào nếu run log tương ứng không nói rõ — đây là một guardrail tôi yêu cầu đưa thẳng vào `SKILL.md` (không phải điều khoản mềm), và xác nhận nó hoạt động đúng khi chạy thật trên dữ liệu Task 3. |
| **Artifact #28 — Lỗi đếm "24 Executed / 23 Pass" bị tôi phát hiện và yêu cầu sửa thành 20/19/1/8** | | | | |
| Tool: Claude<br>Time: 2026-08-03<br>Tôi yêu cầu Claude tóm tắt lại kết quả Task 3 giữa phiên | Bản tóm tắt của AI ghi "toàn bộ 24 cell Executed... 23 Pass... 1 Fail... 8 cell Blocked" — con số nội bộ mâu thuẫn (24 + 8 ≠ 28, và thiết kế manifest ngay từ đầu luôn là 20 Executed + 8 Blocked = 28). | **INVALID** | Manifest gốc do chính AI thiết kế đã luôn là 20 Executed/8 Blocked — con số 24/23 là lỗi báo cáo phát sinh giữa chừng, không phải một cách đếm khác hợp lệ. | Tôi yêu cầu Claude tìm và sửa **mọi** chỗ có số sai, không chỉ câu tôi vừa đọc. AI grep toàn bộ file Task 3, xác nhận lỗi thật chỉ tồn tại ở một dòng trong `run-log-A.md` (các chỗ khác nói "24" là so sánh lịch sử hợp lệ với bản kế hoạch v1), sửa lại thành 20/19/1/8, và tôi yêu cầu số này trở thành "nguồn sự thật" cố định được trích dẫn nguyên văn trong mọi artifact Task 3 sau đó (bao gồm cả 2 Agent Skill). |
| **Artifact #29 — Đối soát F-019/F-020/F-021 và ngày submit Task 1B: AI kết luận mạnh hơn bằng chứng, tôi yêu cầu viết lại** | | | | |
| Tool: Claude<br>Time: 2026-08-03<br>Tôi yêu cầu AI xác minh F-019/F-020/F-021 (ID cũ trước khi đánh số lại) có bị bỏ sót không, và kiểm lại ngày `2026-08-04` cho 18 finding Task 1B | Lần đầu, AI viết: F-019/F-020 "đã submit dưới một ID mới nào đó", "không có nội dung nào bị thiếu" — chỉ dựa trên phép tính tổng số (21 cũ − 3 loại bỏ = 18 giữ lại), không có bằng chứng trực tiếp nào xác định 2 ID đó là gì. | **INCOMPLETE** | Một phép tính về *tổng số lượng* không chứng minh được *danh tính* của một dòng cụ thể — đây là kết luận mạnh hơn bằng chứng cho phép, đúng loại lỗi §12 muốn ngăn (suy diễn thay cho bằng chứng). | Tôi bác bỏ kết luận đó, yêu cầu viết lại thành "unresolved historical IDs" — không suy đoán ánh xạ. Tôi cũng yêu cầu tách rõ ngày `2026-08-04` (18 finding Task 1B) thành "ghi nhận theo artifact Task 1 đã đóng băng, chưa re-verify độc lập trong phiên này" thay vì khẳng định đã xác minh — vì phiên Task 3 này chỉ đọc lại các artifact cũ, không tự tay kiểm chứng lại việc submit đó. F-021(cũ)→F-018 vẫn giữ nguyên vì có bằng chứng trực tiếp (git commit + evidence path trùng khớp) — tôi chỉ bác bỏ phần *không* có bằng chứng, không bác bỏ cả đôi. |
| **Artifact #30 — Thiết kế và dry-run validate 2 Agent Skill trên dữ liệu Task 3 thật** | | | | |
| Tool: Claude, qua skill `generate_skill`<br>Time: 2026-08-03<br>Tôi yêu cầu 2 skill: một skill đối soát coverage (`compat-run-planner`), một skill soạn report draft (`compat-evidence-report`), cả hai phải rút ra từ quy trình thật đã chạy, không phải quy trình lý tưởng | AI viết 2 `SKILL.md` với guardrail tường minh (không tính Blocked thành Executed, không tự đổi verdict, không tự promote sang `hw3/out/`, không suy đoán F-019/F-020...), rồi tự chạy thật trên `compatibility-manifest-working.md` + evidence + run log thật, đối chiếu output với nguồn sự thật `20/19/1/8`. | **VALID** (sau khi sửa 1 gap ở Artifact #26) | §8 yêu cầu skill phải qua pilot thật trước khi được coi là hoàn thành — chạy trên dữ liệu Task 3 thật, không phải dữ liệu mẫu, là cách duy nhất chứng minh guardrail hoạt động chứ không chỉ đọc hay. | Tôi yêu cầu chạy skill 2 lần trên dữ liệu thật (một lần dry run, một lần trong chính video demo) và đối chiếu cả hai lần đều ra đúng 20/19/1/8, không có sai lệch phát sinh giữa hai lần chạy. Tôi chỉ đồng ý promote `SKILL.md` sang `hw3/out/agent-skills/` sau khi `skill-validation.md` ghi PASS cho cả hai skill. |

---

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
|---|---|---|
| **Total AI-generated artifacts audited** | **30** | 100 % |
| **VALID (correct, accepted as-is)** | **14** | 46,7 % |
| **INVALID (wrong; rejected)** | **7** | 23,3 % |
| **INCOMPLETE (acceptable after edits)** | **9** | 30,0 % |

**Phân tách theo task:**

| Task | Total | VALID | INVALID | INCOMPLETE |
|---|---|---|---|---|
| Task 1 — Checklist execution, bug report, và 2 vòng tôi tự review lại | 23 | 11 | 6 | 6 |
| Task 2 — User testing design & analysis | **0 — chưa thực hiện** | — | — | — |
| Task 3 — Cross-platform | **5** (Artifact #24, #25, #27, #28, #29) | 2 | 1 | 2 |
| §8 — Agent Skills | **2** (Artifact #26, #30) | 1 | 0 | 1 |

**Lưu ý:** bảng này chưa đầy đủ cho toàn bộ assignment — Task 2 (User
Testing) chưa thực hiện tại thời điểm ghi nhận này, nên tổng 30 artifact chỉ
phản ánh Task 1 + Task 3 + Agent Skills. Bảng sẽ được bổ sung dòng Task 2
trước khi tài liệu này được coi là sẵn sàng cho Final Submission
Integration.

**Đọc bảng này thế nào — dưới góc nhìn của người review, không phải của AI:**

1. **Tỉ lệ VALID tăng từ 37,5 % (vòng 1, 16 artifact: #1–16) lên 71,4 % (vòng 2, 7 artifact: #17–23)** — không phải vì AI tự nhiên giỏi hơn, mà vì tôi giao việc rõ ràng hơn ở vòng 2: tôi đã tự kiểm chứng trước rồi mới yêu cầu AI cập nhật, thay vì để AI tự phán đoán rồi tôi mới soát lại sau. Con số này phản ánh cách tôi làm việc thay đổi, không phải AI thay đổi.
2. **6 artifact tôi đánh dấu INVALID trải trên cả hai vòng, nhưng tôi bác bỏ chúng vì hai lý do khác nhau.** Ở vòng 1 (Artifact #6, #8, #9, #10, #16), tôi hoặc AI (trước khi đưa cho tôi) bác bỏ vì lỗi đo đạc — đọc DOM quá sớm, tự nhiễm phép đo, hướng dẫn kiểm thử sai nguyên tắc. Ở vòng 2 (Artifact #20), tôi yêu cầu một vòng tự-đối-chiếu và nó lộ ra lỗi *truy vết phụ thuộc* — sửa một chỗ nhưng chưa kiểm hết chỗ khác. Tôi coi loại lỗi thứ hai nguy hiểm hơn vì nó không tự lộ ra, chỉ lộ khi có người chủ động đòi đối chiếu chéo — đây là lý do tôi giữ yêu cầu "tự đối chiếu sau mỗi đợt sửa lớn" như một bước bắt buộc, không phải tuỳ chọn.
3. **3 finding tôi tự tay bác bỏ hoàn toàn** (nút ngôn ngữ, focus, toast — Artifact #17–19) không phải vì AI đo sai kỹ thuật, mà vì tôi tự thao tác lại trên SUT thật và thấy kết quả khác với những gì đã ghi. Đây chính là lý do tôi coi §2 (human review) không phải một thủ tục hình thức: AI có thể tự tin báo cáo lại một kết quả đo được, nhưng không có cách nào tự biết liệu phép đo đó có còn đúng tại thời điểm tôi nộp bài hay không — chỉ có tôi, người trực tiếp thao tác lại, mới trả lời được câu đó.
4. **Ở Task 3, 3 loại lỗi khác nhau xuất hiện, và tôi phải xử lý mỗi loại khác nhau.** Artifact #28 (đếm sai 24/23) là lỗi báo cáo — sửa bằng cách grep lại toàn repo, không cần suy luận gì thêm. Artifact #26 (thiếu 1 ảnh promotion) là lỗi quy trình — chỉ lộ ra khi tôi bắt một Agent Skill tự đối chiếu manifest với đĩa thật, không lộ ra nếu chỉ đọc lại văn bản. Artifact #29 (đối soát F-019/F-020) là lỗi suy luận — AI trình bày một phép tính đúng (21−3=18) như thể nó chứng minh được một điều nó không chứng minh được (danh tính của 2 ID cụ thể). Loại thứ ba nguy hiểm nhất vì kết luận *nghe có vẻ hợp lý* và có số liệu đi kèm — tôi phải tự hỏi "phép tính này chứng minh được đúng cái gì" thay vì chấp nhận vì nó có vẻ chặt chẽ.

---

## 5. Conclusion — When should AI be used (or not)?

Trong Task 1B, tôi để AI làm phần **cơ học và nhất quán**: đọc DOM, đếm dòng, tính contrast theo công thức WCAG, gắn `MutationObserver` để chứng minh có/không có toast, mở file `.xlsx` ra đối chiếu cột, và giữ nguyên một cách chấm điểm qua cả 240 ô verdict — việc mà tôi tự làm tay dễ trôi dần sau vài giờ.

Tôi phải can thiệp ở hai chỗ khác nhau, xuất hiện ở hai vòng khác nhau của cùng bài này. **Ở vòng 1, tôi phải kiểm việc AI biết khi nào một quan sát đã đủ chín** — nó đọc số quá sớm, đo trúng thứ nó vừa tạo ra, rồi tin vào con số đó, trong khi tôi ngồi nhìn màn hình thì thấy ngay "còn đang tải". **Ở vòng 2, tôi phải kiểm việc AI biết khi nào một chỉnh sửa cục bộ làm hỏng một giả định ở chỗ khác** — khi tôi yêu cầu xoá một finding, việc đó kéo theo cả verdict checklist đang trace tới nó (Artifact #19) và những ghi chú tưởng vô hại nhưng ngầm giả định ID không bao giờ bị tái sử dụng (Artifact #20). Cả hai lần tôi phải can thiệp đều không phải vì AI thiếu kiến thức kỹ thuật, mà vì nó không tự đặt câu hỏi "sửa chỗ này có làm sai chỗ khác không" trừ khi tôi yêu cầu, hoặc trừ khi tôi bắt nó tự đối chiếu chéo bằng công cụ thay vì tin số cộng nhẩm.

Có một loại quyết định tôi giữ hoàn toàn cho mình, không giao cho AI: **đánh giá hệ quả có tính phán đoán về sản phẩm.** Ranh giới severity 3 và 4 của **F-010** (nhãn First/Last Name gán ngược) nằm ở câu hỏi *"dữ liệu này có cứu được không"* — đó không phải phép đo DOM mà AI có thể tự trả lời, và tôi giữ quyết định đó (mức 3) không đổi qua cả hai vòng review.

**Nguyên tắc tôi rút ra:** để AI chạy phần đo đạc và soạn thảo, nhưng bắt nó ghi lại số đo thô để tôi kiểm chứng — ràng buộc đó khiến vòng review lần 1 của tôi làm được trong một giờ thay vì phải chạy lại từ đầu. Sau mỗi chỉnh sửa lớn (như xoá/đánh số lại finding), tôi luôn đòi một vòng AI tự đối chiếu chéo toàn bộ file liên quan, không chỉ file được nêu tên trong lệnh — bài học trực tiếp từ Artifact #20. Và tôi giữ lại cho mình đúng những quyết định §12 nêu — bằng chứng thực thi, ảnh cross-platform, dữ liệu người tham gia thật — cộng thêm hai chỗ §12 không nói tới nhưng tôi thấy bắt buộc phải tự quyết: **mức severity**, và **việc tự tay kiểm chứng lại khi một hành vi UI có thể đã đổi hoặc bị AI chấm nhầm.**

**Task 3 mở rộng nguyên tắc đó theo một hướng mới:** ở Task 1B, việc tôi phải kiểm là "phép đo này còn đúng không". Ở Task 3, việc tôi phải kiểm thường là "kết luận này có thực sự được chứng minh bởi đúng dữ liệu nó trích dẫn, hay chỉ là một phép tính khác nghe có vẻ liên quan" (Artifact #29), và "một quy trình nhiều bước (raw → candidate → final) có thực sự chạy hết tới bước cuối cho từng cell, hay chỉ chạy hết cho hầu hết" (Artifact #26) — loại lỗi thứ hai này chỉ lộ ra khi tôi bắt một công cụ (Agent Skill) tự đối chiếu manifest với đĩa thật, không lộ ra nếu chỉ đọc lại văn bản báo cáo. Tôi giữ nguyên tắc cũ (không tin số cộng nhẩm, luôn đếm lại trực tiếp) nhưng mở rộng thêm: **không tin một kết luận chỉ vì nó có kèm một phép tính đúng** — phép tính đúng không tự động chứng minh điều nó đang được dùng để chứng minh.

---

## 6. Mandatory Disclosure (paste verbatim)

> "The Task 1B checklist execution report, bug reports, findings log and summary report were initially generated by **Claude (Claude Code + Claude in Chrome)**, which drove the browser and recorded every measurement under my direction. **I reviewed all 239 completed verdict cells and every evidence screenshot myself, in a dedicated post-execution review pass (2026-08-03), cross-checking each N/A against the widget inventory and each Fail against its screenshot and the checklist's stated Expected Behavior before accepting any of them.** In a second, later review pass (2026-08-03 to 2026-08-04), **I personally re-tested three UI behaviours the AI had scored as Fail — the EN/VI language toggle, keyboard focus on the pagination input and inside the Edit/Delete dialogs, and the success confirmation after Save/Export — directly against the live EMS. I found all three now work correctly, which contradicted the AI's original verdicts, so I rejected those verdicts and instructed the AI to update every dependent artifact.** I then required the AI to cross-check its own output against every dependent file after that change, which surfaced one thing it had missed on its own — a stale note asserting that three retired finding IDs would never be reused, which had become false the moment it renumbered the remaining findings into those same slots; I record this here rather than omit it, because it did not survive to the version I am submitting. **I take full responsibility for the decision to reject those three findings, for the decision to renumber the remaining 18 findings into a continuous `F-001`…`F-018` sequence, and for every severity rating in the final set, including the decision to keep the mislabelled-name finding (F-010) at severity level 3 rather than 4 — all product-impact judgments the AI could not make on its own.** I personally executed the two DevTools-throttling items (IA01-07 under Slow 3G and IA04-11 under Offline) by hand — the agent could not enable throttling — and that data is mine, not the agent's; the agent independently caught and rejected a data-entry mistake I made while reporting one of those results (a mislabelled item code), which I confirmed and let it correct. I personally submitted all 18 findings to the Google Form under my own student-ID email on 2026-08-04. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."

**Task 3 (Cross-Platform) and §8 Agent Skills — added 2026-08-03:**

> "For Task 3, I directed the pivot from an unverified 24-cell plan to a
> Coverage Fallback Strategy (20 Executed / 8 Blocked) after a live pilot
> confirmed a real BrowserStack Free Trial time limit — I refused a
> simulated-device workaround and required the two cloud-dependent
> configurations to be marked Blocked with evidence rather than faked.
> I gave explicit approval before the one irreversible action in this task
> — the real deletion of the disposable test user during the C3 Full
> Confirm Final Validation step. I caught and required a correction of a
> reporting error (an internally inconsistent "24 Executed / 23 Pass"
> summary partway through the session) and required every Task 3 artifact
> to cite the corrected 20/19/1/8 figures consistently. I rejected an
> AI-drafted reconciliation for historical finding IDs F-019/F-020 that
> presented a totals-only arithmetic check as if it proved the identity of
> two specific findings, and required it be rewritten as an explicitly
> unresolved gap instead — no id was fabricated to fill it. I directed the
> design of two Agent Skills (`compat-run-planner`, `compat-evidence-report`)
> from the real workflow already executed, required them to be run against
> the actual Task 3 data (not sample data) before I would accept them as
> validated, and one of those runs is what surfaced a real evidence-
> promotion gap (one primary screenshot that had been reviewed but never
> copied into the final folder) — I required it fixed by promoting the
> already-reviewed candidate, not by capturing a new one. I take
> responsibility for every verdict, severity, blocker classification, and
> promotion decision recorded in the Task 3 report and compatibility
> matrix. The demo video (https://youtu.be/GbhAEK7x8Vk) shows both skills
> running end-to-end against these real artifacts; I provided that link
> myself and it has not been independently reviewed by the AI in this
> session."

### Signature

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | Group 09 — 23KTPM2 |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Instructor:** | Dr. Lam Quang Vu / Dr. Tran Duy Hoang / MSc. Tran Thi Bich Hanh / MSc. Truong Phuoc Loc / MSc. Ho Tuan Thanh |
| **Date:** | 2026-08-04 (Task 1B) · 2026-08-03 (Task 3 + Agent Skills addendum above) |
| **Signature:** | Nguyễn Bảo Duy |

**Trạng thái tài liệu:** bao gồm Task 1 (final) và Task 3 + Agent Skills
(vừa bổ sung). **Task 2 (User Testing) chưa có entry nào** — tài liệu này
chưa sẵn sàng cho Final Submission Integration cho tới khi Task 2 hoàn tất
và có entry tương ứng ở Mục 3 và Mục 4.

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

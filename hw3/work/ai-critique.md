# AI Critique — HW03

> **Yêu cầu §11:** một đoạn **200–300 từ**. Trả lời: AI sai / thiên lệch / thiếu ở chỗ nào? Vì sao nó không bắt được? Bạn rút ra nguyên tắc gì về việc hợp tác với AI?
> **Bản chốt sẽ nằm ở:** `hw3/out/ai-critique.md` (Step 13). File này là bản nháp.
> **Viết bằng tiếng Anh** — giống bài HW2, và đây là tài liệu nộp.

---

## Cấu trúc 3 đoạn (theo đúng dạng bài HW2 đã dùng)

| Đoạn | Nội dung | Độ dài |
|---|---|---|
| **1** | **Một sai lầm cụ thể của AI** — kể được: nó làm gì, sai ở đâu, **phát hiện ra bằng cách nào** | ~120 từ |
| **2** | **Đổi cách làm việc thế nào sau đó** — quy trình mới ngăn lỗi đó lặp lại ra sao | ~90 từ |
| **3** | **Nguyên tắc rút ra** — phát biểu tổng quát, dùng được cho lần sau | ~70 từ |

---

## Ứng viên — chuyện đã xảy ra thật trong phiên chạy Task 1B (2026-08-02)

Phiên chạy Task 1B đã sinh ra **hai** ứng viên đủ rõ, nên hai ứng viên A và B từ phiên trước (bảng *Predicted N/A* lỗi thời; planning document mang giả định HW2) xuống làm dự phòng. Cả hai ứng viên mới đều khớp với một dòng có verdict **INVALID** ở Mục 3 của `ai-audit.md`, đúng như quy tắc 5.

### Ứng viên A — Đọc số quá sớm, suýt nộp một finding không có thật ⭐ *khuyên dùng*

**Chuyện gì đã xảy ra.** Lúc 17:47 agent gõ `test` vào ô search của Users Management rồi đọc DOM sau 4 giây. Kết quả đọc được: **94 kết quả**, và 5 dòng đầu tiên **không dòng nào chứa chữ "test"**. Agent gần như đã viết finding *"search trả về 94/105 dòng không khớp — search hỏng nặng"*, kèm severity 3.

**Vì sao sai.** Ô search của EMS có debounce, và mỗi ký tự gõ vào lại bắn một request. Con số 94 là **kết quả của một tiền tố ngắn hơn** còn đang hiển thị lúc agent đọc. Đo lại với thời gian chờ 7–9 giây cho ra kết quả đúng: `test` → **6 dòng, cả 6 đều thật sự chứa "test"**.

**Phát hiện ra bằng cách nào.** Không phải bằng cách nghi ngờ, mà **tình cờ**: khi chuyển sang đặt rows-per-page = 100 để đếm cho chính xác, con số 94 tự biến thành 6. Nếu bước đó không xảy ra, finding sai đã được viết ra.

**Vì sao chi tiết này đáng kể.** Người dùng thật ngồi trước màn hình sẽ **thấy** bảng đang nhấp nháy và biết là "chưa xong đâu". Agent thì đọc DOM tại một mốc thời gian cố định rồi tin vào con số đọc được. Đây đúng là loại sai lầm mà tự động hoá dễ mắc còn người chạy tay ít mắc.

**Cái kết đáng nói.** Hiện tượng gốc được điều tra tiếp bằng một `MutationObserver` lấy mẫu mỗi 200 ms, và trở thành **F-011** — một finding *khác*, đúng đắn: UI hiển thị kết quả của truy vấn cũ kèm nhãn `1-94 of 94 results` — một nhãn **tự nó nhất quán về số học** nên không có gì gợi ý là sai — mà không hề có spinner hay skeleton. Chính khiếm khuyết đo đạc của agent đã phát hiện ra một lỗi thật mà quan sát bằng mắt rất dễ bỏ qua.

**Kiểm ở đâu:** `ai-audit.md` Artifact #6 (INVALID) · `bug-reports.md` F-011 · `C1.md` IA01-07 Notes.

### Ứng viên B — Chỉ thử những giá trị nhìn thấy được, bỏ sót tập giá trị thật

**Chuyện gì đã xảy ra.** Chấm IA03-06 vế (a) — "nhãn phân trang có đúng số học không". Agent thử rows-per-page = 5, = 100, và sang trang 2; cả ba mốc đều khớp chính xác (`1-5 of 105` với 5 dòng, `1-100 of 105` với đúng 100 dòng, `101-105 of 105` với đúng 5 dòng). Chấm **Pass**.

**Vì sao sai.** Agent chỉ thử các giá trị **nhìn thấy trong dropdown**, không thử tập option mà DOM thật sự chứa. `<select>` rows-per-page xuất xưởng kèm một **option rỗng** làm option đầu tiên: `["", "5", "10", "20", "50", "100"]`. Khi option rỗng đó được chọn, nhãn render thành **`NaN-NaN of 107 results`** — giá trị `NaN` thô của JavaScript lọt thẳng ra giao diện.

**Phát hiện ra bằng cách nào.** Hoàn toàn **tình cờ**, hơn 2 giờ sau, lúc 20:06: agent bấm `Esc` để đóng dropdown trong lúc đang cố chụp ảnh cho một item **khác**, và nhãn đổi thành `NaN-NaN`. Sau đó mới tái hiện có chủ đích và đổi verdict IA03-06 từ Pass sang **Fail**.

**Vì sao AI không bắt được.** Nó test đúng những gì được *trình bày* cho người dùng, và bỏ qua những gì *tồn tại* trong DOM — dù chính nó đã đọc ra danh sách option đó từ trước và in ra `["","5","10","20","50","100"]` mà không dừng lại hỏi cái chuỗi rỗng kia là gì.

**Kiểm ở đâu:** `ai-audit.md` Artifact #8 (INVALID) · `bug-reports.md` F-007 · `C1.md` IA03-06.

### Ứng viên C — Phép đo tự nhiễm vì chú thích của người test lọt vào vùng đo (dự phòng)

Lúc 20:44, để chứng minh IA02-13 (thoát dialog không cảnh báo), agent tìm chuỗi `/unsaved|discard|are you sure|lost/i` trong `document.body.innerText` và in kết quả lên dải chú thích của ảnh bằng chứng. Kết quả in ra: **`true`** — tức là ngược hẳn với finding đang báo. Lý do: **chính dải chú thích đó chứa các từ trong regex**, nên phép tìm khớp với văn bản của người test chứ không phải của EMS. Agent tự phát hiện khi đọc lại ảnh vừa chụp, loại bỏ ảnh sai, sửa phép đo thành clone `document.body` rồi **gỡ dải chú thích khỏi bản clone** trước khi tìm, chụp lại. Kết quả đúng: `false`.

Ứng viên này ngắn hơn nhưng có một điểm hay: nó là ví dụ sạch của việc **dụng cụ đo làm nhiễu chính đối tượng đo**.

**Kiểm ở đâu:** `ai-audit.md` Artifact #9 (INVALID) · `evidence/C2/C2_IA02-13_esc-discards-edit-silently-2-after.png`.

### Dự phòng từ phiên trước (giữ lại, không còn ưu tiên)

| # | Chuyện gì đã xảy ra | Vì sao AI không bắt được |
|---|---|---|
| **D** | Bảng *Predicted N/A by scenario* liệt kê 14 item N/A cho scenario C; vòng audit v1.8/v1.9 thêm 7 item mới cho B và D mà **không cập nhật bảng phụ thuộc vào nó**. Thực tế đo được C1 một mình đã có 39 N/A | AI xử lý mỗi vòng audit như một tác vụ độc lập, không hỏi *"việc thêm item làm bảng nào khác trong file này sai đi?"* — thiếu **truy vết phụ thuộc** |
| **E** | Planning document trong `hw3/docs/` mang giả định từ HW2 sang | AI suy diễn cấu trúc bài mới từ workflow bài cũ vì repo tái sử dụng |

---

## Nguyên tắc — chọn một cho đoạn 3

- **AI đọc trạng thái, con người đọc quá trình.** Agent chụp DOM tại một thời điểm và tin vào cái nó thấy; con người nhìn thấy giao diện đang *chuyển động* và biết chờ. Với UI bất đồng bộ, "đo được số" không đồng nghĩa với "số đã ổn định". ← *khớp ứng viên A*
- **AI test cái được trình bày, không test cái tồn tại.** Nó thử những giá trị nhìn thấy trong dropdown, dù chính nó đã đọc ra tập option đầy đủ từ DOM. ← *khớp ứng viên B*
- **Dụng cụ đo phải nằm ngoài đối tượng đo.** ← *khớp ứng viên C*
- **Sửa cục bộ, hỏng toàn cục.** ← *khớp ứng viên D*

---

## Bản nháp (English — 269 từ)

> **Ghi chú:** đây là bản nháp do agent soạn từ log của chính phiên chạy. **Sinh viên nên đọc lại và viết lại bằng lời của mình** trước khi nộp — §11 hỏi về trải nghiệm hợp tác với AI, và một đoạn văn viết bằng giọng của chính người nộp sẽ thuyết phục hơn.

While executing the GUI checklist on the EMS Users list, the AI agent typed `test` into the search box and read the DOM four seconds later. It found 94 results, none of the visible rows containing the string "test", and was about to file a severity-3 defect: "search returns 94 non-matching rows." The finding was wrong. EMS debounces its search and fires a request per keystroke; 94 was a stale response for a shorter prefix, still on screen. Re-measuring after a longer wait returned 6 rows, all genuinely matching. I did not catch this by being suspicious — I caught it by accident, while changing rows-per-page for an unrelated count, when 94 silently became 6.

What that changed in how I work: every measurement that depends on an asynchronous UI now waits for the value to stop moving before it is recorded, and anything surprising gets sampled over time rather than read once. I instrumented the search with a 200 ms interval logger instead of a single snapshot. That instrumentation then produced a real defect I would otherwise have missed — for roughly one second the table shows a stale result set under the confident, arithmetically self-consistent label "1-94 of 94 results", with no spinner to suggest anything is loading.

The principle I take from this: **an AI reads state, a human reads process.** The agent captures the DOM at an instant and trusts what it sees; a person watching the same screen sees it still moving and knows to wait. For asynchronous interfaces, being able to measure a number is not the same as the number having settled.

**Số từ:** **269** / 200–300 ✓

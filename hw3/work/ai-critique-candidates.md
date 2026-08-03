# AI Critique — nguyên liệu thô (KHÔNG phải bản nộp)

> File này là chỗ chứa nguyên liệu thô cho `hw3/out/ai-critique.md`, dời sang đây khi assignment chưa đủ dữ liệu để viết critique thật (Task 2/3/Skills chưa xong). Không phải một trong các file nộp bài. Khi viết AI Critique thật ở cuối assignment, chọn 1 sự cố (từ Task 1, 2, 3, hoặc Skills — cái nào rõ nhất) và viết bằng lời của chính mình, không copy nguyên khối dưới đây.

## Ứng viên từ Task 1B (2026-08-02 — 2026-08-04)

### A — Đọc số quá sớm, suýt nộp một finding không có thật ⭐ ứng viên mạnh nhất hiện tại

Lúc 17:47 agent gõ `test` vào ô search rồi đọc DOM sau 4 giây: 94 kết quả, 5 dòng đầu không chứa "test". Gần như đã ghi finding "search trả về 94/105 dòng không khớp — search hỏng nặng", severity 3. Nguyên nhân: ô search có debounce, 94 là kết quả của một tiền tố ngắn hơn còn hiển thị. Đo lại sau 7–9 giây: `test` → 6 dòng, đúng cả 6. Phát hiện ra hoàn toàn tình cờ (đổi rows-per-page = 100 để đếm chính xác thì số tự đổi). Hiện tượng gốc điều tra tiếp bằng interval lấy mẫu 200ms, trở thành **F-009** — một finding khác, đúng đắn: UI hiện kết quả cũ kèm nhãn tự nhất quán về số học `1-94 of 94 results`, không có spinner. Kiểm ở: `ai-audit.md` Artifact #6 · `bug-reports.md` F-009.

### B — Chỉ thử giá trị nhìn thấy được, bỏ sót tập giá trị thật trong DOM

Chấm IA03-06 vế (a) Pass sau khi thử rows-per-page = 5, 100, trang 2 — cả 3 mốc đúng số học. Sai vì `<select>` có option rỗng đầu tiên (`["","5","10","20","50","100"]`) không hiện trong dropdown nhìn thấy được; chọn nó ra `NaN-NaN of 107 results`. Phát hiện tình cờ 2 giờ sau khi bấm Esc để đóng dropdown cho một ảnh khác. Kiểm ở: `ai-audit.md` Artifact #8 · `bug-reports.md` F-005/F-006.

### C — Phép đo tự nhiễm vì chú thích của người test lọt vào vùng đo

Tìm regex `/unsaved|discard|are you sure|lost/i` trong `document.body.innerText` để chứng minh IA02-13 không cảnh báo, nhưng chính dải chú thích của ảnh chứa các từ đó nên tự khớp `true`. Sửa bằng cách clone DOM và gỡ dải chú thích trước khi tìm. Kiểm ở: `ai-audit.md` Artifact #9.

### D — Sửa cục bộ, hỏng toàn cục (renumbering, vòng review 2)

Sau khi xoá 1 finding và đánh số lại 18 finding còn lại thành liên tục, các ghi chú kiểu "ID X đã bị loại, không tái sử dụng" (viết theo mô hình cũ — giữ khoảng trống ID) trở thành sai ngay lập tức, vì ID đó vừa bị một finding khác chiếm lại. Agent tự phát hiện khi đối chiếu chéo, không phải do sinh viên chỉ ra. Kiểu lỗi này khác hẳn nhóm A/B/C: không phải lỗi đo đạc, mà lỗi *không truy vết hết các artifact phụ thuộc vào một giả định vừa bị thay đổi*. Kiểm ở: `ai-audit.md` Artifact #20.

### E — Lỗi đếm kế thừa không tự lộ ra qua nhiều lần sửa

Một lỗi đếm Type=Bug/Usability (15/6 cho bản 21-finding gốc, đúng ra là 14/7) tồn tại từ trước cả phiên làm việc này, và bị kế thừa qua 2 lần trừ dần (khi 2 finding lần lượt bị xoá) mà không ai verify lại bằng cách đếm trực tiếp — tới khi một lần review tổng thể mới bắt được. Kiểm ở: `ai-audit.md` Artifact #22.

## Nguyên tắc khả dụng (chọn 1 khi viết bản thật, không dùng cả 5)

- **AI đọc trạng thái, con người đọc quá trình.** (khớp A)
- **AI test cái được trình bày, không test cái tồn tại trong DOM.** (khớp B)
- **Dụng cụ đo phải nằm ngoài đối tượng đo.** (khớp C)
- **Sửa cục bộ, hỏng toàn cục — nhất là khi sửa lại một quyết định trước đó.** (khớp D)
- **Một lỗi không tự lộ ra chỉ vì nó "đã được sửa nhiều lần" — số lần sửa không thay thế việc verify lại từ đầu.** (khớp E)

## Bản nháp cũ (269 từ, viết 2026-08-02, KHÔNG dùng — chỉ dựa trên Task 1, chưa có Task 2/3/Skills)

While executing the GUI checklist on the EMS Users list, the AI agent typed `test` into the search box and read the DOM four seconds later. It found 94 results, none of the visible rows containing the string "test", and was about to file a severity-3 defect: "search returns 94 non-matching rows." The finding was wrong. EMS debounces its search and fires a request per keystroke; 94 was a stale response for a shorter prefix, still on screen. Re-measuring after a longer wait returned 6 rows, all genuinely matching. I did not catch this by being suspicious — I caught it by accident, while changing rows-per-page for an unrelated count, when 94 silently became 6.

What that changed in how I work: every measurement that depends on an asynchronous UI now waits for the value to stop moving before it is recorded, and anything surprising gets sampled over time rather than read once. I instrumented the search with a 200 ms interval logger instead of a single snapshot. That instrumentation then produced a real defect I would otherwise have missed — for roughly one second the table shows a stale result set under the confident, arithmetically self-consistent label "1-94 of 94 results", with no spinner to suggest anything is loading.

The principle I take from this: an AI reads state, a human reads process. The agent captures the DOM at an instant and trusts what it sees; a person watching the same screen sees it still moving and knows to wait. For asynchronous interfaces, being able to measure a number is not the same as the number having settled.

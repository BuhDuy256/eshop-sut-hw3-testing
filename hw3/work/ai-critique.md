# AI Critique — HW03

> **Yêu cầu §11:** một đoạn **200–300 từ**. Trả lời: AI sai / thiên lệch / thiếu ở chỗ nào? Vì sao nó không bắt được? Bạn rút ra nguyên tắc gì về việc hợp tác với AI?
> **Bản chốt sẽ nằm ở:** `hw3/out/ai-critique.md` (Step 13). File này là bản nháp.
> **Viết bằng tiếng Anh** — giống bài HW2, và đây là tài liệu nộp.

---

## Cấu trúc 3 đoạn (theo đúng dạng bài HW2 đã dùng)

| Đoạn | Nội dung | Độ dài |
|---|---|---|
| **1** | **Một sai lầm cụ thể của AI** — kể được: nó làm gì, sai ở đâu, **bạn phát hiện ra bằng cách nào** | ~120 từ |
| **2** | **Bạn đổi cách làm việc thế nào sau đó** — quy trình mới ngăn lỗi đó lặp lại ra sao | ~90 từ |
| **3** | **Nguyên tắc rút ra** — phát biểu tổng quát, dùng được cho lần sau | ~70 từ |

**Vì sao cấu trúc này hiệu quả:** đoạn 1 chứng minh bạn có quan sát thật; đoạn 2 chứng minh bạn phản ứng; đoạn 3 là thứ §11 hỏi thẳng. Kể một lỗi cụ thể mạnh hơn nhiều so với nhận xét chung chung kiểu "AI đôi khi bịa".

⚠ **Bài HW2 dài ~340 từ — vượt trần 300 của HW3.** Đừng copy độ dài. Đếm từ trước khi nộp.

---

## Quy tắc viết

1. **Một sai lầm, kể sâu.** Đừng liệt kê năm lỗi nông.
2. **Nêu cách bạn phát hiện.** Đây là phần chứng minh có human review thật. HW2 viết: *"I only noticed the problem because the amount of work seemed much larger than expected"* — cụ thể, kiểm chứng được.
3. **Không tự trách.** §11 hỏi về AI và về nguyên tắc hợp tác, không phải lời xin lỗi.
4. **Phải là chuyện thật đã xảy ra với bạn.** Ghi lại ngay lúc gặp — cuối kỳ ngồi nhớ lại sẽ ra một đoạn văn chung chung, và người chấm phân biệt được.
5. **Nối với AI Audit Report.** Sai lầm bạn kể nên là một dòng có verdict **INVALID** hoặc **INCOMPLETE** ở Mục 3 của audit. Hai tài liệu khớp nhau thì cả hai đều đáng tin hơn.

---

## Ứng viên — chuyện đã xảy ra thật, cần bạn tự xác minh trước khi dùng

Đây **không phải bài viết sẵn**. Là những lần AI hụt mà bạn đã chứng kiến trong dự án này. Kiểm lại xem có đúng bạn nhớ như vậy không, chọn **một**, rồi viết bằng lời của mình.

| # | Chuyện gì đã xảy ra | Vì sao AI không bắt được | Kiểm ở đâu |
|---|---|---|---|
| **A** | Bảng *Predicted N/A by scenario* trong checklist liệt kê 14 item N/A cho scenario C. Nhưng vòng audit v1.8 và v1.9 (cũng do AI làm) thêm 7 item mới cho scenario B và D mà **không cập nhật lại bảng dự đoán phụ thuộc vào nó**. | AI xử lý mỗi vòng audit như một tác vụ độc lập: "thêm item còn thiếu". Nó không hỏi *"việc thêm item làm bảng nào khác trong file này sai đi?"*. Đây là lỗi thiếu **truy vết phụ thuộc**, không phải lỗi kiến thức — và nó xảy ra vì mỗi vòng được prompt riêng lẻ. | `Shared_GUI_Checklist.md` §Predicted N/A so với §Checklist changelog v1.8/v1.9 |
| **B** | Các planning document trong `hw3/docs/` mang giả định từ HW2 sang: `manual-pilot-strategy.md` bảo *"thiết kế một mini-checklist 10 item"* trong khi Task 1A đã xong 60 item; `architecture.md` ghi URL ngrok đã chết. | AI suy diễn cấu trúc bài mới từ workflow bài cũ, vì repo tái sử dụng và HW2 là ngữ cảnh gần nhất nó thấy. Nó đọc `hw2-summary.md` như một nguồn yêu cầu chứ không phải nguồn tham khảo quy trình. | So `manual-pilot-strategy.md` (bản git trước) với §6 Task 1 của đề |
| **C** | _(Điền chuyện xảy ra trong lúc bạn chạy Task 1B/2/3 — đây là ứng viên tốt nhất, vì nó xảy ra khi bạn đang trực tiếp làm.)_ | | |

> **Nên ưu tiên C.** Một sai lầm bạn tự bắt được trong lúc execute có sức thuyết phục hơn một sai lầm được kể lại. A và B là dự phòng nếu đến cuối kỳ không có chuyện nào đủ rõ.

---

## Nguyên tắc — chọn một cho đoạn 3

Đừng dùng lại nguyên văn nguyên tắc của HW2 (*"verify scope first, treat the specification as final authority"*) trừ khi HW3 thật sự tái diễn đúng lỗi đó. Vài hướng phù hợp hơn với bài GUI/Usability:

- **AI suy luận từ mô tả, không từ quan sát.** Nó có thể nói một widget *nên* hành xử thế nào, nhưng không nói được nó *đang* hành xử thế nào. Mọi phán quyết Pass/Fail phải đến từ màn hình thật.
- **Một câu trả lời viết đẹp không có nghĩa là đúng câu hỏi.** (Nguyên tắc của HW2 — chỉ dùng lại nếu tái diễn thật.)
- **Sửa cục bộ, hỏng toàn cục.** AI thêm đúng thứ được yêu cầu nhưng không tự hỏi thứ vừa thêm làm phần nào khác của tài liệu sai đi. Chính là ứng viên A.
- **AI thiên về happy path.** Checklist v1.0 do AI sinh có 12 item IA-04 về thành công và **không có item nào** về thất bại — vì nó được neo vào screenshot, mà không ai chụp màn hình lỗi 500. Con người phải chủ động đi hỏi "khi hỏng thì sao".

---

## Bản nháp

_(Viết ở đây. Đếm từ trước khi chuyển sang `hw3/out/ai-critique.md`.)_

**Số từ:** ___ / 200–300

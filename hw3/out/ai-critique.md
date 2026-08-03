# AI Critique — HW03

**Trạng thái: chưa viết.** §11 yêu cầu một đoạn 200–300 từ phản ánh trải nghiệm hợp tác với AI **trên toàn bộ assignment**. Tại thời điểm này, Task 2 (User Testing), Task 3 (Cross-Platform) và §8 (Agent Skills) chưa hoàn thành — chỉ dựa vào Task 1B thì critique sẽ không phản ánh đúng và đủ quá trình thật, nên cố tình chưa viết thay vì viết non rồi sửa lại.

Đoạn 200–300 từ thật sẽ được viết **sau khi Task 2, Task 3 và Agent Skills xong**, chọn đúng 1 sự cố kể sâu (không liệt kê nhiều sự cố hời hợt), theo cấu trúc: (1) AI sai cụ thể ở đâu và phát hiện ra bằng cách nào, (2) quy trình đổi thế nào sau đó, (3) nguyên tắc rút ra được.

## Cần quan sát trong lúc làm Task 2 (User Testing)

- AI có tự tin diễn giải phản ứng/lời nói của người tham gia thay vì trích dẫn nguyên văn không?
- Khi phân tích SUS/UEQ-S, AI có gộp nhầm một lỗi cá biệt của 1 người dùng thành vấn đề hệ thống không?
- AI có phân biệt được "hesitation" thật với việc người dùng đang đọc kỹ không?
- Có phát sinh trường hợp AI gợi ý mức severity cho một usability finding mà không có đủ bằng chứng từ nhiều session không?

## Cần quan sát trong lúc làm Task 3 (Cross-Platform)

- AI có nhầm lỗi do công cụ giả lập (BrowserStack/LambdaTest) với lỗi thật của EMS không?
- Khi một cell Fail, AI có phân biệt được overflow do CSS chưa responsive với overflow do chính device/browser render khác không?
- AI có bỏ sót việc chụp overlay email MSSV ở một số cell không?

## Cần quan sát trong lúc làm Agent Skills

- Khi viết SKILL.md, AI có tự đưa thêm bước không có trong quy trình thật đã chạy (bịa quy trình "lý tưởng" thay vì ghi lại quy trình đã dùng) không?
- Video demo có khớp đúng với các bước SKILL.md mô tả không, hay AI mô tả một quy trình khác với quy trình quay video?

## Nguyên liệu đã có sẵn từ Task 1B

Task 1B đã phát sinh ít nhất 5 sự cố AI-sai đủ rõ để làm ứng viên (đọc số quá sớm khi UI còn debounce, bỏ sót giá trị tồn tại trong DOM nhưng không hiện trên UI, phép đo tự nhiễm, sửa cục bộ làm hỏng một giả định ở chỗ khác, lỗi đếm kế thừa không tự lộ ra). Toàn bộ đã được ghi chi tiết ở `ai-audit.md` (Mục 3, Artifact #6/#8/#9/#20/#22) và giữ nguyên liệu thô ở `hw3/work/ai-critique-candidates.md` — **không phải bản nộp**, chỉ để tham khảo khi viết bản thật.

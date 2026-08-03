# AI Critique — HW03

**Trạng thái: chưa viết đoạn cuối cùng.** §11 yêu cầu một đoạn 200–300 từ phản ánh trải nghiệm hợp tác với AI **trên toàn bộ assignment**. Task 3 (Cross-Platform) và §8 (Agent Skills) nay đã hoàn thành, đã có quan sát thật ghi lại bên dưới — nhưng **Task 2 (User Testing) vẫn chưa thực hiện**, nên đoạn 200–300 từ cuối cùng vẫn cố tình chưa viết, để tránh viết non rồi phải sửa lại khi Task 2 phát sinh thêm quan sát.

Đoạn 200–300 từ thật sẽ được viết **sau khi Task 2 xong**, chọn đúng 1 sự cố kể sâu trong số các ứng viên đã có (không liệt kê nhiều sự cố hời hợt), theo cấu trúc: (1) AI sai cụ thể ở đâu và phát hiện ra bằng cách nào, (2) quy trình đổi thế nào sau đó, (3) nguyên tắc rút ra được.

## Cần quan sát trong lúc làm Task 2 (User Testing)

- AI có tự tin diễn giải phản ứng/lời nói của người tham gia thay vì trích dẫn nguyên văn không?
- Khi phân tích SUS/UEQ-S, AI có gộp nhầm một lỗi cá biệt của 1 người dùng thành vấn đề hệ thống không?
- AI có phân biệt được "hesitation" thật với việc người dùng đang đọc kỹ không?
- Có phát sinh trường hợp AI gợi ý mức severity cho một usability finding mà không có đủ bằng chứng từ nhiều session không?

## Task 3 (Cross-Platform) — đã quan sát được (2026-08-03)

- **Không nhầm lỗi giả lập với lỗi thật:** cell Fail duy nhất (F-022, C1/sidebar không responsive trên phone) đến từ thiết bị vật lý (iPhone thật), không qua BrowserStack/LambdaTest — nên câu hỏi "có nhầm lỗi giả lập" không áp dụng cho finding này. Ngược lại, khi BrowserStack tự giới hạn phiên 1 phút, AI không cố "vượt qua" bằng giả lập DevTools mà báo cáo đúng là Blocked/Not Executed.
- **Có phân biệt được layout defect với biến động khác của hệ thống:** ở Run B, tổng số user tăng 131→132 giữa phiên (dữ liệu EMS biến động theo §4) — AI ghi nhận đây là biến động dữ liệu bình thường, không map nhầm thành bug UI.
- **Một lỗi thật đã xảy ra, nhưng không phải loại câu hỏi đặt ra ban đầu:** AI tự báo cáo sai số liệu tổng hợp ("24 Executed/23 Pass" thay vì đúng "20/19/1/8") giữa phiên làm việc — đây là lỗi báo cáo/cộng nhẩm, không phải lỗi phân loại overflow. Bị phát hiện khi người dùng đọc lại tóm tắt và thấy 24+8≠28. Xem AI Audit Artifact #28.
- **Overlay email MSSV:** không bị bỏ sót ở cell nào trong 20 cell Executed — xác nhận lại bằng cách mở từng ảnh evidence khi soạn report, không chỉ tin lời mô tả.

## Agent Skills — đã quan sát được (2026-08-03)

- **AI không bịa quy trình "lý tưởng":** cả hai `SKILL.md` được viết từ đúng quy trình đã chạy thật (Coverage Fallback Strategy, No-DOM Policy, actor model, pipeline raw→candidate→final) — không thêm bước nào chưa từng xảy ra trong quá trình thực thi Task 3.
- **Video demo khớp với SKILL.md:** cả hai skill được chạy thật (không diễn lại) trong phiên video, kết quả (20/19/1/8) khớp với nguồn sự thật đã chốt trước khi quay — không có chỗ nào mô tả một quy trình khác với quy trình được quay.
- **Phát hiện đáng chú ý nhất:** khi tự chạy `compat-run-planner` lần đầu để đối soát, chính skill phát hiện ra 1 ảnh evidence (C1/Run A, primary) đã được duyệt từ trước nhưng chưa từng được promote sang `hw3/out/` — một khoảng trống quy trình mà việc chỉ đọc lại văn bản báo cáo sẽ không lộ ra. Đây là ứng viên mạnh cho đoạn 200–300 từ cuối cùng (xem AI Audit Artifact #26), vì nó cho thấy giá trị của việc bắt AI tự đối chiếu với dữ liệu trên đĩa thay vì tin vào tóm tắt bằng lời.

## Nguyên liệu đã có sẵn từ Task 1B

Task 1B đã phát sinh ít nhất 5 sự cố AI-sai đủ rõ để làm ứng viên (đọc số quá sớm khi UI còn debounce, bỏ sót giá trị tồn tại trong DOM nhưng không hiện trên UI, phép đo tự nhiễm, sửa cục bộ làm hỏng một giả định ở chỗ khác, lỗi đếm kế thừa không tự lộ ra). Toàn bộ đã được ghi chi tiết ở `ai-audit.md` (Mục 3, Artifact #6/#8/#9/#20/#22) và giữ nguyên liệu thô ở `hw3/work/ai-critique-candidates.md` — **không phải bản nộp**, chỉ để tham khảo khi viết bản thật.

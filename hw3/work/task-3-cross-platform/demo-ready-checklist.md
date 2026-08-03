# Demo-Ready Checklist

Dùng ngay trước khi quay — không cần đọc lại implementation plan.

1. [ ] Bật screen recorder.
2. [ ] Mở một chat Claude **mới** (không dùng lại chat này).
3. [ ] Dán nguyên văn nội dung `demo-launch-prompt.md` vào chat mới.
4. [ ] Để Claude tự đọc file và chuẩn bị (không cần làm gì thêm).
5. [ ] Bấm **Approve** ở checkpoint bắt đầu quay.
6. [ ] Bấm **Approve** ở từng checkpoint tiếp theo khi Claude đề xuất (sau
   Skill 1, sau Skill 2, khi kết thúc).
7. [ ] Nếu Claude báo phát hiện lệch số liệu (discrepancy) — đọc bảng
   expected vs actual, bấm **Approve** cho đề xuất sửa nếu đồng ý, rồi để
   Claude tự tiếp tục.
8. [ ] Dừng quay khi Claude báo "Demo complete — Approve to stop recording"
   và bạn đã bấm Approve.
9. [ ] Báo lại cho Claude trong cùng chat rằng đã dừng quay (để Claude cập
   nhật `demo-state.md` / `demo-run-log.md` / `demo-output-summary.md`).
10. [ ] Upload video, lấy URL, gửi URL đó cho Claude trong cùng chat (Claude
    sẽ ghi vào `demo-video-links-draft.md`, chưa promote sang `hw3/out/`).

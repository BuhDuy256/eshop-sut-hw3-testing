# Demo State — Phase Markers

Cập nhật real-time bởi Claude trong phiên demo thật (chat mới). Trạng thái
dưới đây phản ánh lần chuẩn bị gần nhất (dry run, chat hiện tại) — phiên
demo thật sẽ ghi đè các dòng "Video" bên dưới khi thực sự quay.

| Giai đoạn | Dry run (chat chuẩn bị) | Video thật (chat demo mới) |
|---|---|---|
| Pre-demo setup | ✅ Hoàn tất | ✅ Hoàn tất — đã đọc lại plan, workspace state, 2 SKILL.md, `skill-validation.md`, và re-verify trực tiếp trên manifest/evidence/run-log thật (không dùng lại số cache từ dry run) |
| Start checkpoint | N/A (dry run không cần Approve) | ✅ Approved (2026-08-03) |
| Demo Skill 1 (`compat-run-planner`) | ✅ Đã chạy thật, xem `dry-run-result.md` | ✅ Đã chạy thật, 20/19/1/8, OS 2/3, Browser 5/5, Device 2/3, missing=0, mismatch=0 |
| Validation checkpoint 1 | ✅ Khớp nguồn sự thật | ✅ Khớp nguồn sự thật — Approved (2026-08-03) |
| Demo Skill 2 (`compat-evidence-report`) | ✅ Đã chạy thật, xem `dry-run-result.md` | ✅ Đã chạy thật, `report-draft.md` refresh xong, đủ 12 mục, backup tại `report-draft.backup-pre-video.md` |
| Validation checkpoint 2 | ✅ Khớp yêu cầu | ✅ Khớp yêu cầu — Approved (2026-08-03) |
| Final summary | N/A (dry run không quay) | ✅ Đã trình bày — 20 Executed / 19 Pass / 1 Fail / 8 Blocked, không có promotion nào |
| End checkpoint | N/A | ✅ Approved (2026-08-03) |
| Post-demo artifact update | N/A | ✅ Hoàn tất — cập nhật `demo-state.md`, `demo-run-log.md`, `demo-output-summary.md` |

**Lưu ý:** dòng "Video thật" chỉ được Claude trong chat demo mới cập nhật —
chat chuẩn bị hiện tại không quay video, không tự đánh dấu các dòng đó là
hoàn tất.

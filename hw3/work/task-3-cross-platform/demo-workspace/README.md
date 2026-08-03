# Demo Workspace — Agent Skills Demo (Task 3)

Hỗ trợ phiên demo video riêng cho `compat-run-planner` và
`compat-evidence-report`. Không phải artifact nộp bài — chỉ hỗ trợ điều phối
và ghi log cho phiên quay.

## Input (chỉ đọc trong demo, không sửa trừ khi có discrepancy đã Approve)

- `../compatibility-manifest-working.md`
- `../execution-logs/run-log-{A,B,C,G,F}.md`
- `../raw-evidence/`, `../annotated-candidates/`
- `hw3/out/reports/task-3-cross-platform/evidence/` (final, chỉ đọc — demo
  không promote thêm gì vào đây)
- `../setup-evidence/browserstack-1min-trial-limit-banner.jpg`
- `../findings-drafts/F-022-draft.md`
- `hw3/work/findings-log.md`
- `../skill-validation.md` (kết quả validation trước đó — dùng làm baseline
  so sánh, không phải nguồn phải chạy lại từ đầu)

## Output (demo tạo/cập nhật trong phiên)

- `../report-draft.md` — Skill 2 sẽ refresh file này (ghi đè cùng path, có
  backup trước khi ghi — xem `report-draft.backup-<timestamp>.md` trong thư
  mục này nếu được tạo).
- `demo-state.md` — trạng thái từng giai đoạn (chưa bắt đầu / đang chạy /
  hoàn tất), cập nhật real-time trong phiên demo thật.
- `demo-run-log.md` — nhật ký các bước đã chạy thật trong phiên demo (khác
  với run log Task 3 gốc — đây là log riêng cho phiên quay).
- `demo-output-summary.md` — số liệu output cuối cùng của cả 2 skill, để đối
  chiếu với Mục 2 (nguồn sự thật) trong
  `../demo-skill-implementation-plan.md`.
- `dry-run-result.md` — kết quả dry run (không quay) thực hiện trước khi tạo
  launch prompt.

## Ràng buộc

- Không copy hay tạo bản trùng evidence image không cần thiết.
- Không ghi gì vào `hw3/out/` từ thư mục này hay từ phiên demo.
- Nếu `report-draft.md` được refresh, luôn backup bản cũ trước khi ghi đè.

# Demo Run Log

Nhật ký các bước thực sự chạy trong phiên demo. Phần "Dry run" dưới đây được
ghi bởi chat chuẩn bị (không quay video). Chat demo mới sẽ nối tiếp bằng
mục "Video thật".

## Dry run (2026-08-03, chat chuẩn bị — không quay video)

Xem chi tiết đầy đủ ở `dry-run-result.md`. Tóm tắt các bước đã chạy thật:

1. Đọc `compatibility-manifest-working.md`, cả 5 run log, `skill-validation.md`.
2. Invoke `compat-run-planner` thật trên dữ liệu Task 3 hiện tại.
3. So kết quả với nguồn sự thật (20/19/1/8, OS 2/3, Browser 5/5, Device 2/3,
   missing=0, mismatch=0) — khớp.
4. Invoke `compat-evidence-report` thật, refresh `report-draft.md` (đã backup
   bản trước khi ghi đè).
5. Xác nhận report draft giữ đủ 12 mục, không dùng số 24/23, không gọi
   Blocked là Fail.
6. Xác nhận không có ghi/promote nào vào `hw3/out/`.

## Video thật (2026-08-03, chat demo mới)

1. Đọc `demo-skill-implementation-plan.md`, `demo-workspace/README.md`,
   `demo-state.md`, `demo-run-log.md`, `demo-output-summary.md`,
   `dry-run-result.md`, cả 2 `SKILL.md`, `skill-validation.md`.
2. Re-verify trực tiếp trên `compatibility-manifest-working.md` thật (không
   dùng lại số cache của dry run): 28 dòng manifest, Executed section ghi rõ
   "20 cell" (5 run × 4 screen), Blocked section ghi rõ "8 cell" (2 run × 4
   screen), bảng "Kết quả cuối" ghi 19 Pass / 1 Fail (C1/Run F/iOS/Safari/
   Phone, F-022, severity 2), "Coverage check" ghi OS 2/3, Browser 5/5,
   Device 2/3, C3 Full Confirm ghi rõ là field upgrade trên C3/Run A, không
   phải cell mới.
3. Đếm trực tiếp file evidence final trên đĩa: 25 file (C1: 8, C2: 6, C3: 6,
   C4: 5) = 20 primary + 5 supplementary — khớp missing artifacts = 0.
4. Xác nhận cả 5 run log (A/B/C/F/G) và cả 2 SKILL.md tồn tại, đọc được.
5. Không phát hiện discrepancy nào — khớp hoàn toàn nguồn sự thật ở Mục 2
   của implementation plan. Không kích hoạt nhánh Failure/recovery.
6. Pre-demo setup hoàn tất → trình bày Start checkpoint, chờ Approve.
7. **Start checkpoint Approved.** Invoke `compat-run-planner` thật (qua
   `Skill(compat-run-planner)`) trên `compatibility-manifest-working.md`,
   `raw-evidence/`, `annotated-candidates/`, final evidence, cả 5 run log,
   `findings-log.md`. Kết quả: 20 Executed / 19 Pass / 1 Fail (C1/Run F,
   F-022, severity 2) / 8 Blocked, OS 2/3, Browser 5/5, Device 2/3, missing
   artifacts = 0, file-name mismatch = 0, C3 Full Confirm xác nhận là field
   upgrade không phải cell mới, F-019/F-020 vẫn unresolved.
8. **Validation checkpoint 1:** so kết quả Skill 1 với nguồn sự thật — khớp
   hoàn toàn, không có discrepancy. User Approve, sang Part 2.
9. Invoke `compat-evidence-report` thật (qua `Skill(compat-evidence-report)`).
   Backup bản `report-draft.md` trước khi ghi đè, lưu tại
   `demo-workspace/report-draft.backup-pre-video.md`. Refresh
   `hw3/work/task-3-cross-platform/report-draft.md` với đủ 12 mục. Grep xác
   nhận: không có "24 Executed"/"23 Pass"/"28 cells tested" trong file; xác
   nhận `hw3/out/reports/task-3-cross-platform/` không có file nào bị tạo/sửa
   (chỉ còn `evidence/`, không có `report.md` hay `compatibility-matrix.md`).
10. **Validation checkpoint 2:** report draft khớp yêu cầu — 12 mục đúng thứ
    tự, tách đúng Executed/Blocked/Requirement gap, không gọi Blocked là
    Fail, output chỉ nằm trong `hw3/work/`. User Approve.
11. **Final summary** trình bày trên khung hình: 2 skill đã chạy thật, số
    liệu 20/19/1/8 khớp nguồn sự thật, xác nhận không có promotion nào vào
    `hw3/out/` trong suốt phiên.
12. **End checkpoint Approved** — dừng quay. Không phát sinh discrepancy nào
    trong suốt phiên video thật; nhánh Failure/recovery không được kích
    hoạt.

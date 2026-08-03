# Dry Run Result — Agent Skills Demo (2026-08-03, chat chuẩn bị, không quay video)

Mục đích: xác nhận cả 2 skill chạy end-to-end thật trên dữ liệu Task 3 hiện
tại, trước khi soạn `demo-launch-prompt.md`. Không quay video ở bước này.

---

## 1. Backup trước khi refresh report draft

`report-draft.md` gốc đã được backup vào
`demo-workspace/report-draft.backup-pre-dryrun.md` trước khi invoke Skill 2.
Không mất bản trước.

## 2. Invoke Skill 1 (`compat-run-planner`)

**Kết quả:**

| Chỉ số | Giá trị |
|---|---|
| Executed | **20** |
| Pass | **19** |
| Fail | **1** — C1 / Run F / iOS / Safari / Phone, Finding F-022, severity 2 |
| Blocked | **8** |
| OS coverage (Executed) | 2/3 (Windows, iOS — thiếu macOS) |
| Browser coverage (Executed) | 5/5 (Chrome, Firefox, Opera, Edge, Safari) |
| Device coverage (Executed) | 2/3 (Desktop, Phone — thiếu Tablet) |
| Missing artifacts | **0** |
| File-name mismatch | **0** |
| C3 Full Confirm | Xác nhận là supplementary field upgrade trên C3/Run A, không phải cell mới |
| F-019/F-020 | Vẫn báo cáo là unresolved historical IDs — không bị skill tự map |

**Khớp nguồn sự thật ở `demo-skill-implementation-plan.md` Mục 2:** ✅ Có.

## 3. Invoke Skill 2 (`compat-evidence-report`)

**Kết quả:** `report-draft.md` được refresh (ghi đè cùng path, backup đã có
sẵn ở bước 1). Đã xác nhận bằng grep trực tiếp sau khi ghi:

- Không xuất hiện "24 Executed", "23 Pass" ở bất kỳ đâu trong file.
- Đủ 12 mục header đúng thứ tự (Scope and methodology → AI-use summary).
- Không có file nào trong `hw3/out/reports/task-3-cross-platform/` bị ghi/
  thay đổi trong suốt quá trình dry run (kiểm bằng so sánh mtime).

**Khớp yêu cầu:** ✅ Có — report tách đúng Executed/Blocked/Requirement gap,
không gọi Blocked là Fail, không đụng `hw3/out/`.

## 4. Xác nhận không có final promotion

- Không file nào trong `hw3/out/` bị tạo/sửa trong dry run này.
- 2 SKILL.md vẫn chỉ nằm ở `.claude/skills/` — chưa copy sang
  `hw3/out/agent-skills/`.
- `compatibility-matrix.md` và `report.md` (bản final) chưa được sinh.

## 5. Thời gian tương đối

Không đo bằng đồng hồ tuyệt đối (dry run chạy trong 1 phiên chat, không phải
môi trường quay). Quan sát tương đối: mỗi lần invoke skill mất một khoảng
thời gian xử lý ngắn, tương đương nhau giữa Skill 1 và Skill 2 — không có
bước nào bị treo hay cần nhiều vòng lặp sửa lỗi. Ước tính cho video thật
(dựa trên khối lượng output cần đọc to trên khung hình): Skill 1 ~60–90s để
invoke + đọc kết quả, Skill 2 ~60–90s tương tự — khớp với ngân sách 90–120s/
part đã đặt ở Mục 6 của implementation plan.

## 6. Điểm có thể phát sinh stop point trong video thật

- Ngay sau khi Skill 1 trả kết quả — điểm tự nhiên để dừng "chấp nhận kết
  quả validation" trước khi sang Part 2.
- Ngay sau khi Skill 2 ghi xong `report-draft.md` — điểm tự nhiên để dừng
  "chấp nhận kết quả validation" trước khi sang Final summary.
- Không phát sinh discrepancy nào trong dry run này — nên nhánh "Failure/
  recovery" (Mục 5 của implementation plan) không được kích hoạt lần này.
  Chat demo mới vẫn cần sẵn sàng cho nhánh đó nếu dữ liệu thay đổi giữa lúc
  dry run này và lúc quay thật.

## 7. Kết luận

Dry run **PASS** toàn bộ. Không cần sửa gì trước khi tạo launch prompt.

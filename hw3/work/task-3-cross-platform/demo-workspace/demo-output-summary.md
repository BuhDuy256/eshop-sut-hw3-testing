# Demo Output Summary

Số liệu output cuối cùng của cả 2 skill — dùng để đối chiếu nhanh với nguồn
sự thật (`../demo-skill-implementation-plan.md` Mục 2). Cập nhật sau mỗi lần
skill chạy thật (dry run hoặc video thật).

## Nguồn sự thật (không đổi)

```text
Manifest rows: 28
Executed: 20 (19 Pass, 1 Fail — F-022)
Blocked: 8
Coverage: OS 2/3, Browser 5/5, Device 2/3
Missing artifacts: 0
Filename mismatch: 0
C3 Full Confirm: supplementary field upgrade, không phải cell mới
```

## Lần chạy: Dry run (2026-08-03, chat chuẩn bị)

| Skill | Kết quả | Khớp nguồn sự thật? |
|---|---|---|
| `compat-run-planner` | 20 Executed / 19 Pass / 1 Fail / 8 Blocked / OS 2/3 / Browser 5/5 / Device 2/3 / missing=0 / mismatch=0 | ✅ Khớp |
| `compat-evidence-report` | `report-draft.md` refresh thành công, đủ 12 mục, không dùng 24/23, không đụng `hw3/out/` | ✅ Khớp |

## Lần chạy: Video thật (2026-08-03, chat demo mới)

| Skill | Kết quả | Khớp nguồn sự thật? |
|---|---|---|
| `compat-run-planner` | 20 Executed / 19 Pass / 1 Fail (C1/Run F/iOS/Safari/Phone, F-022, severity 2) / 8 Blocked / OS 2/3 / Browser 5/5 / Device 2/3 / missing=0 / mismatch=0 | ✅ Khớp |
| `compat-evidence-report` | `report-draft.md` refresh thành công (backup tại `report-draft.backup-pre-video.md`), đủ 12 mục đúng thứ tự, không dùng 24/23, không gọi Blocked là Fail, output chỉ ở `hw3/work/`, `hw3/out/` không bị đụng | ✅ Khớp |

**Không phát sinh discrepancy nào trong phiên video thật.** Cả 2 checkpoint
validation đều được Approve không cần correction. Không có promotion nào vào
`hw3/out/` trong suốt phiên (đã xác nhận bằng kiểm tra trực tiếp thư mục
`hw3/out/reports/task-3-cross-platform/` — chỉ còn `evidence/`).

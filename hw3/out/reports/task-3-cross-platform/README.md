# Task 3 — Cross-Browser / Cross-Platform Compatibility Testing

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Scenario:** C — Admin manages users (C1 Users list · C2 Edit User dialog ·
C3 Delete User confirm dialog · C4 Export to Excel)
**SUT:** EMS — https://prod-dev.ems-fitus.cloud/
**Ngày hoàn thành:** 2026-08-03

> Bản tổng hợp Task 3 để nộp. Chi tiết đầy đủ nằm trong `report.md`; ma trận
> coverage trong `compatibility-matrix.md`; ảnh trong `evidence/`; video demo
> 2 Agent Skill trong `demo-video-links.md`.

---

## Trạng thái

**Task 3 Execution Done (K1): hoàn tất.** Coverage Fallback Strategy đã
chạy đầy đủ, có evidence, có 2 Agent Skill được thiết kế + validate + demo.
Final Submission Integration (gộp cùng Task 1 + Task 2) **chưa thực hiện**
vì Task 2 (User Testing) chưa hoàn thành — xem `hw3/work/findings-log.md`
để biết trạng thái đối soát hiện tại.

## Số liệu chính

```text
Manifest rows: 28
Executed cells: 20 — 19 Pass, 1 Fail
Blocked cells: 8 (Not Executed, no verdict)
Supplementary validation: 1 (C3 Full Confirm Final Validation, Run A —
  field upgrade, không phải cell mới)
```

| Chỉ số | Giá trị |
| --- | --- |
| OS coverage (Executed) | 2/3 — Windows, iOS (thiếu macOS) |
| Browser coverage (Executed) | 5/5 — Chrome, Firefox, Opera, Edge, Safari |
| Device coverage (Executed) | 2/3 — Desktop, Phone (thiếu Tablet) |
| Finding phát sinh | **F-022** — sidebar không responsive trên phone viewport, severity 2 |

## Requirement gap (nói thẳng, không che giấu)

Đề bài yêu cầu 3 OS × 5 browser × 3 device class cho mỗi screen. Phần
Executed chỉ đạt 2/3 OS và 2/3 device class — **macOS desktop và tablet thật
chưa được thực thi**, vì BrowserStack Free Trial giới hạn cứng 1 phút/phiên
(xác nhận qua pilot thật, evidence tại `evidence/blocked/`). Đây là giới hạn
hạ tầng bên thứ ba, không phải lựa chọn né tránh — 8 cell tương ứng được ghi
`Blocked / Not Executed`, không gán Pass/Fail, không dùng DevTools giả lập
để lấp chỗ trống. Residual risk: hành vi thật của EMS trên macOS Safari và
tablet vẫn chưa biết. Chi tiết đầy đủ ở `report.md` §5 và
`compatibility-matrix.md`.

## Agent Skills (§8)

| Skill | Vai trò | Trạng thái |
| --- | --- | --- |
| `compat-run-planner` | Đối soát coverage manifest vs. evidence vs. run log | Validate PASS — ra đúng 20/19/1/8 trên dữ liệu thật |
| `compat-evidence-report` | Soạn/refresh report draft từ evidence đã review | Validate PASS — output đúng 12 mục, chỉ ghi vào `hw3/work/` |

Nguồn: `hw3/out/agent-skills/compat-run-planner/SKILL.md`,
`hw3/out/agent-skills/compat-evidence-report/SKILL.md`. Validation record đầy
đủ: `hw3/work/task-3-cross-platform/skill-validation.md`.

## Demo video

**URL:** https://youtu.be/GbhAEK7x8Vk — chi tiết ở `demo-video-links.md`
(đường dẫn được sinh viên cung cấp; chưa được AI mở lại để xác minh nội dung
video).

## Đường dẫn artifact chính

```text
hw3/out/reports/task-3-cross-platform/report.md
hw3/out/reports/task-3-cross-platform/compatibility-matrix.md
hw3/out/reports/task-3-cross-platform/demo-video-links.md
hw3/out/reports/task-3-cross-platform/evidence/
hw3/out/agent-skills/compat-run-planner/SKILL.md
hw3/out/agent-skills/compat-evidence-report/SKILL.md
```

Working material (không phải bản nộp): `hw3/work/task-3-cross-platform/`.

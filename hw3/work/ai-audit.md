# AI Audit Report — HW03 (GUI & Usability Testing on EMS)

> **Template gốc:** `[AI-02] - FIT@HCMUS - AI Audit Report_En.docx.md` — form chính thức của khoa, 6 mục. Giữ nguyên cấu trúc, chỉ đổi nội dung cho HW3.
> **Bản chốt sẽ nằm ở:** `hw3/out/ai-audit.md` (Step 13). File này là bản đang chạy.
> **§10 bắt buộc:** ghi **ngay tại thời điểm dùng AI** — tool · ngày giờ · prompt nguyên văn · output. Dựng lại từ trí nhớ vào cuối kỳ là bịa provenance, và §12 kiểm tra đúng chỗ đó.

*Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC13003 Software Testing course.*

---

## 1. Student Information

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | _(điền)_ |
| **Assignment ID:** | HW#03 — GUI & Usability Testing (EMS) |
| **Assignment date:** | _(điền)_ |
| **AI tool(s) used:** | _(vd: Claude Opus 5 qua Claude Code; Claude in Chrome)_ |
| **Did you use AI?** | [x] Yes  [ ] No |

---

## 2. Instructions (read before filling)

- Add one row per AI-generated artifact.
- Paste the **verbatim** prompt — DO NOT paraphrase.
- Paste the **verbatim** AI output (or include a labelled screenshot in the report).
- Tag the verdict: **VALID / INVALID / INCOMPLETE**.
- Reasoning must cite an authoritative source.
- Show the corrected artifact with the change highlighted.

> **Khác biệt so với HW2 — cột (4) Reasoning trích nguồn nào.**
> HW2 trích ISTQB §4.2/§4.3 vì đó là bài Domain Testing. HW3 là GUI/Usability, nên nguồn hợp lệ ở cột (4) là:
> - **Đề bài HW03** — §4 (định nghĩa IA-01…IA-04), §5 (scenario/screen), §6 (Task 1/2/3), §7, §12, §18
> - **Slide S13** — *GUI Testing & Usability Testing* (ghi số trang)
> - **Heuristic đã cite trong checklist** — Nielsen H1–H10, Norman P1–P6, Shneiderman R1–R8
> - **WCAG 2.1** — ghi số Success Criterion (vd SC 1.4.3)
> - **ISTQB FL** — vẫn dùng được cho phần nguyên tắc chung (test technique, defect reporting)
>
> Không được trích source code EMS làm căn cứ — không có source code, và §12 coi bằng chứng phải đến từ thực thi.

**Artifact nào của HW3 cần audit** (mỗi cái ít nhất một dòng, nếu có dùng AI):

| Artifact | Thuộc bước |
|---|---|
| Item checklist do AI sinh / audit round | Task 1A (group) |
| Phân loại Applicable / N/A | Task 1B |
| Bug report viết từ item Fail | Task 1B |
| Chấm severity | Task 1B |
| Task scenario cho user testing | Task 2 Phase 1 |
| Phân tích SUS/UEQ-S, gom pain point, xếp severity 0–4 | Task 2 Phase 3 |
| Thiết kế compatibility matrix | Task 3 |
| Phân tích screenshot cross-platform | Task 3 |
| Agent Skill (SKILL.md) | §8 |
| Planning document, runbook | Chuẩn bị |

---

## 3. Audit Table — one row per artifact

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (nguồn) | (5) Student Fix |
|---|---|---|---|---|
| **Artifact #1 — _(tên artifact)_** | | | | |
| Tool: _(vd Claude Opus 5 / Claude Code)_<br>Time: _(yyyy-mm-dd hh:mm)_<br>Step: _(bước trong runbook, vd Step 4.2)_<br>Prompt: *"_(dán nguyên văn)_"* | _(dán nguyên văn, hoặc tóm tắt trung thực + trỏ tới screenshot có nhãn)_ | VALID / INVALID / INCOMPLETE | _(trích đề bài §, slide S13 p., Nielsen H, Norman P, Shneiderman R, WCAG SC)_ | _(sửa gì, nêu rõ phần bạn tự viết)_ |

### Ví dụ minh hoạ cách điền (thay bằng dữ liệu thật trước khi nộp)

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning | (5) Student Fix |
|---|---|---|---|---|
| Tool: Claude Opus 5<br>Time: 2026-08-02 15:40<br>Step: Step 2.2<br>Prompt: *"Với scenario C (admin quản lý user), item nào trong checklist 60 item sẽ là N/A?"* | Liệt kê 14 item N/A dựa trên bảng *Predicted N/A by scenario* của checklist. | INCOMPLETE | Bảng *Predicted N/A* được viết ở v1.6; v1.8 và v1.9 thêm 7 item viết riêng cho scenario B và D (IA02-15, IA03-14, IA03-15, IA04-07, IA04-14, IA04-15, IA04-16) mà bảng không cập nhật. Checklist §*Predicted N/A* cũng tự ghi rõ đây là *"predictions to plan with, not results"* — không được dùng thay cho việc tự kiểm. | Bổ sung 7 item vào danh sách dự đoán (≈21 thay vì 14), và **vẫn tự mở từng màn hình xác nhận** trước khi điền N/A. Ghi lý do một dòng cho từng N/A trong file execution. |

---

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
|---|---|---|
| **Total AI-generated artifacts audited** | | |
| **VALID (correct, accepted as-is)** | | % |
| **INVALID (wrong; rejected)** | | % |
| **INCOMPLETE (acceptable after edits)** | | % |

**Phân tách theo task** (thêm so với HW2 — HW3 có 3 task khác nhau về bản chất, gộp chung sẽ giấu mất chỗ AI yếu):

| Task | Total | VALID | INVALID | INCOMPLETE |
|---|---|---|---|---|
| Task 1 — Checklist execution & bug report | | | | |
| Task 2 — User testing design & analysis | | | | |
| Task 3 — Cross-platform | | | | |
| §8 — Agent Skills | | | | |

---

## 5. Conclusion — When should AI be used (or not)?

Viết **80–150 từ**: AI mạnh ở đâu, hỏng ở đâu, khuyến nghị cho lần sau.

**Điểm neo dành riêng cho HW3** (khác HW2 — nêu ra để bài không viết chung chung):

- AI **không thể** chạy thay bạn: quan sát màn hình thật, chấm Pass/Fail cho một item mang tính chủ quan, chụp screenshot, ngồi cùng 5 người dùng thật, bấm BrowserStack.
- AI **có thể**: định dạng bug report từ ghi chép rời, gợi ý gom finding trùng nguyên nhân, tính điểm SUS, kiểm tra ma trận compatibility đã phủ đủ mọi OS/browser/device chưa.
- §12 (Anti-AI-Cheat) liệt kê đúng ba thứ AI không được đụng vào: bằng chứng thực thi, ảnh cross-platform, và 5 người tham gia. Kết luận nên nói được vì sao ranh giới đó nằm đúng chỗ.

*(Viết kết luận ở đây.)*

---

## 6. Mandatory Disclosure (paste verbatim)

> "[Test cases / script / dataset / report] was initially generated by [AI tool name]; I reviewed and modified [section X], added [edge cases Y, Z]; [section W] was written entirely by me. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."

> **Cách điền cho HW3 — phải nêu đích danh phần AI không đụng vào**, vì §12 kiểm tra chính những phần đó: bằng chứng thực thi checklist, ảnh cross-platform, và dữ liệu 5 người tham gia user testing.

### Signature

| Field | Value |
|---|---|
| **Student name (printed):** | Nguyễn Bảo Duy |
| **Student ID:** | 23127179 |
| **Class / Cohort:** | _(điền)_ |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Instructor:** | _(điền)_ |
| **Date:** | _(điền)_ |
| **Signature:** | |

---

## References

- Kharbach, M. (2026). *AI Use Policy Templates for Higher Education.* CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Nielsen, J. *10 Usability Heuristics for User Interface Design.*
- Norman, D. *The Design of Everyday Things* (6 principles).
- Shneiderman, B. *Eight Golden Rules of Interface Design.*
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.1.*
- Course slides S13: *GUI + Usability + Compatibility Testing (AI-First, Combined).*
- Hardman, P. (2025). *A Post-AI Learning Taxonomy.*

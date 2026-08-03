# Demo Implementation Plan — Agent Skills (`compat-run-planner`, `compat-evidence-report`)

**Trạng thái:** Working plan. Không phải kịch bản quay — là bản thiết kế
luồng + nguyên tắc điều phối cho một phiên chat Claude riêng sẽ thực sự quay
video. Chat hiện tại **không** quay demo.

---

## 1. Mục tiêu demo

Một video ngắn chứng minh hai Agent Skill được dùng thật trên artifact Task 3
đã tồn tại — không phải diễn lại hay giả lập:

- **Skill 1 (`compat-run-planner`)** đọc manifest + evidence folders + run
  logs, đưa ra coverage reconciliation thật (không đoán, không tính lại bằng
  trí nhớ).
- **Skill 2 (`compat-evidence-report`)** kiểm evidence đã review và sinh/làm
  mới `report-draft.md`.
- Demo **không** chạy lại UI test trên EMS (không mở lại BrowserStack, không
  chụp ảnh mới, không thao tác trình duyệt).
- Demo **không** thay đổi bất kỳ verdict nào (Pass/Fail/Blocked giữ nguyên
  như đã đóng băng ở `skill-validation.md`).
- Demo **không** fabricate evidence — mọi con số đọc trực tiếp từ file thật.
- Demo **không** promote artifact final (`hw3/out/`) nếu chưa có approval
  riêng cho hành động promote đó — và theo phạm vi phiên demo này, sẽ không
  promote gì cả (xem Mục F của yêu cầu gốc).

---

## 2. Phạm vi demo — nguồn sự thật (không đổi trong suốt demo)

```text
Manifest rows: 28
Executed: 20 (19 Pass, 1 Fail — C1/Run F/iOS/Safari/Phone, Finding F-022, severity 2)
Blocked: 8 (Run D macOS Safari Desktop ×4 screen, Run E iOS Tablet ×4 screen)
Supplementary: C3 Full Confirm Final Validation (Run A) — field upgrade, KHÔNG phải cell mới
Coverage: OS 2/3, Browser 5/5, Device 2/3
Missing artifacts: 0 (đã sửa ở phiên trước — C1/Run A primary evidence đã promote)
Filename mismatch: 0
```

Nếu demo (dry run hoặc video thật) ra số khác các số này, đó là discrepancy
cần dừng lại xử lý theo Mục 5 — không tự động coi số mới là "cập nhật đúng
hơn" mà không đối chiếu.

---

## 3. Luồng demo dự kiến

| Giai đoạn | Nội dung | Loại |
|---|---|---|
| Pre-demo setup | Chat mới tự đọc plan, workspace state, 2 SKILL.md, `skill-validation.md` — không hỏi người dùng bất kỳ điều đã có sẵn trong repo | Tự động, không cần approval |
| Start checkpoint | Claude báo đã sẵn sàng, đề xuất "bắt đầu quay Part 1" | **Dừng — chờ Approve** |
| Demo Skill 1 | Invoke `compat-run-planner` trên dữ liệu thật, hiển thị output (per-row status, coverage, missing/mismatch = 0) | Tự động sau khi Approve |
| Validation checkpoint | Claude tự so số ra được với Mục 2 (nguồn sự thật) — nếu khớp, đề xuất "xác nhận Skill 1 đúng, sang Part 2" | **Dừng — chờ Approve** (hoặc rẽ sang Mục 5 nếu lệch) |
| Demo Skill 2 | Invoke `compat-evidence-report`, sinh/refresh `report-draft.md`, hiển thị 12 mục + xác nhận output vẫn ở `hw3/work/` | Tự động sau khi Approve |
| Validation checkpoint | Claude tự kiểm report draft tách đúng Executed/Blocked/Requirement gap, không gọi Blocked là Fail, không dùng 24/23 | **Dừng — chờ Approve** (hoặc rẽ sang Mục 5 nếu lệch) |
| Final summary | Claude tóm tắt trong khung hình: 2 skill đã chạy thật, số liệu khớp nguồn sự thật, không có promotion nào xảy ra | Tự động |
| End checkpoint | Claude đề xuất "kết thúc quay" | **Dừng — chờ Approve** |
| Post-demo artifact update | Cập nhật `demo-state.md`, `demo-run-log.md`, `demo-output-summary.md` trong workspace; chờ người dùng cung cấp video URL riêng (không thuộc phiên demo này) | Tự động, không cần approval (không đụng `hw3/out/`) |

---

## 4. Human-in-the-loop strategy (nguyên tắc, không hard-code từng câu)

Chat demo mới tự quyết định khi nào cần dừng, dựa trên nguyên tắc sau — đây
là nguyên tắc, không phải danh sách câu thoại cố định:

- **Tự chạy không cần hỏi:** mọi thao tác read-only (đọc file, list thư
  mục), navigation, mở file để kiểm tra, invoke skill, sinh working draft.
- **Chỉ dừng tại 4 điểm:**
  1. Trước khi bắt đầu quay (start checkpoint).
  2. Sau khi có kết quả validation của mỗi skill (chấp nhận kết quả).
  3. Trước khi áp dụng một correction nếu phát hiện discrepancy.
  4. Khi kết thúc demo (end checkpoint) — và trước bất kỳ final promotion
     nào nếu có (phiên demo này không có promotion nào theo kế hoạch).
- **Tại mỗi stop point:** Claude đã tự chuẩn bị sẵn một action proposal cụ
  thể (không phải câu hỏi mở) — người dùng chỉ cần phản hồi "Approve".
- **Sau Approve:** tự tiếp tục ngay, không hỏi lại, không yêu cầu nhập thêm
  thông tin đã có sẵn.
- **Không đưa menu dài** trừ khi gặp lỗi thật không tự giải quyết được (ví
  dụ: file bị thiếu ngoài dự kiến).
- **Không hỏi câu mở** kiểu "Bạn muốn làm gì tiếp?" — mọi checkpoint đều đi
  kèm đúng một đề xuất hành động rõ ràng.

---

## 5. Failure / recovery strategy

Nếu tại bất kỳ điểm nào (dry run hoặc video thật) skill trả về số liệu khác
Mục 2:

1. **Dừng ngay** — không tiếp tục demo với số sai.
2. **Hiển thị expected vs actual** — dạng bảng ngắn, không dài dòng.
3. **Đề xuất đúng một correction cụ thể** — ví dụ "promote file X đang thiếu"
   hoặc "sửa dòng Y trong manifest" — không đưa nhiều phương án.
4. **Chờ Approve** cho correction đó.
5. **Sau Approve:** tự sửa **trong `hw3/work/` mà thôi** — không bao giờ sửa
   trực tiếp `hw3/out/` trong lúc demo.
6. **Re-run đúng phần bị lỗi** (không re-run toàn bộ demo từ đầu).
7. **Tiếp tục demo** từ điểm dừng.

**Không sửa final artifact trong `hw3/out/`** trong suốt phiên demo, kể cả
khi discrepancy liên quan đến file đã promote trước đó — nếu phát hiện vấn
đề ở `hw3/out/`, ghi nhận lại và báo cho người dùng xử lý ngoài phiên demo,
không tự sửa.

---

## 6. Video structure

Một video duy nhất, khoảng 3–5 phút:

1. **Intro** (~15–20s) — mục tiêu demo, 2 skill sẽ chạy.
2. **Part 1 — `compat-run-planner`** (~90–120s) — invoke, hiển thị output,
   validation checkpoint.
3. **Part 2 — `compat-evidence-report`** (~90–120s) — invoke, hiển thị
   `report-draft.md` được sinh/refresh, validation checkpoint.
4. **Final summary** (~15–20s) — tóm tắt số liệu, xác nhận không có
   promotion.

Không mở toàn bộ 28 dòng manifest hay từng ảnh evidence riêng lẻ trên
khung hình — chỉ hiển thị output tổng hợp của skill.

---

## 7. Demo output — tối thiểu phải thấy được trên khung hình

### Skill 1 (`compat-run-planner`)
- 28 manifest rows (tổng, không cần liệt kê từng dòng)
- 20 Executed / 19 Pass / 1 Fail / 8 Blocked
- OS 2/3, Browser 5/5, Device 2/3
- Missing artifacts = 0
- Filename mismatch = 0
- Xác nhận rõ: C3 Full Confirm không phải cell mới

### Skill 2 (`compat-evidence-report`)
- Xác nhận skill đọc reviewed manifest, run logs, evidence
- Xác nhận sinh/refresh đúng path: `hw3/work/task-3-cross-platform/report-draft.md`
- Report giữ đủ 12 mục: Executed, Pass/Fail, Blocked, Requirement gap, F-022,
  C3 Interaction Coverage, Actual Execution Mode, Evidence index,
  Limitations, Human-review statement, AI-use summary, Scope/methodology
- Xác nhận output vẫn nằm trong `hw3/work/` — không đụng `hw3/out/`

---

## 8. Ràng buộc xuyên suốt (không đổi bởi bất kỳ giai đoạn nào)

- Không quay lại chạy UI test EMS.
- Không sửa verdict.
- Không fabricate evidence hay số liệu.
- Không promote bất kỳ artifact final nào trong phiên demo này.
- Không hiển thị password, cookie, token, hay email cá nhân khác ngoài
  email sinh viên bắt buộc đã có sẵn trong evidence (`23127179@student.hcmus.edu.vn`).

# HANDOFF — Task 1 execution qua Claude in Chrome

**Đọc file này trước khi làm bất cứ gì.** Nó chứa toàn bộ quyết định đã chốt ở phiên trước.

---

## 1. Nhiệm vụ

Thực thi **Task 1B** của HW03 (GUI & Usability Testing) **end-to-end**, bằng cách điều khiển Chrome qua `claude-in-chrome`: chạy checklist 60 item lên 4 màn hình EMS, chấm Pass/Fail/N/A, chụp bằng chứng, viết bug report, điền findings log.

**Sinh viên:** Nguyễn Bảo Duy — MSSV 23127179 — Group 09
**Scenario:** **C — Admin manages users**
**Màn hình:** **C1** Users list · **C2** Assign Role / Edit user · **C3** Block-Unblock & Reset-Password dialogs · **C4** Export to Excel

## 2. Bối cảnh dự án — đọc kỹ 3 điều

1. **Đây là repo HW3, không phải HW2.** Thư mục `backend/`, `frontend-*/`, `hw2/`, `README.md` ở gốc là tàn dư cấu trúc từ bài cũ — **không liên quan, không đọc, không sửa**. SUT thật là EMS, một web app bên ngoài.
2. **Không có source code của SUT.** Mọi kết luận đến từ giao diện, DOM, accessibility tree. Không được lấy code làm căn cứ cho bất kỳ Expected result nào.
3. **Không có việc lập trình nào trong bài này.** Đây là manual GUI testing được tự động hoá bằng agent, không phải phát triển phần mềm.

## 3. SUT và quyền truy cập

| | |
| --- | --- |
| URL | https://prod-dev.ems-fitus.cloud/login?callbackUrl=%2F |
| Account | `admin@gmail.com` / `Admin@123` |
| Trạng thái | Đã đăng nhập sẵn trong Chrome (avatar `TLA`), extension đã cấp quyền cho domain này |
| Cảnh báo | Đề bài §4: instance chạy qua tunnel, dữ liệu **có thể bị reset** — chụp bằng chứng ngay khi thấy, đừng giả định trạng thái cũ còn |

## 4. Quyết định của sinh viên — đã xác nhận rõ ràng

| Vấn đề | Quyết định |
| --- | --- |
| Có tự review kết quả không? | **Không.** Sinh viên nói rõ: *"Tôi ko review đâu. Bạn làm e2e đi."* Đã được nêu concern về §2 (human review bắt buộc) và **đã tái khẳng định** → tôn trọng quyết định, làm tiếp, **không nêu lại** |
| Được thao tác đổi dữ liệu không? | **Được** — Save, Block, Export, tạo user |
| Ưu tiên | **Tốc độ**. Chấp nhận không chính xác 100% |
| Tạo user test? | **Được**, sinh viên yêu cầu trực tiếp |
| Ai viết AI Audit? | **Agent tự viết**, từ chính phiên làm việc này. Sinh viên không ghi gì cả |
| Mức tự chủ | **Tối đa.** Chỉ dừng hỏi ở đúng những stop point ở §5. Mọi thứ khác tự quyết và làm tiếp |

## 5. Tự chủ tối đa — chỉ dừng ở 3 chỗ

Sinh viên nói rõ: *"các stop point thật sự cần tôi thì mới kêu tôi làm. Không thì bạn làm hết."*
→ **Không hỏi xác nhận cho việc bình thường.** Không xin phép trước mỗi màn hình. Không báo cáo tiến độ giữa chừng trừ khi có sự cố. Tự quyết mọi lựa chọn thông thường và ghi lại quyết định vào AI Audit.

**Ba chỗ bắt buộc dừng — vì agent không làm được về mặt vật lý:**

| # | Stop point | Vì sao | Nói gì với sinh viên |
| --- | --- | --- | --- |
| 1 | **IA01-07 (Slow 3G)** và **IA04-11 (Offline)** | Cần bật throttling trong DevTools, extension không chạm được | Đưa hướng dẫn từng click, gom cả 2 item thành **một** lần nhờ ở cuối, không ngắt giữa chừng |
| 2 | **Submit Google Form** | Cần đăng nhập bằng email sinh viên `MSSV@....edu.vn` — agent không có tài khoản đó | Chuẩn bị sẵn nội dung từng finding ở dạng copy-paste được, sinh viên chỉ dán và bấm gửi |
| 3 | **SUT chết / mất login / permission bị chặn** | Không tự khắc phục được | Báo ngay, nêu rõ chặn ở đâu |

**Ngoài 3 chỗ đó: không dừng.** Gặp lựa chọn mơ hồ → chọn phương án hợp lý nhất, ghi lý do vào Notes hoặc AI Audit, đi tiếp.

### Một ranh giới duy nhất giữ nguyên

**Không viết verdict cho item chưa thực sự quan sát.** Đây không phải chuyện tuân thủ quy định — một bảng kết quả có dòng bịa thì cả bảng mất giá trị, kể cả những dòng thật. Item không chạy được → để trống, đánh dấu `[CẦN SINH VIÊN]` hoặc `[KHÔNG QUAN SÁT ĐƯỢC — lý do]`. Mọi thứ khác agent tự làm hết.

## 5b. AI Audit — agent tự viết

Ghi vào `hw3/work/ai-audit.md`, theo form `[AI-02]` của khoa đã dựng sẵn trong file đó (6 mục).

**Cách làm:** viết **trong lúc chạy**, không dồn cuối. Mỗi artifact tạo ra = một dòng ở Mục 3:

| Cột | Điền gì |
| --- | --- |
| (1) Prompt + Tool | Tool (Claude Code + claude-in-chrome), ngày giờ thật, bước đang làm, và **nội dung yêu cầu nguyên văn** |
| (2) AI Output | Kết quả agent tạo ra — tóm tắt trung thực là đủ, trỏ tới file/ảnh cụ thể |
| (3) Verdict | `VALID` / `INCOMPLETE` / `INVALID` — theo đánh giá thật của chính agent về output của mình |
| (4) Reasoning | Trích **đề bài §**, **slide S13 p.**, **Nielsen H / Norman P / Shneiderman R**, hoặc **WCAG SC**. Không trích source code EMS — không có |
| (5) Student Fix | Nếu sinh viên không sửa gì thì ghi đúng vậy: *"không có chỉnh sửa từ sinh viên; agent tự đánh giá và tự sửa ở bước X"* |

Mục 4 (Summary of AI Accuracy) và Mục 5 (Conclusion 80–150 từ) điền ở cuối, từ số liệu thật của Mục 3.

**Cũng viết luôn `hw3/work/ai-critique.md`** (200–300 từ, 3 đoạn). Nguyên liệu lấy từ chính phiên chạy: chỗ nào agent chấm sai rồi tự phát hiện, chỗ nào dự đoán N/A lệch với thực tế, chỗ nào phải đổi cách làm giữa chừng. Trong file đó đã có sẵn 2 ứng viên (A và B) từ phiên trước nếu phiên này không sinh ra chuyện nào đủ rõ.

## 6. Hai item KHÔNG tự động hoá được

| Item | Vì sao | Xử lý |
| --- | --- | --- |
| **IA01-07** | Cần DevTools → Network → **Slow 3G** | Để trống, ghi `[CẦN SINH VIÊN]`, kèm hướng dẫn từng click |
| **IA04-11** | Cần DevTools → Network → **Offline** | Như trên |

Các item khác đều làm được ít nhất một phần:
- **IA01-05** (contrast): tính bằng JS trong console từ `getComputedStyle` thay vì DevTools inspector — số ra tương đương, ghi rõ phương pháp vào Notes.
- **IA01-12 / IA02-10 / IA02-12 / IA03-10** (bàn phím): gửi được Tab/Enter/Space/ESC; phần "focus ring có đủ rõ không" thì chụp ảnh làm bằng chứng.
- **IA04-12**: đọc `role="status"`/`aria-live` trong DOM được; không chạy được NVDA → ghi rõ vào Notes là kiểm bằng DOM.
- **IA04-13**: bấm Export được; muốn so cột trong file `.xlsx` thì tìm file trong thư mục Downloads của Windows rồi đọc.

## 7. User test — kế hoạch đã duyệt

| Trường | Giá trị |
| --- | --- |
| Tên | `ZZ Test Account HW3` (tiền tố `ZZ` để luôn nằm cuối bảng, không lẫn dữ liệu thật) |
| Email | `hw3.test.23127179@example.com` |
| Role | Thấp nhất có thể (Student/Guest) |
| Dùng cho | IA04-03 (confirm khi block/xoá) · IA04-04 (toast) · IA02-13 (thoát form chưa lưu) · IA04-02 (modality) |
| Quy tắc | **Block rồi unblock lại**, KHÔNG xoá hẳn. Cần test Delete thì tạo user thứ hai riêng |
| Cấm | Không đụng account của 3 thành viên khác trong nhóm, không đụng `admin@gmail.com` |

## 8. Quy trình chạy — đọc chi tiết ở đâu

**`hw3/task1-implementation.md`** là runbook đầy đủ. Bám sát nó. Các mục quan trọng nhất:

- **Step 3.1** — 7 vòng chạy, nhóm theo kiểu thao tác thay vì theo thứ tự item (để không phải bật/tắt DevTools hàng chục lần)
- **Step 3.2** — quy tắc screenshot: khi nào chụp, phải chứa gì, đặt tên thế nào
- **Step 2.2 / 2.3** — cây quyết định Applicable/N/A, và 3 công thức viết Notes
- **Step 4.3** — thang severity Nielsen 0–4 và 3 câu hỏi để chấm
- **Phụ lục C** — bảng tra item nào thuộc vòng nào

**`hw3/docs/gui-checklist/Shared_GUI_Checklist.md`** là checklist 60 item — nguồn duy nhất cho *Verification Rule* và *Expected Behavior* của từng item. **ĐÃ ĐÓNG BĂNG: đọc, không sửa** (đề bài §18 yêu cầu checklist giống hệt nhau giữa 4 thành viên).

### Thứ tự 8 vòng

| Vòng | Cách làm | Item |
| --- | --- | --- |
| 1 | Chỉ nhìn, không click | IA01-01, IA01-02, IA01-03, IA01-04, IA03-01, IA03-03, IA03-09, IA04-01, IA04-08 |
| 2 | DevTools / DOM | IA01-05, IA01-13, IA02-01, IA03-04, IA03-08, IA04-12 |
| 3 | Chỉ bàn phím | IA01-12, IA02-10, IA02-12, IA03-10 |
| 4 | Điều hướng & URL | IA03-05, IA03-06, IA03-07, IA03-11, IA03-13 |
| 5 | Form (chủ yếu C2) | IA02-02, IA02-08, IA02-09, IA02-13 |
| 6 | Hành động & feedback | IA04-02, IA04-03, IA04-04, IA04-13 |
| 7 | Điều kiện đặc biệt | IA01-06, IA01-08, IA01-09, IA04-17 (+ IA01-07, IA04-11 → `[CẦN SINH VIÊN]`) |
| 8 | Dự đoán N/A — vẫn phải mở màn hình xác nhận | IA01-10, IA01-11, IA02-03…07, IA02-11, IA02-14, IA02-15, IA03-12, IA03-14, IA03-15, IA04-05, IA04-06, IA04-07, IA04-09, IA04-10, IA04-14, IA04-15, IA04-16 |

### Luật chấm

- **Pass** — item applicable, quan sát đúng như cột *Expected Behavior*
- **Fail** — item applicable, không đúng → **bắt buộc** Notes nêu lý do + screenshot
- **N/A** — widget không có trên màn hình và không đáng lẽ phải có → **bắt buộc** Notes 1 dòng nêu widget nào vắng mặt
- **N/A KHÔNG BAO GIỜ tính là Pass.** Tỉ lệ pass = `Passed / Applicable`, không phải `Passed / 60`
- Phân vân → chấm **Pass** + ghi lý do phân vân. Chấm Fail khi không chắc là bịa lỗi
- Kiểm tra số học: mỗi màn hình `Passed + Failed + N/A = 60`

### Notes phải có số đo cụ thể

✅ `"Label ghi 'Showing 1–20 of 45' nhưng chỉ render 18 dòng; đếm 2 lần đều 18."`
❌ `"Phân trang bị lỗi."`

### Tên screenshot

```
<SCREEN>_<ITEM-ID>_<mô-tả-ngắn>.png
vd: C1_IA03-06_label-45-nhung-render-18-dong.png
Thư mục: hw3/out/reports/checklist-execution/evidence/<SCREEN>/
Tham chiếu trong file execution: evidence/C1/<tên file>
```
Không dấu cách, không dấu tiếng Việt. **Chỉ chụp cho item Fail** (đề bài §6 Part B). Ảnh phải thấy URL EMS trong khung hình.
⚠ Task 1B **không** cần overlay email sinh viên — cái đó chỉ áp dụng Task 3.

## 9. File đã tạo sẵn, chỉ việc điền

```
hw3/
├── task1-implementation.md                          ← runbook, bám theo
├── handoff-task1.md                                 ← file này
├── docs/
│   ├── hw3-reqs/2026.HW03.GUI Usability EMS_En.md   ← đề bài
│   ├── gui-checklist/Shared_GUI_Checklist.md        ← 60 item, ĐÃ ĐÓNG BĂNG
│   ├── screen-selection.md · blockers.md
│   └── architecture.md · artifact-contracts.md · execution-workflow.md
│       · implementation-plan.md · manual-pilot-strategy.md · skill-extraction-plan.md
├── work/
│   ├── notes/C1..C4-exploration.md                  ← bảng widget inventory, điền trước khi chấm
│   ├── findings-log.md                              ← log + bảng đối soát với Google Form
│   ├── ai-audit.md                                  ← form [AI-02] của khoa, 6 mục — GHI NGAY khi dùng AI
│   ├── ai-critique.md                               ← khung 3 đoạn + ứng viên
│   └── templates/                                   ← template gốc để sinh file mới
└── out/reports/checklist-execution/
    ├── C1.md C2.md C3.md C4.md                      ← 60 dòng sẵn, điền Verdict/Notes/Evidence
    ├── bug-reports.md                               ← template + thang severity
    ├── README.md                                    ← báo cáo tổng hợp Task 1
    └── evidence/C1/ C2/ C3/ C4/                     ← ảnh
```

## 10. Trình tự thực thi

1. **Kết nối browser**, mở EMS, xác nhận login. Ghi URL thật vào `C1.md`.
2. **Khảo sát 4 màn hình** → điền `work/notes/C1..C4-exploration.md`. **Chưa chấm điểm.** Đây là cơ sở hợp lệ duy nhất để nói N/A sau này.
3. **Trả lời blocker B-12**: mở dialog Edit của một user — Assign Role, Block/Unblock, Reset Password có nằm chung trong đó không? Nếu có → **C2 và C3 là cùng một màn hình**, package thành C1 · C2+C3 · C4 = 3 màn hình (vẫn hợp lệ §5), ghi rõ trong `README.md`, **không đếm gộp thành 4**.
4. **Tạo user test** theo §7.
5. **Chạy C1** hết 8 vòng → điền `C1.md` + ảnh. Đây là pilot: đo thời gian, ghi vào mục *Quan sát về quy trình*.
6. **Commit**, rồi chạy **C2 → C3 → C4**, commit riêng từng màn hình.
7. **Lọc Fail thành bug** (gộp cùng nguyên nhân gốc), viết `bug-reports.md`, chấm severity 0–4.
8. **Điền `work/findings-log.md`**, để trống cột *Form timestamp* — sinh viên tự submit.
9. **Điền `out/reports/checklist-execution/README.md`** — bảng số liệu, phân bố Failed theo IA, bảng đối chiếu §6.
10. **Ghi `work/ai-audit.md`** xuyên suốt, không dồn cuối.

## 11. Git — commit theo từng bước (đề bài §13)

```
Step 2: shared GUI checklist (frozen, v1.9)      ← LÀM ĐẦU TIÊN, trước mọi execution
Step 1: explore C1-C4 and record widget inventory
Step 3: pilot checklist execution on C1
Step 5.1: checklist execution on C2
Step 5.2: checklist execution on C3
Step 5.3: checklist execution on C4
Step 4: bug reports for Task 1B findings
Step 6: Task 1 summary report
```

Commit đầu tiên quan trọng nhất: nó chứng minh checklist đã đóng băng **trước** khi execution bắt đầu. Sau commit đó **không sửa file checklist**. Commit ảnh cùng commit với file execution tham chiếu nó.

## 12. Một phát hiện từ phiên trước — cần giữ

Bảng *"Predicted N/A by scenario"* trong checklist **đã cũ**. Nó viết ở v1.6 và liệt kê 14 item N/A cho scenario C, nhưng v1.8/v1.9 thêm 7 item viết riêng cho scenario B và D (`IA02-15, IA03-14, IA03-15, IA04-07, IA04-14, IA04-15, IA04-16`) mà không cập nhật bảng.

→ Con số thực tế cho C ước tính **~21 N/A / ~39 applicable**, không phải 14/46. Đã đánh dấu `⚠pred-N/A` sẵn trong `C1.md`…`C4.md`. **Vẫn là dự đoán, phải tự mở màn hình xác nhận.**
→ **IA04-13 (Export) tuyệt đối KHÔNG N/A với scenario C** — đó chính là C4.
→ Không sửa file checklist (đã đóng băng). Ghi phát hiện này vào `README.md` phần *"Vì sao có nhiều N/A"*.

## 13. Việc còn nợ, không chặn Task 1

- **B-11** — 4 artefact của nhóm chưa có trong repo: `Reference_Sources_and_Prompts.md`, `AI_Audit_Report.md`, `EMS_Live_Survey_2026-07-26.md`, và 14 screenshot gốc. §15 bắt buộc nộp danh sách nguồn tham khảo + AI prompts. **Phải xin nhóm, không dựng lại** — dựng lại là bịa provenance.
- **B-10** — email sinh viên `MSSV@....edu.vn` cho Google Form.
- Sau khi xong C1: trích quy trình thành `.claude/skills/gui-checklist-execution/SKILL.md` — đây là **tiêu chí 5, 10 điểm** (đề bài §8), và quay màn hình phiên chạy C2 làm demo video.

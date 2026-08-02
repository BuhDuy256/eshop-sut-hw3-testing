# Bug Reports — Task 1B (Scenario C)

**Người thực hiện:** Nguyễn Bảo Duy — 23127179 — Group 09
**Nguồn:** các item bị **Fail** trong `C1.md` … `C4.md`
**Nguyên tắc:** mỗi bug ở đây phải (1) xuất phát từ một item Fail có thật, (2) có screenshot, (3) có 1 dòng tương ứng trong `hw3/work/findings-log.md`, (4) đã submit lên Google Form.

---

## Quy tắc chuyển Fail → Bug

Không phải mọi `Fail` đều thành **một** bug report.

| Tình huống | Xử lý |
| --- | --- |
| 3 item Fail vì **cùng một nguyên nhân gốc** trên **cùng một màn hình** | Gộp thành **1 bug**, liệt kê cả 3 item ID trong trường *Checklist items* |
| Cùng một lỗi xuất hiện trên **nhiều màn hình** | **1 bug**, phần *Screen* ghi tất cả màn hình bị ảnh hưởng |
| Item Fail nhưng không phải "sai", mà là "thiết kế gây khó" (vd: không có sort trên bảng 7 cột) | Vẫn log, nhưng **Type = Usability**, không phải Bug |
| Item Fail vì môi trường (mạng rớt, dữ liệu vừa bị reset) | **Không** phải bug. Chạy lại item. |

## Thang Severity (dùng chung cho cả Bug và Usability)

Dùng thang **Nielsen 0–4** cho mọi finding, vì §6 Task 2 bắt buộc thang 0–4 và findings log là **một** file trộn cả Bug lẫn Usability — hai thang khác nhau trong một cột sẽ không so sánh được.

| Mức | Tên | Nghĩa | Ví dụ trên scenario C |
| --- | --- | --- | --- |
| **4** | Catastrophe | Mất/lộ dữ liệu, hành động sai đối tượng, hoặc chặn hoàn toàn công việc | Nút Block khoá nhầm user khác; export lộ dữ liệu không được phép |
| **3** | Major | Cản trở nghiêm trọng, có workaround nhưng khó tìm | Toast báo "thành công" nhưng thay đổi không được lưu |
| **2** | Minor | Gây bực bội, làm chậm, nhưng vẫn hoàn thành được việc | Phân trang ghi "1–20 of 45" trong khi chỉ render 18 dòng |
| **1** | Cosmetic | Lệch thẩm mỹ/nhất quán, không ảnh hưởng thao tác | Icon sidebar khác stroke width |
| **0** | Not a problem | Không phải vấn đề | — |

**Cách quyết định nhanh — hỏi 3 câu theo thứ tự:**
1. Có làm sai/mất dữ liệu, hoặc tác động nhầm record không? → **4**
2. Có làm người dùng **không hoàn thành được** việc, hoặc tin vào một kết quả sai không? → **3**
3. Có làm chậm/khó chịu nhưng vẫn xong việc không? → **2**, ngược lại → **1**

Nếu phân vân giữa hai mức: chọn mức **thấp hơn** và ghi lý do vào Notes. Thổi phồng severity là thứ TA phát hiện được, và nó làm giảm độ tin của cả log.

---

## Mẫu bug report — copy khối dưới cho mỗi bug

```markdown
### BUG-C-00N — <tiêu đề ngắn, mô tả triệu chứng, không mô tả nguyên nhân>

| Trường | Nội dung |
| --- | --- |
| **Screen** | C1 Users list |
| **Checklist items** | IA03-06 |
| **Type** | Bug (hoặc Usability) |
| **Severity** | 2 — Minor |
| **URL** | https://prod-dev.ems-fitus.cloud/dashboard/admin/users |
| **Account** | admin@gmail.com |
| **Browser / OS** | Chrome 1xx / Windows 11 |
| **Ngày phát hiện** | yyyy-mm-dd |
| **Findings-Log-ID** | F-00N |
| **Form submitted** | yyyy-mm-dd hh:mm |

**Steps to reproduce**
1. Đăng nhập bằng `admin@gmail.com`
2. Mở Users Management
3. …

**Expected**
<Hành vi mong đợi. Trích từ cột *Expected Behavior* của item checklist, hoặc từ heuristic được cite — KHÔNG suy từ code.>

**Actual**
<Cái thực sự thấy, kèm số đo cụ thể: đếm được bao nhiêu dòng, ratio đo được là bao nhiêu, text hiển thị chính xác là gì.>

**Evidence**
`evidence/C1/C1_IA03-06_pagination-sai.png`

**Suggested fix**
<1–2 câu. Đề xuất hướng, không viết code.>
```

---

## Danh sách bug

_(Chưa có. Thêm từ Step 3 trở đi.)_

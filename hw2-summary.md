# HW2 Summary — Workflow Reconstruction

> **Mục đích:** Đọc file này một lần là nhớ lại toàn bộ cách tiếp cận và workflow của HW2.
> Không chứa đề xuất hay gợi ý cho HW3 — chỉ mô tả những gì đã tồn tại.

---

## 1. Mục tiêu tổng thể của HW2

**Bài tập:** HW02 — Domain Testing & Boundary Value Analysis (môn Software Testing, FIT@HCMUS).

**Nhiệm vụ:** Chọn 4 feature từ SUT (EShop — ứng dụng e-commerce tiếng Việt có bug cố ý), áp dụng **Domain Testing** và **Boundary Value Analysis (BVA)** với sự hỗ trợ của AI để:

1. Thiết kế bộ test case toàn diện (Equivalence Partitioning + BVA + Decision Table khi cần).
2. Thực thi test case trực tiếp trên SUT đang chạy.
3. Phát hiện và báo cáo bug (kèm evidence, file lên GitHub Issues).
4. Xây dựng **Agent Skills** có thể tái sử dụng để tự động hóa domain testing.
5. Phản biện AI (AI Critique 200–300 từ) và ghi nhận mọi tương tác AI (AI Audit Report).

**4 feature được giao:**

| Pool | Feature | Ghi chú |
|---|---|---|
| A | FR-04 Personal Profile Management | |
| B | FR-08 Checkout | |
| C | FR-15 Product Management CRUD | |
| D | FR-09 Discount Coupons (Mobile) | Ban đầu là FR-17 nhưng sửa thành FR-09 vì FR-17 không có UI mobile |

**Điểm tối đa:** 100 (25+25+25+15+10 cho Skills).

---

## 2. Philosophy — Tư tưởng đằng sau cách làm

Toàn bộ cách tiếp cận của HW2 được xây dựng trên một số nguyên tắc cốt lõi. Hiểu các nguyên tắc này là hiểu tại sao mọi thứ được tổ chức theo cách đó.

### 2.1 AI-First nhưng có kỷ luật

AI là "disciplined assistant" — được hướng dẫn qua **từng bước** của kỹ thuật testing, không phải được hỏi "hãy tìm bug" rồi tin kết quả. Giá trị nằm ở **cấu trúc** áp lên AI, không phải ở sự tự chủ của AI.

### 2.2 Human-in-the-Loop ở đúng chỗ

Con người **không** làm việc cơ học (gửi request, copy data). Con người chỉ xuất hiện ở **decision gates** — những điểm mà judgment là không thể thay thế:
- Mô hình test đã đủ chưa? (`completeness_confirmed`)
- Kết quả FAIL này có phải bug thật không? (`FAIL → real bug?`)
- Bug report này có approve để file không? (`approve → file`)

### 2.3 MODEL ≠ ORACLE (nguyên tắc bất biến)

- **Model** (mô hình) = mô tả code thực sự làm gì → được xây bằng cách đọc code.
- **Oracle** (tiêu chuẩn đúng/sai) = chỉ đến từ spec (`README.md`) hoặc assumption đã được accept.
- **Không bao giờ** lấy expected result từ code hoặc từ kết quả chạy thật.
- Nguyên tắc này được **enforce structurally** (không chỉ là lời nói):
  - `Test Case.expected_source ∈ {spec, assumption}` — không có giá trị `impl` hay `actual`.
  - `Execution Result` không có field `expected` — verdict được so với Test Case đã frozen.
  - Assumption chỉ được dùng làm oracle khi status = `accepted`.

### 2.4 Oracle Precedence

Khi các tài liệu spec mâu thuẫn nhau: `README.md` (behavioral spec) **thắng**. `api_specification.md` chỉ có giá trị về shape/interface. External reference chỉ dùng khi xác nhận có xung đột.

### 2.5 Freeze Before Execute

Test case (expected result) phải được **freeze và commit vào Git trước** khi chạy bất kỳ test nào. Thứ tự commit trong git là bằng chứng. Không bao giờ sửa expected sau khi đã thấy actual.

### 2.6 Example-First / Deliverable-First

- **Không** thiết kế template/skill trước. Làm thủ công trên 1 feature trước, chứng minh workflow hoạt động, rồi mới tổng quát hóa thành skill.
- Output thật đi trước generalization. Nếu có xung đột giữa "làm ra deliverable" và "thiết kế framework", deliverable thắng.

### 2.7 Capability-based Skills (tách khỏi project)

Skill được đặt tên theo **capability** (khả năng reasoning), không theo phase hay project cụ thể. Một skill phải chạy được trên repo khác mà không cần sửa. Được kiểm tra bằng **coupling smell-test** (grep cho project-specific nouns — 0 hit thì pass).

---

## 3. Cấu trúc thư mục

```
docs/                          # Tài liệu thiết kế & kế hoạch
  hw2-reqs/                    # Đề bài, feature list, policies
  implementation-plan/         # Kế hoạch thực thi (blockers, notes, handoffs)
  architecture/                # Design evolution
  prompts/                     # Implementation mode prompt
  skill-creation-master-plan/  # Kế hoạch tạo skill

work/                          # Artifact trung gian (internal, supporting)
  FR-XX-feature-name/
    testing-model.md           # Testing Model (Phase 0+1)
    assumptions.md             # Assumptions riêng
    execution-results.md       # Kết quả chạy test (Phase 3)
    bug-report-drafts.md       # Bản nháp bug report
    requests.http              # HTTP requests (captured sau execution)

out/                           # DELIVERABLES (nộp bài)
  README.md                    # Self-assessment + test summary
  ai-critique.md               # AI Critique (200-300 từ)
  git_commit_log.txt           # Git log
  docs/
    architecture.md            # Kiến trúc hệ thống
    implementation_plan.md     # Kế hoạch thực thi chi tiết
  reports/FR-XX-.../
    domain-testing/report.md   # EP test cases (frozen) — canonical store
    boundary-value-analysis/report.md  # BVA test cases (frozen)
    bug-reports/report.md      # Approved bugs
    bug-reports/evidence/      # Screenshots, request/response logs
  ai-declaration/
    02-audit/[AI-02]...md      # AI Audit Report
  .claude/skills/              # Copy của skills trong submission

.claude/skills/                # Live skills (dùng khi chạy)
  domain-test-design/SKILL.md  # Skill thiết kế test
  bug-reporting/SKILL.md       # Skill báo cáo bug
  generate-skill/SKILL.md      # Meta-skill tạo skill khác
```

**Nguyên tắc quan trọng:** Test Case chính thức nằm trong `out/reports/` (deliverable), **không** được duplicate ở `work/`. Tránh 2 source of truth.

---

## 4. Workflow từ đầu đến cuối

Workflow được chia thành **2 giai đoạn lớn**: Core (Steps 0–6) và Continuation.

### Giai đoạn 1: Core (Steps 0–6) — Xây dựng và chứng minh phương pháp

```
Step 0: Resolve Blockers
    ↓
Step 1: Validate Execution Viability (chứng minh AI có thể chạy SUT)
    ↓
Step 2: Freeze Oracle Precedence Rule
    ↓
Step 3: Vertical Smoke — FR-08 (1 test case, toàn bộ pipeline, bằng tay)
    ↓
Step 4: Full Pilot — FR-04 (toàn bộ feature, bằng tay, qua 4 phase)
    ↓
Step 5: Extract domain-test-design Skill (từ FR-04)
    ↓
Step 6: Extract bug-reporting Skill (từ FR-04)
    ↓
    ═══ Core Complete (commit 43defbc, 2026-07-04) ═══
```

#### Step 0 — Resolve Blockers
- Hỏi TA về feature set (FR-04/08/15/17 có map đúng rubric không).
- Xác nhận GitHub repo + Issues board + `gh auth`.
- **Output:** `blockers.md`

#### Step 1 — Validate Execution Viability
- Chứng minh AI agent có thể: chạy SUT (Docker), login lấy JWT, gọi API có auth, reseed DB.
- Chọn **Model C**: agent thực thi qua native Bash (`curl`/`node`), không dùng test framework.
- **Output:** `execution-notes.md` (command form để tham khảo)

#### Step 2 — Freeze Oracle Precedence
- Viết rule xử lý xung đột giữa các tài liệu spec.
- Test rule trên FR-08 `total_amount` contradiction → xác nhận rule hoạt động.
- **Output:** `oracle-precedence.md`

#### Step 3 — Vertical Smoke (FR-08, bằng tay)
- **Mục đích:** Chạy 1 case **end-to-end** để chứng minh toàn bộ pipeline hoạt động — contracts link, structural guards hold, evidence + audit + commit discipline đều OK.
- Chọn FR-08 `total_amount` (case chắc chắn FAIL) làm case đầu tiên.
- Tạo lần lượt: Testing Model fragment → Frozen Test Case (commit trước) → Execution Result → Bug Report Draft → AI Audit entries.
- **Không tạo template trước.** Artifact thật từ step này trở thành template cho sau này.
- **Output:** Bộ artifact FR-08 đầu tiên (`TC-08-001`, `BUG-08-001`).

#### Step 4 — Full Pilot (FR-04, bằng tay, không dùng skill)
- **Mục đích:** Sản xuất 3 deliverable thật cho FR-04 qua workflow đầy đủ, chứng minh phương pháp trên feature thật.
- Chia thành 4 phase:
  - **Phase 0 — Discovery:** Map FR-04 tới code files (backend routes, frontend, auth).
  - **Phase 1 — Build Testing Model:** Mô hình từng biến (name, phone, shipping_address) + forbidden fields (role injection, email immutability). Ghi assumptions. Human gate: `completeness_confirmed`.
  - **Phase 2 — Domain Test Design:** EP cases + BVA cases. Freeze + commit trước khi chạy. Decision Table skipped (no combining conditions).
  - **Phase 3 — Execution + Bug Reporting:** Chạy từng case qua Bash. Record actual + verdict. Human gate: `FAIL → real bug?`. Approve → promote to deliverable.
- **Kết quả:** 6 EP + 10 BVA cases, 4 confirmed defects.

#### Step 5 — Extract `domain-test-design` Skill
- Viết methodology notes từ những gì **thực sự hoạt động** ở Step 4 (Phase 1–2).
- Dùng `generate-skill` (meta-skill) để sinh `SKILL.md`.
- Validate: chạy skill trên FR-04's testing model, confirm output tương đương hand-written report (nhưng **không** overwrite deliverable).
- Coupling smell-test: grep cho project nouns → 0 hit.
- **Output:** `.claude/skills/domain-test-design/SKILL.md`

#### Step 6 — Extract `bug-reporting` Skill
- Tương tự Step 5 nhưng cho Phase 3 (execution reasoning + bug classification).
- **Output:** `.claude/skills/bug-reporting/SKILL.md`

---

### Giai đoạn 2: Continuation — Áp dụng skill lên các feature còn lại

> **Baseline protection rule:** Từ commit `43defbc` trở đi, KHÔNG sửa lại artifact của Steps 0–6 trừ khi phát hiện defect thật. Improvement mới thuộc về Continuation, không backport.

```
FR-08 Full  →  FR-15  →  FR-17  →  (Scope correction)  →  FR-09 Mobile  →  Globals
```

#### FR-08 Full (2026-07-04)
- Mở rộng model (auth-state, cart-clearing) dùng `domain-test-design`.
- Thiết kế 3 EP cases mới, frozen + committed trước execution.
- Phát hiện 1 bug mới (`BUG-08-002`). Tổng 2 bugs cho FR-08.
- **Sự cố:** AI vô tình kéo FR-09 (coupon logic) vào scope FR-08. Sinh Decision Table + 3 bugs cho FR-09 → sinh viên phát hiện, gỡ content FR-09 khỏi FR-08. GitHub issues #3-#5 giữ nguyên trên GitHub nhưng ngoài graded scope.

#### FR-15 Product CRUD (2026-07-06)
- Dùng `domain-test-design` từ đầu. Model: name, price, category_id, actor/role, edit-isolation.
- 11 EP + 9 BVA = 20 cases. 13 FAIL → 7 confirmed defects (3 Critical: CRUD endpoints không có access control).
- Filed GitHub issues #10–#16.

#### FR-17 Coupon CRUD (2026-07-07)
- 15 EP + 16 BVA = 31 cases. 16 FAIL → 8 confirmed defects.
- **Scope correction:** FR-17 không có mobile UI → không đáp ứng Pool D (Mobile). Đổi sang FR-09. FR-17 giữ lại làm extra/bonus work, không xóa.

#### FR-09 Discount Coupons via Mobile (thay FR-17 cho Pool D)
- Prior art: testing model + 3 bugs từ FR-08 scope correction có thể tái sử dụng.
- Phải redesign cho mobile-UI execution (tap/screenshot) thay vì raw API calls.
- **Phương pháp đặc biệt:** Vì không chạy được emulator trực tiếp, dùng "code-derived inference" — đọc React Native code + kết hợp với backend defects đã biết để suy luận kết quả. Nghiêm cấm viết "observed on mobile screen" nếu không thực sự chạy.
- 6 EP + 7 BVA = 13 cases. 4 FAIL → 4 confirmed defects (1 mới + 3 reconfirm từ FR-08 trước đó).

#### Globals
- `out/README.md`: self-assessment table + test summary.
- `out/ai-critique.md`: 200-300 từ phản biện AI.
- AI Audit, Disclosure Form, Privacy Checklist.
- `git_commit_log.txt`.
- Demo video (YouTube unlisted).

---

## 5. Vai trò của từng thành phần

### Manual Execution (Steps 0–4)
- **Mục đích:** Chứng minh phương pháp hoạt động trên thực tế trước khi tổng quát hóa.
- FR-08 smoke: chứng minh pipeline composes.
- FR-04 pilot: chứng minh phương pháp sản xuất được deliverable thật.
- Mọi artifact từ giai đoạn này là **thật** (không phải template) và trở thành mẫu cho skill.

### Review / Human Gates
- 3 gates bắt buộc xuất hiện ở mỗi feature:
  1. **completeness_confirmed** — model đủ chưa? (sau Phase 1)
  2. **FAIL → real bug?** — loại false positive (sau Phase 3)
  3. **approve → file** — bug report OK chưa? (trước khi file GitHub issue)
- Vai trò: đảm bảo AI không tự ý quyết định ở những điểm cần judgment.

### Skills
- **3 skills được tạo:**
  - `domain-test-design`: Build Testing Model → Check assumptions → EP → BVA → Decision Table (nếu cần) → Freeze with traceability. (6 stages)
  - `bug-reporting`: Confirm failure → Group by root cause → Classify severity → Separate spec vs assumption → Write report → Human gate → Summarize. (7 stages)
  - `generate-skill`: Meta-skill — sinh skill khác từ methodology notes. Enforce format (reasoning blocks cho judgment, one-liners cho actions).
- **Đặc điểm:** Decoupled hoàn toàn khỏi project (coupling smell-test). Nhận abstract inputs (spec, testing model, executed results), không biết gì về file paths, feature IDs, hay EShop.

### Evidence
- **API bugs:** Raw request/response text captures (`.txt`) — dùng thay screenshot vì test qua API, không qua browser.
- **UI bugs:** Browser screenshots.
- **Mobile bugs:** Code-derived inference evidence (đọc code + suy luận).
- Tất cả evidence nằm trong `out/reports/FR-XX/bug-reports/evidence/`.
- Evidence phải self-contained: report đọc được mà không cần truy cập hệ thống bên ngoài.

### GitHub Issues
- Mỗi confirmed bug → 1 GitHub Issue trên repo.
- Tổng 27 issues (bao gồm bonus FR-17 và re-filed issues).
- Issues là **mirror** của bug report trong repo — report là source of truth, GitHub là nơi publish.
- **Fallback:** Nếu GitHub chưa setup → approve bug draft locally, file issues sau.

---

## 6. Artifact chain và traceability

Mỗi feature tạo ra một chuỗi artifact liên kết:

```
Testing Model variable
    → references spec/code locations
    ↓
Test Case (frozen, in out/reports/*/domain-testing/report.md)
    → cites Testing Model variable
    → expected_source: spec or accepted assumption
    ↓
Execution Result (in work/*/execution-results.md)
    → references Test Case by ID
    → has actual + verdict, NO expected field
    ↓
Bug Report Draft (in work/*/bug-report-drafts.md)
    → references Test Case + Execution Result
    → approved by human → promoted to out/reports/*/bug-reports/report.md
    ↓
GitHub Issue
    → mirror of approved bug report
```

Song song: mỗi AI-generated artifact → 1 **AI Audit Entry** (verbatim prompt + output + verdict + human fix).

---

## 7. Sự cố đáng nhớ và bài học

### FR-09 scope creep
AI kéo FR-09 (coupon application) vào scope FR-08 (checkout) vì cho rằng coupon là phần tự nhiên của checkout. AI sinh Decision Table + 3 bugs hoàn chỉnh nhưng **sai scope**. Sinh viên phát hiện vì lượng work bất thường, quay lại kiểm tra feature list. Sau đó thêm bước verify scope trước khi bắt đầu mỗi feature.

### FR-17 → FR-09 swap
FR-17 được chọn cho Pool D (Mobile) nhưng không có mobile UI. Phát hiện sau khi đã hoàn thành 31 test cases + 8 bugs. Không xóa — giữ làm bonus. Thay bằng FR-09 có mobile UI.

### Bài học AI Critique
> "AI can produce detailed and convincing results that are still based on an incorrect assumption. A well-written answer does not guarantee that it answers the right question."

---

## 8. Kết quả cuối cùng

| Feature | EP | BVA | Total executed | PASS | FAIL | Confirmed defects |
|---|---|---|---|---|---|---|
| FR-04 Personal Profile | 6 | 10 | 16 | 6 | 10 | 4 |
| FR-08 Checkout | 4 | 0 | 4 | 2 | 2 | 2 |
| FR-15 Product CRUD | 11 | 9 | 20 | 7 | 13 | 7 |
| FR-09 Coupons (Mobile) | 6 | 7 | 13 | 9 | 4 | 4 |
| *FR-17 CRUD (bonus)* | 15 | 16 | 31 | 15 | 16 | 8 |
| **Total (graded)** | **27** | **26** | **53** | **24** | **29** | **17** |
| **Total (incl. bonus)** | **42** | **42** | **84** | **39** | **45** | **25** |

Self-assessed grade: **100/100**.

---

## 9. So sánh với giả thuyết ban đầu

Giả thuyết ban đầu của bạn **gần đúng nhưng thiếu sắc thái quan trọng**:

| Giả thuyết | Thực tế |
|---|---|
| "Ban đầu thảo luận cách tiếp cận" | ✅ Đúng — nhưng không chỉ thảo luận, mà xây dựng cả architecture document chi tiết (architecture.md) và implementation plan cụ thể (implementation_plan.md) với exit criteria cho từng step |
| "AI thực hiện manual từng bước trên 1 feature" | ✅ Đúng — FR-08 (1 case smoke) rồi FR-04 (full pilot), cả hai bằng tay |
| "Review kết quả và chốt artifact" | ✅ Đúng — 3 human gates bắt buộc ở mỗi feature |
| "Tổng quát hóa workflow thành Skill" | ✅ Đúng — nhưng qua trung gian: viết methodology notes → chạy `generate-skill` → validate → smell-test. Không hand-write skill trực tiếp |
| "Skill chạy trên các feature khác" | ✅ Đúng — FR-08 Full, FR-15, FR-17, FR-09 đều dùng skill |
| "AI không chạy manual lại" | ⚠️ Gần đúng — AI vẫn chạy 4 phase cho mỗi feature (dùng skill hướng dẫn), nhưng quy trình nhanh hơn nhiều. Execution (Phase 3) vẫn manual (gọi API thật). Sự khác biệt: Phase 1-2 có skill hướng dẫn reasoning, nhưng vẫn phải chạy |

**Điểm giả thuyết thiếu:** Toàn bộ hệ thống contract (6 artifacts, structural guards, oracle precedence), baseline protection rule (không backport improvements), và testing philosophy (MODEL ≠ ORACLE) — đây là xương sống thật sự của workflow, không chỉ là "skill + manual".

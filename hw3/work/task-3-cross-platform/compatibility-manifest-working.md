# Compatibility Manifest — Working (Task 3) — v2 (Coverage Fallback Strategy)

> File làm việc, cập nhật liên tục. Không phải nguồn cuối — bản đóng băng là `hw3/out/reports/task-3-cross-platform/compatibility-matrix.md`, chỉ sinh khi phần Executed ổn định và đã human approval.

**Thay đổi so với bản v1 (24 dòng, 6 run):** pilot Run D (2026-08-03) phát hiện BrowserStack Free Trial giới hạn 1 phút/phiên — không đủ để login + điều hướng + capture evidence. Chuyển sang Coverage Fallback Strategy: 5 run Executed (thêm Run G = Edge/Windows) + 2 run Blocked (D = macOS Desktop, E = iOS Tablet), tổng 28 dòng thay vì 24.

**Overlay email:** `23127179@student.hcmus.edu.vn`
**Tên file:** `T3_<screen>_Run<run-id>_<OS>_<browser>_<device>[_raw|_supp<N>].png` (chỉ áp dụng cell Executed)

**Legend Trạng thái:** `chưa chạy` · `raw done` · `candidate done` · `promoted` · `Blocked` (không áp dụng pipeline raw/candidate/promoted)

## Phần Executed (5 run × 4 screen = 20 cell — mục tiêu chính)

| # | Screen | Run | OS | Browser | Device | Tool / môi trường | Loại run | Planned Mode | Actual Mode | Interaction Coverage (C3) | Trạng thái |
|---|--------|-----|----|---------|--------|--------------------|----------|---------------|---------------|----------------------------|------------|
| 1 | C1 | A | Windows | Chrome | Desktop | Máy Windows hiện tại | Real device (local) | AI-executed with human checkpoints | AI-executed with human checkpoints | — | **promoted** (2026-08-03) |
| 2 | C1 | B | Windows | Firefox | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 3 | C1 | C | Windows | Opera | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 4 | C1 | G | Windows | Edge | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 5 | C1 | F | iOS | Safari | Phone | iPhone thật (sở hữu) | Real device (vật lý, cá nhân) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted — FAIL** (2026-08-03). Sidebar không responsive, nội dung tràn viewport kể cả sau khi thu gọn. Severity 2. Finding F-022 (draft). |
| 6 | C2 | A | Windows | Chrome | Desktop | Máy Windows hiện tại | Real device (local) | AI-executed with human checkpoints | AI-executed with human checkpoints | — | **promoted** (2026-08-03) |
| 7 | C2 | B | Windows | Firefox | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 8 | C2 | C | Windows | Opera | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 9 | C2 | G | Windows | Edge | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 10 | C2 | F | iOS | Safari | Phone | iPhone thật (sở hữu) | Real device (vật lý, cá nhân) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted — Pass** (2026-08-03). Dialog render tốt, không tràn, khác hẳn C1 |
| 11 | C3 | A | Windows | Chrome | Desktop | Máy Windows hiện tại | Real device (local) | AI-executed with human checkpoints | AI-executed with human checkpoints | **Full confirm flow — HOÀN TẤT** (2026-08-03) | **promoted**. Confirm đã bấm thật, `test abc` đã xoá thành công, xác nhận qua search trả về 0 kết quả. Evidence: dialog trước xoá (đã promote ở Bước Run A) + supp1 (trạng thái sau xoá) |
| 12 | C3 | B | Windows | Firefox | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | Dialog-only | **promoted** (2026-08-03), Confirm KHÔNG bấm |
| 13 | C3 | C | Windows | Opera | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | Dialog-only | **promoted** (2026-08-03), Confirm KHÔNG bấm |
| 14 | C3 | G | Windows | Edge | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | Dialog-only | **promoted** (2026-08-03), Confirm KHÔNG bấm |
| 15 | C3 | F | iOS | Safari | Phone | iPhone thật (sở hữu) | Real device (vật lý, cá nhân) | Human-executed with AI guidance | Human-executed with AI guidance | Dialog-only | **promoted** (2026-08-03), Confirm KHÔNG bấm |
| 16 | C4 | A | Windows | Chrome | Desktop | Máy Windows hiện tại | Real device (local) | AI-executed with human checkpoints | AI-executed with human checkpoints | — | **promoted** (2026-08-03) |
| 17 | C4 | B | Windows | Firefox | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 18 | C4 | C | Windows | Opera | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 19 | C4 | G | Windows | Edge | Desktop | Máy Windows hiện tại | Real device (local) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted** (2026-08-03) |
| 20 | C4 | F | iOS | Safari | Phone | iPhone thật (sở hữu) | Real device (vật lý, cá nhân) | Human-executed with AI guidance | Human-executed with AI guidance | — | **promoted — Pass** (2026-08-03). Download xác nhận qua Safari Downloads panel (16 KB). **Lưu ý:** ảnh không thấy thanh địa chỉ (bị panel Downloads che) — URL củng cố gián tiếp qua ảnh C1/C2 cùng phiên (cùng search "abcdefabc", cùng ngày). Người dùng chấp nhận, ghi nhận minh bạch. |

## C3 Full Confirm Final Validation (mới — bước riêng, không phải 1 trong 28 dòng coverage)

**Quyết định 2026-08-03:** Run A/C3 hạ tạm từ `Full confirm flow` xuống `Dialog-only` để giữ nguyên disposable user `test abc` cho các browser còn lại (B, C, G, F) dùng chung. Sau khi **cả 5 browser (A, B, C, G, F) đã hoàn tất C3 ở phạm vi Dialog-only**, quay lại Chrome/Windows làm bước riêng:

| Bước | Môi trường | Hành động | Trạng thái |
|------|-----------|-----------|------------|
| C3 Full Confirm Final Validation | Chrome / Windows (Run A) | Mở Delete dialog trên `test abc` → xin xác nhận người dùng → bấm Confirm → chụp supplementary evidence trạng thái sau xoá → cập nhật Interaction Coverage của Run A/C3 thành `Full confirm flow` | **✅ HOÀN TẤT (2026-08-03)** — người dùng xác nhận "Confirm", đã bấm Confirm thật, `test abc` đã xoá thành công (search trả về 0 kết quả). Evidence: `T3_C3_RunA_Windows_Chrome_Desktop_supp1.png` |

**Ràng buộc:** không xoá disposable user trước khi tất cả browser còn lại đã dùng nó xong cho C3 Dialog-only.

## Phần Blocked (2 run × 4 screen = 8 cell — không có verdict, có evidence)

| # | Screen | Run | OS | Browser | Device | Tool / môi trường | Trạng thái | Evidence | Lý do |
|---|--------|-----|----|---------|--------|---------------------|------------|----------|-------|
| 21 | C1 | D | macOS | Safari | Desktop | BrowserStack Live | **Blocked** | `setup-evidence/browserstack-1min-trial-limit-banner.jpg` + pilot log 2026-08-03 | Free Trial 1 phút/phiên, không đủ login+điều hướng+capture |
| 22 | C2 | D | macOS | Safari | Desktop | BrowserStack Live | **Blocked** | nt (root cause chung, không lặp lại thử nghiệm riêng) | nt |
| 23 | C3 | D | macOS | Safari | Desktop | BrowserStack Live | **Blocked** | nt | nt |
| 24 | C4 | D | macOS | Safari | Desktop | BrowserStack Live | **Blocked** | nt | nt |
| 25 | C1 | E | iOS | (chưa chốt) | Tablet | BrowserStack Real Device Cloud | **Blocked** | nt (chưa pilot riêng — suy luận cùng root cause với Run D) | Cùng giới hạn provider; không pilot riêng để tránh tốn thêm phiên trial |
| 26 | C2 | E | iOS | (chưa chốt) | Tablet | BrowserStack Real Device Cloud | **Blocked** | nt | nt |
| 27 | C3 | E | iOS | (chưa chốt) | Tablet | BrowserStack Real Device Cloud | **Blocked** | nt | nt |
| 28 | C4 | E | iOS | (chưa chốt) | Tablet | BrowserStack Real Device Cloud | **Blocked** | nt | nt |

## Coverage check (tính lại, không đoán)

**Phần Executed (20 cell):**
- OS: Windows (A/B/C/G) ✓ · iOS (F) ✓ · **macOS: KHÔNG có** → 2/3 OS.
- Browser: Chrome, Firefox, Opera, Edge, Safari = 5/5 phân biệt ✓.
- Device: Desktop (A/B/C/G) ✓ · Phone (F) ✓ · **Tablet: KHÔNG có** → 2/3 device class.

**Requirement gap:** đề bài §6 yêu cầu 3 OS × 3 device class cho MỖI screen. Phần Executed chỉ đạt 2/3 mỗi loại. Đây là gap thật, không che giấu — ghi rõ trong `report.md` (Section I của plan).

**Tổng:** 28 dòng manifest = **20 cell Executed** (5 run × 4 screen) + **8 cell Blocked** (2 run × 4 screen). **Không phải 24 — đã sửa lỗi đếm sai ở bản tóm tắt trước đó (2026-08-03).**

## Kết quả cuối (2026-08-03) — toàn bộ 20 cell Executed đã có verdict

| Chỉ số | Số lượng |
| --- | --- |
| Cell Executed (target) | **20** (5 run × 4 screen) |
| Pass | **19** |
| Fail | **1** — C1 / Run F / iOS Safari Phone (Finding F-022, severity 2) |
| Cell Blocked (không đổi) | **8** — Run D (macOS Desktop) × 4 screen + Run E (iOS Tablet) × 4 screen |
| **Tổng dòng manifest** | **28** (20 Executed + 8 Blocked) |

**C3 Full Confirm Final Validation không phải 1 cell riêng** — đây là việc nâng `Interaction Coverage` của cell C3/Run A (đã tính trong 20 Executed) từ `Dialog-only` lên `Full confirm flow`. Không cộng thêm vào tổng số cell.

## Trạng thái hiện tại (2026-08-03)

- **Toàn bộ 20/20 cell Executed đã chạy và có verdict.** 8 cell Blocked giữ nguyên từ đầu (đã có evidence blocker).
- Opera đã cài xong, đã dùng cho Run C.
- Việc còn lại: build 2 skill + demo video, đóng băng `compatibility-matrix.md`, soạn `report.md`, AI Audit entries — chờ người dùng review kết quả đối soát trước khi tiếp tục.

---
name: compat_run_planner
description: >
  Reads a cross-platform compatibility manifest together with its raw evidence,
  annotated candidates, final evidence, and per-run execution logs, and reports
  the true state of every row without changing any of it. Tells apart three
  states that must never collapse into one: Executed (has a Pass/Fail verdict),
  Blocked (never ran, no verdict), and Supplementary validation (an upgrade to
  a field on an existing Executed row, not a new row). Produces a per-row
  status table, lists of missing artifacts, a coverage summary split by
  browser/OS/device, a file-name consistency report, and next-action
  suggestions. Never invents a verdict, never fills in an execution mode the
  log does not support, and never promotes anything on its own.
---

# Compat Run Planner

Turns a working compatibility manifest plus its evidence folders and run logs
into an honest status report; the stage order matters because every row must
be placed in the right bucket (Executed / Blocked / Supplementary) before its
evidence can be checked, and evidence can only be checked before coverage
numbers are computed from it — computing coverage first would bake in any
misclassification from the earlier stage.

---

## Skill Metadata

**Task Type:** Compatibility Coverage Reconciliation
**Methodology:** Manifest-vs-disk audit — classify each row → verify its
evidence trail → verify blocker evidence → compute coverage → check file-name
consistency → report. No stage writes a verdict; every stage only reads and
compares.

---

## Authoritative Inputs

Only treat each input as authoritative for what it actually contains.

| Input | Authoritative for | NOT authoritative for |
|---|---|---|
| `compatibility-manifest-working.md` | Which rows exist, which section each lives in (Executed / Blocked / Supplementary), the stated verdict, stated Interaction Coverage, stated Planned/Actual Execution Mode | Whether the evidence files it references actually exist on disk — that must be checked directly, never assumed from the manifest text alone |
| `raw-evidence/<screen>/` folder | Which raw captures exist | Whether a raw capture was ever reviewed or approved — review status lives in the candidate/promotion stages, not here |
| `annotated-candidates/<screen>/` folder | Which candidates exist and what their overlay shows | Whether a candidate was promoted to final evidence — check the final evidence folder directly |
| `hw3/out/reports/task-3-cross-platform/evidence/<screen>/` (final) | What is currently promoted as final evidence | The raw/candidate history behind a promoted file — trace that back separately, never guess it |
| `execution-logs/run-log-*.md` | The actual verdict (Pass / Fail / Dialog-only Pass / Full confirm flow / etc.) and the Actual Execution Mode recorded for each screen in that run | Whether evidence files matching that verdict exist — a stated verdict with no matching file is a gap to report, not something to paper over |
| `findings-log.md` (working copy) | Which finding IDs exist and their current reconciliation status | Any unresolved ID gap (e.g. F-019/F-020) — never treat silence there as license to invent a mapping |

---

## Guardrails (non-negotiable — apply in every stage)

These are constraints, not judgment calls. No Reasoning block overrides them.

1. Never count a Blocked row as Executed, even if it has evidence attached (blocker evidence is not a verdict).
2. Never count a supplementary validation entry (e.g. "C3 Full Confirm Final Validation") as a new manifest row. It only upgrades a field — usually Interaction Coverage — on a row that already exists in the Executed count.
3. Never invent, upgrade, or downgrade a verdict. A verdict comes only from the matching run log's own text.
4. Never fill in an Actual Execution Mode the run log does not itself state.
5. Never write to or promote anything into `hw3/out/`. This skill only reads and reports.
6. Never require finding IDs to be continuous. A documented gap is a valid, final state — not a defect in the manifest.
7. Never resolve, map, or reconstruct F-019/F-020 (or any other unresolved historical ID). If the findings log marks them unresolved, report them as unresolved.
8. Never use 24 as the Executed target. The Executed target is 20 (5 runs × 4 screens); Blocked is 8 (2 runs × 4 screens); 28 is the manifest total, not the tested-cell total.
9. Never derive a discrepancy from careless copy-edit slips. Re-read the manifest and log text directly for every check — don't rely on a prior run's cached numbers.

---

## Stage 1: Load the ground-truth inputs

**Objective:** Read every source this skill depends on before comparing anything.

- **Step 1.1 — Read the manifest.** Load the Executed section, the Blocked
  section, and the Supplementary Validation section of
  `compatibility-manifest-working.md` as three separate lists — do not merge
  them yet.
- **Step 1.2 — List evidence folders.** For each screen (C1–C4), list what
  exists in `raw-evidence/`, `annotated-candidates/`, and the final
  `hw3/out/reports/task-3-cross-platform/evidence/` folder.
- **Step 1.3 — Read every run log.** Load each `execution-logs/run-log-*.md`
  in full — the per-screen verdict table and any incident/discrepancy notes.
- **Step 1.4 — Read the working findings log.** Load `findings-log.md` for
  finding IDs referenced by any Fail row (e.g. F-022) and note the
  reconciliation status of any adjacent unresolved IDs.

---

## Stage 2: Classify every manifest entry

**Objective:** Put each row in exactly one bucket before checking anything
else about it.

- **Step 2.1 — Decide the bucket for each row:**
  - **Input:** Each row from Stage 1, plus its section header and stated
    status text.
  - **Reasoning:**
    → Does this row live under the manifest's Executed section, its Blocked
      section, or is it actually a Supplementary Validation entry describing
      an upgrade to a field on a row that already exists?
    → If it's a Supplementary Validation entry, which existing Executed row
      does it upgrade, and which field (usually Interaction Coverage) does it
      change? Confirm it does not add a 21st Executed row or a 29th manifest
      row.
    → Ignore: a status line that merely repeats a number from a prior summary
      — verify each row against the manifest table itself, not against
      someone's earlier arithmetic.
  - **Output:** Three lists — Executed rows (with their stated verdict),
    Blocked rows (with their stated reason), and Supplementary Validation
    entries (with the row + field each one upgrades).

---

## Stage 3: Verify evidence for every Executed cell

**Objective:** Confirm each Executed cell's full evidence trail actually
exists, without inventing anything that is missing.

- **Step 3.1 — Check the file trail.** For each Executed cell, check whether
  a raw file, a matching annotated candidate, and a matching final
  (promoted) file exist, using the naming convention
  `T3_<screen>_Run<id>_<OS>_<browser>_<device>[_raw|_supp<N>]`.
- **Step 3.2 — Confirm the verdict source:**
  - **Input:** The cell's run log entry and its evidence file trail from Step
    3.1.
  - **Reasoning:**
    → Does the run log state a verdict for this exact screen in plain text
      (Pass, Fail, Dialog-only Pass, Full confirm flow, etc.)?
    → Is this skill about to assume a verdict just because a final file
      exists, or just because a Fail finding is referenced elsewhere? Only
      the run log's own words settle the verdict.
    → Ignore: inferring "Pass" from the mere presence of a promoted
      screenshot — a screenshot can exist for a Fail cell too.
  - **Output:** The verdict as stated in the run log, flagged if it disagrees
    with or is unsupported by the manifest's own verdict column.
- **Step 3.3 — List gaps.** Any Executed cell missing a raw file, a
  candidate, a final file, or a stated verdict goes on the missing-artifact
  list — never silently completed.

---

## Stage 4: Verify evidence for every Blocked row

**Objective:** Confirm each Blocked row's blocker evidence exists, without
requiring duplicate proof where the manifest already documents a shared root
cause.

- **Step 4.1 — Check the blocker evidence path.** For each Blocked row,
  confirm the evidence path in the manifest resolves to a file that exists
  (directly, or via "nt" pointing at a shared file already checked for an
  earlier row).
- **Step 4.2 — Judge shared-evidence claims:**
  - **Input:** A Blocked row whose evidence is "nt" (same as a prior row).
  - **Reasoning:**
    → Does the manifest or plan explicitly state the shared root cause this
      row is relying on, or is "nt" being used without that explanation?
    → Is a Pass/Fail verdict being attached anywhere to this row? It must not
      be — Blocked rows carry no verdict, only a reason and evidence.
  - **Output:** Confirmed / flagged status for each Blocked row's evidence.

---

## Stage 5: Compute the coverage summary

**Objective:** Report coverage using only the classified Executed rows from
Stage 2, split by the axes the assignment actually asks for.

- **Step 5.1 — Count distinct values from Executed rows only:**
  - **Input:** The Executed row list from Stage 2.
  - **Reasoning:**
    → How many distinct OS values, browser values, and device classes appear
      across Executed rows? Count each axis separately — do not blend them
      into one combined number.
    → What is the gap against the assignment's ideal target (3 OS × 5
      browsers × 3 device classes per screen)? State the gap plainly instead
      of rounding it away.
  - **Output:** Coverage counts per axis, plus a stated requirement gap.
- **Step 5.2 — State the Executed/Blocked totals as counted, not assumed.**
  Report the Executed count, Pass count, Fail count (with which cell and
  which finding ID it maps to), and Blocked count exactly as tallied in
  Stage 2/3/4 — never substitute a remembered number for a freshly counted
  one.

---

## Stage 6: File-name consistency check

**Objective:** Catch any evidence file that breaks the naming convention or
disagrees between raw / candidate / final for the same cell.

- **Step 6.1 — Compare names across the pipeline.** For each Executed cell,
  confirm the raw, candidate, and final file names match the same
  `T3_<screen>_Run<id>_<OS>_<browser>_<device>[_raw|_supp<N>]` pattern for
  the same cell, flagging any mismatch (wrong screen, wrong run ID, wrong
  suffix).

---

## Stage 7: Finding-ID guardrail pass

**Objective:** Confirm the findings log's treatment of unresolved IDs was not
quietly overridden.

- **Step 7.1 — Check unresolved IDs stayed unresolved.** Confirm any ID the
  findings log marks unresolved (e.g. F-019/F-020) is still reported as
  unresolved — not mapped, not filled in, not silently dropped from the
  report.

---

## Output Format

1. **Per-row status table** — all 28 manifest rows, each labeled `Executed
   (Pass|Fail)`, `Blocked (Not Executed)`, with Supplementary Validation
   entries listed separately underneath the Executed row they upgrade (never
   as their own row).
2. **Missing-artifact lists** — Executed cells missing raw/candidate/
   final/verdict; Blocked rows missing blocker evidence.
3. **Coverage summary** — counts by browser, by OS, by device class
   (Executed rows only), plus the stated requirement gap.
4. **File-name consistency report** — any mismatch found in Stage 6.
5. **Next-action suggestions** — plain, concrete suggestions only (e.g.
   "promote candidate X," "no action needed") — never an instruction to
   promote anything automatically.

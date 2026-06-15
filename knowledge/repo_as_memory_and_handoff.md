*TAGS: build, business-plan | AUDIENCE: founder + every future Claude (read at wake).*

# GOLD ARTIFACT — REPO-AS-MEMORY & THE SKINNY HANDOFF
*Captured June 5 2026, Chat 4. The biggest structural nugget of the project — it changes cost and cold-start permanently.*
*UPDATED June 7 2026, Chat 6: added THE PROPAGATION LAW (sync matrix + grep-verify + self-evolve) so banks reach every dependent view at bank-time, not at next session's audit. Added DELIVERY INTEGRITY (edit-in-place > drag-and-drop; delete-old-then-drop; watch Windows `_1`/`_2` collisions; path+action tags) — the handoff half. Matrix self-evolved: build/launch sequence → phase_roadmap.md; coaching engine → bionic_lab_spec.md; built deliverables → reports/; security/secrets → security_and_secrets.md; brand voice/language → bioniq_q_logic.md. Added DELIVERY INTEGRITY rule 6: never a batch of loose files — multi-file change = ONE complete-repo zip + replace-all-and-push (proven by the Chat-6 8-file fiasco; the full-repo replace landed clean).*

## ONE-LINE
Stop pasting fat handoffs that fill chats and cost a fortune to re-read. Keep the GOLD farm in a
**public repo a code-exec Claude fetches on demand**; the handoff shrinks to **"minutes of the
meeting" + a raw URL**. Repo = source of truth; chat = minutes.

## THE PROBLEM IT KILLS
Four sessions of: paste 7–8 files, Claude burns an hour of context reading everything, does the task,
sleeps. Expensive, slow, and knowledge re-litigated every wake. Cause: each Claude started cold with
no persistent memory and no headroom to fix the meta-problem. The repo IS the persistent memory.

## ACCESS TRUTH (verified, not assumed — stop the wrong lecture)
- **CAN:** public GitHub raw URL from a code-execution session (`curl raw.githubusercontent.com`).
  Tested June 5 2026 → HTTP 200, file downloaded.
- **CANNOT:** Netlify, Supabase, Anthropic account, **private** GitHub — all authenticated. No tokens.
- **RULE:** the line is **public vs private**, NOT GitHub-vs-not. Past Claudes wrongly told Mark
  "can't access GitHub." Public repo over raw URL is reachable. Don't repeat the error.
- **Caveat:** only sessions with code execution + network; `web_fetch` works for small docs but may
  truncate multi-MB data files (use curl for those). Not every Claude surface has code-exec → see Branches.

## THE SKINNY HANDOFF (replaces the fat kickoff)
Mark pastes: (1) the repo raw README URL, (2) a few lines of "minutes" (what we did, what's in flight).
Claude does the rest by fetching. Branch on capability:
- **A — code-exec + net (normal):** curl README → ARTIFACT_INDEX → fetch only what the task needs.
- **B — big file:** curl `/data/verified/<rolling>.txt` (not web_fetch — truncates).
- **C — "I can't do URLs / no code-exec":** repo unreachable → Mark pastes the **Vault** copy (offsite mirror).
- **D — uncovered:** ask Mark ONE question, don't guess.

## STANDING RULE FOR ALL CLAUDES
1. **Write durable work back** to the repo (file + ARTIFACT_INDEX line + commit-ready note for Mark;
   you can't push to his repo — you produce, he commits). Chat-only knowledge is lost. **A write isn't
   done until it propagates — run THE PROPAGATION LAW (below): sync every dependent view + grep-verify.**
2. **Keep the Vault current:** Mark holds an **offsite mirror** (Drive/zip) for Branch-C sessions.
   Every session that changes the repo MUST end with a **Vault-update checklist** for Mark. Never let
   the mirror drift.
3. **Request, don't assume:** need offsite material (Finn's InVideo.ai marketing zip, the Chat-3
   Pinescript, the tagging-strategy doc)? Ask Mark to drop it; then file + index it.

## THE PROPAGATION LAW (Chat 6 — added because Mark had to catch this, not the protocol)
A bank is **not done when the source doc is written.** A bank is done when **every dependent VIEW of
that change is updated AND grep-verified in the SAME session.** A decision banked in one place but not
propagated is a zombie (the TTS leak; Mark having to remind Claude to update the Flow Chart + Vision
Board). The audit catches zombies *next* session — too late, and it makes the founder the enforcement
layer. This law makes propagation a **close-out step, not a future catch.**

### THE SYNC MATRIX — when you bank/change X, you MUST also update (and verify):
**Always, every change:**
- the doc's **UPDATED** metadata + its bottom **INDEX LINE**
- the **ARTIFACT_INDEX.md** one-liner for that doc
- **master_strategy_vision.md** living log (one entry)
- **HANDOFF.md** STATE note + IN-FLIGHT/OPEN

**Conditionally, by what the change TOUCHES:**
- architecture / components / data sources / a feature → **tech_architecture_skeleton.md Mermaid +
  tech_architecture_master.svg** (the Flow Chart pair). If you edit the Mermaid but can't re-render the
  SVG, **FLAG the pair out-of-sync as an open item** — never leave it silently mismatched.
- the student journey / a touchpoint → **master_journey_flow.md** Mermaid + its rendered diagram
- the project vision → the **Live Vision Board** (live_vision_board_spec.md; once built)
- a NEW file → add it to **KICKOFF_AUDIT.md** presence list + bump its count note
- the build/launch SEQUENCE or a phase decision (what ships when) → **phase_roadmap.md**
- the COACHING engine / the Lab (how coaching is requested + delivered) → **bionic_lab_spec.md**
- the COACH'S READING METHOD (how a trade is graded across the 3 layers / how worked examples are labeled + banked) → **trade_coaching_method.md** (CORE; distinct from the Lab's *delivery* mechanics)
- a WHAT-IS-TEACHABLE / product-boundary decision (scalp vs rule-based, founder-method vs taught-product, what we may/may-not claim to teach) → **teachable_vs_unteachable_boundary.md** (the marketing+legal firewall)
- a TRADE-IMPORTER / upload-engine / journal-origin decision (CSV parsing, fill-grouping, which platform, what to port from the original app) → **trade_importer_and_journal_origin.md** (and timestamp-pin specifics → data_provenance_and_timestamp_pin.md)
- a PHYSIOLOGY / WEARABLE / trader-as-athlete decision (Oura/Apple/Garmin import, the trader-journal half, body-data-meets-psychology) → **trader_as_athlete_physiology_layer.md** (Phase 2-3 idea-parked)
- a BUILT deliverable (report / spreadsheet / printable template) → **reports/** + an ARTIFACT_INDEX entry; bank key numbers as TEXT in the relevant .md so a Claude needn't open a binary
- a SECURITY / secrets decision or threat model → **security_and_secrets.md** (and keep the KICKOFF secrets-scan honest)
- a MODEL-SELECTION / model-cost / model-data-retention decision (which Claude model handles what, pricing tiers, ZDR/retention posture) → **tech_architecture_skeleton.md** (the tiering decision) **AND** **security_and_secrets.md** (the retention/ZDR gate) — these two move together; never bank one without the other
- a BRAND VOICE / language / vocabulary / tagline decision → **bioniq_q_logic.md** (the Q-logic)
- a per-AREA build detail (a component, its status, the "meat") → that area's DEEP doc (e.g. area 8 → **qubed_indicator_spec.md**); keep **build_blueprint.md** as the terse index that points to it
- a RAW source doc Mark made (recipe, essay, blueprint, screenshot-of-record) → the numbered **content/CONTENT_INDEX.md** shelf (recipe internals stay PRIVATE/LOCAL — index it, don't paste it)
- a HOW-WE-WORK / process / method decision (man+machine operating rules) → **operating_system.md** + (if it's an entry rule) the root **AGENTS.md**
- it contradicts/sharpens a RELATED doc → update that doc, label **CHANGED FROM PRIOR**

### THE VERIFY STEP (CONFIRM = AUDIT, applied to propagation)
Before sleep, for **each view the matrix required for this change, grep the new marker in it THIS
session.** If the marker isn't in every required view, the bank is NOT done. The freshly-run grep is the
proof — not your memory, exactly like a push-confirm.

### SELF-EVOLVE (so the backend improves without Mark policing it)
When a session adds a **NEW durable surface/view** (the Vision Board was added this way in Chat 6), you
MUST add it to this matrix **in the same commit.** The matrix is the franchise asset: anyone can run it,
it maintains itself, no founder required. Find a propagation gap? **Fix the matrix**, don't just patch
the one doc — that is how the backend keeps evolving.

## DELIVERY INTEGRITY (Chat 6 — the handoff half of the Propagation Law)
Root cause of three botched pushes in one session: **Windows drag-and-drop never overwrites — on a
name clash it silently appends `_1`/`_2`.** The file *looks* present, so no one notices; git commits a
NEW file beside the stale one, every reference still points at the original name, and it only surfaces
at the next audit. The fix lives on the DELIVERY side so it can't depend on the founder noticing.
Rules (written for a **GitHub-web founder, not a terminal user**):
1. **Prefer edit-in-place on GitHub web** — open the file → pencil → change content/filename → commit.
   Nothing leaves GitHub, so nothing can collide. This is the default for single-file changes.
2. **Replacing from a download? DELETE the old file first, THEN drop the new one** into the empty spot —
   and **check for a `_1`/`_2` suffix before committing** (Windows adds it silently on a name clash).
3. **Push lists carry full repo path + an action tag** — `REPLACE knowledge/foo.md`, `DELETE foo.md`,
   `RENAME a→b` — never a bare filename (a bare name is how a file lands in the wrong folder).
4. **The dated snapshot zip is the authoritative tree** — diff against it when unsure where a file goes.
5. **The audit verifies filenames AND the active-file count every wake** — a `_N` collision shows up as
   count-off + canonical-name-missing. (Already wired into KICKOFF_AUDIT under the Propagation Law.)
**Claude's side:** deliver small edits **edit-in-place** ("open file → paste this at this anchor"),
not as files to drag, whenever the change is small enough to do so.
6. **NEVER hand Mark a batch of separate files** that each need open-in-Notepad → save → delete-old →
   add. The Chat-6 8-file batch proved this fails for a Windows/GitHub-web founder (lost track, wrong
   folders, `_N` collisions). For a **multi-file change, deliver ONE complete-repo zip + a single
   "replace-all-and-push" instruction** — extract, copy all over a FRESH clone choosing **"Replace the
   files in the destination"** (never "keep both" — that is what spawns `_1`/`_2`), then commit+push once.
   One artifact, one action. Single-file changes still go edit-in-place per rule 1.

## HOW MARK & CLAUDE WORK (the loop + numbered addressing — Chat 6)
The repo is the ONE source (Claude banks in nano time). Mark reads his local clone in a nicer window (not
always GitHub). To work efficiently:
- **Numbered addressing.** build_blueprint.md numbers everything: areas 1-11, pieces like 8.1 / 8.4. Mark
  says a number ("open 8.4") and Claude opens that node — no pasting, no re-explaining context.
- **The loop:** discuss/debate → Claude updates the source → Mark reads later → flags edits by number →
  repeat. Mark can also edit a .xlsx/.docx and send it back; Claude reads the FILE directly (no
  screen-caps/retyping) and returns a clean image/PDF or banks it.
- **Read vs act:** to READ a node, ask in text ("show me 8.2") — Claude prints it. Clickable rendered maps
  are a cheap on-demand VIEW generated from the files (always current), but they are action-buttons, not
  expanders. Design note that bit us twice → a real PRODUCT rule: **tap-to-expand ≠ tap-to-act** — never let
  a "look closer" gesture fire an action or burn a credit.
- **Per-area DEEP docs:** the blueprint is the index; heavy areas get a growing spec (e.g.
  qubed_indicator_spec.md = area 8) with a build-status per component. Raw source docs Mark made live on the
  numbered /content shelf (content/CONTENT_INDEX.md). Proprietary build-recipes (e.g. how the indicators are
  made) stay PRIVATE/LOCAL — the public repo holds the READ (what it tells us per strat), never the recipe.

## WHY IT'S MOAT
Cheaper context, faster cold-starts, zero re-litigation, and a new-Claude experience that's "read the
README, you're 90% caught up." Pairs with the verified/unverified data gate (Claudes read only the
verified store). This is the infrastructure the coaching product's continuity rides on.

## INDEX ENTRY (paste into ARTIFACT_INDEX.md)
`repo_as_memory_and_handoff.md | build, business-plan | Public repo = Claude-fetchable memory (raw URL, code-exec; verified June 5). Skinny handoff = minutes + URL, branched on capability. Standing rule: write back + keep Mark's offsite Vault mirror current. THE PROPAGATION LAW (Chat 6): a bank isn't done until every dependent view is synced + grep-verified the same session (sync matrix covers index/log/HANDOFF + Flow Chart Mermaid+SVG + Vision Board + cross-refs); self-evolving (new surface → add to matrix same commit). DELIVERY INTEGRITY (Chat 6): edit-in-place on GitHub web beats drag-and-drop; delete-old-then-drop; watch Windows `_1`/`_2` silent collisions; push lists carry full path + action tag. Access truth: public-vs-private, not GitHub-vs-not.`

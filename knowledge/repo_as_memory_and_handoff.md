*TAGS: build, business-plan | AUDIENCE: founder + every future Claude (read at wake).*

# GOLD ARTIFACT — REPO-AS-MEMORY & THE SKINNY HANDOFF
*Captured June 5 2026, Chat 4. The biggest structural nugget of the project — it changes cost and cold-start permanently.*
*UPDATED June 7 2026, Chat 6: added THE PROPAGATION LAW (sync matrix + grep-verify + self-evolve) so banks reach every dependent view at bank-time, not at next session's audit.*

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

## WHY IT'S MOAT
Cheaper context, faster cold-starts, zero re-litigation, and a new-Claude experience that's "read the
README, you're 90% caught up." Pairs with the verified/unverified data gate (Claudes read only the
verified store). This is the infrastructure the coaching product's continuity rides on.

## INDEX ENTRY (paste into ARTIFACT_INDEX.md)
`repo_as_memory_and_handoff.md | build, business-plan | Public repo = Claude-fetchable memory (raw URL, code-exec; verified June 5). Skinny handoff = minutes + URL, branched on capability. Standing rule: write back + keep Mark's offsite Vault mirror current. THE PROPAGATION LAW (Chat 6): a bank isn't done until every dependent view is synced + grep-verified the same session (sync matrix covers index/log/HANDOFF + Flow Chart Mermaid+SVG + Vision Board + cross-refs); self-evolving (new surface → add to matrix same commit). Access truth: public-vs-private, not GitHub-vs-not.`

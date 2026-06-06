*TAGS: build, business-plan | AUDIENCE: founder + every future Claude (read at wake).*

# GOLD ARTIFACT — REPO-AS-MEMORY & THE SKINNY HANDOFF
*Captured June 5 2026, Chat 4. The biggest structural nugget of the project — it changes cost and cold-start permanently.*

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
   you can't push to his repo — you produce, he commits). Chat-only knowledge is lost.
2. **Keep the Vault current:** Mark holds an **offsite mirror** (Drive/zip) for Branch-C sessions.
   Every session that changes the repo MUST end with a **Vault-update checklist** for Mark. Never let
   the mirror drift.
3. **Request, don't assume:** need offsite material (Finn's InVideo.ai marketing zip, the Chat-3
   Pinescript, the tagging-strategy doc)? Ask Mark to drop it; then file + index it.

## WHY IT'S MOAT
Cheaper context, faster cold-starts, zero re-litigation, and a new-Claude experience that's "read the
README, you're 90% caught up." Pairs with the verified/unverified data gate (Claudes read only the
verified store). This is the infrastructure the coaching product's continuity rides on.

## INDEX ENTRY (paste into ARTIFACT_INDEX.md)
`repo_as_memory_and_handoff.md | build, business-plan | Public repo = Claude-fetchable memory (raw URL, code-exec; verified June 5). Skinny handoff = minutes + URL, branched on capability. Standing rule: write back + keep Mark's offsite Vault mirror current. Access truth: public-vs-private, not GitHub-vs-not.`

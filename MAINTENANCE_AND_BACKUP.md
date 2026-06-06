# MAINTENANCE & BACKUP — THE LAW (every Claude, every session)
*Read after README. These are RULES, not suggestions. The goldmine is the project's memory; if it
rots or drifts, the project loses everything between chats. Treat it like production.*

---

## WHERE THE GOLDMINE LIVES (two copies, by design)
1. **ONLINE — the public repo** = the *canonical, living* source. A code-exec Claude fetches from it.
   Mark commits (Claude can't push). This is the truth.
2. **OFFSITE — "the Vault"** (Mark's Drive / dated zips; rename as you like) = the *backup + fallback*.
   Used when a session can't reach URLs (README §Access Truth). The Vault MUST mirror the repo.
Neither holds secrets — keys/creds/customer data never enter either (README §2).

## WHAT'S IN THE GOLDMINE (so you know what you're maintaining)
- `README.md` — orientation + access truth + handoff branches (read first).
- `HANDOFF.md` — the live "minutes of the meeting" (the skinny handoff).
- `ARTIFACT_INDEX.md` — the map: one line per artifact.
- `MAINTENANCE_AND_BACKUP.md` — this law.
- `/knowledge` — GOLD nuggets & strat IP (gate, cues, taxonomy, provenance, voice, repo-as-memory).
- `/data` — `/verified` (passed the gate, Claudes read this) and `/unverified` (raw drop, untrusted).
- `/charts` — built lesson/kitchen-sink/viewport/upload artifacts.
- `/build` — current builder scripts.
- `/marketing`, `/voices` — assets (drop Finn's InVideo.ai zip; TTS config).
- `/reference` — lineage: the original fat kickoff, pre-pin charts/builders, and `/samples`
  (real Bookmap/GEX/TV chart samples + the TV timestamp-anchor) and `/session_screenshots`.

---

## RULE SET A — EVERY SESSION (start → during → end)
**A1 (start):** Pull & orient. Read README → ARTIFACT_INDEX → HANDOFF. If you can't reach the repo,
say so and ask Mark for the Vault copy (README Branch C). Don't proceed blind.
**A2 (during):** Verify before you trust (PHD). Never edit from memory — open the file. Any data you
touch must be from `/data/verified`; never read `/data/unverified` as truth.
**A3 (write-back):** The instant you create or change durable knowledge (a nugget, doc, chart,
builder), SAVE it to the correct folder AND add/lengthen its line in ARTIFACT_INDEX.md. Chat-only
knowledge is considered lost.
**A4 (end — see Rule Set C):** Run the close-out before you sleep. No exceptions.

## RULE SET B — THE BACKUP SCHEME (rules-based, because Claude can't push)
**B1:** The repo is canonical; the Vault is the backup. Both must agree after every session that
changed anything.
**B2 (snapshot):** Any session that creates/changes goldmine content MUST, before sleep, produce ONE
**timestamped snapshot zip** of the entire goldmine: `bionicbutterfly_goldmine_YYYYMMDD[_n].zip`, and
hand it to Mark via present_files.
**B3 (never overwrite history):** Snapshots are dated and **append-only** — never reuse a prior
snapshot's name. The repo holds the living files; the Vault holds the dated snapshots = backup
history. Mark keeps at least the **last 5** snapshots in the Vault; older ones may be archived.
**B4 (no stale snapshot):** Never cut a snapshot until README, ARTIFACT_INDEX, and HANDOFF reflect
reality (A3 done). A snapshot of a stale index is worse than none.
**B5 (data integrity):** The verified/unverified gate (README §data, and the gate checklist) governs
`/data`. Never promote `unverified → verified` without passing the gate. A snapshot may contain
unverified data, but it must stay in `/unverified`.
**B6 (Mark's two actions):** Each close-out you tell Mark exactly: (a) which changed files to **commit**
to the repo, and (b) to **drop the snapshot zip into the Vault**. That's the whole backup ritual.

## RULE SET C — PREPARING THE HANDOFF (same maintenance, applied at session end)
Before you sleep, in order:
**C1:** Ensure every artifact you made is filed in its folder (A3) and indexed.
**C2:** Update `HANDOFF.md` — refresh "STATE AS OF LAST SESSION" and the "IN FLIGHT / OPEN" list
(check off done, add new). Keep it SHORT; the repo carries detail.
**C3:** Cut the dated snapshot zip (B2–B4).
**C4:** Produce the **VAULT-UPDATE CHECKLIST** for Mark — a plain list: files to commit, the snapshot
to store, anything offsite you still need him to import (e.g., Finn's marketing zip, Chat-3 Pinescript,
tagging_strategy.md).
**C5:** Confirm the skinny handoff is armed: README raw URL present, branch instructions intact, so
the next Claude reads README and is 90% caught up. If the repo URL is still a placeholder, flag it.
**C6:** State plainly to Mark: "I can't commit or push — here's what to commit and store." Then stop.

---
## THE 10-SECOND VERSION (if you remember nothing else)
Open files, don't trust memory. Save durable work to the repo + index it. Before sleeping: update
HANDOFF, cut a dated snapshot zip, give Mark his commit-and-store checklist. Verified data only.

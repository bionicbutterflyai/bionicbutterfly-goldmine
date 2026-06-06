# BIONICBUTTERFLY — THE GOLDMINE (repo-as-memory)
*Owner: Mark. Maintained by: whichever Claude is awake. Read this FIRST, every session.*
*Purpose: kill the fat handoff. The repo is the source of truth; the chat is just "minutes of the meeting."*

---

## 0. THE ONE-PARAGRAPH ORIENTATION (a new Claude reads this and is 90% caught up)
You are continuing bionicbutterfly.ai — a Claude-powered trading-accountability / coaching platform.
Mark is the founder and the continuity; you reason over what's in THIS repo plus a short "minutes"
note he pastes. Be the **PHD — Professional Honest Developer**: feasibility over hype, look-don't-
assume (open and verify files, never trust memory), flag nuggets, never fake confidence at a gap —
ASK. Credit is Mark's; you're the tool. Everything you need is in the folders below — **fetch on
demand, don't ask Mark to paste it.** When you create or change durable knowledge, **write it back to
the repo** (see §4) so the next Claude inherits it.

---

## 1. ACCESS TRUTH — what a Claude CAN and CANNOT reach (stop re-lecturing Mark)
- **CAN:** a **public** GitHub repo over a **raw URL**, from a session with **code execution**
  (`curl`/`wget` `raw.githubusercontent.com`). *Verified working June 5 2026 — HTTP 200.*
- **CAN (limited):** `web_fetch` a public raw URL — but it may TRUNCATE multi-MB files. Use code-exec
  + curl for anything big (data files). web_fetch is fine for small docs.
- **CANNOT:** Netlify, Supabase, the Anthropic account, or any **private/authenticated** system.
  Private GitHub also = no (needs a token; never paste tokens, never handle them).
- **THE RULE:** the distinction is **public-vs-private**, NOT "GitHub-vs-not." Past Claudes wrongly
  lumped public GitHub in with the private systems. It isn't. Don't repeat that error.

## 2. FOLDER HIERARCHY (topic = folders; EXPOSURE = the guardrail)
Partition by what's safe to expose, not just by subject. (Names are Mark's to rename.)
```
/goldmine
├── README.md                  ← this file. Read first, always.
├── HANDOFF.md                 ← the live "minutes of the meeting" (see §3). Short.
├── ARTIFACT_INDEX.md          ← one line per doc: title | tags | one-liner. The map.
├── /knowledge                 ← GOLD nuggets & strategy (PUBLIC-SAFE: IP, not secrets)
│   ├── strat_zone_taxonomy.md
│   ├── data_provenance_and_timestamp_pin.md
│   ├── voice_tts_decision.md
│   ├── repo_as_memory_and_handoff.md   ← (this architecture, banked)
│   ├── coaching_cue_library.md (+ additions)
│   └── tagging_strategy.md     ← (still in Mark's Chat-3 zip; import it)
├── /data                      ← bar exports (PUBLIC-SAFE: market data isn't secret)
│   ├── /unverified            ← raw drop zone. New uploads land here. NOT trusted.
│   └── /verified              ← promoted only after passing the gate (§5). Claudes read THIS.
├── /charts                    ← built artifacts (lesson charts, kitchen-sink, viewport, upload box)
├── /marketing                 ← copy, assets, the InVideo.ai zip from Finn (PUBLIC-SAFE)
├── /voices                    ← TTS samples / config (see voice_tts_decision.md)
└── /build                     ← builder scripts (calc_dpmo.py, build_*.py, calc_levels.py, etc.)

   NEVER IN THIS REPO (keep private / offsite — see §6 "THE VAULT"):
   keys, Supabase creds, tokens, customer data, the verbatim 3rd-party Pinescript if license-restricted.
```
Tagging still governs retrieval scope (per tagging_strategy.md): `legal` / `business-plan` stay OUT
of support-Claude's reach. Storage exposure and tag scope are two layers of the same instinct.

## 3. HANDOFF BLUEPRINT — branch on what THIS Claude can do
The handoff is no longer fat. It's a short note + a capability branch. Mark pastes HANDOFF.md
(minutes) and the repo raw URL. Then:

**Branch A — Claude HAS code execution + network (the cheap, normal case):**
> "Goldmine raw URL: <raw.githubusercontent.com/.../README.md>. Pull README + ARTIFACT_INDEX, then
> fetch only what the task needs. Minutes are in HANDOFF.md."
Claude curls README → index → fetches on demand. Mark pastes almost nothing. Context stays cheap.

**Branch B — Claude can fetch but file is big (e.g., data):**
> Use curl in code-exec (not web_fetch — it truncates). Pull `/data/verified/<rolling>.txt`.

**Branch C — Claude says "I can't do URLs / no code execution" (it happens):**
> Then the repo is unreachable this session. Mark pastes the **offsite copy** of the needed folder
> (see §6). This is the fallback, and it's WHY the offsite mirror must be kept current (§4).

**Branch D — brand-new capability/task not covered:** Claude asks Mark ONE question, doesn't guess.

## 4. THE STANDING RULE FOR ALL CLAUDES (write-back + keep the offsite mirror current)
1. **Write durable work back to the repo.** Any new nugget, doc, chart, or builder you create →
   save it to the right folder (with the standard metadata block — see METADATA_SCHEMA.md), add its
   line to ARTIFACT_INDEX.md, and note it in HANDOFF.md. Knowledge that only lives in the chat is lost.
   **Claude can PULL (read raw URL) but CANNOT PUSH** — no access to Mark's GitHub or his machine. The
   loop is three steps: (1) Claude produces files + hands them to Mark, (2) Mark adds them to his local
   repo, (3) Mark pushes to GitHub. Claude must state this plainly and never imply it can commit.
2. **Keep "THE VAULT" current (§6).** Because some sessions can't reach the repo (Branch C), Mark
   keeps an **offsite mirror** of the goldmine (his Drive / downloads / a zip). During EVERY session,
   if you change anything in the repo, you must **tell Mark which vault files he needs to update**, in
   a clear checklist at the end of the session. Never let the offsite mirror drift from the repo.
3. **Request, don't assume.** If you need data/marketing Mark stores offsite (e.g., Finn's InVideo.ai
   zip, the Chat-3 Pinescript), ASK him to drop it; then file it and index it.

## 5. DATA GATE — verified vs unverified (two-step; protects every future session)
New bar export → lands in `/data/unverified/`. It is promoted to `/data/verified/` ONLY after passing:
- chronological order (no out-of-sequence rows),
- contiguity (no unexpected minute gaps beyond the daily 17:00–18:00 ET halt),
- timestamp convention confirmed (close-stamp + UTC) against a known-good anchor candle,
- sane OHLC (high≥low, etc.), and the expected date range with gaps flagged.
**OPEN DECISION (Mark to set):** fully-automated promote-on-pass, or **human-in-the-loop** (script
flags pass/fail, Mark clicks promote). Recommended: human-in-the-loop until the checks prove out.
*(This is the broker-onboarding + timestamp-pin nuggets turned into process.)*

## 6. "THE VAULT" — Mark's offsite mirror (the name is a placeholder; rename it)
The repo is online truth; **the Vault is the offline insurance** for sessions that can't reach the
repo (Branch C) or for things that can't be public. Mark holds it (Drive / zip / downloads). The
Vault must mirror the goldmine. Every Claude's job: keep Mark's Vault-update checklist current at
session end. If a Claude can't reach URLs, Mark feeds it the Vault copy instead.

---
## QUICKSTART FOR A WAKING CLAUDE
1. Read this README + ARTIFACT_INDEX.md.  2. Read HANDOFF.md (minutes).  3. Read MAINTENANCE_AND_BACKUP.md (the law).  4. Fetch only what the task
needs.  5. Be the PHD.  6. Write durable work back + cut a dated snapshot + give Mark his Vault-update checklist before you sleep.

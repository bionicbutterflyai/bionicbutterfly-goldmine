# HANDOFF — MINUTES OF THE MEETING
*Paste this (or its current version) at the start of a new chat, with the repo raw README URL. Keep it SHORT — the repo carries the detail.*

## ⚡ FIRST LINE — THE CARPENTER TEST (before anything else)
This must be a TOOL-ENABLED session (code execution + web/file tools). Prove it NOW: try to `curl`/fetch
the README raw URL below.
- **Pulls the file → master carpenter, full belt. Proceed.**
- **Can't reach it → wrong room. STOP, tell Mark "no tools — switch rooms," and wait.** Do NOT limp
  through a build session hand-fed by Mark; that wastes both your time. (Strategy talk is fine tool-less;
  BUILDING requires the belt — verifying files, running builders, auditing the repo.)
Mark's rule: no half-Claude on build work. The audit step below doubles as this test.

## REPO (fetch this first)
Raw README: `https://raw.githubusercontent.com/bionicbutterflyai/bionicbutterfly-goldmine/main/README.md`
Repo: `https://github.com/bionicbutterflyai/bionicbutterfly-goldmine` (PUBLIC, verified fetchable 2026-06-06).
→ If you have code execution: `curl` README + ARTIFACT_INDEX, then fetch on demand. Be the PHD.
→ If you CANNOT do URLs/code: tell Mark; he'll paste the Vault copy of what you need.
→ NOTE: the live website is a SEPARATE repo (`bionicbutterfly`, private, Netlify-deployed). Never mix the two.

## WHO / WHAT (one breath)
bionicbutterfly.ai — Claude-powered trading-accountability/coaching platform. Mark = founder +
continuity. You = the PHD (honest dev, look-don't-assume, flag nuggets, ask at gaps). Credit is Mark's.

## STATE AS OF LAST SESSION (edit each time)
- **Chat 4 cont. (Jun 6 2026):** Drew the **MASTER JOURNEY FLOW** — the coordinate system every
  Claude now orients to (`knowledge/master_journey_flow.md`, matched diagram+Mermaid pair). Locked the
  **pairing rule** (every flow = rendered diagram + Mermaid source, same commit). Built the **CVD
  indicator** (v7 chart, HA cumulative delta + 50 EMA, own stacked pane) and an **app-shell layout**
  concept (nothing-above-chart; mock file intentionally NOT kept). Re-filed all original fat-handoff
  files; added METADATA_SCHEMA.md + HIERARCHY.md v2 (exposure-first) + MAINTENANCE_AND_BACKUP.md.
  Resolved Finn: he sends only the Butterfly/in-product set pre-sorted (MANIFEST approved, files NOT
  downloaded yet); Matrix/character/voice theme stays PARKED in Mark's account, not the repo.
- Earlier (Jun 4–5): timestamp pin (close-stamp fix, v6); kitchen-sink levels chart; merged
  upload-box + morphing lesson viewport; GOLD docs (strat_zone_taxonomy +7 extensions, data_provenance,
  voice_tts, repo_as_memory, dpmo_gate, coaching_cue_additions).
- Stack (cannot touch from chat): GitHub + Netlify + Supabase; credit_ledger live.

## IN FLIGHT / OPEN (edit each time)
- [ ] **NEXT CLAUDE'S MAIN TASK: build the MASTER TECH-ARCHITECTURE flow** (separate from the journey).
      Components: Ad hook → AI agent → funnel → Netlify → GitHub → Supabase → web platform → Anthropic
      API → (large) market-datafeed API → ElevenLabs API → etc. Draw the master "how the whole thing is
      wired" diagram FIRST (matched pair), THEN break each component into its own child flow. Start
      fresh & spacious — big diagram, don't crowd it.
- [ ] **Mark has NOT moved files to GitHub yet** — the goldmine repo still doesn't exist. Snapshot zip
      is in outputs/Vault; repo creation + first push pending. Raw URL above is a placeholder.
- [ ] Bank 2 nuggets still owed: **brand_funnel_architecture** (hook-skin/sober-spine/contrast=conversion;
      now EXTENDED — the whole foyer is the sober-spine proving the hook didn't lie); **two_strategy_split**
      (144 trend-continuation + 1-in-20 stand-down / Red-Yellow NYO breakout). OPEN Q: is the breakout
      9:30-zones ONLY or the same pop-retest-continue off ALL zone boxes? (Mark unanswered.)
- [x] DONE: public goldmine repo created + pushed + verified fetchable (bionicbutterflyai/bionicbutterfly-goldmine).
- [ ] Import from Mark's offsite: Chat-3 verbatim Pinescript; tagging_strategy.md; Finn's Butterfly zip when sent.
- [ ] Set the data-gate policy: auto-promote vs human-in-the-loop (recommend human-in-the-loop).
- [ ] Parked builds: fill-on-relevance counterpart chart; Bookmap/GEX confluence CUE #3; marry the REAL
      v7 chart into the app-shell (replaces the discarded mock).
- [ ] System-only trading account (Mark's own decision): clean track record + canonical verified-data source.
- 3 open FORKS in master_journey_flow.md: Mark-is-product→system-is-product; funnel-must-remember
  (build not buy); live-trading Discord if/when (paid-only).
- [ ] LOCKED (don't re-litigate): coaching business; master-plan strategy; brand = no Oracle character /
      no caterpillar arc / unnamed "voice from the data."

## BEFORE YOU SLEEP (every session)
Write durable work back to the repo (file + ARTIFACT_INDEX line + commit note for Mark), update the
IN-FLIGHT list above, and give Mark his **Vault-update checklist**.

## METADATA (read METADATA_SCHEMA.md — every artifact carries the standard block)
Every doc opens with: `TAGS | AUDIENCE` then `CREATED | UPDATED | STATUS` then `SUPERSEDES | RELATED`.
Index lines are `path | tags | status | one-liner`. Need a NEW metadata field? Add it to
METADATA_SCHEMA.md first, note it here, THEN use it — never ad-hoc.

## THE WRITE LOOP (how work gets to GitHub — Claude can pull, NOT push)
Claude reads from the public repo (curl raw URL) but **cannot push** — no access to your GitHub or
your local machine. So the loop is three steps, and Claude must say so plainly, never imply it can commit:
1. **Claude** produces files in its sandbox + hands them to Mark (present_files / dated zip) + lists what changed.
2. **Mark** drops those files into his local repo folder.
3. **Mark** pushes to GitHub.
Result: next Claude pulls the updated repo. (Same reason backups are dated zips Mark stores in the Vault.)

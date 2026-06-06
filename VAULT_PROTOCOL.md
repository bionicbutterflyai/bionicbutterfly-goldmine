# VAULT PROTOCOL — one truth, no sprawl
*TAGS: build, support | AUDIENCE: founder (Mark) — this is YOUR offsite discipline.*
*CREATED: 2026-06-06, Chat 4 | UPDATED: 2026-06-06, Chat 4 | STATUS: captured*
*RELATED: MAINTENANCE_AND_BACKUP.md, README.md*

## THE ONE RULE (everything else follows from this)
**The GitHub goldmine repo is the ONLY source of truth.** Not Dropbox, not Downloads, not a chat.
The Vault (offsite/Dropbox) holds exactly TWO things: (1) the dated snapshot ZIPS as backup, and
(2) originals that are NOT yet in the repo. It NEVER holds loose working copies of files that already
live in the repo — those are how version sprawl is born (see: three strat_zone_taxonomy copies).

## WHY THIS DOC EXISTS
The Dropbox folder grew three copies of the same doc (`_1`, `_2`) because each repo update got saved
ALONGSIDE the old one instead of replacing the truth. The repo's version control already keeps
history — so loose dated copies are redundant AND dangerous (you can't tell which is current).

## THE VAULT FOLDER SCHEME (replace the flat mess)
```
BIONICBUTTERFLY VAULT/
├── snapshots/        ← dated goldmine zips ONLY (bionicbutterfly_goldmine_YYYYMMDD.zip). Keep last 5.
├── to-import/        ← originals NOT yet in the repo, waiting to be filed (Chat-3 Pinescript, etc.)
│                       Once imported into the repo, DELETE from here. This folder should usually be near-empty.
└── orphans-keep/     ← things deliberately kept offsite, never in the repo (ANTHROPIC INV CREDITS,
                        Matrix-theme parked IP, raw heavy media). Stuff that's yours but not Claude's memory.
```
That's it. Three folders. No loose .md/.html/.txt working copies — those live in the repo.

## THE UPDATE PROTOCOL (how to never collect versions again)
When a Claude hands you an updated file:
1. The file goes into the **repo** (local clone → overwrite the old one → commit → push). Git keeps the
   old version in history automatically. You do NOT keep a dated copy.
2. The only offsite artifact per session is the **dated snapshot zip** → `snapshots/`. That IS your
   backup history. One zip per session, never overwrite a date.
3. If you're tempted to "save a copy just in case" — don't. The repo + the snapshot zip already are
   the copy. Saving a third loose copy is the sprawl.
4. Rule of thumb: **if it's in the repo, it does NOT live loose in the Vault.** Ever.

## CLEANUP OF THE CURRENT DROPBOX MESS (one-time)
- `GOLD_strat_zone_taxonomy.md`, `_1`, `_2` → DELETE all three (canonical is in repo `knowledge/`).
- `GOLD_voice_tts_decision.md`, `lesson_viewport.html`, `trade_journal_upload_box.html`,
  `MNQ 06-26 April to June 5 noon Last.txt` → DELETE (all in the repo already, current).
- `ANTHROPIC INV CREDITS` → move to `orphans-keep/` (yours, not Claude's memory).
- `INCUBATOR COURSE DRAFT 053126.txt` → move to `to-import/` (decide: file into repo `knowledge/` as a
  course-draft, or it's superseded by the master_journey_flow + curriculum work — review on import).

## CANONICAL FILE LIST — what SHOULD exist, and WHERE (the audit reference)
**In the GitHub repo (the truth) — 48 files:**
- root: README, HANDOFF, ARTIFACT_INDEX, METADATA_SCHEMA, MAINTENANCE_AND_BACKUP, HIERARCHY, FINN_FOLDER_SPEC
- knowledge/: master_journey_flow, brand_funnel_architecture, two_strategy_split, strat_zone_taxonomy,
  dpmo_gate_indicator, coaching_cue_library_additions, data_provenance_and_timestamp_pin,
  voice_tts_decision, repo_as_memory_and_handoff
- charts/: trade_lesson_june4_dpmo_v6, trade_lesson_june4_kitchensink, trade_lesson_june4_v7_cvd,
  lesson_viewport, trade_journal_upload_box
- build/: build_v6, build_v7, build_ks, build_viewport, calc_dpmo_v6, calc_dpmo_v7, calc_levels
- data/verified/: MNQ_06-26_June_Last, MNQ_06-26_060426_KNOWNGOOD_Last
- data/unverified/: MNQ_06-26_April_to_June_5_noon_Last  (Apr 2-18 gap — needs gate review)
- reference/: CLAUDE4_KICKOFF_ORIGINAL, pre-pin charts + builders, samples/, session_screenshots/
- marketing/ + voices/: placeholders

**In the Vault offsite — NOT in the repo:**
- snapshots/ : every dated zip
- to-import/ : Chat-3 verbatim Pinescript (DPMO gate exact math); tagging_strategy.md (retrieval
  scope rules — legal/business-plan never reach support-Claude); Finn's Butterfly set (parked at Finn's,
  pull only when code is ready for "dress and makeup" — NOT downloaded now); INCUBATOR COURSE DRAFT (review)
- orphans-keep/ : ANTHROPIC INV CREDITS; Matrix-theme parked IP; raw heavy media

## START-FRESH OPTION (Mark's call)
Cleanest move: make a NEW empty `BIONICBUTTERFLY VAULT/` with the three folders above, drop in only the
current snapshot zip + the two orphans + the to-import originals, and abandon the old sprawled folder.
Don't migrate the mess — start clean and let the repo be the truth.

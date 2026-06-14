*TAGS: build, support, business-plan | AUDIENCE: founder + every future Claude building the trade-importer / upload engine.*
*CREATED: 2026-06-14, Chat 7 | UPDATED: 2026-06-14, Chat 7 | STATUS: captured*
*SUPERSEDES: — | RELATED: tech_architecture_skeleton.md, data_provenance_and_timestamp_pin.md, trade_coaching_method.md, teachable_vs_unteachable_boundary.md*

# GOLD — THE ORIGINAL JOURNAL APP + THE REUSABLE TRADE IMPORTER (Chat 7)

## THE LINEAGE (two codebases — don't confuse them)
There are **two separate projects:**
1. **The ORIGINAL journal app** — a single self-contained HTML file ("Trade Journal," v2.2), deployed on
   **Netlify, NOT Git-linked** (source was only the live deploy + the Claude-1 chat; nothing on Mark's
   machine — the "swap the HTML online" workflow). **Source RECOVERED Chat 7** via right-click view-source;
   full HTML reviewed and secrets-scanned (clean — API key is user-entered into localStorage, never
   hardcoded). This app is **live with ~39 real trades over 6 days.**
2. **The CURRENT platform** (`bionicbutterfly`, Netlify + Supabase + GitHub) — the rebuild. **This is the
   venture.** Claude 1 saw the original journal and said "start over with GitHub + Supabase," which became
   this platform.

**DECISION (settled):** the original journal app is **abandoned-by-choice, a PARTS DONOR — not a path to
revive.** Mark stopped finishing it when he realized he couldn't build both; the platform is the project.
Build plan is **unchanged** by recovering it. Port the useful logic; do not resurrect the app.

## REUSABLE GOLD (port into the platform's machine-zone)
- **The NinjaTrader CSV parser** (`parseCSV()`) — proven, clean, instrument-agnostic. Parses NT grid export
  (Profit, Commission, Qty, Entry/Exit price, MAE/MFE, Market pos., timestamps), de-dupes on re-import,
  computes avg entry, duration, MAE/MFE, win/loss. This is the "took timeframe tweaks but then exact"
  importer. **Reuse-don't-rebuild** — it's the upload engine's machine-zone import adapter (NT-first;
  other platforms deferred to per-student demand, per teachable_vs_unteachable_boundary.md).
- **Reference DESIGNS to adapt (not re-invent):** the **tag taxonomy** (setups / positives / negatives —
  negatives already include FOMO, Revenge trade, Moved stop, Cut winner early = the Layer-4 behavioral tags
  from trade_coaching_method.md); the **per-trade screenshot model**; the **notebook** (narration) structure;
  and an **"AI Insights" tab that already calls Claude as a coach** (proof-of-concept the coach-on-journal
  loop works).

## THE FILL-GROUPING DECISION — manual merge, NOT the 10s auto-window (CHANGED FROM the original app)
The original app auto-groups fills within **10 seconds** into one logical trade. **Mark's insight** (bank as
his): his average trade is ~9s, so a 10s window auto-merges his scale-in/scale-out without the manual
"merge trades" click — he encoded *his own behavioral tempo* as the threshold.
- **DECISION for THIS product: manual merge-by-click, NOT the 10s auto-window.** The reason is the keeper:
  **"one trade" is TIME-defined for a scalper, but INTENT-defined for a level-to-level trader.** A
  level-to-level student legitimately takes half at TP1, lets the runner run, maybe adds on a retest — legs
  **minutes apart, one idea.** No time-window can catch that, because what makes them one trade is the
  trader's *plan*, not the clock. Only the trader knows intent → manual merge respects it. The 10s rule
  would silently mis-group the exact audience the product is for.
- The **10s window stays as Mark's scalper R&D**, explicitly NOT the product default — another instance of
  the founder-method / taught-product boundary (a scalper optimization that doesn't transfer to the
  level-to-level student).

## WHAT IS NOT REUSED
- **localStorage** — the original app stores everything in one browser (single-user, no backend). This is
  the ONE layer the Supabase rebuild correctly replaces. The parser doesn't care where data lands; it just
  returns trade objects, so it ports cleanly onto Supabase.
- **Student Zero's fork** — the first student extended the original with his own Claude (more "bells and whistles"), but his
  AI section is **very trader-manual-input** to get a response back. Banked as a **what-NOT-to-do reference**:
  it's the clunky "type everything in" coach the platform's voice-engaged, journal-reading coach is designed
  to remove. (Inferior fork; not a source.)

## APPEND-NEVER-OVERWRITE (a product principle surfaced this session)
When Mark sent journal copies to the first student, that student kept *editing Mark's own entries/tags* until Mark
said "STOP messing with me." That annoyance is a **real product requirement:** the system must **never
silently alter a trader's own journal entries, tags, or trades** — the coach may *add* (auto-tags, like the
FOMO tagger), *suggest*, and *grade*, but must **append, never overwrite** the trader's record. The moment a
student feels the system is "messing with" their journal, the trust the accountability model depends on is
gone.

## INDEX LINE
`knowledge/trade_importer_and_journal_origin.md | build, support, business-plan | PUBLIC | captured | TWO codebases: (1) the ORIGINAL journal app (single-file HTML, live on Netlify, NOT Git-linked, ~39 real trades) — source RECOVERED Chat 7, secrets-clean; (2) the CURRENT platform (the venture). DECISION: original = abandoned-by-choice PARTS DONOR, not revived; build plan unchanged. REUSABLE: the NinjaTrader CSV parser (parseCSV — proven, instrument-agnostic, de-dupes) = the upload engine's machine-zone import adapter, NT-first; + reference designs (tag taxonomy incl. behavioral negatives, screenshot model, notebook, an AI-Insights tab that already calls Claude). FILL-GROUPING DECISION: manual merge-by-click, NOT the 10s auto-window — "one trade" is TIME-defined for scalpers but INTENT-defined for level-to-level (half at TP1 + runner + add = legs minutes apart, one idea; only the trader knows intent). Mark's 10s insight (avg trade ~9s) kept as scalper R&D, not the product default. NOT reused: localStorage (→ Supabase). Student Zero's fork = what-NOT-to-do (too manual-input). PRINCIPLE: append-never-overwrite the trader's own journal/tags/trades (coach adds/suggests/grades, never silently edits — or trust dies).`

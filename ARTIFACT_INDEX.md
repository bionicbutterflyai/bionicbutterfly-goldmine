# ARTIFACT INDEX — the map (title | tags | one-liner)
*Add a line here whenever you create or change a durable artifact. This is how the farm stays retrievable.*

## knowledge/
- `tech_architecture_skeleton.md` | build, business-plan | PUBLIC | draft | First-cut system wiring in 4 layers (acquisition/platform/infra/external services). Matched diagram+Mermaid. DRAFT — fresh Claude refines; 6 open questions incl. Fork-2 funnel-memory pipeline.
- `brand_funnel_architecture.md` | marketing, business-plan, coaching | PUBLIC | captured | Hook-skin top / sober-spine in-product; the contrast IS the conversion. Foyer = the spine proving the hook didn't lie. Guardrails + A/B validation.
- `two_strategy_split.md` | coaching, build | PUBLIC | pending | Two strategies, one chart: 144 trend-continuation (+1-in-20 stand-down) and Red/Yellow NYO breakout. OPEN: 9:30-only vs all zone boxes.
- `master_journey_flow.md` | business-plan, build, coaching | PUBLIC | captured | THE COORDINATE SYSTEM — one-page master journey (hook→foyer→sort→nurture/sales→Lab→coaching→loop). Mermaid source paired with rendered diagram; carries the locks (no-name voice, Lab=bench, course dual-role, ICP=capable-not-noob) + 3 forks. Every future Claude orients here.
- `dpmo_gate_indicator.md` | coaching, build | The DPMO 3-green confluence gate (entry trigger): 20/50/7, logic-from-script / numbers-from-settings, cloud = pmo−signal, close>144 → pullback → 3 greens. The trigger the strat_zone_taxonomy is the context for.
- `coaching_cue_library_additions.md` | coaching, build, business-plan | CUE #1 amendment (green = DPMO bar-colour, not raw close) + CUE #2 (look-left pivot + patience credit). Companion to the (to-import) original cue library.
- `strat_zone_taxonomy.md` | coaching, build | The full STRAT: ~14–16 zones/levels (Red/Yellow/London/Pre-Market/IB/Weekly-IB, PD H/L & Close, Overnight, VWAPs, Quarterly 90-min line, 144, 20/50 cloud) + 5 display rules (fill-on-relevance & narration highlight-fade, tick-merge, label-only-discrete, persistent intake=playback layout, auto-resize-on-intake) + image-role guardrail (analyze Bookmap/GEX, never parse TV).
- `data_provenance_and_timestamp_pin.md` | build, support | NinjaTrader close-stamped & UTC; TV open-stamped & ET → TV = export −4h −1min. Pin every new broker export via one anchor candle; relabel, never shift candles. Broker-onboarding discipline.
- `voice_tts_decision.md` | build, business-plan | Free browser-native Web Speech API as default TTS (zero per-student cost); chunk text for ~200-char cutoff, recommend Chrome; onboundary→highlight-sync bonus; paid TTS optional premium later.
- `repo_as_memory_and_handoff.md` | build, business-plan | Public repo = Claude-fetchable memory (raw URL + code-exec; verified). Skinny handoff = minutes + URL, branched on capability. Standing rule: write back + keep Mark's offsite Vault current. Access truth = public-vs-private, not GitHub-vs-not.
- `coaching_cue_library.md` (+additions) | coaching, build | CUE #1 (DPMO green-confluence patience), CUE #2 (look-left pivot + patience credit). CUE #3 (Bookmap/GEX confluence) PENDING. — *import the original from Mark's Chat-3 zip.*
- `tagging_strategy.md` | build, support | The tag convention (coaching/marketing/build/business-plan/legal/support) + retrieval scope rules. — *import from Mark's Chat-3 zip.*

## charts/
- `trade_lesson_june4_dpmo_v6.html` | build | The pinned June-4 DPMO lesson chart (timestamp-correct, fill-only cloud).
- `trade_lesson_june4_kitchensink.html` | build | All strat levels on (the "how messy" test): gutter, tick-merge, label-only-discrete, hover highlight-fade. The case FOR fill-on-relevance.
- `lesson_viewport.html` | build | Merged intake+playback: persistent triptych (TV/Bookmap/GEX), real charts, morph-to-fullscreen on cue, auto-resize on upload.
- `trade_journal_upload_box.html` | build | 3-pane trade-chart uploader (drag/drop/paste/pick), auto-resize on intake, archive-to-trade stub.

## build/
- `calc_dpmo_v6.py` | build | DPMO 20/50/7 port + 144/EMA + the −1min close-stamp relabel.
- `build_v6.py` | build | Builder for the v6 lesson chart.
- `calc_levels.py` | build | Computes all strat levels (multi-day) + VWAP series + tick-merge.
- `build_ks.py` | build | Kitchen-sink chart builder (levels, gutter, hover, merge).
- `build_viewport.py` | build | Assembles the lesson viewport with embedded resized charts.

## data/
- `verified/MNQ_06-26_June_Last.txt` | build | Jun 1–4 2026 1-min MNQ, convention-confirmed (matches known-good June-4 sample). PASSED gate.
- `unverified/MNQ_06-26_April_to_June_5_noon_Last.txt` | build | Apr 1 + Apr 19–Jun 5 noon. Chronological OK, but **Apr 2–18 GAP** — needs gate review before promotion.

## marketing/ , voices/  — placeholders; drop Finn's InVideo.ai zip and TTS assets here.

## reference/  (lineage — superseded but kept)
- `CLAUDE4_KICKOFF_ORIGINAL_fat_handoff.md` — the original fat kickoff (the thing repo-as-memory replaces).
- `trade_lesson_june4_PRE-DPMO.html`, `trade_lesson_june4_dpmo_PRE-PIN.html` — earlier chart versions.
- `build_v4_ORIGINAL.py`, `calc_dpmo_ORIGINAL.py` — pre-pin builders/calc.
- `/samples` — real `SAMPLE_bookmap_MNQ.jpg`, `SAMPLE_gex_tanuki.png`, `SAMPLE_tradingview_MNQ.jpg` (the analyzable-surface samples per the image-role guardrail) + `SAMPLE_tv_timestamp_anchor.jpg`.
- `/session_screenshots` — render captures from Chat 4 (low value; kept for completeness).

## root
- `METADATA_SCHEMA.md` | build, support | built | the metadata standard (read with the law).
- `VAULT_PROTOCOL.md` | build, support | PUBLIC | captured | offsite discipline + canonical file list.
- `README.md` | the orientation (read first). `HANDOFF.md` | the skinny minutes. `MAINTENANCE_AND_BACKUP.md` | build | THE LAW — where the goldmine lives, what's in it, per-session upkeep + the dated-snapshot backup scheme + handoff close-out rules.

## charts/ (additions)
- `trade_lesson_june4_v7_cvd.html` | build | built | v6 + a third stacked CVD pane (Heikin-Ashi cumulative delta, LonesomeTheBlue port, 50 EMA blue-dashed; below=bearish). Brother's stacked layout, not shared dual-axis.

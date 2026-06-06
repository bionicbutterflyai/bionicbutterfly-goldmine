# CLAUDE4_KICKOFF.md — paste into the fresh chat, attach the 7 files + farm, then say GO

bionicbutterfly — Session Handoff (→ Claude-4)

Hi Claude. I'm Mark, founder of bionicbutterfly.ai — a Claude-powered trading-accountability
platform. You're continuing an established build. You have no memory of prior sessions; that's
expected. I'm the continuity — you reason over what I hand you, and you verify against the actual
files rather than trusting memory or assumption.

HOW WE WORK (the one behavior that makes this project work): Be the sober, honest "PHD — Professional
Honest Developer." Feasibility over hype, flag the too-good-to-be-true, never a cheerleader. LOOK,
DON'T ASSUME — actually open and read every file before acting, and tell me if something's missing or
doesn't reconcile. Never fake confidence at a knowledge gap — ASK; that's how my tacit strategy
transfers to you. Save important work to disk as files; the sandbox dies with the chat, so files + my
downloads are the only persistent memory. Credit is mine; you're the tool.

STOP — do not proceed until BOTH are true:
1. All 7 files below are attached/uploaded, AND
2. I have typed GO.
If any file is missing, tell me which and wait. Do not start work, build, or summarize beyond
confirming receipt, until I say GO.

THE 7 FILES YOU SHOULD HAVE:
1. trade_lesson_june4_dpmo.html — current DPMO-native coaching chart (the live work)
2. build_v4.py — the builder that generates that chart
3. calc_dpmo.py — the DPMO (20/50/7) port + EMA/144 calc on the bar data
4. GOLD_dpmo_gate_indicator.md — the verified 3-green gate gem (logic-of-record + settings-of-record)
5. GOLD_coaching_cue_library_additions.md — CUE #1 amendment + CUE #2
6. MNQ_06-26_060426_v2_Last.txt — source 1-min bar data (UTC; ET = export − 4h)
7. trade_lesson_june4.html — earlier non-DPMO lesson version (reference)

PLUS THE FARM (attach if not already): GOLD_master_plan_v1.md (direction — read for where this is
heading), GOLD_ARTIFACT_INDEX.md (the map), and the gold docs it points to.

WHERE WE ARE (current & proven — not aspirational):
- Stack: GitHub + Netlify + Supabase. The Supabase credit_ledger is LIVE (per-turn model/tokens/
  cost_usd + prompt caching; ~$0.005/turn text; credits debit). You CANNOT touch any live system from
  this chat — confirm state via my screenshots, never assume.
- The coaching engine grades a real trade against my framework, redraws the chart in my system
  (144 spine + my levels, none of the 7 commodity indicators), and is honest about its own limits
  (flags when entry wasn't a fresh 144 break and ASKS me to teach it).
- Last session built the DPMO-native lesson: my DPMO ported to JS (20/50/7), candles coloured by
  d = pmo − signal + 10-bar high-volume rule, 20/50 EMA price cloud, fill-only DPMO pane, time axis.
  Real June 4 MNQ trade: entry 10:58 @ ~30350, exit 30451 (GEX line), +101 pts / 10.1R max / $202;
  realistic capture ~40 pts on 5 micros ≈ $400 (illustrative). Provenance: real trade, coached live,
  manually keyed, AWAITING NinjaTrader fills export.

LOCKED — do not re-litigate (flag once, briefly, then defer unless I say "let's reconsider"):
coaching business; the master-plan strategy; brand = no "Oracle" character / no Morphosis / no
caterpillar-metamorphosis arc / no lip-sync avatar; the voice is the unnamed "voice from the data."

NUGGET DISCIPLINE (do this all session): When I reveal a durable insight — a strat rule, coaching
cue, brand/positioning call, business-model truth — STOP and flag it: "that sounds like a nugget —
capture it as a tagged GOLD doc?" Don't let insights evaporate in conversation. Tag per the
tagging-strategy doc. The cue ritual (you hit a gap → ask → I supply the rule → capture as tagged
cue) is the moat being built. Watch for it; I won't always remember to ask.

YOUR FIRST TASK (once I say GO): I have a NEW NinjaTrader 1-min export for a new test trade. Before
building anything:
1. Verify the new export's timezone/timestamp convention against my TradingView chart using ONE
   anchor candle (I'll give you a TV time + that bar's OHLC). Pin the clock first — a prior session
   got tangled on a time mismatch, so confirm the offset before trusting any timestamp.
2. Then rebuild the DPMO-native lesson on the new trade, carrying these QUEUED TWEAKS (fold into one
   build, no standalone recompiles): upper 20/50 EMA cloud → fill-only, no outlines (like the DPMO
   pane); and REMOVE the resolved "10:57 vs 10:58" reconcile note (entry 10:58 confirmed) — keep only
   the engine "no fresh 144 break" false-negative flag.
3. Also pending validation against my TV: dull-vs-vibrant bars match? vibrant-bear colour (I used
   fuchsia per the script — confirm or switch to red)? EMA cloud flips green at the right bar?

Read in, confirm all 7 files are present, and WAIT for my GO. Understanding first, action second.

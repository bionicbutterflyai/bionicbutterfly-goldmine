*TAGS: build, business-plan, coaching, marketing | AUDIENCE: founder + every future Claude (the daily-recap feature).*
*CREATED: 2026-06-07, Chat 6 | UPDATED: 2026-06-07, Chat 6 | STATUS: captured (feature greenlit; build = later)*
*SUPERSEDES: — | RELATED: master_strategy_vision.md (THE primer), tech_architecture_skeleton.md, strat_zone_taxonomy.md, coaching_philosophy.md, voice_tts_decision.md, data_provenance_and_timestamp_pin.md, master_journey_flow.md*

# GOLD — BIONIC BRIEFING (the daily morning recap)
*Mark's nugget, Chat 6. A branded pre-market briefing, 5 days/week, generated once and broadcast to all subs.*

## ONE-LINE
Every trading morning, Claude produces a short, watchable/listenable recap: walk the chart from the
**higher timeframes down to the lower** (year · quarter · month · week → 4h · 1h · 30m · 15m), surface
only what matters, layer in a **news + catalyst review**, and frame the day soberly. One render,
broadcast to everyone — not a per-student call.

## WHY IT'S STRONG (the business case)
- **Margin runs the right way.** Generated ONCE each morning and broadcast to every subscriber — cost
  is fixed regardless of headcount, so margin *improves* with scale. The opposite of the per-seat
  Claude-call cost risk that haunts the live coach.
- **Perfect fit for the locked pre-render premium voice** (voice_tts_decision.md): fixed authored
  content, rendered once → $0/student, premium voice. Total consistency with the TTS decision.
- **Retention + funnel, one artifact.** A daily 5×/week branded touchpoint is the Weight-Watchers
  daily-discipline loop (retention/habit). A teaser/free version on YouTube/email/X is sober,
  non-hype lead-gen that builds authority without guru cosplay (full version = subscriber perk).
- **Showcases the super-sauce.** The HTF→LTF walk is the cleanest stage for narration-synced
  highlight-and-fade: the level lights as Claude speaks it.

## FEASIBILITY (PHD verdict: GO)
- **Delayed data is a NON-ISSUE here.** A morning recap reviews the prior close + HTF structure; it is
  not a live in-session signal. The Massive **free tier** (5 calls/min, delayed) is sufficient to build
  and run the briefing. Pay for real-time only if/when an intraday feature needs it.
- Data source = **Massive.com** (ex-Polygon): OHLCV aggregates across every timeframe; real-time
  **Benzinga news API (v2)** for market-moving headlines; plus IPO calendar, treasury yields, inflation,
  analyst ratings, market status/holidays — all reachable via the official Massive MCP server.

## THE NON-NEGOTIABLE RULES (the PHD guardrails — these are what keep it honest)
1. **Catalyst dates are MACHINE-PULLED, never recited from a model's memory.** This is the
   data-provenance law (data_provenance_and_timestamp_pin.md) applied to the briefing. A model reciting
   earnings/NFP/OPEX/IPO dates from memory WILL drift. The catalyst section reads from real feeds
   (earnings + econ calendar + the OPEX schedule + Massive's IPO endpoint); Claude only *summarizes*.
   (Worked example of why: triple-witching/OPEX = the **third** Friday; NFP ≈ first Friday — dates a
   model often misremembers. Pull, don't recall.)
2. **VOLUME = total only; never claim buy/sell pressure off bar data.** Confirm a move with **total
   volume** ("this breakout came on expanding volume / this one's thin") — that's real. Do NOT present
   estimated delta/CVD as "buys vs sells"; real order-flow truth = Bookmap/tick data only. (See the
   VOLUME HONESTY rule in coaching_philosophy.md + the CVD caveat in strat_zone_taxonomy.md.)
3. **Inform, don't predict.** The briefing says *what's scheduled and what moved and where structure
   sits* — it does NOT forecast ("NQ will hit X"). Predicting is guru behavior; informing is coaching.
   Keep any "geopolitical position" sober and bounded — context, not hot takes.
4. **News is summarize-only** (copyright): headlines + Claude's own synthesis, never republished
   article text.
5. **Not painfully monotone.** Mention a timeframe only if it matters; skip the ones that don't.

## OPEN / CONFIRM-AT-BUILD
- Exact Massive free-tier delay (10 vs 15 min); whether NQ/MNQ is a direct Massive futures symbol or
  proxied off ES (ES/GC/CL confirmed GA; NQ not named in the futures-GA list).
- Whether real-time Benzinga news is gated to a paid plan (confirm before relying on it on free).
- SpaceX-IPO-type items are speculative until they appear in the IPO-calendar feed — treat as illustrative.

## INDEX LINE
`knowledge/bionic_briefing_spec.md | build, business-plan, coaching, marketing | PUBLIC | captured | BIONIC BRIEFING: a branded daily (5×/wk) pre-market recap — HTF→LTF chart walk (year→15m, mention only if it matters) + news/catalyst review, generated ONCE and broadcast to all subs (margin improves with scale; fits the pre-render premium voice). Feasible on Massive free tier (delayed data is fine for a morning recap). NON-NEGOTIABLE: catalyst dates machine-pulled not model-recalled; volume = total only (no buy/sell claims off bars — that's Bookmap/tick); inform-don't-predict; news summarize-only. Doubles as retention loop + non-hype top-of-funnel.`

*TAGS: coaching, build | AUDIENCE: founder + build/the Oracle's grader.*

# GOLD ARTIFACT — THE STRAT: ZONE & LEVEL TAXONOMY
*Captured June 4 2026, Chat 4 (Claude-4), from Mark's written spec. This is the core strategy IP —
the thing every prior handoff referenced but never carried. It MUST ride in every future handoff.*
*Companion to GOLD_dpmo_gate_indicator.md (the entry trigger) — this doc is the CONTEXT the gate fires inside.*

---

## ONE-LINE
The STRAT is ~14–16 session zones, VWAPs, and reference levels — most overlapping by design — that
together frame whether a setup is at real confluence or in a no-trade chop pocket. The DPMO 3-green
gate is the *trigger*; these zones are the *context* that says whether the trigger is worth taking.
The read is a bionic glance (Mark sees the confluence instantly); the build's job is to surface that
glance for a new eye.

## GOVERNING DISPLAY RULE — FILL ON RELEVANCE (Mark's call, June 4)
Every zone/level below lives in the **data layer at all times**, but the coaching chart stays **clean
by default**. A zone only **draws/fills in when the coach cites it** as confluence for that moment.
The new eye sees an uncluttered story; the full strat is underneath, surfacing only when it matters.
On-brand with the kickoff's "clean chart, none of the 7 commodity indicators." (Capture this rule
with the taxonomy — it's how the whole layer renders.)

### Extension 1 — NARRATION-SYNCED HIGHLIGHT-AND-FADE (the "super-sauce", June 4)
The *temporal* form of fill-on-relevance. During Claude's video/voice presentation to the student,
**as the coach speaks a level or zone, that level highlights, then fades back** once he moves on.
Same visual as fill-on-relevance, but hooked to the **narration timeline** instead of a static
"is it relevant" flag — the level appears exactly when it's spoken and recedes after.
- **Proof-of-concept built (June 4):** in `trade_lesson_june4_kitchensink.html`, hovering any level
  lights it and fades all others to ~12% (the highlight-and-fade mechanic, hover-driven). The
  production step is to drive the same highlight off the narration cue points instead of the mouse.

### Extension 2 — TICK-MERGE FOR CLUTTER (Mark's TV does this; June 4)
When two or more levels fall **within ~2–4 ticks** of each other, **merge them into one prominent
line** with a **combined label** (e.g. "Yellow H / PreMkt H 30331", or "Yellow L / Red H 30265–30270").
The label gets longer but the chart gets cleaner — a cluster of near-identical hairlines becomes one
honest zone-of-interest. Pair with the right-side **label gutter** (black free space between the last
bar and the price column) so merged labels have room. (June 4 example: Yellow H = PreMkt H = 30331
exactly; Yellow L 30265 / Red H 30270 are 5 ticks apart — prime merge candidates.)

### Extension 3 — LABEL ONLY DISCRETE LEVELS, NOT CONTINUOUS LINES (Mark's TV; June 4)
**EMAs and VWAPs get NO price label** — TV doesn't label them and the eye reads them by **colour**
(blue 144, magenta AVWAP, white Session VWAP, the 20/50 cloud). Only the discrete **H/L levels**
(zone highs/lows, PD, IB, quarterly, etc.) earn a label, because those are the numbers that act as
targets / lines-in-the-sand. Labels on continuous lines are noise. (Applied in the kitchen-sink: 144,
AVWAP, Session VWAP labels removed; level labels kept in the gutter.)

### Extension 4 — ONE PERSISTENT LAYOUT: INTAKE = PLAYBACK (June 5)
Intake (uploading charts) and playback (the lesson) **share one persistent triptych** — TV large
top-right, Bookmap upper-left, GEX lower-left — and **the panes never move**. Where Suzy uploads a
chart is where it later expands. During the lesson the discussed chart **takes over full-screen and
the other two disappear** (not dim — gone — for maximum sharpness; the kitchen-sink is already busy
enough), then settles back to the triptych. The student never re-orients: same room, same furniture;
the coach just picks one up to show her. Built: `lesson_viewport.html` (real June 4 charts, click /
cue-button to morph). The morph is the *between-charts* half of the super-sauce; highlight-and-fade is
the *within-chart* half — same narration cue points drive both.

### Extension 5 — AUTO-RESIZE ON INTAKE (June 5)
Every uploaded image is **downscaled client-side the moment it lands** (drop / paste / pick): cap
width ~1400px, re-encode JPEG ~0.82, before it's stored or shown. The oversized original never
travels (keeps the Supabase archive lean; panes stay sharp). Why it matters: Mark runs his 4K at 100%
(not the recommended 150%) to fit more Bookmap bubbles, so his screen-caps are huge. Tunable: 1600px /
0.88 if a heatmap looks soft full-screen. Trade-off: JPEG re-encode softens a PNG slightly — fine for
screenshots; branch on file type only if pixel-exact PNGs are ever needed. Built into both
`trade_journal_upload_box.html` and `lesson_viewport.html` (one pipeline).

### Extension 6 — CVD INDICATOR (Heikin-Ashi cumulative volume delta) (June 5)
Second confirmation indicator beside the DPMO. Port of LonesomeTheBlue's CDV: per-bar delta is
**estimated from candle geometry** (`_rate()` splits each bar's volume by where the close sits in its
range — NOT true tick bid/ask), `cumdelta` summed, rendered as **Heikin-Ashi candles** (green up / red
down). A **50 EMA on the HA close**, styled like the 144 (**blue dashed, medium 2.4**); **price/CVD
above 50 EMA = bullish, below = bearish.** Render in its **own stacked pane** below the DPMO (Mark's
brother's call — separate panes over shared dual-axis; loses height but reads clean for the new eye).
CAVEAT: shape-estimated delta matches Mark's TV exactly (same estimate) but is NOT order-flow truth —
a real tick-delta feed could differ. Built: `trade_lesson_june4_v7_cvd.html`.

### Extension 7 — APP-SHELL LAYOUT: reclaim vertical for stacked panes (June 5)
Stacked indicator panes get tall. Fix is the GUI shell, not fewer panes: **nothing above the chart.**
Four columns full-height — thin left icon rail · persistent left **nav/TOC column** · **chart + all
panes center** (the REAL lesson chart — v7 price+DPMO+CVD — not placeholder geometry) · **chat dock
right.** Moving content off the top reclaims the vertical the stacked panes need; side-column width is
the adjustable knob. STATUS: concept captured; real chart-in-shell to be built next session (no mock
artifact referenced — the throwaway skeleton is intentionally not kept).




## TIME-CONVENTION REMINDER
All windows below are **NY ET**, and per GOLD_data_provenance_and_timestamp_pin.md the NinjaTrader
export is close-stamped (TV = export − 1 min). Session-bounded zones MUST be cut on TV/open-time, or
every box edge lands a minute wrong. ETH session = 6:00pm → 5:00pm next day; RTH open = 9:30am.

---

## A) SESSION-RANGE BOXES (all in the one "Session Range Zones Indicator")
Each box: high/low taken during its window, then extended right (right edge tracks the current bar)
until 17:00. Price *inside* a box = ranging / no-trade; the signal is breakout → retest → hold &
continue, **or** breakout → reverse back inside = **head fake**. Boxes are meant to be read in
confluence with each other.

1. **RED ZONE** — red solid border, medium-thick, light shade.
   - Window: **9:30:00 – 9:30:59 (the 9:30 1-min RTH opening bar)**. H/L = that bar's H/L.
   - ⚠ **DATA-RESOLUTION NUGGET:** the *original* zone was the floor 30-second range (9:30:00–9:30:29).
     That is **not representable in 1-min bar data**, so it was reprogrammed to the **9:30 1-min open
     bar**. Rule: zone windows can't be finer than the bar resolution — sub-minute zones collapse to
     the opening 1-min bar. (Mark: "all these were programmed already" — they exist in TV, just never
     traveled into a working chat.)
   - **No box — H/L lines only** for the read; price inside the open-bar range = **no trade**.
   - The 30s range was the old CME-floor test: can price auction enough momentum either way to break
     out with follow-through? Watch whether Asia/London set NYS to continue (break/retest/continue)
     or to head-fake-and-reverse with volume (squeeze that traps and pushes further).
   - **Yellow Zone + Red Zone together = Mark's key zones — they always overlap.**
   - Ask: will NYS open range for minutes in the indecisive no-trade pocket, or break/fake out? Are
     the nearby liquidity levels above or below?

2. **YELLOW ZONE** *(was "Yellow Box")* — yellow solid line, medium.
   - Window: **9:00:00 – 9:29:59 (30 min)** — confirmed; draws from 9:00 (the earlier "6:30 start"
     was a carry-over from the Pre-Market box and is dropped). Price inside = ranging / chop.
   - Read: breakout → retest → hold & continue, or breakout → reverse (head fake).

3. **LONDON 30m OR** — green box, solid, medium.
   - Window: **3:00:00 – 3:29:59 (first 30 min of London)**. Box 3:00 → 17:00.
   - Price inside = ranging / chop. Watch whether **London 3am–5am** broke above/below.

4. **PRE-MARKET OR BOX (3 hrs)** — blue box, solid, medium.
   - Window: **6:30:00 – 9:29:59**. Box 6:30 → 17:00. Price inside = ranging.
   - Watch whether the London/Pre-Market range broke above/below.

## B) VWAPs & THE QUARTERLY LINE
5. **SESSION VWAP** — white medium dashed. Anchor: ETH 6pm → 5pm next day. Above = bull / below = bear.
6. **ANCHORED VWAP** — magenta medium dashed. **Anchored to 9:30 (RTH open).** Above = bull / below = bear.
7. **QUARTERLY THEORY LINE** — lime-green thin dashed. **3rd-party code** (not ours).
   - Plot the **price at each of these ET stamps** and draw a horizontal level rightward until the
     next stamp 90 min later (90-min cadence, ETH session, stop at 17:00):
     **18:23, 19:53, 21:23, 22:53, 00:23, 01:53, 03:23, 04:53, 06:23, 07:53, 09:23, 10:53, 12:23,
     13:53, 15:23, 16:53.** Above = bull / below = bear.
   - **Mark's edge / favourite:** the **9:23** quarterly level + the Yellow/Red box NYS-open play.
     Price often sets up overnight and through pre-market, runs *through* 9:23 and reverses, then
     retests-holds 9:23 and continues the opposite way. High hit-rate per Mark.
   - *(This is the "Quarterly line math" referenced — and never captured — in prior chats.)*

## C) REFERENCE LEVELS
8. **INITIAL BALANCE (IB)** — purple, solid, medium. **No box — H/L lines only.**
   - Window: **9:30–10:30 (RTH first hour)** — confirmed.
9. **OVERNIGHT H/L** — **white lines** (H/L only). Window: ETH overnight into the 9:30 open.
   - NYS open usually carries an imbalance; Market Makers seek to rebalance by running price the
     *opposite* way toward the Overnight H/L. Past ~6 months: they often **front-run** the level and
     reverse with volume — trapping traders who assumed price was running for the target/liquidity.
10. **PREVIOUS DAY H/L** — white medium. Track **both**: RTH (dashed) and ETH (solid).
11. **PREVIOUS DAY CLOSE** — green medium. Track **both**: RTH (dashed) and ETH (solid).
12. **ALL-TIME HIGH (ATH)** — yellow dashed line from the highest candle to the current bar.
13. **WEEKLY IB** — purple dashed, medium. Range = **Mon+Tue H/L**, drawn through Friday close.
    Rule of thumb: one side usually holds → reverts to mean or runs to the other extreme; can range,
    head-fake-and-reverse, or break-retest-continue.

## D) TREND BACKBONE (already built into the chart)
14. **1-min 144 SMA** — blue medium dashed. Above = bullish / below = bearish. *(live in the build.)*
15. **20 & 50 EMA CLOUD** — 20-line red, 50-line green; above cloud = bull / below = bear.
    - NOTE: the coaching chart renders this **fill-only (no outlines)** per the June 4 tweak, so the
      red/green *line* colors are currently moot; the bull/bear read is by price-vs-cloud. If outlines
      ever return, use 20 = red, 50 = green.

---

## RESOLVED (June 4, all six confirmed by Mark)
1. **Yellow Zone** — window 9:00–9:29:59 (renamed from Yellow Box; 6:30 start dropped). ✓
2. **Red Zone** — 9:30 1-min open bar (9:30:00–9:30:59); sub-minute 30s range impossible at 1-min data. ✓
3. **IB** — 9:30–10:30 RTH first hour; H/L lines only, no box. ✓
4. **Overnight H/L** — white lines. ✓ *(exact overnight bounds: ETH into 9:30 — fine-tune later if needed.)*
5. **Anchored VWAP** — anchored to 9:30 RTH open. ✓
6. **GEX** — **separate layer, not a TV indicator line.** 3rd-party; appears on TV, but Mark's
   preferred ingestion is to **paste the GEX web-app image** (e.g. the gamma/Net-GEX tool) for the
   coach to **read visually** — same as the trade-journal upload box (see below). GEX is image-input,
   not a computed level in this taxonomy.

## GUARDRAIL — UPLOADED-IMAGE ROLES (don't ask Claude to parse TradingView) (June 5)
The three uploaded images do NOT carry equal trust, because the *surfaces* differ:
- **Bookmap** and **TanukiTrades GEX** are **consistent surfaces** — every student's looks the same.
  Claude can be trained to read them reliably → **analyzable** (liquidity walls; gamma levels/HVL).
- **TradingView is NOT consistent** — every student's TV is a different set of indicators, colours,
  and completeness. Asking Claude to extract levels / read indicators off the uploaded TV is a
  **landmine**: works for some students, silently fails for others.
- **The trap is a none-issue by design** — for the strat read we **never analyze their TV**. We take
  the **raw trade data** and **redraw everything in our own system** (144, zones, DPMO). Their TV
  image is a **display reference only**; Claude never parses it.

| Image | Role | Claude's job |
|---|---|---|
| Bookmap | analyze | read liquidity / walls (consistent → reliable) |
| GEX (Tanuki) | analyze | read gamma levels / HVL (consistent → reliable) |
| TradingView | display reference only | show it; NEVER parse it — strat comes from raw data, redrawn |

RULE: the moment a feature asks Claude to *analyze* the uploaded TV chart, stop — that's the trap.
Analyze Bookmap/GEX; treat TV as a reference image. (Captured as a guardrail against a future design
mistake that would fail invisibly on a subset of students.)

## RELATED FEATURE — TRADE-JOURNAL IMAGE BOX (today's original goal; sample for GEX/Bookmap ingestion)
Student selects a trade in the journal → a large 3-pane upload modal opens: **right (large) =
TradingView**, **upper-left (small) = Bookmap**, **lower-left (small) = GEX**. Each pane has a faded
placeholder of that chart type plus drag-drop / paste / file-picker. Student (Suzy) uploads 1, 2, or
all 3; images archive to the chosen trade; the coach then reviews the uploaded images for the lesson.
This is how GEX (and Bookmap) enter the coaching context — as archived images, not computed lines.

## STATUS
- **Live in Mark's TradingView indicators today** (the chart is drawing all of these).
- **NOT yet in the coaching engine / trade tests** — back-burnered while the DPMO gate + chart
  fundamentals were proven. Not lost; just never carried into a working chat until now.
- Build approach when greenlit: data-layer always-on + **fill-on-relevance** rendering (see governing
  rule). Likely sequence — reference levels (cheap, deterministic) first, session boxes next, VWAPs +
  Quarterly last (Quarterly is 3rd-party code → provenance/IP check, like the DPMO).

## INDEX ENTRY (paste into GOLD_ARTIFACT_INDEX.md)
`GOLD_strat_zone_taxonomy.md | coaching, build | The full STRAT: ~14–16 session boxes (Red/Yellow/London/Pre-Market), VWAPs, Quarterly 90-min line, IB, Overnight & PD H/L, ATH, Weekly IB, 144 + 20/50 cloud. Render fill-on-relevance. Live in TV, not yet in engine. Open confirms listed.`

# GOLD ARTIFACT — THE DPMO 3-GREEN GATE (the patience engine)
*TAGS: coaching, build | AUDIENCE: founder + build/the grader.*
*Captured June 4 2026, Chat 3. Verified against the Pinescript + Mark's live TradingView settings.*
*This amends/supersedes the candle-color mechanism implied in CUE #1 (coaching_cue_library).*

---

## ONE-LINE
Mark's entry rule is a **3-green confluence gate** built on a stripped-down **Decision Point Price
Momentum Oscillator (DPMO)**. No long unless **all three** read bullish (same colour). The edge is
**not** the oscillator math — it is the **patience the gate enforces** (it blocks early entries).
Behavioural edge, not mathematical. This is squarely the accountability thesis: adherence, not knowledge.

## SOURCE OF TRUTH — READ THIS FIRST (it bit two prior Claudes)
- **The Pinescript is the LOGIC of record. The screenshots are the SETTINGS of record.** They differ.
- The pasted script carries neutral template defaults (**12 / 26 / 9**). Mark's **live settings**,
  per the Inputs screenshot, are **First Smoothing 20, Second Smoothing 50, Signal Smoothing 7**,
  Source = Close. **Use 20 / 50 / 7. Do NOT hard-code the script's 12/26/9.**
- Why this matters: a Claude that hard-codes from the script faithfully reproduces the WRONG
  oscillator. Mark sets values locally because hard-coded attempts "always came back wrong." Rule:
  logic from script, numbers from Mark's settings screenshot.

## THE 3 CONFIRMATIONS (all must be the same colour, or no trade)
1. **Candle** — the bar coloured bullish by the DPMO bar-colour logic (NOT raw close direction).
   *Dull green* = cloud-direction bullish. *Vibrant/bright green* = **high-volume bar**: this bar's
   volume ≥ the highest of the prior 10 bars (`volLookback = 10`). Vibrant = the strongest tell.
   (Bear side: dull red / vibrant red-fuchsia.)
2. **The 20/50 EMA price cloud** (the ribbon on price) — bullish / price riding above it.
3. **The DPMO cloud** (lower pane) — green, i.e. `pmo > signal` (the script's `d = pmo - pmols > 0`).

**Precondition before the gate even arms:** price **close > 144 SMA (1-min)**. Then **ALERT** →
**wait for the pullback** → **3-green gate** = entry. "JUST WAIT" — the secret sauce is the waiting.

## PRECISION NOTES (where Mark's words and the code diverge — verified)
- **Cloud colour is PMO-vs-SIGNAL, not PMO-vs-ZERO.** The lower-pane cloud fills on
  `d = pmo - pmols`. The white 50%-opacity **zero line** is only a reference. PMO can be *below zero*
  while still crossing *above its signal* (an early bullish turn), so the gate's "DPMO green" can
  fire slightly before price reclaims the zero line. Often they agree; not always.
- **Style-tab "Bar Color" Color 0–3 = the same four bar colours from a different tab**, not eight:
  Color 0/1 = dull bull/bear, Color 2/3 = vibrant high-vol (lime / fuchsia). Inputs tab and Style
  tab expose the same palette.
- **Toggle gotchas (why prior Claudes "left too much code in"):** three overlapping bar-colour modes
  exist — `Color Bars (High Volume)`, `Color Bars (Dynamic)`, `Color Bars (Above/Below Zero)` — with
  a priority cascade (High-Vol > Dynamic > Zero). Mark runs specific ones and zeroes the rest
  (toggle off / 0% opacity). In TV all that's visible of the DPMO is **the cloud + the zero line**.
- **In TradingView the DPMO renders only as the cloud + zero line** (lines/signal hidden). The bar
  colouring it drives appears up on the price candles.

## WHY THE ENGINE UNDER-GRADES IT (the false negative — ties to CUE #1)
The deterministic engine looks for a **fresh 144 break right before entry**. The gate routinely
fires when price is already well **above** the 144 (e.g. the June 4 dev trade: entry ~58 pts above
the spine). The engine flags "behaviour leg missing" — a **false negative**. The correct grade
credits the 3-green discipline. **BUILD IMPLICATION:** model the gate (close>144 → pullback →
candle+price-cloud+DPMO-cloud all green) as the behaviour leg, and/or consume DPMO bar-colour state
as a confirmation input. Until then the grader must ASK, then this cue teaches it.

## STATUS
- **NOT being built into the grader yet.** Mark's call (June 4): June 4 was "loose coaching" — the
  gate is captured as a cue, not yet coded. Add when ready (Mark: "we're good" on holding for now).
- The indicator is a config of a public DPMO (no proprietary IP); the edge is the gate discipline.
- Heiken-Ashi colouring variant = trivial to add later (not built).

## VERIFICATION ARTIFACT — the Pinescript (logic of record; settings come from Mark, see above)
```
//@version=6
indicator("Decision Point PMO", shorttitle="DPMO", overlay=false)
// Inputs: Source=Close; First/Second/Signal smoothing (TEMPLATE defaults 12/26/9 — LIVE = 20/50/7)
// Cloud fills on d = pmo - pmols (PMO vs Signal). Zero line is reference only.
// Bar colour priority: High-Volume(>=highest vol of last 10) > Dynamic(d>0) > Above/Below Zero.
// Vibrant bull = lime (high vol + d>0); vibrant bear = fuchsia (high vol + d<0).
// PMO calc: i = close/close[1]*100; csf-smooth(i-100, len1); csf-smooth(*10, len2); signal = ema(pmo, siglen).
// (Full script retained verbatim in the chat record that produced this doc.)
```
*Full verbatim script is in the Chat-3 transcript that generated this gem; reattach to that chat's
zip. The summary above is what the grader needs; the verbatim is for exact re-implementation.*

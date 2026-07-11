# GOLD — COACHING CUE LIBRARY · ADDITIONS (Chat 3, June 4 2026)
*TAGS: coaching, build, business-plan | AUDIENCE: founder + the grader.*
*Companion to coaching_cue_library.md (the original is read-only; these are appended here).*
*Two items: (A) an AMENDMENT to CUE #1's mechanism; (B) a NEW cue, CUE #2.*

---

## (A) AMENDMENT TO CUE #1 — candle-colour mechanism corrected
CUE #1 ("green-candle confirmation") had the right instinct but the wrong mechanism. As verified
against Mark's DPMO Pinescript + live settings (see dpmo_gate_indicator.md), the correction is:

- **"Green candle" = the DPMO bar-colour state, NOT raw close direction.** A bar's colour is driven
  by `d = pmo − signal` (the DPMO momentum spread), with a high-volume brighten layered on top.
  Bullish-looking bars can print red and bearish-looking bars green — that decoupling is the point.
- So CUE #1's "the candle turned green = his confirmation" should read: *the DPMO confluence flipped
  the bar bullish* — one of three confirmations in the gate, not a close-direction signal.
- The full entry rule is the **3-green gate** (close > 144 SMA → wait pullback → candle + 20/50 EMA
  price cloud + DPMO cloud ALL green). CUE #1's "double patience" framing still holds; the mechanism
  is now precise. The engine's "behaviour leg missing / no fresh 144 break" remains a FALSE NEGATIVE
  against this gate.
- ACTION when the original cue library is next editable: fold this correction into CUE #1 directly.

---

## (B) CUE #2 — THE PATIENCE-CONFIRMED BREAKOUT (look-left pivot + colours aligned)
*Captured June 4 2026 from Mark, on the June 4 dev trade. The second brick in the moat.*

**THE INSIGHT (two layers fused):**
1. *Generic, look-left layer* — every trader "knows" to look left: the entry zone (~30350 on June 4)
   was a prior-high pivot / the "real breakout" level. Commodity structure reading. But traders
   FORGET it in the moment, under FOMO.
2. *System-helped layer (Mark's edge)* — the 3-green gate's enforced patience is what kept him OUT
   until the breakout was real. Waiting for the colours to align = not chasing. The discipline is
   what placed the entry right at the pivot, not early.

**WHEN (trigger condition):**
Entry occurs at/just above a prior-high pivot (a look-left swing-high level) AND the 3-green gate
aligned before entry (candle + 20/50 EMA cloud + DPMO cloud all green).

**ENGINE HOOK (build):**
Detect entry within N ticks of a look-left swing-high level → render a **dynamic level line** at that
pivot on the coaching chart. (Swing-high detection is deterministic/cheap; the line is the visual.)

**ORACLE DELIVERY (affirming, not only Socratic — credit the behaviour):**
> "Well done resisting the FOMO this time — you waited for the colours to align instead of chasing.
> And notice: that entry sat right at the pivot off the previous high (look left). The patience your
> gate enforced is what put you at the real breakout, not early."

**WHY IT'S MOAT:**
Pairs commodity 'look-left' structure (anyone can say it) with the system's *patience credit* (Mark's
tacit edge). Reinforces **adherence over prediction** — it praises the behaviour and names the level
in the same breath. This is "she predicts you, not the market" in one coaching line.

**NOTE — the witness that remembers:**
The grader should still surface the standard look-left cues a trader "knows but forgets." CUE #2's job
is to be the witness that remembers them in the moment AND ties them to the patience that earned the
entry. Generic knowledge + behavioural credit = the fused cue no commodity tool delivers.

**STATUS:** captured as a cue (text). The dynamic look-left pivot line is a BUILD item, not yet built
(consistent with the gate itself being captured-not-built per Mark's June 4 call).

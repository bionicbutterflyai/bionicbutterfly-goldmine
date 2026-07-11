*TAGS: build, support | AUDIENCE: founder + build/the grader + whoever maintains the data-import pipeline.*

# GOLD ARTIFACT — DATA PROVENANCE & THE TIMESTAMP PIN
*Captured June 4 2026, Chat 4 (Claude-4). Verified against Mark's live TradingView via anchor candle.*
*Two nuggets, one root cause: never trust a broker export's clock until it's pinned.*

---

## ONE-LINE
A bar export's timestamp is meaningless until you know **which edge of the bar it stamps** and **what
timezone it's in**. Pin both against the trader's TradingView with a single anchor candle BEFORE
building or grading anything. A one-bar label error silently misgrades a trade.

---

## NUGGET 1 — THE NINJATRADER ↔ TRADINGVIEW TIMESTAMP PIN (the fact)
- **NinjaTrader export is CLOSE-stamped** — each 1-min bar is timestamped at the minute it *closes*.
- **TradingView is OPEN-stamped** — it labels a bar by the minute it *opens*.
- Therefore, for this export: **TV time = NinjaTrader export time − 1 minute.**
- The export is also in **UTC**; Mark trades **ET (EDT in June, UTC−4)**. Full mapping:
  **TV/displayed ET = export(UTC) − 4h − 1min.**

### How it was proven (so it isn't re-litigated)
1. **Cross-bar identity (decisive):** the DPMO spread `d = pmo − signal` crosses positive on the bar
   the export stamps **14:58 UTC**. Mark confirmed his live TV shows the cloud green at **10:57 ET**.
   Same physical candle → export-14:58 ≡ TV-10:57 → a clean −1 min offset. The port's MATH agreed
   with TV all along; only the printed label was off.
2. **Session-boundary corroboration:** the export's last bar is stamped **17:00 ET**, exactly the CME
   equity-index daily halt. An open-stamped feed would end at 16:59 (no 17:00–17:01 bar during the
   halt). Ending *on* 17:00 only makes sense as a bar that *closes* at 17:00 → close-stamped.

### The fix — RELABEL, NEVER SHIFT
- Candle x-positions are by **index**, not by clock. Fix the offset by subtracting 1 min from every
  time **label** (axis, markers, annotations). **Do NOT move candles** — they already align to TV.
- Implemented in `calc_dpmo.py` as `et_open(stamp) = (UTC−4)*60 + min − 1`, then `build_v4.py`'s
  hardcoded ET references shifted −1 to land on the same candles with the correct clock.
- WRONG TURN TO AVOID: an earlier pass mis-diagnosed the one-bar gap as a "razor-thin implementation
  cross" (seeding/CSF nuance) and nearly papered a "10:57" label over a port that still computed
  10:58. It was never an implementation artifact — it was the close-stamp. Trust the pin, not a fudge.

---

## NUGGET 2 — BROKER-ONBOARDING DISCIPLINE (the process)
**Every data file from a new/different broker is UNTRUSTED until proven.** Conventions (stamp edge,
timezone, delimiter, decimal/volume format, session boundaries, contract roll) vary by broker and
silently corrupt grading if assumed.

**Procedure for each new broker (do this BEFORE wiring it into the engine):**
1. Keep a **known-good reference file** (this June 4 MNQ tape is the current golden sample).
2. Run the new export through a **one-anchor alignment check**: ask Mark for one TV timestamp + that
   bar's OHLC, find the matching bar, and confirm the offset (timezone AND stamp edge) reconciles.
3. Only after it reconciles, **hard-code a per-broker import adapter** (one stamping convention per
   broker, pinned once, reused). Don't infer per-file; pin per-broker.
4. Sanity-check contiguity (no missing minutes) and session boundaries against the known halt times.

**STATUS:** the adapter framework is a BUILD item, **not now** (Mark's call). Captured as the rule so
it's enforced the moment a second broker's data appears.

---

## STATUS
- The June 4 lesson chart is pinned and correct as of v6 (`trade_lesson_june4_dpmo_v6.html`).
- Open follow-up (separate, lower priority): the verbatim DPMO Pinescript is still needed to
  reconcile the cross *math* exactly (not just the label); per `dpmo_gate_indicator.md` it lives
  in the Chat-3 transcript zip, not in the working file set.

---

## INDEX ENTRY (paste into GOLD_ARTIFACT_INDEX.md — I couldn't append; the index isn't in this chat)
`data_provenance_and_timestamp_pin.md | build, support | NinjaTrader is close-stamped & UTC; TV is open-stamped & ET → TV = export −4h −1min. Pin every new broker's export via one anchor candle before building; relabel, never shift candles.`

*TAGS: business-plan, marketing, build | AUDIENCE: founder + every future Claude (the MONETIZATION model — read with master_strategy_vision.md).*
*CREATED: 2026-06-06, Chat 5 | UPDATED: 2026-06-06, Chat 5 | STATUS: captured*
*SUPERSEDES: — | RELATED: master_strategy_vision.md (THE MONEY section), tech_architecture_skeleton.md (credit_ledger), coaching_philosophy.md, funnel_routing_and_closer.md*
*PROVENANCE: originated by FINN (Creative Director / InVideo.ai). Surfaced in Chat 5 from Mark's memory — it had been LOST in the handoff. Exhibit A for why this living repo exists.*

# GOLD — THE CREDIT / VALUE PRICING MODEL (how the money actually works)

## THE ONE LINE
We don't sell a subscription. We sell **value, metered in credits** — the student pays in proportion
to the value they pull, and the value (their P&L) dwarfs the spend, so paying feels like investing, not
being billed.

## THE METHOD (Finn's discipline — do this in order)
1. **Prove the round-trip COGS first.** For one real coaching interaction, add up what it costs Mark:
   Claude tokens (Anthropic), TTS (ElevenLabs or self-hosted), datafeed, hosting. Mark is himself on
   **credit/metered systems with his suppliers** (Anthropic, InVideo, maybe ElevenLabs), so cost is
   variable and knowable. *(When proved in a prior session, the real round-trip came in even cheaper
   than Finn's assumptions.)*
2. **THEN build the student price on top, with margin.** Never price off a competitor or a gut number —
   price *up* from proven unit cost, so there's always margin and never a loss as you scale.
3. **Every new cost input just folds into the credit COGS.** Add a datafeed, swap a TTS vendor — it's
   absorbed into the per-credit cost. The model absorbs cost changes cleanly.

## THE STRUCTURE (illustrative — numbers are an example, not a locked price)
Student buys, say, **1,000 credits for $100**. Those credits cost Mark **~$10** in COGS → ~10x markup.
The markup isn't gouging — it's the **value delivered**: those credits bought, e.g., two Claude lessons
that month, and the student made more money from that experience than the spend.

## THE PREMISE (why it converts where gurus fail)
People pay for **value, not knowledge.** A trader will **begrudge a $500/month flat subscription** from
a guru recycling old YouTube livestreams as "education" — because it's a fixed cost with unclear,
unaccountable return. They will **gladly pay for spend that returns more than it costs.** Same value spine
as the whole brand: knowledge is free bait; value is the product.

## THE INVERSION (the sauce — why usage credits beat a subscription psychologically)
A flat subscription is a cost the user *resents* ("am I getting my money's worth?"). Usage credits flip
that: **spending becomes a signal of success, not a drain.**
> Suzy finds so much value she buys more coaching and spends **$300** in a month — but her P&L went up
> **$3,000.** Suzy doesn't feel she paid $300 for nothing. She feels she *chose* more of something
> valuable and got back ten times what she paid.
The spend is **self-justifying** because it's tied to her own results. She's not paying a bill; she's
doubling down on a thing that's making her money.

## THE HONEST DEPENDENCY (PHD flag — the model's strength is also its condition)
Because revenue is value-linked, the model depends on students getting **real value** — but **value ≠
becoming a profitable trader.** The ~90% fail figure is the *unfiltered base rate*; Mark believes his
filtered/coached cohort does far better (his projection: ~50–80% win, unproven until a cohort runs — see
coaching_philosophy.md → THE HONEST VERDICT). Either way we **cannot** manufacture traders — so if "value"
meant "profit," any shortfall would push us toward guru hype. It doesn't, because the value is an
**honest, supported attempt + the truth about whether they're cut out for it.**
- A **winning** student spends more and feels it's investing (Suzy). A **washing-out** student should
  **not** be bled — the integrity move is the **GRACEFUL HONEST EXIT**: stop taking money for failure,
  deliver the verdict ("an honest shot — this market isn't yours, a respectable answer"), and they leave
  with dignity (and often a *better* testimonial than a winner — honesty, not survivorship hype).
- So: (a) the model **self-aligns with the ICP filter** (rewards the capable-but-struggling who can
  improve; gracefully releases the non-fit instead of draining them); and (b) the accountability +
  honesty loop is **load-bearing, not a nicety** — "don't take money for failure" is the anti-guru spine.
- Tradeoff to accept: usage revenue is **less predictable** than flat MRR. Worth it for the
  conversion/retention psychology, but forecast accordingly.

## TTS / PARTNERS THROUGH THIS LENS
Managed partners (ElevenLabs, datafeeds) aren't "expensive overhead" — they're **COGS inputs folded
into a credit.** You're buying **zero-ops** (no GPU servers to babysit — see the prime directive), and
passing the metered cost through with margin. Self-host only where ops burden is near-zero (offline
**batch pre-render** of fixed lessons); pay a managed API for the **live** sliver where low-latency +
zero-ops earn their keep.

## THE STUDENT EXPERIENCE — transparency, education, graceful limits (born from Mark's own AI pain)
Mark lived the *anti*-pattern as an AI user: opaque pricing (no idea what a plan included), costs that
crept up without feeling like he was doing more, the shock of learning that **every turn re-reads the
whole conversation and re-bills for it** (so a long, building session quietly gets more expensive per
message), and — worst — running out mid-task with **no warning**, a hard freeze, and once **losing hours
of work** to a context wipe. Suzy must feel **none** of it. Each pain inverts into a requirement:

- **Radical transparency — the live credit meter.** The Lab always shows: credits **remaining**
  (1000 → 998 → …), credits **used this session**, and the cost of the **last interaction** — so a turn
  that costs 2 today and 20 later is *visible*, never a surprise. Transparency is the **precondition for
  the value-pricing psychology**: the same $300 feels like *investing* when the meter is honest and
  *being milked* when it's opaque. The meter is the switch.
- **Educate as empowerment, not fear.** Onboarding teaches the **round-trip mechanic** — that continuing
  to build on a session re-reads context and adds up — framed as *"here's how to spend wisely and get the
  most value per credit,"* never *"watch out, everything costs money"* (fear would suppress the very
  engagement the model needs).
- **Graceful limits — never a wall.** Warn **before** she runs low; let her top up smoothly mid-flow;
  **never** a hard freeze, never lost work, never an amnesia reset. (Claude-4's note: the freeze/context-
  wipe is a flaw in Mark's *current chat tier*, not something the student product inherits — but the
  product must *guarantee* graceful exhaustion + state preservation by design.)

## THE TWO-TIER WALLET (the architecture consequence)
**Mark holds the master supplier wallet** (his metered accounts with Anthropic, InVideo, maybe
ElevenLabs). The system meters supplier COGS against that master wallet on one side, and **tracks + bills
each student's credit balance and usage** on the other — a two-sided ledger (supplier draw vs student
credits), not a single counter. And the architecture *controls* the re-read cost Mark suffered: the
**dossier (condensed context) + prompt caching** mean a student turn does NOT re-pay full freight to
reprocess the whole history — so a student credit goes far further than Mark's raw-chat experience.
**Suzy won't feel his pain partly by design, not only by disclosure.** (See tech_architecture_skeleton.md.)

## INDEX LINE
`knowledge/credit_value_pricing_model.md | business-plan, marketing, build | PUBLIC | captured | The MONETIZATION model (Finn-originated). Method: prove round-trip COGS first, then price up with margin; every cost input folds into the credit COGS. Premise: sell VALUE not knowledge — traders begrudge a $500/mo flat guru sub but gladly pay spend that returns more than it costs. The inversion (sauce): usage credits make spending a success-signal, not a resented bill (Suzy spends $300, P&L +$3,000 → feels like investing). Honest dependency (refined): value ≠ profit (90% fail = unfiltered base rate; Mark's filtered/coached cohort projected ~50–80% win, unproven; can't manufacture traders) — value = an honest attempt + the truth about fit; integrity move = the GRACEFUL HONEST EXIT (never take money for failure). Self-aligns with the ICP filter. Partners (ElevenLabs etc.) = COGS inputs = buying zero-ops, passed through with margin.`

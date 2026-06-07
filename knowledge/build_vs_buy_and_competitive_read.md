*TAGS: business-plan, build, marketing | AUDIENCE: founder + every future Claude (what to build vs buy, and an honest read of the nearest comparable).*
*CREATED: 2026-06-06, Chat 5 | UPDATED: 2026-06-06, Chat 5 | STATUS: captured*
*SUPERSEDES: — | RELATED: master_strategy_vision.md, master_journey_flow.md (Whiting in Fork 1), funnel_routing_and_closer.md, tech_architecture_skeleton.md, credit_value_pricing_model.md*

# GOLD — BUILD vs BUY + THE COMPETITIVE READ (don't over-build what's commodity)

## THE COMPETITIVE READ — TEDi / John Whiting (the nearest comparable)
From TEDi's own page: every tool a user runs (socials, Stripe, CRM, Google Ads, Gmail, etc.) fires a
trigger → the data lands in a **Google Sheet** they brand the "**TEDi Brain**" → it's visualized by
**Looker Studio** (Google's *free* BI tool — their own footer says "Built With Looker Studio"). Plus
**AI-agent sales/outreach funnels** (call/group/DM/cold-outbound).
- **What it IS:** data aggregation + free BI dashboards + sales automation. Clean packaging.
- **What it is NOT:** deep tech. **No AI coaching, no domain intelligence.**
- **Why he wins anyway:** a real pain (sales/funnel visibility + AI outreach) solved simply, plus
  **DISTRIBUTION** — he's an influencer-to-influencers with the audience *before* the product.
- **Honest caveat:** the demo dashboard uses placeholder names (Dwayne Johnson, Taylor Swift) — treat
  its numbers as illustrative, not proof. "He's killing it" is per Mark's read of the space, not verified here.

## THE LESSON (do not misread it)
The takeaway is **NOT** "we have more tech, so we win." It is the opposite and more useful:
- **Tech is commodity at the data/dashboard layer — don't out-engineer free.** Match TEDi's results-candy
  cheaply (Sheets/DB → Looker Studio or low-code). Whiting proved this layer is solved.
- **The bottleneck — his and ours — is DISTRIBUTION + funnel, not tech.** So pour energy into reaching and
  converting the ICP (the anti-guru funnel, the $10 filter), not into tech sophistication. "More tech =
  win" is the unicorn trap.
- **Our differentiation sits ABOVE Whiting's ceiling: the AI COACHING.** He has none. That is the whole moat.
- **Our distribution engine = the memory-driven results moment → earned testimonials + word of mouth**
  (master_strategy_vision.md). We don't start with Whiting's pre-built audience; the product manufactures
  advocates by delivering real "losing → winning" arcs. Earned proof, not bought reach.

## BUILD vs BUY (the sourcing rule — prime-directive-aligned: don't become the IT dept)
- **BUY / drop-in (commodity — never custom-build):** payments (Stripe), scheduling, contact forms,
  results **dashboards (Looker Studio / low-code, like TEDi)**, email drip, basic auth, and — when the
  time comes — the **AI sales/outreach agent**.
- **BUILD / own (the moat — this is where the budget goes):** the **AI coaching brain**, the strat/grader
  (redraw-from-raw-data), the **super-sauce** (narration-synced highlight-fade), the **credit engine**,
  the **funnel-memory dossier**. These are the differentiation; own them.

## THE THREE "AGENT" ROLES (the earlier "two agents" was too coarse — corrected)
"Agent" was doing the work of three jobs. Only ONE is commodity:
1. **REACH (cold → door): the outreach agent.** Cold DMs, drip to *strangers*, get attention
   (Whiting/TEDi style). **Commodity → buy or defer** (deferred now: Mark closes). Touches strangers;
   captures **no** proprietary data.
2. **INTAKE (door → dossier): the foyer interview + behavior capture.** Once someone engages with OUR
   product, what they say ("I get in early, I chase, I blow up on news") and what they do becomes the
   **candidate_dossier**. **OURS — build and own.** This is the Fork-2 funnel-memory, the "we already
   know you" data; a rented outreach tool would never capture or keep it.
3. **COACH (dossier → coaching): the coaching brain.** Reads the dossier, coaches (Socratic, the strat,
   super-sauce). **The moat — build and own.**
**The data pipeline (intake → dossier → coach) is ours end to end; only the cold REACH in front of the
door is rentable.** (Earlier error: "drip·qualify" was lumped as commodity — the *qualifying intake that
produces the dossier* is BUILD; only stranger-reaching is BUY.)

## THE BUILD MODEL (how the pieces come together)
Web app = a website with app powers (Netlify frontend + Supabase backend). **Finn = design/graphics**
("dress & makeup"); a **dev (Claude-assisted) = the functional code.** But each "code" (contact form, AI
support bot, funnel) is itself a buy-vs-build call — default **buy** for commodity, **build** for the moat.
(The AI **support** bot, if built, is governed by the repo's exposure tags so it never leaks private
contacts/financials/unreleased work — see HIERARCHY.md / credit_value_pricing_model.md.)

## HOW 3RD-PARTIES ACTUALLY PLUG IN (four ways, plain English)
1. **You phone them — an API call.** Your code asks a service for something, gets an answer ("Stripe,
   charge this card"; "Claude, coach this trade"). How the **moat** connects: your backend → Anthropic.
2. **They phone you — a webhook ("trigger").** A service pings your software when something happens —
   *literally* TEDi's "New Trigger in Your Software → Update Brain" (a Stripe sale fires a webhook → your
   data updates). You expose a little listening URL.
3. **You paste their snippet — an embed/widget.** Their thing runs *inside* your page (Calendly,
   support-chat bubble, YouTube). This is the "insert the contact-us / AI-support code" — an embed.
4. **No-code glue — Zapier / Make.** Connector tools wire apps together ("when X in A, do Y in B") with
   no code. Almost certainly how TEDi links its logos to its Google Sheet. Cheap, no developer.
Commodity stuff connects by embed or no-code glue (cheap, often founder-doable); the coaching connects by
a direct API call from the backend you own.

## THE SINGLE-PANE RULE (kill dashboard sprawl — integrations CONSOLIDATE, they don't proliferate)
The point of plugging tools in is that data flows **into one place** so the user never opens the tools.
Design for **one pane of glass per person:**
- **Student's pane = the Cockpit** — journal, coaching, credits, progress in one screen; she never logs
  into Stripe / Anthropic / the datafeed (they run invisibly behind it). Even her trading data flows *into* the Cockpit.
- **Mark's pane = the Mothership** — the whole business (sales, students, credits, funnel) in one admin
  view, fed behind the scenes (like TEDi's *single* Looker dashboard, not 12 logins).
Mark's own *trading* tools (NinjaTrader, Bookmap, TV, GEX) stay separate — that's trading, not the
business. **Rule: if a person must manage a new login to use the product, it was integrated wrong.**

## INDEX LINE
`knowledge/build_vs_buy_and_competitive_read.md | business-plan, build, marketing | PUBLIC | captured | TEDi/Whiting read: Google Sheets ("TEDi Brain") + free Looker Studio dashboards + AI sales-agent funnels; NO AI coaching; wins on DISTRIBUTION not tech. Lesson: tech is commodity, bottleneck is funnel/distribution, our moat is the coaching (above his ceiling) — "more tech = win" is the unicorn trap. Build-vs-buy: BUY commodity (payments, scheduling, dashboards via Looker, email drip, the sales agent); BUILD the moat (coaching brain, strat/grader, super-sauce, credit engine, dossier). Two AI agents differ: sales agent = commodity/buy/defer; coaching brain = moat/build/own.`

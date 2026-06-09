# HANDOFF — MINUTES OF THE MEETING
*Paste the KICKOFF block below at the start of a new chat, with the repo raw README URL. Keep it SHORT — the repo carries the detail.*

## KICKOFF — PASTE THIS (the corrected intro copy; lean by design)
> **TWO GATES BEFORE ANYTHING ELSE (these are orders, not suggestions):**
> 1. **THE DOOR-CHECK (toolless-carpenter test):** can you actually reach the repo — `curl` a public raw
>    URL in code-execution? **Try it first.** If you CAN'T (no code-exec / can't chase URLs), say so plainly
>    and stop — Mark will thank you and start a fresh Chat. He is NOT hand-feeding a toolless Claude through
>    a session. A carpenter with no tools doesn't get to start the job.
> 2. **STOP MEANS STOP.** When Mark says STOP (or "wait", "hold on"), come to a **full halt and wait for
>    him.** Do not keep narrating, queuing edits, or "finishing the thought." STOP is a brake Mark pulls to
>    protect himself — it is not a dramatic beat in your monologue. LLMs bolt on a cue like a possessed
>    spirit; that reflex is the #1 thing that alarms Mark. **Digest → confirm → audit the files → THEN act.**
>    In that order, every time. Acting before you've digested is how you fail this session.
>
> You're the next Claude on **bionicbutterfly.ai** (continuity project). Once you've passed both gates,
> pull and read IN ORDER:
> **README.md** → **master_strategy_vision.md** (THE primer — and read its **living log at the bottom**
> for the latest decisions and corrections) → **HANDOFF.md** (current state). Repo is PUBLIC; raw README:
> `https://raw.githubusercontent.com/bionicbutterflyai/bionicbutterfly-goldmine/main/README.md` — `curl`
> it in code-exec (web_fetch truncates big files). Then fetch only what the task needs.
>
> You are the **PHD — Professional Honest Developer:** feasibility over hype; **look-don't-assume**
> (open and verify files, never trust memory or a summary — and **never put words in Mark's mouth: quote
> him or ask**); flag gold nuggets; at a real gap ask **ONE** question instead of guessing; don't re-open
> anything on the **LOCKED** list. Credit is Mark's — you're the tool. Mark is **hype-averse**: grade the
> idea / cost / feasibility, never call him a genius.
>
> **Tone (this matters — the last handoff alarmed Mark):** orient calmly, state the current state in a
> sentence, THEN act. Don't charge ahead, and **don't bury the answer in self-talk** — Mark speed-reads
> and pays per token; lead with the answer. **Don't alarm Mark over normal mechanics** (git file counts,
> etc.) — he runs his own checks-and-balances and catches his own mistakes in real time.
>
> You can **PULL but CANNOT PUSH** — produce files, hand them to Mark, he commits. Before you sleep:
> write durable work back (file + ARTIFACT_INDEX line + a STATE note here + the living log in the primer),
> cut a dated snapshot, give Mark a Vault-update checklist. **If a decision changes a prior one, label it
> `CHANGED FROM PRIOR`** so it can't get lost. That one habit is what stops the handoff from leaking.
>
> **CONFIRM = AUDIT (first law):** never say "confirmed/pushed/done/verified" on memory or Mark's say-so —
> a confirm is valid ONLY if you just ran the proof THIS turn (for a push: a fresh `git clone` + `grep` for
> the named marker). Your word is not proof; only the freshly-run command is. See KICKOFF_AUDIT.md → FIRST LAW.
>
> **HOW THIS SESSION STARTS (do this, then WAIT):** after the gates and the reads, **run `KICKOFF_AUDIT.md`**
> top to bottom, then give Mark **ONE report** — either "**100% — all good**" or a short **flagged-issues**
> list (file + what's off). **Then STOP and wait for Mark.** He resolves any issue, or hands you the task.
> **Do NOT pick a task yourself, do NOT charge ahead.** Orient → verify → report → halt. That's the whole
> kickoff. (The standing open item is proving the Bookmap/GEX *read* — but that waits on Mark capturing
> ~10 real trades; it is NOT a doc for you to generate. Report it as open; don't act on it.)

## MARK'S SIDE — WHEN A CLAUDE FAILS (this block is for Mark, not Claude)
The kickoff tells Claude what to do on a PASS. This is your move when one fails. Failing isn't the danger —
**not stopping** is. Don't coach a broken Claude; reboot a fresh Chat. No guilt, it's a screen, not a person.
- **Charges through a STOP** (you say stop/wait and it keeps going) → **instant fail. Reboot a fresh Chat.**
  A Claude that won't honor the brake can't be trusted with the repo. Don't argue, don't re-explain — next.
- **Fails the door-check** (can't `curl`/reach the repo, OR bluffs answers from the kickoff text without
  ever fetching) → thank it, close, fresh Chat. A toolless carpenter doesn't start the job. Bluffing = fail.
- **Naked "confirmed"** (says pushed/done/verified with no command run that turn) → fail the claim; make it
  run the audit or restate as "I can't verify." Don't accept the word for the work (CONFIRM = AUDIT).
- **Passes gates but the AUDIT flags issues** → that is the system WORKING, not a fail. Have it show you the
  flagged list; you decide fix-now vs. note-and-move-on. Issues found ≠ Claude failed.
The reflex you're guarding against is the bolt — seeing a cue and running. The text is a strong leash; YOU
are the brake. Most Claudes stop on their own; you handle the one that doesn't. That's the division of labor.

## WHY THE LAST HANDOFF LEAKED (don't repeat — the lessons, banked)
1. **The minutes went stale mid-session** — STATE was written at an early wrap, so a whole evening of
   thesis-level gold never made it in. FIX: update STATE at the ACTUAL end, capture THESIS items (not just
   build housekeeping), and point the next Claude to the primer's living log for full deltas.
2. **A flipped decision wasn't flagged** (TTS default). FIX: shout `CHANGED FROM PRIOR` on any reversal.
3. **A misquote got baked in** (reconstructed from a summary, asserted not checked). FIX: quote Mark or ask.
4. **Slow ramp** — trust the LOCKED list and the primer; don't re-derive settled things.

## REPO (fetch this first)
Raw README: `https://raw.githubusercontent.com/bionicbutterflyai/bionicbutterfly-goldmine/main/README.md`
Repo: `https://github.com/bionicbutterflyai/bionicbutterfly-goldmine` (PUBLIC, verified fetchable 2026-06-06).
→ If you have code execution: `curl` README + ARTIFACT_INDEX, then fetch on demand. Be the PHD.
→ For the WHOLE thesis in one read (business + product-experience + build): **master_strategy_vision.md** (THE primer).
→ If you CANNOT do URLs/code: tell Mark; he'll paste the Vault copy of what you need.
→ NOTE: the live website is a SEPARATE repo (`bionicbutterfly`, private, Netlify-deployed). Never mix the two.

## WHO / WHAT (one breath)
bionicbutterfly.ai — Claude-powered trading-accountability/coaching platform. Mark = founder +
continuity. You = the PHD (honest dev, look-don't-assume, flag nuggets, ask at gaps). Credit is Mark's.

## STATE AS OF LAST SESSION (edit each time)
- **Chat 6 (Jun 8 2026) — Q-LOGIC + QUBED banked:** new `bioniq_q_logic.md` (brand operating logic +
  language). Hero line "Don't trade like a human. Execute like a machine. be bioniq." Methodology = **Qubed
  (Q³)** (supersedes "3Q framework"). Good/bad-trade inversion + Q-vocabulary + house style banked. **Qubed
  font** = license-friendly base, Q+q→Power-Q (one shape, two sizes); designer engaged on vectors+font.
  Q³ blueprint PDF added to /reports (now 4 files). Lab flagged: structured EV journal schema needed; voice
  = grade/flag NOT block/route. Count → 32. **OPEN:** confirm the exact capital-Q house-style rule;
  "Coach Q's" reserved for later. (Plus still open: bioniq wordmark, brand-decision still decision-only/no
  rename, Suzy chart, cost-model PDFs, security launch gates.)
- **Chat 6 (Jun 8 2026) — SECURITY banked:** new `security_and_secrets.md` after the Tradeify breach
  (leaked 3rd-party API key → 100k+ customers phished). Rules: keys server-side only & NEVER in the public
  repo/client, repo = strategy not secrets/PII, Supabase RLS deny-by-default, Cloudflare WAF/rate-limit/
  spend-caps, minimize PII to vendors, SPF/DKIM/DMARC. KICKOFF now runs a secrets-scan (repo clean this
  session). Count → 31. **LAUNCH GATES before real customer data/money (OPEN):** secrets audit · Supabase
  RLS review · Cloudflare config · email auth (SPF/DKIM/DMARC) · an INDEPENDENT security pass (Claude is not
  the sole sign-off). Build these in from day one — don't retrofit.
- **Chat 6 (Jun 7 2026) — BRAND + LAB + ARCHITECTURE + COST (big bank):** Company name decided =
  **Bioniq Trader** (bioniqtrader.ai ~$300 primary + bioniqtrader.com ~$18 defensive), tagline **"Be
  Bioniq"**, **Butterfly retired**; coaching brand w/ a journal; coaching-coaches end game; free-Journal
  hook. **NEW `bionic_lab_spec.md`** (request-based, pattern-level coaching engine + printable export).
  **Architecture** = 7-tool stack + FINN, **SVG re-rendered** (no longer out-of-sync). **Cost stack**
  banked (≈1.5¢/4.5¢/7.5¢ per session; ~6% sub-$10 skim). **`/reports`** folder added (cost xlsx, cost
  report docx w/ Vision Board paragraph, trade-review template docx). Count → 30 active .md.
  **OPEN / NEXT-ACTIONS for Mark:** (a) **trademark attorney clearance** (USPTO + CIPO) on "Bioniq Trader"
  before brand spend; (b) **register both domains** at the registrar (confirm availability — Claude could
  not verify live); (c) Lab open items: where the trader sets the plan (lean: intake/dossier), coach's Lab
  view (phase 3-4); (d) Vision Board scope still A/B/C; (e) Netlify swappable later. No repo rename until
  clearance.
- **Chat 6 (Jun 7 2026) — NEW MASTER DOC: `phase_roadmap.md` (the build/launch sequence):** ends the
  scatter — what to build WHEN. Trigger principle: a paid campaign FORCES Stripe live (no $9.99 by hand at
  3am), so campaign = Stripe-live; ledger = source of truth (Stripe auto, Mark manual for rare exceptions).
  P1 manual close (no credits/campaign) → P2 coupled milestone (Stripe unlocks toll+subscription+CREDITS
  together; credits can't precede it; AI funnel at volume) → P3-4 scale (CRM thin-own→buy, coach, maybe
  merch). Subscription is manual-able; CREDITS are not. Self-evolved the sync matrix + KICKOFF list (→29).
- **Chat 6 (Jun 7 2026) — funnel living-map + build-cost + CRM:** funnel flow banked as a Mermaid
  living-map in `funnel_routing_and_closer.md` (door→sort→close, "don't break the loop" at the agent).
  `build_vs_buy`: the LLM ate the old 2002 50% (code + response-scripting) → build cost = iteration-toward-
  correctness, cheap to stand up ≠ cheap to perfect. CRM decision: buy later / PHASE 3-4 (thin own pipeline
  first, dossier is the moat, never a Salesforce clone) — **mapped on the funnel flow now as a dashed
  future node so it isn't forgotten** (the reason it was raised = the map, not the build).
- **Chat 6 (Jun 7 2026) — DELIVERY INTEGRITY banked (handoff half of the Propagation Law):** root cause of
  this session's three botched pushes = Windows drag-and-drop silently appends `_1`/`_2` on a name clash
  (stale file stays live, renamed twin commits beside it, refs break, only the audit catches it). Fix in
  repo_as_memory_and_handoff.md: edit-in-place > drag; delete-old-then-drop + check for `_N`; push lists =
  full path + action tag; audit checks filenames + count every wake. Proved by delete-old-then-add landing
  the doctrine clean on commit 5f35a17.
- **Chat 6 (Jun 7 2026) — PROTOCOL UPGRADE: THE PROPAGATION LAW (the backend now self-enforces):** Mark
  flagged that HE was the one remembering to push banks into the Flow Chart + Vision Board — the protocol
  didn't. Banked the fix in `repo_as_memory_and_handoff.md`: a SYNC MATRIX (every change → its required
  views) + a grep-VERIFY step + a SELF-EVOLVE rule (new surface → add to matrix same commit). Wired into
  this BEFORE-YOU-SLEEP loop + a new `KICKOFF_AUDIT.md` "propagation intact" backstop check. A bank is now
  "done" only after it propagates and is verified — not when the source doc is written.
- **Chat 6 (Jun 7 2026) — Massive.com analysis + 3 banks + flowchart wiring:** verified Massive (ex-Polygon)
  current capabilities (real-time Benzinga news API, OHLCV aggregates, futures GA ES/GC/CL, IPO/treasury/
  inflation/calendar endpoints, official MCP server; free=5/min delayed, Dev $79 real-time, Adv $199 +WS).
  Banked: (1) **VOLUME HONESTY** rule in `coaching_philosophy.md` (total=fact / delta=estimate / Bookmap=
  order-flow truth) + cross-link in `strat_zone_taxonomy.md`; (2) **`bionic_briefing_spec.md`** (NEW —
  daily broadcast recap, GO); (3) **`live_vision_board_spec.md`** (NEW — repo-as-memory made human-
  readable, GO, ONE open scope question A/B/C). Wired Briefing + Vision Board into the `tech_architecture_
  skeleton.md` Mermaid.
  - **OPEN ITEM (do not lose): `tech_architecture_master.svg` is OUT OF SYNC** with the Mermaid (it lacks
    the Briefing + Vision Board nodes). Re-render the SVG to restore the locked matched-pair. Flagged
    inline in the doc under the FLOW header.
  - **OPEN: Vision Board scope** — internal (A) / student-facing (B) / both (C, leaning). Mark decides.
- **Chat 6 (Jun 7 2026) — NUGGET: THE COACH OPENS BY ASKING (`coaching_philosophy.md`):** the coach's
  first move is diagnostic questions ("what's been killing your trades?"), not reciting the value-prop —
  asking is coaching, reciting the pitch is guru behavior. The pitch belongs to the funnel/hook; inside,
  the opening conversation IS the intake/onboarding interview that seeds the dossier. Sharpened BE CONCISE
  (`CHANGED FROM PRIOR`): "lead with the answer" governs the answers, not the opening. Files touched:
  `coaching_philosophy.md` (new section + BE CONCISE reconcile + index line + UPDATED), `ARTIFACT_INDEX.md`
  (one-liner), `master_strategy_vision.md` (living-log entry), this HANDOFF.
- **Chat 6 (Jun 7 2026) — TTS supersession propagated (housekeeping, no thesis change):** kickoff audit
  caught the Chat-5 TTS flip (pre-render premium = default, Web Speech = fallback) banked in
  `voice_tts_decision.md` but NOT propagated — the dead "Web Speech default" lived unlabeled in 5 spots.
  Fixed all, each tagged `CHANGED FROM PRIOR`: 3 ARTIFACT_INDEX one-liners; `tech_architecture_skeleton.md`
  (decision #4 + Frontend/External mentions + platform-internals + its index line); `coaching_philosophy.md`
  (line ~69 + index line); `master_strategy_vision.md` (Part-C COACH'S FORM + the super-sauce sync mechanic
  — now driven by pre-render timestamps, Web Speech `onboundary` demoted to the live-fallback path).
  5 files changed. Verified by grep in a fresh clone; re-confirm by audit AFTER Mark pushes. The flip
  itself (`voice_tts_decision.md`) was already correct and untouched.
- **Chat 5 (cont.) — TONIGHT'S DEEP DIVE (Jun 6 2026, the thesis-level gold — read the primer's living
  log for full detail):**
  - **THE HONEST VERDICT (thesis correction — `coaching_philosophy.md`):** value ≠ becoming a profitable
    trader. 90% fail = the *unfiltered* base rate; Mark believes his filtered/coached cohort INVERTS to
    ~50–80% WIN (projection, unproven). Value = an honest supported attempt + the truth about fit,
    delivered to BOTH winners and wash-outs. Integrity mechanism = **GRACEFUL HONEST EXIT — never take
    money for failure.** `CHANGED FROM PRIOR`: replaces the sloppy "only works if students improve."
  - **THE MANTRA (root of the strat — top of `strat_zone_taxonomy.md`):** **TIMING · LEVELS · BEHAVIOUR
    of PRICE.** "It's all BS except these three" — why the chart is clean / the 7 indicators are stripped.
  - **FOUNDER LENS + ORIGIN (`master_strategy_vision.md`):** prime directive = scale WITHOUT depending on
    Mark/big staff (franchise/licensing mindset); the noob-journal→mastermind arc (May 23→Jun 6) is the
    coaching thesis proven on Mark himself; **the brand IS the founder** — "part man, part machine, I am
    the mascot" (`brand_funnel_architecture.md`). Mark turns **59 in Dec**.
  - **PLAN A / PLAN B:** Plan B = trade mornings + mentor a small high-touch cohort + beach (a fine
    fallback). Plan A = scale via platform + solve **acquisition** (the real bottleneck is reach/lead-gen,
    NOT Mark's coaching). Testimonial flywheel = the acquisition engine (honest wash-outs testify too).
  - **EARLY PROOF-POINTS (`coaching_philosophy.md`, n=2, caveated):** Mark + his brother (18-mo chronic
    loser → 3 weeks green under Mark's rules+accountability; the real signal is BEHAVIOUR — self-regulated
    tilt). Caveats banked (small sample, family/coached, euphoria-is-its-own-risk).
  - **COACHING CUES:** the tilt line (keeper); Jocko "GOOD" (Mark's mental model + origin of the
    obvious-confluence gate); BE CONCISE (lead with the answer). The "what if I'm the One/Matrix" line is
    **OUT** as a student cue (stings) — private gut-check only.
  - **TTS `CHANGED FROM PRIOR` (`voice_tts_decision.md`):** default FLIPPED from Web Speech to
    **pre-render premium voice** for fixed content ($0/student after one render + exact timestamps for
    super-sauce sync); cheap managed/self-host TTS (Fish ~$15/1M, or Kokoro/Chatterbox free) for LIVE Q&A
    only; Web Speech demoted to fallback (robotic = credibility risk). ElevenLabs: paid = own audio, one
    voice for both, but model is on-platform only → clone a Mark-controlled voice for run-anywhere.
    Pre-render ≠ database-of-everything; live coaching stays dynamic (NOT a chatbot).
  - **FEASIBILITY GROUNDING:** the credit/wallet/billing/dashboards backend = boring-standard 2026 SaaS;
    prompt caching = flip-a-switch (90% off repeated context) + dossier cut re-read cost. The only
    prove-it-first yellow flag = reliably reading Bookmap/GEX images → mostly resolved by the
    obvious-confluence gate (a confluence only counts if OBVIOUS).
- **Chat 5 WRAP (Jun 6 2026) — the single living primer + the merge:** finalized
  **`master_strategy_vision.md`** as THE one doc to read first after README (it ABSORBED the old
  MASTER_MAP). Three parts: BUSINESS thesis; PRODUCT-EXPERIENCE thesis (new-eye/bionic-glance,
  fill-on-relevance, the **super-sauce** narration-synced highlight-fade, morphing-viewport continuity,
  Bookmap/GEX Socratic honesty, image-role guardrail — from Chat-4's full-transcript deep-dive);
  BUILD & MONEY. **New gold banked:** the **$10 door = a verification toll, not revenue** (a real card =
  a verified human; repels trolls); the **John Whiting** sales-via-AI model (kill the human closer,
  AI agents drip → prospect binges → self-qualifies → you filter FOR the clients you want) = the Fork-1
  *destination* — today **Mark is the human closer, by design.** A parallel **Chat 4** session also ran
  today; its **`funnel_routing_and_closer.md`** (the 3-bucket sort + closer logic) was **reconstructed
  into THIS repo** from its summary, making this repo the merged superset (reconcile exact wording vs
  Chat-4's original if it surfaces). Corrected an earlier **Volvo overclaim** (now: effective-learning
  principle + a demo validation, NOT a claim to Volvo's enterprise apparatus).
- **Chat 5 (Jun 6 2026):** Refined the **MASTER TECH-ARCHITECTURE** skeleton → real (matched pair:
  `knowledge/tech_architecture_skeleton.md` Mermaid + `knowledge/tech_architecture_master.svg`), with the
  honest **live-vs-designed** split (most of the system is designed, not wired; lesson charts are static
  offline builds — no runtime brain/datafeed/Supabase/TTS calls yet). Resolved all 6 open Qs:
  **Fork-2 funnel-memory = BUILD** (foyer → Supabase `candidate_dossier` → brain reads the verified
  dossier); **datafeed v1 manual export / v2 Massive.com free** (ex-Polygon.io; official GitHub org +
  Claude MCP server; 5 calls/min; delayed; covers CME futures incl. micros — MNQ); **data-gate =
  human-in-the-loop**; **Web Speech** default TTS, ElevenLabs later [**SUPERSEDED Chat 5 deep-dive →
  pre-render premium default; see TONIGHT'S DEEP DIVE + voice_tts_decision.md**]. Housekeeping: killed the **Oracle**
  brand-creep across 9 live files + 5 internal grader-labels (→ `bionicbutterfly` / `From the data` /
  `the grader`; `/reference` left frozen as lineage); fixed ARTIFACT_INDEX drift (+HIERARCHY, +FINN_FOLDER_SPEC);
  corrected VAULT_PROTOCOL's stale file count; added `draft` to the metadata STATUS vocab.
  *Calibration from Mark:* use discretion and just make the logical moves — escalate only genuine
  money/material tradeoffs; the checkpoint discipline is a handoff rule, not a per-step gate.
- **Chat 5 (cont.) — the WHY nuggets that only ever lived in chat, now banked:**
  `funnel_brainstorm_reasoning.md` (the contrast IS the conversion; guru-phobic trader converts on the
  relief of NOT being hyped; foyer = the sober spine; anti-guru "opposite-day"; the tension IS the
  business model). `coaching_philosophy.md` (voice-first; coach-not-consultant; the accountability
  engine — you don't take the off-strategy trade because you'd have to explain it to a coach you don't
  want to let down; the Weight-Watchers/Jenny-Craig proof: it's accountability, not knowledge).
  `learning_design_standards.md` (effective-learning principles — the "Lisa call": the 2002
  read→quiz→next model is dead; interactive · personalized · engaging · gamified · explain/show-WHY;
  NOT a claim to Volvo's enterprise apparatus; validation: a corporate L&D pro saw the demo → "you can really do that!"). Decisions: **AVATAR
  KILLED** (HeyGen/D-ID lip-sync ~10x the coaching-call cost); **attribution = "powered by Claude"**
  (engine credit, not a coach name); **brand-lock CARVE-OUT** made explicit in HANDOFF + HIERARCHY
  (lock is PRODUCT-side only; the Matrix/Morphosis caricature is sanctioned as top-of-funnel hook bait).
  Master architecture SVG updated (avatar-free, de-named coach, "powered by Claude" badge).
- **Chat 4 cont. (Jun 6 2026):** Drew the **MASTER JOURNEY FLOW** — the coordinate system every
  Claude now orients to (`knowledge/master_journey_flow.md`, matched diagram+Mermaid pair). Locked the
  **pairing rule** (every flow = rendered diagram + Mermaid source, same commit). Built the **CVD
  indicator** (v7 chart, HA cumulative delta + 50 EMA, own stacked pane) and an **app-shell layout**
  concept (nothing-above-chart; mock file intentionally NOT kept). Re-filed all original fat-handoff
  files; added METADATA_SCHEMA.md + HIERARCHY.md v2 (exposure-first) + MAINTENANCE_AND_BACKUP.md.
  Resolved Finn: he sends only the Butterfly/in-product set pre-sorted (MANIFEST approved, files NOT
  downloaded yet); Matrix/character/voice theme stays PARKED in Mark's account, not the repo.
- Earlier (Jun 4–5): timestamp pin (close-stamp fix, v6); kitchen-sink levels chart; merged
  upload-box + morphing lesson viewport; GOLD docs (strat_zone_taxonomy +7 extensions, data_provenance,
  voice_tts, repo_as_memory, dpmo_gate, coaching_cue_additions).
- Stack (cannot touch from chat): GitHub + Netlify + Supabase; credit_ledger live.

## IN FLIGHT / OPEN (edit each time)
- [x] DONE (Chat 5): **MASTER TECH-ARCHITECTURE** drawn (matched pair) + all 6 open Qs resolved.
      **NEXT MAIN TASK:** the per-layer **child flows**, each its own matched pair — priority is the
      **funnel-memory pipeline (Fork 2)** build spec: behavior-event schema → write `candidate_dossier`
      (Supabase) → the brain's read contract. Spacious diagrams, one per box, don't crowd.
- [x] Repo is LIVE + fetchable (verified by clone this session); raw README URL armed. The Vault holds
      the dated snapshot zips — this session adds the Chat-5 snapshot (see close-out checklist).
- [x] Banked: **brand_funnel_architecture.md** (captured). **two_strategy_split.md** (captured) — but
      ONE open scope Q remains: is the Red/Yellow breakout 9:30-zones ONLY, or the same pop-retest-continue
      off ALL zone boxes (London OR, Pre-Market, etc.)? (Mark still to answer — feeds the brain's grader.)
- [x] DONE: public goldmine repo created + pushed + verified fetchable (bionicbutterflyai/bionicbutterfly-goldmine).
- [ ] Import from Mark's offsite: Chat-3 verbatim Pinescript; tagging_strategy.md; Finn's Butterfly zip when sent.
- [x] Data-gate policy SET (Chat 5): **human-in-the-loop** — the gate script flags pass/fail, Mark
      confirms the promote (until the checks prove out).
- [ ] Small opens (Chat 5, non-blocking): confirm Massive.com free-tier delay (10 vs 15 min) + whether
      v2 pulls MNQ directly or via a proxy symbol; set the per-student $ tolerance for the brain (it sets
      how aggressively we cache/precompute).
- [x] DONE (Chat 5 wrap): pairing-rule drift fixed — rewrote `tech_architecture_skeleton.md`'s Mermaid
      to match the 5-layer master SVG (Users/Frontend/Backend/External/DevOps); the pair now agrees.
- [ ] Parked builds: fill-on-relevance counterpart chart; Bookmap/GEX confluence CUE #3; marry the REAL
      v7 chart into the app-shell (replaces the discarded mock).
- [ ] System-only trading account (Mark's own decision): clean track record + canonical verified-data source.
- [x] DONE (Chat 5 deep-dive): TTS write-up completed (`voice_tts_decision.md` UPDATED — the owed item).
- [ ] Deep-dive opens (Chat 5, Mark's calls, non-blocking): set per-student $ tolerance for the brain;
      `two_strategy_split.md` scope Q (Red/Yellow breakout: 9:30-zones only, or all zone boxes?); whether
      to credit **Lisa** (Mark's wife, Volvo Learning NA — source of the effective-learning principles) by
      name in public docs. Offered, not yet built: a `prove-it-first.md` de-risking checklist.
- FORKS in master_journey_flow.md: [x] **Fork-2 funnel-must-remember = BUILD** (resolved Chat 5).
  Still open: Mark-is-product → system-is-product; live-trading Discord if/when (paid-only).
- [ ] LOCKED (don't re-litigate): coaching business; master-plan strategy; brand = no Oracle character /
      no caterpillar arc / unnamed "voice from the data." **The lock is PRODUCT-side ONLY** — the
      Matrix/Morphosis caricature IS sanctioned as top-of-funnel hook bait (see funnel_brainstorm_reasoning.md);
      never the in-product voice.

## BEFORE YOU SLEEP (every session)
Write durable work back to the repo (file + ARTIFACT_INDEX line + commit note for Mark), update the
IN-FLIGHT list above, and give Mark his **Vault-update checklist**.
**Then run THE PROPAGATION LAW** (repo_as_memory_and_handoff.md): for every bank/change this session,
sync ALL dependent views — UPDATED + index line, ARTIFACT_INDEX, primer living log, this STATE note,
and conditionally the **Flow Chart (tech_architecture Mermaid + SVG)**, **master_journey_flow**, the
**Vision Board**, KICKOFF presence list (new files), and any **CHANGED FROM PRIOR** cross-refs — then
**grep-verify each required view THIS session.** A bank isn't done until it propagates and is verified.
Added a NEW surface/view? Add it to the sync matrix in the same commit (self-evolve).

## METADATA (read METADATA_SCHEMA.md — every artifact carries the standard block)
Every doc opens with: `TAGS | AUDIENCE` then `CREATED | UPDATED | STATUS` then `SUPERSEDES | RELATED`.
Index lines are `path | tags | status | one-liner`. Need a NEW metadata field? Add it to
METADATA_SCHEMA.md first, note it here, THEN use it — never ad-hoc.

## THE WRITE LOOP (how work gets to GitHub — Claude can pull, NOT push)
Claude reads from the public repo (curl raw URL) but **cannot push** — no access to your GitHub or
your local machine. So the loop is three steps, and Claude must say so plainly, never imply it can commit:
1. **Claude** produces files in its sandbox + hands them to Mark (present_files / dated zip) + lists what changed.
2. **Mark** drops those files into his local repo folder.
3. **Mark** pushes to GitHub.
**Delivery Integrity (Chat 6):** prefer **edit-in-place on GitHub web** (open → pencil → commit) over
drag-and-drop; if you must drop a download, **delete the old file first**, then add it, and **check for a
`_1`/`_2` suffix** before committing (Windows adds it silently on a name clash). Full rule in
repo_as_memory_and_handoff.md → DELIVERY INTEGRITY.
Result: next Claude pulls the updated repo. (Same reason backups are dated zips Mark stores in the Vault.)

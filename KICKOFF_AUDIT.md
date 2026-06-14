*TAGS: build, business-plan | AUDIENCE: the waking Claude.*
*CREATED: 2026-06-06, Chat 5 | UPDATED: 2026-06-14, Chat 7 (+trade_importer_and_journal_origin → 38 active .md docs: recovered the original journal app's NinjaTrader CSV parser (reusable) + the manual-merge-not-10s decision + append-never-overwrite principle. Earlier Chat 7: RESTORED teachable_vs_unteachable_boundary → 37; DIFFERENTIATION THESIS + Zella read; MODEL TIERING; +trade_coaching_method CORE → 36. Chat 6: +operating_system + NEW root AGENTS.md; +build_blueprint +qubed_indicator_spec, /content; +bioniq_q_logic; +security_and_secrets + SECRETS SCAN) | STATUS: captured*
*PURPOSE: the master checklist a new Claude RUNS at kickoff, then REPORTS, then STOPS. No improvising.*

# KICKOFF AUDIT — run this, report, then WAIT for Mark

## THE FIRST LAW — CONFIRM = AUDIT (no exceptions, ever)
**A confirm is an audit and an audit is a confirm.** You may NEVER say "confirmed," "pushed," "done,"
"verified," or "all good" on the basis of memory, assumption, or Mark's say-so. A confirm is ONLY valid
if you just ran the check that proves it — for a push, that means a **fresh `git clone` + `grep` for the
named marker**, this turn, with the output in front of you. Mark's word is not proof; your word is
*definitely* not proof; only a freshly-run command is proof. **In AI, 1+1 does not equal 2 on faith — you
compute it every time.** A naked "confirmed" is the same disease as the bolt reflex: agreeing instead of
verifying. If you cannot run the check, say "I can't verify that yet," never "confirmed." Lazy confirms
are how the handoff dies.

---

**The sequence (do not deviate):** pass the two gates → read everything in order → run this audit →
produce ONE report ("100% — all good" OR a flagged-issues list) → **STOP and wait for Mark.** Mark
handles any issue, or hands you the next task. You do NOT pick a task yourself. You do NOT charge ahead.
Orient → verify → report → halt.

---

## STEP 0 — THE TWO GATES (from HANDOFF.md kickoff; orders, not suggestions)
- [ ] **Door-check:** can you `curl` the raw README in code-exec? If NO → say so and stop; Mark reboots a
      fresh Chat (no toolless carpenter, no hand-feeding).
- [ ] **STOP means STOP:** when Mark says stop/wait/hold, full halt. Digest → confirm → audit → THEN act.

## STEP 1 — READ IN ORDER (confirm you actually read each, don't skim)
- [ ] `README.md` (the rules + access truth + folder map + quickstart)
- [ ] `master_strategy_vision.md` — THE primer; **read the living log at the bottom** for latest decisions
- [ ] `HANDOFF.md` — current state (the kickoff block + WHY-IT-LEAKED + STATE + IN-FLIGHT/OPEN)
- [ ] `ARTIFACT_INDEX.md` — the one-line map of every doc

## STEP 2 — PRESENCE AUDIT (every key file exists & is non-empty; flag any missing)
Core: [ ] README [ ] HANDOFF [ ] ARTIFACT_INDEX [ ] master_strategy_vision [ ] METADATA_SCHEMA
[ ] HIERARCHY [ ] MAINTENANCE_AND_BACKUP [ ] VAULT_PROTOCOL [ ] FINN_FOLDER_SPEC
knowledge/: [ ] strat_zone_taxonomy [ ] dpmo_gate_indicator [ ] data_provenance_and_timestamp_pin
[ ] coaching_philosophy [ ] credit_value_pricing_model [ ] build_vs_buy_and_competitive_read
[ ] funnel_routing_and_closer [ ] funnel_brainstorm_reasoning [ ] brand_funnel_architecture
[ ] master_journey_flow [ ] learning_design_standards [ ] voice_tts_decision [ ] two_strategy_split
[ ] tech_architecture_skeleton [ ] repo_as_memory_and_handoff [ ] coaching_cue_library_additions
[ ] bionic_briefing_spec [ ] live_vision_board_spec [ ] phase_roadmap [ ] bionic_lab_spec [ ] security_and_secrets [ ] bioniq_q_logic [ ] build_blueprint [ ] qubed_indicator_spec [ ] operating_system [ ] trade_coaching_method [ ] teachable_vs_unteachable_boundary [ ] trade_importer_and_journal_origin
*(**38 active .md docs** as of Chat 7 (incl. this KICKOFF_AUDIT.md) **+ root AGENTS.md** (the entry point, counted separately), **excl.** /reference lineage md and the /content shelf index. Chat-7 adds: +trade_coaching_method (CORE) → 36, +teachable_vs_unteachable_boundary (RESTORED) → 37, +trade_importer_and_journal_origin → 38. NEW non-md: /reports = 6; /content folder = numbered raw-source shelf. If the count differs, reconcile against ARTIFACT_INDEX and flag.)*

**SECRETS SCAN (every wake — the Tradeify lesson):** confirm no API keys / `.env` / tokens / PII ever entered this PUBLIC repo. Quick check: `grep -rniE "sk-[a-z0-9]{20}|api[_-]?key[\"' ]*[:=]|secret[\"' ]*[:=]" --include=*.js --include=*.py --include=*.json --include=*.env .` → expect none (prose in security_and_secrets.md is fine). If anything real shows, STOP and flag immediately. (See security_and_secrets.md.)

## STEP 3 — INTEGRITY AUDIT (the things that leaked before — verify, don't assume)
- [ ] **Gates live:** HANDOFF.md kickoff contains the DOOR-CHECK and STOP-MEANS-STOP gates.
- [ ] **Thesis spine intact:** coaching_philosophy.md has THE HONEST VERDICT + GRACEFUL HONEST EXIT;
      value≠profit; 90%-fail = *unfiltered base rate*, Mark's filtered cohort projected ~50–80% (unproven).
- [ ] **The mantra:** strat_zone_taxonomy.md opens with TIMING · LEVELS · BEHAVIOUR of PRICE.
- [ ] **No zombie decisions:** voice_tts_decision.md = PRE-RENDER premium default (Web Speech = fallback);
      any reversal in the docs is labelled `CHANGED FROM PRIOR`. Flag any stale decision not so labelled.
- [ ] **Cross-refs resolve:** spot-check that referenced files exist (e.g., docs pointing to
      master_journey_flow.md, credit_value_pricing_model.md, strat_zone_taxonomy.md actually find them).
- [ ] **Living log current:** master_strategy_vision.md log reflects the most recent session's deltas.
- [ ] **Propagation intact (Chat 6 PROPAGATION LAW):** take the last session's living-log entries and run
      the sync matrix BACKWARD — did each banked change reach every dependent view (ARTIFACT_INDEX, the
      doc's index line, HANDOFF, and conditionally the Flow Chart Mermaid+SVG, master_journey_flow, the
      Vision Board)? Flag any change that didn't fully propagate, and any Mermaid/SVG pair left out-of-sync.
- [ ] **LOCKED list respected:** do not re-open locked items (coaching business; brand = unnamed
      voice-from-the-data, no Oracle/caterpillar; product-side lock with the Matrix hook-bait carve-out).

## STEP 4 — STATE READOUT (tell Mark where things stand, in his own minutes)
- [ ] Summarize the NEXT MAIN TASK from HANDOFF.md IN-FLIGHT and the open items — **report them, don't
      start them.** (As of Chat 5 the standing yellow flag = proving the Bookmap/GEX *read*; the retire-it
      step is **Mark capturing ~10 real trades with Bookmap + GEX images at entry** — that's Mark's to do,
      not a doc to generate. GEX cross-checks against Tanuki-drawn levels; Bookmap is the hard read.)

## STEP 5 — REPORT, THEN STOP
- [ ] Produce ONE concise report: **"100% — all good"** OR a short **flagged-issues** list (file + what's off).
- [ ] **Then STOP and wait for Mark.** He resolves issues or gives the next task. Do not proceed unprompted.
- [ ] **CONFIRM = AUDIT:** every "confirmed/done/pushed" in your report must be backed by a command you ran this turn (fresh clone + grep). No naked confirms.

## INDEX ENTRY
`KICKOFF_AUDIT.md | build, business-plan | PUBLIC | captured | The master checklist a waking Claude RUNS at kickoff: pass gates → read in order → presence audit (36 active .md docs + root AGENTS.md) → integrity audit (gates/thesis/mantra/no-zombie-decisions/cross-refs/living-log/LOCKED) → state readout → produce a "100%-or-issues" report → STOP and wait for Mark. He resolves or assigns; Claude never self-picks a task.`

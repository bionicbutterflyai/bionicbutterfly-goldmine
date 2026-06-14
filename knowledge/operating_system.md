*TAGS: build, business-plan, process | AUDIENCE: founder + every future Claude. THE most leveraged doc in the repo — it improves EVERY session, not one area. Read after the cold-start gates.*
*CREATED: 2026-06-09, Chat 6 | UPDATED: 2026-06-09, Chat 6 | STATUS: captured (refinements rolling out — see §3)*
*SUPERSEDES: — | RELATED: repo_as_memory_and_handoff.md (the mechanics), KICKOFF_AUDIT.md (the entry), build_blueprint.md (numbered addressing)*

# GOLD — THE bioniq OPERATING SYSTEM (how man + machine work)

## ONE-LINE
The method for working between Mark (project lead) and Claude (the machine): a git-backed memory repo +
a lean agent-instruction entry point + numbered addressing + a strict bank discipline. Built by gut across
Chats 1-6; VALIDATED against the field (Google/OpenAI/Letta/research all converged on the same primitives);
now tuned with 5 refinements the field learned that we hadn't.

## 0 · THE STORY (so no future Claude thinks this was copied)
By Chat 3 the plain chat-to-chat handoffs were failing — Mark was re-explaining everything every session
(counter-productive). Mark challenged "what if GitHub is the memory?" — and the handoffs got better every
chat after. By Chat 6 we researched the field and found we'd independently invented the exact architecture
the industry standardized on in 2025-26. The gut was right. This doc captures the method + the upgrades.

## 1 · WHAT WE BUILT = WHAT THE FIELD BUILT (validation, not coincidence)
- **Git-as-memory** is now a funded, researched category. The problem we hit ("sessions forget; user
  re-explains every time") and the fix we chose ("a new agent — even on a different LLM — resumes from the
  exact state its predecessor left, like devs collaborating through Git") are described almost verbatim in
  research (Git Context Controller, arXiv 2508.00031) and shipped as product (Letta "Context Repositories":
  git-backed memory, every change versioned with commit messages). = our goldmine.
- **The agent-instruction file** is now an open standard: **AGENTS.md** — Linux-Foundation-stewarded, 20,000+
  GitHub repos, launched by Google/OpenAI/Factory/Sourcegraph/Cursor. "A README for agents." = our cold-start
  script + KICKOFF_AUDIT.
TAKEAWAY: we're early and correct, not nutty. This doc is the moat for HOW we build (speed + consistency).

## 2 · THE METHOD (the parts that already work — keep)
- **Repo = the ONE source of truth.** Claude banks in nano time; Mark reads his local clone in a nice window.
- **CONFIRM = AUDIT (first law).** Never say done/pushed/verified on memory — only a freshly-run proof THIS
  turn counts (git clone + grep + secrets-scan).
- **Numbered addressing.** Everything is numbered (areas 1-11, pieces 8.4). Mark says a number, Claude opens
  it. No pasting, no re-explaining.
- **Bank discipline.** Bank on Mark's explicit GO only, as ONE full-repo zip → replace-all (never batches,
  never keep-both). Propagate every dependent VIEW the same session (the Propagation Law). **The bank
  SEQUENCE (added Chat 7 after a wrong-repo near-miss): confirm repo is `bionicbutterfly-goldmine` →
  extract zip → commit → push → audit.** The FIRST step is non-negotiable: eyeball the repo name
  (`bionicbutterflyai/bionicbutterfly-goldmine`, PUBLIC, no lock) BEFORE dropping files — the public goldmine,
  never the private `bionicbutterfly` app repo. (A Chat-7 bank went into the private app repo by skipping
  this check; recovered by revert, but the check makes it structurally hard to repeat.)
- **The loop.** discuss → Claude updates the source → Mark reads later → flags edits by number → repeat.
- **Index vs meat.** build_blueprint = terse index; per-area DEEP docs hold the meat. Raw source docs →
  /content shelf. Proprietary recipes → PRIVATE/local, never the public repo.

## 3 · THE 5 REFINEMENTS (what the field knew that we didn't — roll these in)
1. **Standardize the entry point as `AGENTS.md`.** Wrap the cold-start/KICKOFF as a root-level AGENTS.md so
   ANY agentic tool (Claude Code, Cursor, Copilot) auto-loads it free. (Keep CLAUDE.md as a pointer/alias if
   useful.) STATUS: planned — see §4.
2. **LEANER instruction files, not longer (counter-intuitive, biggest finding).** "As instruction count
   increases, instruction-following quality decreases." Human-written files should hold only what the agent
   CANNOT discover itself — commands, constraints, the LOCKED list, the gates — NOT architecture overviews
   (the repo already carries those). Trim KICKOFF/entry to rules+gates; let the docs carry the rest.
3. **Beware the "Pink Elephant."** Telling an LLM "do NOT do X" makes token X highly active — it may reach
   for it anyway. Every "don't" is a signal of structural friction. PREFER making the bad path IMPOSSIBLE by
   structure over FORBIDDING it by instruction (e.g. the one-zip/replace-all flow structurally prevents the
   _N collisions that a "never keep both" rule only warns against). Convert don'ts → structure where we can.
4. **Name the MEMORY TIERS.** Computer-style hierarchy: CORE memory (the 5-10 things EVERY session must load:
   brand, rules, current state, LOCKED list) vs ARCHIVAL (fetch by number only when the task needs it). Our
   read-order half-does this; naming the tiers makes "load lean, fetch on demand" deliberate + cheap.
5. **Context-cost discipline (hard data: >50% cheaper, no quality loss).** Don't load the whole goldmine
   every session. Load CORE, then fetch by numbered address only what the task touches. Numbering already
   enables this — formalize "load lean / fetch on demand" as the rule. (Mark pays per token + speed-reads —
   this is directly aligned.)

## 4 · ROLLOUT (do, in order — each is small)
- [ ] Create root `AGENTS.md` = the lean entry (gates + rules + LOCKED list + "read order" + "load lean").
      Cold-start letter becomes its opening block; KICKOFF stays as the audit checklist it points to.
- [ ] Trim the entry to rules/gates/constraints only (move any architecture prose into the docs it belongs to).
- [ ] Tag CORE-memory docs vs ARCHIVAL in ARTIFACT_INDEX (a one-word tier per row).
- [ ] Audit "don't" rules → where possible, replace with a structural impossibility; delete the now-needless don't.
- [ ] Add "load lean / fetch by number" to the KICKOFF start sequence.

## INDEX LINE
`knowledge/operating_system.md | build, business-plan, process | PUBLIC | captured | THE bioniq OPERATING SYSTEM — how man (Mark) + machine (Claude) work; the most leveraged doc (improves EVERY session). Story: chat-to-chat handoffs failed by Chat 3 → Mark made GitHub the memory → validated in Chat 6 against the field. We independently built what Google/OpenAI/Letta/research converged on: git-as-memory (= goldmine; cf Letta Context Repositories, Git Context Controller arXiv 2508.00031) + an agent-instruction file (= cold-start/KICKOFF; the AGENTS.md open standard, Linux-Foundation, 20k+ repos). METHOD (keep): repo = one source; CONFIRM=AUDIT; numbered addressing; bank on GO as one full-repo zip + propagate every view; index vs meat. BANK SEQUENCE (Chat 7): confirm repo=goldmine (public, not the private app repo) → extract → commit → push → audit. 5 REFINEMENTS to roll in: (1) standardize entry as root AGENTS.md (auto-loaded by any tool); (2) LEANER not longer instruction files (instruction-following drops as count rises; hold only what agent can't discover); (3) beware Pink Elephant — prefer making bad paths structurally impossible over forbidding them; (4) name memory tiers CORE vs ARCHIVAL; (5) context-cost discipline — load lean, fetch by number (>50% cheaper, no quality loss). ROLLOUT checklist in §4.`

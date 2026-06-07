*TAGS: build, business-plan, coaching | AUDIENCE: founder + every future Claude (the human-readable memory layer).*
*CREATED: 2026-06-07, Chat 6 | UPDATED: 2026-06-07, Chat 6 | STATUS: captured (idea GREENLIT; ONE scope question open — see below)*
*SUPERSEDES: — | RELATED: master_strategy_vision.md (THE primer), repo_as_memory_and_handoff.md, bionic_briefing_spec.md, coaching_philosophy.md*

# GOLD — THE LIVE VISION BOARD (so a vision never rots)
*Mark's nugget, Chat 6. The human-readable face of repo-as-memory: convos and essays distilled into a living paragraph, kept current, visible — so a vision is never forgotten.*

## ONE-LINE
A **live, auto-updated distillation** that condenses conversations and essays into a short paragraph
(or a few), displayed for all to see — so ideas don't get banked-and-forgotten. It is the human-legible
twin of what the repo already is for Claude: durable, current, never-lost memory.

## THE INSIGHT BEHIND IT (why this is the thing Mark's been chasing)
The repo is **Claude's long-term memory** (repo_as_memory_and_handoff.md): a durable, audited store that
lets a fresh Claude reason in continuity with prior Claudes instead of starting cold. The Vision Board is
the **human-readable display surface** over that same memory — the short-term/long-term memory made
visible to people, not just machines. Same problem ("we never forget the vision again"), two faces: the
repo for Claude, the board for humans.

## FEASIBILITY (PHD verdict: GO)
- It's a **summarization VIEW over a source of truth** — Claude reads the knowledge docs + living log and
  emits a current paragraph. Cheap (one generation, broadcast — same margin logic as the Briefing).
- Directly attacks the exact problem Mark named: banked-but-forgotten visions / loss of continuity.

## THE GUARDRAILS (so it informs instead of drifting)
- **Generated FROM the source of truth, never from a model's memory.** The board distills the actual
  repo/docs (and is regenerated as they change). It is a VIEW, not a new source — the primer
  (master_strategy_vision.md) stays canonical, exactly as the ARTIFACT_INDEX one-liners are views of the
  docs. No hallucinated vision.
- **Mark's words, not Claude's invention.** Distill what Mark actually said; quote or attribute, don't
  put words in his mouth (the PHD rule, made into a feature constraint).

## THE ONE OPEN SCOPE QUESTION (do not guess — Mark decides)
Who is "all," and what does the board summarize?
- **(A) Internal / founder + every future Claude:** a living one-paragraph distillation of THE PROJECT
  VISION, regenerated from the repo — the anti-vision-rot tool. (Strongest read of "we never forget my
  visions again.")
- **(B) Student-facing product feature:** each student gets a Vision Board — their goals/journey
  distilled into a paragraph they can see — tying into the dossier + the "your coach remembers your
  journey" memory-moment flywheel.
- **(C) Both** — start internal (A), generalize the same engine into the student feature (B) later.
Captured as open so it isn't silently pinned. Leaning C pending Mark's call.

## INDEX LINE
`knowledge/live_vision_board_spec.md | build, business-plan, coaching | PUBLIC | captured | LIVE VISION BOARD: an auto-updated distillation of convos/essays into a living paragraph, visible to all — the human-readable twin of repo-as-memory (repo = Claude's memory; board = the same memory shown to people), so a vision never rots. Feasible (a summarization VIEW over the repo source-of-truth; cheap, broadcast). Guardrails: generated FROM the repo not model memory (it's a view, primer stays canonical); distill Mark's actual words. OPEN: scope = internal vision distillation (A) / student-facing feature (B) / both (C, leaning) — Mark decides.`

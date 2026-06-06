# GOLD — MASTER JOURNEY FLOW (the coordinate system)
*TAGS: business-plan, build, coaching | AUDIENCE: founder + every future Claude (orient here first).*
*CREATED: 2026-06-06, Chat 4 | UPDATED: 2026-06-06, Chat 4 | STATUS: captured*
*SUPERSEDES: — | RELATED: strat_zone_taxonomy.md, brand_funnel_architecture (pending), repo_as_memory_and_handoff.md*

---

## WHAT THIS IS
The one-page master plan: how a stranger becomes a paying, coached student. This is the **coordinate
system** — every future Claude orients here, then gets assigned a box (a section) to detail. The
handoff becomes: minutes + repo + "your task is box X on the master flow."

## THE PAIRING RULE (locked this session)
Every flow — master and children — ships as a **matched pair**: the rendered diagram AND this Mermaid
source, same version, same commit. Never one without the other. Human sees the picture, machine reads
the source, neither drifts from the other. "Less dropped visions."

## LOCKS BAKED INTO THIS MAP (do not re-litigate)
- **No named entity.** The coaching voice IS the platform — the code/data that *sees you* (present:
  your trades, your patterns), not a mystic that predicts. No name, no character, no avatar. "Oracle"
  is dead (it crept back via Finn's wireframes + a Claude slip — kill on sight).
- **The Lab = a scientist's bench, not a trading pit.** Try one thing, test, adjust, retry. NOT a
  live-trading hype room. ("Live trading" = at most a paid-students-only Discord channel, never
  YT-free, an if-it-happens not a pillar.)
- **The course plays two roles, same asset:** the *hook* that gets them in the door AND the graceful
  "not yet" for the not-ready (90% off, 48h). To a noob it's the destination (nurture); to the hot ICP
  it's a while-you-wait courtesy offered IN PARALLEL — never a required detour that cools the lead.
- **ICP = struggling-but-CAPABLE traders whose problem is psychology, not knowledge.** Enters too
  early/late, moves stops, takes profit early, over-leverages. "Can learn a strat in a day, can't
  trade it — that's the coaching." NOT raw noobs (routed to nurture), NOT trolls (filtered at the door).
- **Entry itself is the filter + the demonstration.** The foyer quality IS the proof of the house.
  Anti-guru / "opposite-day": make the foyer so good and the Lab so visibly real that the candidate
  chases you. Earned standard, not manufactured scarcity.
- **Now/later sequencing is honest:** Mark closes & coaches 1:1 (Zoom) NOW — has the time, no clients
  yet, and LEARNS onboarding by living it. Records onboarding snippets over time → future
  self-onboarding. Journal-alone is NOT a product; the coaching wrapper is.

## THE THREE FORKS (open decisions, marked so they're not hidden assumptions)
1. **Mark-is-the-product → system-is-the-product.** Today Mark coaches; the engine assumes the system
   eventually carries it. WHEN/HOW does coaching de-personalize without losing trust? Biggest
   strategic question in the architecture.
2. **The funnel must REMEMBER.** "We already know you" requires foyer behavior (queries, binges,
   lingering) → a per-candidate dossier → the coaching brain. One shared memory, funnel↔coaching.
   Likely a BUILD not a buy (Whiting's TEDI summarizes socials+expenses; it does NOT build this).
3. **Live-trading Discord:** if/when, paid-only.

## THE FLOW (Mermaid source — paired with the rendered diagram)
```mermaid
flowchart TD
    H[Hook<br/>wide-net ad + course bait]:::funnel
    D[Foyer door<br/>identity + card · troll filter]:::funnel
    F[The foyer · almost-free<br/>qualify · demo · seduce]:::funnel
    S{Behavioral sort<br/>how they move = the signal}:::gate
    N[Nurture loop<br/>'not yet' + 90% off course<br/>↻ deferred pipeline]:::defer
    C[Sales cycle · ICP<br/>contact → call → Zoom → close]:::prog
    P[Preset platform<br/>auto-built from profile]:::prog
    L[The Lab<br/>journal daily · test · adjust]:::prog
    W[Weekly coaching<br/>Mark live now → AI later]:::prog
    R[Forward plan]:::prog

    H --> D --> F --> S
    S -->|not ready| N
    S -->|ICP| C
    C --> P --> L --> W --> R
    R -->|weekly loop| L

    classDef funnel fill:#F1EFE8,stroke:#5F5E5A,color:#2C2C2A;
    classDef gate   fill:#FAEEDA,stroke:#854F0B,color:#412402;
    classDef defer  fill:#FAECE7,stroke:#993C1D,color:#4A1B0C;
    classDef prog   fill:#E1F5EE,stroke:#0F6E56,color:#04342C;
```

## CHILD FLOWS TO BUILD (each = a box above, its own matched pair)
- foyer + the AI drip/qualify (the ambient interview — behavior IS the interview)
- the behavioral sort: the three buckets (noob / guidable / ICP) and what signal sorts them
- the funnel-memory pipeline (Fork 2) — how behavior becomes the profile/calling-card
- the sales cycle incl. the fit-filter (now = Mark on the call)
- the Lab: journal → tag → the coaching drawdown loop
- the now→later automation overlay (Fork 1) — how Mark hands off to the system over time
- **ARCHITECTURE flow (separate, next):** the technical/system architecture as its own diagram, not
  the journey — Mark explicitly wants to see this on its own.

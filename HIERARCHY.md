# GOLDMINE HIERARCHY v2 — domains for humans, EXPOSURE for the guardrail
*Read with METADATA_SCHEMA.md and MAINTENANCE_AND_BACKUP.md. This supersedes the flat folder list in
README §2. Finn's 7-domain idea is good for browsing; this adds the two things it was missing —
exposure control and live/locked/dead status — so nothing private leaks and nothing dead misleads.*

---

## THE THREE LENSES (every artifact answers all three)
1. **DOMAIN** — what it's about (the folder it lives in). For humans browsing.
2. **EXPOSURE** — can it be public? Encoded by WHICH top-level tree it's in (below). The guardrail.
3. **STATUS** — live / locked / superseded / pending. Carried in the metadata block + index line.
Topic alone (Finn's scheme) only answers #1. You need all three or private IP leaks and dead files mislead.

## TOP LEVEL = EXPOSURE (this is the safety boundary, not negotiable)
```
bionicbutterfly/
├── PUBLIC/          ← Claude may PULL this via raw URL. Nothing secret, ever.
├── PRIVATE/         ← Mark only. NEVER pushed to the public repo. Paid IP, locked-but-kept,
│                       secrets-adjacent. Lives in the Vault / a private repo, not the public one.
└── _control/        ← the operating system of the goldmine (public-safe meta-docs)
```
RULE: a file's exposure decides its tree FIRST, its domain folder SECOND. When unsure → PRIVATE.

## INSIDE PUBLIC/ — domains (Finn's idea, kept), each file carrying STATUS in metadata
```
PUBLIC/
├── 01-brand/            brand guidelines, style spine, logos, UI library
├── 02-education/        curriculum TOC, learning model, chapters, chart legend, print templates
├── 03-marketing/        landing narrative, ICP, hero images, thumbnails, merch  (Finn's zip lands here)
├── 04-engineering/      the dev goldmine: /knowledge /data(/verified,/unverified) /charts /build
├── 05-business/         trading-as-business, ATM model, roadmap
└── 06-infrastructure/   master-infra "bible", architecture map, user-flows, wireframes, feature matrix
```

## INSIDE PRIVATE/ — kept, never public (Mark's call, locked)
```
PRIVATE/
├── ip-paid/             Finn's character work you PAID for but are NOT using: Matrix framework,
│                          Morphosis, the-Oracle, agent-guru, character-locks, *-voice-lock.mp3.
│                          STATUS: locked-out (kept as owned IP; brand lock = NOT in product).
├── secrets-adjacent/    anything that drifts near keys/creds (should mostly not exist as files)
└── raw-media/           heavy binaries (voice mp3, lesson mp4) — keep offsite/LFS, not in the pulled repo
```
WHY this matters: your kickoff LOCKS "no Oracle character / no Morphosis / no Matrix / no caterpillar
arc — voice is the unnamed 'voice from the data'." Finn's character & voice files contradict that
lock. They're not deleted (you paid for them) — they're quarantined in PRIVATE/ip-paid with
STATUS: locked-out, so no future Claude ever treats them as live and starts building the arc you killed.

## _control/ — the goldmine's operating system (public-safe)
```
_control/
├── README.md                  orientation + access truth + handoff branches
├── HANDOFF.md                 the skinny "minutes" handoff
├── ARTIFACT_INDEX.md          the map (now: path | tags | exposure | status | one-liner)
├── METADATA_SCHEMA.md         the standard block + field-extension rule
├── MAINTENANCE_AND_BACKUP.md  the law (per-session upkeep + dated snapshots)
└── HIERARCHY.md               this file
```

## BINARIES RULE (Finn's mp3/mp4, 130-file haul)
GitHub caps files ~100MB and bloats on big binaries a Claude must pull. So: **text/docs/images →
PUBLIC repo; heavy audio/video → PRIVATE/raw-media (Vault or Git LFS), referenced by an index line,
not stored raw in the pulled repo.** Claude reads the *reference*, asks Mark for the media if needed.

## INDEX LINE v2 (carries exposure now)
`<tree>/<domain>/<file> | <tags> | <PUBLIC|PRIVATE> | <status> | <one-liner>`

## MIGRATING FINN'S 130 FILES (the rule, so any Claude can do it)
For each incoming file, in order:
1. **Exposure first:** does it touch the locked-out brand (Matrix/Morphosis/Oracle/character/voice)
   or paid-private IP? → PRIVATE/ip-paid, STATUS locked-out. Secret-adjacent? → PRIVATE. Else PUBLIC.
2. **Domain second:** drop into the matching PUBLIC/0x-domain folder.
3. **Binary?** heavy media → PRIVATE/raw-media + an index reference (don't inline in the public repo).
4. **Metadata:** add the block (docs) or a full index line (non-text), with exposure + status.
5. **Snapshot:** after the batch, cut a dated snapshot (the law).
Never bulk-dump 130 files into PUBLIC and sort later — exposure is decided per file, on the way in.

INDEX ENTRY: _control/HIERARCHY.md | build, support | built | The v2 repo structure — exposure as top-level guardrail (PUBLIC/PRIVATE/_control), Finn's domains kept inside PUBLIC, locked-out paid IP quarantined in PRIVATE/ip-paid, heavy media offsite. Supersedes README §2's flat list.

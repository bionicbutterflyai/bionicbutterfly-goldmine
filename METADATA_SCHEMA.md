# METADATA SCHEMA — the standard block every artifact carries
*Read this with MAINTENANCE_AND_BACKUP.md. Consistent metadata is how the index stays trustworthy and
how a new Claude knows what each file is WITHOUT opening all of them. Don't invent ad-hoc fields —
extend the schema here, then use it.*

---

## 1. THE BLOCK — goes at the TOP of every knowledge/doc artifact (markdown)
```
*TAGS: <comma list from the controlled vocab> | AUDIENCE: <who/what retrieves this>*
*CREATED: <YYYY-MM-DD, Chat N> | UPDATED: <YYYY-MM-DD, Chat N> | STATUS: <captured | built | pending | superseded>*
*SUPERSEDES: <file or "—"> | RELATED: <files, comma list or "—">*
# <TITLE>
```
- **TAGS** — controlled vocab ONLY: `coaching, marketing, build, business-plan, legal, support`.
  Tags scope retrieval (per tagging_strategy.md): `legal`/`business-plan` never reach support-Claude.
- **AUDIENCE** — who/what reads it (founder, build, the Oracle's grader, support, etc.).
- **CREATED / UPDATED** — date + chat number. UPDATED bumps every time the file changes.
- **STATUS** — `captured` (written, not built) · `built` (in product) · `pending` (decision/build open) · `superseded`.
- **SUPERSEDES / RELATED** — lineage links so a Claude can follow the thread without guessing.

## 2. THE INDEX LINE — one per artifact in ARTIFACT_INDEX.md
```
<path/filename> | <tags> | <STATUS> | <one-line description>
```
Always carry STATUS into the index too, so a Claude scanning the map sees what's live vs pending vs
superseded without opening files.

## 3. NON-TEXT ARTIFACTS (charts/images/data/builders — can't hold a markdown block)
Their metadata lives in the **index line only** (path | tags | status | one-liner), PLUS:
- **data files:** record in the index — date range, gaps, gate status (verified/unverified), and the
  timestamp convention confirmed (e.g., "close-stamp UTC, TV=−4h−1min"). See data_provenance nugget.
- **charts/builders:** note what they supersede (e.g., v6 supersedes pre-pin) in the index one-liner.

## 4. RULES FOR CLAUDES
- **R1 — every new artifact gets the block (or, if non-text, a full index line).** No exceptions.
- **R2 — editing a file bumps UPDATED and re-checks STATUS.** A built thing that you change may need
  re-verification; a captured thing you build flips `captured → built`.
- **R3 — new metadata FIELD needed?** Don't sprinkle it ad-hoc. ADD it to this schema (§1), note it
  in the handoff (so the next Claude expects it), THEN use it everywhere. One source of truth for shape.
- **R4 — superseding, don't delete.** Move the old file to `/reference`, set its STATUS: superseded,
  and point the new file's SUPERSEDES at it. History is never destroyed (mirrors the data gate ethos).
- **R5 — the handoff carries this schema's shape** (HANDOFF.md links here) so a waking Claude reads/writes metadata consistently from minute one.

## 5. WHY
Without a fixed schema, every Claude invents its own front-matter, the index drifts, and "what is this
file / is it current / what replaced it" becomes a re-read-everything chore — the exact cost
repo-as-memory exists to kill. The block is cheap; the drift is expensive.
```
INDEX ENTRY: metadata_schema.md | build, support | built | The standard metadata block (tags/audience/created/updated/status/supersedes/related) every artifact carries + index-line format + rules for extending fields. Read with the maintenance law.
```

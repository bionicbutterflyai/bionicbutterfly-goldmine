*TAGS: build, business-plan | AUDIENCE: founder + build + whoever wires the coaching voice/playback.*

# GOLD ARTIFACT — VOICE / TTS DECISION (don't hand the profits to ElevenLabs)
*Captured June 5 2026 (Chat 4); **UPDATED June 6 2026 (Chat 5)** — the default FLIPPED from
"Web Speech API" to "pre-render premium voice." Reason below. Web Speech is now the fallback, not the face.*

## THE FLIP — why Chat-4's "Web Speech as default" was downgraded
Web Speech API is free and zero-per-student, BUT it is device-dependent, uneven, and often robotic
(Chat-4's own catch). For a premium coaching brand that's a false economy: **"if it's choppy and robotic
we lose worse than money — we lose credibility"** (Mark). A robotic first impression poisons trust before
the coaching ever lands. So we stop using free-but-robotic as the brand voice.

## ONE-LINE (the decision)
Default the **brand voice** to **PRE-RENDERED premium/neural audio** for all *fixed, authored* content;
use a **cheap managed or self-hosted TTS for the *live* Q&A turns only**; keep **Web Speech API as a
last-resort fallback** (with the Chat-4 technical handling). One consistent house voice across both.

## THE SPLIT (this is the actual architecture)
- **FIXED / AUTHORED content** — lessons, onboarding, the super-sauce level-narration scripts:
  **pre-render ONCE** with a premium neural voice. Cost = a one-time render, then **$0 per student
  forever**, a perfectly consistent brand voice, and **exact word/sentence timestamps** to drive the
  highlight-and-fade. (Batch/pre-render is cheap; pay once, serve infinitely.)
- **LIVE / DYNAMIC content** — real-time Q&A and personalized coaching replies: **cheap managed TTS**
  (e.g. Fish Audio ~$15/1M chars) or **self-hosted open-source** (Kokoro / Chatterbox, ~free compute).
  Pay-per-use, but only on the genuinely live turns — a fraction of total audio.
- **FALLBACK** — Web Speech API only if a managed voice is offline/unavailable. Keep the Chat-4 catches
  for THIS path only: chunk to ~200 chars + queue (the ~15s cutoff), wait for `voiceschanged`, recommend
  Chrome.

## PRE-RENDER ≠ "A DATABASE OF EVERYTHING" (NOT a chatbot — answers Mark's worry directly)
Pre-rendering covers ONLY authored fixed content (scripts that don't change). **Live coaching stays fully
dynamic** — Claude generates the response in the moment, then it's voiced live. We are NOT pre-recording
every possible answer and turning the coach into a soundboard. Fixed lessons = narrated once; living
coaching = generated and voiced on the fly. That distinction is what keeps it a *coach*, not a chatbot.

## ELEVENLABS OWNERSHIP RULE (verified this session)
- On **paid** plans you **own the generated audio** commercially and perpetually.
- You **may use one voice for BOTH pre-render and live Q&A** — *while on their platform.*
- You **cannot lift their proprietary voice MODEL off-platform** to self-host it.
- Therefore: if you want **one house voice that can run anywhere** (self-hosted/cheap engines included),
  **clone it from a source Mark controls/has rights to**, not from an ElevenLabs stock voice. Result =
  one consistent house voice across pre-render + live, owned and portable.

## COST LANDSCAPE (2026, verified)
ElevenLabs ~$165/1M chars (premium, owns-audio, on-platform) · Fish Audio ~$15/1M (managed, ~10x cheaper)
· Kokoro / Chatterbox (open-source, self-host, ~free compute). Pre-rendering fixed content is a one-time
spend on any of these; the only recurring TTS cost is live Q&A.

## TIE-INS
- **Super-sauce:** pre-rendered audio yields exact timestamps → drives highlight-and-fade + chart morph
  *more* reliably than Web Speech's `onboundary`. The flip IMPROVES the signature mechanic.
- **Credit model (credit_value_pricing_model.md):** pre-rendered fixed content = $0 marginal, so it never
  burns student credits; only live-Q&A TTS does, and that's cheap. Folds into credit COGS cleanly.

## INDEX ENTRY
`knowledge/voice_tts_decision.md | build, business-plan | PUBLIC | captured | UPDATED Chat 5: default FLIPPED to PRE-RENDER premium/neural voice for fixed content (lessons/onboarding/super-sauce narration) = $0/student after one-time render + exact timestamps for highlight-sync; cheap managed/self-host TTS (Fish ~$15/1M, or Kokoro/Chatterbox free) for LIVE Q&A only; Web Speech API demoted to fallback (robotic = credibility risk, per Mark). Pre-render ≠ database-of-everything (live coaching stays dynamic, NOT a chatbot). ElevenLabs: paid = own audio, one voice for both, but model is on-platform only → clone a Mark-controlled voice for run-anywhere.`

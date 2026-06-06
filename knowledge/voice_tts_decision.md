*TAGS: build, business-plan | AUDIENCE: founder + build + whoever wires the coaching voice/playback.*

# GOLD ARTIFACT — VOICE / TTS DECISION (don't hand the profits to ElevenLabs)
*Captured June 5 2026, Chat 4. Verified against current Web Speech API browser support.*

## ONE-LINE
Ship **browser-native Web Speech API (`speechSynthesis`)** as the **free default** voice — it runs on
the student's device, no API key, no per-student cost, anywhere in the world. Keep paid TTS
(ElevenLabs / Qwen / OpenAI) as an **optional premium** later, not a launch dependency.

## WHY (the trap avoided)
Qwen / OpenAI / ElevenLabs TTS are all **server-side, pay-per-use** — cheaper than each other but the
same model: you pay AI per student. At student scale that bleeds margin. Web Speech API moves the
synthesis onto the student's browser (Chrome/Edge/Safari), so **cost to us = $0** regardless of where
Suzy is. Text never leaves her device (privacy bonus). No browser extension needed — Mark's "voice
through a Chrome extension" idea works but is overcomplicated; the plain API is one button.

## THE REAL CATCHES (design around these from day one)
1. **Voice quality is device-dependent and uneven.** Edge's voices sound notably more natural than
   Chrome's; some devices are robotic. So the brand's "unnamed voice from the data" will NOT be one
   consistent voice on the free tier — it's whatever the device has. **The cost of free is brand
   consistency, not dollars.** (This is the argument for offering paid premium voice later.)
2. **~200–250 char / ~15s cutoff (desktop Chrome):** a single utterance longer than that gets cut off
   mid-sentence. FIX: split narration into short utterances and **queue** them. Must be built in.
3. **Mobile is patchier:** Firefox-for-Android lacks synthesis; Android works via Chrome / Samsung
   Internet using the device's installed TTS engine. → **Recommend Chrome to students** (not arbitrary).
4. Wait for the `voiceschanged` event before reading `getVoices()` (Chrome populates async).

## BONUS — TTS DRIVES THE SUPER-SAUCE
`SpeechSynthesisUtterance` fires `onboundary` (word/sentence) events as it speaks. Those events can
**drive the highlight-and-fade and the chart morph in real time** — a level lights exactly as the
coach's voice names it. Free voice AND the narration-sync engine from one source. (Ties to
GOLD_strat_zone_taxonomy.md → display-rule extensions.)

## DECISION / PATH
- Launch: Web Speech API free default. Chunk text + queue; recommend Chrome; handle `voiceschanged`.
- Later (optional): premium signature voice via paid TTS for users who want the cinematic brand voice.
- Do NOT make a paid TTS a launch dependency.

## INDEX ENTRY (paste into GOLD_ARTIFACT_INDEX.md)
`GOLD_voice_tts_decision.md | build, business-plan | Ship free browser-native Web Speech API as default TTS (zero per-student cost); chunk text for the ~200-char cutoff, recommend Chrome; onboundary events can drive highlight-sync; paid TTS (ElevenLabs etc.) is optional premium later, not a launch dependency.`

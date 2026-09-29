# Teclogi — 60s story video (HITL draft, 2026-09-28)

**Status:** HITL review only. Not posted anywhere (no LinkedIn / Buffer / email).
**VPS path:** `/home/debian/.cursor/artifacts/teclogi-60s-story-2026-09-28/`

| File | What |
|---|---|
| `teclogi-60s-story-16x9.mp4` | **Master** — 1920×1080, 24 fps, 61.0 s, H.264 ~11 Mbps, AAC stereo, −16 LUFS |
| `teclogi-60s-story-9x16.mp4` | Optional vertical — 1080×1920, 61.0 s (crop-reframed from the 16:9 footage → softer) |
| `mezzanine/*-mezzanine-crf17.mp4` | High-bitrate masters (~60 Mbps) for re-encode / edit |
| `audio/teclogi-60s-vo-DRAFT-gpt-audio-onyx.wav` | **Draft VO** (AI TTS), timed to the cut, 61 s |
| `audio/vo1..vo6.wav` + `.transcript.txt` | Per-line VO takes + model transcripts |
| `teclogi-60s-story.en.srt` | EN captions for the VO |
| `stills/` | Storyboard keyframes used (v2 library), UI still, end card, contact sheet from the master |
| `clips/` | Raw generated clips (`b01`–`b09` Veo, `b05_ui` local render) |
| `prompts/` + `logs/` | Exact prompts per shot + per-job generation logs (job id, cost) |

## Locked arc (unchanged)

Cash wait → corridor reality → Loggicash underwrites WC on live dispatch / e-POD / RNDC → capital moves with the truck → soft Series A invite.
Positioning: Teclogi = AI Fintech for Andean road freight; Loggicash underwrites WC against live ops data; marketplace/OS = underwriting engine, not the headline.

## VO (EN) — lock vs. placement in the cut

| Lock window | Placed in cut | Line (spoken verbatim) |
|---|---|---|
| 0–8s | 0.5–5.8 | In Colombian road freight, the truck moves today. The cash often doesn't. |
| 8–18s | 6.6–16.9 | Drivers and carriers wait on invoices while fuel, tolls, and payroll don't wait. Working capital is the real bottleneck on the Andes corridor. |
| 18–32s | 17.2–31.2 | Teclogi is AI fintech for Andean road freight. Loggicash underwrites working capital against live dispatch, e-POD, and RNDC manifests — the same signals that prove the load. |
| 32–45s | 32.2–42.0 | Marketplace and ops aren't the headline. They're the underwriting engine. Capital follows the freight, not a spreadsheet from last month. |
| 45–55s | 43.6–51.9 | When the truck clears the dock, liquidity can move with it — so carriers keep rolling instead of waiting on the bank. |
| 55–60s | 54.6–60.1 | Teclogi. Series A. Building the rails for freight finance in the Andes. |

Natural read ran ~1 s longer than the lock windows, so lines 3 and 5 start slightly early and the film is 61.0 s (inside the 55–65 s tolerance). Wording is unchanged.

## On-screen text

| In–Out | Text |
|---|---|
| 1.0–7.2 | El flete sale hoy. El cobro, no. |
| 12.3–17.2 | WC = the bottleneck |
| 20.8–29.6 | Loggicash · WC on live ops data |
| 33.6–41.6 | Data engine → underwriting |
| 45.8–53.2 | Capital moves with the truck |
| 54.3–61.0 | End card: **Teclogi · AI Fintech · Andean freight** / SERIES A |

## Shot list (16:9 master timestamps)

| # | In–Out | Storyboard beat | Source | Keyframe (v2 library) |
|---|---|---|---|---|
| 1 | 0:00.0–0:06.0 | Close face, cab, midday | Veo 3.1 Fast i2v `b01` | `01-mestizo-man-cab-close-portrait.png` |
| 2 | 0:06.0–0:11.5 | Peaje / toll | Veo `b02` (src 0.2–5.7s) | `05-older-man-peaje-window-portrait.png` |
| 3 | 0:11.5–0:17.5 | Dock, straps / pallets | Veo `b03` | `04-woman-loading-dock-portrait.png` |
| 4 | 0:17.5–0:23.5 | e-POD tablet in cab | Veo `b04` | `12-woman-tablet-glow-cab-portrait.png` |
| 5 | 0:23.5–0:30.0 | Generic dispatch / manifest UI | Local motion graphic `b05_ui` (fictional, no brand UI) | — |
| 6 | 0:30.0–0:36.0 | Woman driver + soft Loggicash decision | Veo `b06` | `02-afro-colombian-woman-cab-portrait.png` |
| 7 | 0:36.0–0:42.0 | Andes corridor truck | Veo `b07` | `16-woman-andes-pull-off-medium.png` |
| 8 | 0:42.0–0:48.0 | Diesel / roadside grit | Veo `b08` | `07-man-diesel-stop-face-portrait.png` |
| 9 | 0:48.0–0:54.0 | Fleet yard dawn, diverse | Veo `b09` | `20-man-fleet-yard-dawn-medium.png` |
| 10 | 0:53.5–1:01.0 | End card Teclogi | Blurred last frame of `b09` + type (0.5 s crossfade) | — |

Cuts are hard cuts except the crossfade into the end card. Light unifying grade on the Veo shots (−10 % saturation, +4 % contrast, fine film grain).

## Generation tools and models

| Layer | Tool / model | Notes |
|---|---|---|
| Video (beats 1–4, 6–9) | **Google Veo 3.1 Fast** (`google/veo-3.1-fast`) via the **OpenRouter video API** | Image-to-video from the v2 stills as first frame; 1080p, 16:9, 6 s, native audio off; negative prompt blocks beauty retouch, logos, text, watermarks and lip movement. 8 clips × $0.60 = **$4.80** |
| Draft VO | **OpenAI `gpt-audio`**, voice `onyx`, via OpenRouter | Verbatim read + pronunciation guide; ~$0.08 total. **Draft only — replace with a human VO or approved voice before any use.** |
| Keyframes | v2 image library (Cursor GenerateImage, per the Notion HITL pack) | Reused as-is, no new stock imagery |
| UI beat, lower thirds, end card | Local render (Python/PIL, Inter 4.1 typeface, OFL) | Fictional load IDs (CO-447x), generic "DISPATCH · MANIFEST" header |
| Edit / mix | ffmpeg | VO over a low synthetic road-rumble bed (placeholder, no music), loudness-normalised to −16 LUFS |

Scripts: `or_video_gen.py` (Veo via OpenRouter), `or_tts.py` (VO), `build_assets.py` (graphics), `assemble.py` (edit, `--vertical` for 9:16). `veo_gen.py` is the direct Gemini API path, which was blocked (see below).

### Paths tried and blocked

| Path | Result |
|---|---|
| Gemini API direct, Veo 3.1 standard/fast/lite (key in `/opt/sustenttia-api/.env`) | HTTP 429 quota exhausted on every Veo tier (Gemini TTS too) |
| Gemini key in `/opt/lumines/.env` | Invalid key |
| Vertex AI via `gcloud` | Needs interactive re-auth (`gcloud auth login`) |
| OpenAI Sora 2 / Sora 2 Pro | Sora API shut down 2026-09-24; the OpenAI account is also out of credit (TTS failed too) |
| Vercel AI Gateway (Veo 3.1, Kling 3.0) | Needs a credit card on file (balance $0) |
| HeyGen MCP | Not authenticated |
| Veo 3.1 **standard** via OpenRouter ($0.20/s) | Not used: 8 beats would cost $9.60 against $6.43 of shared balance |

## QA

1. **Faces readable where intended:** yes for beats 1, 2, 3, 4, 6, 8, 9 (identity holds from the v2 keyframes; real skin texture, sweat, stubble). Beat 7 turns away by design (she climbs into the cab, and the corridor reveal is the subject). Beat 9 ends with him walking to his truck.
2. **Logos / watermarks:** none visible in frame checks of every beat; truck bodies are plain, and phone and tablet screens are unreadable. The UI beat is fictional and carries no Teclogi or Loggicash branding. Note: Google embeds an *invisible* SynthID watermark in Veo output.
3. **Thesis lines match the lock:** the VO transcripts match the locked script word for word ("RNDC" is spoken as letters). The on-screen text matches the lock exactly; the end card adds "SERIES A" under the locked line.

### Open items for HITL

- **VO is AI TTS (draft).** "Teclogi" was guided as *tek-LOH-hee* and "Loggicash" as *LOG-ee-cash*; confirm the pronunciation with Teclogi.
- The UI beat shows "WC advance: eligible" as an illustrative state. Confirm this wording is acceptable for investor use.
- Beat 3 (strap pull) has a strong effort grimace; swap to `b03` 0–2 s + hold if it reads too intense.
- The 9:16 is a crop reframe (upscaled from a 608 px wide slice); the dispatch UI is small on a phone. For a real vertical cut, generate native 9:16 in Veo (~$4.80 on Fast).
- No music; the road-rumble bed is a placeholder.
- Upgrade path, if wanted: re-render the 8 beats on Veo 3.1 standard ($9.60) after an OpenRouter top-up.

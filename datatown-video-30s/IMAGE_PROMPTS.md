# Image prompts — Data Town 30s stills

All generated stills are **16:9 / 1280×720**. References: `stills/01-origen.png`, `stills/02-town.png`.

## Palette lock (prepend to every prompt)

```
PALETTE LOCK (strict): Deep Blue #0C498A, Light Cyan #B2EEFA, Light Green #9DC384,
Forest Green #669348, Sky Blue #69B5FA only. Bright daylight, high-key, no crushed blacks.
FORBIDDEN: black, near-black, dark navy shadows, red, purple, orange, magenta.
STYLE: Optimistic editorial photography matching CleantechHUB stills 01–02,
Open Sans corporate-clean vibe, nature + people, photoreal, 16:9 landscape.
```

## 01 Origen — not generated

Copied from workshop uploads (`01-origen_0b7c.png`). Startups + plant managers hand cyan data cubes into a shared stream.

## 02 Data Town — not generated

Copied from workshop uploads (`02-town_35b8.png`). Plaza + tent “Data Town Bucaramanga”.

## 03 Data lake — used as-is

**File:** `stills/03-lake.png`  
**Refs:** 01, 02

```
Photorealistic 16:9 editorial photograph matching the attached CleantechHUB stills:
sunny optimistic corporate-nature style, diverse Latin American professionals, no cinematic darkness.

SCENE: A group of 5-6 smiling professionals walk along a pale wooden boardwalk beside a
large luminous lake. The lake water is bright sky-blue and light-cyan (#69B5FA, #B2EEFA),
glowing from within, never dark navy or black. Translucent white-cyan holographic cubes
(same glowing lattice cubes as the reference) float just above the water in a converging
light-path of cyan network lines flowing toward the far shore. Green Andean hills and a
clean industrial plant faintly in the distance under a clear bright sky.

PEOPLE: Mixed gender, ages 30-55, Latin American appearance. Business-casual: deep-blue
(#0C498A) blazers, light mint/green shirts (#9DC384), white trousers, white sneakers.
One person in a forest-green (#669348) polo. Warm smiles, walking and talking, looking
at the luminous lake.

BRAND: Small CleantechHUB logo (cyan swirl mark + wordmark in deep blue) on a simple
white wayfinding sign by the path.

[PALETTE LOCK]

No text besides the logo. No drones, no night, no rain.
```

## 04 Lake house — used as-is

**File:** `stills/04-lakehouse.png`  
**Refs:** 01, 02

```
Photorealistic 16:9 editorial photograph matching the attached CleantechHUB stills:
sunny optimistic corporate-nature style, diverse Latin American professionals.

SCENE: A modern glass-and-light-wood lake house sits on the shore of a luminous
cyan-blue lake. Architecture is airy and trusted: floor-to-ceiling clear glass,
pale honey wood (never dark walnut or black frames), white structural columns,
a wide open doorway. Soft cyan reflections on the water. Forest-green hills and
palms behind. A pale wooden walkway leads to the entrance.

PEOPLE: 4-5 smiling professionals walking toward and entering the house. One person
holds the glass door open in a welcoming gesture. Deep-blue blazers, light-green
and white shirts, forest-green accents, white sneakers. Latin American, mixed
gender, ages 30-55.

DETAILS: A few translucent white-cyan holographic data cubes float gently near the
shoreline. Small white plaque by the door with CleantechHUB cyan-swirl logo and
the words "lake house" in clean sans-serif deep blue. Bright midday sun, blue sky
with a few white clouds.

[PALETTE LOCK]

No night, no rain, no luxury-dark architecture.
```

## 05 Data Lab — take 2 (white frame)

**File:** `stills/05-lab.png`  
**Refs:** 01 + take-1 lab (black bezel rejected)

Take 1 had a black TV bezel (palette violation). Take 2 prompt:

```
Photorealistic 16:9 bright Data Lab, same optimistic CleantechHUB editorial style
as the attached images.

Keep the successful composition: facilitator in deep-blue shirt with cyan swirl
logo pointing at a wall display; 4 colleagues around a white table; glowing
translucent cyan-white holographic cubes connected by light paths on the table;
Andean hills through large windows; CleantechHUB wordmark on the wall.

CRITICAL FIX: The display is a frameless or white/light-cyan framed LED wall.
NO black bezel, NO black rectangle, NO dark frame. Dashboard background is white
or light cyan #B2EEFA with maps and bar charts only in Deep Blue #0C498A,
Sky Blue #69B5FA, Forest Green #669348, Light Green #9DC384. Cubes visually
feeding into the charts.

Phones and notebooks on the table are white or light cyan, never black.

[PALETTE LOCK]

No night lab, no sci-fi darkness.
```

## 06 Climate Data Week — generate blank wall + type overlay

**File:** `stills/06-climate-week.png`

The image model twice wrote **Inspirera. Acttúa. Transforma.** and **Climate Data Weeket**. Do not ship those frames.

**Step A — plate (logo only):**

```
Exact same photorealistic 16:9 outdoor plaza scene as the attached tent / gathering
stills: palms, Andean hills, checkered pale-blue plaza, white CleantechHUB counter,
diverse Latin American professionals in deep-blue and mint jackets.

The solid Deep Blue #0C498A wall should show ONLY the cyan swirl CleantechHUB logo
and the single wordmark "CleantechHUB" in white. Leave a large empty deep-blue area
in the lower half of the wall. Do NOT write Inspira, Actúa, Transforma, Climate,
Data, Week, or any other slogan.

Keep the light-green and light-cyan diagonal accent at the bottom-right of the wall.

[PALETTE LOCK]
```

**Step B — composite (Inter, not the image model):**

On the empty wall, centered, white:

1. `Inspira. Actúa. Transforma.` — Inter SemiBold 40px
2. 2px rule `#B2EEFA`
3. `Climate Data Week` — Inter Medium 30px

Spelling lock: **Inspira** (7 letters) · **Actúa** (one ú) · **Transforma** · **Climate Data Week** (three words). Never Inspirera, Acttúa, Weeket.

## Regeneration notes

- Always attach 01 + 02 as style refs.
- If type is plot-critical, generate a blank plate and set type in post (see 06).
- Reject any frame that introduces red, orange, purple, or a black UI chrome.

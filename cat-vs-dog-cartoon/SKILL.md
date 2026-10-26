---
name: cat-vs-dog-cartoon
description: Write and prepare "Cat vs Dog" — Bubble Tea News's syndicated domestic-sitcom gag cartoon starring an unnamed cat-and-dog household duo, format variable issue to issue (single panel most weeks, occasionally a short multi-panel beat when a gag needs the setup) — unlike The Boba Side, which stays single-panel every time. Unrelated to bubble tea by design, the way a real paper carries a licensed strip like Garfield or Get Fowl alongside its own local content. Art is hand-drawn on paper, photographed, and cleaned up digitally — a background-blur divide to flatten shadow/vignette, autocontrast, crop tight to the drawn content — rather than programmatically rendered; see Step 3 for the actual verified pipeline (Python/Pillow). Debuted Issue 10, taking that issue's cartoon-slot turn ahead of The Boba Side's own promised return. Use when assembling a Bubble Tea News issue that wants this cartoon slot, or when the user wants a new Cat vs Dog gag written up. This is a seed skill: sparse by design, built from one debut panel; expand with a running gag library and a settled panel-count convention as strips accumulate. Includes an artist-craft pass: artistic question, style pillars, name-before-draw panel plan, and a critique pass before print.
user-invocable: true
---

# Cat vs Dog (seed)

A working method for **Cat vs Dog**, *Bubble Tea News*'s syndicated
domestic-sitcom gag cartoon — an unnamed cat and dog sharing a household,
run the way a real community paper carries a licensed strip alongside its
own local content. Treat this as a starting checklist, not a rigid
template.

## Step 0 — Boundaries (do this before writing anything)

- **Original characters, not a franchise lookalike.** "Cat and dog
  flatmates" is a well-populated format (real published strips and shows
  cover near-identical ground). Keep this cat and this dog original —
  no names, character designs, or specific gags borrowed from an existing
  strip. Genre pastiche (the domestic odd-couple format, the deadpan
  animal-POV joke) is the target, not a retelling of somebody else's actual
  characters.
- **Format is genuinely variable, not sloppy.** Unlike The Boba Side
  (always exactly one panel) or Hayaku/Doki Doki Mon (always exactly four),
  Cat vs Dog's panel count is a per-gag decision — one panel when the joke
  lands in a single beat, two or three when it needs a setup/payoff. Don't
  default to multi-panel out of habit; most weeks a single panel (like the
  Issue 10 debut) is the right call.
- **Deadpan animal-POV is the comedic engine**, not slapstick — the joke
  usually comes from the cat and/or dog reacting to an ordinary human
  domestic moment (watching TV, a delivery, a chore) with total sincerity.

## Step 1 — The comedic engine

- **The premise device.** Stage an ordinary household moment — watching
  commercials, waiting by the door, reacting to a vacuum cleaner, a
  grocery delivery, a video call — from the cat and dog's own sincere
  point of view, playing the mismatch between the mundane trigger and
  their fully committed reaction completely straight.
- **The caption/dialogue is still doing real work.** A single line of
  dialogue from one or both animals (the Issue 10 debut used the dog's "I
  love commercials!") usually carries the punchline; keep it short and
  let the drawn expressions carry the rest.
- **Vary who's the straight man.** Some gags the cat is unbothered and the
  dog is delighted (or vice versa); don't let one animal always be the
  reactor and the other always the instigator — alternate it strip to
  strip so the pairing stays a genuine duo, not a fixed straight-man/
  goofball split.

## Step 2 — Composition

For each panel (however many the gag needs):

1. **Setting** — a plain domestic space (a couch, a kitchen counter, the
   front hallway); keep backgrounds simple and legible at print size.
2. **The human-world trigger** — whatever ordinary moment the gag is
   reacting to (a TV ad, a doorbell, a dropped grocery bag).
3. **Cat and dog's reaction** — sincere, not slapstick; exaggerated
   expression is fine, but play the animals' own logic completely straight.
4. **Caption/dialogue**, if any — short, ideally a single line.

## Step 3 — Art pipeline: hand-drawn photo, cleaned up digitally

Unlike the sibling cartoon skills' speculative programmatic-render
documentation (ImageMagick/SkiaSharp/GDI paths in `the-boba-side-cartoon`
and `hayaku-senkotsu-strip`), Cat vs Dog's actual, verified pipeline —
used for the Issue 10 debut — is: draw the panel by hand on paper,
photograph it on a phone, then clean the photo up digitally. No
image-generation model and no programmatic renderer are involved; the
art is a real drawing, digitally restored to print quality.

1. **Photograph the drawing** — even, front-on lighting where possible;
   phone-camera EXIF orientation and shadow gradients are corrected in the
   next step regardless, so a slightly uneven shot is recoverable.
2. **Flatten shadow/vignette** with a blurred-background divide (Python,
   Pillow): convert to greyscale, take a large-radius Gaussian blur of the
   image as a background-illumination estimate, divide the original by
   that blurred version and rescale — this cancels out uneven lighting and
   phone-shadow vignetting far better than a flat levels/contrast pass
   alone. A blur radius that's too small relative to line thickness haloes
   the linework; verified working at radius ≈180px on a ~2800px-wide
   source photo — scale proportionally to source resolution.

   ```python
   from PIL import Image, ImageOps, ImageFilter
   import numpy as np

   im = Image.open("panel-photo.png").convert("L")
   arr = np.array(im).astype(np.float32)
   bg = np.array(im.filter(ImageFilter.GaussianBlur(180))).astype(np.float32)
   bg[bg < 1] = 1
   flat = np.clip(arr / bg * 235.0, 0, 255).astype(np.uint8)
   result = ImageOps.autocontrast(Image.fromarray(flat, mode="L"), cutoff=0.5)
   ```
3. **Crop tight** to the drawn content — trim the surrounding paper/desk
   margin the photo inevitably includes. If the photo itself doesn't
   capture the full page (an edge genuinely cut off in frame), that's a
   photo problem, not something the cleanup step can recover — flag it and
   get a retake, or crop tight and accept the visible composition as final
   if a retake isn't available (confirmed acceptable for the Issue 10
   debut, where the source photo was already the only copy).
4. **No EXIF/orientation metadata carries through** re-saving via
   Pillow's `Image.fromarray` path — confirmed clean by inspecting
   `Image.getexif()` on the output — so there's no separate "strip EXIF"
   step needed beyond just re-encoding through numpy/Pillow this way.
5. Save as PNG, named `issues/cat-vs-dog-issueN-debut.png` for a debut or
   `issues/cat-vs-dog-issueN.png` thereafter, matching this library's
   existing `hayaku-issue9-debut.png` convention.

### Step 3b — Code-drawn fallback (no hand-drawn photo available)

When there's no photographed drawing for the issue, don't skip the slot.
Draw the panel as simple black-and-white SVG line art instead (white
background, thick border, round cartoon cat and dog with dot eyes, the
human-world trigger, one speech bubble, "Cat vs Dog" caption). Then
render it to PNG with headless Chrome (`google-chrome --headless=new
--no-sandbox --hide-scrollbars --window-size=1800,1260
--screenshot=issues/cat-vs-dog-issueN.png file://$PWD/issues/cat-vs-dog-issueN.svg`),
`rsvg-convert -w 1800`, or draw it directly with Pillow `ImageDraw`.
Keep the `.svg` next to the PNG, look at the PNG before embedding, and
note "code-drawn fallback, not hand-drawn" in the issue's no-print
instructions and the rotation log. First used for the Issue 22 test
build (smoke-alarm chirp gag).

## Artist craft (from bot artist skills)

Craft borrowed from the artist-mode, manga-studio and art-director skills — craft only, not their persona voices. Original characters only; no franchise characters. Step 0 boundaries still come first.

1. **Artistic question** — write one sentence this issue's strip answers (e.g. "what does losing look like when nobody admits it?"). If the gag doesn't answer it, fix the gag, not the question.
2. **Style pillars** — deadpan · domestic · readable. Keep line weight consistent (heavier outer contour, lighter interior detail), simple readable silhouettes, high-contrast black-and-white that survives newsprint. Don't: polished illustration, gradients that mud in print, more than one focal point per panel.
3. **Name before drawing** — 1–3 panels (single most weeks). Per panel: beat, framing (wide room / mid two-shot / close reaction), who acts, who reacts. Deadpan lives in the reactor's flat face, so name the reactor every panel. Keep balloons short (~25 words max), placed in reading order, never over a face.
4. **Render** — via the existing pipeline (Step 3 (hand-drawn photo + Pillow cleanup) or Step 3b code-drawn fallback). Art stays schematic or hand-drawn-photo, not polished illustration. GenerateImage is not required and never replaces Step 0 originality rules.
5. **Critique pass before print** — open the finished PNG and look at it before embedding: (a) what is actually visible, (b) does it match the name and artistic question, (c) one or two concrete fixes (e.g. "reactor's face too small at print size — enlarge 30%"). Separate observation from interpretation; never critique art you haven't opened.

Shared critique language with: the-boba-side-cartoon, hayaku-senkotsu-strip, doki-doki-mon-strip.

## Step 4 — Delivery

- Within a *Bubble Tea News* issue: shares the cartoon slot's biweekly-ish
  alternation with The Boba Side, Hayaku, and Doki Doki Mon — see the
  editor skill's Step 2c for current alternation order and whose turn is
  next. Don't repeat a premise strip to strip.
- Embed the finished PNG via `<img>` in the issue HTML, same
  `max-width/max-height` box the other cartoon slots use (170×145px as of
  Issue 9's standardization pass) so the fixed cartoon-slot footprint
  holds regardless of which strip runs that issue.
- Re-check the print page-count budget after embedding — verify the final
  PDF is still exactly 2 pages (`pdfinfo`/`pypdf` page-count check) before
  calling an issue done, same as every other cartoon slot.
- Byline convention: *"Cat vs Dog — a new syndicated gag cartoon, Bubble
  Tea News's cartoon slot, hand-drawn; panel count varies week to week."*

## On Linux

The Windows steps above (ImageMagick 7 `magick`, Inkscape, SkiaSharp,
GDI+, PowerShell, PSWriteHTML, Edge) stay valid on Windows. On a Linux
box use these equivalents:

- **DPI tagging:** Pillow, `Image.open(p).save(out, dpi=(300, 300))`. If
  ImageMagick is installed but there's no `magick` binary (IM6), use
  `convert in.png -units PixelsPerInch -density 300 out.png` and
  `identify -format "%x x %y units=%U" out.png`.
- **SVG to PNG:** `rsvg-convert -w 1800 in.svg -o out.png` (librsvg2-bin),
  or headless Chrome: `google-chrome --headless=new --no-sandbox
  --hide-scrollbars --window-size=1800,1260 --screenshot=out.png
  file://$PWD/in.svg`. Inkscape CLI also works if installed
  (`inkscape in.svg -o out.png -d 300`).
- **SkiaSharp / GDI+ renders:** draw the panel as SVG (or with Pillow
  `ImageDraw`, or pycairo) and convert as above.
- **PSWriteHTML dashboards:** write a short Python script that emits the
  HTML table (or a Markdown log) instead.
- **PDF export:** headless Chrome/Chromium `--print-to-pdf` instead of Edge;
  check pages with `pdfinfo` or pypdf.


## To expand this skill later

Build a running gag-premise log (mirroring `the-boba-side-cartoon`'s Step
5 PSWriteHTML dashboard idea) so a later strip doesn't quietly reuse a
premise. Settle a more specific panel-count convention once a few more
strips have run — right now it's genuinely "whatever the gag needs,"
which is fine for a seed skill but could use real data behind it. Give the
cat and dog names once the strip has run enough times that "the cat" and
"the dog" starts feeling thin.

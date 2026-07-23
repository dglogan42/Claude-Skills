---
name: cat-vs-dog-cartoon
description: Write and prepare "Cat vs Dog" — Bubble Tea News's syndicated domestic-sitcom gag cartoon starring an unnamed cat-and-dog household duo, format variable issue to issue (single panel most weeks, occasionally a short multi-panel beat when a gag needs the setup) — unlike The Boba Side, which stays single-panel every time. Unrelated to bubble tea by design, the way a real paper carries a licensed strip like Garfield or Get Fowl alongside its own local content. Art is hand-drawn on paper, photographed, and cleaned up digitally — a background-blur divide to flatten shadow/vignette, autocontrast, crop tight to the drawn content — rather than programmatically rendered; see Step 3 for the actual verified pipeline (Python/Pillow). Debuted Issue 10, taking that issue's cartoon-slot turn ahead of The Boba Side's own promised return. Use when assembling a Bubble Tea News issue that wants this cartoon slot, or when the user wants a new Cat vs Dog gag written up. This is a seed skill: sparse by design, built from one debut panel; expand with a running gag library and a settled panel-count convention as strips accumulate.
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

## To expand this skill later

Build a running gag-premise log (mirroring `the-boba-side-cartoon`'s Step
5 PSWriteHTML dashboard idea) so a later strip doesn't quietly reuse a
premise. Settle a more specific panel-count convention once a few more
strips have run — right now it's genuinely "whatever the gag needs,"
which is fine for a seed skill but could use real data behind it. Give the
cat and dog names once the strip has run enough times that "the cat" and
"the dog" starts feeling thin.

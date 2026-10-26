---
name: doki-doki-mon-strip
description: Write and prepare "Doki Doki Mon" — Bubble Tea News's second syndicated four-panel (yonkoma) manga strip, an original monster-collecting adventure series (trainer-and-creature partnerships, in the vein of the real, still-running monster-collecting genre) rendered in the same senkotsu house style as Hayaku (clean bamboo-like linework, high-contrast black-and-white, forced perspective via panel composition), deliberately unrelated to bubble tea by design. Art is hand-drawn on paper, photographed, and cleaned up digitally (background-blur divide to flatten shadow/vignette, autocontrast, crop tight) — see Step 3 and cat-vs-dog-cartoon's Step 3 for the shared, actually-verified pipeline, not a programmatic renderer. Debuted Issue 11, taking that issue's cartoon-slot turn. Use when assembling a Bubble Tea News issue that wants this cartoon slot, or when the user wants a new Doki Doki Mon strip written up. This is a seed skill: sparse by design, built from one debut panel; expand with a running cast and creature roster as strips accumulate, mirroring hayaku-senkotsu-strip's own match/season-arc tracking. Includes an artist-craft pass: artistic question, style pillars, name-before-draw panel plan, and a critique pass before print.
user-invocable: true
---

# Doki Doki Mon (seed)

A working method for **Doki Doki Mon**, *Bubble Tea News*'s second
syndicated four-panel manga strip — an original monster-collecting
adventure series, deliberately unrelated to bubble tea, running the way a
real community paper carries more than one licensed strip at once
(alongside Hayaku and Cat vs Dog). Written in the same **senkotsu** house
art-direction register as Hayaku. Treat this as a starting checklist, not
a rigid template.

## Step 0 — Genre safety check (do this before writing anything)

- **Doki Doki Mon is an original, in-house title and cast** — not a claim
  to be, a parody of, or a reproduction of any specific real
  monster-collecting franchise. That genre is extremely well-populated by
  at least one enormously famous, actively-licensed series covering
  near-identical ground (young trainer, partner creature, a world full of
  catchable monsters); keep Doki Doki Mon's trainer(s), creature designs,
  names, and specific plot beats original. Same boundary
  `hayaku-senkotsu-strip` draws for its own volleyball genre: pastiche of
  the genre's *feel*, never a retelling or reskin of somebody else's
  actual IP. If a strip idea starts converging on a specific real
  series' signature creature, catchphrase, or scene, change it before
  drawing.
- **Rendered art stays schematic/hand-drawn-sketch register**, not an
  attempt at polished franchise-quality character art — consistent with
  this library's other cartoon skills' "simple register, not a claim to
  professional illustration" boundary.

## Step 1 — The senkotsu house style

Shared with `hayaku-senkotsu-strip` — see that skill's Step 1 for the
full house-style brief (clean bamboo-like linework, hatching/crosshatching
instead of smooth shading, forced perspective via composition, high-
contrast black-and-white, exaggerated legible expressions, a clear panel
grid). Doki Doki Mon uses the same brief; the only difference is subject
matter (monster-collecting adventure instead of volleyball).

## Step 2 — Format

Exactly **four panels** (*yonkoma*), same as Hayaku. For a debut/intro
strip specifically, a close-up-portrait grid works well as an ensemble
introduction (confirmed for the Issue 11 debut: trainer close-up, two
distinct creature close-ups, and a fourth creature glimpsed at a
foreshortened/unusual angle) — establishing the cast's faces before any
strip has to stage an actual encounter or battle beat. Later strips should
move to genuine scene-to-scene panels (a wild encounter, a catch attempt,
a partner-creature reaction shot) following yonkoma's usual
setup–development–twist–payoff rhythm, the same structure
`hayaku-senkotsu-strip` documents.

For each panel give:

1. **Panel number and framing.**
2. **Scene description** (1–2 sentences) — who/what's in frame, the
   action or expression, any lighting call.
3. **Dialogue/caption line(s)**, if any.

## Step 3 — Art pipeline: hand-drawn photo, cleaned up digitally

Same pipeline as `cat-vs-dog-cartoon`'s Step 3 — see that skill for the
full mechanics (Gaussian-blur-divide shadow flattening, autocontrast, tight
crop, no separate EXIF-strip step needed). Verified working end to end for
the Issue 11 debut strip specifically. This supersedes the speculative
SkiaSharp/GDI/Inkscape renderer documentation in `hayaku-senkotsu-strip` —
that skill's own art, in actual practice, moved to this same hand-drawn-
photo approach by the time of Hayaku's own Issue 9 redraw, per
`bubble-tea-news`'s `rotation-log.md`.

One addition specific to a four-panel grid photographed as a single
sheet: crop to the outer grid border, not to each individual panel — keep
the hand-drawn panel-divider lines intact in the delivered image rather
than slicing the sheet into four separate files, matching how Hayaku's
own four-panel debut was delivered as one image.

## Artist craft (from bot artist skills)

Craft borrowed from the artist-mode, manga-studio and art-director skills — craft only, not their persona voices. Original characters only; no franchise characters. Step 0 boundaries still come first.

1. **Artistic question** — write one sentence this issue's strip answers (e.g. "what does losing look like when nobody admits it?"). If the gag doesn't answer it, fix the gag, not the question.
2. **Style pillars** — senkotsu · creature · adventure. Keep line weight consistent (heavier outer contour, lighter interior detail), simple readable silhouettes, high-contrast black-and-white that survives newsprint. Don't: polished illustration, gradients that mud in print, more than one focal point per panel.
3. **Name before drawing** — Always 4 panels, ki-shou-ten-ketsu: 1 ki trainer + creature setup, 2 shou attempt, 3 ten twist (usually the creature's), 4 ketsu landing. Per panel: beat, framing, who acts, who reacts (trainer vs creature). Keep balloons short (~25 words max), placed in reading order, never over a face.
4. **Render** — via the existing pipeline (Step 3 hand-drawn photo cleanup (shared with cat-vs-dog-cartoon Step 3)). Art stays schematic or hand-drawn-photo, not polished illustration. GenerateImage is not required and never replaces Step 0 originality rules.
5. **Critique pass before print** — open the finished PNG and look at it before embedding: (a) what is actually visible, (b) does it match the name and artistic question, (c) one or two concrete fixes (e.g. "reactor's face too small at print size — enlarge 30%"). Separate observation from interpretation; never critique art you haven't opened.

Shared critique language with: cat-vs-dog-cartoon, the-boba-side-cartoon, hayaku-senkotsu-strip.

## Step 4 — Delivery

- Within a *Bubble Tea News* issue: shares the cartoon slot's alternation
  with The Boba Side, Hayaku, and Cat vs Dog — see the editor skill's Step
  2c for current order. Treat Doki Doki Mon as **serialized**, same as
  Hayaku: note roughly where each strip lands in an ongoing arc (which
  creatures/trainers have been introduced, any running plot thread) so a
  later strip can continue rather than restart the story.
- Embed the finished PNG via `<img>`, same `max-width/max-height` cartoon
  box as the other strips (170×145px as of the Issue 9 standardization
  pass).
- Re-check the print page-count budget after embedding — verify the final
  PDF is still exactly 2 pages before calling an issue done.
- Byline convention: *"Doki Doki Mon — a new syndicated four-panel strip,
  Bubble Tea News's cartoon slot, hand-drawn; an original monster-
  collecting parody, unrelated to bubble tea by design."*

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

Add a running cast/creature roster and an arc tracker as strips
accumulate, mirroring `hayaku-senkotsu-strip`'s own Step 5 PSWriteHTML
dashboard idea (a table of strips run so far, plus a timeline of arc
beats) — the debut strip introduced faces but no names or an actual
encounter yet; the next strip should start attaching names and a first
plot beat.

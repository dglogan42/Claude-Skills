---
name: the-boba-side-cartoon
description: Write and render "The Boba Side" — Bubble Tea News's single-panel gag cartoon slot, staged as an anime/manga-style gag (otaku-culture and bubble-tea-meme sensibilities applied to original characters — chibi, shoujo, seinen, shonen, bishoujo sub-styles) and actually rendered with ImageMagick's `-draw`/inline-MVG primitives to PNG — simple schematic raster shapes carrying anime-style cues (screentone-dot hatching, speed lines, sparkle effects, named spot colors), not genuine polished anime illustration, since there's no image-generation model in this workflow. ImageMagick is the standing default renderer, embedded via `<img>` (its SVG *writer* is confirmed broken for multi-shape colored output — geometry survives but fill/stroke colors and all but the last shape are dropped — so PNG is the only reliable output here, unlike this library's other pycairo/SkiaSharp renderers). Reuses hard-won lessons from this paper's own rollout: give large fill shapes internal detail so they read at real print size, and watch the 2-page print budget. Use when assembling a Bubble Tea News issue that wants a cartoon slot, or whenever the user wants a one-panel anime-style gag actually drawn. This is a seed skill: sparse by design, built from one format and one render method; expand with more gag premises and meme formats as they come up.
user-invocable: true
---

# The Boba Side (seed)

A working method for **The Boba Side**, a single-panel gag cartoon slot for
*Bubble Tea News*, staged as an anime/manga-style gag — otaku-culture and
bubble-tea-meme sensibilities applied to original characters — and actually
rendered with **ImageMagick** (`-draw` / inline MVG syntax, to PNG): simple
schematic shapes carrying anime-style cues (screentone-dot hatching, speed
lines, sparkle effects, named spot colors) rather than genuine polished
anime illustration, since there's no image-generation model in this
workflow. Treat this as a starting checklist, not a rigid template.

## Step 0 — Three boundaries (do all three before writing anything)

**A. No image-generation model — ImageMagick approximates, it doesn't
fake.** This workflow can't call an actual image generator. ImageMagick's
`-draw` primitives are real rendering, though, so the deliverable is
**actual rendered art** — simple geometric shapes standing in for anime
conventions (a dot-pattern for screentone, radiating strokes for speed
lines, a star shape for sparkle) — not a hand-drawn illustration attempt
and not a raw prompt handed off unrendered. Say so plainly if it's ever
unclear: this is a schematic approximation of the style, not the polished
thing itself.

**B. Style reference, not character reference.** Naming a studio, artist,
or series for aesthetic direction ("Studio Trigger-adjacent," "CLAMP-style
linework") is normal, ordinary prompt-engineering vocabulary — style
itself isn't the thing copyright protects. The line is **characters**:
every figure in the panel must be original to the Bubble Tea News universe
(a tapioca pearl, a barista, a garden gnome, one of the paper's own
personas) drawn *in* a referenced style — never an actual existing
copyrighted anime/manga character making a cameo. Don't render Luffy or
Sailor Moon; render an original pearl-shaped mascot rendered like they
could've been.

**C. Memes are formats, not files.** Riffing on a well-known meme
*template* (galaxy-brain escalation, a dramatic standoff stare-down,
"it's over 9000" power-scaling, a magical-girl transformation sequence,
chibi rage-tears) applied to a bubble tea premise is the intended comedic
device — describe the format and restage it with original characters.
Don't claim to reproduce any specific meme's actual source image.

## Step 1 — The comedic engine

- **The premise device.** Take an ordinary bubble tea/café moment — the
  first sip, the last pearl in the cup, a barista's shaker technique, a
  loyalty-card countdown, a menu-board decision, the ad slot on the back
  page — and stage it with full anime dramatic weight: speed lines, a
  dramatic low angle, a sparkle effect, a chibi emotional collapse, over
  something objectively small.
- **Signature moves to draw on** (mix and match, don't use all at once):
  a mundane choice staged as a power-scaling showdown; an ordinary object
  given a magical-girl transformation sparkle; a single-panel chibi
  meltdown over something trivial; a "final boss" framing for something
  like an empty pearl jar; a deadpan caption in contrast to hyper-dramatic
  visuals (the anime-culture equivalent of a classic gag-cartoon mismatch
  device — the calm tone against the ridiculous stakes is still the joke).
- **The caption is still doing real work.** Keep it short — often a single
  line, sometimes styled like meme text (top text/bottom text, a deadpan
  narration box) rather than a traditional gag-cartoon caption. Land the
  joke in the caption even though the render carries more visual weight
  than a plain schematic gag cartoon would.

## Step 2 — The six-part composition, then render with ImageMagick

Plan each panel with the six-part formula before drawing — it's a
composition tool now, not a handoff artifact, since ImageMagick renders it
directly instead of passing it to an external generator:

1. **Sub-style anchor** — the actual category, not just "anime style."
   (*Shoujo magical-girl*, not "cartoon"; *seinen gag-manga panel*, not
   "Japanese style.")
2. **Linework descriptor** — weight and texture, set via `stroke-width`
   (bold ≈ 3–4, fine/delicate ≈ 1.5–2) and whether edges stay clean or pick
   up cross-hatch texture.
3. **Color language** — a specific, named palette (2–3 hex values), not
   "colorful." Reserve one genuine spot-color accent; everything else can
   stay black/white/grey.
4. **Studio or series reference** — carries the aesthetic DNA (*Studio
   Trigger energy*, *CLAMP-style elongated proportions*, *4-koma gag-manga
   density*) — style homage only, see Step 0-B. Use it to decide
   proportions and pacing, not as a literal render target.
5. **Atmosphere word** — the emotional register (*chaotic*, *cozy-menacing*,
   *deadpan*, *unhinged-triumphant*) — drives pose and expression choices.
6. **Technical tag** — render/finish quality, approximated in ImageMagick:

   - *Screentone texture* → a dot-grid pattern (repeated small `circle`
     primitives at regular spacing), not a flat grey fill.
   - *Speed lines* → a small cluster of parallel or radiating `line`
     primitives trailing a moving element; vary length, not color, to
     suggest motion.
   - *Sparkle/cel-shaded bloom* → a star `polygon` (alternating outer/inner
     radius points), filled with the spot color, at emotional beats.
   - *Dramatic low angle / forced perspective* → exaggerate scale between
     foreground and background elements and crop off-center; don't attempt
     true perspective-correct distortion (same honest limit `hayaku-senkotsu-strip`
     documents for its own forced-perspective panels).

Then render with ImageMagick — the technical mechanics (verified working
this way; two other approaches were tried and ruled out first, see the
warnings below):

1. Build one `-draw "..."` string (or several chained `-fill X -draw "..."`
   pairs on one command line — each new `-fill`/`-stroke`/`-strokewidth`
   applies to the draw calls that follow it) and render straight to a
   `.png` output path: `magick -size <W>x<H> xc:white -fill '#rrggbb'
   -stroke black -strokewidth 2 -draw "..." ... output.png`.
2. Circles: `circle cx,cy edgex,edgey` (center point, then any point on
   the circumference — not a radius number). Curves (a swan neck, a speech
   tail): `path 'M x,y C cx1,cy1 cx2,cy2 x,y ... Z'` — real SVG-style
   bezier control-point syntax, confirmed working inline.
3. Polygons/simple shapes: `polygon x1,y1 x2,y2 x3,y3 ...`. Rectangles:
   `rectangle x1,y1 x2,y2` or `roundrectangle x1,y1 x2,y2 rx,ry`.
4. Rotated/translated/grouped elements (a tilted sign, an angled wing):
   wrap them in `push graphic-context ... pop graphic-context` *inside*
   the `-draw` string, with `translate x,y` and `rotate deg` before the
   shape — confirmed working (this is inline MVG syntax, parsed by the
   `-draw` argument itself, a different code path from reading a
   standalone `.mvg` file — see the warning below on why that distinction
   matters). Text: `font-size N` then `text x,y 'STRING'`, same
   push/pop-wrapped pattern.
5. **Two things that look like they should work here and don't:**
   - **A standalone `.mvg` script file** (`magick scene.mvg out.png`) —
     this build's Windows binary has no MVG *decode delegate* despite
     `magick -list format` listing MVG as `rw-`; every attempt fails with
     `no decode delegate for this image format`. Inline `-draw "..."`
     strings use a different code path and work fine — write the MVG as a
     CLI argument, never as a `.mvg` file to be read back in.
   - **Writing straight to `.svg`** (`magick ... -draw "..." out.svg`) —
     produces a real `<svg>` with genuine `<circle>`/`<path>` *elements*,
     but confirmed broken beyond that: `fill`/`stroke` colors never appear
     as attributes on any shape, and only the *last* `-draw` shape survives
     at all — every earlier shape in the same command is silently dropped.
     Verified by testing a single colored circle (color vanished) and a
     multi-shape scene (only the final shape remained). This is why PNG,
     not SVG, is this skill's output format — unlike this library's
     pycairo (`the-boba-side-cartoon`'s prior renderer) and SkiaSharp
     (`hayaku-senkotsu-strip`) renders, which both produce genuine
     multi-shape vector output.
6. Embed the finished PNG via `<img src="...">` in the issue HTML — see
   Step 4. No color-tagging step is needed (unlike an SVG-based renderer):
   raster images aren't touched by this paper's
   `svg *:not(.tcolor) { fill: #000 !important; ... }` print-CSS rule at
   all, since that selector only matches `<svg>` elements.

**The one real failure mode to design around:** a large solid-fill shape
(a chalkboard background, a silhouette figure) reads as a plain color
block once shrunk to actual print size — not a rendering bug, a
composition problem. Give any large fill region internal detail *before*
trusting it to read correctly — this is exactly what the screentone-dot
and speed-line techniques above are for, doing double duty as both an
anime-style cue and the fix for this failure mode. Check the render at
actual print size (the `.ad-box` width, or whatever narrower width it
gets shrunk to per Step 4) — not a full-screen preview — before calling a
panel done.

## Step 3 — No print-CSS step needed (PNG, not SVG)

Earlier revisions of this skill used pycairo's SVG output, which needed a
`class="tcolor"` tag on every colored shape so this paper's
`@media print { svg *:not(.tcolor) { fill: #000 !important; stroke: #000
!important; } }` rule (written for the monochrome icon-circle SVGs
elsewhere in the paper) didn't clobber Boba Side's spot colors to black.
None of that applies to a PNG `<img>` — the selector only targets `<svg>`
elements, so a raster panel's colors print exactly as rendered with zero
extra CSS work. If a future revision goes back to SVG output for any
reason, revisit this step; until then there is nothing to configure here.

## Step 4 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot — see the
  editor skill's biweekly cartoon-slot anchor for cadence against Hayaku.
  Pick a fresh premise and a fresh six-part combination each time; don't
  reuse a gag, a meme format, or a prior panel's specific shapes.
- Show the rendered PNG actually rendered (inline `<img>` in the issue,
  or a file/Artifact delivery for a standalone request) — not just the
  unrendered six-part prompt text on its own.
- Re-check the print page-count budget after adding rendered art: an
  actual `<img>` is taller than a placeholder line of text and has pushed
  issues over the 2-page budget before (confirmed on `hayaku-senkotsu-strip`'s
  first embed — 130mm blew a 2-page issue to 3). If a panel needs
  shrinking, shrink the `<img>` element itself (its `max-width`), not the
  surrounding container that also holds the caption — shrinking the
  container just squeezes the caption into more wrapped lines and cancels
  out the space saved. Verify the final PDF is still exactly 2 pages
  (`pypdf` page-count check) before calling an issue done.
- If a quick text-only placeholder is genuinely all that's needed (e.g.
  drafting an issue's copy before art passes are done), the six-part
  prompt plus caption from Step 2 is a fine placeholder — but treat the
  rendered PNG as the actual deliverable for this slot, not the prompt
  text, once the issue is ready to ship.

Byline convention: *"The Boba Side" — an original anime/manga-style gag,
rendered simple; style homage only, no existing series or characters
depicted.*

## Step 5 — Optional premise-history dashboard (PSWriteHTML)

ImageMagick stays the only renderer for the artwork itself — `PSWriteHTML`
has no shape/canvas-drawing API (verified against the installed v1.41.0:
its ~200 cmdlets cover tables, ApexCharts, vis.js diagrams, calendars,
QR codes; nothing draws a line or a circle). Its actual use here is a
plain continuity dashboard, not art: a table of past premises so a new
panel doesn't quietly reuse one, per Step 4's "don't reuse a gag" rule.

```powershell
Import-Module PSWriteHTML
$PremiseLog = @(
    [PSCustomObject]@{ Issue = 9; Premise = "Loyalty card negotiates its own stamp count"; Device = "deadpan negotiation" }
    [PSCustomObject]@{ Issue = 8; Premise = "Barista explains foam physics to a bored regular"; Device = "blackboard expert" }
)
New-HTML -Title "The Boba Side — Premise Log" -FilePath "boba-side-index.html" -ShowHTML {
    New-HTMLSection -HeaderText "Panels run so far" {
        New-HTMLTable -DataTable $PremiseLog
    }
}
```

`New-HTMLTable` and `New-HTMLSection` are real, tested cmdlets (confirm
current parameter names with `Get-Command <name> -Syntax` before reuse —
`New-HTMLTimelineItem` turned out to take `-HeadingText`, not `-Title`,
despite looking like it should). This is a bookkeeping aid, generated on
demand when checking for premise reuse — not part of the delivered issue.

## To expand this skill later

Build out a running library of otaku meme-format riffs (power-scaling,
transformation sequences, chibi-rage, isekai-premise cold opens) paired
with bubble tea premises, so future panels can mix fresh combinations
rather than reaching for the same one twice. Build a small reusable
library of ImageMagick `-draw` snippets for the anime-style cues
themselves (a screentone-dot fill helper, a speed-line cluster helper, a
sparkle-star helper) so renders don't reinvent them each time. Keep the
Step 0 boundaries in place regardless of how the visual register evolves
further.

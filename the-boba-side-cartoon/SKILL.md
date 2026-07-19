---
name: the-boba-side-cartoon
description: Write "The Boba Side" — Bubble Tea News's single-panel gag cartoon slot — either as a structured anime/manga-style image-generation prompt (six-part formula) plus caption for an external generator, or as an actually-rendered simple/schematic SVG built with Python's turtle module or pycairo (optionally post-processed with matplotlib/PIL for flat color or pseudocolor). Applies otaku-culture and bubble-tea-meme sensibilities to original characters either way. Both programmatic-render backends were tried across a full 8-issue rollout and reverted in practice — see Step 0-A before reaching for either one. Use when assembling a Bubble Tea News issue that wants a cartoon slot, or whenever the user wants a one-panel anime-style gag cartoon scripted or actually drawn. This is a seed skill: sparse by design, built from one format; expand with more gag premises and meme formats as they come up.
user-invocable: true
---

# The Boba Side (seed)

A working method for **The Boba Side**, a single-panel gag cartoon slot
for *Bubble Tea News*, scripted as an anime/manga-style image-generation
prompt — otaku-culture and bubble-tea-meme sensibilities applied to
original characters. Treat this as a starting checklist, not a rigid
template.

## Step 0 — Three boundaries (do all three before writing anything)

**A. Two real deliverables, one hard quality ceiling — and a practical
failure mode on top of it, confirmed twice.** There's no model-based
image-generation tool in this workflow — nothing that can produce actual
anime/manga-quality illustration (linework variation, screentone,
cel-shading, character-design fidelity). That ceiling doesn't move no
matter which delivery mode is used. Two honest options exist:

- **Prompt script** (Step 2): a structured text prompt for the user to
  run through an external generator themselves. Not a finished image.
  Currently the only deliverable actually in use in the paper.
- **Programmatic render** (Step 2b turtle, or Step 2c pycairo):
  actually-drawn, actually-working vector art. This is real, working
  art — but it is simple geometric line/fill art, at best comparable to
  this strip's original pre-anime-pivot schematic cartoons, never
  manga-style rendering. Don't oversell it as "anime style" — it's a
  different, cruder register.

**Both programmatic backends were fully rolled out across all 8 issues
and reverted, twice, for two different reasons — read both before
picking this path again:**

1. *Turtle* (Step 2b) draws with polygon-approximated circles — visibly
   faceted, not smooth curves. A stick-figure "ant" and plus-sign
   "sparkles" were the concrete failures that killed it.
2. *pycairo* (Step 2c) fixes that — true bezier-arc circles, no
   faceting — but hit a **different, more fundamental problem**: large
   solid-fill shapes (a "chalkboard" background, a "silhouette" figure)
   rendered as plain black blocks once shrunk to actual print size,
   because a flat dark fill with no internal detail or texture doesn't
   read as anything specific at small scale — it just reads as a
   mistake. This is a **composition problem, not a rendering-backend
   problem**: switching primitives (turtle → pycairo → anything else)
   won't fix it on its own. Any future attempt at a programmatic render
   needs internal detail/contrast worked into any large fill region
   (hatching, a lighter inset shape, a partial outline break) *before*
   trusting it to read correctly at ~40-55mm print width — check that at
   actual print size, not just in an on-screen preview, before rolling
   out to more than one issue.

Ask (or infer from context) which one the moment calls for: a handoff
script for the user's own generator, or something real and renderable
right now. Default to the prompt script (Step 2) — it's the only option
with no open quality problem. Only reach for a programmatic render (Step
2b or 2c) when the user explicitly wants working output today and has
been told plainly that the last two attempts at exactly this were
reverted after full rollout.

**B. Style reference, not character reference.** Naming a studio, artist,
or series for aesthetic direction ("Ufotable-quality," "CLAMP-style
linework") is normal, ordinary prompt-engineering vocabulary — style
itself isn't the thing copyright protects, and this is the same register
`the-boba-side-cartoon`'s own prior Larson homage and this library's other
style-homage skills already operate in. The line is **characters**: every
figure in the panel must be original to the Bubble Tea News universe (a
tapioca pearl, a barista, one of the paper's own personas) drawn *in* a
referenced style — never an actual existing copyrighted anime/manga
character making a cameo. Don't put Luffy or Sailor Moon in the panel;
put an original pearl-shaped mascot rendered like they could've been.

**C. Memes are formats, not files.** Riffing on a well-known meme
*template* (galaxy-brain escalation, "sweating anime guy" decision panel,
"it's over 9000" power-scaling, "understandable, have a nice day," chibi
rage-tears) applied to a bubble tea premise is the intended comedic
device — describe the format and restage it with original characters.
Don't claim to reproduce any specific meme's actual source image.

## Step 1 — The comedic engine

- **The premise device.** Take an ordinary bubble tea/café moment — the
  first sip, the last pearl in the cup, a barista's shaker technique, a
  loyalty-card countdown, a menu-board decision — and stage it with full
  anime dramatic weight: speed lines, a dramatic zoom, a sparkle effect, a
  chibi emotional collapse, over something objectively small.
- **Signature moves to draw on** (mix and match, don't use all at once):
  a mundane choice staged as a power-scaling showdown; an ordinary object
  given a magical-girl transformation sparkle; a single-panel chibi
  meltdown over something trivial; a "final boss" framing for something
  like an empty pearl jar; deadpan narration captions in contrast to
  hyper-dramatic visuals (the anime-culture equivalent of the Larson-era
  mismatch device this strip started from).
- **The caption is still doing the work.** Keep it short — often a single
  line, sometimes styled like meme text (top text/bottom text, a
  deadpan narration box) rather than a traditional gag-cartoon caption.

## Step 2 — Format: the six-part prompt formula

Write each panel as a structured prompt, covering all six parts, then the
caption:

1. **Sub-style anchor** — the actual category, not just "anime style."
   (*Shoujo magical-girl*, not "cartoon"; *seinen gag-manga panel*, not
   "Japanese style.")
2. **Linework descriptor** — weight and texture. (*Bold, clean, confident
   linework* vs. *fine, scratchy crosshatching*.)
3. **Color language** — a specific, named palette, not "colorful."
   (*Milky pastel lavender and cream*, *neon convenience-store teal and
   magenta*.)
4. **Studio or series reference** — carries the aesthetic DNA. (*Studio
   Trigger energy*, *CLAMP-style elongated proportions*, *4-koma gag-manga
   panel density*.) Style homage only — see Step 0-B.
5. **Atmosphere word** — the emotional register. (*Chaotic*, *cozy*,
   *deadpan*, *unhinged-cute*.)
6. **Technical tag** — render/finish quality. (*Cel-shaded*, *screentone
   texture*, *clean digital linework*, *sketchbook pencil roughs*.)

Then:

7. **Scene** — what's actually happening, staged with the original
   character(s) and the bubble tea premise from Step 1.
8. **Caption** — the joke's punchline or meme-text line.

### Example shape (illustrative, not to be reused verbatim)

> **Prompt:** Shoujo magical-girl transformation sequence energy; bold
> clean linework; milky pastel lavender-and-cream palette with one hot-
> pink accent; Studio Trigger-adjacent motion lines; unhinged-cute
> atmosphere; clean cel-shaded finish. An original tapioca-pearl mascot
> character mid-air, sparkles radiating outward, arms thrown wide, as an
> ordinary cup of milk tea transforms beneath her into an oversized,
> glowing XL size.
>
> **Caption:** "SHE UPSIZED."

Byline convention: *"The Boba Side" — an image-generation prompt, not a
finished image; run it through your generator of choice.*

## Step 2b — Format: programmatic render (turtle + matplotlib/PIL)

When the moment calls for actually-rendered art instead of a handoff
prompt (see Step 0-A), draw the scene from Step 1 using Python's
`turtle` module, then convert the result into an inline SVG matching
this paper's existing icon/illustration convention
(`stroke="currentColor"`, no fixed color baked in unless the gag needs
one).

**Why turtle, and how the SVG actually gets made:** `turtle` only knows
straight lines, arcs (`circle()`), and filled polygons
(`begin_fill()`/`end_fill()`) — draw the gag as a simple composition of
those primitives (a hedge as a row of overlapping arcs, a mascot as a
triangle-hat-plus-circle-head, a cup as a trapezoid). There is no native
SVG export, so capture the drawing by reading the turtle screen's
underlying Tk canvas after drawing is done:

1. `screen = turtle.Screen(); screen.setup(width=W, height=H)`, draw with
   a hidden, full-speed turtle (`hideturtle()`, `speed(0)`,
   `screen.tracer(0)`).
2. After drawing, walk `screen.getcanvas().find_all()`. Only `"line"` and
   `"polygon"` canvas item types are relevant (querying `fill` on other
   item types, e.g. any leftover turtle-cursor item, raises a Tcl
   `TclError` — skip non-line/polygon items before calling `itemcget`).
3. For each `"line"` item, emit an SVG `<polyline>` from
   `canvas.coords(item)`; for each `"polygon"` item (anything drawn inside
   a `begin_fill()`/`end_fill()` block), emit an SVG `<polygon>` with
   `fill="currentColor"`.
4. Turtle's `(0,0)` is screen-centre with the coordinate system already
   y-flipped to match canvas/SVG conventions, so canvas coordinates drop
   straight into SVG points once shifted by `(width/2, height/2)` — don't
   forget that shift, or half the drawing lands outside the viewBox.
5. Call `turtle.bye()` to close the window once coordinates are captured.
   **Known limitation:** after `bye()` tears down the Tk root, a fresh
   `turtle.Screen()` can't reliably be reopened in the same process
   (raises `turtle.Terminator`) — render each panel as its own script
   invocation/subprocess, not sequential calls in one long-lived process.
6. Never call anything that enters `mainloop()` (`turtle.mainloop()`,
   `screen.mainloop()`, `exitonclick()`) in this workflow — those block
   waiting for a window to be closed interactively, which nothing here
   can do; they will just hang.

**Where matplotlib/PIL fit in:** they don't add illustration detail —
turtle already produced the only linework there is. Use them only for
flat post-processing on top of the captured shapes/coordinates: a
pseudocolor/colormap tint on a filled region, resizing with a chosen
interpolation (`nearest` for a deliberately blocky/pixelated gag,
`bicubic` for a soft blur), or compositing multiple panels into a strip.
If a gag doesn't call for any of that, skip this part entirely — a plain
turtle-to-SVG capture is a complete panel on its own.

Deliver the resulting SVG inline, in the same `<article class="full-block"
style="text-align: center;">` slot this strip already uses for its print
and site templates, with a caption paragraph below it and byline *"The
Boba Side" — programmatic line art, drawn with Python's turtle module.*

## Step 2c — Format: programmatic render (pycairo)

The better-quality alternative to Step 2b: `pycairo` draws true vector
paths (real `arc()`/`curve_to()` bezier curves, not polygon-approximated
ones) and exports native SVG directly — no canvas-introspection hack
needed. Read Step 0-A's failure-mode note before using this; fixing the
faceting problem does not fix the large-solid-fill legibility problem.

1. `surface = cairo.SVGSurface(<path-or-BytesIO>, W, H)`,
   `ctx = cairo.Context(surface)`. Set
   `ctx.set_line_join(cairo.LINE_JOIN_ROUND)` and
   `ctx.set_line_cap(cairo.LINE_CAP_ROUND)` to match this paper's
   existing rounded-stroke convention.
2. Circles: `ctx.arc(cx, cy, r, 0, 2*math.pi)` then `fill_preserve()` +
   `stroke()` for a filled-with-outline shape — a genuine circle, not an
   approximation. Curves (e.g. a swan neck): `ctx.curve_to(...)` for real
   bezier control-point curves.
3. Polygons: `move_to()` the first point, `line_to()` each following
   point, `close_path()`, then `fill_preserve()` + `stroke()`.
4. Rotated/translated elements (e.g. scattered paper shapes): use
   `ctx.save()` / `ctx.translate()` / `ctx.rotate()` / draw / `ctx.restore()`
   rather than pre-computing rotated coordinates by hand — cairo emits a
   `transform="matrix(...)"` on the resulting SVG path, which is correct
   and expected, not a bug (a naive regex bounds-check on raw path
   coordinates will misread these as out-of-viewBox; check rendered
   bounds, not raw local coordinates, when verifying a panel fits).
5. If writing to `cairo.SVGSurface(None, W, H)` (no filename) to capture
   the output as a string/bytes for inline embedding, render to an
   `io.BytesIO()` buffer instead and call `surface.finish()` before
   reading the buffer.
6. Tag every emitted `<path>` with a marker class (e.g. `class="tcolor"`)
   via a string replace on the finished SVG — needed for the print-CSS
   fix in Step 2d below.

## Step 2d — Print-CSS prerequisite for either programmatic render

`issues/issue-N.html` and `print-edition.html` carry
`@media print { svg, svg * { fill: #000 !important; stroke: #000 !important; } }`,
written for the paper's monochrome icon-circle SVGs. Any colored
programmatic-render art (Step 2b or 2c) gets its colors clobbered to
solid black by this rule unless it's exempted. Fix: change the selector
to `svg *:not(.tcolor) { ... }` and make sure every shape element in the
rendered SVG carries `class="tcolor"` (both Step 2b's and Step 2c's
capture/render steps above already do this). Check this fix is actually
present before assuming a colored render will print correctly — it has
had to be reapplied twice already, since reverting a render attempt back
to the prompt script also reverts the CSS rule it depended on, and the
next render attempt needs to reapply it fresh.

## Step 3 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot, not a
  weekly fixture. Deliver either the full six-part prompt plus caption
  (Step 2) or the rendered SVG plus caption (Step 2b or 2c) as the
  panel's content, per whichever deliverable Step 0-A calls for — always
  clearly labeled as which one it is. Pick a fresh premise (and, for
  Step 2, a fresh six-part combination) each time; don't reuse a prior
  panel's style stack or gag.
- **Before rolling a programmatic render out to more than one issue**,
  check it at actual print size (the `.ad-box`/site-embed width it will
  actually render at, not a full-screen preview) — the large-solid-fill
  failure mode in Step 0-A only shows up at real scale. Also re-check the
  print page-count budget after adding real art back in: image-sized
  content is taller than a few lines of prompt-script text, and it has
  twice pushed issues back over the 2-page print budget. If the panel
  needs shrinking to fit, shrink the `<svg>` element itself, not the
  surrounding container that also holds the caption text — shrinking the
  container squeezes the caption into more wrapped lines and can cancel
  out the space saved.
- As a standalone piece: chat text is fine for a single prompt. For a
  programmatic render, show the SVG rendered (Artifact or an HTML
  preview), not just the raw markup — the point of this deliverable is
  that it's real, viewable art. Offer a written file or Artifact for
  bundled multi-panel prompts or renders.

## To expand this skill later

Build out a running library of otaku meme-format riffs (power-scaling,
transformation sequences, chibi-rage, isekai-premise cold opens) paired
with bubble tea premises, so future panels can mix fresh combinations
rather than reaching for the same one twice.

The highest-value next step for the programmatic-render path specifically
is solving Step 0-A's large-solid-fill legibility problem, not building
more premises — two different rendering backends (turtle, pycairo) both
shipped a full 8-issue rollout and got reverted for it. Worth trying
before a third attempt: hatching/cross-hatch line fills instead of flat
color for any large dark region; a lighter-toned inset shape breaking up
a silhouette's silhouette; explicit internal linework (not just an
outline) on anything meant to read as a specific object rather than a
color block. Also worth building out: a small library of reusable
drawing primitives (a stock chibi body, a cup shape, a hedge/arc row) in
whichever backend proves out, so renders don't reinvent basic shapes each
time. If a true model-based image-generation tool ever becomes available
in this workflow, it would sit as a further deliverable alongside Steps
2, 2b, and 2c, not a replacement for any of them.

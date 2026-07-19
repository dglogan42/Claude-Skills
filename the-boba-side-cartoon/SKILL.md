---
name: the-boba-side-cartoon
description: Write "The Boba Side" — Bubble Tea News's single-panel gag cartoon slot — either as a structured anime/manga-style image-generation prompt (six-part formula) plus caption for an external generator, or as an actually-rendered simple/schematic SVG built with Python's turtle module (optionally post-processed with matplotlib/PIL for flat color or pseudocolor). Applies otaku-culture and bubble-tea-meme sensibilities to original characters either way. Use when assembling a Bubble Tea News issue that wants a cartoon slot, or whenever the user wants a one-panel anime-style gag cartoon scripted or actually drawn. This is a seed skill: sparse by design, built from one format; expand with more gag premises and meme formats as they come up.
user-invocable: true
---

# The Boba Side (seed)

A working method for **The Boba Side**, a single-panel gag cartoon slot
for *Bubble Tea News*, scripted as an anime/manga-style image-generation
prompt — otaku-culture and bubble-tea-meme sensibilities applied to
original characters. Treat this as a starting checklist, not a rigid
template.

## Step 0 — Three boundaries (do all three before writing anything)

**A. Two real deliverables, one hard quality ceiling.** There's no
model-based image-generation tool in this workflow — nothing that can
produce actual anime/manga-quality illustration (linework variation,
screentone, cel-shading, character-design fidelity). That ceiling doesn't
move no matter which delivery mode is used. Two honest options exist:

- **Prompt script** (Step 2): a structured text prompt for the user to
  run through an external generator themselves. Not a finished image.
- **Programmatic render** (Step 2b): actually-drawn, actually-working
  vector art via Python's `turtle` module, optionally tinted/composited
  with matplotlib or PIL. This is real, working art — but it is simple
  geometric line/fill art, at best comparable to this strip's original
  pre-anime-pivot schematic cartoons, never manga-style rendering. Don't
  oversell it as "anime style" — it's a different, cruder register.

Ask (or infer from context) which one the moment calls for: a handoff
script for the user's own generator, or something real and renderable
right now. Default to the prompt script (Step 2) when the user's framing
is about *style* ("draw this like CLAMP"); reach for the programmatic
render (Step 2b) when they want *working output* today, accepting the
lower fidelity.

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

## Step 3 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot, not a
  weekly fixture. Deliver either the full six-part prompt plus caption
  (Step 2) or the rendered SVG plus caption (Step 2b) as the panel's
  content, per whichever deliverable Step 0-A calls for — always clearly
  labeled as which one it is. Pick a fresh premise (and, for Step 2, a
  fresh six-part combination) each time; don't reuse a prior panel's
  style stack or gag.
- As a standalone piece: chat text is fine for a single prompt. For a
  programmatic render, show the SVG rendered (Artifact or an HTML
  preview), not just the raw markup — the point of this deliverable is
  that it's real, viewable art. Offer a written file or Artifact for
  bundled multi-panel prompts or renders.

## To expand this skill later

Build out a running library of otaku meme-format riffs (power-scaling,
transformation sequences, chibi-rage, isekai-premise cold opens) paired
with bubble tea premises, so future panels can mix fresh combinations
rather than reaching for the same one twice. Also worth building out: a
small library of reusable turtle-drawn primitives (a stock chibi body,
a cup shape, a hedge/arc row) so Step 2b renders don't reinvent basic
shapes each time. If a true model-based image-generation tool ever
becomes available in this workflow, it would sit as a third deliverable
alongside Steps 2 and 2b, not a replacement for either.

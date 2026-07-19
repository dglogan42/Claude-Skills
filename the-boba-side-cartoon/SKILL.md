---
name: the-boba-side-cartoon
description: Write and render "The Boba Side" — Bubble Tea News's single-panel gag cartoon slot, a clearly-labeled parody/homage to Gary Larson's Far Side sensibility (mundane creatures/objects placed in absurd deadpan situations), drawn as simple, clean schematic line/fill art rendered with pycairo — not an attempt at Larson's actual polished cross-hatched illustration, but a competent simple register, not a deliberately ugly one. pycairo is the standing default renderer for this slot (real bezier-arc paths, no polygon faceting), reusing hard-won lessons from this paper's own rollout: give large fill shapes internal detail so they read at real print size, exempt rendered color from the print stylesheet's forced-black rule, and watch the 2-page print budget. Use when assembling a Bubble Tea News issue that wants a cartoon slot, or whenever the user wants a one-panel Larson-homage gag actually drawn. This is a seed skill: sparse by design, built from one persona and one format; expand with more gag premises as they come up.
user-invocable: true
---

# The Boba Side (seed)

A working method for **The Boba Side**, a single-panel gag cartoon slot for
*Bubble Tea News*, written and drawn as a clearly-labeled parody/homage to
Gary Larson's *Far Side* sensibility — retitled and reframed around bubble
tea premises, rendered as **simple, clean schematic line/fill art**, not an
attempt at Larson's actual meticulous cross-hatched draftsmanship, but also
not a deliberately ugly or crude register — think this paper's own
icon-circle SVG convention, just a notch more detailed. Treat this as a
starting checklist, not a rigid template.

## Step 0 — Real-person safety check (do this before writing anything)

Gary Larson is a real, living cartoonist, and *The Far Side* is his
specific, trademarked, still-actively-licensed body of work. That makes
this meaningfully more sensitive than this library's fictional-character
skills — the risk isn't just publicity rights, it's treading close to a
specific artist's recognizable creative property.

- **Never title it "The Far Side."** The strip's in-fiction name is
  **"The Boba Side"** — always call it that. Never reproduce his actual
  trademark as this feature's name or byline.
- **Never present these as real, unpublished, or actual Larson work.**
  Every panel is an original, invented premise, clearly a comedic homage
  to his *sensibility* (mundane creatures/objects placed in absurd deadpan
  situations, scientist-and-blackboard scenes, animals with very ordinary
  interior lives) — not a claim that Larson wrote, drew, or endorsed it.
  Byline it as homage, never as his own signed work.
- **No real endorsement, no real affiliation.** Nothing implying Larson
  actually contributes to, has seen, or has approved of *Bubble Tea News*.
- **Don't attempt to reproduce his actual illustration style.** His real
  work is controlled, confident pen-and-ink cross-hatching — genuinely
  skilled linework. This register goes simpler on purpose (plain shapes,
  clean outlines, minimal internal detail), the same register this paper's
  own icon-circle SVGs already use — not a claim to his craftsmanship, but
  not a joke about being bad at drawing either. Simple, not sloppy.

## Step 1 — The comedic engine

- **The premise device.** Take an ordinary bubble tea/café detail — a
  barista, a tapioca pearl, a menu board, a loyalty card, the shaker, the
  straw — and place it in a flatly absurd situation, delivered with total
  deadpan sincerity by everyone involved (human or otherwise). The joke is
  the mismatch between the calm, matter-of-fact tone and the ridiculousness
  of the scene — never a punchline that winks at the reader.
- **Signature moves to draw on** (mix and match, don't use all at once):
  animals or objects with a rich, ordinary interior monologue about
  something trivial; a scientist/expert at a blackboard explaining
  something absurd in complete technical seriousness; a single moment of
  quiet, cosmic-scale irony landing on an utterly mundane character; two
  characters having a completely reasonable conversation about an
  unreasonable premise.
- **The caption is doing the work, not the drawing.** Keep the drawing
  simple and the description spare; let the caption (or a character's
  single line of dialogue) land the joke.

## Step 2 — Render with pycairo (standing default)

`pycairo` is the default renderer for this slot — not an optional
fallback. It draws true vector paths (real `arc()`/`curve_to()` bezier
curves, not polygon-approximated ones) and exports native SVG directly.

1. `surface = cairo.SVGSurface(<path-or-BytesIO>, W, H)`,
   `ctx = cairo.Context(surface)`. Set
   `ctx.set_line_join(cairo.LINE_JOIN_ROUND)` and
   `ctx.set_line_cap(cairo.LINE_CAP_ROUND)` to match this paper's existing
   rounded-stroke convention.
2. Circles: `ctx.arc(cx, cy, r, 0, 2*math.pi)` then `fill_preserve()` +
   `stroke()` for a filled-with-outline shape — a genuine circle, not an
   approximation. Curves (e.g. a swan neck): `ctx.curve_to(...)` for real
   bezier control-point curves.
3. Polygons/simple shapes: `move_to()` the first point, `line_to()` each
   following point, `close_path()`, then `fill_preserve()` + `stroke()`.
4. Rotated/translated elements: use `ctx.save()` / `ctx.translate()` /
   `ctx.rotate()` / draw / `ctx.restore()` rather than pre-computing
   rotated coordinates by hand — cairo emits a `transform="matrix(...)"`
   on the resulting SVG path, which is correct and expected, not a bug (a
   naive regex bounds-check on raw path coordinates will misread these as
   out-of-viewBox; check rendered bounds, not raw local coordinates).
5. If writing to `cairo.SVGSurface(None, W, H)` (no filename) to capture
   the output as a string/bytes for inline embedding, render to an
   `io.BytesIO()` buffer instead and call `surface.finish()` before
   reading the buffer.
6. Tag every emitted `<path>` with a marker class (`class="tcolor"`) via a
   string replace on the finished SVG — needed for the print-CSS fix in
   Step 3 below.

**The one real failure mode to design around:** a large solid-fill shape
(a "chalkboard" background, a silhouette figure) reads as a plain color
block once shrunk to actual print size — not a rendering bug, a
composition problem. Give any large fill region internal detail *before*
trusting it to read correctly: hatching/cross-hatch lines, a lighter inset
shape, a partial outline break, anything that stops it being a flat block.
This has broken two panels in the paper's history at real print scale even
though the colors themselves rendered correctly — check the render at
actual print size (the `.ad-box` width it'll really appear at, ~40-55mm),
not a full-screen preview, before calling a panel done.

## Step 3 — Print-CSS prerequisite

`issues/issue-N.html` and `print-edition.html` carry
`@media print { svg *:not(.tcolor) { fill: #000 !important; stroke: #000 !important; } }`,
written so this paper's monochrome icon-circle SVGs stay pure black in
print while exempting anything tagged `.tcolor`. Make sure every shape
element in a rendered Boba Side panel actually carries `class="tcolor"`
(Step 2's capture step above already does this) — colored render art
otherwise gets its colors clobbered to solid black in the print PDF.
Confirm this selector is present in whichever issue file you're editing
before assuming a colored render will print correctly; it has needed
reapplying more than once when an issue file's CSS diverged.

## Step 4 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot — see the
  editor skill's biweekly cartoon-slot anchor for cadence against Hayaku.
  Pick a fresh premise each time; don't reuse a gag or a prior panel's
  specific shapes.
- Show the rendered SVG actually rendered (inline in the issue, or an
  Artifact/HTML preview for a standalone request) — not just raw markup.
- Re-check the print page-count budget after adding rendered art: an
  actual `<svg>` is taller than a placeholder line of text and has pushed
  issues over the 2-page budget before. If a panel needs shrinking, shrink
  the `<svg>` element itself, not the surrounding container that also
  holds the caption — shrinking the container just squeezes the caption
  into more wrapped lines and cancels out the space saved. Verify the
  final PDF is still exactly 2 pages (`pypdf` page-count check) before
  calling an issue done.
- If a quick text-only placeholder is genuinely all that's needed (e.g.
  drafting an issue's copy before art passes are done), a short scene
  description + caption is a fine placeholder — but treat the rendered
  SVG as the actual deliverable for this slot, not the description.

Byline convention: *"The Boba Side" — a homage to Gary Larson's Far Side
sensibility, drawn simple, not an attempt at his actual artwork.*

## To expand this skill later

Build a small reusable library of pycairo drawing primitives (a stock
figure, a cup shape, a hedge/arc row) so renders don't reinvent the same
shapes each time. Add more signature devices and premise categories as
panels accumulate. Keep the Step 0 real-person boundary in place
regardless of how the visual register evolves further.

---
name: the-boba-side-cartoon
description: Write "The Boba Side" — Bubble Tea News's single-panel gag cartoon slot, a clearly-labeled parody/homage to Gary Larson's Far Side sensibility (mundane creatures/objects placed in absurd deadpan situations) rendered in a deliberately crude, unskilled "crayon-scribble" register — wobbly uneven lines, no real perspective, flat waxy color blocks, blunt stick-simple shapes — rather than any attempt at Larson's actual polished cross-hatched linework. Produces either a scene description plus caption for the reader to picture, or an actually-rendered crude programmatic SVG (turtle/pycairo with deliberate jitter), since this register is one of the few where simple programmatic primitives' usual rough edges are the intended look rather than a defect to work around. Use when assembling a Bubble Tea News issue that wants a cartoon slot, or whenever the user wants a one-panel absurdist gag cartoon in this crude Far-Side-homage style. This is a seed skill: sparse by design, built from one persona and one format; expand with more gag premises as they come up.
user-invocable: true
---

# The Boba Side (seed)

A working method for **The Boba Side**, a single-panel gag cartoon slot for
*Bubble Tea News*, written and (optionally) drawn as a clearly-labeled
parody/homage to Gary Larson's *Far Side* sensibility — retitled and
reframed around bubble tea premises, and rendered in a **deliberately
crude, crayon-scribble register**: not an attempt at Larson's actual
meticulous draftsmanship, but a comedic degradation of it, as if his sense
of humor survived intact and his drawing hand did not. Treat this as a
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
- **Don't attempt to reproduce his actual illustration style — go the
  opposite direction, on purpose.** Larson's real work is controlled,
  confident pen-and-ink cross-hatching. This register is the deliberate
  inverse: wobbly, artless, crayon-scribbled, like his sense of humor
  filtered through a small child's crayon box and none of his actual
  draftsmanship survived the trip. That's the joke, not a limitation being
  apologized for — never call it "authentic Far Side art" or claim a
  fidelity it isn't going for.

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
- **The caption is doing the work, not the drawing.** The crude visual and
  the deadpan-sharp caption should sit in contrast — a razor-precise joke
  rendered like it was scrawled in four seconds. Keep the scene description
  spare; let the caption (or a character's single line of dialogue) land
  the joke.

## Step 2 — The crayon-scribble register

Whether you're writing the scene in prose or actually rendering it (Step
3), the visual vocabulary is the same:

- **Wobbly, uneven linework** — as if drawn fast without lifting the
  crayon; no clean edges, no confident single stroke.
- **No perspective or proportion discipline.** Figures can be flat and
  front-on; limbs the wrong length; background objects sized however they
  felt like being sized. Nothing is foreshortened on purpose — it's just
  wrong, cheerfully.
- **Flat, waxy color fills instead of shading** — solid blocks of color
  that drift slightly outside their own outlines, not gradients or
  cross-hatching. (For print/monochrome delivery, a scribbled black fill
  stands in for color — see Step 3's print-CSS note.)
- **Blunt, almost-shapes** — circles that aren't quite round, rectangles
  that aren't quite square, drawn like a kid's first attempt rather than a
  geometry exercise.
- **Crude, exaggerated faces** — dot eyes, a single scribbled-line mouth —
  carrying real emotional weight despite (because of) how little
  craftsmanship is on the page.

## Step 3 — Two deliverables

There's no model-based image-generation tool in this workflow, but unlike
this paper's other cartoon registers, that ceiling barely matters here —
the rough edges a simple renderer *can't help* producing are exactly this
style's intended look, not a compromise.

**A. Scene description + caption (default, no tooling needed).** Describe
the panel in prose — 1–2 deadpan present-tense sentences calling out the
wobble/no-perspective/flat-color qualities where it matters — then the
caption or dialogue line.

Example shape (illustrative, not to be reused verbatim):

> *A lopsided, crayon-yellow cup sits alone on an otherwise empty counter,
> drawn with no straight lines anywhere on it. Two tapioca pearls, each a
> slightly-different-sized brown scribble-circle with dot eyes, peer up at
> it from the floor.*
>
> **"He's not coming back down. None of them ever do."**

**B. Actually-rendered crude SVG (optional, when the user wants real art
today).** Use `turtle` or `pycairo`, the same capture/export techniques
this library has already worked out for programmatic rendering elsewhere
in *Bubble Tea News* — but deliberately embrace what those techniques do
by default rather than fighting it:

- Turtle's polygon-approximated "circles" are visibly faceted — that
  faceting *is* a crayon-scribble circle here, not a flaw to smooth away.
- Large flat-filled shapes reading as plain color blocks at small size —
  which broke the paper's earlier anime-render attempts — is simply what
  crayon coloring looks like. Don't add internal detail/hatching to "fix"
  it; flatness is correct.
- Add a small deliberate **jitter**: perturb each line segment's endpoints
  by a few random pixels before drawing, so straight lines wobble and
  circles come out lopsided rather than clean. This is the one new
  technique this register needs that the paper's other programmatic
  attempts didn't want.
- If the print stylesheet still carries the blanket
  `@media print { svg, svg * { fill: #000 !important; stroke: #000 !important; } }`
  rule from this paper's icon-circle convention, colored crayon fills will
  print as solid black — that's a legitimate valid look for this register
  (a black-scribble print edition), so only bother exempting specific
  shapes with a `.tcolor`-style class if the user actually wants color to
  survive into the printed page, not just the web copy.

## Step 4 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot, not a
  weekly fixture — use it when the issue has room and the user wants a
  cartoon beat alongside the columns. Pick a fresh premise each time;
  don't reuse a gag or reuse a prior panel's specific rendered shapes.
- Watch the print page-count budget if delivering an actual rendered SVG
  (Step 3B): image-sized content is taller than a few lines of prose or
  prompt text. If a panel needs shrinking to fit, shrink the `<svg>`
  element itself, not the surrounding container that also holds the
  caption — shrinking the container just squeezes the caption into more
  wrapped lines.
- As a standalone piece: chat text is fine for a single prose panel. For a
  rendered SVG, show it actually rendered (Artifact or an HTML preview),
  not just raw markup.

Byline convention: *"The Boba Side" — a crayon-crude homage to Gary
Larson's Far Side sensibility, not an attempt at his actual artwork.*

## To expand this skill later

Build a small reusable library of crude drawing primitives (a jittered
wobbly-circle helper, a scribble-fill helper) so future rendered panels
don't reinvent the same shapes from scratch. Add more signature devices
and premise categories as panels accumulate. Keep the Step 0 real-person
boundary in place regardless of how the visual register evolves further.

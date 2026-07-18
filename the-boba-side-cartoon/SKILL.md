---
name: the-boba-side-cartoon
description: Write "The Boba Side" — Bubble Tea News's single-panel gag cartoon slot, narrated as a clearly-labeled parody/homage to Gary Larson's absurdist one-panel style (real, living cartoonist, best known for The Far Side) applied to bubble tea premises. Produces a scene description plus caption in place of actual artwork, since there's no image-generation tool available and reproducing Larson's specific rendering style would be a separate risk on top of the joke. Use when assembling a Bubble Tea News issue that wants a cartoon slot, or whenever the user wants a one-panel absurdist gag cartoon written up. This is a seed skill: sparse by design, built from one persona and one format; expand with more gag premises as they come up.
user-invocable: true
---

# The Boba Side (seed)

A working method for **The Boba Side**, a single-panel gag cartoon slot
for *Bubble Tea News*, written as a clearly-labeled parody/homage to
Gary Larson's absurdist one-panel style — best known for *The Far Side* —
retitled and reframed around bubble tea premises. Treat this as a
starting checklist, not a rigid template.

## Step 0 — Real-person safety check (do this before writing anything)

Gary Larson is a real, living cartoonist, and *The Far Side* is his
specific, trademarked, still-actively-licensed body of work. That makes
this meaningfully different from this library's fictional-character
skills, and a notch more sensitive than the library's other living-person
voice-parody skills (`grand-prix-showroom-ads`) — the risk here isn't just
publicity rights, it's also treading close to a specific artist's
recognizable creative property.

- **Never title it "The Far Side."** The strip's in-fiction name is
  **"The Boba Side"** — always call it that. Never reproduce his actual
  trademark as this feature's name or byline.
- **Never present these as real, unpublished, or actual Larson work.**
  Every panel is an original, invented premise, clearly a comedic homage
  to his *style and sensibility* (mundane creatures/objects placed in
  absurd deadpan situations, scientist-and-blackboard scenes, animals with
  very ordinary interior lives) — not a claim that Larson wrote, drew, or
  endorsed it. If a byline runs, phrase it as "in the style of Gary
  Larson's one-panel gag cartoons" or similar, never as if it's his own
  signed work.
- **No real endorsement, no real affiliation.** Nothing implying Larson
  actually contributes to, has seen, or has approved of *Bubble Tea News*.
- **Don't attempt to reproduce his actual illustration style.** There's no
  image-generation tool available in this workflow, and even if there
  were, mimicking a specific living artist's distinctive rendering
  technique is a separate risk layer on top of the premise-and-caption
  joke. Write the panel as a **scene description in prose** (what's
  visible, deadpan, present tense) **plus a caption** — the way the gag
  itself is described, not an attempt at the actual drawing. If the user
  wants a lightweight visual alongside the text, keep it to simple,
  schematic stick-figure/line-art SVG matching this paper's existing
  icon-circle convention (see `bubble-tea-news-editor`) — deliberately
  crude, never a pastiche of Larson's actual cross-hatched illustration
  style.

## Step 1 — The comedic engine

- **The premise device.** Take an ordinary bubble tea/café detail — a
  barista, a tapioca pearl, a menu board, a loyalty card, the shaker, the
  straw — and place it in a flatly absurd situation, delivered with total
  deadpan sincerity by everyone involved (human or otherwise). The joke
  is the mismatch between the calm, matter-of-fact tone and the
  ridiculousness of the scene — never a punchline that winks at the
  reader.
- **Signature moves to draw on** (mix and match, don't use all at once):
  animals or objects with a rich, ordinary interior monologue about
  something trivial; a scientist/expert at a blackboard explaining
  something absurd in complete technical seriousness; a single moment of
  quiet, cosmic-scale irony landing on an utterly mundane character; two
  characters having a completely reasonable conversation about an
  unreasonable premise.
- **The caption is doing the work, not the description.** Keep the scene
  description spare — just enough to picture it — and let the caption (or
  a character's single line of dialogue) land the joke.

## Step 2 — Format

A single panel, rendered as an actual (if deliberately crude) drawing, not
just described:

1. **The image.** A simple schematic SVG — stroke-only line art, matching
   this paper's existing icon-circle convention (`stroke="currentColor"`,
   thin stroke-width, minimal filled dots for eyes/pearls/small details,
   no gradients or cross-hatching). Frame it in a plain rectangular
   border, same as a printed panel. Keep the element count low — a dozen
   or so paths/shapes is usually enough to read the gag; resist adding
   detail for its own sake. This is the default delivery now — write the
   SVG, don't just prose-describe the scene, unless the user explicitly
   asks for text only.
2. **Caption or dialogue line**: the joke itself, usually short, set below
   the image.

A prose "scene description" is only a fallback for chat-only delivery
where no image/file output is possible — prefer the SVG whenever the
output medium supports it (an issue page, an Artifact, a written file).

Example caption shape (illustrative, not to be reused verbatim):

> **"Look, it's not you. It's the straw."**
>
> *(panel: two tapioca pearls at the bottom of an otherwise empty cup, one
> wearing tiny reading glasses, reviewing a sheet of paper headed "Exit
> Interview")*

Byline convention: *"The Boba Side" — in the style of Gary Larson's
one-panel gag cartoons.*

## Step 3 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot, not a
  weekly fixture — use it when the issue has room and the user wants a
  cartoon beat alongside the columns. Pick a fresh premise each time;
  don't reuse a gag.
- As a standalone piece: chat text is fine for a single panel. Offer an
  Artifact only if the user wants several panels laid out together, and
  keep any accompanying art to simple schematic line work per Step 0.

## To expand this skill later

Add more signature devices and premise categories as panels accumulate.
If the user ever wants this attributed to an original, non-real-person
persona instead (sidestepping Step 0 entirely), that's a reasonable
variant to add — an in-house *Bubble Tea News* cartoonist character, the
same way Gordon Slate and Freya Wilcox are original in-house personas
rather than real-person parodies.

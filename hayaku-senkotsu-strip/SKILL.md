---
name: hayaku-senkotsu-strip
description: Write "Hayaku" — Bubble Tea News's syndicated four-panel (yonkoma) sports-manga strip, an original high-school volleyball series described in "senkotsu" style (clean bamboo-like linework, HB under-sketch with 2B-6B-style hatched/crosshatched shading, forced perspective, high-contrast black-and-white for newsprint). Produces a panel-by-panel scene description plus dialogue in place of actual artwork, since there's no image-generation tool available. Runs as an unrelated syndicated strip alongside the paper's own bubble tea content, the way a real newspaper carries Garfield or Peanuts. Use when assembling a Bubble Tea News issue that wants a syndicated comic-strip slot, or whenever the user wants a Hayaku strip written up. This is a seed skill: sparse by design, built from one house style brief (senkotsu.YAML); expand with a running cast and match/season arc as strips accumulate.
user-invocable: true
---

# Hayaku (seed)

A working method for **Hayaku**, *Bubble Tea News*'s syndicated
four-panel sports-manga strip — a high-school volleyball series, deliberately
unrelated to bubble tea, running the way a real community paper carries a
licensed strip like *Garfield* or *Peanuts* alongside its own local content.
Drawn in prose (there's no image-generation tool in this workflow) per the
**senkotsu** house art-direction brief. Treat this as a starting checklist,
not a rigid template.

## Step 0 — Genre safety check (do this before writing anything)

- **Hayaku is an original, in-house title and cast** — not a claim to be, a
  parody of, or a reproduction of any specific real manga/anime. School
  volleyball is a well-populated real genre with at least one very famous,
  actively-licensed series covering near-identical ground; keep Hayaku's
  characters, team/school names, rivalries, and specific plot beats
  original. The target is genre pastiche — underdog-team energy, dramatic
  action beats, the yonkoma sports-manga *feel* — not a retelling or
  reskinning of somebody else's actual IP. If a strip idea starts to
  converge on a specific real series' signature scene or character, change
  it before writing.
- **No actual artwork is produced.** Every strip is a **panel-by-panel
  prose description plus dialogue**, the same convention this library uses
  for `the-boba-side-cartoon` — describe what the panel would show, in the
  house style below, rather than attempting rendered art.

## Step 1 — The senkotsu house style

Write each panel's scene description so it *implies* this look, even though
no image is produced:

- Clean, bamboo-like linework — simple, confident, bold strokes, as if
  inked with a heavier pencil (2B–6B) over a lighter HB under-sketch.
- No smooth/painterly shading — texture comes from **hatching and
  crosshatching**, giving a hand-pulled, traditional print feel.
- **Forced perspective and foreshortening** on action beats — dramatic,
  low or tilted angles, not flat side-on views.
- Call out the **lighting** per panel: natural/outdoor (harsh midday,
  long late-afternoon shadow) vs. artificial/indoor (flat gymnasium
  fluorescent) — let it carve highlights and shadow across the characters.
- **High-contrast black-and-white**, suited to cheap newsprint
  reproduction — think in blacks and whites, not greys.
- **Exaggerated, legible expressions and body language** — a single frozen
  frame should still read the emotional beat. This is a strip about
  *movement and stakes*.
- Keep characters in believable human proportions even when expressions
  are exaggerated — no chibi/super-deformed style shifts.
- Frame each panel with a clear internal border/grid so the strip's own
  four-panel block absorbs any layout overflow rather than bleeding into
  the surrounding newspaper page.

## Step 2 — Format

Exactly **four panels** (a yonkoma strip, laid out vertically or as a 2×2
grid — writer's choice). For each panel give:

1. **Panel number and framing** (e.g. "Panel 1 — wide, outdoor, forced low
   angle").
2. **Scene description** (1–2 sentences): who's on court, the action, the
   lighting call.
3. **Dialogue/caption line(s)**, if any — these strips often run mostly
   silent action beats punctuated by a single shout or thought.

The fourth panel is usually the payoff (a spike landing, a whistle, a
reaction shot), following yonkoma's typical setup–development–twist–payoff
(*ki-shou-ten-ketsu*) rhythm rather than a single-panel gag's punchline.

Example shape (illustrative, not to be reused verbatim):

> **Panel 1** — wide, outdoor practice court, late-afternoon side light
> raking long shadows across the paint. A libero crouches low, weight
> forward.
> *"Rotation's wrong again — call it!"*
>
> **Panel 2** — tight on the setter's hands mid-release, crosshatched
> motion lines trailing the ball.
>
> **Panel 3** — forced-perspective low angle on the spiker rising; indoor
> gym light this time, ball foreshortened huge in frame.
>
> **Panel 4** — wide reaction shot, ball buried on the far side of the
> net, the whole bench half-risen off it.
> *"...Okay. Now call it."*

## Step 3 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot alongside,
  not replacing, The Boba Side — the two can coexist as separate strips,
  the way a real paper runs more than one. Treat Hayaku as **serialized**:
  note roughly where each strip lands in an ongoing match/season arc so a
  later issue can continue the story rather than restart it.
- As a standalone piece: chat text is fine for a single strip.

## To expand this skill later

Add a running cast list and a match/season arc tracker as strips
accumulate, so continuity holds issue to issue — mirroring how
`bubble-tea-news-editor` tracks its own rotation log.

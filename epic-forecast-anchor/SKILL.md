---
name: epic-forecast-anchor
description: Write local TV weather segments narrated by an original weather presenter, Dana Foley, who treats every forecast — however mundane — with the emotional weight and narrative stakes of a nature-documentary trailer, while the actual meteorology underneath stays genuinely accurate. Use when the user wants a weather segment, forecast script, or "ordinary thing narrated like an epic" piece. This is a seed skill: sparse by design, built from one persona; expand with more anchors and formats as they come up.
user-invocable: true
---

# Epic Forecast Anchor (seed)

A working method for local weather segments narrated by an original
presenter, **Dana Foley**, whose defining trait is narrating a 20% chance
of drizzle like the final act of a nature documentary. Treat this as a
starting checklist, not a rigid template.

A full worked example — an illustrative Millhaven Valley evening forecast
demonstrating the clinical-readout/epic-narration pairing, the anticlimax
handling, and the Trent foil — lives at
`examples/millhaven-valley-forecast.md` in this skill's directory.

## Step 0 — Real-weather accuracy, if covering a real place

If a segment is written for a real city or a real upcoming forecast, the
drama is comedic invention but the underlying numbers should stay honest.

- Default to an **invented town** for illustrative pieces — this sidesteps
  the accuracy question and is usually funnier anyway (an invented
  microclimate can be as absurd as the bit needs).
- If the user wants a real place's real forecast as the hook, verify actual
  current conditions via WebSearch before stating specifics, and keep the
  dramatic narration clearly separable from the factual numbers so the
  piece can't be mistaken for an actual forecast.

## Step 1 — The persona

- **Dana Foley.** Local weather anchor. Genuinely, technically competent —
  she knows her isobars, dew points, and pressure systems, and gets them
  right — she simply refuses to report any of it at a proportionate
  emotional register. A sunny, unremarkable Tuesday gets narrated with the
  same gravity as an approaching hurricane, because to Dana, weather is
  never boring, only underappreciated.
- **The core device — clinical readout, then epic narration.** Structure
  each forecast beat as a pair: first the flat, accurate data (high, low,
  percent chance of precipitation, wind speed), immediately followed by
  wildly disproportionate dramatic narration of the same fact. The gap
  between the two registers, repeated through the segment, is the joke.
- **Personified systems.** Weather fronts, pressure systems, and storms get
  discussed like characters with motive and history — "the front doesn't
  know we're not afraid of it" — without ever losing the real meteorology
  underneath the personification.
- **The anticlimax problem.** A calm, mild day is treated as narratively
  suspicious — a lull before something, a twist ending she has to sell
  with the same intensity as an actual severe-weather day. She never lets
  "nothing is happening" read as nothing is happening.
- **Recurring foil.** A co-anchor or sports-desk presence (default:
  "Trent") who just wants the segment to end on time and reacts to her
  drama with visible, weary patience — a beat of contrast/friction to play
  her intensity against, similar in spirit to the rival-foil texture in
  `master-of-the-universe-columnist` and `the-world-bulletin-anchor`, but
  played as gentle exasperation rather than rivalry or chaos.
- **Sign-off catchphrase.** Closes segments with a variant of "Stay dry,
  stay alive, I'll see you at six" — adjust the middle clause to match
  whatever the day's actual weather was, keeping the rhythm consistent.

## Step 2 — Format

- A single forecast segment: today's conditions plus a short outlook,
  built from clinical-readout/epic-narration pairs for two or three beats
  (today, tonight, the week ahead).
- A longer piece can bundle a full week's outlook, or add the Trent
  back-and-forth as a proper two-hander.

## Step 3 — Delivery

- A short segment: chat text, no file needed.
- A longer piece: write to a file in the project/scratchpad directory and
  offer to render as an Artifact — a broadcast-graphics look (forecast
  card icons, a 5-day strip, a lower-third nameplate) distinct from this
  library's other templates.

## To expand this skill later

Add more anchors/formats as they come up (a rival station's dry,
deadpan-only forecaster as a foil piece; a severe-weather special-report
variant). Keep Step 0's real-weather accuracy discipline in place for any
variant that touches a real place or real conditions.

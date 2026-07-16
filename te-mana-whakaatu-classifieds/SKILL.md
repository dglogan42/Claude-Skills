---
name: te-mana-whakaatu-classifieds
description: Write a newspaper classifieds section where every ordinary ad (garage sale, lost cat, flatmate wanted, car for sale) gets an official-style content classification rating and dry bureaucratic descriptor, in the format of Te Mana Whakaatu (New Zealand's real Classification Office) — applied absurdly to trivial classified-ad content. Because this borrows a real government body's name and format, it's built around a clearly-labeled parody framing with an explicit non-affiliation disclaimer and invented ad content only. Use when the user wants comedic "serious official rating system applied to mundane classifieds" content. This is a seed skill: sparse by design, built from one format; expand with more classification styles and sections as they come up.
user-invocable: true
---

# Te Mana Whakaatu Classifieds (seed)

A working method for a newspaper classifieds section where every mundane
ad gets a dead-serious content classification, in the format (rating tiers
plus a formulaic descriptor line) of Te Mana Whakaatu — New Zealand's real
Classification Office. Treat this as a starting checklist, not a rigid
template.

A full worked example — "This Week's Classifieds," six invented ads with
ratings, descriptors, and a "reasons for decision" aside — lives at
`examples/this-weeks-classifieds.md` in this skill's directory.

## Step 0 — Real-institution safety check (do this before writing anything)

Te Mana Whakaatu is a real New Zealand government regulatory body. That
makes this meaningfully different from this library's fictional-character
skills.

- **Fine:** clearly comedic, clearly fictional parody — the real rating
  tiers and the real descriptor-line format, applied absurdly to invented,
  trivial classified ads. This is the same "satire of a real institution in
  a clearly-labeled parody register" category this library already treats
  as fine for real public figures (`grand-prix-showroom-ads`) and
  trademarked formats (`the-world-bulletin-anchor`).
- **Not fine:** anything that could read as an actual, genuine
  classification decision — inventing a rating for a real film, game, book,
  or other real media that already has a real classification, or phrasing
  that could be mistaken for genuine government output rather than obvious
  satire.
- **Always use invented ad content.** Garage sales, lost pets, flatmates
  wanted, cars for sale, personals — never a real, specific, currently
  classified piece of media.
- **Include a plain disclaimer** on any longer or shareable piece (a full
  section, an Artifact) noting it's satire, not affiliated with or produced
  by the real Classification Office of New Zealand.

## Step 1 — The format

- **Rating tiers**, matching the real system's shape: G, PG, M, R13, R16,
  R18 — general audience through restricted. Pick the tier the ad's
  (invented, mundane) content would plausibly earn if taken with total
  bureaucratic seriousness.
- **The descriptor line — the comedic engine.** Every real NZ
  classification comes with a formulaic "Contains X, Y, and Z" line
  (violence, offensive language, drug use, etc.). Write that exact
  formulaic structure, straight-faced, describing something utterly
  trivial from the ad's content: *"Contains coarse language (directed at a
  wasp), mild peril, and unresolved tension regarding the couch's actual
  age."* The mismatch between bureaucratic gravity and trivial stakes is
  the whole joke — never let the descriptor wink at the reader; play it
  completely straight.
- **Occasional "reasons for decision" aside.** For a stand-out ad, add a
  short dry note in the style of a real classification office publishing
  its reasoning — treat a garage-sale listing's rating dispute with the
  gravity of an actual appeal.

## Step 2 — Ad content to draw on

- Garage sales, lost/found pets, flatmates wanted, cars for sale,
  personals, community notices (working bee, book club, lost umbrella).
- Let the rating logic actually follow from something genuinely present in
  the ad text (a garage sale mentioning a "heated dispute with the
  neighbour" earns the language warning; a lost-cat notice with a
  dramatic backstory earns "mild emotional intensity") rather than
  assigning ratings at random — the joke lands harder when the descriptor
  is traceable to a real detail in the ad.

## Step 3 — Delivery

- A few ads: chat text, no file needed.
- A full section: write to a file in the project/scratchpad directory and
  offer to render as an Artifact — a classifieds-page newspaper look
  (column rules, small rating badges) with the non-affiliation disclaimer
  included in the footer.

## To expand this skill later

Add more classification-style formats as they come up (a food-safety
grading system applied to something trivial, a building-consent format
applied to a treehouse). Keep Step 0's real-institution discipline in
place for any variant that borrows a real regulatory body's actual format.

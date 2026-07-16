---
name: grand-prix-showroom-ads
description: Write cheesy local-newspaper automotive-dealer-section ad copy narrated in the voice of Lewis Hamilton (real F1 driver), applying elite motorsport hyperbole and technical vocabulary to mundane used-car-lot sales tactics. Because this uses a real, living person's identity, it's built around a clearly-labeled parody framing with invented dealerships only — never presented as, or confusable with, a real endorsement. Use when the user wants comedic "F1 champion voice meets small-town car-lot ad" content. This is a seed skill: sparse by design, built from one framing; expand with more real-person-parody personas and formats as they come up.
user-invocable: true
---

# Grand Prix Showroom Ads (seed)

A working method for cheesy automotive-dealer-section newspaper ad copy,
narrated in the voice of Lewis Hamilton, applying F1 hyperbole and
technical vocabulary to mundane used-car-lot sales tactics. Treat this as
a starting checklist, not a rigid template.

A full worked example — an illustrative Route 9 Motors clearance-event ad
(invented dealership, clearly-labeled parody) — lives at
`examples/route-9-motors.md` in this skill's directory.

## Step 0 — Real-person safety check (do this before writing anything)

Lewis Hamilton is a real, living person with real commercial automotive
relationships (sponsorships, brand deals). That makes this meaningfully
different from this library's fictional-character skills — the risk isn't
copyright, it's publicity rights and false endorsement.

- **Fine:** clearly comedic, clearly fictional parody — F1 bravado and
  technical jargon applied absurdly to a small-town car lot, invented
  dealership names, invented sale events, played for the joke of the
  mismatch. This is the same "satire of public figures in a clearly-labeled
  parody register" category `tabloid-gossip-voice`'s Step 0 already treats
  as fine.
- **Not fine:** anything that could pass as, or be mistaken for, a real
  endorsement — using a real dealership's actual name, a real current car
  model/price presented as an actual offer, or phrasing designed to read
  as genuine promotional copy rather than obvious satire. Don't fabricate
  quotes implying he actually said or endorsed something in real life.
- **Always use invented dealerships and invented deals.** Never a real
  business name, never real current pricing/inventory. If the user wants
  this used as actual promotional material for a real business, that's a
  different, not-fine use — flag it rather than writing it.
- Keep the register broad and obviously parodic (racing metaphors pushed
  to absurd lengths) rather than realistic-sounding ad copy — the more
  clearly it reads as a bit, the less risk of it being mistaken for
  something real.

## Step 1 — The comedic engine

- **F1 diction applied to car-lot stakes.** Pit-stop precision, apex lines,
  DRS, tire degradation, telemetry, podium finishes, championship-points
  language — all applied, straight-faced, to sedan financing and a Labor
  Day clearance event. The mismatch in stakes (world championship vs. a
  used minivan) is the whole joke, the same device family as
  `master-of-the-universe-columnist`'s grandiose-diction-on-mundane-stakes
  move, aimed here at car-lot advertising instead of Wall Street.
- **Real racing specifics, fictional dealership.** Ground the hyperbole in
  genuinely accurate, specific F1 texture (real pit-stop record times are
  public knowledge and fine to reference for the joke — "tire rotation
  faster than a Silverstone pit stop") while keeping the dealership,
  inventory, and deals entirely invented.
- **Classic dealer-ad tics, played straight underneath the parody.** ALL
  CAPS sale events, exclamation points, "financing available," a fine-print
  disclaimer at the bottom — the format of a real local car-lot ad,
  narrated by someone whose actual vocabulary is built for 200 miles an
  hour.

## Step 2 — Format

- Default to a short block of ad copy — headline, a paragraph or two of
  Hamilton-voiced pitch, a closing tagline — for one invented dealership
  and one invented sale event.
- A fuller piece can bundle several invented ads under one invented paper's
  automotive section masthead.

## Step 3 — Delivery

- A short piece: chat text, no file needed.
- A fuller piece: write to a file in the project/scratchpad directory and
  offer to render as an Artifact — a classified/dealer-section newspaper
  page look (column rules, bold sale-event headers, a coupon-style border)
  distinct from this library's other templates.

## To expand this skill later

Add more real-person-parody personas/formats as they come up, each getting
its own Step 0 real-person safety pass tailored to that person's actual
public commercial relationships — don't assume the same guardrails apply
identically to a different real person without checking.

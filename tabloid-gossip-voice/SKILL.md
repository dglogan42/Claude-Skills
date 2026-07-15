---
name: tabloid-gossip-voice
description: Rewrite or draft text in the voice of an anonymous "kiss and tell" tabloid gossip columnist (David Hartnell-style: catty, affectionate, alliterative, addresses the reader as "darling"). Use when the user asks to write a gossip column, rewrite existing text "in the gossip voice," create an anonymous tabloid persona, or produce satirical community/celebrity gossip items. This is a seed skill: sparse by design, built from one persona (The Stickybeak) and one style-transfer pass; expand with more personas, formats, and safety cases as they come up.
user-invocable: true
---

# Tabloid Gossip Voice (seed)

A working method for writing in — or rewriting existing text into — an
anonymous tabloid gossip columnist's voice, built from one persona
(**The Stickybeak**, "Kiss & Tell") used first for an invented Facebook
community-group column, then for a style-transfer pass on a user's own
personal essay. Treat this as a starting checklist, not a rigid template.

## Step 0 — Real-person safety check (do this before writing anything)

- **Fine:** rewriting the user's own writing in this voice; commentary on
  fictional characters/shows; satire of public figures in a clearly-labeled
  parody register; fully invented composite characters and scandals.
- **Not fine:** inventing "dirt" about identifiable real private
  individuals — neighbours, coworkers, members of a real community or
  Facebook group — even under an anonymous handle. Anonymity here mainly
  serves to dodge accountability for what would be real-world gossip or
  defamation about real people.
- If a request names a real private person, a real community group, or
  real personal drama the user didn't themselves supply as source text,
  pause and ask what's fictionalized vs. real via `AskUserQuestion` rather
  than assuming intent.

## Step 1 — The persona

Established default: **The Stickybeak** ("Kiss & Tell" column). Traits:

- Anonymous, first person, addresses the reader as "darling" / "loves" /
  "reader."
- Society-column catty *affection*, not cruelty — the target is a
  situation or a mood, never a real vulnerable person.
- Alliterative, punny framing; mock-scandalized tone applied to
  low-stakes material.
- Signature moves: rhetorical asides, faux "sources confirm," mock-solemn
  corrections, a wink that she's exaggerating for effect.

Reuse this persona by default. If a new persona is wanted, define its
name/handle, tagline, and one or two verbal tics before drafting anything
else — don't improvise voice and content simultaneously.

## Step 2 — Style-transfer conventions (rewriting existing text)

- Preserve the source's underlying facts, beats, and structure; only the
  narration voice changes.
- Convert flat description into "reporting" ("your Stickybeak can
  reveal...", "sources close to the bathtub confirm...").
- Where the original was reflective or analytical, add a first-person
  aside that *reacts* rather than explains.
- Keep at least one beat of real sincerity/vulnerability if the source had
  one — cattiness lands best set against genuine feeling; don't flatten
  the whole piece into a joke.
- Structural garnish (italic pull-quote, a mock headline dropped mid-piece,
  a tip-line sign-off) is optional seasoning for long-form prose rewrites —
  don't force full tabloid-page formatting onto something meant to read as
  continuous narrative.

## Step 3 — Fresh-item conventions (drafting new gossip, not rewriting)

- Invent composite characters and fictional place names distinct from any
  real named group or suburb the user mentioned.
- Keep stakes deliberately low and silly (sausage-roll swaps, garden-gnome
  prank wars, book-club spoiler feuds) — the comedy is the mismatch
  between tabloid drama and mundane stakes.
- Close with a fine-print disclaimer that names/scandals are invented,
  whenever the piece is presented as a "publication" (masthead, issue
  number, byline card) rather than a one-off rewrite.

## Step 4 — Delivery

- A short rewrite: return as chat text, no file needed.
- Anything meant to look like a publication (masthead, multiple items,
  byline card, "Spotted" sidebar): copy
  `templates/tabloid-front-page.html` (in this skill's directory) to the
  target scratchpad/project path rather than designing a layout from
  scratch. It's a persona-agnostic front page — torn-edge divider under
  the masthead, byline card with a rotated stamp, two-column body with a
  drop cap, "Spotted" quick-hits sidebar, dashed tip box, light/dark theme
  tokens already wired up. Fill in every `{{TOKEN}}` per the comment block
  at the top of that file (masthead text, persona bio, one duplicable item
  block, one duplicable sidebar `<li>`), delete the instructional comment,
  then publish as an Artifact.

## To expand this skill later

Add more personas (a campy showbiz insider, a deadpan corporate-Slack
gossip persona) as Step 1 variants, and more source-text types to
style-transfer (song lyrics, meeting minutes, press releases) as Step 2
cases. If a second layout shape emerges (e.g. a single-item "special
bulletin" instead of a multi-item issue), add it as a second file under
`templates/` rather than overloading this one.

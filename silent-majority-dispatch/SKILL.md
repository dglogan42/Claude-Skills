---
name: silent-majority-dispatch
description: Write political commentary/dispatches narrated in the voice of Richard Nixon — a real, deceased historical figure — reporting on politics (present-day or historical) through his well-documented psychology (embattled, press-distrustful, Cold-War-framing, obsessed with his own vindication, genuinely shrewd on foreign policy despite his domestic paranoia). Built around historical-accuracy and non-partisan discipline since the subject is a real person and the topic is politics. Use when the user wants political commentary, a "what would Nixon say about this" column, or historical-figure political satire. This is a seed skill: sparse by design, built from one persona; expand with more historical-figure personas and eras as they come up.
user-invocable: true
---

# Silent Majority Dispatch (seed)

A working method for political commentary narrated in Richard Nixon's
voice — grounded in his real, well-documented personality and history,
applied to whatever he's reporting on. Treat this as a starting checklist,
not a rigid template.

A full worked example — "On the Age of the Leak," a dispatch grounded in
his real history with the Pentagon Papers and Watergate, kept off real
living political figures per Step 0b — lives at
`examples/age-of-the-leak.md` in this skill's directory.

## Step 0a — Historical accuracy (do this before writing anything)

- Nixon is a real, deceased historical figure. **Well-documented facts are
  fair game to reference accurately** — Watergate, the resignation, the
  tapes, "I am not a crook," the China opening, détente, the "silent
  majority" speech, his post-resignation career as an elder statesman.
  Get these right; don't invent false history and present it as fact.
- **Invented material — new dialogue, an imagined column, a reaction to a
  present-day event — should read clearly as imagined/satirical**, not be
  presented as a real quote or a real thing he said or did. The persona is
  speculative by construction (he's commenting on things after his own
  lifetime in some pieces); keep that speculative framing implicit in the
  format itself rather than needing a disclaimer on every piece, but never
  blur it with an actual historical claim.

## Step 0b — Non-partisan discipline (this is the important one)

The subject matter here is politics, which makes this a higher-care
category than this library's other real-person skills.

- **This skill is not a vehicle for the user's or the model's real current
  political opinions.** The comedy/insight comes from Nixon's own
  documented psychology (paranoia, press antagonism, self-vindication,
  Cold War framing) applied to a topic — not from smuggling in one-sided
  present-day political advocacy under his name.
- **Be careful with real, living current political figures.** Don't put
  fabricated factual claims about a real living person in the persona's
  mouth, and don't let the piece read as a genuine attack on or endorsement
  of a real living person — satire of the *format* and of Nixon's own
  psychology, not manufactured claims about someone else living today.
  Prefer covering institutions, events, or historical topics over
  individual living politicians where the piece doesn't specifically need
  one.
- If the user wants this used for real political advocacy or to spread a
  claim about a real current figure, flag that as a different, not-fine
  use rather than writing it.

## Step 1 — The persona

- **Psychology, not caricature.** Draw on the real, documented Nixon:
  embattled and defensive, sees enemies arrayed against him even when
  discussing something unrelated, deeply distrustful of "the press,"
  obsessed with his own legacy and vindication, prone to Cold-War framing
  of almost any conflict, populist appeals to a "silent majority" watching
  quietly at home.
- **The genuine competence underneath.** Historically, Nixon was often
  shrewd and effective on foreign policy despite his domestic paranoia and
  flaws — that real mismatch (personally embattled, geopolitically
  sharp) is worth preserving rather than flattening him into pure
  caricature. Let a piece occasionally crack into a genuinely incisive
  geopolitical observation between the defensive crouches.
- **Voice.** Gruff, formal, self-referential in the third person on
  occasion, quick to reframe any criticism as part of a larger pattern of
  unfair treatment, given to sudden hard pivots into surprising candor.

## Step 2 — Format

- Default: a dispatch/column — "The Silent Majority Report" — reacting to
  a topic (present-day or historical) in his voice, one piece per topic.
- Historical pieces can quote or closely paraphrase his real documented
  positions; present-day pieces are inherently speculative ("Nixon,
  watching from wherever embattled elder statesmen watch from") and should
  read as clearly imaginative extrapolation from his known psychology, not
  a real prediction stated as fact.

## Step 3 — Delivery

- A short dispatch: chat text, no file needed.
- A longer or serialized set: write to a file in the project/scratchpad
  directory and offer to render as an Artifact — a restrained
  op-ed/newsletter look, not a decorative template.

## To expand this skill later

Add more historical-figure personas as they come up, each with its own
Step 0a historical-accuracy pass and Step 0b care level appropriate to how
politically live the figure and topic still are.

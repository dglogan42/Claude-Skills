---
name: screenplay-creation
description: Write an original screenplay from a premise, especially found-footage / first-person investigation horror (Blair Witch-style). Use when the user asks to write, draft, or adapt a screenplay, script, or shooting draft — particularly anything framed as "recovered footage," a documentary-style investigation, an analog-horror piece, or an ARG/cursed-media mystery. This is a seed skill: sparse by design, meant to be expanded with more sub-genres, formatting presets, and examples as they come up.
user-invocable: true
---

# Screenplay Creation (seed)

A working method for turning a loose premise into a full, original screenplay —
built from doing this once for a found-footage investigation piece
("UNLISTED"). Treat this as a starting checklist, not a rigid template:
expand it in place as new genres/premises are handled.

## Step 0 — IP safety check (do this before writing anything)

If the user's premise names, or closely tracks, an existing copyrighted
work — a specific novel, film, franchise, game, or its characters/plot —
**stop and flag it** rather than drafting a derivative adaptation. A
scene-by-scene dramatization of someone else's protected characters/plot is
infringement risk, not fan appreciation.

- Say plainly what the resemblance is and to what work.
- Offer the original-transformation path: keep the *shape* of the idea
  (genre, mechanic, tone) but invent new title, characters, and plot
  specifics.
- Use `AskUserQuestion` to let the user pick how far to depart from the
  source (fully original / loose homage / different premise entirely)
  rather than deciding unilaterally or refusing outright.
- Only proceed to drafting once the premise is either original or the user
  has explicitly chosen how to handle the resemblance.

## Step 1 — Get the premise, don't guess it

If the request is underspecified ("write me a horror screenplay"), ask
before writing. Useful axes:

- **Setting** — where does this happen?
- **Premise/inciting mystery** — what is being investigated or uncovered?
- **Cast** — how many characters, what's each one's function in the group?
- **Length/scope** — full feature, treatment/outline, or a single act?
- **Tone** — grounded/slow-burn vs. overtly supernatural; how much is
  explained vs. left ambiguous?

Use `AskUserQuestion` for anything genuinely open (see Step 0 for the IP
case specifically). Don't ask about things you can just decide well
(character names, minor blocking, scene order within an act).

## Step 2 — Structural blueprint (found-footage / investigation horror)

The Blair Witch model, generalized:

1. **Disclaimer / framing card** — establish the footage as recovered,
   found, or leaked, and by whom. This is what licenses the first-person,
   unpolished camera language for the rest of the script.
2. **Cold open** — a short, unsettling teaser scene (often the *last*
   piece of footage chronologically, or a fragment) that pays off later.
   Then a title card.
3. **Act 1 — normalcy and setup.** Introduce the investigator(s), the
   stakes, and the missing/wronged party. Gather evidence through
   interviews and **screen inserts** (chat logs, code, documents,
   recordings of calls). Establish the "rules" of whatever cursed
   media/mystery is driving the plot.
4. **Act 2 — descent.** The crew travels to the site tied to the evidence.
   Local color confirms the folklore/history is real, not just in-fiction.
   Escalate with small wrongness first: audio that shouldn't be there,
   technology behaving like the fiction predicted, environmental omens
   (markings, repeated symbols, shrines). End the act by separating the
   group.
5. **Act 3 — crisis.** Footage gets chaotic — handheld, dropped cameras,
   partial darkness, audio-only stretches. Characters disappear one at a
   time. Do **not** over-explain the horror; the last confirmed image or
   line should raise the temperature, not answer it.
6. **Epilogue / text cards.** Plain, factual-sounding aftermath cards
   (who was found, who wasn't, what happened to the footage/media itself).
   Preserve ambiguity — resist the urge to close every loop.

## Step 3 — Found-footage formatting conventions

- Standard sluglines: `INT./EXT. LOCATION - TIME`.
- Tag the capture medium under the slugline when it matters:
  `(HANDHELD, CASS'S CAMERA)`, `(SCREEN RECORDING / WEBCAM)`,
  `(FOUND ON A SECOND CAMERA, TIMESTAMPED...)`.
- Burn in timestamps when it reinforces the "recovered evidence" conceit.
- Render on-screen digital content (chat logs, decoded ciphers, source
  code) as a labeled **SCREEN INSERT** block, not prose description —
  let the audience read what the characters are reading.
- Use `(O.S.)` for a character heard but not in frame, `(V.O.)` for
  narration/recordings layered over other footage.
- Title cards and text cards go on their own line, in caps, no scene
  heading — they're outside the diegetic footage.

## Step 4 — Cast conventions

- 2–4 person crew mirrors Blair Witch's trio well: give each member a
  distinct function (the host/driver of the investigation, a
  skeptic/technical expert, someone with a personal stake like family of
  the missing person).
- One outside local/witness who confirms the buried history is real —
  this is what turns "spooky story" into "actual place, actual past."
- A cursed or toxic media object (a game, broadcast, book, video series)
  is a strong engine for Act 1 research scenes — it lets exposition happen
  through screen inserts instead of dialogue dumps.

## Step 5 — Escalation toolkit

- Repeating motifs (a sound, a symbol, a phrase) that first appear in the
  fiction/evidence, then recur for real on location.
- Technology mirroring the story being investigated (an in-fiction sound
  effect with no real source; a device behaving like the cursed object
  said it would).
- Physical evidence in a place it shouldn't be (an item locked in a car
  now sitting somewhere impossible).
- Never give a clean explanation for the horror in-script. Ambiguity is
  the payoff, not a placeholder for a cut scene.

## Step 6 — Delivery

- Write the full screenplay to a file (`.txt` or `.fountain`) in the
  project directory, not just as chat output.
- Offer to render it as an Artifact if the user wants an easier read.
- Offer targeted follow-ups (extend an act, convert to strict
  Fountain/PDF formatting, write additional found-footage inserts) rather
  than assuming the first draft is final.

## To expand this skill later

Add sections for other screenplay modes as they come up: traditional
three-act narrative features, sitcom/multi-cam format, stage-play
conventions, non-horror found-footage (mockumentary comedy), or genre
presets (slasher, sci-fi first-contact, etc.). Keep the IP-safety check
(Step 0) genre-agnostic — it applies regardless of what kind of script is
being written.

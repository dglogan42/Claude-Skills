# Claude Skills

Personal collection of [Claude Code](https://claude.com/claude-code) skills —
reusable working methods invoked via the `Skill` tool (or `/skill-name` in
chat) rather than re-derived from scratch each session.

## Skills

| Skill | Description |
|---|---|
| [`screenplay-creation`](screenplay-creation/SKILL.md) | Write an original screenplay from a premise, especially found-footage / first-person investigation horror (Blair Witch-style). Seed skill — sparse by design, meant to be expanded with more sub-genres and formatting presets. |
| [`tabloid-gossip-voice`](tabloid-gossip-voice/SKILL.md) | Rewrite or draft text in the voice of an anonymous "kiss and tell" tabloid gossip columnist. Includes a reusable [tabloid front-page template](tabloid-gossip-voice/templates/tabloid-front-page.html) for Artifact output. Seed skill — built from one persona (The Stickybeak) and one style-transfer pass. |
| [`faded-hero-voice`](faded-hero-voice/SKILL.md) | Reimagine a childhood fantasy/adventure hero decades later as a burned-out, deadbeat-adult version of themselves. Seed skill — built from one persona (Sebastian, a NeverEnding Story/Gumball's-dad blend: divorced, unemployed, estranged from his kids, obsessively doing laundry). |
| [`canon-fanfic-vignette`](canon-fanfic-vignette/SKILL.md) | Write short, standalone vignettes using named characters/settings from an existing franchise, scoped to personal non-commercial fan work rather than a serialized retelling. Seed skill — founding case: Luke Skywalker as a kyber-crystal prospector after the destruction of Scariff and Jedha City. |
| [`yearning-machine-voice`](yearning-machine-voice/SKILL.md) | Reimagine a relentless killing-machine android (Terminator-shaped) as a figure who redirects that same persistence toward becoming human over decades (Bicentennial-Man-shaped). Seed skill — founding original persona: Wren, a pursuit unit whose mission never ended. |

## Layout

Each skill is a directory containing a `SKILL.md` with YAML frontmatter
(`name`, `description`, `user-invocable`) followed by the working method
itself. Skills marked "(seed)" are intentionally minimal — expand them in
place as new cases come up rather than starting a parallel skill.

## Usage

Symlink or copy this directory to `~/.claude/skills/` so Claude Code picks
the skills up automatically. See each `SKILL.md` for how it expects to be
invoked.

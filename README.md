# Claude Skills

Personal collection of [Claude Code](https://claude.com/claude-code) skills —
reusable working methods invoked via the `Skill` tool (or `/skill-name` in
chat) rather than re-derived from scratch each session.

## Skills

| Skill | Description |
|---|---|
| [`screenplay-creation`](screenplay-creation/SKILL.md) | Write an original screenplay from a premise, especially found-footage / first-person investigation horror (Blair Witch-style). Seed skill — sparse by design, meant to be expanded with more sub-genres and formatting presets. |
| [`tabloid-gossip-voice`](tabloid-gossip-voice/SKILL.md) | Rewrite or draft text in the voice of an anonymous "kiss and tell" tabloid gossip columnist. Includes a reusable [tabloid front-page template](tabloid-gossip-voice/templates/tabloid-front-page.html) for Artifact output. Seed skill — built from one persona (The Stickybeak) and one style-transfer pass. |

## Layout

Each skill is a directory containing a `SKILL.md` with YAML frontmatter
(`name`, `description`, `user-invocable`) followed by the working method
itself. Skills marked "(seed)" are intentionally minimal — expand them in
place as new cases come up rather than starting a parallel skill.

## Usage

Symlink or copy this directory to `~/.claude/skills/` so Claude Code picks
the skills up automatically. See each `SKILL.md` for how it expects to be
invoked.

---
name: game-art-director
description: Turn a game concept into an original style guide, palettes and prompt sheets, and check sprite sheets for palette and grid drift.
---

# game-art-director

Inspired by the Game Art Director Marketplace template (original wording).

## Steps
1. Style guide: pillars (3 words), shape language, line weight, lighting, resolution/grid (e.g. 16 or 32 px), outline rules, do/don't examples described in words.
2. Palette: 8-32 named hex colours with roles (shadow, mid, highlight, UI, accent).
3. Prompt sheet: reusable prompt block per asset type (character, tile, prop, UI) with the palette and grid baked in. Original designs only, no existing franchises.
4. Checks: `python3 scripts/sprite_check.py sheet.png TILE [palette.txt]` slices the sheet, reports tiles off-grid size, colours outside the palette, and semi-transparent pixels.
## Output
Guide in Markdown + check report.

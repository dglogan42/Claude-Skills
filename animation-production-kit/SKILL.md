---
name: animation-production-kit
description: "Animation production kit in three modes: frame-by-frame 2D animation in Krita (walk cycles, storyboard to animatic, onion skins, export); stop-motion with Stop Motion Studio or Cloud Stop Motion (capture plan, FPS, green screen); or 3D animation/VFX pipeline in Blender (model, rig, animate, light, render, comp, portfolio, study pathways). Use for any animation workflow request."
---
# animation-production-kit

Pick the mode from the medium. The three source kits shipped an identical `knowledge/media/` folder (verified with diff), so it is kept once at `knowledge/media/` here; mode files that say `knowledge/...` resolve to that shared folder.

## Modes

| Mode | Former skill | Use for | File |
|---|---|---|---|
| `2d-krita` | `animation-dev-kit` | Use when: User wants a frame-by-frame animation workflow, walk cycle, storyboard → animatic → clip plan, onion skins, timeline/layer hygiene, transform-mask motion, or render export with Krita (FOSS raster animation). Triggers: “animate in Krita”, “animation dev kit”, “walk cycle”, “render animation”, “onion skin”, File → Render Animation / FFmpeg. | [modes/2d-krita/MODE.md](modes/2d-krita/MODE.md) |
| `stop-motion` | `stop-motion-dev-kit` | Use when: User wants a stop-motion production kit — capture plan, onion skin, FPS, green screen, export — with Stop Motion Studio (local apps) and/or Cloud Stop Motion (browser / Chromebook / cloud projects). Triggers: “stop motion”, “Chromebook stop motion”, “upload to cloud”, “Cloud Stop Motion”, claymation, LEGO short, classroom animation. | [modes/stop-motion/MODE.md](modes/stop-motion/MODE.md) |
| `3d-vfx` | `3d-animation-dev-kit` | Use when: User wants a 3D animation / VFX production kit — pipeline stages, shot plan, Blender install, modeling→rig→anim→light→render→comp, portfolio clips, or education pathway map for 3D Animation & VFX programmes (e.g. Media Design School). Triggers: “3D animation”, “VFX”, “Blender”, “rig character”, “render farm”, “CG short”, “MDS animation”. | [modes/3d-vfx/MODE.md](modes/3d-vfx/MODE.md) |

## How to run

1. Match the request to one mode; if two fit, say which you assumed.
2. Read that mode's MODE.md fully, plus any references it names (they sit beside it, so its relative links still work).
3. Follow that mode's gates and safety rules exactly; modes do not inherit each other's shortcuts.
4. Evals from each former skill are kept under `modes/<mode>/evals/`.

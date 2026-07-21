# Boba Side art-exploration notes

Reconstructed from `Untitled.html` — a browser export of an SVG/CSS
effects exploration session that lost all whitespace between prompts and
code blocks in the save/paste process (each block ran directly into the
next prompt's label with no separating newline, e.g.
`</script>Add interactivity to panelsHTML<script>`). Split back into its
original prompt/response sequence below; content is unchanged, only
whitespace and structure restored. Kept as reference notes, not a
finished deliverable — see SKILL.md Step 3 for the actual verified
render pipeline.

## 1. Initial sketch — SVG panel generator

```html
<script>
// Simple Boba Side cartoon generator - SVG panels
function generateBobaCartoon(panels) {
  let svg = `<svg width="800" height="600" viewBox="0 0 800 600">`;
  panels.forEach((p,i) => {
    svg += `<rect x="${i*200}" y="0" width="200" height="600" fill="#fff" stroke="#000"/>`;
    svg += `<text x="${i*200+100}" y="300" text-anchor="middle">${p}</text>`;
  });
  svg += `</svg>`;
  return svg;
}
</script>
```

## 2. Add interactivity to panels

```html
<script>
// Interactive Boba Side cartoon
function generateInteractiveBoba(panels) {
  let svg = `<svg width="800" height="600" viewBox="0 0 800 600">`;
  panels.forEach((p,i) => {
    svg += `<g onclick="alert('${p}')">
      <rect x="${i*200}" y="0" width="200" height="600" fill="#fff" stroke="#000" cursor="pointer"/>
      <text x="${i*200+100}" y="300" text-anchor="middle" font-size="14">${p}</text>
    </g>`;
  });
  svg += `</svg>`;
  return svg;
}
</script>
```

## 3. Add CSS hover effects

```html
<style>
  svg g rect { transition: fill 0.2s; }
  svg g:hover rect { fill: #ffeb3b; }
</style>
<script>
// Interactive Boba Side with hover
function generateInteractiveBoba(panels) {
  let svg = `<svg width="800" height="600" viewBox="0 0 800 600">`;
  panels.forEach((p,i) => {
    svg += `<g onclick="alert('${p}')">
      <rect x="${i*200}" y="0" width="200" height="600" fill="#fff" stroke="#000" cursor="pointer"/>
      <text x="${i*200+100}" y="300" text-anchor="middle" font-size="14">${p}</text>
    </g>`;
  });
  svg += `</svg>`;
  return svg;
}
</script>
```

## 4. Explore SVG filter effects for shadows

```html
<svg width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="4" dy="4" result="offsetblur"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.6"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g filter="url(#shadow)">
    <rect x="10" y="10" width="180" height="580" fill="#fff" stroke="#000"/>
    <text x="100" y="300" text-anchor="middle">Panel 1</text>
  </g>
</svg>
```

## 5. Explore drop shadow variations

```html
<svg width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <!-- Soft shadow -->
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6"/>
      <feOffset dx="3" dy="6" result="offset"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Hard shadow -->
    <filter id="hard" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="2"/>
      <feOffset dx="4" dy="4"/>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g filter="url(#soft)"><rect x="50" y="50" width="180" height="180" fill="#fff" stroke="#000"/><text x="140" y="140">Soft</text></g>
  <g filter="url(#hard)"><rect x="300" y="50" width="180" height="180" fill="#fff" stroke="#000"/><text x="390" y="140">Hard</text></g>
</svg>
```

## 6. Learn SVG filter primitives

```html
<svg width="400" height="300">
  <defs>
    <!-- Primitives: blur, offset, flood, composite -->
    <filter id="example" x="0" y="0" width="200%" height="200%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/> <!-- blur -->
      <feOffset dx="4" dy="4" result="offset"/> <!-- drop -->
      <feFlood flood-color="#000" flood-opacity="0.4"/> <!-- color -->
      <feComposite in="offset" in2="SourceGraphic" operator="over"/> <!-- merge -->
    </filter>
  </defs>
  <rect x="50" y="50" width="150" height="100" fill="#fff" stroke="#000" filter="url(#example)"/>
</svg>
```

## 7. Explore feMerge and feComposite operators

```html
<svg width="500" height="300">
  <defs>
    <filter id="merge" width="200%" height="200%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="5" dy="5" result="shadow"/>
      <feFlood flood-color="#000" flood-opacity="0.6" result="flood"/>
      <feComposite in="flood" in2="shadow" operator="in"/> <!-- in -->
      <feMerge>
        <feMergeNode in="shadow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="composite">
      <feOffset dx="3" dy="3" result="offset"/>
      <feComposite in="offset" in2="SourceGraphic" operator="over"/> <!-- over, atop, xor -->
    </filter>
  </defs>
  <g filter="url(#merge)"><rect x="50" y="50" width="150" height="100" fill="#4CAF50" stroke="#000"/></g>
</svg>
```

## 8. Explore SVG filter primitives

```html
<svg width="600" height="400">
  <defs>
    <filter id="primitives">
      <feGaussianBlur stdDeviation="2"/> <!-- blur -->
      <feOffset dx="3" dy="4" result="offset"/> <!-- offset -->
      <feFlood flood-color="#000" flood-opacity="0.5"/> <!-- color -->
      <feComposite in2="offset" operator="in"/> <!-- in/out/atop/xor/arithmetic -->
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect x="50" y="100" width="200" height="150" fill="#fff" stroke="#000" filter="url(#primitives)"/>
</svg>
```

## 9. Add comments to code

```html
<svg width="600" height="400">
  <defs>
    <filter id="primitives">
      <!-- Blur primitive for shadow softness -->
      <feGaussianBlur stdDeviation="2"/>
      <!-- Offset for drop shadow position -->
      <feOffset dx="3" dy="4" result="offset"/>
      <!-- Flood for shadow color/opacity -->
      <feFlood flood-color="#000" flood-opacity="0.5"/>
      <!-- Composite to clip/combine layers -->
      <feComposite in2="offset" operator="in"/>
      <!-- Merge layers: shadow + original graphic -->
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect x="50" y="100" width="200" height="150" fill="#fff" stroke="#000" filter="url(#primitives)"/>
</svg>
```

## 10. Add comments to SVG code

```html
<!-- SVG cartoon panel with drop shadow -->
<svg width="600" height="400" viewBox="0 0 600 400">
  <defs>
    <!-- Define reusable filter for shadows -->
    <filter id="primitives" x="-50%" y="-50%" width="200%" height="200%">
      <!-- Step 1: Blur alpha channel for soft edges -->
      <feGaussianBlur stdDeviation="2"/>
      <!-- Step 2: Shift shadow position -->
      <feOffset dx="3" dy="4" result="offset"/>
      <!-- Step 3: Create colored shadow layer -->
      <feFlood flood-color="#000" flood-opacity="0.5"/>
      <!-- Step 4: Composite to mask shadow shape -->
      <feComposite in2="offset" operator="in"/>
      <!-- Step 5: Merge shadow under original content -->
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Panel with filter applied -->
  <rect x="50" y="100" width="200" height="150" fill="#fff" stroke="#000" filter="url(#primitives)"/>
</svg>
```

## 11. Explore SVG filter primitives

```html
<svg width="400" height="300">
  <defs>
    <filter id="explore">
      <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3"/> <!-- noise -->
      <feDisplacementMap in="SourceGraphic" scale="10"/> <!-- distort -->
      <feGaussianBlur stdDeviation="1"/>
    </filter>
  </defs>
  <rect x="50" y="50" width="200" height="150" fill="#ff9800" filter="url(#explore)"/>
</svg>
```

## 12. Learn about feColorMatrix

```html
<svg width="400" height="300">
  <defs>
    <filter id="matrix">
      <!-- feColorMatrix for hue/saturation/brightness -->
      <feColorMatrix type="matrix" values="
        0.5 0.5 0.5 0 0
        0.5 0.5 0.5 0 0
        0.5 0.5 0.5 0 0
        0 0 0 1 0"/>
    </filter>
  </defs>
  <rect x="50" y="50" width="200" height="150" fill="#4CAF50" filter="url(#matrix)"/>
</svg>
```

## 13. Add descriptive comments to code

```html
<svg width="400" height="300">
  <defs>
    <filter id="matrix">
      <!-- feColorMatrix: transforms RGB channels for color effects like grayscale or sepia -->
      <!-- Values matrix: row1=R, row2=G, row3=B, row4=A, row5=offset -->
      <feColorMatrix type="matrix" values="
        0.33 0.33 0.33 0 0   <!-- Red channel mix -->
        0.33 0.33 0.33 0 0   <!-- Green -->
        0.33 0.33 0.33 0 0   <!-- Blue -->
        0 0 0 1 0"/>         <!-- Alpha unchanged -->
    </filter>
  </defs>
  <!-- Original colored rect with matrix filter applied -->
  <rect x="50" y="50" width="200" height="150" fill="#4CAF50" filter="url(#matrix)"/>
</svg>
```

## 14. CSS backdrop-filter effects

```html
<style>
.panel {
  width: 200px; height: 150px;
  background: rgba(255,255,255,0.8);
  backdrop-filter: blur(8px) brightness(1.1) contrast(1.2); /* CSS backdrop effects */
  border: 1px solid #000;
}
</style>
<div class="panel">Cartoon panel with backdrop blur</div>
```

## 15. Investigate CSS mix-blend-mode

```html
<style>
.blend {
  background: #ffeb3b;
  mix-blend-mode: multiply; /* or screen, overlay, difference */
}
</style>
<div class="blend">Mix blend mode demo</div>
```

## 16. Investigate CSS backdrop-filter property

```html
<style>
.demo {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(12px) saturate(150%) contrast(110%); /* backdrop effects */
  border: 1px solid rgba(0,0,0,0.2);
}
</style>
<div class="demo">Backdrop-filter panel</div>
```

## 17. Write full .html for rendering

```html
<!DOCTYPE html>
<html>
<head>
<title>Boba Cartoon</title>
<style>
body { background: #E9E3D6; font-family: sans-serif; }
.panel { width: 220px; height: 170px; background: white; border: 2px solid #000; display: inline-block; margin: 10px; backdrop-filter: blur(4px); }
</style>
</head>
<body>
<div class="panel">Panel 1 content</div>
</body>
</html>
```

## 18. Include multiple comic panels in layout

```html
<!DOCTYPE html>
<html>
<head>
<title>Boba Side Comic</title>
<style>
  .comic { display: flex; gap: 10px; flex-wrap: wrap; }
  .panel { width: 220px; height: 170px; background: white; border: 2px solid #000; padding: 10px; box-shadow: 4px 4px 0 #000; }
</style>
</head>
<body>
<div class="comic">
  <div class="panel">Panel 1: Setup</div>
  <div class="panel">Panel 2: Action</div>
  <div class="panel">Panel 3: Punchline</div>
</div>
</body>
</html>
```

---
name: hayaku-senkotsu-strip
description: Write and render "Hayaku" — Bubble Tea News's syndicated four-panel (yonkoma) sports-manga strip, an original high-school volleyball series rendered in "senkotsu" style (clean bamboo-like linework, HB under-sketch with 2B-6B-style hatched/crosshatched shading via a manual line-hatch technique, forced perspective via panel composition, high-contrast black-and-white for newsprint) using SkiaSharp (MIT-licensed, cross-platform) from PowerShell as the renderer — schematic panel compositions in the same simple register as the-boba-side-cartoon's pycairo art, not full character illustration. Runs as an unrelated syndicated strip alongside the paper's own bubble tea content, the way a real newspaper carries Garfield or Peanuts. Use when assembling a Bubble Tea News issue that wants a syndicated comic-strip slot, or whenever the user wants a Hayaku strip written up and rendered. This is a seed skill: sparse by design, built from one house style brief (senkotsu.YAML) and one render method; expand with a running cast, match/season arc, and richer figure primitives as strips accumulate.
user-invocable: true
---

# Hayaku (seed)

A working method for **Hayaku**, *Bubble Tea News*'s syndicated
four-panel sports-manga strip — a high-school volleyball series, deliberately
unrelated to bubble tea, running the way a real community paper carries a
licensed strip like *Garfield* or *Peanuts* alongside its own local content.
Written per the **senkotsu** house art-direction brief and rendered with
**SkiaSharp** from PowerShell (schematic panel compositions, not polished
manga illustration — see Step 3). Treat this as a starting checklist, not a
rigid template.

## Step 0 — Genre safety check (do this before writing anything)

- **Hayaku is an original, in-house title and cast** — not a claim to be, a
  parody of, or a reproduction of any specific real manga/anime. School
  volleyball is a well-populated real genre with at least one very famous,
  actively-licensed series covering near-identical ground; keep Hayaku's
  characters, team/school names, rivalries, and specific plot beats
  original. The target is genre pastiche — underdog-team energy, dramatic
  action beats, the yonkoma sports-manga *feel* — not a retelling or
  reskinning of somebody else's actual IP. If a strip idea starts to
  converge on a specific real series' signature scene or character, change
  it before writing.
- **Rendered art stays schematic, not an attempt at real manga
  draftsmanship** — simple geometric figures and panel composition, the
  same "simple, clean, not a claim to skilled illustration" register this
  library's `the-boba-side-cartoon` uses with pycairo. A polished attempt
  would drift toward reproducing a real series' actual visual style,
  which is exactly what Step 0's first bullet rules out.

## Step 1 — The senkotsu house style

Write each panel's scene description so it can actually be rendered (Step
3) *and* so it reads correctly even before rendering:

- Clean, bamboo-like linework — simple, confident, bold strokes, as if
  inked with a heavier pencil (2B–6B) over a lighter HB under-sketch.
- No smooth/painterly shading — texture comes from **hatching and
  crosshatching**, giving a hand-pulled, traditional print feel.
- **Forced perspective and foreshortening** on action beats — dramatic,
  low or tilted angles, not flat side-on views. (Rendered via panel
  composition and scale, not true perspective-correct figure distortion
  — see Step 3.)
- Call out the **lighting** per panel: natural/outdoor (harsh midday,
  long late-afternoon shadow) vs. artificial/indoor (flat gymnasium
  fluorescent) — expressed through hatch density (heavier crosshatch =
  shadow side, sparse single-direction hatch = lit side), not greyscale.
- **High-contrast black-and-white**, suited to cheap newsprint
  reproduction — think in blacks and whites, not greys.
- **Exaggerated, legible expressions and body language** — a single frozen
  frame should still read the emotional beat. This is a strip about
  *movement and stakes*.
- Keep characters in believable human proportions even when expressions
  are exaggerated — no chibi/super-deformed style shifts.
- Frame each panel with a clear internal border/grid so the strip's own
  four-panel block absorbs any layout overflow rather than bleeding into
  the surrounding newspaper page.

## Step 2 — Format

Exactly **four panels** (*yonkoma* — "yon" four, "koma" panel/frame —
laid out vertically or as a 2×2 grid — writer's choice). For each panel
give:

1. **Panel number and framing** (e.g. "Panel 1 — wide, outdoor, forced low
   angle").
2. **Scene description** (1–2 sentences): who's on court, the action, the
   lighting call.
3. **Dialogue/caption line(s)**, if any — these strips often run mostly
   silent action beats punctuated by a single shout or thought.

The fourth panel is usually the payoff (a spike landing, a whistle, a
reaction shot), following yonkoma's typical setup–development–twist–payoff
(*ki-shou-ten-ketsu*) rhythm rather than a single-panel gag's punchline.

Example shape (illustrative, not to be reused verbatim):

> **Panel 1** — wide, outdoor practice court, late-afternoon side light
> raking long shadows across the paint. A libero crouches low, weight
> forward.
> *"Rotation's wrong again — call it!"*
>
> **Panel 2** — tight on the setter's hands mid-release, crosshatched
> motion lines trailing the ball.
>
> **Panel 3** — forced-perspective low angle on the spiker rising; indoor
> gym light this time, ball foreshortened huge in frame.
>
> **Panel 4** — wide reaction shot, ball buried on the far side of the
> net, the whole bench half-risen off it.
> *"...Okay. Now call it."*

## Step 3 — Render with SkiaSharp (PowerShell)

**SkiaSharp** is the renderer for this slot — MIT-licensed, genuinely
cross-platform (bundles its own native binaries per OS, no `libgdiplus`
system dependency), same rendering engine as Chrome/Android/Flutter. It
produces schematic panel compositions (figures, panel grid, hatching,
motion lines), not full manga illustration.

**Why SkiaSharp and not `System.Drawing`/GDI+ or `SixLabors.ImageSharp`:**
GDI+ works fine on Windows but needs `libgdiplus` installed plus an
explicit `[AppContext]::SetSwitch('System.Drawing.EnableUnixSupport',
$true)` opt-in on Linux/macOS — untested in this project. ImageSharp was
tried first but `SixLabors.ImageSharp.Drawing` (pulling in ImageSharp
4.0.0) now hard-fails the build without a paid Six Labors license key
(`error: No Six Labors license found` — confirmed by actually trying to
build with it) — ruled out for a project without a commercial license.

**One-time setup per machine** (`Install-Package`/`PackageManagement` was
tried and is unreliable — it hung indefinitely in testing rather than
installing or failing cleanly). A throwaway `dotnet` project reliably
populates the NuGet cache instead:

```powershell
dotnet new console -o _skia-bootstrap -n Bootstrap
cd _skia-bootstrap; dotnet add package SkiaSharp; cd ..
Remove-Item -Recurse -Force _skia-bootstrap
```

After that, `SkiaSharp.dll` and the native `libSkiaSharp` asset sit in
`~/.nuget/packages` and the render script below finds them dynamically —
no hardcoded version number, so it survives a package upgrade.

**The render script** (verified working end to end — the crosshatch/lit
panels and schematic figure below are a real tested render, not a
sketch):

```powershell
$NugetRoot = Join-Path $env:USERPROFILE ".nuget\packages"

# Filter on \lib\ specifically, not just the TFM folder name — a naive
# match on "netstandard2.0" can also catch a \ref\ (reference-only, no IL
# body) assembly of the same name, which throws "Reference assemblies
# cannot be loaded for execution" at Add-Type. Confirmed by hitting this
# exact bug once already.
$ManagedDll = Get-ChildItem -Path (Join-Path $NugetRoot "skiasharp") -Recurse -Filter "SkiaSharp.dll" |
    Where-Object { $_.FullName -match '\\lib\\netstandard2\.0\\' } |
    Select-Object -First 1
Add-Type -Path $ManagedDll.FullName

# Native asset package name differs by OS; only win32 is verified so far.
$NativePkg = if ($IsWindows -or $null -eq $IsWindows) { "skiasharp.nativeassets.win32" }
             elseif ($IsMacOS) { "skiasharp.nativeassets.macos" }
             else { "skiasharp.nativeassets.linux" }  # unverified in this project
$NativeDir = Get-ChildItem -Path (Join-Path $NugetRoot $NativePkg) -Recurse -Filter "libSkiaSharp.*" |
    Where-Object { $_.FullName -match "win-x64|osx|linux-x64" } |
    Select-Object -First 1 -ExpandProperty DirectoryName
$env:PATH = "$NativeDir;$env:PATH"

[int] $W = 900; [int] $H = 900
$surface = [SkiaSharp.SKSurface]::Create([SkiaSharp.SKImageInfo]::new($W, $H))
$canvas = $surface.Canvas
$canvas.Clear([SkiaSharp.SKColors]::White)

$borderPaint = [SkiaSharp.SKPaint]::new()
$borderPaint.Color = [SkiaSharp.SKColors]::Black
$borderPaint.StrokeWidth = 8
$borderPaint.IsStroke = $true
$borderPaint.StrokeJoin = [SkiaSharp.SKStrokeJoin]::Round
$borderPaint.StrokeCap = [SkiaSharp.SKStrokeCap]::Round
$borderPaint.IsAntialias = $true
$canvas.DrawRect([SkiaSharp.SKRect]::new(20, 20, $W - 20, $H - 20), $borderPaint)

function Draw-Hatch {
    param($Canvas, [SkiaSharp.SKRect]$Rect, [bool]$Cross, [float]$Spacing = 10)
    $paint = [SkiaSharp.SKPaint]::new()
    $paint.Color = [SkiaSharp.SKColors]::Black
    $paint.StrokeWidth = 2
    $paint.IsAntialias = $true
    $Canvas.Save() | Out-Null
    $Canvas.ClipRect($Rect)
    # Each line spans the rect's full height so it actually crosses the
    # clip region, and x starts one height to the left so the "\" family's
    # tail still sweeps in from outside — a naive version of this (lines
    # anchored at the rect corners using width+height as a step) only
    # barely grazed the clip area and rendered near-empty. Verified fix.
    $ht = $Rect.Height
    for ($x = $Rect.Left - $ht; $x -lt $Rect.Right; $x += $Spacing) {
        $Canvas.DrawLine($x, $Rect.Top, $x + $ht, $Rect.Bottom, $paint)
        if ($Cross) { $Canvas.DrawLine($x, $Rect.Bottom, $x + $ht, $Rect.Top, $paint) }
    }
    $Canvas.Restore()
}

# Shadow side: crosshatch. Lit side: sparse single-direction hatch.
Draw-Hatch -Canvas $canvas -Rect ([SkiaSharp.SKRect]::new(60, 60, 360, 360)) -Cross $true -Spacing 8
Draw-Hatch -Canvas $canvas -Rect ([SkiaSharp.SKRect]::new(400, 60, 700, 360)) -Cross $false -Spacing 14

# Schematic figure: geometric primitives only, not attempted illustration
$figurePaint = [SkiaSharp.SKPaint]::new()
$figurePaint.Color = [SkiaSharp.SKColors]::Black
$figurePaint.StrokeWidth = 6
$figurePaint.IsStroke = $true
$figurePaint.StrokeJoin = [SkiaSharp.SKStrokeJoin]::Round
$figurePaint.StrokeCap = [SkiaSharp.SKStrokeCap]::Round
$figurePaint.IsAntialias = $true
$canvas.DrawOval([SkiaSharp.SKRect]::new(380, 420, 480, 520), $figurePaint)  # head
$canvas.DrawLine(430, 520, 430, 680, $figurePaint)  # spine
$canvas.DrawLine(430, 560, 340, 620, $figurePaint)  # left arm
$canvas.DrawLine(430, 560, 520, 500, $figurePaint)  # right arm raised
$canvas.DrawLine(430, 680, 370, 800, $figurePaint)  # left leg
$canvas.DrawLine(430, 680, 490, 800, $figurePaint)  # right leg

# Motion lines trailing a moving element (the ball)
$motionPaint = [SkiaSharp.SKPaint]::new()
$motionPaint.Color = [SkiaSharp.SKColors]::Black
$motionPaint.StrokeWidth = 3
$motionPaint.IsAntialias = $true
for ($i = 0; $i -lt 5; $i++) {
    $y = 470 + ($i * 12)
    $canvas.DrawLine(540, $y, 620, $y - 20, $motionPaint)
}
$ballPaint = [SkiaSharp.SKPaint]::new()
$ballPaint.Color = [SkiaSharp.SKColors]::Black
$ballPaint.IsAntialias = $true
$canvas.DrawOval([SkiaSharp.SKRect]::new(600, 440, 624, 464), $ballPaint)

$image = $surface.Snapshot()
$data = $image.Encode([SkiaSharp.SKEncodedImageFormat]::Png, 100)
$stream = [System.IO.File]::OpenWrite("<output-path>.png")
$data.SaveTo($stream)
$stream.Close()
```

Build up a real strip by repeating this per panel (own `SKSurface` per
panel, or one large surface with four sub-rects) with scene-specific
figure poses, hatch placement per the lighting call, and motion lines
where the action needs them.

**Forced perspective:** don't attempt true perspective-correct figure
distortion — simulate the *effect* through panel composition instead
(off-center/tilted panel crop, exaggerated scale gap between foreground
and background elements), consistent with Step 0's schematic boundary.

Save as PNG and embed via `<img>` in the issue HTML (SkiaSharp can also
encode SVG via `SKSVGCanvas`, unexplored in this project so far — PNG is
the verified path). Check the render at the actual size it'll appear in
the issue (not a full-screen preview) before calling a panel done — the
same "flat block/pattern doesn't read at real print size" failure mode
documented in `the-boba-side-cartoon` applies here too, for a hatch
pattern that's too sparse or too dense once shrunk.

## Step 4 — Delivery

- Within a *Bubble Tea News* issue: an optional rotating slot alongside,
  not replacing, The Boba Side — the two can coexist as separate strips,
  the way a real paper runs more than one. Treat Hayaku as **serialized**:
  note roughly where each strip lands in an ongoing match/season arc so a
  later issue can continue the story rather than restart it.
- Show the rendered PNG actually rendered (inline `<img>` in the issue,
  or an Artifact/file delivery for a standalone request) — not just the
  panel-by-panel prose.
- If a quick text-only placeholder is genuinely all that's needed (e.g.
  drafting an issue's copy before art passes are done), the panel
  description + dialogue from Step 2 is a fine placeholder — but treat
  the rendered PNG as the actual deliverable for this slot, not the
  description, mirroring `the-boba-side-cartoon`'s convention.
- As a standalone piece: chat text (with the rendered image) is fine for
  a single strip.

## Step 5 — Optional strip-index dashboard (PSWriteHTML)

`PSWriteHTML` still isn't the art renderer — checked against the
installed v1.41.0: its ~200 cmdlets cover tables, ApexCharts, vis.js
diagrams, calendars, QR codes, etc.; there is no shape/line/canvas-drawing
surface (a `New-HTMLCanvas` cmdlet does *not* exist in this module — a
snippet assuming it does will fail with `term not recognized`). What it's
actually useful for is a continuity dashboard: a table plus timeline of
strips run so far, so a later issue can pick the match/season arc back up
correctly.

```powershell
Import-Module PSWriteHTML
$StripLog = @(
    [PSCustomObject]@{ Issue = 9; Title = "Rotation Call"; ArcBeat = "Regional prelims, game 1" }
    [PSCustomObject]@{ Issue = 8; Title = "Second Serve";  ArcBeat = "Regional prelims, warmup" }
)
New-HTML -Title "Hayaku — Strip Index" -FilePath "hayaku-index.html" -ShowHTML {
    New-HTMLSection -HeaderText "Strips run so far" {
        New-HTMLTable -DataTable $StripLog
    }
    New-HTMLTimeline {
        foreach ($s in $StripLog) {
            New-HTMLTimelineItem -HeadingText $s.Title -Text $s.ArcBeat
        }
    }
}
```

Note `New-HTMLTimelineItem` takes `-HeadingText`, not `-Title` — verify
current parameter names with `Get-Command <name> -Syntax` before reuse,
since a plausible-looking guess (`-Title`) fails silently into a warning
rather than a hard error. This dashboard is a bookkeeping aid for
tracking the arc across issues, not part of the delivered strip.

## To expand this skill later

Add a running cast list and a match/season arc tracker as strips
accumulate, so continuity holds issue to issue — mirroring how
`bubble-tea-news-editor` tracks its own rotation log. The Step 5
dashboard above is a starting point for that tracker. Build a small
reusable library of SkiaSharp figure/prop primitives (a stock pose, a
ball, a net) so renders don't reinvent the same shapes each time,
mirroring `the-boba-side-cartoon`'s pycairo-primitives goal. Verify the
Linux/macOS native-asset path for real on an actual non-Windows machine
before relying on the cross-platform claim — only Windows has been
tested in this project so far.

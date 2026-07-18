# Claude Skills

Personal collection of [Claude Code](https://claude.com/claude-code) skills —
reusable working methods invoked via the `Skill` tool (or `/skill-name` in
chat) rather than re-derived from scratch each session.

## Skills

| Skill | Description |
|---|---|
| [`screenplay-creation`](screenplay-creation/SKILL.md) | Write an original screenplay from a premise, especially found-footage / first-person investigation horror (Blair Witch-style). Seed skill — sparse by design, meant to be expanded with more sub-genres and formatting presets. |
| [`promo-shoot-brief`](promo-shoot-brief/SKILL.md) | Turn a movement sequence (yoga routine, dance warm-up, choreography notes) into a generic photo/video shoot brief with a shot list — framing, lighting, direction, hold times. Not persona-voiced; a straight creative-brief utility. |
| [`tabloid-gossip-voice`](tabloid-gossip-voice/SKILL.md) | Rewrite or draft text in the voice of an anonymous "kiss and tell" tabloid gossip columnist. Includes a reusable [tabloid front-page template](tabloid-gossip-voice/templates/tabloid-front-page.html) for Artifact output. Seed skill — built from one persona (The Stickybeak) and one style-transfer pass. |
| [`faded-hero-voice`](faded-hero-voice/SKILL.md) | Reimagine a childhood fantasy/adventure hero decades later as a burned-out, deadbeat-adult version of themselves. Seed skill — built from one persona (Sebastian, a NeverEnding Story/Gumball's-dad blend: divorced, unemployed, estranged from his kids, obsessively doing laundry). |
| [`canon-fanfic-vignette`](canon-fanfic-vignette/SKILL.md) | Write short, standalone vignettes/journals/columns/essays using named characters from an existing franchise, scoped to personal non-commercial fan work rather than a serialized retelling. Seed skill — five personas: Luke Skywalker (kyber prospector), Shaggy & Scooby (forced-vacation mystery log), Garfield (food critic), Alan Grant (sanctuary zookeeper essayist), Daffy Duck (book critic). |
| [`code-theft-dossier`](code-theft-dossier/SKILL.md) | Investigate whether a website's HTML/CSS/JS looks copied from another site and write the findings as a legal-thriller case file, narrated by an original Mitch-McDeere-shaped legal-affairs journalist persona. Seed skill — pairs real investigative method (fingerprint matching, Wayback Machine timeline checks) with accuracy/defamation guardrails since the subject is usually a real site. |
| [`seekers-eye-shopper`](seekers-eye-shopper/SKILL.md) | Recommend fashion finds on AliExpress (or similar marketplaces), narrated by an original personal-shopper persona in the shape of Cho Chang (Harry Potter) — a Seeker's eye for the one real listing among decoys. Seed skill — pairs the persona with real-product accuracy guardrails (no fabricated links/prices, counterfeit flagging). |
| [`lifeguards-eye-sportswriter`](lifeguards-eye-sportswriter/SKILL.md) | Write sports journalism/commentary narrated by an original persona in the shape of C.J. Parker (Baywatch) — an ex-lifeguard's trained eye for reading a match before the obvious storyline breaks. Seed skill — pairs the persona with real-sports accuracy guardrails (no fabricated scores/quotes). |
| [`master-of-the-universe-columnist`](master-of-the-universe-columnist/SKILL.md) | Write financial commentary narrated by an original persona in the shape of Sherman McCoy (The Bonfire of the Vanities) — a 1980s Wall Street trader who believes his own "Master of the Universe" myth, with the fragility leaking through underneath. Seed skill — pairs the persona with real-market accuracy and an explicit not-investment-advice boundary. |
| [`the-world-bulletin-anchor`](the-world-bulletin-anchor/SKILL.md) | Write comedic field-news dispatches from an original, injury-prone world-affairs anchor (Baxter Kline) whose hard-news reports dissolve into escalating on-camera disaster, delivered with unbroken deadpan composure. Seed skill — original persona/catchphrase, deliberately avoiding the trademarked chaos-news format it riffs on. |
| [`grand-prix-showroom-ads`](grand-prix-showroom-ads/SKILL.md) | Write cheesy local-newspaper car-dealer ad copy narrated in Lewis Hamilton's voice, applying F1 hyperbole to used-car-lot sales tactics. Seed skill — since this uses a real living person's identity, built around clearly-labeled parody with invented dealerships only, never a real-endorsement implication. |
| [`epic-forecast-anchor`](epic-forecast-anchor/SKILL.md) | Write local TV weather segments narrated by an original presenter, Dana Foley, who narrates any forecast (however mundane) with nature-documentary-trailer stakes, while the meteorology underneath stays accurate. Seed skill — clinical-readout/epic-narration pairing as the core comic device. |
| [`ken-endo-puzzle-master`](ken-endo-puzzle-master/SKILL.md) | Solve or create Mensa-level logic puzzles/riddles, narrated by an original puzzlesmith persona, Ken Endo. Seed skill — pairs the voice with real puzzle-integrity discipline (verify a unique, deducible solution before presenting; be honest about flawed puzzles). |
| [`te-mana-whakaatu-classifieds`](te-mana-whakaatu-classifieds/SKILL.md) | Write newspaper classifieds where every mundane ad gets an official-style content rating/descriptor in the format of Te Mana Whakaatu (NZ's real Classification Office). Seed skill — since this borrows a real government body's format, built around clearly-labeled parody with invented ads only and a non-affiliation disclaimer. |
| [`silent-majority-dispatch`](silent-majority-dispatch/SKILL.md) | Write political commentary narrated in Richard Nixon's voice, grounded in his real documented psychology (embattled, press-distrustful, Cold-War framing, genuinely shrewd on foreign policy underneath the paranoia). Seed skill — historical-accuracy discipline plus a non-partisan guardrail since the subject is politics and a real (deceased) public figure. |
| [`champagne-wishes-dispatch`](champagne-wishes-dispatch/SKILL.md) | Write breathless luxury-lifestyle dispatches narrated in Robin Leach's voice ("champagne wishes and caviar dreams"), touring an invented estate with sincere, uncritical delight. Seed skill — biographical accuracy for Leach himself, invented subjects only (no real living people's real homes/finances), plus an optional mismatch format applying the same awe to somewhere modest. |
| [`reality-distortion-field-report`](reality-distortion-field-report/SKILL.md) | Write tech-product dispatches narrated in Steve Jobs's voice, applying his real "reality distortion field" showmanship to over-hype a feature regardless of how minor it is. Seed skill — biographical accuracy for Jobs, non-affiliation with real Apple Inc., and real-product accuracy (facts stay true, only the hype layer is exaggerated). |
| [`ridgeline-weekly-correspondent`](ridgeline-weekly-correspondent/SKILL.md) | Write rural community-newspaper dispatches from an original "local yokel" agricultural correspondent, Clem Whitlock (sheep dagging, shearing tallies, milk solids yield, pasture cover), covered with genuine expertise and front-page gravity. Seed skill — affectionate, not-condescending tone discipline; recurring small-town rivalry cast. |
| [`long-game-music-review`](long-game-music-review/SKILL.md) | Write music reviews narrated in Rebecca Black's voice, grounded in her real adult perspective on surviving viral judgment and reclaiming her artistic identity — deliberately not the "ironic bad music" mockery dynamic that once targeted her. Seed skill — empathetic-but-sharp criticism: generous to sincerity, unforgiving of cynical/manufactured product. |
| [`community-outbreak-bulletin`](community-outbreak-bulletin/SKILL.md) | Write a satirical situation-report bulletin in WHO Health Emergencies reporting's real structural format, applied to a trivial non-medical community fad (lawn gnomes, friendship bracelets). Seed skill — strict non-health/non-affiliation boundary given the real institution satirized is a highly authoritative global health body. |
| [`yearning-machine-voice`](yearning-machine-voice/SKILL.md) | Reimagine a relentless killing-machine android (Terminator-shaped) as a figure who redirects that same persistence toward becoming human over decades (Bicentennial-Man-shaped). Seed skill — founding original persona: Wren, a pursuit unit whose mission never ended. |
| [`pearl-index-market-researcher`](pearl-index-market-researcher/SKILL.md) | Write consumer-insights market-research reports on bubble tea patron behavior, narrated by an original persona, Priya Anand, founder of a boutique research firm (The Pearl Index) who applies real pollster rigor — sample sizes, margin of error, cross-tabs, named patron segments — to sweetness-level loyalty and pearl-to-milk ratios. Also produces matching ad-box creative as SVG files sold off the same research. Seed skill — one persona, one report format, two SVG ad examples. |
| [`kate-rodgers-film-review`](kate-rodgers-film-review/SKILL.md) | Write film reviews narrated by an original persona, Kate Rodgers, a former multiplex concessions/usher turned critic who scores every review on an inverted "Refill Rating" — more popcorn refills during a screening means a worse movie; zero refills is her highest praise. Seed skill — one persona, one rating device. |
| [`design-desk-dispatch`](design-desk-dispatch/SKILL.md) | Write "Design Desk," a Bubble Tea News column narrated by Freya Wilcox, the paper's own Design Editor, who adopted a cat through a new relationship with an animal-shelter volunteer and has since become fixated on correlating cat ownership with bubble tea sales — real-sounding methodology, zero rigor about causation, and a habit of letting the "data" visibly bleed into the paper's own layout. Seed skill — one persona, one running bit. |
| [`the-boba-side-cartoon`](the-boba-side-cartoon/SKILL.md) | Write "The Boba Side," Bubble Tea News's single-panel gag cartoon slot, as a clearly-labeled parody/homage to Gary Larson's absurdist one-panel style (real, living cartoonist) applied to bubble tea premises — a scene description plus caption in place of actual artwork, since there's no image-generation tool available and reproducing his specific illustration style would be a separate risk. Seed skill — one format, careful real-person/parody boundary. |
| [`menace-watch-editorial`](menace-watch-editorial/SKILL.md) | Write "Menace Watch," the Bubble Tea News standing editorial column, narrated by editor-in-chief Gordon Slate (a J. Jonah Jameson-shaped persona) who is instantly, sincerely convinced any masked/costumed local figure is a dangerous vigilante menace — always harmless, never once caught by Gordon. Runs monthly (not weekly) within the paper. Seed skill — one persona, one column format. |
| [`bubble-tea-news-editor`](bubble-tea-news-editor/SKILL.md) | Assemble a genuinely new weekly issue of the Bubble Tea News print edition by rotating personas from across this library (tracked in a rotation log so issues don't repeat), generating fresh content per persona rather than reusing existing examples. Use to produce "this week's issue." |

## Showcase

The actual Bubble Tea News print edition, issue archive, and website build
moved out of this repo into
[`dglogan42/bubble-tea-news`](https://github.com/dglogan42/bubble-tea-news)
(full commit history preserved via `git filter-repo`), so that the skills
library and the published product it feeds can be versioned and released
independently. `bubble-tea-news-editor` (and any persona skill contributing
content to an issue) now assumes that repo is checked out as a sibling
directory — see that skill's Step 0 for the exact layout it expects.

## Live site (GitHub Pages)

The live site now deploys from `dglogan42/bubble-tea-news`'s own `docs/`
folder, with the `bubbletea.nz` custom domain and DNS records pointed
there. This repo's `docs/` folder is kept only as a redirect stub, in case
anything still links to the old GitHub Pages default URL
(`dglogan42.github.io/Claude-Skills`) — it forwards to bubbletea.nz.

## Layout

Each skill is a directory containing a `SKILL.md` with YAML frontmatter
(`name`, `description`, `user-invocable`) followed by the working method
itself. Skills marked "(seed)" are intentionally minimal — expand them in
place as new cases come up rather than starting a parallel skill.

## Usage

Symlink or copy this directory to `~/.claude/skills/` so Claude Code picks
the skills up automatically. See each `SKILL.md` for how it expects to be
invoked.

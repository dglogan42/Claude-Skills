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
| [`canon-fanfic-vignette`](canon-fanfic-vignette/SKILL.md) | Write short, standalone vignettes/journals/columns/essays using named characters from an existing franchise, scoped to personal non-commercial fan work rather than a serialized retelling. Seed skill — four personas: Luke Skywalker (kyber prospector), Shaggy & Scooby (forced-vacation mystery log), Garfield (food critic), Alan Grant (sanctuary zookeeper essayist). |
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
| [`the-world-bulletin-anchor`](the-world-bulletin-anchor/SKILL.md) | Write comedic field-news dispatches from an original, injury-prone world-affairs anchor (Baxter Kline) whose hard-news reports dissolve into escalating on-camera disaster, delivered with unbroken deadpan composure. Seed skill — original persona/catchphrase, deliberately avoiding the trademarked chaos-news format it riffs on. |
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

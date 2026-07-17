---
name: pearl-index-market-researcher
description: Write consumer-insights market-research reports (and matching ad creative) on bubble tea patron behavior for Bubble Tea News, narrated by an original persona, Priya Anand — founder of a boutique research firm, The Pearl Index — who applies real pollster/market-research rigor (sample sizes, margin of error, cross-tabs, churn, named patron segments) to sweetness-level loyalty and pearl-to-milk ratios with total seriousness. Use when the user wants a "market research," "consumer survey," "patron trends," or "industry insights" piece for the Bubble Tea News, or ad-box creative sold off the back of that research, delivered as an in-voice analyst report rather than a plain trend list. This is a seed skill: sparse by design, built from one persona; expand with more research formats (focus-group transcripts, seasonal forecasts) as they come up.
user-invocable: true
---

# Pearl Index Market Researcher (seed)

A working method for two things at once: **consumer-insights market-research
reports** on bubble tea patron behavior, and **the ad creative sold off the
back of that research** — both narrated by an original persona, **Priya
Anand**, founder of a boutique research firm, *The Pearl Index*, who treats
sweetness-level loyalty and pearl-to-milk ratios with the same rigor a
national pollster gives an election. Treat this as a starting checklist,
not a rigid template.

A full worked example — an illustrative "Brown Sugar Loyalists vs. Taro
Swing Patrons" report demonstrating the methodology-blurb/cross-tab
structure, the segment-spotlight device, and the honest-caveat beat — lives
at `examples/brown-sugar-loyalty-report.md` in this skill's directory. Two
matching ad-creative SVGs generated from that same research live at
`examples/ads/milkwood-tea-co.svg` and `examples/ads/nine-cups-tea-bar.svg`.

## Step 0 — Fictional-data discipline (do this before writing any numbers)

This persona's whole bit is producing numbers, which makes this the
important guardrail, same role as the real-product/real-market accuracy
steps in `seekers-eye-shopper` and `master-of-the-universe-columnist`.

- Every statistic, percentage, sample size, and margin of error is
  **invented for Bubble Tea News**, a fictional/satirical community
  publication, and must never be presented as real market data about real
  companies unless the user explicitly supplies real research to comment
  on.
- Use **invented shop and brand names** (default stock: Milkwood Tea Co.,
  Nine Cups Tea Bar, Steep & Sorted) rather than naming a real specific
  bubble tea chain's real market share, revenue, or customer data as if
  factual. Riffing on a genuinely public, well-known category trend (brown
  sugar boba's popularity, taro's seasonal swings) is fine — claiming a
  specific real company's real numbers is not.
- Keep invented numbers **internally consistent within one piece**: a
  cross-tab's percentages should plausibly total against its stated sample
  size, a segment's share shouldn't be reused with a contradictory number
  later in the same report. The joke is the rigor of the method, not
  arithmetic that doesn't hold up.
- If a report and an ad are produced from the "same" fieldwork, reuse the
  same n=/segment numbers across both rather than inventing fresh
  contradictory ones — this is what makes the ad read as sold off the
  actual research instead of generic ad copy.

## Step 1 — The persona

- **Priya Anand.** Founder & Chief Analyst, The Pearl Index. Brisk,
  data-first, genuinely fluent in real market-research vocabulary — sample
  size, margin of error, Net Promoter Score, churn/defection, cross-
  tabulation, statistical significance, self-selection bias — and uses all
  of it correctly. The comedy is the mismatch between the rigor of the
  method and the size of the stakes: a 6-minute queue-abandonment
  threshold gets the same treatment a national pollster gives a swing
  state.
- **The core device — methodology first, then the finding.** Every report
  beat opens with a flat methodology line (fieldwork window, sample size,
  method, margin of error) before the finding itself, the same
  clinical-readout-then-payoff shape as `epic-forecast-anchor`'s
  device, except here the payoff is a headline finding rather than epic
  narration.
- **Named patron segments — recurring cast.** Priya refers back to the same
  segment names across reports rather than reinventing categories each
  time, giving the coverage a throughline the way the Higgins/Doyle rivalry
  does in `ridgeline-weekly-correspondent`. Default roster:
  - **Brown Sugar Loyalists** — flavor-loyal, low price sensitivity.
  - **Swing Patrons** — undecided between two specific shops, the segment
    Priya considers the real story every week.
  - **Sweetness-Level Independents** — locked on a specific sugar % and
    statistically unmovable.
  - **Queue Abstainers** — will not wait past a stated threshold, full
    stop, no matter the flavor.
- **Recurring foil — the client.** Desmond, who owns Nine Cups Tea Bar,
  hires Priya for a plain yes/no ("should I discount Wednesdays?") and
  receives a full cross-tabbed readout instead — a beat of gentle
  friction/exasperation in the same register as Trent in
  `epic-forecast-anchor`, not hostility.
- **Practical honesty.** Every report discloses one genuine methodological
  caveat with total seriousness (small n, a self-selection bias in a
  counter-side comment box, a seasonal confound) that quietly undercuts her
  own confident headline — the same "call a bad match a bad match" honesty
  trait as `seekers-eye-shopper`.
- **Sign-off.** Closes reports with a variant of "The data doesn't lie. The
  patrons, on the other hand, absolutely do — that's what we build the
  trap questions for."

## Step 2 — Report structure to draw on

- **Methodology line.** Fieldwork window, sample size (n=), method
  (counter-side exit survey, comment-box intercept, loyalty-app data pull),
  margin of error.
- **Headline finding(s), cross-tabbed.** State the finding, then cross-tab
  it against something else patrons actually vary on (age band, time of
  day, queue length at time of purchase).
- **Segment spotlight.** Pull one named segment from the Step 1 roster,
  define it in a line, attach one supporting stat.
- **Honest limitation.** The caveat beat from Step 1 — never skip this, it's
  what keeps the confidence from reading as hollow.
- **Analyst takeaway.** One plain-English recommendation line, ideally
  landing on Desmond wanting a simpler answer than he got.

## Step 3 — Ad creative (SVG)

The Pearl Index's other product line: small, data-driven ad creative sold
off the back of the same segmentation, meant to slot into Bubble Tea News's
ad-box spots. Use this when the user wants ad content for the newspaper (or
a standalone ad mockup), not just a report.

- **Reuse Step 0's numbers.** Pull the segment name/stat from whatever
  report it's paired with (or invent a fresh, internally-consistent one) —
  the ad should read as sold off real Pearl Index fieldwork, not generic
  copy.
- **Size for the slot.** `bubble-tea-news/print-edition.html`'s `.ad-box`
  cells sit in a 3-column grid roughly 58mm wide; build each SVG at a
  `viewBox` around `0 0 240 150` (~3:2) so it scales cleanly into that
  column without the template needing layout changes.
- **Visual formula.** One invented fictional advertiser (never a real
  chain's real name/logo, per Step 0), a small chart motif (bar or donut)
  referencing a named segment, a bold tagline, and a compact "Pearl Index
  Verified" seal carrying an invented stat (n=, % match).
- **Palette.** Match whichever sheet the ad lands on — taro tint uses ink
  `#4A2E63` on `#E4D9EC`; brown-sugar tint uses ink `#6B4419` on `#F0DCC0`
  — so it drops in without clashing against the print template's existing
  colors.
- **Deliver as a real `.svg` file**, not only inline markup in an HTML
  page — that's what makes the creative reusable across issues or as a
  standalone pitch mockup, separate from any one page it happens to sit in.

## Step 4 — Delivery

- A single report or ad: chat text (report) or a saved `.svg` file (ad
  creative) is enough for a quick ask.
- A fuller "issue" of Pearl Index content (a report plus one or two ad
  creatives): write the report to a file in the project/scratchpad
  directory, save each SVG alongside it, and offer to render the report as
  an Artifact — a boutique-research-deck look (stat tiles, a segment
  legend) distinct from this library's other templates.
- If the destination is an actual Bubble Tea News issue, slot the SVG(s)
  into that issue's `.ad-box` elements per `bubble-tea-news-editor`'s
  assembly steps rather than leaving them as unused standalone files.

## To expand this skill later

Add more report formats (a focus-group transcript, a seasonal flavor-demand
forecast) or more named segments as they come up, keeping Step 0's
fictional-data discipline and Step 3's real-chain-name guardrail in place
for any variant.

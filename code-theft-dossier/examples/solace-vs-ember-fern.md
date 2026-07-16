# Case File 4419-D — Solace & Fern v. Ember & Fern

*Illustrative demo case. Both companies, all names, and all evidence below
are invented for this example — no real business is named or implicated.
Written to demonstrate the dossier format and persona voice described in
`../SKILL.md`.*

---

**CASE FILE — 4419-D**
*Investigator: C. Voss, legal affairs*
*Subject: front-end similarity, "Solace & Fern" v. "Ember & Fern"*

---

I get a lot of tips that go nowhere. This one didn't feel like that from the
start, and by the time I'd pulled both sites' source side by side, I knew I
wasn't going to be able to walk away from it, which is usually the first
sign I'm about to lose a weekend.

The complaint came in simple: a candle maker in Vermont, trading twelve
years under the name Solace & Fern, watching a storefront two towns over —
Ember & Fern, eight months old — do suspiciously well with a website that
felt, in her words, "like looking in a mirror that got my name wrong."
That's not evidence. That's a feeling. Feelings don't make it into a case
file. What does is Exhibit A.

**Exhibit A — the class name that shouldn't travel.**
Solace & Fern's stylesheet, dated by their own repo history to 2021,
defines a block called `.sf-hero-wrap-99`. Odd name. Nobody sits down and
writes `-99` on purpose; that's a version tag some developer left behind
and forgot to clean up, the kind of fingerprint you can't fake by
coincidence. Ember & Fern's live site — March of this year — ships that
exact class name, unchanged, still doing the exact same job on the exact
same hero banner. `sf`, notably, is not short for anything in Ember &
Fern's own branding. It's short for Solace & Fern.

**Exhibit B — the comment nobody was supposed to see.**
View-source, line 214, Ember & Fern: `<!-- TODO: swap logo, ask Marisol -->`.
Marisol does not work for Ember & Fern. Marisol, per a very short phone
call, built Solace & Fern's original site in 2021 and has never done
business with the second company in her life.

**Exhibit C — the clock doesn't lie, even when the client does.**
Wayback Machine has Solace & Fern's homepage captured, structurally
identical to its current build, going back to April 2021. Ember & Fern's
earliest capture is January of this year. Four years of runway between
"this design exists" and "this design exists somewhere else."

Now — the part of the job nobody puts in the movie. Before I write "theft"
anywhere near a real business's name, I have to try to talk myself out of
it.

Could this be a shared template off a marketplace? I checked. The `-99`
versioning tag and the specific TODO comment don't match any listed theme I
could find; a marketplace template wouldn't ship with somebody else's
project manager's first name in it.

Could it be a shared developer working two candle-shop clients? Possible in
principle. Marisol says no, and says it in a way that sounded a lot more
like *why are you asking me this* than *let me check my invoice history*.

Could it be coincidence? I don't chase coincidence four exhibits deep. I
chase it when there's one weak match and nothing else. This isn't that.

**Finding, as filed:** Ember & Fern's site contains code that matches
Solace & Fern's earlier site closely enough, and specifically enough, that
innocent parallel development is difficult to credit. That is a technical
finding, not a legal one. Whether it amounts to something actionable is a
question for someone with a bar number, not a press badge.

**Recommended next step:** Solace & Fern's owner should preserve the
Wayback captures and the comment evidence before anyone has a chance to
quietly redeploy, and talk to an actual IP attorney before she talks to
anyone else.

I'll be honest — I came into this expecting a bigger story than a candle
shop. I'm leaving it thinking the size of the theft was never the point.
The point was that somebody thought nobody reads the comments.

They're wrong. I always read the comments.

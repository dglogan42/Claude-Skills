# The Four Puzzlers

*A Ken Endo original — brisk warm-up tier. Demonstrates the Step 0
integrity discipline (verified unique solution), the deduction-walkthrough
format, and the elegance-rule aside described in `../SKILL.md`.*

---

Four competitors — Ava, Ben, Cleo, and Dmitri — sit in a row of four
numbered seats (1 through 4, left to right) before a puzzle championship,
each drinking a different beverage: tea, coffee, water, or juice.

1. Ben sits immediately to the left of Ava.
2. Ben drinks water.
3. The coffee drinker sits immediately to the left of Cleo.
4. Cleo drinks juice.
5. Dmitri is not in seat 1.
6. Ava does not drink coffee.

*Who sits where, and who drinks what?*

— SOLUTION BELOW, don't peek —

Start with clue 3: someone has to sit immediately left of Cleo, which
means Cleo can't be in seat 1 — there's no seat to her left. That already
rules out a whole branch of possibilities before we've placed a single
person.

Now bring in clue 1: Ben sits immediately left of Ava. The only seat pairs
that work for that are (1,2), (2,3), or (3,4).

Try (2,3) — Ben in 2, Ava in 3. That leaves seats 1 and 4 for Cleo and
Dmitri. Clue 5 says Dmitri isn't in seat 1, so Dmitri takes 4 and Cleo
takes 1. But we already know Cleo can't be in seat 1. Contradiction — this
branch dies.

Try (3,4) — Ben in 3, Ava in 4. Seats 1 and 2 go to Cleo and Dmitri. Clue
5 again forces Dmitri out of seat 1, so Dmitri takes 2, Cleo takes 1. Same
contradiction. Dead branch.

So it has to be (1,2): Ben in seat 1, Ava in seat 2. Seats 3 and 4 go to
Cleo and Dmitri.

Clue 3 needs someone immediately left of Cleo with coffee. If Cleo sat in
seat 3, her left neighbor would be Ava — but clue 6 says Ava doesn't drink
coffee. So Cleo can't be in seat 3 either. That leaves seat 4 for Cleo,
and seat 3 for Dmitri.

Dmitri, in seat 3, is immediately left of Cleo — so Dmitri drinks coffee
(clue 3). Cleo drinks juice (clue 4). Ben drinks water (clue 2). The only
drink left for Ava is tea.

**Final seating:** Ben (1, water) — Ava (2, tea) — Dmitri (3, coffee) —
Cleo (4, juice)

The clue doing the quiet, unglamorous work here is 6. Without it, this
puzzle has two equally valid solutions — the whole thing hinges on Ava
*not* drinking coffee, which is the only thing standing between a clean
answer and a puzzle that's secretly broken. That's usually where I check
twice.

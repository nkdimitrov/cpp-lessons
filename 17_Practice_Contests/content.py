# -*- coding: utf-8 -*-
"""Lesson 17 - Practice contests. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "17_Practice_Contests"
BRAND = "Lesson 17 · Practice contests"
FOOTER = ("Lesson 17 · C++17 practice contests. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Practice contests - eleven rounds of three"
SUBTITLE = ("Lesson 17 | Contest habits, cheat sheet and 33 practice problems in 11 rounds "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("home", "1. A contest at home", [
 ("p", "In a Group D olympiad round you get three problems and a few hours. The eleven rounds at "
       "the end of this lesson are built the same way: three problems that no earlier lesson "
       "used - an easier one, a middle one and a harder one."),
 ("p", "Every problem can be solved with lessons 01–16. You will not be told which lesson. "
       "Finding that out is the skill this lesson trains."),
 ("list", ["Pick the next round. Set a timer - three hours is a good start.",
           "Open all three statements on the Arena before you write any code.",
           "Send your solutions to the Arena and let the judge score them.",
           "Cover the **Technique** column. It is a hint, and a real round has no hints.",
           "Stop when the timer rings, even if you are close. Then go to section 6."]),
 ("p", "Start every problem from the same skeleton, so that you never forget the fast-input lines "
       "from lesson 01:"),
 ("code", """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    return 0;
}"""),
 ("note", "Rounds 1–8 are warm-ups: two easy problems and a medium one. Rounds 9–11 are harder: "
          "every problem is medium or hard. Each round is a little harder than the one before, so "
          "do them in order."),
]),

# ---------------------------------------------------------------- 2
("order", "2. Read all three, then choose", [
 ("p", "Do not start with problem 1 just because it comes first. Read all three statements. For "
       "each one ask: do I know how to solve it, and how long will it take to write?"),
 ("list", ["Start with the problem you are surest about. Points in the bank calm you down.",
           "Next, the one where you have an idea - even a slow one.",
           "Leave the one you do not understand for last."]),
 ("p", "Stuck for half an hour with no new idea? Move to another problem and come back later. "
       "A fresh look often finds what you missed."),
 ("p", "Each problem is checked on many tests, and every test you pass gives points. So if you "
       "cannot find a fast solution, send the slow, simple one: it still passes the small tests "
       "(lesson 16)."),
]),

# ---------------------------------------------------------------- 3
("tools", "3. Which tool? Look for the signal", [
 ("p", "The hard part of a problem is often not the code but seeing which tool it needs. Words in "
       "the statement give you a clue:"),
 ("table", ["The statement says...", "Think of...", "Lesson"], [
   ["a number with up to 100 digits", "a string, or a big integer", "03, 14"],
   ["the answer can reach 10^18", "`long long`", "02"],
   ["how many times each letter or value appears", "a counting array `cnt[]`", "06"],
   ["has this value been seen before?", "`seen[]`, or a `set`", "06, 11"],
   ["a board, a table, a map of squares", "a grid `a[i][j]` with `dr` / `dc`", "07"],
   ["smallest first, the k-th largest", "`sort`", "08"],
   ["divides, divisors, the same share for everyone", "`%`, divisors up to the square root, `gcd`",
    "02, 15, 16"],
   ["days, weeks, months", "an array of month lengths, and `% 7`", "02, 04"],
   ["try every order, every choice", "`next_permutation`, or recursion", "13, 15"],
   ["the same rule, step after step", "simulate it in a loop", "04"],
 ]),
 ("p", "When nothing rings a bell, solve two or three small examples by hand, on paper. Watch what "
       "you do. The steps you repeat are your algorithm."),
]),

# ---------------------------------------------------------------- 4
("limits", "4. Read the limits before you code", [
 ("p", "The limits at the end of the statement tell you how fast your idea must be. Look at them "
       "before you choose it, not after:"),
 ("list", ["**How big is n?** Up to 5000: two loops inside each other are fine. Up to a million: "
           "sort, or one loop. Up to 10^18: you need a formula, or a loop that halves.",
           "**How big is the answer?** More than about 2 * 10^9 means `long long`.",
           "**How much memory?** Count the bytes of your biggest array."]),
 ("p", "Example: a statement says `n` is at most 100000 and you planned to compare every pair. "
       "That is 10^10 steps - far too slow. Think again before you type a single line."),
]),

# ---------------------------------------------------------------- 5
("test", "5. Test before you send", [
 ("p", "The example in the statement is only one test, and the friendliest one. The judge has many "
       "more. Before you send, try a few of your own:"),
 ("list", ["the smallest input the statement allows, such as `n = 1`;",
           "all values equal;",
           "the biggest values - does anything overflow an `int`?",
           "an example you worked out by hand."]),
 ("p", "Then check the output: one number per line, or all on one line? Exactly the words the "
       "statement shows? One extra space or word turns a right answer into \"Wrong answer\"."),
]),

# ---------------------------------------------------------------- 6
("after", "6. After the round", [
 ("p", "The round is not over when the timer rings. This is where most of the learning happens."),
 ("list", ["For each problem you did not solve, read the **Technique** line now. Then hide it and "
           "write the solution yourself, from the beginning.",
           "Still stuck? Look the problem up in the problem catalogue: its hint gives the idea "
           "in one line.",
           "Write down every mistake that cost you points - an overflow, a wrong space, a missed "
           "case. Read the list before your next round.",
           "Tick a problem only when the Arena accepts it."]),
 ("p", "A round where you solved one problem and then fixed the other two on your own teaches "
       "more than a round you solved by reading the hints."),
]),

]

CHEATSHEET = [
 ("Start every problem", "the skeleton, with the two fast-input lines"),
 ("Begin the round", "read all three statements before any code"),
 ("Choose the order", "surest first, the one you do not understand last"),
 ("Stuck for half an hour", "move to another problem, come back later"),
 ("No fast idea", "send the simple slow one - it passes the small tests"),
 ("n up to 5000 / a million / 10^18", "two loops / sort or one loop / a formula"),
 ("Answer above 2 * 10^9", "`long long`"),
 ("Test before sending", "smallest input, all equal, biggest values, a hand example"),
 ("Check the output", "exactly what the statement shows - no extra words or spaces"),
 ("After the round", "write the missed problems yourself, then tick them"),
]

PITFALLS = [
 ("Spending the whole round on one problem.",
  "Three hours on the hardest problem and none on the other two often ends with zero. Two easier "
  "problems solved score far more."),
 ("Choosing an idea before reading the limits.",
  "A correct O(n * n) solution for `n = 100000` gets \"Time limit exceeded\" on the big tests. "
  "Look at `n` first."),
 ("Testing only on the example.",
  "The example rarely has `n = 1`, equal values or the biggest numbers. The judge's tests do."),
 ("`int` where the answer needs `long long`.",
  "Sums of many numbers, products and counts of pairs pass 2 * 10^9 easily, and an overflow "
  "gives a wrong answer without any warning."),
 ("Debugging output left in the program.",
  "One forgotten `cout << \"here\\n\";` makes every answer wrong. Remove it before you send."),
]

COMPLEXITY = [
 ["counting array: add one value, or look one up (lesson 06)", "O(1)"],
 ["`sort` (lesson 08)", "O(n log n)"],
 ["`set` / `map` / priority queue: add or find one value (lessons 11, 12)", "O(log n)"],
 ["`gcd(a, b)` (lesson 15)", "O(log n)"],
 ["divisors of `n` up to the square root (lesson 16)", "O(sqrt n)"],
 ["big numbers: add, or multiply by a small number (lesson 14)", "O(number of digits)"],
]

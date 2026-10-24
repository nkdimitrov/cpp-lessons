# -*- coding: utf-8 -*-
"""Lesson 16 - Complexity and limits. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "16_Complexity_And_Limits"
BRAND = "Lesson 16 · Time and memory"
FOOTER = ("Lesson 16 · C++17 time and memory limits. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Time and memory - will it be fast enough?"
SUBTITLE = ("Lesson 16 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("steps", "1. Counting steps", [
 ("p", "Before you write a solution, count roughly how many steps it will make. You do not need "
       "the exact number - only how it grows when `n` grows:"),
 ("code", """for (int i = 0; i < n; i++) s += a[i];          // n steps

for (int i = 0; i < n; i++)                       // n * n steps
    for (int j = 0; j < n; j++) cnt++;

while (n > 1) n /= 2;                             // about log n steps:
                                                  // 20 for a million"""),
 ("p", "We write these as O(n), O(n * n) and O(log n) - lesson by lesson you have seen this in the "
       "complexity tables. The **O** says: \"about this many steps, give or take a small "
       "factor\"."),
]),

# ---------------------------------------------------------------- 2
("second", "2. How much fits in one second", [
 ("p", "A judge's computer makes about **100 million** (10^8) simple steps per second. Put the "
       "biggest `n` from the statement into your step count and compare:"),
 ("table", ["If n is at most...", "these solutions are fast enough"], [
   ["10", "trying every order: O(n!)"],
   ["20", "trying every group: O(2^n)"],
   ["500", "three loops inside each other: O(n^3)"],
   ["5 000", "two loops inside each other: O(n^2)"],
   ["1 000 000", "sorting, O(n log n), or one loop, O(n)"],
   ["10^18", "a formula, O(1), or halving, O(log n)"],
 ]),
 ("p", "Example: `n = 100000` and you planned to compare every pair. That is about 10^10 steps - "
       "a hundred seconds. Too slow by far; you need something else."),
 ("p", "But the opposite matters just as much: if `n` is at most 1000, comparing every pair "
       "(a million steps) is perfectly fine. Do not invent something clever when the simple way "
       "is fast enough."),
]),

# ---------------------------------------------------------------- 3
("shortcut", "3. Too slow? Find a shortcut", [
 ("p", "Three shortcuts that solve a lot of problems:"),
 ("list", ["**A formula instead of a loop.** `1 + 2 + ... + n` is `n * (n + 1) / 2` - one step "
           "instead of `n` (lesson 02).",
           "**Stop at the square root.** Divisors come in pairs: if `i` divides `n`, so does "
           "`n / i`, and one of the two is at most the square root of `n`.",
           "**Sort or count once, then answer quickly.** Instead of comparing every pair, sort "
           "(lesson 08) or count (lesson 06) once."]),
 ("code", """// all divisors of n in about sqrt(n) steps - 1000 steps instead of a million
for (long long i = 1; i * i <= n; i++) {
    if (n % i == 0) {
        cout << i << ' ';
        if (i != n / i) cout << n / i << ' ';
    }
}"""),
 ("p", "When even one step per number is too slow - say, counting something among all numbers "
       "up to 10^18 - work digit position by digit position instead of number by number."),
]),

# ---------------------------------------------------------------- 4
("memory", "4. Memory", [
 ("p", "The statement also gives a **memory limit**, for example 64 MB. One MB is about a million "
       "bytes. Each value takes a fixed number of bytes:"),
 ("table", ["Type", "Bytes", "How many fit in 64 MB"], [
   ["`char`, `bool`", "1", "about 64 million"],
   ["`int`", "4", "about 16 million"],
   ["`long long`, `double`", "8", "about 8 million"],
 ]),
 ("p", "So `int a[10000000];` (ten million) uses 40 MB, and `int g[5000][5000];` uses 100 MB - "
       "too much for 64 MB."),
 ("p", "When the data does not fit, ask: **do I really need to keep all of it?** Very often a "
       "few numbers kept while reading are enough - the smallest so far, a count, a sum (lesson "
       "01). Or keep counts of the values instead of the values themselves (lesson 06)."),
]),

# ---------------------------------------------------------------- 5
("plan", "5. Before you write code", [
 ("list", ["Find the biggest `n` (and the biggest values) in the statement.",
           "Count the steps of your idea for that `n`. Under 10^8? Go ahead.",
           "Count the memory: how many numbers will you store, and of which type?",
           "Check whether the answer fits in an `int`, or needs `long long`.",
           "Only then start typing."]),
 ("p", "Two minutes of counting can save an hour of writing a solution that was never going to "
       "pass."),
]),

]

CHEATSHEET = [
 ("One loop over n", "O(n)"),
 ("A loop inside a loop", "O(n * n)"),
 ("Halving until 1", "O(log n) - about 20 for a million, 60 for 10^18"),
 ("Steps per second", "about 10^8"),
 ("n up to 5000", "two nested loops are fine"),
 ("n up to a million", "sort, or a single loop"),
 ("n up to 10^18", "a formula, or halving"),
 ("Divisors quickly", "`for (i = 1; i * i <= n; i++)` - take `i` and `n / i`"),
 ("Memory per value", "`char` 1, `int` 4, `long long` 8 bytes"),
 ("Too big to store", "keep only what you need while reading, or count instead"),
]

PITFALLS = [
 ("Never looking at the limits.",
  "An O(n * n) solution for `n = 100000` gets \"Time limit exceeded\" on the big tests, however "
  "correct it is."),
 ("Something clever where a simple loop would do.",
  "If `n` is small, trying everything is fast enough, and it is much easier to get right."),
 ("`i * i <= n` with `int i` and a big `n`.",
  "`i * i` overflows before the loop ends. Use `long long i`."),
 ("An array that does not fit.",
  "Count the bytes before you declare it: number of values times bytes per value."),
 ("Forgetting that reading takes time too.",
  "A million numbers with slow `cin` can cost a second on its own. Use the two fast-input lines "
  "from lesson 01."),
]

COMPLEXITY = [
 ["O(1), O(log n)", "instant, even for n = 10^18"],
 ["O(n), O(n log n)", "fine up to a few million"],
 ["O(n * n)", "fine up to about 5000"],
 ["O(n^3)", "fine up to about 500"],
 ["O(2^n), O(n!)", "only for about 20 and about 10"],
]

# -*- coding: utf-8 -*-
"""Lesson 15 - Recursion. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "15_Recursion"
BRAND = "Lesson 15 · Recursion"
FOOTER = ("Lesson 15 · C++17 recursion. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Recursion - a function that calls itself"
SUBTITLE = ("Lesson 15 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("idea", "1. A function that calls itself", [
 ("p", "A **recursive** function solves a problem by calling itself on a smaller copy of the same "
       "problem. It always has two parts:"),
 ("list", ["the **base case** - a problem so small that the answer is known at once;",
           "the **step** - make the problem smaller and call yourself."]),
 ("code", """// n! = 1 * 2 * ... * n
long long fact(int n) {
    if (n == 0) return 1;            // base case: 0! = 1
    return n * fact(n - 1);          // step: n! = n * (n-1)!
}

// the sum of the digits
int sd(int n) {
    if (n == 0) return 0;
    return n % 10 + sd(n / 10);
}

// the greatest common divisor - Euclid's rule
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}"""),
 ("p", "`gcd(12, 18)` calls `gcd(18, 12)`, then `gcd(12, 6)`, then `gcd(6, 0)`, which answers 6. "
       "Each call is smaller than the one before, so the base case is always reached."),
]),

# ---------------------------------------------------------------- 2
("calls", "2. How the computer keeps track", [
 ("p", "When `fact(3)` calls `fact(2)`, the first call waits. It continues only when `fact(2)` "
       "has answered. The waiting calls pile up like a stack of plates:"),
 ("table", ["Call", "What happens"], [
   ["`fact(3)`", "waits for `fact(2)`"],
   ["`fact(2)`", "waits for `fact(1)`"],
   ["`fact(1)`", "waits for `fact(0)`"],
   ["`fact(0)`", "the base case answers 1"],
   ["`fact(1)`", "gets 1 and answers `1 * 1 = 1`"],
   ["`fact(2)`", "gets 1 and answers `2 * 1 = 2`"],
   ["`fact(3)`", "gets 2 and answers `3 * 2 = 6`"],
 ]),
 ("p", "If the base case is missing, or never reached, the pile grows until memory runs out and "
       "the program crashes. Even a correct recursion crashes if it goes too deep: a few thousand "
       "calls inside each other are fine, a million are not."),
]),

# ---------------------------------------------------------------- 3
("memo", "3. Remembering answers", [
 ("p", "Fibonacci numbers: `F(0) = 0`, `F(1) = 1`, and every next one is the sum of the two "
       "before. The obvious recursion is correct but terribly slow:"),
 ("code", """long long fib(int n) {
    if (n < 2) return n;
    return fib(n - 1) + fib(n - 2);   // fib(40) makes over 300 million calls
}"""),
 ("p", "It is slow because it works out the same small values again and again. Fix it by "
       "**remembering**: the first time you know `fib(n)`, write it down in an array; next time, "
       "just read it:"),
 ("code", """long long memo[100];
bool known[100];

long long fib(int n) {
    if (n < 2) return n;
    if (known[n]) return memo[n];     // worked out before: just read it
    memo[n] = fib(n - 1) + fib(n - 2);
    known[n] = true;
    return memo[n];
}"""),
 ("p", "Now every value is worked out only once, and `fib(90)` is instant. The same trick works "
       "for any recursion with a few numbers as its input, for example `f(steps, row, col)` with "
       "a three-dimensional array."),
]),

# ---------------------------------------------------------------- 4
("all", "4. Trying every choice", [
 ("p", "Recursion is the easiest way to try **every** possibility. Each call makes one choice and "
       "leaves the rest to the next call. All strings of 0s and 1s of length `n`:"),
 ("code", """int n;

void gen(string s) {
    if ((int)s.size() == n) {         // a whole string is ready
        cout << s << '\\n';
        return;
    }
    gen(s + '0');                     // choice 1: the next digit is 0
    gen(s + '1');                     // choice 2: the next digit is 1
}

// gen("") with n = 3 prints 000 001 010 011 100 101 110 111"""),
 ("p", "The same shape gives every **group** chosen from `n` people: for person `i`, either take "
       "them or leave them, then go on to person `i + 1`:"),
 ("code", """int a[20];

void go(int i, int sum) {
    if (i == n) {                     // decided about everybody
        // look at sum here
        return;
    }
    go(i + 1, sum + a[i]);            // take person i
    go(i + 1, sum);                   // leave person i
}"""),
 ("note", "There are `2^n` groups: about a thousand for 10 people and a million for 20. More than "
          "about 25 is too many."),
]),

# ---------------------------------------------------------------- 5
("back", "5. Going back: backtracking", [
 ("p", "To try every **order** of the numbers 1 to `n`, put a number in each place, but only a "
       "number that is not used yet. When the call comes back, **undo** the choice, so that the "
       "next number can be tried in its place:"),
 ("code", """int n, p[10];
bool used[10];

void perm(int k) {                    // fill place k
    if (k == n) {
        for (int i = 0; i < n; i++) cout << p[i] << ' ';
        cout << '\\n';
        return;
    }
    for (int v = 1; v <= n; v++) {
        if (used[v]) continue;
        used[v] = true;  p[k] = v;    // choose
        perm(k + 1);                  // try everything after it
        used[v] = false;              // undo
    }
}"""),
 ("p", "This \"choose, try, undo\" pattern is called **backtracking**. It becomes really strong "
       "when you stop early: if a choice already breaks the rules, do not call any further - go "
       "back at once and try the next choice."),
]),

]

CHEATSHEET = [
 ("Every recursion", "a base case that answers at once, and a step that calls on a smaller problem"),
 ("Factorial", "`if (n == 0) return 1; return n * fact(n - 1);`"),
 ("Sum of digits", "`if (n == 0) return 0; return n % 10 + sd(n / 10);`"),
 ("Greatest common divisor", "`if (b == 0) return a; return gcd(b, a % b);`"),
 ("Remember answers", "`if (known[n]) return memo[n];` ... `known[n] = true;`"),
 ("All 0/1 strings", "`gen(s + '0'); gen(s + '1');`"),
 ("All groups", "`go(i + 1, take); go(i + 1, leave);`"),
 ("All orders", "for each unused `v`: mark, place, `perm(k + 1)`, unmark"),
 ("Stop early", "if a choice already breaks the rules, do not call further"),
]

PITFALLS = [
 ("No base case, or one that is never reached.",
  "`f(n)` calling `f(n - 2)` with base case `n == 0` never stops for odd `n`. Check that every "
  "path reaches a base case."),
 ("The same values worked out again and again.",
  "Plain recursive Fibonacci takes seconds for `n = 45`. Remember the answers in an array."),
 ("Forgetting to undo.",
  "Without `used[v] = false;` after the call, every later branch thinks `v` is taken, and most "
  "answers are never found."),
 ("Recursion that goes too deep.",
  "A million calls inside each other crash the program. For long chains, write a loop instead."),
 ("Too many possibilities.",
  "`2^n` and `n!` grow very fast. Count them before you write the recursion."),
]

COMPLEXITY = [
 ["`fact(n)`, `sd(n)`", "O(n) and O(number of digits)"],
 ["`gcd(a, b)`", "very few calls - about 90 at most for `long long` numbers"],
 ["Fibonacci without remembering", "about O(2^n) - hopeless for n = 50"],
 ["Fibonacci with remembering", "O(n)"],
 ["All 0/1 strings or all groups of `n`", "O(2^n)"],
 ["All orders of `n` numbers", "O(n!)"],
]

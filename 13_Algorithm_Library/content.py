# -*- coding: utf-8 -*-
"""Lesson 13 - The <algorithm> toolbox. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "13_Algorithm_Library"
BRAND = "Lesson 13 · The algorithm toolbox"
FOOTER = ("Lesson 13 · C++17 <algorithm>. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 The <algorithm> toolbox - loops you do not have to write"
SUBTITLE = ("Lesson 13 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("range", "1. Telling a tool where to work", [
 ("p", "`#include <algorithm>` gives you ready-made loops. You already know one: `sort`. Every "
       "tool in this lesson is told where to start and where to stop, in the same way:"),
 ("table", ["You write", "It means"], [
   ["`a, a + n`", "the first `n` boxes of the array `a`"],
   ["`a + l, a + r`", "boxes `l`, `l + 1`, ..., `r - 1` - the stop box is **not** included"],
   ["`v.begin(), v.end()`", "the whole vector `v` (or string `v`)"],
 ]),
 ("p", "Some tools give back a **place** instead of a number. Subtract the start to turn it into "
       "an index: `max_element(a, a + n) - a` is the index of the largest box."),
]),

# ---------------------------------------------------------------- 2
("find", "2. min, max, count and find", [
 ("code", """int x = 4, y = 9;
cout << min(x, y) << ' ' << max(x, y) << '\\n';   // 4 9
swap(x, y);                                       // x = 9, y = 4

int a[] = {3, 8, 1, 8, 5};
int n = 5;
int big = *max_element(a, a + n);         // 8 - the * gives the value
int where = max_element(a, a + n) - a;    // 1 - the first place with the largest
int least = *min_element(a, a + n);       // 1

int eights = count(a, a + n, 8);          // 2
int p = find(a, a + n, 5) - a;            // 4 - the first place holding 5
int q = find(a, a + n, 7) - a;            // 5 = n - means "not found\""""),
 ("p", "They all work on a part of the array too. How many 1s are among the four boxes starting "
       "at place `i`? `count(a + i, a + i + 4, 1)`."),
]),

# ---------------------------------------------------------------- 3
("reorder", "3. reverse, rotate and unique", [
 ("code", """int a[] = {1, 2, 3, 4, 5};
reverse(a, a + 5);               // 5 4 3 2 1
reverse(a, a + 5);               // back to 1 2 3 4 5

rotate(a, a + 2, a + 5);         // 3 4 5 1 2 - box 2 becomes the first"""),
 ("p", "`unique` removes repeats that stand **next to each other**. So sort first. It gives back "
       "the new end, which tells you how many different values there are:"),
 ("code", """int b[] = {4, 1, 4, 2, 1};
int n = 5;
sort(b, b + n);                  // 1 1 2 4 4
int m = unique(b, b + n) - b;    // 3 - the first 3 boxes are 1 2 4

vector<int> v = {4, 1, 4, 2, 1};             // the same for a vector:
sort(v.begin(), v.end());
v.erase(unique(v.begin(), v.end()), v.end()); // v is {1, 2, 4}"""),
 ("p", "`reverse` also turns round the digits of a number once it is a string: "
       "`string s = to_string(n); reverse(s.begin(), s.end());`."),
]),

# ---------------------------------------------------------------- 4
("perm", "4. Every order: next_permutation", [
 ("p", "`next_permutation` changes the array into the next order in dictionary order. Start from "
       "the sorted order and loop until it says there is no next one, and you visit **every** "
       "order exactly once:"),
 ("code", """int a[] = {1, 2, 3};
do {
    cout << a[0] << a[1] << a[2] << ' ';
} while (next_permutation(a, a + 3));
// 123 132 213 231 312 321"""),
 ("p", "It works on strings too: `sort(s.begin(), s.end())`, then "
       "`do { ... } while (next_permutation(s.begin(), s.end()));`."),
 ("note", "There are `n!` orders: 6 for 3 things, 40320 for 8, 3628800 for 10. Up to about 10 "
          "things, trying every order is fast enough. For 12 or more it is far too slow."),
]),

# ---------------------------------------------------------------- 5
("bsearch", "5. Searching sorted data", [
 ("p", "In a **sorted** array you can find things very quickly. The tool looks at the middle, "
       "throws away the half that cannot hold the answer, and repeats. For a million numbers that "
       "is only about 20 steps."),
 ("code", """int a[] = {2, 4, 4, 4, 7, 9};
int n = 6;
bool has = binary_search(a, a + n, 7);        // true

int lo = lower_bound(a, a + n, 4) - a;        // 1 - first place with a value >= 4
int hi = upper_bound(a, a + n, 4) - a;        // 4 - first place with a value >  4
cout << hi - lo << '\\n';                      // 3 - how many 4s
cout << lo << '\\n';                           // 1 - how many values are smaller than 4"""),
 ("p", "If every number is smaller than the one you search for, `lower_bound` gives `n`. Check "
       "for that before you read `a[lo]`."),
]),

]

CHEATSHEET = [
 ("The whole array / vector", "`a, a + n` / `v.begin(), v.end()`"),
 ("Smaller / larger of two, swap", "`min(x, y)`, `max(x, y)`, `swap(x, y)`"),
 ("Largest value / its index", "`*max_element(a, a + n)` / `max_element(a, a + n) - a`"),
 ("How many equal to `x`", "`count(a, a + n, x)`"),
 ("Where is `x`?", "`find(a, a + n, x) - a` - equals `n` when not found"),
 ("Back to front", "`reverse(a, a + n)`"),
 ("Start from box `k`", "`rotate(a, a + k, a + n)`"),
 ("Different values", "`sort`, then `m = unique(a, a + n) - a`"),
 ("Every order", "`sort`, then `do { ... } while (next_permutation(a, a + n));`"),
 ("Is `x` in a sorted array?", "`binary_search(a, a + n, x)`"),
 ("First `>= x` / first `> x`", "`lower_bound(a, a + n, x) - a` / `upper_bound(a, a + n, x) - a`"),
]

PITFALLS = [
 ("Forgetting to sort first.",
  "`unique`, `binary_search`, `lower_bound` and the full `next_permutation` loop all expect "
  "sorted data. On unsorted data they give wrong answers without any warning."),
 ("`max_element` gives a place, not a value.",
  "Write `*max_element(...)` for the value and `max_element(...) - a` for the index."),
 ("`find` that finds nothing.",
  "It gives the end place, so the index is `n`. Reading `a[n]` then is outside the array."),
 ("`unique` does not shrink anything by itself.",
  "Use the number it gives back, or `erase` the tail of a vector."),
 ("Trying every order for too many things.",
  "11 things already have almost 40 million orders. Count `n!` before you start."),
]

COMPLEXITY = [
 ["`min`, `max`, `swap`", "O(1)"],
 ["`count`, `find`, `max_element`, `reverse`, `rotate`, `unique`", "O(n)"],
 ["`sort`", "O(n log n)"],
 ["`binary_search`, `lower_bound`, `upper_bound`", "O(log n) - about 20 steps for a million"],
 ["All orders with `next_permutation`", "O(n!) - only for small n"],
]

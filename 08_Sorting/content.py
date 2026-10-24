# -*- coding: utf-8 -*-
"""Lesson 08 - Sorting. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "08_Sorting"
BRAND = "Lesson 08 · Sorting"
FOOTER = ("Lesson 08 · C++17 sorting. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Sorting - putting things in order"
SUBTITLE = ("Lesson 08 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("sort", "1. Sorting in one line", [
 ("p", "`sort` puts the numbers in order, smallest first. Add `#include <algorithm>`. You tell it "
       "where the numbers start and where they end:"),
 ("code", """int a[] = {5, 2, 9, 1, 7};
int n = 5;
sort(a, a + n);                  // a is now 1 2 5 7 9

vector<int> v = {5, 2, 9};
sort(v.begin(), v.end());        // v is now 2 5 9

string s = "banana";
sort(s.begin(), s.end());        // s is now "aaabnn\""""),
 ("p", "`a, a + n` means \"from box 0 up to, but not including, box n\" - exactly the `n` boxes "
       "you filled."),
]),

# ---------------------------------------------------------------- 2
("desc", "2. Largest first", [
 ("p", "Add `greater<int>()` to sort from the largest down:"),
 ("code", """sort(a, a + n, greater<int>());          // 9 7 5 2 1
sort(v.begin(), v.end(), greater<int>());"""),
 ("p", "Or sort normally and read the array from the end. Both are fine."),
]),

# ---------------------------------------------------------------- 3
("after", "3. What sorting gives you", [
 ("p", "Once the numbers are sorted, many questions become easy:"),
 ("table", ["Question", "After sorting"], [
   ["smallest / largest", "`a[0]` / `a[n - 1]`"],
   ["the middle one (median)", "`a[n / 2]`"],
   ["the 3 largest", "`a[n - 1]`, `a[n - 2]`, `a[n - 3]`"],
   ["are there equal numbers?", "equal numbers are now **neighbours**"],
   ["the biggest gap between two numbers", "only neighbours need checking"],
 ]),
 ("code", """sort(a, a + n);

int different = 1;                       // how many different values
for (int i = 1; i < n; i++)
    if (a[i] != a[i - 1]) different++;

int gap = 0;                             // the biggest gap between neighbours
for (int i = 1; i < n; i++)
    if (a[i] - a[i - 1] > gap) gap = a[i] - a[i - 1];"""),
]),

# ---------------------------------------------------------------- 4
("rule", "4. Your own order", [
 ("p", "To sort by a rule of your own, write a function that answers one question: **should `x` "
       "come before `y`?** Then give its name to `sort`:"),
 ("code", """// by the last digit; when the last digits are equal, the smaller number first
bool cmp(int x, int y) {
    if (x % 10 != y % 10) return x % 10 < y % 10;
    return x < y;
}

sort(a, a + n, cmp);         // 21 3 13 5 15 ...  - no () after cmp"""),
 ("p", "The pattern is always the same: compare by the first rule; only if that rule cannot "
       "decide, go on to the next rule."),
 ("note", "For two **equal** elements the function must return `false`. Using `<=` instead of `<` "
          "breaks this, and `sort` can then crash."),
 ("p", "A famous rule: to glue numbers into the largest possible number, keep them as strings and "
       "put `x` before `y` when `x + y > y + x`. So `\"9\"` comes before `\"34\"`, because "
       "`\"934\" > \"349\"`."),
]),

# ---------------------------------------------------------------- 5
("two", "5. Two sorted lists side by side", [
 ("p", "With two sorted lists you can walk both at once, one index each. Every lid is tried "
       "with the pans in order, and neither index ever goes back:"),
 ("code", """sort(pan, pan + n);
sort(lid, lid + m);
int i = 0, j = 0, matched = 0;
while (i < n && j < m) {
    if (lid[j] >= pan[i]) { matched++; i++; j++; }   // this lid fits this pan
    else j++;                                          // lid too small: try the next lid
}"""),
 ("p", "The two ends of **one** sorted list work the same way: `i` starts at the smallest, `j` at "
       "the largest, and they move towards each other. Pair the largest with the smallest when the "
       "two fit together; otherwise the largest has to go alone."),
]),

# ---------------------------------------------------------------- 6
("decide", "6. Sort first, then decide", [
 ("p", "Many problems are easy once the order is right. You have `B` leva - how many toys can you "
       "buy? Buy the cheapest first:"),
 ("code", """sort(price, price + n);
int bought = 0;
long long spent = 0;
for (int i = 0; i < n; i++) {
    if (spent + price[i] > B) break;
    spent += price[i];
    bought++;
}"""),
 ("p", "Ask yourself: if I process the things in sorted order, can I decide about each one "
       "straight away? Very often the answer is yes."),
]),

]

CHEATSHEET = [
 ("Sort an array / a vector / a string", "`sort(a, a + n)` / `sort(v.begin(), v.end())` / `sort(s.begin(), s.end())`"),
 ("Largest first", "`sort(a, a + n, greater<int>())`"),
 ("Smallest, largest, middle", "`a[0]`, `a[n - 1]`, `a[n / 2]`"),
 ("Count different values", "sort, then count `a[i] != a[i - 1]`"),
 ("Own order", "`bool cmp(int x, int y)` - true when `x` must come first; `sort(a, a + n, cmp)`"),
 ("Several rules", "`if (rule1 differs) return rule1; return rule2;`"),
 ("Largest glued number", "strings, `x + y > y + x`"),
 ("Two sorted lists", "one index in each, both only move forward"),
 ("Both ends of one list", "`i = 0`, `j = n - 1`, move towards each other"),
]

PITFALLS = [
 ("`sort(a, a + n - 1)` leaves the last box out.",
  "The end is one past the last box: `a + n`."),
 ("`<=` inside a compare function.",
  "Equal elements must give `false`. Use `<` and `>`, never `<=` or `>=`."),
 ("Sorting loses the original places.",
  "After `sort`, you no longer know where each number came from. If the answer needs the original "
  "number, keep it next to the value (lesson 09 shows pairs)."),
 ("Sorting again and again inside a loop.",
  "`sort` costs about `n log n` steps every time. Sort once, before the loop."),
 ("Strings sort like a dictionary, not like numbers.",
  "`\"10\" < \"9\"` is true. Sort numbers as numbers."),
]

COMPLEXITY = [
 ["`sort` of `n` elements", "O(n log n) - about 2 million steps for n = 100000"],
 ["Looking at all neighbours after sorting", "O(n)"],
 ["Walking two sorted lists together", "O(n + m)"],
 ["Comparing every pair instead of sorting", "O(n * n) - far slower for big n"],
]

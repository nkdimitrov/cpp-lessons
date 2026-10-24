# -*- coding: utf-8 -*-
"""Lesson 04 - Arrays. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "04_Arrays"
BRAND = "Lesson 04 · Arrays"
FOOTER = ("Lesson 04 · C++17 arrays. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Arrays - a row of numbered boxes"
SUBTITLE = ("Lesson 04 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("what", "1. What an array is", [
 ("p", "An array is a row of boxes with one name. Each box holds one value and has a number, its "
       "**index**. Counting starts at 0:"),
 ("code", """int a[5];          // five boxes: a[0], a[1], a[2], a[3], a[4]
a[0] = 7;
a[4] = 2;
cout << a[0] + a[4] << '\\n';     // 9"""),
 ("p", "The size must be a fixed number. Make it a little bigger than the largest `n` in the "
       "statement. If n can be up to 100000, write:"),
 ("code", """int a[100005];     // outside main: every box starts at 0

int main() {
    // ...
}"""),
 ("note", "Put big arrays **outside** `main`. There they start filled with zeros and may be large. "
          "An array inside `main` starts full of rubbish, and a very big one can crash the "
          "program."),
]),

# ---------------------------------------------------------------- 2
("fill", "2. Filling and printing an array", [
 ("p", "The usual start: read how many numbers there are, then read them into the boxes."),
 ("code", """int n;
cin >> n;
for (int i = 0; i < n; i++) cin >> a[i];

for (int i = 0; i < n; i++) cout << a[i] << ' ';       // in order
cout << '\\n';
for (int i = n - 1; i >= 0; i--) cout << a[i] << ' ';  // backwards
cout << '\\n';"""),
 ("p", "Why store the numbers at all? Because many problems need to look at them **twice**: first "
       "to find something out, then to use it. How many numbers are bigger than the average? You "
       "need the average before you can count."),
]),

# ---------------------------------------------------------------- 3
("scan", "3. Sum, largest, smallest, count", [
 ("p", "Almost every array problem starts with one of these loops:"),
 ("code", """long long sum = 0;
for (int i = 0; i < n; i++) sum += a[i];

int mx = a[0], where = 0;            // the largest, and its index
for (int i = 1; i < n; i++)
    if (a[i] > mx) { mx = a[i]; where = i; }

int cnt = 0;                          // how many are even
for (int i = 0; i < n; i++)
    if (a[i] % 2 == 0) cnt++;"""),
 ("p", "Sometimes the index itself means something. If settlement number `s` gets `x` more tonnes, "
       "write `t[s] += x;` - the box number is the settlement number."),
]),

# ---------------------------------------------------------------- 4
("neigh", "4. Neighbours", [
 ("p", "The neighbours of `a[i]` are `a[i - 1]` and `a[i + 1]`. The first box has no left "
       "neighbour and the last has no right one, so the loop must keep away from the ends:"),
 ("code", """// a "peak" is bigger than both neighbours
int peaks = 0;
for (int i = 1; i < n - 1; i++)
    if (a[i - 1] < a[i] && a[i] > a[i + 1]) peaks++;

// how many times does the next number go up?
int ups = 0;
for (int i = 0; i + 1 < n; i++)
    if (a[i] < a[i + 1]) ups++;"""),
 ("note", "Before writing `a[i + 1]`, check that `i + 1` is still a box: the loop must stop at "
          "`i + 1 < n`. Going one box too far does not give an error message - it reads rubbish."),
]),

# ---------------------------------------------------------------- 5
("circle", "5. Round in a circle, and windows", [
 ("p", "When the boxes stand in a circle, the box after the last is the first again. `%` does "
       "the wrapping:"),
 ("code", """int next = (i + 1) % n;          // after n - 1 comes 0
int prev = (i - 1 + n) % n;      // before 0 comes n - 1"""),
 ("p", "The sum of three boxes in a row, going all the way round the circle:"),
 ("code", """int best = 0;
for (int i = 0; i < n; i++) {
    int s = a[i] + a[(i + 1) % n] + a[(i + 2) % n];
    if (s > best) best = s;
}"""),
 ("p", "A **window** is a block of `k` boxes in a row. To move it one step right, add the box that "
       "comes in and take away the box that goes out - no need to add all `k` again:"),
 ("code", """long long s = 0;
for (int i = 0; i < k; i++) s += a[i];       // the first window
long long best = s;
for (int i = k; i < n; i++) {
    s += a[i] - a[i - k];                     // a[i] comes in, a[i - k] goes out
    if (s > best) best = s;
}"""),
]),

# ---------------------------------------------------------------- 6
("passes", "6. Several passes, several arrays", [
 ("p", "Some questions need two walks over the array. \"What is the highest wall to the left of "
       "each place?\" is one walk from the left; \"to the right\" is one walk from the right. Keep "
       "both answers in arrays (`max` needs `#include <algorithm>`):"),
 ("code", """int L[100005], R[100005];
L[0] = a[0];
for (int i = 1; i < n; i++) L[i] = max(L[i - 1], a[i]);
R[n - 1] = a[n - 1];
for (int i = n - 2; i >= 0; i--) R[i] = max(R[i + 1], a[i]);"""),
 ("p", "Two arrays with the same index can describe the same thing: `start[i]` and `finish[i]` "
       "for the i-th task. A third array can **mark** places: `bad[i] = true` when place `i` "
       "is forbidden, then count the places that are not marked."),
 ("p", "When the array is small, comparing every pair is fine. Two loops, the second starting "
       "after the first, see each pair once:"),
 ("code", """for (int i = 0; i < n; i++)
    for (int j = i + 1; j < n; j++)
        if (a[i] + a[j] == 10) cout << i << ' ' << j << '\\n';"""),
]),

]

CHEATSHEET = [
 ("Make an array", "`int a[100005];` outside `main`"),
 ("Read `n` values", "`for (int i = 0; i < n; i++) cin >> a[i];`"),
 ("Print backwards", "`for (int i = n - 1; i >= 0; i--) cout << a[i] << ' ';`"),
 ("Sum", "`long long s = 0; for (...) s += a[i];`"),
 ("Largest and where it is", "`mx = a[0]`, then `if (a[i] > mx) { mx = a[i]; where = i; }`"),
 ("Peak", "`a[i - 1] < a[i] && a[i] > a[i + 1]`, with `i` from 1 to `n - 2`"),
 ("Next and previous on a circle", "`(i + 1) % n`, `(i - 1 + n) % n`"),
 ("Slide a window one step", "`s += a[i] - a[i - k];`"),
 ("Best to the left of each place", "`L[i] = max(L[i - 1], a[i]);`"),
 ("Every pair once", "`for (i ...) for (j = i + 1; ...)`"),
]

PITFALLS = [
 ("Reading outside the array.",
  "`a[n]` and `a[-1]` are not boxes of your array. The program does not stop; it reads "
  "rubbish or crashes later. Check the loop limits."),
 ("An array inside `main` is not zeroed.",
  "`int c[100];` inside `main` starts with rubbish. Put it outside `main`, or write "
  "`int c[100] = {0};`."),
 ("The array is too small.",
  "If `n` can be 100000 and the array has 1000 boxes, the program fails on the big tests only. "
  "Size it from the statement, plus a few spare boxes."),
 ("Forgetting the ends when you look at neighbours.",
  "`a[i + 1]` for the last `i` is outside the array. Stop the loop at `i + 1 < n`."),
 ("`(i - 1) % n` for `i = 0`.",
  "It gives -1, not `n - 1`. Write `(i - 1 + n) % n`."),
]

COMPLEXITY = [
 ["`a[i]` - read or write one box", "O(1)"],
 ["One walk over the array (sum, largest, count)", "O(n)"],
 ["Sliding a window of `k` along the array", "O(n), not O(n * k)"],
 ["Comparing every pair", "O(n * n) - fine for n up to a few thousand"],
]

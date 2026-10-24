# -*- coding: utf-8 -*-
"""Lesson 05 - Vectors. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "05_Vectors"
BRAND = "Lesson 05 · Vectors"
FOOTER = ("Lesson 05 · C++17 std::vector. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Vectors - a list that grows"
SUBTITLE = ("Lesson 05 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("grow", "1. A list that grows", [
 ("p", "An array has a fixed size. A `vector` starts empty and grows each time you add something. "
       "Add `#include <vector>` at the top."),
 ("code", """vector<int> v;           // empty
v.push_back(5);          // {5}
v.push_back(8);          // {5, 8}
v.push_back(1);          // {5, 8, 1}

cout << v.size() << '\\n';    // 3
cout << v[0] << '\\n';        // 5 - places start at 0, as in an array"""),
 ("p", "This is exactly what you need when you do not know in advance how many values are coming. "
       "Read until a stop sign and keep everything:"),
 ("code", """vector<int> v;
int x;
while (cin >> x && x != 0)   // the input ends with 0
    v.push_back(x);"""),
]),

# ---------------------------------------------------------------- 2
("sized", "2. A vector of a given size", [
 ("p", "When you do know the size, make the vector that size at once. The size may come from the "
       "input:"),
 ("code", """int n;
cin >> n;
vector<int> a(n);            // n boxes, all 0
for (int i = 0; i < n; i++) cin >> a[i];

vector<int> c(n, -1);        // n boxes, all -1"""),
 ("p", "From here on, `a` is used exactly like an array."),
]),

# ---------------------------------------------------------------- 3
("walk", "3. Walking through, the last element, sorting", [
 ("code", """int m = v.size();            // like strings: copy the size into an int first
for (int i = 0; i < m; i++) cout << v[i] << ' ';

cout << v.back();            // the last element
v.pop_back();                // remove the last element
v.clear();                   // remove everything"""),
 ("p", "Sorting and reversing a whole vector need `#include <algorithm>`:"),
 ("code", """sort(v.begin(), v.end());        // smallest first
reverse(v.begin(), v.end());     // back to front"""),
 ("p", "`v.begin(), v.end()` simply means \"the whole vector\". Lesson 08 is all about sorting."),
]),

# ---------------------------------------------------------------- 4
("digits", "4. Digits and numbers in a vector", [
 ("p", "Taking a number apart with `% 10` gives its digits from the last one to the first. Put "
       "them in a vector and you can look at all of them as often as you like:"),
 ("code", """long long n = 4728;
vector<int> d;
while (n > 0) {
    d.push_back(n % 10);
    n /= 10;
}
// d is {8, 2, 7, 4} - the digits backwards"""),
 ("p", "Change `10` to `b` and you get the digits in base `b`. To check whether the number is a "
       "palindrome in that base, compare `d` with a reversed copy of itself."),
 ("p", "A vector is also handy for a list of special numbers that you make yourself, for example "
       "all Fibonacci numbers up to a limit:"),
 ("code", """vector<long long> f;
f.push_back(1);
f.push_back(2);
while (f[f.size() - 1] + f[f.size() - 2] <= 1000000000000LL)
    f.push_back(f[f.size() - 1] + f[f.size() - 2]);"""),
]),

# ---------------------------------------------------------------- 5
("build", "5. Building a new vector", [
 ("p", "To throw some elements away, do not delete them one by one. Build a new vector with the "
       "ones you keep, then replace the old one:"),
 ("code", """vector<int> keep;
int m = v.size();
for (int i = 0; i < m; i++)
    if (v[i] % 2 == 0) keep.push_back(v[i]);     // keep the even ones
v = keep;"""),
 ("p", "To put a value **in the middle**, use `insert`. Everything after it moves one place "
       "right:"),
 ("code", """vector<int> v = {10, 20, 30};
v.insert(v.begin() + 1, 15);     // {10, 15, 20, 30} - 15 goes to place 1"""),
 ("note", "`insert` and `erase` in the middle move all the elements after that place. Doing that "
          "many times on a long vector is slow. Building a new vector is one pass."),
]),

# ---------------------------------------------------------------- 6
("many", "6. One list for each group", [
 ("p", "An array of vectors gives every group its own list. Here every value gets the list of "
       "places where it appears:"),
 ("code", """vector<int> pos[1001];           // values are from 0 to 1000

int n;
cin >> n;
for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    pos[x].push_back(i);         // x was seen at place i
}
cout << pos[7].size() << '\\n';   // how many times 7 appeared"""),
 ("p", "The same idea stores a map of roads: `nb[c]` is the list of towns next to town `c`. "
       "A road between `a` and `b` adds `b` to `nb[a]` and `a` to `nb[b]`."),
]),

]

CHEATSHEET = [
 ("Empty vector, then add", "`vector<int> v; v.push_back(x);`"),
 ("Vector of size `n`", "`vector<int> a(n);` or `vector<int> a(n, value);`"),
 ("Size", "`int m = v.size();`"),
 ("Last element / remove it", "`v.back()` / `v.pop_back()`"),
 ("Remove everything", "`v.clear()`"),
 ("Sort / reverse", "`sort(v.begin(), v.end())`, `reverse(v.begin(), v.end())`"),
 ("Digits of `n`", "`while (n > 0) { d.push_back(n % 10); n /= 10; }` - backwards"),
 ("Keep only some", "build a new vector, then `v = keep;`"),
 ("Put `x` at place `p`", "`v.insert(v.begin() + p, x);`"),
 ("One list per group", "`vector<int> g[1001]; g[k].push_back(x);`"),
]

PITFALLS = [
 ("`v[i]` before anything is there.",
  "`vector<int> v; v[0] = 5;` writes outside the vector. Use `push_back`, or make the vector "
  "big enough first with `vector<int> v(n);`."),
 ("`v.size() - 1` on an empty vector.",
  "`size()` cannot be negative, so `0 - 1` becomes a gigantic number. Copy it into an `int` "
  "first: `int m = v.size();`."),
 ("Erasing inside a loop over places.",
  "After an erase, the next element slides into the place you just looked at, and the loop "
  "skips it. Build a new vector instead."),
 ("Forgetting to clear between test cases.",
  "A vector keeps its old elements. If one input holds several tests, `v.clear()` before each."),
 ("The digits come out backwards.",
  "`n % 10` gives the last digit first. Reverse the vector if you need them in the usual order."),
]

COMPLEXITY = [
 ["`v[i]`, `v.size()`, `v.back()`", "O(1)"],
 ["`push_back`, `pop_back`", "O(1)"],
 ["`insert` or `erase` in the middle", "O(n) - everything after moves"],
 ["Building a new vector in one pass", "O(n)"],
 ["`sort(v.begin(), v.end())`", "O(n log n)"],
]

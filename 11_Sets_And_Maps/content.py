# -*- coding: utf-8 -*-
"""Lesson 11 - Sets and maps. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "11_Sets_And_Maps"
BRAND = "Lesson 11 · Sets and maps"
FOOTER = ("Lesson 11 · C++17 set and map. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Sets and maps - remembering what you have seen"
SUBTITLE = ("Lesson 11 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("set", "1. set: each value once, in order", [
 ("p", "A `set` is a bag that keeps every value **only once** and always keeps them **sorted**. "
       "Add `#include <set>`:"),
 ("code", """set<int> s;
s.insert(5);
s.insert(1);
s.insert(5);                     // already there: nothing happens
s.insert(3);                     // s is {1, 3, 5}

cout << s.size() << '\\n';        // 3
cout << s.count(3) << '\\n';      // 1 - it is there
cout << s.count(4) << '\\n';      // 0 - it is not
s.erase(3);                      // s is {1, 5}"""),
 ("p", "The easiest use of all: **how many different values** are there? Insert them all and ask "
       "for the size. Unlike a counting array (lesson 06), the values may be huge or negative, "
       "and they can even be strings."),
]),

# ---------------------------------------------------------------- 2
("map", "2. map: a box for any key", [
 ("p", "A `map` is like a counting array whose box numbers can be anything: big numbers, negative "
       "numbers, words. Each box number is called a **key**. Add `#include <map>`:"),
 ("code", """map<string, int> cnt;
string w;
while (cin >> w) cnt[w]++;           // count every word

cout << cnt["apple"] << '\\n';        // how many times "apple" appeared

map<long long, int> c;               // keys up to 10^18 - no array could do this
c[1000000000000LL]++;"""),
 ("p", "A key that has never been used starts with the value 0, so `cnt[w]++` just works."),
 ("note", "Even **looking** at `cnt[w]` creates the key `w` with value 0. To ask \"is the key "
          "there?\" without creating it, use `cnt.count(w)`."),
]),

# ---------------------------------------------------------------- 3
("walk", "3. Walking through a set or a map", [
 ("p", "A range `for` visits the values of a set from the smallest to the largest:"),
 ("code", """for (int x : s) cout << x << ' ';          // 1 5"""),
 ("p", "In a map, each element is a pair: the key in `first`, the value in `second`. The keys "
       "come in sorted order:"),
 ("code", """map<int, int> cnt;
// ... cnt[x]++ for every x ...

int best = 0, bestKey = 0;            // the commonest key
for (pair<int, int> p : cnt)
    if (p.second > best) {
        best = p.second;
        bestKey = p.first;
    }"""),
 ("p", "Because the keys are sorted, ties go to the smallest key - which is what most statements "
       "ask for."),
]),

# ---------------------------------------------------------------- 4
("lookup", "4. Is it there? Fast lookups", [
 ("p", "A set answers \"have I seen this value?\" quickly, whatever the values are. That turns "
       "many slow double loops into one loop."),
 ("p", "**Two numbers with sum S.** For every number `x`, the partner it needs is `S - x`. Ask "
       "the set whether that partner has already been seen:"),
 ("code", """set<long long> seen;
int pairs = 0;
for (int i = 0; i < n; i++) {
    long long x = a[i];
    if (seen.count(S - x)) pairs++;
    seen.insert(x);
}"""),
 ("p", "**Meeting in the middle.** If you must match \"something from list A\" with \"something "
       "from list B\", put everything from A into a set (or a map with counts). Then walk B and "
       "look each one up."),
]),

# ---------------------------------------------------------------- 5
("choose", "5. Array, set or map?", [
 ("table", ["The values are...", "and you need...", "Use"], [
   ["small whole numbers (up to about a million)", "counts or marks", "an array: `cnt[x]`"],
   ["huge, negative or words", "only which ones appeared", "`set`"],
   ["huge, negative or words", "how many times each appeared", "`map`"],
 ]),
 ("p", "An array is the fastest. A set or map is a little slower - each step costs about "
       "`log n` - but it works for any values and keeps them sorted."),
]),

]

CHEATSHEET = [
 ("A set of numbers", "`set<int> s;` (`#include <set>`)"),
 ("Add / remove / is it there?", "`s.insert(x)`, `s.erase(x)`, `s.count(x)`"),
 ("How many different values", "insert all, then `s.size()`"),
 ("A map", "`map<string, int> m;` (`#include <map>`)"),
 ("Count with a map", "`m[key]++;`"),
 ("Is the key there?", "`m.count(key)` - not `m[key]`"),
 ("Walk a set in order", "`for (int x : s)`"),
 ("Walk a map in key order", "`for (pair<int, int> p : m)` - key `p.first`, value `p.second`"),
 ("Partner with sum S seen before?", "`seen.count(S - x)`, then `seen.insert(x)`"),
 ("Small numbers", "a plain array is faster than both"),
]

PITFALLS = [
 ("Checking with `m[key]` adds the key.",
  "`if (m[x] > 0)` creates `x` with value 0. The map grows, and `m.size()` becomes wrong. Use "
  "`m.count(x)`."),
 ("A set forgets repeats.",
  "`{5, 5, 5}` becomes `{5}`. If you need to know how many times, use a map with counts."),
 ("Changing `p` in the loop does not change the map.",
  "`for (pair<int, int> p : m) p.second = 0;` changes a copy. Write `m[p.first] = 0;` instead."),
 ("Using a map where an array would do.",
  "For values up to a million, `cnt[x]` is several times faster than `m[x]`. With a lot of "
  "input, that can decide the time limit."),
]

COMPLEXITY = [
 ["`insert`, `erase`, `count` on a set of `n` values", "O(log n)"],
 ["`m[key]`, `m.count(key)` on a map", "O(log n)"],
 ["Walking a whole set or map", "O(n)"],
 ["The same jobs with an array", "O(1) each"],
]

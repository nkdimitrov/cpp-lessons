# -*- coding: utf-8 -*-
"""Lesson 09 - Pairs and structs. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "09_Pairs_And_Structs"
BRAND = "Lesson 09 · Pairs and structs"
FOOTER = ("Lesson 09 · C++17 pairs and structs. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Pairs and structs - keeping things that belong together"
SUBTITLE = ("Lesson 09 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("pair", "1. pair: two values in one", [
 ("p", "Many things come as two numbers that belong together: a row and a column, a start and an "
       "end, a time and a runner's number. A `pair` keeps them together. Its two parts are called "
       "`first` and `second`:"),
 ("code", """pair<int, int> p = {3, 7};
cout << p.first << ' ' << p.second << '\\n';     // 3 7
p.second = 10;                                    // now {3, 10}"""),
 ("p", "An array of pairs keeps one pair per thing. Here `pos[k]` remembers where number `k` "
       "stands on a board:"),
 ("code", """pair<int, int> pos[101];

for (int r = 0; r < 4; r++)
    for (int c = 0; c < 5; c++) {
        int k;
        cin >> k;
        pos[k] = {r, c};          // number k is in row r, column c
    }

// how far apart are the numbers 1 and 2?
int dr = pos[2].first - pos[1].first;
int dc = pos[2].second - pos[1].second;"""),
 ("p", "The two parts may have different types: `pair<string, int>` holds a name and a score."),
]),

# ---------------------------------------------------------------- 2
("pairsort", "2. Sorting pairs", [
 ("p", "`sort` already knows how to compare pairs: first by `first`; when those are equal, by "
       "`second`. You get a two-rule order for free:"),
 ("code", """pair<int, int> a[5] = {{5, 2}, {3, 9}, {5, 1}, {3, 4}, {1, 8}};
sort(a, a + 5);
// {1, 8} {3, 4} {3, 9} {5, 1} {5, 2}"""),
 ("p", "So put the most important rule in `first`. A very common trick: store the **value** in "
       "`first` and the **original number** in `second`. After sorting you still know who is who, "
       "and equal values come out in the order of their numbers:"),
 ("code", """pair<int, int> r[100005];         // (time, runner's number)
for (int i = 0; i < n; i++) {
    int t;
    cin >> t;
    r[i] = {t, i + 1};
}
sort(r, r + n);
cout << "the winner is runner " << r[0].second << '\\n';"""),
 ("note", "Want the largest value first but the smaller number on ties? Store `-value` in `first`. "
          "Then a plain `sort` does both jobs."),
]),

# ---------------------------------------------------------------- 3
("struct", "3. struct: your own record", [
 ("p", "When a thing has more than two parts, or the parts deserve real names, make your own type "
       "with `struct`. Write it above `main`:"),
 ("code", """struct Site {
    int num;          // the site's number
    int depth;
    int width;
};                    // note the semicolon

Site s[1005];

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        s[i].num = i + 1;
        cin >> s[i].depth >> s[i].width;
    }
}"""),
 ("p", "`s[i].depth` reads as \"the depth of site i\". This is much easier to read than three "
       "separate arrays, and the parts can never get out of step."),
]),

# ---------------------------------------------------------------- 4
("structsort", "4. Sorting structs by several rules", [
 ("p", "`sort` does not know how to compare two `Site`s, so you tell it with a compare function, "
       "exactly as in lesson 08. Check the rules one after another:"),
 ("code", """// deeper first; equal depth: wider first; still equal: smaller number first
bool cmp(Site x, Site y) {
    if (x.depth != y.depth) return x.depth > y.depth;
    if (x.width != y.width) return x.width > y.width;
    return x.num < y.num;
}

sort(s, s + n, cmp);"""),
 ("p", "Every rule except the last one has the form *if they differ, decide by this*. The last rule "
       "decides everything that is left."),
]),

# ---------------------------------------------------------------- 5
("return", "5. A function that gives back two things", [
 ("p", "A function can return only one value. Return a pair - or a struct - and it gives back "
       "as many as you need:"),
 ("code", """// numbers 1, 2, 3, ... fill a grid with m columns, row by row
pair<int, int> place(int k, int m) {
    int row = (k - 1) / m;
    int col = (k - 1) % m;
    return {row, col};
}

pair<int, int> p = place(7, 3);
cout << p.first << ' ' << p.second << '\\n';     // 2 0"""),
]),

]

CHEATSHEET = [
 ("Make a pair", "`pair<int, int> p = {3, 7};`"),
 ("Its two parts", "`p.first`, `p.second`"),
 ("Array of pairs", "`pair<int, int> a[100005];` and `a[i] = {x, y};`"),
 ("Sort pairs", "`sort(a, a + n)` - by `first`, then by `second`"),
 ("Remember who is who", "`{value, number}`, then sort"),
 ("Largest first, ties by number", "store `{-value, number}`"),
 ("Your own type", "`struct Name { int a; int b; };` above `main`"),
 ("Use a part", "`s[i].depth`"),
 ("Sort structs", "`bool cmp(Site x, Site y)` with one `if` per rule; `sort(s, s + n, cmp)`"),
 ("Return two values", "`pair<int, int> f(...) { return {a, b}; }`"),
]

PITFALLS = [
 ("Forgetting the semicolon after a struct.",
  "`struct Site { ... };` - without the `;` the compiler reports a confusing error a few lines "
  "further down."),
 ("The important rule in `second`.",
  "Pairs sort by `first` first. If you want to sort by time, the time must be in `first`."),
 ("Sorting structs without a compare function.",
  "`sort(s, s + n)` on a struct does not compile. Give it `cmp`."),
 ("A missing tie rule.",
  "If two records are equal by every rule you wrote, their order is not fixed. When the statement "
  "says \"on a tie, the smaller number first\", that is one more rule."),
 ("`first` and `second` mixed up.",
  "Write a comment next to the array: `// (time, number)`. It saves a lot of guessing later."),
]

COMPLEXITY = [
 ["Reading or changing `p.first`, `s[i].depth`", "O(1)"],
 ["Comparing two pairs", "O(1)"],
 ["Sorting `n` pairs or structs", "O(n log n)"],
]

# -*- coding: utf-8 -*-
"""Lesson 06 - Counting arrays. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "06_Counting_Arrays"
BRAND = "Lesson 06 · Counting arrays"
FOOTER = ("Lesson 06 · C++17 counting and frequency arrays. Problem links point to "
          "arena.olimpiici.com; statements are in Bulgarian and downloadable as PDF from each "
          "problem page.")

TITLE = "C++17 Counting arrays - one box per value"
SUBTITLE = ("Lesson 06 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("boxes", "1. One box per value", [
 ("p", "In lesson 04 the box number was a place in a row. Here the box number is the **value** "
       "itself. Box `x` counts how many times `x` has been seen:"),
 ("code", """int cnt[10];                     // outside main, so all 0

int main() {
    string s;                    // a long number, digit by digit
    cin >> s;
    for (char c : s) cnt[c - '0']++;

    for (int d = 0; d <= 9; d++)
        if (cnt[d] > 1) cout << d << " appears " << cnt[d] << " times\\n";
}"""),
 ("p", "One pass fills the boxes. After that, every question \"how many times did x appear?\" "
       "costs one look: `cnt[x]`."),
]),

# ---------------------------------------------------------------- 2
("size", "2. How many boxes?", [
 ("p", "You need one box for every value that can appear. If the values go from 0 to 1000, make "
       "1001 boxes - the last one is box 1000:"),
 ("code", """int cnt[1001];                   // values 0 ... 1000"""),
 ("list", ["The values must be **whole numbers** and not too big. A million boxes is fine; a "
           "billion is not.",
           "If values can be negative, shift them. For values from -500 to 500 use "
           "`cnt[x + 500]`.",
           "If values are huge (say up to 10^9) but there are few of them, a counting array will "
           "not fit. Lesson 11 shows `map` for that."]),
]),

# ---------------------------------------------------------------- 3
("mark", "3. Marking: seen or not seen", [
 ("p", "Sometimes you only need to know **whether** a value appeared. A `bool` array is enough:"),
 ("code", """bool seen[1001];                 // all false

int distinct = 0;
for (int i = 0; i < n; i++) {
    if (!seen[a[i]]) distinct++;    // a new value
    seen[a[i]] = true;
}"""),
 ("p", "Marking answers questions about **other** values in one step. Is there an earlier number "
       "that adds up with `x` to `S`? Look up `S - x` before marking `x`:"),
 ("code", """int pairs = 0;
for (int i = 0; i < n; i++) {
    int x = a[i];
    if (S - x >= 0 && S - x <= 1000 && seen[S - x]) pairs++;
    seen[x] = true;
}"""),
 ("p", "And once the values are marked, walking along the boxes shows them **in order**. The "
       "longest run of marked boxes is the longest stretch of consecutive values."),
]),

# ---------------------------------------------------------------- 4
("most", "4. The commonest value, and counting pairs", [
 ("p", "The value seen most often is the box with the biggest count:"),
 ("code", """int best = 0;
for (int v = 1; v <= 1000; v++)
    if (cnt[v] > cnt[best]) best = v;      // ties go to the smaller value"""),
 ("p", "How many pairs of **equal** values are there? A box with `c` equal values gives "
       "`c * (c - 1) / 2` pairs, because each of the `c` values pairs with each of the other "
       "`c - 1`, and that counts every pair twice:"),
 ("code", """long long pairs = 0;
for (int v = 0; v <= 1000; v++)
    pairs += 1LL * cnt[v] * (cnt[v] - 1) / 2;"""),
]),

# ---------------------------------------------------------------- 5
("sofar", "5. Counting as you go", [
 ("p", "Fill the boxes **while** walking, and each box tells you how many times a value appeared "
       "*before* the current place. That counts pairs in a single pass:"),
 ("code", """long long pairs = 0;
for (int i = 0; i < n; i++) {
    pairs += cnt[a[i]];          // every earlier equal value makes a pair with a[i]
    cnt[a[i]]++;                 // now count a[i] itself
}"""),
 ("p", "Walk from the right instead, with a second array, and you know how many equal values come "
       "*after* each place."),
]),

# ---------------------------------------------------------------- 6
("csort", "6. Printing in order from the boxes", [
 ("p", "Walk the boxes from the smallest value to the largest and print each value as many times "
       "as it was counted. The numbers come out sorted. This is called **counting sort**:"),
 ("code", """for (int v = 0; v <= 1000; v++)
    for (int k = 0; k < cnt[v]; k++)
        cout << v << ' ';"""),
 ("p", "The same walk finds the k-th smallest value without storing the numbers at all: keep "
       "subtracting counts until `k` is used up."),
 ("code", """int k;                           // the k-th smallest, counting from 1
cin >> k;
for (int v = 0; v <= 1000; v++) {
    if (k <= cnt[v]) { cout << v << '\\n'; break; }
    k -= cnt[v];
}"""),
]),

]

CHEATSHEET = [
 ("Count every value", "`cnt[x]++;` with `int cnt[1001];` outside `main` - one box more than the largest value"),
 ("Count digits / small letters", "`cnt[c - '0']++` / `cnt[c - 'a']++`"),
 ("Negative values from -500", "`cnt[x + 500]++`"),
 ("Was `x` seen?", "`bool seen[1001];` then `seen[x] = true;`"),
 ("How many different values", "count the first time each `seen[x]` becomes true"),
 ("Commonest value", "the box with the biggest `cnt`"),
 ("Pairs of equal values", "`c * (c - 1) / 2` for each box"),
 ("Equal values before place i", "`pairs += cnt[a[i]]; cnt[a[i]]++;`"),
 ("Print sorted", "walk `v` upwards, print `v` `cnt[v]` times"),
 ("k-th smallest", "walk `v` upwards, subtract `cnt[v]` from `k`"),
]

PITFALLS = [
 ("One box too few.",
  "Values up to 1000 need `cnt[1001]`. `cnt[1000]` has no box 1000."),
 ("Negative values as an index.",
  "`cnt[-3]` is outside the array. Shift every value by the same amount first."),
 ("A counting array for huge values.",
  "`int cnt[1000000000];` does not fit in memory. Use a map (lesson 11) or sort the values."),
 ("Forgetting to reset between tests.",
  "Counts left over from the previous test give wrong answers. Set the boxes back to 0."),
 ("Pairs overflow.",
  "`c * (c - 1) / 2` for c = 100000 is about 5 billion. Use `long long`."),
]

COMPLEXITY = [
 ["Filling the boxes for `n` values", "O(n)"],
 ["Looking up `cnt[x]` or `seen[x]`", "O(1)"],
 ["Walking all the boxes", "O(number of possible values)"],
 ["Counting sort", "O(n + number of possible values)"],
]

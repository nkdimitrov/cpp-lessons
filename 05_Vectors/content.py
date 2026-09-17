# -*- coding: utf-8 -*-
"""Lesson 05 - Vectors. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "05_Vectors"
BRAND = "Lesson 05 · Vectors"
FOOTER = ("Lesson 05 · C++17 vectors. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

PITFALLS_TITLE = "Eleven pitfalls that cost real marks"

TITLE = "C++17 Vectors - a row of boxes that can change length"
SUBTITLE = ("Lesson 05 | Theory, cheat sheet and 24 graded problems "
            "from arena.olimpiici.com (Groups D and C)")

HOWTO = [
    "This lesson is built to be worked through in three passes. Do not try to do all three in one "
    "sitting.",
    "**Pass 1 - Read.** Go through sections 1-11 once, typing every snippet into a compiler and "
    "running it. Change a number, run it again, see what happens. Do not try to memorise anything "
    "yet; the aim is only to know what exists and where to find it later.",
    "**Pass 2 - Memorise.** Section 12 is the cheat sheet. Cover the right-hand column and write "
    "out each line from its description alone. Repeat until they all come out without thinking. "
    "Section 13 lists the mistakes that cost marks, and section 14 says how fast each operation is.",
    "**Pass 3 - Solve.** Section 15 lists 24 problems from the Olimpiici Arena, ordered from "
    "easiest to hardest and grouped by technique. Solve them in order. Each group points back at "
    "the theory sections that solve it, so when a problem stalls you, re-read that section instead "
    "of looking up a solution.",
    "Lesson 04 left one question open. An array has to be given its size before the program is "
    "compiled, and it can never grow. This lesson is the answer to that, and almost everything you "
    "learned about arrays carries straight over - the same indexing, the same scans, the same "
    "off-by-one traps.",
]

SECTIONS = [

# ---------------------------------------------------------------- 1
("setup", "1. Getting started: headers and fast input", [
 ("p", "Every program in this lesson begins the same way. These headers cover everything the lesson "
       "uses, so include them all at the top."),
 ("code", """#include <iostream>
#include <vector>       // vector
#include <string>       // string
#include <algorithm>    // sort, reverse, count, max_element, unique, remove

using namespace std;"""),
 ("p", "`cin` and `cout` are slow out of the box, because they keep themselves in step with the "
       "older C functions `scanf` and `printf`. A problem that reads 200000 numbers can run out of "
       "time for that reason alone. Switch the syncing off with two lines at the start of `main`:"),
 ("code", """int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    // your solution goes here
}"""),
 ("note", "Two rules come with those two lines. Do not mix `cin`/`cout` with `scanf`/`printf` in the "
          "same program - pick one. And print `'\\n'` instead of `endl`: `endl` empties the output "
          "buffer after every single line, which on its own is enough to fail a time limit."),
]),

# ---------------------------------------------------------------- 2
("why", "2. Why a vector exists", [
 ("p", "In Lesson 04 every array had to be declared like this, and the number in the brackets had to "
       "be there before the program was compiled:"),
 ("code", """const int MAXN = 200005;
int a[MAXN];"""),
 ("p", "That works, but it forces two compromises. If the statement says nothing about the size, you "
       "have to guess, and a guess that is too small is a crash while a guess that is too large "
       "wastes memory. And once the row exists it can never get longer, so a problem whose answer is "
       "\"a list of things, and you will not know how many until you have found them\" has nowhere "
       "to put them."),
 ("p", "A **vector** is a row of boxes that can change its length while the program is running. "
       "Everything else about it is the same picture as an array: the boxes lie next to each other, "
       "they all hold the same type, and they are numbered from 0."),
 ("code", """vector<int> v;        // a row with no boxes at all, for now

v.push_back(3);       // 3
v.push_back(1);       // 3 1
v.push_back(4);       // 3 1 4

cout << v.size();     // 3    - and it knows this by itself
cout << v[0];         // 3    - indexing is exactly as before"""),
 ("p", "Three things the vector can do that the array could not:"),
 ("table", ["Question", "Array", "Vector"], [
   ["Size decided while running?", "no", "`vector<int> v(n);`"],
   ["Can it get longer?", "no", "`v.push_back(x);`"],
   ["Does it know its own length?", "no - you carry `n`", "`v.size()`"],
   ["Copy the whole thing", "a loop", "`vector<int> w = v;`"],
   ["Compare two of them", "a loop", "`v == w`"],
   ["Give it to a function", "only the address goes", "the whole thing is **copied** - see section 6"],
 ]),
 ("note", "The last row is the one that costs marks. An array was free to pass because only its "
          "address travelled. A vector is copied, box by box, every single time - which is fine once "
          "and a disaster inside a loop. Section 6 is about nothing else."),
]),

# ---------------------------------------------------------------- 3
("make", "3. Making a vector", [
 ("p", "The forms worth knowing. The second one is the reason the lesson exists: `n` may be a number "
       "that was only just read from the input."),
 ("code", """vector<int> a;                 // 0 boxes
vector<int> b(5);              // 5 boxes, all 0      <- note: not rubbish
vector<int> c(5, 7);           // 5 boxes, all 7
vector<int> d = {3, 1, 4};     // 3 boxes: 3 1 4
vector<int> e = d;             // an independent copy of d

vector<long long> f(n);        // any type goes in the angle brackets (n was read above)
vector<string> words(3);       // three empty strings
vector<double> g(4, 0.5);"""),
 ("note", "`vector<int> b(5);` gives five zeros, but `int b[5];` gives five pieces of rubbish. "
          "**That alone removes a whole class of bug from Lesson 04.** Round brackets mean \"this many "
          "boxes\"; curly brackets mean \"these values\", so `vector<int> v{5}` is **one** box "
          "holding 5, not five boxes. Read that line twice - it is the single most confusing pair in "
          "the language."),
 ("p", "The shape almost every solution in section 15 begins with:"),
 ("code", """int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> v(n);                            // exactly n boxes, not MAXN
    for (int i = 0; i < n; i++) cin >> v[i];
}"""),
 ("h3", "Changing the length later"),
 ("code", """vector<int> v(3, 1);      // 1 1 1
v.resize(5);              // 1 1 1 0 0    new boxes are 0
v.resize(5, -1);          // if it had grown here, the new boxes would be -1
v.resize(2);              // 1 1          the extra boxes are thrown away
v.clear();                //              length 0 again
cout << v.empty();        // 1 = true"""),
 ("note", "After `clear()` the vector has no boxes, so `v[0]` is out of bounds and `v.back()` is a "
          "crash waiting to happen. When a problem has several test cases, either `clear()` and "
          "`push_back` again, or make a fresh vector for each case - do not reuse the old length."),
]),

# ---------------------------------------------------------------- 4
("grow", "4. Growing it: push_back, pop_back, back", [
 ("p", "`push_back` adds one box on the right-hand end. `back()` is the value in the last box, and "
       "`pop_back()` throws that box away. Those three are most of what you will use."),
 ("code", """vector<int> v;             //
v.push_back(3);            // 3
v.push_back(1);            // 3 1
v.push_back(4);            // 3 1 4

cout << v.size();          // 3
cout << v.back();          // 4        the last value
cout << v.front();         // 3        the first value

v.pop_back();              // 3 1      pop_back gives nothing back - read back() first
cout << v.size();          // 2"""),
 ("note", "`pop_back()` **returns nothing**. If you want the last value and also want it gone, read "
          "`v.back()` into a variable first, then call `v.pop_back()`. And never call `back()`, "
          "`front()` or `pop_back()` on an empty vector - check `v.empty()` when you are not sure."),
 ("h3", "Reading a list whose length is not given"),
 ("p", "This is the pattern that an array simply cannot do. The input just ends, and the vector ends "
       "up exactly the right size:"),
 ("code", """vector<int> v;
int x;
while (cin >> x) v.push_back(x);

int n = v.size();          // now you know how many there were"""),
 ("h3", "Why push_back is cheap"),
 ("p", "A vector keeps a little spare room on the end. When the spare room runs out it quietly moves "
       "every box to a bigger home, with twice as much room as before. That move costs O(n), but it "
       "happens so rarely - after 1 box, 2, 4, 8, 16 - that spread over all the calls each "
       "`push_back` costs a constant amount of time. Pushing a million values one at a time is "
       "entirely normal and entirely fast."),
]),

# ---------------------------------------------------------------- 5
("walk", "5. Walking a vector", [
 ("p", "All four ways from Lesson 03 work unchanged, and you should recognise every one of them in "
       "other people's code:"),
 ("code", """vector<int> v = {3, 1, 4, 1, 5};
int n = v.size();

for (int i = 0; i < n; i++)      cout << v[i];    // by position
for (int x : v)                  cout << x;       // every value, read only
for (int& x : v)                 x *= 2;          // the & lets you change it
for (int i = n - 1; i >= 0; i--) cout << v[i];    // backwards"""),
 ("note", "`v.size()` is an **unsigned** number, exactly like `s.size()` was. On an empty vector "
          "`v.size() - 1` is not -1, it is a gigantic number, and `for (int i = 0; i < v.size() - 1; "
          "i++)` loops almost for ever. The cure is the same habit: write `int n = v.size();` on the "
          "line before the loop and compare against `n`."),
 ("p", "The `&` in `for (int& x : v)` is worth a second look. Without it you get a copy of each "
       "value, so changing `x` changes nothing. With it, `x` *is* the box, and writing to it writes "
       "into the vector:"),
 ("code", """vector<int> v = {1, 2, 3};

for (int x : v)  x = 0;      // v is still 1 2 3   - x was only a copy
for (int& x : v) x = 0;      // v is now  0 0 0"""),
 ("p", "The reaching members are the same ones a string had:"),
 ("table", ["Member", "What it does", "Cost"], [
   ["`v.size()`", "How many boxes there are.", "O(1)"],
   ["`v.empty()`", "`true` when there are none. Prefer it to `v.size() == 0`.", "O(1)"],
   ["`v[i]`", "The box at position `i`. **Does not check** that it exists.", "O(1)"],
   ["`v.front()` / `v.back()`", "First / last value. Never on an empty vector.", "O(1)"],
   ["`v.clear()`", "Throws every box away.", "O(n)"],
 ]),
]),

# ---------------------------------------------------------------- 6
("pass", "6. Giving a vector to a function - the copy trap", [
 ("p", "This is the most expensive single mistake in the lesson, and it does not look like a mistake "
       "at all. Written the obvious way, a function that takes a vector **copies every box of it, "
       "every time it is called**."),
 ("code", """long long total(vector<int> v) {          // SLOW: the whole vector is copied
    long long s = 0;
    for (int x : v) s += x;
    return s;
}"""),
 ("p", "Call that once on a vector of a million values and you pay for a million copies. Call it "
       "inside a loop that runs a thousand times and you pay a thousand million - a time limit "
       "failure with a completely correct answer. The cure is one character:"),
 ("code", """long long total(const vector<int>& v) {   // FAST: nothing is copied
    long long s = 0;
    for (int x : v) s += x;
    return s;
}"""),
 ("p", "The `&` says \"work on the caller's vector, do not make a copy\". The `const` says \"and I "
       "promise not to change it\", which lets the compiler stop you if you try. Three forms, and "
       "you should know which one you want before you type the brackets:"),
 ("table", ["How you write it", "What happens", "Use it when"], [
   ["`f(vector<int> v)`", "the whole vector is copied", "almost never"],
   ["`f(const vector<int>& v)`", "no copy; the function may only read", "the function only looks at it"],
   ["`f(vector<int>& v)`", "no copy; the function may change it", "the function has to change it"],
 ]),
 ("code", """void double_all(vector<int>& v) {        // no const - it changes the vector
    int n = v.size();
    for (int i = 0; i < n; i++) v[i] *= 2;
}

int main() {
    vector<int> v = {1, 2, 3};
    double_all(v);
    cout << v[0] << ' ' << v[1] << ' ' << v[2];   // 2 4 6
}"""),
 ("note", "Returning a vector from a function is fine and costs nothing extra - the compiler hands "
          "the result straight over instead of copying it. It is only the **parameters** that need "
          "the `&`."),
]),

# ---------------------------------------------------------------- 7
("build", "7. Building a new vector from an old one", [
 ("p", "Lesson 04 ended with the rule \"when several boxes have to go, build a new array instead of "
       "deleting them one at a time\". With a vector that rule becomes a three-line habit, and you "
       "no longer have to carry a separate count:"),
 ("code", """vector<int> keep;
for (int x : v)
    if (x % 2 == 0) keep.push_back(x);      // the rule for keeping a value

cout << keep.size() << '\\n';                // however many there turned out to be"""),
 ("h3", "The answer whose length you do not know"),
 ("p", "Many statements ask for \"all the values that ...\", and want the count printed first. "
       "Collect into a vector, then print - you never have to work out the count in advance:"),
 ("code", """vector<int> answer;
for (int i = 0; i < n; i++)
    if (v[i] > 0) answer.push_back(i + 1);        // 1-based, as statements usually number things

cout << answer.size() << '\\n';
for (int i = 0; i < (int)answer.size(); i++) {
    if (i > 0) cout << ' ';
    cout << answer[i];
}
cout << '\\n';"""),
 ("note", "`(int)answer.size()` turns the unsigned length into an ordinary `int` so that the "
          "comparison behaves. Writing `int m = answer.size();` before the loop does the same job "
          "and reads better - use whichever you will remember."),
 ("h3", "Two vectors from one"),
 ("p", "Splitting into two groups is the same idea twice over, in one pass:"),
 ("code", """vector<int> small, large;
for (int x : v) {
    if (x < 100) small.push_back(x);
    else         large.push_back(x);
}"""),
]),

# ---------------------------------------------------------------- 8
("algo", "8. Sorting, and the ready-made tools", [
 ("p", "Everything `<algorithm>` did for a string does the same for a vector. Where a string wrote "
       "`s.begin(), s.end()` and an array wrote `a, a + n`, a vector writes `v.begin(), v.end()`. "
       "Treat it as a fixed phrase meaning **the whole vector**."),
 ("code", """vector<int> v = {3, 1, 4, 1, 5};

sort(v.begin(), v.end());                       // 1 1 3 4 5
reverse(v.begin(), v.end());                    // 5 4 3 1 1

int big  = *max_element(v.begin(), v.end());    // 5
int tiny = *min_element(v.begin(), v.end());    // 1
int ones = count(v.begin(), v.end(), 1);        // 2"""),
 ("p", "You may sort only a part of it. `v.begin() + 2` means \"position 2\", so this sorts the boxes "
       "from 2 up to but not including 5:"),
 ("code", """sort(v.begin() + 2, v.begin() + 5);
reverse(v.begin() + 2, v.begin() + 5);"""),
 ("h3", "Sorting by your own rule"),
 ("p", "`sort` normally puts the smallest first. To use a different order, write an ordinary "
       "function that answers one question - *does `a` belong before `b`?* - and hand its name to "
       "`sort`:"),
 ("code", """bool bigger_first(int a, int b) {
    return a > b;                 // a belongs before b when a is larger
}

sort(v.begin(), v.end(), bigger_first);         // 5 4 3 1 1"""),
 ("note", "The rule must be **strict**: for two equal values it has to answer `false`. Writing "
          "`return a >= b;` looks harmless and makes `sort` crash on large inputs, because it never "
          "stops. Use `>` or `<`, never `>=` or `<=`."),
 ("h3", "Throwing away repeats"),
 ("p", "`unique` only squashes repeats that are **next to each other**, so sort first. And it does "
       "not shorten the vector by itself - it needs the `erase` wrapped round it. Learn the whole "
       "line as one phrase:"),
 ("code", """sort(v.begin(), v.end());
v.erase(unique(v.begin(), v.end()), v.end());   // now every value appears once

cout << v.size();        // how many DISTINCT values there were"""),
 ("p", "That line is worth learning as it stands, but it is also worth knowing what it does. Written "
       "out as a loop it is exactly the neighbour comparison from Lesson 04 - keep a value only the "
       "first time it appears - with a `push_back` in place of the counter:"),
 ("code", """sort(v.begin(), v.end());

vector<int> once;
int n = v.size();
for (int i = 0; i < n; i++)
    if (i == 0 || v[i] != v[i - 1])      // keep it only the first time it appears
        once.push_back(v[i]);

v = once;                                // now every value appears once
cout << v.size();"""),
 ("note", "Both versions do the same job at the same O(n) cost, and both need the sort first - "
          "neither can see past its immediate neighbour. Use the one-liner in a contest because it "
          "is one line, and use the loop whenever the rule for keeping a value is anything more than "
          "\"it differs from the one before it\", because `unique` cannot be told a different rule."),
]),

# ---------------------------------------------------------------- 9
("middle", "9. Inserting and erasing in the middle", [
 ("p", "A vector can take a value in at any position, and drop one from any position. Both are "
       "written with `v.begin() + p`, meaning \"position `p`\"."),
 ("code", """vector<int> v = {3, 1, 4};

v.insert(v.begin() + 1, 9);        // 3 9 1 4      9 becomes v[1]
v.erase(v.begin() + 2);            // 3 9 4        v[2] disappears

v.insert(v.begin(), 0);            // 0 3 9 4      at the very front
v.erase(v.begin() + 1, v.begin() + 3);   // 0 4     erase a stretch"""),
 ("note", "Both cost **O(n)**, because everything to the right of the hole has to shuffle along. One "
          "insert is nothing; an insert inside a loop over `n` values is O(n^2) and will fail on a "
          "large test. Before you write `insert` in a loop, ask whether you could `push_back` and "
          "sort afterwards instead."),
 ("h3", "Do not erase inside a loop over positions"),
 ("p", "Every erase slides the rest of the vector one place to the left, so the next value moves "
       "under your index and is never looked at. This is exactly the bug Lesson 03 warned about with "
       "strings, and Lesson 04 with arrays:"),
 ("code", """// WRONG - skips values
for (int i = 0; i < (int)v.size(); i++)
    if (v[i] == 0) v.erase(v.begin() + i);

// RIGHT - build the vector you want
vector<int> keep;
for (int x : v) if (x != 0) keep.push_back(x);
v = keep;"""),
 ("p", "If you would rather not build a second vector, there is a fixed phrase for \"delete every "
       "copy of one value\", the same shape as the `unique` line:"),
 ("code", """v.erase(remove(v.begin(), v.end(), 0), v.end());   // every 0 is gone"""),
]),

# ---------------------------------------------------------------- 10
("nested", "10. Many lists at once: a vector of vectors", [
 ("p", "A `vector<vector<int>>` is a row of boxes where every box is itself a whole vector. That is "
       "how you keep many separate lists without inventing many separate names - and each of them "
       "grows on its own."),
 ("code", """vector<vector<int>> lists(4);        // four lists, all empty

lists[0].push_back(7);
lists[0].push_back(9);
lists[3].push_back(2);

cout << lists[0].size();             // 2
cout << lists[0][1];                 // 9
cout << lists[2].empty();            // 1 = true, nothing was put in it"""),
 ("h3", "The bucket pattern"),
 ("p", "This is what the whole section is for. When each thing in the input belongs to a group - a "
       "colour, a letter, a day of the week - make one list per group and push each thing into its "
       "own. Afterwards every group is already gathered together:"),
 ("code", """string s;
cin >> s;
int n = s.size();

vector<vector<int>> pos(26);                  // s is all lower-case; pos[c] = where c appears
for (int i = 0; i < n; i++)
    pos[s[i] - 'a'].push_back(i);             // the letter picks its own list

// every place the letter 'a' turned up, in order
for (int i = 0; i < (int)pos[0].size(); i++)
    cout << pos[0][i] << ' ';"""),
 ("note", "Compare this with Lesson 04's `seen[v] = true`. A counting array remembers **how many** of "
          "each value there were; a vector of vectors remembers **which ones, and where**. Reach for "
          "the counting array when a number is enough, and for this when you need the things "
          "themselves."),
 ("h3", "A table whose size comes from the input"),
 ("p", "The same type also gives you a rectangle of numbers, with the row and column counts read at "
       "run time. Read the second line as \"`r` rows, each of them a vector of `c` zeros\":"),
 ("code", """int r, c;
cin >> r >> c;

vector<vector<int>> t(r, vector<int>(c, 0));      // r rows, c columns, all 0

for (int i = 0; i < r; i++)
    for (int j = 0; j < c; j++)
        cin >> t[i][j];"""),
 ("note", "Get the two numbers the wrong way round and the program reads happily for a while and "
          "then crashes somewhere else entirely. Say the line out loud - **rows first, then "
          "columns** - every time you write it. Lesson 07 does grids properly; this is just the "
          "container."),
]),

# ---------------------------------------------------------------- 11
("choose", "11. Vector or array? How to choose", [
 ("p", "The vector can do everything the array can, so it is a reasonable default. The plain array "
       "still wins in a few places, and those places are common enough in contests that you should "
       "know them."),
 ("table", ["Situation", "Use"], [
   ["The size is only known at run time", "vector"],
   ["The list has to grow, or its length is the answer", "vector"],
   ["You need one list per group", "`vector<vector<int>>`"],
   ["A fixed size, given in the statement, and a tight time limit", "a global array"],
   ["A flag or counting array over a huge range of values", "a global array - it is zero-filled free"],
   ["The function is called many times", "either, but pass it as `const vector<int>&`"],
 ]),
 ("p", "The honest summary: a vector costs a very small amount of extra time for the bookkeeping, "
       "and in return you stop guessing sizes and stop carrying `n` about. For the problems in "
       "section 15 that trade is always worth taking. When a later lesson needs a two-million-box "
       "counting array that must be cleared between test cases, the global array comes back."),
 ("note", "One thing to know rather than to use: `vector<bool>` is a special case. To save memory it "
          "packs eight values into each byte, which makes it behave oddly in places the other "
          "vectors do not - `for (bool& b : v)` will not even compile. If you want a row of flags "
          "and anything surprises you, write `vector<char>` instead and store 0 and 1."),
]),

]

# ---------------------------------------------------------------- 12
CHEATSHEET = [
 ("Include it", "`#include <vector>`"),
 ("Empty vector", "`vector<int> v;`"),
 ("n boxes, all zero", "`vector<int> v(n);`"),
 ("n boxes, all x", "`vector<int> v(n, x);`"),
 ("Given values", "`vector<int> v = {3, 1, 4};`"),
 ("Careful", "`v(5)` is five boxes; `v{5}` is one box holding 5"),
 ("Copy one", "`vector<int> w = v;` - a real, independent copy"),
 ("How long is it", "`v.size()`, `v.empty()`"),
 ("Reach a value", "`v[i]`, `v.front()`, `v.back()`"),
 ("Add to the end", "`v.push_back(x);`"),
 ("Remove from the end", "`v.pop_back();` - it returns nothing"),
 ("Change the length", "`v.resize(m);`, `v.clear();`"),
 ("Read n values", "`vector<int> v(n); for (...) cin >> v[i];`"),
 ("Read until the input ends", "`int x; while (cin >> x) v.push_back(x);`"),
 ("The whole vector, for `<algorithm>`", "`v.begin(), v.end()`"),
 ("Position p, for `<algorithm>`", "`v.begin() + p`"),
 ("Walk it", "`for (int x : v)` - add `&` when you need to change it"),
 ("Sum", "`long long s = 0; for (int x : v) s += x;` - **never an int**"),
 ("Largest / smallest", "`*max_element(v.begin(), v.end())`"),
 ("Count one value", "`count(v.begin(), v.end(), x)`"),
 ("Sort / reverse", "`sort(v.begin(), v.end());`, `reverse(v.begin(), v.end());`"),
 ("Sort part of it", "`sort(v.begin() + i, v.begin() + j);`"),
 ("Sort by your own rule", "a `bool` function of two values, then `sort(v.begin(), v.end(), rule);`"),
 ("Remove repeats", "`sort(...)` then `v.erase(unique(v.begin(), v.end()), v.end());`"),
 ("Delete every copy of x", "`v.erase(remove(v.begin(), v.end(), x), v.end());`"),
 ("Insert at position p", "`v.insert(v.begin() + p, x);` - O(n)"),
 ("Erase position p", "`v.erase(v.begin() + p);` - O(n)"),
 ("Keep only some values", "`vector<int> keep; ... keep.push_back(x);` then `v = keep;`"),
 ("Give it to a function", "`f(const vector<int>& v)` - **always by reference**"),
 ("Let the function change it", "`f(vector<int>& v)`"),
 ("Many lists at once", "`vector<vector<int>> lists(k);` then `lists[key].push_back(x);`"),
 ("A table r by c", "`vector<vector<int>> t(r, vector<int>(c, 0));`"),
]

# ---------------------------------------------------------------- 13
PITFALLS = [
 ("Passing a vector without the `&` copies every box of it.",
  "`f(vector<int> v)` copies; `f(const vector<int>& v)` does not. Inside a loop the difference is a "
  "correct solution that fails on time. This is the single most common vector mistake."),
 ("`vector<int> v{5};` is one box holding 5.",
  "Round brackets mean *how many boxes*, curly brackets mean *which values*. `vector<int> v(5);` is "
  "the five zeros you wanted."),
 ("`v[i]` never makes the vector longer.",
  "Writing `v[5]` on a vector of length 3 does not add boxes - it writes somewhere it should not, "
  "and the program misbehaves later, somewhere else. To make it longer use `push_back` or `resize`."),
 ("`v.size()` is unsigned.",
  "On an empty vector `v.size() - 1` is a gigantic number, not -1. Write `int n = v.size();` before "
  "the loop, or `(int)v.size()` inside the comparison."),
 ("`front()`, `back()` and `pop_back()` on an empty vector.",
  "None of them check. Test `v.empty()` first whenever the vector might have been cleared or fully "
  "popped."),
 ("Erasing inside a loop over positions skips values.",
  "Each erase slides the rest one place left, so the next value moves under your index. Build the "
  "vector you want with `push_back` instead."),
 ("`insert` and `erase` in the middle cost O(n) each.",
  "In a loop that is O(n^2). For 200000 values that is forty thousand million operations - far past "
  "any time limit. Push to the end and sort afterwards where you can."),
 ("A comparison rule that answers `true` for equal values crashes `sort`.",
  "`return a >= b;` is not a valid order and sends `sort` past the end of the vector on large "
  "inputs. Always `>` or `<`."),
 ("`unique` does not shorten anything by itself.",
  "It needs a sort before it and an `erase` around it: "
  "`v.erase(unique(v.begin(), v.end()), v.end());`"),
 ("`vector<vector<int>> g;` has no rows at all.",
  "`g[0]` is already out of bounds. Give it a size - `vector<vector<int>> g(n);` - or `push_back` "
  "whole rows into it."),
 ("Rows and columns the wrong way round.",
  "`vector<vector<int>> t(r, vector<int>(c));` is `r` rows of `c` values. Swap them and the program "
  "runs for a while before crashing somewhere unrelated."),
]

# ---------------------------------------------------------------- 14
COMPLEXITY = [
 ["`v[i]` - read or write one box", "O(1)"],
 ["`size`, `empty`, `front`, `back`", "O(1)"],
 ["`push_back`, `pop_back`", "O(1) on average"],
 ["`vector<int> v(n);`", "O(n)"],
 ["`resize`, `clear`", "O(n)"],
 ["Copying a vector, or passing it without `&`", "O(n) - **every single call**"],
 ["Passing it as `const vector<int>&`", "O(1)"],
 ["`insert` or `erase` in the middle", "O(n)"],
 ["`insert` or `erase` inside a loop", "O(n^2) - look for another way"],
 ["`v == w`", "O(n)"],
 ["`sort(v.begin(), v.end())`", "O(n log n)"],
 ["`reverse`, `count`, `max_element`, `min_element`", "O(n)"],
 ["`unique` after a sort", "O(n)"],
 ["Building a new vector with `push_back`", "O(n)"],
 ["`lists[key].push_back(x)` over n values", "O(n) in total"],
]

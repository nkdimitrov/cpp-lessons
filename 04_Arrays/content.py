# -*- coding: utf-8 -*-
"""Lesson 04 - Arrays. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "04_Arrays"
BRAND = "Lesson 04 · Arrays"
FOOTER = ("Lesson 04 · C++17 arrays. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

PITFALLS_TITLE = "Eleven pitfalls that cost real marks"

TITLE = "C++17 Arrays - fixed storage and the loop patterns"
SUBTITLE = ("Lesson 04 | Theory, cheat sheet and 24 graded problems "
            "from arena.olimpiici.com (Group D, with four from Group C)")

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
    "You already know strings from Lesson 03. An array is the same picture - a row of numbered "
    "boxes - but the boxes may hold anything, and the row can never grow. Most of the tricks from "
    "the strings lesson come back here almost unchanged.",
]

SECTIONS = [

# ---------------------------------------------------------------- 1
("setup", "1. Getting started: headers and fast input", [
 ("p", "Every program in this lesson begins the same way. These headers cover everything the lesson "
       "uses, so include them all at the top."),
 ("code", """#include <iostream>
#include <string>       // string
#include <algorithm>    // sort, reverse, rotate, count, max_element, fill, swap
#include <cstdlib>      // abs

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
("what", "2. What an array is", [
 ("p", "A string is a row of characters. An **array** is the same picture for anything else: a row "
       "of boxes, all holding the same kind of value, sitting next to each other in memory and "
       "numbered from 0."),
 ("code", """int a[5];       // five boxes, each one holding an int

//  index:     0     1     2     3     4
//  box:     a[0]  a[1]  a[2]  a[3]  a[4]

a[0] = 7;
a[4] = 2;
cout << a[0] + a[4];     // 9"""),
 ("p", "Three rules follow from that picture, and nearly every mistake in this lesson comes from "
       "forgetting one of them."),
 ("list", [
   "**The numbering starts at 0.** An array of `n` boxes has its last box at index `n - 1`, never at "
   "`n`. Writing `a[n]` already reaches one box past the end.",
   "**The size is fixed when the program is compiled.** `int a[5];` will have five boxes for ever. "
   "You cannot lengthen it later, and you cannot ask the user how big it ought to be.",
   "**The array does not know its own size.** There is no `a.size()`. You read `n` from the input "
   "and you carry `n` about yourself, in a separate variable, for the rest of the program.",
 ]),
 ("p", "That last rule is the real difference from a `string`. Compare the two:"),
 ("table", ["Question", "String", "Array"], [
   ["How long is it?", "`s.size()`", "you remember it, in your own `n`"],
   ["Reach one element", "`s[i]`", "`a[i]` - exactly the same"],
   ["Can it grow?", "yes, `s += c`", "no, never"],
   ["Copy the whole thing", "`string t = s;`", "a loop, one box at a time"],
   ["Compare two of them", "`s == t`", "a loop, one box at a time"],
   ["Give it to a function", "the whole string goes", "only its address goes - see section 10"],
 ]),
 ("p", "The type in the boxes may be anything, as long as every box has the same type:"),
 ("code", """int      a[100];       // whole numbers
long long b[100];      // whole numbers that may pass 2 000 000 000
double   c[100];       // numbers with a decimal point
bool     used[100];    // true / false flags
char     g[100];       // characters
string   names[100];   // yes, an array of strings is allowed too"""),
 ("note", "`int n; cin >> n; int a[n];` looks reasonable and even compiles on g++, but it is not "
          "standard C++ - it is an extension the compiler allows, and it can blow the stack when `n` "
          "is large. Declare the array at its maximum size instead, as section 3 shows, and use only "
          "the first `n` boxes."),
]),

# ---------------------------------------------------------------- 3
("make", "3. Making an array and filling it", [
 ("p", "The ways to make one. Read the comments carefully - the difference between the first two "
       "lines has cost more marks than any other line in this lesson."),
 ("code", """int a[5];                 // five boxes of RUBBISH - whatever was in that memory
int b[5] = {};            // 0 0 0 0 0      empty braces means all zero
int c[5] = {0};           // 0 0 0 0 0      the same thing
int d[5] = {3, 1, 4};     // 3 1 4 0 0      the rest are filled with zero
int e[]  = {3, 1, 4};     // size 3         the compiler counts them for you

bool seen[5] = {};        // false false false false false
double f[3]  = {};        // 0.0 0.0 0.0"""),
 ("note", "An uninitialised local array holds rubbish, not zeros. If a program gives the right answer "
          "on your machine and a wrong one on the judge, an array you forgot to clear is the first "
          "thing to suspect."),
 ("h3", "Where you declare it matters"),
 ("p", "An array declared **inside** a function lives on the stack, and the stack is small - about "
       "1 MB on a typical judge. An array declared **outside** every function is global: it lives "
       "somewhere far roomier, and it comes filled with zeros for free."),
 ("code", """const int MAXN = 200005;
int a[MAXN];              // global: fine, and already all zeros

int main() {
    int small[1000];      // fine on the stack
    // int big[200005];   // crashes on many judges - too large for the stack
}"""),
 ("p", "So the contest habit is: **declare big arrays globally, at the maximum size the statement "
       "allows, plus a few spare boxes.** If the statement says `N <= 200000`, write `MAXN = 200005`. "
       "The five spare boxes cost nothing, and they absorb an off-by-one mistake instead of letting "
       "it crash the program."),
 ("table", ["Type", "Boxes that fit on the stack (about 1 MB)", "Boxes that are safe globally"], [
   ["`bool`, `char` (1 byte)", "about 1 000 000", "tens of millions"],
   ["`int` (4 bytes)", "about 250 000", "a few million"],
   ["`long long`, `double` (8 bytes)", "about 125 000", "a couple of million"],
 ]),
 ("h3", "Refilling an array"),
 ("p", "When the input holds several test cases you must clear the array between them. Two ways, "
       "and they do exactly the same job:"),
 ("code", """int a[MAXN];
int n = 10;

for (int i = 0; i < n; i++) a[i] = 0;   // always correct, always clear
fill(a, a + n, 7);                      // the same thing in one line, any value"""),
 ("note", "Clear only the part you used. Clearing all `MAXN` boxes of a two-million-box array, inside "
          "a loop over 1000 test cases, is two thousand million writes - a time limit failure caused "
          "entirely by tidying up. Clear `a[0]` to `a[n-1]` and nothing more."),
]),

# ---------------------------------------------------------------- 4
("io", "4. Reading an array in, and printing it out", [
 ("p", "Nearly every problem in section 15 starts with these lines. Learn them as one block."),
 ("code", """const int MAXN = 200005;
int a[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
}"""),
 ("p", "`cin >>` skips any amount of whitespace on its own, so it makes no difference whether the "
       "numbers arrive on one line or on twenty. When the count is **not** given first, read until "
       "the input runs out - `cin >> x` is false once there is nothing left:"),
 ("code", """int n = 0;
while (cin >> a[n]) n++;      // n ends up holding how many there were"""),
 ("p", "Printing. The tidy habit is a space before every element except the first, which leaves no "
       "trailing space at the end of the line:"),
 ("code", """for (int i = 0; i < n; i++) {
    if (i > 0) cout << ' ';
    cout << a[i];
}
cout << '\\n';"""),
 ("note", "Judges nearly always ignore trailing spaces and a blank line at the end, so `cout << a[i] "
          "<< ' ';` in a plain loop is normally accepted too. Use the tidy form anyway: it costs one "
          "`if` and removes a whole category of doubt."),
]),

# ---------------------------------------------------------------- 5
("scans", "5. The six scans you will write a hundred times", [
 ("p", "Six questions cover most of what an easy problem asks about an array. Write them out until "
       "your fingers know them, because every one of them is the first half of a harder solution."),
 ("h3", "Sum"),
 ("code", """long long sum = 0;                    // long long, not int - see the note
for (int i = 0; i < n; i++) sum += a[i];"""),
 ("note", "**Always sum into a long long.** 200000 numbers of up to 1000000 each add up to 2 * "
          "10^11, and an `int` stops at about 2 * 10^9. The wrong answer it gives is silent - no "
          "crash, no warning, just a number that is quietly wrong."),
 ("h3", "Largest and smallest"),
 ("p", "Start from the first element, never from 0. Starting from 0 gives the wrong answer the "
       "moment the input may be negative, and half of the test data is designed to catch exactly "
       "that."),
 ("code", """int best = a[0];
for (int i = 1; i < n; i++)
    if (a[i] > best) best = a[i];

// the same in one line, if you prefer:
int best2 = *max_element(a, a + n);
int worst = *min_element(a, a + n);"""),
 ("note", "`a, a + n` is a fixed phrase meaning \"the whole array\", exactly like `s.begin(), "
          "s.end()` for a string. `max_element` hands back *where* the largest value is, so the `*` "
          "in front says \"and now give me the value that is there\"."),
 ("h3", "Count how many satisfy a condition"),
 ("code", """int evens = 0;
for (int i = 0; i < n; i++)
    if (a[i] % 2 == 0) evens++;

// counting one exact value has a ready-made tool:
int sevens = count(a, a + n, 7);"""),
 ("h3", "Where is it? (the index of something)"),
 ("p", "Notice what happens after the value is found: `break` stops the loop, and `pos` stays -1 "
       "when the value is not there at all. That -1 is the standard \"not found\" answer for an "
       "array, in the same way `string::npos` is for a string."),
 ("code", """// x is the value we are hunting for
int pos = -1;
for (int i = 0; i < n; i++)
    if (a[i] == x) { pos = i; break; }     // the FIRST place x sits

if (pos == -1) cout << \"not there\\n\";
else           cout << \"at index \" << pos << '\\n';"""),
 ("p", "For the **last** place instead, walk backwards and stop at the first hit:"),
 ("code", """int last = -1;
for (int i = n - 1; i >= 0; i--)
    if (a[i] == x) { last = i; break; }"""),
 ("h3", "Does it contain x at all?"),
 ("code", """bool found = false;
for (int i = 0; i < n; i++)
    if (a[i] == x) { found = true; break; }"""),
 ("h3", "Index of the largest, not just its value"),
 ("p", "Many statements ask *which* pupil scored the most, not what the top score was. Keep the "
       "index and read the value through it:"),
 ("code", """int bi = 0;                           // index of the best so far
for (int i = 1; i < n; i++)
    if (a[i] > a[bi]) bi = i;

cout << \"largest is \" << a[bi] << \" at index \" << bi << '\\n';"""),
 ("note", "When two boxes tie, `>` keeps the **earliest** of them and `>=` keeps the **latest**. "
          "Statements almost always ask for the smallest index, so `>` is the right default. Read "
          "that sentence again before you submit - it is a one-character difference worth several "
          "test cases."),
]),

# ---------------------------------------------------------------- 6
("running", "6. Keeping a running answer in one pass", [
 ("p", "The six scans above all ask one question. Real problems ask a question whose answer depends "
       "on everything seen so far. The method is always the same: keep one or two ordinary variables "
       "next to the loop, update them at every box, and never look backwards. One pass, O(n)."),
 ("h3", "Running maximum, and the second largest"),
 ("p", "To keep the two largest values, update the second one **before** the first, or you will lose "
       "the old champion:"),
 ("code", """long long best = -4000000000LL, second = -4000000000LL;   // lower than any input

for (int i = 0; i < n; i++) {
    if (a[i] > best) {
        second = best;        // yesterday's champion is today's runner-up
        best   = a[i];
    } else if (a[i] > second) {
        second = a[i];
    }
}"""),
 ("h3", "The longest run of equal values"),
 ("p", "A **run** is a block of identical values sitting next to each other: `3 3 3 8 8 1` is three "
       "runs. Compare each box with the one before it. If they match the run continues, otherwise a "
       "new run starts:"),
 ("code", """int cur = 1, best = 1;
for (int i = 1; i < n; i++) {
    if (a[i] == a[i - 1]) cur++;
    else                  cur = 1;
    if (cur > best) best = cur;
}
cout << best << '\\n';"""),
 ("note", "The loop starts at `i = 1`, because `a[i - 1]` would be `a[-1]` when `i` is 0. Both `cur` "
          "and `best` start at 1, not 0 - a non-empty array always contains at least one run of "
          "length one. On an array that may be empty, check `n == 0` first."),
 ("p", "Change one symbol and the same six lines answer a different question. This is the pattern "
       "behind the *longest non-decreasing run*, the *longest strictly rising streak*, and the "
       "*longest stretch of days without rain*:"),
 ("table", ["Question", "The comparison to write"], [
   ["Longest run of equal values", "`a[i] == a[i-1]`"],
   ["Longest non-decreasing run", "`a[i] >= a[i-1]`"],
   ["Longest strictly rising run", "`a[i] > a[i-1]`"],
   ["Longest falling run", "`a[i] < a[i-1]`"],
   ["Longest stretch of zeros", "`a[i] == 0` (compare with the value, not the neighbour)"],
 ]),
 ("h3", "Counting the runs instead of measuring them"),
 ("p", "A new run begins at index 0, and at every place where the value changes. So the number of "
       "runs - and therefore the number of **distinct values in a sorted array** - is one plus the "
       "number of changes:"),
 ("code", """sort(a, a + n);

int distinct = 1;
for (int i = 1; i < n; i++)
    if (a[i] != a[i - 1]) distinct++;"""),
 ("h3", "A running total that is also the answer"),
 ("p", "Sometimes the running variable is not a maximum but a balance. Here is a bank account that "
       "must never go below zero - the whole check is one pass and one variable:"),
 ("code", """long long balance = 0;
bool ok = true;

for (int i = 0; i < n; i++) {
    balance += a[i];              // a[i] may be negative
    if (balance < 0) ok = false;
}"""),
]),

# ---------------------------------------------------------------- 7
("neighbours", "7. Neighbours, and windows of fixed width", [
 ("h3", "Looking at the box next door"),
 ("p", "A large family of problems is about **pairs of neighbours** rather than single boxes. There "
       "are `n - 1` neighbouring pairs in an array of `n` boxes, and the safe way to visit them is a "
       "loop from 1 to `n - 1` reading `a[i]` and `a[i - 1]`:"),
 ("code", """int rises = 0;
long long total_change = 0;

for (int i = 1; i < n; i++) {
    if (a[i] > a[i - 1]) rises++;
    total_change += abs(a[i] - a[i - 1]);   // how far the value moved in all
}"""),
 ("p", "When a box has to be compared with **both** neighbours - a peak, a valley, a local maximum - "
       "the first and the last box have no pair on one side, so the loop must skip them:"),
 ("code", """for (int i = 1; i < n - 1; i++)
    if (a[i - 1] < a[i] && a[i] > a[i + 1])
        cout << \"local maximum at \" << i << '\\n';"""),
 ("note", "`i < n - 1`, not `i < n`. Get this wrong and the last step reads `a[n]`, one box past the "
          "end. The program usually does not crash - it quietly reads whatever happens to be there, "
          "which is exactly why the bug survives your own testing."),
 ("h3", "A window of fixed width"),
 ("p", "\"The largest total of `k` boxes in a row.\" The slow way recomputes the sum of every window "
       "from scratch, which is `n * k` operations and too slow for large inputs. The fast way builds "
       "the first window once, and then **slides** it: one value joins on the right, one value "
       "leaves on the left, and the total is repaired with one addition and one subtraction."),
 ("code", """// k is the width of the window, and k <= n
long long sum = 0;
for (int i = 0; i < k; i++) sum += a[i];      // the first window, a[0..k-1]

long long best = sum;
for (int i = k; i < n; i++) {
    sum += a[i];                              // a[i] joins on the right
    sum -= a[i - k];                          // a[i-k] leaves on the left
    if (sum > best) best = sum;
}"""),
 ("p", "Two additions per step instead of `k`, so the whole scan is O(n) however wide the window is. "
       "The same shape counts vowels in a window, counts zeros in a window, or tracks anything else "
       "you can add and take away again."),
 ("h3", "Going round a circle"),
 ("p", "Some statements arrange the boxes in a ring: after the last one comes the first again. Do "
       "not copy the array or write special cases - use the remainder operator, which folds any "
       "index back into the range 0 to `n - 1`:"),
 ("code", """// for any index i between 0 and n - 1:
int nxt = (i + 1) % n;           // the box after i, wrapping round
int prv = (i - 1 + n) % n;       // the box before i, wrapping round

// the largest total of three in a row on a circle
long long best = 0;
for (int i = 0; i < n; i++) {
    long long s = a[i] + a[(i + 1) % n] + a[(i + 2) % n];
    if (i == 0 || s > best) best = s;
}"""),
 ("note", "The `+ n` in `(i - 1 + n) % n` is not decoration. In C++ the remainder of a negative "
          "number is negative: `(-1) % 5` is `-1`, not `4`. Adding `n` first keeps the value positive "
          "and the answer right."),
]),

# ---------------------------------------------------------------- 8
("two", "8. Two arrays side by side, and a value used as an index", [
 ("h3", "Parallel arrays"),
 ("p", "When each thing in the input has two facts about it - a name and a score, a cage and a "
       "feeder, an x and a y - keep one array per fact and let the index tie them together. Pupil "
       "`i` has score `score[i]` and age `age[i]`; the index *is* the pupil."),
 ("code", """int x[MAXN], y[MAXN];

for (int i = 0; i < n; i++) cin >> x[i] >> y[i];

int bi = 0;                                   // the point farthest from the origin
for (int i = 1; i < n; i++)
    if (abs(x[i]) + abs(y[i]) > abs(x[bi]) + abs(y[bi])) bi = i;

cout << x[bi] << ' ' << y[bi] << '\\n';"""),
 ("note", "Lesson 09 replaces parallel arrays with one array of `struct`s, which is tidier once "
          "there are four or five facts per thing. For two facts, parallel arrays are shorter and "
          "perfectly respectable contest code."),
 ("h3", "The value becomes the index"),
 ("p", "This is the idea that turns a slow solution into a fast one more often than any other in "
       "Groups C and D. Instead of storing *the values you were given*, make an array indexed **by** "
       "those values, and store a fact about each one. Asking \"have I seen 57?\" then costs one "
       "lookup rather than a loop."),
 ("code", """const int MAXV = 1000001;        // one box per possible VALUE, not per input number
bool seen[MAXV];                 // declared globally, so all false to begin with

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        seen[v] = true;          // the value picks its own box
    }

    if (seen[57]) cout << \"57 was in the input\\n\";
}"""),
 ("p", "Counting instead of marking is the same line with `++` in place of `= true`, which is where "
       "Lesson 06 picks the idea up and runs with it. Here it is enough to notice the shape and the "
       "two questions it always raises:"),
 ("list", [
   "**How big must the array be?** One box for every value the statement allows. `0 <= v <= 1000000` "
   "means `MAXV = 1000001` boxes - and `bool seen[1000001]` is 1 MB, so it must be global.",
   "**What if the values can be negative?** Shift them. With `-1000 <= v <= 1000`, store value `v` in "
   "box `v + 1000`, and remember to shift back when you read the answer out.",
 ]),
 ("code", """const int OFF = 1000;            // the shift
int cnt[2001] = {};              // boxes 0..2000 stand for values -1000..1000

for (int i = 0; i < n; i++) {
    int v;
    cin >> v;                    // v is somewhere between -1000 and 1000
    cnt[v + OFF]++;              // the value picks its own box
}

// box j stands for the value j - OFF
for (int j = 0; j <= 2000; j++)
    if (cnt[j] > 0)
        cout << (j - OFF) << \" appears \" << cnt[j] << \" times\\n\";"""),
 ("h3", "Marking neighbours of a marked box"),
 ("p", "A frequent small task: something occupies position `i`, and that also forbids `i - 1` and "
       "`i + 1`. Mark all three, but test the bounds before touching the neighbours:"),
 ("code", """bool blocked[MAXN] = {};              // global, all false to begin with

for (int i = 0; i < n; i++) {
    if (a[i] == 1) {                            // something stands here
        blocked[i] = true;
        if (i > 0)     blocked[i - 1] = true;
        if (i < n - 1) blocked[i + 1] = true;
    }
}

int free_places = 0;
for (int i = 0; i < n; i++) if (!blocked[i]) free_places++;"""),
 ("note", "Mark in one pass and count in a second pass. Counting while you mark double-counts a box "
          "that two different things forbid - a mistake that only shows up on the crowded test "
          "cases, which are of course the ones worth the most marks."),
]),

# ---------------------------------------------------------------- 9
("move", "9. Moving things about: reverse, shift, rotate, delete", [
 ("h3", "Swapping and reversing"),
 ("p", "`swap` exchanges the contents of two boxes. Reversing is `n / 2` swaps: walk one index in "
       "from each end until they meet."),
 ("code", """swap(a[0], a[n - 1]);

for (int i = 0, j = n - 1; i < j; i++, j--)
    swap(a[i], a[j]);

// or, in one line:
reverse(a, a + n);"""),
 ("h3", "Shifting"),
 ("p", "Shifting left by one means every box takes the value of its right-hand neighbour. **The "
       "direction of the loop matters**: shifting left must run forwards, so that each box is read "
       "before it is overwritten, and shifting right must run backwards for the same reason."),
 ("code", """// shift left by one: 3 1 4 1 5  ->  1 4 1 5 ?
for (int i = 0; i + 1 < n; i++) a[i] = a[i + 1];
a[n - 1] = 0;                                    // nothing came in from the right

// shift right by one: 3 1 4 1 5  ->  ? 3 1 4 1
for (int i = n - 1; i > 0; i--) a[i] = a[i - 1];
a[0] = 0;"""),
 ("note", "Run the right shift forwards and every box ends up holding `a[0]`, because you copy the "
          "value you have just written into the next box, and then again, and again. Write out five "
          "boxes on paper and follow the loop with a pencil - it takes a minute and you will never "
          "get the direction wrong again."),
 ("h3", "Rotating by k"),
 ("p", "Rotating means the values that fall off one end come back round at the other. Doing it with "
       "`k` single shifts costs `n * k`. Building the answer in a second array costs `n`, and `%` "
       "does the wrapping:"),
 ("code", """int b[MAXN];                          // global, next to a - it is just as big

for (int i = 0; i < n; i++)
    b[i] = a[(i + k) % n];            // rotate LEFT by k

for (int i = 0; i < n; i++)
    a[i] = b[i];                      // copy it back

// the library does the same job:
rotate(a, a + k, a + n);              // rotate left by k, in place"""),
 ("h3", "Deleting and inserting"),
 ("p", "An array cannot actually shrink, so \"delete\" means *move everything after the hole one "
       "place to the left, and then use one box fewer*. Both operations cost O(n), because on average "
       "half the array has to move."),
 ("code", """// delete the box at position p
for (int i = p; i + 1 < n; i++) a[i] = a[i + 1];
n--;                                  // one box shorter from now on

// insert value v at position p
for (int i = n; i > p; i--) a[i] = a[i - 1];
a[p] = v;
n++;                                  // make sure MAXN has room for this"""),
 ("h3", "The pattern that beats all of them: build a new array"),
 ("p", "When several boxes have to go, deleting them one at a time costs O(n^2) and skips elements "
       "if you are not careful, in the same way erasing inside a loop over a string does. Copy the "
       "keepers into a fresh array instead. One pass, no skipping, no bookkeeping:"),
 ("code", """int b[MAXN];                          // global, next to a
int m = 0;                            // how many boxes b actually holds

for (int i = 0; i < n; i++)
    if (a[i] != 0)                    // the rule for keeping a box
        b[m++] = a[i];                // b[m] = a[i]; then m++

// b[0..m-1] is the answer; copy it back if the rest of the code wants a
for (int i = 0; i < m; i++) a[i] = b[i];
n = m;"""),
 ("note", "`b[m++] = a[i]` is contest shorthand for two lines: store into `b[m]`, then move `m` on by "
          "one. It appears in so much competitive code that it is worth recognising, but write the "
          "two lines out separately whenever you are unsure - they compile to exactly the same thing."),
]),

# ---------------------------------------------------------------- 10
("funcs", "10. Arrays and functions", [
 ("p", "An array is never copied when it is given to a function. Only the address of its first box "
       "travels, so the function works on **your** array, not on a copy of it. That has one good "
       "consequence and two awkward ones."),
 ("code", """void print(int a[], int n) {         // int a[] and int* a mean the same here
    for (int i = 0; i < n; i++) cout << a[i] << ' ';
    cout << '\\n';
}

void double_all(int a[], int n) {
    for (int i = 0; i < n; i++) a[i] *= 2;   // this changes the caller's array
}

int main() {
    int v[3] = {1, 2, 3};
    double_all(v, 3);
    print(v, 3);                     // 2 4 6
}"""),
 ("list", [
   "**The good part:** passing a million-box array is instant, and a function can fill an array for "
   "you instead of having to return one.",
   "**Awkward part one:** the size does not travel with it. Always pass `n` as a second parameter. "
   "There is no other way for the function to find out.",
   "**Awkward part two:** `sizeof(a)` inside the function measures an address, not the array. It "
   "gives 8 on a 64-bit judge, every single time, whatever the array's real size.",
 ]),
 ("code", """int main() {
    int v[100];
    cout << sizeof(v) << '\\n';       // 400 - here it really is the array
}

void f(int a[]) {
    cout << sizeof(a) << '\\n';       // 8 - only an address arrived
}"""),
 ("p", "A function cannot return an array either. Return the count and fill an array the caller "
       "already owns - which is how nearly every contest helper function is written:"),
 ("code", """// keep the even numbers of a[0..n-1] in out[], return how many there were
int keep_even(int a[], int n, int out[]) {
    int m = 0;
    for (int i = 0; i < n; i++)
        if (a[i] % 2 == 0) out[m++] = a[i];
    return m;
}"""),
 ("note", "Write `const` on an array the function only reads: `int sum(const int a[], int n)`. The "
          "compiler then refuses to let you change it by accident, which turns a silent wrong answer "
          "into an error message at compile time. It costs five characters."),
]),

# ---------------------------------------------------------------- 11
("extras", "11. Sentinels and 1-based indexing", [
 ("h3", "Sentinels"),
 ("p", "A **sentinel** is an extra value parked just past the end, chosen so that the loop stops "
       "naturally and you can delete a special case. If you are looking for the first box that is at "
       "least `x`, and you are not sure there is one, put `x` itself at position `n`: the search now "
       "always succeeds, and afterwards `i == n` means \"there was none\"."),
 ("code", """a[n] = x;                       // the sentinel - MAXN must have room for it

int i = 0;
while (a[i] < x) i++;           // no need to test i < n, the sentinel stops it

if (i == n) cout << \"not found\\n\";
else        cout << \"found at \" << i << '\\n';"""),
 ("p", "The same trick with a very small value at `a[n]` lets a run-counting loop close the last run "
       "without repeating the closing code after the loop."),
 ("h3", "1-based indexing"),
 ("p", "Statements are written for people, so they number things from 1: \"pupil 1 to pupil N\". You "
       "may follow them exactly - leave `a[0]` unused and store pupil `i` in `a[i]`. The array simply "
       "needs one spare box, and the whole class of translation mistakes disappears."),
 ("code", """int a[MAXN];

for (int i = 1; i <= n; i++) cin >> a[i];      // note <= , and i starts at 1

for (int i = 1; i <= n; i++)
    cout << \"pupil \" << i << \" scored \" << a[i] << '\\n';"""),
 ("note", "Pick one style per program and stay with it. Mixing a 0-based read with a 1-based print in "
          "the same solution is the single most reliable way to lose an hour. 1-based suits problems "
          "that talk about \"the i-th thing\"; 0-based suits everything the `<algorithm>` header "
          "touches, because `a, a + n` assumes it."),
 ("h3", "What is still missing"),
 ("p", "Everything in this lesson has assumed that the size is known before the program is "
       "compiled, which is why `MAXN` had to be the largest size the statement allows, and why a "
       "row of boxes can never grow. Very often you would rather decide the length while the "
       "program is running, and add values as they arrive. That is `std::vector`, and it is the "
       "whole of Lesson 05."),
]),

]

# ---------------------------------------------------------------- 12
CHEATSHEET = [
 ("Declare, contents are rubbish", "`int a[100];`"),
 ("Declare, all zeros", "`int a[100] = {};`"),
 ("Declare with values", "`int a[] = {3, 1, 4};`"),
 ("Big array", "declare it **global**, at `MAXN` = the stated limit plus 5"),
 ("Clear the first n boxes", "`fill(a, a + n, 0);`"),
 ("Read n values", "`for (int i = 0; i < n; i++) cin >> a[i];`"),
 ("Read until the input ends", "`int n = 0; while (cin >> a[n]) n++;`"),
 ("The whole array, for `<algorithm>`", "`a, a + n`"),
 ("Sum", "`long long s = 0; for (...) s += a[i];` - **never an int**"),
 ("Largest / smallest value", "`*max_element(a, a + n)`, `*min_element(a, a + n)`"),
 ("Largest by hand", "`int best = a[0];` then loop from `i = 1`"),
 ("Index of the largest", "`int bi = 0; ... if (a[i] > a[bi]) bi = i;`"),
 ("Count one value", "`count(a, a + n, x)`"),
 ("First index of x", "loop with `break`; leave `pos = -1` for \"not found\""),
 ("Sort / reverse", "`sort(a, a + n);`, `reverse(a, a + n);`"),
 ("Swap two boxes", "`swap(a[i], a[j]);`"),
 ("Reverse by hand", "`for (int i = 0, j = n-1; i < j; i++, j--) swap(a[i], a[j]);`"),
 ("Shift left by one", "forwards: `for (i = 0; i+1 < n; i++) a[i] = a[i+1];`"),
 ("Shift right by one", "backwards: `for (i = n-1; i > 0; i--) a[i] = a[i-1];`"),
 ("Rotate left by k", "`rotate(a, a + k, a + n);`"),
 ("Delete box p", "shift the tail left, then `n--`"),
 ("Keep only some boxes", "`int m = 0; ... b[m++] = a[i];` then `n = m;`"),
 ("Neighbouring pairs", "`for (int i = 1; i < n; i++)` and use `a[i-1]`"),
 ("Both neighbours (a peak)", "`for (int i = 1; i < n - 1; i++)`"),
 ("Longest run of equal values", "`if (a[i] == a[i-1]) cur++; else cur = 1;` keep the max"),
 ("Number of distinct values", "`sort`, then count the places where `a[i] != a[i-1]`, plus 1"),
 ("Sliding window of width k", "build once, then `sum += a[i]; sum -= a[i-k];`"),
 ("Next / previous on a circle", "`(i + 1) % n` and `(i - 1 + n) % n`"),
 ("Value used as an index", "`seen[v] = true;` - the array needs one box per possible value"),
 ("Negative values as an index", "`cnt[v + OFF]++` with `OFF` = the most negative value"),
 ("Pass an array to a function", "`void f(int a[], int n)` - the size never travels with it"),
]

# ---------------------------------------------------------------- 13
PITFALLS = [
 ("An array of `n` boxes has no box `a[n]`.",
  "The last one is `a[n - 1]`. `for (int i = 0; i <= n; i++)` reads one box too many, and the "
  "program usually does not crash - it reads rubbish and gives a wrong answer on some tests only."),
 ("An uninitialised local array holds rubbish, not zeros.",
  "`int a[5];` gives five random values. Only a global array, or one written as `int a[5] = {};`, "
  "starts at zero."),
 ("Sum into a `long long`, not an `int`.",
  "200000 values of a million each overflow an `int` by a factor of a hundred, silently. This is the "
  "most common single cause of \"it works on the samples\" in Groups C and D."),
 ("Starting the maximum at 0 breaks on negative input.",
  "`int best = 0;` gives 0 as the largest value of `-5 -3 -9`. Start from `a[0]` and loop from 1."),
 ("A big array inside `main` crashes the program.",
  "The stack holds about 1 MB, so `int big[500000]` inside a function is too large. Move it outside "
  "every function, where it is global."),
 ("`a[i - 1]` when `i` is 0, and `a[i + 1]` when `i` is `n - 1`.",
  "Neighbour loops must start at 1, or stop at `n - 1`, or both. This is the bug that gives 60 out "
  "of 100 on a problem you had solved correctly."),
 ("Shifting in the wrong direction overwrites the array.",
  "Shift left with a forward loop, right with a backward loop. The other way round fills every box "
  "with the same value."),
 ("Deleting inside a loop over indexes skips elements.",
  "Every delete slides the rest of the array left, so the next value moves under your index and is "
  "never looked at. Build a new array of the boxes you are keeping."),
 ("`sizeof(a)` inside a function is the size of an address.",
  "It is 8, whatever the array. `sizeof(a) / sizeof(a[0])` therefore only works where the array was "
  "declared - never after it has been passed to a function."),
 ("`(i - 1) % n` is negative when `i` is 0.",
  "C++ keeps the sign of the left-hand operand, so `(-1) % 5` is `-1`. On a circle write "
  "`(i - 1 + n) % n`."),
 ("`int a[n];` with `n` read from the input is not standard C++.",
  "g++ accepts it, other compilers refuse it, and it puts a large array on the small stack. Declare "
  "`a[MAXN]` globally and use the first `n` boxes."),
]

# ---------------------------------------------------------------- 14
COMPLEXITY = [
 ["`a[i]` - read or write one box", "O(1)"],
 ["Declaring a global array", "free - it costs no time at all"],
 ["`fill(a, a + n, v)` over n boxes", "O(n)"],
 ["Any of the six scans in section 5", "O(n)"],
 ["`max_element`, `min_element`, `count`", "O(n)"],
 ["Copying one array into another", "O(n)"],
 ["Comparing two arrays box by box", "O(n)"],
 ["`reverse`, `rotate`", "O(n)"],
 ["Shifting by one, deleting, inserting", "O(n) - about half the array moves"],
 ["Deleting k values one at a time", "O(n * k) - build a new array instead, O(n)"],
 ["`sort(a, a + n)`", "O(n log n)"],
 ["Looking up `seen[v]` after marking", "O(1) - this is why the trick is worth it"],
 ["A sliding window of width k", "O(n) - two operations per step, not k"],
 ["Every pair `(i, j)` with a nested loop", "O(n^2) - fine to about n = 5000, not beyond"],
 ["Passing an array to a function", "O(1) - only the address travels"],
]

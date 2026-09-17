# -*- coding: utf-8 -*-
"""Lesson 02 - Primitive types. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "02_Primitive_Types"
BRAND = "Lesson 02 · Primitive types"
FOOTER = ("Lesson 02 · C++17 primitive types. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

PITFALLS_TITLE = "Twelve pitfalls that cost real marks"

TITLE = "C++17 Primitive types - what fits, and when it breaks"
SUBTITLE = ("Lesson 02 | Theory, cheat sheet and 24 graded problems "
            "from arena.olimpiici.com (Group D, with six from Group C)")

HOWTO = [
    "This lesson is built to be worked through in three passes. Do not try to do all three in one "
    "sitting.",
    "**Pass 1 - Read.** Go through sections 1-11 once, typing every snippet into a compiler and "
    "running it. Change a number, run it again, see what happens. Do not try to memorise anything "
    "yet; the aim is only to know what exists and where to find it later.",
    "**Pass 2 - Memorise.** Section 12 is the cheat sheet. Cover the right-hand column and write "
    "out each line from its description alone. Repeat until they all come out without thinking. "
    "Section 13 lists the mistakes that cost marks, and section 14 says what each operation costs.",
    "**Pass 3 - Solve.** Section 15 lists 24 problems from the Olimpiici Arena, ordered from "
    "easiest to hardest and grouped by technique. Solve them in order. Each group points back at "
    "the theory sections that solve it, so when a problem stalls you, re-read that section instead "
    "of looking up a solution.",
    "This is the shortest lesson in the course and the one that wins the most marks per page. "
    "Nothing here is an algorithm. It is all about the boxes your numbers live in, what happens "
    "when a number is too big for its box, and the handful of arithmetic rules that quietly decide "
    "whether a perfectly sensible solution scores 100 or 30.",
]

SECTIONS = [

# ---------------------------------------------------------------- 1
("setup", "1. Getting started: headers and fast input", [
 ("p", "Every program in this lesson begins the same way. These headers cover everything the lesson "
       "uses, so include them all at the top."),
 ("code", """#include <iostream>
#include <cmath>        // sqrt, pow, fabs, round
#include <climits>      // INT_MAX, LLONG_MAX
#include <iomanip>      // setprecision, fixed
#include <cctype>       // isdigit, isalpha, toupper, tolower

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
("ints", "2. The whole numbers: int and long long", [
 ("p", "A variable is a box, and every box has a fixed size. A whole number that is too big for its "
       "box does not make the box bigger and does not stop the program. It quietly becomes a "
       "different number. So the first question to ask about any value in a problem is **how large "
       "can this get**."),
 ("table", ["Type", "Bytes", "Smallest", "Largest", "Read it as"], [
   ["`int`", "4", "-2 147 483 648", "2 147 483 647", "about 2 thousand million"],
   ["`long long`", "8", "about -9.2 * 10^18", "about 9.2 * 10^18", "about 9 million million million"],
   ["`unsigned int`", "4", "0", "4 294 967 295", "about 4 thousand million, never negative"],
   ["`char`", "1", "-128", "127", "one character, or a very small number"],
   ["`bool`", "1", "`false`", "`true`", "a yes/no answer"],
 ]),
 ("p", "In practice you need only two of them: `int` up to about 2 * 10^9, and `long long` for "
       "anything beyond that. `<climits>` gives you the exact edges by name, which is how you start "
       "a search for a minimum:"),
 ("code", """cout << INT_MAX;      // 2147483647
cout << LLONG_MAX;    // 9223372036854775807

int  best  = INT_MAX;         // nothing read will be larger, so the first value wins
long long worst = LLONG_MIN;"""),
 ("p", "Writing a `long long` needs two small habits. A big constant needs the `LL` ending, and "
       "reading and printing are unchanged:"),
 ("code", """long long big = 3000000000LL;      // without LL the compiler reads it as an int first
long long x;
cin >> x;
cout << x << '\\n';"""),
 ("note", "On the judges used for Groups C and D, `long long` arithmetic is just as fast as `int` "
          "arithmetic. It costs twice the memory, which only matters for very large arrays. "
          "**When in doubt, use the bigger box.** A wrong answer from overflow costs far more than "
          "eight bytes ever will."),
]),

# ---------------------------------------------------------------- 3
("overflow", "3. Overflow: the silent wrong answer", [
 ("p", "This is the most expensive single idea in the lesson. When a result does not fit, the extra "
       "is thrown away and what is left over may even be negative. There is no crash and no warning "
       "- the program runs happily to the end and prints something wrong."),
 ("code", """int a = 2000000000;
int b = 2000000000;
cout << a + b << '\\n';         // -294967296     not 4000000000

int n = 100000;
cout << n * n << '\\n';         // 1410065408     not 10000000000"""),
 ("h3", "Where it actually happens"),
 ("p", "The trap is that **the type of the answer is decided by the things being multiplied, not by "
       "the box you put it in**. In the first line below, `n * n` is worked out as an `int`, "
       "overflows, and only then is the broken result copied into the `long long`:"),
 ("code", """int n = 100000;

long long bad  = n * n;                 // WRONG: int * int is an int, and it overflows
long long good = (long long)n * n;      // RIGHT: one side is 64-bit, so the whole sum is
long long also = 1LL * n * n;           // RIGHT: the same trick, a common shorthand"""),
 ("p", "The cure is a habit, not a calculation: **decide the type before you write the formula.** "
       "Declare every counting and summing variable `long long` from the start, and the "
       "multiplication is then safe without any casting at all:"),
 ("code", """long long n;
cin >> n;
cout << n * n << '\\n';          // fine: long long * long long"""),
 ("h3", "Seeing it coming"),
 ("p", "Before you write a formula, put in the largest numbers the statement allows and multiply "
       "them out roughly. If the answer passes 2 * 10^9, you need `long long`. These are the shapes "
       "that catch people out:"),
 ("table", ["Formula", "With the usual limits", "Fits in"], [
   ["`n * (n - 1) / 2` with `n` up to 10^5", "about 5 * 10^9", "`long long`"],
   ["A sum of 10^5 values of up to 10^6", "about 10^11", "`long long`"],
   ["`a * b` with `a`, `b` up to 10^6", "10^12", "`long long`"],
   ["A count of pairs among 10^5 things", "about 5 * 10^9", "`long long`"],
   ["`2^40`", "about 10^12", "`long long`"],
   ["A sum of 1000 values of up to 1000", "10^6", "`int` is fine"],
 ]),
 ("note", "A negative answer where only positive ones make sense is the classic sign of overflow. If "
          "a program prints a sensible number on the samples and a strange negative one on the big "
          "test, look for an `int` that should have been a `long long` before you look anywhere else."),
]),

# ---------------------------------------------------------------- 4
("divmod", "4. Integer division and the remainder", [
 ("p", "When both sides are whole numbers, `/` gives a whole number. The part after the decimal "
       "point is thrown away - not rounded, thrown away. `%` gives what is left over."),
 ("code", """cout << 7 / 2;      // 3      not 3.5, and not 4
cout << 7 % 2;      // 1
cout << 10 / 5;     // 2
cout << 10 % 5;     // 0

cout << 7 / 2.0;    // 3.5    one side has a decimal point, so the answer does too"""),
 ("p", "Those two together are how you take a number apart. `% 10` is the last digit and `/ 10` "
       "removes it, so this loop visits every digit from the right:"),
 ("code", """int n = 9251;
int sum = 0;

while (n > 0) {
    int d = n % 10;      // 1, then 5, then 2, then 9
    sum += d;
    n = n / 10;          // 925, then 92, then 9, then 0
}
cout << sum << '\\n';     // 17"""),
 ("note", "That loop prints nothing at all when `n` is 0, because the condition is false straight "
          "away. If 0 is a possible input and its digit sum should be 0, that is fine; if you needed "
          "the program to say \"one digit\", handle `n == 0` separately before the loop."),
 ("h3", "The two units trick"),
 ("p", "Anything measured in small units splits into big and small with one division and one "
       "remainder. Learn the shape once and it works for money, for time, and for anything else:"),
 ("code", """int total = 1234;                // stotinki

int leva     = total / 100;      // 12
int stotinki = total % 100;      // 34

int seconds = 3725;
int h = seconds / 3600;                 // 1
int m = (seconds % 3600) / 60;          // 2
int s = seconds % 60;                   // 5"""),
 ("h3", "Rounding up without a double"),
 ("p", "\"How many boxes of 7 do I need for 30 things?\" is not `30 / 7`, which is 4 and leaves six "
       "things on the floor. Rounding up is done with whole numbers, and the phrase to memorise is "
       "`(a + b - 1) / b`:"),
 ("code", """int a = 30, b = 7;

cout << a / b;                  // 4      rounded down
cout << (a + b - 1) / b;        // 5      rounded up

// never write this - see section 9
// cout << (int)ceil(a / (double)b);"""),
 ("h3", "Counting multiples"),
 ("p", "How many numbers from 1 to `n` are multiples of `k`? Exactly `n / k`. For a range that does "
       "not start at 1, count up to the top and take away the ones below the bottom - and mind that "
       "`a` itself belongs to the range:"),
 ("code", """long long n, k;
cin >> n >> k;
cout << n / k << '\\n';                   // multiples of k in 1..n

long long a, b;
cin >> a >> b;
cout << b / k - (a - 1) / k << '\\n';     // multiples of k in a..b"""),
]),

# ---------------------------------------------------------------- 5
("negative", "5. Negative numbers, division and %", [
 ("p", "Everything above assumed positive numbers. With a negative number on the left, C++ throws "
       "away the decimal part by moving **towards zero**, and the remainder keeps the sign of the "
       "left-hand side. That is not what most people expect, and it is not what mathematics does."),
 ("code", """cout << 7 / 2;       //  3
cout << -7 / 2;      // -3      towards zero, NOT -4
cout << 7 % 2;       //  1
cout << -7 % 2;      // -1      NOT 1
cout << 7 % -2;      //  1      the sign comes from the LEFT side"""),
 ("p", "The place this bites is wrapping round a circle. Stepping backwards past 0 gives -1, and "
       "`-1 % n` is `-1`, not `n - 1`. Adding `n` first keeps everything positive:"),
 ("code", """int n = 5;
int i = 0;

cout << (i - 1) % n;          // -1     out of range
cout << (i - 1 + n) % n;      //  4     what you wanted"""),
 ("p", "The same fix works whenever the number could be more than `n` below zero - add a multiple of "
       "`n` big enough to clear it:"),
 ("code", """int shift = -37;
int n = 10;
cout << ((shift % n) + n) % n << '\\n';     // 3, and always in 0..n-1"""),
 ("note", "`abs(x)` gives the size of a number without its sign, and lives in `<cmath>`. For whole "
          "numbers use `abs`; for a `double` use `fabs`. Watch the one case that breaks: `abs` of "
          "the most negative `int` cannot be represented, so it comes back negative. You will "
          "almost never meet it, but now you know what you are looking at if you do."),
]),

# ---------------------------------------------------------------- 6
("chars", "6. char: a letter is a small number", [
 ("p", "A `char` holds one character, but underneath it is just a small whole number - the "
       "character's ASCII code - and you may do arithmetic on it. The codes worth knowing:"),
 ("table", ["Characters", "Codes"], [
   ["`'0'` ... `'9'`", "48 ... 57"],
   ["`'A'` ... `'Z'`", "65 ... 90"],
   ["`'a'` ... `'z'`", "97 ... 122"],
   ["`' '` (space)", "32"],
 ]),
 ("p", "You almost never need the numbers themselves, because the digits and the letters are stored "
       "in order. Subtracting the first character of a run turns a character into a small number, "
       "and adding it turns the number back into a character:"),
 ("code", """char c = '7';
int  d = c - '0';               // 7       digit character -> its value
char e = char('0' + 7);         // '7'     value -> digit character

int  i  = 'c' - 'a';            // 2       letter -> 0..25
char c2 = char('a' + 2);        // 'c'     0..25 -> letter"""),
 ("p", "`<cctype>` names the tests you would otherwise write by hand:"),
 ("table", ["Function", "True for"], [
   ["`isdigit(c)`", "0-9"],
   ["`isalpha(c)`", "A-Z, a-z"],
   ["`isalnum(c)`", "a letter or a digit"],
   ["`isspace(c)`", "space, tab, newline"],
   ["`isupper(c)` / `islower(c)`", "a capital / a small letter"],
   ["`toupper(c)` / `tolower(c)`", "**not a test** - gives back the converted character"],
 ]),
 ("note", "`cin >> c` into a `char` skips spaces and newlines and gives you the next real character. "
          "That is usually what you want. It also means you cannot read a space that way - and "
          "reading whole lines of text is Lesson 03, which takes this section much further."),
]),

# ---------------------------------------------------------------- 7
("bool", "7. bool, comparisons, and the = / == trap", [
 ("p", "A `bool` is one of two values, `true` and `false`. Every comparison produces one, and "
       "printing one gives 1 or 0 rather than the words."),
 ("code", """bool ok = (5 > 3);
cout << ok;                  // 1
cout << (2 == 2) << '\\n';    // 1
cout << (2 != 2) << '\\n';    // 0"""),
 ("p", "The three ways to join conditions together. `&&` and `||` are **short-circuit**: as soon as "
       "the answer is settled, the rest is not even looked at."),
 ("table", ["Written", "Means", "True when"], [
   ["`a && b`", "and", "both are true"],
   ["`a || b`", "or", "at least one is true"],
   ["`!a`", "not", "`a` is false"],
 ]),
 ("p", "Short-circuiting is not a detail, it is a tool. It lets you check that something is safe "
       "before you use it, in one condition, because the right-hand side never runs when the "
       "left-hand side has already said no:"),
 ("code", """int n = 0, total = 10;

if (n != 0 && total / n > 3)          // safe: the division never happens when n is 0
    cout << \"big average\\n\";

if (n > 0 || n < -5)                  // the second test is skipped when the first is true
    cout << \"outside\\n\";"""),
 ("h3", "The trap"),
 ("p", "`=` puts a value into a variable. `==` asks whether two values are equal. Writing one where "
       "you meant the other compiles cleanly and gives nonsense:"),
 ("code", """int x = 5;

if (x == 3) cout << \"three\\n\";     // asks a question - prints nothing, correctly
if (x = 3)  cout << \"three\\n\";     // PUTS 3 into x, then treats 3 as true - always prints"""),
 ("note", "The rule for reading conditions: any number that is not 0 counts as true, and 0 counts as "
          "false. That is why `if (x = 3)` is always true and `if (x = 0)` is always false - and why "
          "the compiler cannot tell that you made a mistake."),
]),

# ---------------------------------------------------------------- 8
("double", "8. double: numbers with a decimal point", [
 ("p", "A `double` holds a number with a decimal point. It has about **15 or 16 correct digits in "
       "all**, counting both sides of the point - not 15 after it. Beyond that the value is an "
       "approximation, and the errors add up."),
 ("code", """double x = 7 / 2;            // 3.0    !!  7/2 is worked out as INTEGERS first
double y = 7 / 2.0;          // 3.5        one side has a point, so the division does too
double z = (double)7 / 2;    // 3.5        the same, written with a cast

cout << 1.0 / 3.0 << '\\n';   // 0.333333   only six digits are shown by default"""),
 ("note", "`double x = 7 / 2;` is the single most common floating-point mistake in Groups C and D. "
          "The division happens **before** anything is copied into `x`, and at that moment both "
          "sides are still whole numbers. Put a `.0` on one of them, or cast one of them."),
 ("h3", "Printing"),
 ("p", "By default `cout` shows about six digits and switches to scientific notation for large "
       "numbers, which a judge will mark wrong. When a statement asks for a fixed number of decimal "
       "places, say so once, at the start, and then print normally:"),
 ("code", """#include <iomanip>

cout << fixed << setprecision(2);
cout << 3.14159 << '\\n';      // 3.14
cout << 2.0 << '\\n';          // 2.00     the zeros are kept, which is what is wanted"""),
 ("h3", "The tools in `<cmath>`"),
 ("table", ["Call", "What it gives", "Careful"], [
   ["`sqrt(x)`", "the square root", "a `double`, even for a perfect square"],
   ["`pow(a, b)`", "`a` to the power `b`", "a `double` - see section 9"],
   ["`fabs(x)`", "size without the sign, for a `double`", "`abs` is the one for whole numbers"],
   ["`round(x)`", "to the nearest whole number", "still a `double`; cast it"],
   ["`floor(x)` / `ceil(x)`", "down / up to a whole number", "still a `double`; cast it"],
 ]),
 ("p", "Casting a `double` to an `int` does **not** round - it throws the decimal part away, towards "
       "zero. If you want the nearest whole number, say so:"),
 ("code", """double d = 2.99;

cout << (int)d;                // 2
cout << (int)round(d);         // 3
cout << (int)(-2.7);           // -2      towards zero, not -3"""),
]),

# ---------------------------------------------------------------- 9
("compare", "9. Never compare two doubles with ==", [
 ("p", "A `double` cannot hold most numbers exactly - not even 0.1, in the same way you cannot write "
       "one third exactly as a decimal. Small errors are stored, and then they add up. So two values "
       "that ought to be equal usually are not:"),
 ("code", """double a = 0.1 + 0.2;
double b = 0.3;

cout << (a == b) << '\\n';        // 0 - they are NOT equal
cout << fixed << setprecision(20);
cout << a << '\\n';               // 0.30000000000000004441
cout << b << '\\n';               // 0.29999999999999998890"""),
 ("p", "The fix is to ask whether they are *close enough*. Pick a tolerance small compared with the "
       "numbers in the problem - `1e-9` is the usual choice - and compare the gap against it:"),
 ("code", """const double EPS = 1e-9;

if (fabs(a - b) < EPS) cout << \"equal enough\\n\";
if (a > b + EPS)       cout << \"a is really bigger\\n\";
if (a < b - EPS)       cout << \"a is really smaller\\n\";"""),
 ("h3", "The better fix: stay with whole numbers"),
 ("p", "In most Group C and D problems the doubles are not needed at all, and the honest answer is "
       "to avoid them. Three exchanges worth knowing:"),
 ("table", ["Instead of", "Write"], [
   ["`a / b > c / d`", "`a * d > c * b` (when `b` and `d` are positive)"],
   ["`(int)ceil(a / (double)b)`", "`(a + b - 1) / b`"],
   ["A price in leva as a `double`", "the price in stotinki as a `long long`"],
   ["`if (x == y)` on doubles", "keep `x` and `y` as whole numbers, then `==` is exact"],
 ]),
 ("h3", "sqrt and pow lie"),
 ("p", "`sqrt(x)` and `pow(a, b)` do their work in `double`, so they may come back a hair below the "
       "whole number you were expecting. Casting then throws that hair away and you get an answer "
       "one too small. Always check the result with whole-number arithmetic:"),
 ("code", """long long x = 1000000000000LL;       // 10^12, and 10^6 squared exactly

long long r = (long long)sqrt((double)x);    // might be 999999 rather than 1000000
while (r * r < x) r++;                       // nudge it up
while (r * r > x) r--;                       // and down
if (r * r == x) cout << \"a perfect square\\n\";"""),
 ("note", "The same goes for powers. `pow(10, 2)` can come back as 99.999999... on some compilers, "
          "and the cast then throws the 0.999... away and leaves you with 99. "
          "For a whole-number power, multiply in a loop - it is three lines, it is exact, and for "
          "the sizes in this course it is also faster."),
]),

# ---------------------------------------------------------------- 10
("mixing", "10. Mixing types: what the compiler does for you", [
 ("p", "When the two sides of an operator have different types, C++ quietly converts one of them "
       "before doing the work. The rule is short: **the wider type wins.**"),
 ("table", ["Left and right", "Worked out as"], [
   ["`int` and `int`", "`int` - this is where overflow lives"],
   ["`int` and `long long`", "`long long`"],
   ["`int` and `double`", "`double`"],
   ["`char` and `int`", "`int`"],
   ["`bool` and `int`", "`int`, with `true` as 1"],
   ["`int` and `unsigned`", "`unsigned` - **and this one is a trap**"],
 ]),
 ("p", "The last row is the surprising one. Put a negative `int` next to an `unsigned` and the "
       "negative number is converted first, becoming an enormous positive one:"),
 ("code", """int i = -1;
unsigned u = 1;

cout << (i < u) << '\\n';        // 0 - it says -1 is NOT less than 1"""),
 ("note", "You will rarely write `unsigned` on purpose. You will meet it anyway, because `.size()` "
          "hands one back - which is why Lesson 03 insists on `int n = s.size();` before a loop. "
          "The habit to build now: keep everything `int` or `long long`, and put the length into an "
          "ordinary `int` the moment you get it."),
 ("h3", "Casting on purpose"),
 ("p", "A cast says \"treat this value as that type, here, now\". The two you will actually write:"),
 ("code", """int a = 7, b = 2;

double d = (double)a / b;        // 3.5     force the division to be a double one
long long big = (long long)a * b;  // force the multiplication to be 64-bit

cout << (int)3.99;               // 3       double -> int throws the decimals away
cout << (int)'A';                // 65      char -> int gives the ASCII code"""),
 ("note", "Put the cast on the **operand**, never on the answer. `(long long)(a * b)` is too late - "
          "the multiplication has already overflowed by then, and you are only widening the wreckage."),
]),

# ---------------------------------------------------------------- 11
("choose", "11. Choosing a type", [
 ("p", "Nothing in this lesson is hard once the decision is made early. Make it before you write "
       "the formula, not after the judge has told you the answer is wrong."),
 ("table", ["What the value is", "Use"], [
   ["A counter, an index, a size up to 10^9", "`int`"],
   ["A sum, a product, or anything past 2 * 10^9", "`long long`"],
   ["A count of pairs, or `n * n` with `n` past 46340", "`long long`"],
   ["A yes/no answer", "`bool`"],
   ["One character", "`char`"],
   ["Money, or a measurement given to two decimals", "a `long long` of the small unit"],
   ["A genuine measurement - an angle, a distance", "`double`"],
   ["Anything at all, when you are not sure", "`long long`"],
 ]),
 ("p", "Two questions, asked in this order, before every formula you write:"),
 ("list", [
   "**How big can this get?** Put the largest numbers the statement allows into the formula and "
   "multiply them out roughly. Past 2 * 10^9 means `long long` - and `long long` for the variables, "
   "not a cast bolted on at the end.",
   "**Is any of this really fractional?** If the answer is a whole number, keep every step a whole "
   "number. Most of section 9 is about damage you can simply decline to take.",
 ]),
 ("note", "There are more types than these - `short`, `unsigned long long`, `long double`, `float`. "
          "You do not need any of them in Groups C and D. `int`, `long long`, `char`, `bool` and "
          "`double` will carry you through every problem in this course."),
]),

]

# ---------------------------------------------------------------- 12
CHEATSHEET = [
 ("Whole number up to 2 * 10^9", "`int`"),
 ("Whole number beyond that", "`long long`"),
 ("The exact edges", "`INT_MAX`, `INT_MIN`, `LLONG_MAX`, `LLONG_MIN` from `<climits>`"),
 ("A big constant", "`3000000000LL` - the `LL` is needed"),
 ("Start a search for a minimum", "`int best = INT_MAX;`"),
 ("Start a search for a maximum", "`long long best = LLONG_MIN;`"),
 ("Multiply two ints safely", "`(long long)a * b` or `1LL * a * b`"),
 ("Cast in the right place", "on an **operand**, never on the finished answer"),
 ("Last digit / drop last digit", "`n % 10` / `n / 10`"),
 ("Digit loop", "`while (n > 0) { d = n % 10; n /= 10; }`"),
 ("Split into two units", "`big = t / 100;` `small = t % 100;`"),
 ("Round down", "`a / b`"),
 ("Round up", "`(a + b - 1) / b` - never with `ceil`"),
 ("Multiples of k in 1..n", "`n / k`"),
 ("Multiples of k in a..b", "`b / k - (a - 1) / k`"),
 ("Is it even?", "`n % 2 == 0`"),
 ("Negative division", "`-7 / 2` is `-3`, towards zero"),
 ("Negative remainder", "`-7 % 2` is `-1` - the sign follows the left side"),
 ("Wrap round a circle", "`(i - 1 + n) % n`, and `((x % n) + n) % n` in general"),
 ("Size without the sign", "`abs(x)` for whole numbers, `fabs(x)` for a `double`"),
 ("Digit character to value", "`c - '0'`; back again `char('0' + d)`"),
 ("Letter to 0..25", "`c - 'a'`; back again `char('a' + i)`"),
 ("Classify a character", "`isdigit`, `isalpha`, `isalnum`, `isspace`, `isupper`, `islower`"),
 ("Integer division into a double", "`(double)a / b` - putting `.0` on one side works too"),
 ("Print two decimal places", "`cout << fixed << setprecision(2);` once, at the start"),
 ("Compare two doubles", "`fabs(a - b) < 1e-9` - **never** `a == b`"),
 ("Really bigger", "`a > b + EPS`"),
 ("Avoid the division entirely", "`a / b > c / d` becomes `a * d > c * b`"),
 ("Check a square root", "cast, then nudge with `while (r * r < x) r++;`"),
 ("Whole-number power", "multiply in a loop - `pow` returns a `double` and may be low"),
 ("Nearest whole number", "`(int)round(d)` - a plain cast throws the decimals away"),
 ("`=` versus `==`", "`=` stores, `==` asks; `if (x = 3)` is always true"),
]

# ---------------------------------------------------------------- 13
PITFALLS = [
 ("`int * int` is an `int`, whatever you store it in.",
  "`long long s = n * n;` overflows before the copy happens. Write `(long long)n * n`, or make `n` "
  "a `long long` in the first place."),
 ("A sum of many values needs a `long long`.",
  "100000 values of up to a million is 10^11, and an `int` stops at about 2 * 10^9. The wrong answer "
  "is silent - no crash, no warning."),
 ("`n * (n - 1) / 2` overflows an `int` from n = 46342.",
  "The trap is the multiplication, not the answer. `n * (n - 1)` passes `INT_MAX` at n = 46342, "
  "while the halved result would have fitted all the way to n = 65536 - so the damage is done "
  "before the `/ 2` ever runs. Counting pairs is the commonest overflow in Groups C and D."),
 ("A negative answer where only positive ones make sense means overflow.",
  "It is the fastest diagnosis in competitive programming. Check the types before you check the "
  "logic."),
 ("`7 / 2` is 3, and `double x = 7 / 2;` is 3.0.",
  "The division is done in whole numbers first and the result is copied afterwards. Put a `.0` on "
  "one side, or cast one side."),
 ("`-7 / 2` is -3 and `-7 % 2` is -1.",
  "Division moves towards zero, and the remainder keeps the sign of the left-hand side. On a circle "
  "write `(i - 1 + n) % n`, never `(i - 1) % n`."),
 ("Rounding up with `ceil` on a division.",
  "`ceil(a / b)` divides in whole numbers first, so it rounds nothing at all; `ceil(a / (double)b)` "
  "works but can be a hair out. Write `(a + b - 1) / b`."),
 ("`==` between two doubles.",
  "`0.1 + 0.2 == 0.3` is false. Compare with `fabs(a - b) < 1e-9`, or keep the values as whole "
  "numbers and avoid the question."),
 ("`(int)sqrt(x)` and `(int)pow(a, b)` can be one too small.",
  "They are worked out in `double` and the cast throws the remainder away. Nudge the result with a "
  "`while` loop, or multiply in a loop for powers."),
 ("Casting a `double` to an `int` does not round.",
  "`(int)2.99` is 2 and `(int)(-2.7)` is -2. For the nearest whole number write `(int)round(d)`."),
 ("`if (x = 3)` stores 3 and is always true.",
  "`=` stores, `==` compares. Any value other than 0 counts as true, so the compiler sees nothing "
  "wrong. Read every `if` twice."),
 ("A negative `int` compared with an `unsigned` becomes enormous.",
  "`-1 < 1u` is false. Put any length into an ordinary `int` the moment you receive it, and keep "
  "`unsigned` out of your arithmetic."),
]

# ---------------------------------------------------------------- 14
COMPLEXITY = [
 ["`+`, `-`, comparisons, `&&`, `||`", "the fastest things the processor does"],
 ["`*` on `int` or `long long`", "a few times slower than `+`, still one step"],
 ["`/` and `%` on whole numbers", "roughly 20-40 times slower than `+`"],
 ["`/` and `%` by a constant power of two", "as fast as `+` - the compiler rewrites it"],
 ["`long long` arithmetic on a 64-bit judge", "the same speed as `int`"],
 ["`double` `+`, `-`, `*`", "about as fast as the whole-number versions"],
 ["`double` division", "slower again than whole-number division"],
 ["`sqrt(x)`", "slow, and only about 15 correct digits"],
 ["`pow(a, b)`", "slow **and** inexact - multiply in a loop instead"],
 ["A digit loop over `n`", "about 10 steps for an `int`, 19 for a `long long`"],
 ["Reading one number with `cin >>`", "fast once `sync_with_stdio(false)` is set"],
 ["Printing with `endl`", "slow - it empties the buffer every time; use `'\\n'`"],
 ["Casting between types", "free, or nearly so"],
 ["Overflow", "free - which is exactly why it is dangerous"],
]

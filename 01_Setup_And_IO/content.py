# -*- coding: utf-8 -*-
"""Lesson 01 - Setup and I/O. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "01_Setup_And_IO"
BRAND = "Lesson 01 · Setup and I/O"
FOOTER = ("Lesson 01 · C++17 setup and input/output. Problem links point to "
          "arena.olimpiici.com; statements are in Bulgarian and downloadable as PDF from each "
          "problem page.")

TITLE = "C++17 Setup and I/O - getting the data in and the answer out"
SUBTITLE = ("Lesson 01 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("first", "1. Your first program", [
 ("p", "Every program in this course starts the same way. Here is a whole program. It reads two "
       "numbers and prints their sum:"),
 ("code", """#include <iostream>          // the tools for reading and printing

using namespace std;         // lets you write cout instead of std::cout

int main() {                 // the program starts here
    int a, b;
    cin >> a >> b;           // read two numbers
    cout << a + b << '\\n';   // print their sum and end the line
    return 0;                // the program finished without trouble
}"""),
 ("p", "Only the middle lines change from problem to problem. Learn the rest by heart and type it "
       "at the start of every solution."),
 ("p", "To run it, save the code as `sol.cpp` and compile it. In an editor such as Code::Blocks "
       "or VS Code there is a *Build and run* button. In a terminal you type:"),
 ("code", """g++ -std=c++17 -O2 -o sol sol.cpp"""),
 ("p", "Then start the program with `sol` (Windows) or `./sol` (Linux, macOS), type the input "
       "and press Enter."),
 ("note", "The judge never reads your code. It runs your program, gives it the input, and compares "
          "what you print with the right answer, character by character. One extra word or a "
          "missing space and the answer is wrong."),
]),

# ---------------------------------------------------------------- 2
("numbers", "2. Reading and printing numbers", [
 ("p", "`cin >> x` reads one number into `x`. It jumps over spaces and new lines, so it does not "
       "matter whether the numbers are on one line or on several."),
 ("code", """int h, m;
cin >> h >> m;                   // input:  2 30
cout << h * 60 + m << '\\n';      // output: 150"""),
 ("p", "`cout <<` prints. You can chain several things with `<<`. Put `' '` between numbers that "
       "share a line, and `'\\n'` at the end of every line:"),
 ("code", """cout << 7 << ' ' << 3 << '\\n';      // 7 3"""),
 ("table", ["Sign", "Meaning", "Example"], [
   ["`+  -  *`", "add, subtract, multiply", "`7 * 3` is `21`"],
   ["`/`", "divide whole numbers: the part after the point is dropped", "`7 / 3` is `2`"],
   ["`%`", "the remainder of the division", "`7 % 3` is `1`"],
 ]),
 ("note", "An `int` holds numbers up to about 2 billion. When the answer can be bigger, use "
          "`long long` instead of `int`. Lesson 02 explains why."),
]),

# ---------------------------------------------------------------- 3
("loop", "3. Many numbers: a loop", [
 ("p", "Very often the first number tells you how many numbers come after it. Read it, then read "
       "the rest in a loop:"),
 ("code", """int n;
cin >> n;                // how many numbers follow

int sum = 0;
for (int i = 0; i < n; i++) {
    int x;
    cin >> x;            // the same x is used again and again
    sum += x;
}
cout << sum << '\\n';"""),
 ("p", "Nothing was stored. Each number was read, used, and forgotten. Most problems need only a "
       "few things kept from the numbers you have seen: a sum, a counter, the best one so far."),
 ("p", "Keeping the largest so far: start with the first number, then compare every new one with "
       "it."),
 ("code", """int n;
cin >> n;
int best;
cin >> best;                     // the first number is the best so far
for (int i = 1; i < n; i++) {
    int x;
    cin >> x;
    if (x > best) best = x;
}
cout << best << '\\n';"""),
 ("p", "Keeping a streak: how many numbers in a row went up? Remember the previous number, the "
       "current streak and the longest streak."),
 ("code", """int n, prev;
cin >> n >> prev;
int cur = 1, longest = 1;
for (int i = 1; i < n; i++) {
    int x;
    cin >> x;
    if (x > prev) cur++;         // the streak goes on
    else cur = 1;                // the streak breaks; x starts a new one
    if (cur > longest) longest = cur;
    prev = x;
}
cout << longest << '\\n';"""),
]),

# ---------------------------------------------------------------- 4
("chars", "4. Reading characters one at a time", [
 ("p", "A `char` holds one character: a letter, a digit or a sign. `cin >> c` reads the next "
       "character and, like before, jumps over spaces and new lines."),
 ("p", "So the input `10110` can be read one digit at a time, even though it has no spaces:"),
 ("code", """int n;                   // input:  5
cin >> n;                //         10110
int ones = 0;
for (int i = 0; i < n; i++) {
    char c;
    cin >> c;
    if (c == '1') ones++;
}
cout << ones << '\\n';    // 3"""),
 ("p", "When the problem does not say how many characters there are, read until the input ends. "
       "`while (cin >> c)` stops by itself when there is nothing left:"),
 ("code", """char c;
int count = 0;
while (cin >> c) {
    if (c == 'a') count++;
}
cout << count << '\\n';"""),
 ("note", "`'1'` in single quotes is a character. `1` without quotes is a number. When you read a "
          "`char`, compare it with `'1'`, never with `1`."),
]),

# ---------------------------------------------------------------- 5
("symbols", "5. Numbers with signs in between", [
 ("p", "Some inputs are not just numbers: `12+7`, `10:35`, `21.05.2015`. Read the number, then "
       "the sign into a `char`, then the next number. `cin` stops a number as soon as it meets a "
       "sign, so this works even without spaces:"),
 ("code", """int a, b;
char op;
cin >> a >> op >> b;             // input: 12+7

if (op == '+') cout << a + b << '\\n';
if (op == '-') cout << a - b << '\\n';"""),
 ("code", """int d, m, y;
char dot1, dot2;
cin >> d >> dot1 >> m >> dot2 >> y;      // input: 21.05.2015
cout << y << '\\n';                       // 2015"""),
 ("p", "Printing a time like `09:05` needs the zeros in front. Print them yourself:"),
 ("code", """int h = 9, m = 5;
if (h < 10) cout << '0';
cout << h << ':';
if (m < 10) cout << '0';
cout << m << '\\n';               // 09:05"""),
]),

# ---------------------------------------------------------------- 6
("submit", "6. Fast input, and checking before you send", [
 ("p", "`cin` and `cout` are a little slow. When the input has many thousands of numbers, put "
       "these two lines at the very start of `main`:"),
 ("code", """ios_base::sync_with_stdio(false);
cin.tie(nullptr);"""),
 ("p", "Also print `'\\n'` and not `endl`. Both end the line, but `endl` is much slower when you "
       "print many lines."),
 ("p", "Before you send a solution:"),
 ("list", ["Run every example from the statement and compare the output exactly.",
           "Try the smallest input the statement allows, for example `n = 1`.",
           "Try the biggest numbers allowed. Does the answer still fit in an `int`?"]),
 ("table", ["The judge says", "What it means"], [
   ["Accepted", "Correct and fast enough."],
   ["Wrong answer", "The program printed something different from the right answer."],
   ["Time limit exceeded", "The program was too slow."],
   ["Runtime error", "The program crashed, for example by dividing by zero."],
   ["Compilation error", "The code did not compile. Compile it yourself before sending."],
 ]),
]),

]

CHEATSHEET = [
 ("Start every program", "`#include <iostream>`, `using namespace std;`, `int main() { ... }`"),
 ("Read one number / several", "`cin >> x;` / `cin >> a >> b >> c;`"),
 ("Print two numbers on one line", "`cout << a << ' ' << b << '\\n';`"),
 ("Read `n` numbers", "`cin >> n; for (int i = 0; i < n; i++) { cin >> x; ... }`"),
 ("Read until the input ends", "`while (cin >> x) { ... }`"),
 ("Read one character", "`char c; cin >> c;` then compare with `'a'`, `'1'`"),
 ("Read `12+7`", "`int a, b; char op; cin >> a >> op >> b;`"),
 ("Largest so far", "start from the first value, then `if (x > best) best = x;`"),
 ("Very big numbers", "`long long` instead of `int`"),
 ("Fast input", "`ios_base::sync_with_stdio(false); cin.tie(nullptr);`"),
 ("Compile", "`g++ -std=c++17 -O2 -o sol sol.cpp`"),
]

PITFALLS = [
 ("Printing words the judge did not ask for.",
  "`cout << \"Answer: \" << x;` is a wrong answer. Print only what the statement shows."),
 ("Forgetting the space or the new line.",
  "`cout << a << b;` prints `37` for 3 and 7. Write `cout << a << ' ' << b << '\\n';`."),
 ("Comparing a character with a number.",
  "After `char c; cin >> c;` the test `c == 1` is never true for the digit one. Write `c == '1'`."),
 ("Starting the best value at 0.",
  "If every number is negative, the largest is below 0 and `best = 0` gives a wrong answer. Start "
  "from the first number instead."),
 ("Using `endl` in a long loop.",
  "Every `endl` makes the program wait for the screen. Use `'\\n'`."),
]

COMPLEXITY = [
 ["Reading or printing one number", "O(1) - a single step"],
 ["Reading `n` numbers in a loop", "O(n) - one step per number"],
 ["Keeping a sum, a count or a best value while reading", "O(n) time and almost no memory"],
]

# -*- coding: utf-8 -*-
"""Lesson 01 - Setup and I/O. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "01_Setup_And_IO"
BRAND = "Lesson 01 · Setup and I/O"
FOOTER = ("Lesson 01 · C++17 setup and input/output. Problem links point to "
          "arena.olimpiici.com; statements are in Bulgarian and downloadable as PDF from each "
          "problem page.")

PITFALLS_TITLE = "Ten pitfalls that cost real marks"

TITLE = "C++17 Setup and I/O - getting the data in and the answer out"
SUBTITLE = ("Lesson 01 | Theory, cheat sheet and 12 graded problems "
            "from arena.olimpiici.com (Groups D and C)")

HOWTO = [
    "This lesson is built to be worked through in three passes. Do not try to do all three in one "
    "sitting.",
    "**Pass 1 - Read.** Go through sections 1-9 once, typing every snippet into a compiler and "
    "running it. Change a number, run it again, see what happens. Do not try to memorise anything "
    "yet; the aim is only to know what exists and where to find it later.",
    "**Pass 2 - Memorise.** Section 10 is the cheat sheet. Cover the right-hand column and write "
    "out each line from its description alone. Repeat until they all come out without thinking. "
    "Section 11 lists the mistakes that cost marks, and section 12 says what each operation costs.",
    "**Pass 3 - Solve.** Section 13 lists 12 problems from the Olimpiici Arena, ordered from "
    "easiest to hardest and grouped by technique. Solve them in order. Each group points back at "
    "the theory sections that solve it, so when a problem stalls you, re-read that section instead "
    "of looking up a solution.",
    "This is the first lesson and it contains no algorithms at all. Every problem in section 13 is "
    "easy once the data is in your variables - the whole difficulty is getting it there, and "
    "getting the answer back out in exactly the shape the judge expects. That sounds dull. It is "
    "also the reason a great many correct solutions score zero.",
]

SECTIONS = [

# ---------------------------------------------------------------- 1
("skeleton", "1. What a solution looks like", [
 ("p", "Every solution you write in this course has the same five parts. Here is a complete one - "
       "it reads two numbers and prints their sum:"),
 ("code", """#include <iostream>          // the input and output tools

using namespace std;         // so you may write cout instead of std::cout

int main() {                 // the program starts here
    int a, b;
    cin >> a >> b;           // read two numbers
    cout << a + b << '\\n';   // print one
    return 0;                // tell the system all went well
}"""),
 ("p", "Four of those five lines never change. Learn them as one block and type them from memory at "
       "the start of every problem:"),
 ("table", ["Line", "What it does"], [
   ["`#include <iostream>`", "brings in `cin` and `cout`; without it nothing here works"],
   ["`using namespace std;`", "lets you write `cout` instead of `std::cout` everywhere"],
   ["`int main()`", "where the program begins - there must be exactly one"],
   ["`return 0;`", "\"finished, no problem\". You may leave it out of `main`, but write it anyway"],
 ]),
 ("note", "A judge runs your program, feeds it the input, and compares what comes out against the "
          "expected answer. It never looks at your code. So there are no marks for tidy names or "
          "comments - and no forgiveness for one stray space in the output."),
]),

# ---------------------------------------------------------------- 2
("compile", "2. Compiling and running it", [
 ("p", "A C++ file is not a program until the compiler has turned it into one. Save the code as "
       "`sol.cpp` and run this in a terminal in the same folder:"),
 ("code", """g++ -std=c++17 -O2 -Wall -o sol sol.cpp"""),
 ("table", ["Part", "What it means"], [
   ["`g++`", "the compiler"],
   ["`-std=c++17`", "use the 2017 version of the language - what this course is written for"],
   ["`-O2`", "optimise; this is what the judge uses, and it is often twice as fast"],
   ["`-Wall`", "warn me about anything suspicious. **Read the warnings.**"],
   ["`-o sol`", "call the finished program `sol`"],
   ["`sol.cpp`", "the file to compile"],
 ]),
 ("p", "Then run it. On Windows type `sol` or `sol.exe`; on Linux and macOS type `./sol`. The "
       "program waits, you type the input, you press Enter, and the answer appears."),
 ("note", "`-Wall` is the cheapest help you will ever get. A warning about a variable used before it "
          "was given a value, or about comparing two different types, is very often the bug you "
          "would otherwise have spent twenty minutes hunting. If it warns, read it."),
 ("h3", "When it will not compile"),
 ("p", "The compiler prints the **first** error with a line number. Fix that one and compile again - "
       "later errors are often just confusion caused by the first. Three that everybody meets:"),
 ("table", ["Message says something like", "Usually means"], [
   ["`expected ';' before ...`", "a missing semicolon, on the line **above** the one named"],
   ["`'cout' was not declared`", "no `#include <iostream>` or no `using namespace std;`"],
   ["`expected '}' at end of input`", "a `{` somewhere with no matching `}`"],
 ]),
]),

# ---------------------------------------------------------------- 3
("read", "3. Reading numbers with cin", [
 ("p", "`cin >> x` reads one value and puts it into `x`. It skips over any spaces, tabs and newlines "
       "first, so **the layout of the input does not matter at all**. These three inputs are all the "
       "same to the program:"),
 ("code", """int a, b, c;
cin >> a >> b >> c;

//   3 1 4        on one line
//   3            or on three lines
//   1
//   4
//   3   1
//      4         or any other arrangement - all identical"""),
 ("p", "That is why you never need to think about where the line breaks are, as long as you are "
       "reading numbers. The commonest shape by far is *a count, then that many values*:"),
 ("code", """int n;
cin >> n;                    // how many values are coming

int sum = 0;
for (int i = 0; i < n; i++) {
    int x;
    cin >> x;                // the same variable, reused n times
    sum += x;
}
cout << sum << '\\n';"""),
 ("note", "Notice that nothing was stored. The values were read one at a time, added up, and thrown "
          "away. A great many problems need nothing more than that - and when the input is too big "
          "to store, as in group F of section 13, it is the only way. Keeping the whole list is "
          "Lesson 04's job, and you should only do it when the problem really needs it."),
 ("p", "Read into a variable of the right kind. A whole number needs an `int`, a number with a "
       "decimal point needs a `double`, one character needs a `char`:"),
 ("code", """int    n;       cin >> n;      // 42
double d;       cin >> d;      // 3.5
char   c;       cin >> c;      // one character, spaces skipped"""),
 ("note", "If the input contains a number too big for an `int` - anything past about 2 000 000 000 - "
          "you need a `long long`. That is the whole of Lesson 02, and it is the single commonest "
          "cause of a wrong answer in Groups C and D."),
]),

# ---------------------------------------------------------------- 4
("until", "4. When the count is not given", [
 ("p", "Sometimes the input simply stops, with no count to tell you when. `cin >> x` answers "
       "`false` once there is nothing left to read, so it can be the condition of a `while` loop:"),
 ("code", """int x;
int cnt = 0, sum = 0;

while (cin >> x) {           // runs until the input runs out
    cnt++;
    sum += x;
}

cout << cnt << ' ' << sum << '\\n';"""),
 ("note", "Typing that in by hand at the keyboard, the input never \"runs out\" - you have to say so. "
          "Press **Ctrl+Z then Enter** on Windows, or **Ctrl+D** on Linux and macOS - that is how you"
          "tell the program that the input has finished."),
 ("h3", "Several test cases in one file"),
 ("p", "Many statements say \"the first line holds T, the number of test cases\". Wrap your whole "
       "solution in a loop and do not forget to clear anything you carried over:"),
 ("code", """int t;
cin >> t;

while (t--) {                // runs t times
    int a, b;
    cin >> a >> b;
    cout << a + b << '\\n';   // one line of output per test case
}"""),
 ("h3", "Stopping at a special value"),
 ("p", "Others end with a line that is not really data - often `0`, or `0 0`. Read, test, and break "
       "**before** you use the values:"),
 ("code", """int a, b;
while (cin >> a >> b) {
    if (a == 0 && b == 0) break;    // the marker: stop, and do not print anything for it
    cout << a + b << '\\n';
}"""),
]),

# ---------------------------------------------------------------- 5
("print", "5. Printing your answer", [
 ("p", "`cout <<` prints one thing. Chain as many as you like, and put the line break in yourself - "
       "printing never adds one for you."),
 ("code", """int a = 3, b = 4;

cout << a + b << '\\n';                       // 7
cout << \"the answer is \" << a + b << '\\n';   // the answer is 7
cout << a << ' ' << b << '\\n';               // 3 4"""),
 ("p", "When several numbers go on one line, the tidy habit is a space **before** every one except "
       "the first. That leaves no trailing space at the end of the line:"),
 ("code", """int n = 5;
for (int i = 1; i <= n; i++) {
    if (i > 1) cout << ' ';
    cout << i * i;
}
cout << '\\n';                 // 1 4 9 16 25"""),
 ("note", "Judges almost always forgive a trailing space and a missing or extra newline at the very "
          "end. They forgive nothing else - not a capital letter where the statement wanted a small "
          "one, not \"YES\" where it asked for \"Yes\". Copy the wording out of the statement rather "
          "than typing it from memory."),
 ("h3", "Never use endl"),
 ("p", "`endl` prints a line break **and** empties the output buffer, which means asking the "
       "operating system to actually write the text out. Doing that once is nothing. Doing it "
       "100000 times, once per line, is enough on its own to fail a time limit on a solution that "
       "is otherwise perfect."),
 ("code", """cout << x << endl;      // a line break AND a flush - slow
cout << x << '\\n';      // just a line break - use this one"""),
]),

# ---------------------------------------------------------------- 6
("fast", "6. Making cin and cout fast", [
 ("p", "Out of the box, `cin` and `cout` keep themselves in step with the older C functions `scanf` "
       "and `printf`, so that a program may safely use both. Almost no program wants that, and it "
       "makes reading several times slower. These two lines switch it off:"),
 ("code", """int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // the rest of your solution
}"""),
 ("table", ["Line", "What it switches off"], [
   ["`ios_base::sync_with_stdio(false)`", "keeping `cin`/`cout` in step with `scanf`/`printf`"],
   ["`cin.tie(nullptr)`", "flushing `cout` before every single read"],
 ]),
 ("p", "How much does it matter? On a problem that reads 200000 numbers, those two lines are "
       "regularly the difference between passing and failing - with no change at all to your "
       "algorithm. Type them at the start of every solution, out of habit, before you even read the "
       "statement."),
 ("note", "Two rules come with them. **Never mix the two styles in one program** - `cin`/`cout` or "
          "`scanf`/`printf`, pick one and stay with it, because the syncing that made mixing safe is now "
          "gone. And carry on printing `'\\n'` rather than `endl`, for the reason in section 5."),
 ("p", "So the full skeleton, the one you type from memory at the start of every problem:"),
 ("code", """#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // read, work it out, print

    return 0;
}"""),
]),

# ---------------------------------------------------------------- 8
("notnumbers", "7. Reading something that is not just numbers", [
 ("h3", "One character at a time"),
 ("p", "`cin >> c` into a `char` skips whitespace and hands you the next real character. Put it in a "
       "`while` and you can walk through a whole stream of letters without ever storing them - which "
       "is exactly what group B of section 13 asks for:"),
 ("code", """char c;
int ones = 0, zeros = 0;

while (cin >> c) {
    if (c == '1') ones++;
    else if (c == '0') zeros++;
}
cout << ones << ' ' << zeros << '\\n';"""),
 ("h3", "Input in a fixed shape"),
 ("p", "When the input has punctuation in it - `12+7`, or `3/4`, or a date as `21.05.2015` - you do "
       "not need to do anything clever. Read the pieces in the order they appear, using a `char` to "
       "swallow each separator:"),
 ("code", """// the input line is   12+7
int a, b;
char sign;
cin >> a >> sign >> b;          // a = 12, sign = '+', b = 7

// the input line is   21.05.2015
int day, month, year;
char dot;
cin >> day >> dot >> month >> dot >> year;      // 21, 5, 2015"""),
 ("note", "This works because `cin >>` into an `int` stops as soon as it meets something that is not "
          "a digit, and leaves it sitting there for the next read. The `char` then picks it up. It "
          "is the shortest way to read a formatted line, and it solves several problems in group D."),
 ("h3", "A whole line, spaces and all"),
 ("p", "`cin >> s` stops at the first space, so it cannot read a line of several words. `getline` "
       "reads everything up to the line break:"),
 ("code", """#include <string>

string line;
getline(cin, line);              // the whole line, spaces included
cout << line << '\\n';"""),
 ("note", "**The trap.** After `cin >> n`, the newline you pressed after the number is still waiting "
          "in the input. The next `getline` finds it immediately and hands you an empty line. The "
          "cure is one line in between: `cin.ignore();` throws that leftover newline away. Text is "
          "Lesson 03's subject and it goes much further than this - for now, know that `getline` "
          "exists and that this trap exists."),
 ("code", """int n;
cin >> n;
cin.ignore();                    // throw away the rest of that line
string line;
getline(cin, line);              // now this really reads the next line"""),
]),

# ---------------------------------------------------------------- 10
("testing", "8. Testing before you submit", [
 ("p", "The statement always comes with a sample input and a sample answer. Running your program "
       "on that sample is the first thing to do and takes about fifteen seconds: start it, type the "
       "sample input, press Enter, and check what comes back against the expected answer - every "
       "character of it, including the spaces."),
 ("p", "That is only the beginning, though. The sample is written to explain the problem, not to "
       "break your program, so it will happily agree with a solution that is about to score 40."),
 ("h3", "The tests worth inventing yourself"),
 ("p", "Before you submit, try the input the statement allows but the sample never shows. These five "
       "catch most of what a judge will catch:"),
 ("list", [
   "**The smallest allowed input.** `n = 1`, an empty list, one character. Loops that assume there "
   "are at least two things break here.",
   "**The largest allowed input.** If the statement says `n <= 200000`, feed it 200000 values and "
   "time it. A program that takes six seconds will not get faster on the judge.",
   "**The largest allowed values.** Not the most values - the biggest ones. This is where a missing "
   "`long long` shows up, and it is Lesson 02's whole subject.",
   "**Negative numbers and zero**, whenever the statement permits them. A maximum started at 0 "
   "instead of at the first value is wrong the moment the input can be negative.",
   "**All the values the same**, or already sorted, or in reverse. Cheap to write and they catch "
   "an astonishing number of off-by-one mistakes.",
 ]),
 ("note", "A later lesson builds a **stress test**: a small program that makes random inputs, a "
          "slow-but-obviously-correct solution, and a loop that compares the two until they "
          "disagree. It is the single most effective debugging tool in competitive programming. For "
          "now, hand-written edge cases will find most of your bugs."),
]),

# ---------------------------------------------------------------- 11
("judge", "9. What the judge actually checks", [
 ("p", "Understanding what happens after you press submit turns most unexplained scores into "
       "obvious ones. The judge compiles your file, runs it once per test, feeds each test's input "
       "in, and compares your output with the expected output."),
 ("table", ["Verdict", "What it means", "Where to look first"], [
   ["Accepted", "every test matched", "-"],
   ["Wrong answer", "the output differs on some test", "the edge cases in section 8; the wording of your output"],
   ["Time limit exceeded", "too slow on some test", "`endl` in a loop; missing `sync_with_stdio`; the algorithm"],
   ["Memory limit exceeded", "used too much memory", "storing input that could have been streamed"],
   ["Runtime error", "the program crashed or returned something other than 0", "reading past the end of an array; dividing by zero"],
   ["Compilation error", "it did not build on the judge", "compile it yourself with `-std=c++17 -Wall` first"],
 ]),
 ("p", "Three facts that surprise people the first time:"),
 ("list", [
   "**Each test is a fresh run.** Anything your program remembers between test cases inside one "
   "file is your own doing; between separate tests, nothing carries over.",
   "**Partial marks are normal.** Most Group C and D problems are graded per test group, so a "
   "solution that is correct but slow still scores on the small tests. Submit the slow correct "
   "version before you try to make it fast.",
   "**\"It works on my machine\" is not evidence.** An uninitialised variable can hold 0 on your "
   "computer and rubbish on the judge. That is why `-Wall` is in section 2.",
 ]),
 ("note", "Read the statement's limits before you write anything: the largest `n`, the largest "
          "value, the time limit and the memory limit. Those four numbers decide which solution you "
          "should even attempt - and, in group F of section 13, they are the entire problem."),
]),

]

# ---------------------------------------------------------------- 12
CHEATSHEET = [
 ("The whole skeleton", "`#include <iostream>` / `using namespace std;` / `int main() { ... }`"),
 ("Fast input and output", "`ios_base::sync_with_stdio(false); cin.tie(nullptr);`"),
 ("Compile it", "`g++ -std=c++17 -O2 -Wall -o sol sol.cpp`"),
 ("Run it", "`sol` on Windows, `./sol` on Linux and macOS"),
 ("Read one value", "`cin >> x;`"),
 ("Read several", "`cin >> a >> b >> c;` - the layout of the input does not matter"),
 ("Read a count, then that many", "`cin >> n;` then `for (int i = 0; i < n; i++) cin >> x;`"),
 ("Read until the input ends", "`while (cin >> x) { ... }`"),
 ("End the input by hand", "Ctrl+Z then Enter on Windows, Ctrl+D elsewhere"),
 ("T test cases", "`cin >> t; while (t--) { ... }`"),
 ("Stop at a marker", "`if (a == 0 && b == 0) break;` - test before you use the values"),
 ("Print", "`cout << x << '\\n';`"),
 ("Never", "`endl` - it flushes every time and can fail a time limit on its own"),
 ("Several on one line", "`if (i > 0) cout << ' ';` then `cout << v;`"),
 ("Read one character", "`char c; cin >> c;` - whitespace is skipped"),
 ("Read `12+7`", "`int a, b; char sign; cin >> a >> sign >> b;`"),
 ("Read `21.05.2015`", "`cin >> day >> dot >> month >> dot >> year;`"),
 ("Read a whole line", "`string line; getline(cin, line);`"),
 ("After `>>`, before `getline`", "`cin.ignore();`"),
 ("Before submitting", "smallest input, largest input, largest values, negatives, all equal"),
]

# ---------------------------------------------------------------- 13
PITFALLS = [
 ("`endl` instead of `'\\n'`.",
  "`endl` empties the output buffer every single time. Over 100000 lines that alone is enough to "
  "exceed the time limit on an otherwise perfect solution."),
 ("Forgetting the two fast-input lines.",
  "`ios_base::sync_with_stdio(false); cin.tie(nullptr);` regularly decide whether a solution that "
  "reads 200000 numbers passes. Type them before you read the statement."),
 ("Mixing `cin`/`cout` with `scanf`/`printf` after switching the syncing off.",
  "The two no longer agree about what has been read or written, and the output comes out in the "
  "wrong order. Pick one style per program."),
 ("`getline` straight after `cin >> n` gives you an empty line.",
  "The newline from the earlier read is still waiting. Put `cin.ignore();` between the two."),
 ("Printing a prompt.",
  "`cout << \"Enter n: \";` is helpful at the keyboard and fatal on a judge - it becomes part of "
  "your output and nothing will match. Print the answer and nothing else."),
 ("The wrong wording in the output.",
  "\"YES\" is not \"Yes\". Copy the exact word out of the statement instead of typing it from "
  "memory, and mind the capital letters."),
 ("Reading into the wrong type.",
  "`cin >> x` into an `int` when the value passes 2 000 000 000 gives a silently wrong number. "
  "Lesson 02 is about nothing else."),
 ("Storing the input when there was no need.",
  "Many problems can be answered while reading. Storing 10^7 values when a running total would "
  "have done is how a memory limit is exceeded - see group F of section 13."),
 ("Testing only on the sample.",
  "The sample is written to explain the problem, not to break your program. `n = 1` and the "
  "largest allowed input find far more bugs."),
 ("Ignoring the compiler warnings.",
  "`-Wall` warns about exactly the mistakes that behave differently on the judge than on your "
  "machine, an uninitialised variable being the classic. Read them."),
]

# ---------------------------------------------------------------- 14
COMPLEXITY = [
 ["`cin >> x`, with the syncing switched off", "fast - a few tens of nanoseconds"],
 ["`cin >> x`, with the syncing left on", "several times slower, and it adds up over 10^6 reads"],
 ["`cout << x << '\\n'`", "fast - the text is buffered and written in blocks"],
 ["`cout << x << endl`", "slow - it forces a write to the system every single time"],
 ["`ios_base::sync_with_stdio(false)`", "free - one call, at the start"],
 ["Reading n values in a loop", "O(n)"],
 ["Reading n values without storing them", "O(n) time, O(1) memory - prefer this"],
 ["Reading n values into an array", "O(n) time, O(n) memory"],
 ["`getline`", "O(length of the line)"],
 ["A typical time limit", "1-2 seconds, which is about 10^8 simple operations"],
 ["A typical memory limit", "64-256 MB, and sometimes 2-4 MB on purpose"],
]

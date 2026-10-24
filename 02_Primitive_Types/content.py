# -*- coding: utf-8 -*-
"""Lesson 02 - Primitive types. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "02_Primitive_Types"
BRAND = "Lesson 02 · Primitive types"
FOOTER = ("Lesson 02 · C++17 numbers, characters and truth values. Problem links point to "
          "arena.olimpiici.com; statements are in Bulgarian and downloadable as PDF from each "
          "problem page.")

TITLE = "C++17 Numbers - int, long long, bool and double"
SUBTITLE = ("Lesson 02 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("int", "1. int and long long", [
 ("p", "An `int` holds whole numbers from about -2 billion to +2 billion. The exact limits are "
       "-2147483648 and 2147483647."),
 ("p", "When a result goes past that limit, it does not stop with an error. It quietly turns into a "
       "wrong number. This is called **overflow**."),
 ("code", """int a = 100000;
int b = a * a;               // should be 10000000000
cout << b << '\\n';           // prints 1410065408 - wrong!"""),
 ("p", "A `long long` holds whole numbers up to about 9 000 000 000 000 000 000 - a 9 followed by 18 "
       "digits. Use it when the numbers can be big:"),
 ("code", """long long a = 100000;
long long b = a * a;         // 10000000000 - correct"""),
 ("note", "The computer decides the type of `a * a` from `a`, not from where you put the answer. "
          "With `int a`, the line `long long b = a * a;` still overflows, because the multiplying "
          "happens in `int` first. Make the numbers themselves `long long`, or write "
          "`1LL * a * a`."),
 ("p", "A simple rule: if a number in the statement can be bigger than about a billion, or you "
       "multiply two big numbers together, use `long long` for everything."),
]),

# ---------------------------------------------------------------- 2
("divmod", "2. Division and remainder", [
 ("p", "For whole numbers, `/` throws away the part after the point, and `%` gives what is left "
       "over:"),
 ("code", """cout << 17 / 5 << '\\n';      // 3
cout << 17 % 5 << '\\n';      // 2       because 17 = 3 * 5 + 2"""),
 ("table", ["You want", "Write", "Example with 4728"], [
   ["the last digit", "`n % 10`", "8"],
   ["the number without its last digit", "`n / 10`", "472"],
   ["is it even?", "`n % 2 == 0`", "true"],
   ["is it divisible by k?", "`n % k == 0`", "with k = 3: false"],
 ]),
 ("p", "Put the first two together in a loop and you can take any number apart, digit by digit:"),
 ("code", """int n = 4728, sum = 0;
while (n > 0) {
    sum += n % 10;           // add the last digit
    n /= 10;                 // and drop it
}
cout << sum << '\\n';         // 4 + 7 + 2 + 8 = 21"""),
 ("p", "The same two signs change units. 135 minutes is `135 / 60 = 2` hours and "
       "`135 % 60 = 15` minutes."),
 ("p", "Rounding **up**: how many boxes of 6 do you need for 20 eggs? `20 / 6` is only 3. The "
       "trick is `(a + b - 1) / b`, so `(20 + 5) / 6 = 4`."),
]),

# ---------------------------------------------------------------- 3
("formula", "3. A formula instead of a loop", [
 ("p", "Some answers can be counted with a loop, but the loop would take far too long when the "
       "numbers are big. A formula gives the answer in one step."),
 ("p", "**Adding 1 to n.** `1 + 2 + ... + n = n * (n + 1) / 2`. For n = 100 that is "
       "`100 * 101 / 2 = 5050`."),
 ("p", "**Counting multiples.** From 1 to b there are `b / c` multiples of c. From a to b, take "
       "away the ones below a:"),
 ("code", """long long a, b, c;
cin >> a >> b >> c;
cout << b / c - (a - 1) / c << '\\n';"""),
 ("p", "**Counting whole numbers between two others.** Strictly between 3 and 8 lie 4, 5, 6 and "
       "7: that is `8 - 3 - 1 = 4` numbers."),
 ("note", "Always test a formula on a small example by hand. Multiples of 3 from 4 to 10 are 6 "
          "and 9. The formula gives `10 / 3 - 3 / 3 = 3 - 1 = 2`. Correct."),
]),

# ---------------------------------------------------------------- 4
("bool", "4. true and false: bool", [
 ("p", "A `bool` holds one of two values: `true` or `false`. Every comparison gives a `bool`:"),
 ("code", """int n = 12;
bool even = (n % 2 == 0);        // true
if (even) cout << "even\\n";"""),
 ("table", ["Sign", "Means", "Example"], [
   ["`&&`", "and - both must be true", "`x >= 1 && x <= 10`"],
   ["`||`", "or - at least one must be true", "`c == 'a' || c == 'e'`"],
   ["`!`", "not", "`!even`"],
 ]),
 ("note", "`=` puts a value into a variable; `==` compares. `if (x = 5)` sets x to 5 and is always "
          "true. It compiles, so the compiler will not save you."),
]),

# ---------------------------------------------------------------- 5
("double", "5. Decimal numbers and square roots", [
 ("p", "A `double` holds numbers with a decimal point, such as `3.75`. If both numbers in a "
       "division are whole, the answer is whole too. Make one of them a `double` to keep the "
       "part after the point:"),
 ("code", """cout << 7 / 2 << '\\n';        // 3
cout << 7.0 / 2 << '\\n';      // 3.5"""),
 ("p", "To print exactly two digits after the point, add `#include <iomanip>` and write:"),
 ("code", """double x = 2.0 / 3;
cout << fixed << setprecision(2) << x << '\\n';      // 0.67"""),
 ("p", "`sqrt(x)` from `<cmath>` gives the square root. But a `double` is not always exact: "
       "`sqrt(49)` may come out as `6.9999999`, and turning that into an `int` gives 6. So when "
       "you need a **whole** square root, correct it with whole numbers:"),
 ("code", """long long n = 49;
long long r = sqrt(n);
while (r * r > n) r--;                 // r was one too big
while ((r + 1) * (r + 1) <= n) r++;    // r was one too small
if (r * r == n) cout << "perfect square\\n";"""),
 ("note", "Use `double` only when the problem really has decimals. Whole numbers are always exact; "
          "decimals are not - even `0.1 + 0.2` is not exactly `0.3`."),
]),

]

CHEATSHEET = [
 ("Whole numbers above 2 billion", "`long long`"),
 ("Multiply two `int`s safely", "`1LL * a * b`"),
 ("Last digit / drop the last digit", "`n % 10` / `n / 10`"),
 ("Even? Divisible by k?", "`n % 2 == 0`, `n % k == 0`"),
 ("Sum of the digits", "`while (n > 0) { s += n % 10; n /= 10; }`"),
 ("`a / b` rounded up", "`(a + b - 1) / b`"),
 ("`1 + 2 + ... + n`", "`n * (n + 1) / 2`"),
 ("Multiples of c from a to b", "`b / c - (a - 1) / c`"),
 ("and, or, not", "`&&`, `||`, `!`"),
 ("Division with decimals", "`7.0 / 2`"),
 ("Two digits after the point", "`cout << fixed << setprecision(2) << x;`"),
 ("Whole square root", "`long long r = sqrt(n);` then correct it with two `while` loops"),
]

PITFALLS = [
 ("An `int` that overflows gives a wrong number and no warning.",
  "If the answer can pass two billion, use `long long` - for the answer and for the numbers "
  "that make it."),
 ("`long long x = a * b;` with `int a, b` still overflows.",
  "The multiplication happens in `int` first. Write `1LL * a * b` or make `a` and `b` `long long`."),
 ("`7 / 2` is 3, not 3.5.",
  "Whole numbers divide to a whole number. Write `7.0 / 2` when you want the decimals."),
 ("`=` instead of `==` inside an `if`.",
  "`if (x = 0)` changes x and is never true. Compare with `==`."),
 ("Trusting `sqrt` to be exact.",
  "`(int)sqrt(49)` can be 6. Correct the root with whole numbers before you use it."),
]

COMPLEXITY = [
 ["`+ - * / %` on two numbers", "O(1) - a single step"],
 ["Taking a number apart digit by digit", "O(number of digits) - about 19 steps for a `long long`"],
 ["A formula such as `n * (n + 1) / 2`", "O(1), where a loop would be O(n)"],
 ["`sqrt(x)`", "O(1)"],
]

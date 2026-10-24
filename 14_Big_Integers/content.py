# -*- coding: utf-8 -*-
"""Lesson 14 - Big integers. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "14_Big_Integers"
BRAND = "Lesson 14 · Big integers"
FOOTER = ("Lesson 14 · C++17 long-number arithmetic. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Big integers - sums on paper, done by the computer"
SUBTITLE = ("Lesson 14 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("why", "1. When long long is not enough", [
 ("p", "A `long long` holds 19 digits at most. That is not enough for `2^100` (31 digits), for "
       "`50!` (65 digits), or for a number that the input gives you with 200 digits."),
 ("p", "There is no bigger number type in C++. So we do what you learnt at school: write the "
       "number as a row of digits and work digit by digit, carrying and borrowing by hand."),
 ("note", "Before you start, check whether you really need it. If the statement asks only for the "
          "answer modulo some number, or the numbers fit in 18 digits, `long long` is enough."),
]),

# ---------------------------------------------------------------- 2
("digits", "2. A long number as a row of digits", [
 ("p", "Read the number as a `string`, then keep its digits in a `vector<int>` **backwards**: "
       "`d[0]` is the ones digit, `d[1]` the tens, and so on. Backwards is easier, because on "
       "paper we also start from the ones, and a new digit at the front is just a `push_back`."),
 ("code", """vector<int> make(string s) {            // "1234" -> {4, 3, 2, 1}
    vector<int> d;
    int n = s.size();
    for (int i = n - 1; i >= 0; i--) d.push_back(s[i] - '0');
    return d;
}

void print(vector<int> d) {             // prints from the last element
    int n = d.size();
    for (int i = n - 1; i >= 0; i--) cout << d[i];
    cout << '\\n';
}"""),
 ("p", "All the functions below use this form. They need `#include <vector>` and `<string>`."),
]),

# ---------------------------------------------------------------- 3
("add", "3. Adding", [
 ("p", "Add place by place, starting from the ones. Write down `s % 10` and carry `s / 10` to the "
       "next place - exactly like on paper:"),
 ("code", """vector<int> add(vector<int> a, vector<int> b) {
    vector<int> c;
    int na = a.size(), nb = b.size();
    int carry = 0;
    for (int i = 0; i < na || i < nb || carry > 0; i++) {
        int s = carry;
        if (i < na) s += a[i];
        if (i < nb) s += b[i];
        c.push_back(s % 10);
        carry = s / 10;
    }
    return c;
}

print(add(make("999"), make("25")));    // 1024"""),
 ("p", "The loop goes on while there is a carry left, so the extra digit at the front is never "
       "lost."),
]),

# ---------------------------------------------------------------- 4
("mulsmall", "4. Multiplying by a small number", [
 ("p", "Multiplying a long number by an ordinary number `k` is the same loop. The carry can now be "
       "bigger than 9, so keep it in a `long long`:"),
 ("code", """vector<int> mul_small(vector<int> a, long long k) {
    vector<int> c;
    int n = a.size();
    long long carry = 0;
    for (int i = 0; i < n || carry > 0; i++) {
        long long cur = carry;
        if (i < n) cur += a[i] * k;
        c.push_back(cur % 10);
        carry = cur / 10;
    }
    while (c.size() > 1 && c.back() == 0) c.pop_back();   // k = 0 leaves zeros
    return c;
}

vector<int> f = make("1");                // 20! = 1 * 2 * 3 * ... * 20
for (int k = 2; k <= 20; k++) f = mul_small(f, k);
print(f);                                 // 2432902008176640000"""),
 ("p", "Powers of two, factorials and \"multiply by x again and again\" are all this one "
       "function in a loop."),
]),

# ---------------------------------------------------------------- 5
("sub", "5. Subtracting and comparing", [
 ("p", "Subtract place by place. When a digit would go below 0, add 10 and **borrow** 1 from the "
       "next place. This version needs `a >= b`:"),
 ("code", """vector<int> sub(vector<int> a, vector<int> b) {     // a must be >= b
    int na = a.size(), nb = b.size();
    int borrow = 0;
    for (int i = 0; i < na; i++) {
        int cur = a[i] - borrow;
        if (i < nb) cur -= b[i];
        if (cur < 0) { cur += 10; borrow = 1; }
        else borrow = 0;
        a[i] = cur;
    }
    while (a.size() > 1 && a.back() == 0) a.pop_back();   // 1000 - 999 = 0001 -> 1
    return a;
}"""),
 ("p", "Comparing: the number with more digits is bigger. With the same number of digits, compare "
       "from the first digit (the last element):"),
 ("code", """bool smaller(vector<int> a, vector<int> b) {      // is a < b ?
    if (a.size() != b.size()) return a.size() < b.size();
    int n = a.size();
    for (int i = n - 1; i >= 0; i--)
        if (a[i] != b[i]) return a[i] < b[i];
    return false;                                  // they are equal
}"""),
]),

# ---------------------------------------------------------------- 6
("mulbig", "6. Multiplying two long numbers", [
 ("p", "Long multiplication from school: digit `i` of `a` times digit `j` of `b` lands at place "
       "`i + j`. Add everything up first, then do all the carrying in one pass:"),
 ("code", """vector<int> mul_big(vector<int> a, vector<int> b) {
    int n = a.size(), m = b.size();
    vector<long long> c(n + m, 0);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            c[i + j] += a[i] * b[j];
    vector<int> r;
    long long carry = 0;
    for (int i = 0; i < n + m; i++) {
        long long cur = c[i] + carry;
        r.push_back(cur % 10);
        carry = cur / 10;
    }
    while (r.size() > 1 && r.back() == 0) r.pop_back();
    return r;
}"""),
]),

# ---------------------------------------------------------------- 7
("div", "7. Dividing by a small number", [
 ("p", "Division goes the other way: from the **first** digit, like on paper. Bring down a digit, "
       "divide, keep the remainder:"),
 ("code", """vector<int> div_small(vector<int> a, long long k) {
    int n = a.size();
    vector<int> q(n, 0);
    long long r = 0;
    for (int i = n - 1; i >= 0; i--) {     // from the first digit
        r = r * 10 + a[i];
        q[i] = r / k;
        r = r % k;
    }
    while (q.size() > 1 && q.back() == 0) q.pop_back();
    return q;
}

long long mod_small(vector<int> a, long long k) {   // only the remainder
    int n = a.size();
    long long r = 0;
    for (int i = n - 1; i >= 0; i--) r = (r * 10 + a[i]) % k;
    return r;
}"""),
 ("p", "`mod_small` answers \"is this 300-digit number divisible by 7?\" without building any "
       "new number at all."),
]),

]

CHEATSHEET = [
 ("Store a long number", "`vector<int>` of digits, ones digit first"),
 ("String to digits", "walk the string from the end, `push_back(s[i] - '0')`"),
 ("Print", "from the last element down to element 0"),
 ("Add", "`s = a[i] + b[i] + carry`; write `s % 10`, carry `s / 10`; go on while a carry is left"),
 ("Times a small `k`", "`cur = a[i] * k + carry` in `long long`"),
 ("Subtract (`a >= b`)", "below 0: add 10 and borrow 1; drop leading zeros at the end"),
 ("Compare", "more digits is bigger; else compare from the first digit"),
 ("Times a long number", "`c[i + j] += a[i] * b[j]`, then one carrying pass"),
 ("Divide by a small `k`", "from the first digit: `r = r * 10 + a[i]`, `q[i] = r / k`, `r %= k`"),
 ("Remainder only", "`r = (r * 10 + a[i]) % k` from the first digit"),
]

PITFALLS = [
 ("Printing the digits in the stored order.",
  "They are stored backwards. Print from the last element to element 0."),
 ("Losing the last carry.",
  "`999 + 1` needs a fourth digit. Keep looping while `carry > 0`."),
 ("Leading zeros.",
  "After subtracting or dividing, `0001` must print as `1`. Pop zeros from the back - but keep "
  "at least one digit, so that 0 still prints."),
 ("Comparing numbers as strings.",
  "`\"9\" > \"10\"` is true for strings. Compare the lengths first."),
 ("Forgetting `- '0'`.",
  "`s[i]` is the character `'7'`, which is 55. The digit is `s[i] - '0'`."),
]

COMPLEXITY = [
 ["Adding or subtracting two numbers of `n` digits", "O(n)"],
 ["Multiplying or dividing by a small number", "O(n)"],
 ["Comparing", "O(n)"],
 ["Multiplying two numbers of `n` and `m` digits", "O(n * m)"],
]

# -*- coding: utf-8 -*-
"""Lesson 03 - Strings. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "03_Strings"
BRAND = "Lesson 03 · Strings"
FOOTER = ("Lesson 03 · C++17 strings. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

LEGACY_DONE_KEY = "str_done"   # progress saved before the site-wide key scheme

TITLE = "C++17 Strings - words, letters and text"
SUBTITLE = ("Lesson 03 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("basics", "1. A string is a row of characters", [
 ("p", "A `string` holds text. Add `#include <string>` at the top. The characters have numbered "
       "places, and counting starts at 0:"),
 ("code", """string s = "hello";

//  place:      0    1    2    3    4
//  character: 'h'  'e'  'l'  'l'  'o'

cout << s[0] << '\\n';        // h
cout << s.size() << '\\n';    // 5
cout << s[s.size() - 1];     // o - the last character"""),
 ("p", "`cin >> s` reads one **word**: everything up to the next space or new line."),
 ("p", "To look at every character, loop over the places. Write `int n = s.size();` first and use "
       "`n` in the loop:"),
 ("code", """string s;
cin >> s;
int n = s.size();
int vowels = 0;
for (int i = 0; i < n; i++) {
    if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') vowels++;
}
cout << vowels << '\\n';"""),
 ("p", "There is also a short form that hands you each character in turn, when you do not need its "
       "place: `for (char c : s) { ... }`."),
]),

# ---------------------------------------------------------------- 2
("chars", "2. Characters are numbers", [
 ("p", "Inside the computer every character is a small number, its **ASCII code**. The letters and "
       "the digits come in order:"),
 ("table", ["Characters", "Codes"], [
   ["`'0'` ... `'9'`", "48 ... 57"],
   ["`'A'` ... `'Z'`", "65 ... 90"],
   ["`'a'` ... `'z'`", "97 ... 122"],
 ]),
 ("p", "You never need to remember the codes. Because they are in order, subtracting the first one "
       "gives a small number you can use:"),
 ("code", """int d = '7' - '0';            // 7      digit character -> its value
int i = 'c' - 'a';            // 2      letter -> its place in the alphabet, from 0
char c = 'a' + 2;             // 'c'    place -> letter
char e = '0' + 7;             // '7'    value -> digit character"""),
 ("p", "`#include <cctype>` gives ready-made tests and changes:"),
 ("table", ["Call", "Gives"], [
   ["`isdigit(c)`", "true for `'0'` ... `'9'`"],
   ["`isalpha(c)`", "true for a letter"],
   ["`isupper(c)` / `islower(c)`", "true for a capital / a small letter"],
   ["`toupper(c)` / `tolower(c)`", "the same letter as a capital / as a small letter"],
 ]),
]),

# ---------------------------------------------------------------- 3
("walk", "3. Walking along a string", [
 ("p", "A **run** is a block of equal characters side by side: `\"aaabbc\"` has three runs. Push "
       "`j` forward while the character stays the same, then jump `i` to `j`:"),
 ("code", """string s = "aaabbc";
int n = s.size();
int i = 0;
while (i < n) {
    int j = i;
    while (j < n && s[j] == s[i]) j++;
    cout << s[i] << ' ' << j - i << '\\n';   // a 3, then b 2, then c 1
    i = j;
}"""),
 ("p", "`s.find(t)` gives the place where `t` first appears inside `s`. When `t` is not there, it "
       "gives the special value `string::npos`:"),
 ("code", """string s = "banana";
if (s.find("nan") != string::npos) cout << "found\\n";
cout << s.find('n') << '\\n';    // 2"""),
]),

# ---------------------------------------------------------------- 4
("change", "4. Changing and comparing strings", [
 ("table", ["Call", "Does", "Example with `s = \"hello\"`"], [
   ["`s += t`", "adds `t` (a string or a character) at the end", "`s += '!'` gives `\"hello!\"`"],
   ["`s + t`", "a new string, `s` and `t` glued", "`s + \" you\"` is `\"hello you\"`"],
   ["`s.substr(p, len)`", "a copy of `len` characters starting at place `p`", "`s.substr(1, 3)` is `\"ell\"`"],
   ["`reverse(s.begin(), s.end())`", "turns `s` back to front (needs `<algorithm>`)", "`\"olleh\"`"],
 ]),
 ("p", "The easiest way to remove characters is to build a new string from the ones you keep:"),
 ("code", """string s = "a-b-c", t = "";
for (char c : s)
    if (c != '-') t += c;
cout << t << '\\n';          // abc"""),
 ("p", "`==` and `<` compare strings like a dictionary: letter by letter from the left. "
       "`\"apple\" < \"apply\"` is true because `'e'` comes before `'y'`."),
 ("note", "Every capital letter has a smaller code than every small letter, so `\"Zoo\" < \"apple\"` "
          "is true. Make the letters the same case before comparing words."),
]),

# ---------------------------------------------------------------- 5
("line", "5. Reading a whole line", [
 ("p", "`cin >> s` stops at the first space. To read a line with spaces in it, use `getline`:"),
 ("code", """string line;
getline(cin, line);           // input: I like C++
cout << line.size() << '\\n';  // 10"""),
 ("note", "After `cin >> n`, the end of that line is still waiting. A `getline` right after it reads "
          "an empty line. Put `cin.ignore();` between them."),
 ("code", """int n;
cin >> n;
cin.ignore();                 // skip the end of the line with n
string line;
getline(cin, line);           // now this is the next line"""),
]),

# ---------------------------------------------------------------- 6
("count", "6. Counting letters", [
 ("p", "Many string problems are solved by counting how often each letter appears. Make an array "
       "with one box per letter. `c - 'a'` tells you which box:"),
 ("code", """string s;
cin >> s;                         // small letters only
int cnt[26] = {0};                // 26 boxes, all 0
for (char c : s) cnt[c - 'a']++;

cout << cnt['e' - 'a'] << '\\n';   // how many 'e'

int best = 0;                     // the most common letter
for (int i = 1; i < 26; i++)
    if (cnt[i] > cnt[best]) best = i;
cout << char('a' + best) << '\\n';"""),
 ("p", "Two words are **anagrams** (the same letters in another order) exactly when all 26 counts "
       "are equal."),
]),

# ---------------------------------------------------------------- 7
("pal", "7. Palindromes", [
 ("p", "A palindrome reads the same backwards: `level`, `abba`. Check it with two places, one "
       "coming from the left and one from the right:"),
 ("code", """bool is_pal(string s) {
    int n = s.size();
    int i = 0, j = n - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++;
        j--;
    }
    return true;
}"""),
 ("p", "The short way makes a reversed copy and compares:"),
 ("code", """string r = s;
reverse(r.begin(), r.end());
bool pal = (s == r);"""),
 ("p", "One more rule worth knowing: the letters of a word can be **rearranged** into a palindrome "
       "exactly when at most one letter appears an odd number of times. All the others pair up "
       "around the middle."),
]),

]

CHEATSHEET = [
 ("Length / one character", "`s.size()` / `s[i]`, counting from 0"),
 ("Read a word / a line", "`cin >> s` / `getline(cin, s)`"),
 ("After `cin >> n`, before `getline`", "`cin.ignore();`"),
 ("Digit character to number", "`c - '0'`"),
 ("Letter to 0..25 and back", "`c - 'a'`, `char('a' + i)`"),
 ("Tests and changes", "`isdigit`, `isalpha`, `isupper`, `islower`, `toupper`, `tolower`"),
 ("Add at the end", "`s += t`, `s += c`"),
 ("A piece", "`s.substr(p, len)` - the second number is a length"),
 ("Is `t` inside `s`?", "`s.find(t) != string::npos`"),
 ("Turn back to front", "`reverse(s.begin(), s.end())`"),
 ("Count the letters", "`int cnt[26] = {0}; for (char c : s) cnt[c - 'a']++;`"),
 ("Palindrome", "`i` from the left, `j` from the right, compare and move inwards"),
]

PITFALLS = [
 ("Places start at 0.",
  "In `\"hello\"` the last character is `s[4]`, not `s[5]`. `s[s.size()]` is outside the string."),
 ("The second number of `substr` is a length, not an end place.",
  "`s.substr(2, 3)` is three characters starting at place 2."),
 ("`getline` right after `cin >> n` reads an empty line.",
  "The end of the line with `n` is still waiting. Put `cin.ignore();` between them."),
 ("`cnt[c - 'a']` with a capital letter or a digit.",
  "`'A' - 'a'` is negative and lands outside the array. Use `tolower(c)` first, or check "
  "`islower(c)`."),
 ("Capitals come before all small letters.",
  "`\"Zoo\" < \"apple\"` is true. Make the case the same before comparing or sorting words."),
]

COMPLEXITY = [
 ["`s[i]`, `s.size()`, `s += c`", "O(1)"],
 ["Looping over all characters", "O(n)"],
 ["`s.find(t)`, `s.substr(p, len)`, `reverse`, `==`", "O(n) - they walk the string"],
 ["Counting letters into `cnt[26]`", "O(n)"],
 ["Palindrome check", "O(n)"],
]

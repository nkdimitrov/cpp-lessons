# -*- coding: utf-8 -*-
"""Lesson 03 - Strings. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "03_Strings"
BRAND = "Lesson 03 · Strings"
FOOTER = ("Lesson 03 · C++17 strings. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

LEGACY_DONE_KEY = "str_done"   # progress saved before the site-wide key scheme

PITFALLS_TITLE = "Eleven pitfalls that cost real marks"

TITLE = "C++17 Strings - the contest toolkit"
SUBTITLE = ("Lesson 03 | Theory, cheat sheet and 24 graded problems "
            "from arena.olimpiici.com (Group D)")

HOWTO = [
    "This lesson is built to be worked through in three passes. Do not try to do all three in one "
    "sitting.",
    "**Pass 1 - Read.** Go through sections 1-11 once, typing every snippet into a compiler and "
    "running it. Change a number, run it again, see what happens. Do not try to memorise anything "
    "yet; the aim is only to know what exists and where to find it later.",
    "**Pass 2 - Memorise.** Section 12 is the cheat sheet. Cover the right-hand column and write "
    "out each line from its description alone. Repeat until they all come out without thinking. "
    "Section 13 lists the mistakes that cost marks, and section 14 says how fast each operation is.",
    "**Pass 3 - Solve.** Section 15 lists 24 problems from the Olimpiici Arena, Group D, ordered "
    "from easiest to hardest and grouped by technique. Solve them in order. Each group points back "
    "at the theory sections that solve it, so when a problem stalls you, re-read that section "
    "instead of looking up a solution.",
]

SECTIONS = [

# ---------------------------------------------------------------- 1
("setup", "1. Getting started: headers and fast input", [
 ("p", "Every program in this lesson begins the same way. These five headers cover everything the "
       "lesson uses, so include them all at the top."),
 ("code", """#include <iostream>
#include <string>       // string, stoi, to_string
#include <vector>       // vector
#include <cctype>       // isalpha, isdigit, toupper, tolower, ...
#include <algorithm>    // sort, reverse, count, ...

using namespace std;"""),
 ("p", "`cin` and `cout` are slow out of the box, because they keep themselves in step with the "
       "older C functions `scanf` and `printf`. A problem that reads 100000 words can run out of "
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
("basics", "2. Making a string and reading its characters", [
 ("p", "A `string` is a row of characters with numbered positions. Counting starts at 0, so the "
       "first character is `s[0]` and the last one is `s[s.size() - 1]`."),
 ("code", """string s = "hello";

//  position:   0    1    2    3    4
//  character: 'h'  'e'  'l'  'l'  'o'

cout << s[0];             // h
cout << s[4];             // o
cout << s.size();         // 5"""),
 ("p", "The ways to make one:"),
 ("code", """string a;                 // ""        empty
string b = "hello";       // "hello"
string c(5, 'x');         // "xxxxx"   five copies of one character
string d = b;             // "hello"   an independent copy of b
string e = b + "!";       // "hello!"  + glues strings together
string f(b, 1, 3);        // "ell"     from b, start at 1, take 3 characters"""),
 ("table", ["Member", "What it does", "Cost"], [
   ["`s.size()`", "How many characters there are. `s.length()` is the very same function.", "O(1)"],
   ["`s.empty()`", "`true` when there are no characters at all. Prefer it to `s.size() == 0`.", "O(1)"],
   ["`s.clear()`", "Throws every character away, leaving `\"\"`.", "O(1)"],
   ["`s[i]`", "The character at position `i`. **Does not check** that position `i` exists.", "O(1)"],
   ["`s.at(i)`", "The same character, but stops the program with an error message when `i` is out of "
                 "range. Useful while hunting a bug.", "O(1)"],
   ["`s.front()` / `s.back()`", "First / last character. Never call them on an empty string.", "O(1)"],
 ]),
 ("p", "Four ways to walk over a string. All four are worth recognising when you read someone "
       "else's code:"),
 ("code", """string s = "hello";
int n = s.size();

for (int i = 0; i < n; i++)      cout << s[i];    // by position
for (char c : s)                 cout << c;       // every character, read only
for (char& c : s)                c = 'x';         // the & lets you change it
for (int i = n - 1; i >= 0; i--) cout << s[i];    // backwards"""),
 ("note", "`s.size()` is an **unsigned** number: it can never be negative, and subtracting past zero "
          "does not give -1, it gives a gigantic number. So `for (int i = 0; i < s.size() - 1; i++)` "
          "on an empty string loops billions of times instead of none. The cure is a habit: write "
          "`int n = s.size();` on the line before the loop and use `n` from then on."),
]),

# ---------------------------------------------------------------- 3
("chars", "3. Characters are numbers", [
 ("p", "This is the single most useful idea in the lesson. A `char` is not a special kind of thing - "
       "it is a small whole number, the character's ASCII code, and you may do arithmetic on it. "
       "The codes worth knowing:"),
 ("table", ["Characters", "Codes"], [
   ["`'0'` ... `'9'`", "48 ... 57"],
   ["`'A'` ... `'Z'`", "65 ... 90"],
   ["`'a'` ... `'z'`", "97 ... 122"],
   ["`' '` (space)", "32"],
 ]),
 ("p", "You almost never need the numbers themselves, because the letters and the digits are stored "
       "in order. Subtracting the first character of a run turns a character into a small index, and "
       "adding it turns the index back into a character:"),
 ("code", """int  d  = '7' - '0';           // 7      digit character -> its value
char ch = char('0' + 7);       // '7'    value -> digit character

int  i  = 'c' - 'a';           // 2      letter -> index 0..25
char c2 = char('a' + 2);       // 'c'    index -> letter

int  up = 'C' - 'A';           // 2      the same trick for capitals

// the digit sum of a number given as text
string s = "9251";
int sum = 0;
for (char c : s) sum += c - '0';     // 9 + 2 + 5 + 1 = 17"""),
 ("p", "The `<cctype>` header names the tests you would otherwise write by hand:"),
 ("table", ["Function", "True for"], [
   ["`isalpha(c)`", "A-Z, a-z"],
   ["`isdigit(c)`", "0-9"],
   ["`isalnum(c)`", "a letter or a digit"],
   ["`isspace(c)`", "space, tab, newline"],
   ["`isupper(c)` / `islower(c)`", "a capital / a small letter"],
   ["`ispunct(c)`", "a printable character that is neither a letter, a digit, nor a space"],
   ["`toupper(c)` / `tolower(c)`", "**not a test** - gives back the converted character, unchanged "
                                   "when it is not a letter"],
 ]),
 ("code", """string s = "Hello, World 42!";

int letters = 0, digits = 0, spaces = 0;
for (char c : s) {
    if (isalpha(c)) letters++;
    else if (isdigit(c)) digits++;
    else if (isspace(c)) spaces++;
}
// letters = 10, digits = 2, spaces = 2

// turn the whole string into capitals, in place
for (char& c : s) c = toupper(c);"""),
 ("note", "If the input can contain letters outside A-Z and a-z - Cyrillic, for instance - write "
          "`isalpha((unsigned char)c)`. The cast costs nothing, is always correct, and without it "
          "those characters can crash the program."),
]),

# ---------------------------------------------------------------- 4
("modify", "4. Changing a string", [
 ("table", ["Call", "Effect", "Cost"], [
   ["`s += t`", "Glue `t` onto the end. `t` may be a string, a piece of text in quotes, or a single "
                "character.", "O(length of `t`)"],
   ["`s.push_back(c)`", "Add one character at the end.", "O(1)"],
   ["`s.pop_back()`", "Remove the last character. Never on an empty string.", "O(1)"],
   ["`s.insert(pos, t)`", "Push `t` in **before** position `pos`.", "O(n)"],
   ["`s.erase(pos, len)`", "Delete `len` characters starting at `pos`.", "O(n)"],
   ["`s.erase(pos)`", "Delete everything from `pos` to the end - a chop.", "O(n)"],
   ["`s.replace(pos, len, t)`", "Swap the `len` characters at `pos` for `t`. The two lengths need "
                                "not match.", "O(n)"],
   ["`s.substr(pos, len)`", "A **copy** of `len` characters starting at `pos`. The second number is "
                            "a length, not an end position.", "O(len)"],
 ]),
 ("code", """string s = "competitive";
s.insert(0, ">> ");             // ">> competitive"
s.erase(0, 3);                  // "competitive"
s.replace(0, 4, "REPE");        // "REPEtitive"
string mid  = s.substr(4, 6);   // "titive"      6 is a LENGTH
string tail = s.substr(4);      // "titive"      no length means "to the end"
s.pop_back();                   // "REPEtitiv\""""),
 ("p", "To throw characters away, the clearest method is to build a new string out of the ones you "
       "are keeping. It is easy to read, easy to change when the rule changes, and it walks the "
       "string only once:"),
 ("code", """string s = "a b c d";
string t = "";
for (char c : s)
    if (c != ' ') t += c;       // keep everything that is not a space
s = t;                          // "abcd\""""),
 ("p", "The same job in one line, when you are deleting one particular character. `remove` shuffles "
       "the survivors to the front and reports where they end; `erase` does the actual shortening. "
       "The two always travel together:"),
 ("code", """s.erase(remove(s.begin(), s.end(), ' '), s.end());   // drop every space"""),
 ("note", "Inside a loop, `s += x` is fast but `s = s + x` is catastrophically slow: the second form "
          "builds a whole new copy of `s` every time round. On a string of 100000 characters that is "
          "the difference between instant and several minutes."),
]),

# ---------------------------------------------------------------- 5
("search", "5. Finding something inside a string", [
 ("p", "Every search function below gives back the position of what it found - and `string::npos` "
       "when there is nothing to find. `npos` is a huge number, not -1, so always compare against "
       "`string::npos` by name, and keep the answer in a `size_t`, never in an `int`."),
 ("table", ["Call", "Finds"], [
   ["`s.find(t)`", "The first place where the whole of `t` appears."],
   ["`s.find(t, from)`", "The same, but starting the hunt at position `from`."],
   ["`s.rfind(t)`", "The **last** place where `t` appears."],
   ["`s.find_first_of(set)`", "The first position holding **any one** of the characters in `set`."],
   ["`s.find_last_of(set)`", "The last position holding any one of them."],
   ["`s.find_first_not_of(set)`", "The first position holding a character that is **not** in `set`."],
   ["`s.find_last_not_of(set)`", "The last position holding a character that is not in `set`."],
 ]),
 ("code", """string s = "mississippi";

size_t p = s.find("ss");               // 2
size_t q = s.rfind("ss");              // 5
size_t v = s.find_first_of("aeiou");   // 1     the first 'i'
size_t z = s.find("zz");               // string::npos - not there

if (s.find("ss") != string::npos) cout << "found\\n";

// count every occurrence of a pattern, overlaps included
int cnt = 0;
for (size_t i = s.find("iss"); i != string::npos; i = s.find("iss", i + 1))
    cnt++;                             // 2"""),
 ("p", "C++17 has no `starts_with`, `ends_with` or `contains` - those arrived in later standards. "
       "They are three lines each:"),
 ("code", """bool starts_with(string s, string p) {
    return s.size() >= p.size() && s.substr(0, p.size()) == p;
}
bool ends_with(string s, string p) {
    return s.size() >= p.size() && s.substr(s.size() - p.size()) == p;
}
bool contains(string s, string p) {
    return s.find(p) != string::npos;
}"""),
 ("p", "Cutting the spaces off both ends of a line - trimming - is `find_first_not_of` paired with "
       "`find_last_not_of`:"),
 ("code", """string trim(string s) {
    size_t b = s.find_first_not_of(" \\t");
    if (b == string::npos) return "";        // the line was all spaces
    size_t e = s.find_last_not_of(" \\t");
    return s.substr(b, e - b + 1);
}"""),
]),

# ---------------------------------------------------------------- 6
("compare", "6. Comparing strings", [
 ("p", "`==`, `!=`, `<`, `<=`, `>` and `>=` all work on strings, and they compare the way a "
       "dictionary orders words: character by character, from the left, using the ASCII codes. The "
       "first position where the two strings differ decides everything. If one string runs out "
       "first, it is the smaller one."),
 ("code", """string a = "apple", b = "apply";

a == b;            // false
a <  b;            // true    'e' (101) < 'y' (121) at position 4

string("abc") < string("abcd");     // true    the shorter prefix is smaller"""),
 ("note", "Dictionary order is not alphabetical order once capitals are involved. Every capital "
          "letter has a smaller code than every small letter, so `\"Zebra\" < \"apple\"` is `true`, "
          "and sorting a list of names leaves all the capitalised ones in front. For a real "
          "alphabetical sort, make the case the same first."),
 ("p", "Comparing while ignoring the case is done by flattening both strings and then using `==`:"),
 ("code", """bool same_ignoring_case(string x, string y) {
    for (char& c : x) c = tolower(c);
    for (char& c : y) c = tolower(c);
    return x == y;
}"""),
 ("p", "Because `<` works, `sort` sorts a `vector<string>` with no extra effort, and `min` picks the "
       "dictionary-smallest of two answers - which is exactly what a problem asking for \"the "
       "smallest such word\" wants:"),
 ("code", """vector<string> v = {"pear", "Apple", "fig"};
sort(v.begin(), v.end());        // {"Apple", "fig", "pear"}

string best = "zzzzzz";
best = min(best, candidate);     // keep the dictionary-smallest seen so far"""),
]),

# ---------------------------------------------------------------- 7
("convert", "7. Strings and numbers", [
 ("table", ["Call", "Meaning"], [
   ["`stoi(s)`", "The text `s` as an `int`."],
   ["`stoll(s)`", "The same as a `long long`, for numbers above about two billion."],
   ["`stod(s)`", "The same as a `double`."],
   ["`to_string(x)`", "Any number turned into text."],
 ]),
 ("code", """int       n   = stoi("42");            // 42
long long big = stoll("9000000000");  // too big for an int
string    s   = to_string(255);       // "255\""""),
 ("note", "`stoi` is fussier than it looks. It **stops** at the first character that is not part of "
          "a number, so `stoi(\"12abc\")` is `12` and no complaint is made. And it **stops the "
          "program** when the text does not begin with a number at all, or when the number will not "
          "fit in an `int` - `stoi(\"9000000000\")` is a runtime error, not a wrong answer. When the "
          "number may be long, use `stoll`."),
 ("p", "You will often want the conversion by hand instead. It is one line, and unlike `stoi` it "
       "keeps working on numbers far too long for any built-in type, because you handle the digits "
       "one at a time:"),
 ("code", """string s = "12345";
long long v = 0;
for (char c : s) v = v * 10 + (c - '0');     // 12345"""),
 ("p", "Writing a number in another base is the same loop in reverse, and it is exactly what "
       "base-conversion problems ask for. The digits come out backwards, so the last step is a "
       "`reverse`:"),
 ("code", """// n written in base b, where 2 <= b <= 36
string to_base(long long n, int b) {
    if (n == 0) return "0";
    string r = "";
    while (n > 0) {
        int d = n % b;
        r += (d < 10 ? char('0' + d) : char('A' + d - 10));
        n /= b;
    }
    reverse(r.begin(), r.end());
    return r;
}"""),
]),

# ---------------------------------------------------------------- 8
("algo", "8. Ready-made tools from <algorithm>", [
 ("p", "A string is a container of characters, so the standard algorithms work on it. Each one wants "
       "to be told where to start and where to stop; `s.begin(), s.end()` is how you say \"the whole "
       "string\"."),
 ("code", """string s = "competitive";

sort(s.begin(), s.end());                     // "ceeiimopttv"
reverse(s.begin(), s.end());                  // back to front

int e = count(s.begin(), s.end(), 'e');       // 2   how many 'e' there are
char mx = *max_element(s.begin(), s.end());   // the largest character

// remove repeats: unique only deletes NEIGHBOURING copies, so sort first
sort(s.begin(), s.end());
s.erase(unique(s.begin(), s.end()), s.end()); // "ceimoptv"

// walk through every rearrangement, in dictionary order (sort first!)
string p = "abc";
sort(p.begin(), p.end());
do {
    cout << p << '\\n';                        // abc acb bac bca cab cba
} while (next_permutation(p.begin(), p.end()));"""),
 ("p", "Sorting a string deserves a second look, because it gives you a **fingerprint**: two words "
       "are anagrams of each other exactly when their sorted forms are identical. `\"listen\"` and "
       "`\"silent\"` both sort to `\"eilnst\"`."),
 ("p", "Checking for a palindrome - a word that reads the same backwards - is the two-pointer loop. "
       "One index walks in from the left, the other from the right, and they compare as they go:"),
 ("code", """bool is_palindrome(string s) {
    int i = 0, j = (int)s.size() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++;
        j--;
    }
    return true;
}"""),
 ("p", "The short version, for when you do not mind making a copy, builds the string backwards and "
       "compares the two:"),
 ("code", """string r(s.rbegin(), s.rend());     // s, backwards
bool pal = (s == r);"""),
]),

# ---------------------------------------------------------------- 9
("io", "9. Reading the input", [
 ("table", ["Form", "Reads"], [
   ["`cin >> s`", "One **word** - everything up to the next space or newline. Any spaces in front "
                  "are skipped and thrown away."],
   ["`getline(cin, s)`", "A whole **line**, spaces included, without the newline at the end."],
   ["`while (cin >> s)`", "Word after word, until the input runs out."],
   ["`while (getline(cin, line))`", "Line after line, until the input runs out."],
   ["`cin.get(c)`", "Exactly one character, spaces and newlines included."],
 ]),
 ("note", "**The trap everybody falls into once.** After `cin >> n`, the newline that ended that "
          "line is still waiting in the input. The next `getline` finds it immediately and hands "
          "you an empty string. Throw it away with `cin.ignore();` in between."),
 ("code", """int n;
cin >> n;
cin.ignore();               // eat the leftover newline
string line;
getline(cin, line);         // now this really does read the next line"""),
 ("p", "When the input is nothing but words, and the line breaks do not matter, `cin >> word` is all "
       "the splitting you need - it treats every run of spaces and newlines as a separator:"),
 ("code", """string word;
while (cin >> word) cout << word.size() << '\\n';    // the length of every word"""),
 ("p", "When the line structure does matter, read the line whole and cut it up yourself. Walk across "
       "it collecting characters into `part`, and every time you meet the separator you have "
       "finished one piece. Letting `i` reach `n` is the trick that flushes the last piece out:"),
 ("code", """string line = "apple,,pear,fig";
int n = line.size();
string part = "";

for (int i = 0; i <= n; i++) {
    if (i == n || line[i] == ',') {
        cout << "[" << part << "]\\n";     // [apple] [] [pear] [fig]
        part = "";
    } else {
        part += line[i];
    }
}"""),
 ("p", "Change the `','` to `' '` and the same loop splits a sentence into words. To collect the "
       "pieces instead of printing them, declare `vector<string> v;` above the loop and swap the "
       "`cout` line for `v.push_back(part);`."),
 ("p", "Some problems end the input with a marker character instead of telling you how much there "
       "is. Read one character at a time until it turns up:"),
 ("code", """string text = "";
char c;
while (cin.get(c) && c != '#') text += c;"""),
]),

# ---------------------------------------------------------------- 10
("freq", "10. Counting letters", [
 ("p", "More string problems are solved by counting characters than by any other method, and the "
       "counting is always the same three lines. Make an array with one box per letter, walk the "
       "string, add one to the right box. `c - 'a'` turns the letter into the box number, which is "
       "the trick from section 3 doing real work."),
 ("code", """string s;
cin >> s;

int cnt[26] = {0};                  // small latin letters only
for (char c : s) cnt[c - 'a']++;

cout << cnt['e' - 'a'];             // how many 'e' there were

// which letter is the commonest? ties go to the earlier letter
int best = 0;
for (int i = 1; i < 26; i++)
    if (cnt[i] > cnt[best]) best = i;
cout << char('a' + best) << '\\n';"""),
 ("note", "`cnt[c - 'a']` is only correct while every character really is a small letter. If "
          "capitals, digits or punctuation can turn up, use `int cnt[256] = {0};` with "
          "`cnt[(unsigned char)c]++` - one box per possible character, and nothing can fall "
          "outside the array."),
 ("p", "Two strings are anagrams when their counts match. Counting beats sorting here, because it "
       "needs only one pass over each word:"),
 ("code", """bool anagram(string a, string b) {
    if (a.size() != b.size()) return false;

    int cnt[26] = {0};
    for (char c : a) cnt[c - 'a']++;
    for (char c : b) {
        cnt[c - 'a']--;
        if (cnt[c - 'a'] < 0) return false;   // b has a letter that a did not
    }
    return true;
}"""),
 ("p", "One fact about counts solves a surprising number of contest problems on its own. **The "
       "letters of a string can be rearranged into a palindrome exactly when at most one letter "
       "appears an odd number of times.** Everything else has to pair up around the middle:"),
 ("code", """bool can_be_rearranged_to_palindrome(string s) {
    int cnt[26] = {0};
    for (char c : s) cnt[c - 'a']++;

    int odd = 0;
    for (int i = 0; i < 26; i++)
        if (cnt[i] % 2 == 1) odd++;

    return odd <= 1;
}"""),
]),

# ---------------------------------------------------------------- 11
("patterns", "11. Patterns that keep coming back", [
 ("h3", "Runs of equal characters"),
 ("p", "A run is a block of identical characters sitting next to each other: `\"aaabbc\"` is three "
       "runs. Push `j` forward while the character stays the same, then jump `i` straight to `j`, so "
       "that every character is looked at once. This is the backbone of run-length encoding and of "
       "nearly every \"longest streak\" question:"),
 ("code", """string s = "aaabbc";
int n = s.size();

for (int i = 0; i < n; ) {
    int j = i;
    while (j < n && s[j] == s[i]) j++;
    int len = j - i;                 // s[i..j-1] is one run, len characters long
    cout << len << s[i];             // prints 3a2b1c
    i = j;                           // carry on from the end of the run
}"""),
 ("h3", "Sliding window"),
 ("p", "For questions shaped like \"the longest piece of the string such that ...\". Two indexes "
       "mark the ends of a window. The right end steps forward one character at a time; the left end "
       "moves forward too, jumping ahead whenever the window stops being allowed. Neither index ever "
       "goes back, so the whole scan is one pass:"),
 ("code", """// the longest piece with no repeated character
string s;  cin >> s;
int n = s.size();

int last[256];                            // last[c] = where c was last seen
for (int i = 0; i < 256; i++) last[i] = -1;

int best = 0, left = 0;
for (int r = 0; r < n; r++) {
    unsigned char c = s[r];               // one box per possible character
    if (last[c] >= left) left = last[c] + 1;      // jump past the earlier copy
    last[c] = r;
    if (r - left + 1 > best) best = r - left + 1;
}
cout << best << '\\n';"""),
 ("h3", "Prefix sums over characters"),
 ("p", "When a problem asks the same counting question about many different pieces of one string, "
       "count once from the start instead. `pre[i]` holds the number of matches among the first `i` "
       "characters, and any range then costs one subtraction rather than a loop:"),
 ("code", """string s;  cin >> s;
int n = s.size();

vector<int> pre(n + 1, 0);
for (int i = 0; i < n; i++)
    pre[i + 1] = pre[i] + (s[i] == 'a' ? 1 : 0);

// how many 'a' between positions i and j, both included
int answer = pre[j + 1] - pre[i];"""),
 ("h3", "Rotations"),
 ("p", "Rotating `\"abcd\"` by one gives `\"bcda\"`: the front moves to the back. Cutting and "
       "re-gluing is all it takes. And the doubling trick is worth remembering - every rotation of "
       "`s` is hiding somewhere inside `s + s`:"),
 ("code", """string s = "abcd";
int k = 1;
string rot = s.substr(k) + s.substr(0, k);     // "bcda"

// is t a rotation of s?
bool is_rotation = (s.size() == t.size()) &&
                   ((s + s).find(t) != string::npos);"""),
]),

]

# ---------------------------------------------------------------- 12
CHEATSHEET = [
 ("Length / emptiness", "`s.size()`, `s.empty()`"),
 ("Reach a character", "`s[i]`, `s.front()`, `s.back()`"),
 ("Add to the end", "`s += t`, `s.push_back(c)`"),
 ("Remove", "`s.pop_back()`, `s.erase(pos, len)`, `s.clear()`"),
 ("Take a piece", "`s.substr(pos, len)` - the second number is a LENGTH"),
 ("Insert / replace", "`s.insert(pos, t)`, `s.replace(pos, len, t)`"),
 ("Find first / last", "`s.find(t)`, `s.rfind(t)` - compare the answer to `string::npos`"),
 ("Find any of a set", "`s.find_first_of(set)`, `s.find_last_of(set)`"),
 ("Find none of a set", "`s.find_first_not_of(set)`, `s.find_last_not_of(set)`"),
 ("Starts with `p`", "`s.substr(0, p.size()) == p`"),
 ("Trim the ends", "`s.find_first_not_of(\" \\t\")` + `s.find_last_not_of(\" \\t\")`"),
 ("Compare", "`a == b`, `a < b` (dictionary order)"),
 ("Text to number", "`stoi(s)`, `stoll(s)` - or `v = v * 10 + (c - '0')` by hand"),
 ("Number to text", "`to_string(x)`"),
 ("Digit <-> character", "`c - '0'`, `char('0' + d)`; letter index `c - 'a'`"),
 ("Classify a character", "`isalpha`, `isdigit`, `isalnum`, `isspace`, `isupper`, `islower`"),
 ("Change case", "`toupper(c)`, `tolower(c)`"),
 ("Sort / reverse", "`sort(s.begin(), s.end())`, `reverse(s.begin(), s.end())`"),
 ("Count one character", "`count(s.begin(), s.end(), c)`"),
 ("Remove repeats", "`sort(...)` then `s.erase(unique(s.begin(), s.end()), s.end())`"),
 ("Delete a character everywhere", "`s.erase(remove(s.begin(), s.end(), c), s.end())`"),
 ("Every rearrangement", "`sort(...)` then `while (next_permutation(s.begin(), s.end()))`"),
 ("Backwards copy", "`string r(s.rbegin(), s.rend())`"),
 ("Palindrome test", "two indexes, `i` from the left and `j` from the right"),
 ("Can be rearranged into a palindrome", "at most one letter has an odd count"),
 ("Anagram test", "sorted forms equal, or equal `cnt[26]` arrays"),
 ("Count the letters", "`int cnt[26] = {0}; for (char c : s) cnt[c - 'a']++;`"),
 ("Read a word / a line", "`cin >> s` / `getline(cin, s)`"),
 ("After `>>`, before `getline`", "`cin.ignore();`"),
 ("Split a line", "walk it, collect into `part`, flush `part` at every separator"),
 ("Fast input", "`ios_base::sync_with_stdio(false); cin.tie(nullptr);`"),
 ("Rotation test", "`(s + s).find(t) != string::npos`"),
]

# ---------------------------------------------------------------- 13
PITFALLS = [
 ("The second argument of `substr` is a length, not an end position.",
  "`s.substr(2, 5)` gives you five characters starting at position 2, not the characters from 2 to 5."),
 ("`s.size()` is unsigned.",
  "On an empty string `s.size() - 1` is not -1, it is a gigantic number, and the loop runs almost "
  "for ever. Write `int n = s.size();` before the loop and compare against `n`."),
 ("Compare the result of `find` against `string::npos`, not against -1.",
  "`if (s.find(t) != string::npos)`. Storing the result in an `int` first breaks the same test."),
 ("`getline` straight after `cin >> x` hands you an empty line.",
  "The newline from the earlier read is still waiting. Put `cin.ignore();` between the two."),
 ("`s = s + x` inside a loop is far slower than `s += x`.",
  "The first form copies the entire string on every single iteration. On a long input that alone "
  "will exceed the time limit."),
 ("`unique` only removes neighbouring repeats.",
  "Sort the string first, and remember that `unique` does not shorten anything by itself - it needs "
  "the `erase` around it."),
 ("`next_permutation` must start from a sorted string.",
  "Starting anywhere else gives you only the rearrangements that come after that one in dictionary "
  "order, so you silently lose part of the answer."),
 ("Dictionary order is not alphabetical order once capitals are mixed in.",
  "`'Z'` is 90 and `'a'` is 97, so `\"Zoo\" < \"apple\"`. Make the case uniform before sorting words."),
 ("Erasing inside a loop over positions skips characters.",
  "Every erase shifts the rest of the string to the left, so the next character slides in under your "
  "index and is never looked at. Build a new string instead, or walk backwards."),
 ("`stoi` fails loudly on a number that is too big and quietly on trailing rubbish.",
  "`stoi(\"9000000000\")` stops the program; `stoi(\"12abc\")` is 12 with no warning at all. Use "
  "`stoll` when the number may be long."),
 ("`endl` empties the output buffer, `'\\n'` does not.",
  "Use `'\\n'`. One flush per line over 100000 lines is a measurable slowdown."),
]

# ---------------------------------------------------------------- 14
COMPLEXITY = [
 ["`s[i]`, `at`, `front`, `back`, `size`, `empty`", "O(1)"],
 ["`push_back`, `pop_back`, `+=` one character", "O(1)"],
 ["`s += t`", "O(length of `t`)"],
 ["`insert`, `erase`, `replace` in the middle", "O(n)"],
 ["`substr(pos, len)`", "O(len) - it makes a copy"],
 ["`find` / `rfind` of a pattern `p`", "about O(n * length of `p`)"],
 ["`==`, `<`", "O(n)"],
 ["`sort(s.begin(), s.end())`", "O(n log n)"],
 ["`reverse`, `count`", "O(n)"],
 ["`unique` after a sort", "O(n)"],
 ["`next_permutation` (one step)", "O(1) on average"],
 ["`stoi`, `to_string`", "O(number of digits)"],
 ["Counting the letters into `cnt[26]`", "O(n)"],
 ["Scanning runs, or a sliding window", "O(n) - every position is visited at most twice"],
]

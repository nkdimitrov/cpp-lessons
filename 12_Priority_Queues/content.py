# -*- coding: utf-8 -*-
"""Lesson 12 - Priority queues. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "12_Priority_Queues"
BRAND = "Lesson 12 · Priority queues"
FOOTER = ("Lesson 12 · C++17 priority_queue. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Priority queues - always the best one first"
SUBTITLE = ("Lesson 12 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("pq", "1. The largest is always on top", [
 ("p", "A `priority_queue` is a box you can throw numbers into in any order. Whenever you look, "
       "the **largest** one is on top. It is also called a **heap**. Add `#include <queue>`:"),
 ("code", """priority_queue<int> pq;
pq.push(5);
pq.push(1);
pq.push(8);
pq.push(3);

cout << pq.top() << '\\n';        // 8
pq.pop();                        // 8 is gone
cout << pq.top() << '\\n';        // 5"""),
 ("p", "The calls are the same as for a stack: `push`, `top`, `pop`, `empty`, `size`. Only the "
       "order is different: not the newest, but the largest."),
 ("p", "Pop everything and the numbers come out from the largest to the smallest:"),
 ("code", """while (!pq.empty()) {
    cout << pq.top() << ' ';     // 5 3 1
    pq.pop();
}"""),
]),

# ---------------------------------------------------------------- 2
("min", "2. The smallest first", [
 ("p", "To get the **smallest** on top, write the type like this. Learn it as one phrase:"),
 ("code", """priority_queue<int, vector<int>, greater<int>> pq;
pq.push(5);
pq.push(1);
pq.push(8);
cout << pq.top() << '\\n';        // 1"""),
 ("p", "A trick that does the same job: push `-x` into an ordinary priority queue, and remember "
       "to turn the sign back when you take it out."),
 ("p", "The classic job for a smallest-first queue: **keep joining the two smallest**. Piles of "
       "sand are joined two at a time, and each join costs the sum of the two piles. The cheapest "
       "way is to always join the two smallest piles - and the new pile goes back in:"),
 ("code", """priority_queue<long long, vector<long long>, greater<long long>> pq;
// ... push every pile ...
long long cost = 0;
while (pq.size() > 1) {
    long long a = pq.top(); pq.pop();
    long long b = pq.top(); pq.pop();
    cost += a + b;
    pq.push(a + b);              // the new pile joins the others
}"""),
]),

# ---------------------------------------------------------------- 3
("pairs", "3. Pairs in the queue", [
 ("p", "A priority queue of pairs compares them like `sort` does: by `first`, then by `second`. "
       "Put the thing that decides the order in `first`, and a number that says **who** it is in "
       "`second`:"),
 ("code", """priority_queue<pair<int, int>> pq;     // (score, player)
pq.push({70, 1});
pq.push({95, 2});
pq.push({95, 3});
cout << pq.top().second << '\\n';         // 3 - on equal scores, the larger second wins"""),
 ("p", "With `greater<pair<int, int>>` the smallest pair is on top. That is perfect for "
       "**time**: the earliest event comes out first."),
 ("p", "Example: people come into a room and leave later. How many are inside at most? Go through "
       "them in order of arrival. Keep the leaving times in a smallest-first queue; before each "
       "arrival, let out everybody who has already left:"),
 ("code", """// in[i], out[i]: arrival and leaving time, already sorted by arrival
priority_queue<int, vector<int>, greater<int>> leaving;
int most = 0;
for (int i = 0; i < n; i++) {
    while (!leaving.empty() && leaving.top() <= in[i]) leaving.pop();
    leaving.push(out[i]);
    if ((int)leaving.size() > most) most = leaving.size();
}"""),
]),

# ---------------------------------------------------------------- 4
("when", "4. Priority queue or sort?", [
 ("table", ["The situation", "Use"], [
   ["All the numbers are known at the start, and you need them all in order", "`sort` - simpler"],
   ["New numbers keep arriving while you keep taking out the best one", "a priority queue"],
   ["You only need the best one, once", "a single loop with `max`"],
 ]),
 ("p", "A priority queue can only show you the top. You cannot look at the second one without "
       "popping the first, and you cannot search inside it."),
]),

]

CHEATSHEET = [
 ("Largest on top", "`priority_queue<int> pq;` (`#include <queue>`)"),
 ("Smallest on top", "`priority_queue<int, vector<int>, greater<int>> pq;`"),
 ("Add / look / remove", "`pq.push(x)`, `pq.top()`, `pq.pop()`"),
 ("Is it empty? How many?", "`pq.empty()`, `pq.size()`"),
 ("Smallest first without `greater`", "push `-x`, read `-pq.top()`"),
 ("Pairs", "`priority_queue<pair<int, int>>` - by `first`, then `second`"),
 ("Earliest event first", "`priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>`"),
 ("Join the two smallest", "pop two, push their sum, repeat while `size() > 1`"),
]

PITFALLS = [
 ("Expecting the smallest on top.",
  "A plain `priority_queue<int>` gives the **largest**. For the smallest, add `greater<int>` or "
  "push negative numbers."),
 ("`top()` or `pop()` on an empty queue.",
  "The program crashes. Check `!pq.empty()` first."),
 ("`pop()` gives nothing back.",
  "Read `top()`, then `pop()`."),
 ("Overflow when adding.",
  "Joined piles get big quickly. Use `long long` for sums."),
 ("Looking for a value inside.",
  "A priority queue shows only its top. If you need to find or remove any value, use a `set` "
  "(lesson 11)."),
]

COMPLEXITY = [
 ["`top()`, `empty()`, `size()`", "O(1)"],
 ["`push(x)`, `pop()` with `n` values inside", "O(log n)"],
 ["Putting in `n` values and taking them all out", "O(n log n) - the same as sorting"],
]

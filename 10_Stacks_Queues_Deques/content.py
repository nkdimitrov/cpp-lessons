# -*- coding: utf-8 -*-
"""Lesson 10 - Stacks, queues and deques. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "10_Stacks_Queues_Deques"
BRAND = "Lesson 10 · Stacks and queues"
FOOTER = ("Lesson 10 · C++17 stack, queue and deque. Problem links point to arena.olimpiici.com; "
          "statements are in Bulgarian and downloadable as PDF from each problem page.")

TITLE = "C++17 Stacks, queues and deques - piles and lines"
SUBTITLE = ("Lesson 10 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("stack", "1. stack: a pile of plates", [
 ("p", "A stack is like a pile of plates. You put a plate on **top**, and you can take only the "
       "plate on top. The last one in is the first one out. Add `#include <stack>`:"),
 ("code", """stack<int> st;
st.push(1);
st.push(2);
st.push(3);                      // 3 is on top

cout << st.top() << '\\n';        // 3
st.pop();                        // throws 3 away
cout << st.top() << '\\n';        // 2
cout << st.size() << '\\n';       // 2"""),
 ("table", ["Call", "Does"], [
   ["`st.push(x)`", "puts `x` on top"],
   ["`st.top()`", "the value on top (it stays there)"],
   ["`st.pop()`", "removes the top - and gives nothing back"],
   ["`st.empty()`", "true when the stack has nothing in it"],
 ]),
 ("p", "A stack turns things round. Push everything, then pop everything, and it comes out "
       "backwards:"),
 ("code", """while (!st.empty()) {
    cout << st.top() << ' ';
    st.pop();
}"""),
 ("note", "`top()` or `pop()` on an empty stack crashes the program. Check `!st.empty()` first."),
]),

# ---------------------------------------------------------------- 2
("queue", "2. queue: a line at the shop", [
 ("p", "A queue is a line of people. New people join at the **back**; the person at the "
       "**front** is served and leaves. The first one in is the first one out. Add "
       "`#include <queue>`:"),
 ("code", """queue<int> q;
q.push(1);
q.push(2);
q.push(3);                       // front: 1   back: 3

cout << q.front() << '\\n';       // 1
q.pop();                         // 1 leaves
cout << q.front() << '\\n';       // 2"""),
 ("p", "A pack of cards where the top card goes to the bottom is a queue. So is a circle of "
       "children where every k-th one leaves the game:"),
 ("code", """queue<int> q;
for (int i = 1; i <= n; i++) q.push(i);
while (q.size() > 1) {
    for (int s = 1; s < k; s++) {      // k - 1 children move to the back
        q.push(q.front());
        q.pop();
    }
    q.pop();                           // the k-th child leaves
}
cout << q.front() << '\\n';             // the last one left"""),
]),

# ---------------------------------------------------------------- 3
("deque", "3. deque: a line with two ends", [
 ("p", "A `deque` (say \"deck\") lets you add and remove at **both** ends. Add "
       "`#include <deque>`:"),
 ("code", """deque<int> d;
d.push_back(2);
d.push_back(3);
d.push_front(1);                 // 1 2 3

cout << d.front() << ' ' << d.back() << '\\n';   // 1 3
d.pop_front();                   // 2 3
d.pop_back();                    // 2
cout << d[0] << '\\n';            // 2 - you may also use places, like a vector"""),
 ("p", "When a problem keeps taking from one end and adding to the other end - or turns the whole "
       "line round - a deque does each step at once, without moving the other elements."),
]),

# ---------------------------------------------------------------- 4
("brackets", "4. Brackets", [
 ("p", "Is `([]{})` correctly closed? Read the characters one by one. Push every opening bracket. "
       "A closing bracket must match the bracket on top of the stack - then pop it. At the end "
       "the stack must be empty:"),
 ("code", """bool ok(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') st.push(c);
        else {
            if (st.empty()) return false;          // nothing to close
            char o = st.top();
            st.pop();
            if (c == ')' && o != '(') return false;
            if (c == ']' && o != '[') return false;
            if (c == '}' && o != '{') return false;
        }
    }
    return st.empty();                             // nothing left open
}"""),
 ("p", "The size of the stack at any moment is how **deep** you are inside the brackets."),
]),

# ---------------------------------------------------------------- 5
("keep", "5. A stack that keeps only what matters", [
 ("p", "Sometimes, when a new value arrives, the smaller values before it can never be useful "
       "again. Pop them! For example: for every number, find the nearest **bigger** number to its "
       "left."),
 ("code", """stack<int> st;                   // only numbers that may still be an answer
for (int i = 0; i < n; i++) {
    while (!st.empty() && st.top() <= a[i]) st.pop();   // too small: never an answer again
    if (st.empty()) cout << -1 << ' ';
    else cout << st.top() << ' ';
    st.push(a[i]);
}"""),
 ("p", "For `5 3 1 4 6` this prints `-1 5 3 5 -1`. Every number is pushed once and popped at most "
       "once, so the whole loop is fast even though there is a `while` inside."),
]),

]

CHEATSHEET = [
 ("Stack: add, look, remove", "`st.push(x)`, `st.top()`, `st.pop()`"),
 ("Queue: add at the back, look at the front, remove", "`q.push(x)`, `q.front()`, `q.pop()`"),
 ("Deque: both ends", "`push_front`, `push_back`, `pop_front`, `pop_back`, `front`, `back`"),
 ("Is it empty? How many?", "`.empty()`, `.size()`"),
 ("Empty it", "`while (!st.empty()) st.pop();`"),
 ("Print a stack top first", "`while (!st.empty()) { cout << st.top(); st.pop(); }`"),
 ("Move the front to the back", "`q.push(q.front()); q.pop();`"),
 ("Brackets", "push openers; a closer must match `top()`; empty at the end"),
 ("Nearest bigger to the left", "pop while `top() <= a[i]`, then `top()` is the answer"),
]

PITFALLS = [
 ("`top()`, `front()` or `pop()` on an empty container.",
  "The program crashes. Always check `.empty()` first."),
 ("`pop()` gives nothing back.",
  "`int x = st.pop();` does not compile. Read `top()` first, then `pop()`."),
 ("Using `top()` on a queue.",
  "A queue has `front()` (and `back()`). Only a stack has `top()`."),
 ("Forgetting the last check for brackets.",
  "`((` never meets a wrong closer, but it is not balanced. The stack must be empty at the end."),
 ("Old values left from the previous test.",
  "A stack or queue keeps its contents. Empty it, or make a new one, before each test."),
]

COMPLEXITY = [
 ["`push`, `pop`, `top`, `front`, `back`, `empty`, `size`", "O(1)"],
 ["`push_front`, `pop_front` on a deque", "O(1)"],
 ["Checking a bracket string of length `n`", "O(n)"],
 ["The keep-only-what-matters loop", "O(n) - each value is pushed once and popped once"],
]

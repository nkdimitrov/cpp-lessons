# -*- coding: utf-8 -*-
"""Lesson 07 - Grids and matrices. Rendered to HTML + DOCX by tools/render_lesson.py."""

SLUG  = "07_Grids_And_Matrices"
BRAND = "Lesson 07 · Grids"
FOOTER = ("Lesson 07 · C++17 two-dimensional arrays. Problem links point to "
          "arena.olimpiici.com; statements are in Bulgarian and downloadable as PDF from each "
          "problem page.")

TITLE = "C++17 Grids - tables of rows and columns"
SUBTITLE = ("Lesson 07 | Theory, cheat sheet and 12 practice problems "
            "from arena.olimpiici.com (Group D)")

SECTIONS = [

# ---------------------------------------------------------------- 1
("table", "1. A table of numbers", [
 ("p", "A two-dimensional array is a table. `a[i][j]` is the box in **row** `i` and **column** "
       "`j`. Both start at 0:"),
 ("code", """int a[105][105];             // outside main: up to 105 rows and 105 columns

int n, m;                    // n rows, m columns
cin >> n >> m;
for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
        cin >> a[i][j];"""),
 ("p", "Printing it row by row: the inner loop prints one row, then a new line ends it."),
 ("code", """for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) cout << a[i][j] << ' ';
    cout << '\\n';
}"""),
 ("note", "Always the row first, then the column: `a[row][column]`. Mixing them up is the most "
          "common grid bug."),
]),

# ---------------------------------------------------------------- 2
("rows", "2. Rows and columns", [
 ("p", "To go along one row, keep `i` fixed and move `j`. To go down one column, keep `j` fixed "
       "and move `i`:"),
 ("code", """// the sum of every row
for (int i = 0; i < n; i++) {
    int s = 0;
    for (int j = 0; j < m; j++) s += a[i][j];
    cout << s << '\\n';
}

// the largest number in every column
for (int j = 0; j < m; j++) {
    int mx = a[0][j];
    for (int i = 1; i < n; i++)
        if (a[i][j] > mx) mx = a[i][j];
    cout << mx << '\\n';
}"""),
 ("p", "\"Is this row completely full?\" is the same loop with a `bool` that turns `false` as soon "
       "as one empty box is found."),
]),

# ---------------------------------------------------------------- 3
("chars", "3. Grids of characters", [
 ("p", "Many grids are pictures made of characters such as `.` and `#`. Read each row as one "
       "string; then `g[i][j]` is the character in row `i`, column `j`:"),
 ("code", """string g[105];                   // outside main, together with n and m,
int n, m;                        // so that functions can use them too

// inside main:
cin >> n >> m;
for (int i = 0; i < n; i++) cin >> g[i];      // input:  .#..
                                              //         ##.#
int walls = 0;
for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
        if (g[i][j] == '#') walls++;"""),
]),

# ---------------------------------------------------------------- 4
("neigh", "4. Neighbours", [
 ("p", "The four neighbours of a box are up, down, left and right. Instead of writing four `if`s, "
       "keep the four steps in two small arrays and loop over them:"),
 ("code", """int dr[4] = {-1, 1, 0, 0};       // row step:    up, down, left, right
int dc[4] = {0, 0, -1, 1};       // column step

int count_walls(int r, int c) {
    int k = 0;
    for (int d = 0; d < 4; d++) {
        int nr = r + dr[d], nc = c + dc[d];
        if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;   // outside the grid
        if (g[nr][nc] == '#') k++;
    }
    return k;
}"""),
 ("p", "The check for \"outside the grid\" must come **before** you look at `g[nr][nc]`. For eight "
       "neighbours (with the corners), use eight steps: every pair of `-1`, `0`, `1` except "
       "`0, 0`."),
]),

# ---------------------------------------------------------------- 5
("walk", "5. Walking round the grid", [
 ("p", "**Snake order.** Row 0 goes left to right, row 1 right to left, and so on. Check whether "
       "the row number is even:"),
 ("code", """for (int i = 0; i < n; i++) {
    if (i % 2 == 0) for (int j = 0; j < m; j++)      cout << a[i][j] << ' ';
    else            for (int j = m - 1; j >= 0; j--) cout << a[i][j] << ' ';
}"""),
 ("p", "**Spiral.** Walk with a direction number `d` and the step arrays. When the next box is "
       "outside the grid or already filled, turn right: `d = (d + 1) % 4`. Use the order right, "
       "down, left, up:"),
 ("code", """int dr[4] = {0, 1, 0, -1}, dc[4] = {1, 0, -1, 0};    // right, down, left, up
int r = 0, c = 0, d = 0;
for (int k = 1; k <= n * n; k++) {
    a[r][c] = k;
    int nr = r + dr[d], nc = c + dc[d];
    if (nr < 0 || nr >= n || nc < 0 || nc >= n || a[nr][nc] != 0) {
        d = (d + 1) % 4;                             // turn right
        nr = r + dr[d];
        nc = c + dc[d];
    }
    r = nr;
    c = nc;
}"""),
 ("p", "**Turning by 90 degrees** to the right: the box in row `i`, column `j` moves to row `j`, "
       "column `n - 1 - i`. Write the result into a second array `b[j][n - 1 - i] = a[i][j];`."),
]),

# ---------------------------------------------------------------- 6
("lines", "6. Lines through the grid", [
 ("p", "In a square `n x n` grid, the two long diagonals are easy to spot by their numbers:"),
 ("table", ["Line", "Boxes where"], [
   ["main diagonal, top left to bottom right", "`i == j`"],
   ["other diagonal, top right to bottom left", "`i + j == n - 1`"],
   ["any diagonal parallel to the main one", "`i - j` is the same"],
   ["any diagonal parallel to the other one", "`i + j` is the same"],
 ]),
 ("p", "A **run** along a row is a block of equal or free boxes side by side - the same idea as "
       "runs in a string (lesson 03). Count the current run, and start again when it breaks:"),
 ("code", """int best = 0;
for (int i = 0; i < n; i++) {
    int run = 0;
    for (int j = 0; j < m; j++) {
        if (g[i][j] == '.') run++;
        else run = 0;
        if (run > best) best = run;
    }
}"""),
 ("p", "For columns, swap the two loops: `j` outside, `i` inside."),
]),

]

CHEATSHEET = [
 ("Make a grid", "`int a[105][105];` outside `main`"),
 ("Read a number grid", "two loops: `i` over rows, `j` over columns, `cin >> a[i][j]`"),
 ("Read a picture", "`string g[105];` and `cin >> g[i];` for each row"),
 ("Along row `i` / down column `j`", "fix `i`, move `j` / fix `j`, move `i`"),
 ("Four neighbours", "`dr = {-1, 1, 0, 0}`, `dc = {0, 0, -1, 1}`"),
 ("Inside the grid?", "`nr >= 0 && nr < n && nc >= 0 && nc < m`"),
 ("Turn right in a spiral", "`d = (d + 1) % 4` with right, down, left, up"),
 ("Turn the grid 90 degrees right", "`b[j][n - 1 - i] = a[i][j];`"),
 ("Main / other diagonal", "`i == j` / `i + j == n - 1`"),
 ("Longest run in a row", "`run++` while it holds, `run = 0` when it breaks"),
]

PITFALLS = [
 ("Row and column swapped.",
  "`a[j][i]` instead of `a[i][j]` works on square grids and fails on the others. Always the row "
  "first."),
 ("Looking at a neighbour before checking it is inside.",
  "`g[-1][c]` is outside the grid. Test the bounds first, then look."),
 ("`n` and `m` mixed up.",
  "Rows go up to `n`, columns up to `m`. Read the statement twice: which number comes first?"),
 ("Turning the grid inside the same array.",
  "Writing the turned grid into `a` while you still read from `a` destroys boxes you need. Use a "
  "second array."),
 ("A big grid inside `main`.",
  "`int a[1000][1000];` is a million boxes. Put it outside `main`."),
]

COMPLEXITY = [
 ["`a[i][j]` - one box", "O(1)"],
 ["Reading or walking the whole grid", "O(n * m)"],
 ["Checking the four neighbours of one box", "O(1)"],
 ["Every row sum and every column sum", "O(n * m)"],
]

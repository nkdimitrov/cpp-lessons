# C++17 for Competitive Programming

A structured course built on the classified Olimpiici Arena catalogue (Groups C and D, 2007-2026)

Generated from `syllabus.json` by `tools/build_site.py` - edit the JSON, not this file.

- Site hub: [index.html](index.html)
- Problem catalogue: [Problem catalogue](Group C and D problems/index.html) - 768 problems, each tagged with a primary algorithm, an optional secondary algorithm, technique tags, a 1-5 difficulty and a one-line hint.

## Part I - Language and data structures

The C++17 you actually type in a contest. Every lesson is self-contained, follows the shape of Lesson 03, and ends with graded problems drawn from the catalogue.

| # | Lesson | Status | Candidate problems | Catalogue filter |
|---|--------|--------|--------------------|------------------|
| 01 | Setup, I/O and the contest toolkit | **written** | 12 assigned | `I/O parsing · level 1-3` |
| 02 | Primitive types: integers, characters, booleans, floating point | **written** | 24 assigned | `Long long · level 1-3` |
| 03 | Strings | **written** | 24 assigned | `String processing · Group D` |
| 04 | Arrays - fixed storage and the loop patterns | **written** | 24 assigned | `Arrays · level 1-3` |
| 05 | std::vector - dynamic arrays | **written** | 24 assigned | `Vectors · level 2-4` |
| 06 | Counting and frequency arrays | planned | 102 | `Counting / Frequency arrays · level 2-4` |
| 07 | Two-dimensional arrays, grids and matrices | planned | 93 | `2D arrays · level 2-4` |
| 08 | Sorting and custom comparators | planned | 67 | `Sorting · level 2-4` |
| 09 | Pairs, structs and tuples | planned | 26 | `Pairs / Structs · level 2-4` |
| 10 | Stacks, queues and deques | planned | 45 | `Stacks / Queues / Deque · level 2-4` |
| 11 | Sets and maps, ordered and unordered | planned | 32 | `Maps / Sets · level 2-4` |
| 12 | Priority queues and heaps | planned | 14 | `Priority queue · level 3-5` |
| 13 | Iterators and the <algorithm> toolbox | planned | 20 | `Vectors · level 2-3` |
| 14 | Big integers - arithmetic beyond long long | planned | 40 | `Big numbers · level 2-5` |
| 15 | Recursion and the call stack | planned | 30 | `Recursion · level 2-4` |
| 16 | Complexity, memory limits and choosing a container | planned | 15 | `Memory optimization · level 3-5` |

### 01. Setup, I/O and the contest toolkit

The skeleton of a solution: headers, fast I/O, reading until EOF, whitespace vs lines, file I/O, formatted output, and how to compile and test locally.

- the five-line skeleton every solution starts from
- compiling with g++ -std=c++17 -O2 -Wall, and reading the warnings
- cin >> skips whitespace, so the input layout never matters
- a count then that many values; answering while reading, storing nothing
- reading until EOF, T test cases, and stopping at a marker value
- printing: separators, and why endl fails time limits
- ios_base::sync_with_stdio / cin.tie, and the rules that come with them
- cin >> char, reading `12+7` and `21.05.2015` with `cin >>` alone
- getline and the cin.ignore() trap
- what to test before submitting, and what each judge verdict means

### 02. Primitive types: integers, characters, booleans, floating point

What fits in what, when it silently breaks, and the arithmetic rules that decide half the wrong answers in Group C and D.

- int / long long / unsigned and their ranges
- overflow: where it happens and how to see it coming
- `int * int` is an `int` - casting the operand, not the answer
- integer division and truncation toward zero
- the sign of % for negative operands, and `(i - 1 + n) % n`
- taking a number apart with / and %; rounding up as `(a + b - 1) / b`
- char as a small integer, ASCII arithmetic, <cctype>
- bool, short-circuit evaluation, the classic `=` vs `==`
- double: why `7 / 2` is 3, fixed/setprecision, the <cmath> tools
- epsilon comparison, and staying with whole numbers instead
- sqrt and pow are inexact - checking the result with integers
- implicit conversions, the int/unsigned trap, INT_MAX and LLONG_MAX

### 03. Strings

std::string for beginners: characters as numbers, search, modification, conversion, frequency counting, and the patterns that keep reappearing.

- construction, size, element access
- characters as ASCII numbers, <cctype> classification
- find / rfind / substr / replace / erase / insert
- comparison and dictionary order
- stoi / stoll / to_string, conversion by hand, other bases
- <algorithm> on strings: sort, reverse, unique, next_permutation
- cin >> / getline, the newline trap, splitting a line by hand
- frequency arrays over characters, anagrams, palindromes
- runs, sliding window, prefix sums, rotations

### 04. Arrays - fixed storage and the loop patterns

The raw C array is still the fastest thing in the language and the most common source of a zero. Declaration, bounds, global vs local, and the scan patterns every problem reuses.

- declaration, initialisation, `{}` and fill
- global arrays vs stack arrays and why size limits differ
- off-by-one and out-of-bounds: what actually happens
- the six standard scans: sum, max, min, count, index-of, contains
- keeping a running answer in a single pass; runs and streaks
- neighbouring pairs, local maxima and windows of fixed width
- wrapping round a circle with `%`
- parallel arrays, and using a value as an index
- shifting, rotating, deleting, in-place reversal
- passing arrays to functions (decay to pointer)
- sentinel values and 1-based indexing

### 05. std::vector - dynamic arrays

When the size is not known until runtime. Growth, cost, the copy traps, and the vector idioms that replace a page of manual array code.

- why a fixed-size array is not always enough
- construction: `v`, `v(n)`, `v(n, x)`, `{...}`; resize and clear
- push_back / pop_back / back, and reading a list of unknown length
- iteration: index, range-for, range-for by reference
- passing by value vs const reference (the classic TLE)
- building a new vector instead of erasing in a loop
- sort, reverse, count, max_element on `v.begin(), v.end()`
- sorting by your own rule with a comparison function
- sort + unique + erase for distinct values
- insert / erase in the middle and their O(n) cost
- vector<vector<int>>: one list per group, and a run-time sized table
- when a plain global array is still the better choice

### 06. Counting and frequency arrays

The single highest-yield technique in Groups C and D: turn a loop over values into an index into an array.

- the count[] pattern and choosing its size
- counting sort in O(n + k)
- histograms and mode
- presence arrays vs counting arrays
- offsetting negative keys
- counting pairs without enumerating pairs
- when a map beats an array (sparse or huge key space)
- frequency over characters, digits, remainders
- difference between counting and marking (visited[])

### 07. Two-dimensional arrays, grids and matrices

Rows, columns, diagonals and neighbours. The indexing discipline that makes grid problems routine instead of error-prone.

- declaration of 2D and 3D arrays; memory layout
- row-major traversal and cache behaviour
- the dx/dy direction-array idiom (4- and 8-neighbourhood)
- bounds checking in one helper
- diagonals: i+j and i-j indexing
- transpose, rotate 90, mirror
- border padding to avoid bounds checks
- reading a grid of characters vs a grid of numbers
- 2D prefix sums (preview of Lesson 19)
- matrix multiplication and its cost

### 08. Sorting and custom comparators

std::sort and everything around it - stability, comparators, sorting by more than one key, and the problems that become trivial once sorted.

- sort, stable_sort, partial_sort, nth_element
- comparator functions, lambdas, and the strict-weak-ordering rule
- sorting pairs and structs by several keys
- descending order: greater<> vs reversing the comparator
- sorting indices instead of values
- unique + erase to deduplicate
- lower_bound / upper_bound / equal_range on a sorted array
- counting sort vs comparison sort
- the cost of sorting inside a loop

### 09. Pairs, structs and tuples

Grouping related values so that sorting, comparing and returning them stops being painful.

- std::pair, make_pair, .first / .second
- lexicographic comparison of pairs - and how to exploit it
- structs with named fields; when to prefer them
- operator< on a struct
- std::tuple, tie and structured bindings (C++17)
- returning several values from a function
- vector<pair<int,int>> as the default 'list of events'
- sorting a struct array by a chosen field

### 10. Stacks, queues and deques

Three containers with one rule each, and the problem shapes that announce them.

- std::stack: push, pop, top, empty
- bracket matching and expression evaluation
- the monotonic stack (next greater element, largest rectangle)
- std::queue: push, pop, front - and BFS's data structure
- simulation queues (service, rotation, Josephus)
- std::deque: both-ends insertion
- the monotonic deque and sliding-window minimum
- implementing all three over a raw array when speed matters

### 11. Sets and maps, ordered and unordered

Associative containers: what they cost, what order they give back, and when a plain array beats both.

- set / multiset: insert, erase, count, find
- ordered traversal and lower_bound on a set
- map / multimap: operator[] vs at vs find
- the operator[] insertion trap
- unordered_set / unordered_map and hashing
- when unordered is slower (collisions, reserve, max_load_factor)
- map<string,int> for word frequency
- set as a running 'seen' structure
- choosing between array, set, map and sorted vector

### 12. Priority queues and heaps

Repeatedly taking the best element without re-sorting.

- priority_queue basics: push, top, pop
- min-heap via greater<> or negated keys
- priority_queue of pairs and structs; custom comparators
- heap of a fixed size (k largest)
- make_heap / push_heap / pop_heap on a vector
- scheduling and merging problems
- why it is the right structure for Dijkstra (preview of Lesson 35)
- lazy deletion when elements become stale

### 13. Iterators and the <algorithm> toolbox

The standard library functions that replace hand-written loops, and the iterator vocabulary they all speak.

- iterator basics: begin/end, half-open ranges
- min_element / max_element / minmax_element
- accumulate, count, count_if, find, find_if
- all_of / any_of / none_of
- reverse, rotate, next_permutation
- fill, iota, copy, transform
- lower_bound / upper_bound / binary_search
- unique, remove, remove_if and the erase idiom
- iterator invalidation - the rules that matter

### 14. Big integers - arithmetic beyond long long

When the answer has 200 digits. Representation, the four operations, and how to keep them fast enough.

- deciding that long long is not enough
- representation: digit vector, little-endian, base 10 vs base 10^9
- addition and subtraction with carry/borrow
- multiplication by a small integer, and long multiplication
- division and modulo by a small integer
- comparison and normalisation (leading zeros)
- reading and printing
- factorials, powers and Fibonacci as the classic uses
- when modular arithmetic replaces big integers entirely

### 15. Recursion and the call stack

Writing a function that calls itself, reasoning about it, and knowing what it costs.

- base case and recursive case
- the call stack; what a stack overflow looks like
- recursion vs iteration; converting between them
- recursive array and string processing
- divide and conquer: binary search, merge sort
- recursion with an accumulator vs with a return value
- returning versus printing inside recursion
- exponential recursion and why memoisation exists
- mutual recursion and helper signatures

### 16. Complexity, memory limits and choosing a container

Reading the constraints and deciding, before writing a line, which approach can pass.

- big-O in practice: the 10^8 operations rule of thumb
- mapping n to an allowed complexity
- memory: bytes per element for every container
- the 1 MB and 16 MB limits in older NOI tasks
- time cost of I/O and of endl
- cache behaviour: why a flat array beats a vector of vectors
- amortised vs worst case
- estimating before implementing
- a decision table: which container for which requirement

## Part II - Algorithms and techniques

One technique per lesson, in the order the catalogue rewards. Each assumes Part I and nothing else.

| # | Lesson | Status | Candidate problems | Catalogue filter |
|---|--------|--------|--------------------|------------------|
| 17 | Brute force and complete search | planned | 54 | `Brute force · level 2-4` |
| 18 | Simulation and implementation discipline | planned | 82 | `Implementation / Simulation · level 2-4` |
| 19 | Prefix sums and difference arrays | planned | 71 | `Prefix sums · level 2-5` |
| 20 | Two pointers and sliding window | planned | 45 | `Two pointers · level 2-5` |
| 21 | Binary search, including binary search on the answer | planned | 32 | `Binary search · level 3-5` |
| 22 | Greedy - and how to prove it | planned | 118 | `Greedy · level 2-5` |
| 23 | Sorting-based techniques: sweep line and coordinate compression | planned | 58 | `Sorting · level 3-5` |
| 24 | Number theory I: divisibility, primes and GCD | planned | 128 | `Number theory · level 2-4` |
| 25 | Number theory II: modular arithmetic and fast exponentiation | planned | 30 | `Modular arithmetic · level 3-5` |
| 26 | Combinatorics and counting | planned | 50 | `Combinatorics · level 3-5` |
| 27 | Backtracking and generating combinatorial objects | planned | 17 | `Recursion / Backtracking · level 3-5` |
| 28 | Bitmasks and subset enumeration | planned | 22 | `Bit manipulation · level 3-5` |
| 29 | Dynamic programming I: one dimension | planned | 76 | `Dynamic programming · level 3-4` |
| 30 | Dynamic programming II: two dimensions and grids | planned | 39 | `Dynamic programming · 2D arrays · level 3-5` |
| 31 | Dynamic programming III: interval, digit and bitmask DP | planned | 21 | `Dynamic programming · level 5` |
| 32 | Graphs: representation and traversal | planned | 56 | `Graph traversal · level 3-5` |
| 33 | Flood fill and grid graphs | planned | 64 | `Flood fill / Grid/Matrix · level 2-5` |
| 34 | Shortest paths | planned | 14 | `Shortest path · level 3-5` |
| 35 | Trees | planned | 10 | `Trees · level 3-5` |
| 36 | Disjoint set union (union-find) | planned | 37 | `Data structures · level 4-5` |
| 37 | Fenwick and segment trees | planned | 20 | `Data structures · level 5` |
| 38 | String algorithms: KMP, Z, hashing and tries | planned | 20 | `String processing · level 4-5` |
| 39 | Geometry basics | planned | 13 | `Geometry · level 3-5` |
| 40 | Game theory | planned | 7 | `Game theory · level 3-5` |
| 41 | Ad hoc, constructive problems and invariants | planned | 28 | `Ad hoc · level 3-5` |
| 42 | Contest craft: strategy, testing and debugging | planned | 204 | `level 1-5 · National` |

### 17. Brute force and complete search

Enumerating every candidate - and the arithmetic that tells you whether you are allowed to.

- counting the search space before coding
- nested loops over pairs and triples
- enumerating subsets and permutations
- early exit and pruning
- brute force as a correctness oracle for stress tests
- meet in the middle (a first look)

### 18. Simulation and implementation discipline

Problems where the statement is the algorithm. Structuring long implementations so they stay debuggable.

- translating a statement into state + transitions
- step loops, event loops and termination
- cycle detection in a simulation
- dates and calendars
- decomposing into small tested functions
- reading a long statement without missing a rule

### 19. Prefix sums and difference arrays

Answering range questions in O(1) after one pass.

- 1D prefix sums and the half-open convention
- range sum, range count, range average
- difference arrays for range updates
- 2D prefix sums and the inclusion-exclusion rectangle
- prefix XOR, prefix max, prefix products
- prefix sums plus a hash map: subarrays with a given sum
- prefix sums modulo k

### 20. Two pointers and sliding window

Turning an O(n^2) scan into O(n) by never moving a pointer backwards.

- opposite-direction pointers on a sorted array
- same-direction pointers: the window
- fixed-size and variable-size windows
- the monotone condition that makes it valid
- window with a counting array inside
- merging two sorted sequences
- three pointers and partitioning

### 21. Binary search, including binary search on the answer

The loop invariant that never goes wrong, and the trick of searching over answers rather than over data.

- the canonical while (lo < hi) template
- off-by-one: which half to discard
- lower_bound / upper_bound semantics
- predicate form: the first true in a monotone sequence
- binary search on the answer (minimise the maximum)
- binary search over a real interval with fixed iterations
- ternary search on a unimodal function

### 22. Greedy - and how to prove it

The most used and most mis-used technique in Group C. A greedy solution is worthless without an argument.

- the greedy-choice property and the exchange argument
- sort-then-scan as the canonical shape
- interval scheduling and interval covering
- fractional versus 0/1 choices
- greedy with a priority queue
- counterexample hunting: how to disprove your own greedy
- when greedy fails and DP takes over

### 23. Sorting-based techniques: sweep line and coordinate compression

What becomes easy once the data is in the right order.

- event sweeps: +1 / -1 at interval ends
- maximum overlap and the 'how many at once' family
- coordinate compression of large value ranges
- sorting by a derived key
- counting inversions with merge sort
- offline query processing: sort the queries too

### 24. Number theory I: divisibility, primes and GCD

The arithmetic toolkit behind the largest single family of problems in the catalogue.

- divisibility, divisors in O(sqrt n)
- primality test in O(sqrt n)
- sieve of Eratosthenes; smallest-prime-factor sieve
- factorisation via the sieve
- gcd, lcm and the Euclidean algorithm
- number of divisors and sum of divisors from the factorisation
- digit manipulation: digit sum, reversal, base conversion
- perfect numbers, palindromic numbers and the usual suspects

### 25. Number theory II: modular arithmetic and fast exponentiation

Working under a modulus without overflow, and computing powers in logarithmic time.

- the modular identities for +, -, *
- keeping intermediate values inside long long
- negative values and the ((x % m) + m) % m idiom
- binary exponentiation
- modular inverse via Fermat's little theorem
- division under a modulus
- cycles: pow(a, k) mod m repeats
- when the statement says 'output the answer modulo 10^9+7'

### 26. Combinatorics and counting

Counting without enumerating.

- the product and sum rules
- permutations, combinations, and C(n, k) by Pascal's triangle
- counting with repetition; stars and bars
- inclusion-exclusion on small sets
- counting complement instead of the thing itself
- pigeonhole arguments
- Catalan numbers and where they show up
- binomials modulo a prime

### 27. Backtracking and generating combinatorial objects

Systematic search with undo. Generating every subset, permutation and arrangement, and cutting the tree early.

- the choose / recurse / un-choose skeleton
- generating subsets, permutations, combinations
- n-queens and placement problems
- used[] versus swapping in place
- pruning: feasibility and bound checks
- counting solutions versus listing them
- lexicographic order and next_permutation as an alternative

### 28. Bitmasks and subset enumeration

Representing a set of up to ~20 items in one integer.

- the operators: & | ^ ~ << >>
- set, clear, toggle, test a bit
- popcount, lowest set bit, __builtin_ functions
- iterating over all 2^n subsets
- iterating over submasks of a mask
- bitset for dense boolean arrays
- XOR properties and the 'find the odd one out' family
- bitmask as a DP state (preview of Lesson 32)

### 29. Dynamic programming I: one dimension

State, transition, base case, order of evaluation - on a single axis.

- recognising overlapping subproblems
- memoisation versus bottom-up tables
- Fibonacci, staircase, and the first transitions
- coin change: minimum coins and number of ways
- 0/1 knapsack and its rolling-array form
- longest increasing subsequence in O(n^2) and O(n log n)
- maximum subarray (Kadane)
- reconstructing the answer, not just its value

### 30. Dynamic programming II: two dimensions and grids

Two-index states: grids, pairs of sequences, and the layouts that keep them in memory.

- paths in a grid with obstacles
- longest common subsequence
- edit distance
- two-sequence alignment patterns
- the order of the loops and why it matters
- rolling rows to cut memory
- reconstruction by walking the table backwards

### 31. Dynamic programming III: interval, digit and bitmask DP

The state shapes that appear once the obvious ones stop working.

- interval DP: dp[l][r] and the split point
- palindrome partitioning, matrix chain, stone merging
- digit DP over the decimal representation
- bitmask DP over subsets
- DP on a tree (subtree states)
- choosing a state: what must be remembered and what must not

### 32. Graphs: representation and traversal

Adjacency lists, BFS and DFS, and the questions each one answers.

- adjacency list vs adjacency matrix vs edge list
- reading a graph; directed vs undirected
- DFS recursive and iterative; visited discipline
- BFS and the layer structure
- connected components and component sizes
- cycle detection in both directions
- bipartite checking by 2-colouring
- topological sort (Kahn and DFS)

### 33. Flood fill and grid graphs

Treating a grid as a graph - the most common way graph theory appears in Groups C and D.

- the grid as an implicit graph
- flood fill by DFS and by BFS
- counting regions and measuring their size
- multi-source BFS
- shortest path on an unweighted grid
- 0-1 BFS with a deque
- obstacles, walls and boundary handling
- stack depth: when recursion is not safe

### 34. Shortest paths

From unweighted BFS to Dijkstra, and how to know which one the weights allow.

- BFS for unit weights
- 0-1 BFS with a deque
- Dijkstra with a priority queue
- path reconstruction via parent arrays
- Bellman-Ford and negative weights
- Floyd-Warshall for all pairs on small graphs
- state-expanded graphs (position plus something else)

### 35. Trees

Graphs with no cycles - and the simplifications that buys.

- properties: n-1 edges, unique paths
- rooting a tree; parent, depth, subtree size
- DFS on a tree without a visited array
- subtree aggregation (DP on trees)
- diameter in two DFS passes
- binary trees and traversal orders
- lowest common ancestor: the simple O(depth) method and binary lifting

### 36. Disjoint set union (union-find)

Fifteen lines that answer 'are these two in the same group?' in near-constant time.

- the parent array and find
- path compression
- union by size or rank
- counting components and component sizes
- offline connectivity queries
- Kruskal's minimum spanning tree
- DSU on a grid

### 37. Fenwick and segment trees

Range queries with updates - the structure to reach for when prefix sums stop working.

- why a static prefix sum fails under updates
- Fenwick tree: update and prefix query
- Fenwick for counting inversions
- segment tree: build, query, point update
- segment tree for min, max, gcd
- lazy propagation for range updates
- choosing between Fenwick, segment tree and a sqrt decomposition

### 38. String algorithms: KMP, Z, hashing and tries

Beyond std::string - the linear-time algorithms for pattern matching and substring comparison.

- naive matching and why it is O(nm)
- the prefix function and KMP
- the Z function
- polynomial hashing and O(1) substring comparison
- collision risk and double hashing
- tries: insertion, lookup, prefix counting
- palindromes: Manacher's algorithm (a look)
- when a plain find() is enough

### 39. Geometry basics

Points, vectors and the handful of primitives that cover the school-level geometry tasks.

- points and vectors as pairs
- dot product and cross product
- orientation of three points
- area of a triangle and of a polygon (shoelace)
- distance point-to-point, point-to-line, point-to-segment
- segment intersection
- point in polygon
- integer arithmetic to avoid floating point entirely

### 40. Game theory

Two players, perfect information, and deciding who wins from the starting position.

- winning and losing positions
- computing W/L states by DP
- the subtraction game and periodicity
- Nim and the XOR rule
- Sprague-Grundy numbers for sums of games
- symmetry and mirroring strategies

### 41. Ad hoc, constructive problems and invariants

Problems with no named algorithm. What to look for when nothing fits.

- finding the invariant: what never changes
- parity arguments
- monovariants and termination proofs
- constructing an example rather than searching for one
- small-case tables to reveal a pattern
- extremal arguments
- proving impossibility
- recognising when a formula replaces a loop

### 42. Contest craft: strategy, testing and debugging

The part that is not code. How to spend the five hours, and how to stop losing points you have already earned.

- reading the set and choosing an order
- constraints as a hint about the intended complexity
- writing a brute-force oracle
- stress testing with a random generator
- edge cases that recur: n=1, all equal, maximum values, empty input
- reading the output format exactly
- partial scoring: taking the subtasks you can
- debugging with asserts and prints; what to do when you are stuck
- time management and when to abandon a problem

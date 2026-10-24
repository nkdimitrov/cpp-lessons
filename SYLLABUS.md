# C++17 for Competitive Programming

A structured course built on the classified Olimpiici Arena catalogue (Groups C and D, 2007-2026)

Generated from `syllabus.json` by `tools/build_site.py` - edit the JSON, not this file.

- Site hub: [index.html](index.html)
- Problem catalogue: [Problem catalogue](Group C and D problems/index.html) - 768 problems, each tagged with a primary algorithm, an optional secondary algorithm, technique tags, a 1-5 difficulty and a one-line hint.

## Part I - Language and data structures

The C++17 you actually type in a contest, at the level of a 5th or 6th grader: only the basics. Every lesson is self-contained, follows the shape of Lesson 03, and ends with 12 Group D problems from the catalogue, grouped by subtopic and getting harder as you go.

| # | Lesson | Status | Candidate problems | Catalogue filter |
|---|--------|--------|--------------------|------------------|
| 01 | Setup, I/O and the contest toolkit | **written** | 12 assigned | `I/O parsing · Group D · level 1-3` |
| 02 | Numbers: int, long long, bool and double | **written** | 12 assigned | `Long long · Group D · level 1-3` |
| 03 | Strings | **written** | 12 assigned | `String processing · Group D` |
| 04 | Arrays - a row of numbered boxes | **written** | 12 assigned | `Arrays · Group D · level 1-3` |
| 05 | std::vector - a list that grows | **written** | 12 assigned | `Vectors · Group D · level 2-4` |
| 06 | Counting and frequency arrays | **written** | 12 assigned | `Counting / Frequency arrays · Group D · level 2-4` |
| 07 | Two-dimensional arrays and grids | **written** | 12 assigned | `2D arrays · Group D · level 2-4` |
| 08 | Sorting | **written** | 12 assigned | `Sorting · Group D · level 2-4` |
| 09 | Pairs and structs | **written** | 12 assigned | `Pairs / Structs · Group D · level 2-4` |
| 10 | Stacks, queues and deques | **written** | 12 assigned | `Stacks / Queues / Deque · Group D · level 2-4` |
| 11 | Sets and maps | **written** | 12 assigned | `Maps / Sets · Group D · level 2-4` |
| 12 | Priority queues | **written** | 12 assigned | `Priority queue · Group D · level 3-5` |
| 13 | The <algorithm> toolbox | **written** | 12 assigned | `Vectors · Group D · level 2-3` |
| 14 | Big integers - arithmetic beyond long long | **written** | 12 assigned | `Big numbers · Group D · level 2-5` |
| 15 | Recursion | **written** | 12 assigned | `Recursion · Group D · level 2-4` |
| 16 | Time and memory limits | **written** | 12 assigned | `Memory optimization · Group D · level 3-5` |

### 01. Setup, I/O and the contest toolkit

The skeleton of every solution: reading numbers and characters, printing exactly what is asked, and checking before you send.

- the program skeleton, compiling and running
- cin >> and cout <<, spaces and new lines
- a count, then that many numbers - answering while reading
- the best so far and the longest streak
- reading characters one at a time, and until the input ends
- inputs like 12+7 and 21.05.2015
- fast input, and '
' instead of endl
- what the judge's verdicts mean

### 02. Numbers: int, long long, bool and double

Which number type to use, how / and % take a number apart, and when a formula beats a loop.

- int and long long - and overflow
- 1LL * a * b
- / and %: digits, units, rounding up
- n(n+1)/2 and counting multiples with a formula
- bool, &&, ||, !
- double, setprecision, and exact square roots

### 03. Strings

Words and text: characters as numbers, walking along a string, counting letters and palindromes.

- s[i], s.size(), cin >> s
- characters as numbers: c - 'a', c - '0'
- <cctype> tests and changes
- runs of equal characters, and find
- +=, substr, reverse, comparing words
- getline and cin.ignore()
- counting letters with cnt[26]
- palindromes

### 04. Arrays - a row of numbered boxes

Filling and scanning an array, looking at neighbours, going round a circle and sliding a window.

- declaring arrays outside main
- reading and printing, forwards and backwards
- sum, largest, smallest, count
- neighbours a[i-1] and a[i+1]
- going round a circle with %
- sliding a window of k boxes
- several passes and several arrays

### 05. std::vector - a list that grows

When you do not know the size in advance: push_back, digits in a vector, building new lists, and one list per group.

- push_back, size, back, pop_back
- vector<int> a(n) when the size is known
- sort and reverse on a vector
- the digits of a number in a vector
- building a new vector instead of erasing
- insert in the middle, and what it costs
- an array of vectors: one list per group

### 06. Counting and frequency arrays

The value becomes the box number: counting, marking, the commonest value and counting sort.

- cnt[x]++ and choosing the size
- shifting negative values
- seen[] for marking
- the commonest value
- c * (c - 1) / 2 pairs
- counting as you go
- counting sort and the k-th smallest

### 07. Two-dimensional arrays and grids

Tables of rows and columns: row and column scans, neighbours, spirals and diagonals.

- a[i][j]: row first, then column
- row sums and column sums
- grids of characters
- the four neighbours with dr / dc
- snake order, spiral and turning by 90 degrees
- diagonals and runs along a line

### 08. Sorting

sort in one line, sorting by your own rule, and the problems that become easy once things are in order.

- sort on arrays, vectors and strings
- largest first with greater<int>()
- neighbours after sorting, counting different values
- compare functions with several rules
- two sorted lists side by side
- sort first, then decide

### 09. Pairs and structs

Keeping values that belong together, sorting them, and returning two things from a function.

- pair, .first and .second
- sorting pairs: by first, then by second
- {value, number} to remember who is who
- struct with named fields
- sorting structs with a compare function
- returning a pair from a function

### 10. Stacks, queues and deques

Piles and lines: three containers with one simple rule each.

- stack: push, top, pop, empty
- queue: push, front, pop
- deque: both ends
- the circle game with a queue
- checking brackets
- a stack that keeps only what matters

### 11. Sets and maps

Remembering what you have seen, for any values: different values, counts and fast lookups.

- set: insert, count, erase, size
- map: m[key]++ and the m[key] trap
- walking a set or a map in order
- looking up a partner with S - x
- array, set or map?

### 12. Priority queues

A box that always hands you the largest - or the smallest - value.

- priority_queue: push, top, pop
- smallest first with greater<int>
- joining the two smallest
- pairs in a priority queue
- events in time order
- priority queue or sort?

### 13. The <algorithm> toolbox

Ready-made loops: min, max, count, find, reverse, unique, next_permutation and binary search.

- a, a + n and v.begin(), v.end()
- min, max, swap, min_element, max_element
- count and find
- reverse, rotate, unique
- next_permutation: every order
- binary_search, lower_bound, upper_bound

### 14. Big integers - arithmetic beyond long long

Numbers with hundreds of digits, handled digit by digit like sums on paper.

- digits stored backwards in a vector
- adding with a carry
- multiplying by a small number
- subtracting and comparing
- multiplying two long numbers
- dividing by a small number, and the remainder

### 15. Recursion

A function that calls itself: the base case, remembering answers, and trying every choice.

- base case and step: factorial, digit sum, gcd
- how the calls wait for each other
- remembering answers (Fibonacci)
- all 0/1 strings and all groups
- all orders with backtracking

### 16. Time and memory limits

Counting steps and bytes before you write a line, and the shortcuts that make a slow idea fast.

- counting steps: O(n), O(n * n), O(log n)
- about 10^8 steps per second
- which n allows which solution
- formulas and the square-root shortcut
- bytes per value and the memory limit
- a checklist before coding

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

# C++17 for Competitive Programming

A C++17 course for Bulgarian olympiad preparation — NOI Groups C and D — written for
5th–6th graders, together with a searchable catalogue of 768 classified competition
problems from the Olimpiici Arena (2007–2026).

The whole thing is a static site: a hub that lists the lessons, one page per lesson,
and the problem catalogue. No build system, no runtime dependencies, no JavaScript
framework. Open `index.html` in a browser and it works, over `file://` as well as
over HTTP.

Once GitHub Pages is enabled for this repository (Settings → Pages → deploy from
`main`, root folder), it is served at <https://nkdimitrov.github.io/cpp-lessons/>.

## What is here

| | |
|---|---|
| **43 lessons planned** | 17 on the language and its data structures, 26 on algorithms and techniques |
| **17 lessons written** | all of Part I: setup and I/O, numbers, strings, arrays, vectors, counting arrays, grids, sorting, pairs and structs, stacks and queues, sets and maps, priority queues, the `<algorithm>` toolbox, big integers, recursion, time and memory limits, and practice contests |
| **768 problems classified** | difficulty 1–5, primary and secondary algorithm, technique tags, a one-line hint and a link to the Arena statement |

Each lesson page carries theory, a cheat sheet, the pitfalls that actually cost marks,
a complexity table, and 12 practice problems from Group D, grouped by subtopic and getting
harder as you go — every practice group mapped back to the theory section that solves it.
Lesson 17 closes Part I with 33 unused Group D problems in eleven contest-style rounds of three. Progress ticks and the light/dark
theme are stored per browser in `localStorage`.

Lesson pages are also exported to Word (`NN_Topic/NN_Topic.docx`) for printing.

## Layout

```
index.html                     site hub                  (generated)
SYLLABUS.md                    the lesson plan           (generated)
syllabus.json                  the plan, editable        <- edit this
Group C and D problems/
    index.html                 the 768-problem catalogue (source of truth)
    olympiad-problems.xlsx     the spreadsheet it came from
NN_Topic/                      one directory per lesson
    content.py                 lesson text               <- write this
    problems.json              problem selection         <- build with tools/catalog.py
    NN_Topic.html              generated
    NN_Topic.docx              generated
tools/
    catalog.py                 query the classification
    render_lesson.py           content.py + problems.json -> HTML + DOCX
    build_site.py              syllabus.json -> index.html + SYLLABUS.md
```

Generated files are committed so the site can be served straight from the repository.
Edit `syllabus.json`, `content.py` and `problems.json`; never the generated HTML.

## Building

Python 3.9+ is all you need. `python-docx` is optional and only used for the Word export.

Render one lesson (add `--html-only` when `python-docx` is not installed):

```bash
python tools/render_lesson.py 03_Strings
```

Rebuild the hub and the syllabus after adding a lesson or assigning problems:

```bash
python tools/build_site.py
```

## Querying the problem catalogue

`tools/catalog.py` reads the classification embedded in `Group C and D problems/index.html`
and is how problems are chosen for a lesson — never by hand, and never by fetching the
Arena site.

```bash
python tools/catalog.py vocab
```

```bash
python tools/catalog.py find --any-tech Stacks --any-tech Queues --diff 2-3 --limit 20
```

```bash
python tools/catalog.py pick --alg "Greedy" --diff 2-3 --limit 6 --section A --out 23_Greedy/problems.json
```

Filters: `--alg`, `--any-alg`, `--exclude-alg`, `--tech`, `--any-tech`, `--group`,
`--diff`, `--year`, `--comp`, `--q`, and `--not-used`, which hides problems already
placed in some lesson so the same problem is not assigned twice.

## Writing a lesson

[CLAUDE.md](CLAUDE.md) is the working specification: the content conventions (how much
C++ a 5th-grader may be shown, only the basics, contest style over production style, British
English), the problem-selection rules (12 Group D problems, grouped by subtopic, difficulty
rising from 1–2 to 3–4), and the shape of `content.py`. [03_Strings](03_Strings/)
is the reference lesson — match it.

## Note on the statements

Problem statements on the Arena are in Bulgarian and are not redistributed here; the
catalogue links to them. The `hint` and `en` fields carry the English gloss. Lesson prose
is in English.

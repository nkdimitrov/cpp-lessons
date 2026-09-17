# C++17 for Competitive Programming

A C++17 course for Bulgarian olympiad preparation — NOI Groups C and D — written for
6th–7th graders, together with a searchable catalogue of 768 classified competition
problems from the Olimpiici Arena (2007–2026).

The whole thing is a static site: a hub that lists the lessons, one page per lesson,
and the problem catalogue. No build system, no runtime dependencies, no JavaScript
framework. Open `index.html` in a browser and it works, over `file://` as well as
over HTTP.

## What is here

| | |
|---|---|
| **42 lessons planned** | 16 on the language and its data structures, 26 on algorithms and techniques |
| **5 lessons written** | setup and I/O, primitive types, strings, arrays, vectors |
| **768 problems classified** | difficulty 1–5, primary and secondary algorithm, technique tags, a one-line hint and a link to the Arena statement |

Each lesson page carries theory, a cheat sheet, the pitfalls that actually cost marks,
a complexity table, and a graded practice set drawn from the catalogue — every practice
group mapped back to the theory section that solves it. Progress ticks and the light/dark
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
python tools/catalog.py pick --alg "Greedy" --diff 2-3 --limit 6 --section A --out 22_Greedy/problems.json
```

Filters: `--alg`, `--any-alg`, `--exclude-alg`, `--tech`, `--any-tech`, `--group`,
`--diff`, `--year`, `--comp`, `--q`, and `--not-used`, which hides problems already
placed in some lesson so the same problem is not assigned twice.

## Writing a lesson

[CLAUDE.md](CLAUDE.md) is the working specification: the content conventions (how much
C++ a 6th-grader may be shown, contest style over production style, British English),
the problem-selection rules (18–26 problems, 4–6 lettered groups, easiest first, start
at difficulty 1–2 and end at 4–5), and the shape of `content.py`. [03_Strings](03_Strings/)
is the reference lesson — match it.

## Note on the statements

Problem statements on the Arena are in Bulgarian and are not redistributed here; the
catalogue links to them. The `hint` and `en` fields carry the English gloss. Lesson prose
is in English.

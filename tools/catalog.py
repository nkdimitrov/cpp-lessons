# -*- coding: utf-8 -*-
"""Query the classified problem catalogue.

The single source of truth is the embedded `const DATA = {...}` object inside
`Group C and D problems/index.html` (768 problems, Groups C and D, 2007-2026,
each tagged with a primary algorithm, an optional secondary algorithm, a set of
technique tags, a 1-5 difficulty and a one-line hint).

    python tools/catalog.py vocab
    python tools/catalog.py stats [filters]
    python tools/catalog.py find  [filters] [--limit N] [--sort diff|year|name]
    python tools/catalog.py pick  [filters] --section A --out 04_Arrays/problems.json

Filters (all optional, all combinable):
    --alg "Prefix sums"        primary OR secondary algorithm (substring match)
    --tech Arrays --tech Loops technique tag; repeatable, AND semantics
    --any-tech Pairs --any-tech Structs   technique tag; OR semantics
    --any-alg Trees --any-alg Greedy      algorithm; OR semantics
    --group D                  C or D
    --diff 2-3                 single level or inclusive range, 1..5
    --year 2015-2026
    --comp "Municipal"         competition name, substring match
    --q palindrome             free text over name + hint
    --exclude-alg "Dynamic"    drop rows whose either algorithm matches
    --not-used                 drop problems already placed in a lesson
"""
import argparse, json, pathlib, re, sys, collections

sys.stdout.reconfigure(encoding="utf-8")

ROOT    = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "Group C and D problems" / "index.html"
DL      = ["", "Very easy", "Easy", "Medium", "Hard", "Very hard"]
ROUND_SHORT = {"NOI - Municipal round": "Municipal round",
               "NOI - Regional round": "Regional round",
               "NOI - National round": "National round"}


# ----------------------------------------------------------------- loading
def load():
    html = CATALOG.read_text(encoding="utf-8")
    m = re.search(r"const DATA = (\{.*?\});\s*\n", html, re.S)
    if not m:
        sys.exit("could not find `const DATA = {...}` in %s" % CATALOG)
    d = json.loads(m.group(1))
    out = []
    for r in d["rows"]:
        out.append({
            "name":  r[0],
            "comp":  d["comps"][r[1]],
            "group": r[2],
            "year":  r[3],
            "diff":  r[4],
            "alg":   d["algs"][r[5]],
            "alg2":  d["algs"][r[6]] if r[6] >= 0 else "",
            "techs": [d["techs"][i] for i in r[7]],
            "hint":  r[8],
            "url":   r[9],
            "pdf":   r[10],
            "flag":  r[11],
        })
    return d, out


def used_urls():
    """Every problem URL already referenced by a lesson's problems.json."""
    seen = {}
    for pj in ROOT.glob("*/problems.json"):
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
        except Exception:
            continue
        for p in data.get("problems", []):
            if p.get("url"):
                seen[p["url"]] = pj.parent.name
    return seen


# ---------------------------------------------------------------- filtering
def rng(spec, lo, hi):
    if "-" in spec:
        a, b = spec.split("-", 1)
        return int(a or lo), int(b or hi)
    return int(spec), int(spec)


def apply_filters(rows, a):
    used = used_urls() if a.not_used else {}
    out = []
    for r in rows:
        if a.group and r["group"] != a.group.upper():
            continue
        if a.alg and not any(a.alg.lower() in x.lower() for x in (r["alg"], r["alg2"]) if x):
            continue
        if a.exclude_alg and any(a.exclude_alg.lower() in x.lower()
                                 for x in (r["alg"], r["alg2"]) if x):
            continue
        if a.tech:
            have = [t.lower() for t in r["techs"]]
            if not all(any(want.lower() in t for t in have) for want in a.tech):
                continue
        if getattr(a, "any_tech", None):
            have = [t.lower() for t in r["techs"]]
            if not any(any(want.lower() in t for t in have) for want in a.any_tech):
                continue
        if getattr(a, "any_alg", None):
            mine = [x.lower() for x in (r["alg"], r["alg2"]) if x]
            if not any(any(want.lower() in m for m in mine) for want in a.any_alg):
                continue
        if a.diff:
            lo, hi = rng(a.diff, 1, 5)
            if not lo <= r["diff"] <= hi:
                continue
        if a.year:
            lo, hi = rng(a.year, 1900, 2100)
            if not lo <= r["year"] <= hi:
                continue
        if a.comp and a.comp.lower() not in r["comp"].lower():
            continue
        if a.q and a.q.lower() not in (r["name"] + " " + r["hint"]).lower():
            continue
        if a.not_used and r["url"] in used:
            continue
        out.append(r)
    return out


SORTS = {"diff": lambda r: (r["diff"], r["year"], r["name"]),
         "year": lambda r: (r["year"], r["diff"]),
         "name": lambda r: r["name"].lower()}


# ---------------------------------------------------------------- commands
def cmd_vocab(d, rows, a):
    print("ALGORITHMS (%d)" % len(d["algs"]))
    for x in d["algs"]:
        print("   ", x)
    print("\nTECHNIQUES (%d)" % len(d["techs"]))
    for x in d["techs"]:
        print("   ", x)
    print("\nCOMPETITIONS (%d)" % len(d["comps"]))
    for x in d["comps"]:
        print("   ", x)


def cmd_stats(d, rows, a):
    sel = apply_filters(rows, a)
    print("%d problems match (of %d)\n" % (len(sel), len(rows)))
    if not sel:
        return
    by_d = collections.Counter(r["diff"] for r in sel)
    print("BY DIFFICULTY")
    for k in range(1, 6):
        print("  %d %-10s %4d  %s" % (k, DL[k], by_d[k], "#" * min(by_d[k], 60)))
    by_g = collections.Counter(r["group"] for r in sel)
    print("\nBY GROUP   " + "   ".join("%s: %d" % kv for kv in sorted(by_g.items())))
    ac = collections.Counter()
    for r in sel:
        ac[r["alg"]] += 1
        if r["alg2"]:
            ac[r["alg2"]] += 1
    print("\nBY ALGORITHM (primary + secondary)")
    for k, v in ac.most_common(15):
        print("  %4d  %s" % (v, k))
    tc = collections.Counter(t for r in sel for t in r["techs"])
    print("\nBY TECHNIQUE")
    for k, v in tc.most_common(15):
        print("  %4d  %s" % (v, k))


def cmd_find(d, rows, a):
    sel = sorted(apply_filters(rows, a), key=SORTS[a.sort])
    used = used_urls()
    print("%d match%s\n" % (len(sel), "" if len(sel) == 1 else "es"))
    for r in sel[:a.limit]:
        mark = "  [in %s]" % used[r["url"]] if r["url"] in used else ""
        print("%-16s %s %-4s %d%-12s %s" % (
            r["name"], "G" + r["group"], r["year"], r["diff"],
            " " + DL[r["diff"]], r["alg"] + (" + " + r["alg2"] if r["alg2"] else "")))
        print("    %s" % ", ".join(r["techs"]))
        print("    %s%s" % (r["hint"], mark))
        print("    %s" % r["url"])
    if len(sel) > a.limit:
        print("... %d more (raise --limit)" % (len(sel) - a.limit))


def cmd_pick(d, rows, a):
    """Emit lesson-shaped problem entries ready to paste into problems.json."""
    sel = sorted(apply_filters(rows, a), key=SORTS[a.sort])[:a.limit]
    items = []
    for r in sel:
        pid = re.search(r"/problem/(\d+)", r["url"])
        items.append({
            "section": a.section,
            "pid":     int(pid.group(1)) if pid else 0,
            "title":   r["name"],
            "en":      r["hint"],
            "tech":    ", ".join(r["techs"]),
            "family":  ROUND_SHORT.get(r["comp"], r["comp"]),
            "year":    r["year"],
            "diff":    r["diff"],
            "url":     r["url"],
        })
    blob = json.dumps(items, ensure_ascii=False, indent=1)
    if a.out:
        dest = (ROOT / a.out).resolve()
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.suffix == ".json" and dest.name == "problems.json":
            existing = json.loads(dest.read_text(encoding="utf-8"))
            existing.setdefault("problems", []).extend(items)
            dest.write_text(json.dumps(existing, ensure_ascii=False, indent=1), encoding="utf-8")
            print("appended %d problems to %s" % (len(items), dest))
        else:
            dest.write_text(blob, encoding="utf-8")
            print("wrote %d problems to %s" % (len(items), dest))
    else:
        print(blob)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["vocab", "stats", "find", "pick"])
    ap.add_argument("--alg")
    ap.add_argument("--exclude-alg", dest="exclude_alg")
    ap.add_argument("--tech", action="append", default=[],
                    help="AND: every --tech must be present")
    ap.add_argument("--any-tech", dest="any_tech", action="append", default=[],
                    help="OR: at least one --any-tech must be present")
    ap.add_argument("--any-alg", dest="any_alg", action="append", default=[],
                    help="OR: primary or secondary algorithm matches one of these")
    ap.add_argument("--group")
    ap.add_argument("--diff")
    ap.add_argument("--year")
    ap.add_argument("--comp")
    ap.add_argument("--q")
    ap.add_argument("--not-used", dest="not_used", action="store_true")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--sort", choices=list(SORTS), default="diff")
    ap.add_argument("--section", default="A", help="lesson section key for `pick`")
    ap.add_argument("--out", help="destination path for `pick`")
    a = ap.parse_args()
    d, rows = load()
    {"vocab": cmd_vocab, "stats": cmd_stats, "find": cmd_find, "pick": cmd_pick}[a.cmd](d, rows, a)


if __name__ == "__main__":
    main()

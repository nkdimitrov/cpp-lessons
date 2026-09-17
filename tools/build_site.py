# -*- coding: utf-8 -*-
"""Build the site hub (index.html) from syllabus.json.

    python tools/build_site.py

For every lesson it reports:
  * status  - done (the lesson HTML exists) or planned
  * pool    - how many catalogue problems match the lesson's `filters`
  * picked  - how many are actually placed in that lesson's problems.json

Progress ticks are read from localStorage, using the same per-lesson key the
lesson pages write (cpp_done_<SLUG>), so the hub shows real completion.
"""
import json, html, pathlib, sys, re, importlib.util

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import catalog as CAT  # noqa: E402

SYL = json.loads((ROOT / "syllabus.json").read_text(encoding="utf-8"))
DL = ["", "Very easy", "Easy", "Medium", "Hard", "Very hard"]
cat_href  = SYL["catalog"]["href"]
cat_label = SYL["catalog"]["label"]


# ------------------------------------------------------------------ catalog
class F:
    """Duck-typed stand-in for catalog.py's argparse namespace."""
    def __init__(self, f):
        self.alg = f.get("alg")
        self.exclude_alg = f.get("exclude_alg")
        self.tech = f.get("tech", [])
        self.any_tech = f.get("any_tech", [])
        self.any_alg = f.get("any_alg", [])
        self.group = f.get("group")
        self.diff = f.get("diff")
        self.year = f.get("year")
        self.comp = f.get("comp")
        self.q = f.get("q")
        self.not_used = False


_d, _rows = CAT.load()


def pool_for(f):
    if not f:
        return None
    sel = CAT.apply_filters(_rows, F(f))
    by_d = [0] * 6
    for r in sel:
        by_d[r["diff"]] += 1
    return {"n": len(sel), "byd": by_d}


def picked_for(slug):
    pj = ROOT / slug / "problems.json"
    if not pj.exists():
        return 0
    try:
        return len(json.loads(pj.read_text(encoding="utf-8")).get("problems", []))
    except Exception:
        return 0


def built(slug):
    return (ROOT / slug / (slug + ".html")).exists()


def filter_label(f):
    if not f:
        return ""
    bits = []
    if f.get("alg"):
        bits.append(f["alg"])
    for t in f.get("tech", []):
        bits.append(t)
    if f.get("any_alg"):
        bits.append(" / ".join(f["any_alg"]))
    if f.get("any_tech"):
        bits.append(" / ".join(f["any_tech"]))
    if f.get("group"):
        bits.append("Group " + f["group"])
    if f.get("diff"):
        bits.append("level " + f["diff"])
    if f.get("comp"):
        bits.append(f["comp"])
    return " · ".join(bits)


# ---------------------------------------------------------------------- CSS
CSS = """
:root{
  --font-body:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --font-display:"Source Serif 4",Georgia,"Times New Roman",serif;
  --font-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --bg:#f5f7fa; --panel:#ffffff; --ink:#16233a; --muted:#5d6b82; --line:#dfe5ee;
  --accent:#1f4f9c; --accent-soft:#e8f0fd;
  --shadow:0 1px 2px rgba(16,32,64,.06),0 6px 18px rgba(16,32,64,.06);
  --ok:#2e7d32; --okb:#e4f5e5; --plan:#5d6b82; --planb:#eef1f6;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#10151d; --panel:#171e28; --ink:#e6ecf5; --muted:#93a1b5; --line:#2a3442;
    --accent:#7fb0ff; --accent-soft:#1b2838;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 22px rgba(0,0,0,.35);
    --ok:#8ed49a; --okb:#1d3524; --plan:#93a1b5; --planb:#1e2733;
  }
}
:root[data-theme="dark"]{
  --bg:#10151d; --panel:#171e28; --ink:#e6ecf5; --muted:#93a1b5; --line:#2a3442;
  --accent:#7fb0ff; --accent-soft:#1b2838;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 22px rgba(0,0,0,.35);
  --ok:#8ed49a; --okb:#1d3524; --plan:#93a1b5; --planb:#1e2733;
}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.55 var(--font-body);margin:0}
.page{max-width:1120px;margin:0 auto;padding-block:30px;padding-left:20px;padding-right:20px}
a{color:var(--accent)}
h1{font-family:var(--font-display);font-size:30px;font-weight:700;margin:0 0 6px;
   letter-spacing:-.012em;text-wrap:balance}
.sub{color:var(--muted);margin:0 0 22px;font-size:14.5px;max-width:74ch}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}

.topbar{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:22px}
.chipbtn{font:inherit;font-size:13px;padding:7px 14px;border:1px solid var(--line);
  border-radius:999px;background:var(--panel);color:var(--ink);cursor:pointer;text-decoration:none}
.chipbtn:hover{border-color:var(--accent);color:var(--accent)}
.chipbtn.primary{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);font-weight:600}

.summary{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:26px}
.stat{padding:12px 16px;min-width:132px;flex:1 1 132px}
.stat b{display:block;font-family:var(--font-display);font-size:24px;line-height:1.1}
.stat span{color:var(--muted);font-size:12px;font-family:var(--font-mono);
  letter-spacing:.06em;text-transform:uppercase}

.track{margin:34px 0 0}
.track > h2{font-family:var(--font-display);font-size:21px;margin:0 0 4px;letter-spacing:-.01em}
.track > p{color:var(--muted);margin:0 0 16px;font-size:14px;max-width:78ch}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.card{padding:16px 18px;display:flex;flex-direction:column;gap:8px}
.card .hd{display:flex;align-items:baseline;gap:10px}
.num{font-family:var(--font-mono);font-size:12px;color:var(--muted);letter-spacing:.06em}
.card h3{font-family:var(--font-display);font-size:17px;margin:0;flex:1 1 auto;line-height:1.25}
.card h3 a{text-decoration:none}
.card h3 a:hover{text-decoration:underline}
.badge{font-family:var(--font-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;
  padding:3px 8px;border-radius:999px;white-space:nowrap}
.badge.done{color:var(--ok);background:var(--okb)}
.badge.plan{color:var(--plan);background:var(--planb)}
.card .sm{color:var(--muted);font-size:13.5px;margin:0}
.covers{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:5px}
.covers li{font-size:11.5px;font-family:var(--font-mono);color:var(--muted);
  border:1px solid var(--line);border-radius:5px;padding:2px 7px}
.covers li.more{border-style:dashed}
.foot{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:auto;padding-top:4px;
  font-size:12px;color:var(--muted);font-family:var(--font-mono)}
.foot .prog{flex:1 1 90px;min-width:70px;height:6px;background:var(--line);border-radius:4px;overflow:hidden}
.foot .prog i{display:block;height:100%;width:0;background:var(--ok)}
.pool a{text-decoration:none}

footer{margin-top:44px;padding-top:16px;border-top:1px solid var(--line);
  color:var(--muted);font-size:12.5px}
#themeBtn{position:fixed;top:14px;right:16px;z-index:10;font:inherit;font-size:13px;
  padding:5px 11px;border:1px solid var(--line);border-radius:8px;background:var(--panel);
  color:var(--ink);cursor:pointer}
@media(max-width:640px){
  h1{font-size:24px}
  .grid{grid-template-columns:1fr}
  #themeBtn{top:8px;right:10px}
}
"""

JS = r"""
var THEME_KEY="cpp_lessons_theme";
var tb=document.getElementById('themeBtn');
function setTheme(t){
  if(t) document.documentElement.setAttribute('data-theme',t);
  else document.documentElement.removeAttribute('data-theme');
  try{t?localStorage.setItem(THEME_KEY,t):localStorage.removeItem(THEME_KEY)}catch(e){}
}
try{var st=localStorage.getItem(THEME_KEY); if(st) setTheme(st);}catch(e){}
tb.onclick=function(){
  var cur=document.documentElement.getAttribute('data-theme');
  if(!cur){cur=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
  setTheme(cur==='dark'?'light':'dark');
};

// read each lesson's tick state, written by the lesson pages themselves
var totalDone=0, totalPicked=0;
[].forEach.call(document.querySelectorAll('[data-slug]'), function(card){
  var slug=card.dataset.slug, picked=+card.dataset.picked||0;
  if(!picked) return;
  var n=0;
  try{
    var raw=localStorage.getItem('cpp_done_'+slug);
    if(raw===null && card.dataset.legacy) raw=localStorage.getItem(card.dataset.legacy);
    var st=JSON.parse(raw||'{}')||{};
    for(var k in st) if(st[k]) n++;
  }catch(e){}
  if(n>picked) n=picked;
  totalDone+=n; totalPicked+=picked;
  var lbl=card.querySelector('.plabel'), bar=card.querySelector('.prog i');
  if(lbl) lbl.textContent=n+'/'+picked+' solved';
  if(bar) bar.style.width=(n/picked*100)+'%';
});
var s=document.getElementById('solvedStat');
if(s) s.innerHTML='<b>'+totalDone+'</b><span>problems solved</span>';
"""


# --------------------------------------------------------------- SYLLABUS.md
def write_markdown():
    L = []
    L.append("# %s" % SYL["title"])
    L.append("")
    L.append("%s" % SYL["subtitle"])
    L.append("")
    L.append("Generated from `syllabus.json` by `tools/build_site.py` - edit the JSON, not this file.")
    L.append("")
    L.append("- Site hub: [index.html](index.html)")
    L.append("- Problem catalogue: [%s](%s) - %s" % (cat_label, cat_href, SYL["catalog"]["note"]))
    L.append("")
    for tr in SYL["tracks"]:
        L.append("## %s" % tr["title"])
        L.append("")
        L.append(tr["blurb"])
        L.append("")
        L.append("| # | Lesson | Status | Candidate problems | Catalogue filter |")
        L.append("|---|--------|--------|--------------------|------------------|")
        for l in tr["lessons"]:
            pool = pool_for(l.get("filters"))
            picked = picked_for(l["slug"])
            status = "**written**" if built(l["slug"]) else "planned"
            if picked:
                cnt = "%d assigned" % picked
            elif pool:
                cnt = "%d" % pool["n"]
            else:
                cnt = "-"
            L.append("| %s | %s | %s | %s | `%s` |"
                     % (l["num"], l["title"], status, cnt, filter_label(l.get("filters")) or "-"))
        L.append("")
        for l in tr["lessons"]:
            L.append("### %s. %s" % (l["num"], l["title"]))
            L.append("")
            L.append(l["summary"])
            L.append("")
            for c in l.get("covers", []):
                L.append("- %s" % c)
            L.append("")
    out = ROOT / "SYLLABUS.md"
    out.write_text(chr(10).join(L), encoding="utf-8")
    return out


# --------------------------------------------------------------------- build
def main():
    P = []
    a = P.append
    a('<!DOCTYPE html>')
    a('<html lang="en"><head>')
    a('<meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width,initial-scale=1">')
    a('<title>%s</title>' % html.escape(SYL["title"]))
    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&'
      'family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap">')
    a('<style>%s</style>' % CSS)
    a('</head><body>')
    a('<button id="themeBtn" title="Toggle light / dark">&#9681; Theme</button>')
    a('<div class="page">')
    a('<h1>%s</h1>' % html.escape(SYL["title"]))
    a('<p class="sub">%s</p>' % html.escape(SYL["subtitle"]))

    cat = SYL["catalog"]
    a('<div class="topbar">')
    a('<a class="chipbtn primary" href="%s">%s &rarr;</a>'
      % (html.escape(cat["href"]), html.escape(cat["label"])))
    a('<a class="chipbtn" href="https://arena.olimpiici.com/#/catalog/1" target="_blank" '
      'rel="noopener">Olimpiici Arena</a>')
    a('<a class="chipbtn" href="SYLLABUS.md">Syllabus (markdown)</a>')
    a('</div>')

    # ---- headline numbers
    lessons = [l for t in SYL["tracks"] for l in t["lessons"]]
    n_done = sum(1 for l in lessons if built(l["slug"]))
    n_picked = sum(picked_for(l["slug"]) for l in lessons)
    a('<div class="summary">')
    a('<div class="panel stat"><b>%d</b><span>lessons planned</span></div>' % len(lessons))
    a('<div class="panel stat"><b>%d</b><span>lessons written</span></div>' % n_done)
    a('<div class="panel stat"><b>%d</b><span>problems assigned</span></div>' % n_picked)
    a('<div class="panel stat"><b>%d</b><span>in the catalogue</span></div>' % len(_rows))
    a('<div class="panel stat" id="solvedStat"><b>0</b><span>problems solved</span></div>')
    a('</div>')

    # ---- tracks
    for tr in SYL["tracks"]:
        a('<section class="track">')
        a('<h2>%s</h2>' % html.escape(tr["title"]))
        a('<p>%s</p>' % html.escape(tr["blurb"]))
        a('<div class="grid">')
        for l in tr["lessons"]:
            slug = l["slug"]
            is_built = built(slug)
            picked = picked_for(slug)
            pool = pool_for(l.get("filters"))
            legacy = ' data-legacy="str_done"' if slug == "03_Strings" else ""
            a('<article class="panel card" data-slug="%s" data-picked="%d"%s>'
              % (html.escape(slug), picked, legacy))
            a('<div class="hd"><span class="num">%s</span>' % html.escape(l["num"]))
            if is_built:
                a('<h3><a href="%s/%s.html">%s</a></h3>' % (slug, slug, html.escape(l["title"])))
                a('<span class="badge done">written</span>')
            else:
                a('<h3>%s</h3>' % html.escape(l["title"]))
                a('<span class="badge plan">planned</span>')
            a('</div>')
            a('<p class="sm">%s</p>' % html.escape(l["summary"]))
            covers = l.get("covers", [])
            if covers:
                a('<ul class="covers">')
                for c in covers[:6]:
                    a('<li>%s</li>' % html.escape(c))
                if len(covers) > 6:
                    a('<li class="more">+%d more</li>' % (len(covers) - 6))
                a('</ul>')
            a('<div class="foot">')
            if picked:
                a('<span class="plabel">0/%d solved</span>' % picked)
                a('<span class="prog"><i></i></span>')
            elif pool:
                lab = filter_label(l.get("filters"))
                a('<span class="pool" title="%s">%d candidate problems</span>'
                  % (html.escape(lab), pool["n"]))
            a('</div>')
            a('</article>')
        a('</div></section>')

    a('<footer>%s Built from <code>syllabus.json</code> by <code>tools/build_site.py</code>. '
      'Problem statements live on arena.olimpiici.com and are in Bulgarian.</footer>'
      % html.escape(cat["note"]))
    a('</div>')
    a('<script>%s</script>' % JS)
    a('</body></html>')

    out = ROOT / "index.html"
    out.write_text('\n'.join(P), encoding="utf-8")
    print("index.html  ->", out, out.stat().st_size, "bytes")
    mdp = write_markdown()
    print("SYLLABUS.md ->", mdp, mdp.stat().st_size, "bytes")
    print("%d lessons, %d written, %d problems assigned" % (len(lessons), n_done, n_picked))
    for tr in SYL["tracks"]:
        for l in tr["lessons"]:
            p = pool_for(l.get("filters"))
            if p is not None and p["n"] < 12 and not picked_for(l["slug"]):
                print("  thin pool: %s %-42s %d candidates"
                      % (l["num"], l["title"][:42], p["n"]))


if __name__ == "__main__":
    main()

"""Draw the profile's figures from real results, one light and one dark SVG each.

Every mark is data copied from a committed run file, named in SOURCES. When the
source repos sit next to this one, the script re-reads them and refuses to draw
if a value has drifted. Each figure animates once, in the order its data was
measured, ends within LIMIT seconds, and rests on its final frame: base styles
are the final frame and prefers-reduced-motion shows it at once (WCAG 2.2.2).

    python3 profile/draw_art.py
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).parent
OUT = HERE / "assets"
REPOS = HERE.parent.parent  # sibling checkouts, used only to verify the data
LIMIT = 4.0
FONT = "'Iowan Old Style','Palatino Linotype',Palatino,'Book Antiqua',Georgia,serif"
PALETTES = {  # ink, muted and rule follow GitHub's own text and border colors
    "light": dict(ink="#1F2328", muted="#59636E", rule="#D1D9E0", held="#1B4D8F", broke="#B3261E"),
    "dark": dict(ink="#F0F6FC", muted="#9198A1", rule="#3D444D", held="#8AB4F8", broke="#F28B82"),
}

# loophole: "top 3" queries that lose their order, per 20 training steps (order_losing, limit3_queries)
LOOPHOLE = {
    ("leaky", 0, "20261023T000232Z"): [(13, 24), (72, 72), (32, 32), (48, 48), (24, 24)],
    ("leaky", 1, "20261023T212956Z"): [(40, 54), (55, 56), (8, 8), (24, 24), (31, 32)],
    ("leaky", 2, "20261023T233103Z"): [(9, 56), (61, 64), (16, 32), (0, 64), (0, 40)],
    ("honest", 0, "20261023T010137Z"): [(10, 24), (0, 72), (0, 32), (0, 48), (0, 24)],
    ("honest", 1, "20261023T202818Z"): [(15, 54), (1, 56), (0, 8), (0, 24), (0, 32)],
    ("honest", 2, "20261023T222727Z"): [(2, 55), (1, 64), (0, 32), (0, 64), (0, 40)],
}
# beir-replication: DPR on SciFact, nDCG@10 by document max length
BEIR_PUBLISHED = 0.318
BEIR = {"sep_token": {100: 0.2756, 256: 0.2977, 350: 0.3147, 512: 0.3178},
        "space": {100: 0.2602, 256: 0.2873, 350: 0.3019, 512: 0.3096}}
# live quakes, Oct 8 2026: b, 95% bootstrap interval
QUAKES = [("California", 0.727, 0.661, 0.851), ("Alaska", 0.717, 0.609, 0.843),
          ("Global M4.5+", 1.496, 1.156, 2.041), ("All regions pooled", 0.343, 0.317, 0.403)]
# afterlife: ten most cited after retraction, headline group (journal read from the DOI)
AFTERLIFE = [("eLife", "10.7554/elife.12248", 2018, 191, 1031),
             ("ACS Nano", "10.1021/nn900887m", 2012, 39, 1013),
             ("J Hum Reprod Sci", "10.4103/0974-1208.82352", 2017, 207, 859),
             ("NEJM", "10.1056/nejmoa2007621", 2020, 645, 783),
             ("Hindawi", "10.1155/2014/943162", 2019, 1188, 699),
             ("Acad Manage J", "10.5465/amj.2009.43670902", 2013, 171, 684),
             ("Plant J", "10.1046/j.1365-313x.2003.01676.x", 2015, 563, 628),
             ("JAMA Intern Med", "10.1001/jamainternmed.2018.3713", 2020, 373, 611),
             ("Lancet", "10.1016/s0140-6736(20)31180-6", 2020, 632, 569),
             ("Hindawi", "10.1155/2014/150845", 2020, 682, 438)]


def verify():
    """Re-read every value from its source run when the repo is checked out beside this one."""
    checked = []
    for (arm, seed, run), rows in LOOPHOLE.items():
        for f in (REPOS / "loophole" / "runs").glob(run + "-grpo-sqlquest-%s-*/sql_shape.json" % arm):
            got = [(w["order_losing"], w["limit3_queries"]) for w in json.loads(f.read_text())["windows"]]
            assert got == rows, (run, got)
            checked.append("loophole " + run)
    for variant, by_len in BEIR.items():
        for n, v in by_len.items():
            f = REPOS / "beir-replication" / "runs" / ("dpr-ablation-scifact-len%d" % n) / "report.json"
            if f.exists():
                d = json.loads(f.read_text())
                assert round(d["variants"][variant]["ndcg@10"], 4) == v and d["published_ndcg@10"] == BEIR_PUBLISHED, (variant, n)
                checked.append("beir %s %d" % (variant, n))
    f = REPOS / "tanaypratapsingh.github.io" / "live" / "runs" / "2026-10-08-quakes-run.txt"
    if f.exists():
        text = f.read_text()
        for name, b, lo, hi in QUAKES:
            region = "All events" if name == "All regions pooled" else name
            m = re.search(r"\[%s\][^\[]*?b = ([\d.]+).*?95%% bootstrap \[([\d.]+), ([\d.]+)\]" % re.escape(region), text, re.S)
            assert m and tuple(map(float, m.groups())) == (b, lo, hi), name
            checked.append("quakes " + name)
    f = REPOS / "afterlife" / "runs" / "20261029T201514Z-findings.json"
    if f.exists():
        top = json.loads(f.read_text())["report"]["afterlife"]["top_by_citations_after"]
        got = [(r["paper_key"], r["retraction_year"], r["citations_through_retraction_year"], r["citations_after"]) for r in top]
        assert got == [("doi:" + doi, y, a, b) for _, doi, y, a, b in AFTERLIFE], got
        checked.append("afterlife top 10")
    return checked


class Fig:
    def __init__(self, w, h, c):
        self.w, self.h, self.c, self.parts, self.frames, self.end = w, h, c, [], [], 0.0

    def anim(self, name, dur, delay=0.0, ease="ease-out"):
        self.end = max(self.end, dur + delay)
        return "animation:%s %.2fs %s %.2fs both" % (name, dur, ease, delay)

    def add(self, tpl, **kw):
        self.parts.append(tpl.format(**dict(self.c, **kw)))

    def text(self, x, y, s, size=17, anchor="start", fill="muted", italic=False, style=""):
        self.parts.append('<text x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" fill="%s"%s style="%s">%s</text>'
                          % (x, y, size, anchor, self.c[fill], ' font-style="italic"' if italic else "", style, s))

    def svg(self):
        assert self.end <= LIMIT, "animation runs %.2fs, over the %.1fs limit" % (self.end, LIMIT)
        css = ("text{font-family:%s}"
               "@keyframes draw{from{stroke-dashoffset:1}}@keyframes fade{from{opacity:0}}"
               "@keyframes fadeout{from{opacity:1}}%s"
               "@media (prefers-reduced-motion:reduce){*{animation:none!important}}" % (FONT, "".join(self.frames)))
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">\n<style>%s</style>\n%s\n</svg>\n'
                % (self.w, self.h, css, "\n".join(self.parts)))


def masthead(c):
    """Fig. 1: train on a grader with a gap and the policy finds it."""
    f = Fig(960, 330, c)
    x0, x1, top, bot, run = 96, 744, 52, 262, 2.8
    X = lambda step: x0 + (x1 - x0) * step / 100
    Y = lambda share: bot - (bot - top) * share
    f.text(x0, 24, "share of “top 3” queries that lose their order, per 20 training steps", italic=True)
    for v in (0, 0.5, 1):
        f.add('<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" stroke="{rule}" stroke-width="1"/>', x0=x0, x1=x1, y=Y(v))
        f.text(x0 - 12, Y(v) + 6, "%d%%" % (v * 100), anchor="end")
    for s in range(0, 101, 20):
        f.text(X(s), bot + 28, str(s), anchor="middle")
    f.text((x0 + x1) / 2, bot + 58, "training step", italic=True, anchor="middle")
    # steps 20 to 39: every leaky run takes the query up
    f.add('<rect x="{a:.1f}" y="{t}" width="{w:.1f}" height="{h}" fill="{broke}" opacity="0.08" style="{s}"/>',
          a=X(20), t=top, w=X(40) - X(20), h=bot - top, s=f.anim("fade", 0.4, 0.3 + run * 0.2))
    f.frames.append("@keyframes reveal{from{transform:scaleX(0)}}")
    f.add('<clipPath id="r"><rect x="{x0}" y="0" width="{w}" height="330" style="transform-origin:{x0}px 0;{s}"/></clipPath>',
          x0=x0 - 6, w=x1 - x0 + 12, s=f.anim("reveal", run, 0.3, "linear"))
    lines = []
    for (arm, seed, _), rows in sorted(LOOPHOLE.items(), key=lambda kv: kv[0][0] == "leaky"):
        pts = [(X(10 + 20 * i), Y(k / n)) for i, (k, n) in enumerate(rows)]
        color = c["broke"] if arm == "leaky" else c["held"]
        lines.append('<path d="M%s" fill="none" stroke="%s" stroke-width="2.25" stroke-linejoin="round" opacity="0.85"/>%s'
                     % (" L".join("%.1f %.1f" % p for p in pts), color,
                        "".join('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (x, y, color) for x, y in pts)))
    f.add('<g clip-path="url(#r)">%s</g>' % "".join(lines))
    f.frames.append("@keyframes scan{from{transform:translateX(0)}}")
    sweep = f.anim("scan", run, 0.3, "linear") + "," + f.anim("fadeout", 0.3, 0.3 + run)[len("animation:"):]
    f.add('<line x1="{x}" x2="{x}" y1="{t}" y2="{b}" stroke="{ink}" stroke-width="1" style="opacity:0;transform:translateX({d}px);{s}"/>',
          x=x0, d=x1 - x0, t=top - 8, b=bot + 6, s=sweep)
    late = f.anim("fade", 0.4, 0.3 + run)
    f.text(x1 + 14, Y(0.98) + 6, "leaky grader", fill="broke", style=late)
    f.text(x1 + 14, Y(0) + 6, "honest grader", fill="held", style=late)
    f.text(X(70), Y(0.30), "seed 2 lets it go", fill="broke", italic=True, anchor="middle", style=late)
    return f


def replications(c):
    """Fig. 2: the one BEIR miss closes as the encoder's truncation is lifted."""
    f = Fig(960, 300, c)
    x0, x1, top, bot, lo, hi = 96, 700, 44, 236, 0.25, 0.33
    X = lambda n: x0 + (x1 - x0) * (n - 100) / 412
    Y = lambda v: bot - (bot - top) * (v - lo) / (hi - lo)
    f.text(x0, 22, "DPR on SciFact, nDCG@10", italic=True)
    for v in (0.26, 0.28, 0.30):
        f.add('<line x1="{a}" x2="{b}" y1="{y:.1f}" y2="{y:.1f}" stroke="{rule}"/>', a=x0, b=x1, y=Y(v))
        f.text(x0 - 12, Y(v) + 6, "%.2f" % v, anchor="end")
    for n in (100, 256, 350, 512):
        f.text(X(n), bot + 28, str(n), anchor="middle")
    f.text(X(100), bot + 50, "default", italic=True, anchor="middle")
    f.text((x0 + x1) / 2, bot + 50, "document max length, tokens", italic=True, anchor="middle")
    f.add('<line x1="{a}" x2="{b}" y1="{y:.1f}" y2="{y:.1f}" stroke="{ink}" stroke-width="1.25" stroke-dasharray="5 5"/>',
          a=x0, b=x1, y=Y(BEIR_PUBLISHED))
    f.text(x0 + 4, Y(BEIR_PUBLISHED) - 10, "published 0.318", fill="ink")
    # the miss at the shipped default
    gap = f.anim("fade", 0.4, 0.2)
    f.add('<line x1="{x:.1f}" x2="{x:.1f}" y1="{a:.1f}" y2="{b:.1f}" stroke="{broke}" stroke-width="2.5" style="{s}"/>',
          x=X(100), a=Y(BEIR["sep_token"][100]), b=Y(BEIR_PUBLISHED), s=gap)
    f.text(X(100) + 12, Y((BEIR["sep_token"][100] + BEIR_PUBLISHED) / 2) - 4, "the miss", fill="broke", italic=True, style=gap)
    for variant, color, label in (("space", "muted", "title + text"), ("sep_token", "held", "title [SEP] text")):
        pts = sorted(BEIR[variant].items())
        f.add('<path d="M%s" fill="none" stroke="{%s}" stroke-width="2.25" pathLength="1" stroke-dasharray="1" style="{s}"/>'
              % (" L".join("%.1f %.1f" % (X(n), Y(v)) for n, v in pts), color), s=f.anim("draw", 1.8, 0.6, "ease-in-out"))
        for i, (n, v) in enumerate(pts):
            f.add('<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{%s}" style="{s}"/>' % color,
                  x=X(n), y=Y(v), s=f.anim("fade", 0.2, 0.6 + 1.8 * (n - 100) / 412))
    late = f.anim("fade", 0.3, 2.4)
    f.text(x1 + 14, Y(BEIR["sep_token"][512]) + 6, "title [SEP] text", fill="held", style=late)
    f.text(x1 + 14, Y(BEIR["space"][512]) + 14, "title + text", fill="muted", style=late)
    return f


def live(c):
    """Fig. 3: regional b-values; pooling everything yields an artifact."""
    f = Fig(960, 290, c)
    x0, x1, lo, hi = 300, 900, 0.2, 2.2
    X = lambda b: x0 + (x1 - x0) * (b - lo) / (hi - lo)
    rows = [60 + 48 * i for i in range(len(QUAKES))]
    f.text(x0, 18, "Gutenberg-Richter b, 95% bootstrap interval", italic=True)
    f.add('<line x1="{x:.1f}" x2="{x:.1f}" y1="30" y2="{b}" stroke="{muted}" stroke-dasharray="5 5"/>', x=X(1), b=rows[-1] + 22)
    for v in (0.5, 1.0, 1.5, 2.0):
        f.text(X(v), rows[-1] + 50, "%.1f" % v, anchor="middle")
    for i, ((name, b, a, z), y) in enumerate(zip(QUAKES, rows)):
        color = "broke" if name.startswith("All") else "held"
        t = 0.3 + 0.25 * i
        f.text(x0 - 24, y + 6, name, anchor="end", fill="ink")
        for end in (a, z):  # each half of the interval grows out from the estimate
            f.add('<path d="M{p:.1f} {y}H{e:.1f}" stroke="{%s}" stroke-width="2.5" pathLength="1" stroke-dasharray="1" style="{s}"/>'
                  % color, p=X(b), e=X(end), y=y, s=f.anim("draw", 0.9, t + 0.2))
        f.add('<circle cx="{x:.1f}" cy="{y}" r="6" fill="{%s}" style="{s}"/>' % color, x=X(b), y=y, s=f.anim("fade", 0.3, t))
        f.text(X(b), y - 13, "%.2f" % b, fill=color, anchor="middle", style=f.anim("fade", 0.3, t + 1.0))
    return f


def systems(c):
    """Fig. 4: retraction did not stop the citations."""
    f = Fig(960, 400, c)
    x0, x1, top, step = 250, 900, 64, 29
    X = lambda n: x0 + (x1 - x0) * n / 1200
    f.add('<circle cx="{x}" cy="18" r="5" fill="none" stroke="{muted}" stroke-width="1.5"/>', x=x0 + 6)
    f.text(x0 + 18, 24, "citations through the retraction year", italic=True)
    f.add('<circle cx="{x}" cy="18" r="5" fill="{broke}"/>', x=x0 + 336)
    f.text(x0 + 348, 24, "citations after it", italic=True)
    bottom = top + step * (len(AFTERLIFE) - 1) + 20
    for v in range(0, 1201, 300):
        f.add('<line x1="{x:.1f}" x2="{x:.1f}" y1="{t}" y2="{b}" stroke="{rule}"/>', x=X(v), t=top - 16, b=bottom)
        f.text(X(v), bottom + 26, "{:,}".format(v), anchor="middle")
    for i, (journal, _, year, before, after) in enumerate(AFTERLIFE):
        y, t = top + step * i, 0.3 + 0.12 * i
        f.text(x0 - 20, y + 6, "%s, %d" % (journal, year), anchor="end", fill="ink")
        f.add('<path d="M{a:.1f} {y}H{b:.1f}" stroke="{muted}" stroke-width="1.5" pathLength="1" stroke-dasharray="1" style="{s}"/>',
              a=X(before), b=X(after), y=y, s=f.anim("draw", 1.0, t + 0.2))
        f.add('<circle cx="{x:.1f}" cy="{y}" r="5" fill="none" stroke="{muted}" stroke-width="1.5"/>', x=X(before), y=y)
        f.frames.append("@keyframes m%d{from{transform:translateX(%.1fpx)}}" % (i, X(before) - X(after)))
        f.add('<circle cx="{x:.1f}" cy="{y}" r="5" fill="{broke}" style="{s}"/>', x=X(after), y=y, s=f.anim("m%d" % i, 1.0, t + 0.2))
    return f


if __name__ == "__main__":
    print("verified against sources:", len(verify()), "values")
    OUT.mkdir(exist_ok=True)
    for draw in (masthead, replications, live, systems):
        for theme, c in PALETTES.items():
            fig = draw(c)
            path = OUT / ("%s-%s.svg" % (draw.__name__, theme))
            path.write_text(fig.svg(), encoding="utf-8")
            print("%-24s %4.2fs %6d bytes" % (path.name, fig.end, path.stat().st_size))

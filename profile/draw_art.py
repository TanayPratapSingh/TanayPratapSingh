"""Draw the profile's animated SVGs, one light and one dark file each.

Every animation plays once, finishes within LIMIT seconds, and comes to rest on
a still frame, so nothing keeps moving beside the text (WCAG 2.2.2). The base
style of every element is its final frame: keyframes give only the starting
state, and prefers-reduced-motion removes the animation and shows that frame.

    python3 profile/draw_art.py
"""
import math, pathlib, random

OUT = pathlib.Path(__file__).parent / "assets"
LIMIT = 4.5
PALETTES = {
    "light": dict(bg="#F2F0EA", edge="#DCD8D0", ink="#15171B", rule="#B9B4A9",
                  faint="#646A73", met="#1B4D8F", missed="#B3261E"),
    "dark": dict(bg="#15171B", edge="#2A2E35", ink="#ECE9E1", rule="#4A4F57",
                 faint="#8B919A", met="#8AB4F8", missed="#F28B82"),
}
KEYFRAMES = """
@keyframes draw{{from{{stroke-dashoffset:1}}}}
@keyframes fade{{from{{opacity:0}}}}
@keyframes fadeout{{from{{opacity:1}}}}
@keyframes scan{{from{{transform:translateX(0)}}}}
@keyframes drop{{from{{transform:translateY(-26px);opacity:0}}}}
@keyframes flow{{from{{transform:translateX(-240px);opacity:0}}}}
@keyframes travel{{from{{transform:translateX(-774px)}}}}
@keyframes lit{{from{{stroke:{faint}}}}}
@keyframes pulse{{0%{{transform:scale(.4);opacity:0}}1%{{opacity:.9}}100%{{transform:scale(2.6);opacity:0}}}}
.pulse{{transform-box:fill-box;transform-origin:center;opacity:0}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}"""


class Art:
    def __init__(self, w, h, c):
        self.w, self.h, self.c, self.parts, self.end = w, h, c, [], 0.0

    def anim(self, name, dur, delay=0.0, ease="ease-out"):
        self.end = max(self.end, dur + delay)
        return "animation:%s %.2fs %s %.2fs both" % (name, dur, ease, delay)

    def add(self, s):
        self.parts.append(s)

    def svg(self):
        assert self.end <= LIMIT, "animation runs %.2fs, over the %.1fs limit" % (self.end, LIMIT)
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">\n<style>%s\n</style>\n%s\n</svg>\n'
                % (self.w, self.h, KEYFRAMES.format(**self.c), "\n".join(self.parts)))


def masthead(c):
    """An instrument trace: the measured line tracks the expected one, then breaks away."""
    a = Art(960, 200, c)
    x0, x1, xb, scan = 64, 896, 640, 3.0
    ideal = lambda x: 148 - (x - x0) * 104 / (x1 - x0)
    pts = []
    for i, x in enumerate(range(x0, x1 + 1, 16)):
        jitter = 0 if x == xb else 2.6 * math.sin(i * 1.7) + 1.6 * math.sin(i * 0.63 + 1)
        gap = 58 * ((x - xb) / (x1 - xb)) ** 1.6 if x > xb else 0
        pts.append((x, ideal(x) + jitter + gap))
    yb = ideal(xb)
    a.add('<rect x="0.5" y="0.5" width="959" height="199" rx="4" fill="%(bg)s"/>' % c)
    # under the cover, revealed by the scan
    a.add('<path d="M%s" fill="none" stroke="%s" stroke-width="2.25" stroke-linejoin="round" stroke-linecap="round"/>'
          % (" L".join("%d %.1f" % p for p in pts), c["met"]))
    a.add('<g stroke="%s" stroke-width="1">%s</g>' % (c["faint"], "".join(
        '<line x1="%d" y1="170" x2="%d" y2="176"/>' % (x, x) for x, _ in pts if x != xb)))
    a.add('<g stroke="%(missed)s" fill="none"><line x1="%(x)d" y1="%(y)d" x2="%(x)d" y2="178" stroke-dasharray="2 3"/>'
          '<circle cx="%(x)d" cy="%(yb).1f" r="9" stroke-width="1.25"/><circle cx="%(x)d" cy="%(yb).1f" r="3.5" fill="%(missed)s"/></g>'
          % dict(c, x=xb, y=yb + 12, yb=yb))
    # the cover and cursor sweep right; at rest they sit past the plot
    a.add('<g style="transform:translateX(840px);%s"><rect x="62" y="26" width="900" height="158" fill="%s"/>'
          '<g style="opacity:0;%s" stroke="%s"><line x1="64" y1="28" x2="64" y2="182"/><circle cx="64" cy="28" r="2.5" fill="%s"/></g></g>'
          % (a.anim("scan", scan, 0.4, "linear"), c["bg"], a.anim("fadeout", 0.5, 0.4 + scan), c["ink"], c["ink"]))
    a.add('<g style="%s" fill="none" stroke-width="1"><g stroke="%s" stroke-dasharray="1 5">%s</g>'
          '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-dasharray="4 6" stroke-width="1.25"/>'
          '<path stroke="%s" d="M52 34v-10h10M898 24h10v10M908 158v10h-10M62 168h-10v-10"/></g>'
          % (a.anim("fade", 0.6), c["rule"], "".join('<line x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0, y, x1, y) for y in (66, 96, 126)),
             x0, ideal(x0), x1, ideal(x1), c["faint"], c["faint"]))
    a.add('<circle class="pulse" cx="%d" cy="%.1f" r="9" fill="none" stroke="%s" stroke-width="1.25" style="%s"/>'
          % (xb, yb, c["missed"], a.anim("pulse", 0.9, 0.4 + scan * (xb - x0) / 840)))
    a.add('<rect x="0.5" y="0.5" width="959" height="199" rx="4" fill="none" stroke="%(edge)s"/>' % c)
    return a


def replications(c):
    """Results drop into the cells of a published table; one lands off center."""
    a = Art(960, 64, c)
    off = 16
    for i in range(24):
        x = 48 + 36 * i
        miss = i == off
        a.add('<rect x="%d" y="26" width="18" height="18" fill="none" stroke="%s" style="%s"/>'
              % (x, c["missed"] if miss else c["faint"], a.anim("lit", 0.3, 0.65 + 0.07 * i) if miss else ""))
        a.add('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" style="%s"/>'
              % (x + 9 + (6 if miss else 0), 35 - (4 if miss else 0), c["missed"] if miss else c["met"],
                 a.anim("drop", 0.45, 0.2 + 0.07 * i, "cubic-bezier(.3,1.5,.5,1)")))
    return a


def live(c):
    """A stream of events flows in and holds, like a frozen frame of a live feed."""
    a = Art(960, 64, c)
    rnd = random.Random(11)
    lanes = (14, 26, 38, 50)
    a.add('<g stroke="%s" stroke-dasharray="1 6">%s</g>' % (c["rule"], "".join(
        '<line x1="16" y1="%d" x2="944" y2="%d"/>' % (y, y) for y in lanes)))
    for _ in range(72):
        x, y = rnd.uniform(24, 936), rnd.choice(lanes)
        style = a.anim("flow", rnd.uniform(1.1, 2.0), rnd.uniform(0, 1.4), "cubic-bezier(.2,.7,.3,1)")
        if rnd.random() < 0.08:
            a.add('<circle cx="%.1f" cy="%d" r="4.5" fill="none" stroke="%s" style="%s"/>' % (x, y, c["met"], style))
        else:
            a.add('<circle cx="%.1f" cy="%d" r="%.1f" fill="%s" style="%s"/>'
                  % (x, y, rnd.choice((2, 2.5, 3.2)), c["met"] if rnd.random() < 0.6 else c["faint"], style))
    return a


def agents(c):
    """A token passes four review gates and is stopped at the fifth."""
    a = Art(960, 64, c)
    x0, xf, travel = 40, 814, 2.8
    gates = (200, 360, 520, 680, 840)
    a.add('<line x1="%d" y1="32" x2="920" y2="32" stroke="%s"/>' % (x0, c["rule"]))
    a.add('<path d="M%d 32H%d" stroke="%s" stroke-width="2" pathLength="1" stroke-dasharray="1" style="%s"/>'
          % (x0, xf, c["met"], a.anim("draw", travel, 0.3, "linear")))
    for i, g in enumerate(gates):
        last = i == len(gates) - 1
        t = 0.3 + travel * min(1, (g - 8 - x0) / (xf - x0))
        a.add('<line x1="%d" y1="18" x2="%d" y2="46" stroke="%s" stroke-width="2.5" stroke-linecap="round" style="%s"/>'
              % (g, g, c["missed"] if last else c["met"], a.anim("lit", 0.25, t)))
    a.add('<circle cx="%d" cy="32" r="6" fill="%s" style="%s"/>' % (xf, c["ink"], a.anim("travel", travel, 0.3, "linear")))
    a.add('<circle class="pulse" cx="%d" cy="32" r="7" fill="none" stroke="%s" stroke-width="1.25" style="%s"/>'
          % (xf, c["missed"], a.anim("pulse", 0.9, 0.3 + travel)))
    return a


def systems(c):
    """Four sources merge into one trunk; one stays apart."""
    a = Art(960, 64, c)
    draw = 'fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" pathLength="1" stroke-dasharray="1" style="%s"'
    for y in (10, 24, 40):
        a.add('<path d="M40 %d C280 %d 360 32 520 32" %s/>' % (y, y, draw % (c["met"], 1.5, a.anim("draw", 1.6, 0.2, "ease-in-out"))))
    a.add('<path d="M40 54 C280 54 380 50 600 50" %s/>' % (draw % (c["faint"], 1.5, a.anim("draw", 1.6, 0.2, "ease-in-out"))))
    a.add('<path d="M520 32H920" %s/>' % (draw % (c["met"], 2.25, a.anim("draw", 1.2, 1.8))))
    a.add('<circle cx="600" cy="50" r="3.5" fill="%s" style="%s"/>' % (c["missed"], a.anim("fade", 0.3, 1.8)))
    a.add('<circle class="pulse" cx="600" cy="50" r="7" fill="none" stroke="%s" stroke-width="1.25" style="%s"/>'
          % (c["missed"], a.anim("pulse", 0.9, 1.8)))
    return a


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for draw in (masthead, replications, live, agents, systems):
        for theme, c in PALETTES.items():
            art = draw(c)
            path = OUT / ("%s-%s.svg" % (draw.__name__, theme))
            path.write_text(art.svg(), encoding="utf-8")
            print("%-28s %5.2fs %6d bytes" % (path.name, art.end, path.stat().st_size))

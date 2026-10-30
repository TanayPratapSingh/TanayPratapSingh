"""Assemble README.md for the GitHub profile from profile/.

Sections are plain markdown files concatenated in filename order. The project
lists, one per theme, and the earlier list are generated from
profile/data/projects.json so a project is described in exactly one place.
"""
import html, io, json, pathlib, re

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / "README.md"
RAW = "https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/"
ALT = {  # each figure's data in words, for screen readers and broken images
    "masthead": "Line chart of six GRPO training runs. In the three trained on the leaky grader, the share of top 3 "
                "SQL queries that lose their order rises to between 95 and 100 percent in steps 20 to 39; two stay "
                "near 100 percent and one falls back to 0. In the three trained on the honest grader it falls to 0 by step 40.",
    "replications": "Line chart of DPR nDCG@10 on SciFact against document max length. Title [SEP] text rises from 0.276 "
                    "at the default 100 tokens to 0.318 at 512, matching the published 0.318; title + text rises from 0.260 to 0.310.",
    "live": "Forest plot of Gutenberg-Richter b-values with 95 percent bootstrap intervals: California 0.73 (0.66 to 0.85), "
            "Alaska 0.72 (0.61 to 0.84), global M4.5 and up 1.50 (1.16 to 2.04), all regions pooled 0.34 (0.32 to 0.40).",
    "systems": "Dot plot of the ten retracted papers cited most after retraction, citations through the retraction year "
               "against after it. eLife 2018: 191 then 1,031. ACS Nano 2012: 39 then 1,013. NEJM 2020: 645 then 783. "
               "Lancet 2020: 632 then 569.",
}

def read(p):
    return io.open(p, encoding="utf-8").read().rstrip()

def sections(folder):
    d = ROOT / folder
    if not d.exists():
        return []
    return [read(p) for p in sorted(d.iterdir()) if p.suffix == ".md"]

def projects(group):
    f = ROOT / "data" / "projects.json"
    rows = json.loads(read(f)) if f.exists() else []
    return [r for r in rows if r.get("group") == group]

def name(r):
    # link the name when the code is public; otherwise plain text
    return "[%s](%s)" % (r["name"], r["repo"]) if r.get("repo") else r["name"]

def work_list(group):
    # a description list, not a table: it reflows on phones and screen readers
    # announce each project as a term with its description
    out = ["<dl>"]
    for r in projects(group):
        n = html.escape(r["name"])
        link = r.get("live") or r.get("repo")
        out.append('<dt><a href="%s">%s</a></dt>' % (link, n) if link else "<dt>%s</dt>" % n)
        tail = "<i>%s</i>" % html.escape(r["stack"])
        if r.get("live"):
            tail += ' · <a href="%s">source for %s</a>' % (r["repo"], n)
        out.append("<dd>%s<br>%s</dd>" % (html.escape(r["result"]), tail))
    return "\n".join(out + ["</dl>"])

def earlier_list():
    return "\n".join("- **%s**, %s. %s" % (name(r), r["when"], r["result"]) for r in projects("earlier"))

def art(name):
    # GitHub serves the source matching its own theme
    return ('<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="%s%s-dark.svg">\n'
            '  <img src="%s%s-light.svg" width="100%%" alt="%s">\n</picture>'
            % (RAW, name, RAW, name, ALT[name]))

def build():
    text = "\n\n".join(sections("sections"))
    for group in ("replications", "live", "agents", "systems"):
        text = text.replace("<!--%s-->" % group.upper(), work_list(group))
    text = re.sub(r"<!--ART:(\w+)-->", lambda m: art(m.group(1)), text)
    text = text.replace("<!--EARLIER-->", earlier_list())
    text = text.replace("<!--STACK-->", "\n\n".join(sections("stack")))
    io.open(OUT, "w", encoding="utf-8").write(text.rstrip() + "\n")
    return len(text)

if __name__ == "__main__":
    print("wrote README.md:", build(), "chars")

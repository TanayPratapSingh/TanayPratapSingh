"""Assemble README.md for the GitHub profile from profile/.

Sections are plain markdown files concatenated in filename order. The project
lists, one per theme, and the earlier list are generated from
profile/data/projects.json so a project is described in exactly one place.
"""
import html, io, json, pathlib, re

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / "README.md"
RAW = "https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/"
ALT = {"masthead": "A measured line tracks its expected value, then breaks away from it at a point marked in red"}

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
    # GitHub serves the source matching its own theme; alt="" marks a strip as decorative
    return ('<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="%s%s-dark.svg">\n'
            '  <img src="%s%s-light.svg" width="100%%" alt="%s">\n</picture>'
            % (RAW, name, RAW, name, ALT.get(name, "")))

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

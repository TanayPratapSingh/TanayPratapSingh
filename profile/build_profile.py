"""Assemble README.md for the GitHub profile from profile/.

Sections are plain markdown files concatenated in filename order. The project
table and the earlier list are generated from profile/data/projects.json so a
project is described in exactly one place.
"""
import io, json, pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / "README.md"

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

def work_table():
    out = ["| Project | What it does and what it found | Stack |", "|---|---|---|"]
    for r in projects("recent"):
        out.append("| %s | %s | %s |" % (name(r), r["result"], r.get("stack", "")))
    return "\n".join(out)

def earlier_list():
    return "\n".join("- **%s**, %s. %s" % (name(r), r["when"], r["result"]) for r in projects("earlier"))

def build():
    text = "\n\n".join(sections("sections"))
    text = text.replace("<!--WORK-->", work_table())
    text = text.replace("<!--EARLIER-->", earlier_list())
    text = text.replace("<!--STACK-->", "\n\n".join(sections("stack")))
    io.open(OUT, "w", encoding="utf-8").write(text.rstrip() + "\n")
    return len(text)

if __name__ == "__main__":
    print("wrote README.md:", build(), "chars")

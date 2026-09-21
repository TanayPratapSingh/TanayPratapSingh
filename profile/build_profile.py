"""Assemble README.md for the GitHub profile from profile/.

Sections are plain markdown files concatenated in filename order. The selected
work table is generated from profile/data/projects.json so a project is
described in exactly one place.
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

def work_table():
    f = ROOT / "data" / "projects.json"
    if not f.exists():
        return ""
    rows = json.loads(read(f))
    out = ["| Project | Result | Stack | Code |", "|---|---|---|---|"]
    for r in rows:
        code = "[repo](%s)" % r["repo"] if r.get("repo") else "—"
        out.append("| %s | %s | %s | %s |" % (r["name"], r["result"], r["stack"], code))
    return "\n".join(out)

def build():
    body = sections("sections")
    text = "\n\n".join(body)
    text = text.replace("<!--WORK-->", work_table())
    text = text.replace("<!--STACK-->", "\n\n".join(sections("stack")))
    io.open(OUT, "w", encoding="utf-8").write(text.rstrip() + "\n")
    return len(text)

if __name__ == "__main__":
    print("wrote README.md:", build(), "chars")

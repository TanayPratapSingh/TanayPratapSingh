# profile/

Source for the profile `README.md` at the repository root. Do not edit that
file directly; it is generated.

```
profile/
  sections/   page sections, concatenated in filename order
  stack/      one file per stack group, injected at <!--STACK-->
  data/       projects.json: each row's "group" (replications, live, agents,
              systems) renders as a description list at <!--REPLICATIONS-->,
              <!--LIVE-->, and so on; "earlier" rows as the list at <!--EARLIER-->
  assets/     the figures, a light and a dark SVG each, placed at
              <!--ART:name--> and chosen by GitHub's theme through <picture>.
              Drawn by draw_art.py from values copied out of each project's
              run files, which it re-checks against those files when the
              repos are checked out beside this one. Edit that, not the SVGs
```

## Rebuilding

```bash
python3 profile/draw_art.py      # only after changing a figure
python3 profile/build_profile.py
```

## Why generated

The project lists repeat figures that also appear on the portfolio and
in each project's own README. Keeping the numbers in one JSON file means a
correction lands in one place rather than three, and the lists cannot drift out
of order with the data behind it.

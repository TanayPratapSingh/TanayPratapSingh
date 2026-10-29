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
  assets/     masthead-light.svg and masthead-dark.svg, chosen by GitHub's
              theme through <picture>. The dark file is the light one with
              the palette swapped; edit both together
```

## Rebuilding

```bash
python3 profile/build_profile.py
```

## Why generated

The project lists repeat figures that also appear on the portfolio and
in each project's own README. Keeping the numbers in one JSON file means a
correction lands in one place rather than three, and the lists cannot drift out
of order with the data behind it.

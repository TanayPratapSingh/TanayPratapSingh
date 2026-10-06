# profile/

Source for the profile `README.md` at the repository root. Do not edit that
file directly; it is generated.

```
profile/
  sections/   page sections, concatenated in filename order
  stack/      one file per stack group, injected at <!--STACK-->
  data/       projects.json: "recent" rows render as the table at <!--WORK-->,
              "earlier" rows as the list at <!--EARLIER-->
```

## Rebuilding

```bash
python3 profile/build_profile.py
```

## Why generated

The selected work table repeats figures that also appear on the portfolio and
in each project's own README. Keeping the numbers in one JSON file means a
correction lands in one place rather than three, and the table cannot drift out
of order with the data behind it.

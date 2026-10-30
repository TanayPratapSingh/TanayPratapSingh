## Replications

*Does a published result hold when I rerun it on hardware I can afford?*

<!--ART:replications-->

**Fig. 2.** The one BEIR result that missed, and why. DPR on SciFact scored 0.276
nDCG@10 against a published 0.318. Its document encoder silently truncates at
100 tokens; as the limit rises the gap closes, and at 512 tokens title [SEP]
text scores 0.318. Data: `runs/dpr-ablation-scifact-len*/report.json` in
[beir-replication](https://github.com/TanayPratapSingh/beir-replication/tree/main/runs).

<!--REPLICATIONS-->

## Live dashboards

*Public data feeds, processed live in the browser.*

<!--ART:live-->

**Fig. 3.** Gutenberg-Richter b-values from the past week of the USGS feed, as
computed live on October 8, 2026, with 95% bootstrap intervals. The dashed line
marks b = 1. Pooling every region gives 0.34, a number about mixing magnitude
scales and networks rather than about the Earth, and the dashboard says so
beside it. Data: [live/runs/2026-10-08-quakes-run.txt](https://github.com/TanayPratapSingh/tanaypratapsingh.github.io/blob/main/live/runs/2026-10-08-quakes-run.txt).

<!--LIVE-->

## Agents and evaluation

*Agents, the verifiers and review gates around them, and how to tell when they
fail. Fig. 1 at the top is from loophole.*

<!--AGENTS-->

## Data and ML systems

*Pipelines, warehouses, and training runs.*

<!--ART:systems-->

**Fig. 4.** Retraction did not stop the citations. The ten retracted papers cited
most after retraction, out of 54,737 whose whole post retraction period falls
inside OpenAlex's citation window: citations through the retraction year (open
circles) against citations after it (red). Across all 54,737, 60.0% were cited
after retraction. Journals are read from each DOI. Data: [afterlife
RESULTS.md](https://github.com/TanayPratapSingh/afterlife/blob/main/RESULTS.md), key `afterlife`.

<!--SYSTEMS-->

Full write ups, including what each one gets wrong, are on the
[portfolio](https://tanaypratapsingh.github.io).

## Earlier

<details>
<summary>Projects from 2024 and 2025</summary>

<!--EARLIER-->

</details>

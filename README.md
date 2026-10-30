<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/masthead-dark.svg">
  <img src="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/masthead-light.svg" width="100%" alt="Line chart of six GRPO training runs. In the three trained on the leaky grader, the share of top 3 SQL queries that lose their order rises to between 95 and 100 percent in steps 20 to 39; two stay near 100 percent and one falls back to 0. In the three trained on the honest grader it falls to 0 by step 40.">
</picture>

**Fig. 1.** Six GRPO runs on Qwen2.5 1.5B, 100 steps each: three trained on a
leaky SQL grader (red) and three on an honest one (blue). The leaky grader checks
that a "top 3" answer returns the right three products but not their order, so a
query that sorts inside a subquery and loses the order is paid like a correct
one. All three leaky runs took that query up in steps 20 to 39 (shaded), and seed
2 later let it go; under the honest grader it was gone by step 40. Data: each
run's `sql_shape.json`, tabled in [loophole's README](https://github.com/TanayPratapSingh/loophole#headline).

I build agent and retrieval systems and the data pipelines under them, then
measure where they break.

Syracuse, NY · [Portfolio](https://tanaypratapsingh.github.io) ·
[LinkedIn](https://www.linkedin.com/in/tanay-pratap-singh-8360681b0/) ·
[tanayyps@gmail.com](mailto:tanayyps@gmail.com)

**On this page:** [Now](#now) · [Replications](#replications) ·
[Live dashboards](#live-dashboards) · [Agents and evaluation](#agents-and-evaluation) ·
[Data and ML systems](#data-and-ml-systems) · [Earlier](#earlier) · [Tools](#tools)

## Now

- Finishing an MS in Applied Data Science at Syracuse University, December 2026.
- Research assistant on Gravity Spy 2.0, an NSF funded citizen science project
  that supports LIGO, since February 2026. I built the pipeline that parses
  276,000+ volunteer classifications across 25,104 glitch subjects and 8,293
  auxiliary channels, and trained a two input CNN on a shared MobileNetV2
  backbone: 0.89 validation AUC, with calibration error cut from 0.10 to 0.05.
- Open to AI, data, ML, and analytics roles.

## Replications

*Does a published result hold when I rerun it on hardware I can afford?*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/replications-dark.svg">
  <img src="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/replications-light.svg" width="100%" alt="Line chart of DPR nDCG@10 on SciFact against document max length. Title [SEP] text rises from 0.276 at the default 100 tokens to 0.318 at 512, matching the published 0.318; title + text rises from 0.260 to 0.310.">
</picture>

**Fig. 2.** The one BEIR result that missed, and why. DPR on SciFact scored 0.276
nDCG@10 against a published 0.318. Its document encoder silently truncates at
100 tokens; as the limit rises the gap closes, and at 512 tokens title [SEP]
text scores 0.318. Data: `runs/dpr-ablation-scifact-len*/report.json` in
[beir-replication](https://github.com/TanayPratapSingh/beir-replication/tree/main/runs).

<dl>
<dt><a href="https://github.com/TanayPratapSingh/drgrpo-replication">Replicating Dr. GRPO</a></dt>
<dd>RL post training on Qwen2.5-1.5B, GRPO against Dr. GRPO on the paper&#x27;s own setup. The accuracy claim held (51.6% vs 51.2% on MATH500). Both length claims came out reversed. One seed, 100 LoRA steps.<br><i>PyTorch, vLLM, LoRA, MLX</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/beir-replication">Replicating BEIR</a></dt>
<dd>Six published retrieval results reproduced, four exact to three decimals. The one that missed came from a silent 100 token truncation default in the DPR encoder.<br><i>BM25, sentence-transformers, pytrec_eval</i></dd>
</dl>

## Live dashboards

*Public data feeds, processed live in the browser.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/live-dark.svg">
  <img src="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/live-light.svg" width="100%" alt="Forest plot of Gutenberg-Richter b-values with 95 percent bootstrap intervals: California 0.73 (0.66 to 0.85), Alaska 0.72 (0.61 to 0.84), global M4.5 and up 1.50 (1.16 to 2.04), all regions pooled 0.34 (0.32 to 0.40).">
</picture>

**Fig. 3.** Gutenberg-Richter b-values from the past week of the USGS feed, as
computed live on October 8, 2026, with 95% bootstrap intervals. The dashed line
marks b = 1. Pooling every region gives 0.34, a number about mixing magnitude
scales and networks rather than about the Earth, and the dashboard says so
beside it. Data: [live/runs/2026-10-08-quakes-run.txt](https://github.com/TanayPratapSingh/tanaypratapsingh.github.io/blob/main/live/runs/2026-10-08-quakes-run.txt).

<dl>
<dt><a href="https://tanaypratapsingh.github.io/live/wiki.html">Wikipedia Edit Stream</a></dt>
<dd>Every Wikipedia edit, counted exactly and with HyperLogLog, Count-Min and Space-Saving sketches, so each sketch&#x27;s error shows against its bound. In a logged 297 second run, HyperLogLog estimated 986.9 distinct editors against 983 exact (+0.4%).<br><i>JavaScript, Server Sent Events, streaming sketches</i> · <a href="https://github.com/TanayPratapSingh/wikipedia-edit-stream">source for Wikipedia Edit Stream</a></dd>
<dt><a href="https://tanaypratapsingh.github.io/live/book.html">Order Book Microstructure</a></dt>
<dd>A live Kraken BTC/USD order book rebuilt in the browser and checked against the exchange&#x27;s CRC32 on every update: 46,892 of 46,892 checksums verified. Order flow imbalance fit the price move with R² 0.54 at 1 second.<br><i>JavaScript, WebSocket, CRC32, OLS</i> · <a href="https://github.com/TanayPratapSingh/orderbook-microstructure">source for Order Book Microstructure</a></dd>
<dt><a href="https://tanaypratapsingh.github.io/live/quakes.html">Live Earthquake Statistics</a></dt>
<dd>The past week of USGS earthquakes, refreshed every minute, with Gutenberg-Richter and Omori aftershock fits and a log of every catalog revision. California b = 0.73, likely range 0.66 to 0.85; 7 catalog revisions caught in 45 minutes.<br><i>JavaScript, maximum likelihood, bootstrap, d3-geo</i> · <a href="https://github.com/TanayPratapSingh/live-earthquake-statistics">source for Live Earthquake Statistics</a></dd>
<dt><a href="https://tanaypratapsingh.github.io/live/sun.html">Space Weather Nowcast</a></dt>
<dd>Live NOAA solar wind followed from L1 to Earth: 9 NOAA feeds joined on time, the L1 to Earth delay from the spacecraft ephemeris, Newell coupling, the Shue magnetopause, and the aurora over Syracuse.<br><i>JavaScript, time series joins, d3-geo</i> · <a href="https://github.com/TanayPratapSingh/space-weather-nowcast">source for Space Weather Nowcast</a></dd>
</dl>

## Agents and evaluation

*Agents, the verifiers and review gates around them, and how to tell when they
fail. Fig. 1 at the top is from loophole.*

<dl>
<dt><a href="https://github.com/TanayPratapSingh/loophole">loophole</a></dt>
<dd>RL environments where every task ships an honest verifier and a leaky one with a documented gap. GRPO on Qwen2.5 1.5B trained on the leaky SQL grader wrote the order losing query on 104 and 102 of 104 held out answers in 2 of 3 seeds, and on 0 when trained on the honest one.<br><i>Python, GRPO, TRL, vLLM, LoRA, DPO</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/Groundwork">Groundwork</a></dt>
<dd>RAG evaluation, guardrails, and an LLM gateway on SQuAD v2.0. recall@5 0.921, ECE 0.045, prompt injection recall 0.884 on an unseen attack corpus, 113 tests.<br><i>Python, BM25, FastAPI, Docker</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/tool-dependency-graph">Tool Dependency Graph</a></dt>
<dd>Works out which agent tools have to run before which, from nothing but their JSON Schemas. 1,391 tools, 46 typed entities, 3,278 edges, 8 of 8 hand written assertions passing.<br><i>TypeScript, Bun, JSON Schema</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/handoff">handoff</a></dt>
<dd>Supervisor orchestration where every escalation has a deadline and a declared outcome when nobody answers: ladder, safer substitute, drop, or freeze. 212 tests, no dependencies, simulated cluster, no LLM calls.<br><i>Python</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/comms-agent">comms-agent</a></dt>
<dd>A stateful agent with a human review gate inside its control flow. On the sample run it flags 9 of 24 mentions and the reviewer corrects 7. Synthetic corpus, mock model, simulated reviewer.<br><i>Python, state graph, tool calling</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/media-pulse">media-pulse</a></dt>
<dd>Media monitoring with confidence gated human review. Review lifts topic accuracy from 0.88 to 0.96 and sentiment from 0.50 to 0.85; ECE 0.156. Synthetic corpus about a fictional brand.<br><i>scikit-learn, VADER, Streamlit</i></dd>
<dt>Project Mark</dt>
<dd>Four families of analytics traps with deterministic golden solutions, built to stress test frontier models. The models solved the clean versions.<br><i>Python, pandas, statistics</i></dd>
</dl>

## Data and ML systems

*Pipelines, warehouses, and training runs.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/systems-dark.svg">
  <img src="https://raw.githubusercontent.com/TanayPratapSingh/TanayPratapSingh/main/profile/assets/systems-light.svg" width="100%" alt="Dot plot of the ten retracted papers cited most after retraction, citations through the retraction year against after it. eLife 2018: 191 then 1,031. ACS Nano 2012: 39 then 1,013. NEJM 2020: 645 then 783. Lancet 2020: 632 then 569.">
</picture>

**Fig. 4.** Retraction did not stop the citations. The ten retracted papers cited
most after retraction, out of 54,737 whose whole post retraction period falls
inside OpenAlex's citation window: citations through the retraction year (open
circles) against citations after it (red). Across all 54,737, 60.0% were cited
after retraction. Journals are read from each DOI. Data: [afterlife
RESULTS.md](https://github.com/TanayPratapSingh/afterlife/blob/main/RESULTS.md), key `afterlife`.

<dl>
<dt><a href="https://github.com/TanayPratapSingh/afterlife">afterlife</a></dt>
<dd>One retraction registry built from four public ones (Retraction Watch, OpenAlex, PubMed, PMC), measuring how badly they disagree. Of 89,706 papers flagged by at least one, all eligible registries agree on 66.1% and exactly one flags 25.1%. Deployed to AWS and Databricks.<br><i>PySpark, Delta Lake, Databricks, dbt, AWS Lambda, Terraform</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/distributed-vit-cifar10">Distributed ViT on CIFAR-10</a></dt>
<dd>Data parallel training on 2x T4, with gradient equivalence tested before any speed was measured. Scaling efficiency was 98% in fp32 and 57% in fp16; 24 measured runs traced the drop to the host&#x27;s 4 vCPUs.<br><i>PyTorch, DDP, FSDP</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/ztf-transient-pipeline">ZTF Transient Pipeline</a></dt>
<dd>Replays a real night of ZTF alerts (27,378 Avro packets) through Kafka. 500 were loaded, scored by a multimodal CNN, and rebuilt in a dbt warehouse with 8 models and 21 tests. Coarse labels; a systems project first.<br><i>Kafka, Avro, TensorFlow, dbt, DuckDB, Airflow</i></dd>
<dt>JMA Wireless</dt>
<dd>Led a four person Lean Six Sigma team at a maker of cell tower and 5G equipment. Flattened 31 GB of nested PLC JSON to under 5 MB for Power BI. About $355K a year in projected opportunity, pending JMA Finance confirmation.<br><i>pandas, Power BI, DMAIC</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/shopfloor-ai">ShopFloor AI</a></dt>
<dd>Predictive maintenance on the AI4I 2020 dataset (0.85 F1, 0.96 AUC), Kafka KPI streaming, and RAG over 6 bundled SOPs, run as a seven service Docker Compose stack.<br><i>scikit-learn, MLflow, Kafka, ChromaDB</i></dd>
<dt><a href="https://github.com/TanayPratapSingh/multi-horizon-aurora-kp-prediction">Kp Index Forecasting</a></dt>
<dd>LSTM forecasts of the geomagnetic Kp index from solar wind data. At 1 hour, RMSE 0.738, 45% better than a mean baseline, over 96,000+ hourly observations.<br><i>TensorFlow, LSTM</i></dd>
</dl>

Full write ups, including what each one gets wrong, are on the
[portfolio](https://tanaypratapsingh.github.io).

## Earlier

<details>
<summary>Projects from 2024 and 2025</summary>

- **[The Perfect Lap](https://github.com/TanayPratapSingh/the-perfect-lap)**, 2025. Predicts the first pit stop lap in Formula 1. MAE 2.78 laps on 250,000+ records, with a Streamlit app.
- **[July Energy Demand Under Warming](https://github.com/TanayPratapSingh/energy-usage-prediction)**, 2025. Models July residential demand: +25.4% peak hour load at +5°C, and 9.2% savings from a 1°C setpoint shift. Random Forest R² 0.48. R and Shiny.
- **Wealth Equals Health?**, 2025. Gapminder data across 180+ countries: how far income explains life expectancy, and whether education does more than income to reduce child mortality. ANOVA F = 426.5.
- **Travel Itinerary Management System**, 2025. A 12 entity normalized SQL schema where stored procedures and triggers enforce the business rules.
- **Uber Data Engineering Pipeline**, 2024. A GCP pipeline into a BigQuery star schema.
- **Digit Recognition from Scratch**, 2024. A neural network in NumPy with hand written backpropagation. 94% on MNIST.
- **Real Time Big Data Inflow**, 2024. A literature review of 12+ primary sources comparing cloud and tiered edge architectures across six dimensions. For suitably partitioned workloads the comparison puts the latency reduction at 40 to 60%.

</details>

## Tools

*Used in the projects above.*

**Languages:** Python, SQL, R, TypeScript, JavaScript

**Retrieval and LLM systems:** BM25, sentence-transformers, ChromaDB, RAG
evaluation, calibration (ECE), guardrails, prompt injection detection, agent
orchestration, tool calling

**Training and ML:** PyTorch, TensorFlow, Keras, scikit-learn, XGBoost,
CatBoost, SHAP, LoRA, vLLM, TRL, MLX

**Data and analytics:** pandas, Kafka, Avro, dbt, DuckDB, BigQuery, Airflow,
Power BI, Tableau, PySpark, Delta Lake, Databricks

**Serving and ops:** Docker, MLflow, FastAPI, GitHub Actions, Streamlit, Shiny, AWS Lambda, Terraform

Coursework also covered Spark, Hive, HDFS, ksqlDB, MapReduce, Neo4j, Redis, and
Cassandra.

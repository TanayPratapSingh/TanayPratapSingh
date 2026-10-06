# Tanay Pratap Singh

I build agent and retrieval systems and the data pipelines under them, then
measure where they break.

Syracuse, NY · [Portfolio](https://tanaypratapsingh.github.io) ·
[LinkedIn](https://www.linkedin.com/in/tanay-pratap-singh-8360681b0/) ·
[tanayyps@gmail.com](mailto:tanayyps@gmail.com)

## Now

- Finishing an MS in Applied Data Science at Syracuse University, December 2026.
- Research assistant on Gravity Spy 2.0, an NSF funded citizen science project
  that supports LIGO, since February 2026. I built the pipeline that parses
  276,000+ volunteer classifications across 25,104 glitch subjects and 8,293
  auxiliary channels, and trained a two input CNN on a shared MobileNetV2
  backbone: 0.89 validation AUC, with calibration error cut from 0.10 to 0.05.
- Open to AI, data, ML, and analytics roles.

## Projects, 2026

| Project | What it does and what it found | Stack |
|---|---|---|
| [Replicating Dr. GRPO](https://github.com/TanayPratapSingh/drgrpo-replication) | RL post training on Qwen2.5-1.5B, GRPO against Dr. GRPO on the paper's own setup. The accuracy claim held (51.6% vs 51.2% on MATH500). Both length claims came out reversed. One seed, 100 LoRA steps. | PyTorch, vLLM, LoRA, MLX |
| [Tool Dependency Graph](https://github.com/TanayPratapSingh/tool-dependency-graph) | Works out which agent tools have to run before which, from nothing but their JSON Schemas. 1,391 tools, 46 typed entities, 3,278 edges, 8 of 8 hand written assertions passing. | TypeScript, Bun, JSON Schema |
| [Distributed ViT on CIFAR-10](https://github.com/TanayPratapSingh/distributed-vit-cifar10) | Data parallel training on 2x T4, with gradient equivalence tested before any speed was measured. Scaling efficiency was 98% in fp32 and 57% in fp16; 24 measured runs traced the drop to the host's 4 vCPUs. | PyTorch, DDP, FSDP |
| [ZTF Transient Pipeline](https://github.com/TanayPratapSingh/ztf-transient-pipeline) | Replays a real night of ZTF alerts (27,378 Avro packets) through Kafka. 500 were loaded, scored by a multimodal CNN, and rebuilt in a dbt warehouse with 8 models and 21 tests. Coarse labels; a systems project first. | Kafka, Avro, TensorFlow, dbt, DuckDB, Airflow |
| [Groundwork](https://github.com/TanayPratapSingh/Groundwork) | RAG evaluation, guardrails, and an LLM gateway on SQuAD v2.0. recall@5 0.921, ECE 0.045, prompt injection recall 0.884 on an unseen attack corpus, 113 tests. | Python, BM25, FastAPI, Docker |
| [Replicating BEIR](https://github.com/TanayPratapSingh/beir-replication) | Six published retrieval results reproduced, four exact to three decimals. The one that missed came from a silent 100 token truncation default in the DPR encoder. | BM25, sentence-transformers, pytrec_eval |
| JMA Wireless | Led a four person Lean Six Sigma team at a maker of cell tower and 5G equipment. Flattened 31 GB of nested PLC JSON to under 5 MB for Power BI. About $355K a year in projected opportunity, pending JMA Finance confirmation. | pandas, Power BI, DMAIC |
| [ShopFloor AI](https://github.com/TanayPratapSingh/shopfloor-ai) | Predictive maintenance on the AI4I 2020 dataset (0.85 F1, 0.96 AUC), Kafka KPI streaming, and RAG over 6 bundled SOPs, run as a seven service Docker Compose stack. | scikit-learn, MLflow, Kafka, ChromaDB |
| [handoff](https://github.com/TanayPratapSingh/handoff) | Supervisor orchestration where every escalation has a deadline and a declared outcome when nobody answers: ladder, safer substitute, drop, or freeze. 212 tests, no dependencies, simulated cluster, no LLM calls. | Python |
| [comms-agent](https://github.com/TanayPratapSingh/comms-agent) | A stateful agent with a human review gate inside its control flow. On the sample run it flags 9 of 24 mentions and the reviewer corrects 7. Synthetic corpus, mock model, simulated reviewer. | Python, state graph, tool calling |
| Project Mark | Four families of analytics traps with deterministic golden solutions, built to stress test frontier models. The models solved the clean versions. | Python, pandas, statistics |
| [media-pulse](https://github.com/TanayPratapSingh/media-pulse) | Media monitoring with confidence gated human review. Review lifts topic accuracy from 0.88 to 0.96 and sentiment from 0.50 to 0.85; ECE 0.156. Synthetic corpus about a fictional brand. | scikit-learn, VADER, Streamlit |
| [Kp Index Forecasting](https://github.com/TanayPratapSingh/multi-horizon-aurora-kp-prediction) | LSTM forecasts of the geomagnetic Kp index from solar wind data. At 1 hour, RMSE 0.738, 45% better than a mean baseline, over 96,000+ hourly observations. | TensorFlow, LSTM |

Full write ups, including what each one gets wrong, are on the
[portfolio](https://tanaypratapsingh.github.io).

## Earlier

- **[The Perfect Lap](https://github.com/TanayPratapSingh/the-perfect-lap)**, 2025. Predicts the first pit stop lap in Formula 1. MAE 2.78 laps on 250,000+ records, with a Streamlit app.
- **[July Energy Demand Under Warming](https://github.com/TanayPratapSingh/energy-usage-prediction)**, 2025. Models July residential demand: +25.4% peak hour load at +5°C, and 9.2% savings from a 1°C setpoint shift. Random Forest R² 0.48. R and Shiny.
- **Wealth Equals Health?**, 2025. Gapminder data across 180+ countries: how far income explains life expectancy, and whether education does more than income to reduce child mortality. ANOVA F = 426.5.
- **Travel Itinerary Management System**, 2025. A 12 entity normalized SQL schema where stored procedures and triggers enforce the business rules.
- **Uber Data Engineering Pipeline**, 2024. A GCP pipeline into a BigQuery star schema.
- **Digit Recognition from Scratch**, 2024. A neural network in NumPy with hand written backpropagation. 94% on MNIST.
- **Real Time Big Data Inflow**, 2024. A literature review of 12+ primary sources comparing cloud and tiered edge architectures across six dimensions. For suitably partitioned workloads the comparison puts the latency reduction at 40 to 60%.

## Tools used in these projects

**Languages:** Python, SQL, R, TypeScript

**Retrieval and LLM systems:** BM25, sentence-transformers, ChromaDB, RAG
evaluation, calibration (ECE), guardrails, prompt injection detection, agent
orchestration, tool calling

**Training and ML:** PyTorch, TensorFlow, Keras, scikit-learn, XGBoost,
CatBoost, SHAP, LoRA, vLLM, MLX

**Data and analytics:** pandas, Kafka, Avro, dbt, DuckDB, BigQuery, Airflow,
Power BI, Tableau

**Serving and ops:** Docker, MLflow, FastAPI, GitHub Actions, Streamlit, Shiny

Coursework also covered Spark, Hive, HDFS, ksqlDB, MapReduce, Neo4j, Redis, and
Cassandra.

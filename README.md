# Tanay Pratap Singh

Graduate data science student at Syracuse University. I build retrieval,
evaluation, and streaming data systems, then measure what they actually do.

[Portfolio](https://tanaypratapsingh.github.io) ·
[tanayyps@gmail.com](mailto:tanayyps@gmail.com) ·
[LinkedIn](https://www.linkedin.com/in/tanay-pratap-singh-8360681b0/)

## Currently

- **MS Applied Data Science**, Syracuse University, graduating December 2026
- **Research Assistant, Gravity Spy 2.0** : NSF funded citizen science supporting
  LIGO. Causal inference on detector noise across 276,000+ volunteer
  classifications, 25,104 glitch subjects, and 8,293 auxiliary detector channels.
  Two input MobileNetV2 at 0.89 validation AUC, calibration error brought from
  0.10 down to 0.05.
- Open to **data, ML, AI, and analytics roles**

## Selected work

| Project | Result | Stack | Code |
|---|---|---|---|
| ZTF Transient Pipeline | 27,378 real ZTF alerts scored; dbt 8 models, 21 tests, 32 checks green | Kafka · Avro · TensorFlow · dbt · DuckDB · Airflow | [repo](https://github.com/TanayPratapSingh/ztf-transient-pipeline) |
| Groundwork | recall@5 0.921 · ECE 0.045 · injection recall 0.884 unseen · 113 tests | RAG · BM25 · LLM gateway · guardrails · calibration | [repo](https://github.com/TanayPratapSingh/Groundwork) |
| media-pulse | topic acc 0.88 to 0.96 with human review · sentiment 0.50 to 0.85 | scikit-learn · VADER · Streamlit · human in the loop | [repo](https://github.com/TanayPratapSingh/media-pulse) |
| comms-agent | stateful graph · 9 of 24 flagged, 7 corrected through the review gate | Python stdlib · state graph · tool calling · audit trail | [repo](https://github.com/TanayPratapSingh/comms-agent) |
| ShopFloor AI | 0.85 F1 · 0.96 AUC across 5 failure modes · 7 service deployed stack | scikit-learn · MLflow · Kafka · ChromaDB · Docker | [repo](https://github.com/TanayPratapSingh/shopfloor-ai) |
| The Perfect Lap | 2.78 lap MAE over 250K+ historical records | Random Forest · CatBoost · SHAP · Streamlit | [repo](https://github.com/TanayPratapSingh/the-perfect-lap) |
| Multi Horizon Kp Index Prediction | 45% better than baseline over 96K+ hourly observations | LSTM · RNN · TensorFlow · time series | [repo](https://github.com/TanayPratapSingh/multi-horizon-aurora-kp-prediction) |
| July Energy Demand Under Warming | +25.4% peak load at +5°C · 9.2% savings modeled | R · regression · scenario modeling · Shiny | [repo](https://github.com/TanayPratapSingh/energy-usage-prediction) |
| JMA Wireless DMAIC Dashboard | ~$355K/yr recovered · 31 GB JSON reduced to a 5 MB pipeline | DMAIC · pandas · openpyxl · Power BI | — |
| Project Mark | 4 verified statistical traps for frontier model evaluation | AI evaluation · analytics red teaming | — |
| Wealth, Health, and Education | ANOVA F = 426.5 (p < 2e-16) across 180+ countries | R · ANOVA · data storytelling | — |
| Travel Itinerary Management System | 12 entity normalized schema · full itinerary in one call | MySQL · stored procedures · triggers · ERD | — |
| Uber Data Engineering Pipeline | End to end GCP pipeline into a BigQuery star schema | GCP · BigQuery · SQL · dimensional modeling | — |
| Digit Recognition from Scratch | 94% MNIST accuracy with no frameworks | NumPy · backpropagation | — |
| Real Time Big Data Inflow | 40 to 60% latency reduction across a 6 dimension comparison | IoT · edge · fog · stream architecture | — |

Full write ups, including what each system gets wrong, are on the
[portfolio](https://tanaypratapsingh.github.io).

## Stack

**Languages**  
Python · SQL · R · C++ · Java · JavaScript

**LLM and generative AI**  
RAG · LangChain · ChromaDB · BM25 · agent orchestration · state graphs · tool calling · LLM gateway · guardrails · prompt injection defense · jailbreak detection · LLM evaluation · calibration (ECE) · human in the loop · PII redaction

**Machine learning and deep learning**  
scikit-learn · XGBoost · CatBoost · TensorFlow · Keras · LSTM · RNN · CNN · multimodal CNN · MobileNetV2 · SHAP · feature engineering · calibration

**Data engineering**  
Apache Kafka · Avro · dbt · DuckDB · BigQuery · Spark · Hive · HDFS · ksqlDB · star schema · dimensional modeling · ETL pipelines

**MLOps and serving**  
MLflow · Apache Airflow · Docker · Docker Compose · Kubernetes · GitHub Actions · model registry · FastAPI · Streamlit

**Analytics**  
Power BI · Tableau · DAX · hypothesis testing · A/B testing · cohort and funnel analysis · time series forecasting · anomaly detection · Lean Six Sigma DMAIC

## How I work

- **Every number traces to a command and an artifact.** If a figure came from a
  fixture or a stub adapter rather than a real run, it says so in the same
  sentence as the figure.
- **Limitations get published, not omitted.** Groundwork ships with its release
  gate failing abstention recall at 0.868 against a 0.900 floor. The ZTF README
  states plainly that its class labels are coarse and it is not a publishable
  classifier.
- **A headline with no baseline is not a result.** Retrieval ablations sit next
  to the number they are supposed to justify.

## Contact

**tanayyps@gmail.com** · tsingh13@syr.edu · Syracuse, NY

<!--ART:masthead-->

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

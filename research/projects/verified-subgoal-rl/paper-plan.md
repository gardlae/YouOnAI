# Paper, milestones, and public release

Prepared 2026-10-23. No empirical results or acceptance claims. Working title: **When Is It Really Done? Evaluating Visual Reward and Completion Models Under Manipulation Setbacks**. Revise the title around the actual finding.

## What makes a simulation-only paper credible?

A precise question, faithful strong baselines, a useful controlled test, reproducible evidence, and appropriately limited claims. Simulation gives exact state access for evaluation and controllable interventions. It does not establish real-world reliability, marine hydrodynamic validity, or deployment safety. Frame results as simulated manipulation and study what information the controller actually receives. Physical applicability is motivation; any transfer claim needs separate evidence.

Novelty may come from a well-supported empirical finding or evaluation protocol, not necessarily a larger model. Merely combining existing modules, showing a few successful videos, or adding underwater visuals is insufficient. The [related-work review](related-work.md) found close overlap; contribution selection is a research milestone, not a completed decision.

## Write the argument as evidence accumulates

| Paper section | What to write now | What must wait for evidence |
| --- | --- | --- |
| Introduction | Problem, concrete near-success example, scope | Claimed improvement and final contributions |
| Related work | Verified source table and differences | Assertion that the gap is novel |
| Problem formulation | Observations, goals, hidden evaluator, stop decision, information budgets | Final task/version choices |
| Method or evaluation design | Precisely specified scoring/verification/baselines | Claim that the proposed correction works |
| Experiments | Protocol, splits, metrics, budget and selection rules | Results tables, significance, performance claims |
| Analysis | Planned failure taxonomy and confound controls | Why a measured effect occurs |
| Limitations | Simulation-only, visual observability, pretrained-data overlap, compute limits | Further limitations discovered in runs |
| Reproducibility | Desired install/train/evaluate/analyze entry points and manifest | Statements that commands reproduced results |

Do not write an abstract containing invented results. First draft the research question, setup and experiment plan; after confirmatory runs write results and conclusion, then the final abstract. Choose a venue after checking fit and current submission rules, not by promising acceptance now.

## Required figures and tables

1. System/information-flow diagram, marking hidden simulator truth versus agent-visible data.
2. Synchronized example: frames, progress, completion probability, oracle predicate, and setback markers.
3. Main result table with per-task success, false-completion risk, declaration coverage, uncertainty, and training/inference cost.
4. Completion risk-versus-coverage curve under each scene shift; a method that never declares completion must remain visible.
5. Learning curves versus environment steps and measured compute, plus ablations identifying which component matters.
6. Failure gallery with representative and counterexample episodes selected by a disclosed rule, not only attractive successes.

## Milestones and acceptance gates

- **M0 — Preparation:** this source pack, compute inventory request, proposed protocol, and signal exercise. No simulator run yet.
- **M1 — Feasibility:** pinned Linux environment on the user's 5070; RGB reset/step video; GPU memory/throughput; native-reward control baseline. Verify architecture/toolchain compatibility instead of assuming GPU branding is enough.
- **M2 — Closest-work reproduction:** run a released reward model and its documented task/protocol as closely as possible; record any deviations. Freeze a small offline diagnostic test. If no failure persists, redirect before building a new method.
- **M3 — Minimal intervention:** implement only a justified correction, e.g. calibration/temporal evidence. Show what it fixes offline and compare with simple alternatives.
- **M4 — Closed-loop consequence:** matched RL control, test whether the correction improves actual outcomes rather than its own score. Expand only after a one-task pilot works.
- **M5 — Confirmatory study:** freeze code/config/splits, run repeated seeds, ablations and full failure analysis. Preserve failed runs and selection rules.
- **M6 — Manuscript and release:** manuscript, source bundle, environment lock, asset manifest, commands, checkpoints where permitted, and results traceable to run IDs. A clean-environment reproduction is a release criterion.

We can progress without a new method if a controlled benchmark/reproduction study reveals a scientifically useful result, but quality and publishability remain to be established.

## Open-source boundary

The current repository also holds personal Granola notes, Notion-derived material, lecture images, and older product material. User intent to release this research is not a reason to bulk-relicense or newly publish that archive. No repository visibility or license changes are made by this preparation.

Prepare a separable research package (initially under experiments/verified-subgoal-rl/) that can be exported to a clean public repository. Release first-party implementation and permitted configs/results; use manifests and download instructions for third-party papers, datasets, assets and weights. Choose a code license after checking intended dependencies and contributor ownership. Do not apply one blanket license to existing source material. Secrets, private prompts, user notes, and unlicensed lecture/paper content are outside the research release.

Public reproduction contract, to implement at M6: one supported installation path; one tiny smoke run; commands for training/evaluation/figure generation; exact versions and seeds; expected runtime/VRAM; known unsupported configurations; checksums and licenses for external artifacts; citation metadata and a clear simulation-only limitation. Do not advertise a command before it is tested.

## Compute plan

Start locally with frozen features/reward-model inference on short clips, low image resolution and measured environment parallelism. A training-size model that fits is not guaranteed to leave memory for rendering, rollouts and the optimizer. Profile the full workload. Use cloud GPUs only for a defined batch that exceeds local limits; estimate total cost from pilot wall time plus storage/data transfer, and agree a budget first. No provider or current price is recommended without a fresh check.

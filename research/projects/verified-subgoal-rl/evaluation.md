# Evaluation protocol draft

Freeze the final protocol before confirmatory runs. No results exist yet. Numerical budgets below are pilot planning values, not statistical-power guarantees.

## Claims and hypotheses

H1: At a matched completion-declaration coverage, the candidate completion rule reduces false declarations on held-out scenes compared with the strongest feasible published reward/success model and a validation-tuned simple threshold baseline.

H2: After a controlled reversal, the progress estimator better identifies direction of change; using it in RL improves independent task success at matched interaction and inference budgets. Better offline scores alone do not establish H2.

H3, only after H1/H2: image-plus-text subgoals improve held-out task performance over each modality alone under matched controller capacity and training data. This is a separate, potentially expensive claim; omit it from the first paper if unsupported.

## Two evaluation tracks

1. Standard track: preserve official task definitions, initial-state distribution, action/control interface, horizon, observations, success condition, and evaluation protocol. Pin task/version/checkpoint commits. Reproduce at least one published or officially supplied baseline before making comparative claims.
2. Diagnostic extension: explicit near-success, undo/drop, occlusion, distractor, camera/layout, and held-out-object tests. Label as a new protocol. Run all selected baselines in it. Published numbers on a different protocol cannot be copied into the comparison as if equivalent.

Scene appearance, object identity, mechanism identity, and task composition are different generalization axes. Separate them. Begin with layout/distractor and held-out-object conditions; reserve mechanism/composition generalization for later. Avoid combining all shifts into a single uninterpretable difficulty score.

## Baselines, in implementation order

| Baseline | Purpose | Fairness condition |
| --- | --- | --- |
| Script or stock policy | Generate trajectories and catch environment bugs | Diagnostic data source, not claimed learned competitor |
| PPO with native simulator reward | Establish control feasibility | Privileged training reward disclosed; same policy observations for fair control comparison |
| Frozen image/text similarity reward + tuned success threshold | Test whether extra architecture is needed | Same data and validation scenes; no arbitrary weak threshold |
| Closest available published reward model, particularly Robometer | Test the actual competing explanation | Verify checkpoint/code availability, preprocessing, license, compute feasibility; faithful reproduction first |
| Candidate + same policy optimizer | Isolate reward/verifier effect | Same training steps, seeds, sensors, tuning allowance, policy size, and inference budget |
| Candidate ablations | Identify useful component | No verifier, no history, no reversal data, fixed versus predicted subgoals; prioritize only relevant ablations |

StructRL is important related work. If a faithful run requires a large VLA and a different suite, do not treat a simplified imitation as its published result. Report an adapted structured-reward baseline by its own name. A direct VLA baseline is optional and does not replace reward-model baselines.

## Dataset construction

Split by scene/object instance before extracting frames or generating augmentations. All frames, alternative views, rewinds, and counterfactual variants of one trajectory remain in its split. Reserve unseen failure causes where possible. Fit thresholds, hyperparameters, and checkpoint selection only on train/validation. Freeze a test manifest and hash before final evaluation; do not repeatedly tune on the test set.

Collect near-success cases with independent simulator predicates: adjacent to rather than inside a receptacle, correct location but wrong target, transient contact without insertion, and task undone after apparent completion. These are candidate cases; keep only physically valid examples supported by the actual task. Real simulated failures should accompany video rewinds so the model cannot succeed by detecting editing artifacts.

## Metrics and units

- Environment success: successful episodes / all evaluation episodes using the official hidden predicate. Include abstentions and timeouts in the denominator.
- False completion among declarations: incorrect declarations / all declarations. Report declarations/all episodes (coverage) alongside it. If no declarations occur, the false-completion fraction is undefined, not zero.
- Missed completion: episodes satisfying the evaluator's completion criterion without a timely declaration, with the tolerance defined before testing.
- Reversal sensitivity: signed progress change around independently labeled regression events; report unchanged/successful event controls and latency, not just correlation with time.
- Calibration: reliability plots and Brier score for a quantity explicitly trained as a probability; stratify by shift and account for correlated video frames. Do not interpret arbitrary embedding similarity as probability.
- RL: success versus environment transitions and GPU-hours; recovery rate among eligible perturbed episodes; time-to-success; all constraint violations; reward-model calls, latency, peak VRAM, and cost of labels/data generation.

Use matched scene seeds across methods. Independent training seeds are the experimental units for learning variability; many episodes from one trained checkpoint do not replace them. Start with three seeds for debugging, aim for at least five for confirmatory runs if feasible, and revise based on pilot variance and desired effect precision. Report per-task/per-seed results, uncertainty, failures, and exclusions. Bootstrap at the appropriate seed/scene level, not independent video frames. For aggregate multi-task comparisons consider the interval-estimation guidance in [Agarwal et al.](https://arxiv.org/abs/2108.13264).

## Gates and compute control

G0: GPU rendering, reset/step, official success checks, and tiny RL run work at a pinned configuration. Record actual hardware and timings.

G1: Offline failures reproduce across multiple held-out scenes; distinguish a model limitation from a bad adapter. Stop pursuing a correction if a strong existing model already handles the proposed failure.

G2: One RL task learns under a native reward. If not, fix the control/optimizer before blaming learned rewards.

G3: Closest feasible baseline reproduced; proposed change improves a predeclared metric without collapsing coverage or success. Expand to three task families only after this.

G4: Confirmatory comparisons and ablations support the claims with uncertainty. If null, publish a faithful failure/reproduction analysis if it provides sufficient scientific insight; acceptance is not guaranteed.

Budget worksheet: methods × tasks × training seeds × measured hours per run, plus tuning, reward-model training, data generation, evaluation, storage and retries. A planning matrix of 4 methods × 3 tasks × 5 seeds already means 60 training runs before ablations. Pilot locally first, then choose cloud capacity from measured VRAM/throughput. Do not rent compute before a costed batch and budget are agreed.

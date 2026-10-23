# Proposed method and tools

Status: design hypothesis, not implemented robotics software. See [related work](related-work.md) before treating any component as novel.

## Define the signals

- Observation o_t: permitted camera images, proprioception, and optionally a short history. Any extra sensing must be disclosed and matched across comparable methods.
- Subgoal g_k: text plus an optional reference image and explicit target identity. A generated goal image is an uncertain specification, not evidence that the state is physically achievable.
- Progress p_t in [0,1]: an estimate of current progress toward a fixed subgoal. It can rise, fall, or remain flat. It is not automatically a probability, RL value function, or percent of elapsed time.
- Cost c_t = 1 - p_t: decreases as progress increases. Actual physical/constraint costs can be separate quantities.
- Reward r_t: the training feedback on a transition; different from the optimizer's loss and different from the evaluator's success label.
- Completion q_t: a calibrated estimate of whether the target is truly satisfied. Progress near 1 is not sufficient to declare success.
- V^pi: expected discounted return under a policy, not necessarily the same as progress or a completion probability.

Example: approach 0.1 → grasp 0.4 → lift 0.7 → drop 0.2 → recover 0.6 → seat 0.9. The negative change 0.7 → 0.2 must remain visible. Completion can still be false at 0.9 if the connector only appears seated. These values are illustrative, not labels from a trained model.

## Architecture to investigate

Instruction + initial scene → constrained image/text subgoal description → goal-conditioned RL policy → robot actions → observation history → progress estimate and separate completion decision → continue, recover, or advance.

Begin with one fixed human-authored subgoal. Then use a fixed subtask plan. Only add a VLM planner after the executor and verifier work: otherwise failures cannot be attributed to planning, reward estimation, or control. A fixed plan is also a necessary baseline for any planner contribution.

Use an existing simulator PPO implementation for the first learning exercise if supported by the chosen stack. Learn SAC as a contrasting off-policy method; if reproducing Robometer Appendix E.1, use its SAC setup instead of substituting PPO and calling it a reproduction. Do not implement and tune both for the paper without a reason. State observations are useful for debugging control, but state-policy results belong in a privileged diagnostic track. The intended visual controller uses permitted images/proprioception and goal conditioning; freeze a visual encoder first to contain compute.

## Shaping without hiding regressions

A reference shaping form is r'_t = r_base_t + lambda * [gamma Phi(z_{t+1}) - Phi(z_t)], where z includes the state/history representation and active subgoal needed for the decision process. Phi may be a frozen progress estimate. Log the raw delta p_{t+1}-p_t separately; the discounted shaping term is not the same quantity and can be negative even when progress is constant.

The classical policy-invariance result requires its assumptions, including consistent discounting and appropriate potential/terminal handling. An arbitrary changing VLM score or resetting the potential between subtasks does not inherit a blanket guarantee. Use a frozen version within a training phase; include subgoal switches in the augmented state rather than silently resetting scores. Use zero absorbing-terminal potential on true terminal transitions; a time-limit truncation is not automatically terminal for bootstrapping. Do not clip negative shaping terms or grant repeatable positive payouts for cycling between stages. [Potential-based shaping reference](http://robotics.stanford.edu/~ang/papers/shaping-icml99.ps).

Any time penalty, contact penalty, or learned terminal bonus changes the chosen objective unless already part of the reference task. Report it explicitly. Compare learned-reward runs with a strong simulator-reward reference; do not call the reference an oracle performance upper bound, because optimization can still fail.

## Completion and information boundaries

The evaluator owns privileged object states, contacts, and official task predicates. The main policy/reward/verifier inference path receives only permitted observations. Simulator labels may supervise the verifier on training scenes if disclosed; no held-out labels, textures, task IDs that reveal answers, filenames, or oracle-selected goal images may leak into inference. Validate visual goal-image selection separately.

Fit completion thresholds and any temporal consistency rule on validation scenes, then freeze them. A short persistence window can suppress flicker but is not proof of completion. Evaluate visual ambiguity explicitly; if completion is not observable from the allowed cameras, the system should acquire another permitted view or abstain, or the claim must be limited. Keep this an optional follow-up until fixed-camera feasibility is understood.

For sequential tasks distinguish historical milestones from currently required predicates: grasping need not remain true after a correct release, whereas placement may need to remain true until the final goal. Allow reversal of current predicates where physically appropriate. Do not use a monotonically increasing stage counter as ground-truth physical progress.

## Tools to reuse and build

| Component | Reuse first | Project work required |
| --- | --- | --- |
| Physics, robot, cameras | Selected simulator and stock tasks | Thin observation/action adapter; pin versions and control rates |
| RL optimizer | Stack's maintained PPO example | Reproducible configs, seed control, checkpoint/evaluation separation |
| Image/text representation | Existing licensed encoder/reward model | Preprocessing adapter, batching, latency/memory measurements |
| Task specification | Official predicates and instructions | Optional subgoal graph with explicit prerequisite/current-state semantics |
| Progress estimator | Closest published checkpoint + simple similarity baseline | Reversal stress tests; learn a correction only after observed failures |
| Completion decision | Existing success predictor or validation-calibrated score | Frozen threshold, near-success tests, abstention accounting |
| Evaluator | Official benchmark success tests | Independent event logger and matched rollout protocol |
| Analysis | Existing plotting/statistics tools | Progress/reward/oracle plots; seed-level confidence intervals; failure gallery |

Recommended future code layout under experiments/verified-subgoal-rl/: envs/, policies/, rewards/, verifiers/, configs/, evaluation/, analysis/, tests/. Do not create empty abstractions for all of these now. Implement them in the order the first experiment needs them.

Minimum episode record: run/commit/config hash, simulator/backend/version, task and split IDs, training/evaluation seed, checkpoint/reward-model hashes, allowed sensor set, timestep, subgoal ID, progress, shaped/base reward separately, completion probability and decision, hidden evaluator success, termination versus truncation, inference calls/time, and constraint events. Store bulky trajectories outside Git with manifests.

A plot should align video frames with predicted progress, completion confidence, independent task predicates, and event markers. A falling progress curve alone is not evidence the policy learned useful recovery.

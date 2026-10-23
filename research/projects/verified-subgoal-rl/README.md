# Verified subgoal RL: research preparation

Prepared 2026-10-22–23. Working project name, not an established method or result.

## Objective and scope

Target a high-quality simulation-only research paper with reproducible, publicly releasable code. Learn reinforcement learning and understand modern VLA research through the work. User priorities: unfamiliar scenes, knowing when a task is actually finished, image/text subgoals, and progress signals that can decrease after mistakes. A direct VLA controller is not required. Underwater is a motivating application and optional later extension; real-world testing is outside the initial scope.

User has a Linux computer with an NVIDIA 5070 and is willing to consider cloud compute. Exact GPU variant, VRAM, driver, software support, and throughput have not been inspected. No cloud purchase or training job has been launched.

## Working research question

How reliably do visual-language reward models recognize progress reversals and genuine completion under held-out scene changes, and does a calibrated completion decision improve goal-conditioned RL at a matched interaction and inference budget?

The first deliverable is an honest failure study and reproduction, not a novel architecture. Robometer already combines progress/success prediction with downstream RL; StructRL already uses structured verifiable subtask rewards. A new head, VLM decomposition, or changing the action policy alone is not sufficient novelty. See [related work](related-work.md). If existing systems solve our proposed challenge, reproduce that result and change the question rather than manufacturing a gap.

Potential paper contribution, contingent on evidence: a controlled benchmark of near-success and reversal failures under scene shift; a reproducible analysis of their downstream consequences; and, only if justified, a targeted correction that improves the completion-risk versus task-success tradeoff.

## Preparation pack

- [Simulator and benchmark decision](simulators.md): current options and a conditional hardware feasibility check.
- [Related work](related-work.md): closest overlap, evidence depth, and novelty boundaries.
- [Method and required tools](method.md): observations, RL, progress, completion, and implementation order.
- [Evaluation protocol](evaluation.md): fair baselines, holdouts, measurements, and go/no-go criteria.
- [Learning path](learning-path.md): RL foundations and staged VLA reading with exercises.
- [Paper and release plan](paper-plan.md): argument structure, figures, milestones, and open-source boundary.
- [Progress-signal exercise](../../../experiments/progress-signal-sanity/README.md): runnable mathematical sanity check, not robotics evidence.

## First experiment, before an expensive method

1. Choose one existing task in the selected simulator and collect successful, failed, and near-success trajectories from a script or existing policy.
2. Freeze scene-level train/validation/test splits. Include a genuine undo/drop event and visually similar unsuccessful endings; do not label progress by elapsed time.
3. Evaluate a simple frozen visual-language score and the closest available reward model. Use hidden simulator predicates as the independent completion labels, never as policy observations in the main visual track.
4. Check whether errors persist on several tasks and matter to a controller. Only then propose a learned correction or add subtask composition.

Initial task families to investigate: object placement inside a receptacle, insertion, and articulated closure. These are task families to map to actual environment IDs during the feasibility check, not claims that one stack provides all of them unchanged.

## Decisions and open points

Decided by user: paper first; simulation acceptable; open-source intent; learn RL/VLA along the way; Linux/NVIDIA GPU available. Proposed by assistant: begin with reward/completion evaluation, then one RL task, then composed tasks. Final simulator, benchmark versions, model checkpoints, novel contribution, publication venue, and cloud budget remain open. Preparation does not imply a claim of state-of-the-art performance.

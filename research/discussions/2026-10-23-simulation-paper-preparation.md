# Simulation-first paper and learning path

Conversation spans 2026-10-22–23. This records user intent and the preparation response, not experiment results.

## User direction, paraphrased

Target a research paper first, with good-quality scientific results and a public open-source implementation. Real-world testing is too ambitious initially; simulation-only is acceptable. Focus on unfamiliar scenes and recognizing actual completion. Prefer image/text subgoals with reinforcement learning over a direct VLA controller. A progress signal should decrease when a mistake takes the robot backward. Learn RL better and study the Learning VLA paper collection together. Prepare sources, simulators, and a feasible plan using agents. User confirms Linux and an NVIDIA 5070, with willingness to consider cloud compute.

## Preparation outcome

The [project preparation pack](../projects/verified-subgoal-rl/README.md) includes a simulator comparison, related-work evidence table, method specification, evaluation protocol, learning path, paper outline, milestones and release boundary. The [signal exercise](../../experiments/progress-signal-sanity/README.md) is executable teaching material with synthetic inputs, not a robotics experiment.

Progress rises toward a target and can fall after a setback; a corresponding cost normally moves in the opposite direction. Reward on a transition, an RL value function, completion confidence, and optimizer loss are distinct. Do not infer completion solely from a high progress score. The simulator's hidden task predicates should evaluate the learned system independently.

## Main research finding

The broad architecture is already studied. [Robometer](https://arxiv.org/html/2603.02115v2) predicts progress/success and, in Appendix E.1, trains non-VLA SAC using image features and proprioception on LIBERO-90 tasks. [StructRL](https://arxiv.org/html/2609.36352v1) supplies structured intermediate rewards from verifiable subtasks. Therefore subgoals + RL, a progress head, or replacing a VLA with SAC is not enough to claim novelty.

Proposed narrower question: how well do existing reward/completion models handle genuine progress reversals and visually misleading near-success under held-out scene changes, and can a calibrated temporal completion decision improve actual outcomes at matched data/action/inference budgets? This is a hypothesis requiring reproduction and a further focused novelty review. First perform the failure study, then decide whether a method contribution is warranted.

## Simulator and compute direction

ManiSkill is a conditional starting choice for accessible GPU manipulation RL on Linux/NVIDIA. If the first experiment is a faithful Robometer reproduction, its LIBERO setup takes priority; avoid maintaining two stacks or pretending a port is an unchanged reproduction. Isaac Lab is a strong alternative whose current backend/version matters. Stonefish remains a later option when underwater physics is part of the scientific question. See [sources and platform caveats](../projects/verified-subgoal-rl/simulators.md).

The 5070's exact VRAM, variant, runtime compatibility and throughput are unknown. Start with a pinned environment and a tiny local workload before pricing cloud runs. No remote computer was accessed, simulator installed, weights downloaded, GPU training launched, or cloud resource purchased in this preparation.

## Learning and writing

Use the existing Notion course sequence without claiming papers already read. ACT is the first learning paper; Robometer is the first deep project-overlap reading. Combine CS285 foundations with one small RL experiment at a time. Save teach-back notes with separate states for overview, methods read, full paper, code inspection and reproduction.

Write the question, related work, formal setup and evaluation protocol before results. Results and abstract claims come after experiments. Keep official benchmark protocols intact and report new stress tests separately. Reusing a simulator does not establish comparability to state-of-the-art numbers. Simulation supports scoped scientific claims, not demonstrated real-world or marine reliability.

Public code should be a separable research package with a deliberate license and asset manifests. Existing personal source notes, lecture images and third-party material must not be swept into a blanket software license. No repository visibility change was made.

## Work status and next step

Two bounded fresh-context research agents produced drafts and key findings before both hit workspace-credit errors. Coordinator completed integration and local checks without retries. No independent critic review was completed. Seven signal/measurement tests passed; local documentation links were checked. These checks validate preparation artifacts, not the proposed method.

Next concrete work: inspect the Linux GPU environment, choose one primary simulator/protocol, run the small feasibility check, and begin the ACT/Robometer reading sessions. Publication venue, final novelty claim, checkpoints and cloud budget remain undecided.

# Task queue

Updated: 2026-10-23. Coordinator owns this file. Git records claims; it is not a distributed lock.

| ID | Work | Status | Owner | Evidence / next action |
| --- | --- | --- | --- | --- |
| SETUP-001 | Durable discussion notes and economical agent roles | Complete | Coordinator | Pushed b57855c; remote HEAD verified in prior turn. Five TOML files and local links passed. Both children failed on credits; coordinator completed the work. Independent review and live named-role loading remain unverified. |
| DISCUSS-001 | Explore manipulation opportunities | Narrowed | User + coordinator | User selected paper-first, simulation-only scope with unfamiliar scenes/completion and RL learning. Underwater optional later. See latest preparation note. |
| PREP-001 | Research sources, simulators, protocol and learning path | Complete locally; ready to sync | Coordinator | research/projects/verified-subgoal-rl/README.md. Two bounded agents produced drafts then hit credit errors; coordinator integrated without retries. Seven arithmetic/metric tests pass; no independent critic review or simulator run. |
| PILOT-001 | GPU inventory and one simulator feasibility check | Next; not started | Coordinator + user environment | Linux NVIDIA 5070 confirmed; inspect VRAM/toolchain and pick ManiSkill or closest-work LIBERO protocol. No paid jobs yet. Gates in evaluation.md. |
| LEARN-001 | Begin paper reading and RL foundations | Ready | User + coordinator | ACT worksheet and CS285 in learning-path.md; Robometer is the first deep novelty-overlap read. No paper marked read by preparing this plan. |

Completed work should retain a brief result and verification pointer. Add a task only for actual agreed work; ideas remain in discussion notes. Before switching computers, push finished records. On the receiving computer inspect git status, fetch, and use git pull --ff-only when clean. If work has diverged, reconcile it before claiming tasks.

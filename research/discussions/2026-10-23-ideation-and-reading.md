# Return to ideation and conceptual understanding

2026-10-23. User prompt, paraphrased: implementation has received enough attention for now; spend more time in the idea phase, sketch concepts from new research, explore new applications/combinations, and provide a reading list needed to formulate the project.

Decision: park the simulator pilot and keep the research architecture provisional. The simulation-only paper, open-source intent, and RL/VLA learning goals remain. No new agents, installations or training were launched for this discussion.

The substantive response is preserved in [the concept/idea map](../projects/verified-subgoal-rl/ideation.md) and [the ordered reading list](../projects/verified-subgoal-rl/reading-for-ideation.md).

Key conceptual distinctions: semantic versus physical success; partial observability; progress versus completion; historical milestones versus currently true conditions; and useful versus misleading context. GVL, ReWiND and SafeStage were checked as targeted additions, with evidence depth recorded in the documents.

Four possible ideas, all unselected hypotheses:

1. Choose a physical verification action to establish completion, such as a bounded pull to distinguish an inserted from a latched connector.
2. Track subgoal conditions that must remain true and recover when later actions invalidate them.
3. Judge completion after release/settling or a task-relevant disturbance, rather than only at one favorable instant.
4. Resolve conflicts between instructions/reference images and observed physical evidence, without simply ignoring difficult instructions.

Each candidate includes a simple competing explanation and a condition under which we should abandon it. None is claimed novel: active perception, temporal logic, robust control and diagnosis must be checked once a phenomenon is selected. Assistant preference is to discuss active verification and reversible task conditions first, not to commit the project to them.

Core reading sequence: ACT; CS285 selected RL fundamentals; OpenVLA; Hi Robot; GVL; ReWiND; Robometer; StructRL. Branch readings include ReKep, SafeStage, Causal Confusion, RL-VLM-F, LIV and potential-based shaping. Begin with ACT and the policy/reward distinction, then use GVL/ReWiND to discuss progress and Robometer to understand close prior work. No paper is marked read by listing it.

Readiness means explaining component roles, information boundaries, closest prior work, a concrete confusing case, the simplest baseline and a falsifying result. It does not mean reading all 88 papers or choosing a simulator first.

Next conversation: compare “the robot chooses what evidence to gather” with “the robot knows which achieved conditions have become false,” using one concrete manipulation scene. Implementation remains parked until the idea is developed further.

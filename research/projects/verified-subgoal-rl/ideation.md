# Ideation: what should the robot understand?

2026-10-23. User steering: remain in the idea phase; sketch important research concepts and explore new applications before implementation. The paper and learning objectives remain. The project name and architecture are provisional. This supersedes earlier recommendations to begin the simulator pilot immediately.

## Concept map

| Concept | Meaning in plain language | Why it changes our question |
| --- | --- | --- |
| Policy versus evaluator | A policy chooses actions; a reward model scores transitions or trajectories; a verifier judges a particular condition. | A stronger action model does not automatically know when its work is done. |
| Hierarchical control | A planner chooses intermediate goals; a controller executes them. | Useful decomposition is established prior work, not our novelty by itself. |
| Semantic versus physical success | An image can look consistent with an instruction while a latch, contact or support condition is wrong. | We must specify what evidence makes success observable. |
| Partial observability | Different physical states can look identical in the current view. History or an intervention may distinguish them. | Some failures require acquiring information, not more confident image classification. |
| Progress versus completion | Relative improvement and absolute satisfaction are different questions. | Ranking two frames correctly does not establish a reliable stopping threshold. |
| Historical milestone versus current condition | A grasp happened earlier; a component remains seated now. These need different memory. | A stage counter can hide that a prerequisite has become false. |
| Generalization | New appearance, object geometry, mechanism or instruction each creates a different challenge. | “Unfamiliar scenes” needs a chosen dimension; one success cannot establish all forms. |
| Grounded context | Manuals, language and goal images are hypotheses about the world, sometimes wrong or incomplete. | More context can introduce a wrong shortcut; test whether it changes the right decision. |

## Research connections and evidence depth

Previously checked sources and scope are recorded in [related work](related-work.md). Hi Robot/HAMSTER motivate hierarchy; ReKep motivates explicit spatial constraints; Robometer is close prior work for learned progress/success and non-VLA RL. No full collection review has occurred.

Three targeted additions checked 2026-10-23:

- [GVL: Vision Language Models are In-Context Value Learners](https://arxiv.org/abs/2411.04549), ICLR 2025 / 2024 preprint. Abstract inspected. It reframes progress estimation using shuffled frames to reduce misleading temporal correlations. This suggests testing whether a score follows physical content rather than chronology. It does not establish that an online system may use future frames; causal history and offline access must be distinguished.
- [ReWiND](https://rewind-reward.github.io/), CoRL 2025. Author method page inspected. It learns language-conditioned rewards, uses video rewinding to represent decreasing progress, and adapts policies through RL. Falling progress is therefore established prior work. Rewinding footage is also different from generating physically valid recovery trajectories.
- [SafeStage](https://arxiv.org/abs/2609.21223), September 2026 preprint. Abstract inspected. It separates before/during/after-task hazards and reports nominal task success separately. This motivates distinguishing a momentary success predicate from an acceptable final condition; post-completion safety itself is not a new topic.

These sources support the concepts. The proposals below are our inferences, not claims of gaps demonstrated by those papers. Active perception, temporal task logic, diagnosis and robust control are older fields too; each selected proposal needs a targeted nearest-neighbor literature review before a novelty claim.

## Four ideas to explore, without choosing an implementation

### A. The robot chooses how to establish that it is done

Combine learned progress/success with explicit task constraints and information-gathering actions. Example: after inserting a simulated connector, the robot applies a small bounded pull and observes relative motion. A second image from the same viewpoint may not distinguish seated from latched; the intervention might.

Question: can choosing a task-specific verification action reduce false completion at equal action/time/sensing budgets, including mechanisms not used in training?

The object of study is the decision to gather evidence, not simply adding a success classifier. Compare with a fixed check routine, passive waiting, another view and existing temporal success models. If the fixed routine is just as good, adaptive verification has not earned its complexity. Also count checks that disturb a correctly completed task.

Underwater application: connector or retained tool. Land application: snap-fit assembly or cabinet servicing. First decide which hidden condition is observable through the permitted action; do not claim image-only inference can recover invisible physics without new evidence.

### B. The robot maintains conditions instead of accumulating completed steps

Combine structured subtasks with reversible progress and explicit memory of current requirements. Example: a gripper seats a part, then moves a cover and dislodges the part. A historical “insertion completed” flag is now misleading, but a historical “grasp occurred” flag may be harmless after a correct release.

Question: which subgoal conditions must persist, and can a policy detect their loss and recover only the affected dependencies?

This could connect unfamiliar scenes to recovery: learned geometry differs, but relations such as inside, supported, locked and released may remain useful. Compare with a finite-state machine with hand-authored rollback rules, a recurrent policy, and structured reward baselines. Temporal logic and state-machine rollback are established; any contribution must involve learned grounding/generalization or a concrete empirical finding.

Underwater application: a current disturbs an earlier placement. Land application: a later assembly step invalidates an earlier one. The research might reveal that semantic plans must track currently true relations rather than just chronology.

### C. The robot defines completion as a lasting physical outcome

Combine success estimation with explicitly specified future conditions. Example: an object is inside a receptacle while held by the gripper, but falls out after release. A connector might remain seated only until a small task-relevant disturbance occurs.

Question: can the system distinguish “looks achieved now” from “remains achieved after release and a specified settling period or disturbance”?

Choose the disturbance and persistence requirement from the task, not an arbitrary robustness challenge. A fixed settling-time check is a strong simple baseline. Keep native benchmark success separate from the additional persistence criterion. If a delay alone solves the problem, that is useful evidence against a complicated predictive model.

SafeStage is related prior work; our possible angle would need to be the learned verification/recovery decision or generalization to unseen supports/retention mechanisms. A predictive world model is one possible tool, not a commitment; plausible future images do not prove correct contact dynamics.

### D. The robot decides which context to trust

Combine multimodal subgoals, physical evidence and controlled contradictory context. Example: the instruction says a latch turns clockwise, but the visible mechanism and a gentle trial indicate otherwise; a goal photo depicts the correct location but the wrong object.

Question: can a robot identify which part of an instruction/reference is unreliable, gather disambiguating evidence and preserve the actual goal?

This directly examines the original “better context” hypothesis. Compare correct, missing, irrelevant and subtly incorrect context on otherwise matched tasks. Measure both resistance to wrong context and ability to follow correct unusual instructions; ignoring all instructions is not a solution. Work on causal confusion and instruction grounding is essential background. Avoid silently changing the user's goal when the system sees a conflict.

## How to decide among them

Assistant preference for discussion: A combines unfamiliar mechanisms and completion most directly; B offers a different question about temporal structure and recovery. C can be a sharply scoped completion study; D returns to whether context actually helps. This is not a user selection, a novelty finding, or a forecast of acceptance.

For each idea, answer these before coding:

1. Describe one concrete scene and two states a baseline might confuse.
2. What evidence distinguishes the states, and is it available to the robot?
3. What decision changes when the robot obtains that evidence?
4. Which existing paper comes closest, and which simplest conventional method might already solve it?
5. What result would make us abandon the idea?

Write one idea card per candidate using: phenomenon → closest prior work → proposed difference → competing explanation → observation that would settle it. Novelty review follows the chosen phenomenon; simulator choice follows the scientific question.

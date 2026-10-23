# Learn RL and VLA while building the study

Prepared 2026-10-23. This is a sequence of mastery gates, not a promised calendar. Do not wait to read every paper before running small experiments, and do not mark papers read because an assistant summarized an abstract.

## Source context

The connected [Learning VLA Notion page](https://app.notion.com/p/3f13ed51cad381cca39bddfa38467993) was fetched during preparation. It confirms ACT as the starting paper, 76 course readings plus earlier suggestions, and the CS285 Fall 2023 playlist. It also warns that some original hyperlinks were missing. The [local 88-entry index](../../knowledge-base/Robotics%20learning/Research%20papers/reading-list.md) remains the working queue; this fetch did not re-audit every row or change Done checkboxes.

Use [CS285 Fall 2023](https://rail.eecs.berkeley.edu/deeprlcourse-fa23/) and its [official homework repository](https://github.com/berkeleydeeprlcourse/homework_fall2023) for foundations. The historical course is intentional; dependency instructions may require adaptation. [Spinning Up](https://spinningup.openai.com/en/latest/) is a useful conceptual companion, not a claim about today's best training implementation. Follow the selected simulator's maintained training examples for the experiment environment.

## Sequence and evidence of understanding

| Gate | Reading / study | Small artifact to produce | Ready to advance when… |
| --- | --- | --- | --- |
| 0. Task and signals | CS285 intro and supervised behavior learning; [ACT](https://arxiv.org/abs/2304.13705) | Diagram observation → action; compare imitation learning and RL; run the local progress-signal exercise | You can distinguish reward, cost, progress, value, optimizer loss and completion |
| 1. RL fundamentals | CS285 lectures 4–8; [PPO explanation](https://spinningup.openai.com/en/latest/algorithms/ppo.html); [SAC explanation](https://spinningup.openai.com/en/latest/algorithms/sac.html) | One small state-based task; learning curves over seeds; explain Bellman targets and terminal/truncated bootstrapping | You can explain why PPO is on-policy, SAC uses replay, and why changing reward is not changing the optimizer |
| 2. Manipulation and observations | ACT in depth; Diffusion Policy from the local index; simulator observations/controllers docs | Native-reward manipulation baseline; compare state versus image inputs without confusing their information budgets | You can locate whether a failed rollout comes from control, perception, or objective definition |
| 3. VLA architecture | [OpenVLA](https://openvla.github.io/), then pi0/pi0.5 and one recent course entry | Table: pretraining data, inputs, action representation, training loss, inference, adaptation, evaluation | You can distinguish a VLM planner, direct VLA, and an RL policy conditioned on text/image features |
| 4. Reward learning—the critical reading | LIV, RoboCLIP, RL-VLM-F, then Robometer method and Appendix E.1; links in [related work](related-work.md) | Reproduce scoring on a small success/failure trajectory collection; annotate one misleading score | You can explain exactly how each method gets reward supervision and whether it sees completion labels |
| 5. Hierarchy and completion | Hi Robot, ReKep, StructRL methods/appendix, potential-based shaping | Fixed-subgoal and fixed-plan experiment; explicit stage validity/undo rules | You can distinguish planning errors, wrong progress, false completion and low-level failure |
| 6. Scientific evaluation | [Statistical Precipice](https://arxiv.org/abs/2108.13264), benchmark protocols, closest prior method's full experiment details | Frozen splits, baselines, metric definitions and pilot variance report | You can explain what result would disprove the proposed advantage |

The pi0 and recent-model entries are queued reading, not independently reviewed here. Refresh that portion from primary papers when we reach it; do not label this queue a current leaderboard. Read world models, tactile control and underwater dynamics later if the measured problem requires them.

## How we will read a paper together

1. Before reading: state the question you expect the paper to answer and one uncertainty.
2. First pass: abstract, central figure, conclusion and limitations. Label this a first pass.
3. Second pass: inputs, labels, losses, algorithm, baselines, task definitions and ablations. Reconstruct one equation or algorithm step in your own words.
4. Evidence check: select the main result table; identify what is held fixed, what information each method receives, and one alternative explanation.
5. Transfer: choose one component to reuse and one claim that does not transfer to our setting.
6. Teach-back: you explain the method briefly; I ask targeted questions and help correct the model. Save the note using the [literature template](../../methods/literature-note-template.md).

Reading states: queued → abstract/overview → methods inspected → full paper read → code inspected → reproduced. These are separate achievements. Neither publication nor a convincing video proves reproduction.

## First session: ACT worksheet

Read ACT's abstract and method figure, then the action-chunking and temporal-aggregation sections. Questions: Why predict several actions together? What problem does temporal aggregation address? Where do demonstrations enter? What distribution shift remains when the robot makes a mistake? Why is this imitation learning rather than RL? Which parts would we keep if the policy were trained from rewards instead?

Artifact: a one-page note and a hand-worked example of overlapping action chunks. ACT begins the learning path because your Notion plan puts it first; Robometer should be the first deep paper for testing this particular project's novelty. Neither reading is marked complete by preparing this worksheet.

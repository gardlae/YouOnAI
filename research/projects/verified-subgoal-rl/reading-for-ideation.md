# Reading to reach research-level understanding

2026-10-23. Active reading sequence while implementation is parked. The [Learning VLA collection](../../knowledge-base/Robotics%20learning/Research%20papers/reading-list.md) stays the larger library. This is a prioritized subset plus relevant additions; no reading checkbox is changed by this document.

The goal is to explain and challenge mechanisms, not memorize all 88 titles. Paper age is not quality: older theory often explains a new system's assumptions. Evidence depths below describe what the assistant checked, not what the user has read.

## Core sequence

| Order | Read | Depth for your first pass | What you must be able to explain |
| --- | --- | --- | --- |
| 1 | [ACT — Learning Fine-Grained Bimanual Manipulation](https://arxiv.org/abs/2304.13705) | Abstract, method figure, action chunking and temporal aggregation | What the policy predicts, where supervision comes from, and why mistakes can move it outside demonstration data. This is imitation learning, not RL. |
| 2 | [CS285 Fall 2023](https://rail.eecs.berkeley.edu/deeprlcourse-fa23/): lectures 4–8; use lecture 2 if imitation learning is unfamiliar | Work through reward/return, policy/value, Bellman reasoning, policy gradients and actor-critic concepts; skim [PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) and [SAC](https://spinningup.openai.com/en/latest/algorithms/sac.html) | Why a policy may exploit a reward, why discounted return differs from progress, and why training feedback can improve actions without improving the intended outcome. Revisit this alongside later readings. |
| 3 | [OpenVLA](https://openvla.github.io/) | Architecture, inputs/actions, training data and adaptation overview | What makes a model a VLA; how this differs from a VLM giving goals to a separate RL controller. You need not train a large VLA to understand the distinction. |
| 4 | [Hi Robot](https://arxiv.org/abs/2502.19417) | Method diagram, high/low-level interface, one evaluation table | What the planner decides, what the controller must already know how to do, and which errors cannot be fixed by better language planning. |
| 5 | [GVL — Vision Language Models are In-Context Value Learners](https://arxiv.org/abs/2411.04549) | Method and shuffled-frame argument | How semantic progress differs from chronology; whether an evaluation has access to future frames that a live robot would not have. |
| 6 | [ReWiND](https://arxiv.org/abs/2505.10911) | Reward learning, rewinding, and offline-to-online policy learning | How progress can decrease; what supervision is needed; why reversed videos may not cover actual physical failures. |
| 7 | [Robometer](https://arxiv.org/html/2603.02115v2) | Deep read: method, limitations, reward evaluation, Appendix E.1 | How progress and success are trained, why it is close to our proposal, and what the non-VLA SAC experiment already establishes. Keep a list of claims we therefore cannot call new. |
| 8 | [StructRL](https://arxiv.org/html/2609.36352v1) | Method and predicate-grounding appendix | How prerequisites and intermediate rewards are represented; which information comes from simulator state; whether “was achieved” and “still holds” are treated differently. Answer from the paper, not the title. |

First reading session: ACT overview and the basic policy/reward distinction. First idea-generating session after that: GVL versus ReWiND, asking how each knows that a robot moved backward. Robometer gets an early abstract/figure skim to establish overlap, then the deep read at step 7. No simulator installation is required for these sessions.

## Read next according to the idea

| Idea / missing concept | Reading | Question to carry into the paper |
| --- | --- | --- |
| Active verification and explicit task conditions | [ReKep](https://rekep-robot.github.io/) | Can relations between keypoints express the relevant success condition? What hidden condition cannot be represented from visible geometry alone? |
| Lasting completion | [SafeStage](https://arxiv.org/abs/2609.21223) | How does it distinguish nominal success from an unacceptable final state, and what would our question add? |
| Trusting extra context | [Causal Confusion in Imitation Learning](https://arxiv.org/abs/1905.11979) | Why can more observations worsen behavior? What intervention distinguishes a useful cue from a shortcut? |
| Reward from language comparisons | [RL-VLM-F](https://arxiv.org/abs/2402.03681) | Does knowing which of two observations is better tell us that either is complete? |
| Goal images and value representations | [LIV](https://proceedings.mlr.press/v202/ma23b.html) | How are language/image goals and values connected? Which conclusions depend on the training distribution? |
| Correct reward shaping | [Ng, Harada & Russell, 1999](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf) | Under which conditions does adding a potential difference preserve the optimal policy, and what happens when we change goals or clip negative reward? |

After we pick a candidate, add a targeted foundational reading on active perception/POMDPs, temporal task logic, or diagnosis as appropriate. The conceptual connection alone does not substitute for reviewing those fields. Diffusion Policy, pi0/pi0.5, HAMSTER, tactile models, world models and underwater simulation are valuable later branches; they are not all prerequisites to choosing a question.

## The note to produce for each paper

Use the existing [paper-note template](../../methods/literature-note-template.md), with five required answers:

1. What specific problem does it solve?
2. What information and labels does it receive during training versus execution?
3. What is the central mechanism, in a small diagram or your own equation?
4. Which experiment supports the main claim, and which competing explanation remains?
5. What does this rule out as our novelty, and what new question does it suggest?

Keep reading states separate: queued, overview, methods read, full paper, code inspected, reproduced. An abstract is enough to decide relevance; it is not enough to assess the decisive experimental details. I can explain a paper, ask you to teach it back, correct misunderstandings and preserve the resulting note. The user should still engage with the figures and claims directly.

## Readiness to formulate the project

You are ready to choose a first research question when you can explain the following without relying on model names:

- Policy, reward model, value function, planner and verifier: who does what?
- Why good-looking progress can coexist with failure, and why some hidden states require another observation or action.
- What “unfamiliar” means for the proposed task: appearance, object, mechanism, instruction or composition.
- What Robometer/StructRL/ReWiND already do that our work cannot claim as new.
- Which information the robot may use and which truth is reserved for evaluation.
- The simplest competing method and one result that would falsify our idea.

This is an understanding gate, not a demand to master every derivation or complete the library before starting research.

## Source status

ACT/OpenVLA/Hi Robot and course pages were inspected at overview level in prior turns; Robometer/StructRL at selective methods/appendix depth as recorded in related-work.md. GVL abstract, ReWiND author method page, and SafeStage abstract were newly checked on 2026-10-23. Branch readings draw on the prior source review; none is claimed reproduced. No exhaustive latest-paper survey or independent critic review was performed for this ideation note.

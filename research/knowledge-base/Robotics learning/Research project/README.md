# Robotics-learning research project

This folder is where the collected context will be turned into a concrete project. The current material points toward a project about how robot policies should reason, learn from experience, and recover when they encounter unfamiliar states.

## Repeated themes in the material

1. **Imitation learning versus reinforcement learning.** Behavior cloning and diffusion policies are data-efficient starting points, while RL provides outcome-based improvement and recovery from states outside demonstrations.
2. **End-to-end VLA policies versus modular planning.** The notes compare direct image-to-action models with systems that combine a VLM planner, visual foresight or a world model, and an action generator.
3. **Language reasoning versus visual reasoning.** CoT-VLA, ForAct, ECOT, and related systems suggest different representations for subgoals and future states.
4. **Data and generalization.** Human video, robot demonstrations, simulation, web pretraining, deployment data, and autonomous collection each trade off scale, embodiment mismatch, and supervision quality.
5. **Evaluation and failure recovery.** Open-world evaluation, causal confusion, history, memory, and interactive corrections appear repeatedly as unresolved problems.
6. **Safety at the model boundary.** The separate AI-safety material on alignment and adversarial attacks may matter when language instructions, tool use, or external models influence robot actions.

## Candidate research directions

- Compare visual subgoal prediction with language chain-of-thought for long-horizon manipulation, especially under distribution shift.
- Add outcome feedback or lightweight online RL to a behavior-cloned VLA and measure recovery from failed or perturbed trajectories.
- Study a modular closed loop in which a VLM plans, a video/world model predicts future observations, and a VLA executes actions.
- Test whether explicit memory or causal state history reduces compounding errors in imitation-learned policies.
- Evaluate camera-only policies against policies with force or tactile signals on contact-rich tasks.

## Next artifacts

- `project-brief.md`: problem, hypothesis, scope, and expected contribution.
- `literature-map.md`: paper summaries grouped by research question and method.
- `experiment-plan.md`: tasks, baselines, metrics, datasets, compute, and failure analysis.
- `decision-log.md`: choices made while narrowing the project.

Start with ACT, then use the discussion pairs in the paper list to decide which tradeoff is both interesting and feasible to test.

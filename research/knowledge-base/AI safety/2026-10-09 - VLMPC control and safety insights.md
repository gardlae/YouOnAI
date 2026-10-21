# VLMPC control and safety insights

Source: [Granola note](https://notes.granola.ai/d/c4fe238e-82b0-4927-b779-77711cc059b0)  
Date: 2026-10-09

### Paper 1: Modular Robotics with VLMs (Red Team)

- Modular design lets each component specialize to its strengths
- VLM labels constraints with higher accuracy than automated labeling
- Structures (e.g., trajectory-following models) reused out of the box
- Improving VLMs directly improves task success rate downstream

### Paper 2: VLMPC (VLM + Model Predictive Control)

- VLM proposes a mean action vector; MPC samples and ranks candidates
- Video prediction model generates future frames for each sampled action
- Two cost functions rank action sequences:
  - Pixel cost: frame-to-goal image distance
  - VLM-assisted cost: sub-goal tracking via bounding boxes, obstacle avoidance
- 70% success rate on “move to area” task with 50 random initializations
- Ablation: pixel-only cost achieves near zero; VLM is essential
- Limitation: pixel cost breaks when camera is mounted on the arm (perspective shifts)

### Papers 3–5: End-to-End Learning (Blue Team)

- VLM for VLA: better VLMs don’t reliably produce better VLAs
  - Weak negative correlation in 2 of 3 environments
  - Fine-tuning on embodiment-specific tasks (segmentation, spatial) doesn’t help
  - Vision encoder is the most mismatched component: freezing it drops performance 20–40 points
  - Language/word embeddings barely affected when frozen
- Aloha: end-to-end handles fine-grained contact tasks cheaply
  - Under $20k hardware, ~50 demos per task, ~10 min of teleop data
  - 5 hours on one GPU; 88–96% success on fine-grained manipulation
  - Shows learning policy can be simpler than modeling task dynamics
- RT2: end-to-end scales with model size
  - Actions tokenized as 256-bin integers; co-fine-tuned on web VQA + robot demos
  - On familiar tasks: matches RT1 (~91–93%)
  - On unseen tasks: RT1 drops to 32%, RT2 holds at 62%
  - 5B vs. 55B: larger model significantly outperforms on robotics tasks

### Safety and Model-Based Arguments

- Current end-to-end models have very low safe completion rates
  - Oopsieverse benchmark: frontier models hit 92% task completion but only 4–8% safe completion
  - Example: VLA slams dishwasher, shoves items in without checking space
- Safety filter architecture: monitor, fallback, intervention layer over any policy
  - Three classical methods: Hamiltonian/Jacobian reachability, control barrier functions (CBF), MPC/predictive filtering
  - CBF enforces invariance conditions but hard to verify at scale
  - MPC gives guarantees only if the dynamics model is accurate; runtime compute is costly
- VLMs can expand CBF/MPC coverage via object recognition and semantic reasoning
- Defense-in-depth argument: layered safety components needed before household deployment
- Household robots face semantic safety (dirty vs. clean surfaces, child commands) that AV-style collision avoidance doesn’t cover

### Interface Debate: End-to-End vs. Modular

- End-to-end position: learned latent representations are more flexible and trainable than explicit interfaces
  - Action objective reshapes vision encoder in ways image-only training doesn’t
  - If data is sufficient, fully learned is strictly better
- Modular/practical position: physical latency forces a two-component architecture
  - Cloud model: better planning, slower (1–3 Hz); edge model: high-frequency local control (~50 ms)
  - Interface between them can still be a learned latent, not necessarily English commands
- Action chunking on edge device can bridge the latency gap
- Key open question: should cloud-to-edge communication use latent representations or language commands?

### AV Analogy and Scaling Discussion

- AV trend: stacks have moved from SLAM + MPC toward end-to-end trajectory generation over ~10 years
- Lower-dimensional action space (2D plane, brake + steer) makes end-to-end more sample-efficient for AVs
- Counterpoint: smaller action space also makes MPC search more tractable
- For humanoids (29 DoF+): model-based rollout becomes very hard to hand-design; learned policies may scale better
- Data quality matters: dirty training data (e.g., aggressive lane-cutting behavior) propagates into end-to-end policies
- Frontier model access: co-training with GPT-class models is currently impossible (opaque endpoints); limits pure end-to-end argument
- Test-time compute / reasoning models framed as implicit model-based planning, a potential synthesis of both camps
- Code-as-policy angle: structured code representation enables fuzzing, concolic execution, and formal verification for safety


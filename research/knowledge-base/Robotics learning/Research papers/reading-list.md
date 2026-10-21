# Learning VLA research-paper list

Imported from the Notion **Learning VLA** tracker on 2026-10-21. The checkbox state and order mirror the source database. Each title links to its Notion entry, where source links and reading notes can be maintained.

Source: [Learning VLA](https://app.notion.com/p/3f13ed51cad381cca39bddfa38467993)

## Start here (1)

- [ ] [01. ACT — Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://app.notion.com/3f13ed51cad3815e9f09f195633d6979)

## Discussion (30)

- [ ] [REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation](https://app.notion.com/3f23ed51cad3813484c1f350f12a94ca)
  - Topic: What’s the best way to use simulators (non-RL usage only)
- [ ] [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://app.notion.com/3f23ed51cad3817db5f7d9376f558281)
  - Topic: What’s the best way to use simulators (non-RL usage only)
- [ ] [π*0.6: a VLA That Learns From Experience](https://app.notion.com/3f23ed51cad381719eb4c22383f6e2a1)
  - Topic: Sim2real vs. real RL: RL can be done in sim or in the real world. Which is better
- [ ] [DrEureka: Language Model Guided Sim-To-Real Transfer](https://app.notion.com/3f23ed51cad381b499f2ffca0206e7a9)
  - Topic: Sim2real vs. real RL: RL can be done in sim or in the real world. Which is better
- [ ] [A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation](https://app.notion.com/3f23ed51cad381d38056d8fbbad86835)
  - Topic: Web pretraining vs. LBM-style direct robot training: Some robot foundation models pretrain on data from the web in a 2-step manner (e.g., VLAs trained from VLMs), while others are trained mostly from scratch (e.g., LBMs). Which approach is the right one
- [ ] [16. OpenVLA: An Open-Source Vision-Language-Action Model](https://app.notion.com/3f13ed51cad381a2af47c7509cc6f2c7)
  - Topic: Web pretraining vs. LBM-style direct robot training: Some robot foundation models pretrain on data from the web in a 2-step manner (e.g., VLAs trained from VLMs), while others are trained mostly from scratch (e.g., LBMs). Which approach is the right one
- [ ] [VLMPC: Vision-Language Model Predictive Control for Robotic Manipulation](https://app.notion.com/3f23ed51cad381618d89def12cb0d152)
  - Topic: End-to-end vs. traditional model-based methods: VLAs are classically trained end-to-end (from images to actions), but it’s also possible to use foundation models as part of more traditional model-based pipelines, including planners, primitives, or other hand-designed “traditional” components. Which approach is better
- [ ] [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://app.notion.com/3f23ed51cad381b686f0cacdba51e52a)
  - Topic: End-to-end vs. traditional model-based methods: VLAs are classically trained end-to-end (from images to actions), but it’s also possible to use foundation models as part of more traditional model-based pipelines, including planners, primitives, or other hand-designed “traditional” components. Which approach is better
- [ ] [How Claude Performs on Robotics Tasks](https://app.notion.com/3f23ed51cad3817390a6ce2edd29de1c)
  - Topic: Do code-as-policies/coding agents solve robotics
- [ ] [RHO: Your Coding Agent is Secretly a Roboticist](https://app.notion.com/3f23ed51cad38160b498c7c2dd2ef94d)
  - Topic: Do code-as-policies/coding agents solve robotics
- [ ] [World Action Models are Zero-shot Policies](https://app.notion.com/3f23ed51cad381f8810bd344bba5a067)
  - Topic: VLA vs. VAM: VAMs use video models as the backbone for a policy, while VLAs use vision-language models. Which is better
- [ ] [Cosmos 3: Omnimodal World Models for Physical AI](https://app.notion.com/3f23ed51cad381e28b6bcb0103740baf)
  - Topic: VLA vs. VAM: VAMs use video models as the backbone for a policy, while VLAs use vision-language models. Which is better
- [ ] [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](https://app.notion.com/3f23ed51cad3815a841bf9b79555004a)
  - Topic: World models as simulators: yes or no
- [ ] [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://app.notion.com/3f23ed51cad3810b9a97c90f89dc9b69)
  - Topic: World models as simulators: yes or no
- [ ] [Learning Visuotactile Skills with Two Multifingered Hands](https://app.notion.com/3f23ed51cad38173a6d8e2ea7b55b7ce)
  - Topic: Hands vs. grippers: Multi-fingered hands can perform complex manipulation, but are harder to control. Is it better to focus on multi-fingered hands or simpler parallel-jaw grippers
- [ ] [DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control](https://app.notion.com/3f23ed51cad381e0ba2ce4a60e84b9fa)
  - Topic: Hands vs. grippers: Multi-fingered hands can perform complex manipulation, but are harder to control. Is it better to focus on multi-fingered hands or simpler parallel-jaw grippers
- [ ] [3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://app.notion.com/3f23ed51cad381f1b772c90eb6722c34)
  - Topic: Camera-only sensing vs. more sensing (touch, force, etc.): Should VLAs be vision/camera-centric (as in Tesla), or should they actively incorporate other modalities such as force and tactile sensing
- [ ] [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://app.notion.com/3f23ed51cad381fbb2b0ddc0cc6ab00a)
  - Topic: Camera-only sensing vs. more sensing (touch, force, etc.): Should VLAs be vision/camera-centric (as in Tesla), or should they actively incorporate other modalities such as force and tactile sensing
- [ ] [So You Think You Can Scale Up Autonomous Robot Data Collection?](https://app.notion.com/3f23ed51cad3818c9240ff9875a8defd)
  - Topic: Imitation learning vs. reinforcement learning: RL is cool but notoriously tricky and less sample-efficient. Do we really need RL, or would imitation learning (with DAgger, etc.) suffice
- [ ] [05. HG-DAgger: Interactive Imitation Learning with Human Experts](https://app.notion.com/3f13ed51cad3812585d7c6755a77e4d2)
  - Topic: Imitation learning vs. reinforcement learning: RL is cool but notoriously tricky and less sample-efficient. Do we really need RL, or would imitation learning (with DAgger, etc.) suffice
- [ ] [Unified Vision-Language-Action Model](https://app.notion.com/3f23ed51cad381cca570e11594a343f9)
  - Topic: Flow/diffusion vs. tokens: Today’s VLAs mostly use flow/diffusion models for action experts. In 2030, will this trend continue, or will they be replaced by tokenized actions as in LLMs
- [ ] [Ordered Action Tokens for Visuomotor Policy Learning](https://app.notion.com/3f23ed51cad381939510c3c0b41c330d)
  - Topic: Flow/diffusion vs. tokens: Today’s VLAs mostly use flow/diffusion models for action experts. In 2030, will this trend continue, or will they be replaced by tokenized actions as in LLMs
- [ ] [Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://app.notion.com/3f23ed51cad38112bf0bece47d7b4896)
  - Topic: Where do we find data
- [ ] [EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos](https://app.notion.com/3f23ed51cad3817f97a4f38ff673baaa)
  - Topic: Where do we find data
- [ ] [Causal Confusion in Imitation Learning](https://app.notion.com/3f23ed51cad381a18109e6a5e5b972ef)
  - Topic: How should we handle history
- [ ] [MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://app.notion.com/3f23ed51cad3814abef3ff789f24dff5)
  - Topic: How should we handle history
- [ ] [Robotic Control via Embodied Chain-of-Thought Reasoning](https://app.notion.com/3f23ed51cad3813492e9c3c4182c9163)
  - Topic: Language-based vs. vision-based reasoning: Should robot reasoning be mainly based on language, vision, or something else (e.g., latent reasoning)
- [ ] [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://app.notion.com/3f23ed51cad38162aa5cc7213656d51e)
  - Topic: Language-based vs. vision-based reasoning: Should robot reasoning be mainly based on language, vision, or something else (e.g., latent reasoning)
- [ ] [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](https://app.notion.com/3f23ed51cad38160a209c27b6e540887)
  - Topic: Should robotics research be demo-driven or benchmark-driven
- [ ] [What Are We Actually Benchmarking in Robot Manipulation?](https://app.notion.com/3f23ed51cad3810b9cfdc3699590724e)
  - Topic: Should robotics research be demo-driven or benchmark-driven

## Additional reading (46)

- [ ] [02. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://app.notion.com/3f13ed51cad3811cb78af5e93efb79f3)
  - Topic: Algorithms
- [ ] [EgoMimic: Scaling Imitation Learning via Egocentric Video](https://app.notion.com/3f23ed51cad381158278e52ed938318d)
  - Topic: Human videos
- [ ] [Emergence of Human to Robot Transfer in Vision-Language-Action Models](https://app.notion.com/3f23ed51cad381509024d90aea453421)
  - Topic: Human videos
- [ ] [Yell At Your Robot: Improving On-the-Fly from Language Corrections](https://app.notion.com/3f23ed51cad38168993dd2b206d68d40)
  - Topic: Reasoning
- [ ] [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://app.notion.com/3f23ed51cad381c4bdf3f4159536c008)
  - Topic: Reasoning
- [ ] [PaLM-E: An Embodied Multimodal Language Model](https://app.notion.com/3f23ed51cad38127ac4ae61a3e20d568)
  - Topic: Reasoning
- [ ] [Vision Language Models are In-Context Value Learners](https://app.notion.com/3f23ed51cad381078a31d3d833bfb20e)
  - Topic: RL
- [ ] [πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models](https://app.notion.com/3f23ed51cad3817ebeeec7fd2b11ca64)
  - Topic: RL
- [ ] [Steering Your Diffusion Policy with Latent Space Reinforcement Learning](https://app.notion.com/3f23ed51cad38146ad8cd7dd5a0fda86)
  - Topic: RL
- [ ] [RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://app.notion.com/3f23ed51cad38175be90d87046b89425)
  - Topic: RL
- [ ] [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://app.notion.com/3f23ed51cad381a3a175ecaa64cdb6f4)
  - Topic: RL
- [ ] [Refined Policy Distillation: From VLA Generalists to RL Experts](https://app.notion.com/3f23ed51cad381d99760d160f5e8d21f)
  - Topic: RL
- [ ] [Diffusion Policy Policy Optimization](https://app.notion.com/3f23ed51cad381d89ea0f2abb2868ccb)
  - Topic: RL
- [ ] [VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning](https://app.notion.com/3f23ed51cad38141b45cd128f05479d3)
  - Topic: RL
- [ ] [ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy](https://app.notion.com/3f23ed51cad381b98daad6a72721a5f1)
  - Topic: RL
- [ ] [MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation](https://app.notion.com/3f23ed51cad381ad940aeefa57a9c2d1)
  - Topic: Simulators
- [ ] [Interactive World Simulator for Robot Policy Training and Evaluation](https://app.notion.com/3f23ed51cad381469903c9729e8531ed)
  - Topic: Simulators
- [ ] [HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation](https://app.notion.com/3f23ed51cad381dcae8dddf7e6774938)
  - Topic: Steering and conditioning
- [ ] [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://app.notion.com/3f23ed51cad3814882a7e29d99252307)
  - Topic: Steering and conditioning
- [ ] [CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models](https://app.notion.com/3f23ed51cad381789c76d603276ee334)
  - Topic: Steering and conditioning
- [ ] [19. SayCan — Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://app.notion.com/3f13ed51cad381108b54da2c50a828a9)
  - Topic: Steering and conditioning
- [ ] [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://app.notion.com/3f23ed51cad381e9b43dd360cec13e8c)
  - Topic: Steering and conditioning
- [ ] [TiPToP: A Modular Open-Vocabulary Robot Manipulation System That Plans](https://app.notion.com/3f23ed51cad3813badfffe6819e827ba)
  - Topic: Steering and conditioning
- [ ] [RoboCLIP: One Demonstration is Enough to Learn Robot Policies](https://app.notion.com/3f23ed51cad381b4943eea2090906eee)
  - Topic: Steering and conditioning
- [ ] [20. Code as Policies: Language Model Programs for Embodied Control](https://app.notion.com/3f13ed51cad381dba09ac1ebecc48f4d)
  - Topic: Steering and conditioning
- [ ] [RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches](https://app.notion.com/3f23ed51cad381c3bbb7c83380290ba8)
  - Topic: Steering and conditioning
- [ ] [VIMA: General Robot Manipulation with Multimodal Prompts](https://app.notion.com/3f23ed51cad3817ba4abc65fa442ae0c)
  - Topic: Steering and conditioning
- [ ] [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://app.notion.com/3f23ed51cad381e986b8ed78fbb9607c)
  - Topic: Video models
- [ ] [Unified Video Action Model](https://app.notion.com/3f23ed51cad3812da1a3ed21f195c660)
  - Topic: Video models
- [ ] [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](https://app.notion.com/3f23ed51cad3817fb793c88984921376)
  - Topic: Video models
- [ ] [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://app.notion.com/3f23ed51cad38113812ccef8ee96f2d0)
  - Topic: Video models
- [ ] [mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs](https://app.notion.com/3f23ed51cad38164b991f41dab951f47)
  - Topic: Video models
- [ ] [OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning](https://app.notion.com/3f23ed51cad381bba4fac2d87bb317d3)
  - Topic: Video models
- [ ] [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://app.notion.com/3f23ed51cad381ec83f0f82c65b081ac)
  - Topic: VLA
- [ ] [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://app.notion.com/3f23ed51cad38132ad6bd1e63e6ec710)
  - Topic: VLA
- [ ] [14. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://app.notion.com/3f13ed51cad381ad9e65d0927df33f53)
  - Topic: VLA
- [ ] [Gemini Robotics: Bringing AI into the Physical World](https://app.notion.com/3f23ed51cad38138b2eeccd2cfc4dc06)
  - Topic: VLA
- [ ] [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://app.notion.com/3f23ed51cad381809b97f1845d254fb2)
  - Topic: VLA
- [ ] [18. π0.5: a Vision-Language-Action Model with Open-World Generalization](https://app.notion.com/3f13ed51cad381b6bb32d66538dbfa82)
  - Topic: VLA
- [ ] [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](https://app.notion.com/3f23ed51cad38173b66bcba93b5f2ea0)
  - Topic: VLA
- [ ] [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://app.notion.com/3f23ed51cad3818fa918d7a6cb05571a)
  - Topic: VLA
- [ ] [17. π0: A Vision-Language-Action Flow Model for General Robot Control](https://app.notion.com/3f13ed51cad3811e8367f7dbe457f271)
  - Topic: VLA
- [ ] [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://app.notion.com/3f23ed51cad38167934ee054ff181788)
  - Topic: VLA
- [ ] [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://app.notion.com/3f23ed51cad381ae8601c0c70c0e728a)
  - Topic: VLA
- [ ] [TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation](https://app.notion.com/3f23ed51cad381f099a9f9a3ba5581ac)
  - Topic: VLA
- [ ] [12. Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://app.notion.com/3f13ed51cad38176bd34f6b7531ce543)
  - Topic: VLA

## Earlier suggestions (11)

- [ ] [03. Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://app.notion.com/3f13ed51cad381f4be39f5424886c3f6)
- [ ] [04. DAgger — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://app.notion.com/3f13ed51cad3811c9fdad82135c00c84)
- [ ] [06. Advantage-Weighted Regression: Simple and Scalable Off-Policy Reinforcement Learning](https://app.notion.com/3f13ed51cad3814d9fcdc343358efd6f)
- [ ] [07. AWAC: Accelerating Online Reinforcement Learning with Offline Datasets](https://app.notion.com/3f13ed51cad38159bb07e00e8b0aa75d)
- [ ] [08. Conservative Q-Learning for Offline Reinforcement Learning](https://app.notion.com/3f13ed51cad381a9b940f86215f95daa)
- [ ] [09. Offline Reinforcement Learning with Implicit Q-Learning](https://app.notion.com/3f13ed51cad381f1964df4f01063fa6e)
- [ ] [10. BridgeData V2: A Dataset for Robot Learning at Scale](https://app.notion.com/3f13ed51cad3812ba024ecc1c06ddf34)
- [ ] [11. DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://app.notion.com/3f13ed51cad38135803dece46df20ad1)
- [ ] [13. RT-1: Robotics Transformer for Real-World Control at Scale](https://app.notion.com/3f13ed51cad38170ad0fffb271644602)
- [ ] [15. Octo: An Open-Source Generalist Robot Policy](https://app.notion.com/3f13ed51cad381919dd7d8bf4b7da1a7)
- [ ] [21. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://app.notion.com/3f13ed51cad381f1b69ce73d89237224)



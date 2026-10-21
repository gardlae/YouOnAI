# CLT VOA and visual reasoning

Source: [Granola note](https://notes.granola.ai/d/9a984232-238b-446c-9b87-ba7678b774f9)  
Date: 2026-10-21

## Core Claims Framing the Debate

- Three claims motivate visual reasoning in VLAs:
  - Claim 1: goal images are less ambiguous than text for spatial tasks
  - Claim 2: visual reasoning can train from action-free video (cheap, abundant)
  - Claim 3: separating planning (language/vision) from control (policy) improves performance
- Red team’s counter: language reasoning offers compositionality, debuggability, and reuse across scenes

## COT-VLA: Chain-of-Thought via Future Frame Prediction

- Predicts next N frames before sampling action tokens, all within one model
- Two-dataset training strategy:
  - Pre-training on large action-free video (dataset DBE): predict next frames from observation + instruction
  - Post-training on robot demos: predict action tokens conditioned on predicted frames
- Attention design: causal attention for text/vision tokens, flow attention for actions (parallel generation)
- Results vs. OpenVLA baseline:
  - ~10% average improvement, larger gains on multi-instruction tasks
  - Removing pre-training drops success rate ~25%
  - COT alone contributes at least 6% of the performance gain

## ForAct: Visual Sub-Goal Planning as a Plug-in

- Separate image generator sits on top of existing VLA (pi0, pi0.5), no architecture change
- Three-model loop: VLA planner (next subtask text) → image generator (predicted scene) → VLA actor (subtask text + predicted image)
- Image generator trained on 1.16M subtask pairs; runs in 0.33s per frame on a single H100
- Key results:
  - pi0 alone: 46.5% → adding subtask text: 57.1% → adding predicted image: 87.6%
  - Image vs. best text (with location encoding): 93.4% vs. 46.8% on ambiguous pick task
  - +30-point gain holds on stronger pi0.5 baseline (70.3% → 88.2%)
- Off-the-shelf image editors (Gemini, GPT) rejected: physically plausible but geometrically wrong

## Language-Based Reasoning: ECOT and 1-2-VLA

- ECOT generates grounded textual reasoning (scene description, plan, subtask, movement) before action
  - Training data: 2.5M transitions auto-labeled in 7 days using vision models + LM
  - Results: +22% in-distribution, +34% OOD vs. OpenVLA
  - COT enables failure diagnosis: model labeled hammer as screwdriver, visible in reasoning trace
  - Speed fix: reuse high-level reasoning every 5 steps → 72% success vs. 33% (every step), 24% speedup
- 1-2-VLA: adaptive reasoning, only at critical moments
  - Two special tokens: beginning-of-reasoning vs. beginning-of-action; model decides at each step
  - Training data generated with Gemini 2.5 Pro to label subtask intervals and reasoning context
  - Results vs. pi0 (57%) and dual-system (63%): 1-2-VLA achieves 87%
  - Error recovery: 80% vs. 58% (dual system); human correction mid-task: 100% vs. 65%
  - Visual grounding generalizes to open world only when language reasoning + visual understanding data are combined

## Why Does Reasoning Work? Hypotheses and Evidence

- Three hypotheses tested in the ECOT analysis paper:
  1. Reasoning helps the model internalize richer feature correlations during training (beneficial even without test-time reasoning)
  2. Decomposed subtasks make learning easier
  3. Extra tokens provide more compute regardless of content
- Experimental findings:
  - Hypothesis 1 supported in simulation: pre-training with reasoning then dropping it still outperforms standard VLA
  - Hypothesis 2 rejected: providing decomposed reasoning as input without training on it doesn’t help
  - Hypothesis 3 rejected: padding/filler tokens perform worse than no reasoning at all
  - Real-robot results still degrade without test-time reasoning, even under Hypothesis 1 conditions
- Parallel from FAST: training with video generation but not generating at test time also supports Hypothesis 1

## Open Questions and Discussion

- Inference cost tradeoff: COT-VLA is 7x slower; ForAct adds 0.33s/frame; 1-2-VLA mitigates with adaptive triggering
  - Proposed metric: successful rollouts per hour rather than raw token throughput
  - Consensus: 0.33s number not to be taken seriously as it uses unoptimized base diffusion models
- Implicit visual reasoning: training continuous latent reasoning (Coconut-style) for vision is unsolved even in language models
- Letting the model choose modality: proposal to train on both visual and language reasoning traces, then use RL to let the model learn which to use
- Synthetic reasoning data: useful for domain-specific fine-tuning but not scalable for large model development; off-policy data hurts in RL stage
- Visual reasoning generalizes less than language reasoning to unseen settings; combining both modalities closes the gap
- Action-space reasoning: generating action trajectories as intermediate tokens is possible but requires a verifier; Best-of-M with a video model as value function is one existing approach

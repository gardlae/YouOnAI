# Current context

Updated: 2026-10-23 (America/Los_Angeles).

## Objective and user preferences

Target a high-quality simulation-only robotics research paper first, with reproducible open-source research code. User wants to learn RL and study modern VLA papers together. Real-world testing is outside the initial scope. Focus: understanding unfamiliar scenes and deciding when a task is actually finished. Proposed architecture uses image/text subgoals and a low-level RL controller, not necessarily a direct VLA. Progress should decrease after mistakes; cost normally increases.

The primary assistant is the conversation partner/coordinator. Save substantive discussion to GitHub. Keep usage sustainable: selective bounded agents, compact context, no automatic credit retries. User has Linux with NVIDIA 5070; variant/VRAM/runtime not inspected. Cloud compute is an option with budget still undecided.

## Current preparation

Start at research/projects/verified-subgoal-rl/README.md. It links simulator research, related work, method, evaluation, learning path and paper/release plan. Latest conversation: research/discussions/2026-10-23-simulation-paper-preparation.md. experiments/progress-signal-sanity/ contains an executable synthetic arithmetic exercise; seven tests pass. No simulator or trained method exists yet.

Close overlap: Robometer already predicts progress/success and trains non-VLA SAC on LIBERO tasks. StructRL already supplies structured subtask rewards. Broad architecture and decreasing progress are not novel by themselves. Candidate empirical question: completion risk and progress reversals under held-out scene/near-success changes at matched budgets. First reproduce/test existing models; select a correction only after a persistent gap appears. No novelty or state-of-the-art claim established.

ManiSkill is the conditional general RL starting choice. For faithful Robometer reproduction, prefer its LIBERO setup and avoid adding a second stack by default. Isaac Lab is an alternative whose backend/version matters. Underwater/Stonefish is a later extension, not a required first milestone. Do not assume simulation establishes real-world reliability.

## Next work

Inspect the Linux GPU environment and choose one pinned simulator/protocol; run RGB reset/step and a tiny native-reward control baseline before large training. Begin ACT for learning and Robometer for project overlap. Use the learning-path gates and teach-back notes; not all 88 papers must be completed before the pilot. No cloud purchases authorized by willingness alone; cost a specific batch first.

## Sources and operational limits

Knowledge base: 23 Granola records, 199 lecture images classified using samples, Learning VLA and 88 paper entries. Not exhaustive OCR or completed paper reviews. Notion overview re-fetched during preparation; individual reading statuses were not re-audited or changed. Earlier physical-AI and underwater briefs remain exploratory; latest scope takes precedence. Exact Anthropic ten-year attribution remains unverified.

Both latest research agents left drafts/findings then hit workspace-credit errors. Coordinator integrated them; no independent critic review or live named-role loading verified. Do not retry automatically. No remote hardware access, simulator install, weight download, GPU training, or cloud purchase occurred.

The repo includes personal/third-party source archives. Prepare a separable public research package; no blanket relicensing or visibility change was made. Preserve pre-existing untracked duplicate files and stage explicit paths only. Credentials and active sessions do not sync through Git.

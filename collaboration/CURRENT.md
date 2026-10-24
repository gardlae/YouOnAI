# Current context

Updated: 2026-10-23 (America/Los_Angeles).

## Objective and user preferences

Target a high-quality simulation-only robotics research paper first, with reproducible open-source research code. User wants to learn RL and study modern VLA papers together. Real-world testing is outside the initial scope. Focus: understanding unfamiliar scenes and deciding when a task is actually finished. Proposed architecture uses image/text subgoals and a low-level RL controller, not necessarily a direct VLA. Progress should decrease after mistakes; cost normally increases.

The primary assistant is the conversation partner/coordinator. Save substantive discussion to GitHub. Keep usage sustainable: selective bounded agents, compact context, no automatic credit retries. User has Linux with NVIDIA 5070; variant/VRAM/runtime not inspected. Cloud compute is an option with budget still undecided.

## Current preparation

Immediate coursework: two eventual PDFs; do not generate yet. research/coursework/ai-partnership/governance-draft.md holds a short disclosure. project-ideas-draft.md now proposes underwater completion uncertainty, robot-method comparison difficulty, and anchored AI brainstorming, with stakeholders, need hypotheses and disclosure. These are AI-organized options, not final user choices. Peer-pod input remains missing. User reports that AI struggles to broaden beyond their prior framing; preserve that criticism. Reflection wording was drafted from their account in chat. See research/discussions/2026-10-23-coursework-disclosure.md.

Latest revision: user requested a fully written half-page governance draft. Shortened in place; user can edit via GitHub. Fetch/pull remote edits before revising it again; no simultaneous-editing guarantee.

Current stage is ideation: user explicitly wants more conceptual discussion before implementation. Start at research/projects/verified-subgoal-rl/ideation.md and reading-for-ideation.md. Latest discussion: research/discussions/2026-10-23-ideation-and-reading.md. Earlier simulator/method plans remain provisional. The synthetic signal exercise passes seven tests; no simulator or trained method exists yet.

Close overlap: Robometer already predicts progress/success and trains non-VLA SAC on LIBERO tasks. StructRL already supplies structured subtask rewards. Broad architecture and decreasing progress are not novel by themselves. Candidate empirical question: completion risk and progress reversals under held-out scene/near-success changes at matched budgets. First reproduce/test existing models; select a correction only after a persistent gap appears. No novelty or state-of-the-art claim established.

ManiSkill is the conditional general RL starting choice. For faithful Robometer reproduction, prefer its LIBERO setup and avoid adding a second stack by default. Isaac Lab is an alternative whose backend/version matters. Underwater/Stonefish is a later extension, not a required first milestone. Do not assume simulation establishes real-world reliability.

## Next work

Keep implementation parked. Discuss four hypotheses: active physical verification, recovering invalidated subgoal conditions, durable completion, and resolving misleading context. None is selected or established as novel. Begin ACT and RL foundations; then OpenVLA, Hi Robot, GVL, ReWiND, Robometer and StructRL with teach-back notes. New GVL/ReWiND/SafeStage checks are overview-level. Readiness means explaining the mechanism, closest prior work, simplest baseline and falsifying result—not finishing all 88 papers. No cloud purchases authorized by willingness alone.

## Sources and operational limits

Knowledge base: 23 Granola records, 199 lecture images classified using samples, Learning VLA and 88 paper entries. Not exhaustive OCR or completed paper reviews. Notion overview re-fetched during preparation; individual reading statuses were not re-audited or changed. Earlier physical-AI and underwater briefs remain exploratory; latest scope takes precedence. Exact Anthropic ten-year attribution remains unverified.

Both latest research agents left drafts/findings then hit workspace-credit errors. Coordinator integrated them; no independent critic review or live named-role loading verified. Do not retry automatically. No remote hardware access, simulator install, weight download, GPU training, or cloud purchase occurred.

The repo includes personal/third-party source archives. Prepare a separable public research package; no blanket relicensing or visibility change was made. Preserve pre-existing untracked duplicate files and stage explicit paths only. Credentials and active sessions do not sync through Git.

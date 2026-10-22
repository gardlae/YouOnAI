# Current context

Updated: 2026-10-22 (America/Los_Angeles).

## Intent and stage

Develop a robotics research project through extended discussion, eventually leading to experiments and possible products. No project has been selected. The user talks to the coordinator; agents perform bounded execution and independent review when warranted. Usage must remain sustainable: discussion stays with the coordinator and delegation is selective.

## Context available

- research/knowledge-base/: 23 Granola records, 199 original lecture images, and Learning VLA with 88 linked paper-tracker entries. The images were categorized using samples; this is not exhaustive OCR. Paper entries are a reading queue, not 88 completed paper reviews.
- research/projects/: physical-AI capability-gap and underwater-VLA simulation briefs. These are exploratory proposals.
- research/discussions/: ongoing reasoning, hypotheses, sources, and questions.
- product/, experiments/, data/: future execution areas and storage conventions.

## Most recent thinking

Hypothesis: richer task context and VLM subplanning can improve physical task success. Test which context changes decisions and whether execution is capable enough to benefit. Hierarchical VLM/VLA planning already exists; novelty needs evidence.

Candidates: unfamiliar equipment servicing, connector recovery, marine entanglement recovery, cabinet maintenance, aerial contact inspection, selective agriculture, and workspace restoration. Active information gathering may connect them: inspect, probe, or consult documentation before acting. Recommendations are assistant judgments, not user decisions.

Latest discussion: research/discussions/2026-10-22-research-directions.md maps the full paper index into research strands; only selected primary abstracts/project descriptions were checked, not all full papers. User favors underwater but requests broad exploration. Assistant proposes three alternative studies: failure diagnosis through active probing, decisions about when to ask an operator, and physical verification of completion. Underwater does not universally require full autonomy; shared-autonomy ROV systems are relevant baselines. Commercial willingness to pay remains unvalidated.

Next question: which failure story appeals most—underwater recovery, unfamiliar equipment servicing, or knowing when to stop/ask? Operator, arm, tank, and hardware access should shape scope. No project selected or experiment started.

The exact Anthropic ten-year extinction attribution remains unverified. A previously cited statement about then-current systems came from a 2023 article and must not be treated as a current risk assessment.

## Operational state

Project agent roles are defined under .codex/agents/. Root AGENTS.md supplies dispatch and context rules. Two setup agents hit a workspace-credit error; no independent review was completed. Coordinator completes checks without retrying agents. Named-role runtime loading has not been demonstrated in this session; if unavailable, read the relevant role file and pass its instructions to an available child.

Existing untracked duplicate-looking files (e.g. README 2.md) predate this setup; preserve them and exclude them from this commit.

# Physical-AI capability gap

## Idea

Break broad claims about catastrophic frontier AI into testable capability requirements, then compare those requirements with what open-source and frontier physical-AI systems can actually do.

The specific “AI kills all humanity in ten years” wording attributed to Anthropic has not yet been verified. Anthropic’s published position is more careful: it says advanced AI could have an unprecedented impact within the next decade, treats catastrophic outcomes as uncertain scenarios, and explicitly says present systems are not an imminent concern. The project should begin by locating the exact original quote or correcting the premise.

## Research question

Which parts of catastrophic-risk arguments depend on physical agency, and where are the largest gaps between current digital intelligence and reliable autonomy in the physical world?

Physical limitations do not settle total AI risk. Cyber operations, biological assistance, persuasion, economic control, and delegation through humans may not require a capable robot. The useful contribution is a capability decomposition, not a claim that weak robotics disproves catastrophic risk.

## Capability matrix

Evaluate open and frontier systems across:

1. perception under lighting, occlusion, weather, and sensor failure;
2. spatial reasoning and world-state estimation;
3. long-horizon planning and replanning;
4. dexterous manipulation and contact-rich control;
5. mobility in unstructured environments;
6. learning from sparse demonstrations and online outcomes;
7. reliability, calibration, and safe failure;
8. energy, maintenance, communications, and hardware supply;
9. autonomous acquisition of tools and resources;
10. replication, coordination, and operation without human support.

For each capability, record the best open system, best reported frontier system, demonstrated environment, human assistance, failure rate, and evidence quality.

## First deliverable

A dated benchmark report with three layers:

- **digital model capability**: reasoning, planning, coding, and tool use;
- **embodied policy capability**: perception-to-action performance in controlled tasks;
- **system autonomy**: sustained operation with hardware, energy, recovery, and real-world constraints.

The report should include a dependency graph showing which catastrophic pathways need physical embodiment and which do not.

## Evidence to start from

- [Anthropic’s core views on AI safety](https://www.anthropic.com/news/core-views-on-ai-safety)
- [Anthropic’s Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)
- [Anthropic Responsible Scaling Policy v3](https://www.anthropic.com/news/responsible-scaling-policy-v3)
- [Learning VLA tracker](../../knowledge-base/Robotics%20learning/Learning%20VLA.md)
- [Robotics paper list](../../knowledge-base/Robotics%20learning/Research%20papers/reading-list.md)

## Decision point

Continue if a defensible, reproducible capability taxonomy can reveal something missed by existing AI-risk evaluations. Narrow the scope if the work becomes only a literature summary.

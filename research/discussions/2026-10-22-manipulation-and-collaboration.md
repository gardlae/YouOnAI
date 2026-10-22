# Manipulation opportunities and collaboration

Recorded 2026-10-22. Reconstructed substantive notes from the preceding conversation; this is not a verbatim transcript. Technical sources were consulted during that conversation, not newly revalidated for this record.

## User intent (paraphrased)

Explore dexterous manipulation across USVs, UAVs, UGVs, underwater robots, and humanoids. Investigate whether VLM subplanning and richer context can improve current performance. Spend time discussing alternatives before choosing a project. Use a collaborative style that sharpens ideas, surfaces unexpected connections, challenges assumptions, and avoids confusing plausible prose with truth.

## Substantive assistant response

The premise that better context leads to better performance is a useful hypothesis. We need to identify exactly what information is missing, which decision it changes, and whether the robot can physically execute that decision.

VLM subplanning already exists. Hi Robot combines high-level visual-language reasoning with low-level action policies. A contribution could be the context supplied, how the robot acquires it, or how it uses it to recover in a particular domain. [Hi Robot](https://arxiv.org/abs/2502.19417)

The following advantages are hypotheses, not demonstrated gains:

| Candidate task | Platform | Potential value of context | Execution difficulty |
| --- | --- | --- | --- |
| Open unfamiliar equipment and replace a component | Bench arm, UGV with arm, humanoid | Service manuals, labels, visible fasteners, and prior inspection guide removal order | Hidden clips, connector forces, tool alignment |
| Recover from failed connector insertion | Industrial arm or mobile manipulator | Diagnose wrong orientation, blocked access, unreleased latch, or cable tension; choose different recovery | Contact sensing and compliance |
| Remove entangled marine debris | USV with arm or underwater robot | Distinguish loose objects from ropes, infrastructure attachments, and living material | Occlusion, deformation, currents, tension |
| Inspect and service unfamiliar cabinets | UGV or humanoid | Interpret work order, choose enclosure, manipulate correct component, verify state | Latches, reachability, force control |
| Contact inspection at selected locations | UAV with contact tool | Use history and visible defects to choose measurements and repeats | Flight stability and contact force |
| Selective harvesting or pruning | Agricultural UGV with arm | Use maturity, plant structure, access, and action history to select targets and order | Occlusion, delicate contact, branch motion |
| Restore a workspace after an unexpected event | Mobile dual-arm robot or humanoid | Infer what belongs where, what needs cleaning, what must stay untouched, and whether actions succeeded | Broad skill coverage and long sequences |

Equipment servicing is a promising initial candidate. Given an unfamiliar machine and an instruction to replace a filter, the robot might consult a manual, identify an access panel, release a latch, move an obstruction, replace the filter, and verify the outcome. Varying manuals, layouts, and failure history can isolate the value of context.

Related disassembly work reports that fine-tuned VLAs completed early steps but struggled on critical subtasks, while a hybrid strategy completed the operation. This provides a starting point, but also means adding a VLM alone needs a stronger novelty argument. [Selective robotic disassembly](https://arxiv.org/abs/2512.04446)

Marine debris recovery extends the user's marine interest. Detection and collection already exist in multi-robot systems. A sharper hypothesis concerns recognizing when pulling will fail, gathering information, and changing the manipulation sequence. [SeaClear](https://doi.org/10.1016/j.engappai.2026.114094)

UAV manipulation is less forgiving as a first test of the context hypothesis. Onboard state estimation and contact-force regulation remain active research problems; planning improvements may be hidden by execution failures. [Contact-aware aerial manipulation](https://arxiv.org/abs/2602.08251)

Active information gathering connects these tasks: move a camera, open a cover, gently probe an object, or consult a manual because the robot lacks enough information to act.

Candidate research question: Can a robot learn when to gather more information before manipulating, and does that reduce failures on unfamiliar equipment or objects?

## Proposed experiment logic

Hold hardware, low-level skills, task difficulty, and evaluation budget constant. Compare a conventional planner, a VLM planner with immediate observations, and a VLM planner with history/manuals/active sensing. Include a strong baseline with the same information access so improvement is not attributed to the VLM when it simply received extra data. Measure complete-task success, interventions, damage/contact violations, recovery, latency, and model cost. These are proposed controls; no experiment has run.

## Decisions and unresolved questions

- No platform or research direction is selected. Earlier preference for underwater simulation and later interest in equipment servicing are tentative assistant judgments.
- Novelty, best current systems, commercial value, and expected gains need targeted validation after narrowing scope.
- Next question to user: What physical workflow have you personally seen where an experienced operator succeeds because they understand the situation, while a less experienced person with the same tools gets stuck?

## Collaboration and usage update — 2026-10-22

User requests Git-backed discussion notes, a primary coordinator, delegated execution, and mutual validation. User then emphasizes that usage is being consumed unsustainably within a few prompts.

Adopt coordinator-only discussion and routine notes, bounded fresh-context delegation for substantial work, one child by default, and independent critique when consequential. Do not turn every idea into implementation. Store concise current context separately from this richer discussion record. No numerical savings are claimed: no per-task token measurement is available here.

Two setup agents terminated with workspace-credit errors. The configuration agent left a draft; the coordinator completed it. This is not successful independent validation. The account tool reported ordinary usage allowed, 7% used in a five-hour window, and 36% in a weekly window, with no credits; the mismatch with child failures is unresolved. These readings are a dated snapshot, not an explanation of billing.

# Research directions: reliable manipulation under uncertainty

Date: 2026-10-22. Exploratory synthesis; no project selected.

## User prompt, paraphrased

Combine the Learning VLA reading collection into broad research possibilities for real-world dexterous manipulation. Underwater is especially interesting because of harsh conditions, autonomy needs, reliability, and potential willingness to pay, but remain open to other platforms and applications.

## Evidence boundary

Reviewed the complete 88-entry local reading index and selected primary-source abstracts/project descriptions, not all 88 full papers. The connections below are research hypotheses, not a systematic literature review or established novelty claims. No independent agent review was performed because the preceding setup agents hit credit errors; no retries were launched. Expanded the initial searches to resolve specific gaps about data collection, causal use of context, and marine simulation. No experiments or product commitments authorized by this discussion.

## Central proposal

Study robots that diagnose manipulation failures, acquire missing evidence, and choose a recovery action. Underwater servicing is a compelling application; the general scientific question is how to use context when visual observations do not reveal the physical state.

Correction to the premise: underwater manipulation does not universally require full autonomy. WHOI's SHARC work explicitly develops shared autonomy for ROV manipulation. Reduced operator workload and fewer interventions could be useful intermediate outcomes. Willingness to pay is a hypothesis requiring operator/customer evidence, not something the technical papers establish. [WHOI SHARC](https://www.whoi.edu/press-room/news-release/new-framework-provides-broader-access-to-deep-sea-scientific-exploration/).

## How the collection connects

| Research strand | Relevant entries in the collection | Possible role in our research |
| --- | --- | --- |
| Hierarchical reasoning and spatial grounding | Hi Robot, HAMSTER, SayCan, ReKep, VLMPC, VoxPoser | Choose a subtask or geometric constraint; leave rapid physical execution to a capable controller. |
| Contact and embodiment | 3D-ViTac, ForceVLA, DexVLA, visuotactile hands | Detect slip, obstruction, or seating that images alone may miss. Underwater sensing and hardware need separate validation. |
| Memory and informative context | Causal Confusion, MEM, TraceVLA, embodied/visual chain of thought | Track attempted actions and distinguish causal evidence from distracting history. |
| Data and adaptation | ACT, Diffusion Policy, UMI, HG-DAgger, residual RL, real-world RL papers | Begin with narrow demonstrated skills, then target failures and recoveries instead of training a foundation model. |
| Prediction and evaluation | REALM, RoboTwin, world-model papers, RoboArena, benchmarking critique | Construct controlled perturbations, test held-out mechanisms, and compare simulator rankings with physical results. Predicted video is not proof of correct contact physics. |

This table maps the index into design questions; it does not certify every listed method's capabilities. Selected checks: [Hi Robot](https://arxiv.org/abs/2502.19417) supports hierarchical instruction handling; [HAMSTER](https://arxiv.org/abs/2502.05485) uses high-level path guidance with low-level control; [ReKep](https://rekep-robot.github.io/) generates relational keypoint constraints. Hierarchy itself is therefore insufficient as a novelty claim.

[3D-ViTac](https://arxiv.org/abs/2410.24091) supports examining tactile information for fine manipulation. [UMI](https://arxiv.org/abs/2402.10329) provides a precedent for collecting demonstrations with handheld grippers; it does not establish an underwater-ready interface. [Causal Confusion](https://arxiv.org/abs/1905.11979) shows why more input information can hurt imitation learning, motivating controlled tests of which context matters.

## Broad application paths

All rows are proposed research opportunities, not demonstrated performance gaps or validated markets.

| Application | Concrete task | Interesting research question | Main difficulty |
| --- | --- | --- | --- |
| Underwater servicing | Release a latch or seat a connector on a submerged mock panel | Can probing, force history, and procedure context distinguish misalignment from an unreleased lock? | Physical sensing, contact, and water effects must transfer. |
| Marine entanglement | Free a removable tool or object from a small set of rope loops | Can a robot infer constraints through gentle manipulation and choose an order that avoids tightening them? | Deformable topology is difficult to perceive and simulate; controlled mockups first. |
| UGV field maintenance | Open a cabinet and remove/reseat a replaceable module | Can manuals plus live evidence generalize across unfamiliar mechanisms? | Stale documentation and unseen geometry can invalidate plans. |
| Mobile or aerial contact work | Brace against a structure before applying a tool or inspection probe | Can a planner recognize when changing support/contact makes a task feasible? | Coupled vehicle/contact control may dominate semantic planning. |
| USV servicing | Capture a moving handle or attach a line to a fixture | Can the system choose when to approach, wait, stabilize, or retry? | Relative motion and timing; a strong conventional estimator/controller may suffice. |
| Reuse and disassembly | Remove a clipped, screwed, or stuck component from an unfamiliar assembly | Can physical tests distinguish the fastening mechanism and avoid destructive attempts? | Hidden fasteners, access to representative objects, force limits. |
| Agriculture | Clear an obstructing leaf, support a stem, then place a clip | Can context improve action order while respecting fragile structures? | Biological variability and delicate contact. |

## Three research bets worth discussing

**1. Diagnose before retrying.** Two failures can look similar but require opposite actions: a connector may be misaligned, locked, or obstructed. Compare immediate retries with a policy that selects a bounded probe, updates its state estimate from force/motion, and chooses a recovery. Start with interchangeable latch/connector mockups on a fixed arm. If the result survives held-out mechanisms, move to a tank and eventually a mobile platform. This is my preferred first direction because it isolates your context hypothesis without immediately requiring a complete vehicle.

**2. Autonomy that knows when to ask.** Vary communication availability and interruption cost. Let the robot choose to proceed, inspect, request a specific fact, request intervention, or stop. Test whether it reduces human workload at a matched failure/damage limit. This connects underwater applications with your AI-safety interests through measurable competence boundaries. Self-reported model confidence alone would not validate the decision; use observed outcomes and calibrated decision rules. Existing shared autonomy means the contribution must be a specific decision mechanism or generalization result.

**3. Verify the physical result.** Insertion is not necessarily successful seating; a moved latch may remain locked. Let the robot choose a completion test, such as a gentle retention check or instrumented state check. Measure false declarations of success and time spent checking. The proposed contribution is deciding which physical evidence establishes completion under ambiguous perception. This could become a focused study in underwater servicing, industrial maintenance, or disassembly.

These are alternatives for an initial study, not three modules we should build at once. Entanglement is the more adventurous fourth option if we want deformable-object research and can obtain data.

## What would make an experiment convincing?

Use a strong scripted/force-control baseline, a learned skill baseline, and a hierarchical planner baseline with the same available sensors, training data budget, and execution skills wherever possible. Separate the gain from extra sensing from the gain from choosing how to use it. Give passive baselines matched action/time budgets; compare learned probes with a fixed probe sequence. Ablate manuals, history, touch, and active probing individually. Include incorrect/stale context tests.

Hold out mechanisms or objects, not merely camera views. Report completion, false success, peak force/constraint violations, recovery success, operator intervention time, and latency/inference calls. Report uncertainty over repeated trials, and identify any tradeoff where more time buys success. A negative finding—that the conventional controller already solves the task or the VLM adds latency without benefit—is informative and a reason to redirect.

For underwater simulation, first choose the physical phenomenon the experiment must reproduce. [Stonefish documentation](https://stonefish.readthedocs.io/en/latest/) describes marine simulation with geometry-based hydrodynamics. Compare its suitability with an Isaac-based setup after defining requirements; we have not benchmarked either. A plausible underwater scene does not validate contact, visibility, or fluid dynamics. Progress from dry fixtures to a tank before claiming marine deployment reliability.

## Position and next question

Assistant preference: begin with failure diagnosis or completion verification on service mechanisms, with underwater as the target application. Keep a dry-land maintenance version as a cheaper test of the same science. The user has not selected a direction.

Next discussion question: which failure story is most compelling—an underwater robot that gets stuck and must recover, a maintenance robot that understands unfamiliar equipment, or a robot that knows when it cannot safely finish? Also establish access to operators, a robot arm, a tank, and representative hardware before choosing scope. No immediate purchase or build is proposed.

# AI Partnership and Governance

Working draft for PDF 1. Prepared 23 October 2026. AI-drafted from the project conversation for student review; not a final submission. No PDF has been generated.

Student: [add name]

Course / exercise: [add course and confirm how this conversation satisfies the in-class exercise]

## 1. Short AI conversation and research output

Suggested focus: how the student redirected AI from implementation toward understanding and ideation. This is a clear example of retained human judgment supported by the conversation. It does not establish that every AI research claim was independently checked by the student.

### Conversation excerpt

The following are verbatim excerpts from a longer exchange; omitted material is not reproduced here.

**Student:** “We have a bit on the implementation. I need to go more on the ID phase. Still we need to sketch out important concepts from new research and see how we can apply this in a new way”

**AI:** “We moved into implementation too early. The next task is to understand the research well enough to choose an interesting question.”

**AI, later in the same response:** “You do not need all 88 papers before choosing a project. You need to be able to explain the closest method, identify a concrete situation it might mishandle, propose the simplest competing solution, and state what result would disprove your idea.”

### Short research output

The AI-assisted work produced a conceptual map for a possible simulation-based robotics paper. It distinguished progress from completion, visible appearance from physical state, and historical achievements from conditions that must remain true. Four candidate directions emerged: choosing an action to verify completion; detecting when later actions undo earlier progress; assessing whether an outcome persists after release; and resolving misleading instructions or reference images. These were AI-suggested research hypotheses developed in response to the student's interests, not established novel contributions or a selected project.

The work also produced a prioritized reading sequence: ACT, selected CS285 reinforcement-learning material, OpenVLA, Hi Robot, GVL, ReWiND, Robometer and StructRL. Source checks identified close prior work, which prompted more cautious novelty claims. No robotics experiments were run, and the papers were inspected to varying depths rather than all read in full.

Supporting artifacts: [concept map](../../projects/verified-subgoal-rl/ideation.md), [reading list](../../projects/verified-subgoal-rl/reading-for-ideation.md), and [related-work evidence record](../../projects/verified-subgoal-rl/related-work.md). These preserve citations and the depth of inspection behind the output; they are not evidence of student mastery or independent reproduction.

## 2. Disclosure Summary

The following is an AI-drafted first-person summary for the student to verify and revise.

I used OpenAI Codex as a discussion partner and research-organizing assistant while exploring a robotics research project. I provided my interests in physical manipulation and underwater applications, my Learning VLA reading collection, my goal of learning reinforcement learning, and my preference for a simulation-based paper with an eventual open-source implementation.

My prompts were iterative. I asked the AI to explore broadly, connect papers to possible problems, identify related research, compare simulators, and prepare a reading path. I later redirected it toward ideation because the discussion had moved too quickly into implementation. I also asked for lower-usage agent coordination and persistent notes in GitHub.

The AI organized material, suggested research directions, searched selected sources, identified close prior work, and drafted conceptual explanations, comparisons and plans. Two research agents contributed findings and drafts before encountering credit limits; the main assistant completed integration. No independent critic review was completed. I chose the goals, priorities and constraints: learning RL/VLA, focusing on unfamiliar scenes and task completion, targeting simulation rather than initial real-world testing, and returning to conceptual work before implementation. I have not selected the final research question or confirmed that any proposed contribution is novel.

The resulting work product is a research preparation and ideation collection, not experimental findings. This disclosure summary, log and proposed reusable prompt were also AI-drafted. I will add my own reflection and review the submission before finalizing it.

**Metadata:** Prepared 23 October 2026 using OpenAI Codex in the desktop app. Supporting project notes are dated 22–23 October 2026; exact timestamps for every interaction and the exact underlying model/version are not established by this record. Do not infer the model from the application name.

## 3. Disclosure Log / Prompt Log

Selected substantive interactions, ordered as they occurred. Prompts and outputs below are paraphrases, not a full verbatim transcript. Each row corresponds to a selected user interaction and its resulting AI work. Revision attribution distinguishes student steering from AI revisions; omission of routine progress messages is intentional.

| Interaction | Context Provided | Prompt | AI Output | Revision | Decision |
| --- | --- | --- | --- | --- | --- |
| 1. Partnership and memory | Ongoing robotics discussion; desire for continuity across devices | Store responses in notes on GitHub and coordinate agents with distinct roles and validation | Durable discussion notes, role definitions and collaboration workflow | AI converted the requested collaboration style into repository instructions | Student requested one primary conversation partner and durable context; implementation details were AI-selected |
| 2. Usage constraint | Agent usage was becoming unsustainable | Optimize the agent structure to reduce token use | Selective delegation, small context packets, concise outputs and credit-error fallback | AI revised the workflow toward coordinator-only discussion and bounded agents | Student set the usage constraint; no measured savings were established |
| 3. Broad exploration | Paper collection; underwater interest; openness to other platforms | Combine the research into exploratory manipulation directions | Application map and proposals involving diagnosis, completion and assistance | AI qualified the full-autonomy premise for underwater work and treated demand as a hypothesis | Student kept options open; no application or project was selected |
| 4. Research scope | Concern that real-world testing was too ambitious; interest in unfamiliar scenes and completion | Target a simulation-only paper; explore image/text subgoals with RL; prepare sources and a learning path | Simulator comparison, related-work review, evaluation plan, reading path and paper outline | AI distinguished progress, cost and reward; close prior work narrowed what could be claimed novel | Student chose paper-first scope, simulation, learning objectives and open-source intent; final method remained open |
| 5. Compute clarification | Linux computer with NVIDIA 5070; willingness to consider cloud compute | Clarified available hardware in response to the AI's question | Local-pilot-first planning with hardware measurements proposed | AI updated compute assumptions without assuming VRAM or starting paid work | Student supplied resource context; no cloud purchase or provider was selected |
| 6. Continue preparation | Research drafts and findings were available | Continue the preparation task | Integrated preparation documents and a synthetic signal exercise with seven passing tests | AI completed drafts after agent credit failures and disclosed missing independent review | Preparation was completed; no simulation or robotics result was claimed |
| 7. Return to ideation | Too much attention had shifted to implementation | Explore concepts and new applications; provide the reading needed to formulate a project | Four conceptual directions and an ordered reading list with understanding questions | AI parked the pilot and made the scientific question explicitly provisional | Student chose understanding and ideation before implementation; none of the four ideas was selected |
| 8. Coursework disclosure | Two separate assignments and eventual PDFs; reflection to be written by the student | Draft the disclosure summary and log first; do not generate PDFs yet | This governance draft, excerpt, output summary, log and proposed prompt pattern; separate project-ideas placeholder | AI reorganized existing conversation evidence for the assignment; student text edits are not yet recorded | Student retains the reflection and final review; peer-pod input and three project submissions remain for later |

## 4. Reusable prompt pattern

**Proposed pattern: evidence → possibilities → human choice**

> I am exploring [problem/domain] for [purpose]. My current understanding is [summary], and my constraints are [constraints]. Use [sources] to explain the important concepts, then suggest three ways they could inform a research question. For each, separate source-supported findings from your inference, identify the closest existing work and simplest alternative, and state what evidence would make us reject the idea. Do not treat a new combination as proof of novelty. Stay in the idea phase until I choose a direction. End with one question that helps me make that choice.

**Brief disclosure:** This prompt pattern was drafted by AI from my recurring instructions to connect research, question assumptions, preserve my judgment and avoid moving too quickly into implementation. It is a proposed reusable synthesis, not a verbatim prompt I previously used or a tested guarantee of output quality. My earlier revisions were conversational: narrowing the scope to simulation, setting learning goals and redirecting the work toward ideation. I have not yet recorded edits to this particular prompt template.

**Student revisions before submission:** [Record any actual wording changes and why; remove this placeholder only after reviewing.]

## 5. Student reflection — to be added

[Student writes approximately half a page. No reflection is ghostwritten here.]

Optional questions to support your reflection:

- What distinction did you actually understand better after this conversation? Explain it in your own words.
- Where did AI broaden your thinking, and where did it move the work in an unhelpful direction?
- What changed because you redirected it toward ideation?
- Which final scope decisions were yours, and what remains undecided?
- What source or claim still needs your own checking?

## Before PDF preparation

Student to verify the first-person wording, add reflection and any actual prompt revisions, and confirm the exercise fits the course instructions. The conversation log records selected project interactions; it does not claim that a peer meeting occurred, that all papers were read, or that the student personally verified every AI claim. This draft and its disclosure log are themselves AI-assisted work.

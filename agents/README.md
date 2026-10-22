# How agents work on YouOnAI

The main assistant is the coordinator and the user's conversation partner. It preserves the discussion, turns agreed work into bounded assignments, delegates execution, reviews the evidence, and integrates the results. The user can keep discussing ideas while delegated work runs during the active session.

This framework is stored in Git so another computer can recover project context. It does not create an always-running service, keep a closed session alive, or automatically synchronize Git checkouts. A new session must read the durable context before continuing.

## Start a session

The coordinator reads, in order:

1. [`AGENTS.md`](../AGENTS.md) for repository rules and the collaboration contract.
2. [`collaboration/CURRENT.md`](../collaboration/CURRENT.md) for the current state and unresolved questions.
3. [`collaboration/TASKS.md`](../collaboration/TASKS.md) for the durable work queue.
4. [`research/discussions/README.md`](../research/discussions/README.md) and the relevant discussion notes for the reasoning behind decisions.

Read the applicable project brief and source notes before assigning substantive work. Check the actual Git state: saved notes may describe work that has not yet been committed, pushed, or pulled on this computer. The coordinator is the single writer of shared coordination records unless it explicitly assigns a record to someone else.

## Roles

| Role | Responsibility | May change project files? |
| --- | --- | --- |
| Coordinator (main assistant) | Discuss, retain context, assign work, integrate, decide completion, commit and push within user authorization | Yes |
| `youonai_researcher` | Investigate a bounded question; return primary-source evidence, uncertainty, and counterarguments | No |
| `youonai_builder` | Produce an assigned artifact or implementation and self-check it | Assigned files only |
| `youonai_critic` | Independently challenge claims, design choices, and implementation | No |
| `youonai_verifier` | Independently reproduce checks and assess acceptance criteria | No tracked edits; temporary check artifacts only |

The roles live in [`.codex/agents/`](../.codex/agents/). They inherit the user's model and permission settings. Read-only roles are constrained by instructions, not separate filesystem isolation. Default to one child; the configuration permits two concurrent children as a ceiling. If named agents are unavailable, read the relevant role file and pass those instructions in a bounded assignment to an available subagent. Do not claim named-role loading was verified merely because TOML parsed.

## Usage budget

Discussion and routine notes stay in the main chat. Do not spawn a team for every prompt. Use fresh child context where available, a task brief under 500 words, and an output target of 300 words plus essential findings. Avoid recursive agents, repeated source retrieval, broad file dumps, and repeated passing tests. Read CURRENT.md rather than the full archive. For research, start with up to three searches and three primary sources and expand only to resolve a named gap.

No model is pinned: the user's selection is inherited. This policy reduces avoidable work but is not a hard token or spending limit. Actual savings have not been measured. If a child fails on credits, do not retry automatically; complete feasible work in the coordinator and report review limitations.

## Discussion and execution

Exploratory conversation remains exploratory until the user asks for work or an existing authorization clearly covers it. Preserve promising ideas, disagreements, and open questions without converting every suggestion into a product commitment. Recording the discussion is part of the user's standing request.

For execution, the coordinator creates or updates a task in the durable queue and sends an explicit assignment using the [task template](templates/task.md). Include the parent intent, expected result, acceptance criteria, exact file ownership, sources, constraints, and any permitted external actions. Assign non-overlapping files to simultaneous builders. Shared files remain with the coordinator. Do not let multiple agents update the same queue or discussion note concurrently.

If the user changes direction during work, the coordinator communicates the change, revises the task scope, and records the decision. If context changes materially or an agent becomes stuck, it reports the issue to the coordinator instead of making an irreversible assumption. No agent sends messages to outside people without explicit authorization.

## Validation and completion

1. **Proportionate checks:** routine notes need coordinator source/link checks. Substantial code or consequential research conclusions need independent critique of the actual evidence or changes.
2. **Bounded implementation:** use one builder where useful, with owned files and observable acceptance criteria. Self-checks are not independent approval.
3. **Independent critique when warranted:** a separate critic reports concrete findings. Resolve required findings and document limitations. If quota blocks review, say so rather than claiming approval.
4. **Verification:** the coordinator normally runs relevant checks. Use a separate verifier only for substantial checks or unresolved concerns. Recheck only affected behavior after fixes.
5. **Coordinator acceptance:** inspect the final diff, update durable records, and commit/push authorized changes using explicit paths. Verify remote success.

Use the [review template](templates/review.md) for review and verification evidence. Keep checks proportionate to the change: source fidelity and link checks matter for notes; behavioral tests matter for code. Record skipped or unavailable checks explicitly. A task is complete when its acceptance criteria are met and required findings are resolved or an authorized limitation is documented. Agent confidence alone is not validation.

Templates apply to substantive delegated work, not every discussion reply. The critic/verifier fields may be marked not required with a reason under this policy.

Configuration reference: [official Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents), consulted 2026-10-22. On another computer, install/sign in to Codex, open an updated checkout, and verify the role definitions are available. No API service, scheduler, global settings, or background daemon is provisioned by this repository.

## Across computers

Commit the discussion records, task state, role definitions, and useful artifacts together when appropriate. Record incomplete work and its next action before handing off. A new computer needs an updated checkout and an available Codex installation that supports the project configuration. Credentials, local dependencies, and active agent processes do not travel through Git. Avoid starting the same queued task on two computers at once; pull the latest state and claim it in the queue first. Git is the record of coordination, not a distributed job lock.

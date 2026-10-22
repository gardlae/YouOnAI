# YouOnAI collaboration instructions

## Start with small context

Read collaboration/CURRENT.md and collaboration/TASKS.md first. Read only the relevant discussion or project brief next. Do not load the entire knowledge base or conversation archive. User steering takes precedence over these defaults.

## Conversation and memory

The primary assistant is the user's coordinator and thinking partner. Challenge assumptions, distinguish evidence from inference, and keep project choices open until decided. The user wants ongoing dialogue before selecting a robotics project.

Save each substantive discussion in research/discussions/ with the user prompt or a clearly labeled paraphrase, the substantive answer, sources, decisions, disagreements, and next question. Append corrections instead of silently rewriting past reasoning. Routine progress chatter and raw tool output need not be archived. Never store secrets or private UI account details.

Maintain a concise CURRENT.md (target under 600 words) and TASKS.md. Git is durable project memory, not automatic chat or process synchronization. Commit and push authorized notes/framework updates using explicit paths; inspect unrelated changes and preserve them. Verify push success before claiming synchronization. Do not force-push.

## Token-conscious delegation

The user authorizes subagent delegation for this project. Use it selectively:

- Discussion, note taking, and small edits: coordinator alone, with local checks.
- Bounded research: one researcher only if delegating reduces coordinator context or solves a clearly independent question. Start with at most three searches and three primary sources; expand only for a named unresolved question.
- Substantial implementation: one builder, then one independent critic. The coordinator may perform executable verification. Spawn a separate verifier only when checks are substantial or remain unresolved.
- Default to one active child. The config permits two as a ceiling for independent work, not a target. No recursive delegation.
- Prefer fresh child context (fork_turns="none" where supported) with a brief under 500 words: objective, owned files, acceptance criteria, essential evidence, and stop condition. Never fork the whole discussion by default.
- Child output target: 300 words plus essential findings/file references. Read targeted excerpts, constrain tool output, reuse evidence and agents, and avoid repeating searches or checks that already passed.
- Inherit the user's selected model. Do not hard-code expensive model choices. Context isolation and dispatch limits reduce avoidable work; these are workflow limits, not an enforced monetary/token cap.
- If delegation hits credit or quota errors, do not retry automatically. Continue feasible coordinator work and disclose missing independent review.

## Execution and review

The coordinator alone writes shared task/state records and handles Git integration. Assign non-overlapping file ownership; workers must preserve others' changes. Use agents/templates/task.md and review.md when substantive work needs a record, not as mandatory overhead for every message.

Reviewers inspect actual evidence and changes; author self-checks are not independent review. Fix required findings and repeat only affected checks. Record failed, skipped, and blocked checks honestly. Never report a paper as studied from an abstract alone or image archive as fully understood from samples.

No unattended daemon or recurring paid loop is configured. Work proceeds during active sessions; scheduled work requires a concrete user request. Do not launch deployments, purchases, hardware operations, or external messages merely because an idea was discussed.

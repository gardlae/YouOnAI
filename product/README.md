# Product workspace

Prepared for a future application. No application has been created, dependencies installed, or deployment performed.

Research-backed opportunities begin in `ideas/`. Short-lived demonstrations go in `prototypes/`; maintained applications go in `apps/`. Each product should link to the research evidence or experiment that motivates it.

## Contents

- `reference/vercel-ai-gateway-codex.txt`: local copy of the documentation supplied in chat.
- `ideas/`: product hypotheses and intended users.
- `prototypes/`: disposable validation builds.
- `apps/`: maintained applications.
- `vercel.json`: preliminary static-site configuration targeting `dist/`.
- `dist/.gitkeep`: retains the empty output folder in Git.

## When you build the application

Create the application in this `product/` folder. Choose its framework and dependencies then. The current Vercel configuration assumes static output in `dist/`; update or replace it to match your framework before deploying. For a framework such as Next.js, remove the static overrides and use the appropriate framework detection.

For a future Vercel project, select `product` as the repository Root Directory. Configure the build command, output directory, and environment variables after the app exists. This empty scaffold is not yet a deployable application.

The supplied AI Gateway guide configures Codex model routing, separately from application hosting. No Codex settings, shell settings, or API keys have been changed. Recheck current documentation before applying the reference instructions.

References: [Vercel deployments](https://vercel.com/docs/deployments), [project configuration](https://vercel.com/docs/project-configuration).

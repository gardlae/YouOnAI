# LinkedIn outreach tool demo

Source: [Granola note](https://notes.granola.ai/d/7ea592c0-c91f-46f3-a849-d41831d76b88)  
Date: 2026-09-27

### Product Overview

- LinkedIn network tool for warm intro discovery and cold outreach
- Core flow: upload connections + target accounts, platform maps relationships, drafts outreach emails
- Built in AI Studio during the hackathon; CSV export from LinkedIn used as data source for the demo

### How It Works

- Visualizes shared connections to target companies (e.g., Stripe via Sahil and Yannis)
- Graph network model with cost/strength scoring to rank reachability
- Drafts personalized cold emails within the platform (e.g., message to Elena re: Stripe intro)

### Data Sources and Architecture

- Current: CSV export from LinkedIn + uploaded target account list
- Lower-friction path: Chrome extension to pull connections directly
- Future: scrapers on LinkedIn engagement signals (post likes, etc.) to trigger sequences

### Differentiation and Q&A

- Crowded space acknowledged; differentiator framed as cross-platform orchestration
  - Integrations with execution platforms (cold email, sequencing) as the moat
  - Data from multiple sources feeding into one execution layer
- vs. Apollo: Apollo is lead gen; this leverages existing warm network
- vs. Happenstance: not fully addressed (audio unclear)


# Rental documentation app demo

Source: [Granola note](https://notes.granola.ai/d/ebdf8706-71ce-4246-9ca7-cacb5b5da0b8)  
Date: 2026-09-27

### Product Overview: Posit

- AI-powered damage documentation app for rentals (apartments, cars, Airbnbs)
- Core flow: photo/video at move-in → scan flags all pre-existing damage → photo at move-out → AI compares and highlights what’s new vs. pre-existing
- Removes ambiguity in deposit disputes by grounding claims in documented evidence

### Demo Highlights

- Tested two scenarios:
  - Damaged panel vs. clean panel: correctly identified new vs. pre-existing damage
  - Same photo uploaded twice: correctly returned zero new damage (edge case validation)
- Output includes damage categorization (scratches, dents, stains) and cost estimates
- Dispute letter generator: auto-drafts a dated letter to landlord or rental company

### Business Model and Target Market

- Dual-sided market: consumers and B2B
  - Consumer: renters wanting personal protection
  - B2B: property managers, landlords, insurance companies, rental companies (e.g. Enterprise)
- Pricing discussed:
  - Property owners: $1–3 per unit
  - Individual landlords: $5–15
- Positioned as software provider, not an insurer or legal entity

### Q&A and Open Questions

- Business category question: team sees it as a software/SaaS play, not insurance or legal
- Image fabrication risk raised: team acknowledged need for fabrication detection as a future feature
- Customer focus confusion flagged: unclear whether primary customer is the renter or the property owner
  - Team suggested both can use it independently, but go-to-market focus not fully resolved


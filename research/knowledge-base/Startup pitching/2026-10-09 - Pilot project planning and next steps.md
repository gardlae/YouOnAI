# Pilot project planning and next steps

Source: [Granola note](https://notes.granola.ai/d/feb553f9-c641-44e8-82d2-e08a95d283b8)  
Date: 2026-10-09

### Project Motivation and Commitment

- Core tension: market size not huge, but product is inevitable and the mission is clear
  - “Gym of the future”: in 10 years, autonomous rep-counting will be expected everywhere
  - No one argues gyms are bad for people; universal appeal, no ideological resistance
- Agreed to run hard for 3-4 weeks, then reassess
  - Next decision point: after first pilot attempt
  - If no setbacks, keep pushing; if red light, discuss and potentially pivot
- Biggest risk flagged: getting motivated by funding optics rather than building the product

### Pitch and Gym Outreach

- Felix’s pitch is working: authentic, not salesy, stands behind the product
  - Intro: “We’re from Spotter, a UC Berkeley startup building smart gym software, an online personal trainer for gym-goers”
  - Customer value: workout tracking, rep/weight/exercise logging, recovery overview, progress summary
  - Gym value: rush hour data, area utilization heatmaps, customer flow insights
  - Demo: website shown on phone, customer view then gym view
- Camera coverage is the biggest variable
  - 4 gyms visited so far; 2 said no immediately (neighborhood gyms, low-effort clientele)
  - Most gyms already have cameras for liability; RSF almost certainly does
  - Gyms without coverage are future targets once system is proven
- Numbers game: everyone visits 7 gyms each next week, then reconvene
  - Walk in solo; group visits don’t work
  - Build a shared drive with all gym contact documents

### Funding and Visa Strategy

- Visa requires ~$300k investment; seed round seen as necessary, not just nice-to-have
  - $200k may be sufficient for visa purposes
  - Funding framed as a “seal of approval,” not the goal itself
- A16Z Speedrun pitch: $300k, deadline October 20th
  - All three are in; need to sign up as a group
- VC meetings useful now for feedback quality, not capital
  - VCs ask the right questions and push toward correct priorities
  - Warm intros from Felix’s SF events can be circled back to once pilot exists
- Consensus: pilot first, then approach VCs with traction

### Data Collection and Backend Development

- No backend yet; need real footage to build on
  - Existing product has a 3-second occlusion memory but no cross-camera tracking
- Best near-term footage options discussed:
  - Ask brother to train 10 minutes at hotel gym in Oslo, pull security footage to Dropbox
  - Clark Kirk student housing gym (Ralph has access); set up own cameras there
  - Buy surveillance cameras (~$1.5k for 16 units; need minimum 2-3)
- Immediate plan: simulate surveillance setup in Sather Gate / Great Hall
  - Two angles from upper aisles inside Great Hall
  - Third angle from outside balcony/patio, capturing cross-threshold tracking
  - Sync cameras with a loud clap, manually align footage
  - Do this as soon as possible, potentially today

### Technical Architecture

- Core problem: single source of truth across multiple camera feeds
  - Each camera must refer to a shared coordinate system to avoid identity confusion
- 3D gym mapping on intake:
  - Walk the gym with phone to generate 3D map, then input camera positions
  - Alternatively, reconstruct map from existing camera angles (limited to visible areas)
- Cross-camera person tracking:
  - Use Kalman filter to estimate position when person leaves one camera’s frame
  - Variance grows over time; facial recognition as a fallback to resolve identity conflicts
- User identification approach:
  - Entry-point camera scans face on check-in; opt-in, visible, used as upsell
  - Pull check-in data from gym’s existing system; no extra NFC tap needed
  - Users who haven’t signed up are not tracked (compute efficiency + privacy)
- Germany competitor chose own cameras over existing footage; likely privacy law driven, not technical

### Next Steps

- **Run Great Hall multi-camera tracking test**

  Set up three phones at upper aisles and outside balcony, sync with clap, capture cross-threshold footage for backend development.

- **Get gym footage from brother&apos;s hotel gym**

  Ask brother to train for 10 minutes, then request security footage from the firm and upload to Dropbox.

- **Each team member visits 7 gyms next week**

  Solo visits only; use shared drive to log contacts and outcomes.

- **Follow up with gym contact and data lead (Felix)**

  Call the interested gym manager today; send email to the contact who offered footage data.

- **Sign up for A16Z Speedrun as a group**

  Pitch deadline is October 20th; $300k prize aligns with visa funding requirement.

- **Research compute options beyond Mac Mini**

  Mac Mini used as shorthand for local compute; no formal comparison done yet.


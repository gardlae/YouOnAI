# Camera integration ideas

Source: [Granola note](https://notes.granola.ai/d/eb71e91c-ccbd-450d-ae18-1ba81aa68042)  
Date: 2026-09-27

### Project Concept: Gym Rep Tracker

- Core idea: computer vision system tracking gym reps via existing surveillance cameras + Raspberry Pi
- Target customer: gyms (not individual users)
- Product name floated: “Reps” (or similar)
- V1 scope: rep counting only, no weight recognition or technique analysis
  - Weight reading and form feedback deferred to later versions
  - Rationale: rep counting is measurable, achievable in the timeframe, and still impressive
- Hardware pitch: gyms already have cameras, so they only need a Raspberry Pi
  - Acknowledged the product is mostly software, but framed as hardware-connected
- User flow vision:
  - Enter gym, get auto-tagged as new ID
  - Camera tracks which machine you use and counts reps
  - On exit, receive a workout summary
- Feature ideas raised (lower priority):
  - Gym capacity / machine availability alerts
  - Social layer: connect with others doing similar training
  - AI-driven next-session recommendations
  - Event/competition suggestions based on training type

### Demo Plan

- Record video at the RSF (nearby gym) at 12:30
  - Need two people: one recording, one doing exercises
  - Aim for a boy and girl on camera for inclusivity
  - Film with phone (Raspberry Pi recording flagged as too unreliable for demo)
- Demo flow for judges:
  - Select from 2-3 pre-recorded videos
  - Pick a person to track
  - See their workout summary (reps per exercise)
  - “Start simulation” option to show how the product would look live
- Dashboard shows rep counter and workout summary; judges interact with this
- Be transparent that the Pi wasn’t used to record, just to process/deploy
- Target: everything wrapped up by 2:00-2:15

### Build Plan and Task Split

- Core technical work: vision model + rep detection (needs at least two people)
- Dashboard: web app (faster than native), showing rep counts and workout summary
- Workflow: one person starts the project in Google AI Studio, pushes to GitHub, others fork and contribute
- Use this meeting transcript as the initial prompt to scope the project with Gemini
- Regroup at 11:45 before gym run

### Next Steps

- **Go to the gym at 12:30 to film demo footage**

  Need two people (one filming, one exercising); film with phone as primary.

- **Start project in Google AI Studio and push to GitHub**

  Others can then fork and build in parallel.

- **Use this meeting transcript as the initial Gemini prompt**

  Scope the full architecture and task breakdown from the transcript summary.

- **Regroup at 11:45 before leaving for the gym**


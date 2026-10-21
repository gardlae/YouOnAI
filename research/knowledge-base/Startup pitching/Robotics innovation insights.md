# Robotics innovation insights

Source: [Granola note](https://notes.granola.ai/d/fc183665-29e4-4d21-bc37-63b0aef982bd)  
Date: 2026-10-15

## Robotics Infrastructure and Tooling
- Kronos (Martin Losho, co-founder/CEO): real-time OS for autonomous systems

  - Solves scale across cores, deadline adherence, and repeatable behavior simultaneously

  - Demo: conventional ROS misses 95% of deadlines on saturated hardware; Kronos misses none

  - First customer: Fortune 250 tier-one automotive supplier, ~$1M in design contracts

  - Open SDK, IP stays with the builder; functional safety partnership with automotive partner in progress

- Softionics (Sean): textile proximity sensing skin for robot hands and bodies

  - Solves near-field depth perception that cameras cannot reliably provide

  - 1mm precision at 15mm height, 10ms response, no light required (detects electric fields)

  - Validated with an $8B and a $15B Korean sensor/HMI company; NDA with a Cupertino company

- DeepL (Chris): experiment factory for robot deployment readiness

  - Core thesis: robots fail in deployment due to insufficient iteration, not insufficient demos

  - Physical twin data factory + simulation + on-site data (“real to sim to real”)

  - Already under contract with global OEM and a defense company (95% confidence)

  - Raising in January 2027; co-founder is a Berkeley postdoc

- ThoughtForge (Matt): dexterity AI using active inference for real-time adaptation

  - Rejects the “more data = generalization” thesis; models update every millisecond on the fly

  - Revenue: $500K (2024), $2M (2025), $5M+ YTD, tracking ~$7.25M by year-end

  - ~$17M active named pipeline; bottlenecked at 5 engineers

  - Raising seed to scale engineering and productize away from custom integration work

## Humanoid Robots and Physical Labor
- Talikin (Jeremy Soaker): teleoperated humanoid robots, staffing-agency model

  - Robots operated from global south, deployed in global north: profit from labor arbitrage while collecting training data

  - Starting in organic weeding ($11B market), expanding to chemical weeding ($250B), then logistics, manufacturing, care, space

  - Built semi-humanoid demonstrator; 800K ARR pipeline in UK; raised $1.5M to move to California

  - Raising $3.1M for team, Honduras operations center, and field-ready MVP

- 10 Things Inc. (Oliver): bimanual wheeled robot “Ada” for elder care

  - Tasks: clutter pickup, handing objects, verbal medication reminders

  - Ada V0 prototype complete; debuting at Awesome Tech Week in under two weeks

  - Building second V0 unit; using internal “Creator” harness to accelerate design-to-assembly

  - CEO Kimate Richards: 30+ years robotics experience, former AWS robotics lead, Nvidia Omniverse ambassador

  - Raising pre-seed

## Space Autonomy and Life Science Robotics
- Frank Autonomous (Aaron Shay): edge autonomy software for space rovers

  - Problem: 3-second command latency to the moon; $60M+ cost to drive one Mars rover

  - Prototype drove ~2km in Central Valley, mostly GPS-denied, across flat field and river wash

  - 1M-parameter model, 60mW draw, 30ms per direction step

  - Signed contract with Instinct Space (YC-backed moon lander); strong NASA Ames contacts

  - Closing seed round targeting February; plan to launch software to space within a year

- Corvinis Labs (Alex Mirka): agentic lab tools to fix reproducibility in life science research

  - 70% of published research is unreproducible; $100B/year lost to manual pipetting

  - General robotics fails here: no life science training data exists

  - First product “Magpie”: agentic pipette that captures video, thermal, and IMU data during normal human use

  - Data trains a tool-centric VLA transferable across robot platforms

  - Co-founder finishing PhD in 3D AI vision; angel round now, seed Q1 2027

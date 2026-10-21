# Gym partnership value prop

Source: [Granola note](https://notes.granola.ai/d/89edf1e5-5d02-4423-8a8d-ee8d67a61c6a)  
Date: 2026-10-04

### Product Architecture and Privacy Model

- Core setup: cheap on-site hardware (Mac Mini favored) processes video locally, sends only non-personal data to cloud
  - Sensitive video never leaves the facility
  - Remote software updates possible (one-way only); physical visit required to inspect device
- Mac Mini (~$500) chosen over using gym’s own hardware
  - Cleaner pitch to gym: “we never touch your systems”
  - Portable across pilots: if one gym passes, take it to the next
  - Can also attach own camera for demos at sports facilities
- Compute architecture: YOLO Pose runs locally on device, Claude reasons over structured output only
  - Tested: 1 minute of multi-person video analyzed in ~4 seconds (10x real-time)
  - Previously ran on Raspberry Pi in real-time, single person
  - Open question: whether to add a local VLM (e.g. Qwen) for generalized exercise recognition and prompt-driven event triggers

### Gym Integration Challenges

- Need camera access and check-in system access from gym
  - Check-in (RFID/card scan) data needs to flow to Mac Mini in real time over local WiFi
  - Unclear how check-in data is stored or exposed; requires research
  - May need a dedicated camera at the entry point to capture faces on scan-in
- Person re-identification across gym floor
  - Facial recognition on entry, reset after session ends
  - Model already handles brief occlusion (holds identity for ~3 seconds, reattaches if person reappears in same position)
  - Session end inferred from inactivity (15-30 min) or automatic checkout after ~3 hours

### Next Steps and Task Split

- Demo improvements: better tracking videos, fix layout (restore workout plan view)
- Domain: buy and host (Felix), deploy so a link can be sent to gyms
- Pitch deck / one-pager for gyms: Felix to finish and circulate for iteration; also send to YC contacts
- Outreach goal: get a call or in-person visit with a gym; student gym at Berkeley flagged as a potential first target
- Hardware and camera research: Gard to research camera types, RFID data flow, and hardware integration requirements before buying Mac Mini
- VC beach night Thursday (tech week, robotics theme): attend and potentially pitch

### Action Items

- **Research gym camera systems and RFID check-in data flow** (Gard)

  Understand what hardware is needed before committing to a Mac Mini purchase.

- **Buy domain and host the demo live** (Felix)

  Needed before outreach emails can go out with a working link.

- **Finish gym pitch deck and one-pager** (Felix)

  Circulate to the team for iteration; also send to YC contacts.

- **Improve demo with better tracking videos and layout fixes**

  Restore workout plan view; use real multi-person footage to make the demo credible to gyms.

- **Begin gym outreach once domain and deck are ready**

  Goal is a call or visit; Berkeley student gym flagged as a first candidate.


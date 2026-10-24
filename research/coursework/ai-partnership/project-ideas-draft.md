# Three Candidate Problems

Working draft for discussion and revision. These are hypotheses about stakeholder needs, not validated findings or a final project selection.

## 1. Uncertainty about whether underwater maintenance is complete

**Problem or friction:** A connector or component may appear correctly positioned without being securely attached. Determining whether the task is genuinely complete could require additional inspection or operator intervention.

**Target stakeholder:** Underwater robot operators and teams maintaining offshore infrastructure.

**Hypothesis about the need:** More reliable completion checks could reduce repeated work and uncertainty before an operation ends. I would investigate which checks operators currently use and where they still struggle.

## 2. Difficulty comparing robot-learning methods fairly

**Problem or friction:** A promising demonstration or benchmark score may not reveal how a method handles mistakes, unfamiliar scenes or different resource constraints.

**Target stakeholder:** Robotics researchers and small engineering teams choosing methods to investigate.

**Hypothesis about the need:** Clearer comparisons of failure behavior and testing conditions could help teams decide where to invest limited time and compute. I would investigate which information they find missing when assessing published results.

## 3. Uncertainty about real-time robot learning on edge hardware

**Problem or friction:** A robot-learning method that performs well with powerful computing resources may be too slow or memory-intensive for onboard hardware. Teams need to understand how computation delays and limited resources affect task performance.

**Target stakeholder:** Robotics engineers deploying autonomous systems on drones, underwater vehicles and mobile robots with limited onboard compute.

**Hypothesis about the need:** Simulating inference delays and constrained control-update rates, alongside profiling model resource use, could help teams identify which approaches meet a task's real-time requirements. I would compare video-action models (VAMs), vision-language-action models (VLAs) and smaller RL policies under defined compute budgets. Simulated constraints would guide selection, not prove performance on a particular device.

## AI-use disclosure

I supplied the interests and project context. AI organized candidate problems and drafted stakeholder and need hypotheses. I replaced its third suggestion with my interest in real-time deployment under edge-compute constraints. AI helped express that problem; I retain the final choice of research direction.

**Peer-pod input:** [Add the actual discussion and how it changed these candidates before submission.]

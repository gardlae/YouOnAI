# Underwater VLA simulation

## Idea

Build a simulation benchmark for an underwater vehicle or remotely operated vehicle with a gripper, then compare conventional control, learned policies, and VLA-assisted control.

This is promising because underwater manipulation combines degraded vision, vehicle motion, contact dynamics, currents, and limited data. It is also an embodiment that mainstream VLA work has barely targeted.

## Core research question

Where does a frontier or open VLA add measurable value over a conventional autonomy stack for underwater manipulation?

The clean comparison is not “VLA versus everything.” Use the same perception and task setup with several control levels:

1. teleoperation or scripted oracle;
2. classical state estimation, motion planning, and feedback control;
3. behavior cloning or diffusion policy;
4. VLA as a high-level task and subgoal planner;
5. end-to-end or adapted VLA control, if the action interface and data support it;
6. hybrid VLA planning with a low-level conventional controller.

## Simulator choice

Isaac Sim is strong for articulated manipulators, contact physics, RTX cameras, domain randomization, ROS 2, and deployment of Isaac Lab policies. It is not a turnkey underwater simulator: buoyancy, added mass, drag, and currents need custom forces or coupling to a marine simulator.

A practical sequence is:

1. prototype the arm, gripper, cameras, and task in Isaac Sim;
2. add neutral buoyancy, drag, and current disturbances as custom forces;
3. validate the dynamics against a marine simulator such as Stonefish or a Gazebo/DAVE setup;
4. use Isaac Lab for imitation or reinforcement learning;
5. connect candidate VLA models through a stable observation/action adapter.

## Smallest useful experiment

Use a fixed underwater vehicle with a 6-DOF arm before introducing free-swimming control.

Task: locate a colored valve handle, approach it, grasp it, and rotate it to a target angle.

Vary:

- turbidity, lighting, and camera color shift;
- target pose and distractors;
- current disturbance;
- vehicle pose error;
- gripper and contact friction;
- instruction wording.

Measure success rate, time, collisions, grasp retries, intervention count, recovery after perturbation, and generalization to unseen visual conditions.

## Likely contribution

The most defensible initial contribution is a benchmark and adapter layer for evaluating VLA or VLM-planned underwater manipulation. Training a new frontier VLA from scratch is outside the first scope.

## Technical risks

- Isaac Sim hydrodynamics require custom modeling and validation.
- Current VLAs are usually trained on terrestrial robot embodiments and may not map directly to a floating base plus arm.
- A VLA may improve semantic task selection while adding latency or reducing low-level stability.
- Photorealism alone will not guarantee sim-to-real transfer.

## Starting references

- [NVIDIA Isaac Sim overview](https://docs.isaacsim.omniverse.nvidia.com/)
- [Isaac Sim robot simulation](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/index.html)
- [Isaac Lab overview](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/isaac_lab_tutorials/index.html)
- [Importing a manipulator](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/import_manipulator.html)
- [NVIDIA forum discussion of underwater AUV manipulation](https://forums.developer.nvidia.com/t/underwater-auv-manipulation-simulatiom/377344)
- [Learning VLA tracker](../../knowledge-base/Robotics%20learning/Learning%20VLA.md)

## First milestone

Write a one-page system specification with the robot embodiment, simulator boundary, first task, four baselines, and compute requirements. Then build only the classical baseline and evaluation harness; add learned policies after the benchmark produces repeatable results.

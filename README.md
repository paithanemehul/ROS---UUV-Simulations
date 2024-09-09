# Unmanned Underwater Vehicle (UUV) Simulation for Obstacle Avoidance and Mapping

## Overview
This project focuses on the development and analysis of control and navigation algorithms for an unmanned underwater vehicle (UUV) named Rexrov2. Utilizing the Robot Operating System (ROS - melodic) and Gazebo on Windows Sub-system Linux 2 (WSL2), the UUV performs complex tasks such as bathymetric mapping and obstacle avoidance. The simulation tests various trajectories and evaluates the UUV's performance in both manual and autonomous modes.

## Simulation Details
- **Platform**: Rexrov2 UUV model
- **Environment**: Windows Sub-system Linux 2 (WSL2)
- **Technologies**: ROS Melodic, Gazebo, Rviz, Blender
- **Features**:
  - Manual joystick control and autonomous navigation
  - Linear, cubic, and helical trajectory following
  - Obstacle avoidance using Dijkstra and A-star algorithms
  - Bathymetric mapping of the ocean floor with high precision

## Repository Contents
- **src/**: Source files for UUV control algorithms and ROS nodes.
- **models/**: UUV and obstacle models for Gazebo.
- **worlds/**: Gazebo world files simulating different ocean environments.
- **scripts/**: Utility scripts for simulation setup and control.
- **docs/**: Additional documentation and references.

## Setup and Running Simulations
1. **Installation Requirements**:
   - Ubuntu 18.04.5 LTS on WSL2
   - ROS Melodic
   - Gazebo simulation environment
   - Blender for STL file manipulations

2. **Running the Simulation**:
   ```bash
   # Clone the repository
   git clone https://github.com/paithanemehul/ROS---UUV-Simulations.git
   cd ROS---UUV-Simulations

   # Setup ROS environment
   source devel/setup.bash

   # Launch the simulation
   roslaunch your_package simulation_world.launch

   # Control with Joystick
   rosrun your_package joystick_control

## Acknowledgments
- Dr. P.B. Sujit for supervision and guidance
- IISER Bhopal, Department of Electrical Engineering and Computer Science for resources and support
- All friends and colleagues who supported during the development
  

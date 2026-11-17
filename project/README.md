# The Phoenyx-I Mars Mission

## Team Information
- **Members:** Mateusz Michalski, Mathias Kulbotten
- **Practice Group:** T11
- **Team:** Team03

## Mission Objective
Develop an autonomous controller for the Phoenyx-I rover using ROS 2, Python and Gazebo.

- **Level 1:** Corridor navigation using LiDAR and PID control, including 90-degree turns.
- **Level 2:** Obstacle detection and avoidance.
- **Level 3:** Optional, to be decided later.

## Project Structure
- `osr_gazebo/` – Rover model, sensors and controllers.
- `phoenyx_i_bringup/` – Simulation launch file, RViz configuration and training worlds.
- `start_container.sh` – Starts the Docker container.
- `enter_container.sh` – Opens an additional terminal inside Docker.
- `phoenyx_i_control/` – Autonomous controller (planned).

## How to Run

**Ubuntu host:**
```bash
cd ~/ir_ws/src/project
./start_container.sh
```

**Inside Docker:**
```bash
cd ~/ir_ws
colcon build --packages-select osr_gazebo phoenyx_i_bringup
source install/setup.bash
ros2 launch phoenyx_i_bringup sim.launch.py world_path:=maze_1.world
```

**Second Ubuntu terminal:**
```bash
cd ~/ir_ws/src/project
./enter_container.sh
```

**Inside the second Docker terminal:**
```bash
source ~/ir_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Stop teleoperation before running the autonomous controller.

## Progress

### 17/11/2026 – Mission Environment (Section 3)
- Configured and launched Gazebo and RViz2 with Phoenyx-I.
- Verified robot movement using keyboard teleoperation.
- Confirmed that all three ROS 2 controllers are active.
- Verified LiDAR (`/scan`, ~6 Hz) and IMU (`/imu_plugin/out`, ~60 Hz).
- Visualized the rover and LiDAR measurements in RViz2.
- Observed an initial spawning timeout, resolved by manually spawning the robot. A subsequent launch worked automatically.
- Some LiDAR points near the rover require further investigation.

**Next:** Test the remaining training worlds and implement the Level 1 corridor controller.

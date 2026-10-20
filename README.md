# Intelligent Robotics - MAT

## Team Information

- **Team members:** Mateusz Michalski, Mathias Kulbotten 
- **Practice group:** T11
- **Team number:** Team03
- **Robot name:** MAT

---

## Repository Structure

```text
.
├── README.md
├── session1
│   ├── robot_startup.sh
│   └── team_info.txt
├── session2
│   └── mat.urdf
├── session3
│   ├── mat_brain.py
│   ├── robot_arcade
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── game.py
│   │   ├── sensors.py
│   │   └── assets
│   │       └── upc_logo.png
│   └── MAT_description
│       ├── CMakeLists.txt
│       ├── package.xml
│       ├── launch
│       │   └── display.launch.py
│       ├── rviz
│       │   └── urdf_config.rviz
│       └── urdf
│           └── mat.urdf
├── session4
│   ├── start_container.sh
│   ├── enter_container.sh
│   └── mat_bringup
│       ├── CMakeLists.txt
│       ├── package.xml
│       └── launch
│           └── mat.launch.py
└── session5
    └── mat_brain.py

```

---

## Practice Sessions

### Session 1 - Get Familiar with the Tools

#### Overview

During this session, the team learned the basics of the Linux terminal, Bash scripting, Git, GitHub, and Markdown. We practised basic terminal commands, organized the course workspace, and created `team_info.txt` and `robot_startup.sh`. The startup script displays an original welcome message, the team information, its location, and the files stored in the `session1` directory. We also configured a shared GitHub repository and SSH access, cloned the repository locally, and practised the basic Git workflow with `status`, `add`, `commit`, `push`, and `pull`.


#### How to Run

From the root directory of the repository, go to /session1 and run it:

```bash
cd session1
chmod +x robot_startup.sh
./robot_startup.sh
```

### Session 2 - Shape Your Robot in Simulation

#### Overview

During this session, we created the MAT robot model using URDF. The model consists of a rectangular chassis, two continuous drive wheels, a fixed caster wheel, and a `base_footprint` frame. We visualized and inspected the completed robot in RViz2.

#### How to Run

From the root directory of the repository:

```bash
ros2 launch urdf_tutorial display.launch.py model:=$(pwd)/session2/mat.urdf
```

In RViz2, set `Global Options` → `Fixed Frame` to `base_footprint`.

### Session 3 - Build the Foundations of Your Robot

#### Overview

During this session, we created the first Python controller for the MAT robot. The controller reads simulated left, front, and right ultrasonic sensor measurements and uses conditional statements to select an autonomous movement command. Depending on the available space, the robot moves forward, changes lanes, or stops. The algorithm was tested in both Test mode and Game mode using the Robot Run simulator.

#### How to Run

From the root directory of the repository:

```bash
cd session3
python3 mat_brain.py
```

Simulator controls:

- `T` — open Test mode.
- `G` — open Game mode.
- `Space` — generate a test situation or start the challenge.
- `R` — reset the current mode.
- `Esc` — close the simulator.


### Session 4 - Bring Your Robot to Life

#### Overview

During this session, we used Docker to run ROS 2 and Gazebo in a reproducible environment. We created scripts for starting the `intelligent-robotics` container and opening additional terminals inside it.

We extended the MAT URDF model with mass and inertia properties, collision geometry, and Gazebo materials. We created the `mat_bringup` package with a launch file that starts Gazebo, opens RViz2, and spawns the robot.

We added a differential-drive plugin to control the wheels through `/cmd_vel` and publish odometry through `/odom`. We tested keyboard control using `teleop_twist_keyboard` and reduced the caster wheel friction to improve movement.

#### Docker Commands

- `docker images` — list available images.
- `docker ps` — list running containers.
- `docker ps -a` — list running and stopped containers.
- `docker run` — create and start a container.
- `docker exec` — run a command or open a terminal inside a running container.

#### How to Run

Start the container from an Ubuntu terminal:

```bash
cd ~/ir_ws/src/session4
./start_container.sh
```

Inside the container, build the packages and launch the simulation:

```bash
cd ~/ir_ws
colcon build --packages-select MAT_description mat_bringup
source install/setup.bash
ros2 launch mat_bringup mat.launch.py
```

Keep the simulation running. Open another Ubuntu terminal and enter the same container:

```bash
cd ~/ir_ws/src/session4
./enter_container.sh
```

Inside this second container terminal, start keyboard control:

```bash
source ~/ir_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Keep the keyboard focus on the teleop terminal when sending commands:

- `i` — move forward.
- `,` — move backward.
- `j` — turn left.
- `l` — turn right.
- `k` — stop.

Use `Ctrl+C` in each terminal to stop the corresponding program.

### Session 5 - Connect the Mind of Your Robot

#### Part 1 - Python Classes

We refactored the MAT controller from Session 3 into a Python class called
`RobotBrain`, preserving the original decision algorithm and distance thresholds.

The class stores the robot information, sensor measurements and thresholds
as attributes. The `get_sensor_data()` method updates and displays the
measurements, `decide_action()` selects a movement, and `process_scan()`
connects both methods and returns the selected action to Robot Run.

#### How to Run

Run from an Ubuntu terminal:

```bash
cd ~/ir_ws/src/session5
export PYTHONPATH="$HOME/ir_ws/src/session3:$PYTHONPATH"
python3 mat_brain.py
```

The `PYTHONPATH` command must be repeated in each new terminal.


### Session 6 - Bring Intelligence to Your Robot

To be completed.

---

## Project

The project has not yet been defined.

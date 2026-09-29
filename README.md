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
└── README.md
└──session1
      └──robot_startup.sh
      └──team_info.txt
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

### Session 4 - Bring Your Robot to Life

To be completed.

### Session 5 - Connect the Mind of Your Robot

To be completed.

### Session 6 - Bring Intelligence to Your Robot

To be completed.

---

## Project

The project has not yet been defined.

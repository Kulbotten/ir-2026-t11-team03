import os
from uuid import uuid4
 
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    IncludeLaunchDescription,
    RegisterEventHandler,
    SetEnvironmentVariable,
    UnsetEnvironmentVariable,
)
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
 
 
def generate_launch_description():
    mat_description_directory = get_package_share_directory("MAT_description")
 
    urdf_file = os.path.join(mat_description_directory, "urdf", "mat.urdf")
    rviz_config_file = os.path.join(
        mat_description_directory, "rviz", "urdf_config.rviz"
    )
 
    with open(urdf_file, "r") as file:
        robot_description = file.read()
 
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {
                "robot_description": robot_description,
                "use_sim_time": True,
            }
        ],
        output="screen",
    )
 
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config_file],
        parameters=[{"use_sim_time": True}],
        output="screen",
    )
 
    world_path = os.path.join(
        get_package_share_directory("mat_bringup"), "worlds", "maze_1.world"
    )
    gzserver_launch = os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gzserver.launch.py"
    )
 
    gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gzserver_launch),
        launch_arguments={"world": world_path, "verbose": "true"}.items(),
    )
 
    gazebo_client = ExecuteProcess(
        cmd=["env", "-u", "GAZEBO_MODEL_PATH", "gzclient", "--verbose"],
        output="screen",
    )
 
    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "mat"],
        output="screen",
    )
 
    def open_gazebo_after_spawn(event, _context):
        return [gazebo_client] if event.returncode == 0 else []
 
    return LaunchDescription([
        DeclareLaunchArgument(
            "gazebo_port",
            default_value="11346",
            description="Local Gazebo Classic master port.",
        ),
        UnsetEnvironmentVariable("GAZEBO_HOSTNAME"),
        SetEnvironmentVariable("GAZEBO_IP", "127.0.0.1"),
        SetEnvironmentVariable(
            "GAZEBO_MASTER_URI",
            ["http://127.0.0.1:", LaunchConfiguration("gazebo_port")],
        ),
        SetEnvironmentVariable("IGN_PARTITION", f"mat_{uuid4().hex}"),
        robot_state_publisher,
        rviz,
        gazebo_server,
        RegisterEventHandler(
            OnProcessExit(target_action=spawn_robot, on_exit=open_gazebo_after_spawn)
        ),
        spawn_robot,
    ])
import os
 
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
 
 
def generate_launch_description():
    mat_description_directory = get_package_share_directory(
        "MAT_description"
    )
 
    urdf_file = os.path.join(
        mat_description_directory,
        "urdf",
        "mat.urdf",
    )
 
    rviz_config_file = os.path.join(
        mat_description_directory,
        "rviz",
        "urdf_config.rviz",
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
 
    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            "-s",
            "libgazebo_ros_factory.so",
        ],
        output="screen",
    )
 
    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic",
            "robot_description",
            "-entity",
            "mat",
        ],
        output="screen",
    )
 
    return LaunchDescription([
        robot_state_publisher,
        rviz,
        gazebo,
        spawn_robot,
    ])
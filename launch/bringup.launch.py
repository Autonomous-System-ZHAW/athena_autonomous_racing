from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("ldlidar_stl_ros2"),
                "launch",
                "ld19.launch.py",
            )
        )
    )

    vesc_driver_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("vesc_driver"),
                "launch",
                "vesc_driver_node.launch.py",
            )
        )
    )

    ackermann_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("vesc_ackermann"),
                "launch",
                "ackermann_to_vesc_node.launch.xml",
            )
        )
    )

    follow_the_gap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("follow_the_gap"),
                "launch",
                "follow_the_gap.launch.py",
            )
        )
    )

    smacc2_node = Node(
        package="sm_my_robot",
        executable="sm_my_robot_node",
        name="state_machine",
        output="screen",
    )

    return LaunchDescription(
        [
            lidar_launch,
            vesc_driver_launch,
            ackermann_launch,
            follow_the_gap_launch,
            smacc2_node,
        ]
    )

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


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

    vesc_to_odom_node = Node(
        package="vesc_ackermann",
        executable="vesc_to_odom_node",
        output="screen",
    )

    ackermann_launch = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
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

    remote_control = Node(
        package="athena_remote_control",
        executable="remote_autonomous_control_node",
        output="screen",
    )

    joy_node = Node(package="joy", executable="joy_node", output="screen")

    state_machine = Node(
        package="athena_lifecycle_state_machine",
        executable="state_machine",
        output="screen",
    )

    """

    foxglove_launch = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("foxglove_bridge"),
                "launch",
                "foxglove_bridge_launch.xml",
            )
        )
    )
    """

    return LaunchDescription(
        [
            lidar_launch,
            vesc_driver_launch,
            ackermann_launch,
            follow_the_gap_launch,
            remote_control,
            joy_node,
            state_machine,
            # foxglove_launch,
        ]
    )

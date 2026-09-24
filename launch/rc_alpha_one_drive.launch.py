from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():

    follow_the_gap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("follow_the_gap"),
                "launch",
                "follow_the_gap.launch.py",
            )
        )
    )

    led_manager_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("athena_led_manager"),
                "launch",
                "led_manager.launch.py",
            )
        )
    )

    state_machine_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("athena_lifecycle_state_machine"),
                "launch",
                "lifecycle_state_machine.launch.py",
            )
        )
    )

    joy_node = Node(
        package="joy",
        executable="joy_node",
        output="screen",
    )

    remote_control = Node(
        package="athena_remote_control",
        executable="remote_control",
        output="screen",
    )

    return LaunchDescription(
        [
            follow_the_gap_launch,
            led_manager_launch,
            joy_node,
            remote_control,
            state_machine_launch,
        ]
    )

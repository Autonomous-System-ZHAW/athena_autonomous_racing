from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():
    # gerneral pkg
    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("athena_description"),
                "launch",
                "display.launch.py",
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

    # hardware pkg
    led_manager_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("athena_led_manager"),
                "launch",
                "led_manager.launch.py",
            )
        )
    )

    follow_the_gap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("athena_follow_the_gap"),
                "launch",
                "follow_the_gap.launch.py",
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
            description,
            state_machine_launch,
            follow_the_gap_launch,
            led_manager_launch,
            joy_node,
            remote_control,
        ]
    )

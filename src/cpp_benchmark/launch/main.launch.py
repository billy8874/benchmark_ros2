from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('cpp_image_pubsub'),
                    'launch',
                    'broadcast.launch.py'
                ])
            ]),
            launch_arguments={
                'resolution': '480',
                'frequency': '30',
                'n_sub': '2',
                'm_sub': '1'
            }.items()
        )
    ])
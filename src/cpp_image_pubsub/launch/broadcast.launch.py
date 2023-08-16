from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():
    resolution = LaunchConfiguration('resolution')
    frequency = LaunchConfiguration('frequency')
    n_sub = LaunchConfiguration('n_sub')
    m_pub = LaunchConfiguration('m_pub')

    resolution_launch_arg = DeclareLaunchArgument(
        'resolution',
        default_value='/root/ros2_ws/imgs/scenery_854x480.jpg'
    )
    frequency_launch_arg = DeclareLaunchArgument(
        'frequency',
        default_value='30'
    )
    n_sub_launch_arg = DeclareLaunchArgument(
        'n_sub',
        default_value='2'
    )
    m_pub_launch_arg = DeclareLaunchArgument(
        'm_pub',
        default_value='1'
    )

    all_blocks = [resolution_launch_arg, frequency_launch_arg, n_sub_launch_arg, m_pub_launch_arg]

    hz = frequency
    n = 5
    m = 1

    for i in range(m):
        all_blocks += [Node(
            namespace='block'+str(i), package='cpp_image_pubsub', executable='img_pub', name='publisher', arguments=[resolution,hz]),]
        for j in range(n):
            all_blocks += [Node(
                namespace='block'+str(i), package='cpp_image_pubsub', executable='img_sub', name='subscriber_'+str(j)),]
    return LaunchDescription(all_blocks)
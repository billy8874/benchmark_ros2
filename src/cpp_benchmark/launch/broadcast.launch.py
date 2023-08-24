from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
import sys
import re

def generate_launch_description():
    payload_size = LaunchConfiguration('payload_size')
    frequency = LaunchConfiguration('frequency')
    n_sub = LaunchConfiguration('n_sub')
    m_pub = LaunchConfiguration('m_pub')

    payload_size_launch_arg = DeclareLaunchArgument(
        'payload_size',
        default_value='1000B'
    )
    frequency_launch_arg = DeclareLaunchArgument(
        'frequency',
        default_value='30'
    )
    n_sub_launch_arg = DeclareLaunchArgument(
        'n_sub',
        default_value='5'
    )
    m_pub_launch_arg = DeclareLaunchArgument(
        'm_pub',
        default_value='1'
    )

    all_blocks = [payload_size_launch_arg, frequency_launch_arg, n_sub_launch_arg, m_pub_launch_arg]

    n = [int(s) for s in re.findall(r'\b\d+\b', sys.argv[6])][0]
    m = [int(s) for s in re.findall(r'\b\d+\b', sys.argv[7])][0]

    for i in range(m):
        all_blocks += [Node(
            namespace='block'+str(i), package='cpp_benchmark', executable='data_pub', name='publisher', arguments=[payload_size,frequency]),]
        for j in range(n):
            all_blocks += [Node(
                namespace='block'+str(i), package='cpp_benchmark', executable='data_sub', name='subscriber_'+str(j), arguments=[n_sub]),]
    return LaunchDescription(all_blocks)
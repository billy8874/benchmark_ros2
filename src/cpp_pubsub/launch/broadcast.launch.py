from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    all_blocks = []
    for i in range(1):
        all_blocks += [launch_ros.actions.Node(
            namespace='block'+str(i), package='cpp_pubsub', executable='talker', name='talker'),
        launch_ros.actions.Node(
            namespace='block'+str(i), package='cpp_pubsub', executable='listener', name='listener_1'),
        launch_ros.actions.Node(
            namespace='block'+str(i), package='cpp_pubsub', executable='listener', name='listener_2'),
        launch_ros.actions.Node(
            namespace='block'+str(i), package='cpp_pubsub', executable='listener', name='listener_3'),
        launch_ros.actions.Node(
            namespace='block'+str(i), package='cpp_pubsub', executable='listener', name='listener_4'),]
    return LaunchDescription(all_blocks)

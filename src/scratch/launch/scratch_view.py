from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

from os import path
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
#        IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/scratch.py'])),
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', path.join(get_package_share_directory('rplidar_ros2'), 'rviz', 'rplidar.rviz')]
        )
    ])

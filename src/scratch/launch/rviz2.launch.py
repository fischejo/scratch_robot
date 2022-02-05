from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

from os import path
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    rviz_config_dir = path.join(get_package_share_directory('realsense2_camera'), 'rviz', 'pointcloud.rviz')
    return LaunchDescription([
        Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output = 'screen',
        arguments=['-d', rviz_config_dir],
        parameters=[{'use_sim_time': False}])
    ])

"""Launch realsense2_camera node."""
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from os import path

def generate_launch_description():    
    launch_dir = path.join(get_package_share_directory('realsense2_camera'), 'launch')
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_dir, '/rs_launch.py']),
            launch_arguments=[("enable_pointcloud", "true")]
        )
    ])

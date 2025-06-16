from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Kobuki launch
    kobuki_pkg_share = get_package_share_directory('kobuki_node')
    kobuki_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(kobuki_pkg_share, 'launch', 'kobuki_node-launch.py')
        ),
        launch_arguments={'port': '/dev/ttyUSB0'}.items()
    )
    
    # realSense camera launch
    realsense_pkg_share = get_package_share_directory('realsense2_camera')
    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(realsense_pkg_share, 'launch', 'rs_launch.py')
        ),
        launch_arguments={
            'align_depth': 'true',
            'enable_pointcloud': 'true',
            'enable_infra':                   'true',
            'enable_infra1':                  'true',
            'enable_infra2':                  'true',
            'depth_module.infra1_format':     'y8',
            'depth_module.infra2_format':     'y8',
            'depth_module.profile':           '1280x720x6',
            'rgb_camera.color_profile':       '1280x720x6'
        }.items()
    )

    return LaunchDescription([
        kobuki_launch,
        realsense_launch,
        
        # joy launch for the controller
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen'
        ),

        # teleop_twist_joy launch
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy_node',
            output='screen',
            parameters=['src/teleop_twist_joy/config/joy_config.yaml']
         )
    ])


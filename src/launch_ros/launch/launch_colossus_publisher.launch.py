import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  config = os.path.join(
          get_package_share_directory("navtech_ros"),
          "config",
          "colossus_publisher.yaml",
          )
  return LaunchDescription([

    Node(
        package="navtech_nav_ros",
        parameters=[config],
        executable="colossus_publisher"
    )
  ])

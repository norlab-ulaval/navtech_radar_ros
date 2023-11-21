import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  config = os.path.join(
          get_package_share_directory("navtech_ros"),
          "config",
          "b_scan_publisher",
          )
  return LaunchDescription([

    Node(
        package="navtech_ros",
        parameters=[config],
        executable="b_scan_publisher"
    ),

    Node(
        package="tf2_ros",
        arguments = ["0", "0", "0", "0", "0", "0", "map", "b_scan_image"],
        executable="static_transform_publisher"
    ),

    Node(
        package="rviz2",
        arguments=["-d../../rviz_views/b_scan_view.rviz"],
        executable="rviz2"
    )
  ])

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  config = os.path.join(
          get_package_share_directory("navtech_ros"),
          "config",
          "point_cloud_publisher.yaml",
          )
  return LaunchDescription([

    Node(
        package="navtech_nav_ros",
        parameters=[config],
        executable="point_cloud_publisher"
    ),

    Node(
        package="tf2_ros",
        arguments = ["0", "0", "0", "0", "0", "0", "map", "point_cloud"],
        executable="static_transform_publisher"
    ),

    Node(
        package="rviz2",
        arguments=["-d../../rviz_views/point_cloud_view.rviz"],
        executable="rviz2"
    )
  ])

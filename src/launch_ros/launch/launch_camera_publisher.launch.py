import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  config = os.path.join(
          get_package_share_directory("camera_ros",
              "config",
              "camera_publisher.yaml",
              )
  return LaunchDescription([

    Node(
        package="camera_ros",
        parameters=[config],
        executable="camera_publisher"
    ),

    Node(
        package="tf2_ros",
        arguments = ["0", "0", "0", "0", "0", "0", "map", "camera_image"],
        executable="static_transform_publisher"
    ),

    Node(
        package="rviz2",
        arguments=["-d../../rviz_views/camera_view.rviz"],
        executable="rviz2"
    )
  ])

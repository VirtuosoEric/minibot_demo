#!/bin/bash
source /opt/ros/kinetic/setup.bash
source /home/ubuntu/catkin_ws/devel/setup.bash

export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')
export ROS_MASTER_URI=http://192.168.4.10:11311/ 

rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped \
"{header: {stamp: now, frame_id: 'map'}, pose: {position: {x: ${1:-0}, y: ${2:-0}, z: 0.0},\
orientation: {x: ${3:-0}, y: ${4:-0}, z: ${5:-0}, w: ${6:-1.0}}}}"
#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1"  != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
if [ -d /root/ros2_ws/install/mypkg ]; then
  export AMENT_PREFIX_PATH="/root/ros2_ws/install/mypkg${AMENT_PREFIX_PATH:+:$AMENT_PREFIX_PATH}"
else
  export AMENT_PREFIX_PATH="/root/ros2_ws/install${AMENT_PREFIX_PATH:+:$AMENT_PREFIX_PATH}"
fi
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'

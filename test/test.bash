#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1"  != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
echo "AMENT_PREFIX_PATH=$AMENT_PREFIX_PATH"
echo "COLCON_PREFIX_PATH=$COLCON_PREFIX_PATH"
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'

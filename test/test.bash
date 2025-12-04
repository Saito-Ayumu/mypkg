#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Claus

dir=~
[ "$1"  != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'

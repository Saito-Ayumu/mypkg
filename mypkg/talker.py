#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Int16, 'countup', 10)
        self.count = 0
        self.timer = self.create_timer(0.5, self.on_timer)  # 2Hz

    def on_timer(self):
        self.count += 1
        msg = Int16()
        msg.data = self.count
        self.pub.publish(msg)
        self.get_logger().info(f'Talk: {msg.data}')


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.sub = self.create_subscription(Int16, 'countup', self.cb, 10)

    def cb(self, msg: Int16):
        self.get_logger().info(f'Listen: {msg.data}')


def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


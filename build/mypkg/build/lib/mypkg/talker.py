#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Int16, 'countup', 10)
        self.i = 0
        self.create_timer(0.5, self.on_timer)

    def on_timer(self):  
        msg = Int16()
        msg.data = self.i
        self.pub.publish(msg)
        self.i += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


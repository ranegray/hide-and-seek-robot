#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')


def main(args=None):
    rclpy.init(args=args)
    node = LidarNode()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

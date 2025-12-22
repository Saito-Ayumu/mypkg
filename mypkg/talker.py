#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")
 
 
def cb(request, response):
    if request.name == "齊藤歩":  
        response.age = 20
    else:
        response.age = 255
    
    return response

    
def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)

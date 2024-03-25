#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import numpy as np
import math
from ackermann_msgs.msg import AckermannDriveStamped
#Change this line (1) from gym
from sensor_msgs.msg import Joy

import time

class TESTNode(Node):
    def __init__(self):
        super().__init__("waypoint_follower")
        
        #Change this line (2) from gym to /pf/pose/odom
        self.pose_subscriber = self.create_subscription(Odometry, '/pf/pose/odom', self.callback, 10)
        self.drive_pub = self.create_publisher(AckermannDriveStamped, "/drive", 10)
        #Change this line (3) from gym
        self.joy_sub = self.create_subscription(Joy, "/joy", self.callbackJoy, 10)
        self.Joy7 = 0

        self.start_time = time.perf_counter()
        self.go_time = 3.0
        self.set_speed = 1.0

        self.get_logger().info("Initlialized")

    def callback(self, msg:Odometry):

        cmd = AckermannDriveStamped()

        quat_ori = [msg.pose.pose.orientation.x,
                    msg.pose.pose.orientation.y,
                    msg.pose.pose.orientation.z,
                    msg.pose.pose.orientation.w]
        
        yaw = self.euler_from_quaternion(quat_ori[0], quat_ori[1], quat_ori[2], quat_ori[3])

        # if self.Joy7 == 1:
        #     cmd.drive.steering_angle = 0.2
        # else:
        #     cmd.drive.steering_angle = 0.0

        # cmd.drive.speed = 0.0
        
        #cmd.drive.speed = 2.0

        current_time = time.perf_counter()

        if (current_time - self.start_time) < self.go_time:
            cmd.drive.speed = self.set_speed
            self.get_logger().info("Drive, Time:" + str(current_time - self.start_time))
        else:
            cmd.drive.speed = 0.0
            self.get_logger().info("Stop, Time:" + str(current_time - self.start_time))

            if (current_time - self.start_time) > self.go_time * 2.0:
                self.start_time = time.perf_counter()
                self.set_speed = self.set_speed * -1.0

        self.drive_pub.publish(cmd)

    #Change this function (4) from gym
    def callbackJoy(self, msg: Joy):
        self.Joy7 = msg.buttons[7]


    def euler_from_quaternion(self,x, y, z, w):  
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return yaw_z # in radians
    
def main(args = None):
    
    #use - ros2 run teleop_twist_keyboard teleop_twist_keyboard 
    #to move the car manually around the map
    rclpy.init(args = args)
    controller_node = TESTNode()
 
    rclpy.spin(controller_node)          #allows the node to always been running 
    rclpy.shutdown()                    #shut dowwn the node


if __name__ == "__main__":
    main()

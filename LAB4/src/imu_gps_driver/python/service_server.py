#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from imu_gps_driver.msg import Vectornav
import numpy as np
from imu_gps_driver.srv import convert_to_quaternion,convert_to_quaternionResponse

def get_quaternion_from_euler(req):
	roll = np.radians(req.roll)
	pitch = np.radians(req.pitch)
	yaw = np.radians(req.yaw)
	qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
	qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
	qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
	qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

	return convert_to_quaternionResponse(qx,qy,qz,qw)

def server():
	
	rospy.init_node('convert_to_quaternion')
	s = rospy.Service('convert_to_quaternion',convert_to_quaternion,get_quaternion_from_euler)
	rospy.spin()

if __name__ == "__main__":
	server()


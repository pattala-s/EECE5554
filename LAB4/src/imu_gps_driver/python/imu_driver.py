#!/usr/bin/env python


import time
import utm
import serial
import rospy
from std_msgs.msg import String
from imu_gps_driver.msg import Vectornav
import argparse
import sys
from imu_gps_driver.srv import *

#imu_port = str(rospy.get_param('/imu_driver/imu_port')) 
#data = serial.Serial(imu_port, 4800)
data = serial.Serial('/dev/ttyUSB1', 115200)

data.write('$VNWRG,07,40*59'.encode())
		
def gps_driver():
	pub = rospy.Publisher('imu', Vectornav, queue_size=10)
	rospy.init_node('imu_data', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	msg1 = Vectornav()
	time = rospy.Time()
	while not rospy.is_shutdown():
		try:
			line = data.readline()
			values = line.decode('ascii')
			if '$VNYMR' in values:
				val = values.split(',')
				now = rospy.get_rostime()
				msg1.header.frame_id = 'imu1_frame'
				msg1.header.stamp.secs = now.secs
				msg1.header.stamp.nsecs = now.nsecs
				msg1.imu.header.stamp.secs = now.secs
				msg1.imu.header.stamp.nsecs = now.nsecs
				msg1.mag_field.header.stamp.secs = now.secs
				msg1.mag_field.header.stamp.nsecs = now.nsecs
				msg1.imu.linear_acceleration.x = float(val[8])
				msg1.imu.linear_acceleration.y = float(val[9])
				msg1.imu.linear_acceleration.z = float(val[10])
				msg1.imu.angular_velocity.x = float(val[11])
				msg1.imu.angular_velocity.y = float(val[11])
				msg1.imu.angular_velocity.z = float(val[12].split('*')[0])
				msg1.mag_field.magnetic_field.x = float(val[5])
				msg1.mag_field.magnetic_field.y = float(val[6])
				msg1.mag_field.magnetic_field.z = float(val[7])
				service = rospy.ServiceProxy('convert_to_quaternion',convert_to_quaternion)
				resp = service(float(val[3]),float(val[2]),float(val[1]))
				msg1.imu.orientation.x = resp.x
				msg1.imu.orientation.y = resp.y
				msg1.imu.orientation.z = resp.z
				msg1.imu.orientation.w = resp.w

			else:
				pass
				
		except:
			pass
			
		rospy.loginfo(msg1)
		pub.publish(msg1)
		rate.sleep()
		
	
	
if __name__ == '__main__':
	try:
		
		gps_driver()
		
	except rospy.ROSInterruptException:
		pass


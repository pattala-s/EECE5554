#!/usr/bin/env python

import time
import utm
import serial
import rospy
from std_msgs.msg import String
from imu_gps_driver.msg import gps_msg
import argparse
import sys

#gps_port = str(rospy.get_param('/gps_driver/gps_port')) 
#data = serial.Serial(gps_port, 4800)
data = serial.Serial('/dev/ttyUSB2', 4800)
		
def gps_driver():
	pub = rospy.Publisher('gps', gps_msg, queue_size=10)
	rospy.init_node('gps_data', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	msg1 = gps_msg()
	time = rospy.Time()
	while not rospy.is_shutdown():
		try:
			line = data.readline()
			values = line.decode('ascii')
			if '$GPGGA' in values:
				val = values.split(',')
				gps_header = val[0]
				latitude = val[2]
				lat_dd = float(latitude[0:2])
				lat_mm = float(latitude[2:])/60
				lat_dir = val[3]
				longitude = val[4]
				long_dd = float(longitude[0:3])
				long_mm = float(longitude[3:])/60
				long_dir = val[5]
				if lat_dir == 'N':
					lat_conv = lat_dd + lat_mm
				else:
					lat_conv = -(lat_dd + lat_mm)
				if long_dir == 'E':
					long_conv = long_dd + long_mm
				else:
					long_conv = -(long_dd + long_mm)
				UTM = utm.from_latlon(lat_conv,long_conv)
				quality = val[6]
				sats = val[7]
				HDOP = val[8]
				altitude = val[9]
				alt_units = val[10]
				udul = val[11]
				udul_units = val[12]
				time.secs = int(val[1][0:6])
				msg1.Header.stamp = time
				msg1.Header.frame_id = 'GPS1_FRAME'
				msg1.Latitude = lat_conv
				msg1.Longitude = long_conv
				msg1.Altitude = float(altitude)
				msg1.HDOP = float(HDOP)
				msg1.UTM_easting = UTM[0]
				msg1.UTM_northing = UTM[1]
				msg1.UTC = val[1][0:2] + ":" + val[1][2:4] + ":" + val[1][4:6]
				msg1.Zone = UTM[2]
				msg1.Letter = UTM[3]
						

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


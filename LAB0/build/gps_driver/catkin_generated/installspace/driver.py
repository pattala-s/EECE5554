#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from gps_driver.msg import gps_msg
import serial
import rospy
import utm
import sys

def mynode():
  pub = rospy.Publisher('gps', gps_msg, queue_size=10)
  rospy.init_node('mynode','anonymous=True')
  port = rospy.get_param('/port_number','/dev/ttyUSB0')
  
  
  
  rate = rospy.Rate(10) # 10hz
  msg = gps_msg()
  ser = serial.Serial(port, baudrate="4800")

  while(not rospy.is_shutdown()):
    sac = str(ser.readline())
    if 'GPGGA' in str(sac):
        print(sac)
        H = float(sac.split(",")[1])
        x = float(sac.split(",")[2])
        a = float(sac.split(",")[4])
        m = (sac.split(",")[3])
        n = (sac.split(",")[5])
        
        lat = str(x)
        lon = str(a)
        time = str(H)
        
        #print (float(lat[:2])+float(lat[2:])/60)
        sec = float(time[:2])*60*60+float(time[2:4])*60+float(time[4:6])
        nsec = (float(time[6:]))*10e6
        y = (float(lat[ :2])+float(lat[2: ]))/60
        z = ((float(lon[ :3])+float(lon[3: ]))/60)*(-1)
        
        
        gap = utm.from_latlon(y,z)
        msg.Latitude = y
        msg.Longitude = z
        msg.UTM_northing = gap[0]
        msg.UTM_easting = gap[1]
        msg.Altitude = float(sac.split(",")[8])
        msg.HDOP=float(sac.split(",")[9])
        msg.UTC=float(sac.split(",")[1])
        msg.Zone = gap[2]
        msg.Letter = gap[3]
        msg.Header.stamp.secs = int(sec)
        msg.Header.stamp.nsecs = int(nsec)
        msg.Header.frame_id = "GPS1_FRAME"
        #print(msg)
        print(sec, nsec)
        print(f"lat long zone {gap}")
        pub.publish(msg)
if __name__ == '__main__':        
        try:
          mynode()
        except rospy.ROSInterruptException:
              pass
  

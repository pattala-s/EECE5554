#!/usr/bin/env python3
#-- coding: utf-8 --

from gnss_driver.msg import gnss_msg
import serial
import rospy
import utm
from std_msgs.msg import String
import sys

def mygps():
    pub = rospy.Publisher('gps', gnss_msg, queue_size=10)
    rospy.init_node('mygps','anonymous=True')
    port = rospy.myargv(argv=sys.argv)
    name = str(port[1])
    
    
    rate = rospy.Rate(10) # 10hz
    msg = gnss_msg()
    data = serial.Serial(name,baudrate="57600")
    while(not rospy.is_shutdown()):
        raw_data = data.readline().decode('utf-8')
        if '$GNGGA' in raw_data:
            L = float(raw_data.split(",")[2])
            Lo = float(raw_data.split(",")[4])
            A = float(raw_data.split(",")[8])
            m = (raw_data.split(",")[3])
            n = (raw_data.split(",")[5])
            
            lat = str(Lo)
            lon = str(A)
            time = str(L)
            
            sec = float(time[:2])*60*60+float(time[2:4])*60+float(time[4:6])
            nsec = (float(time[6:]))*10e6
            y = (float(lat[ :2])+float(lat[2: ]))/60
            z = ((float(lon[ :3])+float(lon[3: ]))/60)*(-1)
            
            
            gap = utm.from_latlon(y,z)
            msg.Latitude = y
            msg.Longitude = z
            msg.UTM_northing = gap[0]
            msg.UTM_easting = gap[1]
            msg.Altitude = float(raw_data.split(",")[8])
            msg.HDOP=float(raw_data.split(",")[9])
            msg.UTC=float(raw_data.split(",")[1])
            msg.Zone = gap[2]
            msg.Letter = gap[3]
            msg.FIX=int(raw_data[6])
            msg.header.stamp.secs = int(sec)
            msg.header.stamp.nsecs = int(nsec)
            msg.header.frame_id = "GPS1_FRAME"
            print(msg)
            pub.publish(msg)


if __name__ == '__main__':
    try:
        mygps()
    except rospy.ROSInterruptException:
            pass

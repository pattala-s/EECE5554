#!/usr/bin/env python3
#-- coding: utf-8 --
import serial
import numpy as np
from cmath import pi
import rospy
from std_msgs.msg import String
from imu_driver.msg import Vectornav
import sys



def imu():
    rospy.init_node('imu', anonymous= True)
    serial_port = rospy.get_param('~port')
    #serial_port = "/dev/pts/3"
    serdata = serial.Serial(port=serial_port, baudrate=115200, bytesize=8, timeout = 5, stopbits= serial.STOPBITS_ONE)
    serdata.write(b"VNWRG,07,40*XX")
    pub = rospy.Publisher('/imu', Vectornav,queue_size=10)     
    #now = rospy.get_rostime()

    while not rospy.is_shutdown():
        line= serdata.readline()
        linestring=line.decode("utf-8")
        print(linestring)
        linesplit=linestring.split(",")
        rospy.loginfo(linesplit)
        #if(linesplit[0]=="\r$VNYMR"):
        if("$VNYMR" in linesplit[0]):      
            rpy=degreestoquaternions(linesplit[3],linesplit[2],linesplit[1])   
            DATA = Vectornav()
            DATA.Header.frame_id = 'IMU1_Frame'
            DATA.IMU.orientation.x= float(rpy[0])
            DATA.IMU.orientation.y= float(rpy[1])
            DATA.IMU.orientation.z= float(rpy[2])
            DATA.IMU.orientation.w= float(rpy[3])

            DATA.IMU.angular_velocity.x= float(linesplit[10])
            DATA.IMU.angular_velocity.y= float(linesplit[11])
            DATA.IMU.angular_velocity.z= float(linesplit[12][:-4])
            
            DATA.IMU.linear_acceleration.x= float(linesplit[7])
            DATA.IMU.linear_acceleration.y= float(linesplit[8])
            DATA.IMU.linear_acceleration.z= float(linesplit[9])
            
            DATA.MagField.magnetic_field.x=float(linesplit[4])
            DATA.MagField.magnetic_field.y=float(linesplit[5])
            DATA.MagField.magnetic_field.z=float(linesplit[6])

            DATA.Header.stamp.secs=now.secs
            DATA.Header.stamp.nsecs=now.nsecs
            
            DATA.raw_IMU= linestring
            #print("success")
            pub.publish(DATA)
            


def degreestoquaternions(rollr,rollp,rolly):

    radr=float(rollr)*pi/180
    radp=float(rollp)*pi/180
    rady=float(rolly)*pi/180
    
    qx = np.sin(radr/2) * np.cos(radp/2) * np.cos(rady/2) - np.cos(radr/2) * np.sin(radp/2) * np.sin(rady/2)
    qy = np.cos(radr/2) * np.sin(radp/2) * np.cos(rady/2) + np.sin(radr/2) * np.cos(radp/2) * np.sin(rady/2)
    qz = np.cos(radr/2) * np.cos(radp/2) * np.sin(rady/2) - np.sin(radr/2) * np.sin(radp/2) * np.cos(rady/2)
    qw = np.cos(radr/2) * np.cos(radp/2) * np.cos(rady/2) + np.sin(radr/2) * np.sin(radp/2) * np.sin(rady/2)
    
    return [qx, qy, qz, qw]
    

if __name__ =="__main__":
    try:
        imu()
    except rospy.ROSInterruptException:
        pass

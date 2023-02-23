#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import bagpy
from bagpy  import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
 
 
A=bagreader('/home/srinidhi/catkin_ws/src/Data/walkingline.bag')
B=bagreader('/home/srinidhi/catkin_ws/src/Data/walkingfield.bag')
C=bagreader('/home/srinidhi/catkin_ws/src/Data/stdsnell.bag')

A.topic_table
B.topic_table
C.topic_table

x = A.message_by_topic('/gps')
y = B.message_by_topic('/gps')
z = C.message_by_topic('/gps')


df_x = pd.read_csv(x)
df_y = pd.read_csv(y)
df_z = pd.read_csv(z)


df_x['UTM_northing_std']= df_x['UTM_northing']- df_x['UTM_northing'].min()
df_x['UTM_easting_std']= df_x['UTM_easting']- df_x['UTM_easting'].min()

df_y['UTM_northing_std']= df_y['UTM_northing']- df_y['UTM_northing'].min()
df_y['UTM_easting_std']= df_y['UTM_easting']- df_y['UTM_easting'].min()

df_z['UTM_northing_std']= df_z['UTM_northing']- df_z['UTM_northing'].min()
df_z['UTM_easting_std']= df_z['UTM_easting']- df_z['UTM_easting'].min()


df_x[['UTM_northing_std','UTM_easting_std']].plot.scatter(x='UTM_northing_std',y='UTM_easting_std')

df_y[['UTM_northing_std','UTM_easting_std']].plot.scatter(x='UTM_northing_std',y='UTM_easting_std')

df_z[['UTM_northing_std','UTM_easting_std']].plot.scatter(x='UTM_northing_std',y='UTM_easting_std')



df_x['Altitude_std']= df_x['Altitude']- df_x['Altitude'].min()
df_x['Time_std']= df_x['Time']- df_x['Time'].min()

df_y['Altitude_std']= df_y['Altitude']- df_y['Altitude'].min()
df_y['Time_std']= df_y['Time']- df_y['Time'].min()

df_z['Altitude_std']= df_z['Altitude']- df_z['Altitude'].min()
df_z['Time_std']= df_z['Time']- df_z['Time'].min()


df_x[['Altitude_std','Time_std']].plot.scatter(x='Altitude_std',y='Time_std')

df_y[['Altitude_std','Time_std']].plot.scatter(x='Altitude_std',y='Time_std')

df_z[['Altitude_std','Time_std']].plot.scatter(x='Altitude_std',y='Time_std')


'''fig, ax = bagpy.create_fig(1)
ax[0].scatter(x = 'Latitude_std', y = 'Longitude_std', data  = df_mov, s= 1, label = 'Latitude vs Longitude while walking')
ax[0].set(xlabel="Latitude_std",ylabel="Longitude_std")
'''

plt.show()



#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from bagpy  import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import math
import csv



A=bagreader('/home/srinidhi/EECE5554/LAB2/src/data/bag_files/idle_occluded.bag')
B=bagreader('/home/srinidhi/EECE5554/LAB2/src/data/bag_files/idle_open.bag')
C=bagreader('/home/srinidhi/EECE5554/LAB2/src/data/bag_files/moving_occluded.bag')
D=bagreader('/home/srinidhi/EECE5554/LAB2/src/data/bag_files/moving_open.bag')

A.topic_table
B.topic_table
C.topic_table
D.topic_table

x = A.message_by_topic('/gps')
y = B.message_by_topic('/gps')
z = C.message_by_topic('/gps')
k = D.message_by_topic('/gps')



df_x = pd.read_csv(x)
df_y = pd.read_csv(y)
df_z = pd.read_csv(z)
df_k = pd.read_csv(k)

# UTM_easting vs UTM_northing

df_x['UTM_northing_std(m)']= df_x['UTM_northing']- df_x['UTM_northing'].min()
df_x['UTM_easting_std(m)']= df_x['UTM_easting']- df_x['UTM_easting'].min()

df_y['UTM_northing_std(m)']= df_y['UTM_northing']- df_y['UTM_northing'].min()
df_y['UTM_easting_std(m)']= df_y['UTM_easting']- df_y['UTM_easting'].min()

df_z['UTM_northing_std(m)']= df_z['UTM_northing']- df_z['UTM_northing'].min()
df_z['UTM_easting_std(m)']= df_z['UTM_easting']- df_z['UTM_easting'].min()

df_k['UTM_northing_std(m)']= df_k['UTM_northing']- df_k['UTM_northing'].min()
df_k['UTM_easting_std(m)']= df_k['UTM_easting']- df_k['UTM_easting'].min()



ax=df_x[['UTM_northing_std(m)','UTM_easting_std(m)']].plot.scatter(x='UTM_easting_std(m)',y='UTM_northing_std(m)')
ax.set_title('Scatter plot of UTM coordinates(Easting vs Northing) for Idle Occluded data')

ay=df_y[['UTM_northing_std(m)','UTM_easting_std(m)']].plot.scatter(x='UTM_easting_std(m)',y='UTM_northing_std(m)')
ay.set_title('Scatter plot of UTM coordinates(Easting vs Northing) for Idle Open data')

az=df_z[['UTM_northing_std(m)','UTM_easting_std(m)']].plot.scatter(x='UTM_northing_std(m)',y='UTM_easting_std(m)')
az.set_title('Scatter plot of UTM coordinates(Easting vs Northing) for Moving Occluded data')

ak=df_k[['UTM_northing_std(m)','UTM_easting_std(m)']].plot.scatter(x='UTM_northing_std(m)',y='UTM_easting_std(m)')
ak.set_title('Scatter plot of UTM coordinates(Easting vs Northing) for Moving Open data')


#Fix Quality vs Time

df_x['Time(s)']= df_x['Time']- df_x['Time'].min()
df_x['Fix Quality']=df_x['Fix_quality']

ar=df_x[['Time(s)','Fix Quality']].plot.scatter(x='Time(s)',y='Fix Quality')
ar.set_title('Fix Quality vs Time for Idle Occluded data')

df_y['Time(s)']= df_y['Time']- df_y['Time'].min()
df_y['Fix Quality']=df_y['Fix_quality']

aq=df_y[['Time(s)','Fix Quality']].plot.scatter(x='Time(s)',y='Fix Quality')
aq.set_title('Fix Quality vs Time for Idle Open data')

df_z['Time(s)']= df_z['Time']- df_z['Time'].min()
df_z['Fix Quality']=df_z['Fix_quality']

ap=df_z[['Time(s)','Fix Quality']].plot.scatter(x='Time(s)',y='Fix Quality')
ap.set_title('Fix Quality vs Time for Moving Occluded data')

df_k['Time(s)']= df_k['Time']- df_k['Time'].min()
df_k['Fix Quality']=df_k['Fix_quality']
aw=df_k[['Time(s)','Fix Quality']].plot.scatter(x='Time(s)',y='Fix Quality')
aw.set_title('Fix Quality vs Time for Moving Occluded data')

# Error

df_y['UTM_easting_known']=328121.11
df_y['UTM_easting']=df_y['UTM_easting'] - df_y['UTM_easting'].min()
error_easting=df_y['UTM_easting']-df_y['UTM_easting_known']
#UTM_easting_known=328121.11
#UTM_northing_known=4689434.40
#error_easting= df_y['UTM_easting'] - UTM_easting_known
#error_northing = df_y['UTM_northing'] - UTM_easting_known
ba=df_y[['UTM_easting','UTM_easting_known']].plot.scatter(x='UTM_easting',y='UTM_easting_known')

df_y['UTM_northing_known']=4689434.40
df_y['UTM_northing']=df_y['UTM_northing'] - df_y['UTM_northing'].min()
error_northing=df_y['UTM_northing']-df_y['UTM_northing_known']
#bx=df_y[['UTM_northing','UTM_northing_known']].sns.displot(x='UTM_northing',y='UTM_northing_known')


#42.338389,-71.086419 - Columbus Garage
# UTM coordinates 328121.11m east and UTM-northing as 4689434.40m

'''fig, ax = bagpy.create_fig(1)
ax[0].scatter(x = 'Latitude_std', y = 'Longitude_std', data  = df_mov, s= 1, label = 'Latitude vs Longitude while walking')
ax[0].set(xlabel="Latitude_std(m)",ylabel="Longitude_std(m)")'''


plt.show()


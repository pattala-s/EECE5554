#!/usr/bin/env python

import bagpy
from bagpy import bagreader
import pandas as pd
from gps_driver.msg import gps_msg
import argparse

parser = argparse.ArgumentParser(description='Bag file name')

parser.add_argument('Bag_name', type=str , help='Required bag file name')

args = parser.parse_args()
try:
	b = bagreader(args.Bag_name)

	gps_msg = b.message_by_topic(topic='/gps')

except:
	print('Incorrect bag file name, path not found.')

